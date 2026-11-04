# UEFA Europa League — football model report

Fixtures in this report: **17**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Europa League |
| Training matches | 714 |
| Training data through | 2026-10-22 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 5 |
| Training seasons loaded | ['2022', '2023', '2024', '2025', '2026'] |
| Training sha256 | 2f4fd2fcddcb84697ea931176b022e41bf3522fece1debae7653f99b8c0db30f |
| Training as of utc | 2026-11-04T19:40:41.614358+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 793.678 |
| Base scoring parameter | 0.103 |
| Home-advantage parameter | 0.267 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 108, 'matches': 714, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-22'} |
| Training data health | {'training_end': '2026-10-22', 'verified_at_utc': '2026-11-04T12:05:52.166800+00:00', 'official_source_health': {'2025': {'status': 'REVIEWED_HISTORICAL_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 17.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 1.00 |
| Over 1 5 in window quote fixtures | 16 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 17.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 17.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 14, 'ANCHORED_MAIN': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 17} |
| Legacy comparison status | {'None': 17} |
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

## 2026-11-05 — AC Milan vs Ferencváros TC

The model's most likely 1X2 outcome is **AC Milan win** at **73.2%**. Expected goals are 2.92 for AC Milan and 1.00 for Ferencváros TC (3.92 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.3%; Under 3.5 goals: 59.9%; Double Chance 1X: 89.2%; Double Chance X2: 26.8%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 73.2% | 1.37 |
| Draw | 15.9% | 6.28 |
| Ferencváros TC win | 10.8% | 9.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 2.92 |
| Ferencváros TC expected goals | 1.00 |
| Expected total goals | 3.92 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.63% |
| 2 | 1-0 | 10.12% |
| 3 | 2-1 | 9.51% |
| 4 | 3-0 | 9.27% |
| 5 | 3-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 73.2% | 71.7% | 1.37 | +0.3% |
| Draw | 15.9% | 17.2% | 5.20 | -17.2% |
| Ferencváros TC win | 10.8% | 11.1% | 9.10 | -1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | cb7170b1b0e68a09be62b7a0fcb8d268 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | milan |
| Matched away-team name | ferencvaros |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9243 |
| Dc lambda away | 1.0000 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.53 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.79 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.50 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.07785789990291017, "-10": 1.7004571500697384e-09, "-11": 1.2466459847714253e-10, "-12": 8.396313241231366e-12, "-13": 5.229104575362318e-13, "-14": 3.0282234586363416e-14, "-15": 1.6386165369930956e-15, "-16": 8.318902608568831e-17, "-17": 3.958879395863318e-18, "-18": 1.6230893592279132e-19, "-2": 0.023610807409016003, "-3": 0.005602805790199985, "-4": 0.0010494270301697024, "-5": 0.00016164428522231198, "-6": 2.1093328446950735e-05, "-7": 2.384456549632042e-06, "-8": 2.37560659649482e-07, "-9": 2.1146157366270165e-08, "0": 0.15930675989099263, "1": 0.23295029983597149, "10": 8.220353960490835e-05, "11": 1.762399898362327e-05, "12": 3.471254372540092e-06, "13": 6.322103849889834e-07, "14": 1.070677579832791e-07, "15": 1.6942777730322594e-08, "16": 2.515415952101879e-09, "17": 3.5006809660266637e-10, "18": 4.197195350944446e-11, "2": 0.21337509990321687, "3": 0.14807268734895412, "4": 0.08110696053705695, "5": 0.0365344628499548, "6": 0.013941964653704932, "7": 0.004608979389469194, "8": 0.0013428464842481732, "9": 0.00034955844168816134} |
| Raw goal margin distribution | {"-1": 0.06959158578716249, "-10": 7.0799718514391955e-09, "-11": 6.299150953827772e-10, "-12": 5.154049296054377e-11, "-13": 3.902695168506958e-12, "-14": 2.7497327895877187e-13, "-15": 1.8112706988432125e-14, "-16": 1.120085057695175e-15, "-17": 6.52659994868459e-17, "-18": 3.593687056447905e-18, "-19": 1.8606088596309433e-19, "-2": 0.023802079829624942, "-20": 8.116124463676755e-21, "-3": 0.006530440224888968, "-4": 0.001439697196082349, "-5": 0.0002638153510165341, "-6": 4.123447047307844e-05, "-7": 5.608699343934975e-06, "-8": 6.745149265619885e-07, "-9": 7.264368924017525e-08, "0": 0.13053435414947556, "1": 0.19795472907148465, "10": 0.000323889179749806, "11": 8.427202221102735e-05, "12": 2.0164453603718045e-05, "13": 4.465180423225261e-06, "14": 9.200286774707215e-07, "15": 1.772273421547741e-07, "16": 3.205050357145862e-08, "17": 5.461442151481597e-09, "18": 8.794215242397083e-10, "19": 1.331522197973009e-10, "2": 0.20355786593842654, "20": 1.6985507043275445e-11, "3": 0.16332472332914313, "4": 0.10529727260267857, "5": 0.05642642260793233, "6": 0.02579166427126275, "7": 0.01025929684996585, "8": 0.00360814092506839, "9": 0.0011363871382173507} |
| Unadjusted home-win probability | 76.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 10.2% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 59.5% |
| Home training matches | 9 |
| Away training matches | 33 |
| P home draw | 89.2% |
| P draw away | 26.8% |
| P home away | 84.1% |
| Raw p home draw | 89.8% |
| Raw p draw away | 23.2% |
| Raw p home away | 86.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8183 |
| Totals anchor target over 2 5 | 0.6233 |
| Totals anchor reference over odds | 1.50 |
| Totals anchor reference under odds | 2.31 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7393 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.72, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 5.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.29, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.1, "draw": 5.2, "home": 1.37}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.24, "home_away": 1.18, "home_draw": 1.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.01, "home_away": 1.16, "home_draw": 1.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.92, "draw": 4.72, "home": 1.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.5, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.14, "under": 4.47}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.34 |
| Reference draw odds | 4.72 |
| Reference away odds | 6.92 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:40Z |
| Home probability edge | +1.5% |
| Draw probability edge | -1.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0506 |
| Raw ev home | 0.0519 |
| Raw edge prob draw | -0.0411 |
| Raw ev draw | -0.3212 |
| Raw edge prob away | -0.0095 |
| Raw ev away | -0.0748 |
| Market p home draw | 89.4% |
| Market home draw odds | 1.08 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.4% |
| Market draw away odds | 3.24 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.1% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.08 |
| Market reference dc draw away odds | 3.28 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 84.8% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.47 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,446.6112 |
| Elo away rating | 1,471.6144 |
| Elo rating diff | 34.9969 |
| Elo home expectancy | 0.5502 |

</details>


---

## 2026-11-05 — AZ Alkmaar vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **53.4%**. Expected goals are 0.79 for AZ Alkmaar and 2.01 for Juventus (2.80 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 53.2%; Under 3.5 goals: 68.1%; Double Chance 1X: 46.6%; Double Chance X2: 77.2%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AZ Alkmaar win | 22.8% | 4.38 |
| Draw | 23.8% | 4.21 |
| Juventus win | 53.4% | 1.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AZ Alkmaar expected goals | 0.79 |
| Juventus expected goals | 2.01 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 31.9% |
| Under 3.5 | 68.1% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 0-2 | 9.33% |
| 3 | 0-1 | 9.21% |
| 4 | 1-0 | 7.86% |
| 5 | 1-2 | 7.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AZ Alkmaar win | 22.8% | 26.5% | 3.64 | -17.0% |
| Draw | 23.8% | 25.6% | 3.78 | -10.2% |
| Juventus win | 53.4% | 47.9% | 2.03 | +8.5% |
| Over 2.5 | 53.2% | 53.1% | 1.83 | -2.6% |
| Under 2.5 | 46.8% | 46.9% | 2.06 | -3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | c91f4c9744f6ca502b7986a564e858df |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | az alkmaar |
| Matched away-team name | juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7901 |
| Dc lambda away | 2.0096 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.20 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.30 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.14 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.30 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.19577665004335762, "-10": 2.375449526658427e-05, "-11": 4.499446928941746e-06, "-12": 7.827859166209495e-07, "-13": 1.2590492257043873e-07, "-14": 1.8827820740392605e-08, "-15": 2.630079754491536e-09, "-16": 3.4323140631275917e-10, "-17": 3.8637500209513624e-11, "-2": 0.16126522423412468, "-3": 0.09999147096576451, "-4": 0.04872663408941979, "-5": 0.019478230777467007, "-6": 0.006586205869080293, "-7": 0.001927237925216471, "-8": 0.0004966699001230226, "-9": 0.00011430110606176377, "0": 0.2375211864492284, "1": 0.1618938162419105, "10": 4.287470078618032e-09, "11": 3.1930897623925686e-10, "12": 2.1841964438493427e-11, "13": 1.3813002834556494e-12, "14": 8.121610244201529e-14, "15": 4.460748168570358e-15, "16": 2.2888772673686436e-16, "17": 1.0130740826956248e-17, "2": 0.050959180130589345, "3": 0.012423425589759146, "4": 0.0023803538234219443, "5": 0.00037412894546381975, "6": 4.973977345179331e-05, "7": 5.7226941170040285e-06, "8": 5.798687963602054e-07, "9": 5.246975419836376e-08} |
| Raw goal margin distribution | {"-1": 0.25347731424131736, "-10": 2.07847407955567e-05, "-11": 3.7524998660178027e-06, "-12": 6.221414001821834e-07, "-13": 9.5347961855517e-08, "-14": 1.358445096996448e-08, "-15": 1.8078416960154674e-09, "-16": 2.249110732004944e-10, "-17": 2.4315954019440063e-11, "-2": 0.20219418980763407, "-3": 0.1206053090770404, "-4": 0.05633666402710831, "-5": 0.02154306543824492, "-6": 0.006959492205203525, "-7": 0.0019440207964871328, "-8": 0.0004779777609519523, "-9": 0.0001049025166227815, "0": 0.19357132562757115, "1": 0.10259383245277122, "10": 1.8353191564992182e-09, "11": 1.3028198553711687e-10, "12": 8.492772372734064e-12, "13": 5.117625413227249e-13, "14": 2.8667899241835426e-14, "15": 1.5000677559744944e-15, "16": 7.337667253639923e-17, "17": 3.119142295044961e-18, "2": 0.031258063467205534, "3": 0.007330886935668524, "4": 0.001346411835528758, "5": 0.00020243751291346593, "6": 2.5713295668277787e-05, "7": 2.824085207155894e-06, "8": 2.7301171200983617e-07, "9": 2.3558964265977763e-08} |
| Unadjusted home-win probability | 14.3% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 66.4% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 46.8% |
| Home training matches | 15 |
| Away training matches | 11 |
| P home draw | 46.6% |
| P draw away | 77.2% |
| P home away | 76.2% |
| Raw p home draw | 33.6% |
| Raw p draw away | 85.7% |
| Raw p home away | 80.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0504 |
| Totals anchor target over 2 5 | 0.5322 |
| Totals anchor reference over odds | 1.80 |
| Totals anchor reference under odds | 2.03 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5027 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.81, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.03, "draw": 3.78, "home": 3.64}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.31, "home_away": 1.29, "home_draw": 1.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.31, "home_away": 1.3, "home_draw": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.02, "draw": 3.67, "home": 3.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.8, "under": 2.03}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.25, "under": 3.92}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.56 |
| Reference draw odds | 3.67 |
| Reference away odds | 2.02 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -3.7% |
| Draw probability edge | -1.9% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.1219 |
| Raw ev home | -0.4804 |
| Raw edge prob draw | -0.0628 |
| Raw ev draw | -0.2683 |
| Raw edge prob away | 0.1847 |
| Raw ev away | 0.3472 |
| Market p home draw | 52.5% |
| Market home draw odds | 1.84 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:14Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T19:40:14Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.84 |
| Market reference dc draw away odds | 1.32 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 78.1% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.92 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.3% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.03 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,483.3792 |
| Elo away rating | 1,491.7497 |
| Elo rating diff | 51.6295 |
| Elo home expectancy | 0.5738 |

</details>


---

## 2026-11-05 — Anderlecht vs Salzburg

