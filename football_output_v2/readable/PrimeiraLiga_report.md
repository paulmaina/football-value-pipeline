# Primeira Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,602 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 9aa0490d3c785bbac1db1df68144a198798f6e850afaca727c2a89dab1ac3be4 |
| Training as of utc | 2026-10-24T14:50:19.997502+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 1992.111 |
| Base scoring parameter | 0.085 |
| Home-advantage parameter | 0.186 |
| Dixon-Coles low-score adjustment | 0.045 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 36.00 |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Alverca vs Arouca

The model's most likely 1X2 outcome is **Alverca win** at **44.3%**. Expected goals are 1.46 for Alverca and 1.28 for Arouca (2.74 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.5%; Double Chance 1X: 69.8%; Double Chance X2: 55.7%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 44.3% | 2.26 |
| Draw | 25.6% | 3.91 |
| Arouca win | 30.2% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.46 |
| Arouca expected goals | 1.28 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.5% |
| Under 3.5 | 70.5% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.08% |
| 2 | 1-0 | 10.54% |
| 3 | 2-1 | 9.29% |
| 4 | 0-1 | 7.91% |
| 5 | 2-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 44.3% | 46.5% | 2.09 | -7.5% |
| Draw | 25.6% | 26.7% | 3.29 | -15.9% |
| Arouca win | 30.2% | 26.7% | 3.97 | +19.8% |
| Over 2.5 | 51.3% | 49.6% | 1.95 | -0.1% |
| Under 2.5 | 48.7% | 50.4% | 1.93 | -5.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T17:00:00+00:00 |
| Fixture id | 3f752f1b9f725906b91ae5b699705cca |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:07Z |
| Market best draw last update utc | 2026-10-24T14:50:07Z |
| Market best away last update utc | 2026-10-24T14:50:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Alverca |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4600 |
| Dc lambda away | 1.2778 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.11 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.39 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.06 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.17350150024803188, "-10": 2.1981344241141735e-07, "-11": 2.5183287322117045e-08, "-12": 2.6502743415068444e-09, "-13": 2.5781646501465414e-10, "-14": 2.317798440073486e-11, "-15": 1.7560954472844672e-12, "-2": 0.08468817072821817, "-3": 0.031562544730206823, "-4": 0.009267128256691728, "-5": 0.002235111325769088, "-6": 0.00045638323800317027, "-7": 8.0690266828992e-05, "-8": 1.256943536105392e-05, "-9": 1.7489731273852038e-06, "0": 0.25562677003642875, "1": 0.23215337133303512, "10": 9.793934264061275e-07, "11": 1.2820154793890735e-07, "12": 1.5415215198311653e-08, "13": 1.7133548596243705e-09, "14": 1.7599091488189442e-10, "15": 1.523493519151039e-11, "2": 0.1299278937214581, "3": 0.05532603769120291, "4": 0.018560114127951433, "5": 0.005114610187525534, "6": 0.0011932212438501312, "7": 0.0002410406859262416, "8": 4.2900552294342454e-05, "9": 6.820373564290408e-06} |
| Raw goal margin distribution | {"-1": 0.19335614734430423, "-10": 2.449677973873478e-07, "-11": 2.8065137229984547e-08, "-12": 2.953558530310399e-09, "-13": 2.873196965207602e-10, "-14": 2.5830357435098387e-11, "-15": 1.9570542593025734e-12, "-2": 0.09437946296853822, "-3": 0.03517440506676132, "-4": 0.010327612234464108, "-5": 0.002490886327890605, "-6": 0.0005086094615127841, "-7": 8.992405886942632e-05, "-8": 1.4007818907803474e-05, "-9": 1.9491168966059597e-06, "0": 0.2439846305086171, "1": 0.2201435276128953, "10": 9.28727084908996e-07, "11": 1.2156937823753548e-07, "12": 1.461774960743525e-08, "13": 1.6247189549072602e-09, "14": 1.6688648804648183e-10, "15": 1.4446795912352472e-11, "2": 0.12320641606415901, "3": 0.052463890729861906, "4": 0.017599955467214646, "5": 0.004850019289323591, "6": 0.0011314930829369161, "7": 0.00022857108037389892, "8": 4.06812051205139e-05, "9": 6.4675394867589845e-06} |
| Unadjusted home-win probability | 42.0% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.8% |
| P home draw | 69.8% |
| P draw away | 55.7% |
| P home away | 74.4% |
| Raw p home draw | 66.4% |
| Raw p draw away | 58.0% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.98 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market best over 2 5 last update utc | 2026-10-24T14:50:07Z |
| Market best under 2 5 last update utc | 2026-10-24T14:50:07Z |
| Home probability edge | -2.3% |
| Draw probability edge | -1.2% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | +1.7% |
| Under 2.5 probability edge | -1.7% |
| Raw edge prob home | -0.0458 |
| Raw ev home | -0.1229 |
| Raw edge prob draw | -0.0233 |
| Raw ev draw | -0.1973 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.3353 |
| Market p home draw | 74.8% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.4% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.25 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 76.0% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.77 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.9% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.27 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.18 |
| Market reference btts yes last update utc | 2026-10-24T14:50:08Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,429.4069 |
| Elo away rating | 1,475.9199 |
| Elo rating diff | 13.4870 |
| Elo home expectancy | 0.5194 |

