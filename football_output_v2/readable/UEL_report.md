# UEFA Europa League — football model report

Fixtures in this report: **18**.

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
| Training as of utc | 2026-11-04T10:20:21.270738+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 794.123 |
| Base scoring parameter | 0.103 |
| Home-advantage parameter | 0.267 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 108, 'matches': 714, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-22'} |
| Training data health | {'training_end': '2026-10-22', 'verified_at_utc': '2026-11-04T00:36:38.177871+00:00', 'official_source_health': {'2025': {'status': 'REVIEWED_HISTORICAL_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 17 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 16, 'ANCHORED_MAIN': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 18} |
| Legacy comparison status | {'None': 18} |
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

## 2026-11-04 — Rennes vs Olympiakos Piraeus

The model's most likely 1X2 outcome is **Rennes win** at **47.0%**. Expected goals are 1.47 for Rennes and 0.71 for Olympiakos Piraeus (2.18 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 54.5%; Under 3.5 goals: 66.5%; Double Chance 1X: 73.4%; Double Chance X2: 53.0%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 47.0% | 2.13 |
| Draw | 26.4% | 3.79 |
| Olympiakos Piraeus win | 26.6% | 3.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.47 |
| Olympiakos Piraeus expected goals | 0.71 |
| Expected total goals | 2.18 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.38% |
| 2 | 1-0 | 8.03% |
| 3 | 0-1 | 7.92% |
| 4 | 2-0 | 7.72% |
| 5 | 2-1 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 47.0% | 43.2% | 2.26 | +6.2% |
| Draw | 26.4% | 26.8% | 3.67 | -3.2% |
| Olympiakos Piraeus win | 26.6% | 30.0% | 3.22 | -14.2% |
| Over 2.5 | 54.5% | 54.4% | 1.79 | -2.5% |
| Under 2.5 | 45.5% | 45.6% | 2.12 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T15:30:00+00:00 |
| Fixture id | 29ebc4d234c1c6e86ebea07ab9174818 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:20:08Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | rennes |
| Matched away-team name | olympiacos |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4654 |
| Dc lambda away | 0.7118 |
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
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.80 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.57 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.97 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.17789662014575494, "-10": 1.9620650022325004e-08, "-11": 1.7212163278068336e-09, "-12": 1.387181250262858e-10, "-13": 1.0337848184019884e-11, "-14": 7.163920820736216e-13, "-15": 4.6377786392832966e-14, "-16": 2.8021856053742777e-15, "-17": 1.4461588399208275e-16, "-2": 0.0649683973736095, "-3": 0.018431589583217892, "-4": 0.004128754997357709, "-5": 0.0007607125484650397, "-6": 0.00011875477691751794, "-7": 1.6061120946431904e-05, "-8": 1.9145447361929292e-06, "-9": 2.039127415313086e-07, "0": 0.26368366315408565, "1": 0.18529733869548137, "10": 1.3876396841833782e-05, "11": 2.50626632868213e-06, "12": 4.158659991917374e-07, "13": 6.380853833632531e-08, "14": 9.103908108417546e-09, "15": 1.2134322864930413e-09, "16": 1.5094921892684392e-10, "17": 1.603904149637528e-11, "2": 0.1423108254898588, "3": 0.0831241117316175, "4": 0.03833643995431032, "5": 0.014542587661931701, "6": 0.004674128419726377, "7": 0.0013015289921217109, "8": 0.00031942724434704325, "9": 7.004533904813612e-05} |
| Raw goal margin distribution | {"-1": 0.1366617094926815, "-10": 1.1455515621835446e-09, "-11": 7.354529925069733e-11, "-12": 4.333354095634938e-12, "-13": 2.3589420167922296e-13, "-14": 1.1908583204904426e-14, "-15": 5.283272599317353e-16, "-2": 0.04009367931607408, "-3": 0.008785321731544686, "-4": 0.0014881808584232602, "-5": 0.00020488932196836685, "-6": 2.372647317873773e-05, "-7": 2.3689806928572693e-06, "-8": 2.07789883036435e-07, "-9": 1.6246237252579886e-08, "0": 0.25442507801121544, "1": 0.2751084276593263, "10": 1.5678303315498922e-06, "11": 2.072372314044385e-07, "12": 2.5140012118511426e-08, "13": 2.8176497853504593e-09, "14": 2.9285880352940606e-10, "15": 2.675036115424422e-11, "2": 0.1699545501985152, "3": 0.07667309540300216, "4": 0.026740497458421456, "5": 0.007579866127615958, "6": 0.001807190102727036, "7": 0.0003715015374434622, "8": 6.708909520330922e-05, "9": 1.0799627333426921e-05} |
| Unadjusted home-win probability | 55.8% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 18.7% |
| Raw p over 1 5 | 63.4% |
| Raw p under 3 5 | 82.4% |
| Raw p btts yes | 38.6% |
| Home training matches | 19 |
| Away training matches | 25 |
| P home draw | 73.4% |
| P draw away | 53.0% |
| P home away | 73.6% |
| Raw p home draw | 81.3% |
| Raw p draw away | 44.2% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3758 |
| Totals anchor target over 2 5 | 0.5447 |
| Totals anchor reference over odds | 1.78 |
| Totals anchor reference under odds | 2.11 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3609 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.34, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.64, "price": 2.34, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.67, "home": 2.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.79, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.31, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.22, "draw": 3.6, "home": 2.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.78, "under": 2.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.32, "home_draw": 1.38}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.22 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:04Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:04Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.1262 |
| Raw ev home | 0.2618 |
| Raw edge prob draw | -0.0132 |
| Raw ev draw | -0.0663 |
| Raw edge prob away | -0.1129 |
| Raw ev away | -0.3970 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:42Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.1% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:11Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:11Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.69 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 79.2% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 4.24 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.7% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.88 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,490.6687 |
| Elo away rating | 1,481.7280 |
| Elo rating diff | 68.9408 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-05 — AC Milan vs Ferencváros TC

The model's most likely 1X2 outcome is **AC Milan win** at **75.1%**. Expected goals are 2.92 for AC Milan and 1.00 for Ferencváros TC (3.92 combined). The most likely exact score is 2-0 at 11.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.7%; Double Chance 1X: 90.0%; Double Chance X2: 24.9%; Double Chance 12 (either team wins): 85.1%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 75.1% | 1.33 |
| Draw | 14.9% | 6.70 |
| Ferencváros TC win | 10.0% | 10.02 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 2.92 |
| Ferencváros TC expected goals | 1.00 |
| Expected total goals | 3.92 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.3% |
| Under 3.5 | 58.7% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.70% |
| 2 | 1-0 | 10.07% |
| 3 | 2-1 | 9.69% |
| 4 | 3-0 | 9.45% |
| 5 | 3-1 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 75.1% | 74.4% | 1.33 | -0.1% |
| Draw | 14.9% | 15.7% | 5.50 | -17.9% |
| Ferencváros TC win | 10.0% | 9.9% | 10.20 | +1.8% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | milan |
| Matched away-team name | ferencvaros |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9240 |
| Dc lambda away | 0.9998 |
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
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.26 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.04 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.74 |
| Fair Over 3.5 odds | 2.42 |
| Fair Under 3.5 odds | 1.70 |
| Fair Over 4.5 odds | 4.32 |
| Fair Under 4.5 odds | 1.30 |
| Goal margin distribution | {"-1": 0.0715351264531017, "-10": 1.7159308300460014e-09, "-11": 1.2726923882423497e-10, "-12": 8.672366503029421e-12, "-13": 5.464656065652535e-13, "-14": 3.202021995281329e-14, "-15": 1.7531784791832342e-15, "-16": 9.00598637662063e-17, "-17": 4.3357750402720375e-18, "-18": 1.794723645575172e-19, "-2": 0.021858002541957872, "-3": 0.005234089269390825, "-4": 0.000990249623740543, "-5": 0.00015415410631352787, "-6": 2.0337419160608534e-05, "-7": 2.3248664297039797e-06, "-8": 2.3426731596925622e-07, "-9": 2.109347678984201e-08, "0": 0.14934636808762358, "1": 0.23598423475633848, "10": 9.154586399622356e-05, "11": 1.985885159685796e-05, "12": 3.957856465400357e-06, "13": 7.294188518859387e-07, "14": 1.250058086721e-07, "15": 2.001814114773127e-08, "16": 3.0076038702534902e-09, "17": 4.234945477544668e-10, "18": 5.12708361636097e-11, "2": 0.21777877856626837, "3": 0.15252391494870401, "4": 0.08439821040758891, "5": 0.03842690288324572, "6": 0.014827497440541229, "7": 0.004957488982093722, "8": 0.0014610570901776824, "9": 0.0003847648468485232} |
| Raw goal margin distribution | {"-1": 0.06958845388596255, "-10": 7.067292116243584e-09, "-11": 6.286525263979483e-10, "-12": 5.142614108937123e-11, "-13": 3.8931970554568575e-12, "-14": 2.7424477682232254e-13, "-15": 1.806080608333955e-14, "-16": 1.11663306653689e-15, "-17": 6.505071005242132e-17, "-18": 3.581054275747094e-18, "-19": 1.853673620101695e-19, "-2": 0.023797332263093492, "-20": 8.084413944974079e-21, "-3": 0.006528021562089018, "-4": 0.0014388959482986683, "-5": 0.0002636169387647649, "-6": 4.1195145144863835e-05, "-7": 5.602196534764065e-06, "-8": 6.735921832518481e-07, "-9": 7.252900711728348e-08, "0": 0.1305393386937577, "1": 0.19796938621130267, "10": 0.0003237206277474405, "11": 8.422087121270308e-05, "12": 2.0150449316273903e-05, "13": 4.461685118544834e-06, "14": 9.192266962476395e-07, "15": 1.7705701027413372e-07, "16": 3.2016821474147994e-08, "17": 5.455210389703203e-09, "18": 8.783388644085128e-10, "19": 1.3297689833661197e-10, "2": 0.20356904563825004, "20": 1.6962240050337384e-11, "3": 0.16332654668619617, "4": 0.10529222961820166, "5": 0.056419856619561615, "6": 0.02578673968593293, "7": 0.010256530420116443, "8": 0.0036068734393441782, "9": 0.0011358927572891935} |
| Unadjusted home-win probability | 76.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 10.2% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 59.5% |
| Home training matches | 9 |
| Away training matches | 33 |
| P home draw | 90.0% |
| P draw away | 24.9% |
| P home away | 85.1% |
| Raw p home draw | 89.8% |
| Raw p draw away | 23.2% |
| Raw p home away | 86.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8283 |
| Totals anchor target over 2 5 | 0.6357 |
| Totals anchor reference over odds | 1.47 |
| Totals anchor reference under odds | 2.36 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7440 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.91, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.11, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.09, "price": 6.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.18, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 10.2, "draw": 5.5, "home": 1.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.5, "home_away": 1.17, "home_draw": 1.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.21, "home_away": 1.14, "home_draw": 1.07}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.3, "draw": 4.9, "home": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.47, "under": 2.36}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.29 |
| Reference draw odds | 4.90 |
| Reference away odds | 7.30 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:43Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0242 |
| Raw ev home | 0.0212 |
| Raw edge prob draw | -0.0269 |
| Raw ev draw | -0.2820 |
| Raw edge prob away | 0.0027 |
| Raw ev away | 0.0370 |
| Market p home draw | 89.0% |
| Market home draw odds | 1.07 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:54Z |
| Market reference home draw last update utc | 2026-11-04T10:20:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.9% |
| Market draw away odds | 3.50 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.1% |
| Market home away odds | 1.17 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.29 |
| Market reference dc home draw odds | 1.07 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 85.6% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.61 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.5% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,446.6112 |
| Elo away rating | 1,471.6144 |
| Elo rating diff | 34.9969 |
| Elo home expectancy | 0.5502 |

</details>


---

