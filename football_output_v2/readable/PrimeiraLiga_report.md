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
| Training as of utc | 2026-10-25T10:24:35.009850+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 1990.570 |
| Base scoring parameter | 0.085 |
| Home-advantage parameter | 0.186 |
| Dixon-Coles low-score adjustment | 0.045 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Additional event odds calls used before this league | 29.00 |
| Over 1 5 in window quote fixtures | 5 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **Alverca win** at **42.0%**. Expected goals are 1.46 for Alverca and 1.28 for Arouca (2.74 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.6%; Double Chance 1X: 66.4%; Double Chance X2: 58.0%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 42.0% | 2.38 |
| Draw | 24.4% | 4.10 |
| Arouca win | 33.6% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.46 |
| Arouca expected goals | 1.28 |
| Expected total goals | 2.74 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.53% |
| 2 | 1-0 | 9.99% |
| 3 | 2-1 | 8.81% |
| 4 | 0-1 | 8.81% |
| 5 | 1-2 | 7.71% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T17:00:00+00:00 |
| Fixture id | 3f752f1b9f725906b91ae5b699705cca |
| Matched home-team name | Alverca |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4602 |
| Dc lambda away | 1.2780 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.88 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.00 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.1933494435225365, "-10": 2.4527284148900033e-07, "-11": 2.810453322044897e-08, "-12": 2.9581746106786223e-09, "-13": 2.878145580082429e-10, "-14": 2.5878884074744984e-11, "-15": 1.960980759612555e-12, "-2": 0.0943854520374273, "-3": 0.03518106540571561, "-4": 0.010330996065315711, "-5": 0.0024920648522835896, "-6": 0.0005089263815087002, "-7": 8.99938456690685e-05, "-8": 1.402086139983926e-05, "-9": 1.951236767083229e-06, "0": 0.24395983483012681, "1": 0.22013426077322368, "10": 9.298177718112804e-07, "11": 1.2173055299616303e-07, "12": 1.4639352276537809e-08, "13": 1.6273675493222802e-09, "14": 1.6718344786305793e-10, "15": 1.4474244449576654e-11, "2": 0.12321249052675307, "3": 0.05247271085244459, "4": 0.017605223718824017, "5": 0.004852142312242399, "6": 0.0011321500560468423, "7": 0.00022873713488877982, "8": 4.071677765581065e-05, "9": 6.474161264646527e-06} |
| Raw goal margin distribution | {"-1": 0.1933494435225365, "-10": 2.4527284148900033e-07, "-11": 2.810453322044897e-08, "-12": 2.9581746106786223e-09, "-13": 2.878145580082429e-10, "-14": 2.5878884074744984e-11, "-15": 1.960980759612555e-12, "-2": 0.0943854520374273, "-3": 0.03518106540571561, "-4": 0.010330996065315711, "-5": 0.0024920648522835896, "-6": 0.0005089263815087002, "-7": 8.99938456690685e-05, "-8": 1.402086139983926e-05, "-9": 1.951236767083229e-06, "0": 0.24395983483012681, "1": 0.22013426077322368, "10": 9.298177718112804e-07, "11": 1.2173055299616303e-07, "12": 1.4639352276537809e-08, "13": 1.6273675493222802e-09, "14": 1.6718344786305793e-10, "15": 1.4474244449576654e-11, "2": 0.12321249052675307, "3": 0.05247271085244459, "4": 0.017605223718824017, "5": 0.004852142312242399, "6": 0.0011321500560468423, "7": 0.00022873713488877982, "8": 4.071677765581065e-05, "9": 6.474161264646527e-06} |
| Unadjusted home-win probability | 42.0% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.8% |
| P home draw | 66.4% |
| P draw away | 58.0% |
| P home away | 75.6% |
| Raw p home draw | 66.4% |
| Raw p draw away | 58.0% |
| Raw p home away | 75.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Elo home rating | 1,429.4069 |
| Elo away rating | 1,475.9199 |
| Elo rating diff | 13.4870 |
| Elo home expectancy | 0.5194 |

</details>


---

## 2026-10-24 — Gil Vicente vs FC Porto

