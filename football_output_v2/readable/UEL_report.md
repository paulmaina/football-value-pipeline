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
| Training as of utc | 2026-11-03T13:22:43.859506+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-03', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 795.121 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 0.7117 |
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
| Goal margin distribution | {"-1": 0.18226428654224827, "-10": 2.0314967984245822e-08, "-11": 1.784451624844948e-09, "-12": 1.4400302830685693e-10, "-13": 1.074582241050925e-11, "-14": 7.456464610504634e-13, "-15": 4.833541472998317e-14, "-16": 2.92425268226702e-15, "-17": 1.5107583473910215e-16, "-2": 0.06661959997545165, "-3": 0.018919275410597215, "-4": 0.004242774669205931, "-5": 0.0007826510154436154, "-6": 0.00012232990540949866, "-7": 1.6565434274451413e-05, "-8": 1.977178387204986e-06, "-9": 2.1085494098535492e-07, "0": 0.2609552762445306, "1": 0.18355955168668836, "10": 1.3893985794807728e-05, "11": 2.512770255499596e-06, "12": 4.1750042685611524e-07, "13": 6.414491778679661e-08, "14": 9.164163945152947e-09, "15": 1.2231018795416344e-09, "16": 1.523524267834812e-10, "17": 1.62056620203966e-11, "2": 0.14109589130608508, "3": 0.08250003661087463, "4": 0.03809227442611611, "5": 0.014467463167527816, "6": 0.004655798407557522, "7": 0.0012980805672306742, "8": 0.0003189936018624243, "9": 7.004178338354915e-05} |
| Raw goal margin distribution | {"-1": 0.13665951971385337, "-10": 1.1453788020930956e-09, "-11": 7.353308597473797e-11, "-12": 4.3325683216906505e-12, "-13": 2.358478234064668e-13, "-14": 1.190606039463438e-14, "-15": 5.282075868913476e-16, "-2": 0.04009245810648914, "-3": 0.008784925989942481, "-4": 0.0014880917105070007, "-5": 0.0002048739736545998, "-6": 2.372433766299045e-05, "-7": 2.3687315747088826e-06, "-8": 2.0776487548602677e-07, "-9": 1.6244034755118676e-08, "0": 0.25442412353215227, "1": 0.275109449160197, "10": 1.567913477147605e-06, "11": 2.0724928435665882e-07, "12": 2.5141602880288956e-08, "13": 2.8178424676728087e-09, "14": 2.928803358749609e-10, "15": 2.6752480907291544e-11, "2": 0.16995630260606326, "3": 0.07667433052005013, "4": 0.026741075994208593, "5": 0.007580070883853751, "6": 0.0018072484784300055, "7": 0.0003715154810249431, "8": 6.709196157800063e-05, "9": 1.0800144515110916e-05} |
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
| Totals anchor scale | 1.3777 |
| Totals anchor target over 2 5 | 0.5459 |
| Totals anchor reference over odds | 1.76 |
| Totals anchor reference under odds | 2.09 |
| Totals anchor reference last update utc | 2026-11-03T13:22:36Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3613 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.33, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.86, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.86, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.67, "home": 2.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.79, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.31, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:35Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.66, "home_away": 1.31, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.07, "draw": 3.58, "home": 2.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.76, "under": 2.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.58 |
| Reference away odds | 3.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:34Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:34Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
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
| Market best home draw last update utc | 2026-11-03T13:22:35Z |
| Market reference home draw last update utc | 2026-11-03T13:22:35Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.8% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-03T13:21:30Z |
| Market reference draw away last update utc | 2026-11-03T13:22:35Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-03T13:22:35Z |
| Market reference home away last update utc | 2026-11-03T13:22:35Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home draw odds | 1.39 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 79.4% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-03T13:22:36Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.15 |
| Market reference over 1 5 last update utc | 2026-11-03T13:22:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.9% |
| Market under 3 5 odds | 1.43 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-03T13:22:36Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-11-03T13:22:36Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,490.6687 |
| Elo away rating | 1,481.7280 |
| Elo rating diff | 68.9408 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-05 — AC Milan vs Ferencváros TC

