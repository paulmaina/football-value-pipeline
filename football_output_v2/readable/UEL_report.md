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
| Training as of utc | 2026-10-22T15:07:38.857486+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 997.396 |
| Base scoring parameter | 0.052 |
| Home-advantage parameter | 0.290 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-15', 'verified_at_utc': '2026-10-22T09:02:22.673333+00:00', 'official_source_health': {'2025': {'status': 'HTTP_403_USING_REVIEWED_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}, '2026': {'status': 'HTTP_403_USING_REVIEWED_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'f70b1b52c2d0762cfe38cf1abbccd3cfaa1bcfd0a6bc8ebd090533e34ae1ba20'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 17.00 |
| Over 1 5 in window quote fixtures | 17 |
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

The model's most likely 1X2 outcome is **Besiktas JK win** at **42.6%**. Expected goals are 1.80 for Besiktas JK and 1.71 for Crystal Palace (3.51 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.6%; Under 3.5 goals: 53.4%; Double Chance 1X: 65.9%; Double Chance X2: 57.4%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 72.7%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 42.6% | 2.35 |
| Draw | 23.3% | 4.28 |
| Crystal Palace win | 34.1% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.80 |
| Crystal Palace expected goals | 1.71 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 46.6% |
| Under 3.5 | 53.4% |
| Over 4.5 | 27.3% |
| Under 4.5 | 72.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.58% |
| 2 | 2-1 | 8.55% |
| 3 | 2-2 | 7.76% |
| 4 | 1-2 | 7.15% |
| 5 | 1-0 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Besiktas JK win | 42.6% | 43.9% | 2.22 | -5.4% |
| Draw | 23.3% | 25.4% | 3.77 | -12.0% |
| Crystal Palace win | 34.1% | 30.7% | 3.14 | +7.0% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | crystal palace |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8022 |
| Dc lambda away | 1.7086 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.11 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.1698865440655741, "-10": 2.0950171708413062e-06, "-11": 3.181331944394326e-07, "-12": 4.4434053798400894e-08, "-13": 5.743902441998709e-09, "-14": 6.903327621114999e-10, "-15": 7.654194344902069e-11, "-16": 6.854530813297351e-12, "-2": 0.09976256838883284, "-3": 0.04638217883396205, "-4": 0.01737170811505616, "-5": 0.005416491579334699, "-6": 0.0014420152392692694, "-7": 0.0003343224546354713, "-8": 6.856504040901452e-05, "-9": 1.2597168710251027e-05, "0": 0.23340533789831872, "1": 0.2029556773321982, "10": 4.050506978727093e-06, "11": 6.487838681250756e-07, "12": 9.55820302909549e-08, "13": 1.3032766914230887e-08, "14": 1.652179831729997e-09, "15": 1.9322689493959936e-10, "16": 1.8252194221875455e-11, "2": 0.1258738025892798, "3": 0.061728842746070905, "4": 0.02438646053359678, "5": 0.008020354752832897, "6": 0.002252239725438708, "7": 0.0005507817854169154, "8": 0.00011914779717310922, "9": 2.309008253654973e-05} |
| Raw goal margin distribution | {"-1": 0.18666995958022933, "-10": 2.301987910530939e-06, "-11": 3.495621791224142e-07, "-12": 4.88237786703793e-08, "-13": 6.311353512888099e-09, "-14": 7.585320515468354e-10, "-15": 8.410366794150495e-11, "-16": 7.531702977993174e-12, "-2": 0.10961830268073008, "-3": 0.05096436269158977, "-4": 0.019087892272535743, "-5": 0.005951597107012727, "-6": 0.0015844746734301027, "-7": 0.0003673508071921094, "-8": 7.53387114451352e-05, "-9": 1.3841667019020851e-05, "0": 0.21298800874473864, "1": 0.19664705295537896, "10": 3.924602015631882e-06, "11": 6.286172298740962e-07, "12": 9.261098196057281e-08, "13": 1.2627659591621014e-08, "14": 1.6008238800347875e-09, "15": 1.8722067764281596e-10, "16": 1.7684847504049518e-11, "2": 0.12196117225611652, "3": 0.05981007857440749, "4": 0.023628437789868485, "5": 0.00777105201752857, "6": 0.0021822316595343154, "7": 0.0005336614198106762, "8": 0.00011544423633868984, "9": 2.2372356087762502e-05} |
| Unadjusted home-win probability | 41.3% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 37.4% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 67.9% |
| Home training matches | 0 |
| Away training matches | 2 |
| P home draw | 65.9% |
| P draw away | 57.4% |
| P home away | 76.7% |
| Raw p home draw | 62.6% |
| Raw p draw away | 58.7% |
| Raw p home away | 78.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.71, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.87, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.20 |
| Reference draw odds | 3.72 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | -1.3% |
| Draw probability edge | -2.0% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | -0.0265 |
| Raw ev home | -0.0839 |
| Raw edge prob draw | -0.0408 |
| Raw ev draw | -0.1970 |
| Raw edge prob away | 0.0673 |
| Raw ev away | 0.1754 |
| Market p home draw | 69.1% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.5% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.40 |
| Market reference dc draw away odds | 1.71 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 84.1% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.3% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.2% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.86 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Bournemouth vs AC Milan

The model's most likely 1X2 outcome is **Bournemouth win** at **63.2%**. Expected goals are 2.89 for Bournemouth and 1.02 for AC Milan (3.91 combined). The most likely exact score is 1-1 at 8.0%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 71.9%; Under 3.5 goals: 47.4%; Double Chance 1X: 82.4%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 67.2%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 63.2% | 1.58 |
| Draw | 19.1% | 5.23 |
| AC Milan win | 17.6% | 5.67 |

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
| Over 3.5 | 52.6% |
| Under 3.5 | 47.4% |
| Over 4.5 | 32.8% |
| Under 4.5 | 67.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.01% |
| 2 | 2-1 | 7.11% |
| 3 | 2-0 | 6.97% |
| 4 | 3-1 | 6.85% |
| 5 | 3-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 63.2% | 50.5% | 1.93 | +22.0% |
| Draw | 19.1% | 24.9% | 3.86 | -26.2% |
| AC Milan win | 17.6% | 24.6% | 3.92 | -30.8% |
| Over 2.5 | 71.9% | 55.0% | 1.78 | +28.0% |
| Under 2.5 | 28.1% | 45.0% | 2.15 | -39.7% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
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
| Dc lambda home | 2.8907 |
| Dc lambda away | 1.0200 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.00 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.80 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.90 |
| Fair Under 3.5 odds | 2.11 |
| Fair Over 4.5 odds | 3.05 |
| Fair Under 4.5 odds | 1.49 |
| Goal margin distribution | {"-1": 0.11981163385391726, "-10": 1.4494040398051992e-08, "-11": 1.3152132192980708e-09, "-12": 1.0975644799771075e-10, "-13": 8.47661173833061e-12, "-14": 6.091601669900261e-13, "-15": 4.092731495042824e-14, "-16": 2.581460394343893e-15, "-17": 1.5334823824165955e-16, "-18": 8.532571181901588e-18, "-19": 3.965455060979298e-19, "-2": 0.04175218682217547, "-3": 0.011669939678282228, "-4": 0.0026220168705461005, "-5": 0.0004897914135447177, "-6": 7.805285215409179e-05, "-7": 1.082569099528023e-05, "-8": 1.3276510105561e-06, "-9": 1.45818894916673e-07, "0": 0.19131062629202936, "1": 0.16663775296764, "10": 0.00024404734592377392, "11": 6.27567335354975e-05, "12": 1.4841361814616596e-05, "13": 3.2482208082297435e-06, "14": 6.615067708188078e-07, "15": 1.2594925241369592e-07, "16": 2.2512687899006334e-08, "17": 3.789834273170197e-09, "18": 5.975866569492893e-10, "19": 7.870340976060339e-11, "2": 0.16901587505197993, "3": 0.13387405743159164, "4": 0.08523988211274745, "5": 0.045123010789234114, "6": 0.020377702787718825, "7": 0.008009430120920006, "8": 0.0027836168983393856, "9": 0.0008664008712216328} |
| Raw goal margin distribution | {"-1": 0.07252615125612907, "-10": 8.77374702612984e-09, "-11": 7.961443292992338e-10, "-12": 6.643939735036986e-11, "-13": 5.131188059944355e-12, "-14": 3.687458470368152e-13, "-15": 2.477472795522638e-14, "-16": 1.562647808059839e-15, "-17": 9.282702492093499e-17, "-18": 5.1650622584515375e-18, "-19": 2.400427940934586e-19, "-2": 0.025274051603631078, "-3": 0.007064220585531452, "-4": 0.001587198054416076, "-5": 0.00029648778670366197, "-6": 4.7248107543563545e-05, "-7": 6.553167478987168e-06, "-8": 8.036733571661924e-07, "-9": 8.82692513952596e-08, "0": 0.13392471283271284, "1": 0.20011509894261864, "10": 0.0002930761961588828, "11": 7.536449404241808e-05, "12": 1.782297549674685e-05, "13": 3.900784887279399e-06, "14": 7.944027720976578e-07, "15": 1.5125232223582696e-07, "16": 2.7035462769645088e-08, "17": 4.55120791684498e-09, "18": 7.17641175858982e-10, "19": 9.451484043008613e-11, "2": 0.20297098320491866, "3": 0.16076921208830314, "4": 0.10236448307222508, "5": 0.054188175295606406, "6": 0.024471561437698502, "7": 0.009618516047999952, "8": 0.003342842549837466, "9": 0.0010404598776734427} |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 13.4% |
| Unadjusted away-win probability | 10.7% |
| Raw p over 1 5 | 89.9% |
| Raw p under 3 5 | 45.1% |
| Raw p btts yes | 60.1% |
| Home training matches | 2 |
| Away training matches | 8 |
| P home draw | 82.4% |
| P draw away | 36.8% |
| P home away | 80.9% |
| Raw p home draw | 89.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 86.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.91, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.94 |
| Reference draw odds | 3.86 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.11 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | +12.7% |
| Draw probability edge | -5.7% |
| Away probability edge | -7.0% |
| Over 2.5 probability edge | +16.9% |
| Under 2.5 probability edge | -16.9% |
| Raw edge prob home | 0.2540 |
| Raw ev home | 0.4654 |
| Raw edge prob draw | -0.1148 |
| Raw ev draw | -0.4831 |
| Raw edge prob away | -0.1393 |
| Raw ev away | -0.5813 |
| Market p home draw | 75.0% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-22T15:07:21Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.1% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-22T15:07:21Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-22T15:07:21Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.93 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 79.0% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.15 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.6% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Celtic vs Celta Vigo