The model's most likely 1X2 outcome is **Anderlecht win** at **49.9%**. Expected goals are 1.85 for Anderlecht and 1.24 for Salzburg (3.09 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 59.9%; Under 3.5 goals: 61.8%; Double Chance 1X: 73.8%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 79.6%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Anderlecht win | 49.9% | 2.00 |
| Draw | 23.9% | 4.19 |
| Salzburg win | 26.2% | 3.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Anderlecht expected goals | 1.85 |
| Salzburg expected goals | 1.24 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 59.9% |
| Under 2.5 | 40.1% |
| Over 3.5 | 38.2% |
| Under 3.5 | 61.8% |
| Over 4.5 | 20.4% |
| Under 4.5 | 79.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.83% |
| 2 | 2-1 | 9.20% |
| 3 | 1-0 | 8.28% |
| 4 | 2-0 | 7.30% |
| 5 | 2-2 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Anderlecht win | 49.9% | 49.0% | 1.99 | -0.6% |
| Draw | 23.9% | 24.8% | 3.90 | -6.9% |
| Salzburg win | 26.2% | 26.2% | 3.67 | -3.9% |
| Over 2.5 | 59.9% | 59.5% | 1.64 | -1.8% |
| Under 2.5 | 40.1% | 40.5% | 2.37 | -4.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | 9604c5b1c465435911e038db95ab2a7b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | anderlecht |
| Matched away-team name | salzburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8461 |
| Dc lambda away | 1.2403 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.49 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.62 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.91 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.15602465263683896, "-10": 1.4937920813968075e-07, "-11": 1.6809108866617662e-08, "-12": 1.7384248828475355e-09, "-13": 1.663039213221781e-10, "-14": 1.4791165307750827e-11, "-15": 1.219274260699018e-12, "-16": 8.364285011964373e-14, "-2": 0.07121616933580224, "-3": 0.025398136941814874, "-4": 0.007206186701352092, "-5": 0.0016892387056247336, "-6": 0.000336455079874811, "-7": 5.816626644303866e-05, "-8": 8.874562048848072e-06, "-9": 1.2109358700820068e-06, "0": 0.23871785884120875, "1": 0.21898995330418122, "10": 7.598132258301892e-06, "11": 1.2725627281088139e-06, "12": 1.9588818931798555e-07, "13": 2.7891548417976154e-08, "14": 3.6922435403373786e-09, "15": 4.530093516997303e-10, "16": 4.625433034185328e-11, "2": 0.1504017191783361, "3": 0.07983509833458959, "4": 0.03371439160821544, "5": 0.011763015091726186, "6": 0.003487165290081714, "7": 0.0008972933413482683, "8": 0.0002037642545284747, "9": 4.13828147433256e-05} |
| Raw goal margin distribution | {"-1": 0.15676779075863528, "-10": 1.332730997390628e-07, "-11": 1.4774503879781334e-08, "-12": 1.505242963781806e-09, "-13": 1.418436560252096e-10, "-14": 1.242684271673954e-11, "-15": 1.0094623199351545e-12, "-16": 6.845584732237336e-14, "-2": 0.0708997026132991, "-3": 0.02500187281313058, "-4": 0.007004741760109679, "-5": 0.0016201042881942918, "-6": 0.00031821589682160125, "-7": 5.4232542533406e-05, "-8": 8.155033444510987e-06, "-9": 1.0965154751188613e-06, "0": 0.21725018545374114, "1": 0.2307787479991363, "10": 7.1108354725925255e-06, "11": 1.1732994062343762e-06, "12": 1.7791819477026342e-07, "13": 2.4954075655411374e-08, "14": 3.2539448316154302e-09, "15": 3.934207932775114e-10, "16": 3.9709604401645064e-11, "2": 0.15706522465087128, "3": 0.08243772172112572, "4": 0.034376636471558523, "5": 0.011834012868702058, "6": 0.0034596227978471363, "7": 0.0008775758380523923, "8": 0.00019641210564213363, "9": 3.930746926026342e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 62.8% |
| Raw p btts yes | 59.3% |
| Home training matches | 13 |
| Away training matches | 13 |
| P home draw | 73.8% |
| P draw away | 50.1% |
| P home away | 76.1% |
| Raw p home draw | 73.8% |
| Raw p draw away | 47.9% |
| Raw p home away | 78.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0156 |
| Totals anchor target over 2 5 | 0.5987 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.36 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5889 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.67, "draw": 3.9, "home": 1.99}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.37}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.87, "home_away": 1.28, "home_draw": 1.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.87, "home_away": 1.28, "home_draw": 1.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.64, "draw": 3.84, "home": 1.99}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.36}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.99 |
| Reference draw odds | 3.84 |
| Reference away odds | 3.64 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.37 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0310 |
| Raw ev home | 0.0369 |
| Raw edge prob draw | -0.0307 |
| Raw ev draw | -0.1527 |
| Raw edge prob away | -0.0004 |
| Raw ev away | -0.0396 |
| Market p home draw | 73.4% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.4% |
| Market draw away odds | 1.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.31 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.86 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,445.9180 |
| Elo away rating | 1,427.7213 |
| Elo rating diff | 78.1968 |
| Elo home expectancy | 0.6107 |

</details>


---

## 2026-11-05 — Bayer Leverkusen vs Marseille

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **75.4%**. Expected goals are 2.87 for Bayer Leverkusen and 0.55 for Marseille (3.42 combined). The most likely exact score is 3-0 at 10.6%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.4%; Under 3.5 goals: 51.6%; Double Chance 1X: 90.0%; Double Chance X2: 24.6%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 75.4% | 1.33 |
| Draw | 14.6% | 6.85 |
| Marseille win | 10.0% | 9.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.87 |
| Marseille expected goals | 0.55 |
| Expected total goals | 3.42 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 68.4% |
| Under 2.5 | 31.6% |
| Over 3.5 | 48.4% |
| Under 3.5 | 51.6% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.59% |
| 2 | 2-0 | 10.08% |
| 3 | 4-0 | 8.35% |
| 4 | 1-1 | 6.88% |
| 5 | 1-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 75.4% | 71.4% | 1.41 | +6.3% |
| Draw | 14.6% | 16.4% | 5.64 | -17.7% |
| Marseille win | 10.0% | 12.2% | 7.48 | -25.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | e1c3625feeebcd65317e17a4e9a38c4f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:40:40Z |
| Market best away last update utc | 2026-11-04T19:40:40Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | leverkusen |
| Matched away-team name | marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8659 |
| Dc lambda away | 0.5522 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.24 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.30 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.07 |
| Fair Under 3.5 odds | 1.94 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Goal margin distribution | {"-1": 0.07897323644538617, "-10": 1.1751644562564887e-10, "-11": 6.396426304799582e-12, "-12": 3.198331561378018e-13, "-13": 1.478721347676858e-14, "-14": 6.357083485358706e-16, "-15": 2.5535826862006143e-17, "-16": 9.62526139367704e-19, "-17": 3.4172617628260953e-20, "-18": 1.1464259760695777e-21, "-19": 3.6317166033080765e-23, "-2": 0.017564595517650897, "-20": 1.0064622471007521e-24, "-3": 0.0031018671215793108, "-4": 0.0004319851608878139, "-5": 4.9447962880393896e-05, "-6": 4.7936071163675896e-06, "-7": 4.024777231594009e-07, "-8": 2.977808555506928e-08, "-9": 1.968233031229836e-09, "0": 0.14591565579115218, "1": 0.15010359937217888, "10": 0.000643092546362422, "11": 0.00018166038969444728, "12": 4.7140516533303935e-05, "13": 1.1311109536601693e-05, "14": 2.5236248350476183e-06, "15": 5.260957762881238e-07, "16": 1.0291423137556186e-07, "17": 1.896221915996783e-08, "18": 3.301451675879665e-09, "19": 5.427738185747853e-10, "2": 0.18265387216986878, "20": 7.806429472541082e-11, "3": 0.1674024971322519, "4": 0.12099170129338545, "5": 0.07187587946618025, "6": 0.03616139832447597, "7": 0.015756967498971274, "8": 0.0060502814432454284, "9": 0.002075407263020657} |
| Raw goal margin distribution | {"-1": 0.03933023876917549, "-10": 2.748119846248904e-11, "-11": 1.3634362595680676e-12, "-12": 6.211891346355896e-14, "-13": 2.616163028895193e-15, "-14": 1.02426868249359e-16, "-15": 3.746288453172008e-18, "-16": 1.2855538791352943e-19, "-17": 4.154221617915952e-21, "-18": 1.2648040238601827e-22, "-19": 3.393430149187945e-24, "-2": 0.008213671592838001, "-3": 0.0013467533694669512, "-4": 0.0001729080244389397, "-5": 1.8172101445690252e-05, "-6": 1.6133593961235389e-06, "-7": 1.2385078899519898e-07, "-8": 8.368388999579783e-09, "-9": 5.04720146933341e-10, "0": 0.1039653287780721, "1": 0.193249145573133, "10": 0.00038950747033765346, "11": 0.00010029123394431717, "12": 2.37137369609651e-05, "13": 5.183092550417487e-06, "14": 1.0531398979194256e-06, "15": 1.9990396032048993e-07, "16": 3.560069527953651e-08, "17": 5.970433567121453e-09, "18": 9.433817269035027e-10, "19": 1.3135637278816173e-10, "2": 0.22122456970718007, "3": 0.18824875284128764, "4": 0.12543166810308784, "5": 0.06841403634754595, "6": 0.03152239425147646, "7": 0.012558415959261396, "8": 0.004403783482821987, "9": 0.0013784237630462383} |
| Unadjusted home-win probability | 84.7% |
| Unadjusted draw probability | 10.4% |
| Unadjusted away-win probability | 4.9% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 55.4% |
| Raw p btts yes | 39.8% |
| Home training matches | 24 |
| Away training matches | 17 |
| P home draw | 90.0% |
| P draw away | 24.6% |
| P home away | 85.4% |
| Raw p home draw | 95.1% |
| Raw p draw away | 15.3% |
| Raw p home away | 89.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0997 |
| Totals anchor target over 2 5 | 0.6837 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.89 |
| Totals anchor reference last update utc | 2026-11-04T19:40:40Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6303 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.11, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.4, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.4, "draw": 5.35, "home": 1.41}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.06, "home_away": 1.18, "home_draw": 1.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.26, "home_away": 1.17, "home_draw": 1.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.48, "draw": 5.64, "home": 1.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.42, "under": 2.89}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.13, "under": 6.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.38 |
| Reference draw odds | 5.64 |
| Reference away odds | 7.48 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:40Z |
| Market reference home last update utc | 2026-11-04T19:40:40Z |
| Market reference draw last update utc | 2026-11-04T19:40:40Z |
| Market reference away last update utc | 2026-11-04T19:40:40Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.89 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:56Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:56Z |
| Home probability edge | +4.0% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1328 |
| Raw ev home | 0.1942 |
| Raw edge prob draw | -0.0599 |
| Raw ev draw | -0.4136 |
| Raw edge prob away | -0.0729 |
| Raw ev away | -0.6329 |
| Market p home draw | 86.8% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:15Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.5% |
| Market draw away odds | 3.26 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:15Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.7% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 3.06 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 87.1% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.19 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:40Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.1% |
| Market under 3 5 odds | 1.79 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 3 5 odds | 1.79 |
| Market reference under 3 5 opposite odds | 2.09 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:40Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,523.2260 |
| Elo away rating | 1,423.2467 |
| Elo rating diff | 159.9793 |
| Elo home expectancy | 0.7152 |

</details>


---

## 2026-11-05 — Benfica vs Lech Poznań

