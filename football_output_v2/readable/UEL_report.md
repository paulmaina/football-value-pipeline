# UEFA Europa League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Europa League |
| Training matches | 696 |
| Training data through | 2026-10-15 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 5 |
| Training seasons loaded | ['2022', '2023', '2024', '2025', '2026'] |
| Training sha256 | cb7bcd063c85ea171d3f3686cb2c583c24b68c5ce95d6bd2f8818fdfda795800 |
| Training as of utc | 2026-10-22T10:58:07.768738+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 997.560 |
| Base scoring parameter | 0.052 |
| Home-advantage parameter | 0.290 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-15', 'verified_at_utc': '2026-10-22T10:58:04.197154+00:00', 'official_source_health': {'2025': {'status': 'HTTP_403_USING_REVIEWED_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}, '2026': {'status': 'HTTP_403_USING_REVIEWED_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'f70b1b52c2d0762cfe38cf1abbccd3cfaa1bcfd0a6bc8ebd090533e34ae1ba20'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 5.00 |
| Over 1 5 in window quote fixtures | 18 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-22 — Besiktas JK vs Crystal Palace

The model's most likely 1X2 outcome is **Besiktas JK win** at **42.2%**. Expected goals are 1.80 for Besiktas JK and 1.71 for Crystal Palace (3.51 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 67.7%; Under 3.5 goals: 53.4%; Double Chance 1X: 65.1%; Double Chance X2: 57.8%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 42.2% | 2.37 |
| Draw | 22.9% | 4.37 |
| Crystal Palace win | 34.9% | 2.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.80 |
| Crystal Palace expected goals | 1.71 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.7% |
| Under 2.5 | 32.3% |
| Over 3.5 | 46.6% |
| Under 3.5 | 53.4% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.40% |
| 2 | 2-1 | 8.48% |
| 3 | 2-2 | 7.62% |
| 4 | 1-2 | 7.32% |
| 5 | 1-0 | 5.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Besiktas JK win | 42.2% | 43.2% | 2.28 | -3.7% |
| Draw | 22.9% | 24.5% | 3.77 | -13.6% |
| Crystal Palace win | 34.9% | 32.3% | 3.03 | +5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 7b1674efd0f6f93a16f202822f4b64b5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | crystal palace |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8027 |
| Dc lambda away | 1.7088 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.3% |
| P btts no | 31.7% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.81 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.10 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.17387222103103264, "-10": 2.1454942880225727e-06, "-11": 3.2582911779694776e-07, "-12": 4.551331943509458e-08, "-13": 5.883986907978301e-09, "-14": 7.072372507262152e-10, "-15": 7.842318744702816e-11, "-16": 7.023287575747473e-12, "-2": 0.10210420131826105, "-3": 0.04747277268399695, "-4": 0.017781230256921347, "-5": 0.00554457648741717, "-6": 0.0014762318381877746, "-7": 0.00034228430307442503, "-8": 7.020410785362698e-05, "-9": 1.2899482267358482e-05, "0": 0.2290869376018111, "1": 0.20116502401925834, "10": 4.023791045850898e-06, "11": 6.446819054035646e-07, "12": 9.500394302662557e-08, "13": 1.2957533734349073e-08, "14": 1.6430974011711989e-09, "15": 1.9221629524566145e-10, "16": 1.8160746449195578e-11, "2": 0.12478759684452302, "3": 0.061209655819401396, "4": 0.024187148813571535, "5": 0.007956806209299026, "6": 0.0022349741301782708, "7": 0.0005467042463503276, "8": 0.00011829748722934184, "9": 2.293151806707029e-05} |
| Raw goal margin distribution | {"-1": 0.1866386409087447, "-10": 2.303025380474888e-06, "-11": 3.4975284351641106e-07, "-12": 4.885509618638566e-08, "-13": 6.316013639889689e-09, "-14": 7.591655440578917e-10, "-15": 8.418134325340385e-11, "-16": 7.538966489735164e-12, "-2": 0.10960111541746445, "-3": 0.050958420622749155, "-4": 0.01908680195811691, "-5": 0.0059516822980102465, "-6": 0.001584622904750317, "-7": 0.0003674162367708275, "-8": 7.535878473464308e-05, "-9": 1.384661577640135e-05, "0": 0.21296496647530347, "1": 0.19664870393095088, "10": 3.933453630486942e-06, "11": 6.302082668864448e-07, "12": 9.287102644009963e-08, "13": 1.2666626454693144e-08, "14": 1.606208514367274e-09, "15": 1.879008814715706e-10, "16": 1.7753022768565547e-11, "2": 0.12198601275629414, "3": 0.05983544874974162, "4": 0.02364412744791328, "5": 0.007778169371722397, "6": 0.0021847971244578065, "7": 0.0005344302867880601, "8": 0.00011564161143495414, "9": 2.2416686643433837e-05} |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 67.9% |
| Home training matches | 0 |
| Away training matches | 2 |
| P home draw | 65.1% |
| P draw away | 57.8% |
| P home away | 77.1% |
| Raw p home draw | 62.6% |
| Raw p draw away | 58.7% |
| Raw p home away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:04Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.25, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:04Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.68, "price": 2.25, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | -0.9% |
| Draw probability edge | -1.6% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | -0.0190 |
| Raw ev home | -0.0589 |
| Raw edge prob draw | -0.0322 |
| Raw ev draw | -0.1971 |
| Raw edge prob away | 0.0512 |
| Raw ev away | 0.1341 |
| Market p home draw | 68.1% |
| Market home draw odds | 1.42 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:04Z |
| Market reference home draw last update utc | 2026-10-22T10:58:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.5% |
| Market draw away odds | 1.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:04Z |
| Market reference draw away last update utc | 2026-10-22T10:58:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:04Z |
| Market reference home away last update utc | 2026-10-22T10:58:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.68 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 85.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.9% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.13 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.3% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:04Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.85 |
| Market reference btts yes last update utc | 2026-10-22T10:58:04Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Bournemouth vs AC Milan

The model's most likely 1X2 outcome is **Bournemouth win** at **63.2%**. Expected goals are 2.89 for Bournemouth and 1.02 for AC Milan (3.91 combined). The most likely exact score is 1-1 at 7.9%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 71.9%; Under 3.5 goals: 47.5%; Double Chance 1X: 82.1%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 67.2%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 63.2% | 1.58 |
| Draw | 18.9% | 5.29 |
| AC Milan win | 17.9% | 5.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 2.89 |
| AC Milan expected goals | 1.02 |
| Expected total goals | 3.91 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 52.5% |
| Under 3.5 | 47.5% |
| Over 4.5 | 32.8% |
| Under 4.5 | 67.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 7.92% |
| 2 | 2-1 | 7.11% |
| 3 | 2-0 | 6.97% |
| 4 | 3-1 | 6.85% |
| 5 | 3-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 63.2% | 50.5% | 1.97 | +24.5% |
| Draw | 18.9% | 24.4% | 3.91 | -26.1% |
| AC Milan win | 17.9% | 25.1% | 3.68 | -34.1% |
| Over 2.5 | 71.9% | 55.7% | 1.75 | +25.9% |
| Under 2.5 | 28.1% | 44.3% | 2.20 | -38.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | af99d0f507da72d045d9403ae167a5a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | bournemouth |
| Matched away-team name | milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8887 |
| Dc lambda away | 1.0195 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.44 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.76 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.05 |
| Fair Under 4.5 odds | 1.49 |
| Goal margin distribution | {"-1": 0.12168860787538965, "-10": 1.4664959031809012e-08, "-11": 1.3300554498324765e-09, "-12": 1.1093899119330155e-10, "-13": 8.563588001114735e-12, "-14": 6.15096475221336e-13, "-15": 4.130497970918452e-14, "-16": 2.6039424430644566e-15, "-17": 1.5460430969370742e-16, "-18": 8.598203842760513e-18, "-19": 3.99449555937761e-19, "-2": 0.042395227218204226, "-3": 0.011845680243974347, "-4": 0.00266044973369177, "-5": 0.0004967561216860457, "-6": 7.912671452913259e-05, "-7": 1.0969462729874387e-05, "-8": 1.344634183078193e-06, "-9": 1.4761175421992199e-07, "0": 0.18891327838137895, "1": 0.16667539599642875, "10": 0.00024285876853244933, "11": 6.241076404707824e-05, "12": 1.474995796290094e-05, "13": 3.2261098642936842e-06, "14": 6.565736423527208e-07, "15": 1.249278992404958e-07, "16": 2.2315428071986143e-08, "17": 3.754155484288468e-09, "18": 5.915823585777724e-10, "19": 7.787288026574619e-11, "2": 0.16898780252427104, "3": 0.13378740022584087, "4": 0.08513871379113035, "5": 0.04504349416672633, "6": 0.020329598254091943, "7": 0.007985605243297049, "8": 0.0027735975580215353, "9": 0.0008627342865075311} |
| Raw goal margin distribution | {"-1": 0.07257812980678184, "-10": 8.746548414060933e-09, "-11": 7.93278341938218e-10, "-12": 6.616678951332843e-11, "-13": 5.1075381040857726e-12, "-14": 3.6685892460880567e-13, "-15": 2.4635323152595353e-14, "-16": 1.5530564112924e-15, "-17": 9.220987776545279e-17, "-18": 5.128183857966948e-18, "-19": 2.382417074883424e-19, "-2": 0.025285574039779306, "-3": 0.0070650600200569385, "-4": 0.0015867587729660449, "-5": 0.0002962777774478497, "-6": 4.719315191903839e-05, "-7": 6.542461975855103e-06, "-8": 8.019734631364944e-07, "-9": 8.803934276042413e-08, "0": 0.1340226765573803, "1": 0.20022697696475827, "10": 0.0002917459818345246, "11": 7.49739848554195e-05, "12": 1.7719108903945236e-05, "13": 3.87552236862573e-06, "14": 7.887412222847964e-07, "15": 1.5007575325645752e-07, "16": 2.68075001461165e-08, "17": 4.509863013559925e-09, "18": 7.106672618089772e-10, "19": 9.354860871896789e-11, "2": 0.2030048684814723, "3": 0.16071866242194682, "4": 0.10227704684998054, "5": 0.05411070191263609, "6": 0.024421924885734622, "7": 0.00959309913464103, "8": 0.0033319198135961627, "9": 0.0010364017861097619} |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 13.4% |
| Unadjusted away-win probability | 10.7% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 45.2% |
| Raw p btts yes | 60.1% |
| Home training matches | 2 |
| Away training matches | 8 |
| P home draw | 82.1% |
| P draw away | 36.8% |
| P home away | 81.1% |
| Raw p home draw | 89.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 86.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | +12.7% |
| Draw probability edge | -5.5% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | +16.3% |
| Under 2.5 probability edge | -16.3% |
| Raw edge prob home | 0.2544 |
| Raw ev home | 0.4954 |
| Raw edge prob draw | -0.1098 |
| Raw ev draw | -0.4760 |
| Raw edge prob away | -0.1446 |
| Raw ev away | -0.6067 |
| Market p home draw | 74.1% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-22T10:57:31Z |
| Market reference home draw last update utc | 2026-10-22T10:57:53Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.1% |
| Market draw away odds | 1.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-22T10:57:31Z |
| Market reference draw away last update utc | 2026-10-22T10:57:53Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-22T10:57:31Z |
| Market reference home away last update utc | 2026-10-22T10:57:53Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.87 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 79.8% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.85 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.1% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:57:45Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-22T10:57:45Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Celtic vs Celta Vigo