The model's most likely 1X2 outcome is **Celta Vigo win** at **42.4%**. Expected goals are 1.67 for Celtic and 2.10 for Celta Vigo (3.77 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.7%; Under 3.5 goals: 48.1%; Double Chance 1X: 57.6%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 71.7%; BTTS No (at least one team does not score): 28.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celtic win | 34.2% | 2.92 |
| Draw | 23.4% | 4.28 |
| Celta Vigo win | 42.4% | 2.36 |

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
| 2 | 2-2 | 8.22% |
| 3 | 1-2 | 7.44% |
| 4 | 2-1 | 7.34% |
| 5 | 1-3 | 5.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 34.2% | 36.9% | 2.59 | -11.3% |
| Draw | 23.4% | 26.6% | 3.57 | -16.6% |
| Celta Vigo win | 42.4% | 36.5% | 2.73 | +15.8% |
| Over 2.5 | 71.7% | 57.7% | 1.70 | +21.9% |
| Under 2.5 | 28.3% | 42.3% | 2.27 | -35.8% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Dc lambda away | 2.0988 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 71.7% |
| P btts no | 28.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.40 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.76 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.54 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.08 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.17918260256884253, "-10": 1.2654633323432566e-05, "-11": 2.353260282654187e-06, "-12": 4.026896650042247e-07, "-13": 6.38013608821121e-08, "-14": 9.408972395436702e-09, "-15": 1.2962324908396623e-09, "-16": 1.6516530793220186e-10, "-17": 1.690169666984376e-11, "-2": 0.12563759512387407, "-3": 0.070176480491198, "-4": 0.031788756139629455, "-5": 0.012038149554675555, "-6": 0.0039031694506811393, "-7": 0.001104174138158165, "-8": 0.0002766818125141396, "-9": 6.217025272259462e-05, "0": 0.23353167527392543, "1": 0.17750456027637015, "10": 1.6134586151792366e-06, "11": 2.390492339650488e-07, "12": 3.259094861994298e-08, "13": 4.114012310925545e-09, "14": 4.833780948632844e-10, "15": 5.305628056144982e-11, "16": 5.38619231654019e-12, "17": 4.391394509995684e-13, "2": 0.09866312480627415, "3": 0.04390722212771562, "4": 0.01584626955880199, "5": 0.004781039873788902, "6": 0.0012350631496248377, "7": 0.00027836745286482524, "8": 5.55738677616107e-05, "9": 9.949053603141361e-06} |
| Raw goal margin distribution | {"-1": 0.20418498881849775, "-10": 1.442040759874849e-05, "-11": 2.6816243185001753e-06, "-12": 4.588792860881782e-07, "-13": 7.270393426344993e-08, "-14": 1.072186080463742e-08, "-15": 1.4771033172519212e-09, "-16": 1.8821177988182974e-10, "-17": 1.926008829021096e-11, "-2": 0.14316853638564095, "-3": 0.07996861123228492, "-4": 0.03622442538432497, "-5": 0.01371790227944957, "-6": 0.004447801288843499, "-7": 0.0012582459503392828, "-8": 0.00031528882818172046, "-9": 7.084522813607976e-05, "0": 0.20134574024161203, "1": 0.1635010279419353, "10": 1.4861710691423547e-06, "11": 2.201903738200508e-07, "12": 3.0019812407449675e-08, "13": 3.7894533005507664e-09, "14": 4.452438589279578e-10, "15": 4.887061153283266e-11, "16": 4.961269609502584e-12, "17": 4.04495250919166e-13, "2": 0.09087948107177024, "3": 0.040443332502438575, "4": 0.014596139715369483, "5": 0.004403858316534352, "6": 0.0011376276430445443, "7": 0.0002564067346670642, "8": 5.118958347653297e-05, "9": 9.164161690439542e-06} |
| Unadjusted home-win probability | 31.5% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 48.3% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 47.9% |
| Raw p btts yes | 70.9% |
| Home training matches | 12 |
| Away training matches | 16 |
| P home draw | 57.6% |
| P draw away | 65.8% |
| P home away | 76.6% |
| Raw p home draw | 51.7% |
| Raw p draw away | 68.5% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.51, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.51, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.63 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.66 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | -2.7% |
| Draw probability edge | -3.2% |
| Away probability edge | +5.9% |
| Over 2.5 probability edge | +14.0% |
| Under 2.5 probability edge | -14.0% |
| Raw edge prob home | -0.0540 |
| Raw ev home | -0.1834 |
| Raw edge prob draw | -0.0644 |
| Raw ev draw | -0.2812 |
| Raw edge prob away | 0.1184 |
| Raw ev away | 0.3196 |
| Market p home draw | 63.6% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:06:50Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.2% |
| Market draw away odds | 1.54 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:06:50Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:06:50Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 81.2% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.2% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.0% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:06:50Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Dinamo Zagreb vs NEC Nijmegen

The model's most likely 1X2 outcome is **Dinamo Zagreb win** at **77.7%**. Expected goals are 3.61 for Dinamo Zagreb and 0.82 for NEC Nijmegen (4.42 combined). The most likely exact score is 3-0 at 8.4%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 78.9%; Under 3.5 goals: 38.3%; Double Chance 1X: 90.3%; Double Chance X2: 22.3%; Double Chance 12 (either team wins): 87.4%; Under 4.5 goals: 57.6%; BTTS Yes (both teams score): 56.4%; BTTS No (at least one team does not score): 43.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Dinamo Zagreb win | 77.7% | 1.29 |
| Draw | 12.6% | 7.93 |
| NEC Nijmegen win | 9.7% | 10.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Dinamo Zagreb expected goals | 3.61 |
| NEC Nijmegen expected goals | 0.82 |
| Expected total goals | 4.42 |
| Over 0.5 | 98.4% |
| Under 0.5 | 1.6% |
| Over 1.5 | 92.0% |
| Under 1.5 | 8.0% |
| Over 2.5 | 78.9% |
| Under 2.5 | 21.1% |
| Over 3.5 | 61.7% |
| Under 3.5 | 38.3% |
| Over 4.5 | 42.4% |
| Under 4.5 | 57.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 8.36% |
| 2 | 4-0 | 7.54% |
| 3 | 2-0 | 6.96% |
| 4 | 3-1 | 6.82% |
| 5 | 4-1 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Dinamo Zagreb win | 77.7% | 68.2% | 1.47 | +14.2% |
| Draw | 12.6% | 17.2% | 4.98 | -37.2% |
| NEC Nijmegen win | 9.7% | 14.6% | 6.45 | -37.5% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | gnk dinamo |
| Matched away-team name | n.e.c. |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6053 |
| Dc lambda away | 0.8156 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 56.4% |
| P btts no | 43.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 61.93 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.50 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.75 |
| Fair Over 3.5 odds | 1.62 |
| Fair Under 3.5 odds | 2.61 |
| Fair Over 4.5 odds | 2.36 |
| Fair Under 4.5 odds | 1.74 |
| Goal margin distribution | {"-1": 0.07170407549870571, "-10": 1.1499925749955918e-09, "-11": 8.344679157826145e-11, "-12": 5.568622921322136e-12, "-13": 3.439073532885371e-13, "-14": 1.9762857842383435e-14, "-15": 1.0617664842258239e-15, "-16": 5.355334461920641e-17, "-17": 2.545205200920641e-18, "-18": 1.143572970766591e-19, "-19": 4.8717363600646e-21, "-2": 0.0197915605218401, "-20": 1.9724075534203392e-22, "-21": 7.556120859364569e-24, "-22": 2.471122755727149e-25, "-3": 0.0044252543078063065, "-4": 0.0007952735755303094, "-5": 0.00011881419777812465, "-6": 1.5142553332666426e-05, "-7": 1.6795910045406427e-06, "-8": 1.6472458410850536e-07, "-9": 1.44679447400026e-08, "0": 0.12609872653370569, "1": 0.13267443102521162, "10": 0.0014262144681866581, "11": 0.000457446753831119, "12": 0.00013493351156470266, "13": 3.6834483052446025e-05, "14": 9.356296354687392e-06, "15": 2.2218991366088165e-06, "16": 4.953623929911918e-07, "17": 1.0406395813434345e-07, "18": 2.066724204330128e-08, "19": 3.891737390732728e-09, "2": 0.1684383575564253, "20": 6.964621374762386e-10, "21": 1.1793449601463813e-10, "22": 1.704815498627267e-11, "3": 0.16647165533590966, "4": 0.13223905048994378, "5": 0.08732781925545001, "6": 0.049195399570126495, "7": 0.024119595805548597, "8": 0.01045601049929764, "9": 0.004059341021580467} |
| Raw goal margin distribution | {"-1": 0.035071984315901, "-10": 5.62485762115098e-10, "-11": 4.081559583733665e-11, "-12": 2.723731592652667e-12, "-13": 1.6821238146883732e-13, "-14": 9.666432981176423e-15, "-15": 5.193325096645255e-16, "-16": 2.619407682876758e-17, "-17": 1.2449138527565239e-18, "-18": 5.59345797513813e-20, "-19": 2.382869593158264e-21, "-2": 0.009680472070540968, "-20": 9.647463731593816e-23, "-21": 3.6958589930285075e-24, "-22": 1.2086785573728372e-25, "-3": 0.0021644857506050346, "-4": 0.00038898517516417863, "-5": 5.8114544424409525e-05, "-6": 7.4065440394048135e-06, "-7": 8.215235878669284e-07, "-8": 8.057028823140041e-08, "-9": 7.076578666910679e-09, "0": 0.08008568715914016, "1": 0.14897897527864307, "10": 0.001601483935948798, "11": 0.0005136630178376384, "12": 0.0001515156773488509, "13": 4.1361123599084234e-05, "14": 1.0506104548959819e-05, "15": 2.494951393321457e-06, "16": 5.562381623131333e-07, "17": 1.1685252181973228e-07, "18": 2.3207067990829574e-08, "19": 4.369998379075524e-09, "2": 0.1891379801855374, "20": 7.820513324218943e-10, "21": 1.3242762927639984e-10, "22": 1.9143226321910964e-11, "3": 0.1869295872101421, "4": 0.1484900902274749, "5": 0.09805965569600411, "6": 0.05524109023680777, "7": 0.027083686279859485, "8": 0.011740964085175436, "9": 0.004558199051833119} |
| Unadjusted home-win probability | 87.3% |
| Unadjusted draw probability | 8.0% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.6% |
| Raw p btts yes | 54.1% |
| Home training matches | 12 |
| Away training matches | 2 |
| P home draw | 90.3% |
| P draw away | 22.3% |
| P home away | 87.4% |
| Raw p home draw | 95.3% |
| Raw p draw away | 12.7% |
| Raw p home away | 92.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.18, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.19, "price": 5.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.42 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:28Z |
| Market reference home last update utc | 2026-10-22T15:07:28Z |
| Market reference draw last update utc | 2026-10-22T15:07:28Z |
| Market reference away last update utc | 2026-10-22T15:07:28Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +9.5% |
| Draw probability edge | -4.6% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | +14.3% |
| Under 2.5 probability edge | -14.3% |
| Raw edge prob home | 0.1910 |
| Raw ev home | 0.2826 |
| Raw edge prob draw | -0.0920 |
| Raw ev draw | -0.6012 |
| Raw edge prob away | -0.0990 |
| Raw ev away | -0.6944 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.0% |
| Market draw away odds | 2.85 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.9% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.85 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.52 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.5% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.30 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-22T15:07:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — FC Ararat-Armenia vs AZ Alkmaar

