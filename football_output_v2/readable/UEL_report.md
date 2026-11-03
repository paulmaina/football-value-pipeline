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
| Training as of utc | 2026-11-03T13:57:49.323273+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 795.093 |
| Base scoring parameter | 0.103 |
| Home-advantage parameter | 0.267 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 108, 'matches': 714, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-22'} |
| Training data health | {'training_end': '2026-10-22', 'verified_at_utc': '2026-11-03T11:55:13.839686+00:00', 'official_source_health': {'2025': {'status': 'REVIEWED_HISTORICAL_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 18.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 15, 'ANCHORED_MAIN': 2} |
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

The model's most likely 1X2 outcome is **Rennes win** at **46.6%**. Expected goals are 1.47 for Rennes and 0.71 for Olympiakos Piraeus (2.18 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 54.6%; Under 3.5 goals: 66.5%; Double Chance 1X: 72.7%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 83.2%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 46.6% | 2.15 |
| Draw | 26.1% | 3.83 |
| Olympiakos Piraeus win | 27.3% | 3.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.47 |
| Olympiakos Piraeus expected goals | 0.71 |
| Expected total goals | 2.18 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 54.6% |
| Under 2.5 | 45.4% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 16.8% |
| Under 4.5 | 83.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.25% |
| 2 | 0-1 | 8.10% |
| 3 | 1-0 | 7.94% |
| 4 | 2-0 | 7.64% |
| 5 | 2-1 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 46.6% | 42.7% | 2.26 | +5.3% |
| Draw | 26.1% | 26.4% | 3.67 | -4.2% |
| Olympiakos Piraeus win | 27.3% | 31.0% | 3.18 | -13.2% |
| Over 2.5 | 54.6% | 54.2% | 1.79 | -2.3% |
| Under 2.5 | 45.4% | 45.8% | 2.12 | -3.7% |

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
| Market best home last update utc | 2026-11-03T13:57:15Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
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
| Fair Under 0.5 odds | 17.04 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.56 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.95 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.1822641857192105, "-10": 2.0316488263435745e-08, "-11": 1.7846002038243441e-09, "-12": 1.4401623259365008e-10, "-13": 1.0746898377672648e-11, "-14": 7.457274126153266e-13, "-15": 4.834107013039087e-14, "-16": 2.9246194580104655e-15, "-17": 1.5109603368868616e-16, "-2": 0.06662012585190266, "-3": 0.018919580773708238, "-4": 0.0042428784281127434, "-5": 0.0007826766946366148, "-6": 0.00012233494426075022, "-7": 1.656625571216245e-05, "-8": 1.977293055248667e-06, "-9": 2.108689443890449e-07, "0": 0.26095488630340963, "1": 0.1835607950730746, "10": 1.3893219710896702e-05, "11": 2.512614681649724e-06, "12": 4.174717508157476e-07, "13": 6.414007780320108e-08, "14": 9.163410464020521e-09, "15": 1.2229930405801769e-09, "16": 1.523378364367708e-10, "17": 1.6203997778667484e-11, "2": 0.1410958270823784, "3": 0.0824994251587971, "4": 0.03809172972955297, "5": 0.014467157219613485, "6": 0.004655668183987926, "7": 0.0012980354245791543, "8": 0.0003189803409171704, "9": 7.00383963310183e-05} |
| Raw goal margin distribution | {"-1": 0.13666076517635828, "-10": 1.1456026200762476e-09, "-11": 7.3549041354685e-11, "-12": 4.333602023273465e-12, "-13": 2.359091951277404e-13, "-14": 1.190941500778736e-14, "-15": 5.283669501922654e-16, "-2": 0.04009356182787421, "-3": 0.008785341081938382, "-4": 0.0014881924852663672, "-5": 0.00020489212563102975, "-6": 2.3726940868319255e-05, "-7": 2.369041909695212e-06, "-8": 2.0779654049556985e-07, "-9": 1.6246859270598765e-08, "0": 0.2544228237284157, "1": 0.27510790073768554, "10": 1.567981465906505e-06, "11": 2.0725959050828423e-07, "12": 2.514301400639217e-08, "13": 2.8180187182393087e-09, "14": 2.929005091985506e-10, "15": 2.6754450418036345e-11, "2": 0.169955813685346, "3": 0.0766744563205562, "4": 0.026741260694514043, "5": 0.007580166259510053, "6": 0.0018072819198419205, "7": 0.00037152461461198736, "8": 6.709402624481668e-05, "9": 1.0800544549981047e-05} |
| Unadjusted home-win probability | 55.8% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 18.7% |
| Raw p over 1 5 | 63.4% |
| Raw p under 3 5 | 82.4% |
| Raw p btts yes | 38.6% |
| Home training matches | 19 |
| Away training matches | 25 |
| P home draw | 72.7% |
| P draw away | 53.4% |
| P home away | 73.9% |
| Raw p home draw | 81.3% |
| Raw p draw away | 44.2% |
| Raw p home away | 74.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.3776 |
| Totals anchor target over 2 5 | 0.5459 |
| Totals anchor reference over odds | 1.76 |
| Totals anchor reference under odds | 2.09 |
| Totals anchor reference last update utc | 2026-11-03T13:57:15Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3613 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.26, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.65, "price": 2.26, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.67, "home": 2.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.79, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.31, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.07, "draw": 3.58, "home": 2.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.76, "under": 2.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:34Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.66, "home_away": 1.31, "home_draw": 1.39}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.58 |
| Reference away odds | 3.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | +4.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | 0.1318 |
| Raw ev home | 0.2618 |
| Raw edge prob draw | -0.0093 |
| Raw ev draw | -0.0663 |
| Raw edge prob away | -0.1224 |
| Raw ev away | -0.4045 |
| Market p home draw | 69.0% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-03T13:57:34Z |
| Market reference home draw last update utc | 2026-11-03T13:57:34Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.8% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:56:12Z |
| Market reference draw away last update utc | 2026-11-03T13:57:34Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-03T13:57:34Z |
| Market reference home away last update utc | 2026-11-03T13:57:34Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home draw odds | 1.39 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 78.5% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-03T13:57:15Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-03T13:57:40Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 68.5% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:57:15Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-11-03T13:57:40Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,490.6687 |
| Elo away rating | 1,481.7280 |
| Elo rating diff | 68.9408 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-05 — AC Milan vs Ferencváros TC

The model's most likely 1X2 outcome is **AC Milan win** at **76.4%**. Expected goals are 2.92 for AC Milan and 1.00 for Ferencváros TC (3.92 combined). The most likely exact score is 2-0 at 8.4%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 74.7%; Under 3.5 goals: 44.8%; Double Chance 1X: 90.7%; Double Chance X2: 23.6%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 64.6%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 76.4% | 1.31 |
| Draw | 14.2% | 7.03 |
| Ferencváros TC win | 9.3% | 10.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 2.92 |
| Ferencváros TC expected goals | 1.00 |
| Expected total goals | 3.92 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 90.0% |
| Under 1.5 | 10.0% |
| Over 2.5 | 74.7% |
| Under 2.5 | 25.3% |
| Over 3.5 | 55.2% |
| Under 3.5 | 44.8% |
| Over 4.5 | 35.4% |
| Under 4.5 | 64.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 8.41% |
| 2 | 2-1 | 8.41% |
| 3 | 3-0 | 8.20% |
| 4 | 3-1 | 8.20% |
| 5 | 1-0 | 6.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 76.4% | 76.3% | 1.30 | -0.6% |
| Draw | 14.2% | 14.7% | 5.73 | -18.5% |
| Ferencváros TC win | 9.3% | 9.0% | 11.10 | +3.5% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | milan |
| Matched away-team name | ferencvaros |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9239 |
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
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.37 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 10.04 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.96 |
| Fair Over 3.5 odds | 1.81 |
| Fair Under 3.5 odds | 2.23 |
| Fair Over 4.5 odds | 2.82 |
| Fair Under 4.5 odds | 1.55 |
| Goal margin distribution | {"-1": 0.06381894756967943, "-10": 6.48674643697269e-09, "-11": 5.770666008791941e-10, "-12": 4.721072525446104e-11, "-13": 3.5744122151519463e-12, "-14": 2.518130140903301e-13, "-15": 1.6585116575265428e-14, "-16": 1.025494899411789e-15, "-17": 5.974708292430679e-17, "-18": 3.2894039354611103e-18, "-19": 1.702867688388481e-19, "-2": 0.02182624980419179, "-20": 7.42737345461892e-21, "-3": 0.0059878492569554395, "-4": 0.0013199520566631055, "-5": 0.00024184784393375483, "-6": 3.77968413135303e-05, "-7": 5.140539014767171e-06, "-8": 6.181422224716433e-07, "-9": 6.656474948214672e-08, "0": 0.1422765972923019, "1": 0.1971339808158283, "10": 0.00032220705370986487, "11": 8.382311127796228e-05, "12": 2.005433314312806e-05, "13": 4.440193577090187e-06, "14": 9.147557660459594e-07, "15": 1.7618755485951748e-07, "16": 3.1858103600179445e-08, "17": 5.427912493136674e-09, "18": 8.739026465240091e-10, "19": 1.322989713354385e-10, "2": 0.2026980254289551, "20": 1.687487402219704e-11, "3": 0.1626188819234714, "4": 0.10483057910409734, "5": 0.05616965592521717, "6": 0.025671117024498345, "7": 0.010210044488428714, "8": 0.003590352583778523, "9": 0.001130635735710361} |
| Raw goal margin distribution | {"-1": 0.06960124554409232, "-10": 7.074476291685266e-09, "-11": 6.293515595699015e-10, "-12": 5.148823987049852e-11, "-13": 3.898270838624599e-12, "-14": 2.7462846211562934e-13, "-15": 1.8087806444506102e-14, "-16": 1.118409579227925e-15, "-17": 6.516045073632059e-17, "-18": 3.587439463111822e-18, "-19": 1.8571555411380298e-19, "-2": 0.023803811090266157, "-20": 8.100328558351395e-21, "-3": 0.006530376671588533, "-4": 0.0014395459452215462, "-5": 0.0002637604004917805, "-6": 4.122141359635914e-05, "-7": 5.606296120837041e-06, "-8": 6.74148826419387e-07, "-9": 7.259583007428085e-08, "0": 0.13055393719525787, "1": 0.19797844104073464, "10": 0.00032358728780200967, "11": 8.418218323049524e-05, "12": 2.0140239624630174e-05, "13": 4.459213975558376e-06, "14": 9.186742932158198e-07, "15": 1.7694228715674308e-07, "16": 3.199457373698671e-08, "17": 5.451163970054844e-09, "18": 8.776461717263909e-10, "19": 1.3286569868820867e-10, "2": 0.20356632027814053, "20": 1.6947160696737257e-11, "3": 0.16331549027599793, "4": 0.105279640468561, "5": 0.05641026913699945, "6": 0.025781084048785027, "7": 0.010253781120892183, "8": 0.0036057325296297836, "9": 0.0011354790250494892} |
| Unadjusted home-win probability | 76.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 10.2% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.9% |
| Raw p btts yes | 59.5% |
| Home training matches | 9 |
| Away training matches | 33 |
| P home draw | 90.7% |
| P draw away | 23.6% |
| P home away | 85.8% |
| Raw p home draw | 89.8% |
| Raw p draw away | 23.2% |
| Raw p home away | 86.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7474 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.95, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.76, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 11.1, "draw": 5.73, "home": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.86, "draw": 5.14, "home": 1.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 5.14 |
| Reference away odds | 7.86 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +11.7% |
| Under 2.5 probability edge | -11.7% |
| Raw edge prob home | 0.0047 |
| Raw ev home | -0.0019 |
| Raw edge prob draw | -0.0167 |
| Raw ev draw | -0.2519 |
| Raw edge prob away | 0.0121 |
| Raw ev away | 0.1287 |
| Elo home rating | 1,446.6112 |
| Elo away rating | 1,471.6144 |
| Elo rating diff | 34.9969 |
| Elo home expectancy | 0.5502 |

</details>


---

## 2026-11-05 — AZ Alkmaar vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **54.7%**. Expected goals are 0.79 for AZ Alkmaar and 2.01 for Juventus (2.80 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.6%; Under 3.5 goals: 70.9%; Double Chance 1X: 45.3%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AZ Alkmaar win | 22.2% | 4.50 |
| Draw | 23.1% | 4.33 |
| Juventus win | 54.7% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AZ Alkmaar expected goals | 0.79 |
| Juventus expected goals | 2.01 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 29.1% |
| Under 3.5 | 70.9% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.95% |
| 2 | 0-1 | 10.47% |
| 3 | 0-2 | 10.12% |
| 4 | 1-0 | 8.23% |
| 5 | 1-2 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AZ Alkmaar win | 22.2% | 25.6% | 3.85 | -14.5% |
| Draw | 23.1% | 24.7% | 3.83 | -11.5% |
| Juventus win | 54.7% | 49.7% | 1.96 | +7.2% |
| Over 2.5 | 50.6% | 53.8% | 1.81 | -8.4% |
| Under 2.5 | 49.4% | 46.2% | 2.09 | +3.3% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda away | 2.0100 |
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
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.97 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.44 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.12 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.2088401089153781, "-10": 1.715222636436218e-05, "-11": 3.0972316314213166e-06, "-12": 5.135931141003339e-07, "-13": 7.872607044347644e-08, "-14": 1.1218280789755448e-08, "-15": 1.4932126527654448e-09, "-16": 1.8580150660002554e-10, "-17": 2.009129107322251e-11, "-2": 0.1666189437760116, "-3": 0.09940323157517013, "-4": 0.04644116289849027, "-5": 0.01776221257940334, "-6": 0.005739109980416947, "-7": 0.0016034123354500107, "-8": 0.0003943022416348653, "-9": 8.655350288979935e-05, "0": 0.23096037733271846, "1": 0.15964405256245248, "10": 2.850548161408656e-09, "11": 2.0230679537953617e-10, "12": 1.31851440373528e-11, "13": 7.943523083480685e-13, "14": 4.448870813110327e-14, "15": 2.327416191882674e-15, "16": 1.138231296478521e-16, "17": 4.837467255792692e-18, "2": 0.04862963946778921, "3": 0.011402657442467738, "4": 0.002093811406718413, "5": 0.0003147461599021842, "6": 3.997024639125894e-05, "7": 4.389008276561556e-06, "8": 4.2420846137310503e-07, "9": 3.659852905855544e-08} |
| Raw goal margin distribution | {"-1": 0.25346773177321824, "-10": 2.08175332507478e-05, "-11": 3.7590876602670537e-06, "-12": 6.233442529859235e-07, "-13": 9.554926307193282e-08, "-14": 1.3615546366749664e-08, "-15": 1.8123014114347534e-09, "-16": 2.2550594654706797e-10, "-17": 2.4384654859515958e-11, "-2": 0.20222420860002346, "-3": 0.12064498418977328, "-4": 0.05636530397310127, "-5": 0.021557869114114267, "-6": 0.006965516330595086, "-7": 0.0019460499703550297, "-8": 0.00047856178269271794, "-9": 0.00010504936129579213, "0": 0.1935284121176974, "1": 0.10255164737111398, "10": 1.8311262159221334e-09, "11": 1.2995720672040792e-10, "12": 8.469831604450085e-12, "13": 5.102735523597015e-13, "14": 2.857851723898398e-14, "15": 1.4950783368669594e-15, "16": 7.311734616456669e-17, "17": 3.1074770918339907e-18, "2": 0.031238555764764253, "3": 0.007324803438425043, "4": 0.001345016025319222, "5": 0.00020218565417007346, "6": 2.5675961913140483e-05, "7": 2.81939741482548e-06, "8": 2.7250170516411245e-07, "9": 2.3510048674354374e-08} |
| Unadjusted home-win probability | 14.3% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 66.4% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 46.8% |
| Home training matches | 15 |
| Away training matches | 11 |
| P home draw | 45.3% |
| P draw away | 77.8% |
| P home away | 76.9% |
| Raw p home draw | 33.6% |
| Raw p draw away | 85.7% |
| Raw p home away | 80.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5060 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.95, "draw": 3.8, "home": 3.67}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.96, "draw": 3.83, "home": 3.85}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.95 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -3.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.1135 |
| Raw ev home | -0.4506 |
| Raw edge prob draw | -0.0535 |
| Raw ev draw | -0.2588 |
| Raw edge prob away | 0.1670 |
| Raw ev away | 0.3010 |
| Elo home rating | 1,483.3792 |
| Elo away rating | 1,491.7497 |
| Elo rating diff | 51.6295 |
| Elo home expectancy | 0.5738 |