</details>


---

## 2026-10-24 — Gil Vicente vs FC Porto

The model's most likely 1X2 outcome is **FC Porto win** at **64.9%**. Expected goals are 0.68 for Gil Vicente and 1.65 for FC Porto (2.33 combined). The most likely exact score is 0-1 at 17.5%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 42.2%; Under 3.5 goals: 78.9%; Double Chance 1X: 35.1%; Double Chance X2: 85.9%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 38.9%; BTTS No (at least one team does not score): 61.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gil Vicente win | 14.1% | 7.11 |
| Draw | 21.1% | 4.75 |
| FC Porto win | 64.9% | 1.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gil Vicente expected goals | 0.68 |
| FC Porto expected goals | 1.65 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 42.2% |
| Under 2.5 | 57.8% |
| Over 3.5 | 21.1% |
| Under 3.5 | 78.9% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.53% |
| 2 | 0-2 | 13.99% |
| 3 | 1-2 | 9.58% |
| 4 | 1-1 | 9.51% |
| 5 | 0-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gil Vicente win | 14.1% | 12.4% | 7.85 | +10.4% |
| Draw | 21.1% | 18.9% | 4.73 | -0.3% |
| FC Porto win | 64.9% | 68.7% | 1.43 | -7.2% |
| Over 2.5 | 42.2% | 50.4% | 1.93 | -18.6% |
| Under 2.5 | 57.8% | 49.6% | 1.96 | +13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:30:00+00:00 |
| Fixture id | 2fdd5b6eaa94bcdf2f61444eef54b645 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:07Z |
| Market best draw last update utc | 2026-10-24T14:50:07Z |
| Market best away last update utc | 2026-10-24T14:50:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Gil Vicente |
| Matched away-team name | Porto |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6850 |
| Dc lambda away | 1.6458 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 38.9% |
| P btts no | 61.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.93 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.74 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.07 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.2909251435022041, "-10": 4.597637370975073e-06, "-11": 6.821170720546488e-07, "-12": 9.28865840363243e-08, "-13": 1.1686856851739818e-08, "-14": 1.363251894111232e-09, "-15": 1.3912234509196306e-10, "-2": 0.20049074493578387, "-3": 0.10099241154841453, "-4": 0.03941094906128623, "-5": 0.01251449934500929, "-6": 0.0033447483758704947, "-7": 0.0007711234268314532, "-8": 0.0001562257389058172, "-9": 2.8219019284917767e-05, "0": 0.21070703823278736, "1": 0.10424106993231166, "10": 6.019647914333257e-10, "11": 3.716976608310704e-11, "12": 2.1065823112768804e-12, "13": 1.1031071476052764e-13, "14": 5.3553839967793325e-15, "15": 2.2746046833349053e-16, "2": 0.029159122107263815, "3": 0.006113126605719072, "4": 0.0009928555632801187, "5": 0.0001312130990209801, "6": 1.4595591408013387e-05, "7": 1.4004792401585528e-06, "8": 1.1808640421041644e-07, "9": 8.877358525328918e-09} |
| Raw goal margin distribution | {"-1": 0.27377185430507994, "-10": 4.326555255148105e-06, "-11": 6.418986458904615e-07, "-12": 8.740988161271276e-08, "-13": 1.0997786003582731e-08, "-14": 1.282872956399923e-09, "-15": 1.3091952772658645e-10, "-2": 0.18866957441806853, "-3": 0.09503777998528935, "-4": 0.0370872330749564, "-5": 0.01177662972041103, "-6": 0.0031475380712118893, "-7": 0.0007256570811320579, "-8": 0.00014701448529182487, "-9": 2.6555192663312085e-05, "0": 0.23196486242831935, "1": 0.11683026206365965, "10": 6.746640684129447e-10, "11": 4.165875806104194e-11, "12": 2.3609942189288683e-12, "13": 1.2363293778805762e-13, "14": 6.0021536252605056e-15, "15": 2.549308649822983e-16, "2": 0.032680668757045415, "3": 0.006851408795384103, "4": 0.0011127627117094993, "5": 0.0001470597026177902, "6": 1.635830071851305e-05, "7": 1.5696150926758839e-06, "8": 1.323476971122475e-07, "9": 9.949476953955903e-09} |
| Unadjusted home-win probability | 15.8% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 61.0% |
| Raw p over 1 5 | 67.1% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 39.5% |
| P home draw | 35.1% |
| P draw away | 85.9% |
| P home away | 78.9% |
| Raw p home draw | 39.0% |
| Raw p draw away | 84.2% |
| Raw p home away | 76.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.31, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 6.25 |
| Reference draw odds | 4.30 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market best over 2 5 last update utc | 2026-10-24T14:50:07Z |
| Market best under 2 5 last update utc | 2026-10-24T14:50:07Z |
| Home probability edge | +1.7% |
| Draw probability edge | +2.1% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | 0.0340 |
| Raw ev home | 0.2375 |
| Raw edge prob draw | 0.0425 |
| Raw ev draw | 0.0972 |
| Raw edge prob away | -0.0765 |
| Raw ev away | -0.1271 |
| Market p home draw | 34.0% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 87.1% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.74 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 74.8% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.62 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.34 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.36 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.3% |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.80 |
| Market reference btts yes last update utc | 2026-10-24T14:50:08Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,473.4882 |
| Elo away rating | 1,682.6975 |
| Elo rating diff | -149.2093 |
| Elo home expectancy | 0.2976 |