## 2026-11-05 — AZ Alkmaar vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **53.6%**. Expected goals are 0.79 for AZ Alkmaar and 2.01 for Juventus (2.80 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 53.5%; Under 3.5 goals: 67.9%; Double Chance 1X: 46.4%; Double Chance X2: 77.0%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AZ Alkmaar win | 23.0% | 4.35 |
| Draw | 23.4% | 4.27 |
| Juventus win | 53.6% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AZ Alkmaar expected goals | 0.79 |
| Juventus expected goals | 2.01 |
| Expected total goals | 2.80 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 76.9% |
| Under 1.5 | 23.1% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 32.1% |
| Under 3.5 | 67.9% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.09% |
| 2 | 0-2 | 9.33% |
| 3 | 0-1 | 9.18% |
| 4 | 1-0 | 7.88% |
| 5 | 1-2 | 7.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AZ Alkmaar win | 23.0% | 26.7% | 3.64 | -16.4% |
| Draw | 23.4% | 25.1% | 3.78 | -11.5% |
| Juventus win | 53.6% | 48.2% | 2.03 | +8.8% |
| Over 2.5 | 53.5% | 53.1% | 1.83 | -2.1% |
| Under 2.5 | 46.5% | 46.9% | 2.06 | -4.2% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
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
| Dc lambda home | 0.7900 |
| Dc lambda away | 2.0098 |
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
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.55 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.33 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.24 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.1959354383242449, "-10": 2.433616301066017e-05, "-11": 4.622815100879463e-06, "-12": 8.065589624568659e-07, "-13": 1.3010237697300517e-07, "-14": 1.951169044266827e-08, "-15": 2.7334894506039648e-09, "-16": 3.5774332431139393e-10, "-17": 4.0368217842854635e-11, "-2": 0.1617092445385782, "-3": 0.10049923021348557, "-4": 0.049097851284356675, "-5": 0.01967858928783017, "-6": 0.006672067903400452, "-7": 0.0019577736972451634, "-8": 0.0005059547969986009, "-9": 0.00011676739802869932, "0": 0.23403735804936718, "1": 0.16297533228872874, "10": 4.406358399955298e-09, "11": 3.290033064277364e-10, "12": 2.25629503269295e-11, "13": 1.4305762924781668e-12, "14": 8.433089629896814e-14, "15": 4.6438186111420324e-15, "16": 2.3888859186188433e-16, "17": 1.0595695659114777e-17, "2": 0.051384761881165676, "3": 0.012552443115219063, "4": 0.0024104273107852948, "5": 0.0003797445428307412, "6": 5.060856976412877e-05, "7": 5.837032648038404e-06, "8": 5.929353967539725e-07, "9": 5.3787739008960005e-08} |
| Raw goal margin distribution | {"-1": 0.25347363328282385, "-10": 2.080581003149787e-05, "-11": 3.7567180198021764e-06, "-12": 6.229093491068711e-07, "-13": 9.547616048132467e-08, "-14": 1.3604211271686544e-08, "-15": 1.8106703966205592e-09, "-16": 2.2528785530230387e-10, "-17": 2.4359523417178444e-11, "-2": 0.20221674120600946, "-3": 0.12063296221837103, "-4": 0.05635605235633089, "-5": 0.021552918812394472, "-6": 0.006963456374440649, "-7": 0.0019453450204136018, "-8": 0.0004783564640523387, "-9": 0.00010499725522564936, "0": 0.19354273172081074, "1": 0.10256253288928086, "10": 1.8316601400903472e-09, "11": 1.2999746705560213e-10, "12": 8.472609064439925e-12, "13": 5.104500976673676e-13, "14": 2.8588919375217695e-14, "15": 1.4956493955822587e-15, "16": 7.314661040356665e-17, "17": 3.1087889460472346e-18, "2": 0.031242743293700116, "3": 0.007325952054511194, "4": 0.00134525517139231, "5": 0.00020222564340441852, "6": 2.568153738650117e-05, "7": 2.820063085140569e-06, "8": 2.725711331000517e-07, "9": 2.351647291932754e-08} |
| Unadjusted home-win probability | 14.3% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 66.4% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 46.8% |
| Home training matches | 15 |
| Away training matches | 11 |
| P home draw | 46.4% |
| P draw away | 77.0% |
| P home away | 76.6% |
| Raw p home draw | 33.6% |
| Raw p draw away | 85.7% |
| Raw p home away | 80.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0534 |
| Totals anchor target over 2 5 | 0.5350 |
| Totals anchor reference over odds | 1.79 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5038 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.78, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.64, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.49, "price": 2.64, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.03, "draw": 3.78, "home": 3.64}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.31, "home_away": 1.29, "home_draw": 1.84}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.01, "draw": 3.74, "home": 3.53}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.79, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.31, "home_away": 1.29, "home_draw": 1.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.53 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.01 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -3.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.1244 |
| Raw ev home | -0.4805 |
| Raw edge prob draw | -0.0578 |
| Raw ev draw | -0.2684 |
| Raw edge prob away | 0.1822 |
| Raw ev away | 0.3474 |
| Market p home draw | 52.4% |
| Market home draw odds | 1.84 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:42Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 73.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:11Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:11Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home draw odds | 1.83 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 78.1% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.92 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,483.3792 |
| Elo away rating | 1,491.7497 |
| Elo rating diff | 51.6295 |
| Elo home expectancy | 0.5738 |

</details>


---

## 2026-11-05 — Anderlecht vs Salzburg

The model's most likely 1X2 outcome is **Anderlecht win** at **50.7%**. Expected goals are 1.85 for Anderlecht and 1.24 for Salzburg (3.09 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 60.0%; Under 3.5 goals: 61.7%; Double Chance 1X: 74.4%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Anderlecht win | 50.7% | 1.97 |
| Draw | 23.6% | 4.23 |
| Salzburg win | 25.6% | 3.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Anderlecht expected goals | 1.85 |
| Salzburg expected goals | 1.24 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.71% |
| 2 | 2-1 | 9.34% |
| 3 | 1-0 | 8.41% |
| 4 | 2-0 | 7.42% |
| 5 | 2-2 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Anderlecht win | 50.7% | 50.2% | 1.93 | -2.1% |
| Draw | 23.6% | 24.4% | 4.00 | -5.5% |
| Salzburg win | 25.6% | 25.4% | 3.81 | -2.3% |
| Over 2.5 | 60.0% | 59.5% | 1.64 | -1.6% |
| Under 2.5 | 40.0% | 40.5% | 2.37 | -5.2% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
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
| Dc lambda home | 1.8460 |
| Dc lambda away | 1.2402 |
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
| Fair Under 0.5 odds | 23.76 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.15267726734032072, "-10": 1.465915645689274e-07, "-11": 1.6501394821491198e-08, "-12": 1.707221652926793e-09, "-13": 1.6337859584780657e-10, "-14": 1.4536300383670233e-11, "-15": 1.1986902234795618e-12, "-16": 8.225319810607744e-14, "-2": 0.06970305353692854, "-3": 0.024865126251492963, "-4": 0.007057083977624736, "-5": 0.0016548206329532883, "-6": 0.00032971062450917944, "-7": 5.7019957224620393e-05, "-8": 8.702723789091115e-06, "-9": 1.1879111451412819e-06, "0": 0.23621470072867767, "1": 0.22247506653253682, "10": 7.744426818375591e-06, "11": 1.2975966224636524e-06, "12": 1.9982402927644056e-07, "13": 2.8463723467773807e-08, "14": 3.769547253346226e-09, "15": 4.6268030897558627e-10, "16": 4.72569400721334e-11, "2": 0.15283474561650467, "3": 0.08115209087160694, "4": 0.034282547098824535, "5": 0.011965682466796865, "6": 0.0035486097319466824, "7": 0.0009134629459754805, "8": 0.00020751906339486903, "9": 4.216241769213493e-05} |
| Raw goal margin distribution | {"-1": 0.15676384761813572, "-10": 1.3320657082944953e-07, "-11": 1.4766297549857271e-08, "-12": 1.5043219884434889e-09, "-13": 1.4174885142617414e-10, "-14": 1.2417834126550699e-11, "-15": 1.0086743150104682e-12, "-16": 6.839905449507098e-14, "-2": 0.07089474066897783, "-3": 0.024998911162262095, "-4": 0.007003552189410781, "-5": 0.0016197431533158402, "-6": 0.0003181277252647497, "-7": 5.421453845025897e-05, "-8": 8.151874319925834e-06, "-9": 1.096029551716121e-06, "0": 0.2172514026888992, "1": 0.23078369793111672, "10": 7.110713085928581e-06, "11": 1.1732697493072914e-06, "12": 1.7791223361649248e-07, "13": 2.4953031095149277e-08, "14": 3.253781341029276e-09, "15": 3.9339806797888027e-10, "16": 3.97072773838226e-11, "2": 0.15706937645061245, "3": 0.08243987893694735, "4": 0.0343774272862022, "5": 0.011834227297079149, "6": 0.0034596648117410384, "7": 0.0008775806115727579, "8": 0.00019641175720195347, "9": 3.930710151755218e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 62.8% |
| Raw p btts yes | 59.3% |
| Home training matches | 13 |
| Away training matches | 13 |
| P home draw | 74.4% |
| P draw away | 49.3% |
| P home away | 76.4% |
| Raw p home draw | 73.8% |
| Raw p draw away | 47.9% |
| Raw p home away | 78.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0160 |
| Totals anchor target over 2 5 | 0.6000 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.35 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5900 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:15Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.77, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:15Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.45, "price": 2.77, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.81, "draw": 4.0, "home": 1.93}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.37}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.93, "home_away": 1.27, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.83, "home": 1.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.9, "home_away": 1.28, "home_draw": 1.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.83 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.37 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0195 |
| Raw ev home | 0.0057 |
| Raw edge prob draw | -0.0271 |
| Raw ev draw | -0.1310 |
| Raw edge prob away | 0.0076 |
| Raw ev away | -0.0031 |
| Market p home draw | 74.4% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:42Z |
| Market reference home draw last update utc | 2026-11-04T10:20:15Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.5% |
| Market draw away odds | 1.93 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:15Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market home away odds | 1.28 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:15Z |
| Market reference home away last update utc | 2026-11-04T10:20:15Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.90 |
| Market reference dc home draw odds | 1.29 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.83 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.5% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.50 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,445.9180 |
| Elo away rating | 1,427.7213 |
| Elo rating diff | 78.1968 |
| Elo home expectancy | 0.6107 |

</details>


---