</details>


---

## 2026-11-05 — Anderlecht vs Salzburg

The model's most likely 1X2 outcome is **Anderlecht win** at **50.7%**. Expected goals are 1.85 for Anderlecht and 1.24 for Salzburg (3.09 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 59.0%; Under 3.5 goals: 62.8%; Double Chance 1X: 74.4%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

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
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.80% |
| 2 | 2-1 | 9.40% |
| 3 | 1-0 | 8.72% |
| 4 | 2-0 | 7.58% |
| 5 | 2-2 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Anderlecht win | 50.7% | 50.2% | 1.93 | -2.1% |
| Draw | 23.6% | 24.4% | 4.00 | -5.5% |
| Salzburg win | 25.6% | 25.4% | 3.81 | -2.3% |
| Over 2.5 | 59.0% | 59.5% | 1.64 | -3.2% |
| Under 2.5 | 41.0% | 40.5% | 2.37 | -2.8% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda away | 1.2404 |
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
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.74 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.21 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.09 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.15358129182186583, "-10": 1.3061794739231e-07, "-11": 1.4480844590987317e-08, "-12": 1.4753948333682902e-09, "-13": 1.3903760011634443e-10, "-14": 1.2181586355192618e-11, "-15": 9.895862914049518e-13, "-16": 6.711091445994174e-14, "-2": 0.06946152203894412, "-3": 0.024495784161797898, "-4": 0.006863260635292038, "-5": 0.0015874544350799413, "-6": 0.0003118173968167842, "-7": 5.3144554180771996e-05, "-8": 7.991807107967698e-06, "-9": 1.0746190533226594e-06, "0": 0.2362149072297416, "1": 0.22473673976684766, "10": 6.923605931150066e-06, "11": 1.14238900161046e-06, "12": 1.7322836758945605e-07, "13": 2.429593692902588e-08, "14": 3.1680780377383253e-09, "15": 3.830331190649941e-10, "16": 3.866040925653507e-11, "2": 0.15294972834311746, "3": 0.08027612403629428, "4": 0.03347465997998991, "5": 0.011523319013769228, "6": 0.003368738439416004, "7": 0.0008545084324781157, "8": 0.0001912463748615966, "9": 3.8273077873982786e-05} |
| Raw goal margin distribution | {"-1": 0.15677449670167107, "-10": 1.3333370698812742e-07, "-11": 1.4781924905282854e-08, "-12": 1.5060706919032964e-09, "-13": 1.4192841798811277e-10, "-14": 1.2434861350680263e-11, "-15": 1.0101614001126436e-12, "-16": 6.850625953745441e-14, "-2": 0.07090574007163734, "-3": 0.02500509136056032, "-4": 0.007005958988014641, "-5": 0.0016204601950161527, "-6": 0.00031830058771400885, "-7": 5.424951590971711e-05, "-8": 8.157969777606026e-06, "-9": 1.0969621314690631e-06, "0": 0.2172520910257788, "1": 0.2307746115509906, "10": 7.109618440451326e-06, "11": 1.1730809050637845e-06, "12": 1.7788239378012968e-07, "13": 2.4948681790436927e-08, "14": 3.2531929549248424e-09, "15": 3.9332384796136456e-10, "16": 3.9699076073788083e-11, "2": 0.1570589400817647, "3": 0.08243285615211096, "4": 0.03437400427583866, "5": 0.011832909349577677, "6": 0.0034592443833600566, "7": 0.000877466015466658, "8": 0.00019638448041476257, "9": 3.930133848338455e-05} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5900 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.81, "draw": 4.0, "home": 1.93}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.83, "home": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.83 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.37 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0195 |
| Raw ev home | 0.0056 |
| Raw edge prob draw | -0.0271 |
| Raw ev draw | -0.1310 |
| Raw edge prob away | 0.0076 |
| Raw ev away | -0.0029 |
| Elo home rating | 1,445.9180 |
| Elo away rating | 1,427.7213 |
| Elo rating diff | 78.1968 |
| Elo home expectancy | 0.6107 |

</details>


---

## 2026-11-05 — Bayer Leverkusen vs Marseille

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **75.0%**. Expected goals are 2.87 for Bayer Leverkusen and 0.55 for Marseille (3.42 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 62.9%; Under 3.5 goals: 58.2%; Double Chance 1X: 89.9%; Double Chance X2: 25.0%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 76.2%; BTTS Yes (both teams score): 41.8%; BTTS No (at least one team does not score): 58.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 75.0% | 1.33 |
| Draw | 14.8% | 6.74 |
| Marseille win | 10.1% | 9.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.87 |
| Marseille expected goals | 0.55 |
| Expected total goals | 3.42 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 62.9% |
| Under 2.5 | 37.1% |
| Over 3.5 | 41.8% |
| Under 3.5 | 58.2% |
| Over 4.5 | 23.8% |
| Under 4.5 | 76.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.92% |
| 2 | 3-0 | 11.39% |
| 3 | 1-0 | 8.55% |
| 4 | 4-0 | 8.16% |
| 5 | 1-1 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 75.0% | 70.9% | 1.42 | +6.5% |
| Draw | 14.8% | 16.7% | 5.53 | -18.0% |
| Marseille win | 10.1% | 12.4% | 7.37 | -25.2% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:57:15Z |
| Market best away last update utc | 2026-11-03T13:57:15Z |
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
| P btts yes | 41.8% |
| P btts no | 58.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.22 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.69 |
| Fair Over 3.5 odds | 2.39 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.20 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.08130944700427489, "-10": 5.678156208798161e-11, "-11": 2.8169422557235337e-12, "-12": 1.283329937392253e-13, "-13": 5.4044386981820276e-15, "-14": 2.1157821964004292e-16, "-15": 7.73801408439427e-18, "-16": 2.6551544831397533e-19, "-17": 8.57946816408576e-21, "-18": 2.611952851025985e-22, "-19": 7.00736888606153e-24, "-2": 0.01697963639082335, "-3": 0.002783902796971713, "-4": 0.0003574001443592751, "-5": 3.7559303427429135e-05, "-6": 3.33438560971316e-06, "-7": 2.559502085711603e-07, "-8": 1.7293000893576843e-08, "-9": 1.0429194906166705e-09, "0": 0.14831764360198058, "1": 0.17117956542446752, "10": 0.0003449699071556637, "11": 8.882168989027256e-05, "12": 2.100132153072369e-05, "13": 4.5901418293911584e-06, "14": 9.326392302213508e-07, "15": 1.7702697502799982e-07, "16": 3.152585968370238e-08, "17": 5.286944144526507e-09, "18": 8.353662008704947e-10, "19": 1.1631447326774337e-10, "2": 0.19595870960707001, "3": 0.16674678293812423, "4": 0.11110288371981311, "5": 0.06059758944423701, "6": 0.02792034969777481, "7": 0.011123148352979449, "8": 0.0039004060108471595, "9": 0.0012208363402825735} |
| Raw goal margin distribution | {"-1": 0.039329446343386205, "-10": 2.74652882501527e-11, "-11": 1.3625572843100408e-12, "-12": 6.207477454726282e-14, "-13": 2.6141314401645716e-15, "-14": 1.0234055873390402e-16, "-15": 3.742883772417622e-18, "-16": 1.2843004057395202e-19, "-17": 4.1498958023470585e-21, "-18": 1.2634037407791026e-22, "-19": 3.389470089474121e-24, "-2": 0.008213064077633987, "-3": 0.001346576070956986, "-4": 0.000172874743570173, "-5": 1.8167465937462e-05, "-6": 1.612845059916323e-06, "-7": 1.2380332624877787e-07, "-8": 8.364638745166994e-09, "-9": 5.044610147763457e-10, "0": 0.10396694852977406, "1": 0.19325332834584666, "10": 0.0003894540950123288, "11": 0.00010027532876388715, "12": 2.370946132156457e-05, "13": 5.182044853950442e-06, "14": 1.0529039195727648e-06, "15": 1.9985476681358656e-07, "16": 3.55911483811303e-08, "17": 5.968700470612908e-09, "18": 9.430874433261835e-10, "19": 1.313133319274831e-10, "2": 0.2212277660363228, "3": 0.18824893446743707, "4": 0.1254297030982327, "5": 0.06841170452089532, "6": 0.031520704555449836, "7": 0.012557488597237964, "8": 0.004403366965135552, "9": 0.0013782643129169156} |
| Unadjusted home-win probability | 84.7% |
| Unadjusted draw probability | 10.4% |
| Unadjusted away-win probability | 4.9% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 55.4% |
| Raw p btts yes | 39.8% |
| Home training matches | 24 |
| Away training matches | 17 |
| P home draw | 89.9% |
| P draw away | 25.0% |
| P home away | 85.2% |
| Raw p home draw | 95.1% |
| Raw p draw away | 15.3% |
| Raw p home away | 89.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6288 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.2, "draw": 5.32, "home": 1.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.37, "draw": 5.53, "home": 1.39}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.39 |
| Reference draw odds | 5.53 |
| Reference away odds | 7.37 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +4.1% |
| Draw probability edge | -1.9% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.1382 |
| Raw ev home | 0.2027 |
| Raw edge prob draw | -0.0634 |
| Raw ev draw | -0.4251 |
| Raw edge prob away | -0.0748 |
| Raw ev away | -0.6383 |
| Elo home rating | 1,523.2260 |
| Elo away rating | 1,423.2467 |
| Elo rating diff | 159.9793 |
| Elo home expectancy | 0.7152 |