The model's most likely 1X2 outcome is **Benfica win** at **89.1%**. Expected goals are 5.16 for Benfica and 0.20 for Lech Poznań (5.35 combined). The most likely exact score is 4-0 at 15.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 74.9%; Under 3.5 goals: 42.0%; Double Chance 1X: 96.7%; Double Chance X2: 10.9%; Double Chance 12 (either team wins): 92.4%; Under 4.5 goals: 60.0%; BTTS Yes (both teams score): 16.2%; BTTS No (at least one team does not score): 83.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 89.1% | 1.12 |
| Draw | 7.6% | 13.22 |
| Lech Poznań win | 3.3% | 29.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 5.16 |
| Lech Poznań expected goals | 0.20 |
| Expected total goals | 5.35 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 88.3% |
| Under 1.5 | 11.7% |
| Over 2.5 | 74.9% |
| Under 2.5 | 25.1% |
| Over 3.5 | 58.0% |
| Under 3.5 | 42.0% |
| Over 4.5 | 40.0% |
| Under 4.5 | 60.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-0 | 15.20% |
| 2 | 3-0 | 14.56% |
| 3 | 5-0 | 12.69% |
| 4 | 2-0 | 10.46% |
| 5 | 6-0 | 8.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Benfica win | 89.1% | 84.9% | 1.17 | +4.2% |
| Draw | 7.6% | 10.4% | 8.20 | -38.0% |
| Lech Poznań win | 3.3% | 4.7% | 17.00 | -43.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | bc4a4cc34a2219d9564b7b0c17ba2934 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | benfica |
| Matched away-team name | lech poznan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.1568 |
| Dc lambda away | 0.1954 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 16.2% |
| P btts no | 83.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.40 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.52 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.98 |
| Fair Over 3.5 odds | 1.72 |
| Fair Under 3.5 odds | 2.38 |
| Fair Over 4.5 odds | 2.50 |
| Fair Under 4.5 odds | 1.67 |
| Goal margin distribution | {"-1": 0.031415507325906505, "-10": 3.614935248292447e-16, "-11": 5.172897974582221e-18, "-12": 6.790614161976056e-20, "-13": 8.233453973745248e-22, "-14": 9.274246749265272e-24, "-15": 9.753969814316398e-26, "-16": 9.620443161856448e-28, "-17": 8.932977928144739e-30, "-18": 7.83559512349657e-32, "-19": 6.512535023770135e-34, "-2": 0.0019519756086624413, "-20": 5.143080416312795e-36, "-21": 3.8687212561729623e-38, "-22": 2.777135229115376e-40, "-23": 1.8567677235096808e-42, "-3": 9.771872882082456e-05, "-4": 3.7435715837117054e-06, "-5": 1.1592735404175362e-07, "-6": 3.009679881148793e-09, "-7": 6.7229550802231e-11, "-8": 1.3173997639992643e-12, "-9": 2.298809230281697e-14, "0": 0.07565613820359204, "1": 0.06897380577675437, "10": 0.0056546873810133695, "11": 0.002135772502424529, "12": 0.0007400194477458521, "13": 0.0002368258696673657, "14": 7.04107103213799e-05, "15": 1.9545846634514042e-05, "16": 5.0883989935319506e-06, "17": 1.2470829489769685e-06, "18": 2.887247859468434e-07, "19": 6.333957618013666e-08, "2": 0.12962192318886315, "20": 1.3202658698957792e-08, "21": 2.6213108290483557e-09, "22": 4.966622024618568e-10, "23": 8.764651672655847e-11, "3": 0.17127535778713854, "4": 0.17318736996836503, "5": 0.14155623364997355, "6": 0.09700103785613627, "7": 0.05719121009307016, "8": 0.029580101369822656, "9": 0.013623792153316645} |
| Raw goal margin distribution | {"-1": 0.001715819556942493, "-10": 1.1591077251900507e-16, "-11": 2.0432358083640546e-18, "-12": 3.305409728194852e-20, "-13": 4.940426103577349e-22, "-14": 6.86175181881307e-24, "-15": 8.90019878449824e-26, "-16": 1.0827991202950156e-27, "-17": 1.2403498302924195e-29, "-18": 1.342351169072605e-31, "-19": 1.3766830457991342e-33, "-2": 0.00012488326396703332, "-20": 1.3416347232220486e-35, "-21": 1.2454876541908321e-37, "-22": 1.1038830307743005e-39, "-23": 9.359942250735421e-42, "-24": 7.606747076564385e-44, "-25": 5.931358387733722e-46, "-26": 4.29079935725874e-48, "-3": 7.530188967213529e-06, "-4": 3.506970123341177e-07, "-5": 1.3268141139540838e-08, "-6": 4.2209465677941345e-10, "-7": 1.1575537362948536e-11, "-8": 2.7883706618068167e-13, "-9": 5.986668293112633e-15, "0": 0.010379498212315768, "1": 0.039227316690633805, "10": 0.01902189606652714, "11": 0.008850371393481288, "12": 0.003779038407912071, "13": 0.0014908481579111784, "14": 0.0005465337824862945, "15": 0.00018710901511993216, "16": 6.008359372283063e-05, "17": 1.8166246317644045e-05, "18": 5.189196933132815e-06, "19": 1.404691556067573e-06, "2": 0.0870022014355936, "20": 3.613219106005356e-07, "21": 8.853447892840231e-08, "22": 2.071138140131896e-08, "23": 4.63523949841947e-09, "24": 9.94285225468298e-10, "25": 2.0463465151747985e-10, "26": 3.907295143360334e-11, "3": 0.13846655142222059, "4": 0.170209606498295, "5": 0.16997109987370174, "6": 0.14272099243722422, "7": 0.10330757422851465, "8": 0.06568323100331862, "9": 0.037222213796225805} |
| Unadjusted home-win probability | 98.8% |
| Unadjusted draw probability | 1.0% |
| Unadjusted away-win probability | 0.2% |
| Raw p over 1 5 | 97.0% |
| Raw p under 3 5 | 21.9% |
| Raw p btts yes | 17.6% |
| Home training matches | 9 |
| Away training matches | 3 |
| P home draw | 96.7% |
| P draw away | 10.9% |
| P home away | 92.4% |
| Raw p home draw | 99.8% |
| Raw p draw away | 1.2% |
| Raw p home away | 99.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8097 |
| Totals anchor target over 2 5 | 0.7488 |
| Totals anchor reference over odds | 1.30 |
| Totals anchor reference under odds | 3.50 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8324 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 13.96, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.04, "price": 13.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.86, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.0, "draw": 8.2, "home": 1.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 5.5, "home_away": 1.1, "home_draw": 1.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 16.1, "draw": 7.85, "home": 1.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.3, "under": 3.5}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 7.85 |
| Reference away odds | 16.10 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.50 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:17Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:17Z |
| Home probability edge | +4.2% |
| Draw probability edge | -2.8% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1384 |
| Raw ev home | 0.1557 |
| Raw edge prob draw | -0.0933 |
| Raw ev draw | -0.9149 |
| Raw edge prob away | -0.0452 |
| Raw ev away | -0.9686 |
| Market p home draw | 94.5% |
| Market home draw odds | 1.04 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:14Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 17.2% |
| Market draw away odds | 5.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:14Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.3% |
| Market home away odds | 1.10 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T19:40:14Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 5.55 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 91.3% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:17Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.2% |
| Market under 3 5 odds | 2.09 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 2.09 |
| Market reference under 3 5 opposite odds | 1.75 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,490.8432 |
| Elo away rating | 1,407.9321 |
| Elo rating diff | 142.9112 |
| Elo home expectancy | 0.6948 |

</details>


---

## 2026-11-05 — Celta Vigo vs Union Saint-Gilloise

The model's most likely 1X2 outcome is **Celta Vigo win** at **38.6%**. Expected goals are 1.05 for Celta Vigo and 1.34 for Union Saint-Gilloise (2.39 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.1%; Double Chance 1X: 65.1%; Double Chance X2: 61.4%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 38.6% | 2.59 |
| Draw | 26.5% | 3.77 |
| Union Saint-Gilloise win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.05 |
| Union Saint-Gilloise expected goals | 1.34 |
| Expected total goals | 2.39 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.46% |
| 2 | 1-0 | 10.05% |
| 3 | 2-1 | 9.15% |
| 4 | 0-1 | 7.58% |
| 5 | 1-2 | 7.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 38.6% | 42.3% | 2.28 | -12.1% |
| Draw | 26.5% | 26.7% | 3.67 | -2.7% |
| Union Saint-Gilloise win | 34.9% | 31.0% | 3.12 | +8.9% |
| Over 2.5 | 52.5% | 52.5% | 1.84 | -3.5% |
| Under 2.5 | 47.5% | 47.5% | 2.12 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | b828d43ba5fa1c8cdd2e34aabea9d0ce |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | celta |
| Matched away-team name | union sg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0487 |
| Dc lambda away | 1.3407 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.23 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.64 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.17306050087564512, "-10": 1.485063899514969e-06, "-11": 2.109235023395082e-07, "-12": 2.7521460275733527e-08, "-13": 3.319543067348606e-09, "-14": 3.6982384827046094e-10, "-15": 3.455672434763796e-11, "-2": 0.1040298191738548, "-3": 0.047804677599615895, "-4": 0.017342233320936002, "-5": 0.005174184668830383, "-6": 0.0013079195375045477, "-7": 0.00028641555394750585, "-8": 5.527957932603613e-05, "-9": 9.532639030379436e-06, "0": 0.26521462418070296, "1": 0.22741309531492565, "10": 2.1245724096908429e-07, "11": 2.3603884455597374e-08, "12": 2.4091402812729638e-09, "13": 2.2730083577799545e-10, "14": 1.9808415999000443e-11, "15": 1.4478364732993877e-12, "2": 0.10617624529089861, "3": 0.03816559372735389, "4": 0.010830257032593653, "5": 0.0025275966627628776, "6": 0.0004997801295703059, "7": 8.561042765239406e-05, "8": 1.2924891518169377e-05, "9": 1.7434417221058546e-06} |
| Raw goal margin distribution | {"-1": 0.23857414913277014, "-10": 5.383445474063501e-07, "-11": 6.492871482857728e-08, "-12": 7.188771370176649e-09, "-13": 7.32625097091653e-10, "-14": 6.375627732272937e-11, "-2": 0.12847853036795434, "-3": 0.05173707996503975, "-4": 0.016248300880653033, "-5": 0.0041676738408731595, "-6": 0.0009018037585970487, "-7": 0.00016856883096032165, "-8": 2.7717015540254487e-05, "-9": 4.066184579876347e-06, "0": 0.2607482456551238, "1": 0.18802248215799688, "10": 4.6172289974201174e-08, "11": 4.356021474510006e-09, "12": 3.7725932781190355e-10, "13": 3.007455544914773e-11, "14": 2.0472575676085743e-12, "2": 0.07861307410067936, "3": 0.024762714030384193, "4": 0.006083260170897283, "5": 0.0012205463377403922, "6": 0.00020658781320682677, "7": 3.0206613728815597e-05, "8": 3.885110200166212e-06, "9": 4.4583696668694947e-07} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 47.3% |
| Home training matches | 17 |
| Away training matches | 29 |
| P home draw | 65.1% |
| P draw away | 61.4% |
| P home away | 73.5% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.1% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1824 |
| Totals anchor target over 2 5 | 0.5247 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-04T19:40:40Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4234 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.12, "draw": 3.67, "home": 2.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.79, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.67, "home_away": 1.31, "home_draw": 1.4}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.65, "home_away": 1.31, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.07, "draw": 3.54, "home": 2.28}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:40Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.24, "under": 3.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.28 |
| Reference draw odds | 3.54 |
| Reference away odds | 3.07 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:40Z |
| Market reference home last update utc | 2026-11-04T19:40:40Z |
| Market reference draw last update utc | 2026-11-04T19:40:40Z |
| Market reference away last update utc | 2026-11-04T19:40:40Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -3.7% |
| Draw probability edge | -0.2% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.1240 |
| Raw ev home | -0.3184 |
| Raw edge prob draw | -0.0064 |
| Raw ev draw | -0.0431 |
| Raw edge prob away | 0.1303 |
| Raw ev away | 0.3738 |
| Market p home draw | 69.1% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.5% |
| Market draw away odds | 1.67 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 78.4% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.88 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:40Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.5% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.93 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:40Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,446.1006 |
| Elo away rating | 1,494.2964 |
| Elo rating diff | 11.8042 |
| Elo home expectancy | 0.5170 |

</details>


---