## 2026-11-05 — Bayer Leverkusen vs Marseille

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **75.4%**. Expected goals are 2.87 for Bayer Leverkusen and 0.55 for Marseille (3.42 combined). The most likely exact score is 3-0 at 10.7%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 67.9%; Under 3.5 goals: 52.2%; Double Chance 1X: 90.0%; Double Chance X2: 24.6%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 45.7%; BTTS No (at least one team does not score): 54.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 75.4% | 1.33 |
| Draw | 14.6% | 6.84 |
| Marseille win | 10.0% | 9.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.87 |
| Marseille expected goals | 0.55 |
| Expected total goals | 3.42 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 67.9% |
| Under 2.5 | 32.1% |
| Over 3.5 | 47.8% |
| Under 3.5 | 52.2% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 10.67% |
| 2 | 2-0 | 10.24% |
| 3 | 4-0 | 8.34% |
| 4 | 1-1 | 6.90% |
| 5 | 1-0 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 75.4% | 71.4% | 1.41 | +6.3% |
| Draw | 14.6% | 16.4% | 5.62 | -17.9% |
| Marseille win | 10.0% | 12.2% | 7.46 | -25.3% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:20:08Z |
| Market best away last update utc | 2026-11-04T10:20:08Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | leverkusen |
| Matched away-team name | marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8657 |
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
| P btts yes | 45.7% |
| P btts no | 54.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.65 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.15 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.12 |
| Fair Over 3.5 odds | 2.09 |
| Fair Under 3.5 odds | 1.92 |
| Fair Over 4.5 odds | 3.45 |
| Fair Under 4.5 odds | 1.41 |
| Goal margin distribution | {"-1": 0.0790997028462832, "-10": 1.1050463474580781e-10, "-11": 5.9681298056887854e-12, "-12": 2.96093573332844e-13, "-13": 1.3582667651696071e-14, "-14": 5.793495682616959e-16, "-15": 2.308921792100698e-17, "-16": 8.634598247421317e-19, "-17": 3.0413964627964216e-20, "-18": 1.0122880186132986e-21, "-19": 3.181841914892204e-23, "-2": 0.017501597109273324, "-20": 8.759716996296253e-25, "-3": 0.003071844238917749, "-4": 0.0004249205698565776, "-5": 4.829382622694948e-05, "-6": 4.647409269126745e-06, "-7": 3.8728449113905205e-07, "-8": 2.8436714448120928e-08, "-9": 1.865180568879834e-09, "0": 0.1460970158142724, "1": 0.15185705779278624, "10": 0.0006108933214297306, "11": 0.00017122547080377314, "12": 4.408636730447606e-05, "13": 1.0495560406435215e-05, "14": 2.3233063035100273e-06, "15": 4.805296949457478e-07, "16": 9.326063498691487e-08, "17": 1.7048041504851007e-08, "18": 2.9447659239357444e-09, "19": 4.803640588078957e-10, "2": 0.18386572026666265, "20": 6.86320873295457e-11, "3": 0.16748175406596225, "4": 0.12023233739914149, "5": 0.07091700317817558, "6": 0.035417255494850565, "7": 0.015317197610884806, "8": 0.005836787082450406, "9": 0.0019868292334362047} |
| Raw goal margin distribution | {"-1": 0.039333783249323885, "-10": 2.7469268586323135e-11, "-11": 1.362756912827282e-12, "-12": 6.208396244149702e-14, "-13": 2.614522120724444e-15, "-14": 1.0235599492976395e-16, "-15": 3.7434533262209866e-18, "-16": 1.2844975096786587e-19, "-17": 4.150538021382812e-21, "-18": 1.2636011886179758e-22, "-19": 3.390015934800618e-24, "-2": 0.008214056327719332, "-3": 0.0013467468037649372, "-4": 0.00017289739996015927, "-5": 1.8169906766009292e-05, "-6": 1.613066097310889e-06, "-7": 1.238205785086609e-07, "-8": 8.365821386454699e-09, "-9": 5.045332665973083e-10, "0": 0.10397680680717772, "1": 0.1932651730398735, "10": 0.00038931339257332873, "11": 0.00010023418573793834, "12": 2.3698569144433563e-05, "13": 5.179409430511739e-06, "14": 1.052316624667084e-06, "15": 1.9973344596503078e-07, "16": 3.556778856206437e-08, "17": 5.964488676855367e-09, "18": 9.423756858724833e-10, "19": 1.3120821011465154e-10, "2": 0.22123209211108252, "3": 0.18824421037504918, "4": 0.12542074080589147, "5": 0.06840357860995763, "6": 0.031515449978274636, "7": 0.012554788544899904, "8": 0.004402206254587546, "9": 0.0013778337869265048} |
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
| Totals anchor scale | 1.0910 |
| Totals anchor target over 2 5 | 0.6791 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.86 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6302 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.11, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.15, "price": 6.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.43, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.4, "draw": 5.35, "home": 1.41}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.06, "home_away": 1.18, "home_draw": 1.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 3.23, "home_away": 1.17, "home_draw": 1.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.46, "draw": 5.62, "home": 1.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.43, "under": 2.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.38 |
| Reference draw odds | 5.62 |
| Reference away odds | 7.46 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.89 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:43Z |
| Home probability edge | +4.0% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.1331 |
| Raw ev home | 0.1942 |
| Raw edge prob draw | -0.0602 |
| Raw ev draw | -0.4157 |
| Raw edge prob away | -0.0729 |
| Raw ev away | -0.6338 |
| Market p home draw | 86.8% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:54Z |
| Market reference home draw last update utc | 2026-11-04T10:20:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 30.9% |
| Market draw away odds | 3.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:19:54Z |
| Market reference draw away last update utc | 2026-11-04T10:20:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.3% |
| Market home away odds | 1.18 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.09 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 87.1% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.77 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.77 |
| Market reference under 3 5 opposite odds | 2.11 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,523.2260 |
| Elo away rating | 1,423.2467 |
| Elo rating diff | 159.9793 |
| Elo home expectancy | 0.7152 |

</details>


---

## 2026-11-05 — Benfica vs Lech Poznań

The model's most likely 1X2 outcome is **Benfica win** at **89.9%**. Expected goals are 5.16 for Benfica and 0.20 for Lech Poznań (5.35 combined). The most likely exact score is 4-0 at 15.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 74.3%; Under 3.5 goals: 43.2%; Double Chance 1X: 96.8%; Double Chance X2: 10.1%; Double Chance 12 (either team wins): 93.1%; Under 4.5 goals: 61.4%; BTTS Yes (both teams score): 15.6%; BTTS No (at least one team does not score): 84.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 89.9% | 1.11 |
| Draw | 6.9% | 14.43 |
| Lech Poznań win | 3.2% | 31.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 5.16 |
| Lech Poznań expected goals | 0.20 |
| Expected total goals | 5.35 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 88.1% |
| Under 1.5 | 11.9% |
| Over 2.5 | 74.3% |
| Under 2.5 | 25.7% |
| Over 3.5 | 56.8% |
| Under 3.5 | 43.2% |
| Over 4.5 | 38.6% |
| Under 4.5 | 61.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-0 | 15.47% |
| 2 | 3-0 | 15.18% |
| 3 | 5-0 | 12.61% |
| 4 | 2-0 | 11.17% |
| 5 | 6-0 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Benfica win | 89.9% | 86.0% | 1.17 | +5.1% |
| Draw | 6.9% | 9.5% | 8.20 | -43.2% |
| Lech Poznań win | 3.2% | 4.5% | 17.00 | -45.4% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | benfica |
| Matched away-team name | lech poznan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.1577 |
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
| P btts yes | 15.6% |
| P btts no | 84.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.92 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.42 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.90 |
| Fair Over 3.5 odds | 1.76 |
| Fair Under 3.5 odds | 2.32 |
| Fair Over 4.5 odds | 2.59 |
| Fair Under 4.5 odds | 1.63 |
| Goal margin distribution | {"-1": 0.030163340970504236, "-10": 2.82924570447415e-16, "-11": 3.9530660450458935e-18, "-12": 5.066684530544362e-20, "-13": 5.997902659019433e-22, "-14": 6.5961242074472455e-24, "-15": 6.77292868981152e-26, "-16": 6.52181635442719e-28, "-17": 5.9121125551289066e-30, "-18": 5.062753389101447e-32, "-19": 4.107989295730799e-34, "-2": 0.0018397414272366681, "-20": 3.1671136038448585e-36, "-21": 2.325766892334851e-38, "-22": 1.629920957437217e-40, "-23": 1.0651897449151978e-42, "-3": 9.011446212709717e-05, "-4": 3.3748884534788527e-06, "-5": 1.0212118349278588e-07, "-6": 2.5899344731746785e-09, "-7": 5.650565236120521e-11, "-8": 1.0813381998582131e-12, "-9": 1.8425665065333717e-14, "0": 0.06930013750784496, "1": 0.07439559378645746, "10": 0.004966770089715195, "11": 0.001831737106379595, "12": 0.0006196958936982478, "13": 0.00019363321136664152, "14": 5.620758694597767e-05, "15": 1.5233801771013145e-05, "16": 3.8719170399342755e-06, "17": 9.264582491501987e-07, "18": 2.0940913028772144e-07, "19": 4.485014219931117e-08, "2": 0.13707388808926801, "20": 9.126911592941877e-09, "21": 1.7690987150731112e-09, "22": 3.2724883415774807e-10, "23": 5.6450035807984934e-11, "3": 0.1772221984265623, "4": 0.17518976455345545, "5": 0.13992355353810984, "6": 0.09366761111073772, "7": 0.05394090667700511, "8": 0.027246678999324946, "9": 0.01225464919004159} |
| Raw goal margin distribution | {"-1": 0.0017147194039197962, "-10": 1.1597541005482167e-16, "-11": 2.0446689558358438e-18, "-12": 3.308204640776782e-20, "-13": 4.945317183671053e-22, "-14": 6.869537974911052e-24, "-15": 8.911587784447601e-26, "-16": 1.0843418132627551e-27, "-17": 1.2422971427575209e-29, "-18": 1.344653763948875e-31, "-19": 1.3792448236272236e-33, "-2": 0.00012481579708355285, "-20": 1.3443266107139044e-35, "-21": 1.2481680733627588e-37, "-22": 1.1064196064532869e-39, "-23": 9.382815165181646e-42, "-24": 7.626445491541705e-44, "-25": 5.947581395826706e-46, "-26": 4.303112176095094e-48, "-3": 7.527049089088713e-06, "-4": 3.505969142053018e-07, "-5": 1.3266159410933006e-08, "-6": 4.220901953687843e-10, "-7": 1.1577042013157145e-11, "-8": 2.789128399151388e-13, "-9": 5.989149037674387e-15, "0": 0.010372116980605457, "1": 0.03920311919977586, "10": 0.019038061564497052, "11": 0.008859424151022654, "12": 0.0037835592446625508, "13": 0.001492890673515751, "14": 0.0005473776527032448, "15": 0.00018743051770229698, "16": 6.019731229005874e-05, "17": 1.8203800345426528e-05, "18": 5.200830861953206e-06, "19": 1.4080863939371282e-06, "2": 0.0869602774163961, "20": 3.6225835929250636e-07, "21": 8.877943381039822e-08, "22": 2.0772312402703642e-08, "23": 4.649688131996333e-09, "24": 9.97558824894082e-10, "25": 2.0534419011656768e-10, "26": 3.921483338150435e-11, "3": 0.1384209391296357, "4": 0.17018089893679975, "5": 0.16997052533700813, "6": 0.14274448900139464, "7": 0.10334212235043436, "8": 0.06571642897094392, "9": 0.03724742459398139} |
| Unadjusted home-win probability | 98.8% |
| Unadjusted draw probability | 1.0% |
| Unadjusted away-win probability | 0.2% |
| Raw p over 1 5 | 97.0% |
| Raw p under 3 5 | 21.9% |
| Raw p btts yes | 17.6% |
| Home training matches | 9 |
| Away training matches | 3 |
| P home draw | 96.8% |
| P draw away | 10.1% |
| P home away | 93.1% |
| Raw p home draw | 99.8% |
| Raw p draw away | 1.2% |
| Raw p home away | 99.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7903 |
| Totals anchor target over 2 5 | 0.7433 |
| Totals anchor reference over odds | 1.28 |
| Totals anchor reference under odds | 3.10 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8382 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 2.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 11.06, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.03, "price": 11.06, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.0, "draw": 8.2, "home": 1.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.42, "draw": 6.8, "home": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.28, "under": 3.1}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 5.03, "home_away": 1.08, "home_draw": 1.03}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.13 |
| Reference draw odds | 6.80 |
| Reference away odds | 12.42 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.50 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:46Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:46Z |
| Home probability edge | +3.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | 0.1274 |
| Raw ev home | 0.1557 |
| Raw edge prob draw | -0.0842 |
| Raw ev draw | -0.9149 |
| Raw edge prob away | -0.0432 |
| Raw ev away | -0.9686 |
| Market p home draw | 92.7% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.0% |
| Market draw away odds | 5.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:11Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.4% |
| Market home away odds | 1.08 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:11Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 5.03 |
| Market reference dc home draw odds | 1.03 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 90.2% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.8% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.92 |
| Market reference under 3 5 opposite odds | 1.72 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,490.8432 |
| Elo away rating | 1,407.9321 |
| Elo rating diff | 142.9112 |
| Elo home expectancy | 0.6948 |

</details>


---

## 2026-11-05 — Celta Vigo vs Union Saint-Gilloise