</details>


---

## 2026-11-05 — Benfica vs Lech Poznań

The model's most likely 1X2 outcome is **Benfica win** at **89.9%**. Expected goals are 5.16 for Benfica and 0.20 for Lech Poznań (5.35 combined). The most likely exact score is 5-0 at 13.1%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 83.8%; Under 3.5 goals: 28.0%; Double Chance 1X: 96.8%; Double Chance X2: 10.1%; Double Chance 12 (either team wins): 93.1%; Under 4.5 goals: 43.4%; BTTS Yes (both teams score): 20.4%; BTTS No (at least one team does not score): 79.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Benfica win | 89.9% | 1.11 |
| Draw | 6.9% | 14.48 |
| Lech Poznań win | 3.2% | 30.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Benfica expected goals | 5.16 |
| Lech Poznań expected goals | 0.20 |
| Expected total goals | 5.35 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 92.7% |
| Under 1.5 | 7.3% |
| Over 2.5 | 83.8% |
| Under 2.5 | 16.2% |
| Over 3.5 | 72.0% |
| Under 3.5 | 28.0% |
| Over 4.5 | 56.6% |
| Under 4.5 | 43.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-0 | 13.10% |
| 2 | 4-0 | 12.70% |
| 3 | 6-0 | 11.26% |
| 4 | 3-0 | 9.85% |
| 5 | 7-0 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Benfica win | 89.9% | 86.0% | 1.17 | +5.1% |
| Draw | 6.9% | 9.4% | 8.65 | -40.3% |
| Lech Poznań win | 3.2% | 4.5% | 17.00 | -45.1% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda away | 0.1953 |
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
| P btts yes | 20.4% |
| P btts no | 79.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.41 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.76 |
| Fair Over 2.5 odds | 1.19 |
| Fair Under 2.5 odds | 6.18 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.58 |
| Fair Over 4.5 odds | 1.77 |
| Fair Under 4.5 odds | 2.30 |
| Goal margin distribution | {"-1": 0.02996933768088535, "-10": 2.0216911529444053e-15, "-11": 3.5632179896129724e-17, "-12": 5.763444253778714e-19, "-13": 8.612993141831644e-21, "-14": 1.1960727609660293e-22, "-15": 1.5511550201158253e-24, "-16": 1.886845299037598e-26, "-17": 2.161053390797047e-28, "-18": 2.3384083698147133e-30, "-19": 2.3978448702392878e-32, "-2": 0.0021808845063560145, "-20": 2.33643830002597e-34, "-21": 2.168664462577174e-36, "-22": 1.9218031579342685e-38, "-23": 1.629265737755768e-40, "-24": 1.32388616061394e-42, "-25": 1.0321403070180266e-44, "-26": 7.4654427454402e-47, "-3": 0.00013148220455710483, "-4": 6.122459656035347e-06, "-5": 2.3159904254882902e-07, "-6": 7.36663871411871e-09, "-7": 2.019917052349147e-10, "-8": 4.864920521275008e-12, "-9": 1.0443433843418195e-13, "0": 0.06904726922673578, "1": 0.035665339523688146, "10": 0.01731988783300697, "11": 0.008059780503341654, "12": 0.003442020692394539, "13": 0.0013581134152471181, "14": 0.0004979549976447968, "15": 0.00017050544634002277, "16": 5.47608152552393e-05, "17": 1.6559593259111293e-05, "18": 4.731023259625574e-06, "19": 1.2808738724883829e-06, "2": 0.07911493393834707, "20": 3.295263581580314e-07, "21": 8.075673693039984e-08, "22": 1.8894954917138704e-08, "23": 4.229406611077982e-09, "24": 9.073789815186082e-10, "25": 1.8677870886720016e-10, "26": 3.5669314033718805e-11, "3": 0.12593409850616297, "4": 0.15482919298501924, "5": 0.15463729190807943, "6": 0.1298665802883076, "7": 0.09401824213014613, "8": 0.059786743491996586, "9": 0.0338862122465132} |
| Raw goal margin distribution | {"-1": 0.0017142148866386112, "-10": 1.156386273018395e-16, "-11": 2.038123560544637e-18, "-12": 3.296630056806569e-20, "-13": 4.9265423278476325e-22, "-14": 6.841411559317255e-24, "-15": 8.872445081302878e-26, "-16": 1.079255849707113e-27, "-17": 1.2361000208849816e-29, "-18": 1.3375452208052558e-31, "-19": 1.3715422797067251e-33, "-2": 0.00012474432123401322, "-20": 1.3364183614146548e-35, "-21": 1.2404534746341751e-37, "-22": 1.0992513807274418e-39, "-23": 9.319230246895028e-42, "-24": 7.572490886866367e-44, "-25": 5.9037350048564e-46, "-26": 4.270155458838874e-48, "-3": 7.520645093321719e-06, "-4": 3.5019831258780266e-07, "-5": 1.3247223902504451e-08, "-6": 4.2136405824826863e-10, "-7": 1.1553715059644253e-11, "-8": 2.78268384462907e-13, "-9": 5.973535335561039e-15, "0": 0.010371184183075845, "1": 0.03920214156815752, "10": 0.0190374381357897, "11": 0.008859039631192105, "12": 0.0037833533695692894, "13": 0.0014927925846540712, "14": 0.0005473353842398587, "15": 0.0001874138515104832, "16": 6.019124619850574e-05, "17": 1.8201747913366195e-05, "18": 5.200181634690598e-06, "19": 1.4078934772762599e-06, "2": 0.08696047428194477, "20": 3.622042889671799e-07, "21": 8.876508890726552e-08, "22": 2.0768698895846862e-08, "23": 4.648821486941361e-09, "24": 9.973604559641847e-10, "25": 2.0530087431430343e-10, "26": 3.9206510215896946e-11, "3": 0.13842252516951148, "4": 0.17018304110776747, "5": 0.16997210989876332, "6": 0.14274497687182724, "7": 0.10334168935998288, "8": 0.06571557746466118, "9": 0.03724658470765829} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8383 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.77, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.38, "draw": 6.83, "home": 1.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 17.0, "draw": 8.65, "home": 1.17}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.13 |
| Reference draw odds | 6.83 |
| Reference away odds | 12.38 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +3.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +8.3% |
| Under 2.5 probability edge | -8.3% |
| Raw edge prob home | 0.1273 |
| Raw ev home | 0.1557 |
| Raw edge prob draw | -0.0838 |
| Raw ev draw | -0.9103 |
| Raw edge prob away | -0.0435 |
| Raw ev away | -0.9686 |
| Elo home rating | 1,490.8432 |
| Elo away rating | 1,407.9321 |
| Elo rating diff | 142.9112 |
| Elo home expectancy | 0.6948 |

</details>


---

## 2026-11-05 — Celta Vigo vs Union Saint-Gilloise

The model's most likely 1X2 outcome is **Celta Vigo win** at **39.1%**. Expected goals are 1.05 for Celta Vigo and 1.34 for Union Saint-Gilloise (2.39 combined). The most likely exact score is 1-0 at 13.4%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 42.5%; Under 3.5 goals: 78.4%; Double Chance 1X: 64.9%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 47.4%; BTTS No (at least one team does not score): 52.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 39.1% | 2.56 |
| Draw | 25.8% | 3.88 |
| Union Saint-Gilloise win | 35.1% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.05 |
| Union Saint-Gilloise expected goals | 1.34 |
| Expected total goals | 2.39 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 67.8% |
| Under 1.5 | 32.2% |
| Over 2.5 | 42.5% |
| Under 2.5 | 57.5% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.42% |
| 2 | 1-1 | 12.12% |
| 3 | 0-1 | 10.31% |
| 4 | 2-1 | 8.84% |
| 5 | 0-0 | 8.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 39.1% | 43.0% | 2.24 | -12.4% |
| Draw | 25.8% | 25.7% | 3.77 | -2.7% |
| Union Saint-Gilloise win | 35.1% | 31.3% | 3.21 | +12.7% |
| Over 2.5 | 42.5% | 56.6% | 1.72 | -26.8% |
| Under 2.5 | 57.5% | 43.4% | 2.22 | +27.5% |

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
| Market best home last update utc | 2026-11-03T13:57:15Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | celta |
| Matched away-team name | union sg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0486 |
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
| P btts yes | 47.4% |
| P btts no | 52.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.85 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.11 |
| Fair Over 2.5 odds | 2.35 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.63 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.70 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.19019916871806355, "-10": 4.2920509302946256e-07, "-11": 5.17655397394752e-08, "-12": 5.731363154651171e-09, "-13": 5.840967493833899e-10, "-14": 5.083124411452823e-11, "-2": 0.1024296684664517, "-3": 0.041247917227722725, "-4": 0.012954205777157085, "-5": 0.00332275309105611, "-6": 0.0007189805618595641, "-7": 0.00013439485941961997, "-8": 2.2097939881937726e-05, "-9": 3.241844000566948e-06, "0": 0.2580304649037163, "1": 0.24589887337000996, "10": 6.030705925646801e-08, "11": 5.688686398052664e-09, "12": 4.926030940145619e-10, "13": 3.926376653793996e-11, "14": 2.6724271198502984e-12, "2": 0.10279816433002424, "3": 0.032376476130598124, "4": 0.007952548146219351, "5": 0.0015953704652491383, "6": 0.00026999056501036603, "7": 3.947135701018456e-05, "8": 5.075971201432699e-06, "9": 5.824081393751985e-07} |
| Raw goal margin distribution | {"-1": 0.23859041681330204, "-10": 5.384052030011108e-07, "-11": 6.493593944837239e-08, "-12": 7.189559939684192e-09, "-13": 7.327050261783953e-10, "-14": 6.376393652067625e-11, "-2": 0.1284902424031365, "-3": 0.051742380528649996, "-4": 0.016250067635356913, "-5": 0.004168141481932111, "-6": 0.000901906528251003, "-7": 0.00016858814758556278, "-8": 2.772018785719376e-05, "-9": 4.0666471707113865e-06, "0": 0.2607550668684602, "1": 0.1880083989032799, "10": 4.6109335508474914e-08, "11": 4.349433598060508e-09, "12": 3.76632547076057e-10, "13": 3.0020137060988154e-11, "14": 2.043273875568867e-12, "2": 0.07859701844506801, "3": 0.02475427949718453, "4": 0.006080328159625868, "5": 0.0012197821109075995, "6": 0.0002064283302762851, "7": 3.017885577238117e-05, "8": 3.8809662093267255e-06, "9": 4.4529533743493667e-07} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 47.3% |
| Home training matches | 17 |
| Away training matches | 29 |
| P home draw | 64.9% |
| P draw away | 60.9% |
| P home away | 74.2% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.1% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4255 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.64, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.37, "price": 1.64, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.21, "draw": 3.77, "home": 2.2}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.04, "draw": 3.67, "home": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.24 |
| Reference draw odds | 3.67 |
| Reference away odds | 3.04 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | -0.1315 |
| Raw ev home | -0.3305 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0170 |
| Raw edge prob away | 0.1276 |
| Raw ev away | 0.4135 |
| Elo home rating | 1,446.1006 |
| Elo away rating | 1,494.2964 |
| Elo rating diff | 11.8042 |
| Elo home expectancy | 0.5170 |

