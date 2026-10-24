# Eredivisie — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,611 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 07f731cdf742d41e92a355644fdc463e45a578cdc0186b7ef5b6327b823cce3b |
| Training as of utc | 2026-10-24T14:50:06.074652+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 1255.025 |
| Base scoring parameter | 0.289 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.101 |
| Xi per day | 0.0019 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-18'} |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 29.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — ADO Den Haag vs Heerenveen

The model's most likely 1X2 outcome is **Heerenveen win** at **46.1%**. Expected goals are 1.36 for ADO Den Haag and 1.68 for Heerenveen (3.04 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.6%; Double Chance 1X: 53.9%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ADO Den Haag win | 28.4% | 3.52 |
| Draw | 25.5% | 3.92 |
| Heerenveen win | 46.1% | 2.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ADO Den Haag expected goals | 1.36 |
| Heerenveen expected goals | 1.68 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.80% |
| 2 | 1-2 | 9.62% |
| 3 | 0-1 | 7.24% |
| 4 | 0-2 | 7.06% |
| 5 | 2-1 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| ADO Den Haag win | 28.4% | 26.8% | 3.55 | +0.9% |
| Draw | 25.5% | 25.0% | 3.99 | +1.7% |
| Heerenveen win | 46.1% | 48.2% | 1.99 | -8.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 37b2e2ce6ac958b456f8b82543199993 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Den Haag |
| Matched away-team name | Heerenveen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3625 |
| Dc lambda away | 1.6821 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.38 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.53 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.17 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.21326995584463485, "-10": 3.0668376789382716e-06, "-11": 4.610874303834005e-07, "-12": 6.370759994189839e-08, "-13": 8.137818804876673e-09, "-14": 9.58297790042023e-10, "-15": 9.322073021179552e-11, "-2": 0.1426096024260239, "-3": 0.06819439883012204, "-4": 0.025909492526879623, "-5": 0.008126649632793826, "-6": 0.0021647079096079845, "-7": 0.0005003236110203749, "-8": 0.00010203136176128517, "-9": 1.8605527806310185e-05, "0": 0.25499728478620187, "1": 0.15377885831064045, "10": 3.362118054411836e-07, "11": 4.0944528295764134e-08, "12": 4.582413267650011e-09, "13": 4.741343779541112e-10, "14": 4.5225599989837396e-11, "15": 3.5635821230137068e-12, "2": 0.08436213719027653, "3": 0.032676680366859764, "4": 0.010056307673224787, "5": 0.0025549452738410543, "6": 0.0005512642010033258, "7": 0.0001032052773466701, "8": 1.7048061775668006e-05, "9": 2.518104462433082e-06} |
| Raw goal margin distribution | {"-1": 0.203459481452497, "-10": 2.925762334336121e-06, "-11": 4.398772865992086e-07, "-12": 6.077703348991364e-08, "-13": 7.763476986888679e-09, "-14": 9.142158381701975e-10, "-15": 8.893255195932082e-11, "-2": 0.13604952298523917, "-3": 0.0650574384422392, "-4": 0.02471764901595674, "-5": 0.007752821599676588, "-6": 0.002065130773064954, "-7": 0.00047730859254645056, "-8": 9.733789212656905e-05, "-9": 1.7749668604890435e-05, "0": 0.2596898975378045, "1": 0.16271475001547292, "10": 3.55748641104508e-07, "11": 4.33237621825011e-08, "12": 4.848691409888466e-09, "13": 5.016857169449203e-10, "14": 4.7853601447481834e-11, "15": 3.770657297601111e-12, "2": 0.08926431249709094, "3": 0.03457548024246972, "4": 0.010640666780228219, "5": 0.0027034098581774665, "6": 0.0005832974548265913, "7": 0.00010920240329667614, "8": 1.8038702722532954e-05, "9": 2.6644282745939413e-06} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 63.7% |
| Raw p btts yes | 61.7% |
| P home draw | 53.9% |
| P draw away | 71.6% |
| P home away | 74.5% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.9% |
| Raw p home away | 74.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.8, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.37, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.31, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.64, "price": 1.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.62, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:30Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.45 |
| Reference away odds | 1.92 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +1.7% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | 0.0330 |
| Raw ev home | 0.0672 |
| Raw edge prob draw | 0.0094 |
| Raw ev draw | 0.0362 |
| Raw edge prob away | -0.0424 |
| Raw ev away | -0.1250 |
| Market p home draw | 52.9% |
| Market reference home draw last update utc | 2026-10-24T14:50:11Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.1% |
| Market reference draw away last update utc | 2026-10-24T14:50:11Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market reference home away last update utc | 2026-10-24T14:50:11Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.32 |
| Market reference dc home draw odds | 1.80 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 86.5% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.17 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.6% |
| Market reference btts yes odds | 1.41 |
| Market reference btts yes opposite odds | 2.69 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,365.4130 |
| Elo away rating | 1,478.9271 |
| Elo rating diff | -53.5141 |
| Elo home expectancy | 0.4236 |