The model's most likely 1X2 outcome is **Celta Vigo win** at **39.0%**. Expected goals are 1.05 for Celta Vigo and 1.34 for Union Saint-Gilloise (2.39 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 55.6%; Under 3.5 goals: 66.1%; Double Chance 1X: 65.0%; Double Chance X2: 61.0%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 39.0% | 2.57 |
| Draw | 26.0% | 3.85 |
| Union Saint-Gilloise win | 35.0% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.05 |
| Union Saint-Gilloise expected goals | 1.34 |
| Expected total goals | 2.39 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 78.6% |
| Under 1.5 | 21.4% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 1-0 | 9.29% |
| 3 | 2-1 | 9.26% |
| 4 | 1-2 | 7.00% |
| 5 | 0-1 | 6.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 39.0% | 42.9% | 2.25 | -12.3% |
| Draw | 26.0% | 25.9% | 3.77 | -2.1% |
| Union Saint-Gilloise win | 35.0% | 31.2% | 3.21 | +12.5% |
| Over 2.5 | 55.6% | 56.6% | 1.72 | -4.4% |
| Under 2.5 | 44.4% | 43.4% | 2.22 | -1.4% |

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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
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
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.12 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.67 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.16925624766089775, "-10": 2.0955183384563038e-06, "-11": 3.115175651263635e-07, "-12": 4.255290112289565e-08, "-13": 5.373626054332361e-09, "-14": 6.260827853724101e-10, "-15": 6.062595141531839e-11, "-2": 0.10472273457397091, "-3": 0.049854667658790285, "-4": 0.018809372154311152, "-5": 0.005849655583519002, "-6": 0.0015435027749951754, "-7": 0.0003531605720490183, "-8": 7.126485439256371e-05, "-9": 1.2854790994047208e-05, "0": 0.2597720493011671, "1": 0.22548292631934957, "10": 3.039660803467343e-07, "11": 3.5346419858780674e-08, "12": 3.776776639607391e-09, "13": 3.730686904431259e-10, "14": 3.400026947308605e-11, "15": 2.5753626819021073e-12, "2": 0.10837790553352906, "3": 0.04035848358021671, "4": 0.011910570067703291, "5": 0.002897462208454879, "6": 0.0005980316005529331, "7": 0.00010703311497985848, "8": 1.6894704112823562e-05, "9": 2.3837979533542453e-06} |
| Raw goal margin distribution | {"-1": 0.23857357838288404, "-10": 5.384463146772458e-07, "-11": 6.494247252831282e-08, "-12": 7.190459200864921e-09, "-13": 7.328136973484119e-10, "-14": 6.377394134370714e-11, "-2": 0.1284804234858241, "-3": 0.051738853892107035, "-4": 0.016249196825550018, "-5": 0.004167993603778221, "-6": 0.0009018928161878354, "-7": 0.00016858924077856773, "-8": 2.7720995692036174e-05, "-9": 4.066860646076395e-06, "0": 0.2607447627648656, "1": 0.18802082148499227, "10": 4.617796138390357e-08, "11": 4.356627228530162e-09, "12": 3.7731793007238443e-10, "13": 3.007970896457722e-11, "14": 2.0476350002342584e-12, "2": 0.07861319167901903, "3": 0.02476307131090503, "4": 0.006083434526051407, "5": 0.0012205995837492193, "6": 0.0002066000090009679, "7": 3.0208871237180273e-05, "8": 3.885462334339835e-06, "9": 4.458845291450976e-07} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 47.3% |
| Home training matches | 17 |
| Away training matches | 29 |
| P home draw | 65.0% |
| P draw away | 61.0% |
| P home away | 74.0% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.1% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2394 |
| Totals anchor target over 2 5 | 0.5560 |
| Totals anchor reference over odds | 1.71 |
| Totals anchor reference under odds | 2.10 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4250 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.37, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.64, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.74, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:32Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.67, "home_away": 1.3, "home_draw": 1.39}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.21, "draw": 3.77, "home": 2.2}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.72, "home_away": 1.3, "home_draw": 1.38}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.05, "draw": 3.64, "home": 2.25}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.1}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.25 |
| Reference draw odds | 3.64 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.0% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.1297 |
| Raw ev home | -0.3274 |
| Raw edge prob draw | 0.0014 |
| Raw ev draw | -0.0170 |
| Raw edge prob away | 0.1283 |
| Raw ev away | 0.4134 |
| Market p home draw | 69.0% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:32Z |
| Market reference home draw last update utc | 2026-11-04T10:20:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.4% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.63 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 80.5% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.8% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.71 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,446.1006 |
| Elo away rating | 1,494.2964 |
| Elo rating diff | 11.8042 |
| Elo home expectancy | 0.5170 |

</details>


---

## 2026-11-05 — Celtic vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **46.2%**. Expected goals are 2.00 for Celtic and 2.43 for Besiktas JK (4.43 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 62.8%; Under 3.5 goals: 59.2%; Double Chance 1X: 53.8%; Double Chance X2: 68.4%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 77.3%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celtic win | 31.6% | 3.17 |
| Draw | 22.3% | 4.49 |
| Besiktas JK win | 46.2% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celtic expected goals | 2.00 |
| Besiktas JK expected goals | 2.43 |
| Expected total goals | 4.43 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.8% |
| Under 2.5 | 37.2% |
| Over 3.5 | 40.8% |
| Under 3.5 | 59.2% |
| Over 4.5 | 22.7% |
| Under 4.5 | 77.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.80% |
| 2 | 1-2 | 9.13% |
| 3 | 0-1 | 7.52% |
| 4 | 2-1 | 7.26% |
| 5 | 2-2 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 31.6% | 31.0% | 3.10 | -2.1% |
| Draw | 22.3% | 23.8% | 3.94 | -12.2% |
| Besiktas JK win | 46.2% | 45.1% | 2.23 | +2.9% |
| Over 2.5 | 62.8% | 58.4% | 1.67 | +4.9% |
| Under 2.5 | 37.2% | 41.6% | 2.31 | -14.2% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:20:08Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | celtic |
| Matched away-team name | besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0013 |
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
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.04 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.69 |
| Fair Over 3.5 odds | 2.45 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.41 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.21610119125498822, "-10": 4.382113949080971e-06, "-11": 6.956058231511848e-07, "-12": 1.0151089443326687e-07, "-13": 1.3705156890480231e-08, "-14": 1.7203691252752707e-09, "-15": 1.9985541172707598e-10, "-16": 1.911970801043072e-11, "-2": 0.13767213154054925, "-3": 0.0684229816241045, "-4": 0.02717566074197051, "-5": 0.00894142344495073, "-6": 0.002503966061945409, "-7": 0.0006093381872235587, "-8": 0.00013096954415629865, "-9": 2.51903823591488e-05, "0": 0.22273722080746075, "1": 0.1726489133622002, "10": 6.006803911924717e-07, "11": 7.843478953215492e-08, "12": 9.415511519609135e-09, "13": 1.0456853272479124e-09, "14": 1.0797529035162417e-10, "15": 1.0318210686256178e-11, "16": 8.119989588883021e-13, "2": 0.09001604355372719, "3": 0.03680116925281873, "4": 0.012023349523392127, "5": 0.0032541514455478354, "6": 0.0007496270932477623, "7": 0.00015005862773018495, "8": 2.6531305984170734e-05, "9": 4.1976749926635965e-06} |
| Raw goal margin distribution | {"-1": 0.18885049160439177, "-10": 3.6696903820861295e-05, "-11": 7.835998721220103e-06, "-12": 1.541817927131031e-06, "-13": 2.811951140155859e-07, "-14": 4.7779900969008414e-08, "-15": 7.596858958587555e-09, "-16": 1.1323798315558215e-09, "-17": 1.5537650275635808e-10, "-18": 1.652983651342302e-11, "-2": 0.14068118587611275, "-3": 0.08548021590100313, "-4": 0.042886194837900814, "-5": 0.01819998623388768, "-6": 0.006665551775935534, "-7": 0.0021417341611492235, "-8": 0.0006119952109749019, "-9": 0.00015727890508244926, "0": 0.1863819159096718, "1": 0.1558597498699802, "10": 5.205791910056248e-06, "11": 9.144026479284951e-07, "12": 1.4800007914699918e-07, "13": 2.220354734108814e-08, "14": 3.1034558967490444e-09, "15": 4.0590101213387665e-10, "16": 4.9769575269356464e-11, "17": 5.617497514336317e-12, "18": 4.91599964874607e-13, "2": 0.09519354422164666, "3": 0.04757982326996731, "4": 0.019636336531709882, "5": 0.00685487831463854, "6": 0.002065144925686719, "7": 0.0005458404674465974, "8": 0.00012830214824438476, "9": 2.712327452017504e-05} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 48.6% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.4% |
| Raw p btts yes | 78.6% |
| Home training matches | 13 |
| Away training matches | 11 |
| P home draw | 53.8% |
| P draw away | 68.4% |
| P home away | 77.7% |
| Raw p home draw | 51.4% |
| Raw p draw away | 67.2% |
| Raw p home away | 81.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7316 |
| Totals anchor target over 2 5 | 0.6284 |
| Totals anchor reference over odds | 1.54 |
| Totals anchor reference under odds | 2.51 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8116 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.77, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.33, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.62, "price": 2.33, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.23, "draw": 3.83, "home": 3.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.4, "home_away": 1.29, "home_draw": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.14, "draw": 3.94, "home": 3.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.51}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.39, "home_away": 1.27, "home_draw": 1.73}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.06 |
| Reference draw odds | 3.94 |
| Reference away odds | 2.14 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +0.5% |
| Draw probability edge | -1.6% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +4.4% |
| Under 2.5 probability edge | -4.4% |
| Raw edge prob home | 0.0175 |
| Raw ev home | 0.0165 |
| Raw edge prob draw | -0.0519 |
| Raw ev draw | -0.2657 |
| Raw edge prob away | 0.0345 |
| Raw ev away | 0.0832 |
| Market p home draw | 55.5% |
| Market home draw odds | 1.73 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.0% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home draw odds | 1.73 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.6% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.23 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.3% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | crystal palace |
| Matched away-team name | hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7143 |
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
| Goal margin distribution | {"-1": 0.15056750945697953, "-10": 6.70513410862625e-08, "-11": 6.954368194950598e-09, "-12": 6.630191232208905e-10, "-13": 5.847713469781233e-11, "-14": 4.797563844600513e-12, "-15": 3.677319710853267e-13, "-16": 2.6237666095771568e-14, "-17": 1.5641644944517392e-15, "-2": 0.06246900948467393, "-3": 0.020399045711542482, "-4": 0.00531243470059971, "-5": 0.0011447031959872724, "-6": 0.00020977146020670383, "-7": 3.338709804239582e-05, "-8": 4.691719354242466e-06, "-9": 5.898222241943332e-07, "0": 0.2163129308809716, "1": 0.20855499972250408, "10": 2.3540492105469172e-05, "11": 4.50784297948449e-06, "12": 7.934876744123889e-07, "13": 1.2921211808130493e-07, "14": 1.9572259022003998e-08, "15": 2.7698395493505113e-09, "16": 3.6488117188260225e-10, "17": 4.016166482520362e-11, "2": 0.16242334221070423, "3": 0.09792570455602365, "4": 0.0470850991517054, "5": 0.018732071661510863, "6": 0.006337855703782165, "7": 0.0018624200957952843, "8": 0.00048320790812817675, "9": 0.00011215694484685477} |
| Raw goal margin distribution | {"-1": 0.11195694496152009, "-10": 2.8298335575757473e-07, "-11": 3.673672262797068e-08, "-12": 4.390694348408217e-09, "-13": 4.860677650358678e-10, "-14": 5.010480737102898e-11, "-15": 4.831495725556263e-12, "-16": 4.375630448350634e-13, "-17": 3.731211930726465e-14, "-18": 2.9618775667624343e-15, "-19": 1.8939833984305068e-16, "-2": 0.052719563440937124, "-3": 0.020146756893797187, "-4": 0.0062867783147483505, "-5": 0.001647270501185661, "-6": 0.00037063434356879305, "-7": 7.290702229517139e-05, "-8": 1.272172311588877e-05, "-9": 1.9927170058819864e-06, "0": 0.16534612583398428, "1": 0.2041346841238132, "10": 0.00013025403916940462, "11": 3.122006099581516e-05, "12": 6.889212392155152e-06, "13": 1.4081088239006822e-06, "14": 2.679919982501108e-07, "15": 4.771193834341329e-08, "16": 7.977909903059167e-09, "17": 1.2560341276837256e-09, "18": 1.8408637912380577e-10, "19": 2.1733704188865646e-11, "2": 0.17971232662063139, "3": 0.1267985356645147, "4": 0.0730533724139431, "5": 0.03534110097811875, "6": 0.014681277365117052, "7": 0.005332005343968874, "8": 0.001717790453606917, "9": 0.0004967900667908066} |
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
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7713 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.64, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.78, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.47, "price": 2.78, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.72, "draw": 4.05, "home": 1.94}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.92, "home_away": 1.27, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.68, "draw": 4.01, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.54, "under": 2.56}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.92, "home_away": 1.27, "home_draw": 1.31}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 4.01 |
| Reference away odds | 3.68 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:46Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:46Z |
| Home probability edge | +4.2% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.1398 |
| Raw ev home | 0.2508 |
| Raw edge prob draw | -0.0728 |
| Raw ev draw | -0.3303 |
| Raw edge prob away | -0.0670 |
| Raw ev away | -0.2812 |
| Market p home draw | 73.7% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.3% |
| Market draw away odds | 1.92 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.0% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.92 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 5.55 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
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
| Dc lambda away | 1.3083 |
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
| Goal margin distribution | {"-1": 0.09645078181817242, "-10": 0.0001428283770835775, "-11": 3.6006954353506494e-05, "-12": 8.340256530326801e-06, "-13": 1.7865195591085874e-06, "-14": 3.5587058102952107e-07, "-15": 6.624230031180585e-08, "-16": 1.1571212940783774e-08, "-17": 1.903587893263313e-09, "-18": 2.9453616198360724e-10, "-19": 3.936366736246944e-11, "-2": 0.10306795274792876, "-3": 0.0835985948070125, "-4": 0.0536432545030808, "-5": 0.02834460232941563, "-6": 0.01269885222354554, "-7": 0.004931266214968915, "-8": 0.0016883409455706539, "-9": 0.0005165995014480565, "0": 0.2641210150532492, "1": 0.2626110400277161, "10": 2.107943049902683e-09, "11": 1.3876907520059357e-10, "12": 8.393588013800949e-12, "13": 4.695025431528366e-13, "14": 2.4422166913060658e-14, "15": 1.1871058546218586e-15, "16": 5.414955118995916e-17, "17": 2.3262203119479378e-18, "18": 9.398931118154146e-20, "19": 3.2801773889569093e-21, "2": 0.07035136853492639, "3": 0.014900807764094318, "4": 0.0024968237496915523, "5": 0.000344512568562694, "6": 4.0305202320813085e-05, "7": 4.0871165152727074e-06, "8": 3.654101925491002e-07, "9": 2.919687837434098e-08} |
| Raw goal margin distribution | {"-1": 0.31606412998775596, "-10": 8.098155523764202e-07, "-11": 9.599288160525922e-08, "-12": 1.0435794500267329e-08, "-13": 1.0471984236483525e-09, "-14": 9.48334776167009e-11, "-2": 0.1902707123262101, "-3": 0.08005969877193457, "-4": 0.025621375799674325, "-5": 0.006606717652158878, "-6": 0.0014255505050144092, "-7": 0.0002643398283752541, "-8": 4.2964286994165795e-05, "-9": 6.21486615632927e-06, "0": 0.2794032554373557, "1": 0.08570622649663781, "10": 1.194003094761115e-12, "11": 3.695900768112283e-14, "12": 1.0492252312103972e-15, "13": 2.7493758969062346e-17, "14": 6.501727327596369e-19, "2": 0.012974654799746783, "3": 0.0014256067845627991, "4": 0.00011913796626736383, "5": 8.02223567990243e-06, "6": 4.520164206148226e-07, "7": 2.1887499101436738e-08, "8": 9.289729759435164e-10, "9": 3.509047002934381e-11} |
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
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2009 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.47, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.55, "price": 2.47, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.7, "home": 2.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.24}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.78, "home_away": 1.3, "home_draw": 1.33}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.33, "draw": 3.66, "home": 2.11}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.75, "home_away": 1.3, "home_draw": 1.34}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.11 |
| Reference draw odds | 3.66 |
| Reference away odds | 3.33 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -10.7% |
| Draw probability edge | +0.7% |
| Away probability edge | +10.1% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.3579 |
| Raw ev home | -0.7885 |
| Raw edge prob draw | 0.0218 |
| Raw ev draw | 0.0338 |
| Raw edge prob away | 0.3360 |
| Raw ev away | 1.1775 |
| Market p home draw | 71.5% |
| Market home draw odds | 1.34 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.8% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.7% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:11Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.34 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.5% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.53 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.9% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,422.3390 |
| Elo away rating | 1,425.2946 |
| Elo rating diff | 57.0445 |
| Elo home expectancy | 0.5814 |