</details>


---

## 2026-10-25 — Estoril vs Moreirense FC

The model's most likely 1X2 outcome is **Estoril win** at **47.5%**. Expected goals are 1.52 for Estoril and 1.18 for Moreirense FC (2.70 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.3%; Double Chance 1X: 72.2%; Double Chance X2: 52.5%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Estoril win | 47.5% | 2.11 |
| Draw | 24.7% | 4.04 |
| Moreirense FC win | 27.8% | 3.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Estoril expected goals | 1.52 |
| Moreirense FC expected goals | 1.18 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.7% |
| Under 3.5 | 71.3% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 1-0 | 11.17% |
| 3 | 2-1 | 9.51% |
| 4 | 2-0 | 8.08% |
| 5 | 0-1 | 7.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Estoril win | 47.5% | 49.1% | 1.95 | -7.4% |
| Draw | 24.7% | 25.2% | 3.56 | -11.9% |
| Moreirense FC win | 27.8% | 25.6% | 3.85 | +6.9% |
| Over 2.5 | 50.6% | 48.5% | 1.94 | -1.9% |
| Under 2.5 | 49.4% | 51.5% | 1.91 | -5.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:30:00+00:00 |
| Fixture id | 399511b408ef714458e62100cac3fb16 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:07Z |
| Market best draw last update utc | 2026-10-24T14:50:07Z |
| Market best away last update utc | 2026-10-24T14:50:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Estoril |
| Matched away-team name | Moreirense |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5239 |
| Dc lambda away | 1.1763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.89 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.49 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.30 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1671600671980033, "-10": 1.0259315615094802e-07, "-11": 1.0825819390498748e-08, "-12": 1.0492751536127293e-09, "-13": 9.400359864450303e-11, "-14": 7.785916178782553e-12, "-15": 5.454057021265271e-13, "-2": 0.07551593394324672, "-3": 0.026026370094407062, "-4": 0.0070557849398798665, "-5": 0.0015699025862785832, "-6": 0.00029555403391348585, "-7": 4.816191345601822e-05, "-8": 6.912962139769299e-06, "-9": 8.861732154358717e-07, "0": 0.24749358341306177, "1": 0.23985701115246955, "10": 1.5233089148998033e-06, "11": 2.0823692656954078e-07, "12": 2.6146510218023295e-08, "13": 3.0345632700187334e-09, "14": 3.2560331355504945e-10, "15": 2.9547867360657856e-11, "2": 0.14134784559220595, "3": 0.0631090396410057, "4": 0.022164129550364023, "5": 0.006388595990154497, "6": 0.0015581059484560276, "7": 0.00032892069709771675, "8": 6.116162591593679e-05, "9": 1.0156892076502238e-05} |
| Raw goal margin distribution | {"-1": 0.17994492988107946, "-10": 1.1043976351118318e-07, "-11": 1.165380789672114e-08, "-12": 1.1295266094811478e-09, "-13": 1.011932529712233e-10, "-14": 8.381404508478948e-12, "-15": 5.871198335284657e-13, "-2": 0.08129160071601169, "-3": 0.028016938615785893, "-4": 0.007595430819962155, "-5": 0.0016899730632041726, "-6": 0.00031815882106362104, "-7": 5.1845469345954756e-05, "-8": 7.441684538436236e-06, "-9": 9.539501855141839e-07, "0": 0.24278626366517064, "1": 0.23150674510900188, "10": 1.4702771746780686e-06, "11": 2.009874668661328e-07, "12": 2.5236258250070796e-08, "13": 2.928919451192507e-09, "14": 3.1426791718804064e-10, "15": 2.8519202189299796e-11, "2": 0.13642703002090026, "3": 0.06091199204077875, "4": 0.02139251825796042, "5": 0.006166186497491761, "6": 0.0015038628011283604, "7": 0.00031746981094362027, "8": 5.903237463578775e-05, "9": 9.803294945419548e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 53.5% |
| P home draw | 72.2% |
| P draw away | 52.5% |
| P home away | 75.3% |
| Raw p home draw | 70.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.72, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.35, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.97, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.84, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.40 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market best over 2 5 last update utc | 2026-10-24T14:50:07Z |
| Market best under 2 5 last update utc | 2026-10-24T14:50:07Z |
| Home probability edge | -1.7% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +2.0% |
| Under 2.5 probability edge | -2.0% |
| Raw edge prob home | -0.0331 |
| Raw ev home | -0.1063 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.1357 |
| Raw edge prob away | 0.0425 |
| Raw ev away | 0.1508 |
| Market p home draw | 75.4% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.3% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.3% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 1.86 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.69 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.2% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.1% |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-24T14:49:45Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,397.5496 |
| Elo away rating | 1,419.4582 |
| Elo rating diff | 38.0914 |
| Elo home expectancy | 0.5546 |

</details>


---

## 2026-10-25 — Nacional vs Braga

The model's most likely 1X2 outcome is **Braga win** at **60.2%**. Expected goals are 0.96 for Nacional and 1.81 for Braga (2.76 combined). The most likely exact score is 0-1 at 12.4%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.7%; Double Chance 1X: 39.8%; Double Chance X2: 81.8%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 18.2% | 5.50 |
| Draw | 21.6% | 4.63 |
| Braga win | 60.2% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.96 |
| Braga expected goals | 1.81 |
| Expected total goals | 2.76 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 76.1% |
| Under 1.5 | 23.9% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.38% |
| 2 | 0-2 | 10.71% |
| 3 | 1-2 | 10.27% |
| 4 | 1-1 | 10.24% |
| 5 | 0-3 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 18.2% | 16.1% | 5.78 | +5.0% |
| Draw | 21.6% | 21.2% | 4.12 | -11.1% |
| Braga win | 60.2% | 62.7% | 1.56 | -6.0% |
| Over 2.5 | 52.5% | 51.5% | 1.86 | -2.3% |
| Under 2.5 | 47.5% | 48.5% | 1.99 | -5.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T18:00:00+00:00 |
| Fixture id | 070aa87111dbdfdcb504340fe440e63f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:07Z |
| Market best draw last update utc | 2026-10-24T14:50:07Z |
| Market best away last update utc | 2026-10-24T14:50:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Sp Braga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 0.9589 |
| Dc lambda away | 1.8056 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.52 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.18 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.74 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.2607881972455503, "-10": 7.798719558806623e-06, "-11": 1.2637463948754499e-06, "-12": 1.880863523826507e-07, "-13": 2.587976703570898e-08, "-14": 3.3100748369198995e-09, "-15": 3.9366904499719563e-10, "-16": 4.0087960801057046e-11, "-2": 0.183964393790294, "-3": 0.09769566622796706, "-4": 0.0407574396547207, "-5": 0.013944674972910898, "-6": 0.004035009373357701, "-7": 0.0010102994380263239, "-8": 0.00022277024305910324, "-9": 4.38623696344501e-05, "0": 0.2158404453391199, "1": 0.12112372459444365, "10": 1.1966119580418967e-08, "11": 1.0298023009588765e-09, "12": 8.13982570103695e-11, "13": 5.94815225916789e-12, "14": 4.0403912342181347e-13, "15": 2.5520005708431393e-14, "16": 1.3801533969476983e-15, "2": 0.044601828568472654, "3": 0.012579346569535273, "4": 0.0027871065427458085, "5": 0.0005064294649173986, "6": 7.782497873707966e-05, "7": 1.0348763622228579e-05, "8": 1.2118794681107757e-06, "9": 1.2672381314753967e-07} |
| Raw goal margin distribution | {"-1": 0.2500716777788434, "-10": 7.478248268886062e-06, "-11": 1.2118155061899015e-06, "-12": 1.8035735590957518e-07, "-13": 2.4816294723076362e-08, "-14": 3.174054565294228e-09, "-15": 3.774920782912211e-10, "-16": 3.8440633901900595e-11, "-2": 0.17640478017258737, "-3": 0.09368107691755001, "-4": 0.03908260198918904, "-5": 0.013371649113679263, "-6": 0.0038691995056004637, "-7": 0.0009687833966212063, "-8": 0.0002136159881060001, "-9": 4.205994167563839e-05, "0": 0.2196053169661203, "1": 0.135118460532529, "10": 1.3348694994874132e-08, "11": 1.148786515807016e-09, "12": 9.080307936449303e-11, "13": 6.635406721209085e-12, "14": 4.5072213998092564e-13, "15": 2.846860840558055e-14, "16": 1.5396174689864851e-15, "2": 0.049755160958650485, "3": 0.01403277474063679, "4": 0.003109131152108151, "5": 0.0005649427467415438, "6": 8.681694154584637e-05, "7": 1.1544468383320417e-05, "8": 1.3519010303751817e-06, "9": 1.4136558797741012e-07} |
| Unadjusted home-win probability | 20.3% |
| Unadjusted draw probability | 22.0% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 51.0% |
| P home draw | 39.8% |
| P draw away | 81.8% |
| P home away | 78.4% |
| Raw p home draw | 42.2% |
| Raw p draw away | 79.7% |
| Raw p home away | 78.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.45, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.54, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.90 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.50 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market best over 2 5 last update utc | 2026-10-24T14:50:07Z |
| Market best under 2 5 last update utc | 2026-10-24T14:50:07Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0420 |
| Raw ev home | 0.1715 |
| Raw edge prob draw | 0.0075 |
| Raw ev draw | -0.0952 |
| Raw edge prob away | -0.0495 |
| Raw ev away | -0.0988 |
| Market p home draw | 38.7% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.1% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.2% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.41 |
| Market reference dc draw away odds | 1.11 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 76.4% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.74 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.5% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.3% |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.80 |
| Market reference btts yes last update utc | 2026-10-24T14:49:45Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,367.2841 |
| Elo away rating | 1,563.4097 |
| Elo rating diff | -136.1256 |
| Elo home expectancy | 0.3135 |