The model's most likely 1X2 outcome is **AZ Alkmaar win** at **55.3%**. Expected goals are 1.44 for FC Ararat-Armenia and 1.44 for AZ Alkmaar (2.88 combined). The most likely exact score is 0-1 at 12.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 56.2%; Under 3.5 goals: 67.3%; Double Chance 1X: 44.7%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Ararat-Armenia win | 24.9% | 4.02 |
| Draw | 19.8% | 5.05 |
| AZ Alkmaar win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Ararat-Armenia expected goals | 1.44 |
| AZ Alkmaar expected goals | 1.44 |
| Expected total goals | 2.88 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.52% |
| 2 | 1-2 | 12.14% |
| 3 | 1-1 | 9.23% |
| 4 | 0-2 | 8.43% |
| 5 | 1-3 | 5.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Ararat-Armenia win | 24.9% | 11.7% | 8.31 | +106.8% |
| Draw | 19.8% | 15.9% | 5.45 | +7.9% |
| AZ Alkmaar win | 55.3% | 72.4% | 1.36 | -24.8% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | az alkmaar |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4407 |
| Dc lambda away | 1.4438 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.91 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.2968275917025343, "-10": 1.0585368053712479e-06, "-11": 1.3681137222526745e-07, "-12": 1.6239443430592623e-08, "-13": 1.7677463246634484e-09, "-14": 1.587263627824905e-10, "-2": 0.16023764094387885, "-3": 0.06660042726980851, "-4": 0.021903403944279334, "-5": 0.0059324351710209515, "-6": 0.0013624582698359403, "-7": 0.0002712271833967506, "-8": 4.760633979341169e-05, "-9": 7.467899657231862e-06, "0": 0.19791028827572582, "1": 0.13375958488581516, "10": 4.6781559535475463e-07, "11": 6.033298054944504e-08, "12": 7.146075030550233e-09, "13": 7.76211769057774e-10, "14": 6.954616620211726e-11, "2": 0.07204809146575915, "3": 0.029881252889751287, "4": 0.009806121037636784, "5": 0.002650223418094855, "6": 0.0006073465163783381, "7": 0.00012064529750951059, "8": 2.113030793304013e-05, "9": 3.3075266882262416e-06} |
| Raw goal margin distribution | {"-1": 0.20510534305525013, "-10": 7.314399357451128e-07, "-11": 9.45354954139306e-08, "-12": 1.1221317387488642e-08, "-13": 1.2214976858287075e-09, "-14": 1.096785676280405e-10, "-2": 0.11072284799283251, "-3": 0.04602032918991499, "-4": 0.015135065963043265, "-5": 0.004099262281939995, "-6": 0.0009414470845864331, "-7": 0.00018741567850016287, "-8": 3.289557617917749e-05, "-9": 5.160255191618859e-06, "0": 0.23689033506668555, "1": 0.2046762153919508, "10": 7.158419760369455e-07, "11": 9.23203083556081e-08, "12": 1.0934779690057555e-08, "13": 1.1877435726872094e-09, "14": 1.0641813897239813e-10, "2": 0.11024653448209469, "3": 0.04572368969195769, "4": 0.015005128367976357, "5": 0.004055318350620111, "6": 0.0009293493734293609, "7": 0.00018460899770406827, "8": 3.23331704527427e-05, "9": 5.061110539718869e-06} |
| Unadjusted home-win probability | 38.1% |
| Unadjusted draw probability | 23.7% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 77.7% |
| Raw p under 3 5 | 67.3% |
| Raw p btts yes | 57.7% |
| Home training matches | 0 |
| Away training matches | 14 |
| P home draw | 44.7% |
| P draw away | 75.1% |
| P home away | 80.2% |
| Raw p home draw | 61.8% |
| Raw p draw away | 61.9% |
| Raw p home away | 76.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.86, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.77, "price": 1.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 7.00 |
| Reference draw odds | 5.30 |
| Reference away odds | 1.34 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:28Z |
| Market reference home last update utc | 2026-10-22T15:07:28Z |
| Market reference draw last update utc | 2026-10-22T15:07:28Z |
| Market reference away last update utc | 2026-10-22T15:07:28Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +13.2% |
| Draw probability edge | +3.9% |
| Away probability edge | -17.1% |
| Over 2.5 probability edge | -9.2% |
| Under 2.5 probability edge | +9.2% |
| Raw edge prob home | 0.2639 |
| Raw ev home | 2.1649 |
| Raw edge prob draw | 0.0780 |
| Raw ev draw | 0.2911 |
| Raw edge prob away | -0.3419 |
| Raw ev away | -0.4801 |
| Market p home draw | 29.1% |
| Market home draw odds | 3.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.5% |
| Market draw away odds | 1.10 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.5% |
| Market home away odds | 1.18 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.35 |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.2% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.22 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.5% |
| Market btts yes odds | 1.77 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-22T15:07:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Ferencváros TC vs Torreense

The model's most likely 1X2 outcome is **Ferencváros TC win** at **52.2%**. Expected goals are 2.21 for Ferencváros TC and 2.87 for Torreense (5.08 combined). The most likely exact score is 3-2 at 8.0%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.0%; Under 3.5 goals: 26.3%; Double Chance 1X: 68.6%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 43.2%; BTTS Yes (both teams score): 84.3%; BTTS No (at least one team does not score): 15.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ferencváros TC win | 52.2% | 1.92 |
| Draw | 16.5% | 6.08 |
| Torreense win | 31.4% | 3.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ferencváros TC expected goals | 2.21 |
| Torreense expected goals | 2.87 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 95.7% |
| Under 1.5 | 4.3% |
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 73.7% |
| Under 3.5 | 26.3% |
| Over 4.5 | 56.8% |
| Under 4.5 | 43.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-2 | 7.97% |
| 2 | 2-1 | 7.53% |
| 3 | 2-2 | 6.01% |
| 4 | 3-1 | 5.55% |
| 5 | 4-2 | 4.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ferencváros TC win | 52.2% | 74.2% | 1.34 | -30.1% |
| Draw | 16.5% | 15.8% | 5.50 | -9.5% |
| Torreense win | 31.4% | 10.0% | 9.19 | +188.3% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | torreense |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2105 |
| Dc lambda away | 2.8722 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 84.3% |
| P btts no | 15.7% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 245.54 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 23.27 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.31 |
| Fair Over 3.5 odds | 1.36 |
| Fair Under 3.5 odds | 3.80 |
| Fair Over 4.5 odds | 1.76 |
| Fair Under 4.5 odds | 2.31 |
| Goal margin distribution | {"-1": 0.10734533468464888, "-10": 6.831094606032353e-05, "-11": 1.7047549073491072e-05, "-12": 3.9257582222411274e-06, "-13": 8.389156472592934e-07, "-14": 1.6718061287310186e-07, "-15": 3.120346963346818e-08, "-16": 5.473928310040751e-09, "-17": 9.024416383545123e-10, "-18": 1.3609332951417128e-10, "-19": 1.542018781673541e-11, "-2": 0.08730039231740254, "-3": 0.058968764074258904, "-4": 0.03340279736073192, "-5": 0.016176399070444165, "-6": 0.006811521881695838, "-7": 0.0025299133117839072, "-8": 0.0008389518818270359, "-9": 0.0002509572653045444, "0": 0.1645638714908218, "1": 0.24088872768048417, "10": 1.447271589947975e-05, "11": 2.7796695197183325e-06, "12": 4.926361111185208e-07, "13": 8.102004271268042e-08, "14": 1.2426006162358134e-08, "15": 1.784925187116421e-09, "16": 2.4098372565132964e-10, "17": 3.057589744483003e-11, "18": 3.548692802056633e-12, "19": 3.0945158290774953e-13, "2": 0.15028100915598772, "3": 0.0781234495850489, "4": 0.034057573585574076, "5": 0.012693582086063693, "6": 0.0041135613447553536, "7": 0.001175847339954718, "8": 0.000300091595156414, "9": 6.908567916416514e-05} |
| Raw goal margin distribution | {"-1": 0.18040101022369076, "-10": 0.00011480111096417066, "-11": 2.8649545727631284e-05, "-12": 6.59749910200372e-06, "-13": 1.409853820872951e-06, "-14": 2.8095819478996284e-07, "-15": 5.243951645312558e-08, "-16": 9.199302418912028e-09, "-17": 1.5166134951774323e-09, "-18": 2.2871393713743892e-10, "-19": 2.591465635791562e-11, "-2": 0.14671414471108982, "-3": 0.0991009496769504, "-4": 0.05613563370849515, "-5": 0.027185519917215628, "-6": 0.011447217824869587, "-7": 0.004251688427493888, "-8": 0.0014099147154860699, "-9": 0.00042175045908528826, "0": 0.1710986682776791, "1": 0.13929236706102105, "10": 8.368755461709107e-06, "11": 1.6073261325972226e-06, "12": 2.848636824071463e-07, "13": 4.6849321832125695e-08, "14": 7.185258638442821e-09, "15": 1.0321215805085798e-09, "16": 1.3934729903045145e-10, "17": 1.7680317261480754e-11, "18": 2.052008930141909e-12, "19": 1.7893839985395204e-13, "2": 0.08689903297352347, "3": 0.045174385370608694, "4": 0.019693574235577882, "5": 0.0073399827060252765, "6": 0.002378640554412755, "7": 0.0006799262085104498, "8": 0.00017352604676420922, "9": 3.994835239264061e-05} |
| Unadjusted home-win probability | 30.2% |
| Unadjusted draw probability | 17.1% |
| Unadjusted away-win probability | 52.7% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.4% |
| Raw p btts yes | 83.8% |
| Home training matches | 0 |
| Away training matches | 2 |
| P home draw | 68.6% |
| P draw away | 47.8% |
| P home away | 83.5% |
| Raw p home draw | 47.3% |
| Raw p draw away | 69.8% |
| Raw p home away | 82.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.66, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.11, "price": 7.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.53, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.31 |
| Reference draw odds | 5.30 |
| Reference away odds | 8.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:28Z |
| Market reference home last update utc | 2026-10-22T15:07:28Z |
| Market reference draw last update utc | 2026-10-22T15:07:28Z |
| Market reference away last update utc | 2026-10-22T15:07:28Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | -22.0% |
| Draw probability edge | +0.7% |
| Away probability edge | +21.4% |
| Over 2.5 probability edge | +25.3% |
| Under 2.5 probability edge | -25.3% |
| Raw edge prob home | -0.4401 |
| Raw ev home | -0.5957 |
| Raw edge prob draw | 0.0131 |
| Raw ev draw | -0.0590 |
| Raw edge prob away | 0.4270 |
| Raw ev away | 3.8451 |
| Market p home draw | 89.3% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 27.4% |
| Market draw away odds | 3.55 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.2% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.09 |
| Market reference dc draw away odds | 3.55 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.39 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.5% |
| Market btts yes odds | 1.93 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-22T15:07:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Jagiellonia Białystok vs Anderlecht