</details>


---

## 2026-10-24 — Willem II vs SC Cambuur

The model's most likely 1X2 outcome is **SC Cambuur win** at **38.5%**. Expected goals are 1.50 for Willem II and 1.64 for SC Cambuur (3.14 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.9%; Under 3.5 goals: 61.5%; Double Chance 1X: 61.5%; Double Chance X2: 64.2%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II win | 35.8% | 2.79 |
| Draw | 25.6% | 3.90 |
| SC Cambuur win | 38.5% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II expected goals | 1.50 |
| SC Cambuur expected goals | 1.64 |
| Expected total goals | 3.14 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 38.5% |
| Under 3.5 | 61.5% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.65% |
| 2 | 2-1 | 8.40% |
| 3 | 1-2 | 8.37% |
| 4 | 2-2 | 6.53% |
| 5 | 0-1 | 5.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Willem II win | 35.8% | 37.7% | 2.49 | -10.8% |
| Draw | 25.6% | 25.5% | 3.81 | -2.3% |
| SC Cambuur win | 38.5% | 36.8% | 2.71 | +4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:45:00+00:00 |
| Fixture id | d962e99711c241eb444793ef2e07098b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Willem II |
| Matched away-team name | Cambuur |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4994 |
| Dc lambda away | 1.6449 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.66 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.95 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.18366921371183437, "-10": 2.058521359214133e-06, "-11": 3.022667117165695e-07, "-12": 4.0796122535705845e-08, "-13": 5.090653891033796e-09, "-14": 5.849481009613489e-10, "-15": 5.508835070280124e-11, "-2": 0.11840099122142647, "-3": 0.05481127981816279, "-4": 0.020225939758688444, "-5": 0.006173539762722984, "-6": 0.001602255678357151, "-7": 0.0003611211790770611, "-8": 7.185492244399427e-05, "-9": 1.2789919456518071e-05, "0": 0.2563659992901111, "1": 0.18334955725301924, "10": 8.97619206931695e-07, "11": 1.20142738399078e-07, "12": 1.4780752280109113e-08, "13": 1.6812088497026996e-09, "14": 1.7609048021968074e-10, "15": 1.5116413331571822e-11, "2": 0.10832495845794952, "3": 0.0457102484173036, "4": 0.01537527151955259, "5": 0.004277783293466067, "6": 0.001012014640876045, "7": 0.00020791143774239154, "8": 3.770964054712979e-05, "9": 6.118347265421629e-06} |
| Raw goal margin distribution | {"-1": 0.1919113049274822, "-10": 2.1508967795097824e-06, "-11": 3.158308238455112e-07, "-12": 4.262683415246913e-08, "-13": 5.319095189764578e-09, "-14": 6.111974407778061e-10, "-15": 5.7560421020064374e-11, "-2": 0.12371419396209477, "-3": 0.057270916677154726, "-4": 0.021133571675025036, "-5": 0.006450575183191566, "-6": 0.0016741563370735793, "-7": 0.0003773263646805951, "-8": 7.507938675735426e-05, "-9": 1.3363862583245892e-05, "0": 0.25737469312245304, "1": 0.17398497933809784, "10": 8.517733094712397e-07, "11": 1.1400644850830076e-07, "12": 1.4025825415588667e-08, "13": 1.5953411143224058e-09, "14": 1.6709665963566094e-10, "15": 1.4344342580169287e-11, "2": 0.10279226163114337, "3": 0.043375597659333465, "4": 0.01458997958721796, "5": 0.0040592955285922725, "6": 0.0009603259970772126, "7": 0.00019729236187816609, "8": 3.5783620804633455e-05, "9": 5.8058527029257955e-06} |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 40.3% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 61.5% |
| Raw p btts yes | 63.8% |
| P home draw | 61.5% |
| P draw away | 64.2% |
| P home away | 74.4% |
| Raw p home draw | 59.7% |
| Raw p draw away | 66.0% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.65, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.4, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.05, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.49, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:06Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.43, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.43, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.40 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.47 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.1% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | -0.0366 |
| Raw ev home | -0.1534 |
| Raw edge prob draw | 0.0020 |
| Raw ev draw | -0.0194 |
| Raw edge prob away | 0.0346 |
| Raw ev away | 0.0911 |
| Market p home draw | 63.4% |
| Market reference home draw last update utc | 2026-10-24T14:50:11Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.2% |
| Market reference draw away last update utc | 2026-10-24T14:50:11Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.4% |
| Market reference home away last update utc | 2026-10-24T14:50:11Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.37 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.1% |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.60 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,340.9350 |
| Elo away rating | 1,415.8533 |
| Elo rating diff | -14.9183 |
| Elo home expectancy | 0.4785 |