The model's most likely 1X2 outcome is **AC Milan win** at **76.5%**. Expected goals are 2.92 for AC Milan and 1.00 for Ferencváros TC (3.92 combined). The most likely exact score is 2-0 at 8.4%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 74.7%; Under 3.5 goals: 44.8%; Double Chance 1X: 90.7%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 64.6%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 76.5% | 1.31 |
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
| AC Milan win | 76.5% | 76.3% | 1.31 | +0.1% |
| Draw | 14.2% | 14.7% | 5.67 | -19.3% |
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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | milan |
| Matched away-team name | ferencvaros |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9241 |
| Dc lambda away | 0.9997 |
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
| Goal margin distribution | {"-1": 0.06381546556113475, "-10": 6.4786162203572265e-09, "-11": 5.762644377656232e-10, "-12": 4.713863632311729e-11, "-13": 3.5684644289525077e-12, "-14": 2.5135946673559746e-13, "-15": 1.6552968804907947e-14, "-16": 1.02336633996834e-15, "-17": 5.961486374590928e-17, "-18": 3.2816728909828855e-18, "-19": 1.6986332334754786e-19, "-2": 0.021822253117870255, "-20": 7.407940789539675e-21, "-3": 0.0059859859944919195, "-4": 0.001319368165279354, "-5": 0.00024170867076111254, "-6": 3.777001339521525e-05, "-7": 5.13619546330196e-06, "-8": 6.175360041257865e-07, "-9": 6.649040468922083e-08, "0": 0.14226989688859742, "1": 0.19710972467083882, "10": 0.00032239821631125157, "11": 8.38791504490569e-05, "12": 2.006924551291576e-05, "13": 4.443827893172392e-06, "14": 9.15572906018274e-07, "15": 1.763580995049284e-07, "16": 3.18913180810937e-08, "17": 5.4339761006284305e-09, "18": 8.749440562738194e-10, "19": 1.3246661537523425e-10, "2": 0.20269141095837012, "20": 1.6897643878747663e-11, "3": 0.16262723598615708, "4": 0.10484444201612486, "5": 0.056181517976734235, "6": 0.025678532788290877, "7": 0.010213778539146293, "8": 0.003591939431271745, "9": 0.0011312211730325034} |
| Raw goal margin distribution | {"-1": 0.0695819476866654, "-10": 7.064035825218893e-09, "-11": 6.283367457983994e-10, "-12": 5.139816967273674e-11, "-13": 3.890917398059713e-12, "-14": 2.7407276764578456e-13, "-15": 1.8048725325661136e-14, "-16": 1.1158395932057363e-15, "-17": 6.500177181253466e-17, "-18": 3.5782108524518415e-18, "-19": 1.852124837627218e-19, "-2": 0.02379415180162197, "-20": 8.077335861318108e-21, "-3": 0.0065268906315950745, "-4": 0.001438588684555971, "-5": 0.0002635499081049735, "-6": 4.1182980850822234e-05, "-7": 5.600311474553007e-06, "-8": 6.733376863410725e-07, "-9": 7.249859920426955e-08, "0": 0.1305316025162431, "1": 0.1979641676518642, "10": 0.00032379576731226005, "11": 8.424275478910279e-05, "12": 2.015624287436823e-05, "13": 4.4630912631484136e-06, "14": 9.195417860137729e-07, "15": 1.7712258710451587e-07, "16": 3.2029562467237226e-08, "17": 5.4575316240608505e-09, "18": 8.787368159102174e-10, "19": 1.33040839553755e-10, "2": 0.20357004976574877, "20": 1.6970892792428476e-11, "3": 0.16333220222028874, "4": 0.1052989279514576, "5": 0.05642505696893128, "6": 0.02578984562250353, "7": 0.010258053835035903, "8": 0.003607509984375828, "9": 0.0011361248579871603} |
| Unadjusted home-win probability | 76.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 10.2% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 59.5% |
| Home training matches | 9 |
| Away training matches | 33 |
| P home draw | 90.7% |
| P draw away | 23.5% |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.75, "market_key": "spreads", "opposite_price": 1.95, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.76, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 11.1, "draw": 5.67, "home": 1.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.86, "draw": 5.14, "home": 1.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 5.14 |
| Reference away odds | 7.86 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:37Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:37Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +11.7% |
| Under 2.5 probability edge | -11.7% |
| Raw edge prob home | 0.0047 |
| Raw ev home | 0.0058 |
| Raw edge prob draw | -0.0168 |
| Raw ev draw | -0.2599 |
| Raw edge prob away | 0.0120 |
| Raw ev away | 0.1283 |
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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 2.0097 |
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
| Goal margin distribution | {"-1": 0.20885885839412163, "-10": 1.7136688878700787e-05, "-11": 3.094088051991242e-06, "-12": 5.130158301560401e-07, "-13": 7.862900069977641e-08, "-14": 1.1203226303776851e-08, "-15": 1.4910461706652383e-09, "-16": 1.855116624450119e-10, "-17": 2.0057717911503508e-11, "-2": 0.16661459601357648, "-3": 0.09938953468025842, "-4": 0.04642962207819967, "-5": 0.0177558421154107, "-6": 0.005736421501212141, "-7": 0.0016024855473625815, "-8": 0.00039403119624047595, "-9": 8.648454758321908e-05, "0": 0.2309683695332162, "1": 0.15964573942194735, "10": 2.8540586311295965e-09, "11": 2.0258351199269597e-10, "12": 1.3204976781559153e-11, "13": 7.95655520306542e-13, "14": 4.45677676513863e-14, "15": 2.3318698797580207e-15, "16": 1.1405645967112906e-16, "17": 4.848033780102622e-18, "2": 0.04863684945839345, "3": 0.011405872075085127, "4": 0.002094683617897396, "5": 0.00031491983169074355, "6": 3.999772033613116e-05, "7": 4.392621211365718e-06, "8": 4.246153487029917e-07, "9": 3.663861497184423e-08} |
| Raw goal margin distribution | {"-1": 0.25347334180389286, "-10": 2.0797268695882853e-05, "-11": 3.7550183143e-06, "-12": 6.226014920687208e-07, "-13": 9.542499524948996e-08, "-14": 1.3596355127274397e-08, "-15": 1.80954956169124e-09, "-16": 2.2513893537999129e-10, "-17": 2.434226073569157e-11, "-2": 0.20220525367984787, "-3": 0.12062020107473716, "-4": 0.05634748536566887, "-5": 0.021548679678420203, "-6": 0.006961782416545416, "-7": 0.0019447935797673888, "-8": 0.0004782004692259199, "-9": 0.00010495857086870541, "0": 0.19355505278602314, "1": 0.10257823684492168, "10": 1.8338372404635357e-09, "11": 1.3016732892031043e-10, "12": 8.484681399798442e-12, "13": 5.112378238498328e-13, "14": 2.863642363615028e-14, "15": 1.4983118352137696e-15, "16": 7.328545425766563e-17, "17": 3.115039331010049e-18, "2": 0.0312509577843955, "3": 0.007328690708423096, "4": 0.0013459109716918464, "5": 0.00020234753022099734, "6": 2.5700000793961394e-05, "7": 2.822420069718156e-06, "8": 2.72830919039588e-07, "9": 2.35416525230178e-08} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.95, "draw": 3.8, "home": 3.67}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.96, "draw": 3.83, "home": 3.85}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.09}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.67 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.95 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -3.4% |
| Draw probability edge | -1.6% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | -0.1134 |
| Raw ev home | -0.4505 |
| Raw edge prob draw | -0.0534 |
| Raw ev draw | -0.2587 |
| Raw edge prob away | 0.1669 |
| Raw ev away | 0.3009 |
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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Goal margin distribution | {"-1": 0.15358115693508204, "-10": 1.3055793984353982e-07, "-11": 1.44734463107499e-08, "-12": 1.474565043426647e-09, "-13": 1.3895223678201414e-10, "-14": 1.2173479489644118e-11, "-15": 9.888768840627656e-13, "-16": 6.705944488236148e-14, "-2": 0.06945794480282844, "-3": 0.02449329829829534, "-4": 0.006862217227333616, "-5": 0.0015871323257601838, "-6": 0.00031173819467366596, "-7": 5.31283326458008e-05, "-8": 7.988957519474481e-06, "-9": 1.0741806488342115e-06, "0": 0.23621338026699992, "1": 0.22473192440889134, "10": 6.9259349353761345e-06, "11": 1.1428177518397612e-06, "12": 1.733001194478022e-07, "13": 2.4306944795599495e-08, "14": 3.1696365435561716e-09, "15": 3.8323650107746094e-10, "16": 3.868249695404205e-11, "2": 0.15295293374793095, "3": 0.08028105275556664, "4": 0.033478049988866124, "5": 0.011524941601686819, "6": 0.003369345267438849, "7": 0.0008546958431100283, "8": 0.0001912957941412415, "9": 3.828446114093477e-05} |
| Raw goal margin distribution | {"-1": 0.1567637434593004, "-10": 1.3326342760172488e-07, "-11": 1.477337239612938e-08, "-12": 1.505121727136725e-09, "-13": 1.4183167541314366e-10, "-14": 1.242574449760318e-11, "-15": 1.0093688917291716e-12, "-16": 6.844908466541364e-14, "-2": 0.07089728751609387, "-3": 0.025000860831704084, "-4": 0.007004419568491929, "-5": 0.0016200216857110978, "-6": 0.00031819819144183683, "-7": 5.4229284864855824e-05, "-8": 8.154508743670428e-06, "-9": 1.09644036432132e-06, "0": 0.2172470011499733, "1": 0.230779053567862, "10": 7.112299303549497e-06, "11": 1.1735689082173732e-06, "12": 1.779633118639325e-07, "13": 2.496100066694745e-08, "14": 3.2549257236150026e-09, "15": 3.9354870138697654e-10, "16": 3.972337290385582e-11, "2": 0.15706862023995932, "3": 0.0824412705186102, "4": 0.034378883694649774, "5": 0.011835056911731468, "6": 0.0034600082476405314, "7": 0.0008776941606321882, "8": 0.0001964432175782215, "9": 3.931462666774973e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.81, "draw": 4.0, "home": 1.93}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.64, "under": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.83, "home": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.83 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.37 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.8% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0195 |
| Raw ev home | 0.0057 |
| Raw edge prob draw | -0.0271 |
| Raw ev draw | -0.1310 |
| Raw edge prob away | 0.0076 |
| Raw ev away | -0.0030 |
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
| Marseille win | 10.1% | 9.86 |

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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:22:36Z |
| Market best away last update utc | 2026-11-03T13:22:36Z |
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
| Goal margin distribution | {"-1": 0.08130897342536089, "-10": 5.677179406204623e-11, "-11": 2.816406538091557e-12, "-12": 1.2830625958388001e-13, "-13": 5.403214838746918e-15, "-14": 2.1152647065076568e-16, "-15": 7.735981208917523e-18, "-16": 2.6544088181910816e-19, "-17": 8.576903256177695e-21, "-18": 2.6111245995759864e-22, "-19": 7.005017877056527e-24, "-2": 0.016979196702989308, "-3": 0.00278377917924268, "-4": 0.00035737770888447573, "-5": 3.75562587131076e-05, "-6": 3.334054488130033e-06, "-7": 2.5592013090790235e-07, "-8": 1.72906542341851e-08, "-9": 1.042759016543374e-09, "0": 0.1483161018097476, "1": 0.17117345499679615, "10": 0.000345025528339352, "11": 8.883796746032751e-05, "12": 2.100563299522187e-05, "13": 4.5911853273262e-06, "14": 9.328718109719556e-07, "15": 1.7707502506097933e-07, "16": 3.153511188678205e-08, "17": 5.288612354356721e-09, "18": 8.356481942063448e-10, "19": 1.1635626971094209e-10, "2": 0.19595596071426447, "3": 0.16674805631435047, "4": 0.1111061547060444, "5": 0.060600699629591984, "6": 0.027922395106257363, "7": 0.01112420755098505, "8": 0.003900863189736679, "9": 0.0012210063025941316} |
| Raw goal margin distribution | {"-1": 0.03932679060774406, "-10": 2.7458869094609404e-11, "-11": 1.3622141016388852e-12, "-12": 6.205801391589402e-14, "-13": 2.6133781994814602e-15, "-14": 1.0230921470081097e-16, "-15": 3.741669588631777e-18, "-16": 1.2838605061983254e-19, "-17": 4.1483991767306124e-21, "-18": 1.2629251858962157e-22, "-19": 3.3881238398292205e-24, "-2": 0.00821234465638803, "-3": 0.0013464331951106362, "-4": 0.00017285322558003633, "-5": 1.8164872340645843e-05, "-6": 1.6125853913265927e-06, "-7": 1.2378113972574547e-07, "-8": 8.362987624765756e-09, "-9": 5.043522722074803e-10, "0": 0.10396180922233064, "1": 0.19324773995791686, "10": 0.0003895195290684173, "11": 0.00010029438521577181, "12": 2.3714489508832147e-05, "13": 5.183258048102981e-06, "14": 1.0531736310641955e-06, "15": 1.9991036809221513e-07, "16": 3.560183500154702e-08, "17": 5.970624271222914e-09, "18": 9.434121951520644e-10, "19": 1.3136140853144688e-10, "2": 0.2212261623160129, "3": 0.18825164816429513, "4": 0.12543424617303905, "5": 0.06841567954275628, "6": 0.03152322741044882, "7": 0.01255876951301176, "8": 0.00440391295084716, "9": 0.0013784655363479387} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.2, "draw": 5.32, "home": 1.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 7.37, "draw": 5.53, "home": 1.39}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.39 |
| Reference draw odds | 5.53 |
| Reference away odds | 7.37 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:38Z |
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
| Benfica win | 89.9% | 86.0% | 1.21 | +8.7% |
| Draw | 6.9% | 9.4% | 7.60 | -47.5% |
| Lech Poznań win | 3.2% | 4.5% | 13.10 | -57.7% |

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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | benfica |
| Matched away-team name | lech poznan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.1579 |
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
| Goal margin distribution | {"-1": 0.029969580601393358, "-10": 2.0175818955334475e-15, "-11": 3.555156035037286e-17, "-12": 5.749077934745772e-19, "-13": 8.589540981783531e-21, "-14": 1.1925405479195337e-22, "-15": 1.5462168856020246e-24, "-16": 1.880403799720103e-26, "-17": 2.1531778732192393e-28, "-18": 2.329347739530744e-30, "-19": 2.3880014722633714e-32, "-2": 0.0021804056578410102, "-20": 2.326308682458342e-34, "-21": 2.158762614426504e-36, "-22": 1.9125857439547585e-38, "-23": 1.621076125623854e-40, "-24": 1.3169266659330967e-42, "-25": 1.0264770543115649e-44, "-26": 7.422809288490225e-47, "-3": 0.0001314245302041334, "-4": 6.1184049263954475e-06, "-5": 2.3139330251291574e-07, "-6": 7.358418496429634e-09, "-7": 2.0172016520778853e-10, "-8": 4.857266240575554e-12, "-9": 1.0424606137381809e-13, "0": 0.06904617463164811, "1": 0.03565614689299764, "10": 0.01732479677183179, "11": 0.008062504373557055, "12": 0.003443370961303217, "13": 0.0013587197640717817, "14": 0.00049820423066146, "15": 0.00017059998487813536, "16": 5.479412759602636e-05, "17": 1.6570557681060046e-05, "18": 4.734409989386881e-06, "19": 1.2818595604061138e-06, "2": 0.07910058893633905, "20": 3.29797620739828e-07, "21": 8.08275444158617e-08, "22": 1.8912534395878962e-08, "23": 4.2335680632024135e-09, "24": 9.083203582488783e-10, "25": 1.8698252588302002e-10, "26": 3.571037403463758e-11, "3": 0.12591955202485702, "4": 0.15482078766871596, "5": 0.15463797759055647, "6": 0.12987458731943827, "7": 0.09402932789416235, "8": 0.05979711698282299, "9": 0.03389395996228126} |
| Raw goal margin distribution | {"-1": 0.0017133229799094446, "-10": 1.153426026023867e-16, "-11": 2.0324376950773673e-18, "-12": 3.2866750689304973e-20, "-13": 4.910531831159308e-22, "-14": 6.817603330522897e-24, "-15": 8.839526175761018e-26, "-16": 1.0750030453945369e-27, "-17": 1.2309445297501272e-29, "-18": 1.3316586119168431e-31, "-19": 1.3651902083328459e-33, "-2": 0.0001246510309500257, "-20": 1.3299212214646188e-35, "-21": 1.2341372555925465e-37, "-22": 1.0934010554730748e-39, "-23": 9.267486973390577e-42, "-24": 7.528703019266814e-44, "-25": 5.8682393620816756e-46, "-26": 4.2435260935430985e-48, "-3": 7.5133740013724395e-06, "-4": 3.4978146341818023e-07, "-5": 1.3228462148518834e-08, "-6": 4.206714692943501e-10, "-7": 1.1532086456544054e-11, "-8": 2.77683761418054e-13, "-9": 5.959615347720581e-15, "0": 0.010367535532783646, "1": 0.039192160772166966, "10": 0.01904289385121688, "11": 0.008862061528493502, "12": 0.0037848494599989906, "13": 0.001493463766503604, "14": 0.0005476110574721766, "15": 0.00018751835567477445, "16": 6.022805168933815e-05, "17": 1.8213857001136357e-05, "18": 5.203920603710652e-06, "19": 1.408981349822795e-06, "2": 0.08694498056869157, "20": 3.6250359336644613e-07, "21": 8.884319792243257e-08, "22": 2.0788087138994585e-08, "23": 4.653410270909709e-09, "24": 9.983983300257687e-10, "25": 2.055255504186953e-10, "26": 3.925176561000168e-11, "3": 0.13840697207489389, "4": 0.17017433822546496, "5": 0.16997339890368404, "6": 0.14275422753101455, "7": 0.10335419996967025, "8": 0.06572718666253642, "9": 0.03725521807035162} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 2.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 2.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -2.5, "market_key": "spreads", "opposite_price": 1.77, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.38, "draw": 6.83, "home": 1.13}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.1, "draw": 7.6, "home": 1.21}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.13 |
| Reference draw odds | 6.83 |
| Reference away odds | 12.38 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:38Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:38Z |
| Home probability edge | +3.8% |
| Draw probability edge | -2.5% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | +8.3% |
| Under 2.5 probability edge | -8.3% |
| Raw edge prob home | 0.1273 |
| Raw ev home | 0.1952 |
| Raw edge prob draw | -0.0838 |
| Raw ev draw | -0.9212 |
| Raw edge prob away | -0.0435 |
| Raw ev away | -0.9758 |
| Elo home rating | 1,490.8432 |
| Elo away rating | 1,407.9321 |
| Elo rating diff | 142.9112 |
| Elo home expectancy | 0.6948 |