The model's most likely 1X2 outcome is **Celta Vigo win** at **43.3%**. Expected goals are 1.67 for Celtic and 2.10 for Celta Vigo (3.77 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.7%; Under 3.5 goals: 48.1%; Double Chance 1X: 56.7%; Double Chance X2: 66.7%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 71.7%; BTTS No (at least one team does not score): 28.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celtic win | 33.3% | 3.00 |
| Draw | 23.4% | 4.28 |
| Celta Vigo win | 43.3% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celtic expected goals | 1.67 |
| Celta Vigo expected goals | 2.10 |
| Expected total goals | 3.77 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.7% |
| Under 2.5 | 28.3% |
| Over 3.5 | 51.9% |
| Under 3.5 | 48.1% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.91% |
| 2 | 2-2 | 8.23% |
| 3 | 1-2 | 7.60% |
| 4 | 2-1 | 7.14% |
| 5 | 1-3 | 5.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 33.3% | 35.1% | 2.75 | -8.4% |
| Draw | 23.4% | 26.6% | 3.55 | -17.1% |
| Celta Vigo win | 43.3% | 38.3% | 2.58 | +11.8% |
| Over 2.5 | 71.7% | 56.0% | 1.78 | +27.7% |
| Under 2.5 | 28.3% | 44.0% | 2.13 | -39.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | c614844f2e3b782814e4f4e77f98bf2a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | celtic |
| Matched away-team name | celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6721 |
| Dc lambda away | 2.0986 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 71.7% |
| P btts no | 28.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.38 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.77 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.54 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.18302341694868535, "-10": 1.2917969888589896e-05, "-11": 2.4020464512119976e-06, "-12": 4.1100628999759513e-07, "-13": 6.511399277327687e-08, "-14": 9.601804750159535e-09, "-15": 1.3226956514037903e-09, "-16": 1.6852466505371897e-10, "-17": 1.7244445311428044e-11, "-2": 0.1283241901826055, "-3": 0.07167291470564699, "-4": 0.03246451224500079, "-5": 0.012293208155289875, "-6": 0.003985583647878359, "-7": 0.0011274059839975602, "-8": 0.00028248218491436406, "-9": 6.346881114522303e-05, "0": 0.23361105223448192, "1": 0.17276278029373016, "10": 1.5699648259534222e-06, "11": 2.325967614840432e-07, "12": 3.171008000683022e-08, "13": 4.0026701632985226e-09, "14": 4.702783165007609e-10, "15": 5.161650771218101e-11, "16": 5.239849001124508e-12, "17": 4.27199893795234e-13, "2": 0.09602655025280445, "3": 0.04273310683203043, "4": 0.015422148908218414, "5": 0.00465294428937884, "6": 0.0012019354738262154, "7": 0.00027089199263742917, "8": 5.407960406707162e-05, "9": 9.681204869539967e-06} |
| Raw goal margin distribution | {"-1": 0.204187642041915, "-10": 1.4411761377284112e-05, "-11": 2.6798111909671167e-06, "-12": 4.585337035999823e-07, "-13": 7.26435604250432e-08, "-14": 1.071212582503376e-08, "-15": 1.475647819835847e-09, "-16": 1.880123022338184e-10, "-17": 1.9238536167470128e-11, "-2": 0.14316317686097424, "-3": 0.07996093448588887, "-4": 0.03621860150936933, "-5": 0.013714754254986108, "-6": 0.004446463413199553, "-7": 0.0012577754985360651, "-8": 0.00031514749433775394, "-9": 7.080813541242212e-05, "0": 0.20135377252798256, "1": 0.16350965394367206, "10": 1.4858779475471176e-06, "11": 2.2013894378183369e-07, "12": 3.001169696173924e-08, "13": 3.788288265208908e-09, "14": 4.4509034097226067e-10, "15": 4.885194194866689e-11, "16": 4.959204149379261e-12, "17": 4.0431918657752234e-13, "2": 0.09088339499136039, "3": 0.04044433354315984, "4": 0.014596142912051113, "5": 0.004403733890378528, "6": 0.0011375601449213324, "7": 0.00025638309303051493, "8": 5.11831155494468e-05, "9": 9.162682235634995e-06} |
| Unadjusted home-win probability | 31.5% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 48.3% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 47.9% |
| Raw p btts yes | 70.9% |
| Home training matches | 12 |
| Away training matches | 16 |
| P home draw | 56.7% |
| P draw away | 66.7% |
| P home away | 76.6% |
| Raw p home draw | 51.7% |
| Raw p draw away | 68.5% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.58, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.58, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | -1.8% |
| Draw probability edge | -3.2% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | +15.7% |
| Under 2.5 probability edge | -15.7% |
| Raw edge prob home | -0.0357 |
| Raw ev home | -0.1329 |
| Raw edge prob draw | -0.0645 |
| Raw ev draw | -0.2852 |
| Raw edge prob away | 0.1002 |
| Raw ev away | 0.2471 |
| Market p home draw | 62.7% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.8% |
| Market draw away odds | 1.49 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.54 |
| Market reference dc draw away odds | 1.49 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 80.4% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.1% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.55 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.51 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Dinamo Zagreb vs NEC Nijmegen

The model's most likely 1X2 outcome is **Dinamo Zagreb win** at **76.4%**. Expected goals are 3.61 for Dinamo Zagreb and 0.82 for NEC Nijmegen (4.42 combined). The most likely exact score is 3-0 at 8.2%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 78.5%; Under 3.5 goals: 38.6%; Double Chance 1X: 90.0%; Double Chance X2: 23.6%; Double Chance 12 (either team wins): 86.4%; Under 4.5 goals: 58.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Dinamo Zagreb win | 76.4% | 1.31 |
| Draw | 13.6% | 7.36 |
| NEC Nijmegen win | 10.0% | 10.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Dinamo Zagreb expected goals | 3.61 |
| NEC Nijmegen expected goals | 0.82 |
| Expected total goals | 4.42 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 78.5% |
| Under 2.5 | 21.5% |
| Over 3.5 | 61.4% |
| Under 3.5 | 38.6% |
| Over 4.5 | 42.0% |
| Under 4.5 | 58.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 8.22% |
| 2 | 4-0 | 7.41% |
| 3 | 2-0 | 6.84% |
| 4 | 3-1 | 6.71% |
| 5 | 4-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Dinamo Zagreb win | 76.4% | 65.6% | 1.51 | +15.4% |
| Draw | 13.6% | 19.2% | 4.78 | -35.1% |
| NEC Nijmegen win | 10.0% | 15.3% | 5.98 | -40.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | 13c0a92ee5159d2f1d2e0368811c9421 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | gnk dinamo |
| Matched away-team name | n.e.c. |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6065 |
| Dc lambda away | 0.8162 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 57.57 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.31 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.65 |
| Fair Over 3.5 odds | 1.63 |
| Fair Under 3.5 odds | 2.59 |
| Fair Over 4.5 odds | 2.38 |
| Fair Under 4.5 odds | 1.73 |
| Goal margin distribution | {"-1": 0.07399590686694764, "-10": 1.1927961565573042e-09, "-11": 8.660687713831788e-11, "-12": 5.783135768100849e-12, "-13": 3.573805539162878e-13, "-14": 2.055009907049326e-14, "-15": 1.1047616531135008e-15, "-16": 5.575735395727054e-17, "-17": 2.6516415435602817e-18, "-18": 1.1921550863176779e-19, "-19": 5.0819435970196955e-21, "-2": 0.02043325404597356, "-20": 2.058826794698717e-22, "-21": 7.892124554498613e-24, "-22": 2.5823794405380194e-25, "-3": 0.004570981373471076, "-4": 0.0008219059200514134, "-5": 0.00012286294925828816, "-6": 1.5667762899733232e-05, "-7": 1.7388907628043075e-06, "-8": 1.7064438989580284e-07, "-9": 1.499712996532321e-08, "0": 0.1358710165445483, "1": 0.13042501625752406, "10": 0.0014050685533154852, "11": 0.0004508014592964351, "12": 0.00013301418978627435, "13": 3.632178254858226e-05, "14": 9.228939681098565e-06, "15": 2.1923411217292633e-06, "16": 4.889262395289695e-07, "17": 1.0274428060103297e-07, "18": 2.041160936649678e-08, "19": 3.844819747524361e-09, "2": 0.16559819862035777, "20": 6.882838928431629e-10, "21": 1.1658518776272549e-10, "22": 1.6856645453181066e-11, "3": 0.16369264880923506, "4": 0.1300599206025757, "5": 0.08591004830276204, "6": 0.048409619491277804, "7": 0.023740979329728427, "8": 0.01029484934644068, "9": 0.00399795394467589} |
| Raw goal margin distribution | {"-1": 0.03506955644991081, "-10": 5.653127844062946e-10, "-11": 4.1046388852481365e-11, "-12": 2.7408543913325932e-12, "-13": 1.693766323075628e-13, "-14": 9.739496276460076e-15, "-15": 5.235897875706228e-16, "-16": 2.6425592372536826e-17, "-17": 1.2567167122368683e-18, "-18": 5.65008956128369e-20, "-19": 2.4085319769295605e-21, "-2": 0.009684118846048242, "-20": 9.757586000953077e-23, "-21": 3.740386722624855e-24, "-22": 1.2238906907091323e-25, "-3": 0.002166366980226015, "-4": 0.00038953338475312233, "-5": 5.822956048587451e-05, "-6": 7.4255660714315175e-06, "-7": 8.241283923453544e-07, "-8": 8.08750553604548e-08, "-9": 7.107726875369621e-09, "0": 0.08006287728170408, "1": 0.14892537564584568, "10": 0.0016043729041789725, "11": 0.0005147461629205971, "12": 0.0001518818149198885, "13": 4.1473907885077854e-05, "14": 1.0538034406732657e-05, "15": 2.5033174958759505e-06, "16": 5.582788177782729e-07, "17": 1.1731821872085294e-07, "18": 2.3306928990062e-08, "19": 4.3901947772047825e-09, "2": 0.1890877581883333, "20": 7.859146982221652e-10, "21": 1.3312241301947105e-10, "22": 1.92477051433682e-11, "3": 0.18691191240677715, "4": 0.14850849237360217, "5": 0.09809610596466765, "6": 0.0552763647226695, "7": 0.02710855912717662, "8": 0.01175513985069272, "9": 0.004565050556329139} |
| Unadjusted home-win probability | 87.3% |
| Unadjusted draw probability | 8.0% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.6% |
| Raw p btts yes | 54.1% |
| Home training matches | 12 |
| Away training matches | 2 |
| P home draw | 90.0% |
| P draw away | 23.6% |
| P home away | 86.4% |
| Raw p home draw | 95.3% |
| Raw p draw away | 12.7% |
| Raw p home away | 92.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.88, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.2, "price": 4.88, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.46 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.40 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | +10.8% |
| Draw probability edge | -5.6% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | +13.9% |
| Under 2.5 probability edge | -13.9% |
| Raw edge prob home | 0.2168 |
| Raw ev home | 0.3176 |
| Raw edge prob draw | -0.1116 |
| Raw ev draw | -0.6173 |
| Raw edge prob away | -0.1052 |
| Raw ev away | -0.7167 |
| Market p home draw | 84.3% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.5% |
| Market draw away odds | 2.73 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.1% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.73 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.21 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.27 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — FC Ararat-Armenia vs AZ Alkmaar