The model's most likely 1X2 outcome is **Jagiellonia Białystok win** at **42.3%**. Expected goals are 1.75 for Jagiellonia Białystok and 1.08 for Anderlecht (2.83 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.4%; Double Chance 1X: 66.6%; Double Chance X2: 57.7%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Jagiellonia Białystok win | 42.3% | 2.36 |
| Draw | 24.3% | 4.12 |
| Anderlecht win | 33.4% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Jagiellonia Białystok expected goals | 1.75 |
| Anderlecht expected goals | 1.08 |
| Expected total goals | 2.83 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
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
| 1 | 1-1 | 11.46% |
| 2 | 0-1 | 9.67% |
| 3 | 1-0 | 8.57% |
| 4 | 1-2 | 8.42% |
| 5 | 2-1 | 7.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Jagiellonia Białystok win | 42.3% | 30.9% | 3.17 | +34.1% |
| Draw | 24.3% | 26.1% | 3.57 | -13.3% |
| Anderlecht win | 33.4% | 42.9% | 2.29 | -23.5% |
| Over 2.5 | 52.6% | 54.5% | 1.79 | -5.8% |
| Under 2.5 | 47.4% | 45.5% | 2.12 | +0.4% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
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
| Dc lambda home | 1.7529 |
| Dc lambda away | 1.0803 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.34 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.62 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.21198932684751146, "-10": 5.824100884603472e-08, "-11": 5.639948467833486e-09, "-12": 5.017171536593672e-10, "-13": 4.126752694051469e-11, "-14": 3.1554299336112426e-12, "-15": 2.241789256989479e-13, "-16": 1.3534672281146499e-14, "-2": 0.08646459795221521, "-3": 0.027196489205313628, "-4": 0.006743172353885131, "-5": 0.0013738617742024893, "-6": 0.00023702259494627793, "-7": 3.541260058763819e-05, "-8": 4.661985338009317e-06, "-9": 5.482603631456513e-07, "0": 0.2428640062903297, "1": 0.19110915902074593, "10": 4.150860212190582e-06, "11": 6.522012308483284e-07, "12": 9.413750581490901e-08, "13": 1.2563465184495025e-08, "14": 1.5586794071357063e-09, "15": 1.796760947399624e-10, "16": 1.7601128759359387e-11, "2": 0.12828310690960754, "3": 0.06546983512827437, "4": 0.02633843234901178, "5": 0.008706948217718374, "6": 0.0024373052811086865, "7": 0.0005908473085661111, "8": 0.00012620762762771015, "9": 2.408234694083468e-05} |
| Raw goal margin distribution | {"-1": 0.15158009045911278, "-10": 4.1644442767924015e-08, "-11": 4.032768591004985e-09, "-12": 3.5874604003662944e-10, "-13": 2.9507784942242344e-11, "-14": 2.256247339840068e-12, "-15": 1.6029609764701296e-13, "-16": 9.677783684771939e-15, "-2": 0.06182533702998764, "-3": 0.01944648042057838, "-4": 0.004821613854732117, "-5": 0.0009823612118063344, "-6": 0.00016947978899265137, "-7": 2.5321299332809496e-05, "-8": 3.3334893306342193e-06, "-9": 3.9202613016712546e-07, "0": 0.2243299045648283, "1": 0.24247839189724413, "10": 5.266591692410543e-06, "11": 8.275098193087568e-07, "12": 1.1944121958455522e-07, "13": 1.594046486418093e-08, "14": 1.9776450174456984e-09, "15": 2.2797217432259994e-10, "16": 2.233222844480466e-11, "2": 0.1627649958296722, "3": 0.08306781538376375, "4": 0.03341807767773935, "5": 0.01104733448141928, "6": 0.0030924413468939984, "7": 0.0007496642545654911, "8": 0.00016013163758944317, "9": 3.0555567243594044e-05} |
| Unadjusted home-win probability | 53.7% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 68.5% |
| Raw p btts yes | 54.0% |
| Home training matches | 0 |
| Away training matches | 12 |
| P home draw | 66.6% |
| P draw away | 57.7% |
| P home away | 75.7% |
| Raw p home draw | 76.1% |
| Raw p draw away | 46.3% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.08 |
| Reference draw odds | 3.62 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | +11.4% |
| Draw probability edge | -1.9% |
| Away probability edge | -9.5% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.2274 |
| Raw ev home | 0.7017 |
| Raw edge prob draw | -0.0371 |
| Raw ev draw | -0.1991 |
| Raw edge prob away | -0.1904 |
| Raw ev away | -0.4530 |
| Market p home draw | 57.5% |
| Market home draw odds | 1.67 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:23Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.1% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:23Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.3% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:23Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.67 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 77.8% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.0% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.0% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:23Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Juventus vs Rennes

The model's most likely 1X2 outcome is **Juventus win** at **73.0%**. Expected goals are 2.03 for Juventus and 0.45 for Rennes (2.48 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.6%; Double Chance 1X: 90.3%; Double Chance X2: 27.0%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 31.3%; BTTS No (at least one team does not score): 68.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 73.0% | 1.37 |
| Draw | 17.3% | 5.77 |
| Rennes win | 9.7% | 10.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 2.03 |
| Rennes expected goals | 0.45 |
| Expected total goals | 2.48 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 69.7% |
| Under 1.5 | 30.3% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.86% |
| 2 | 2-0 | 16.72% |
| 3 | 3-0 | 11.30% |
| 4 | 0-0 | 8.05% |
| 5 | 2-1 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 73.0% | 70.8% | 1.40 | +2.2% |
| Draw | 17.3% | 17.4% | 4.98 | -13.6% |
| Rennes win | 9.7% | 11.8% | 8.01 | -22.7% |
| Over 2.5 | 44.6% | 59.2% | 1.65 | -26.4% |
| Under 2.5 | 55.4% | 40.8% | 2.36 | +30.8% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | juventus |
| Matched away-team name | rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0276 |
| Dc lambda away | 0.4514 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 31.3% |
| P btts no | 68.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.42 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.30 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.61 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.07946758693076701, "-10": 1.132293400400296e-11, "-11": 4.61449577607356e-13, "-12": 1.7256652208002297e-14, "-13": 5.961911477168212e-16, "-14": 1.9138911316426933e-17, "-15": 5.737321891491135e-19, "-16": 1.611068904219958e-20, "-17": 4.059132817560777e-22, "-2": 0.014728702118427172, "-3": 0.002065262254359319, "-4": 0.00022313904532867836, "-5": 1.9559864048355932e-05, "-6": 1.440592089029797e-06, "-7": 9.141779989514359e-08, "-8": 5.093905633461086e-09, "-9": 2.529248582932674e-10, "0": 0.17339838607778701, "1": 0.25649899544701954, "10": 2.8597146508990772e-05, "11": 5.235194944335117e-06, "12": 8.79447731476384e-07, "13": 1.3648467534923092e-07, "14": 1.9681603524601028e-08, "15": 2.6503140970380306e-09, "16": 3.3430827481595554e-10, "17": 3.783651727631222e-11, "2": 0.22437225570558583, "3": 0.141326877650446, "4": 0.06859145385525815, "5": 0.027008791393864813, "6": 0.008935630983398, "7": 0.0025471812316780066, "8": 0.0006375655717199124, "9": 0.00014220352386807867} |
| Raw goal margin distribution | {"-1": 0.061841081769164134, "-10": 8.81142255166798e-12, "-11": 3.5909660986716607e-13, "-12": 1.3428997676585125e-14, "-13": 4.639514919224675e-16, "-14": 1.4893757636343956e-17, "-15": 4.464740983475767e-19, "-16": 1.2537217712225609e-20, "-17": 3.1587867982120286e-22, "-2": 0.011461765824761331, "-3": 0.0016071716391473196, "-4": 0.00017364513609914933, "-5": 1.5221339903801681e-05, "-6": 1.1210579887283708e-06, "-7": 7.11406481160418e-08, "-8": 3.9640392639292675e-09, "-9": 1.9682423296425156e-10, "0": 0.17232107475794048, "1": 0.2643977821840422, "10": 2.9477784505908646e-05, "11": 5.396410735141532e-06, "12": 9.065299820917676e-07, "13": 1.4068766780764788e-07, "14": 2.0287690845186925e-08, "15": 2.731929488171023e-09, "16": 3.4460316802827076e-10, "17": 3.9001678100105753e-11, "2": 0.2312817119957926, "3": 0.1456789838441747, "4": 0.07070370098137571, "5": 0.027840516613190043, "6": 0.009210800261841316, "7": 0.002625620686360888, "8": 0.0006571991553645849, "9": 0.00014658262604089426} |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 7.5% |
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 76.2% |
| Raw p btts yes | 31.2% |
| Home training matches | 10 |
| Away training matches | 18 |
| P home draw | 90.3% |
| P draw away | 27.0% |
| P home away | 82.7% |
| Raw p home draw | 92.5% |
| Raw p draw away | 24.7% |
| Raw p home away | 82.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:23Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.41, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:23Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.05, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.37 |
| Reference draw odds | 4.90 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:28Z |
| Market reference home last update utc | 2026-10-22T15:07:28Z |
| Market reference draw last update utc | 2026-10-22T15:07:28Z |
| Market reference away last update utc | 2026-10-22T15:07:28Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | +2.2% |
| Draw probability edge | -0.1% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | 0.0450 |
| Raw ev home | 0.0536 |
| Raw edge prob draw | -0.0022 |
| Raw ev draw | -0.1418 |
| Raw edge prob away | -0.0428 |
| Raw ev away | -0.3984 |
| Market p home draw | 87.6% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:23Z |
| Market reference home draw last update utc | 2026-10-22T15:07:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.5% |
| Market draw away odds | 3.12 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:23Z |
| Market reference draw away last update utc | 2026-10-22T15:07:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.9% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:23Z |
| Market reference home away last update utc | 2026-10-22T15:07:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 3.06 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.1% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.8% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:23Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-22T15:07:43Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Lech Poznań vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **72.2%**. Expected goals are 0.06 for Lech Poznań and 2.08 for Sunderland (2.14 combined). The most likely exact score is 0-2 at 21.4%. Goal-market probabilities: at least one goal: 84.2%; Over 2.5 goals: 30.7%; Under 3.5 goals: 85.8%; Double Chance 1X: 27.8%; Double Chance X2: 89.9%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 94.5%; BTTS Yes (both teams score): 5.3%; BTTS No (at least one team does not score): 94.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lech Poznań win | 10.1% | 9.85 |
| Draw | 17.6% | 5.67 |
| Sunderland win | 72.2% | 1.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lech Poznań expected goals | 0.06 |
| Sunderland expected goals | 2.08 |
| Expected total goals | 2.14 |
| Over 0.5 | 84.2% |
| Under 0.5 | 15.8% |
| Over 1.5 | 54.2% |
| Under 1.5 | 45.8% |
| Over 2.5 | 30.7% |
| Under 2.5 | 69.3% |
| Over 3.5 | 14.2% |
| Under 3.5 | 85.8% |
| Over 4.5 | 5.5% |
| Under 4.5 | 94.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 21.40% |
| 2 | 0-1 | 20.67% |
| 3 | 0-0 | 15.76% |
| 4 | 0-3 | 14.82% |
| 5 | 1-0 | 9.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lech Poznań win | 10.1% | 19.5% | 4.87 | -50.6% |
| Draw | 17.6% | 22.1% | 4.12 | -27.3% |
| Sunderland win | 72.2% | 58.4% | 1.70 | +22.8% |
| Over 2.5 | 30.7% | 56.5% | 1.73 | -46.8% |
| Under 2.5 | 69.3% | 43.5% | 2.21 | +53.1% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | lech poznan |
| Matched away-team name | sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.0582 |
| Dc lambda away | 2.0773 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 5.3% |
| P btts no | 94.7% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.34 |
| Fair Over 1.5 odds | 1.84 |
| Fair Under 1.5 odds | 2.18 |
| Fair Over 2.5 odds | 3.25 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.07 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.10 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.2193758053842759, "-10": 4.1350512634394504e-05, "-11": 7.801669813825873e-06, "-12": 1.349480902874075e-06, "-13": 2.1549232779570508e-07, "-14": 3.19558671620457e-08, "-15": 4.4232080355713565e-09, "-16": 5.739986063600642e-10, "-17": 6.964347638218162e-11, "-2": 0.2227850891317023, "-3": 0.1527330984519927, "-4": 0.0788428803871428, "-5": 0.03262475032705604, "-6": 0.01126281039571214, "-7": 0.0033351106558681207, "-8": 0.0008645481353037152, "-9": 0.00019927871055314475, "0": 0.17643150060180138, "1": 0.09887423872729396, "10": 1.8137385507603977e-19, "11": 9.589288266107727e-22, "12": 4.648047672430774e-24, "13": 2.0798914305570732e-26, "14": 8.642999394342768e-29, "15": 3.3524033322662817e-31, "16": 1.2190871627413834e-33, "17": 4.144855399903278e-36, "2": 0.002570039081496452, "3": 4.937325864761547e-05, "4": 7.14210340812325e-07, "5": 8.281630903806125e-09, "6": 8.011622352372659e-11, "7": 6.647968712837125e-13, "8": 4.829174733090057e-15, "9": 3.119246295774257e-17} |
| Raw goal margin distribution | {"-1": 0.26136565251190946, "-10": 4.926524918032335e-05, "-11": 9.294956287459499e-06, "-12": 1.6077796551639425e-06, "-13": 2.5673885398153265e-07, "-14": 3.807241212293974e-08, "-15": 5.26983662755315e-09, "-16": 6.83865388115302e-10, "-17": 8.297365616933862e-11, "-2": 0.26542749365106094, "-3": 0.18196713109335458, "-4": 0.09393388136949501, "-5": 0.038869323544283234, "-6": 0.013418579970734618, "-7": 0.003973470872248125, "-8": 0.001030027842476955, "-9": 0.0002374218529897548, "0": 0.13148544252390132, "1": 0.008018615258818994, "10": 1.4709262802769707e-20, "11": 7.776829859990549e-23, "12": 3.7695264681297607e-25, "13": 1.6867739642224865e-27, "14": 7.009397768066841e-30, "15": 2.718770112401932e-32, "16": 9.886691468694909e-35, "17": 3.361441886488884e-37, "2": 0.000208427947055938, "3": 4.004128580563197e-06, "4": 5.792184102311683e-08, "5": 6.716331047192701e-10, "6": 6.497356446891849e-12, "7": 5.391445137487733e-14, "8": 3.916418948019633e-16, "9": 2.5296817720433758e-18} |
| Unadjusted home-win probability | 0.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 86.0% |
| Raw p over 1 5 | 62.9% |
| Raw p under 3 5 | 83.2% |
| Raw p btts yes | 4.9% |
| Home training matches | 2 |
| Away training matches | 2 |
| P home draw | 27.8% |
| P draw away | 89.9% |
| P home away | 82.4% |
| Raw p home draw | 14.0% |
| Raw p draw away | 99.2% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.27, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.27, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.64 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:28Z |
| Market reference home last update utc | 2026-10-22T15:07:28Z |
| Market reference draw last update utc | 2026-10-22T15:07:28Z |
| Market reference away last update utc | 2026-10-22T15:07:28Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:28Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:28Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | -9.3% |
| Draw probability edge | -4.5% |
| Away probability edge | +13.8% |
| Over 2.5 probability edge | -25.8% |
| Under 2.5 probability edge | +25.8% |
| Raw edge prob home | -0.1865 |
| Raw ev home | -0.9599 |
| Raw edge prob draw | -0.0899 |
| Raw ev draw | -0.4583 |
| Raw edge prob away | 0.2764 |
| Raw ev away | 0.4625 |
| Market p home draw | 43.1% |
| Market home draw odds | 2.25 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.1% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.25 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.80 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.1% |
| Market under 3 5 odds | 1.46 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 2.98 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Lillestrom vs Real Sociedad