</details>


---

## 2026-10-25 — AZ Alkmaar vs FC Twente Enschede

The model's most likely 1X2 outcome is **AZ Alkmaar win** at **41.9%**. Expected goals are 1.47 for AZ Alkmaar and 1.30 for FC Twente Enschede (2.77 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.8%; Double Chance 1X: 68.0%; Double Chance X2: 58.1%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AZ Alkmaar win | 41.9% | 2.39 |
| Draw | 26.1% | 3.83 |
| FC Twente Enschede win | 32.0% | 3.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AZ Alkmaar expected goals | 1.47 |
| FC Twente Enschede expected goals | 1.30 |
| Expected total goals | 2.77 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.2% |
| Under 3.5 | 69.8% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.39% |
| 2 | 2-1 | 9.22% |
| 3 | 1-0 | 8.39% |
| 4 | 1-2 | 7.73% |
| 5 | 2-0 | 7.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AZ Alkmaar win | 41.9% | 43.8% | 2.18 | -8.7% |
| Draw | 26.1% | 24.4% | 3.97 | +3.5% |
| FC Twente Enschede win | 32.0% | 31.8% | 2.94 | -5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:00:00+00:00 |
| Fixture id | b435848f58054cad7d3fad610a96c4b5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | AZ Alkmaar |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.4696 |
| Dc lambda away | 1.2997 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.23 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.31 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.17511674490484064, "-10": 2.8041077343569655e-07, "-11": 3.266549643779593e-08, "-12": 3.495623920914287e-09, "-13": 3.4578820141677246e-10, "-14": 3.1603681023667025e-11, "-15": 2.4290904879195235e-12, "-2": 0.0951566025050076, "-3": 0.03597276709834829, "-4": 0.010723426773825961, "-5": 0.002627280883634286, "-6": 0.0005451310377026141, "-7": 9.79607523296368e-05, "-8": 1.5512181599857022e-05, "-9": 2.1943918642408566e-06, "0": 0.26082427764892374, "1": 0.2105693993505489, "10": 1.0107305089821998e-06, "11": 1.3313277695316772e-07, "12": 1.6109255839834776e-08, "13": 1.8018390511824592e-09, "14": 1.8620808872300104e-10, "15": 1.618302161445534e-11, "2": 0.12836281176528308, "3": 0.05486927076846663, "4": 0.018494559043043878, "5": 0.005123561394915961, "6": 0.0012020468558659003, "7": 0.0002442461051560057, "8": 4.373241530826392e-05, "9": 6.9951948477671256e-06} |
| Raw goal margin distribution | {"-1": 0.17638347996260298, "-10": 2.8243916973485263e-07, "-11": 3.290178754484825e-08, "-12": 3.5209100771398426e-09, "-13": 3.482895158258155e-10, "-14": 3.183229131863779e-11, "-15": 2.446661703517419e-12, "-2": 0.09584493304950319, "-3": 0.036232981878111116, "-4": 0.010800996401111655, "-5": 0.002646285741243401, "-6": 0.0005490743304865652, "-7": 9.86693671415907e-05, "-8": 1.562439145314999e-05, "-9": 2.2102653497057265e-06, "0": 0.27750937784554347, "1": 0.20101815907304543, "10": 9.648846739422226e-07, "11": 1.2709399284962334e-07, "12": 1.5378554352854274e-08, "13": 1.7201092377702917e-09, "14": 1.7776185578272824e-10, "15": 1.5448974177684265e-11, "2": 0.12254038903126974, "3": 0.05238044955048628, "4": 0.01765566232874727, "5": 0.004891161216588455, "6": 0.0011475230818483873, "7": 0.00023316731951865987, "8": 4.174875192786254e-05, "9": 6.677899044174362e-06} |
| Unadjusted home-win probability | 40.0% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 69.9% |
| Raw p btts yes | 57.2% |
| P home draw | 68.0% |
| P draw away | 58.1% |
| P home away | 73.9% |
| Raw p home draw | 67.7% |
| Raw p draw away | 60.0% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.93, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.3, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.29, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.59, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | -0.0380 |
| Raw ev home | -0.1282 |
| Raw edge prob draw | 0.0334 |
| Raw ev draw | 0.1017 |
| Raw edge prob away | 0.0046 |
| Raw ev away | -0.0516 |
| Market p home draw | 67.7% |
| Market reference home draw last update utc | 2026-10-24T14:50:14Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.0% |
| Market reference draw away last update utc | 2026-10-24T14:50:14Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market reference home away last update utc | 2026-10-24T14:50:14Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.64 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 87.2% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.29 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.0% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.2% |
| Market reference btts yes odds | 1.40 |
| Market reference btts yes opposite odds | 2.73 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,554.0981 |
| Elo away rating | 1,560.3337 |
| Elo rating diff | 53.7643 |
| Elo home expectancy | 0.5768 |