</details>


---

## 2026-11-05 — Lillestrom vs Viktoria Plzeň

The model's most likely 1X2 outcome is **Viktoria Plzeň win** at **55.6%**. Expected goals are 0.46 for Lillestrom and 2.49 for Viktoria Plzeň (2.95 combined). The most likely exact score is 1-1 at 9.8%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 61.9%; Under 3.5 goals: 58.0%; Double Chance 1X: 44.4%; Double Chance X2: 76.3%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lillestrom win | 23.7% | 4.23 |
| Draw | 20.7% | 4.83 |
| Viktoria Plzeň win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lillestrom expected goals | 0.46 |
| Viktoria Plzeň expected goals | 2.49 |
| Expected total goals | 2.95 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 42.0% |
| Under 3.5 | 58.0% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.78% |
| 2 | 1-0 | 8.88% |
| 3 | 0-3 | 7.87% |
| 4 | 0-2 | 7.41% |
| 5 | 2-1 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lillestrom win | 23.7% | 31.5% | 3.04 | -28.1% |
| Draw | 20.7% | 24.2% | 3.90 | -19.2% |
| Viktoria Plzeň win | 55.6% | 44.3% | 2.24 | +24.6% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | lillestrøm |
| Matched away-team name | viktoria plzen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.4624 |
| Dc lambda away | 2.4858 |
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
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.24 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.37 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.38 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.1080044697080643, "-10": 0.0005121892742929651, "-11": 0.00014621633151103196, "-12": 3.834384288321149e-05, "-13": 9.297407545341229e-06, "-14": 2.096179709421284e-06, "-15": 4.415794032834158e-07, "-16": 8.728790798058584e-08, "-17": 1.6251664452134714e-08, "-18": 2.8591830144080393e-09, "-19": 4.750344874875643e-10, "-2": 0.13318344025716, "-20": 6.911861746797004e-11, "-3": 0.12354057683406396, "-4": 0.09031974341066133, "-5": 0.05425583906090798, "-6": 0.027596584764568124, "-7": 0.012155433090658958, "-8": 0.004717588628036823, "-9": 0.001635554515042543, "0": 0.20723888623708997, "1": 0.18773888720649512, "10": 2.2504190698368311e-10, "11": 1.1951431002421743e-11, "12": 5.830566687048096e-13, "13": 2.6300748255752625e-14, "14": 1.103127862954593e-15, "15": 4.323119645528574e-17, "16": 1.5897675837286458e-18, "17": 5.506409484715745e-20, "18": 1.8022030416474235e-21, "19": 5.570292606130974e-23, "2": 0.04079005632722581, "20": 1.5077836052217016e-24, "3": 0.007038900178504072, "4": 0.000957346121368898, "5": 0.00010698524279343512, "6": 1.0123340317528848e-05, "7": 8.29526071922107e-07, "8": 5.989227039634431e-08, "9": 3.862841054481257e-09} |
| Raw goal margin distribution | {"-1": 0.22407483143940066, "-10": 0.0001444182408410336, "-11": 3.2355549239324077e-05, "-12": 6.653600436095798e-06, "-13": 1.264304089232573e-06, "-14": 2.2326555130950623e-07, "-15": 3.6823193929954776e-08, "-16": 5.696615727806673e-09, "-17": 8.283570187048422e-10, "-18": 1.0752711755470641e-10, "-2": 0.23370368663125024, "-3": 0.1775300795518459, "-4": 0.10453209871736092, "-5": 0.05009871443071024, "-6": 0.020213237927822397, "-7": 0.0070356922537983145, "-8": 0.0021521917688660094, "-9": 0.0005870033957709018, "0": 0.12638067348800203, "1": 0.044138449784721416, "10": 7.170230300370839e-12, "11": 2.9884840088340195e-13, "12": 1.1432730924550483e-14, "13": 4.041437932358013e-16, "14": 1.3276915618695739e-17, "15": 4.0736905615446916e-19, "16": 1.1723967656816125e-20, "17": 3.1715119266637253e-22, "18": 7.658750151712306e-24, "2": 0.008088123504440891, "3": 0.0011429974566214349, "4": 0.00012520281449359162, "5": 1.1163030437767559e-05, "6": 8.378813441043629e-07, "7": 5.4255600293285487e-08, "8": 3.0875202142134872e-09, "9": 1.5666088031025316e-10} |
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
| Totals anchor scale | 1.2811 |
| Totals anchor target over 2 5 | 0.6193 |
| Totals anchor reference over odds | 1.56 |
| Totals anchor reference under odds | 2.45 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4794 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.28, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.64, "price": 2.28, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.24, "draw": 3.9, "home": 3.04}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.41, "home_away": 1.28, "home_draw": 1.69}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.18, "draw": 3.89, "home": 3.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.56, "under": 2.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.4, "home_away": 1.27, "home_draw": 1.71}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.02 |
| Reference draw odds | 3.89 |
| Reference away odds | 2.18 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:25Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:25Z |
| Home probability edge | -7.8% |
| Draw probability edge | -3.5% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | -0.2616 |
| Raw ev home | -0.8373 |
| Raw edge prob draw | -0.1155 |
| Raw ev draw | -0.5071 |
| Raw edge prob away | 0.3771 |
| Raw ev away | 0.8371 |
| Market p home draw | 56.1% |
| Market home draw odds | 1.71 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.5% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home draw odds | 1.71 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 83.9% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.15 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.1% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,400.8156 |
| Elo away rating | 1,451.8117 |
| Elo rating diff | 9.0039 |
| Elo home expectancy | 0.5130 |

</details>


---

## 2026-11-05 — NEC Nijmegen vs Omonoia FC