The model's most likely 1X2 outcome is **Real Sociedad win** at **53.9%**. Expected goals are 0.69 for Lillestrom and 0.92 for Real Sociedad (1.61 combined). The most likely exact score is 0-1 at 25.7%. Goal-market probabilities: at least one goal: 85.2%; Over 2.5 goals: 24.1%; Under 3.5 goals: 91.5%; Double Chance 1X: 46.1%; Double Chance X2: 79.5%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 27.9%; BTTS No (at least one team does not score): 72.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lillestrom win | 20.5% | 4.89 |
| Draw | 25.7% | 3.89 |
| Real Sociedad win | 53.9% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lillestrom expected goals | 0.69 |
| Real Sociedad expected goals | 0.92 |
| Expected total goals | 1.61 |
| Over 0.5 | 85.2% |
| Under 0.5 | 14.8% |
| Over 1.5 | 48.5% |
| Under 1.5 | 51.5% |
| Over 2.5 | 24.1% |
| Under 2.5 | 75.9% |
| Over 3.5 | 8.5% |
| Under 3.5 | 91.5% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 25.72% |
| 2 | 0-0 | 14.76% |
| 3 | 0-2 | 11.45% |
| 4 | 1-0 | 11.03% |
| 5 | 1-1 | 9.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lillestrom win | 20.5% | 14.2% | 6.42 | +31.3% |
| Draw | 25.7% | 17.8% | 5.25 | +34.8% |
| Real Sociedad win | 53.9% | 68.0% | 1.44 | -22.4% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | lillestrøm |
| Matched away-team name | real sociedad |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6930 |
| Dc lambda away | 0.9212 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 27.9% |
| P btts no | 72.1% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.77 |
| Fair Over 1.5 odds | 2.06 |
| Fair Under 1.5 odds | 1.94 |
| Fair Over 2.5 odds | 4.14 |
| Fair Under 2.5 odds | 1.32 |
| Fair Over 3.5 odds | 11.81 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 36.48 |
| Fair Under 4.5 odds | 1.03 |
| Goal margin distribution | {"-1": 0.3454663289392543, "-10": 3.469276763479859e-08, "-11": 2.8880074493080033e-09, "-12": 2.1051427366439838e-10, "-2": 0.14090535200399606, "-3": 0.04114681996469035, "-4": 0.009189277672305162, "-5": 0.0016583479716785936, "-6": 0.0002508537109590368, "-7": 3.264504704294044e-05, "-8": 3.7264498567001117e-06, "-9": 3.787698962582593e-07, "0": 0.2568334945843597, "1": 0.14775985536996186, "10": 1.1346316167315855e-09, "11": 7.104762165406832e-11, "12": 3.895543736095479e-12, "2": 0.044963593367151666, "3": 0.009876546212498519, "4": 0.0016591494217108856, "5": 0.00022522421949693725, "6": 2.5626851844930475e-05, "7": 2.5085763771879873e-06, "8": 2.1539747732107447e-07, "9": 1.6468577479386963e-08} |
| Raw goal margin distribution | {"-1": 0.25482673767074887, "-10": 2.559046730918768e-08, "-11": 2.130284357771332e-09, "-12": 1.5528189318982397e-10, "-2": 0.1039361818032359, "-3": 0.03035117757878911, "-4": 0.006778297780782942, "-5": 0.0012232491798645493, "-6": 0.00018503752013277272, "-7": 2.4080004742005965e-05, "-8": 2.7487456244787713e-06, "-9": 2.7939248750448286e-07, "0": 0.33518885878292964, "1": 0.1932559202914897, "10": 1.4839908765088015e-09, "11": 9.292357164874296e-11, "12": 5.0950028874211004e-12, "2": 0.05880812886574945, "3": 0.012917588629325695, "4": 0.002170010572837994, "5": 0.0002945719843988254, "6": 3.351749922240721e-05, "7": 3.280980718214146e-06, "8": 2.817195347405021e-07, "9": 2.1539342257082578e-08} |
| Unadjusted home-win probability | 26.7% |
| Unadjusted draw probability | 33.5% |
| Unadjusted away-win probability | 39.7% |
| Raw p over 1 5 | 47.3% |
| Raw p under 3 5 | 91.9% |
| Raw p btts yes | 29.5% |
| Home training matches | 2 |
| Away training matches | 22 |
| P home draw | 46.1% |
| P draw away | 79.5% |
| P home away | 74.3% |
| Raw p home draw | 60.3% |
| Raw p draw away | 73.3% |
| Raw p home away | 66.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:24Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.2, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:24Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.19, "price": 5.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 6.35 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.44 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +6.3% |
| Draw probability edge | +7.8% |
| Away probability edge | -14.1% |
| Over 2.5 probability edge | -43.2% |
| Under 2.5 probability edge | +43.2% |
| Raw edge prob home | 0.1259 |
| Raw ev home | 0.7172 |
| Raw edge prob draw | 0.1567 |
| Raw ev draw | 0.7597 |
| Raw edge prob away | -0.2827 |
| Raw ev away | -0.4278 |
| Market p home draw | 33.8% |
| Market home draw odds | 2.92 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:24Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.9% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:24Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.3% |
| Market home away odds | 1.19 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:24Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.84 |
| Market reference dc draw away odds | 1.13 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 86.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.0% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.3% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:24Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — NK Celje vs Salzburg