</details>


---

## 2026-10-25 — Fortuna Sittard vs Excelsior

The model's most likely 1X2 outcome is **Fortuna Sittard win** at **41.6%**. Expected goals are 1.65 for Fortuna Sittard and 1.40 for Excelsior (3.04 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.7%; Under 3.5 goals: 63.7%; Double Chance 1X: 67.7%; Double Chance X2: 58.4%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fortuna Sittard win | 41.6% | 2.40 |
| Draw | 26.1% | 3.84 |
| Excelsior win | 32.3% | 3.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fortuna Sittard expected goals | 1.65 |
| Excelsior expected goals | 1.40 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 2-1 | 8.87% |
| 3 | 1-2 | 7.85% |
| 4 | 1-0 | 6.62% |
| 5 | 2-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fortuna Sittard win | 41.6% | 40.9% | 2.42 | +0.7% |
| Draw | 26.1% | 26.0% | 3.63 | -5.4% |
| Excelsior win | 32.3% | 33.1% | 2.86 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:15:00+00:00 |
| Fixture id | f168373343a58c07d02f40538d04b404 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | For Sittard |
| Matched away-team name | Excelsior |
| Home-name matching confidence | 85/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6456 |
| Dc lambda away | 1.3986 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.08 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.50 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.1720072697339308, "-10": 4.7367270211364333e-07, "-11": 5.920828593945641e-08, "-12": 6.801527419510128e-09, "-13": 7.223378136967252e-10, "-14": 7.07169714604719e-11, "-15": 5.716558699282823e-12, "-2": 0.09660928086423431, "-3": 0.038389763289866104, "-4": 0.012122777062026812, "-5": 0.003160666527768615, "-6": 0.0006998749517065033, "-7": 0.00013447645608959685, "-8": 2.2799067567259587e-05, "-9": 3.4563976112848487e-06, "0": 0.26059139587115104, "1": 0.19629591163467094, "10": 2.3137036860411967e-06, "11": 3.4028963120297426e-07, "12": 4.599488387970455e-08, "13": 5.7475170718584565e-09, "14": 6.620646787181068e-10, "15": 6.297211485791993e-11, "2": 0.12845572445165926, "3": 0.060060216547634, "4": 0.022315695357359593, "5": 0.006845794034744483, "6": 0.0017836204702438656, "7": 0.0004032413861258384, "8": 8.044013210554957e-05, "9": 1.4348821462300569e-05} |
| Raw goal margin distribution | {"-1": 0.16798650703251586, "-10": 4.626003472283935e-07, "-11": 5.782426032188615e-08, "-12": 6.642538047704391e-09, "-13": 7.054527777117579e-10, "-14": 6.906392411168765e-11, "-15": 5.582931056485634e-12, "-2": 0.09435098681823093, "-3": 0.03749238186761105, "-4": 0.01183940060983404, "-5": 0.0030867842429900677, "-6": 0.0006835149972358057, "-7": 0.0001313329963992018, "-8": 2.226612706629544e-05, "-9": 3.375602452927816e-06, "0": 0.26112174541531374, "1": 0.19960799415378358, "10": 2.3527425914831285e-06, "11": 3.46031306256504e-07, "12": 4.677095124452114e-08, "13": 5.8444943887239886e-09, "14": 6.732356339898867e-10, "15": 6.403463744983536e-11, "2": 0.13062314585077692, "3": 0.061073606952278606, "4": 0.022692225993578407, "5": 0.006961302475868421, "6": 0.0018137153312678725, "7": 0.0004100452402400076, "8": 8.179739091528857e-05, "9": 1.4590927781985936e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 63.7% |
| Raw p btts yes | 61.9% |
| P home draw | 67.7% |
| P draw away | 58.4% |
| P home away | 73.9% |
| Raw p home draw | 68.4% |
| Raw p draw away | 57.7% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.0, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.55, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.21, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.23, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:04Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.18, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.23 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0140 |
| Raw ev home | 0.0243 |
| Raw edge prob draw | 0.0011 |
| Raw ev draw | -0.0521 |
| Raw edge prob away | -0.0151 |
| Raw ev away | -0.0974 |
| Market p home draw | 66.2% |
| Market reference home draw last update utc | 2026-10-24T14:50:11Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.4% |
| Market reference draw away last update utc | 2026-10-24T14:50:11Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.4% |
| Market reference home away last update utc | 2026-10-24T14:50:11Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.82 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.2% |
| Market under 3 5 odds | 1.54 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.6% |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.44 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,433.5693 |
| Elo away rating | 1,444.5118 |
| Elo rating diff | 49.0575 |
| Elo home expectancy | 0.5701 |

</details>


---

## 2026-10-25 — NEC Nijmegen vs Groningen

The model's most likely 1X2 outcome is **NEC Nijmegen win** at **46.3%**. Expected goals are 1.97 for NEC Nijmegen and 1.35 for Groningen (3.32 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 64.2%; Under 3.5 goals: 57.8%; Double Chance 1X: 70.5%; Double Chance X2: 53.7%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NEC Nijmegen win | 46.3% | 2.16 |
| Draw | 24.2% | 4.13 |
| Groningen win | 29.5% | 3.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| NEC Nijmegen expected goals | 1.97 |
| Groningen expected goals | 1.35 |
| Expected total goals | 3.32 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.2% |
| Under 2.5 | 35.8% |
| Over 3.5 | 42.2% |
| Under 3.5 | 57.8% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.76% |
| 2 | 2-1 | 8.62% |
| 3 | 1-2 | 7.56% |
| 4 | 2-2 | 6.51% |
| 5 | 2-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NEC Nijmegen win | 46.3% | 41.8% | 2.26 | +4.6% |
| Draw | 24.2% | 24.6% | 4.00 | -3.2% |
| Groningen win | 29.5% | 33.6% | 2.88 | -15.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:30:00+00:00 |
| Fixture id | c655584661b81e424d8979da8b040c46 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nijmegen |
| Matched away-team name | Groningen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9675 |
| Dc lambda away | 1.3550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.50 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.18 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.1632953193375047, "-10": 3.059956877712258e-07, "-11": 3.695793274950327e-08, "-12": 4.103905085040791e-09, "-13": 4.2162820982200987e-10, "-14": 4.027446835768189e-11, "-15": 3.5589619500654413e-12, "-16": 2.583448092782346e-13, "-2": 0.08625624374667265, "-3": 0.03252372964164985, "-4": 0.009810468944599882, "-5": 0.0024530412507657194, "-6": 0.0005222676462916022, "-7": 9.665171372800525e-05, "-8": 1.5801278336756306e-05, "-9": 2.312004326585402e-06, "0": 0.2421103059275875, "1": 0.19012079136141247, "10": 1.0012512160336277e-05, "11": 1.7560398053692594e-06, "12": 2.831541480077081e-07, "13": 4.2242947714939505e-08, "14": 5.859402154498424e-09, "15": 7.518752169779379e-10, "16": 7.925398350203675e-11, "2": 0.14276666422704198, "3": 0.07816917848095571, "4": 0.03423922357146762, "5": 0.012431911988168917, "6": 0.003843484492850389, "7": 0.0010328577302676474, "8": 0.00024520092462189483, "9": 5.2097568911870595e-05} |
| Raw goal margin distribution | {"-1": 0.1406147892007508, "-10": 2.634951161298067e-07, "-11": 3.1824745154672336e-08, "-12": 3.5339025685126416e-09, "-13": 3.630671233305529e-10, "-14": 3.468063813012832e-11, "-15": 3.064648064698118e-12, "-16": 2.2246259748991917e-13, "-2": 0.07427587992659172, "-3": 0.028006420552266435, "-4": 0.008447866284239477, "-5": 0.0021123316931347296, "-6": 0.0004497284753023474, "-7": 8.322749486569853e-05, "-8": 1.3606595899010966e-05, "-9": 1.9908837701716204e-06, "0": 0.23816343093353182, "1": 0.20856838413998902, "10": 1.0984035294138663e-05, "11": 1.92642993998027e-06, "12": 3.106288517400384e-07, "13": 4.634181923567983e-08, "14": 6.427945258585459e-09, "15": 8.248303510471307e-10, "16": 8.694406938510203e-11, "2": 0.15661944311122863, "3": 0.08575400474917425, "4": 0.03756148648115836, "5": 0.01363819168106626, "6": 0.00421642127828641, "7": 0.001133076852383345, "8": 0.0002689929926748644, "9": 5.715264326306584e-05} |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.8% |
| P home draw | 70.5% |
| P draw away | 53.7% |
| P home away | 75.8% |
| Raw p home draw | 74.6% |
| Raw p draw away | 49.2% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.7, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.23, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.66, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.89, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.17, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 3.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.18 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +4.5% |
| Draw probability edge | -0.4% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0898 |
| Raw ev home | 0.1477 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.0473 |
| Raw edge prob away | -0.0819 |
| Raw ev away | -0.2685 |
| Market p home draw | 65.7% |
| Market reference home draw last update utc | 2026-10-24T14:50:11Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.8% |
| Market reference draw away last update utc | 2026-10-24T14:50:11Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.6% |
| Market reference home away last update utc | 2026-10-24T14:50:11Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.45 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 88.0% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 6.54 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 53.4% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 70.4% |
| Market reference btts yes odds | 1.36 |
| Market reference btts yes opposite odds | 2.90 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,487.2038 |
| Elo away rating | 1,481.0181 |
| Elo rating diff | 66.1857 |
| Elo home expectancy | 0.5941 |