The model's most likely 1X2 outcome is **AZ Alkmaar win** at **55.0%**. Expected goals are 1.44 for FC Ararat-Armenia and 1.44 for AZ Alkmaar (2.88 combined). The most likely exact score is 0-1 at 12.4%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 56.1%; Under 3.5 goals: 67.3%; Double Chance 1X: 45.0%; Double Chance X2: 75.2%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Ararat-Armenia win | 24.8% | 4.03 |
| Draw | 20.2% | 4.95 |
| AZ Alkmaar win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Ararat-Armenia expected goals | 1.44 |
| AZ Alkmaar expected goals | 1.44 |
| Expected total goals | 2.88 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.45% |
| 2 | 1-2 | 12.07% |
| 3 | 1-1 | 9.42% |
| 4 | 0-2 | 8.38% |
| 5 | 1-3 | 5.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Ararat-Armenia win | 24.8% | 11.5% | 7.64 | +89.4% |
| Draw | 20.2% | 16.7% | 5.32 | +7.5% |
| AZ Alkmaar win | 55.0% | 71.8% | 1.39 | -23.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | 0c104f64573962dd1a690f53ba969caa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | az alkmaar |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4404 |
| Dc lambda away | 1.4438 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.41 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.295148724893271, "-10": 1.0525964398058148e-06, "-11": 1.3604226595553202e-07, "-12": 1.6147987403614755e-08, "-13": 1.7577795204734222e-09, "-14": 1.5783486331507833e-10, "-2": 0.15933815139662047, "-3": 0.06622792374678288, "-4": 0.021781092868071766, "-5": 0.0058993216128522, "-6": 0.0013548507914401288, "-7": 0.0002697114881542811, "-8": 4.733998857255813e-05, "-9": 7.426058151621844e-06, "0": 0.20205181031767816, "1": 0.13322890801492657, "10": 4.649376911526565e-07, "11": 5.994635986248651e-08, "12": 7.09844894362786e-09, "13": 7.708423431675122e-10, "14": 6.904944666741496e-11, "2": 0.0717470120687887, "3": 0.029749610688894847, "4": 0.009760586510071622, "5": 0.002637268959107572, "6": 0.0006042267119382591, "7": 0.00011999523438407711, "8": 2.1011100661874265e-05, "9": 3.288024932112439e-06} |
| Raw goal margin distribution | {"-1": 0.20513850099617809, "-10": 7.315906782038806e-07, "-11": 9.455404735471209e-08, "-12": 1.122340586523137e-08, "-13": 1.2217171395271698e-09, "-14": 1.0970065100941931e-10, "-2": 0.11074548785811143, "-3": 0.04603068167215373, "-4": 0.015138607637998493, "-5": 0.0041002311393771715, "-6": 0.000941667833835355, "-7": 0.0001874587477937605, "-8": 3.290291799994214e-05, "-9": 5.161365471204463e-06, "0": 0.23690851151871545, "1": 0.20465996366502223, "10": 7.142153485724076e-07, "11": 9.208677016201543e-08, "12": 1.0904302410991235e-08, "13": 1.1841316445110293e-09, "14": 1.0607050269045039e-10, "2": 0.11021437540737848, "3": 0.045699948557377905, "4": 0.014993752559142487, "5": 0.004051248166691988, "6": 0.0009281845716011225, "7": 0.00018433101850740693, "8": 3.227626167692929e-05, "9": 5.050908794211735e-06} |
| Unadjusted home-win probability | 38.1% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 77.7% |
| Raw p under 3 5 | 67.3% |
| Raw p btts yes | 57.7% |
| Home training matches | 0 |
| Away training matches | 14 |
| P home draw | 45.0% |
| P draw away | 75.2% |
| P home away | 79.8% |
| Raw p home draw | 61.8% |
| Raw p draw away | 61.9% |
| Raw p home away | 76.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:45Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.19, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:45Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.61, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 6.75 |
| Reference draw odds | 4.85 |
| Reference away odds | 1.34 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | +13.3% |
| Draw probability edge | +3.5% |
| Away probability edge | -16.8% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | 0.2658 |
| Raw ev home | 1.9091 |
| Raw edge prob draw | 0.0697 |
| Raw ev draw | 0.2604 |
| Raw edge prob away | -0.3355 |
| Raw ev away | -0.4686 |
| Market p home draw | 31.1% |
| Market home draw odds | 3.20 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:57:45Z |
| Market reference home draw last update utc | 2026-10-22T10:57:53Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.1% |
| Market draw away odds | 1.11 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:57:45Z |
| Market reference draw away last update utc | 2026-10-22T10:57:53Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.8% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:57:45Z |
| Market reference home away last update utc | 2026-10-22T10:57:53Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.05 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.0% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:57:45Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.13 |
| Market reference btts yes last update utc | 2026-10-22T10:57:45Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Ferencváros TC vs Torreense

The model's most likely 1X2 outcome is **Ferencváros TC win** at **54.1%**. Expected goals are 2.21 for Ferencváros TC and 2.87 for Torreense (5.07 combined). The most likely exact score is 3-2 at 8.3%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.0%; Under 3.5 goals: 26.5%; Double Chance 1X: 69.8%; Double Chance X2: 45.9%; Double Chance 12 (either team wins): 84.3%; Under 4.5 goals: 43.3%; BTTS Yes (both teams score): 84.1%; BTTS No (at least one team does not score): 15.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ferencváros TC win | 54.1% | 1.85 |
| Draw | 15.7% | 6.37 |
| Torreense win | 30.2% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ferencváros TC expected goals | 2.21 |
| Torreense expected goals | 2.87 |
| Expected total goals | 5.07 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 95.6% |
| Under 1.5 | 4.4% |
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 73.5% |
| Under 3.5 | 26.5% |
| Over 4.5 | 56.7% |
| Under 4.5 | 43.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-2 | 8.26% |
| 2 | 2-1 | 7.83% |
| 3 | 3-1 | 5.76% |
| 4 | 2-2 | 5.74% |
| 5 | 4-2 | 4.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ferencváros TC win | 54.1% | 78.0% | 1.30 | -29.7% |
| Draw | 15.7% | 14.3% | 5.80 | -8.9% |
| Torreense win | 30.2% | 7.7% | 10.53 | +218.1% |
| Over 2.5 | 88.0% | 61.3% | 1.62 | +42.5% |
| Under 2.5 | 12.0% | 38.7% | 2.42 | -70.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | 4e761167a147b5282b086d0f801819d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 6.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | torreense |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2057 |
| Dc lambda away | 2.8684 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 84.1% |
| P btts no | 15.9% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 254.83 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 22.91 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.32 |
| Fair Over 3.5 odds | 1.36 |
| Fair Under 3.5 odds | 3.77 |
| Fair Over 4.5 odds | 1.76 |
| Fair Under 4.5 odds | 2.31 |
| Goal margin distribution | {"-1": 0.10343841853852319, "-10": 6.533971721108096e-05, "-11": 1.628721326886198e-05, "-12": 3.746255030006266e-06, "-13": 7.996019035158902e-07, "-14": 1.5915389441935498e-07, "-15": 2.9669167872597337e-08, "-16": 5.198409969593918e-09, "-17": 8.559946402817009e-10, "-18": 1.2895763287083048e-10, "-19": 1.460528840709658e-11, "-2": 0.0841040868948989, "-3": 0.056783105755414336, "-4": 0.03214303321896946, "-5": 0.015553557255457377, "-6": 0.006543210314253341, "-7": 0.002427830988415616, "-8": 0.0008042510145422076, "-9": 0.00024031321390752388, "0": 0.15706809662267335, "1": 0.2499932088404725, "10": 1.4794026395099898e-05, "11": 2.8356648144547447e-06, "12": 5.015386687431084e-07, "13": 8.231516927887259e-08, "14": 1.2598600331550765e-08, "15": 1.8059651578035177e-09, "16": 2.4331758697718117e-10, "17": 3.0808672944271554e-11, "18": 3.569011700270317e-12, "19": 3.108207677610656e-13, "2": 0.15578816378546198, "3": 0.08087894423908804, "4": 0.03520482262937848, "5": 0.013099176932154233, "6": 0.004237445526836864, "7": 0.0012090121670325442, "8": 0.0003079660275040261, "9": 7.075999895351777e-05} |
| Raw goal margin distribution | {"-1": 0.18057525087321877, "-10": 0.0001140653153255814, "-11": 2.8433029657689885e-05, "-12": 6.539938945668428e-06, "-13": 1.3958867156530542e-06, "-14": 2.778392672498327e-07, "-15": 5.179427051853683e-08, "-16": 9.075005183414177e-09, "-17": 1.4943330447132878e-09, "-18": 2.251248350147013e-10, "-19": 2.549684783903534e-11, "-2": 0.14682278407856048, "-3": 0.0991278067860805, "-4": 0.05611296430619697, "-5": 0.027152266469824216, "-6": 0.011422659595017806, "-7": 0.004238330361244362, "-8": 0.0014040027947828026, "-9": 0.00041952129105047464, "0": 0.17120376879317092, "1": 0.13931091754598843, "10": 8.244101513237902e-06, "11": 1.580199194157513e-06, "12": 2.7948684066846723e-07, "13": 4.587085310589681e-08, "14": 7.020681002192836e-09, "15": 1.006389990978678e-09, "16": 1.3559086846434068e-10, "17": 1.7168404358454282e-11, "18": 1.9888632055373335e-12, "19": 1.7320761051862817e-13, "2": 0.08681432643879021, "3": 0.045070504052324774, "4": 0.019618197491405195, "5": 0.007299631721916669, "6": 0.0023613538429017437, "7": 0.000673732678958677, "8": 0.00017161678136607534, "9": 3.94316326651024e-05} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 52.7% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 83.7% |
| Home training matches | 0 |
| Away training matches | 2 |
| P home draw | 69.8% |
| P draw away | 45.9% |
| P home away | 84.3% |
| Raw p home draw | 47.3% |
| Raw p draw away | 69.9% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 8.55, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 8.55, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.24 |
| Reference draw odds | 5.40 |
| Reference away odds | 9.25 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | -23.9% |
| Draw probability edge | +1.4% |
| Away probability edge | +22.5% |
| Over 2.5 probability edge | +26.7% |
| Under 2.5 probability edge | -26.7% |
| Raw edge prob home | -0.4789 |
| Raw ev home | -0.6082 |
| Raw edge prob draw | 0.0283 |
| Raw ev draw | -0.0070 |
| Raw edge prob away | 0.4506 |
| Raw ev away | 4.5538 |
| Market p home draw | 90.8% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 25.5% |
| Market draw away odds | 3.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.7% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.07 |
| Market reference dc draw away odds | 3.81 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.5% |
| Market btts yes odds | 2.07 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 2.07 |
| Market reference btts yes opposite odds | 1.81 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Jagiellonia Białystok vs Anderlecht