The model's most likely 1X2 outcome is **FC Porto win** at **61.0%**. Expected goals are 0.68 for Gil Vicente and 1.65 for FC Porto (2.33 combined). The most likely exact score is 0-1 at 16.5%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.3%; Double Chance 1X: 39.0%; Double Chance X2: 84.2%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 39.5%; BTTS No (at least one team does not score): 60.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gil Vicente win | 15.8% | 6.34 |
| Draw | 23.2% | 4.31 |
| FC Porto win | 61.0% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gil Vicente expected goals | 0.68 |
| FC Porto expected goals | 1.65 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 67.1% |
| Under 1.5 | 32.9% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.7% |
| Under 3.5 | 79.3% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.50% |
| 2 | 0-2 | 13.17% |
| 3 | 1-1 | 10.47% |
| 4 | 0-0 | 9.23% |
| 5 | 1-2 | 9.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:30:00+00:00 |
| Fixture id | 2fdd5b6eaa94bcdf2f61444eef54b645 |
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
| P btts yes | 39.5% |
| P btts no | 60.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.84 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.04 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.83 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.44 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.2737757371245121, "-10": 4.325781931466897e-06, "-11": 6.41769276472841e-07, "-12": 8.739026579033011e-08, "-13": 1.0995065972181651e-08, "-14": 1.2825265322601792e-09, "-15": 1.308816241192013e-10, "-2": 0.1886684750980397, "-3": 0.09503541452029025, "-4": 0.03708554709196123, "-5": 0.011775842351415367, "-6": 0.0031472587038260964, "-7": 0.0007255765478116867, "-8": 0.0001469948701711846, "-9": 2.6551049436183412e-05, "0": 0.23196694038190238, "1": 0.11683172574915407, "10": 6.744932867431798e-10, "11": 4.164695295582392e-11, "12": 2.360253613815039e-12, "13": 1.235904038897209e-13, "14": 5.9999077246557195e-15, "15": 2.548286123704035e-16, "2": 0.03267999196963294, "3": 0.006851085320913187, "4": 0.0011126790059713552, "5": 0.0001470443992995398, "6": 1.6356118516399864e-05, "7": 1.56935914833586e-06, "8": 1.3232216144926785e-07, "9": 9.947258396878966e-09} |
| Raw goal margin distribution | {"-1": 0.2737757371245121, "-10": 4.325781931466897e-06, "-11": 6.41769276472841e-07, "-12": 8.739026579033011e-08, "-13": 1.0995065972181651e-08, "-14": 1.2825265322601792e-09, "-15": 1.308816241192013e-10, "-2": 0.1886684750980397, "-3": 0.09503541452029025, "-4": 0.03708554709196123, "-5": 0.011775842351415367, "-6": 0.0031472587038260964, "-7": 0.0007255765478116867, "-8": 0.0001469948701711846, "-9": 2.6551049436183412e-05, "0": 0.23196694038190238, "1": 0.11683172574915407, "10": 6.744932867431798e-10, "11": 4.164695295582392e-11, "12": 2.360253613815039e-12, "13": 1.235904038897209e-13, "14": 5.9999077246557195e-15, "15": 2.548286123704035e-16, "2": 0.03267999196963294, "3": 0.006851085320913187, "4": 0.0011126790059713552, "5": 0.0001470443992995398, "6": 1.6356118516399864e-05, "7": 1.56935914833586e-06, "8": 1.3232216144926785e-07, "9": 9.947258396878966e-09} |
| Unadjusted home-win probability | 15.8% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 61.0% |
| Raw p over 1 5 | 67.1% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 39.5% |
| P home draw | 39.0% |
| P draw away | 84.2% |
| P home away | 76.8% |
| Raw p home draw | 39.0% |
| Raw p draw away | 84.2% |
| Raw p home away | 76.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Elo home rating | 1,473.4882 |
| Elo away rating | 1,682.6975 |
| Elo rating diff | -149.2093 |
| Elo home expectancy | 0.2976 |

</details>


---

## 2026-10-25 — Estoril vs Moreirense FC