</details>


---

## 2026-11-05 — Celtic vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **46.2%**. Expected goals are 2.00 for Celtic and 2.43 for Besiktas JK (4.43 combined). The most likely exact score is 2-2 at 8.4%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 81.2%; Under 3.5 goals: 35.3%; Double Chance 1X: 53.8%; Double Chance X2: 68.4%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 55.2%; BTTS Yes (both teams score): 79.4%; BTTS No (at least one team does not score): 20.6%.

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
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 93.3% |
| Under 1.5 | 6.7% |
| Over 2.5 | 81.2% |
| Under 2.5 | 18.8% |
| Over 3.5 | 64.7% |
| Under 3.5 | 35.3% |
| Over 4.5 | 44.8% |
| Under 4.5 | 55.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.40% |
| 2 | 1-2 | 6.68% |
| 3 | 1-1 | 6.56% |
| 4 | 2-1 | 5.56% |
| 5 | 2-3 | 5.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 31.6% | 31.0% | 3.10 | -2.1% |
| Draw | 22.3% | 23.8% | 3.94 | -12.2% |
| Besiktas JK win | 46.2% | 45.1% | 2.23 | +2.9% |
| Over 2.5 | 81.2% | 58.4% | 1.67 | +35.5% |
| Under 2.5 | 18.8% | 41.6% | 2.31 | -56.5% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:57:16Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda home | 2.0015 |
| Dc lambda away | 2.4330 |
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
| P btts yes | 79.4% |
| P btts no | 20.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 93.25 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.03 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.31 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
| Fair Over 4.5 odds | 2.23 |
| Fair Under 4.5 odds | 1.81 |
| Goal margin distribution | {"-1": 0.17946581647417584, "-10": 3.487617709395242e-05, "-11": 7.44733508016899e-06, "-12": 1.465368628722602e-06, "-13": 2.672569257383639e-07, "-14": 4.541234771319518e-08, "-15": 7.220551249063721e-09, "-16": 1.0763062470726781e-09, "-17": 1.476845784939367e-10, "-18": 1.5711547645710467e-11, "-2": 0.13368958602352654, "-3": 0.08123212339086819, "-4": 0.04075514240784106, "-5": 0.017295776088172534, "-6": 0.0063344680687466475, "-7": 0.002035379220337854, "-8": 0.0005816128816352903, "-9": 0.0001494731058216614, "0": 0.22273659421458197, "1": 0.15004665979348944, "10": 5.014081996896663e-06, "11": 8.807826369424546e-07, "12": 1.4256733528410889e-07, "13": 2.1389833474389773e-08, "14": 2.9899070146230717e-09, "15": 3.9107438849828874e-10, "16": 4.7954589045391115e-11, "17": 5.412959190988553e-12, "18": 4.737223383522464e-13, "2": 0.09164690353134174, "3": 0.04580926417396038, "4": 0.01890659048770554, "5": 0.0066004895731926186, "6": 0.0019886187909231965, "7": 0.0005256443691317652, "8": 0.00012356230160721427, "9": 2.6122835985296747e-05} |
| Raw goal margin distribution | {"-1": 0.18884470253640495, "-10": 3.669880659341129e-05, "-11": 7.836532914923207e-06, "-12": 1.5419488136177673e-06, "-13": 2.8122377639040676e-07, "-14": 4.778559763559293e-08, "-15": 7.597897357653704e-09, "-16": 1.1325540264976397e-09, "-17": 1.5540257661778707e-10, "-18": 1.653263334395321e-11, "-2": 0.14067620564644318, "-3": 0.08547731528781932, "-4": 0.04288500671627924, "-5": 0.018199653586827767, "-6": 0.0066655074580230554, "-7": 0.0021417481666698946, "-8": 0.0006120079789098013, "-9": 0.0001572845724085064, "0": 0.1863798272667427, "1": 0.15586182848178487, "10": 5.208406433502112e-06, "11": 9.149180160211448e-07, "12": 1.480926372485705e-07, "13": 2.22188122070008e-08, "14": 3.1057830606228992e-09, "15": 4.0623076413450407e-10, "16": 4.9813104423611705e-11, "17": 5.622742406701453e-12, "18": 4.920817960884166e-13, "2": 0.09519874670151417, "3": 0.04758463590849217, "4": 0.019639329311467748, "5": 0.006856296402523421, "6": 0.0020656891751746577, "7": 0.000546016103369374, "8": 0.00012835104950969283, "9": 2.7135245712246004e-05} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 48.6% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.3% |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8117 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.23, "draw": 3.83, "home": 3.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.14, "draw": 3.94, "home": 3.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.06 |
| Reference draw odds | 3.94 |
| Reference away odds | 2.14 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | +0.5% |
| Draw probability edge | -1.6% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +22.7% |
| Under 2.5 probability edge | -22.7% |
| Raw edge prob home | 0.0175 |
| Raw ev home | 0.0165 |
| Raw edge prob draw | -0.0519 |
| Raw ev draw | -0.2657 |
| Raw edge prob away | 0.0345 |
| Raw ev away | 0.0831 |
| Elo home rating | 1,392.0962 |
| Elo away rating | 1,450.5156 |
| Elo rating diff | 1.5806 |
| Elo home expectancy | 0.5023 |

</details>


---

## 2026-11-05 — Crystal Palace vs TSG Hoffenheim

The model's most likely 1X2 outcome is **Crystal Palace win** at **54.2%**. Expected goals are 2.71 for Crystal Palace and 1.47 for TSG Hoffenheim (4.18 combined). The most likely exact score is 2-2 at 7.9%. Goal-market probabilities: at least one goal: 98.4%; Over 2.5 goals: 77.2%; Under 3.5 goals: 40.8%; Double Chance 1X: 75.6%; Double Chance X2: 45.8%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 61.0%; BTTS Yes (both teams score): 73.2%; BTTS No (at least one team does not score): 26.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 54.2% | 1.85 |
| Draw | 21.4% | 4.66 |
| TSG Hoffenheim win | 24.4% | 4.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 2.71 |
| TSG Hoffenheim expected goals | 1.47 |
| Expected total goals | 4.18 |
| Over 0.5 | 98.4% |
| Under 0.5 | 1.6% |
| Over 1.5 | 91.5% |
| Under 1.5 | 8.5% |
| Over 2.5 | 77.2% |
| Under 2.5 | 22.8% |
| Over 3.5 | 59.2% |
| Under 3.5 | 40.8% |
| Over 4.5 | 39.0% |
| Under 4.5 | 61.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.86% |
| 2 | 1-1 | 7.49% |
| 3 | 2-1 | 6.97% |
| 4 | 3-1 | 6.31% |
| 5 | 1-2 | 5.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 54.2% | 49.9% | 1.96 | +6.2% |
| Draw | 21.4% | 23.6% | 4.06 | -12.9% |
| TSG Hoffenheim win | 24.4% | 26.5% | 3.73 | -9.2% |

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
| Market best home last update utc | 2026-11-03T13:57:16Z |
| Market best draw last update utc | 2026-11-03T13:57:16Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | crystal palace |
| Matched away-team name | hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7140 |
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
| P btts yes | 73.2% |
| P btts no | 26.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 63.21 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.71 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.38 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Goal margin distribution | {"-1": 0.1411271187368119, "-10": 3.566295347697707e-07, "-11": 4.629563796992275e-08, "-12": 5.532938473598577e-09, "-13": 6.124945166576945e-10, "-14": 6.313458783254826e-11, "-15": 6.0876822058627474e-12, "-16": 5.513067667123961e-13, "-17": 4.700943489280132e-14, "-18": 3.73152558178184e-15, "-19": 2.386100625127076e-16, "-2": 0.06645543390451229, "-3": 0.025395586892670245, "-4": 0.007924500943974181, "-5": 0.00207633265829829, "-6": 0.0004671585277982019, "-7": 9.18911013702006e-05, "-8": 1.6033734739198482e-05, "-9": 2.5114147461698713e-06, "0": 0.21447591773028885, "1": 0.17249893497753646, "10": 0.00010997014414463387, "11": 2.6355371592995724e-05, "12": 5.815090725927579e-06, "13": 1.1884322879506603e-06, "14": 2.261575914503599e-07, "15": 4.0259407316803713e-08, "16": 6.731011158447043e-09, "17": 1.0596040299586047e-09, "18": 1.552803772683057e-10, "19": 1.8331182962934296e-11, "2": 0.1518501825323668, "3": 0.10713087635082112, "4": 0.06171630384924752, "5": 0.029853585967904248, "6": 0.012400392590651212, "7": 0.004503147723553842, "8": 0.0014506044818172338, "9": 0.00041947332048465933} |
| Raw goal margin distribution | {"-1": 0.11197126091587979, "-10": 2.8295241230343917e-07, "-11": 3.6731288818165197e-08, "-12": 4.389872782807804e-09, "-13": 4.859575108461091e-10, "-14": 5.0091431542638234e-11, "-15": 4.830010410095719e-12, "-16": 4.374107143458732e-13, "-17": 3.7297620379441094e-14, "-18": 2.9606189672955353e-15, "-19": 1.8931492264495387e-16, "-2": 0.052726214462558825, "-3": 0.020149039472520253, "-4": 0.006287355476169152, "-5": 0.0016473771158330682, "-6": 0.00037064690240520387, "-7": 7.290705414710944e-05, "-8": 1.2721279311929323e-05, "-9": 1.9925743423969168e-06, "0": 0.1653625048210531, "1": 0.20414599220823496, "10": 0.00013014552346431838, "11": 3.11905895799849e-05, "12": 6.881940843170907e-06, "13": 1.4064648493486899e-06, "14": 2.6764899103910813e-07, "15": 4.764549215028287e-08, "16": 7.965898176036942e-09, "17": 1.2540014584548766e-09, "18": 1.8376847771283576e-10, "19": 2.169426457506096e-11, "2": 0.1797089714444237, "3": 0.12678535697408308, "4": 0.07303892100186159, "5": 0.03533059452909263, "6": 0.014675397558366363, "7": 0.005329305715451913, "8": 0.0017167357658228767, "9": 0.0004964308749290267} |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 16.5% |
| Unadjusted away-win probability | 19.3% |
| Raw p over 1 5 | 91.8% |
| Raw p under 3 5 | 39.8% |
| Raw p btts yes | 71.6% |
| Home training matches | 3 |
| Away training matches | 11 |
| P home draw | 75.6% |
| P draw away | 45.8% |
| P home away | 78.6% |
| Raw p home draw | 80.7% |
| Raw p draw away | 35.9% |
| Raw p home away | 83.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7715 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.73, "draw": 4.0, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.62, "draw": 4.06, "home": 1.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.96 |
| Reference draw odds | 4.06 |
| Reference away odds | 3.62 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:38Z |
| Home probability edge | +4.3% |
| Draw probability edge | -2.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +14.1% |
| Under 2.5 probability edge | -14.1% |
| Raw edge prob home | 0.1420 |
| Raw ev home | 0.2571 |
| Raw edge prob draw | -0.0702 |
| Raw ev draw | -0.3286 |
| Raw edge prob away | -0.0719 |
| Raw ev away | -0.2792 |
| Elo home rating | 1,446.0302 |
| Elo away rating | 1,431.4646 |
| Elo rating diff | 74.5656 |
| Elo home expectancy | 0.6057 |