The model's most likely 1X2 outcome is **NEC Nijmegen win** at **50.7%**. Expected goals are 2.30 for NEC Nijmegen and 2.20 for Omonoia FC (4.50 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 61.1%; Under 3.5 goals: 61.4%; Double Chance 1X: 72.6%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 78.9%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NEC Nijmegen win | 50.7% | 1.97 |
| Draw | 21.9% | 4.57 |
| Omonoia FC win | 27.4% | 3.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NEC Nijmegen expected goals | 2.30 |
| Omonoia FC expected goals | 2.20 |
| Expected total goals | 4.50 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 61.1% |
| Under 2.5 | 38.9% |
| Over 3.5 | 38.6% |
| Under 3.5 | 61.4% |
| Over 4.5 | 21.1% |
| Under 4.5 | 78.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.79% |
| 2 | 1-1 | 9.81% |
| 3 | 1-0 | 9.41% |
| 4 | 2-0 | 7.01% |
| 5 | 2-2 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NEC Nijmegen win | 50.7% | 54.3% | 1.79 | -9.3% |
| Draw | 21.9% | 23.2% | 4.15 | -9.2% |
| Omonoia FC win | 27.4% | 22.5% | 4.30 | +17.9% |
| Over 2.5 | 61.1% | 60.4% | 1.62 | -1.1% |
| Under 2.5 | 38.9% | 39.6% | 2.42 | -5.8% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | n.e.c. |
| Matched away-team name | omonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2975 |
| Dc lambda away | 2.2006 |
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
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.30 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.45 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.57 |
| Fair Over 3.5 odds | 2.59 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.74 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.14365728501051395, "-10": 8.094640351541511e-07, "-11": 1.1113237222290898e-07, "-12": 1.4024220353174642e-08, "-13": 1.6362258807178649e-09, "-14": 1.7578720056314302e-10, "-15": 1.5476218688984758e-11, "-2": 0.07974963915128101, "-3": 0.03451268461347997, "-4": 0.011906376476631633, "-5": 0.0033976862580646825, "-6": 0.0008244592359517215, "-7": 0.00017373428630897806, "-8": 3.232132169914868e-05, "-9": 5.379029086335604e-06, "0": 0.218905857117438, "1": 0.25674494792467806, "10": 2.134939279946826e-06, "11": 3.06021724291776e-07, "12": 4.031940391449471e-08, "13": 4.911366420522529e-09, "14": 5.508965235305946e-10, "15": 5.063739347945212e-11, "2": 0.14897969246866663, "3": 0.0673132861007666, "4": 0.0242451772422884, "5": 0.007223584030581744, "6": 0.001830047431383197, "7": 0.0004026265371643597, "8": 7.82041276839378e-05, "9": 1.3588394906229317e-05} |
| Raw goal margin distribution | {"-1": 0.1699946678046378, "-10": 1.2824743355051328e-05, "-11": 2.4737584078872127e-06, "-12": 4.397634140376884e-07, "-13": 7.247373953718591e-08, "-14": 1.1129002243786112e-08, "-15": 1.5992459934775647e-09, "-16": 2.1541554005762993e-10, "-17": 2.6670772424382596e-11, "-18": 2.5455950632710038e-12, "-2": 0.11310938680422193, "-3": 0.06166412466817926, "-4": 0.02781805910893196, "-5": 0.010630528381169898, "-6": 0.003509382563397686, "-7": 0.0010171396948488918, "-8": 0.00026230657018034014, "-9": 6.0862012831407894e-05, "0": 0.1884369921318538, "1": 0.17735995806944438, "10": 1.9737207731108693e-05, "11": 3.974825024343401e-06, "12": 7.377403382348651e-07, "13": 1.2693716912280996e-07, "14": 2.0351108549388008e-08, "15": 3.053309402185691e-09, "16": 4.293943015488525e-10, "17": 5.5505822584039346e-11, "18": 5.531156828671465e-12, "2": 0.12329516717223629, "3": 0.07017843510483078, "4": 0.03305381844006896, "5": 0.013187830780193283, "6": 0.0045454086219723746, "7": 0.001375455435166822, "8": 0.00037033843938640693, "9": 8.97138795391052e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.3% |
| Raw p btts yes | 79.7% |
| Home training matches | 3 |
| Away training matches | 9 |
| P home draw | 72.6% |
| P draw away | 49.3% |
| P home away | 78.1% |
| Raw p home draw | 61.2% |
| Raw p draw away | 57.7% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.6989 |
| Totals anchor target over 2 5 | 0.6108 |
| Totals anchor reference over odds | 1.58 |
| Totals anchor reference under odds | 2.40 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.8208 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.14, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.37, "price": 3.14, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.3, "draw": 4.15, "home": 1.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.09, "home_away": 1.26, "home_draw": 1.24}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.13, "draw": 4.02, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.58, "under": 2.4}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.06, "home_away": 1.26, "home_draw": 1.25}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 4.02 |
| Reference away odds | 4.13 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -3.6% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.1191 |
| Raw ev home | -0.2420 |
| Raw edge prob draw | -0.0435 |
| Raw ev draw | -0.2180 |
| Raw edge prob away | 0.1626 |
| Raw ev away | 0.6688 |
| Market p home draw | 77.0% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.7% |
| Market draw away odds | 2.09 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.06 |
| Market reference dc home draw odds | 1.25 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.1% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.92 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.9% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,432.8516 |
| Elo away rating | 1,467.0936 |
| Elo rating diff | 25.7579 |
| Elo home expectancy | 0.5370 |

</details>


---

## 2026-11-05 — PFC Levski Sofia vs Jagiellonia Białystok

The model's most likely 1X2 outcome is **PFC Levski Sofia win** at **58.0%**. Expected goals are 2.26 for PFC Levski Sofia and 0.35 for Jagiellonia Białystok (2.61 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 52.7%; Under 3.5 goals: 66.9%; Double Chance 1X: 80.7%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 82.3%; BTTS Yes (both teams score): 39.6%; BTTS No (at least one team does not score): 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 1.72 |
| Draw | 22.8% | 4.40 |
| Jagiellonia Białystok win | 19.3% | 5.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PFC Levski Sofia expected goals | 2.26 |
| Jagiellonia Białystok expected goals | 0.35 |
| Expected total goals | 2.61 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.7% |
| Under 4.5 | 82.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.53% |
| 2 | 2-0 | 10.04% |
| 3 | 3-0 | 9.57% |
| 4 | 0-1 | 9.52% |
| 5 | 0-0 | 8.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 47.9% | 2.02 | +17.1% |
| Draw | 22.8% | 26.6% | 3.75 | -14.7% |
| Jagiellonia Białystok win | 19.3% | 25.5% | 3.79 | -27.0% |
| Over 2.5 | 52.7% | 52.7% | 1.83 | -3.5% |
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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | levski sofia |
| Matched away-team name | jagiellonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2607 |
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
| P btts yes | 39.6% |
| P btts no | 60.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.27 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.66 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.16074078266798736, "-10": 1.771953158349782e-11, "-11": 7.104923270158257e-13, "-12": 2.6152193161415444e-14, "-13": 8.895931640141392e-16, "-14": 2.812473725092849e-17, "-15": 8.305134468590223e-19, "-16": 2.3006119877743823e-20, "-17": 6.000874496520195e-22, "-18": 1.4760639675185946e-23, "-19": 3.2419156173926966e-25, "-2": 0.027774381829968064, "-3": 0.0037475493337392734, "-4": 0.00039312967771508667, "-5": 3.36240949508423e-05, "-6": 2.4234751761599617e-06, "-7": 1.5079059657492367e-07, "-8": 8.249141684536901e-09, "-9": 4.0250216680475174e-10, "0": 0.22752384150058808, "1": 0.12697356078881922, "10": 0.00027891226733868567, "11": 7.186286257677431e-05, "12": 1.699741890098531e-05, "13": 3.715318422703602e-06, "14": 7.547842333220474e-07, "15": 1.4322233700506247e-07, "16": 2.5493954570398904e-08, "17": 4.273051378694321e-09, "18": 6.75396010881531e-10, "19": 9.532015958009262e-11, "2": 0.15039100006947853, "3": 0.13039308064647756, "4": 0.08789673827590853, "5": 0.04830780160777699, "6": 0.02237355458776656, "7": 0.008945413353533738, "8": 0.0031445945591655196, "9": 0.000985947658719141} |
| Raw goal margin distribution | {"-1": 0.040439508246418114, "-10": 6.309721122266637e-13, "-11": 2.005978467283387e-14, "-12": 5.851275658908639e-16, "-13": 1.5766130273529635e-17, "-14": 3.9469824081096226e-19, "-15": 9.22653696699598e-21, "-16": 2.0208357400993952e-22, "-17": 3.99511997976196e-24, "-2": 0.0058690496844221104, "-3": 0.0006469782045344612, "-4": 5.4779761348035376e-05, "-5": 3.7566165920047436e-06, "-6": 2.162295233481005e-07, "-7": 1.07167430602008e-08, "-8": 4.66173566089838e-10, "-9": 1.8064079046922385e-11, "0": 0.13853625090785388, "1": 0.2440307388933858, "10": 7.573690985451375e-05, "11": 1.5472248263131397e-05, "12": 2.9000631755663617e-06, "13": 5.021248934731375e-07, "14": 8.077585697073445e-08, "15": 1.2133465268539092e-08, "16": 1.7076815292831657e-09, "17": 2.1693790158281618e-10, "2": 0.24234120856808045, "3": 0.17166386064849012, "4": 0.09339832820841526, "5": 0.04115717720802055, "6": 0.015222761424614827, "7": 0.004848093758279092, "8": 0.0013551444072738917, "9": 0.00033742985098736856} |
| Unadjusted home-win probability | 81.4% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 26.3% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 80.7% |
| P draw away | 42.0% |
| P home away | 77.2% |
| Raw p home draw | 95.3% |
| Raw p draw away | 18.6% |
| Raw p home away | 86.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2657 |
| Totals anchor target over 2 5 | 0.5274 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.03 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4034 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.7, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.48, "price": 2.7, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.79, "draw": 3.75, "home": 2.0}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.87, "home_away": 1.3, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.55, "home": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.03}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.03}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.82, "home_away": 1.31, "home_draw": 1.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.02 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:08Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +10.1% |
| Draw probability edge | -3.8% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3352 |
| Raw ev home | 0.6452 |
| Raw edge prob draw | -0.1271 |
| Raw ev draw | -0.4805 |
| Raw edge prob away | -0.2081 |
| Raw ev away | -0.8218 |
| Market p home draw | 74.3% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:42Z |
| Market reference home draw last update utc | 2026-11-04T10:20:12Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.6% |
| Market draw away odds | 1.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:12Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T10:20:12Z |
| Market reference home away last update utc | 2026-11-04T10:20:12Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.82 |
| Market reference dc home draw odds | 1.29 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 77.6% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,427.6479 |
| Elo away rating | 1,424.2193 |
| Elo rating diff | 63.4285 |
| Elo home expectancy | 0.5903 |

</details>


---