## 2026-11-05 — Celtic vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **46.2%**. Expected goals are 2.00 for Celtic and 2.43 for Besiktas JK (4.43 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.3%; Under 3.5 goals: 58.8%; Double Chance 1X: 53.8%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 76.9%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celtic win | 31.7% | 3.16 |
| Draw | 22.2% | 4.51 |
| Besiktas JK win | 46.2% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celtic expected goals | 2.00 |
| Besiktas JK expected goals | 2.43 |
| Expected total goals | 4.43 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 63.3% |
| Under 2.5 | 36.7% |
| Over 3.5 | 41.2% |
| Under 3.5 | 58.8% |
| Over 4.5 | 23.1% |
| Under 4.5 | 76.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.71% |
| 2 | 1-2 | 9.11% |
| 3 | 0-1 | 7.41% |
| 4 | 2-1 | 7.27% |
| 5 | 2-2 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 31.7% | 31.2% | 3.10 | -1.8% |
| Draw | 22.2% | 23.7% | 3.97 | -12.0% |
| Besiktas JK win | 46.2% | 45.2% | 2.23 | +3.0% |
| Over 2.5 | 63.3% | 58.4% | 1.67 | +5.7% |
| Under 2.5 | 36.7% | 41.6% | 2.31 | -15.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | 5ecf6578ba030a1e99abaa3200319e37 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:40:39Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | celtic |
| Matched away-team name | besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0014 |
| Dc lambda away | 2.4329 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.78 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.97 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.72 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.33 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.21537327370061216, "-10": 4.593905486110214e-06, "-11": 7.339322857938205e-07, "-12": 1.0779932663155915e-07, "-13": 1.4649079877796621e-08, "-14": 1.850852893187413e-09, "-15": 2.163683518041855e-10, "-16": 2.0798944019387032e-11, "-2": 0.13772552562661558, "-3": 0.06877299632493948, "-4": 0.02746092702652658, "-5": 0.009087100763148098, "-6": 0.0025599781070317555, "-7": 0.0006267963659752402, "-8": 0.0001355653173497755, "-9": 2.6239740170441655e-05, "0": 0.221603152676518, "1": 0.17265997122841537, "10": 6.322611082592142e-07, "11": 8.309667247544233e-08, "12": 1.0040536437266824e-08, "13": 1.122443382080948e-09, "14": 1.1666463504618106e-10, "15": 1.1219520322237654e-11, "16": 8.872276477199318e-13, "2": 0.09036973865411882, "3": 0.03712271764287142, "4": 0.012194113640098146, "5": 0.003319507206379227, "6": 0.0007693035762046386, "7": 0.00015495343140084215, "8": 2.7569986362545443e-05, "9": 4.389961531149053e-06} |
| Raw goal margin distribution | {"-1": 0.18884628185328436, "-10": 3.668837003081464e-05, "-11": 7.834008505921221e-06, "-12": 1.5413934428318544e-06, "-13": 2.811117227493744e-07, "-14": 4.776471946887386e-08, "-15": 7.594284589684659e-09, "-16": 1.131972072308705e-09, "-17": 1.5531712736250093e-10, "-18": 1.6523100690640078e-11, "-2": 0.14067419927009428, "-3": 0.08547380435776403, "-4": 0.042881944926143216, "-5": 0.01819775950849705, "-6": 0.006664585146784712, "-7": 0.002141375893520156, "-8": 0.0006118793963940785, "-9": 0.00015724572243467055, "0": 0.18638343645678604, "1": 0.15586596319563448, "10": 5.207876758186978e-06, "11": 9.148071441199437e-07, "12": 1.4807176187546889e-07, "13": 2.221523550562552e-08, "14": 3.1052203553843435e-09, "15": 4.0614890717212534e-10, "16": 4.980206621015418e-11, "17": 5.621396601197889e-12, "18": 4.919598435343111e-13, "2": 0.09520086796119359, "3": 0.04758528980850655, "4": 0.019639362529766828, "5": 0.006856209218484858, "6": 0.0020656297950130942, "7": 0.0005459910274846454, "8": 0.00012834284263987995, "9": 2.71330048703351e-05} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 48.6% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.3% |
| Raw p btts yes | 78.6% |
| Home training matches | 13 |
| Away training matches | 11 |
| P home draw | 53.8% |
| P draw away | 68.3% |
| P home away | 77.8% |
| Raw p home draw | 51.4% |
| Raw p draw away | 67.2% |
| Raw p home away | 81.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7366 |
| Totals anchor target over 2 5 | 0.6330 |
| Totals anchor reference over odds | 1.53 |
| Totals anchor reference under odds | 2.54 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8119 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.76, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.23, "draw": 3.83, "home": 3.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.4, "home_away": 1.29, "home_draw": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:16Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.39, "home_away": 1.27, "home_draw": 1.73}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.14, "draw": 3.97, "home": 3.05}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.53, "under": 2.54}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.16, "under": 5.32}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.97 |
| Reference away odds | 2.14 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | +0.5% |
| Draw probability edge | -1.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | 0.0161 |
| Raw ev home | 0.0166 |
| Raw edge prob draw | -0.0503 |
| Raw ev draw | -0.2601 |
| Raw edge prob away | 0.0342 |
| Raw ev away | 0.0831 |
| Market p home draw | 56.6% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:16Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.8% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.6% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.70 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 84.7% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.32 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.6% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,392.0962 |
| Elo away rating | 1,450.5156 |
| Elo rating diff | 1.5806 |
| Elo home expectancy | 0.5023 |

</details>


---

## 2026-11-05 — Crystal Palace vs TSG Hoffenheim

The model's most likely 1X2 outcome is **Crystal Palace win** at **54.4%**. Expected goals are 2.71 for Crystal Palace and 1.47 for TSG Hoffenheim (4.18 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 63.2%; Under 3.5 goals: 58.5%; Double Chance 1X: 76.0%; Double Chance X2: 45.6%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 54.4% | 1.84 |
| Draw | 21.6% | 4.62 |
| TSG Hoffenheim win | 24.0% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 2.71 |
| TSG Hoffenheim expected goals | 1.47 |
| Expected total goals | 4.18 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.2% |
| Under 2.5 | 36.8% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.66% |
| 2 | 2-1 | 8.83% |
| 3 | 2-0 | 7.60% |
| 4 | 1-0 | 7.49% |
| 5 | 2-2 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 54.4% | 50.2% | 1.95 | +6.0% |
| Draw | 21.6% | 23.8% | 4.05 | -12.4% |
| TSG Hoffenheim win | 24.0% | 26.0% | 3.72 | -10.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | 2347e0e7725940f6a14d5a80601390a5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | crystal palace |
| Matched away-team name | hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7144 |
| Dc lambda away | 1.4701 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.01 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.01 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.72 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.31 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.15056712552729823, "-10": 6.703465794372512e-08, "-11": 6.9524446588178945e-09, "-12": 6.628173006842656e-10, "-13": 5.845770727311644e-11, "-14": 4.795836435185533e-12, "-15": 3.6758932865973427e-13, "-16": 2.622676139601821e-14, "-17": 1.563472487540823e-15, "-2": 0.06246716687746917, "-3": 0.02039789962603649, "-4": 0.005311992315928138, "-5": 0.001144576585356071, "-6": 0.0002097424924147914, "-7": 3.338156639917034e-05, "-8": 4.690812237619848e-06, "-9": 5.896918390072987e-07, "0": 0.2163112804709271, "1": 0.20855219063862956, "10": 2.354436876447096e-05, "11": 4.508671976153965e-06, "12": 7.93648830338349e-07, "13": 1.292408389698919e-07, "14": 1.957698458089684e-08, "15": 2.7705613830950153e-09, "16": 3.649832989467603e-10, "17": 4.01737170142693e-11, "2": 0.16242463462851062, "3": 0.09792847353314489, "4": 0.04708736827545454, "5": 0.018733342917108764, "6": 0.006338409529150751, "7": 0.0018626189993405538, "8": 0.0004832688602329388, "9": 0.00011217325583975541} |
| Raw goal margin distribution | {"-1": 0.11195071365789411, "-10": 2.829194764557e-07, "-11": 3.6727771451638225e-08, "-12": 4.389546042652749e-09, "-13": 4.859319735379071e-10, "-14": 5.008991763567523e-11, "-15": 4.8299740436427694e-12, "-16": 4.374174629907683e-13, "-17": 3.7299041800223883e-14, "-18": 2.9607858952734473e-15, "-19": 1.893248128551224e-16, "-2": 0.05271550947090456, "-3": 0.020144807910506685, "-4": 0.00628604944008052, "-5": 0.0016470485829967203, "-6": 0.0003705775551910975, "-7": 7.289451691755521e-05, "-8": 1.2719309927379496e-05, "-9": 1.9923030147879186e-06, "0": 0.16534062446716957, "1": 0.20413274023268124, "10": 0.00013028586524991008, "11": 3.12285973885581e-05, "12": 6.891296813524542e-06, "13": 1.408575948128963e-06, "14": 2.6808872896244474e-07, "15": 4.773055458972765e-08, "16": 7.981256101682784e-09, "17": 1.2565976694592972e-09, "18": 1.8417429818435223e-10, "19": 2.1744679065803197e-11, "2": 0.17971540224966, "3": 0.12680415002490214, "4": 0.07305863853291343, "5": 0.035344646111279646, "6": 0.014683168588998563, "7": 0.0053328452480354525, "8": 0.0017181105887229115, "9": 0.000496897031623417} |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 16.5% |
| Unadjusted away-win probability | 19.3% |
| Raw p over 1 5 | 91.8% |
| Raw p under 3 5 | 39.8% |
| Raw p btts yes | 71.6% |
| Home training matches | 3 |
| Away training matches | 11 |
| P home draw | 76.0% |
| P draw away | 45.6% |
| P home away | 78.4% |
| Raw p home draw | 80.7% |
| Raw p draw away | 35.9% |
| Raw p home away | 83.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7905 |
| Totals anchor target over 2 5 | 0.6319 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.56 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7713 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.72, "draw": 4.05, "home": 1.94}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.92, "home_away": 1.27, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.92, "home_away": 1.27, "home_draw": 1.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.68, "draw": 4.01, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.16, "under": 5.55}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 4.01 |
| Reference away odds | 3.68 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:56Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:56Z |
| Home probability edge | +4.2% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.1399 |
| Raw ev home | 0.2508 |
| Raw edge prob draw | -0.0728 |
| Raw ev draw | -0.3304 |
| Raw edge prob away | -0.0670 |
| Raw ev away | -0.2813 |
| Market p home draw | 73.7% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:15Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.3% |
| Market draw away odds | 1.92 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.0% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.31 |
| Market reference dc draw away odds | 1.92 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.55 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,446.0302 |
| Elo away rating | 1,431.4646 |
| Elo rating diff | 74.5656 |
| Elo home expectancy | 0.6057 |

</details>


---

## 2026-11-05 — Hapoel Be'er Sheva vs OFI Crete