</details>


---

## 2026-10-25 — Rio Ave FC vs Famalicão

The model's most likely 1X2 outcome is **Famalicão win** at **45.4%**. Expected goals are 1.03 for Rio Ave FC and 1.30 for Famalicão (2.32 combined). The most likely exact score is 0-1 at 14.0%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.4%; Double Chance 1X: 54.6%; Double Chance X2: 72.3%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rio Ave FC win | 27.7% | 3.62 |
| Draw | 26.9% | 3.72 |
| Famalicão win | 45.4% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rio Ave FC expected goals | 1.03 |
| Famalicão expected goals | 1.30 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.97% |
| 2 | 1-1 | 12.55% |
| 3 | 1-0 | 9.81% |
| 4 | 0-0 | 9.29% |
| 5 | 1-2 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rio Ave FC win | 27.7% | 25.3% | 3.82 | +5.6% |
| Draw | 26.9% | 27.1% | 3.31 | -10.9% |
| Famalicão win | 45.4% | 47.6% | 2.05 | -6.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T18:00:00+00:00 |
| Fixture id | fa1bd8d92c7780ff1ebb56219fcb6ea6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-24T14:50:07Z |
| Market best draw last update utc | 2026-10-24T14:50:07Z |
| Market best away last update utc | 2026-10-24T14:50:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rio Ave |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0260 |
| Dc lambda away | 1.2961 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.77 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.86 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.56 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.25041736067277204, "-10": 4.281807466085462e-07, "-11": 4.995195100985503e-08, "-12": 5.349236984092397e-09, "-13": 5.274566569590639e-10, "-14": 4.459505875890243e-11, "-2": 0.13181704716755083, "-3": 0.05157611652484844, "-4": 0.01571035275497857, "-5": 0.003904537675470425, "-6": 0.0008181281199880583, "-7": 0.00014802923618382861, "-8": 2.355371095751604e-05, "-9": 3.3431673620636935e-06, "0": 0.2690647342035142, "1": 0.17496406568379008, "10": 3.628460546297107e-08, "11": 3.3509004110654525e-09, "12": 2.8406301951430944e-10, "13": 2.2172947753493584e-11, "14": 1.484011244060758e-12, "2": 0.07243633807331883, "3": 0.022436098698231238, "4": 0.0054100145774596065, "5": 0.0010643780546086494, "6": 0.00017654743379456135, "7": 2.5287237214830766e-05, "8": 3.1851289604061453e-06, "9": 3.5788178366120523e-07} |
| Raw goal margin distribution | {"-1": 0.23845399708338216, "-10": 4.0772496854311014e-07, "-11": 4.7565561542588083e-08, "-12": 5.0936841470423605e-09, "-13": 5.022581014440129e-10, "-14": 4.246458784909954e-11, "-2": 0.1255196592456094, "-3": 0.04911213466329617, "-4": 0.014959811092769372, "-5": 0.0037180034681988964, "-6": 0.0007790431135179562, "-7": 0.000140957332025231, "-8": 2.2428463062134003e-05, "-9": 3.183451891119117e-06, "0": 0.2670260817481561, "1": 0.18999042621084045, "10": 3.94008199904373e-08, "11": 3.6386842909731742e-09, "12": 3.0845907665291537e-10, "13": 2.4077217099255093e-11, "14": 1.6114619173879005e-12, "2": 0.07865735566853256, "3": 0.024362968118775013, "4": 0.00587464043751721, "5": 0.001155789558583044, "6": 0.00019170977801624345, "7": 2.745896968822799e-05, "8": 3.458675965027711e-06, "9": 3.8861758467463196e-07} |
| Unadjusted home-win probability | 30.0% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 43.3% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 46.0% |
| P home draw | 54.6% |
| P draw away | 72.3% |
| P home away | 73.1% |
| Raw p home draw | 56.7% |
| Raw p draw away | 70.0% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.8, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.35 |
| Reference draw odds | 3.15 |
| Reference away odds | 1.92 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0475 |
| Raw ev home | 0.1470 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.1161 |
| Raw edge prob away | -0.0434 |
| Raw ev away | -0.1129 |
| Market p home draw | 52.6% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.5% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.24 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 72.7% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.30 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.68 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.7% |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-10-24T14:49:45Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,391.3818 |
| Elo away rating | 1,495.7667 |
| Elo rating diff | -44.3849 |
| Elo home expectancy | 0.4365 |