The model's most likely 1X2 outcome is **Jagiellonia Białystok win** at **42.1%**. Expected goals are 1.75 for Jagiellonia Białystok and 1.08 for Anderlecht (2.83 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.4%; Double Chance 1X: 66.2%; Double Chance X2: 57.9%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Jagiellonia Białystok win | 42.1% | 2.38 |
| Draw | 24.1% | 4.14 |
| Anderlecht win | 33.8% | 2.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Jagiellonia Białystok expected goals | 1.75 |
| Anderlecht expected goals | 1.08 |
| Expected total goals | 2.83 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.39% |
| 2 | 0-1 | 9.77% |
| 3 | 1-0 | 8.52% |
| 4 | 1-2 | 8.50% |
| 5 | 2-1 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Jagiellonia Białystok win | 42.1% | 30.5% | 3.18 | +33.9% |
| Draw | 24.1% | 25.9% | 3.57 | -13.8% |
| Anderlecht win | 33.8% | 43.6% | 2.28 | -23.0% |
| Over 2.5 | 52.6% | 54.6% | 1.79 | -5.8% |
| Under 2.5 | 47.4% | 45.4% | 2.12 | +0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 573ca8b5bb0abdb338c4004d610b1824 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | anderlecht |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7528 |
| Dc lambda away | 1.0803 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.44 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.16 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.62 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.21420841147495553, "-10": 5.885007877612118e-08, "-11": 5.698906958546336e-09, "-12": 5.069598916665145e-10, "-13": 4.169858100470572e-11, "-14": 3.188376056243009e-12, "-15": 2.2651875890704558e-13, "-16": 1.3675955260102426e-14, "-2": 0.08737026226249618, "-3": 0.027481406934191446, "-4": 0.006813813113522974, "-5": 0.0013882518989199537, "-6": 0.0002395046301416567, "-7": 3.57833242710937e-05, "-8": 4.710774373084984e-06, "-9": 5.539960549572561e-07, "0": 0.24148391596577123, "1": 0.19016033937011534, "10": 4.128452526128632e-06, "11": 6.486472601629523e-07, "12": 9.361973286987092e-08, "13": 1.2493722268524922e-08, "14": 1.5499471333694477e-09, "15": 1.7866039695168466e-10, "16": 1.7500826826684698e-11, "2": 0.12764084958486346, "3": 0.06513910465603301, "4": 0.026204134173793185, "5": 0.008662129015039481, "6": 0.0024246388540923574, "7": 0.000587747249803176, "8": 0.00012553909696032598, "9": 2.3953564179094568e-05} |
| Raw goal margin distribution | {"-1": 0.15158751311665875, "-10": 4.164606341537e-08, "-11": 4.032909479982128e-09, "-12": 3.587571034137589e-10, "-13": 2.9508571355686053e-11, "-14": 2.2562979386226646e-12, "-15": 1.6029909890352572e-13, "-16": 9.677976850204103e-15, "-2": 0.0618287614642552, "-3": 0.019447593609497618, "-4": 0.004821888074369043, "-5": 0.0009824154499243785, "-6": 0.00016948872835156447, "-7": 2.532255899734478e-05, "-8": 3.3336439365413475e-06, "-9": 3.9204288790138726e-07, "0": 0.22433760046389548, "1": 0.24247912398863267, "10": 5.264313028049058e-06, "11": 8.271094800468013e-07, "12": 1.193773154251304e-07, "13": 1.593111813464344e-08, "14": 1.9763838472996525e-09, "15": 2.2781520419979888e-10, "16": 2.2315826591747072e-11, "2": 0.16275865669477502, "3": 0.08306081639692842, "4": 0.033413673536704463, "5": 0.011045339224785674, "6": 0.00309172936521122, "7": 0.0007494540593010707, "8": 0.00016007864919727715, "9": 3.054390456912035e-05} |
| Unadjusted home-win probability | 53.7% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.5% |
| Raw p btts yes | 54.0% |
| Home training matches | 0 |
| Away training matches | 12 |
| P home draw | 66.2% |
| P draw away | 57.9% |
| P home away | 75.9% |
| Raw p home draw | 76.1% |
| Raw p draw away | 46.3% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:06Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.31, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:06Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.31, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.43 |
| Reference away odds | 2.13 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | +11.6% |
| Draw probability edge | -1.7% |
| Away probability edge | -9.9% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | 0.2316 |
| Raw ev home | 0.7070 |
| Raw edge prob draw | -0.0343 |
| Raw ev draw | -0.1991 |
| Raw edge prob away | -0.1974 |
| Raw ev away | -0.4554 |
| Market p home draw | 57.4% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:06Z |
| Market reference home draw last update utc | 2026-10-22T10:58:06Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.4% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:06Z |
| Market reference draw away last update utc | 2026-10-22T10:58:06Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:06Z |
| Market reference home away last update utc | 2026-10-22T10:58:06Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 79.5% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.6% |
| Market btts yes odds | 1.63 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:06Z |
| Market reference btts yes odds | 1.63 |
| Market reference btts yes opposite odds | 2.35 |
| Market reference btts yes last update utc | 2026-10-22T10:58:06Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Juventus vs Rennes

The model's most likely 1X2 outcome is **Juventus win** at **72.2%**. Expected goals are 2.03 for Juventus and 0.45 for Rennes (2.48 combined). The most likely exact score is 1-0 at 16.7%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 44.3%; Under 3.5 goals: 76.8%; Double Chance 1X: 89.9%; Double Chance X2: 27.8%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 31.4%; BTTS No (at least one team does not score): 68.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 72.2% | 1.39 |
| Draw | 17.7% | 5.64 |
| Rennes win | 10.1% | 9.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 2.03 |
| Rennes expected goals | 0.45 |
| Expected total goals | 2.48 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 69.5% |
| Under 1.5 | 30.5% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.2% |
| Under 3.5 | 76.8% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.67% |
| 2 | 2-0 | 16.53% |
| 3 | 3-0 | 11.17% |
| 4 | 0-0 | 8.23% |
| 5 | 1-1 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 72.2% | 69.0% | 1.43 | +3.2% |
| Draw | 17.7% | 18.2% | 4.87 | -13.7% |
| Rennes win | 10.1% | 12.7% | 7.36 | -25.5% |
| Over 2.5 | 44.3% | 59.7% | 1.64 | -27.3% |
| Under 2.5 | 55.7% | 40.3% | 2.37 | +32.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | 953ffa67dff5e7704dd0f77fe48fe614 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | juventus |
| Matched away-team name | rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0274 |
| Dc lambda away | 0.4511 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 31.4% |
| P btts no | 68.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.15 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.31 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.70 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.08337729909886094, "-10": 1.1812970970250013e-11, "-11": 4.811081339441809e-13, "-12": 1.798013483498917e-14, "-13": 6.207827037138236e-16, "-14": 1.9915388828153393e-17, "-15": 5.966204037763029e-19, "-16": 1.6742525754763353e-20, "-17": 4.2157299024074345e-22, "-2": 0.01544438329809745, "-3": 0.0021643054376590683, "-4": 0.00023369445362263363, "-5": 2.0472173833298108e-05, "-6": 1.5068219491950713e-06, "-7": 9.555927490520293e-08, "-8": 5.3212424399041925e-09, "-9": 2.640419657810413e-10, "0": 0.17719861131272682, "1": 0.25350801180984295, "10": 2.8246699527924356e-05, "11": 5.170581165742465e-06, "12": 8.685157362880954e-07, "13": 1.3477596264507952e-07, "14": 1.943344123354392e-08, "15": 2.6166588823467634e-09, "16": 3.3003353488007704e-10, "17": 3.735063249858891e-11, "2": 0.22175552502893425, "3": 0.13967237411400088, "4": 0.06778419719504884, "5": 0.02668898755570519, "6": 0.008829135121379571, "7": 0.0025166171870437512, "8": 0.0006298620548727102, "9": 0.0001404731896734498} |
| Raw goal margin distribution | {"-1": 0.06181293128571102, "-10": 8.757711880284912e-12, "-11": 3.566762697509181e-13, "-12": 1.3329825397020901e-14, "-13": 4.602259730495959e-16, "-14": 1.476455311538966e-17, "-15": 4.423129127575877e-19, "-16": 1.2412306529638742e-20, "-17": 3.1253905510617336e-22, "-2": 0.011449910393757558, "-3": 0.0016045382225764418, "-4": 0.00017325266421139057, "-5": 1.5177333496091564e-05, "-6": 1.117103607481434e-06, "-7": 7.08442100819787e-08, "-8": 3.944977791885569e-09, "-9": 1.9575121842236e-10, "0": 0.17232250801515403, "1": 0.26442073132139565, "10": 2.9462630759741066e-05, "11": 5.393158359933036e-06, "12": 9.059025965842151e-07, "13": 1.4057764231092176e-07, "14": 2.0269989521749434e-08, "15": 2.729297785695831e-09, "16": 3.4424043654697216e-10, "17": 3.895845930108825e-11, "2": 0.2313014002361962, "3": 0.1456848288342172, "4": 0.07070209287031534, "5": 0.02783786420525739, "6": 0.009209201512265421, "7": 0.0026249496112700967, "8": 0.0006569756276814147, "9": 0.000146520116975098} |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 7.5% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.2% |
| Raw p btts yes | 31.1% |
| Home training matches | 10 |
| Away training matches | 18 |
| P home draw | 89.9% |
| P draw away | 27.8% |
| P home away | 82.3% |
| Raw p home draw | 92.5% |
| Raw p draw away | 24.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:45Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.88, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:45Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | +3.1% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -15.4% |
| Under 2.5 probability edge | +15.4% |
| Raw edge prob home | 0.0621 |
| Raw ev home | 0.0762 |
| Raw edge prob draw | -0.0098 |
| Raw ev draw | -0.1608 |
| Raw edge prob away | -0.0524 |
| Raw ev away | -0.4476 |
| Market p home draw | 85.8% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:57:45Z |
| Market reference home draw last update utc | 2026-10-22T10:57:53Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.4% |
| Market draw away odds | 2.98 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:57:45Z |
| Market reference draw away last update utc | 2026-10-22T10:57:53Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.7% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:57:45Z |
| Market reference home away last update utc | 2026-10-22T10:57:53Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.85 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 82.6% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.2% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:57:45Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.01 |
| Market reference btts yes last update utc | 2026-10-22T10:57:45Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Lech Poznań vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **71.6%**. Expected goals are 0.06 for Lech Poznań and 2.08 for Sunderland (2.14 combined). The most likely exact score is 0-2 at 21.2%. Goal-market probabilities: at least one goal: 83.6%; Over 2.5 goals: 30.5%; Under 3.5 goals: 85.9%; Double Chance 1X: 28.4%; Double Chance X2: 89.9%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 5.3%; BTTS No (at least one team does not score): 94.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lech Poznań win | 10.1% | 9.89 |
| Draw | 18.3% | 5.46 |
| Sunderland win | 71.6% | 1.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lech Poznań expected goals | 0.06 |
| Sunderland expected goals | 2.08 |
| Expected total goals | 2.14 |
| Over 0.5 | 83.6% |
| Under 0.5 | 16.4% |
| Over 1.5 | 53.9% |
| Under 1.5 | 46.1% |
| Over 2.5 | 30.5% |
| Under 2.5 | 69.5% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 21.20% |
| 2 | 0-1 | 20.43% |
| 3 | 0-0 | 16.35% |
| 4 | 0-3 | 14.71% |
| 5 | 1-0 | 9.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lech Poznań win | 10.1% | 19.4% | 4.71 | -52.4% |
| Draw | 18.3% | 23.5% | 3.94 | -27.9% |
| Sunderland win | 71.6% | 57.1% | 1.75 | +25.3% |
| Over 2.5 | 30.5% | 53.1% | 1.85 | -43.5% |
| Under 2.5 | 69.5% | 46.9% | 2.05 | +42.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | dc02d531f844fa790c5dcae1918efd22 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | lech poznan |
| Matched away-team name | sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.0583 |
| Dc lambda away | 2.0809 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 5.3% |
| P btts no | 94.7% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 6.12 |
| Fair Over 1.5 odds | 1.86 |
| Fair Under 1.5 odds | 2.17 |
| Fair Over 2.5 odds | 3.27 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.10 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.16 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.21695358355112707, "-10": 4.1535219507994465e-05, "-11": 7.85017346581228e-06, "-12": 1.3602372636718067e-06, "-13": 2.175885823354945e-07, "-14": 3.232297781755873e-08, "-15": 4.481822705911197e-09, "-16": 5.82619086577199e-10, "-17": 7.081141722757864e-11, "-2": 0.22069784226308933, "-3": 0.15156219146529007, "-4": 0.0783737166070131, "-5": 0.032486855614129395, "-6": 0.01123468976699906, "-7": 0.0033325694616696067, "-8": 0.0008653929255285721, "-9": 0.00019982078064781952, "0": 0.18308339697884915, "1": 0.0985455902396974, "10": 1.822119251529279e-19, "11": 9.642365083569771e-22, "12": 4.678030148060192e-24, "13": 2.095214454481036e-26, "14": 8.71460634211727e-29, "15": 3.383257965138877e-31, "16": 1.2314284392022208e-33, "17": 4.19055734849707e-36, "2": 0.0025633394877592644, "3": 4.928819881407049e-05, "4": 7.13619229735206e-07, "5": 8.2822399994021e-09, "6": 8.019462262412348e-11, "7": 6.660508773681313e-13, "8": 4.842677697928123e-15, "9": 3.130811405196761e-17} |
| Raw goal margin distribution | {"-1": 0.26090221867025365, "-10": 4.9949075489863986e-05, "-11": 9.440395685808615e-06, "-12": 1.6357827061487392e-06, "-13": 2.616658501760469e-07, "-14": 3.887069523626063e-08, "-15": 5.3897127142100936e-09, "-16": 7.00641168675631e-10, "-17": 8.51557995008021e-11, "-2": 0.2654049578702088, "-3": 0.18226438749052204, "-4": 0.09425000598519591, "-5": 0.03906777002072024, "-6": 0.013510518878298673, "-7": 0.004007653398439643, "-8": 0.00104069695736894, "-9": 0.0002402987964250539, "0": 0.1310391754227755, "1": 0.007998861188682121, "10": 1.4789985961580676e-20, "11": 7.826625183985167e-23, "12": 3.7971170196238754e-25, "13": 1.700667634254316e-27, "14": 7.073571356673925e-30, "15": 2.746161524105161e-32, "16": 9.995399210675315e-35, "17": 3.4014395217795384e-37, "2": 0.00020806407158535935, "3": 4.000680899012971e-06, "4": 5.79238619033279e-08, "5": 6.722623298052056e-10, "6": 6.509328858742854e-12, "7": 5.406277946794893e-14, "8": 3.9307600262005073e-16, "9": 2.541252812753826e-18} |
| Unadjusted home-win probability | 0.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 86.1% |
| Raw p over 1 5 | 63.0% |
| Raw p under 3 5 | 83.1% |
| Raw p btts yes | 4.9% |
| Home training matches | 2 |
| Away training matches | 2 |
| P home draw | 28.4% |
| P draw away | 89.9% |
| P home away | 81.7% |
| Raw p home draw | 13.9% |
| Raw p draw away | 99.2% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.1, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 4.40 |
| Reference draw odds | 3.70 |
| Reference away odds | 1.66 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:52Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:52Z |
| Home probability edge | -9.3% |
| Draw probability edge | -5.2% |
| Away probability edge | +14.5% |
| Over 2.5 probability edge | -22.6% |
| Under 2.5 probability edge | +22.6% |
| Raw edge prob home | -0.1859 |
| Raw ev home | -0.9613 |
| Raw edge prob draw | -0.1041 |
| Raw ev draw | -0.4837 |
| Raw edge prob away | 0.2900 |
| Raw ev away | 0.5063 |
| Market p home draw | 45.3% |
| Market home draw odds | 2.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:57:45Z |
| Market reference home draw last update utc | 2026-10-22T10:57:53Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.2% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:57:45Z |
| Market reference draw away last update utc | 2026-10-22T10:57:53Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:57:45Z |
| Market reference home away last update utc | 2026-10-22T10:57:53Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.10 |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 78.2% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.5% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.4% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:57:45Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-22T10:57:45Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Lillestrom vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.4%**. Expected goals are 0.69 for Lillestrom and 0.92 for Real Sociedad (1.62 combined). The most likely exact score is 0-1 at 26.0%. Goal-market probabilities: at least one goal: 85.3%; Over 2.5 goals: 24.2%; Under 3.5 goals: 91.5%; Double Chance 1X: 45.6%; Double Chance X2: 80.0%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 97.2%; BTTS Yes (both teams score): 27.9%; BTTS No (at least one team does not score): 72.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lillestrom win | 20.0% | 5.00 |
| Draw | 25.6% | 3.91 |
| Real Sociedad win | 54.4% | 1.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lillestrom expected goals | 0.69 |
| Real Sociedad expected goals | 0.92 |
| Expected total goals | 1.62 |
| Over 0.5 | 85.3% |
| Under 0.5 | 14.7% |
| Over 1.5 | 48.6% |
| Under 1.5 | 51.4% |
| Over 2.5 | 24.2% |
| Under 2.5 | 75.8% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.8% |
| Under 4.5 | 97.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 25.97% |
| 2 | 0-0 | 14.68% |
| 3 | 0-2 | 11.57% |
| 4 | 1-0 | 10.77% |
| 5 | 1-1 | 9.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lillestrom win | 20.0% | 13.2% | 6.49 | +29.7% |
| Draw | 25.6% | 17.7% | 5.07 | +29.7% |
| Real Sociedad win | 54.4% | 69.1% | 1.46 | -20.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 9be240eead573e6718f4ba21ed1a6472 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | lillestrøm |
| Matched away-team name | real sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6944 |
| Dc lambda away | 0.9220 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 27.9% |
| P btts no | 72.1% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.81 |
| Fair Over 1.5 odds | 2.06 |
| Fair Under 1.5 odds | 1.94 |
| Fair Over 2.5 odds | 4.13 |
| Fair Under 2.5 odds | 1.32 |
| Fair Over 3.5 odds | 11.75 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.23 |
| Fair Under 4.5 odds | 1.03 |
| Goal margin distribution | {"-1": 0.34903164626032385, "-10": 3.5280184775554756e-08, "-11": 2.9392032387207246e-09, "-12": 2.143869463083152e-10, "-2": 0.14243368881966825, "-3": 0.04162081890989467, "-4": 0.009301802110155018, "-5": 0.0016799043081012848, "-6": 0.00025430770838243187, "-7": 3.3120039410308846e-05, "-8": 3.783610124812381e-06, "-9": 3.848807778568339e-07, "0": 0.2557732973272921, "1": 0.1443118201172674, "10": 1.1281340618589976e-09, "11": 7.078492276142226e-11, "12": 3.888577574011373e-12, "2": 0.04399388465700347, "3": 0.00968214304474965, "4": 0.0016297059591533682, "5": 0.00022167054313976134, "6": 2.527343368729541e-05, "7": 2.479001869345585e-06, "8": 2.1329156077574914e-07, "9": 1.6340855846104027e-08} |
| Raw goal margin distribution | {"-1": 0.2546982246068198, "-10": 2.5744944684564e-08, "-11": 2.1448194015692074e-09, "-12": 1.5644419406852096e-10, "-2": 0.10393787513328298, "-3": 0.030371884030038928, "-4": 0.006787787034455407, "-5": 0.0012258734970513848, "-6": 0.00018557549873435985, "-7": 2.4168625759573373e-05, "-8": 2.761006893556423e-06, "-9": 2.808583458140448e-07, "0": 0.334919251908586, "1": 0.193395335091279, "10": 1.5118364160594567e-09, "11": 9.486037835107015e-11, "12": 5.211165394097744e-12, "2": 0.058957139188560666, "3": 0.012975245527493741, "4": 0.002184003568208117, "5": 0.0002970654027892094, "6": 3.38694652516331e-05, "7": 3.322163055142782e-06, "8": 2.858365505670194e-07, "9": 2.1898727972993254e-08} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 33.5% |
| Unadjusted away-win probability | 39.7% |
| Raw p over 1 5 | 47.4% |
| Raw p under 3 5 | 91.9% |
| Raw p btts yes | 29.5% |
| Home training matches | 2 |
| Away training matches | 22 |
| P home draw | 45.6% |
| P draw away | 80.0% |
| P home away | 74.4% |
| Raw p home draw | 60.3% |
| Raw p draw away | 73.2% |
| Raw p home away | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.18, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.19, "price": 5.18, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 6.10 |
| Reference draw odds | 4.70 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.55 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:52Z |
| Home probability edge | +6.8% |
| Draw probability edge | +7.9% |
| Away probability edge | -14.7% |
| Over 2.5 probability edge | -39.9% |
| Under 2.5 probability edge | +39.9% |
| Raw edge prob home | 0.1360 |
| Raw ev home | 0.7383 |
| Raw edge prob draw | 0.1583 |
| Raw ev draw | 0.6980 |
| Raw edge prob away | -0.2943 |
| Raw ev away | -0.4200 |
| Market p home draw | 33.8% |
| Market home draw odds | 2.87 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 85.2% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.9% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.87 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 85.1% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.4% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.27 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — NK Celje vs Salzburg