The model's most likely 1X2 outcome is **OFI Crete win** at **38.5%**. Expected goals are 0.34 for Hapoel Be'er Sheva and 1.31 for OFI Crete (1.65 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 57.4%; Under 3.5 goals: 63.1%; Double Chance 1X: 61.5%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hapoel Be'er Sheva win | 35.1% | 2.85 |
| Draw | 26.4% | 3.79 |
| OFI Crete win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hapoel Be'er Sheva expected goals | 0.34 |
| OFI Crete expected goals | 1.31 |
| Expected total goals | 1.65 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 36.9% |
| Under 3.5 | 63.1% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.32% |
| 2 | 1-0 | 11.51% |
| 3 | 2-1 | 10.45% |
| 4 | 2-2 | 6.71% |
| 5 | 0-0 | 5.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hapoel Be'er Sheva win | 35.1% | 45.8% | 2.11 | -26.0% |
| Draw | 26.4% | 25.8% | 3.70 | -2.3% |
| OFI Crete win | 38.5% | 28.4% | 3.51 | +35.2% |
| Over 2.5 | 57.4% | 57.0% | 1.71 | -1.8% |
| Under 2.5 | 42.6% | 43.0% | 2.24 | -4.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | 2af127e906ae56f3543d283b85f7b54e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | h. beer-sheva |
| Matched away-team name | ofi crete |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.3416 |
| Dc lambda away | 1.3084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.81 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 4.96 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.09644497064166828, "-10": 0.00014288146319943118, "-11": 3.602200838241138e-05, "-12": 8.344130029560846e-06, "-13": 1.7874319933886703e-06, "-14": 3.5606879843309426e-07, "-15": 6.628225910597766e-08, "-16": 1.1578727581951642e-08, "-17": 1.9049120735489896e-09, "-18": 2.9475472556858777e-10, "-19": 3.939479850307774e-11, "-2": 0.10306714894943811, "-3": 0.08360208203183851, "-4": 0.05364808521775188, "-5": 0.028348505492581333, "-6": 0.01270120054750384, "-7": 0.004932409570853847, "-8": 0.001688811308562214, "-9": 0.0005167674938398743, "0": 0.26411500976581814, "1": 0.2626140961335572, "10": 2.1065844153431897e-09, "11": 1.3866936859649053e-10, "12": 8.386935742080156e-12, "13": 4.690956619561087e-13, "14": 2.4399192074515822e-14, "15": 1.185901084435993e-15, "16": 5.409057990462715e-17, "17": 2.3235144247215263e-18, "18": 9.387303350938686e-20, "19": 3.275884616011611e-21, "2": 0.07034709092808636, "3": 0.014898845291395207, "4": 0.0024963149658110083, "5": 0.00034441730165065543, "6": 4.0291107237664174e-05, "7": 4.085386956320851e-06, "8": 3.6522864481460487e-07, "9": 2.9180217733076245e-08} |
| Raw goal margin distribution | {"-1": 0.31606349727893673, "-10": 8.103528823703883e-07, "-11": 9.60637100917163e-08, "-12": 1.0444270463521541e-08, "-13": 1.0481268094754703e-09, "-14": 9.492452788648543e-11, "-2": 0.1902842681566653, "-3": 0.0800712794807094, "-4": 0.025626972421024182, "-5": 0.006608649589878406, "-6": 0.0014260730034192576, "-7": 0.00026445632433814926, "-8": 4.2986411053790986e-05, "-9": 6.218528053724773e-06, "0": 0.27938323781258545, "1": 0.08569608933993188, "10": 1.1933574634603438e-12, "11": 3.693731858411171e-14, "12": 1.0485611352058061e-15, "13": 2.7475089374202235e-17, "14": 6.497007486053795e-19, "2": 0.012972454578654336, "3": 0.0014252980139775136, "4": 0.00011910660629836082, "5": 8.019751493643246e-06, "6": 4.518555093578771e-07, "7": 2.1878695203680916e-08, "8": 9.285563946691511e-10, "9": 3.507311450191559e-11} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 62.0% |
| Raw p over 1 5 | 48.7% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 20.7% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 61.5% |
| P draw away | 64.9% |
| P home away | 73.6% |
| Raw p home draw | 38.0% |
| Raw p draw away | 90.0% |
| Raw p home away | 72.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 2.1524 |
| Totals anchor target over 2 5 | 0.5740 |
| Totals anchor reference over odds | 1.68 |
| Totals anchor reference under odds | 2.22 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2009 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.18, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.7, "home": 2.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.24}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.78, "home_away": 1.3, "home_draw": 1.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.75, "home_away": 1.3, "home_draw": 1.34}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.33, "draw": 3.66, "home": 2.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.2, "under": 4.53}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.11 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.33 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -10.7% |
| Draw probability edge | +0.7% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.3579 |
| Raw ev home | -0.7885 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0337 |
| Raw edge prob away | 0.3361 |
| Raw ev away | 1.1776 |
| Market p home draw | 72.2% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:14Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.9% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.9% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T19:40:14Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.53 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.9% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,422.3390 |
| Elo away rating | 1,425.2946 |
| Elo rating diff | 57.0445 |
| Elo home expectancy | 0.5814 |

</details>


---

## 2026-11-05 — Lillestrom vs Viktoria Plzeň

The model's most likely 1X2 outcome is **Viktoria Plzeň win** at **55.6%**. Expected goals are 0.46 for Lillestrom and 2.49 for Viktoria Plzeň (2.95 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 61.8%; Under 3.5 goals: 58.2%; Double Chance 1X: 44.4%; Double Chance X2: 76.3%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lillestrom win | 23.7% | 4.22 |
| Draw | 20.7% | 4.83 |
| Viktoria Plzeň win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lillestrom expected goals | 0.46 |
| Viktoria Plzeň expected goals | 2.49 |
| Expected total goals | 2.95 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 61.8% |
| Under 2.5 | 38.2% |
| Over 3.5 | 41.8% |
| Under 3.5 | 58.2% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.78% |
| 2 | 1-0 | 8.93% |
| 3 | 0-3 | 7.88% |
| 4 | 0-2 | 7.45% |
| 5 | 2-1 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lillestrom win | 23.7% | 31.6% | 3.05 | -27.7% |
| Draw | 20.7% | 24.2% | 3.95 | -18.2% |
| Viktoria Plzeň win | 55.6% | 44.3% | 2.24 | +24.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | c50815d0a3cbc7dfe6b9f3a737ce4836 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:40:39Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | lillestrøm |
| Matched away-team name | viktoria plzen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.4626 |
| Dc lambda away | 2.4854 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.12 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.34 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.62 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.10843605780044684, "-10": 0.0005025035070905067, "-11": 0.0001430464073242635, "-12": 3.7406271224276546e-05, "-13": 9.04429249737147e-06, "-14": 2.033303273559974e-06, "-15": 4.2711113342715575e-07, "-16": 8.418651936858547e-08, "-17": 1.5629353446237455e-08, "-18": 2.7418214989939135e-09, "-19": 4.5424612407581857e-10, "-2": 0.1334611159213916, "-20": 6.593270268217532e-11, "-3": 0.12351616494827869, "-4": 0.09007742806805322, "-5": 0.05396925502896208, "-6": 0.02737721215545015, "-7": 0.01202587353747047, "-8": 0.0046543987923986065, "-9": 0.0016091446841253621, "0": 0.20709998024044932, "1": 0.1881557649231239, "10": 2.2131696272696792e-10, "11": 1.1725928812113157e-11, "12": 5.707020218502947e-13, "13": 2.5682321955140995e-14, "14": 1.0746240128327137e-15, "15": 4.2013606870401423e-17, "16": 1.5412969660993137e-18, "17": 5.325734056789777e-20, "18": 1.7388909011650905e-21, "19": 5.361904591905378e-23, "2": 0.04081998144469466, "20": 1.4485164257988776e-24, "3": 0.007031314829866467, "4": 0.0009543845868558733, "5": 0.00010642620027515222, "6": 1.0048148601781167e-05, "7": 8.215011097140871e-07, "8": 5.917657249863634e-08, "9": 3.8078164442603e-09} |
| Raw goal margin distribution | {"-1": 0.2241107966965291, "-10": 0.0001442374536925047, "-11": 3.2310171970869606e-05, "-12": 6.643268440197211e-06, "-13": 1.2621509368289916e-06, "-14": 2.2285182610106283e-07, "-15": 3.674943861894743e-08, "-16": 5.684352301123356e-09, "-17": 8.264492893074057e-10, "-18": 1.0726236058459684e-10, "-2": 0.2337000732879161, "-3": 0.17749843355995226, "-4": 0.10449695398231787, "-5": 0.05007409163311961, "-6": 0.020200197683318454, "-7": 0.00703007974089987, "-8": 0.002150148103975868, "-9": 0.0005863571640333408, "0": 0.1264252929378921, "1": 0.0441653922418023, "10": 7.194903748618221e-12, "11": 2.9997212884844386e-13, "12": 1.147937204439354e-14, "13": 4.05921746026741e-16, "14": 1.333957260808898e-17, "15": 4.094219491304125e-19, "16": 1.1786804844722458e-20, "17": 3.189525003996867e-22, "18": 7.704631025860197e-24, "2": 0.008095584997156248, "3": 0.0011444019974966447, "4": 0.0001253956317645618, "5": 1.1183726827308188e-05, "6": 8.39699287097997e-07, "7": 5.4390507391804743e-08, "8": 3.0961780591644355e-09, "9": 1.5715003534594836e-10} |
| Unadjusted home-win probability | 5.4% |
| Unadjusted draw probability | 12.6% |
| Unadjusted away-win probability | 82.0% |
| Raw p over 1 5 | 79.0% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 33.6% |
| Home training matches | 3 |
| Away training matches | 25 |
| P home draw | 44.4% |
| P draw away | 76.3% |
| P home away | 79.3% |
| Raw p home draw | 18.0% |
| Raw p draw away | 94.6% |
| Raw p home away | 87.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2776 |
| Totals anchor target over 2 5 | 0.6177 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.46 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4794 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.72, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.24, "draw": 3.9, "home": 3.04}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.41, "home_away": 1.28, "home_draw": 1.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.41, "home_away": 1.27, "home_draw": 1.71}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.2, "draw": 3.95, "home": 3.05}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.57, "under": 2.46}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 5.21}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.95 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:28Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:28Z |
| Home probability edge | -7.9% |
| Draw probability edge | -3.5% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.2622 |
| Raw ev home | -0.8367 |
| Raw edge prob draw | -0.1152 |
| Raw ev draw | -0.5006 |
| Raw edge prob away | 0.3774 |
| Raw ev away | 0.8369 |
| Market p home draw | 56.8% |
| Market home draw odds | 1.71 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:15Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.1% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.69 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.0% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.21 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,400.8156 |
| Elo away rating | 1,451.8117 |
| Elo rating diff | 9.0039 |
| Elo home expectancy | 0.5130 |

</details>


---

## 2026-11-05 — NEC Nijmegen vs Omonoia FC

The model's most likely 1X2 outcome is **NEC Nijmegen win** at **50.5%**. Expected goals are 2.30 for NEC Nijmegen and 2.20 for Omonoia FC (4.50 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 60.9%; Under 3.5 goals: 61.6%; Double Chance 1X: 72.5%; Double Chance X2: 49.5%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NEC Nijmegen win | 50.5% | 1.98 |
| Draw | 22.0% | 4.55 |
| Omonoia FC win | 27.5% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NEC Nijmegen expected goals | 2.30 |
| Omonoia FC expected goals | 2.20 |
| Expected total goals | 4.50 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 38.4% |
| Under 3.5 | 61.6% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.76% |
| 2 | 1-1 | 9.85% |
| 3 | 1-0 | 9.42% |
| 4 | 2-0 | 7.01% |
| 5 | 2-2 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NEC Nijmegen win | 50.5% | 54.0% | 1.81 | -8.6% |
| Draw | 22.0% | 23.3% | 4.15 | -8.8% |
| Omonoia FC win | 27.5% | 22.7% | 4.30 | +18.3% |
| Over 2.5 | 60.9% | 60.4% | 1.62 | -1.3% |
| Under 2.5 | 39.1% | 39.6% | 2.42 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | 02228f9f6863e25c9538d6062932e155 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | n.e.c. |
| Matched away-team name | omonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2973 |
| Dc lambda away | 2.2015 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.05 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1442396174191776, "-10": 8.023444513360473e-07, "-11": 1.09972014457454e-07, "-12": 1.3854609434525162e-08, "-13": 1.613734142838309e-09, "-14": 1.7309202336362454e-10, "-15": 1.522105305647996e-11, "-2": 0.08000123777906434, "-3": 0.03458088653718966, "-4": 0.011913759960589328, "-5": 0.0033948283703505735, "-6": 0.0008225065440776466, "-7": 0.00017304992016232428, "-8": 3.214228289815378e-05, "-9": 5.340514768868444e-06, "0": 0.21965881238499352, "1": 0.2562105349721038, "10": 2.093981431807237e-06, "11": 2.995061283512913e-07, "12": 3.937579904871212e-08, "13": 4.7860655261260836e-09, "14": 5.357168013318373e-10, "15": 4.91602940737403e-11, "2": 0.14846230524434215, "3": 0.06696797644554492, "4": 0.024076394945891807, "5": 0.007159323651066953, "6": 0.0018101105308348624, "7": 0.0003974190640380983, "8": 7.703100642828853e-05, "9": 1.3356219052613654e-05} |
| Raw goal margin distribution | {"-1": 0.17002773729232526, "-10": 1.2869819730804606e-05, "-11": 2.483436724870254e-06, "-12": 4.416595710365885e-07, "-13": 7.281527921678022e-08, "-14": 1.1185923035782747e-08, "-15": 1.6080697989396884e-09, "-16": 2.1669059757711725e-10, "-17": 2.6839001166741833e-11, "-18": 2.562512201567483e-12, "-2": 0.11316744498589197, "-3": 0.06171656638908003, "-4": 0.027851622501844465, "-5": 0.01064727665523866, "-6": 0.003516237785502972, "-7": 0.0010195174846882385, "-8": 0.0002630218203863595, "-9": 6.105186569766074e-05, "0": 0.18842663206675997, "1": 0.17730927358846313, "10": 1.971006529430142e-05, "11": 3.968992317985294e-06, "12": 7.365909275232561e-07, "13": 1.2672806339879096e-07, "14": 2.031578770079058e-08, "15": 3.0477426629982554e-09, "16": 4.2857321606549755e-10, "17": 5.539401801848538e-11, "18": 5.519173168938494e-12, "2": 0.1232379968833262, "3": 0.07013526395439905, "4": 0.03302909999759469, "5": 0.013176386894170495, "6": 0.004540959161016173, "7": 0.0013739647722926219, "8": 0.0003698999380824408, "9": 8.959896222868592e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.2% |
| Raw p btts yes | 79.7% |
| Home training matches | 3 |
| Away training matches | 9 |
| P home draw | 72.5% |
| P draw away | 49.5% |
| P home away | 78.0% |
| Raw p home draw | 61.2% |
| Raw p draw away | 57.7% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.6974 |
| Totals anchor target over 2 5 | 0.6093 |
| Totals anchor reference over odds | 1.59 |
| Totals anchor reference under odds | 2.41 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8207 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.3, "draw": 4.15, "home": 1.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.09, "home_away": 1.26, "home_draw": 1.24}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.07, "home_away": 1.26, "home_draw": 1.25}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.18, "draw": 4.07, "home": 1.81}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.59, "under": 2.41}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.18, "under": 4.98}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.81 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.18 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -3.5% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.1170 |
| Raw ev home | -0.2339 |
| Raw edge prob draw | -0.0446 |
| Raw ev draw | -0.2180 |
| Raw edge prob away | 0.1616 |
| Raw ev away | 0.6696 |
| Market p home draw | 77.4% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:14Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.9% |
| Market draw away odds | 2.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.7% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 83.2% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.98 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,432.8516 |
| Elo away rating | 1,467.0936 |
| Elo rating diff | 25.7579 |
| Elo home expectancy | 0.5370 |