</details>


---

## 2026-11-05 — Hapoel Be'er Sheva vs OFI Crete

The model's most likely 1X2 outcome is **OFI Crete win** at **38.7%**. Expected goals are 0.34 for Hapoel Be'er Sheva and 1.31 for OFI Crete (1.65 combined). The most likely exact score is 1-0 at 24.3%. Goal-market probabilities: at least one goal: 82.2%; Over 2.5 goals: 20.1%; Under 3.5 goals: 93.4%; Double Chance 1X: 61.3%; Double Chance X2: 65.1%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 97.9%; BTTS Yes (both teams score): 20.9%; BTTS No (at least one team does not score): 79.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hapoel Be'er Sheva win | 34.9% | 2.87 |
| Draw | 26.4% | 3.78 |
| OFI Crete win | 38.7% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hapoel Be'er Sheva expected goals | 0.34 |
| OFI Crete expected goals | 1.31 |
| Expected total goals | 1.65 |
| Over 0.5 | 82.2% |
| Under 0.5 | 17.8% |
| Over 1.5 | 42.0% |
| Under 1.5 | 58.0% |
| Over 2.5 | 20.1% |
| Under 2.5 | 79.9% |
| Over 3.5 | 6.6% |
| Under 3.5 | 93.4% |
| Over 4.5 | 2.1% |
| Under 4.5 | 97.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 24.33% |
| 2 | 0-0 | 17.77% |
| 3 | 0-1 | 15.93% |
| 4 | 0-2 | 10.25% |
| 5 | 1-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hapoel Be'er Sheva win | 34.9% | 45.5% | 2.12 | -26.0% |
| Draw | 26.4% | 25.8% | 3.70 | -2.2% |
| OFI Crete win | 38.7% | 28.7% | 3.51 | +35.8% |
| Over 2.5 | 20.1% | 57.0% | 1.71 | -65.6% |
| Under 2.5 | 79.9% | 43.0% | 2.24 | +79.0% |

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
| Market best home last update utc | 2026-11-03T13:57:15Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda away | 1.3085 |
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
| P btts yes | 20.9% |
| P btts no | 79.1% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.63 |
| Fair Over 1.5 odds | 2.38 |
| Fair Under 1.5 odds | 1.72 |
| Fair Over 2.5 odds | 4.97 |
| Fair Under 2.5 odds | 1.25 |
| Fair Over 3.5 odds | 15.19 |
| Fair Under 3.5 odds | 1.07 |
| Fair Over 4.5 odds | 48.31 |
| Fair Under 4.5 odds | 1.02 |
| Goal margin distribution | {"-1": 0.1970314387089289, "-10": 5.053405849879602e-07, "-11": 5.990804780916215e-08, "-12": 6.51357945896604e-09, "-13": 6.536891092837447e-10, "-14": 5.92042445344929e-11, "-2": 0.1186268892437985, "-3": 0.049919951056316574, "-4": 0.015977589283866483, "-5": 0.004120433942256531, "-6": 0.0008891767531811495, "-7": 0.00016489834688072257, "-8": 2.680460812918056e-05, "-9": 3.877767378693941e-06, "0": 0.2643572103927557, "1": 0.2983231698265248, "10": 4.1493653929820885e-12, "11": 1.2841589304111227e-13, "12": 3.644932004024164e-15, "13": 9.549421696938162e-17, "14": 2.257848372031448e-18, "2": 0.04515353835030095, "3": 0.004960425189211647, "4": 0.00041446905732255235, "5": 2.7903579794800692e-05, "6": 1.5719588530955526e-06, "7": 7.610364936453347e-08, "8": 3.2294959950941937e-09, "9": 1.219672263499121e-10} |
| Raw goal margin distribution | {"-1": 0.31606747729636, "-10": 8.106408039204618e-07, "-11": 9.610134131316946e-08, "-12": 1.0448741790928666e-08, "-13": 1.0486137088641927e-09, "-14": 9.497233709437448e-11, "-2": 0.19029502026928538, "-3": 0.08007896151251484, "-4": 0.025630408889666105, "-5": 0.006609783545352039, "-6": 0.001426370609127558, "-7": 0.00026452126041633675, "-8": 4.2998543414298644e-05, "-9": 6.2205105995116e-06, "0": 0.27937324882155606, "1": 0.08568303354170427, "10": 1.1917619886863374e-12, "11": 3.688303284363671e-14, "12": 1.046880908846744e-15, "13": 2.7427417724155605e-17, "14": 6.484890124536746e-19, "2": 0.012968795361236041, "3": 0.001424710920427295, "4": 0.00011904193080684152, "5": 8.014340169695226e-06, "6": 4.5149092245931705e-07, "7": 2.1858146468942612e-08, "8": 9.275612545661949e-10, "9": 3.50308759202483e-11} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 62.0% |
| Raw p over 1 5 | 48.7% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 20.7% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 61.3% |
| P draw away | 65.1% |
| P home away | 73.6% |
| Raw p home draw | 38.0% |
| Raw p draw away | 90.0% |
| Raw p home away | 72.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2010 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.3, "draw": 3.65, "home": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.7, "home": 2.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -10.7% |
| Draw probability edge | +0.6% |
| Away probability edge | +10.0% |
| Over 2.5 probability edge | -36.9% |
| Under 2.5 probability edge | +36.9% |
| Raw edge prob home | -0.3553 |
| Raw ev home | -0.7876 |
| Raw edge prob draw | 0.0215 |
| Raw ev draw | 0.0337 |
| Raw edge prob away | 0.3338 |
| Raw ev away | 1.1777 |
| Elo home rating | 1,422.3390 |
| Elo away rating | 1,425.2946 |
| Elo rating diff | 57.0445 |
| Elo home expectancy | 0.5814 |

</details>


---

## 2026-11-05 — Lillestrom vs Viktoria Plzeň

The model's most likely 1X2 outcome is **Viktoria Plzeň win** at **54.1%**. Expected goals are 0.46 for Lillestrom and 2.49 for Viktoria Plzeň (2.95 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 47.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 45.9%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 37.8%; BTTS No (at least one team does not score): 62.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lillestrom win | 24.9% | 4.02 |
| Draw | 21.0% | 4.76 |
| Viktoria Plzeň win | 54.1% | 1.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lillestrom expected goals | 0.46 |
| Viktoria Plzeň expected goals | 2.49 |
| Expected total goals | 2.95 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 47.5% |
| Under 2.5 | 52.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.68% |
| 2 | 0-2 | 10.68% |
| 3 | 1-1 | 9.53% |
| 4 | 0-3 | 8.85% |
| 5 | 0-1 | 8.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lillestrom win | 24.9% | 33.3% | 2.92 | -27.3% |
| Draw | 21.0% | 24.6% | 3.88 | -18.4% |
| Viktoria Plzeň win | 54.1% | 42.1% | 2.32 | +25.5% |
| Over 2.5 | 47.5% | 60.7% | 1.61 | -23.5% |
| Under 2.5 | 52.5% | 39.3% | 2.44 | +28.1% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
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
| P btts yes | 37.8% |
| P btts no | 62.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.16 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.53 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.1477635200866023, "-10": 9.523594843952077e-05, "-11": 2.133674643048473e-05, "-12": 4.3876976850576e-06, "-13": 8.337427755981736e-07, "-14": 1.4723220701325486e-07, "-15": 2.4283043694350627e-08, "-16": 3.75663632848129e-09, "-17": 5.46261189546097e-10, "-18": 7.09089899437193e-11, "-2": 0.1541133067303308, "-3": 0.11707037489535763, "-4": 0.06893269317298785, "-5": 0.03303715871097479, "-6": 0.0133294594323286, "-7": 0.004639637303106258, "-8": 0.0014192493847434593, "-9": 0.0003870962080900552, "0": 0.21024003499792077, "1": 0.20535820022094978, "10": 3.336045010366923e-11, "11": 1.390433406929849e-12, "12": 5.3192414211763714e-14, "13": 1.880338750347122e-15, "14": 6.177287890315708e-17, "15": 1.895348816418315e-18, "16": 5.454766798930452e-20, "17": 1.4755991210949899e-21, "18": 3.563365314327312e-23, "2": 0.03763076702017886, "3": 0.005317909570593203, "4": 0.0005825191307825112, "5": 5.193721324444828e-05, "6": 3.898338061724892e-06, "7": 2.524306001633503e-07, "8": 1.4365068136341024e-08, "9": 7.288848108073342e-10} |
| Raw goal margin distribution | {"-1": 0.22407454557275774, "-10": 0.0001444196230319171, "-11": 3.235590054710345e-05, "-12": 6.653681262558573e-06, "-13": 1.2643210818017699e-06, "-14": 2.2326884105653208e-07, "-15": 3.682378423135842e-08, "-16": 5.696714437319913e-09, "-17": 8.283724409098865e-10, "-18": 1.0752924462918774e-10, "-2": 0.2337036174562885, "-3": 0.17753022558839374, "-4": 0.10453230871050485, "-5": 0.050098876372450224, "-6": 0.020213328453998796, "-7": 0.007035732633512247, "-8": 0.0021522068556191726, "-9": 0.0005870082606984493, "0": 0.1263804293909941, "1": 0.04413838397641228, "10": 7.170282728994621e-12, "11": 2.98850903166612e-13, "12": 1.1432838818148548e-14, "13": 4.0414803830210847e-16, "14": 1.3277069264448162e-17, "15": 4.073742063297248e-19, "16": 1.172412843577384e-20, "17": 3.171558794928647e-22, "18": 7.658870516141324e-24, "2": 0.00808811745660265, "3": 0.0011429976223308125, "4": 0.00012520295289119614, "5": 1.1163053914485951e-05, "6": 8.378839610648407e-07, "7": 5.425582589552471e-08, "8": 3.087536278400155e-09, "9": 1.5666186020024685e-10} |
| Unadjusted home-win probability | 5.4% |
| Unadjusted draw probability | 12.6% |
| Unadjusted away-win probability | 82.0% |
| Raw p over 1 5 | 79.0% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 33.6% |
| Home training matches | 3 |
| Away training matches | 25 |
| P home draw | 45.9% |
| P draw away | 75.1% |
| P home away | 79.0% |
| Raw p home draw | 18.0% |
| Raw p draw away | 94.6% |
| Raw p home away | 87.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4748 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.32, "draw": 3.88, "home": 2.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.29, "draw": 3.83, "home": 2.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.87 |
| Reference draw odds | 3.83 |
| Reference away odds | 2.29 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -8.4% |
| Draw probability edge | -3.6% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | -0.2792 |
| Raw ev home | -0.8438 |
| Raw edge prob draw | -0.1198 |
| Raw ev draw | -0.5096 |
| Raw edge prob away | 0.3990 |
| Raw ev away | 0.9027 |
| Elo home rating | 1,400.8156 |
| Elo away rating | 1,451.8117 |
| Elo rating diff | 9.0039 |
| Elo home expectancy | 0.5130 |

</details>


---

## 2026-11-05 — NEC Nijmegen vs Omonoia FC