The model's most likely 1X2 outcome is **Salzburg win** at **44.1%**. Expected goals are 1.73 for NK Celje and 0.97 for Salzburg (2.70 combined). The most likely exact score is 0-1 at 14.4%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 49.6%; Under 3.5 goals: 73.4%; Double Chance 1X: 55.9%; Double Chance X2: 64.9%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NK Celje win | 35.1% | 2.85 |
| Draw | 20.9% | 4.79 |
| Salzburg win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NK Celje expected goals | 1.73 |
| Salzburg expected goals | 0.97 |
| Expected total goals | 2.70 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.40% |
| 2 | 1-2 | 11.14% |
| 3 | 1-1 | 9.91% |
| 4 | 1-0 | 7.66% |
| 5 | 0-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NK Celje win | 35.1% | 14.4% | 5.98 | +109.6% |
| Draw | 20.9% | 19.2% | 4.64 | -3.1% |
| Salzburg win | 44.1% | 66.4% | 1.53 | -32.6% |
| Over 2.5 | 49.6% | 60.5% | 1.63 | -19.2% |
| Under 2.5 | 50.4% | 39.5% | 2.40 | +21.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | e342a49042c35c6a3f3e8720324b3f3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | salzburg |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7273 |
| Dc lambda away | 0.9732 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.59 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 7.72 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.2914380473404835, "-10": 3.331057100852133e-08, "-11": 2.9104925926900407e-09, "-12": 2.3355419637043195e-10, "-13": 1.7325901136746664e-11, "-14": 1.1947290752436323e-12, "-15": 7.662249546836653e-14, "-16": 4.217573885929149e-15, "-2": 0.10917145508288414, "-3": 0.031348983054359195, "-4": 0.007064063611742761, "-5": 0.0013046216952849897, "-6": 0.00020369548098138045, "-7": 2.7512949257080465e-05, "-8": 3.2720364702622487e-06, "-9": 3.4743393131887455e-07, "0": 0.2089246418821184, "1": 0.1578472444220745, "10": 3.207949180036157e-06, "11": 4.974758848271302e-07, "12": 7.085220039088579e-08, "13": 9.328710848926285e-09, "14": 1.1417088448474703e-09, "15": 1.2995780198073028e-10, "16": 1.2696057989335979e-11, "2": 0.1067759490352543, "3": 0.05441867096623105, "4": 0.021764024592797047, "5": 0.007133938080896836, "6": 0.0019769071219882476, "7": 0.0004739168514915698, "8": 0.00010003299519816137, "9": 1.885200299729219e-05} |
| Raw goal margin distribution | {"-1": 0.14370517339098685, "-10": 1.642510793019368e-08, "-11": 1.4351346589865992e-09, "-12": 1.151632279720648e-10, "-13": 8.543227796549322e-12, "-14": 5.891089048937997e-13, "-15": 3.77817827748058e-14, "-16": 2.0796433138967005e-15, "-2": 0.053831347777675426, "-3": 0.015457868615879954, "-4": 0.0034832188021918634, "-5": 0.0006432958518677592, "-6": 0.00010044019537089305, "-7": 1.356635888678958e-05, "-8": 1.6134083129898621e-06, "-9": 1.7131618125261714e-07, "0": 0.22610765289023144, "1": 0.25067965201329095, "10": 5.094593745187515e-06, "11": 7.900491525845672e-07, "12": 1.1252147608526351e-07, "13": 1.481507008819482e-08, "14": 1.8131654877773426e-09, "15": 2.063879968017086e-10, "16": 2.01628062014e-11, "2": 0.16957253733219563, "3": 0.08642313364916003, "4": 0.03456378431759363, "5": 0.011329517484775868, "6": 0.0031395567988344703, "7": 0.000752634687099594, "8": 0.00015886394797662653, "9": 2.9939157749742962e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 21.7% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 50.6% |
| Home training matches | 0 |
| Away training matches | 12 |
| P home draw | 55.9% |
| P draw away | 64.9% |
| P home away | 79.1% |
| Raw p home draw | 78.3% |
| Raw p draw away | 44.3% |
| Raw p home away | 77.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 4.74, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.21, "price": 4.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 5.60 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.44 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | +20.6% |
| Draw probability edge | +1.7% |
| Away probability edge | -22.3% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | 0.4123 |
| Raw ev home | 2.3288 |
| Raw edge prob draw | 0.0344 |
| Raw ev draw | 0.0491 |
| Raw edge prob away | -0.4467 |
| Raw ev away | -0.6676 |
| Market p home draw | 36.7% |
| Market home draw odds | 2.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.7% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.6% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.65 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.3% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.34 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.4% |
| Market btts yes odds | 1.75 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — OFI Crete vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **62.7%**. Expected goals are 1.00 for OFI Crete and 1.23 for Bayer Leverkusen (2.23 combined). The most likely exact score is 0-1 at 20.6%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 41.5%; Under 3.5 goals: 80.7%; Double Chance 1X: 37.3%; Double Chance X2: 81.5%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 41.7%; BTTS No (at least one team does not score): 58.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| OFI Crete win | 18.5% | 5.41 |
| Draw | 18.9% | 5.30 |
| Bayer Leverkusen win | 62.7% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| OFI Crete expected goals | 1.00 |
| Bayer Leverkusen expected goals | 1.23 |
| Expected total goals | 2.23 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 65.5% |
| Under 1.5 | 34.5% |
| Over 2.5 | 41.5% |
| Under 2.5 | 58.5% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 20.62% |
| 2 | 0-2 | 12.12% |
| 3 | 1-2 | 12.09% |
| 4 | 1-1 | 8.67% |
| 5 | 0-0 | 6.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| OFI Crete win | 18.5% | 6.5% | 13.00 | +140.3% |
| Draw | 18.9% | 10.4% | 7.61 | +43.5% |
| Bayer Leverkusen win | 62.7% | 83.0% | 1.21 | -24.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | ffcb32a8a5597aacba7b654852d47b67 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | ofi crete |
| Matched away-team name | leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9970 |
| Dc lambda away | 1.2344 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.7% |
| P btts no | 58.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.36 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 11.92 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.35461357294492785, "-10": 4.027817598032511e-07, "-11": 4.4786648891888705e-08, "-12": 4.5709281696453736e-09, "-13": 4.297282546295787e-10, "-14": 3.482920216150082e-11, "-2": 0.1792987150320418, "-3": 0.06726460417160787, "-4": 0.019598786093171783, "-5": 0.004653149763840869, "-6": 0.0009306483886079446, "-7": 0.0001606470970750031, "-8": 2.4377611784909967e-05, "-9": 3.29902825791399e-06, "0": 0.18859846975683378, "1": 0.11818070854551596, "10": 1.9506336478729513e-08, "11": 1.7518406328584096e-09, "12": 1.444077610846675e-10, "13": 1.0965290921258727e-11, "14": 7.178106308567243e-13, "2": 0.04794708472899238, "3": 0.014528197362454405, "4": 0.003418963181548626, "5": 0.0006556203006994339, "6": 0.00010590856960345879, "7": 1.4765850461077091e-05, "8": 1.8097427737038957e-06, "9": 1.9781163881690227e-07} |
| Raw goal margin distribution | {"-1": 0.2392714262903929, "-10": 2.717723558958231e-07, "-11": 3.0219275788390354e-08, "-12": 3.084181165259109e-09, "-13": 2.8995419309138754e-10, "-14": 2.3500603229964258e-11, "-2": 0.12097974401113512, "-3": 0.04538601736346632, "-4": 0.013224055309360107, "-5": 0.003139659239467175, "-6": 0.0006279442872641004, "-7": 0.00010839477949851832, "-8": 1.6448512934485883e-05, "-9": 2.225981341007442e-06, "0": 0.2729746915501538, "1": 0.19452582506889057, "10": 3.210749236737613e-08, "11": 2.883535296835208e-09, "12": 2.376956376135385e-10, "13": 1.804890400328541e-11, "14": 1.1815185991785386e-12, "2": 0.07892105514804118, "3": 0.023913459425627653, "4": 0.005627624355583881, "5": 0.0010791531164018437, "6": 0.00017432584503454927, "7": 2.4304637187706745e-05, "8": 2.9788424062598003e-06, "9": 3.2559859153549886e-07} |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 42.3% |
| Raw p over 1 5 | 64.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 44.1% |
| Home training matches | 2 |
| Away training matches | 23 |
| P home draw | 37.3% |
| P draw away | 81.5% |
| P home away | 81.1% |
| Raw p home draw | 57.7% |
| Raw p draw away | 69.6% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 10.96, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.07, "price": 10.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 10.00 |
| Reference draw odds | 6.75 |
| Reference away odds | 1.17 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.35 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | +11.9% |
| Draw probability edge | +8.4% |
| Away probability edge | -20.4% |
| Over 2.5 probability edge | -32.2% |
| Under 2.5 probability edge | +32.2% |
| Raw edge prob home | 0.2388 |
| Raw ev home | 2.9555 |
| Raw edge prob draw | 0.1688 |
| Raw ev draw | 1.0773 |
| Raw edge prob away | -0.4076 |
| Raw ev away | -0.4885 |
| Market p home draw | 20.0% |
| Market home draw odds | 4.88 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 92.1% |
| Market draw away odds | 1.06 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.9% |
| Market home away odds | 1.11 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.88 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 89.5% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 49.8% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.84 |
| Market reference under 3 5 opposite odds | 1.83 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.5% |
| Market btts yes odds | 1.84 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.84 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Olympiakos Piraeus vs Sparta Prague