</details>


---

## 2026-10-25 — PSV Eindhoven vs Feyenoord

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **50.2%**. Expected goals are 2.34 for PSV Eindhoven and 1.69 for Feyenoord (4.03 combined). The most likely exact score is 1-1 at 8.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 76.3%; Under 3.5 goals: 42.8%; Double Chance 1X: 72.3%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 62.5%; BTTS Yes (both teams score): 74.7%; BTTS No (at least one team does not score): 25.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 50.2% | 1.99 |
| Draw | 22.1% | 4.52 |
| Feyenoord win | 27.7% | 3.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| PSV Eindhoven expected goals | 2.34 |
| Feyenoord expected goals | 1.69 |
| Expected total goals | 4.03 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.3% |
| Under 2.5 | 23.7% |
| Over 3.5 | 57.2% |
| Under 3.5 | 42.8% |
| Over 4.5 | 37.5% |
| Under 4.5 | 62.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.10% |
| 2 | 2-1 | 7.95% |
| 3 | 2-2 | 7.29% |
| 4 | 3-1 | 6.22% |
| 5 | 1-2 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 50.2% | 48.5% | 2.07 | +3.9% |
| Draw | 22.1% | 23.2% | 4.24 | -6.1% |
| Feyenoord win | 27.7% | 28.3% | 3.12 | -13.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:30:00+00:00 |
| Fixture id | 9b70765a6abd2b34bae75afa9d3acedb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV Eindhoven |
| Matched away-team name | Feyenoord |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3447 |
| Dc lambda away | 1.6903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 74.7% |
| P btts no | 25.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.48 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.10 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.23 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.34 |
| Fair Over 4.5 odds | 2.67 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.14011280059546008, "-10": 1.3529214883410115e-06, "-11": 2.0197681959503563e-07, "-12": 2.7759509657202105e-08, "-13": 3.5338101786708157e-09, "-14": 4.1887462979243223e-10, "-15": 4.644130901172502e-11, "-16": 4.829864826321953e-12, "-17": 4.654961665803856e-13, "-18": 3.5824680961066605e-14, "-2": 0.08214900767374535, "-3": 0.03614148240285766, "-4": 0.012978895173949519, "-5": 0.0039127190222387, "-6": 0.0010127292665815845, "-7": 0.0002291406843467663, "-8": 4.598634255463451e-05, "-9": 8.284241427528042e-06, "0": 0.22140374192960452, "1": 0.1866865198854231, "10": 3.379101741069798e-05, "11": 6.997646818292501e-06, "12": 1.3340868297909986e-06, "13": 2.3557941559973667e-07, "14": 3.873468211850242e-08, "15": 5.957200373815714e-09, "16": 8.593984150810541e-10, "17": 1.1489403912628273e-10, "18": 1.226550789826286e-11, "2": 0.14967748028079414, "3": 0.09134439846247576, "4": 0.045502525267462963, "5": 0.01902822389468434, "6": 0.006831794090904299, "7": 0.0021442006822722515, "8": 0.0005969169490741297, "9": 0.00014916248295305723} |
| Raw goal margin distribution | {"-1": 0.1370563569865268, "-10": 1.3234086371321668e-06, "-11": 1.9757086413072154e-07, "-12": 2.71539591613281e-08, "-13": 3.4567230639326946e-09, "-14": 4.0973722992794873e-10, "-15": 4.542823068115041e-11, "-16": 4.724505362963245e-12, "-17": 4.553417568670618e-13, "-18": 3.504319549578305e-14, "-2": 0.08035699574894221, "-3": 0.03535308617897141, "-4": 0.012695771426248784, "-5": 0.0038273663278506867, "-6": 0.000990637424285462, "-7": 0.0002241421718822245, "-8": 4.4983188936963676e-05, "-9": 8.103527626516143e-06, "0": 0.21085867433517377, "1": 0.1928518551756211, "10": 3.4906968108486634e-05, "11": 7.228744590663206e-06, "12": 1.3781451400372174e-06, "13": 2.43359442167979e-07, "14": 4.00138976867522e-08, "15": 6.15393733006734e-09, "16": 8.877801074501193e-10, "17": 1.186884227512676e-10, "18": 1.2670577148810644e-11, "2": 0.15462058946666069, "3": 0.09436105356830907, "4": 0.04700524932593699, "5": 0.019656632310887545, "6": 0.0070574145654295605, "7": 0.0022150130587833853, "8": 0.0006166301727911005, "9": 0.0001540885843163933} |
| Unadjusted home-win probability | 51.9% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 27.1% |
| Raw p over 1 5 | 91.8% |
| Raw p under 3 5 | 42.7% |
| Raw p btts yes | 74.4% |
| P home draw | 72.3% |
| P draw away | 49.8% |
| P home away | 77.9% |
| Raw p home draw | 72.9% |
| Raw p draw away | 48.1% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.8, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.69, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.8, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.05, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.09, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:03Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.79, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.91 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.52 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +1.7% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0332 |
| Raw ev home | 0.0735 |
| Raw edge prob draw | -0.0211 |
| Raw ev draw | -0.1060 |
| Raw edge prob away | -0.0121 |
| Raw ev away | -0.1559 |
| Market p home draw | 70.5% |
| Market reference home draw last update utc | 2026-10-24T14:50:11Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.0% |
| Market reference draw away last update utc | 2026-10-24T14:50:11Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market reference home away last update utc | 2026-10-24T14:50:11Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.83 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 92.1% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-10-24T14:49:48Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.6% |
| Market under 3 5 odds | 2.10 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 2.10 |
| Market reference under 3 5 opposite odds | 1.78 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 75.9% |
| Market reference btts yes odds | 1.27 |
| Market reference btts yes opposite odds | 3.42 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,681.3663 |
| Elo away rating | 1,658.8042 |
| Elo rating diff | 82.5621 |
| Elo home expectancy | 0.6166 |