</details>


---

## 2026-10-25 — Sporting Lisbon vs Académico de Viseu

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **73.8%**. Expected goals are 1.93 for Sporting Lisbon and 0.72 for Académico de Viseu (2.65 combined). The most likely exact score is 1-0 at 15.7%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 51.5%; Under 3.5 goals: 71.5%; Double Chance 1X: 89.5%; Double Chance X2: 26.2%; Double Chance 12 (either team wins): 84.3%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 42.0%; BTTS No (at least one team does not score): 58.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 73.8% | 1.35 |
| Draw | 15.7% | 6.38 |
| Académico de Viseu win | 10.5% | 9.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 1.93 |
| Académico de Viseu expected goals | 0.72 |
| Expected total goals | 2.65 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 74.9% |
| Under 1.5 | 25.1% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 28.5% |
| Under 3.5 | 71.5% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.66% |
| 2 | 2-0 | 14.61% |
| 3 | 2-1 | 10.55% |
| 4 | 3-0 | 9.38% |
| 5 | 1-1 | 7.36% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:30:00+00:00 |
| Fixture id | 9b60d2e564e8761e9ec267bd7baf6998 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Porto |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 72/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9265 |
| Dc lambda away | 0.7222 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.27 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.98 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.51 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.26 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.07718694879415945, "-10": 6.563514905225482e-10, "-11": 4.2646131821012125e-11, "-12": 2.544021971018111e-12, "-13": 1.4026209277143117e-13, "-14": 7.187323345530814e-15, "-15": 3.429381186407416e-16, "-16": 1.4240789905255563e-17, "-2": 0.022030084490441745, "-3": 0.004783320602414157, "-4": 0.0008097082851027512, "-5": 0.00011192417341867343, "-6": 1.3049705423598968e-05, "-7": 1.3142897848181939e-06, "-8": 1.164293981166055e-07, "-9": 9.202149181615117e-09, "0": 0.1567983591439002, "1": 0.2896833121671795, "10": 1.7326616482380854e-05, "11": 3.0030930042579644e-06, "12": 4.778832906508088e-07, "13": 7.028346315903771e-08, "14": 9.607090291210273e-09, "15": 1.2227911883097784e-09, "16": 1.3545107911689118e-10, "2": 0.22682903499563467, "3": 0.13137835610974782, "4": 0.059324592886157344, "5": 0.021874691141323906, "6": 0.006803471860099375, "7": 0.001827817653406182, "8": 0.00043193285309472084, "9": 9.106567390135996e-05} |
| Raw goal margin distribution | {"-1": 0.10034322438764773, "-10": 8.532585614480801e-10, "-11": 5.544007687093371e-11, "-12": 3.3072348560601766e-12, "-13": 1.8234106760169996e-13, "-14": 9.343538130137211e-15, "-15": 4.458204026384512e-16, "-16": 1.8513062107573995e-17, "-2": 0.028639164338498925, "-3": 0.006218328616746937, "-4": 0.0010526227737965813, "-5": 0.0001455017023370375, "-6": 1.6964649334758745e-05, "-7": 1.7085799717268304e-06, "-8": 1.5135850558996745e-07, "-9": 1.1962816701588334e-08, "0": 0.20030098953829015, "1": 0.2602608686374891, "10": 1.5566793345868088e-05, "11": 2.6980760059671013e-06, "12": 4.293458238986974e-07, "13": 6.314493933314869e-08, "14": 8.63132102972571e-09, "15": 1.0985952019497346e-09, "16": 1.216936358712396e-10, "2": 0.20379055057923978, "3": 0.11803456963221755, "4": 0.053299135392397744, "5": 0.01965293090246145, "6": 0.006112459439977334, "7": 0.0016421705711231749, "8": 0.0003880624627580375, "9": 8.181635046670639e-05} |
| Unadjusted home-win probability | 66.3% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 43.5% |
| P home draw | 89.5% |
| P draw away | 26.2% |
| P home away | 84.3% |
| Raw p home draw | 86.4% |
| Raw p draw away | 33.7% |
| Raw p home away | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.85, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.18, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.19 |
| Reference draw odds | 6.25 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Home probability edge | -7.5% |
| Draw probability edge | +4.4% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -15.7% |
| Under 2.5 probability edge | +15.7% |
| Raw edge prob home | -0.1500 |
| Raw edge prob draw | 0.0870 |
| Raw edge prob away | 0.0630 |
| Market p home draw | 90.5% |
| Market reference home draw last update utc | 2026-10-24T14:49:57Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 25.5% |
| Market reference draw away last update utc | 2026-10-24T14:49:57Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.0% |
| Market reference home away last update utc | 2026-10-24T14:49:57Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 3.65 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 86.8% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.42 |
| Market reference over 1 5 last update utc | 2026-10-24T14:50:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.6% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.04 |
| Market reference under 3 5 last update utc | 2026-10-24T14:50:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.8% |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.83 |
| Market reference btts yes last update utc | 2026-10-24T14:49:45Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,691.2508 |
| Elo away rating | 1,431.9052 |
| Elo rating diff | 319.3457 |
| Elo home expectancy | 0.8627 |