The model's most likely 1X2 outcome is **Olympiakos Piraeus win** at **54.9%**. Expected goals are 1.18 for Olympiakos Piraeus and 0.89 for Sparta Prague (2.06 combined). The most likely exact score is 1-0 at 19.8%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 35.6%; Under 3.5 goals: 84.1%; Double Chance 1X: 79.0%; Double Chance X2: 45.1%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 38.8%; BTTS No (at least one team does not score): 61.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Olympiakos Piraeus win | 54.9% | 1.82 |
| Draw | 24.2% | 4.14 |
| Sparta Prague win | 21.0% | 4.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Olympiakos Piraeus expected goals | 1.18 |
| Sparta Prague expected goals | 0.89 |
| Expected total goals | 2.06 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 35.6% |
| Under 2.5 | 64.4% |
| Over 3.5 | 15.9% |
| Under 3.5 | 84.1% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.82% |
| 2 | 2-0 | 11.17% |
| 3 | 1-1 | 10.66% |
| 4 | 0-0 | 10.20% |
| 5 | 2-1 | 9.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Olympiakos Piraeus win | 54.9% | 66.5% | 1.51 | -17.1% |
| Draw | 24.2% | 19.8% | 4.52 | +9.2% |
| Sparta Prague win | 21.0% | 13.7% | 6.41 | +34.4% |
| Over 2.5 | 35.6% | 54.5% | 1.78 | -36.6% |
| Under 2.5 | 64.4% | 45.5% | 2.13 | +37.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 5290ae078657c841a4e1d4ebb626825a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | olympiacos |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 0/100 |
| Dc lambda home | 1.1776 |
| Dc lambda away | 0.8858 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.8% |
| P btts no | 61.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.80 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.81 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.30 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.05 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.14037647617693094, "-10": 8.497524461176311e-09, "-11": 6.788764482662739e-10, "-12": 4.964318738335138e-11, "-13": 3.131260273678666e-12, "-2": 0.05169154553589873, "-3": 0.014095880713605579, "-4": 0.002971541186144348, "-5": 0.0005091399348992603, "-6": 7.33741367130621e-05, "-7": 9.117241024485819e-06, "-8": 9.952186153408131e-07, "-9": 9.683650386388654e-08, "0": 0.24154419606227573, "1": 0.3158924466210786, "10": 2.502115656401311e-07, "11": 2.657481234739445e-08, "12": 2.583471229545282e-09, "13": 2.1663451284736832e-10, "2": 0.1559977794384715, "3": 0.05655299660827851, "4": 0.015849284730502077, "5": 0.003610186047431982, "6": 0.0006916715818740738, "7": 0.00011425754050323676, "8": 1.6580760006871368e-05, "9": 2.1448135824370145e-06} |
| Raw goal margin distribution | {"-1": 0.18896126759046314, "-10": 1.1438547520889539e-08, "-11": 9.138379712568108e-10, "-12": 6.682486888590633e-11, "-13": 4.2150004515301924e-12, "-2": 0.06958217098897915, "-3": 0.01897451453397144, "-4": 0.004000002026859401, "-5": 0.0006853550544909645, "-6": 9.876918312282485e-05, "-7": 1.2272750163233786e-05, "-8": 1.3396672733642134e-06, "-9": 1.3035195794547147e-07, "0": 0.2851051978570618, "1": 0.24902778996011274, "10": 1.9724951919652445e-07, "11": 2.0949746846636897e-08, "12": 2.036630307564522e-09, "13": 1.7077968954470714e-10, "2": 0.12297787638729653, "3": 0.044582477079214866, "4": 0.012494481558844993, "5": 0.002846021366934549, "6": 0.0005452661095721884, "7": 9.00727545154937e-05, "8": 1.3071126152386698e-05, "9": 1.6908229114810418e-06} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 28.2% |
| Raw p over 1 5 | 60.4% |
| Raw p under 3 5 | 84.6% |
| Raw p btts yes | 40.0% |
| Home training matches | 24 |
| Away training matches | 0 |
| P home draw | 79.0% |
| P draw away | 45.1% |
| P home away | 75.8% |
| Raw p home draw | 71.8% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.04, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.19, "price": 5.04, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.44 |
| Reference draw odds | 4.25 |
| Reference away odds | 5.90 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | -11.6% |
| Draw probability edge | +4.4% |
| Away probability edge | +7.3% |
| Over 2.5 probability edge | -18.9% |
| Under 2.5 probability edge | +18.9% |
| Raw edge prob home | -0.2323 |
| Raw ev home | -0.3468 |
| Raw edge prob draw | 0.0871 |
| Raw ev draw | 0.2887 |
| Raw edge prob away | 0.1452 |
| Raw ev away | 0.8096 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.1% |
| Market draw away odds | 2.69 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.69 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 78.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.3% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.1% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.93 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Omonoia FC vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **67.6%**. Expected goals are 0.59 for Omonoia FC and 1.48 for Benfica (2.08 combined). The most likely exact score is 0-1 at 21.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 36.4%; Under 3.5 goals: 83.6%; Double Chance 1X: 32.4%; Double Chance X2: 87.6%; Double Chance 12 (either team wins): 80.0%; Under 4.5 goals: 93.5%; BTTS Yes (both teams score): 32.6%; BTTS No (at least one team does not score): 67.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Omonoia FC win | 12.4% | 8.06 |
| Draw | 20.0% | 5.00 |
| Benfica win | 67.6% | 1.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Omonoia FC expected goals | 0.59 |
| Benfica expected goals | 1.48 |
| Expected total goals | 2.08 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 36.4% |
| Under 2.5 | 63.6% |
| Over 3.5 | 16.4% |
| Under 3.5 | 83.6% |
| Over 4.5 | 6.5% |
| Under 4.5 | 93.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 21.76% |
| 2 | 0-2 | 15.67% |
| 3 | 0-0 | 9.55% |
| 4 | 1-2 | 9.28% |
| 5 | 1-1 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Omonoia FC win | 12.4% | 9.5% | 8.99 | +11.6% |
| Draw | 20.0% | 14.8% | 5.81 | +16.2% |
| Benfica win | 67.6% | 75.6% | 1.32 | -10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 86b70325b671e4bdf5b970aa6cd85bb3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | benfica |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5920 |
| Dc lambda away | 1.4830 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 32.6% |
| P btts no | 67.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.48 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.74 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 6.09 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.49 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.32499365946007674, "-10": 2.187959218258009e-06, "-11": 2.930379349825058e-07, "-12": 3.6012811150478595e-08, "-13": 4.088453672032748e-09, "-14": 4.3063577936088815e-10, "-15": 4.022117936050526e-11, "-2": 0.2079137245930438, "-3": 0.0960392616529078, "-4": 0.034149145773480064, "-5": 0.009846266167278765, "-6": 0.0023845764819822282, "-7": 0.0004974820501023838, "-8": 9.112008513946047e-05, "-9": 1.4870612084001576e-05, "0": 0.19995348770282315, "1": 0.09537640606309458, "10": 1.607396720299279e-10, "11": 8.594508726090132e-12, "12": 4.2166503656172523e-13, "13": 1.911098210474152e-14, "14": 8.036138107353511e-16, "15": 2.9964389856932454e-17, "2": 0.023673374068381603, "3": 0.004365552055968489, "4": 0.0006197029445864764, "5": 7.133269684042908e-05, "6": 6.8967055568925455e-06, "7": 5.74408953166081e-07, "8": 4.200212457085392e-08, "9": 2.7365245151905083e-09} |
| Raw goal margin distribution | {"-1": 0.2863179373349481, "-10": 1.927582130018673e-06, "-11": 2.5816508926504287e-07, "-12": 3.172712299485552e-08, "-13": 3.601909108659734e-09, "-14": 3.7938816496936507e-10, "-15": 3.543467626664118e-11, "-2": 0.18317104668443399, "-3": 0.08461015314980272, "-4": 0.030085242265516777, "-5": 0.008674515755629546, "-6": 0.0021008010460045576, "-7": 0.00043827942576822273, "-8": 8.027638099234998e-05, "-9": 1.3100941679517644e-05, "0": 0.25145275621348034, "1": 0.1176154388259324, "10": 1.982195371256686e-10, "11": 1.0598500793201288e-11, "12": 5.199851866923136e-13, "13": 2.3567113077806247e-14, "14": 9.909934217241503e-16, "15": 3.695122313418904e-17, "2": 0.02919332353224979, "3": 0.005383473145764345, "4": 0.000764199834926093, "5": 8.79654286404347e-05, "6": 8.504818791248595e-06, "7": 7.083445883616159e-07, "8": 5.1795811112387957e-08, "9": 3.374603269273266e-09} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 60.8% |
| Raw p under 3 5 | 84.3% |
| Raw p btts yes | 34.0% |
| Home training matches | 0 |
| Away training matches | 8 |
| P home draw | 32.4% |
| P draw away | 87.6% |
| P home away | 80.0% |
| Raw p home draw | 40.5% |
| Raw p draw away | 84.7% |
| Raw p home away | 74.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.31, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.31, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 8.00 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | +2.9% |
| Draw probability edge | +5.1% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | -28.2% |
| Under 2.5 probability edge | +28.2% |
| Raw edge prob home | 0.0579 |
| Raw ev home | 0.3760 |
| Raw edge prob draw | 0.1030 |
| Raw ev draw | 0.4609 |
| Raw edge prob away | -0.1609 |
| Raw ev away | -0.2139 |
| Market p home draw | 27.0% |
| Market home draw odds | 3.60 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.2% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.8% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.60 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.1% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.23 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.4% |
| Market btts yes odds | 1.88 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.88 |
| Market reference btts yes opposite odds | 1.98 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — SK Sturm Graz vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **40.0%**. Expected goals are 1.80 for SK Sturm Graz and 1.29 for Marseille (3.09 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.5%; Double Chance 1X: 60.0%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SK Sturm Graz win | 36.7% | 2.73 |
| Draw | 23.3% | 4.29 |
| Marseille win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SK Sturm Graz expected goals | 1.80 |
| Marseille expected goals | 1.29 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.5% |
| Under 3.5 | 63.5% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.62% |
| 2 | 1-2 | 9.72% |
| 3 | 0-1 | 9.12% |
| 4 | 2-1 | 6.99% |
| 5 | 2-2 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SK Sturm Graz win | 36.7% | 23.5% | 4.27 | +56.5% |
| Draw | 23.3% | 24.6% | 3.81 | -11.2% |
| Marseille win | 40.0% | 51.9% | 1.85 | -25.9% |
| Over 2.5 | 58.8% | 58.7% | 1.72 | +1.1% |
| Under 2.5 | 41.2% | 41.3% | 2.22 | -8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | fcbdc440ac1bfd04e900e145e84ffaca |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | marseille |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7968 |
| Dc lambda away | 1.2928 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.51 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.234309799038666, "-10": 2.8696968783568436e-07, "-11": 3.315265682466612e-08, "-12": 3.5199737430352564e-09, "-13": 3.4568619919775537e-10, "-14": 3.156276287814713e-11, "-15": 2.6715537552370037e-12, "-16": 1.8850006701942193e-13, "-2": 0.11026028325889432, "-3": 0.04045025778352811, "-4": 0.011797466522506706, "-5": 0.0028415172064687622, "-6": 0.0005813573056159488, "-7": 0.00010322008402245875, "-8": 1.6171904582194782e-05, "-9": 2.265772204651348e-06, "0": 0.2330404345467208, "1": 0.16697561004799782, "10": 3.991879537553868e-06, "11": 6.40928972667401e-07, "12": 9.457604610631328e-08, "13": 1.2908445199749168e-08, "14": 1.638011967292301e-09, "15": 1.9268865218667417e-10, "16": 1.889530448591571e-11, "2": 0.11019431609761988, "3": 0.0561838566917564, "4": 0.022773468027236902, "5": 0.0076232624580903205, "6": 0.0021676236478375605, "7": 0.000534878471490039, "8": 0.00011646682709141076, "9": 2.2678142644960475e-05} |
| Raw goal margin distribution | {"-1": 0.16471742694488611, "-10": 2.0173679797177743e-07, "-11": 2.330598357794107e-08, "-12": 2.4745060609720727e-09, "-13": 2.4301391361278605e-10, "-14": 2.218830415923847e-11, "-15": 1.8780753613935273e-12, "-16": 1.3251364708504573e-13, "-2": 0.07751186773721871, "-3": 0.02843612349418042, "-4": 0.00829350005005579, "-5": 0.0019975579544239115, "-6": 0.0004086883259238704, "-7": 7.256267863730553e-05, "-8": 1.136868591286597e-05, "-9": 1.5928150214999085e-06, "0": 0.22047020310960838, "1": 0.2268623229781891, "10": 5.423588898272323e-06, "11": 8.708016431954001e-07, "12": 1.2849626069102552e-07, "13": 1.753812945022305e-08, "14": 2.2254938901506996e-09, "15": 2.617974878728667e-10, "16": 2.567220846100113e-11, "2": 0.1497161083688382, "3": 0.07633450322057002, "4": 0.030941296500988178, "5": 0.010357387102329847, "6": 0.002945053687478841, "7": 0.0007267155515609287, "8": 0.0001582382896296138, "9": 3.081178215062409e-05} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 22.0% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| Home training matches | 0 |
| Away training matches | 16 |
| P home draw | 60.0% |
| P draw away | 63.3% |
| P home away | 76.7% |
| Raw p home draw | 71.9% |
| Raw p draw away | 50.2% |
| Raw p home away | 78.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.98, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.21, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.17, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.38, "price": 3.17, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.80 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.83 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | +13.1% |
| Draw probability edge | -1.3% |
| Away probability edge | -11.9% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.2630 |
| Raw ev home | 1.1268 |
| Raw edge prob draw | -0.0251 |
| Raw ev draw | -0.1600 |
| Raw edge prob away | -0.2378 |
| Raw ev away | -0.4793 |
| Market p home draw | 48.0% |
| Market home draw odds | 2.02 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 77.5% |
| Market draw away odds | 1.25 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.02 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.4% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — TSG Hoffenheim vs Lyon