</details>


---

## 2026-11-05 — Celta Vigo vs Union Saint-Gilloise

The model's most likely 1X2 outcome is **Celta Vigo win** at **39.1%**. Expected goals are 1.05 for Celta Vigo and 1.34 for Union Saint-Gilloise (2.39 combined). The most likely exact score is 1-0 at 13.4%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 42.5%; Under 3.5 goals: 78.4%; Double Chance 1X: 64.9%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 47.3%; BTTS No (at least one team does not score): 52.7%.

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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 1.3406 |
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
| P btts yes | 47.3% |
| P btts no | 52.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.85 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.11 |
| Fair Over 2.5 odds | 2.35 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.63 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.71 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.1902044741060216, "-10": 4.2881841169261916e-07, "-11": 5.1713416014021196e-08, "-12": 5.724984203054603e-09, "-13": 5.833849916390919e-10, "-14": 5.07642319432414e-11, "-2": 0.10242261266735196, "-3": 0.04124096140670541, "-4": 0.012950696819208903, "-5": 0.0033215087024569957, "-6": 0.0007186361823796004, "-7": 0.0001343163715868789, "-8": 2.2082705379318747e-05, "-9": 3.2392665056034453e-06, "0": 0.2580338942468781, "1": 0.24590015002365856, "10": 6.032598406739063e-08, "11": 5.6906478117678996e-09, "12": 4.92788160150993e-10, "13": 3.9279749977597975e-11, "14": 2.6736144075639145e-12, "2": 0.10280326718381298, "3": 0.03237929128354209, "4": 0.007953516469526004, "5": 0.0015956180237314446, "6": 0.0002700412494630657, "7": 3.948002972482718e-05, "8": 5.077246962548377e-06, "9": 5.825727694978838e-07} |
| Raw goal margin distribution | {"-1": 0.23858141307779396, "-10": 5.378848373375953e-07, "-11": 6.48662967876758e-08, "-12": 7.181086709093208e-09, "-13": 7.31764151857168e-10, "-14": 6.367569557841431e-11, "-2": 0.12847295930418268, "-3": 0.0517302597393898, "-4": 0.016244599723488486, "-5": 0.004166307041445626, "-6": 0.0009014153672609553, "-7": 0.00016847863270985546, "-8": 2.7699259329944827e-05, "-9": 4.06314722024707e-06, "0": 0.2607664980123334, "1": 0.18802629370241025, "10": 4.6127955582990864e-08, "11": 4.351324782475745e-09, "12": 3.7680794958728675e-10, "13": 3.003506018656146e-11, "14": 2.0443656004083013e-12, "2": 0.07860799315173748, "3": 0.024758659692437852, "4": 0.006081615743309512, "5": 0.001220081171719995, "6": 0.00020648566208041378, "7": 3.01882030722878e-05, "8": 3.882290956259855e-06, "9": 4.4546129252095485e-07} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.64, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.37, "price": 1.64, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.21, "draw": 3.77, "home": 2.2}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.04, "draw": 3.67, "home": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.24 |
| Reference draw odds | 3.67 |
| Reference away odds | 3.04 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -3.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | -0.1314 |
| Raw ev home | -0.3304 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0169 |
| Raw edge prob away | 0.1275 |
| Raw ev away | 0.4134 |
| Elo home rating | 1,446.1006 |
| Elo away rating | 1,494.2964 |
| Elo rating diff | 11.8042 |
| Elo home expectancy | 0.5170 |