## 2026-11-05 — Real Sociedad vs Lyon

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.5%**. Expected goals are 1.96 for Real Sociedad and 1.16 for Lyon (3.12 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 62.0%; Under 3.5 goals: 59.7%; Double Chance 1X: 76.9%; Double Chance X2: 45.5%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 54.5% | 1.84 |
| Draw | 22.4% | 4.46 |
| Lyon win | 23.1% | 4.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 1.96 |
| Lyon expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 40.3% |
| Under 3.5 | 59.7% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.08% |
| 2 | 2-1 | 9.33% |
| 3 | 1-0 | 8.11% |
| 4 | 2-0 | 7.77% |
| 5 | 2-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.5% | 53.6% | 1.83 | -0.3% |
| Draw | 22.4% | 23.1% | 4.13 | -7.4% |
| Lyon win | 23.1% | 23.3% | 4.25 | -1.8% |

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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:20:08Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | real sociedad |
| Matched away-team name | lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9619 |
| Dc lambda away | 1.1600 |
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
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.21 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.80 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.141998451252113, "-10": 8.671819564175621e-08, "-11": 9.302415433476394e-09, "-12": 9.172238174723987e-10, "-13": 8.366184815947063e-11, "-14": 7.0980549802434576e-12, "-15": 5.626330235726623e-13, "-16": 4.1525820497171125e-14, "-17": 2.5662981661736032e-15, "-2": 0.06127049120504296, "-3": 0.020747097913514156, "-4": 0.0055974281297636605, "-5": 0.001248783403885994, "-6": 0.00023685449723274184, "-7": 3.900754746351218e-05, "-8": 5.671034950358575e-06, "-9": 7.37492827357871e-07, "0": 0.22428096532544706, "1": 0.22114149089568336, "10": 1.5509517417014172e-05, "11": 2.813817680278694e-06, "12": 4.6923210451694234e-07, "13": 7.238557371801146e-08, "14": 1.0386664344328248e-08, "15": 1.392432428633245e-09, "16": 1.7381181858988976e-10, "17": 1.8166880793298528e-11, "2": 0.16369749801412858, "3": 0.0937476106471148, "4": 0.04277633267490427, "5": 0.016140400711948343, "6": 0.005177510651028328, "7": 0.0014421159589078413, "8": 0.0003545896318115363, "9": 7.798905917942356e-05} |
| Raw goal margin distribution | {"-1": 0.14108133006955847, "-10": 6.579416848567237e-08, "-11": 6.822529777244292e-09, "-12": 6.501601740822358e-10, "-13": 5.730598230634109e-11, "-14": 4.695976664106581e-12, "-15": 3.5683229924137033e-13, "-16": 2.26493488037329e-14, "-2": 0.05961686006021967, "-3": 0.019678453365026265, "-4": 0.0051592968483100176, "-5": 0.0011164872495279907, "-6": 0.00020516452733019525, "-7": 3.271006241304606e-05, "-8": 4.601169127457876e-06, "-9": 5.78713776895835e-07, "0": 0.20809318096055665, "1": 0.23513947093733722, "10": 1.2598217972355943e-05, "11": 2.2094253211594317e-06, "12": 3.560954476676971e-07, "13": 5.308333397799711e-08, "14": 7.356925054008084e-09, "15": 9.454677762227983e-10, "16": 1.0149635944644568e-10, "2": 0.17052711383472063, "3": 0.09519792374346195, "4": 0.04221231814181631, "5": 0.015449507000751409, "6": 0.004801481980375637, "7": 0.001294692325533514, "8": 0.0003080105339207201, "9": 6.551992103161496e-05} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 58.5% |
| Home training matches | 23 |
| Away training matches | 25 |
| P home draw | 76.9% |
| P draw away | 45.5% |
| P home away | 77.6% |
| Raw p home draw | 77.3% |
| Raw p draw away | 43.5% |
| Raw p home away | 79.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0357 |
| Totals anchor target over 2 5 | 0.6199 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.49 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5979 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.02, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.43, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.13, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.39, "price": 3.13, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.25, "draw": 4.1, "home": 1.81}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.06, "home_away": 1.26, "home_draw": 1.25}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.1, "draw": 4.13, "home": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.57, "under": 2.49}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.06, "home_away": 1.26, "home_draw": 1.27}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.13 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0292 |
| Raw ev home | 0.0340 |
| Raw edge prob draw | -0.0231 |
| Raw ev draw | -0.1406 |
| Raw edge prob away | -0.0061 |
| Raw ev away | -0.0357 |
| Market p home draw | 76.2% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.0% |
| Market draw away odds | 2.06 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.06 |
| Market reference dc home draw odds | 1.27 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 83.5% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.21 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.7% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
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
| 3 | 2-0 | 8.59% |
| 4 | 1-0 | 8.14% |
| 5 | 2-2 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SK Sturm Graz win | 59.1% | 63.7% | 1.58 | -6.6% |
| Draw | 24.2% | 20.1% | 4.56 | +10.4% |
| NK Celje win | 16.7% | 16.3% | 5.57 | -7.0% |
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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
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
| Dc lambda away | 0.4750 |
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
| Fair Under 0.5 odds | 22.80 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.95 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.44 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.51 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.1094391386208739, "-10": 2.0432497058698636e-08, "-11": 1.9174562304622704e-09, "-12": 1.6537664811201083e-10, "-13": 1.319338486497748e-11, "-14": 9.789656331252638e-13, "-15": 6.786522513011401e-14, "-16": 4.383102367063118e-15, "-17": 2.3808770041468037e-16, "-2": 0.04148147310619962, "-3": 0.012354020295003619, "-4": 0.0029256857266240005, "-5": 0.0005722695377634526, "-6": 9.509171195535834e-05, "-7": 1.3713180881831734e-05, "-8": 1.7451279849233425e-06, "-9": 1.9860366071670711e-07, "0": 0.24214274334825103, "1": 0.21447575543551686, "10": 3.491130155582593e-05, "11": 6.9354693914341395e-06, "12": 1.2662818745551043e-06, "13": 2.138544252804373e-07, "14": 3.359195354415326e-08, "15": 4.929704803889929e-09, "16": 6.740017722884532e-10, "17": 7.75036561077299e-11, "2": 0.17573259686309703, "3": 0.11079298704098117, "4": 0.05554403664293941, "5": 0.022999383745117324, "6": 0.008090289114043098, "7": 0.002469820466325069, "8": 0.0006653654846643234, "9": 0.00016029723813159073} |
| Raw goal margin distribution | {"-1": 0.14145004003028025, "-10": 3.8261700899414713e-11, "-11": 1.6461521535708452e-12, "-12": 6.491850259331738e-14, "-13": 2.2878229269799447e-15, "-2": 0.03000318198592911, "-3": 0.004572405729179595, "-4": 0.0005304675805668114, "-5": 4.961021930148515e-05, "-6": 3.883435073710608e-06, "-7": 2.6128808710937443e-07, "-8": 1.5411291627701867e-08, "-9": 8.090465076422836e-10, "0": 0.33901779108556906, "1": 0.2933708375511639, "10": 6.915479871414526e-08, "11": 6.298452066834943e-09, "12": 5.258212737433589e-10, "13": 3.9228154021864824e-11, "2": 0.13445560960357145, "3": 0.04337726593480919, "4": 0.010653248728127998, "5": 0.002109114567909137, "6": 0.0003495029760727551, "7": 4.9780613414971705e-05, "8": 6.215634634949351e-06, "9": 6.907576952586065e-07} |
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
| Totals anchor scale | 2.2112 |
| Totals anchor target over 2 5 | 0.6154 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2100 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 4.42, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.22, "price": 4.42, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.57, "draw": 4.56, "home": 1.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.48, "home_away": 1.22, "home_draw": 1.17}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.53, "draw": 4.54, "home": 1.53}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.57, "under": 2.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.56, "home_away": 1.21, "home_draw": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.53 |
| Reference draw odds | 4.54 |
| Reference away odds | 5.53 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -4.6% |
| Draw probability edge | +4.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.1523 |
| Raw ev home | -0.2347 |
| Raw edge prob draw | 0.1384 |
| Raw ev draw | 0.5459 |
| Raw edge prob away | 0.0139 |
| Raw ev away | -0.0163 |
| Market p home draw | 82.9% |
| Market home draw odds | 1.17 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T10:19:42Z |
| Market reference home draw last update utc | 2026-11-04T10:20:12Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.6% |
| Market draw away odds | 2.56 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-04T10:20:12Z |
| Market reference draw away last update utc | 2026-11-04T10:20:12Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:12Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.56 |
| Market reference dc home draw odds | 1.16 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.8% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,441.2526 |
| Elo away rating | 1,413.6182 |
| Elo rating diff | 87.6344 |
| Elo home expectancy | 0.6235 |

</details>


---

## 2026-11-05 — Sparta Prague vs Bournemouth

The model's most likely 1X2 outcome is **Bournemouth win** at **74.2%**. Expected goals are 0.26 for Sparta Prague and 3.59 for Bournemouth (3.85 combined). The most likely exact score is 0-3 at 13.1%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 61.5%; Under 3.5 goals: 57.0%; Double Chance 1X: 25.8%; Double Chance X2: 89.3%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 73.6%; BTTS Yes (both teams score): 26.0%; BTTS No (at least one team does not score): 74.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sparta Prague win | 10.7% | 9.33 |
| Draw | 15.1% | 6.62 |
| Bournemouth win | 74.2% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sparta Prague expected goals | 0.26 |
| Bournemouth expected goals | 3.59 |
| Expected total goals | 3.85 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 61.5% |
| Under 2.5 | 38.5% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 26.4% |
| Under 4.5 | 73.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 13.12% |
| 2 | 0-4 | 11.58% |
| 3 | 0-2 | 11.15% |
| 4 | 0-5 | 8.18% |
| 5 | 0-0 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Prague win | 10.7% | 14.9% | 6.18 | -33.8% |
| Draw | 15.1% | 19.7% | 4.71 | -28.8% |
| Bournemouth win | 74.2% | 65.4% | 1.52 | +12.7% |
| Over 2.5 | 61.5% | 60.9% | 1.62 | -0.3% |
| Under 2.5 | 38.5% | 39.1% | 2.42 | -6.9% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
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
| Dc lambda away | 3.5895 |
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
| P btts yes | 26.0% |
| P btts no | 74.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.01 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 3.79 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.09667520975054224, "-10": 0.0016071381596235816, "-11": 0.0005123218714802563, "-12": 0.00014986085681479064, "-13": 4.049684817703114e-05, "-14": 1.0168336494600487e-05, "-15": 2.384204494794993e-06, "-16": 5.243200626121331e-07, "-17": 1.0856189754339284e-07, "-18": 2.1235719741468143e-08, "-19": 3.936250281478186e-09, "-2": 0.1486061633835853, "-20": 6.927331154305184e-10, "-21": 1.1170476464741962e-10, "-3": 0.16323674975798116, "-4": 0.13807790330221376, "-5": 0.09472777791813657, "-6": 0.05459212202241299, "-7": 0.027104548611637108, "-8": 0.01181537239720898, "-9": 0.0045893019205761896, "0": 0.15111276700367882, "1": 0.09672272822019201, "10": 7.161815305318034e-14, "11": 1.634121419910382e-15, "12": 3.421378795983457e-17, "13": 6.617678954508638e-19, "14": 1.1893396626724232e-20, "15": 1.9960481670418718e-22, "16": 3.1419228217113363e-24, "17": 4.6563753854648506e-26, "18": 6.519421589919902e-28, "19": 8.649605658745945e-30, "2": 0.009612460062731362, "20": 1.0895598087357512e-31, "21": 1.2575589304548583e-33, "3": 0.0007557657167979842, "4": 4.575778090410091e-05, "5": 2.246930518003622e-06, "6": 9.268592553187598e-08, "7": 3.2938022086770347e-09, "8": 1.0277187353090449e-10, "9": 2.8572287513409692e-12} |
| Raw goal margin distribution | {"-1": 0.11886230765333439, "-10": 0.002271736171896116, "-11": 0.0007361894485583265, "-12": 0.00021892316726192064, "-13": 6.014412946535322e-05, "-14": 1.535323235942763e-05, "-15": 3.6599820738626537e-06, "-16": 8.183211760069477e-07, "-17": 1.7226691288990935e-07, "-18": 3.426044519623143e-08, "-19": 6.4567435953769435e-09, "-2": 0.185063265919736, "-20": 1.155264130868121e-09, "-21": 1.8915910518857677e-10, "-3": 0.20625460150836114, "-4": 0.1771560289151277, "-5": 0.123464187928367, "-6": 0.07229972670241039, "-7": 0.03648071630964241, "-8": 0.01616336088319175, "-9": 0.006381583199570942, "0": 0.04411648334410353, "1": 0.00942205282584098, "10": 8.018130399549012e-15, "11": 1.8598432059401586e-16, "12": 3.958676279259658e-18, "13": 7.784362135957417e-20, "14": 1.4223324982614607e-21, "15": 2.4268994929297838e-23, "16": 3.8839009398151944e-25, "17": 5.85218097596193e-27, "18": 8.330679016001274e-29, "19": 1.123757133940504e-30, "2": 0.0009481199097437152, "20": 1.4391687921648406e-32, "21": 1.6866664900467109e-34, "3": 7.56341991773153e-05, "4": 4.649883000538005e-06, "5": 2.3195226360047999e-07, "6": 9.7222277094091e-09, "7": 3.5112682742062927e-10, "8": 1.1135349358158483e-11, "9": 3.14682169244613e-13} |
| Unadjusted home-win probability | 1.0% |
| Unadjusted draw probability | 4.4% |
| Unadjusted away-win probability | 94.5% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.4% |
| Raw p btts yes | 21.9% |
| Home training matches | 13 |
| Away training matches | 3 |
| P home draw | 25.8% |
| P draw away | 89.3% |
| P home away | 84.9% |
| Raw p home draw | 5.5% |
| Raw p draw away | 99.0% |
| Raw p home away | 95.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9835 |
| Totals anchor target over 2 5 | 0.6154 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.43 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6237 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.57, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.52, "draw": 4.71, "home": 6.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.14, "home_away": 1.21, "home_draw": 2.64}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.14, "home_away": 1.21, "home_draw": 2.67}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.49, "draw": 4.61, "home": 6.01}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.57, "under": 2.43}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.01 |
| Reference draw odds | 4.61 |
| Reference away odds | 1.49 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:04Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:04Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -4.1% |
| Draw probability edge | -4.6% |
| Away probability edge | +8.7% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.1381 |
| Raw ev home | -0.9354 |
| Raw edge prob draw | -0.1529 |
| Raw ev draw | -0.7922 |
| Raw edge prob away | 0.2910 |
| Raw ev away | 0.4371 |
| Market p home draw | 36.6% |
| Market home draw odds | 2.67 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:54Z |
| Market reference home draw last update utc | 2026-11-04T10:20:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.5% |
| Market draw away odds | 1.14 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.21 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.13 |
| Market reference dc home draw odds | 2.61 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 83.2% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.94 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.5% |
| Market under 3 5 odds | 1.57 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.43 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
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
| Dinamo Zagreb win | 15.8% | 6.31 |

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
| 2 | 2-1 | 10.50% |
| 3 | 2-0 | 10.17% |
| 4 | 1-1 | 10.01% |
| 5 | 3-1 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 62.8% | 66.3% | 1.47 | -7.7% |
| Draw | 21.4% | 19.7% | 4.82 | +3.1% |
| Dinamo Zagreb win | 15.8% | 13.9% | 6.95 | +10.1% |
| Over 2.5 | 57.6% | 58.1% | 1.68 | -3.2% |
| Under 2.5 | 42.4% | 41.9% | 2.29 | -2.9% |

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
| Market best home last update utc | 2026-11-04T10:19:42Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
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
| Dc lambda home | 1.4771 |
| Dc lambda away | 0.7771 |
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
| Goal margin distribution | {"-1": 0.10343388028128862, "-10": 1.80724703918918e-08, "-11": 1.6703853160863297e-09, "-12": 1.418453499790308e-10, "-13": 1.11385134544479e-11, "-14": 8.131267834940999e-13, "-15": 5.511766289840027e-14, "-16": 3.1560479580031434e-15, "-2": 0.03969061284366961, "-3": 0.011831899679854967, "-4": 0.00278779158803488, "-5": 0.0005405926065104257, "-6": 8.885280197746946e-05, "-7": 1.2655344999009165e-05, "-8": 1.58897272842979e-06, "-9": 1.7827970105006386e-07, "0": 0.21394657379792467, "1": 0.25603332272441104, "10": 1.4754685659419922e-05, "11": 2.5920181496421145e-06, "12": 4.1835543248399584e-07, "13": 6.244051529165282e-08, "14": 8.663760658451519e-09, "15": 1.1162151403378377e-09, "16": 1.2148135954550208e-10, "2": 0.19025179553872903, "3": 0.10779642878484941, "4": 0.04827464989884912, "5": 0.017792536534477477, "6": 0.0055583747949398375, "7": 0.0015047336170246198, "8": 0.00035909636839553233, "9": 7.657824370975719e-05} |
| Raw goal margin distribution | {"-1": 0.14426661744191194, "-10": 2.5780573025574725e-09, "-11": 1.8057527664296969e-10, "-12": 1.160924013472197e-11, "-13": 6.896144400208685e-13, "-14": 3.797632298339265e-14, "-15": 1.82763407041095e-15, "-2": 0.045699735439368463, "-3": 0.010854313866072683, "-4": 0.0019982277983875626, "-5": 0.0002994175278274853, "-6": 3.77690484412777e-05, "-7": 4.11010344516723e-06, "-8": 3.9307016596423534e-07, "-9": 3.351746017043031e-08, "0": 0.2527024227235113, "1": 0.2687790234744361, "10": 1.586287552363692e-06, "11": 2.1118184218957084e-07, "12": 2.5805424922354927e-08, "13": 2.913550176978664e-09, "14": 3.049565757994495e-10, "15": 2.7894801202915223e-11, "2": 0.16509410108400968, "3": 0.07452966697131022, "4": 0.026078387631068744, "5": 0.0074271448731744035, "6": 0.0017806954678927485, "7": 0.00036831151556561013, "8": 6.69486096413307e-05, "9": 1.0850544116915542e-05} |
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
| Totals anchor scale | 1.3281 |
| Totals anchor target over 2 5 | 0.5760 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.22 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4085 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.1, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.18, "price": 5.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.43, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.02, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.95, "draw": 4.82, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.29}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.8, "home_away": 1.21, "home_draw": 1.12}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:19:54Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.74, "home_away": 1.21, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.37, "draw": 4.59, "home": 1.47}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.22}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 4.59 |
| Reference away odds | 6.37 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:05Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:05Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.1193 |
| Raw ev home | -0.2001 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.2180 |
| Raw edge prob away | 0.0640 |
| Raw ev away | 0.4120 |
| Market p home draw | 84.9% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:19:54Z |
| Market reference home draw last update utc | 2026-11-04T10:20:04Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.4% |
| Market draw away odds | 2.80 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:04Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.6% |
| Market home away odds | 1.21 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:04Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.61 |
| Market reference dc home draw odds | 1.12 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 80.7% |
| Market over 1 5 odds | 1.21 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.31 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.7% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,448.0520 |
| Elo away rating | 1,437.3148 |
| Elo rating diff | 70.7371 |
| Elo home expectancy | 0.6004 |