The model's most likely 1X2 outcome is **Lyon win** at **40.5%**. Expected goals are 1.08 for TSG Hoffenheim and 1.60 for Lyon (2.67 combined). The most likely exact score is 1-0 at 11.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.6%; Double Chance 1X: 59.5%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 36.7% | 2.73 |
| Draw | 22.8% | 4.38 |
| Lyon win | 40.5% | 2.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.08 |
| Lyon expected goals | 1.60 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.4% |
| Under 3.5 | 72.6% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.22% |
| 2 | 1-1 | 10.84% |
| 3 | 0-1 | 9.39% |
| 4 | 2-1 | 8.94% |
| 5 | 1-2 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 36.7% | 47.1% | 2.09 | -23.3% |
| Draw | 22.8% | 21.9% | 4.08 | -6.8% |
| Lyon win | 40.5% | 30.9% | 3.22 | +30.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | b3c60081286aa25692de7e0a482b6c01 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | lyon |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0775 |
| Dc lambda away | 1.5961 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.49 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.65 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.62 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19600156240850242, "-10": 1.928843067399062e-06, "-11": 2.763125474302328e-07, "-12": 3.6354359367770795e-08, "-13": 4.421025914927137e-09, "-14": 4.97231348868415e-10, "-15": 4.746627637577748e-11, "-2": 0.12176703087823385, "-3": 0.057203351066469774, "-4": 0.0211054242501917, "-5": 0.006385192313436648, "-6": 0.0016336150149146968, "-7": 0.0003616340439666739, "-8": 7.049734343855852e-05, "-9": 1.2271322449235378e-05, "0": 0.22849718672423883, "1": 0.23126304636735862, "10": 6.551321637967467e-08, "11": 6.335730745778698e-09, "12": 5.62751524257691e-10, "13": 4.620056886828544e-11, "14": 3.5078970772335027e-12, "15": 2.2606721432663108e-13, "2": 0.09586258074970361, "3": 0.030402195663409903, "4": 0.0075725411747963045, "5": 0.0015466271065434193, "6": 0.00026713170133898525, "7": 3.992170673275609e-05, "8": 5.253837332532512e-06, "9": 6.173896105958179e-07} |
| Raw goal margin distribution | {"-1": 0.2421656719869944, "-10": 2.383142112921682e-06, "-11": 3.413922465955707e-07, "-12": 4.491687595634696e-08, "-13": 5.462307026557682e-09, "-14": 6.143438973244427e-10, "-15": 5.864597493005452e-11, "-2": 0.15044673366955488, "-3": 0.07067641594635925, "-4": 0.02607636991926635, "-5": 0.00788909214982105, "-6": 0.0020183792057246394, "-7": 0.00044680945495751263, "-8": 8.710153295367752e-05, "-9": 1.5161578359741e-05, "0": 0.2377049781022356, "1": 0.1654123934038927, "10": 4.685875279760488e-08, "11": 4.5316724962497255e-09, "12": 4.025116765576429e-10, "13": 3.3045256443543544e-11, "14": 2.5090461293932522e-12, "15": 1.6169604084743562e-13, "2": 0.06856633244592814, "3": 0.021745367573467532, "4": 0.00541630917497668, "5": 0.0011062350661518972, "6": 0.00019106768144161267, "7": 2.8554259589505827e-05, "8": 3.7578412175218453e-06, "9": 4.415919220796259e-07} |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 72.0% |
| Raw p btts yes | 52.0% |
| Home training matches | 0 |
| Away training matches | 24 |
| P home draw | 59.5% |
| P draw away | 63.3% |
| P home away | 77.2% |
| Raw p home draw | 50.0% |
| Raw p draw away | 73.8% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.45, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.58, "price": 2.45, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 4.05 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | -10.4% |
| Draw probability edge | +0.9% |
| Away probability edge | +9.5% |
| Over 2.5 probability edge | -17.3% |
| Under 2.5 probability edge | +17.3% |
| Raw edge prob home | -0.2090 |
| Raw ev home | -0.4514 |
| Raw edge prob draw | 0.0184 |
| Raw ev draw | -0.0302 |
| Raw edge prob away | 0.1906 |
| Raw ev away | 0.6094 |
| Market p home draw | 70.2% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.5% |
| Market draw away odds | 1.81 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.81 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.8% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.08 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.8% |
| Market btts yes odds | 1.44 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.90 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Union Saint-Gilloise vs Hapoel Be'er Sheva