The model's most likely 1X2 outcome is **Salzburg win** at **43.0%**. Expected goals are 1.73 for NK Celje and 0.97 for Salzburg (2.70 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 49.5%; Under 3.5 goals: 73.4%; Double Chance 1X: 57.0%; Double Chance X2: 64.4%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NK Celje win | 35.6% | 2.81 |
| Draw | 21.3% | 4.69 |
| Salzburg win | 43.0% | 2.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NK Celje expected goals | 1.73 |
| Salzburg expected goals | 0.97 |
| Expected total goals | 2.70 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 72.3% |
| Under 1.5 | 27.7% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.07% |
| 2 | 1-2 | 10.89% |
| 3 | 1-1 | 10.12% |
| 4 | 1-0 | 7.79% |
| 5 | 2-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NK Celje win | 35.6% | 15.6% | 5.94 | +111.6% |
| Draw | 21.3% | 20.1% | 4.79 | +2.2% |
| Salzburg win | 43.0% | 64.4% | 1.51 | -35.0% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | salzburg |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7275 |
| Dc lambda away | 0.9732 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.22 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.75 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.28471876269706575, "-10": 3.251886169998667e-08, "-11": 2.8410867773043647e-09, "-12": 2.2796617333328562e-10, "-13": 1.6909987743998905e-11, "-14": 1.16595453749093e-12, "-15": 7.477100808335775e-14, "-16": 4.1153312633096244e-15, "-2": 0.10664565893218673, "-3": 0.030621238685598084, "-4": 0.006899520844096002, "-5": 0.001274130329040762, "-6": 0.00019891865525018313, "-7": 2.6865571789841747e-05, "-8": 3.1947867026006414e-06, "-9": 3.3920381909827584e-07, "0": 0.21336669544785355, "1": 0.1604175232292767, "10": 3.2622598643435136e-06, "11": 5.059335677724302e-07, "12": 7.206181285237886e-08, "13": 9.48863727871414e-09, "14": 1.161362897646065e-09, "15": 1.3220422804325912e-10, "16": 1.2916435697810147e-11, "2": 0.10852259620679872, "3": 0.055312785008591506, "4": 0.022123176299987127, "5": 0.007252173424194351, "6": 0.0020098128568221234, "7": 0.00048183902554719, "8": 0.00010171231284305351, "9": 1.9169826101476202e-05} |
| Raw goal margin distribution | {"-1": 0.14368685242005674, "-10": 1.6411046598027292e-08, "-11": 1.4337896548020998e-09, "-12": 1.1504595480191886e-10, "-13": 8.533834898622856e-12, "-14": 5.884134082698489e-13, "-15": 3.77341159465604e-14, "-16": 2.0768529277431767e-15, "-2": 0.05382005355415498, "-3": 0.015453387624538902, "-4": 0.0034819287071344964, "-5": 0.0006430056622140732, "-6": 0.00010038676478423659, "-7": 1.3558043777587735e-05, "-8": 1.6122887058853777e-06, "-9": 1.7118341142466575e-07, "0": 0.22609566294462827, "1": 0.25068440280307586, "10": 5.097932254648765e-06, "11": 7.906221947697693e-07, "12": 1.1261096765586227e-07, "13": 1.4827889882265342e-08, "14": 1.8148613603636564e-09, "15": 2.0659549709976845e-10, "16": 2.0184509173739268e-11, "2": 0.16958821999675228, "3": 0.08643726818694013, "4": 0.034571879226329344, "5": 0.01133296866371708, "6": 0.003140733790274899, "7": 0.000752969662758569, "8": 0.00015894579276316297, "9": 2.995667998949846e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 21.7% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 50.6% |
| Home training matches | 0 |
| Away training matches | 12 |
| P home draw | 57.0% |
| P draw away | 64.4% |
| P home away | 78.7% |
| Raw p home draw | 78.3% |
| Raw p draw away | 44.3% |
| Raw p home away | 77.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 4.74, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.21, "price": 4.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.92, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.85 |
| Reference draw odds | 4.60 |
| Reference away odds | 1.52 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +20.0% |
| Draw probability edge | +1.3% |
| Away probability edge | -21.3% |
| Over 2.5 probability edge | -15.1% |
| Under 2.5 probability edge | +15.1% |
| Raw edge prob home | 0.4009 |
| Raw ev home | 2.3068 |
| Raw edge prob draw | 0.0255 |
| Raw ev draw | 0.0830 |
| Raw edge prob away | -0.4264 |
| Raw ev away | -0.6720 |
| Market p home draw | 36.2% |
| Market home draw odds | 2.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:42Z |
| Market reference home draw last update utc | 2026-10-22T15:07:42Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.6% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:42Z |
| Market reference draw away last update utc | 2026-10-22T15:07:42Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.2% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:42Z |
| Market reference home away last update utc | 2026-10-22T15:07:42Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.68 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.10 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.8% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.30 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.6% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:42Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — OFI Crete vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **62.6%**. Expected goals are 1.00 for OFI Crete and 1.23 for Bayer Leverkusen (2.23 combined). The most likely exact score is 0-1 at 20.6%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 41.3%; Under 3.5 goals: 80.7%; Double Chance 1X: 37.4%; Double Chance X2: 82.0%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 41.9%; BTTS No (at least one team does not score): 58.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| OFI Crete win | 18.0% | 5.55 |
| Draw | 19.4% | 5.15 |
| Bayer Leverkusen win | 62.6% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| OFI Crete expected goals | 1.00 |
| Bayer Leverkusen expected goals | 1.23 |
| Expected total goals | 2.23 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 65.5% |
| Under 1.5 | 34.5% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 20.60% |
| 2 | 0-2 | 12.11% |
| 3 | 1-2 | 12.07% |
| 4 | 1-1 | 8.93% |
| 5 | 0-0 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| OFI Crete win | 18.0% | 5.6% | 13.58 | +144.5% |
| Draw | 19.4% | 11.5% | 7.84 | +52.2% |
| Bayer Leverkusen win | 62.6% | 82.9% | 1.20 | -24.9% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | ofi crete |
| Matched away-team name | leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9968 |
| Dc lambda away | 1.2342 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.9% |
| P btts no | 58.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.95 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.90 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 11.98 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.3542178017064746, "-10": 4.017549772151841e-07, "-11": 4.466466304406158e-08, "-12": 4.557678788742107e-09, "-13": 4.284083755955661e-10, "-14": 3.471720782292163e-11, "-2": 0.17907766933882274, "-3": 0.06717204484783873, "-4": 0.01956876410704587, "-5": 0.004645264727730911, "-6": 0.000928915993380764, "-7": 0.00016032079949259833, "-8": 2.4323916500276703e-05, "-9": 3.2911915504127642e-06, "0": 0.19417470795521932, "1": 0.11510565559986133, "10": 1.8960175543115992e-08, "11": 1.7023799163488663e-09, "12": 1.4029670660814597e-10, "13": 1.0650574928466735e-11, "14": 6.970617067755168e-13, "2": 0.04669085487755793, "3": 0.01414458788469884, "4": 0.0033279474825539308, "5": 0.0006380208510694692, "6": 0.00010304150195799345, "7": 1.4362728369162302e-05, "8": 1.7599159124654467e-06, "9": 1.923193181222705e-07} |
| Raw goal margin distribution | {"-1": 0.2392871700478326, "-10": 2.7140028278453306e-07, "-11": 3.01726247790616e-08, "-12": 3.078879870212908e-09, "-13": 2.8940563497144576e-10, "-14": 2.3452752436178715e-11, "-2": 0.12097356064096751, "-3": 0.045377190080595604, "-4": 0.013219420825125113, "-5": 0.0031380473975806604, "-6": 0.0006275169632847712, "-7": 0.0001083026042891526, "-8": 1.6431701387651076e-05, "-9": 2.223321099023165e-06, "0": 0.2730089189874967, "1": 0.19452614247288016, "10": 3.204229878879594e-08, "11": 2.8769863342062262e-09, "12": 2.370984900429597e-10, "13": 1.7999248126913945e-11, "14": 1.178019656618563e-12, "2": 0.0789065649360095, "3": 0.02390405670112369, "4": 0.005624161408575729, "5": 0.001078241849447034, "6": 0.00017413797598425163, "7": 2.427270954219134e-05, "8": 2.9742209602510166e-06, "9": 3.2501561180791394e-07} |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 42.3% |
| Raw p over 1 5 | 64.6% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 44.1% |
| Home training matches | 2 |
| Away training matches | 23 |
| P home draw | 37.4% |
| P draw away | 82.0% |
| P home away | 80.6% |
| Raw p home draw | 57.7% |
| Raw p draw away | 69.6% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 11.65, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.06, "price": 11.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.16, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 14.50 |
| Reference draw odds | 7.40 |
| Reference away odds | 1.19 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.35 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +12.4% |
| Draw probability edge | +7.9% |
| Away probability edge | -20.3% |
| Over 2.5 probability edge | -32.7% |
| Under 2.5 probability edge | +32.7% |
| Raw edge prob home | 0.2484 |
| Raw ev home | 3.1316 |
| Raw edge prob draw | 0.1577 |
| Raw ev draw | 1.1404 |
| Raw edge prob away | -0.4061 |
| Raw ev away | -0.4927 |
| Market p home draw | 19.2% |
| Market home draw odds | 5.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 92.9% |
| Market draw away odds | 1.05 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.9% |
| Market home away odds | 1.11 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 5.09 |
| Market reference dc draw away odds | 1.05 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 88.9% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 48.0% |
| Market under 3 5 odds | 2.02 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.96 |
| Market reference under 3 5 opposite odds | 1.82 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.1% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.90 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Olympiakos Piraeus vs Sparta Prague