The model's most likely 1X2 outcome is **Estoril win** at **50.4%**. Expected goals are 1.52 for Estoril and 1.18 for Moreirense FC (2.70 combined). The most likely exact score is 1-0 at 11.9%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 50.8%; Under 3.5 goals: 71.2%; Double Chance 1X: 74.8%; Double Chance X2: 49.6%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Estoril win | 50.4% | 1.98 |
| Draw | 24.3% | 4.11 |
| Moreirense FC win | 25.2% | 3.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Estoril expected goals | 1.52 |
| Moreirense FC expected goals | 1.18 |
| Expected total goals | 2.70 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.86% |
| 2 | 1-1 | 11.53% |
| 3 | 2-1 | 10.10% |
| 4 | 2-0 | 8.58% |
| 5 | 0-1 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Estoril win | 50.4% | 55.0% | 1.79 | -9.7% |
| Draw | 24.3% | 24.4% | 3.77 | -8.3% |
| Moreirense FC win | 25.2% | 20.6% | 4.71 | +18.9% |
| Over 2.5 | 50.8% | 50.0% | 1.98 | +0.5% |
| Under 2.5 | 49.2% | 50.0% | 1.90 | -6.5% |

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
| Market best home last update utc | 2026-10-25T10:24:26Z |
| Market best draw last update utc | 2026-10-25T10:24:26Z |
| Market best away last update utc | 2026-10-25T10:24:26Z |
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
| Dc lambda home | 1.5240 |
| Dc lambda away | 1.1763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.25 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15192873662895062, "-10": 9.323830646153789e-08, "-11": 9.838633193514289e-09, "-12": 9.535894388170792e-10, "-13": 8.5430823952838e-11, "-14": 7.075834965731506e-12, "-15": 4.95659506697391e-13, "-2": 0.06863358186102934, "-3": 0.02365414948732843, "-4": 0.006412621956663047, "-5": 0.001426790112889776, "-6": 0.00026860969413343975, "-7": 4.377096694241722e-05, "-8": 6.282671454352042e-06, "-9": 8.053722451549623e-07, "0": 0.24333399316349372, "1": 0.25473120734932186, "10": 1.61856624663676e-06, "11": 2.21271369896424e-07, "12": 2.778473378922547e-08, "13": 3.224881455776489e-09, "14": 3.4604390742193417e-10, "15": 3.140445818033816e-11, "2": 0.15011979009927828, "3": 0.06702903599225316, "4": 0.023542123107593592, "5": 0.006786165270148419, "6": 0.0016551614995955872, "7": 0.00034942919400593665, "8": 6.497880908844602e-05, "9": 1.0791415372623755e-05} |
| Raw goal margin distribution | {"-1": 0.1799373848168527, "-10": 1.1042714763313875e-07, "-11": 1.1652423144522455e-08, "-12": 1.129387327354494e-09, "-13": 1.0118032563099305e-10, "-14": 8.380292414586938e-12, "-15": 5.870362472147665e-13, "-2": 0.08128644721668606, "-3": 0.028014883117284648, "-4": 0.007594813531024932, "-5": 0.001689824369585436, "-6": 0.0003181289265694836, "-7": 5.18403134079814e-05, "-8": 7.440906152734901e-06, "-9": 9.538457227560901e-07, "0": 0.2427771860345391, "1": 0.23151069168822258, "10": 1.4710227113563911e-06, "11": 2.0110095040405748e-07, "12": 2.5251962666261205e-08, "13": 2.9309111522229223e-09, "14": 3.1449960605684896e-10, "15": 2.8541724082725747e-11, "2": 0.1364353304160132, "3": 0.06091887463353085, "4": 0.021396095363275042, "5": 0.006167559255698854, "6": 0.0015042820532845487, "7": 0.0003175763002977337, "8": 5.905554012670975e-05, "9": 9.807703041995157e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 29.9% |
| Raw p over 1 5 | 74.6% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 53.5% |
| P home draw | 74.8% |
| P draw away | 49.6% |
| P home away | 75.7% |
| Raw p home draw | 70.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.74 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.33 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:31Z |
| Market reference home last update utc | 2026-10-25T10:24:31Z |
| Market reference draw last update utc | 2026-10-25T10:24:31Z |
| Market reference away last update utc | 2026-10-25T10:24:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market best over 2 5 last update utc | 2026-10-25T10:24:26Z |
| Market best under 2 5 last update utc | 2026-10-25T10:24:26Z |
| Home probability edge | -4.6% |
| Draw probability edge | -0.1% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0919 |
| Raw ev home | -0.1796 |
| Raw edge prob draw | -0.0011 |
| Raw ev draw | -0.0847 |
| Raw edge prob away | 0.0931 |
| Raw ev away | 0.4078 |
| Elo home rating | 1,397.5496 |
| Elo away rating | 1,419.4582 |
| Elo rating diff | 38.0914 |
| Elo home expectancy | 0.5546 |
| Market p home draw | 78.6% |
| Market reference home draw last update utc | 2026-10-25T10:24:31Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.5% |
| Market reference draw away last update utc | 2026-10-25T10:24:31Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market reference home away last update utc | 2026-10-25T10:24:31Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.01 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 75.4% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.67 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.34 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.36 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.8% |
| Market reference btts yes odds | 1.90 |
| Market reference btts yes opposite odds | 2.04 |
| Market reference btts yes last update utc | 2026-10-25T10:24:27Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — Nacional vs Braga

The model's most likely 1X2 outcome is **Braga win** at **61.3%**. Expected goals are 0.96 for Nacional and 1.81 for Braga (2.76 combined). The most likely exact score is 0-1 at 12.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.6%; Double Chance 1X: 38.7%; Double Chance X2: 82.9%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 50.8%; BTTS No (at least one team does not score): 49.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 17.1% | 5.86 |
| Draw | 21.6% | 4.62 |
| Braga win | 61.3% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.96 |
| Braga expected goals | 1.81 |
| Expected total goals | 2.76 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.59% |
| 2 | 0-2 | 10.90% |
| 3 | 1-2 | 10.45% |
| 4 | 1-1 | 10.26% |
| 5 | 0-3 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 17.1% | 13.9% | 6.89 | +17.6% |
| Draw | 21.6% | 21.3% | 4.46 | -3.6% |
| Braga win | 61.3% | 64.8% | 1.50 | -8.1% |
| Over 2.5 | 52.6% | 51.8% | 1.92 | +1.0% |
| Under 2.5 | 47.4% | 48.2% | 1.97 | -6.6% |

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
| Market best home last update utc | 2026-10-25T10:24:26Z |
| Market best draw last update utc | 2026-10-25T10:24:26Z |
| Market best away last update utc | 2026-10-25T10:24:26Z |
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
| Dc lambda away | 1.8057 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.8% |
| P btts no | 49.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.48 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.20 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2653390268821991, "-10": 7.935904193388929e-06, "-11": 1.285995863263153e-06, "-12": 1.914006648121086e-07, "-13": 2.63361948026384e-08, "-14": 3.3685032971754e-09, "-15": 4.006240213803438e-10, "-16": 4.0796866689203853e-11, "-2": 0.18717717254325175, "-3": 0.09940348570510188, "-4": 0.0414705842596681, "-5": 0.014188890953239478, "-6": 0.004105738690686626, "-7": 0.0010280246067716273, "-8": 0.00022668207341000967, "-9": 4.463326494539488e-05, "0": 0.21625301085235277, "1": 0.11383583748802067, "10": 1.1242988382638073e-08, "11": 9.67539978222405e-10, "12": 7.64745254555829e-11, "13": 5.588179866399268e-12, "14": 3.7957563625227685e-13, "15": 2.397410148497441e-14, "16": 1.2965108761164658e-15, "2": 0.041916616204977886, "3": 0.011821673181648023, "4": 0.00261915674961775, "5": 0.00047589790082607853, "6": 7.313085398865941e-05, "7": 9.724266472448377e-06, "8": 1.138713630171283e-06, "9": 1.1906935501316826e-07} |
| Raw goal margin distribution | {"-1": 0.2500743674572277, "-10": 7.479360441929909e-06, "-11": 1.2120139499905562e-06, "-12": 1.8038959721153632e-07, "-13": 2.4821102775145374e-08, "-14": 3.174717044894826e-09, "-15": 3.775765665234734e-10, "-16": 3.8449868273877874e-11, "-2": 0.1764090777606085, "-3": 0.0936849136097235, "-4": 0.0390848276210133, "-5": 0.013372619820552255, "-6": 0.0038695401052856035, "-7": 0.0009688834932790167, "-8": 0.00021364130557043222, "-9": 4.206556280062728e-05, "0": 0.21960005630027138, "1": 0.13511442688159425, "10": 1.3344566748730815e-08, "11": 1.1483959052552974e-09, "12": 9.07694088784679e-11, "13": 6.632741820336296e-12, "14": 4.5052723010747724e-13, "15": 2.845542364885199e-14, "16": 1.538859183872253e-15, "2": 0.04975181542409547, "3": 0.014031421316577678, "4": 0.003108738609446274, "5": 0.0005648543863090212, "6": 8.680072674898252e-05, "7": 1.1541960073926896e-05, "8": 1.351565929657639e-06, "9": 1.413262116462955e-07} |
| Unadjusted home-win probability | 20.3% |
| Unadjusted draw probability | 22.0% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 70.0% |
| Raw p btts yes | 51.0% |
| P home draw | 38.7% |
| P draw away | 82.9% |
| P home away | 78.4% |
| Raw p home draw | 42.2% |
| Raw p draw away | 79.7% |
| Raw p home away | 78.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.41, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.08, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.41, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 6.15 |
| Reference draw odds | 4.15 |
| Reference away odds | 1.49 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:31Z |
| Market reference home last update utc | 2026-10-25T10:24:31Z |
| Market reference draw last update utc | 2026-10-25T10:24:31Z |
| Market reference away last update utc | 2026-10-25T10:24:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market best over 2 5 last update utc | 2026-10-25T10:24:26Z |
| Market best under 2 5 last update utc | 2026-10-25T10:24:26Z |
| Home probability edge | +3.2% |
| Draw probability edge | +0.3% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0638 |
| Raw ev home | 0.3964 |
| Raw edge prob draw | 0.0067 |
| Raw ev draw | -0.0206 |
| Raw edge prob away | -0.0705 |
| Raw ev away | -0.1334 |
| Elo home rating | 1,367.2841 |
| Elo away rating | 1,563.4097 |
| Elo rating diff | -136.1256 |
| Elo home expectancy | 0.3135 |
| Market p home draw | 37.6% |
| Market reference home draw last update utc | 2026-10-25T10:24:31Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.7% |
| Market reference draw away last update utc | 2026-10-25T10:24:31Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market reference home away last update utc | 2026-10-25T10:24:31Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.48 |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 75.9% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.73 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.9% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.27 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 47.3% |
| Market reference btts yes odds | 2.08 |
| Market reference btts yes opposite odds | 1.87 |
| Market reference btts yes last update utc | 2026-10-25T10:24:27Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — Rio Ave FC vs Famalicão