The model's most likely 1X2 outcome is **Union Saint-Gilloise win** at **66.0%**. Expected goals are 1.66 for Union Saint-Gilloise and 0.77 for Hapoel Be'er Sheva (2.43 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 45.5%; Under 3.5 goals: 76.5%; Double Chance 1X: 85.5%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 41.9%; BTTS No (at least one team does not score): 58.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Saint-Gilloise win | 66.0% | 1.52 |
| Draw | 19.5% | 5.12 |
| Hapoel Be'er Sheva win | 14.5% | 6.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Saint-Gilloise expected goals | 1.66 |
| Hapoel Be'er Sheva expected goals | 0.77 |
| Expected total goals | 2.43 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 70.2% |
| Under 1.5 | 29.8% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.90% |
| 2 | 2-0 | 13.50% |
| 3 | 2-1 | 10.44% |
| 4 | 1-1 | 9.06% |
| 5 | 3-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Saint-Gilloise win | 66.0% | 72.9% | 1.38 | -8.9% |
| Draw | 19.5% | 16.0% | 5.24 | +2.4% |
| Hapoel Be'er Sheva win | 14.5% | 11.1% | 8.21 | +18.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T16:45:00+00:00 |
| Fixture id | 382e017f27a6fbffbc48f736ca1680f2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | union sg |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 0/100 |
| Dc lambda home | 1.6595 |
| Dc lambda away | 0.7734 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.38 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.48 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.10342879923887854, "-10": 1.687878637304692e-09, "-11": 1.1753982301973358e-10, "-12": 7.514047498606799e-12, "-13": 4.438750033867493e-13, "-14": 2.429639904677394e-14, "-15": 1.153986060420886e-15, "-2": 0.03200836653381596, "-3": 0.007496523391615118, "-4": 0.0013653332755132906, "-5": 0.0002027671566628108, "-6": 2.5378298218520594e-05, "-7": 2.7421827105908473e-06, "-8": 2.6052156729562855e-07, "-9": 2.2076302475389607e-08, "0": 0.19549064954249126, "1": 0.29826957496993184, "10": 4.805978005237154e-06, "11": 7.181126411123148e-07, "12": 9.850277201086654e-08, "13": 1.2485391988139181e-08, "14": 1.4663930111979214e-09, "15": 1.4944314892073995e-10, "2": 0.20284684541921916, "3": 0.10193694738204061, "4": 0.03983615150044836, "5": 0.012694140146301176, "6": 0.00340906397150278, "7": 0.0007903801410717197, "8": 0.00016112031067544235, "9": 2.9295432984755888e-05} |
| Raw goal margin distribution | {"-1": 0.12747592989248077, "-10": 2.080309356962828e-09, "-11": 1.4486775781117167e-10, "-12": 9.261058807507783e-12, "-13": 5.470756619930321e-13, "-14": 2.994529651623434e-14, "-15": 1.422287092353833e-15, "-2": 0.03945029158478116, "-3": 0.009239460356682301, "-4": 0.001682772401787486, "-5": 0.00024991039282538604, "-6": 3.127873656371839e-05, "-7": 3.3797384629817137e-06, "-8": 3.210926675398658e-07, "-9": 2.720902889086348e-08, "0": 0.23092289128377083, "1": 0.2670698537948507, "10": 4.303261046083383e-06, "11": 6.429963166354923e-07, "12": 8.819914308048893e-08, "13": 1.1179389695311283e-08, "14": 1.3130047446036e-09, "15": 1.3381103297890027e-10, "2": 0.18162857326067802, "3": 0.0912740953761691, "4": 0.03566919340682593, "5": 0.011366302289684639, "6": 0.003052467609337367, "7": 0.00070770446077062, "8": 0.00014426673528404347, "9": 2.6231059620761924e-05} |
| Unadjusted home-win probability | 59.1% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 77.2% |
| Raw p btts yes | 43.0% |
| Home training matches | 28 |
| Away training matches | 0 |
| P home draw | 85.5% |
| P draw away | 34.0% |
| P home away | 80.5% |
| Raw p home draw | 82.2% |
| Raw p draw away | 40.9% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.67, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:03Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.67, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.32 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.90 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:51Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:51Z |
| Home probability edge | -6.9% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1381 |
| Raw ev home | -0.1845 |
| Raw edge prob draw | 0.0709 |
| Raw ev draw | 0.2100 |
| Raw edge prob away | 0.0672 |
| Raw ev away | 0.4625 |
| Market p home draw | 88.5% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:03Z |
| Market reference home draw last update utc | 2026-10-22T10:58:03Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.8% |
| Market draw away odds | 3.27 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:03Z |
| Market reference draw away last update utc | 2026-10-22T10:58:03Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.8% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:03Z |
| Market reference home away last update utc | 2026-10-22T10:58:03Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 3.27 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.8% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.1% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:03Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-22T10:58:03Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Viktoria Plzeň vs PFC Levski Sofia

The model's most likely 1X2 outcome is **Viktoria Plzeň win** at **53.6%**. Expected goals are 1.33 for Viktoria Plzeň and 0.84 for PFC Levski Sofia (2.17 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 37.9%; Under 3.5 goals: 82.2%; Double Chance 1X: 78.3%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 92.8%; BTTS Yes (both teams score): 40.6%; BTTS No (at least one team does not score): 59.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viktoria Plzeň win | 53.6% | 1.87 |
| Draw | 24.8% | 4.04 |
| PFC Levski Sofia win | 21.7% | 4.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viktoria Plzeň expected goals | 1.33 |
| PFC Levski Sofia expected goals | 0.84 |
| Expected total goals | 2.17 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 63.7% |
| Under 1.5 | 36.3% |
| Over 2.5 | 37.9% |
| Under 2.5 | 62.1% |
| Over 3.5 | 17.8% |
| Under 3.5 | 82.2% |
| Over 4.5 | 7.2% |
| Under 4.5 | 92.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.32% |
| 2 | 1-1 | 11.14% |
| 3 | 2-0 | 11.09% |
| 4 | 0-0 | 9.88% |
| 5 | 2-1 | 9.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viktoria Plzeň win | 53.6% | 58.2% | 1.71 | -8.4% |
| Draw | 24.8% | 22.6% | 4.08 | +1.0% |
| PFC Levski Sofia win | 21.7% | 19.2% | 4.84 | +4.9% |
| Over 2.5 | 37.9% | 55.2% | 1.77 | -33.0% |
| Under 2.5 | 62.1% | 44.8% | 2.14 | +33.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-22T19:00:00+00:00 |
| Fixture id | 410fd021774146ae969af3713990ed87 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T10:57:52Z |
| Market best draw last update utc | 2026-10-22T10:57:52Z |
| Market best away last update utc | 2026-10-22T10:57:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | viktoria plzen |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 0/100 |
| Dc lambda home | 1.3344 |
| Dc lambda away | 0.8395 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.12 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.75 |
| Fair Over 2.5 odds | 2.64 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.61 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.90 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.14902254723705916, "-10": 5.405767322587121e-09, "-11": 4.0912317601616156e-10, "-12": 2.841741692976777e-11, "-13": 1.8189942469401536e-12, "-14": 1.0099670762348261e-13, "-2": 0.05135060572697618, "-3": 0.013200909254842184, "-4": 0.002628567328276295, "-5": 0.0004258538812486679, "-6": 5.806708449487059e-05, "-7": 6.829570835470124e-06, "-8": 7.058522318386133e-07, "-9": 6.504093776596365e-08, "0": 0.24751103163467109, "1": 0.28532484324220553, "10": 6.797090320992559e-07, "11": 8.176365225041919e-08, "12": 9.026747773947455e-09, "13": 9.183718050333839e-10, "14": 8.10466262479455e-11, "2": 0.15852114427498706, "3": 0.06477180227517247, "4": 0.0204994283022556, "5": 0.005278660873267654, "6": 0.0011440201686780996, "7": 0.0002138639490478002, "8": 3.513164360616953e-05, "9": 5.145315127866657e-06} |
| Raw goal margin distribution | {"-1": 0.16630649284454124, "-10": 6.032739482858081e-09, "-11": 4.565741346269749e-10, "-12": 3.171332817021866e-11, "-13": 2.0299649906788442e-12, "-14": 1.1271051626159549e-13, "-2": 0.057306355999345714, "-3": 0.014731978222325642, "-4": 0.002933434045225245, "-5": 0.0004752453019209265, "-6": 6.480182597260065e-05, "-7": 7.6216786945240654e-06, "-8": 7.877184447588052e-07, "-9": 7.258452128033124e-08, "0": 0.26885078355977676, "1": 0.26057707108539047, "10": 6.20754178858375e-07, "11": 7.467184694664915e-08, "12": 8.24380894994517e-09, "13": 8.387164342358394e-10, "14": 7.401701250078193e-11, "2": 0.14477174511304727, "3": 0.059153792337175125, "4": 0.018721401632006848, "5": 0.0048208139676134245, "6": 0.0010447930906727916, "7": 0.00019531436807388255, "8": 3.208448549129808e-05, "9": 4.699034022399211e-06} |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 63.3% |
| Raw p under 3 5 | 82.4% |
| Raw p btts yes | 41.2% |
| Home training matches | 24 |
| Away training matches | 0 |
| P home draw | 78.3% |
| P draw away | 46.4% |
| P home away | 75.2% |
| Raw p home draw | 75.8% |
| Raw p draw away | 51.1% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:57:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.24, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:57:52Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:04Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.69, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:58:04Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.3, "price": 3.69, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.63 |
| Reference draw odds | 3.83 |
| Reference away odds | 4.45 |
| Market reference 1x2 last update utc | 2026-10-22T10:58:03Z |
| Market reference home last update utc | 2026-10-22T10:58:03Z |
| Market reference draw last update utc | 2026-10-22T10:58:03Z |
| Market reference away last update utc | 2026-10-22T10:58:03Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market reference under 2 5 last update utc | 2026-10-22T10:57:53Z |
| Market best over 2 5 last update utc | 2026-10-22T10:57:31Z |
| Market best under 2 5 last update utc | 2026-10-22T10:57:31Z |
| Home probability edge | -4.6% |
| Draw probability edge | +2.1% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -17.4% |
| Under 2.5 probability edge | +17.4% |
| Raw edge prob home | -0.0929 |
| Raw ev home | -0.1633 |
| Raw edge prob draw | 0.0427 |
| Raw ev draw | 0.0969 |
| Raw edge prob away | 0.0503 |
| Raw ev away | 0.1704 |
| Market p home draw | 80.1% |
| Market home draw odds | 1.21 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:58:04Z |
| Market reference home draw last update utc | 2026-10-22T10:58:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.5% |
| Market draw away odds | 2.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:58:04Z |
| Market reference draw away last update utc | 2026-10-22T10:58:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:58:04Z |
| Market reference home away last update utc | 2026-10-22T10:58:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.23 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 79.7% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market reference over 1 5 last update utc | 2026-10-22T10:57:53Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:57:52Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.65 |
| Market reference under 3 5 last update utc | 2026-10-22T10:57:53Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:58:04Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-22T10:58:04Z |
| Market btts yes bookmakers | 2 |

</details>


---