The model's most likely 1X2 outcome is **Olympiakos Piraeus win** at **54.2%**. Expected goals are 1.18 for Olympiakos Piraeus and 0.89 for Sparta Prague (2.06 combined). The most likely exact score is 1-0 at 19.6%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 35.4%; Under 3.5 goals: 84.2%; Double Chance 1X: 78.9%; Double Chance X2: 45.8%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 38.9%; BTTS No (at least one team does not score): 61.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Olympiakos Piraeus win | 54.2% | 1.84 |
| Draw | 24.6% | 4.06 |
| Sparta Prague win | 21.1% | 4.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Olympiakos Piraeus expected goals | 1.18 |
| Sparta Prague expected goals | 0.89 |
| Expected total goals | 2.06 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 35.4% |
| Under 2.5 | 64.6% |
| Over 3.5 | 15.8% |
| Under 3.5 | 84.2% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.59% |
| 2 | 2-0 | 11.05% |
| 3 | 1-1 | 10.87% |
| 4 | 0-0 | 10.40% |
| 5 | 2-1 | 9.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Olympiakos Piraeus win | 54.2% | 65.2% | 1.51 | -18.1% |
| Draw | 24.6% | 20.7% | 4.55 | +12.0% |
| Sparta Prague win | 21.1% | 14.0% | 6.43 | +35.8% |
| Over 2.5 | 35.4% | 54.8% | 1.78 | -36.9% |
| Under 2.5 | 64.6% | 45.2% | 2.13 | +37.5% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
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
| Dc lambda away | 0.8856 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 38.9% |
| P btts no | 61.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.61 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.82 |
| Fair Under 2.5 odds | 1.55 |
| Fair Over 3.5 odds | 6.31 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.14 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.14141882610054324, "-10": 8.548979850157993e-09, "-11": 6.828813768130555e-10, "-12": 4.992833277161297e-11, "-13": 3.1487853046930533e-12, "-2": 0.05206797993488511, "-3": 0.014196452119373844, "-4": 0.0029922938152663575, "-5": 0.0005126178063742759, "-6": 7.386404281166072e-05, "-7": 9.176704086150488e-06, "-8": 1.0015549560003686e-06, "-9": 9.743797296168375e-08, "0": 0.24626112375050307, "1": 0.3122804774893905, "10": 2.474152151047327e-07, "11": 2.627845901350788e-08, "12": 2.5547252744753186e-09, "13": 2.1423119262008458e-10, "2": 0.15422071693546074, "3": 0.05591062229860155, "4": 0.015669720648268208, "5": 0.0035693835861263638, "6": 0.0006838724742284869, "7": 0.00011297212353513698, "8": 1.6394639224066527e-05, "9": 2.1207908235265952e-06} |
| Raw goal margin distribution | {"-1": 0.18894195732428676, "-10": 1.1421824311187191e-08, "-11": 9.123604509602619e-10, "-12": 6.670651411785864e-11, "-13": 4.206919793264856e-12, "-2": 0.06956517964464345, "-3": 0.018967103068639524, "-4": 0.00399784007501114, "-5": 0.0006848806086593999, "-6": 9.868570691428244e-05, "-7": 1.2260492323634078e-05, "-8": 1.3381227872731058e-06, "-9": 1.3018154539058736e-07, "0": 0.2851100145938042, "1": 0.24904570611839563, "10": 1.9731523867766056e-07, "11": 2.0957241494370182e-08, "12": 2.0374099752740188e-09, "13": 1.7085076552845874e-10, "2": 0.12299202196711742, "3": 0.04458908389605369, "4": 0.01249670384425022, "5": 0.002846606559465289, "6": 0.0005453927335081463, "7": 9.009600120922924e-05, "8": 1.3074831109968158e-05, "9": 1.6913444363249985e-06} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 28.2% |
| Raw p over 1 5 | 60.4% |
| Raw p under 3 5 | 84.6% |
| Raw p btts yes | 40.0% |
| Home training matches | 24 |
| Away training matches | 0 |
| P home draw | 78.9% |
| P draw away | 45.8% |
| P home away | 75.4% |
| Raw p home draw | 71.8% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 5.08, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.45 |
| Reference away odds | 6.45 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | -11.0% |
| Draw probability edge | +3.9% |
| Away probability edge | +7.1% |
| Over 2.5 probability edge | -19.3% |
| Under 2.5 probability edge | +19.3% |
| Raw edge prob home | -0.2197 |
| Raw ev home | -0.3467 |
| Raw edge prob draw | 0.0777 |
| Raw ev draw | 0.2973 |
| Raw edge prob away | 0.1420 |
| Raw ev away | 0.8150 |
| Market p home draw | 85.4% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:22Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.1% |
| Market draw away odds | 2.69 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:22Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:22Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.65 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 78.5% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.0% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 2.89 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.5% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:22Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Omonoia FC vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **66.7%**. Expected goals are 0.59 for Omonoia FC and 1.48 for Benfica (2.07 combined). The most likely exact score is 0-1 at 21.5%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 36.2%; Under 3.5 goals: 83.7%; Double Chance 1X: 33.3%; Double Chance X2: 87.3%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 93.6%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Omonoia FC win | 12.7% | 7.88 |
| Draw | 20.6% | 4.85 |
| Benfica win | 66.7% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Omonoia FC expected goals | 0.59 |
| Benfica expected goals | 1.48 |
| Expected total goals | 2.07 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 62.1% |
| Under 1.5 | 37.9% |
| Over 2.5 | 36.2% |
| Under 2.5 | 63.8% |
| Over 3.5 | 16.3% |
| Under 3.5 | 83.7% |
| Over 4.5 | 6.4% |
| Under 4.5 | 93.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 21.48% |
| 2 | 0-2 | 15.47% |
| 3 | 0-0 | 9.84% |
| 4 | 1-2 | 9.16% |
| 5 | 1-1 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Omonoia FC win | 12.7% | 10.1% | 8.84 | +12.1% |
| Draw | 20.6% | 16.1% | 5.82 | +19.9% |
| Benfica win | 66.7% | 73.9% | 1.33 | -11.3% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | benfica |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.5922 |
| Dc lambda away | 1.4827 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.17 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.64 |
| Fair Over 2.5 odds | 2.76 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 6.12 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.62 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.32079818621657397, "-10": 2.155363492261617e-06, "-11": 2.8860762952278176e-07, "-12": 3.546040085664441e-08, "-13": 4.0248374634667675e-09, "-14": 4.238401001152141e-10, "-15": 3.957763219885778e-11, "-2": 0.20518327515361942, "-3": 0.09475687960311122, "-4": 0.03368563404549382, "-5": 0.009710448552392913, "-6": 0.002351157657391388, "-7": 0.0004904002080394429, "-8": 8.98028365594903e-05, "-9": 1.4652356293551572e-05, "0": 0.20605118594133873, "1": 0.09748536270667273, "10": 1.6459974097320664e-10, "11": 8.8027048085335e-12, "12": 4.319681008049688e-13, "13": 1.9581956827777457e-14, "14": 8.235870158117002e-16, "15": 3.071545559682191e-17, "2": 0.024202093668379988, "3": 0.004463971734770711, "4": 0.0006338042064891596, "5": 7.297084716468904e-05, "6": 7.056535880297311e-06, "7": 5.878413794087027e-07, "8": 4.299315024090466e-08, "9": 2.80166619497154e-09} |
| Raw goal margin distribution | {"-1": 0.28631323674850406, "-10": 1.9236676650732876e-06, "-11": 2.575830790489412e-07, "-12": 3.1648502335393635e-08, "-13": 3.5921781701528582e-09, "-14": 3.78278419709866e-10, "-15": 3.532314228873697e-11, "-2": 0.18312662028653492, "-3": 0.08457076775689511, "-4": 0.03006451822324128, "-5": 0.008666601230215431, "-6": 0.0020984144796233244, "-7": 0.00043768349354419896, "-8": 8.014927112831713e-05, "-9": 1.3077267068981705e-05, "0": 0.2515028655128603, "1": 0.1176623088275081, "10": 1.9866762576030938e-10, "11": 1.0624636796147073e-11, "12": 5.213743137365113e-13, "13": 2.363491490152882e-14, "14": 9.940482048812137e-16, "15": 3.707275966224101e-17, "2": 0.029211300449788292, "3": 0.005387898308736625, "4": 0.0007649852676292774, "5": 8.807392326508565e-05, "6": 8.517056109215276e-06, "7": 7.095093253506534e-07, "8": 5.1891619220149025e-08, "9": 3.3815385603706295e-09} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 59.5% |
| Raw p over 1 5 | 60.8% |
| Raw p under 3 5 | 84.3% |
| Raw p btts yes | 34.0% |
| Home training matches | 0 |
| Away training matches | 8 |
| P home draw | 33.3% |
| P draw away | 87.3% |
| P home away | 79.4% |
| Raw p home draw | 40.5% |
| Raw p draw away | 84.7% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.24, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.70 |
| Reference draw odds | 5.60 |
| Reference away odds | 1.33 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +2.6% |
| Draw probability edge | +4.5% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | -29.2% |
| Under 2.5 probability edge | +29.2% |
| Raw edge prob home | 0.0525 |
| Raw ev home | 0.3536 |
| Raw edge prob draw | 0.0909 |
| Raw ev draw | 0.4637 |
| Raw edge prob away | -0.1434 |
| Raw ev away | -0.2082 |
| Market p home draw | 27.1% |
| Market home draw odds | 3.59 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.2% |
| Market draw away odds | 1.09 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.8% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.59 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 84.8% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.42 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.3% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.86 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — SK Sturm Graz vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **40.5%**. Expected goals are 1.80 for SK Sturm Graz and 1.29 for Marseille (3.09 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.5%; Double Chance 1X: 59.5%; Double Chance X2: 63.7%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SK Sturm Graz win | 36.3% | 2.75 |
| Draw | 23.1% | 4.32 |
| Marseille win | 40.5% | 2.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SK Sturm Graz expected goals | 1.80 |
| Marseille expected goals | 1.29 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
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
| 1 | 1-1 | 10.54% |
| 2 | 1-2 | 9.84% |
| 3 | 0-1 | 9.23% |
| 4 | 2-1 | 6.93% |
| 5 | 2-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SK Sturm Graz win | 36.3% | 22.9% | 4.17 | +51.6% |
| Draw | 23.1% | 24.2% | 3.95 | -8.6% |
| Marseille win | 40.5% | 52.9% | 1.84 | -25.5% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | marseille |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7969 |
| Dc lambda away | 1.2929 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.68 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.23706776657716547, "-10": 2.904177296512336e-07, "-11": 3.355213583766769e-08, "-12": 3.5625102639086077e-09, "-13": 3.498756453288266e-10, "-14": 3.1946381778704935e-11, "-15": 2.704113116942397e-12, "-16": 1.9080125761712091e-13, "-2": 0.1115592260589418, "-3": 0.040927575394057475, "-4": 0.01193697222988727, "-5": 0.0028751985328359397, "-6": 0.0005882659294909438, "-7": 0.00010444998525757563, "-8": 1.6365126869374415e-05, "-9": 2.2929193819208925e-06, "0": 0.23144409962843918, "1": 0.1655444898045131, "10": 3.9604968907855205e-06, "11": 6.359451662209489e-07, "12": 9.38487671894124e-08, "13": 1.2810294347883939e-08, "14": 1.6256985647445397e-09, "15": 1.9125647548078083e-10, "16": 1.87562267699167e-11, "2": 0.10925679461842416, "3": 0.05570984216962088, "4": 0.022583073236460416, "5": 0.0075601366610648394, "6": 0.002149851452439509, "7": 0.0005305375018275952, "8": 0.00011553139839581652, "9": 2.2497921004346815e-05} |
| Raw goal margin distribution | {"-1": 0.16470730972629344, "-10": 2.017732045073397e-07, "-11": 2.3310980270253644e-08, "-12": 2.4751213119886566e-09, "-13": 2.430827147566021e-10, "-14": 2.2195352300443835e-11, "-15": 1.8787336765253187e-12, "-16": 1.325627785179314e-13, "-2": 0.07750787998137562, "-3": 0.028435206245472584, "-4": 0.00829343698069657, "-5": 0.0019975985015164345, "-6": 0.00040870886856122894, "-7": 7.256860062047493e-05, "-8": 1.1369981077148121e-05, "-9": 1.5930490604783993e-06, "0": 0.22045923429267664, "1": 0.22686005335822254, "10": 5.427414328496625e-06, "11": 8.714911291348525e-07, "12": 1.2860915127610045e-07, "13": 1.755506367338032e-08, "14": 2.227836538551328e-09, "15": 2.6209542995911093e-10, "16": 2.570329348229519e-11, "2": 0.14972411516779063, "3": 0.07634405580096693, "4": 0.030947554977310932, "5": 0.01036031467039422, "6": 0.0029461289577720697, "7": 0.0007270418128400015, "8": 0.00015832275200204505, "9": 3.083086344657091e-05} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 22.0% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 80.9% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 60.0% |
| Home training matches | 0 |
| Away training matches | 16 |
| P home draw | 59.5% |
| P draw away | 63.7% |
| P home away | 76.9% |
| Raw p home draw | 71.9% |
| Raw p draw away | 50.2% |
| Raw p home away | 78.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.11, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.41, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.10 |
| Reference draw odds | 3.88 |
| Reference away odds | 1.84 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | +13.5% |
| Draw probability edge | -1.1% |
| Away probability edge | -12.4% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | 0.2693 |
| Raw ev home | 1.0771 |
| Raw edge prob draw | -0.0220 |
| Raw ev draw | -0.1292 |
| Raw edge prob away | -0.2473 |
| Raw ev away | -0.4822 |
| Market p home draw | 47.9% |
| Market home draw odds | 2.04 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:26Z |
| Market reference home draw last update utc | 2026-10-22T15:07:29Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 76.7% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:26Z |
| Market reference draw away last update utc | 2026-10-22T15:07:29Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:26Z |
| Market reference home away last update utc | 2026-10-22T15:07:29Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.00 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 85.7% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.77 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.7% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.7% |
| Market btts yes odds | 1.50 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:26Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.72 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — TSG Hoffenheim vs Lyon

The model's most likely 1X2 outcome is **Lyon win** at **39.9%**. Expected goals are 1.08 for TSG Hoffenheim and 1.60 for Lyon (2.67 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 49.5%; Under 3.5 goals: 72.7%; Double Chance 1X: 60.1%; Double Chance X2: 63.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 87.0%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 36.4% | 2.75 |
| Draw | 23.7% | 4.22 |
| Lyon win | 39.9% | 2.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.08 |
| Lyon expected goals | 1.60 |
| Expected total goals | 2.67 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 73.3% |
| Under 1.5 | 26.7% |
| Over 2.5 | 49.5% |
| Under 2.5 | 50.5% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 13.0% |
| Under 4.5 | 87.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 1-0 | 11.13% |
| 3 | 0-1 | 9.26% |
| 4 | 2-1 | 8.87% |
| 5 | 1-2 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 36.4% | 46.6% | 2.01 | -26.8% |
| Draw | 23.7% | 23.7% | 4.17 | -1.1% |
| Lyon win | 39.9% | 29.8% | 3.37 | +34.4% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | __LEAGUE_AVERAGE__ |
| Matched away-team name | lyon |
| Home-name matching confidence | 0/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0776 |
| Dc lambda away | 1.5962 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.89 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.75 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.68 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19321981674557362, "-10": 1.9024932296967849e-06, "-11": 2.7255604888555893e-07, "-12": 3.586252191409879e-08, "-13": 4.3615068725353715e-09, "-14": 4.905695905047288e-10, "-15": 4.6832834005953725e-11, "-2": 0.12004394091758694, "-3": 0.05639684113263713, "-4": 0.020809065273118068, "-5": 0.006295917385585247, "-6": 0.0016108761778456096, "-7": 0.0003566233007592611, "-8": 6.952508223454344e-05, "-9": 1.2102880844637182e-05, "0": 0.23716271492131155, "1": 0.22940370592896855, "10": 6.502839920401156e-08, "11": 6.2893376358502e-09, "12": 5.586747632513468e-10, "13": 4.586949196064395e-11, "14": 3.4830293521922548e-12, "15": 2.244791926805701e-13, "2": 0.09509705167321421, "3": 0.030161346729113667, "4": 0.00751307396455604, "5": 0.001534593146879501, "6": 0.000265073025303438, "7": 3.961705906045405e-05, "8": 5.214145797096476e-06, "9": 6.127729121844685e-07} |
| Raw goal margin distribution | {"-1": 0.24215943168770013, "-10": 2.3843655741570025e-06, "-11": 3.4159031414506266e-07, "-12": 4.4945948463667616e-08, "-13": 5.466209643216419e-09, "-14": 6.148233407980101e-10, "-15": 5.869487228703706e-11, "-2": 0.15044922927565418, "-3": 0.07068129567498814, "-4": 0.026079682226000073, "-5": 0.00789057665888176, "-6": 0.002018886397454798, "-7": 0.0004469505110449949, "-8": 8.713471881679211e-05, "-9": 1.5168354863831186e-05, "0": 0.23769451452101828, "1": 0.16540994908200554, "10": 4.6888275660858005e-08, "11": 4.534883226462094e-09, "12": 4.028285583643547e-10, "13": 3.3073878640726326e-11, "14": 2.511414126743188e-12, "15": 1.6185916300218751e-13, "2": 0.06856906871411123, "3": 0.02174762960565324, "4": 0.005417249808123637, "5": 0.0011065077316821106, "6": 0.0001911290641138597, "7": 2.8565605317629725e-05, "8": 3.7596236177236507e-06, "9": 4.418356529717502e-07} |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 50.0% |
| Raw p over 1 5 | 74.1% |
| Raw p under 3 5 | 72.0% |
| Raw p btts yes | 52.0% |
| Home training matches | 0 |
| Away training matches | 24 |
| P home draw | 60.1% |
| P draw away | 63.6% |
| P home away | 76.3% |
| Raw p home draw | 50.0% |
| Raw p draw away | 73.8% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 4.05 |
| Reference away odds | 3.24 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.68 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | -10.2% |
| Draw probability edge | +0.1% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | -16.6% |
| Under 2.5 probability edge | +16.6% |
| Raw edge prob home | -0.2031 |
| Raw ev home | -0.4724 |
| Raw edge prob draw | 0.0011 |
| Raw ev draw | -0.0088 |
| Raw edge prob away | 0.2020 |
| Raw ev away | 0.6844 |
| Market p home draw | 71.4% |
| Market home draw odds | 1.35 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:42Z |
| Market reference home draw last update utc | 2026-10-22T15:07:42Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.1% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:42Z |
| Market reference draw away last update utc | 2026-10-22T15:07:42Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:42Z |
| Market reference home away last update utc | 2026-10-22T15:07:42Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.85 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 85.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.0% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.69 |
| Market reference under 3 5 opposite odds | 2.20 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.5% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:42Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.96 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Union Saint-Gilloise vs Hapoel Be'er Sheva