</details>


---

## 2026-11-05 — Celtic vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **46.0%**. Expected goals are 2.00 for Celtic and 2.43 for Besiktas JK (4.43 combined). The most likely exact score is 2-2 at 8.5%. Goal-market probabilities: at least one goal: 98.9%; Over 2.5 goals: 81.1%; Under 3.5 goals: 35.3%; Double Chance 1X: 54.0%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 55.3%; BTTS Yes (both teams score): 79.4%; BTTS No (at least one team does not score): 20.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celtic win | 31.5% | 3.18 |
| Draw | 22.5% | 4.44 |
| Besiktas JK win | 46.0% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celtic expected goals | 2.00 |
| Besiktas JK expected goals | 2.43 |
| Expected total goals | 4.43 |
| Over 0.5 | 98.9% |
| Under 0.5 | 1.1% |
| Over 1.5 | 93.4% |
| Under 1.5 | 6.6% |
| Over 2.5 | 81.1% |
| Under 2.5 | 18.9% |
| Over 3.5 | 64.7% |
| Under 3.5 | 35.3% |
| Over 4.5 | 44.7% |
| Under 4.5 | 55.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.49% |
| 2 | 1-2 | 6.66% |
| 3 | 1-1 | 6.62% |
| 4 | 2-1 | 5.55% |
| 5 | 2-3 | 5.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celtic win | 31.5% | 30.9% | 3.10 | -2.4% |
| Draw | 22.5% | 24.2% | 3.89 | -12.5% |
| Besiktas JK win | 46.0% | 44.9% | 2.23 | +2.6% |
| Over 2.5 | 81.1% | 58.4% | 1.67 | +35.5% |
| Under 2.5 | 18.9% | 41.6% | 2.31 | -56.4% |

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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:22:36Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
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
| P btts yes | 79.4% |
| P btts no | 20.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 92.30 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.04 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.30 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
| Fair Over 4.5 odds | 2.24 |
| Fair Under 4.5 odds | 1.81 |
| Goal margin distribution | {"-1": 0.17887679244862087, "-10": 3.475227305446276e-05, "-11": 7.420602189464076e-06, "-12": 1.4600539114370762e-06, "-13": 2.6627756901806366e-07, "-14": 4.5244216764987345e-08, "-15": 7.193544110317794e-09, "-16": 1.0722399562911581e-09, "-17": 1.471215086853392e-10, "-18": 1.565129096179044e-11, "-2": 0.1332485359633965, "-3": 0.08096229608066746, "-4": 0.04061865806446098, "-5": 0.017237330765533146, "-6": 0.0063128576100671225, "-7": 0.002028366391955729, "-8": 0.0005795886039854399, "-9": 0.00014894751961514642, "0": 0.22499184152913823, "1": 0.14970294778540824, "10": 5.001195164224764e-06, "11": 8.78485561966185e-07, "12": 1.4219006787251396e-07, "13": 2.1332406176964495e-08, "14": 2.981763722531589e-09, "15": 3.899940261048548e-10, "16": 4.7820258764972304e-11, "17": 5.397603716162939e-12, "18": 4.723673623173743e-13, "2": 0.0914353015723416, "3": 0.04570241643075591, "4": 0.01886195957368456, "5": 0.006584702302682077, "6": 0.001983796020928521, "7": 0.0005243512632365894, "8": 0.00012325389190156392, "9": 2.605667347412087e-05} |
| Raw goal margin distribution | {"-1": 0.18884807033305034, "-10": 3.668949792862385e-05, "-11": 7.834254991977318e-06, "-12": 1.5414429115298014e-06, "-13": 2.8112090111678795e-07, "-14": 4.776630278772633e-08, "-15": 7.594539825390683e-09, "-16": 1.1320107203830878e-09, "-17": 1.5532262536345372e-10, "-18": 1.6523753897276595e-11, "-2": 0.14067631997940322, "-3": 0.08547544471963174, "-4": 0.042882897719639816, "-5": 0.01819820563753938, "-6": 0.0066647604847393325, "-7": 0.0021414353075415093, "-8": 0.0006118970938117392, "-9": 0.00015725042513994072, "0": 0.18638355596576953, "1": 0.15586450767698298, "10": 5.207037226720399e-06, "11": 9.146427751941928e-07, "12": 1.4804240833837732e-07, "13": 2.221041760048823e-08, "14": 3.1044888660954888e-09, "15": 4.0604562418457973e-10, "16": 4.978847243591044e-11, "17": 5.619761389476076e-12, "18": 4.918093294716602e-13, "2": 0.09519864822099787, "3": 0.04758346273073558, "4": 0.019638290937261396, "5": 0.0068557192613081935, "6": 0.0020654462367488548, "7": 0.0005459328136365612, "8": 0.0001283268463627531, "9": 2.712912900396216e-05} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 48.6% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.4% |
| Raw p btts yes | 78.6% |
| Home training matches | 13 |
| Away training matches | 11 |
| P home draw | 54.0% |
| P draw away | 68.5% |
| P home away | 77.5% |
| Raw p home draw | 51.4% |
| Raw p draw away | 67.2% |
| Raw p home away | 81.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.8112 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.67, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.23, "draw": 3.83, "home": 3.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.15, "draw": 3.89, "home": 3.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.07 |
| Reference draw odds | 3.89 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | +0.6% |
| Draw probability edge | -1.7% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +22.7% |
| Under 2.5 probability edge | -22.7% |
| Raw edge prob home | 0.0185 |
| Raw ev home | 0.0165 |
| Raw edge prob draw | -0.0552 |
| Raw ev draw | -0.2750 |
| Raw edge prob away | 0.0366 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:22:36Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | crystal palace |
| Matched away-team name | hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7142 |
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
| Fair Under 0.5 odds | 63.23 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.71 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.38 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.45 |
| Fair Over 4.5 odds | 2.56 |
| Fair Under 4.5 odds | 1.64 |
| Goal margin distribution | {"-1": 0.14112390989369306, "-10": 3.5664121893275805e-07, "-11": 4.6297818222117017e-08, "-12": 5.533280694249592e-09, "-13": 6.125416482453171e-10, "-14": 6.314041681017817e-11, "-15": 6.088339242620204e-12, "-16": 5.513749607257298e-13, "-17": 4.701598285232987e-14, "-18": 3.73209334769614e-15, "-19": 2.3864612393643865e-16, "-2": 0.06645322420335799, "-3": 0.025394671752022594, "-4": 0.00792423884186368, "-5": 0.0020762778595179165, "-6": 0.0004671504879671495, "-7": 9.189052341907377e-05, "-8": 1.603382901496023e-05, "-9": 2.5114623925363687e-06, "0": 0.2144719464822215, "1": 0.1724859216897447, "10": 0.00011003818731297594, "11": 2.6373926418245048e-05, "12": 5.819683135989829e-06, "13": 1.1894731221541508e-06, "14": 2.26375189749907e-07, "15": 4.030162882888291e-08, "16": 6.738654159481309e-09, "17": 1.0608989517357976e-09, "18": 1.5548316465160686e-10, "19": 1.8356405014839288e-11, "2": 0.1518479620014569, "3": 0.1071366066283861, "4": 0.06172416347792322, "5": 0.029859704218032787, "6": 0.012403927183595936, "7": 0.004504799843795529, "8": 0.0014512572241701278, "9": 0.00041969732253297685} |
| Raw goal margin distribution | {"-1": 0.11195891456745583, "-10": 2.829369154511389e-07, "-11": 3.6729803467706016e-08, "-12": 4.389760041313372e-09, "-13": 4.8595236708341e-10, "-14": 5.009167147317122e-11, "-15": 4.830108899588158e-12, "-16": 4.3742652941679247e-13, "-17": 3.7299550525734225e-14, "-18": 2.9608102594892465e-15, "-19": 1.8932696112076954e-16, "-2": 0.05271984638832802, "-3": 0.02014654984612458, "-4": 0.006286597219256748, "-5": 0.001647189449804602, "-6": 0.00037060808201712673, "-7": 7.290021420739178e-05, "-8": 1.2720240632699139e-05, "-9": 1.992437735442332e-06, "0": 0.16534926732749536, "1": 0.20413786474623433, "10": 0.00013023069000971482, "11": 3.1213660635324475e-05, "12": 6.887621188108055e-06, "13": 1.4077467943519816e-06, "14": 2.679160560720545e-07, "15": 4.769715913233624e-08, "16": 7.975227531057297e-09, "17": 1.2555786848993623e-09, "18": 1.8401502525555587e-10, "19": 2.1724887964402232e-11, "2": 0.17971274655563815, "3": 0.12679665620835612, "4": 0.07305082532066096, "5": 0.03533909435221897, "6": 0.0146801036567009, "7": 0.005331450892993461, "8": 0.0017175694574802576, "9": 0.0004967136704391537} |
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
| Unanchored p over 2 5 | 0.7716 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.73, "draw": 4.0, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.62, "draw": 4.06, "home": 1.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.96 |
| Reference draw odds | 4.06 |
| Reference away odds | 3.62 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:37Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:37Z |
| Home probability edge | +4.3% |
| Draw probability edge | -2.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +14.1% |
| Under 2.5 probability edge | -14.1% |
| Raw edge prob home | 0.1421 |
| Raw ev home | 0.2572 |
| Raw edge prob draw | -0.0702 |
| Raw ev draw | -0.3287 |
| Raw edge prob away | -0.0719 |
| Raw ev away | -0.2793 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Goal margin distribution | {"-1": 0.19703209625660323, "-10": 5.052988533938338e-07, "-11": 5.990253625107067e-08, "-12": 6.512918877902266e-09, "-13": 6.53616657720677e-10, "-14": 5.919711385046573e-11, "-2": 0.11862609410355869, "-3": 0.04991913562250209, "-4": 0.015977175836160065, "-5": 0.004120288195543548, "-6": 0.0008891368832331379, "-7": 0.0001648893946830171, "-8": 2.6802899940479524e-05, "-9": 3.877483691576538e-06, "0": 0.26435797697368424, "1": 0.2983230647006927, "10": 4.1499673879633755e-12, "11": 1.2843660474521432e-13, "12": 3.645578960232875e-15, "13": 9.551271422398184e-17, "14": 2.2583218825747395e-18, "2": 0.04515425958666097, "3": 0.004960583742868708, "4": 0.00041448897036533276, "5": 2.7905370445361416e-05, "6": 1.5720851262449424e-06, "7": 7.611099351218887e-08, "8": 3.2298599181083065e-09, "9": 1.2198294561879328e-10} |
| Raw goal margin distribution | {"-1": 0.31606715514708567, "-10": 8.105703290253708e-07, "-11": 9.60920813343707e-08, "-12": 1.0447636606177206e-08, "-13": 1.0484929180953045e-09, "-14": 9.496048472867932e-11, "-2": 0.19029291573233073, "-3": 0.08007730457812155, "-4": 0.025629634002590242, "-5": 0.006609520951629851, "-6": 0.0014263004381471491, "-7": 0.00026450574744691936, "-8": 4.29956159165385e-05, "-9": 6.2200284258750255e-06, "0": 0.27937580409131785, "1": 0.08568507798355848, "10": 1.1919637511891002e-12, "11": 3.6889874755673267e-14, "12": 1.0470920772290145e-15, "13": 2.7433394648564086e-17, "14": 6.486407171183229e-19, "2": 0.0129693165288936, "3": 0.0014247909570053795, "4": 0.00011905053263216875, "5": 8.015048535284538e-06, "6": 4.5153812285429207e-07, "7": 2.1860785122468183e-08, "8": 9.27688240387125e-10, "9": 3.5036239046743094e-11} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.3, "draw": 3.65, "home": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.7, "home": 2.1}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda home | 0.4626 |
| Dc lambda away | 2.4856 |
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
| Goal margin distribution | {"-1": 0.14778153225802967, "-10": 9.517393791466923e-05, "-11": 2.132117643791085e-05, "-12": 4.384152160349655e-06, "-13": 8.330039283414965e-07, "-14": 1.470902560262282e-07, "-15": 2.42577422756726e-08, "-16": 3.752430206754039e-09, "-17": 5.456067945322109e-10, "-18": 7.081773051522655e-11, "-2": 0.15411554152381976, "-3": 0.11706118345199414, "-4": 0.06892126795804955, "-5": 0.03302890634341834, "-6": 0.013325035281552947, "-7": 0.00463772218373334, "-8": 0.0014185500033302501, "-9": 0.0003868747193993544, "0": 0.21024824372148773, "1": 0.20535362432174717, "10": 3.3441849427032706e-11, "11": 1.394214856484947e-12, "12": 5.335196934881303e-14, "13": 1.8865059516500405e-15, "14": 6.199281081297144e-17, "15": 1.9026289293159735e-18, "16": 5.477250902975693e-20, "17": 1.4820951167441042e-21, "18": 3.5800130127893484e-23, "2": 0.03763988886129581, "3": 0.005320606004274274, "4": 0.0005829720621672071, "5": 5.199181413744749e-05, "6": 3.903511287738698e-06, "7": 2.5283552512464434e-07, "8": 1.4392104678644891e-08, "9": 7.304597753998408e-10} |
| Raw goal margin distribution | {"-1": 0.22409393380444578, "-10": 0.0001443204831962315, "-11": 3.2331146039057894e-05, "-12": 6.648069545622346e-06, "-13": 1.263155986572604e-06, "-14": 2.2304569179637512e-07, "-15": 3.678411509686128e-08, "-16": 5.6901348464158495e-09, "-17": 8.273508267844729e-10, "-18": 1.073870569060768e-10, "-2": 0.23369874051768502, "-3": 0.1775100088268026, "-4": 0.10451128651543964, "-5": 0.05008459067017873, "-6": 0.020205904815714774, "-7": 0.007032579728773784, "-8": 0.0021510702026660915, "-9": 0.0005866516366085509, "0": 0.1264077918028838, "1": 0.04415734973004537, "10": 7.191026920738966e-12, "11": 2.997991061515003e-13, "12": 1.1472315509907984e-14, "13": 4.0565684365182645e-16, "14": 1.333036237786537e-17, "15": 4.091237800929814e-19, "16": 1.1777775263559889e-20, "17": 3.1869606694022728e-22, "18": 7.698129856046148e-24, "2": 0.008093734608959917, "3": 0.0011440940518215998, "4": 0.00012535693644067305, "5": 1.1179840275765981e-05, "6": 8.393750715487294e-07, "7": 5.436741982998082e-08, "8": 3.0947454750086077e-09, "9": 1.570713342537549e-10} |
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
| Unanchored p over 2 5 | 0.4749 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.32, "draw": 3.88, "home": 2.92}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.29, "draw": 3.83, "home": 2.87}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.87 |
| Reference draw odds | 3.83 |
| Reference away odds | 2.29 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -8.4% |
| Draw probability edge | -3.6% |
| Away probability edge | +12.0% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | -0.2792 |
| Raw ev home | -0.8437 |
| Raw edge prob draw | -0.1198 |
| Raw ev draw | -0.5095 |
| Raw edge prob away | 0.3989 |
| Raw ev away | 0.9025 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 2.2014 |
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
| Fair Under 0.5 odds | 102.60 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.91 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.57 |
| Fair Over 3.5 odds | 1.52 |
| Fair Under 3.5 odds | 2.93 |
| Fair Over 4.5 odds | 2.17 |
| Fair Under 4.5 odds | 1.86 |
| Goal margin distribution | {"-1": 0.12116715479209782, "-10": 9.17038380509233e-06, "-11": 1.7695469385387788e-06, "-12": 3.1469550886660093e-07, "-13": 5.1882310160048266e-08, "-14": 7.970076366827744e-09, "-15": 1.1457487956376227e-09, "-16": 1.5438975007694035e-10, "-17": 1.9122244262034647e-11, "-18": 1.8257170045244662e-12, "-2": 0.08064584050324387, "-3": 0.04398020055370811, "-4": 0.01984726206823141, "-5": 0.007587226904939397, "-6": 0.0025056305971454538, "-7": 0.0007264866671546875, "-8": 0.00018742125047780753, "-9": 4.35030807728506e-05, "0": 0.22098847551975853, "1": 0.2104097532660149, "10": 2.339015990329894e-05, "11": 4.710055971573829e-06, "12": 8.741235654645765e-07, "13": 1.503903228884751e-07, "14": 2.4109120709933633e-08, "15": 3.616817544353074e-09, "16": 5.0859719197319e-10, "17": 6.573742039352648e-11, "18": 6.549762608599902e-12, "2": 0.14624506850439062, "3": 0.0832290170832666, "4": 0.039195523303762574, "5": 0.01563641678025938, "6": 0.005388768313209909, "7": 0.0016304910488596338, "8": 0.00043896298896842066, "9": 0.00010632793742656235} |
| Raw goal margin distribution | {"-1": 0.17002679260867384, "-10": 1.2868264077387268e-05, "-11": 2.483101883893279e-06, "-12": 4.4159383054550504e-07, "-13": 7.280341611369357e-08, "-14": 1.1183942742759617e-08, "-15": 1.607762377450995e-09, "-16": 2.166461204959226e-10, "-17": 2.683312870498638e-11, "-18": 2.561922057368103e-12, "-2": 0.11316559856113327, "-3": 0.061714847156920244, "-4": 0.027850503854079608, "-5": 0.010646712449876005, "-6": 0.0035160050974687215, "-7": 0.0010194363158994673, "-8": 0.0002629972960917189, "-9": 6.10453328304631e-05, "0": 0.1884270950763892, "1": 0.1773109949831886, "10": 1.9710742781141264e-05, "11": 3.96913497489071e-06, "12": 7.366185109053615e-07, "13": 1.2673299299717186e-07, "14": 2.0316606596860608e-08, "15": 3.0478697280307046e-09, "16": 4.2859170145221523e-10, "17": 5.5396516733081453e-11, "18": 5.5194443556344036e-12, "2": 0.12323981281948683, "3": 0.07013657685273471, "4": 0.033029824558990256, "5": 0.013176711508113484, "6": 0.0045410816586108176, "7": 0.0013740047012886266, "8": 0.0003699113901644245, "9": 8.960189386172869e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.3, "draw": 4.15, "home": 1.79}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.07, "draw": 3.97, "home": 1.81}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.81 |
| Reference draw odds | 3.97 |
| Reference away odds | 4.07 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -3.4% |
| Draw probability edge | -1.4% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | +21.7% |
| Under 2.5 probability edge | -21.7% |
| Raw edge prob home | -0.1129 |
| Raw ev home | -0.2338 |
| Raw edge prob draw | -0.0465 |
| Raw ev draw | -0.2180 |
| Raw edge prob away | 0.1594 |
| Raw ev away | 0.6696 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda home | 2.2595 |
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
| Goal margin distribution | {"-1": 0.1607890643440678, "-10": 1.7472823494917605e-11, "-11": 6.993785315732011e-13, "-12": 2.5698071989443312e-14, "-13": 8.726124059364231e-16, "-14": 2.7539390901721554e-17, "-15": 8.117964033651043e-19, "-16": 2.2447984360339817e-20, "-17": 5.844957602949008e-22, "-18": 1.4351942960965664e-23, "-19": 3.1473473350044733e-25, "-2": 0.027750367274793384, "-3": 0.003738956039830069, "-4": 0.0003916183774996596, "-5": 3.344042749132538e-05, "-6": 2.4062203180047884e-06, "-7": 1.494633516456654e-07, "-8": 8.162527915628994e-09, "-9": 3.975884504272772e-10, "0": 0.2275587574583064, "1": 0.12741252546995316, "10": 0.00027452882422210356, "11": 7.057124211803601e-05, "12": 1.6653541758434112e-05, "13": 3.631767654889991e-06, "14": 7.361081197705088e-07, "15": 1.3935578593806205e-07, "16": 2.474832653724319e-08, "17": 4.138476145000647e-09, "18": 6.52620024079855e-10, "19": 9.191469979419396e-11, "2": 0.15064986975276273, "3": 0.13035899048689853, "4": 0.08768883448631823, "5": 0.04808876889557489, "6": 0.022222751623554044, "7": 0.008865184203845366, "8": 0.0031093408387768986, "9": 0.0009726755873461137} |
| Raw goal margin distribution | {"-1": 0.04047873817739482, "-10": 6.320265141432779e-13, "-11": 2.0094596890532488e-14, "-12": 5.861804386729324e-16, "-13": 1.5795503475076426e-17, "-14": 3.954586208699066e-19, "-15": 9.244895351837165e-21, "-16": 2.0249857922055557e-22, "-17": 4.003647949041355e-24, "-2": 0.005875510869068536, "-3": 0.0006477464151852631, "-4": 5.484904259635705e-05, "-5": 3.761639796364386e-06, "-6": 2.1653369036468864e-07, "-7": 1.0732543216496563e-08, "-8": 4.668918163182445e-10, "-9": 1.809309417168296e-11, "0": 0.13865263743358144, "1": 0.24413957575143744, "10": 7.54468898524948e-05, "11": 1.5405505259862438e-05, "12": 2.886147843466819e-06, "13": 4.99472210832403e-07, "14": 8.030997834217728e-08, "15": 1.2057605351923175e-08, "16": 1.6961788770795321e-09, "17": 2.153754294068408e-10, "2": 0.2423409704959793, "3": 0.17158401711869542, "4": 0.09331070458548335, "5": 0.04109890284565628, "6": 0.015193894407723868, "7": 0.0048365633052851, "8": 0.0013512667696468183, "9": 0.0003363010962937599} |
| Unadjusted home-win probability | 81.4% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.4% |
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
| Totals anchor scale | 1.2634 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-03T13:22:36Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4032 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.79, "draw": 3.75, "home": 2.0}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.69, "draw": 3.55, "home": 2.02}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.02 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.69 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:36Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:36Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | +10.1% |
| Draw probability edge | -3.8% |
| Away probability edge | -6.2% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3351 |
| Raw ev home | 0.6449 |
| Raw edge prob draw | -0.1270 |
| Raw ev draw | -0.4801 |
| Raw edge prob away | -0.2081 |
| Raw ev away | -0.8216 |
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
| 4 | 2-0 | 8.18% |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:22:36Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | real sociedad |
| Matched away-team name | lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9622 |
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
| Goal margin distribution | {"-1": 0.14372030208774722, "-10": 6.697508064587352e-08, "-11": 6.944429571005953e-09, "-12": 6.617239292422096e-10, "-13": 5.832057682800697e-11, "-14": 4.778737339136794e-12, "-15": 3.630918824796853e-13, "-16": 2.3044721559546926e-14, "-2": 0.060726487547146775, "-3": 0.02004302341151338, "-4": 0.005254444058118383, "-5": 0.0011369843029942967, "-6": 0.00020891408058213448, "-7": 3.330517671785402e-05, "-8": 4.6845042184958375e-06, "-9": 5.891480229158144e-07, "0": 0.22427512930620017, "1": 0.2266164269982096, "10": 1.2154437830757373e-05, "11": 2.1318521259501276e-06, "12": 3.4363406287407715e-07, "13": 5.123185082477589e-08, "14": 7.101175779796945e-09, "15": 9.127093724278e-10, "16": 9.799102568567353e-11, "2": 0.16436481324095292, "3": 0.09176832190777964, "4": 0.04069632537667043, "5": 0.01489641493900859, "6": 0.004630137324867413, "7": 0.0012486386395366472, "8": 0.00029708965541164027, "9": 6.320438183539386e-05} |
| Raw goal margin distribution | {"-1": 0.14105521327903575, "-10": 6.573312293148682e-08, "-11": 6.81565499104944e-09, "-12": 6.494531991319758e-10, "-13": 5.723910459086247e-11, "-14": 4.690122444669557e-12, "-15": 3.5635885938918426e-13, "-16": 2.2617389939476135e-14, "-2": 0.059600401113961816, "-3": 0.019671354018874935, "-4": 0.005157007858417508, "-5": 0.0011159005444885519, "-6": 0.00020504006577661482, "-7": 3.268757953462017e-05, "-8": 4.597636743367288e-06, "-9": 5.782231098747271e-07, "0": 0.20807372756306672, "1": 0.23514159270618284, "10": 1.2611680043808786e-05, "11": 2.2120510456814123e-06, "12": 3.5656135754424134e-07, "13": 5.3159160435966764e-08, "14": 7.368317491658344e-09, "15": 9.470449179406977e-10, "16": 1.0167738568583025e-10, "2": 0.17054811287196459, "3": 0.09522058775350602, "4": 0.04222729522796216, "5": 0.015456808585188445, "6": 0.004804320143244824, "7": 0.0012956116302082915, "8": 0.0003082659791056368, "9": 6.558209044087375e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.03, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.43, "price": 3.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.21, "draw": 4.11, "home": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.1, "draw": 4.13, "home": 1.83}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.13 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:53Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:53Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0293 |
| Raw ev home | 0.0341 |
| Raw edge prob draw | -0.0231 |
| Raw ev draw | -0.1407 |
| Raw edge prob away | -0.0061 |
| Raw ev away | -0.0450 |
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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 0.4748 |
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
| Fair Over 3.5 odds | 14.69 |
| Fair Under 3.5 odds | 1.07 |
| Fair Over 4.5 odds | 49.10 |
| Fair Under 4.5 odds | 1.02 |
| Goal margin distribution | {"-1": 0.13374430060466425, "-10": 3.6069100671664546e-11, "-11": 1.551291638156374e-12, "-12": 6.115676712306513e-14, "-13": 2.1545509399504604e-15, "-2": 0.028359844361154355, "-3": 0.004320557931252928, "-4": 0.0005010832406717763, "-5": 4.684646060012765e-05, "-6": 3.6658568488987177e-06, "-7": 2.4656553814926444e-07, "-8": 1.453800389531755e-08, "-9": 7.629427784387448e-10, "0": 0.24194077178669904, "1": 0.35801342377252066, "10": 8.43346175924443e-08, "11": 7.680349048965116e-09, "12": 6.411342327522873e-10, "13": 4.782755210117892e-11, "2": 0.16407366781414987, "3": 0.05292877181919503, "4": 0.01299806791109719, "5": 0.002573135453206151, "6": 0.00042636181925626216, "7": 6.0722846445357516e-05, "8": 7.581261313460275e-06, "9": 8.424528276714243e-07} |
| Raw goal margin distribution | {"-1": 0.1414235034941044, "-10": 3.814008194597011e-11, "-11": 1.6403622241644278e-12, "-12": 6.466820813907115e-14, "-13": 2.2782588940742006e-15, "-2": 0.029988182898031453, "-3": 0.0045686316121475124, "-4": 0.0005298539610106625, "-5": 4.953624606368854e-05, "-6": 3.876339526508647e-06, "-7": 2.607226034180791e-07, "-8": 1.5372733158657247e-08, "-9": 8.0674870035225e-10, "0": 0.33904814511012965, "1": 0.2933894248329281, "10": 6.911161231952476e-08, "11": 6.293990784613022e-09, "12": 5.254048907043582e-10, "13": 3.919433482205877e-11, "2": 0.1344571902443764, "3": 0.04337474767709768, "4": 0.010651823130518184, "5": 0.002108665989890498, "6": 0.00034940044315711754, "7": 4.9761935753955076e-05, "8": 6.212789098314707e-06, "9": 6.903840307296446e-07} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.87, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.87, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.53, "draw": 4.55, "home": 1.53}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.57, "draw": 4.56, "home": 1.58}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.61, "under": 2.44}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.53 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.53 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -4.6% |
| Draw probability edge | +4.2% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -39.7% |
| Under 2.5 probability edge | +39.7% |
| Raw edge prob home | -0.1524 |
| Raw ev home | -0.2347 |
| Raw edge prob draw | 0.1387 |
| Raw ev draw | 0.5461 |
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
| 5 | 0-0 | 6.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Prague win | 10.7% | 14.9% | 6.18 | -33.7% |
| Draw | 15.1% | 19.7% | 4.71 | -28.9% |
| Bournemouth win | 74.2% | 65.4% | 1.52 | +12.7% |
| Over 2.5 | 62.4% | 60.4% | 1.62 | +1.0% |
| Under 2.5 | 37.6% | 39.6% | 2.42 | -8.9% |

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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda away | 3.5899 |
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
| Fair Under 1.5 odds | 5.07 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09321938207125081, "-10": 0.0017835373852484035, "-11": 0.0005780482479602365, "-12": 0.0001719160243614775, "-13": 4.723544205326963e-05, "-14": 1.2059370605760235e-05, "-15": 2.8751058290786856e-06, "-16": 6.429078178854003e-07, "-17": 1.3535578255285572e-07, "-18": 2.692265951860192e-08, "-19": 5.074444443529327e-09, "-2": 0.14515679101662532, "-20": 9.08042786028318e-10, "-21": 1.4869755322835584e-10, "-3": 0.16179803789517255, "-4": 0.1389879252191807, "-5": 0.0968753229400461, "-6": 0.05673610727074644, "-7": 0.028631016138439935, "-8": 0.012686898534283397, "-9": 0.005009594007293863, "0": 0.1510403016119519, "1": 0.09670665044257556, "10": 8.21466202376028e-14, "11": 1.9050409450805152e-15, "12": 4.0540521122424034e-17, "13": 7.970282118980027e-19, "14": 1.4560057647314778e-20, "15": 2.4838480831887324e-22, "16": 3.974226768324956e-24, "17": 5.987058391007132e-26, "18": 8.520937523332273e-28, "19": 1.1491868999665923e-29, "2": 0.009729329284399976, "20": 1.471435465525629e-31, "21": 1.7241358085556725e-33, "3": 0.0007759818020930833, "4": 4.769667449111129e-05, "5": 2.3787945452945307e-06, "6": 9.968643114027039e-08, "7": 3.59953182172749e-09, "8": 1.141293817067357e-10, "9": 3.2246105543826144e-12} |
| Raw goal margin distribution | {"-1": 0.11882871975764173, "-10": 0.0022735128620244437, "-11": 0.0007368503388143202, "-12": 0.00021914499567357847, "-13": 6.021201794800726e-05, "-14": 1.537233500507581e-05, "-15": 3.6649582656107075e-06, "-16": 8.195282056590884e-07, "-17": 1.7254088146879047e-07, "-18": 3.4318884034450094e-08, "-19": 6.46850175690912e-09, "-2": 0.18503443444249906, "-20": 1.1575013623930085e-09, "-21": 1.8954791899085818e-10, "-3": 0.20624738412969157, "-4": 0.17717085061712295, "-5": 0.12348902497846512, "-6": 0.0723227170274737, "-7": 0.03649656238324758, "-8": 0.016172258140176372, "-9": 0.006385835532971972, "0": 0.044098066908907226, "1": 0.009416542718897015, "10": 7.998800032265861e-15, "11": 1.8549809509999254e-16, "12": 3.9475211606293495e-18, "13": 7.760841856434957e-20, "14": 1.4177453587533361e-21, "15": 2.4185783992679715e-23, "16": 3.869793438946378e-25, "17": 5.829732582137811e-27, "18": 8.297027332278053e-29, "19": 1.1189889719071572e-30, "2": 0.0009473665400826812, "20": 1.4327696033118014e-32, "21": 1.678829575850641e-34, "3": 7.555908259727334e-05, "4": 4.6443318100607066e-06, "5": 2.3162854211920294e-07, "6": 9.706690626040687e-09, "7": 3.504944594007322e-10, "8": 1.1113033006565974e-11, "9": 3.1398753754976377e-13} |
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
| Unanchored p over 2 5 | 0.6237 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.0, "market_key": "spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.52, "draw": 4.71, "home": 6.18}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.42}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.49, "draw": 4.61, "home": 6.0}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.00 |
| Reference draw odds | 4.61 |
| Reference away odds | 1.49 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:34Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:34Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -4.1% |
| Draw probability edge | -4.6% |
| Away probability edge | +8.7% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.1383 |
| Raw ev home | -0.9355 |
| Raw edge prob draw | -0.1528 |
| Raw ev draw | -0.7923 |
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
| Dinamo Zagreb win | 15.8% | 6.32 |

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
| Market best home last update utc | 2026-11-03T13:21:30Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda home | 1.4770 |
| Dc lambda away | 0.7766 |
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
| Fair Over 3.5 odds | 5.06 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.00 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.11246994072463076, "-10": 1.9982923568237504e-09, "-11": 1.398738535726394e-10, "-12": 8.986559231573055e-12, "-13": 5.334664793442233e-13, "-14": 2.935797078380374e-14, "-15": 1.4119960906989016e-15, "-2": 0.03560659145486218, "-3": 0.008451866620316155, "-4": 0.0015549629748474836, "-5": 0.00023284786315402363, "-6": 2.9352706262114302e-05, "-7": 3.1921261095172843e-06, "-8": 3.050782626095489e-07, "-9": 2.5997121354773453e-08, "0": 0.2139497030610674, "1": 0.3100454538119929, "10": 1.8296579004136447e-06, "11": 2.435728905590747e-07, "12": 2.97623619006838e-08, "13": 3.360180674020234e-09, "14": 3.516924702624827e-10, "15": 3.2170074940107156e-11, "2": 0.1904534890166008, "3": 0.08597906311171626, "4": 0.030084421738691015, "5": 0.008567920231596172, "6": 0.0020541532847145124, "7": 0.0004248604280181065, "8": 7.722520118058312e-05, "9": 1.2515683943007992e-05} |
| Raw goal margin distribution | {"-1": 0.14420574167903466, "-10": 2.5621533144829628e-09, "-11": 1.7934225505935397e-10, "-12": 1.1522309256874754e-11, "-13": 6.839954642021944e-13, "-14": 3.764195058513708e-14, "-15": 1.8104210084511984e-15, "-2": 0.04565375331691884, "-3": 0.010836741681397984, "-4": 0.0019937290588632126, "-5": 0.0002985508713542942, "-6": 3.763520056597713e-05, "-7": 4.0928528119615275e-06, "-8": 3.911626239536789e-07, "-9": 3.333276555789954e-08, "0": 0.25271285360065365, "1": 0.2688289318829445, "10": 1.5864286124241992e-06, "11": 2.1119303379414552e-07, "12": 2.5805841890931742e-08, "13": 2.9134882334973012e-09, "14": 3.049395176401079e-10, "15": 2.7893480708759112e-11, "2": 0.1651351677511114, "3": 0.07454926178222483, "4": 0.026085088050452513, "5": 0.007428926359020125, "6": 0.0017810802469901724, "7": 0.0003683807443688448, "8": 6.695911226103788e-05, "9": 1.085188608578531e-05} |
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
| Unanchored p over 2 5 | 0.4083 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.95, "draw": 4.82, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.68, "under": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.37, "draw": 4.59, "home": 1.47}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 4.59 |
| Reference away odds | 6.37 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | -0.1192 |
| Raw ev home | -0.1999 |
| Raw edge prob draw | 0.0554 |
| Raw ev draw | 0.2181 |
| Raw edge prob away | 0.0638 |
| Raw ev away | 0.4111 |
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
| Market best home last update utc | 2026-11-03T13:22:36Z |
| Market best draw last update utc | 2026-11-03T13:21:30Z |
| Market best away last update utc | 2026-11-03T13:21:30Z |
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
| Dc lambda home | 4.8068 |
| Dc lambda away | 0.9300 |
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
| Goal margin distribution | {"-1": 0.13315845100686813, "-10": 1.522266406633004e-11, "-11": 6.075200106530246e-13, "-12": 2.2250741366205816e-14, "-13": 7.529430800343611e-16, "-14": 2.367622578809888e-17, "-15": 6.952766968284723e-19, "-16": 1.915028526432822e-20, "-17": 4.959536615984449e-22, "-18": 1.1539448523566299e-23, "-2": 0.023775617865655144, "-3": 0.003244927074240459, "-4": 0.0003420934569165144, "-5": 2.9299444424116068e-05, "-6": 2.1101316644256264e-06, "-7": 1.31008706585737e-07, "-8": 7.144549714727224e-09, "-9": 3.472795595210677e-10, "0": 0.17973964670768444, "1": 0.20031923878188215, "10": 6.371526621003786e-05, "11": 1.3142793260402744e-05, "12": 2.4879739289017915e-06, "13": 4.351487458290728e-07, "14": 7.072326684060692e-08, "15": 1.0734498619815524e-08, "16": 1.5281767535593507e-09, "17": 2.045566924305987e-10, "18": 2.4599818135396053e-11, "2": 0.19538474241630654, "3": 0.13782818153305146, "4": 0.07510210388913163, "5": 0.03324612025972047, "6": 0.012375575132966417, "7": 0.003971277599390402, "8": 0.001119384271021521, "9": 0.0002812275154434598} |
| Raw goal margin distribution | {"-1": 0.017764530668992206, "-10": 6.415397002885878e-10, "-11": 5.2509356870173866e-11, "-12": 3.958698052497513e-12, "-13": 2.7654553515547426e-13, "-14": 1.799435959242576e-14, "-15": 1.09556862529262e-15, "-16": 6.266464246828621e-17, "-17": 3.3793835058170144e-18, "-18": 1.7237419721206776e-19, "-19": 8.340168874413041e-21, "-2": 0.0050537707020107, "-20": 3.8377172457519786e-22, "-21": 1.6834098596669306e-23, "-22": 7.054135465756744e-25, "-23": 2.827348805852209e-26, "-24": 1.0736438179702429e-27, "-25": 3.3881134761240323e-29, "-3": 0.0011947785934003548, "-4": 0.00023210167194574643, "-5": 3.801624335853487e-05, "-6": 5.361816459942861e-06, "-7": 6.624331788255598e-07, "-8": 7.269990854277732e-08, "-9": 7.169680330741128e-09, "0": 0.04300584654103428, "1": 0.08881308761206672, "10": 0.008729031115979061, "11": 0.0036927801638080332, "12": 0.001438942311665483, "13": 0.000519555452913753, "14": 0.00017473338953416412, "15": 5.4986153934267654e-05, "16": 1.625588333081965e-05, "17": 4.531059216379783e-06, "18": 1.194562191598974e-06, "19": 2.987346530081353e-07, "2": 0.13500940842455006, "20": 7.10490021983647e-08, "21": 1.6108278378538776e-08, "22": 3.488809898184188e-09, "23": 7.227484198784552e-10, "24": 1.4185421312811118e-10, "25": 2.313738159154077e-11, "3": 0.16497197901014568, "4": 0.16564383271854405, "5": 0.14022984417067072, "6": 0.1022250770121224, "7": 0.06527724693927382, "8": 0.03702779650256849, "9": 0.01887417801072816} |
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
| Totals anchor scale | 0.4756 |
| Totals anchor target over 2 5 | 0.4722 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.82 |
| Totals anchor reference last update utc | 2026-11-03T13:22:36Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.8607 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.43, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.35, "price": 3.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.67, "draw": 4.0, "home": 1.76}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-03T13:21:30Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.04, "under": 1.85}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.25, "draw": 3.92, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-03T13:22:36Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.02, "under": 1.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.92 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-11-03T13:22:36Z |
| Market reference home last update utc | 2026-11-03T13:22:36Z |
| Market reference draw last update utc | 2026-11-03T13:22:36Z |
| Market reference away last update utc | 2026-11-03T13:22:36Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-11-03T13:22:36Z |
| Market reference under 2 5 last update utc | 2026-11-03T13:22:36Z |
| Market best over 2 5 last update utc | 2026-11-03T13:21:30Z |
| Market best under 2 5 last update utc | 2026-11-03T13:21:30Z |
| Home probability edge | +11.7% |
| Draw probability edge | -5.9% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.3900 |
| Raw ev home | 0.6695 |
| Raw edge prob draw | -0.1953 |
| Raw ev draw | -0.8280 |
| Raw edge prob away | -0.1947 |
| Raw ev away | -0.8866 |
| Elo home rating | 1,421.4152 |
| Elo away rating | 1,403.0006 |
| Elo rating diff | 78.4146 |
| Elo home expectancy | 0.6110 |

</details>


---