</details>


---

## 2026-10-25 — Sparta Rotterdam vs Ajax

The model's most likely 1X2 outcome is **Ajax win** at **63.4%**. Expected goals are 1.13 for Sparta Rotterdam and 2.02 for Ajax (3.15 combined). The most likely exact score is 1-2 at 11.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 62.5%; Under 3.5 goals: 60.6%; Double Chance 1X: 36.6%; Double Chance X2: 83.3%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 58.7%; BTTS No (at least one team does not score): 41.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sparta Rotterdam win | 16.7% | 5.98 |
| Draw | 19.9% | 5.04 |
| Ajax win | 63.4% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sparta Rotterdam expected goals | 1.13 |
| Ajax expected goals | 2.02 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.7% |
| Under 1.5 | 16.3% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 39.4% |
| Under 3.5 | 60.6% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.02% |
| 2 | 0-2 | 9.73% |
| 3 | 1-1 | 9.19% |
| 4 | 0-1 | 8.54% |
| 5 | 1-3 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Rotterdam win | 16.7% | 13.6% | 6.10 | +2.0% |
| Draw | 19.9% | 16.4% | 5.22 | +3.6% |
| Ajax win | 63.4% | 70.0% | 1.43 | -9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:45:00+00:00 |
| Fixture id | 6a5709e9c094b7f5d089026af10fb820 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:09Z |
| Market best draw last update utc | 2026-10-24T14:50:09Z |
| Market best away last update utc | 2026-10-24T14:50:09Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sparta Rotterdam |
| Matched away-team name | Ajax |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1329 |
| Dc lambda away | 2.0177 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.7% |
| P btts no | 41.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.26 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.14 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.57 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.24658602493454476, "-10": 1.8095885617385127e-05, "-11": 3.263544685355648e-06, "-12": 5.409050362636542e-07, "-13": 8.292157982335201e-08, "-14": 1.1823035823426565e-08, "-15": 1.5749111188920994e-09, "-16": 1.955011718716119e-10, "-17": 2.045336067491383e-11, "-2": 0.19612743733627974, "-3": 0.11253596142381081, "-4": 0.05129841844360869, "-5": 0.01930318634294331, "-6": 0.006168365867444901, "-7": 0.0017102612146005722, "-8": 0.00041838574129356544, "-9": 9.151883964289766e-05, "0": 0.19852268415457383, "1": 0.10074965123268864, "10": 4.248808807580226e-08, "11": 4.302393099060961e-09, "12": 4.003821693344492e-10, "13": 3.4463108664746504e-11, "14": 2.7589832617349164e-12, "15": 2.0635228762715855e-13, "16": 1.4382546346877062e-14, "17": 8.448590732324753e-16, "2": 0.04661871216346832, "3": 0.01501918692165202, "4": 0.0038440785286770265, "5": 0.0008121765705208555, "6": 0.00014572187732513666, "7": 2.268559934394795e-05, "8": 3.116002980968624e-06, "9": 3.827054728397179e-07} |
| Raw goal margin distribution | {"-1": 0.22098507768704398, "-10": 1.621714243552615e-05, "-11": 2.9247183656084963e-06, "-12": 4.847474283742003e-07, "-13": 7.431253155591446e-08, "-14": 1.0595549730079627e-08, "-15": 1.4114013803131936e-09, "-16": 1.7520393406489406e-10, "-17": 1.8329860740918912e-11, "-2": 0.17576517966832622, "-3": 0.10085230168428372, "-4": 0.04597253631057356, "-5": 0.017299099309196993, "-6": 0.005527956463799016, "-7": 0.0015326992171351512, "-8": 0.00037494827846570937, "-9": 8.201721039820614e-05, "0": 0.23283435495432964, "1": 0.11975191822654954, "10": 5.0501713768762645e-08, "11": 5.11386213523739e-09, "12": 4.758977546311449e-10, "13": 4.0963152925678653e-11, "14": 3.2793516791897444e-12, "15": 2.452721371383895e-13, "16": 1.7095220608187685e-14, "17": 1.0042068971239044e-15, "2": 0.05541140975201098, "3": 0.017851937173628447, "4": 0.004569105421113441, "5": 0.0009653601880358331, "6": 0.0001732063002079869, "7": 2.6964302152098116e-05, "8": 3.703708445688098e-06, "9": 4.5488707829377803e-07} |
| Unadjusted home-win probability | 19.9% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 56.8% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 61.4% |
| Raw p btts yes | 59.8% |
| P home draw | 36.6% |
| P draw away | 83.3% |
| P home away | 80.1% |
| Raw p home draw | 43.2% |
| Raw p draw away | 80.1% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.15, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.31, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:23Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.75, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:49:02Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:09Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 5.60 |
| Reference draw odds | 4.75 |
| Reference away odds | 1.36 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.14 |
| Market reference over 2 5 last update utc | 2026-10-24T14:49:26Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:49:26Z |
| Home probability edge | +3.2% |
| Draw probability edge | +3.4% |
| Away probability edge | -6.6% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0631 |
| Raw ev home | 0.2124 |
| Raw edge prob draw | 0.0686 |
| Raw ev draw | 0.2154 |
| Raw edge prob away | -0.1317 |
| Raw ev away | -0.1872 |
| Market p home draw | 34.9% |
| Market reference home draw last update utc | 2026-10-24T14:50:14Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.0% |
| Market reference draw away last update utc | 2026-10-24T14:50:14Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.1% |
| Market reference home away last update utc | 2026-10-24T14:50:14Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.11 |
| Market reference dc home draw odds | 2.67 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 89.6% |
| Market over 1 5 odds | 1.10 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.18 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:09Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.88 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:09Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.1% |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.53 |
| Market reference btts yes last update utc | 2026-10-24T14:50:11Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,400.1683 |
| Elo away rating | 1,618.3103 |
| Elo rating diff | -158.1420 |
| Elo home expectancy | 0.2869 |

</details>


---