</details>


---

## 2026-10-26 — Santa Clara vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **68.7%**. Expected goals are 0.70 for Santa Clara and 1.84 for Benfica (2.54 combined). The most likely exact score is 0-1 at 15.8%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 47.5%; Under 3.5 goals: 74.6%; Double Chance 1X: 31.3%; Double Chance X2: 87.6%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 88.3%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 12.4% | 8.09 |
| Draw | 19.0% | 5.27 |
| Benfica win | 68.7% | 1.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 0.70 |
| Benfica expected goals | 1.84 |
| Expected total goals | 2.54 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 72.1% |
| Under 1.5 | 27.9% |
| Over 2.5 | 47.5% |
| Under 2.5 | 52.5% |
| Over 3.5 | 25.4% |
| Under 3.5 | 74.6% |
| Over 4.5 | 11.7% |
| Under 4.5 | 88.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.84% |
| 2 | 0-2 | 14.13% |
| 3 | 1-2 | 9.83% |
| 4 | 1-1 | 8.79% |
| 5 | 0-3 | 8.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Over 2.5 | 47.5% | 51.5% | 1.83 | -13.1% |
| Under 2.5 | 52.5% | 48.5% | 1.85 | -2.8% |

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
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 14.00 |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Santa Clara |
| Matched away-team name | Benfica |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6957 |
| Dc lambda away | 1.8394 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.75 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.58 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.93 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.55 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.28006973440684946, "-10": 1.1454530443108196e-05, "-11": 1.8971315768077893e-06, "-12": 2.884441968436291e-07, "-13": 4.052864531968634e-08, "-14": 5.292301372723672e-09, "-15": 6.437549455986594e-10, "-16": 6.85261782585779e-11, "-2": 0.2120460349968263, "-3": 0.11814186494183007, "-4": 0.05118228596129153, "-5": 0.018079788462042373, "-6": 0.005382194229821638, "-7": 0.0013832018304246363, "-8": 0.00031254970426755884, "-9": 6.299174951376595e-05, "0": 0.18964561343522368, "1": 0.09173759769834361, "10": 5.776450870170067e-10, "11": 3.6183189677524004e-11, "12": 2.080639336471585e-12, "13": 1.1056627787197789e-13, "14": 5.460479391766487e-15, "15": 2.512073756745468e-16, "16": 1.0113324040515203e-17, "2": 0.025545189303061495, "3": 0.005382801867933401, "4": 0.0008819619605089696, "5": 0.00011782816738909924, "6": 1.3266023048514462e-05, "7": 1.2894144686543434e-06, "8": 1.101924094744901e-07, "9": 8.399276159149269e-09} |
| Raw goal margin distribution | {"-1": 0.26579311977481146, "-10": 1.0870633303085047e-05, "-11": 1.8004248887905462e-06, "-12": 2.737406921971682e-07, "-13": 3.8462688953450856e-08, "-14": 5.022525177966323e-09, "-15": 6.109393995160199e-10, "-16": 6.503304166073733e-11, "-2": 0.20123694299581898, "-3": 0.11211955810008255, "-4": 0.048573257984014115, "-5": 0.01715816737703651, "-6": 0.005107835727441231, "-7": 0.0013126928211840473, "-8": 0.0002966174162228131, "-9": 5.9780731605277865e-05, "0": 0.20896540587764167, "1": 0.1033706280935787, "10": 6.50894910682799e-10, "11": 4.0771495409044085e-11, "12": 2.3444803487715264e-12, "13": 1.245869292018955e-13, "14": 6.152910023598056e-15, "15": 2.830623959720972e-16, "16": 1.139577102966608e-17, "2": 0.02878451506556634, "3": 0.0060653823944815475, "4": 0.0009938014957863056, "5": 0.00013276968195937873, "6": 1.4948256431763874e-05, "7": 1.4529221043702358e-06, "8": 1.2416565142656357e-07, "9": 9.464368741785333e-09} |
| Unadjusted home-win probability | 13.9% |
| Unadjusted draw probability | 20.9% |
| Unadjusted away-win probability | 65.2% |
| Raw p over 1 5 | 71.5% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 41.7% |
| P home draw | 31.3% |
| P draw away | 87.6% |
| P home away | 81.0% |
| Raw p home draw | 34.8% |
| Raw p draw away | 86.1% |
| Raw p home away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.84, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:50:07Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 7.00 |
| Reference draw odds | 4.70 |
| Reference away odds | 1.33 |
| Market reference 1x2 last update utc | 2026-10-24T14:50:09Z |
| Market reference home last update utc | 2026-10-24T14:50:09Z |
| Market reference draw last update utc | 2026-10-24T14:50:09Z |
| Market reference away last update utc | 2026-10-24T14:50:09Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:50:09Z |
| Market best over 2 5 last update utc | 2026-10-24T14:50:07Z |
| Market best under 2 5 last update utc | 2026-10-24T14:50:07Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0314 |
| Raw edge prob draw | 0.0386 |
| Raw edge prob away | -0.0700 |
| Elo home rating | 1,479.7454 |
| Elo away rating | 1,690.3969 |
| Elo rating diff | -150.6514 |
| Elo home expectancy | 0.2958 |

</details>


---