</details>


---

## 2026-11-05 — PFC Levski Sofia vs Jagiellonia Białystok

The model's most likely 1X2 outcome is **PFC Levski Sofia win** at **58.0%**. Expected goals are 2.26 for PFC Levski Sofia and 0.35 for Jagiellonia Białystok (2.61 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 52.7%; Under 3.5 goals: 66.9%; Double Chance 1X: 80.8%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 1.72 |
| Draw | 22.7% | 4.40 |
| Jagiellonia Białystok win | 19.2% | 5.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PFC Levski Sofia expected goals | 2.26 |
| Jagiellonia Białystok expected goals | 0.35 |
| Expected total goals | 2.61 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.51% |
| 2 | 2-0 | 10.06% |
| 3 | 3-0 | 9.59% |
| 4 | 0-1 | 9.52% |
| 5 | 0-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 48.0% | 2.03 | +17.8% |
| Draw | 22.7% | 26.5% | 3.75 | -14.8% |
| Jagiellonia Białystok win | 19.2% | 25.5% | 3.79 | -27.0% |
| Over 2.5 | 52.7% | 52.7% | 1.84 | -3.0% |
| Under 2.5 | 47.3% | 47.3% | 2.06 | -2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | 3493023efb0aadbdffe37e74e528177c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | levski sofia |
| Matched away-team name | jagiellonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2600 |
| Dc lambda away | 0.3518 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.27 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.02 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.67 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.16059241266235735, "-10": 1.758523195382534e-11, "-11": 7.045291653554482e-13, "-12": 2.5911356572342958e-14, "-13": 8.806734838084442e-16, "-14": 2.781970998793471e-17, "-15": 8.208253786452208e-19, "-16": 2.2718880501687747e-20, "-17": 5.921029145289486e-22, "-18": 1.4552240924386242e-23, "-19": 3.1938752570719848e-25, "-2": 0.02773415867007257, "-3": 0.0037396430850100584, "-4": 0.000392015775708291, "-5": 3.3503337513321966e-05, "-6": 2.4128847689817303e-06, "-7": 1.5001227961018135e-07, "-8": 8.199960418784097e-09, "-9": 3.9977785228253307e-10, "0": 0.22715773522935573, "1": 0.1273350806937961, "10": 0.0002768826537479649, "11": 7.125410619361727e-05, "12": 1.683310932459692e-05, "13": 3.6749580539454816e-06, "14": 7.456814459927344e-07, "15": 1.413236310616521e-07, "16": 2.512547099580517e-08, "17": 4.206179051646601e-09, "18": 6.640238927076369e-10, "19": 9.361276065037951e-11, "2": 0.1506802947211788, "3": 0.13050732637700477, "4": 0.08787625799347597, "5": 0.0482413392557081, "6": 0.022316759764631305, "7": 0.008912194169460786, "8": 0.0031291966600339436, "9": 0.0009799481679056198} |
| Raw goal margin distribution | {"-1": 0.04046495302997333, "-10": 6.319537868104474e-13, "-11": 2.0092926357321744e-14, "-12": 5.861505521307722e-16, "-13": 1.5795208575809345e-17, "-14": 3.954640702040383e-19, "-15": 9.245323650159244e-21, "-16": 2.0251448124387016e-22, "-17": 4.00405393410086e-24, "-2": 0.005873512307018756, "-3": 0.0006475389095187274, "-4": 5.483283243800658e-05, "-5": 3.76063149566129e-06, "-6": 2.164819478933924e-07, "-7": 1.0730301790615007e-08, "-8": 4.668086932891225e-10, "-9": 1.8090439311852678e-11, "0": 0.13860664348095406, "1": 0.24409505339128945, "10": 7.55645410032264e-05, "11": 1.5432603327532835e-05, "12": 2.8918013233904308e-06, "13": 5.005505140014017e-07, "14": 8.049943853010661e-08, "15": 1.2088466497954273e-08, "16": 1.7008595342317971e-09, "17": 2.1601084535333144e-10, "2": 0.2423396234295563, "3": 0.17161517518642044, "4": 0.09334558280325168, "5": 0.041122275946071166, "6": 0.015205521649410027, "7": 0.0048412203077299295, "8": 0.001352835894288027, "9": 0.0003367585018393739} |
| Unadjusted home-win probability | 81.4% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 26.3% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 80.8% |
| P draw away | 42.0% |
| P home away | 77.3% |
| Raw p home draw | 95.3% |
| Raw p draw away | 18.6% |
| Raw p home away | 86.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2645 |
| Totals anchor target over 2 5 | 0.5271 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4035 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.77, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.79, "draw": 3.75, "home": 2.0}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.87, "home_away": 1.3, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.83, "home_away": 1.32, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.74, "draw": 3.6, "home": 2.03}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.26, "under": 3.94}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.03 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.74 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:39Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:39Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | +10.0% |
| Draw probability edge | -3.8% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3343 |
| Raw ev home | 0.6531 |
| Raw edge prob draw | -0.1265 |
| Raw ev draw | -0.4802 |
| Raw edge prob away | -0.2078 |
| Raw ev away | -0.8217 |
| Market p home draw | 74.5% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:14Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.6% |
| Market draw away odds | 1.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.9% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T19:40:14Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.0% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.04 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,427.6479 |
| Elo away rating | 1,424.2193 |
| Elo rating diff | 63.4285 |
| Elo home expectancy | 0.5903 |

</details>


---

## 2026-11-05 — Real Sociedad vs Lyon

The model's most likely 1X2 outcome is **Real Sociedad win** at **56.8%**. Expected goals are 1.96 for Real Sociedad and 1.16 for Lyon (3.12 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.3%; Double Chance 1X: 78.4%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 56.8% | 1.76 |
| Draw | 21.6% | 4.63 |
| Lyon win | 21.6% | 4.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.96 |
| Lyon expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.73% |
| 2 | 1-1 | 9.69% |
| 3 | 1-0 | 8.41% |
| 4 | 2-0 | 8.08% |
| 5 | 3-1 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 56.8% | 57.0% | 1.75 | -0.5% |
| Draw | 21.6% | 21.9% | 4.32 | -6.7% |
| Lyon win | 21.6% | 21.1% | 4.50 | -3.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | d6ef4964addd663baed90f8f19fda1d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:40:39Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | real sociedad |
| Matched away-team name | lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9621 |
| Dc lambda away | 1.1599 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.39 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.45 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.132335584248775, "-10": 8.217131995660187e-08, "-11": 8.833280462589399e-09, "-12": 8.728167081264382e-10, "-13": 7.978123134730445e-11, "-14": 6.78330580377205e-12, "-15": 5.388358416216518e-13, "-16": 3.9852191401904296e-14, "-17": 2.466850433306619e-15, "-2": 0.05717223931975341, "-3": 0.01938941402651535, "-4": 0.005240329775051158, "-5": 0.0011713144511328166, "-6": 0.0002225965516576773, "-7": 3.6733199190174746e-05, "-8": 5.351330461642793e-06, "-9": 6.973618810006236e-07, "0": 0.2159659604100724, "1": 0.23044635179965403, "10": 1.646010527612507e-05, "11": 2.9931417598497656e-06, "12": 5.002893280294818e-07, "13": 7.735561506561341e-08, "14": 1.1125650837071741e-08, "15": 1.494973267387165e-09, "16": 1.8703465355834796e-10, "17": 1.9584189913168215e-11, "2": 0.17082608158205487, "3": 0.0980001141648396, "4": 0.04480365418774527, "5": 0.0169403056137422, "6": 0.005445767464243089, "7": 0.0015201706231869462, "8": 0.00037461768335436343, "9": 8.25805229042604e-05} |
| Raw goal margin distribution | {"-1": 0.14105686784017415, "-10": 6.5738393013845e-08, "-11": 6.816253718557716e-09, "-12": 6.495152362968742e-10, "-13": 5.724501176049094e-11, "-14": 4.690642494774299e-12, "-15": 3.5640110232850697e-13, "-16": 2.2620240372098634e-14, "-2": 0.05960155336507736, "-3": 0.01967188131521457, "-4": 0.0051571850106938814, "-5": 0.00111594734786035, "-6": 0.00020505022769228126, "-7": 3.268944918858734e-05, "-8": 4.597934889915311e-06, "-9": 5.782650352860883e-07, "0": 0.2080747544975308, "1": 0.2351412247407068, "10": 1.2610964258946578e-05, "11": 2.2119121802000587e-06, "12": 3.565368283748619e-07, "13": 5.3155183741433056e-08, "14": 7.367721983243477e-09, "15": 9.469626624963085e-10, "16": 1.0166792357844282e-10, "2": 0.17054673947899704, "3": 0.09521922863414804, "4": 0.0422264329534472, "5": 0.015456398635070558, "6": 0.004804163537391764, "7": 0.0012955615511619147, "8": 0.000308252200927834, "9": 6.557876351102119e-05} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 58.5% |
| Home training matches | 23 |
| Away training matches | 25 |
| P home draw | 78.4% |
| P draw away | 43.2% |
| P home away | 78.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 43.5% |
| Raw p home away | 79.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0381 |
| Totals anchor target over 2 5 | 0.6250 |
| Totals anchor reference over odds | 1.56 |
| Totals anchor reference under odds | 2.53 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6017 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.83, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.48, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.5, "draw": 4.2, "home": 1.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.15, "home_away": 1.25, "home_draw": 1.23}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.21, "home_away": 1.25, "home_draw": 1.23}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.49, "draw": 4.32, "home": 1.72}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.56, "under": 2.53}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 5.33}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 4.32 |
| Reference away odds | 4.49 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:56Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:56Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0048 |
| Raw ev home | -0.0111 |
| Raw edge prob draw | -0.0113 |
| Raw ev draw | -0.1011 |
| Raw edge prob away | 0.0161 |
| Raw ev away | 0.0208 |
| Market p home draw | 78.6% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.7% |
| Market draw away odds | 2.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:15Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.7% |
| Market home away odds | 1.25 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.16 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 84.1% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.33 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.0% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,487.8577 |
| Elo away rating | 1,510.1036 |
| Elo rating diff | 37.7541 |
| Elo home expectancy | 0.5541 |