The model's most likely 1X2 outcome is **Union Saint-Gilloise win** at **65.4%**. Expected goals are 1.66 for Union Saint-Gilloise and 0.77 for Hapoel Be'er Sheva (2.43 combined). The most likely exact score is 1-0 at 16.7%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.6%; Double Chance 1X: 85.6%; Double Chance X2: 34.6%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 42.1%; BTTS No (at least one team does not score): 57.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Saint-Gilloise win | 65.4% | 1.53 |
| Draw | 20.3% | 4.93 |
| Hapoel Be'er Sheva win | 14.4% | 6.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Saint-Gilloise expected goals | 1.66 |
| Hapoel Be'er Sheva expected goals | 0.77 |
| Expected total goals | 2.43 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.74% |
| 2 | 2-0 | 13.37% |
| 3 | 2-1 | 10.34% |
| 4 | 1-1 | 9.39% |
| 5 | 3-0 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Saint-Gilloise win | 65.4% | 71.6% | 1.41 | -7.8% |
| Draw | 20.3% | 17.4% | 5.10 | +3.4% |
| Hapoel Be'er Sheva win | 14.4% | 10.9% | 7.62 | +9.4% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | union sg |
| Matched away-team name | __LEAGUE_AVERAGE__ |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 0/100 |
| Dc lambda home | 1.6594 |
| Dc lambda away | 0.7734 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 42.1% |
| P btts no | 57.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.87 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.55 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.10277541550295004, "-10": 1.6775309868286215e-09, "-11": 1.1682157991574005e-10, "-12": 7.468281446871573e-12, "-13": 4.4118030770617864e-13, "-14": 2.4149384763062428e-14, "-15": 1.1470278901841095e-15, "-2": 0.03180692029207501, "-3": 0.007449503447810684, "-4": 0.0013567979353569456, "-5": 0.00020150371160681732, "-6": 2.5220680071128642e-05, "-7": 2.725206960568378e-06, "-8": 2.589140103482708e-07, "-9": 2.1940521569333494e-08, "0": 0.2026872276640263, "1": 0.29543900293761255, "10": 4.758772421181537e-06, "11": 7.110322071761348e-07, "12": 9.752785817828958e-08, "13": 1.2361351117406944e-08, "14": 1.4517696299456477e-09, "15": 1.479474304485266e-10, "2": 0.20091460293732324, "3": 0.1009622501463606, "4": 0.03945378580385897, "5": 0.012571826279958724, "6": 0.0033760893115024693, "7": 0.000782705591230487, "8": 0.0001595498172344135, "9": 2.900878368691891e-05} |
| Raw goal margin distribution | {"-1": 0.1274831513506989, "-10": 2.080818020951926e-09, "-11": 1.4490608557061556e-10, "-12": 9.263694526185757e-12, "-13": 5.472423114518109e-13, "-14": 2.9955020446376886e-14, "-15": 1.4227792649849842e-15, "-2": 0.039453466704572206, "-3": 0.009240402200052822, "-4": 0.0016829791025311923, "-5": 0.0002499462350873407, "-6": 3.12838606289357e-05, "-7": 3.380360660338507e-06, "-8": 3.2115826344771705e-07, "-9": 2.7215135236853688e-08, "0": 0.23093045517513075, "1": 0.26707000893969696, "10": 4.301819937211592e-06, "11": 6.427566300954604e-07, "12": 8.816292262212089e-08, "13": 1.1174374813774147e-08, "14": 1.3123660863756695e-09, "15": 1.3374104698301104e-10, "2": 0.1816221428756904, "3": 0.09126753333531383, "4": 0.03566530763565624, "5": 0.011364639480880942, "6": 0.0030519064633946795, "7": 0.0007075477075422535, "8": 0.00014422933563758308, "9": 2.6223267887995037e-05} |
| Unadjusted home-win probability | 59.1% |
| Unadjusted draw probability | 23.1% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 77.2% |
| Raw p btts yes | 43.0% |
| Home training matches | 28 |
| Away training matches | 0 |
| P home draw | 85.6% |
| P draw away | 34.6% |
| P home away | 79.7% |
| Raw p home draw | 82.2% |
| Raw p draw away | 40.9% |
| Raw p home away | 76.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:42Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.14, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:42Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 5.20 |
| Reference away odds | 8.10 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:26Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:26Z |
| Home probability edge | -6.3% |
| Draw probability edge | +2.8% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -17.9% |
| Under 2.5 probability edge | +17.9% |
| Raw edge prob home | -0.1255 |
| Raw ev home | -0.1668 |
| Raw edge prob draw | 0.0565 |
| Raw ev draw | 0.1777 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.3575 |
| Market p home draw | 87.6% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:42Z |
| Market reference home draw last update utc | 2026-10-22T15:07:42Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 31.4% |
| Market draw away odds | 3.10 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:42Z |
| Market reference draw away last update utc | 2026-10-22T15:07:42Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:42Z |
| Market reference home away last update utc | 2026-10-22T15:07:42Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 3.10 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 82.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.8% |
| Market btts yes odds | 1.79 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:42Z |
| Market reference btts yes odds | 1.84 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-22 — Viktoria Plzeň vs PFC Levski Sofia

The model's most likely 1X2 outcome is **Viktoria Plzeň win** at **52.3%**. Expected goals are 1.33 for Viktoria Plzeň and 0.84 for PFC Levski Sofia (2.17 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 37.7%; Under 3.5 goals: 82.3%; Double Chance 1X: 77.5%; Double Chance X2: 47.7%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 40.7%; BTTS No (at least one team does not score): 59.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Viktoria Plzeň win | 52.3% | 1.91 |
| Draw | 25.2% | 3.96 |
| PFC Levski Sofia win | 22.5% | 4.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Viktoria Plzeň expected goals | 1.33 |
| PFC Levski Sofia expected goals | 0.84 |
| Expected total goals | 2.17 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 63.6% |
| Under 1.5 | 36.4% |
| Over 2.5 | 37.7% |
| Under 2.5 | 62.3% |
| Over 3.5 | 17.7% |
| Under 3.5 | 82.3% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.90% |
| 2 | 1-1 | 11.36% |
| 3 | 2-0 | 10.82% |
| 4 | 0-0 | 10.08% |
| 5 | 0-1 | 9.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Viktoria Plzeň win | 52.3% | 55.7% | 1.73 | -9.5% |
| Draw | 25.2% | 23.6% | 4.05 | +2.2% |
| PFC Levski Sofia win | 22.5% | 20.7% | 4.72 | +6.0% |
| Over 2.5 | 37.7% | 55.0% | 1.77 | -33.3% |
| Under 2.5 | 62.3% | 45.0% | 2.14 | +33.4% |

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
| Market best home last update utc | 2026-10-22T15:06:57Z |
| Market best draw last update utc | 2026-10-22T15:06:57Z |
| Market best away last update utc | 2026-10-22T15:06:57Z |
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
| Dc lambda away | 0.8396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 40.7% |
| P btts no | 59.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.93 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.74 |
| Fair Over 2.5 odds | 2.66 |
| Fair Under 2.5 odds | 1.60 |
| Fair Over 3.5 odds | 5.64 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.01 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.15445162335334534, "-10": 5.605262985843855e-09, "-11": 4.2424379053551865e-10, "-12": 2.946923102691297e-11, "-13": 1.886419277271745e-12, "-14": 1.0474548834758775e-13, "-2": 0.05322384378451144, "-3": 0.013683135975668939, "-4": 0.0027247251082779507, "-5": 0.0004414549097033768, "-6": 6.0197455495898276e-05, "-7": 7.0805018495338235e-06, "-8": 7.318246420003154e-07, "-9": 6.743769375232424e-08, "0": 0.2523081691607386, "1": 0.2785649342409107, "10": 6.636012802628153e-07, "11": 7.982611363592639e-08, "12": 8.812853786071637e-09, "13": 8.966114011069283e-10, "14": 7.912607563188555e-11, "2": 0.15476448221917227, "3": 0.06323666762289773, "4": 0.020013557656524725, "5": 0.005153546796307773, "6": 0.0011169051072866213, "7": 0.00020879517233472668, "8": 3.4299019971287365e-05, "9": 5.02337571506219e-06} |
| Raw goal margin distribution | {"-1": 0.16631171490906763, "-10": 6.035682108431661e-09, "-11": 4.5682078835824127e-10, "-12": 3.1732125844511205e-11, "-13": 2.0312743772387972e-12, "-14": 1.1278872580200537e-13, "-2": 0.057310817080918, "-3": 0.01473384196319727, "-4": 0.002933952363691267, "-5": 0.00047535352166439996, "-6": 6.481992121106623e-05, "-7": 7.624202189955743e-06, "-8": 7.88020278332353e-07, "-9": 7.261612570949154e-08, "0": 0.2688491954463675, "1": 0.26057232455125456, "10": 6.207390339507973e-07, "11": 7.467011613176376e-08, "12": 8.24362837779515e-09, "13": 8.386989469519449e-10, "14": 7.40152938351807e-11, "2": 0.14476818842871594, "3": 0.05915218842700108, "4": 0.01872087474079256, "5": 0.004820677347839604, "6": 0.0010447638031036183, "7": 0.00019530901675976017, "8": 3.208363388630588e-05, "9": 4.6989140637351584e-06} |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 63.3% |
| Raw p under 3 5 | 82.4% |
| Raw p btts yes | 41.2% |
| Home training matches | 24 |
| Away training matches | 0 |
| P home draw | 77.5% |
| P draw away | 47.7% |
| P home away | 74.8% |
| Raw p home draw | 75.8% |
| Raw p draw away | 51.1% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:07:21Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.13, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.6, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:07:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.13, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.75 |
| Reference draw odds | 3.98 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-22T15:07:29Z |
| Market reference home last update utc | 2026-10-22T15:07:29Z |
| Market reference draw last update utc | 2026-10-22T15:07:29Z |
| Market reference away last update utc | 2026-10-22T15:07:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:07:29Z |
| Market best over 2 5 last update utc | 2026-10-22T15:07:21Z |
| Market best under 2 5 last update utc | 2026-10-22T15:07:21Z |
| Home probability edge | -3.4% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -17.4% |
| Under 2.5 probability edge | +17.4% |
| Raw edge prob home | -0.0676 |
| Raw ev home | -0.1535 |
| Raw edge prob draw | 0.0331 |
| Raw ev draw | 0.0888 |
| Raw edge prob away | 0.0345 |
| Raw ev away | 0.1415 |
| Market p home draw | 79.4% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:07:41Z |
| Market reference home draw last update utc | 2026-10-22T15:07:41Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.3% |
| Market draw away odds | 2.19 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:07:41Z |
| Market reference draw away last update utc | 2026-10-22T15:07:41Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:07:41Z |
| Market reference home away last update utc | 2026-10-22T15:07:41Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.19 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 79.1% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-22T15:07:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.6% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:07:43Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-22T15:07:44Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:07:41Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-22T15:07:44Z |
| Market btts yes bookmakers | 2 |

</details>


---