</details>


---

## 2026-11-05 — Torreense vs FC Ararat-Armenia

The model's most likely 1X2 outcome is **Torreense win** at **66.0%**. Expected goals are 4.80 for Torreense and 0.93 for FC Ararat-Armenia (5.73 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 47.3%; Under 3.5 goals: 73.9%; Double Chance 1X: 83.9%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 33.5%; BTTS No (at least one team does not score): 66.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torreense win | 66.0% | 1.52 |
| Draw | 18.0% | 5.56 |
| FC Ararat-Armenia win | 16.1% | 6.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torreense expected goals | 4.80 |
| FC Ararat-Armenia expected goals | 0.93 |
| Expected total goals | 5.73 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 71.0% |
| Under 1.5 | 29.0% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 26.1% |
| Under 3.5 | 73.9% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.12% |
| 2 | 1-0 | 12.62% |
| 3 | 3-0 | 10.77% |
| 4 | 0-1 | 8.66% |
| 5 | 1-1 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torreense win | 66.0% | 54.3% | 1.79 | +18.1% |
| Draw | 18.0% | 23.8% | 4.00 | -28.1% |
| FC Ararat-Armenia win | 16.1% | 21.9% | 4.67 | -25.0% |
| Over 2.5 | 47.3% | 47.3% | 2.04 | -3.6% |
| Under 2.5 | 52.7% | 52.7% | 1.85 | -2.4% |

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
| Market best home last update utc | 2026-11-04T10:20:08Z |
| Market best draw last update utc | 2026-11-04T10:19:42Z |
| Market best away last update utc | 2026-11-04T10:19:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | torreense |
| Matched away-team name | ararat-armenia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.8046 |
| Dc lambda away | 0.9299 |
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
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.88 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.84 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.05 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.13314720415524317, "-10": 1.5341096280887383e-11, "-11": 6.128081268038166e-13, "-12": 2.2465048443702572e-14, "-13": 7.60894695015889e-16, "-14": 2.3948311253356614e-17, "-15": 7.039154406974168e-19, "-16": 1.9406120765837003e-20, "-17": 5.030414379014719e-22, "-18": 1.1714285593990083e-23, "-2": 0.023791283527795175, "-3": 0.0032497306311926265, "-4": 0.00034289451914788733, "-5": 2.9393938089231256e-05, "-6": 2.118830045444446e-06, "-7": 1.3166747151753194e-07, "-8": 7.186996164015934e-09, "-9": 3.4966142585817166e-10, "0": 0.17975546700382267, "1": 0.200185389267213, "10": 6.397657226195661e-05, "11": 1.3204302377531194e-05, "12": 2.5010632639411446e-06, "13": 4.376916352406651e-07, "14": 7.11778650660326e-08, "15": 1.080978181141005e-08, "16": 1.5397901561724188e-09, "17": 2.0623052313189358e-10, "18": 2.4813690600548176e-11, "2": 0.19533112982733125, "3": 0.1378565248125986, "4": 0.07515655736508958, "5": 0.03328821310639508, "6": 0.012398101957243618, "7": 0.003980741251229974, "8": 0.001122688410723623, "9": 0.0002822187887129261} |
| Raw goal margin distribution | {"-1": 0.017789054477176623, "-10": 6.421360612223929e-10, "-11": 5.2553129103900075e-11, "-12": 3.96160817426063e-12, "-13": 2.7672103507896346e-13, "-14": 1.8003941015940925e-14, "-15": 1.0960385929236635e-15, "-16": 6.268496786131361e-17, "-17": 3.380122878720454e-18, "-18": 1.723935768684511e-19, "-19": 8.340213780008903e-21, "-2": 0.0050609298284903246, "-20": 3.8373248556810665e-22, "-21": 1.683055705103768e-23, "-22": 7.051886062826493e-25, "-23": 2.826142688546714e-26, "-24": 1.0730827884248824e-27, "-25": 3.3862501210825363e-29, "-3": 0.0011964728564763509, "-4": 0.0002324237415139614, "-5": 3.806703698732711e-05, "-6": 5.3686271937504835e-06, "-7": 6.632243038448885e-07, "-8": 7.278067969773304e-08, "-9": 7.177010301351393e-09, "0": 0.04305858086149503, "1": 0.0889046379292879, "10": 0.00870744596683576, "11": 0.003682041515914671, "12": 0.0014341282577951266, "13": 0.0005175889790191376, "14": 0.0001739950131291371, "15": 5.47294947710479e-05, "16": 1.617280584683101e-05, "17": 4.505892505808196e-06, "18": 1.1873965743886722e-06, "19": 2.9680982078117376e-07, "2": 0.13510862101510926, "20": 7.055958591861857e-08, "21": 1.5990141976815178e-08, "22": 3.4616686038589027e-09, "23": 7.168043963409777e-10, "24": 1.4062617919780815e-10, "25": 2.292864311067304e-11, "3": 0.16503724643667247, "4": 0.16564791714630303, "5": 0.14017834823752753, "6": 0.10214602808727576, "7": 0.06519961667316737, "8": 0.036968096555339336, "9": 0.018835663585075046} |
| Unadjusted home-win probability | 93.3% |
| Unadjusted draw probability | 4.3% |
| Unadjusted away-win probability | 2.4% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.7% |
| Raw p btts yes | 60.0% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 83.9% |
| P draw away | 34.0% |
| P home away | 82.0% |
| Raw p home draw | 97.6% |
| Raw p draw away | 6.7% |
| Raw p home away | 95.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.4761 |
| Totals anchor target over 2 5 | 0.4726 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-11-04T10:20:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.8605 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.43, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.35, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.25, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.25, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.67, "draw": 4.0, "home": 1.76}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.85}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:19:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.13, "home_away": 1.27, "home_draw": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.25, "draw": 3.92, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.03, "under": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.03, "under": 1.83}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:20:11Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.07, "home_away": 1.27, "home_draw": 1.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.92 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-11-04T10:20:08Z |
| Market reference home last update utc | 2026-11-04T10:20:08Z |
| Market reference draw last update utc | 2026-11-04T10:20:08Z |
| Market reference away last update utc | 2026-11-04T10:20:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:20:08Z |
| Market best over 2 5 last update utc | 2026-11-04T10:19:42Z |
| Market best under 2 5 last update utc | 2026-11-04T10:19:42Z |
| Home probability edge | +11.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3899 |
| Raw ev home | 0.6694 |
| Raw edge prob draw | -0.1953 |
| Raw ev draw | -0.8278 |
| Raw edge prob away | -0.1946 |
| Raw ev away | -0.8864 |
| Market p home draw | 77.7% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-04T10:20:11Z |
| Market reference home draw last update utc | 2026-11-04T10:20:11Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.5% |
| Market draw away odds | 2.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T10:19:42Z |
| Market reference draw away last update utc | 2026-11-04T10:20:11Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T10:19:42Z |
| Market reference home away last update utc | 2026-11-04T10:20:11Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.07 |
| Market reference dc home draw odds | 1.24 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 73.1% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-11-04T10:20:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.1% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.65 |
| Market reference under 3 5 last update utc | 2026-11-04T10:20:08Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,421.4152 |
| Elo away rating | 1,403.0006 |
| Elo rating diff | 78.4146 |
| Elo home expectancy | 0.6110 |

</details>


---