</details>


---

## 2026-11-05 — SK Sturm Graz vs NK Celje

The model's most likely 1X2 outcome is **SK Sturm Graz win** at **59.1%**. Expected goals are 1.01 for SK Sturm Graz and 0.47 for NK Celje (1.48 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 61.5%; Under 3.5 goals: 59.1%; Double Chance 1X: 83.3%; Double Chance X2: 40.9%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 77.8%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SK Sturm Graz win | 59.1% | 1.69 |
| Draw | 24.2% | 4.13 |
| NK Celje win | 16.7% | 5.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SK Sturm Graz expected goals | 1.01 |
| NK Celje expected goals | 0.47 |
| Expected total goals | 1.48 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 40.9% |
| Under 3.5 | 59.1% |
| Over 4.5 | 22.2% |
| Under 4.5 | 77.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.02% |
| 2 | 2-1 | 9.03% |
| 3 | 2-0 | 8.60% |
| 4 | 1-0 | 8.14% |
| 5 | 2-2 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SK Sturm Graz win | 59.1% | 63.7% | 1.58 | -6.6% |
| Draw | 24.2% | 20.1% | 4.56 | +10.4% |
| NK Celje win | 16.7% | 16.3% | 5.57 | -7.1% |
| Over 2.5 | 61.5% | 60.7% | 1.61 | -0.9% |
| Under 2.5 | 38.5% | 39.3% | 2.44 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | 84b68e09ecbe93fdbce759cd822322a2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | sturm graz |
| Matched away-team name | celje |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0055 |
| Dc lambda away | 0.4749 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.79 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.95 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.44 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.10943890658144653, "-10": 2.0414835894582106e-08, "-11": 1.9156123232900134e-09, "-12": 1.6520151543011452e-10, "-13": 1.3178128029416727e-11, "-14": 9.777381564855273e-13, "-15": 6.777351873569285e-14, "-16": 4.3767541832278966e-15, "-17": 2.377205531899585e-16, "-2": 0.04147746976123701, "-3": 0.012351674594829816, "-4": 0.002924852768120924, "-5": 0.0005720518419885222, "-6": 9.504638561764037e-05, "-7": 1.3705319460708822e-05, "-8": 1.7439585014285418e-06, "-9": 1.98451294265814e-07, "0": 0.24214024286916966, "1": 0.21446106202562457, "10": 3.4929962749813056e-05, "11": 6.939627108054589e-06, "12": 1.2671231421910227e-06, "13": 2.1401036203124772e-07, "14": 3.3618623417709375e-08, "15": 4.93393791204711e-09, "16": 6.746244616432843e-10, "17": 7.75805661354022e-11, "2": 0.1757333623002545, "3": 0.11080110409234771, "4": 0.055551851599482616, "5": 0.023004150555687396, "6": 0.008092499897058774, "7": 0.0024706574882920433, "8": 0.0006656344781020159, "9": 0.0001603724934773313} |
| Raw goal margin distribution | {"-1": 0.14143296992265564, "-10": 3.8220788419328394e-11, "-11": 1.64421767844077e-12, "-12": 6.483534346531836e-14, "-13": 2.284653758284415e-15, "-2": 0.029996401861009943, "-3": 0.004570895513819678, "-4": 0.0005302366756406856, "-5": 4.958339823219138e-05, "-6": 3.880925641543703e-06, "-7": 2.610916334827905e-07, "-8": 1.539807454440734e-08, "-9": 8.082670448447208e-10, "0": 0.3390094561552979, "1": 0.29338176678293765, "10": 6.919304995330245e-08, "11": 6.3022906688458395e-09, "12": 5.261713719747709e-10, "13": 3.9256544990829046e-11, "2": 0.1344688620832887, "3": 0.043384055169229864, "4": 0.010655526095875077, "5": 0.0021096854347464242, "6": 0.00034961738603918194, "7": 4.9799724285720194e-05, "8": 6.218371783158645e-06, "9": 6.911008408376096e-07} |
| Unadjusted home-win probability | 48.4% |
| Unadjusted draw probability | 33.9% |
| Unadjusted away-win probability | 17.7% |
| Raw p over 1 5 | 43.0% |
| Raw p under 3 5 | 93.7% |
| Raw p btts yes | 23.4% |
| Home training matches | 23 |
| Away training matches | 3 |
| P home draw | 83.3% |
| P draw away | 40.9% |
| P home away | 75.8% |
| Raw p home draw | 82.3% |
| Raw p draw away | 51.6% |
| Raw p home away | 66.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 2.2113 |
| Totals anchor target over 2 5 | 0.6154 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2100 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.41, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.57, "draw": 4.56, "home": 1.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.48, "home_away": 1.22, "home_draw": 1.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:30Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.56, "home_away": 1.21, "home_draw": 1.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.53, "draw": 4.54, "home": 1.53}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.57, "under": 2.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.17, "under": 5.0}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.53 |
| Reference draw odds | 4.54 |
| Reference away odds | 5.53 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -4.6% |
| Draw probability edge | +4.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.1523 |
| Raw ev home | -0.2346 |
| Raw edge prob draw | 0.1384 |
| Raw ev draw | 0.5459 |
| Raw edge prob away | 0.0139 |
| Raw ev away | -0.0164 |
| Market p home draw | 82.9% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:39:55Z |
| Market reference home draw last update utc | 2026-11-04T19:40:30Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.6% |
| Market draw away odds | 2.56 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:30Z |
| Market reference draw away last update utc | 2026-11-04T19:40:30Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:30Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.56 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,441.2526 |
| Elo away rating | 1,413.6182 |
| Elo rating diff | 87.6344 |
| Elo home expectancy | 0.6235 |

</details>


---

## 2026-11-05 — Sparta Prague vs Bournemouth

The model's most likely 1X2 outcome is **Bournemouth win** at **74.1%**. Expected goals are 0.26 for Sparta Prague and 3.59 for Bournemouth (3.85 combined). The most likely exact score is 0-3 at 13.1%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 61.4%; Under 3.5 goals: 57.2%; Double Chance 1X: 25.9%; Double Chance X2: 89.3%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 73.8%; BTTS Yes (both teams score): 25.9%; BTTS No (at least one team does not score): 74.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sparta Prague win | 10.7% | 9.31 |
| Draw | 15.2% | 6.60 |
| Bournemouth win | 74.1% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sparta Prague expected goals | 0.26 |
| Bournemouth expected goals | 3.59 |
| Expected total goals | 3.85 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 79.6% |
| Under 1.5 | 20.4% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 26.2% |
| Under 4.5 | 73.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 13.14% |
| 2 | 0-4 | 11.57% |
| 3 | 0-2 | 11.19% |
| 4 | 0-5 | 8.15% |
| 5 | 0-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Prague win | 10.7% | 14.9% | 6.18 | -33.6% |
| Draw | 15.2% | 19.8% | 4.71 | -28.6% |
| Bournemouth win | 74.1% | 65.3% | 1.52 | +12.6% |
| Over 2.5 | 61.4% | 60.7% | 1.62 | -0.6% |
| Under 2.5 | 38.6% | 39.3% | 2.42 | -6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | d437cbfcee6b57ec58d464e6b459c56e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | sparta praha |
| Matched away-team name | bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.2569 |
| Dc lambda away | 3.5896 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 25.9% |
| P btts no | 74.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.92 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.91 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 3.81 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.09705157866068449, "-10": 0.0015832264084640222, "-11": 0.0005035748346675831, "-12": 0.00014697334183914345, "-13": 3.962772864142313e-05, "-14": 9.927825851229567e-06, "-15": 2.322592162649291e-06, "-16": 5.096244532051792e-07, "-17": 1.0528216294543148e-07, "-18": 2.0547894467401197e-08, "-19": 3.8001921567643374e-09, "-2": 0.14892907013750836, "-20": 6.672892050956621e-10, "-21": 1.0737952072250075e-10, "-3": 0.16327128203886035, "-4": 0.13782148675744849, "-5": 0.09435064766976196, "-6": 0.05425711674946617, "-7": 0.026879308569266767, "-8": 0.011691377872349345, "-9": 0.004531087528425509, "0": 0.15154247709522703, "1": 0.09696741364913414, "10": 7.031179078786205e-14, "11": 1.600366702210961e-15, "12": 3.342446088397825e-17, "13": 6.449044539960424e-19, "14": 1.156167348896331e-20, "15": 1.9355743588825737e-22, "16": 3.0391876555350074e-24, "17": 4.49295853663733e-26, "18": 6.275022576451306e-28, "19": 8.304698639790627e-30, "2": 0.009618376644523797, "20": 1.043524796651593e-31, "21": 1.2016569134754936e-33, "3": 0.0007545750802453955, "4": 4.5580589771644865e-05, "5": 2.2329461486340816e-06, "6": 9.188834492142829e-08, "7": 3.2575580581548683e-09, "8": 1.0139350198139077e-10, "9": 2.812012400373531e-12} |
| Raw goal margin distribution | {"-1": 0.11884830039295648, "-10": 0.00227240994127712, "-11": 0.000736438400907148, "-12": 0.00021900626673206208, "-13": 6.016944288023689e-05, "-14": 1.5360326738689726e-05, "-15": 3.661823759827272e-06, "-16": 8.187665454872349e-07, "-17": 1.7236773134611773e-07, "-18": 3.428189901059899e-08, "-19": 6.46105099964851e-09, "-2": 0.1850524456748853, "-20": 1.1560823568566863e-09, "-21": 1.8930195885539622e-10, "-3": 0.20625295679449618, "-4": 0.17716291483638763, "-5": 0.1234745265072705, "-6": 0.07230893946101331, "-7": 0.036486930876989114, "-8": 0.01616679986254918, "-9": 0.006383209290670135, "0": 0.04410794713846802, "1": 0.009418858596399928, "10": 8.001846589286653e-15, "11": 1.8557109083917872e-16, "12": 3.9491241814085475e-18, "13": 7.764090566697174e-20, "14": 1.4183565231416057e-21, "15": 2.419651105947756e-23, "16": 3.8715578565281457e-25, "17": 5.832462889215774e-27, "18": 8.301015863002793e-29, "19": 1.1195407234273945e-30, "2": 0.0009476228781765907, "20": 1.4334939159184336e-32, "21": 1.6797031731155752e-34, "3": 7.558075837610367e-05, "4": 4.6457328589645145e-06, "5": 2.31701656977526e-07, "6": 9.709885664994453e-09, "7": 3.5061445103768527e-10, "8": 1.1116981789162768e-11, "9": 3.141031345912363e-13} |
| Unadjusted home-win probability | 1.0% |
| Unadjusted draw probability | 4.4% |
| Unadjusted away-win probability | 94.5% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.4% |
| Raw p btts yes | 21.9% |
| Home training matches | 13 |
| Away training matches | 3 |
| P home draw | 25.9% |
| P draw away | 89.3% |
| P home away | 84.8% |
| Raw p home draw | 5.5% |
| Raw p draw away | 99.0% |
| Raw p home away | 95.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9812 |
| Totals anchor target over 2 5 | 0.6139 |
| Totals anchor reference over odds | 1.58 |
| Totals anchor reference under odds | 2.44 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6233 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.86, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.86, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.52, "draw": 4.71, "home": 6.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.14, "home_away": 1.21, "home_draw": 2.64}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.15, "home_away": 1.21, "home_draw": 2.68}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.5, "draw": 4.69, "home": 6.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.58, "under": 2.44}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.18, "under": 5.0}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.14 |
| Reference draw odds | 4.69 |
| Reference away odds | 1.50 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -4.2% |
| Draw probability edge | -4.6% |
| Away probability edge | +8.8% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.1385 |
| Raw ev home | -0.9354 |
| Raw edge prob draw | -0.1535 |
| Raw ev draw | -0.7923 |
| Raw edge prob away | 0.2920 |
| Raw ev away | 0.4371 |
| Market p home draw | 36.3% |
| Market home draw odds | 2.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:15Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.3% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T19:40:15Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.4% |
| Market home away odds | 1.21 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.65 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.2% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.4% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,456.4745 |
| Elo away rating | 1,460.7151 |
| Elo rating diff | 55.7595 |
| Elo home expectancy | 0.5796 |