The model's most likely 1X2 outcome is **Famalicão win** at **45.9%**. Expected goals are 1.03 for Rio Ave FC and 1.30 for Famalicão (2.32 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.4%; Double Chance 1X: 54.1%; Double Chance X2: 72.9%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rio Ave FC win | 27.1% | 3.70 |
| Draw | 27.0% | 3.70 |
| Famalicão win | 45.9% | 2.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rio Ave FC expected goals | 1.03 |
| Famalicão expected goals | 1.30 |
| Expected total goals | 2.32 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 67.0% |
| Under 1.5 | 33.0% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.11% |
| 2 | 1-1 | 12.61% |
| 3 | 1-0 | 9.60% |
| 4 | 0-0 | 9.33% |
| 5 | 1-2 | 8.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rio Ave FC win | 27.1% | 24.1% | 3.93 | +6.4% |
| Draw | 27.0% | 27.4% | 3.32 | -10.2% |
| Famalicão win | 45.9% | 48.5% | 2.09 | -4.1% |

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
| Market best home last update utc | 2026-10-25T10:24:26Z |
| Market best draw last update utc | 2026-10-25T10:24:26Z |
| Market best away last update utc | 2026-10-25T10:24:26Z |
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
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.71 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.03 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.85 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.57 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2529449224241747, "-10": 4.324442630081291e-07, "-11": 5.0448516114328525e-08, "-12": 5.402324803848987e-09, "-13": 5.326827907798711e-10, "-14": 4.503635405327263e-11, "-2": 0.13314556688366957, "-3": 0.05209528439322713, "-4": 0.01586827348804603, "-5": 0.003943727923935648, "-6": 0.0008263271173426265, "-7": 0.00014951039556322133, "-8": 2.378900831007172e-05, "-9": 3.376510823530101e-06, "0": 0.27036778633840364, "1": 0.17124286639344688, "10": 3.550287095711634e-08, "11": 3.278600521413418e-09, "12": 2.7792497291178936e-10, "13": 2.169313504473261e-11, "14": 1.4518563596845165e-12, "2": 0.07089340888322267, "3": 0.02195757298919736, "4": 0.005294468538003473, "5": 0.0010416130531096656, "6": 0.0001727659873321599, "7": 2.4744826039714615e-05, "8": 3.1167080712473365e-06, "9": 3.501827161991933e-07} |
| Raw goal margin distribution | {"-1": 0.23845799822363953, "-10": 4.076768662202651e-07, "-11": 4.755917632456921e-08, "-12": 5.092917249073927e-09, "-13": 5.021744289633938e-10, "-14": 4.245698522789602e-11, "-2": 0.12551991574746532, "-3": 0.04911162918094969, "-4": 0.01495944925464559, "-5": 0.0037178586439594267, "-6": 0.0007790008527983052, "-7": 0.00014094748096917293, "-8": 2.2426539528761354e-05, "-9": 3.183127790204219e-06, "0": 0.2670269212433834, "1": 0.18999090629446994, "10": 3.93898021637897e-08, "11": 3.6375488074911955e-09, "12": 3.0835280089306843e-10, "13": 2.4068146453747957e-11, "14": 1.6108087384620358e-12, "2": 0.07865497283303667, "3": 0.024361535637108574, "4": 0.005874118420627713, "5": 0.001155651106153338, "6": 0.00019168078181242164, "7": 2.7453943188399503e-05, "8": 3.4579320212443656e-06, "9": 3.8852147841581493e-07} |
| Unadjusted home-win probability | 30.0% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 43.3% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 46.0% |
| P home draw | 54.1% |
| P draw away | 72.9% |
| P home away | 73.0% |
| Raw p home draw | 56.7% |
| Raw p draw away | 70.0% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.76 |
| Reference draw odds | 3.34 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:31Z |
| Market reference home last update utc | 2026-10-25T10:24:31Z |
| Market reference draw last update utc | 2026-10-25T10:24:31Z |
| Market reference away last update utc | 2026-10-25T10:24:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:31Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | 0.0593 |
| Raw ev home | 0.1800 |
| Raw edge prob draw | -0.0067 |
| Raw ev draw | -0.1135 |
| Raw edge prob away | -0.0526 |
| Raw ev away | -0.0956 |
| Elo home rating | 1,391.3818 |
| Elo away rating | 1,495.7667 |
| Elo rating diff | -44.3849 |
| Elo home expectancy | 0.4365 |
| Market p home draw | 52.6% |
| Market reference home draw last update utc | 2026-10-25T10:24:31Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.5% |
| Market reference draw away last update utc | 2026-10-25T10:24:31Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market reference home away last update utc | 2026-10-25T10:24:31Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.24 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 73.0% |
| Market over 1 5 odds | 1.34 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.38 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.9% |
| Market under 3 5 odds | 1.29 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.73 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.0% |
| Market reference btts yes odds | 1.89 |
| Market reference btts yes opposite odds | 2.04 |
| Market reference btts yes last update utc | 2026-10-25T10:24:27Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — Sporting Lisbon vs Académico de Viseu

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **72.8%**. Expected goals are 1.93 for Sporting Lisbon and 0.72 for Académico de Viseu (2.65 combined). The most likely exact score is 1-0 at 15.5%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 51.2%; Under 3.5 goals: 71.7%; Double Chance 1X: 89.2%; Double Chance X2: 27.2%; Double Chance 12 (either team wins): 83.7%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 42.2%; BTTS No (at least one team does not score): 57.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 72.8% | 1.37 |
| Draw | 16.3% | 6.12 |
| Académico de Viseu win | 10.8% | 9.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 1.93 |
| Académico de Viseu expected goals | 0.72 |
| Expected total goals | 2.65 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 51.2% |
| Under 2.5 | 48.8% |
| Over 3.5 | 28.3% |
| Under 3.5 | 71.7% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.45% |
| 2 | 2-0 | 14.42% |
| 3 | 2-1 | 10.41% |
| 4 | 3-0 | 9.26% |
| 5 | 1-1 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 72.8% | 79.3% | 1.22 | -11.1% |
| Draw | 16.3% | 12.6% | 7.16 | +16.9% |
| Académico de Viseu win | 10.8% | 8.0% | 11.49 | +24.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

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
| Market best home last update utc | 2026-10-25T10:24:26Z |
| Market best draw last update utc | 2026-10-25T10:24:26Z |
| Market best away last update utc | 2026-10-25T10:24:26Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Porto |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 72/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9269 |
| Dc lambda away | 0.7219 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.2% |
| P btts no | 57.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.50 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.53 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.32 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.07974570344891709, "-10": 6.757336992245612e-10, "-11": 4.388813902293369e-11, "-12": 2.6170779999762804e-12, "-13": 1.4423289101672516e-13, "-14": 7.387870995191702e-15, "-15": 3.5236798386609327e-16, "-16": 1.4626792466943546e-17, "-2": 0.02275149780872795, "-3": 0.004938086514238036, "-4": 0.0008355845733885104, "-5": 0.00011545608118884138, "-6": 1.3456241436779636e-05, "-7": 1.3547018591100268e-06, "-8": 1.199621822393388e-07, "-9": 9.477630745962698e-09, "0": 0.1632876383781587, "1": 0.2857071791304947, "10": 1.7121352564873767e-05, "11": 2.9681204253652443e-06, "12": 4.724141283234007e-07, "13": 6.949321091530278e-08, "14": 9.500998126656687e-09, "15": 1.209534414980384e-09, "16": 1.340117094056913e-10, "2": 0.2237678102674609, "3": 0.12963377633863393, "4": 0.05854930588115338, "5": 0.021593349251520153, "6": 0.006717363134503557, "7": 0.001805055840806517, "8": 0.0004266415333182915, "9": 8.996848711589947e-05} |
| Raw goal margin distribution | {"-1": 0.10028432518426819, "-10": 8.497698948058453e-10, "-11": 5.519159296560224e-11, "-12": 3.2911102395671395e-12, "-13": 1.8138028156280313e-13, "-14": 9.29062789916726e-15, "-15": 4.431208698433287e-16, "-16": 1.8393944108818196e-17, "-2": 0.02861117911062359, "-3": 0.006209897867401927, "-4": 0.0010507905937569269, "-5": 0.00014519196257212617, "-6": 1.6921915960882513e-05, "-7": 1.703607290313112e-06, "-8": 1.5085861649224269e-07, "-9": 1.191860830863921e-08, "0": 0.2002442036887355, "1": 0.26025735741855904, "10": 1.559624083485242e-05, "11": 2.7037303744222166e-06, "12": 4.303330879497575e-07, "13": 6.330299254778808e-08, "14": 8.654681596758054e-09, "15": 1.1017932118738232e-09, "16": 1.22074403097652e-10, "2": 0.2038353364195565, "3": 0.11808644138645094, "4": 0.05333393327284955, "5": 0.01966988729901617, "6": 0.006119003321957992, "7": 0.0016442676188639666, "8": 0.00038863775969628505, "9": 8.19544009324143e-05} |
| Unadjusted home-win probability | 66.3% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 43.5% |
| P home draw | 89.2% |
| P draw away | 27.2% |
| P home away | 83.7% |
| Raw p home draw | 86.4% |
| Raw p draw away | 33.7% |
| Raw p home away | 80.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.84, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.01, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.23 |
| Reference draw odds | 6.35 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:31Z |
| Market reference home last update utc | 2026-10-25T10:24:31Z |
| Market reference draw last update utc | 2026-10-25T10:24:31Z |
| Market reference away last update utc | 2026-10-25T10:24:31Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:28Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:28Z |
| Home probability edge | -6.5% |
| Draw probability edge | +3.7% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -21.9% |
| Under 2.5 probability edge | +21.9% |
| Raw edge prob home | -0.1298 |
| Raw ev home | -0.1906 |
| Raw edge prob draw | 0.0739 |
| Raw ev draw | 0.4337 |
| Raw edge prob away | 0.0558 |
| Raw ev away | 0.5663 |
| Elo home rating | 1,691.2508 |
| Elo away rating | 1,431.9052 |
| Elo rating diff | 319.3457 |
| Elo home expectancy | 0.8627 |
| Market p home draw | 90.4% |
| Market reference home draw last update utc | 2026-10-25T10:24:31Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 24.2% |
| Market reference draw away last update utc | 2026-10-25T10:24:31Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.4% |
| Market reference home away last update utc | 2026-10-25T10:24:31Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 3.84 |
| Market reference dc home away odds | 1.09 |
| Market p over 1 5 | 89.0% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 7.18 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 48.8% |
| Market under 3 5 odds | 1.98 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference under 3 5 odds | 1.98 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.5% |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-25T10:24:27Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-26 — Santa Clara vs Benfica