The model's most likely 1X2 outcome is **NEC Nijmegen win** at **50.2%**. Expected goals are 2.30 for NEC Nijmegen and 2.20 for Omonoia FC (4.50 combined). The most likely exact score is 2-2 at 8.3%. Goal-market probabilities: at least one goal: 99.0%; Over 2.5 goals: 82.0%; Under 3.5 goals: 34.1%; Double Chance 1X: 72.3%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 53.9%; BTTS Yes (both teams score): 80.3%; BTTS No (at least one team does not score): 19.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NEC Nijmegen win | 50.2% | 1.99 |
| Draw | 22.1% | 4.53 |
| Omonoia FC win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NEC Nijmegen expected goals | 2.30 |
| Omonoia FC expected goals | 2.20 |
| Expected total goals | 4.50 |
| Over 0.5 | 99.0% |
| Under 0.5 | 1.0% |
| Over 1.5 | 93.7% |
| Under 1.5 | 6.3% |
| Over 2.5 | 82.0% |
| Under 2.5 | 18.0% |
| Over 3.5 | 65.9% |
| Under 3.5 | 34.1% |
| Over 4.5 | 46.1% |
| Under 4.5 | 53.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.34% |
| 2 | 2-1 | 7.67% |
| 3 | 3-2 | 6.46% |
| 4 | 1-1 | 6.27% |
| 5 | 3-1 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NEC Nijmegen win | 50.2% | 53.6% | 1.81 | -9.1% |
| Draw | 22.1% | 23.5% | 4.15 | -8.3% |
| Omonoia FC win | 27.7% | 22.9% | 4.30 | +19.0% |
| Over 2.5 | 82.0% | 60.4% | 1.62 | +32.9% |
| Under 2.5 | 18.0% | 39.6% | 2.42 | -56.5% |

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
| Market best home last update utc | 2026-11-03T13:57:16Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda home | 2.2975 |
| Dc lambda away | 2.2012 |
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
| P btts yes | 80.3% |
| P btts no | 19.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 102.59 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.91 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.57 |
| Fair Over 3.5 odds | 1.52 |
| Fair Under 3.5 odds | 2.93 |
| Fair Over 4.5 odds | 2.17 |
| Fair Under 4.5 odds | 1.86 |
| Goal margin distribution | {"-1": 0.12117000658352907, "-10": 9.161395973093655e-06, "-11": 1.7676084447791498e-06, "-12": 3.1431438875815256e-07, "-13": 5.1813470064559633e-08, "-14": 7.958577435345847e-09, "-15": 1.1439628546378895e-09, "-16": 1.5413122016215927e-10, "-17": 1.9088046208753127e-11, "-18": 1.822257332006241e-12, "-2": 0.08063925175725689, "-3": 0.04397190546456492, "-4": 0.019841342989653156, "-5": 0.007584118547322974, "-6": 0.0025043216649749856, "-7": 0.0007260246196538046, "-8": 0.00018728063632081734, "-9": 4.3465450910840226e-05, "0": 0.22098861055163416, "1": 0.2104009972982805, "10": 2.340514216063691e-05, "11": 4.713409922839105e-06, "12": 8.7480835464746e-07, "13": 1.505188368202332e-07, "14": 2.4131434314038695e-08, "15": 3.620421438631211e-09, "16": 5.091401391006186e-10, "17": 6.581239768658672e-11, "18": 6.557759077656463e-12, "2": 0.1462513878082486, "3": 0.08323927854377108, "4": 0.03920338808037032, "5": 0.015640735264227656, "6": 0.0053906567406565254, "7": 0.001631182039458349, "8": 0.0004391809304568486, "9": 0.0001063884062089648} |
| Raw goal margin distribution | {"-1": 0.17001133610421695, "-10": 1.2854180781873167e-05, "-11": 2.4800978548997597e-06, "-12": 4.410085523327651e-07, "-13": 7.269849628834667e-08, "-14": 1.116652892429522e-08, "-15": 1.6050725658458344e-09, "-16": 2.1625858918376827e-10, "-17": 2.678207529296509e-11, "-18": 2.556774671184998e-12, "-2": 0.11314340339038277, "-3": 0.06169614585211379, "-4": 0.02783901170664379, "-5": 0.010641132766748738, "-6": 0.003513766189355059, "-7": 0.001018671361933207, "-8": 0.0002627699057307648, "-9": 6.098554908165439e-05, "0": 0.18842754518264093, "1": 0.17732749007584153, "10": 1.9726023961426925e-05, "11": 3.972496148061058e-06, "12": 7.372948408941714e-07, "13": 1.2685836989939615e-07, "14": 2.0338148268242497e-08, "15": 3.051317507868518e-09, "16": 4.291070105318144e-10, "17": 5.546716720686818e-11, "18": 5.526927023612496e-12, "2": 0.12326173284900682, "3": 0.07015466908155861, "4": 0.03304090047114072, "5": 0.013182125384197793, "6": 0.004543284689501092, "7": 0.001374772081065156, "8": 0.0003701448809041464, "9": 8.966492216507655e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.3% |
| Raw p btts yes | 79.7% |
| Home training matches | 3 |
| Away training matches | 9 |
| P home draw | 72.3% |
| P draw away | 49.8% |
| P home away | 77.9% |
| Raw p home draw | 61.2% |
| Raw p draw away | 57.7% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8204 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.3, "draw": 4.15, "home": 1.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.07, "draw": 3.97, "home": 1.81}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.81 |
| Reference draw odds | 3.97 |
| Reference away odds | 4.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -3.4% |
| Draw probability edge | -1.4% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +21.7% |
| Under 2.5 probability edge | -21.7% |
| Raw edge prob home | -0.1128 |
| Raw ev home | -0.2337 |
| Raw edge prob draw | -0.0465 |
| Raw ev draw | -0.2180 |
| Raw edge prob away | 0.1593 |
| Raw ev away | 0.6693 |
| Elo home rating | 1,432.8516 |
| Elo away rating | 1,467.0936 |
| Elo rating diff | 25.7579 |
| Elo home expectancy | 0.5370 |

</details>


---

## 2026-11-05 — PFC Levski Sofia vs Jagiellonia Białystok

The model's most likely 1X2 outcome is **PFC Levski Sofia win** at **58.0%**. Expected goals are 2.26 for PFC Levski Sofia and 0.35 for Jagiellonia Białystok (2.61 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 52.6%; Under 3.5 goals: 67.0%; Double Chance 1X: 80.7%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 1.72 |
| Draw | 22.8% | 4.39 |
| Jagiellonia Białystok win | 19.3% | 5.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PFC Levski Sofia expected goals | 2.26 |
| Jagiellonia Białystok expected goals | 0.35 |
| Expected total goals | 2.61 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.1% |
| Under 1.5 | 24.9% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.53% |
| 2 | 2-0 | 10.07% |
| 3 | 3-0 | 9.58% |
| 4 | 0-1 | 9.54% |
| 5 | 0-0 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PFC Levski Sofia win | 58.0% | 47.9% | 2.02 | +17.1% |
| Draw | 22.8% | 26.6% | 3.75 | -14.7% |
| Jagiellonia Białystok win | 19.3% | 25.5% | 3.79 | -27.0% |
| Over 2.5 | 52.6% | 52.6% | 1.83 | -3.7% |
| Under 2.5 | 47.4% | 47.4% | 2.06 | -2.4% |

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
| Market best home last update utc | 2026-11-03T13:57:16Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda home | 2.2599 |
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
| Fair Under 0.5 odds | 12.23 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.01 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.69 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.16079021860084491, "-10": 1.7435898676991016e-11, "-11": 6.977328439044719e-13, "-12": 2.5631435942935324e-14, "-13": 8.701401897261944e-16, "-14": 2.745475441305545e-17, "-15": 8.091065048325777e-19, "-16": 2.2368209247515415e-20, "-17": 5.822781601431783e-22, "-18": 1.4294051070036475e-23, "-19": 3.133924896310533e-25, "-2": 0.02774415928171581, "-3": 0.0037372664014091333, "-4": 0.0003913501786735804, "-5": 3.340964862669724e-05, "-6": 2.4034350295005995e-06, "-7": 1.492547512367643e-07, "-8": 8.149186645839817e-09, "-9": 3.968434884440998e-10, "0": 0.22754498554552433, "1": 0.1273936583516862, "10": 0.0002747133864931782, "11": 7.062469253984302e-05, "12": 1.6667568861289567e-05, "13": 3.635134349362344e-06, "14": 7.368527672680618e-07, "15": 1.3950853101153066e-07, "16": 2.477754121342788e-08, "17": 4.1437105289242545e-09, "18": 6.535008467325959e-10, "19": 9.204735788770224e-11, "2": 0.1506439574021713, "3": 0.1303665344622666, "4": 0.08770200419686447, "5": 0.04810030245414804, "6": 0.02223003789867191, "7": 0.008868862030999044, "8": 0.003110899034261938, "9": 0.0009732464478232596} |
| Raw goal margin distribution | {"-1": 0.040459563176572275, "-10": 6.308702041806043e-13, "-11": 2.005484950681541e-14, "-12": 5.8493395412791e-16, "-13": 1.5759571099315724e-17, "-14": 3.945003428648767e-19, "-15": 9.221121813686232e-21, "-16": 2.0194780825548352e-22, "-17": 3.992160210084807e-24, "-2": 0.005871767064207503, "-3": 0.0006472364371933416, "-4": 5.479765951111098e-05, "-5": 3.7575547991331733e-06, "-6": 2.1626629286939323e-07, "-7": 1.0717692668786735e-08, "-8": 4.66176360305228e-10, "-9": 1.8062679917285835e-11, "0": 0.13860673105764107, "1": 0.2440999408623843, "10": 7.555430069032397e-05, "11": 1.5430162460836453e-05, "12": 2.891277926905049e-06, "13": 5.004484171781703e-07, "14": 8.048116020915127e-08, "15": 1.208544148979893e-08, "16": 1.7003950123891573e-09, "17": 2.1594868182306166e-10, "2": 0.2423442128971905, "3": 0.17161636966565144, "4": 0.09334470318771923, "5": 0.041121117637089984, "6": 0.015204786986152888, "7": 0.00484088450422573, "8": 0.0013527127575684455, "9": 0.00033672041077633167} |
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
| Totals anchor scale | 1.2633 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-03T13:57:16Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4033 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.79, "draw": 3.75, "home": 2.0}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.55, "home": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.02 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:16Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:16Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | +10.1% |
| Draw probability edge | -3.8% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3351 |
| Raw ev home | 0.6450 |
| Raw edge prob draw | -0.1271 |
| Raw ev draw | -0.4802 |
| Raw edge prob away | -0.2081 |
| Raw ev away | -0.8217 |
| Elo home rating | 1,427.6479 |
| Elo away rating | 1,424.2193 |
| Elo rating diff | 63.4285 |
| Elo home expectancy | 0.5903 |

</details>


---

## 2026-11-05 — Real Sociedad vs Lyon