</details>


---

## 2026-11-05 — Sunderland vs Dinamo Zagreb

The model's most likely 1X2 outcome is **Sunderland win** at **62.8%**. Expected goals are 1.48 for Sunderland and 0.78 for Dinamo Zagreb (2.25 combined). The most likely exact score is 1-0 at 10.9%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 57.6%; Under 3.5 goals: 64.4%; Double Chance 1X: 84.2%; Double Chance X2: 37.2%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 62.8% | 1.59 |
| Draw | 21.4% | 4.67 |
| Dinamo Zagreb win | 15.8% | 6.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.48 |
| Dinamo Zagreb expected goals | 0.78 |
| Expected total goals | 2.25 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 10.90% |
| 2 | 2-1 | 10.49% |
| 3 | 2-0 | 10.17% |
| 4 | 1-1 | 10.01% |
| 5 | 3-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 62.8% | 66.3% | 1.47 | -7.7% |
| Draw | 21.4% | 19.7% | 4.82 | +3.1% |
| Dinamo Zagreb win | 15.8% | 13.9% | 6.95 | +10.1% |
| Over 2.5 | 57.6% | 57.9% | 1.68 | -3.2% |
| Under 2.5 | 42.4% | 42.1% | 2.29 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | 6dad8d4dd99ba6f5dae0b3abdf8f669b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:55Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | sunderland |
| Matched away-team name | gnk dinamo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4773 |
| Dc lambda away | 0.7767 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.37 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.98 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.41 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.1034264256903864, "-10": 1.8012330134796336e-08, "-11": 1.6642149531203899e-09, "-12": 1.412694055999624e-10, "-13": 1.108920500695605e-11, "-14": 8.09229256206599e-13, "-15": 5.483335402867823e-14, "-16": 3.1386537371361927e-15, "-2": 0.03967357105782626, "-3": 0.011822636350082242, "-4": 0.002784609225509172, "-5": 0.0005397800575060233, "-6": 8.868696870637405e-05, "-7": 1.2627113128340002e-05, "-8": 1.584847731537948e-06, "-9": 1.7775168949364813e-07, "0": 0.21394038649687197, "1": 0.2559798020496604, "10": 1.47849399648414e-05, "11": 2.59796568046131e-06, "12": 4.194173870696471e-07, "13": 6.261423047485442e-08, "14": 8.68997512476793e-09, "15": 1.1198660839822477e-09, "16": 1.2190990957496504e-10, "2": 0.19026389336252042, "3": 0.10783102662544428, "4": 0.04830231978964629, "5": 0.017807169357859923, "6": 0.005564321148590487, "7": 0.0015067138159766788, "8": 0.0003596570389435514, "9": 7.671655313534164e-05} |
| Raw goal margin distribution | {"-1": 0.14420072978228496, "-10": 2.5659588447153872e-09, "-11": 1.796411000302587e-10, "-12": 1.1543601024790453e-11, "-13": 6.853837894442084e-13, "-14": 3.77251491935333e-14, "-15": 1.8147107020654944e-15, "-2": 0.04565836238929451, "-3": 0.010839527379946253, "-4": 0.001994572647420339, "-5": 0.0002987284134515746, "-6": 3.7664163679952625e-05, "-7": 4.096727287179334e-06, "-8": 3.916027634146308e-07, "-9": 3.3376259718204464e-08, "0": 0.25268179838666893, "1": 0.26881524162783416, "10": 1.5885208262038868e-06, "11": 2.115062741994892e-07, "12": 2.584837108537163e-08, "13": 2.9187710017861954e-09, "14": 3.0554239822268045e-10, "15": 2.7952601956403925e-11, "2": 0.16514634868445546, "3": 0.07456470683102756, "4": 0.026094390042372236, "5": 0.007432726382267773, "6": 0.0017822731497608155, "7": 0.00036868656588024106, "8": 6.702554114487925e-05, "9": 1.0864420594324733e-05} |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 20.3% |
| Raw p over 1 5 | 65.2% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 41.1% |
| Home training matches | 3 |
| Away training matches | 13 |
| P home draw | 84.2% |
| P draw away | 37.2% |
| P home away | 78.6% |
| Raw p home draw | 79.7% |
| Raw p draw away | 45.6% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3282 |
| Totals anchor target over 2 5 | 0.5760 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.22 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4084 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.1, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.02, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.95, "draw": 4.82, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.29}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.8, "home_away": 1.21, "home_draw": 1.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:14Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.74, "home_away": 1.21, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.37, "draw": 4.59, "home": 1.47}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.21, "under": 4.31}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 4.59 |
| Reference away odds | 6.37 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.34 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:40Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.1192 |
| Raw ev home | -0.1999 |
| Raw edge prob draw | 0.0553 |
| Raw ev draw | 0.2179 |
| Raw edge prob away | 0.0638 |
| Raw ev away | 0.4111 |
| Market p home draw | 86.3% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:14Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.0% |
| Market draw away odds | 2.80 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.8% |
| Market home away odds | 1.21 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.82 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 80.7% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.31 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.7% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,448.0520 |
| Elo away rating | 1,437.3148 |
| Elo rating diff | 70.7371 |
| Elo home expectancy | 0.6004 |

</details>


---

## 2026-11-05 — Torreense vs FC Ararat-Armenia

The model's most likely 1X2 outcome is **Torreense win** at **65.9%**. Expected goals are 4.81 for Torreense and 0.93 for FC Ararat-Armenia (5.74 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 47.1%; Under 3.5 goals: 74.0%; Double Chance 1X: 84.1%; Double Chance X2: 34.1%; Double Chance 12 (either team wins): 81.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 33.5%; BTTS No (at least one team does not score): 66.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torreense win | 65.9% | 1.52 |
| Draw | 18.1% | 5.51 |
| FC Ararat-Armenia win | 15.9% | 6.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torreense expected goals | 4.81 |
| FC Ararat-Armenia expected goals | 0.93 |
| Expected total goals | 5.74 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.13% |
| 2 | 1-0 | 12.64% |
| 3 | 3-0 | 10.76% |
| 4 | 0-1 | 8.60% |
| 5 | 1-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torreense win | 65.9% | 54.2% | 1.79 | +18.0% |
| Draw | 18.1% | 24.1% | 4.00 | -27.4% |
| FC Ararat-Armenia win | 15.9% | 21.7% | 4.67 | -25.6% |
| Over 2.5 | 47.1% | 47.1% | 2.04 | -3.8% |
| Under 2.5 | 52.9% | 52.9% | 1.85 | -2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | 402e102fa845ed84ab7e59b3b17f8c29 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:39Z |
| Market best draw last update utc | 2026-11-04T19:39:55Z |
| Market best away last update utc | 2026-11-04T19:39:55Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | torreense |
| Matched away-team name | ararat-armenia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.8065 |
| Dc lambda away | 0.9301 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 25 |
| Score grid omitted mass | 0 |
| P btts yes | 33.5% |
| P btts no | 66.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.74 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.09 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.13213179691573015, "-10": 1.5045790755948693e-11, "-11": 6.001766908013342e-13, "-12": 2.197134580868659e-14, "-13": 7.431346734088434e-16, "-14": 2.3356658477118653e-17, "-15": 6.8556476387115105e-19, "-16": 1.8873760679022615e-20, "-17": 4.885598367869149e-22, "-18": 1.1362604006996342e-23, "-2": 0.023584430534779228, "-3": 0.0032175347604434636, "-4": 0.00033905909082223386, "-5": 2.9026559920742227e-05, "-6": 2.089523373073351e-06, "-7": 1.2966916463903726e-07, "-8": 7.068194743602892e-09, "-9": 3.434066395019047e-10, "0": 0.18149210102777646, "1": 0.20031374407954564, "10": 6.337999494467957e-05, "11": 1.306556579452072e-05, "12": 2.471824715211077e-06, "13": 4.3205640747462454e-07, "14": 7.0177121355327e-08, "15": 1.0644989594001071e-08, "16": 1.5144924452686991e-09, "17": 2.0259948799800737e-10, "18": 2.435063928032731e-11, "2": 0.1952842704214098, "3": 0.1376819571493454, "4": 0.074979249778239, "5": 0.033172116368128855, "6": 0.012340613744560565, "7": 0.00395765700660812, "8": 0.0011148639203811077, "9": 0.0002799200170858914} |
| Raw goal margin distribution | {"-1": 0.017770555570206736, "-10": 6.421921056998028e-10, "-11": 5.25667284500938e-11, "-12": 3.96332299771446e-12, "-13": 2.7688956794381243e-13, "-14": 1.8018108605702434e-14, "-15": 1.0970975953480398e-15, "-16": 6.275684777050576e-17, "-17": 3.3846122296889574e-18, "-18": 1.7265397647948563e-19, "-19": 8.354338477498803e-21, "-2": 0.005055872481842248, "-20": 3.844528577428693e-22, "-21": 1.686525402054005e-23, "-22": 7.067726231355094e-25, "-23": 2.833010677988218e-26, "-24": 1.0758751440416017e-27, "-25": 3.395408191062949e-29, "-3": 0.0011953641575840749, "-4": 0.00023223275927182702, "-5": 3.804056512479856e-05, "-6": 5.365650015053878e-06, "-7": 6.629567153767024e-07, "-8": 7.276285097250988e-08, "-9": 7.176429352688728e-09, "0": 0.043017464339313076, "1": 0.08883078983042415, "10": 0.008725375060019653, "11": 0.00369098265889554, "12": 0.0014381442103101488, "13": 0.0005192320331364328, "14": 0.00017461276865046705, "15": 5.494446835912896e-05, "16": 1.6242457822821457e-05, "17": 4.5270100646029885e-06, "18": 1.1934137576845554e-06, "19": 2.9842722173789957e-07, "2": 0.13502678899603948, "20": 7.097107387031792e-08, "21": 1.608951985833497e-08, "22": 3.4845109226663856e-09, "23": 7.218089073020991e-10, "24": 1.4166018802449642e-10, "25": 2.3104142044641587e-11, "3": 0.16498177511039525, "4": 0.16564225678831163, "5": 0.14021889196402418, "6": 0.10221010313295525, "7": 0.06526323138165144, "8": 0.037017324015882334, "9": 0.018867555722028466} |
| Unadjusted home-win probability | 93.3% |
| Unadjusted draw probability | 4.3% |
| Unadjusted away-win probability | 2.4% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.6% |
| Raw p btts yes | 60.0% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 84.1% |
| P draw away | 34.1% |
| P home away | 81.9% |
| Raw p home draw | 97.6% |
| Raw p draw away | 6.7% |
| Raw p home away | 95.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.4754 |
| Totals anchor target over 2 5 | 0.4714 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-11-04T19:40:39Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.8603 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.43, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.35, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.67, "draw": 4.0, "home": 1.76}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.85}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:39:55Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.13, "home_away": 1.27, "home_draw": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.06, "home_away": 1.27, "home_draw": 1.24}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.27, "draw": 3.87, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:39Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.34, "under": 3.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.87 |
| Reference away odds | 4.27 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:39Z |
| Market reference home last update utc | 2026-11-04T19:40:39Z |
| Market reference draw last update utc | 2026-11-04T19:40:39Z |
| Market reference away last update utc | 2026-11-04T19:40:39Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:39Z |
| Market best over 2 5 last update utc | 2026-11-04T19:39:55Z |
| Market best under 2 5 last update utc | 2026-11-04T19:39:55Z |
| Home probability edge | +11.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3907 |
| Raw ev home | 0.6695 |
| Raw edge prob draw | -0.1978 |
| Raw ev draw | -0.8279 |
| Raw edge prob away | -0.1929 |
| Raw ev away | -0.8865 |
| Market p home draw | 79.3% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T19:40:15Z |
| Market reference home draw last update utc | 2026-11-04T19:40:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.1% |
| Market draw away odds | 2.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:39:55Z |
| Market reference draw away last update utc | 2026-11-04T19:40:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:39:55Z |
| Market reference home away last update utc | 2026-11-04T19:40:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 72.7% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.29 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:39Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.1% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.66 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:39Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,421.4152 |
| Elo away rating | 1,403.0006 |
| Elo rating diff | 78.4146 |
| Elo home expectancy | 0.6110 |

</details>


---