The model's most likely 1X2 outcome is **Benfica win** at **68.0%**. Expected goals are 0.70 for Santa Clara and 1.84 for Benfica (2.54 combined). The most likely exact score is 0-1 at 15.7%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 47.0%; Under 3.5 goals: 74.6%; Double Chance 1X: 32.0%; Double Chance X2: 88.3%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 88.4%; BTTS Yes (both teams score): 41.4%; BTTS No (at least one team does not score): 58.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 11.7% | 8.52 |
| Draw | 20.3% | 4.93 |
| Benfica win | 68.0% | 1.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 0.70 |
| Benfica expected goals | 1.84 |
| Expected total goals | 2.54 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 72.0% |
| Under 1.5 | 28.0% |
| Over 2.5 | 47.0% |
| Under 2.5 | 53.0% |
| Over 3.5 | 25.4% |
| Under 3.5 | 74.6% |
| Over 4.5 | 11.6% |
| Under 4.5 | 88.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.68% |
| 2 | 0-2 | 13.99% |
| 3 | 1-2 | 9.73% |
| 4 | 1-1 | 9.40% |
| 5 | 0-3 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Over 2.5 | 47.0% | 50.9% | 1.81 | -14.9% |
| Under 2.5 | 53.0% | 49.1% | 1.88 | -0.4% |

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
| P btts yes | 41.4% |
| P btts no | 58.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.80 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.58 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.94 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.64 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.27724785708776456, "-10": 1.1339722545320571e-05, "-11": 1.8781340850564286e-06, "-12": 2.8555843841428495e-07, "-13": 4.0123551514563855e-08, "-14": 5.2394530970263414e-09, "-15": 6.373323091952421e-10, "-16": 6.784279849247411e-11, "-2": 0.209908349953196, "-3": 0.11695124994203472, "-4": 0.05066676939984302, "-5": 0.017897811356210817, "-6": 0.0053280627777622545, "-7": 0.0013693016383349858, "-8": 0.0003094114790786037, "-9": 6.23598216523022e-05, "0": 0.2028213897461383, "1": 0.08709585105023981, "10": 5.487187927021029e-10, "11": 3.437350076907729e-11, "12": 1.976705332497357e-12, "13": 1.0505000267425878e-13, "14": 5.188387713937346e-15, "15": 2.387053570184261e-16, "16": 9.61058334162802e-18, "2": 0.0242537558435368, "3": 0.005110976913799488, "4": 0.0008374753445509964, "5": 0.00011189186367754465, "6": 1.2598466323121262e-05, "7": 1.2246084133741635e-06, "8": 1.0466085970608423e-07, "9": 7.978155656319181e-09} |
| Raw goal margin distribution | {"-1": 0.2657907035723366, "-10": 1.0871113181162457e-05, "-11": 1.8005209674616633e-06, "-12": 2.737578535480774e-07, "-13": 3.8465462272268936e-08, "-14": 5.022934855550763e-09, "-15": 6.109948139897135e-10, "-16": 6.503922278440843e-11, "-2": 0.2012339738377382, "-3": 0.11211828770210323, "-4": 0.04857298602044243, "-5": 0.0171581916727542, "-6": 0.005107882777722305, "-7": 0.001312715812048997, "-8": 0.0002966251771303185, "-9": 5.978282770410745e-05, "0": 0.2089629774799345, "1": 0.10337589893243865, "10": 6.51285885294144e-10, "11": 4.0798631606556326e-11, "12": 2.346193167727209e-12, "13": 1.2468605942024014e-13, "14": 6.158206590448337e-15, "15": 2.833244128647911e-16, "16": 1.1407003665798396e-17, "2": 0.02878729333923422, "3": 0.006066326082308926, "4": 0.0009940171148539994, "5": 0.00013280680826254133, "6": 1.4953384869865506e-05, "7": 1.4535135031834907e-06, "8": 1.2422417744006318e-07, "9": 9.469440884378893e-09} |
| Unadjusted home-win probability | 13.9% |
| Unadjusted draw probability | 20.9% |
| Unadjusted away-win probability | 65.2% |
| Raw p over 1 5 | 71.5% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 41.7% |
| P home draw | 32.0% |
| P draw away | 88.3% |
| P home away | 79.7% |
| Raw p home draw | 34.8% |
| Raw p draw away | 86.1% |
| Raw p home away | 79.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.93, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:26Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 3.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.37 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:31Z |
| Market reference home last update utc | 2026-10-25T10:24:31Z |
| Market reference draw last update utc | 2026-10-25T10:24:31Z |
| Market reference away last update utc | 2026-10-25T10:24:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:31Z |
| Market best over 2 5 last update utc | 2026-10-25T10:24:26Z |
| Market best under 2 5 last update utc | 2026-10-25T10:24:26Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.0439 |
| Raw edge prob draw | 0.0123 |
| Raw edge prob away | -0.0562 |
| Elo home rating | 1,479.7454 |
| Elo away rating | 1,690.3969 |
| Elo rating diff | -150.6514 |
| Elo home expectancy | 0.2958 |
| Market p home draw | 32.1% |
| Market reference home draw last update utc | 2026-10-25T10:24:31Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 88.9% |
| Market reference draw away last update utc | 2026-10-25T10:24:31Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market reference home away last update utc | 2026-10-25T10:24:31Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.91 |
| Market reference dc draw away odds | 1.05 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 76.9% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.33 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:26Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.5% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.2% |
| Market reference btts yes odds | 2.16 |
| Market reference btts yes opposite odds | 1.79 |
| Market reference btts yes last update utc | 2026-10-25T10:24:27Z |
| Market btts yes bookmakers | 0 |

</details>


---