The model's most likely 1X2 outcome is **Real Sociedad win** at **54.5%**. Expected goals are 1.96 for Real Sociedad and 1.16 for Lyon (3.12 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 59.8%; Under 3.5 goals: 62.1%; Double Chance 1X: 76.9%; Double Chance X2: 45.5%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 79.7%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

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
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 59.8% |
| Under 2.5 | 40.2% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.3% |
| Under 4.5 | 79.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.27% |
| 2 | 2-1 | 9.48% |
| 3 | 1-0 | 8.82% |
| 4 | 2-0 | 8.17% |
| 5 | 3-1 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 54.5% | 53.6% | 1.83 | -0.3% |
| Draw | 22.4% | 23.1% | 4.13 | -7.4% |
| Lyon win | 23.1% | 23.3% | 4.21 | -2.7% |

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
| Market best home last update utc | 2026-11-03T13:57:15Z |
| Market best draw last update utc | 2026-11-03T13:57:15Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | real sociedad |
| Matched away-team name | lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9620 |
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
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.76 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.34 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.49 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.94 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.14372109862248442, "-10": 6.70275612810225e-08, "-11": 6.9504795233688706e-09, "-12": 6.623584405933776e-10, "-13": 5.838161594593361e-11, "-14": 4.784158200022749e-12, "-15": 3.635355094478244e-13, "-16": 2.3074833186761596e-14, "-2": 0.06073201589950973, "-3": 0.02004654244042048, "-4": 0.005255816719429995, "-5": 0.001137379490348056, "-6": 0.00020900482046545628, "-7": 3.332254188265962e-05, "-8": 4.687355461174812e-06, "-9": 5.895581067844807e-07, "0": 0.22427836197493695, "1": 0.22662597120543998, "10": 1.2147929028685993e-05, "11": 2.130577156658792e-06, "12": 3.4340707915820793e-07, "13": 5.119481180693516e-08, "14": 7.095598642644624e-09, "15": 9.119352821203724e-10, "16": 9.790151690231484e-11, "2": 0.16436038898399566, "3": 0.0917598324037502, "4": 0.04068993691621357, "5": 0.014893126130519022, "6": 0.004628821656774654, "7": 0.0012482050591552966, "8": 0.0002969678095645123, "9": 6.31744940781574e-05} |
| Raw goal margin distribution | {"-1": 0.14107313875359462, "-10": 6.579262574210136e-08, "-11": 6.822421840649894e-09, "-12": 6.501549535179087e-10, "-13": 5.730597585142085e-11, "-14": 4.696013459678423e-12, "-15": 3.568376241048882e-13, "-16": 2.264969566105727e-14, "-2": 0.05961307134369962, "-3": 0.01967719903572204, "-4": 0.005158982003548458, "-5": 0.001116424075485476, "-6": 0.00020515405406927974, "-7": 3.27085975524228e-05, "-8": 4.60099424301425e-06, "-9": 5.786959145099521e-07, "0": 0.20808450312552246, "1": 0.23513720780227174, "10": 1.2604160490484954e-05, "11": 2.2105937856959353e-06, "12": 3.5630418395248973e-07, "13": 5.311750033862205e-08, "14": 7.362083187741004e-09, "15": 9.4618421178117e-10, "16": 1.0157833721162071e-10, "2": 0.17053315969667776, "3": 0.09520599366902714, "4": 0.04221810104657314, "5": 0.015452457082258866, "6": 0.004802663145796377, "7": 0.0012950830428361808, "8": 0.00030812082647339596, "9": 6.554709534324772e-05} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5979 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.21, "draw": 4.11, "home": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.1, "draw": 4.13, "home": 1.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.13 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:36Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:36Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0292 |
| Raw ev home | 0.0340 |
| Raw edge prob draw | -0.0231 |
| Raw ev draw | -0.1406 |
| Raw edge prob away | -0.0061 |
| Raw ev away | -0.0448 |
| Elo home rating | 1,487.8577 |
| Elo away rating | 1,510.1036 |
| Elo rating diff | 37.7541 |
| Elo home expectancy | 0.5541 |

</details>


---

## 2026-11-05 — SK Sturm Graz vs NK Celje

The model's most likely 1X2 outcome is **SK Sturm Graz win** at **59.1%**. Expected goals are 1.01 for SK Sturm Graz and 0.47 for NK Celje (1.48 combined). The most likely exact score is 1-0 at 28.6%. Goal-market probabilities: at least one goal: 84.1%; Over 2.5 goals: 21.0%; Under 3.5 goals: 93.2%; Double Chance 1X: 83.3%; Double Chance X2: 40.9%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 98.0%; BTTS Yes (both teams score): 21.8%; BTTS No (at least one team does not score): 78.2%.

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
| Over 0.5 | 84.1% |
| Under 0.5 | 15.9% |
| Over 1.5 | 44.8% |
| Under 1.5 | 55.2% |
| Over 2.5 | 21.0% |
| Under 2.5 | 79.0% |
| Over 3.5 | 6.8% |
| Under 3.5 | 93.2% |
| Over 4.5 | 2.0% |
| Under 4.5 | 98.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 28.58% |
| 2 | 0-0 | 15.85% |
| 3 | 2-0 | 14.04% |
| 4 | 0-1 | 10.73% |
| 5 | 1-1 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SK Sturm Graz win | 59.1% | 63.7% | 1.58 | -6.6% |
| Draw | 24.2% | 20.0% | 4.56 | +10.3% |
| NK Celje win | 16.7% | 16.3% | 5.57 | -7.0% |
| Over 2.5 | 21.0% | 60.7% | 1.61 | -66.2% |
| Under 2.5 | 79.0% | 39.3% | 2.44 | +92.8% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | sturm graz |
| Matched away-team name | celje |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0054 |
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
| P btts yes | 21.8% |
| P btts no | 78.2% |
| Fair Over 0.5 odds | 1.19 |
| Fair Under 0.5 odds | 6.31 |
| Fair Over 1.5 odds | 2.23 |
| Fair Under 1.5 odds | 1.81 |
| Fair Over 2.5 odds | 4.76 |
| Fair Under 2.5 odds | 1.27 |
| Fair Over 3.5 odds | 14.68 |
| Fair Under 3.5 odds | 1.07 |
| Fair Over 4.5 odds | 49.09 |
| Fair Under 4.5 odds | 1.02 |
| Goal margin distribution | {"-1": 0.13374444867924787, "-10": 3.610046285143434e-11, "-11": 1.5527935796990587e-12, "-12": 6.122200929102653e-14, "-13": 2.1570530567752073e-15, "-2": 0.02836242621020108, "-3": 0.004321358577401227, "-4": 0.0005012242596829133, "-5": 4.6864192637902846e-05, "-6": 3.6676024222250464e-06, "-7": 2.4670711445078e-07, "-8": 1.4547780208016633e-08, "-9": 7.635309444287233e-10, "0": 0.24193763444956115, "1": 0.35800845234719986, "10": 8.435599419342076e-08, "11": 7.682541505492214e-09, "12": 6.413377116489576e-10, "13": 4.7844061156334756e-11, "2": 0.16407502305375463, "3": 0.05293067227376398, "4": 0.012998917840180374, "5": 0.0025733820402621312, "6": 0.00042641589737624447, "7": 6.0732452704549405e-05, "8": 7.582700249869141e-06, "9": 8.426394944031908e-07} |
| Raw goal margin distribution | {"-1": 0.14143038885607337, "-10": 3.817506109137525e-11, "-11": 1.642028524987502e-12, "-12": 6.474027644575812e-14, "-13": 2.2810131980471135e-15, "-2": 0.02999233992455666, "-3": 0.00456969563988501, "-4": 0.0005300282938924785, "-5": 4.955735399605375e-05, "-6": 3.878369845381473e-06, "-7": 2.6088472063624076e-07, "-8": 1.5383802708304313e-08, "-9": 8.074090509220122e-10, "0": 0.3390376873196701, "1": 0.2933845074512022, "10": 6.912893157894404e-08, "11": 6.295769389758321e-09, "12": 5.255701294435718e-10, "13": 3.920775117120292e-11, "2": 0.13445791435389545, "3": 0.04337618040101202, "4": 0.010652489020682178, "5": 0.00210886200427994, "6": 0.00034944375531046143, "7": 4.976966495122758e-05, "8": 6.213950434333555e-06, "9": 6.905350178287316e-07} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2100 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.53, "draw": 4.55, "home": 1.53}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.57, "draw": 4.56, "home": 1.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.53 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.53 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -4.6% |
| Draw probability edge | +4.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -39.7% |
| Under 2.5 probability edge | +39.7% |
| Raw edge prob home | -0.1524 |
| Raw ev home | -0.2347 |
| Raw edge prob draw | 0.1387 |
| Raw ev draw | 0.5460 |
| Raw edge prob away | 0.0137 |
| Raw ev away | -0.0165 |
| Elo home rating | 1,441.2526 |
| Elo away rating | 1,413.6182 |
| Elo rating diff | 87.6344 |
| Elo home expectancy | 0.6235 |

</details>


---

## 2026-11-05 — Sparta Prague vs Bournemouth

The model's most likely 1X2 outcome is **Bournemouth win** at **74.2%**. Expected goals are 0.26 for Sparta Prague and 3.59 for Bournemouth (3.85 combined). The most likely exact score is 0-3 at 12.9%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 62.4%; Under 3.5 goals: 56.0%; Double Chance 1X: 25.8%; Double Chance X2: 89.3%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 72.7%; BTTS Yes (both teams score): 26.5%; BTTS No (at least one team does not score): 73.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sparta Prague win | 10.7% | 9.32 |
| Draw | 15.1% | 6.62 |
| Bournemouth win | 74.2% | 1.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sparta Prague expected goals | 0.26 |
| Bournemouth expected goals | 3.59 |
| Expected total goals | 3.85 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 80.3% |
| Under 1.5 | 19.7% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 27.3% |
| Under 4.5 | 72.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 12.91% |
| 2 | 0-4 | 11.59% |
| 3 | 0-2 | 10.79% |
| 4 | 0-5 | 8.32% |
| 5 | 0-0 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Prague win | 10.7% | 14.9% | 6.18 | -33.7% |
| Draw | 15.1% | 19.7% | 4.71 | -28.9% |
| Bournemouth win | 74.2% | 65.4% | 1.52 | +12.7% |
| Over 2.5 | 62.4% | 60.5% | 1.62 | +1.1% |
| Under 2.5 | 37.6% | 39.5% | 2.42 | -9.0% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda away | 3.5903 |
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
| P btts yes | 26.5% |
| P btts no | 73.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.34 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.08 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09319569126897789, "-10": 0.0017848142578178292, "-11": 0.0005785267337727204, "-12": 0.00017207758396470084, "-13": 4.72851282679901e-05, "-14": 1.207340909359656e-05, "-15": 2.878775707956259e-06, "-16": 6.43800704686504e-07, "-17": 1.3555898988899873e-07, "-18": 2.696610722079719e-08, "-19": 5.083204736430687e-09, "-2": 0.14513391545007384, "-20": 9.097124245668432e-10, "-21": 1.489868810420903e-10, "-3": 0.1617892869802353, "-4": 0.13899526373439713, "-5": 0.09689097018192301, "-6": 0.056751502154377444, "-7": 0.02864194971079592, "-8": 0.012693151968894202, "-9": 0.005012621216997968, "0": 0.15103604523474778, "1": 0.09670568010521485, "10": 8.216183801665473e-14, "11": 1.9054441025148938e-15, "12": 4.055017577196318e-17, "13": 7.972392532085083e-19, "14": 1.4564302127631337e-20, "15": 2.4846387451597305e-22, "16": 3.975598632649663e-24, "17": 5.989286245443766e-26, "18": 8.5243380380312e-28, "19": 1.1496765407615998e-29, "2": 0.009729280945794224, "20": 1.4721018367722842e-31, "21": 1.724953601691227e-33, "3": 0.0007759920186673614, "4": 4.7698328052134594e-05, "5": 2.3789325011556883e-06, "6": 9.969464640948419e-08, "7": 3.5999188819015014e-09, "8": 1.1414457554090893e-10, "9": 3.2251234771039164e-12} |
| Raw goal margin distribution | {"-1": 0.11879988196246362, "-10": 0.002275166590499455, "-11": 0.0007374687257371806, "-12": 0.0002193534527727377, "-13": 6.027604474335892e-05, "-14": 1.539040652710142e-05, "-15": 3.6696783901151486e-06, "-16": 8.206757917956093e-07, "-17": 1.728018943631628e-07, "-18": 3.43746616522412e-08, "-19": 6.4797429415067484e-09, "-2": 0.18500739454205076, "-20": 1.1596429747638144e-09, "-21": 1.8991890763138342e-10, "-3": 0.20623859251786095, "-4": 0.17718223557492346, "-5": 0.12351038620036064, "-6": 0.07234317021882296, "-7": 0.03651091803157235, "-8": 0.016180414943047852, "-9": 0.00638976760398926, "0": 0.04408387898489363, "1": 0.009413511292883661, "10": 7.997786574401538e-15, "11": 1.8547948328854448e-16, "12": 3.947229750542942e-18, "13": 7.760475604993684e-20, "14": 1.417716336850765e-21, "15": 2.4185937021331333e-23, "16": 3.8699218684676133e-25, "17": 5.830082953395967e-27, "18": 8.297749656282836e-29, "19": 1.1191165904472181e-30, "2": 0.0009470663559288998, "20": 1.4329713879943443e-32, "21": 1.6791020125761033e-34, "3": 7.55365106058427e-05, "4": 4.643044227411681e-06, "5": 2.3156972724117616e-07, "6": 9.704462848455945e-09, "7": 3.5042281912887864e-10, "8": 1.1111045904508516e-11, "9": 3.139395352954535e-13} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6238 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": -1.0, "market_key": "spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.52, "draw": 4.71, "home": 6.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:16Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.49, "draw": 4.61, "home": 6.0}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.00 |
| Reference draw odds | 4.61 |
| Reference away odds | 1.49 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:16Z |
| Market reference home last update utc | 2026-11-03T13:57:16Z |
| Market reference draw last update utc | 2026-11-03T13:57:16Z |
| Market reference away last update utc | 2026-11-03T13:57:16Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -4.1% |
| Draw probability edge | -4.6% |
| Away probability edge | +8.7% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | -0.1383 |
| Raw ev home | -0.9355 |
| Raw edge prob draw | -0.1528 |
| Raw ev draw | -0.7924 |
| Raw edge prob away | 0.2911 |
| Raw ev away | 0.4371 |
| Elo home rating | 1,456.4745 |
| Elo away rating | 1,460.7151 |
| Elo rating diff | 55.7595 |
| Elo home expectancy | 0.5796 |

</details>


---

## 2026-11-05 — Sunderland vs Dinamo Zagreb

The model's most likely 1X2 outcome is **Sunderland win** at **62.8%**. Expected goals are 1.48 for Sunderland and 0.78 for Dinamo Zagreb (2.25 combined). The most likely exact score is 1-0 at 18.6%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 40.8%; Under 3.5 goals: 80.2%; Double Chance 1X: 84.2%; Double Chance X2: 37.2%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

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
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 40.8% |
| Under 2.5 | 59.2% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 18.58% |
| 2 | 2-0 | 13.21% |
| 3 | 2-1 | 10.26% |
| 4 | 1-1 | 9.69% |
| 5 | 0-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 62.8% | 66.3% | 1.47 | -7.7% |
| Draw | 21.4% | 19.7% | 4.82 | +3.1% |
| Dinamo Zagreb win | 15.8% | 13.9% | 6.95 | +10.1% |
| Over 2.5 | 40.8% | 58.0% | 1.68 | -31.4% |
| Under 2.5 | 59.2% | 42.0% | 2.29 | +35.5% |

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
| Market best home last update utc | 2026-11-03T13:56:12Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda home | 1.4768 |
| Dc lambda away | 0.7768 |
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
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.93 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 5.05 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.00 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.1124765674947804, "-10": 2.0036352629459056e-09, "-11": 1.4028926457709672e-10, "-12": 9.015912714178983e-12, "-13": 5.353672683522116e-13, "-14": 2.947126901273966e-14, "-15": 1.4178480326740952e-15, "-2": 0.035618688850955496, "-3": 0.008457128724376844, "-4": 0.0015563789246349174, "-5": 0.00023312762620362034, "-6": 2.939656344183069e-05, "-7": 3.1978335861787284e-06, "-8": 3.057136376971278e-07, "-9": 2.6058941451221472e-08, "0": 0.21395571489597454, "1": 0.3100645375013118, "10": 1.8277014881262907e-06, "11": 2.432834791330206e-07, "12": 2.9723466537553023e-08, "13": 3.3553911558777373e-09, "14": 3.5114925958936855e-10, "15": 3.211620235527513e-11, "2": 0.19043724280505514, "3": 0.08596040986908836, "4": 0.030074087449831702, "5": 0.008563916789401911, "6": 0.002052942759781127, "7": 0.0004245586732942165, "8": 7.716107171876984e-05, "9": 1.2503793387022543e-05} |
| Raw goal margin distribution | {"-1": 0.14425172299998654, "-10": 2.5696715803217467e-09, "-11": 1.7992163687415426e-10, "-12": 1.1562950154023481e-11, "-13": 6.866110214573048e-13, "-14": 3.7797040119321684e-14, "-15": 1.8183967222761374e-15, "-2": 0.045681134766040736, "-3": 0.010846307077966718, "-4": 0.001996063238059533, "-5": 0.0002989872691512357, "-6": 3.770122987580747e-05, "-7": 4.101236505949689e-06, "-8": 3.9207916781822853e-07, "-9": 3.342071408846033e-08, "0": 0.2527328930503438, "1": 0.26880680415254216, "10": 1.584504309739049e-06, "11": 2.1091175100468324e-07, "12": 2.5768409740378166e-08, "13": 2.9089169002094704e-09, "14": 3.044247207739783e-10, "15": 2.784276391685499e-11, "2": 0.1650973279388069, "3": 0.07452236636527493, "4": 0.02607237641666498, "5": 0.007424386941307946, "6": 0.0017797745811628976, "7": 0.00036806614862552206, "8": 6.689388364388454e-05, "9": 1.0840016621168749e-05} |
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
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4084 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:17Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:17Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.95, "draw": 4.82, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:17Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.37, "draw": 4.59, "home": 1.47}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 4.59 |
| Reference away odds | 6.37 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:17Z |
| Market reference home last update utc | 2026-11-03T13:57:17Z |
| Market reference draw last update utc | 2026-11-03T13:57:17Z |
| Market reference away last update utc | 2026-11-03T13:57:17Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | -0.1193 |
| Raw ev home | -0.2001 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.2182 |
| Raw edge prob away | 0.0639 |
| Raw ev away | 0.4117 |
| Elo home rating | 1,448.0520 |
| Elo away rating | 1,437.3148 |
| Elo rating diff | 70.7371 |
| Elo home expectancy | 0.6004 |

</details>


---

## 2026-11-05 — Torreense vs FC Ararat-Armenia

The model's most likely 1X2 outcome is **Torreense win** at **66.0%**. Expected goals are 4.81 for Torreense and 0.93 for FC Ararat-Armenia (5.74 combined). The most likely exact score is 2-0 at 14.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 47.2%; Under 3.5 goals: 74.0%; Double Chance 1X: 83.9%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 33.5%; BTTS No (at least one team does not score): 66.5%.

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
| Torreense expected goals | 4.81 |
| FC Ararat-Armenia expected goals | 0.93 |
| Expected total goals | 5.74 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 70.9% |
| Under 1.5 | 29.1% |
| Over 2.5 | 47.2% |
| Under 2.5 | 52.8% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.13% |
| 2 | 1-0 | 12.63% |
| 3 | 3-0 | 10.77% |
| 4 | 0-1 | 8.66% |
| 5 | 1-1 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torreense win | 66.0% | 54.3% | 1.79 | +18.1% |
| Draw | 18.0% | 23.8% | 4.00 | -28.1% |
| FC Ararat-Armenia win | 16.1% | 21.9% | 4.67 | -25.0% |
| Over 2.5 | 47.2% | 47.2% | 2.04 | -3.7% |
| Under 2.5 | 52.8% | 52.8% | 1.85 | -2.4% |

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
| Market best home last update utc | 2026-11-03T13:57:15Z |
| Market best draw last update utc | 2026-11-03T13:56:12Z |
| Market best away last update utc | 2026-11-03T13:56:12Z |
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
| Dc lambda home | 4.8063 |
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
| Fair Under 0.5 odds | 12.87 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.44 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.84 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.07 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.13315974183853901, "-10": 1.5221733198044017e-11, "-11": 6.074781027111051e-13, "-12": 2.2249032189405094e-14, "-13": 7.528793455315882e-16, "-14": 2.3674036203833255e-17, "-15": 6.952069510775353e-19, "-16": 1.9148214214889796e-20, "-17": 4.958961411662939e-22, "-18": 1.1538020095038395e-23, "-2": 0.023775651656339398, "-3": 0.00324490638033511, "-4": 0.00034208860277669303, "-5": 2.92987995686557e-05, "-6": 2.1100687124650367e-06, "-7": 1.3100377278692012e-07, "-8": 7.1442247170956286e-09, "-9": 3.472610429092353e-10, "0": 0.17974240750783743, "1": 0.20031592466790685, "10": 6.371841905318479e-05, "11": 1.3143539665619912e-05, "12": 2.4881334082293863e-06, "13": 4.351798188255967e-07, "14": 7.072883383011582e-08, "15": 1.07354220249704e-08, "16": 1.52831937695845e-09, "17": 2.0457727846483877e-10, "18": 2.4602474193617883e-11, "2": 0.1953829703733705, "3": 0.13782794343573554, "4": 0.07510252452468551, "5": 0.03324654985830713, "6": 0.012375825592859872, "7": 0.003971387015529187, "8": 0.0011194232967683326, "9": 0.0002812393759166439} |
| Raw goal margin distribution | {"-1": 0.0177681322802716, "-10": 6.410770895516247e-10, "-11": 5.246509009736064e-11, "-12": 3.95487383703289e-12, "-13": 2.762441318804717e-13, "-14": 1.7972506555977792e-14, "-15": 1.0941010473009968e-15, "-16": 6.2572829404891e-17, "-17": 3.37400645266363e-18, "-18": 1.7207815294419812e-19, "-19": 8.324789188109267e-21, "-2": 0.005054448750797172, "-20": 3.8301535312947595e-22, "-21": 1.679878178225149e-23, "-22": 7.038439148676283e-25, "-23": 2.8206989841969513e-26, "-24": 1.07098789523394e-27, "-25": 3.379419243342475e-29, "-3": 0.0011948431139217972, "-4": 0.00023209242133219335, "-5": 3.801081611432672e-05, "-6": 5.360466236932782e-06, "-7": 6.621912564183709e-07, "-8": 7.26648886419386e-08, "-9": 7.165374782393721e-09, "0": 0.04301504920821083, "1": 0.08883175472959223, "10": 0.008724057435599288, "11": 0.0036902816059323326, "12": 0.0014378134610602339, "13": 0.0005190913580268073, "14": 0.00017455818357224815, "15": 5.492496932721433e-05, "16": 1.62359987242796e-05, "17": 4.5250142378882095e-06, "18": 1.192835629789412e-06, "19": 2.9826956280232976e-07, "2": 0.13503161108017186, "20": 7.093044786351219e-08, "21": 1.607959602749827e-08, "22": 3.482206575186763e-09, "23": 7.212996792700258e-10, "24": 1.4155472981629817e-10, "25": 2.308674582561932e-11, "3": 0.16498838174456887, "4": 0.1656472625404113, "5": 0.14022043950620625, "6": 0.10220861908026542, "7": 0.06526032371290033, "8": 0.037014443131575, "9": 0.018865414188247245} |
| Unadjusted home-win probability | 93.3% |
| Unadjusted draw probability | 4.3% |
| Unadjusted away-win probability | 2.4% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.6% |
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
| Totals anchor scale | 0.4757 |
| Totals anchor target over 2 5 | 0.4722 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.82 |
| Totals anchor reference last update utc | 2026-11-03T13:57:15Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.8606 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.43, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.35, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.67, "draw": 4.0, "home": 1.76}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:56:12Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.85}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.25, "draw": 3.92, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:57:15Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.92 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-11-03T13:57:15Z |
| Market reference home last update utc | 2026-11-03T13:57:15Z |
| Market reference draw last update utc | 2026-11-03T13:57:15Z |
| Market reference away last update utc | 2026-11-03T13:57:15Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:57:15Z |
| Market best over 2 5 last update utc | 2026-11-03T13:56:12Z |
| Market best under 2 5 last update utc | 2026-11-03T13:56:12Z |
| Home probability edge | +11.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3900 |
| Raw ev home | 0.6695 |
| Raw edge prob draw | -0.1953 |
| Raw ev draw | -0.8279 |
| Raw edge prob away | -0.1947 |
| Raw ev away | -0.8865 |
| Elo home rating | 1,421.4152 |
| Elo away rating | 1,403.0006 |
| Elo rating diff | 78.4146 |
| Elo home expectancy | 0.6110 |

</details>


---
