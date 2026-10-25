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
| Training as of utc | 2026-10-25T10:24:18.131719+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Optimizer objective | 1253.084 |
| Base scoring parameter | 0.289 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.101 |
| Xi per day | 0.0019 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-18'} |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 7, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Additional event odds calls used before this league | 24.00 |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **Heerenveen win** at **44.0%**. Expected goals are 1.36 for ADO Den Haag and 1.68 for Heerenveen (3.04 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 58.7%; Under 3.5 goals: 63.7%; Double Chance 1X: 56.0%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 61.7%; BTTS No (at least one team does not score): 38.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| ADO Den Haag win | 30.1% | 3.33 |
| Draw | 26.0% | 3.85 |
| Heerenveen win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| ADO Den Haag expected goals | 1.36 |
| Heerenveen expected goals | 1.68 |
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
| 1 | 1-1 | 12.01% |
| 2 | 1-2 | 9.18% |
| 3 | 2-1 | 7.43% |
| 4 | 0-1 | 6.91% |
| 5 | 0-2 | 6.74% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 37b2e2ce6ac958b456f8b82543199993 |
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
| P btts yes | 61.7% |
| P btts no | 38.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.06 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.2034625589033444, "-10": 2.925223206074429e-06, "-11": 4.397845980690931e-07, "-12": 6.076260925926614e-08, "-13": 7.761427508687274e-09, "-14": 9.139510640659237e-10, "-15": 8.890518579431189e-11, "-2": 0.1360501651347427, "-3": 0.06505657389658043, "-4": 0.024716797911356725, "-5": 0.007752376280433451, "-6": 0.002064962204056406, "-7": 0.00047725771073476545, "-8": 9.732503117668293e-05, "-9": 1.7746863269906642e-05, "0": 0.2596954329317287, "1": 0.16271423388624434, "10": 3.5562373413966027e-07, "11": 4.330668252342858e-08, "12": 4.846569984606757e-09, "13": 5.014444763018732e-10, "14": 4.782856618611791e-11, "15": 3.768553504156639e-12, "2": 0.08926175447341604, "3": 0.034573289792632106, "4": 0.010639590128292086, "5": 0.002703029017700305, "6": 0.0005831914437612084, "7": 0.0001091780072523711, "8": 1.803391148583845e-05, "9": 2.6636070659935175e-06} |
| Raw goal margin distribution | {"-1": 0.2034625589033444, "-10": 2.925223206074429e-06, "-11": 4.397845980690931e-07, "-12": 6.076260925926614e-08, "-13": 7.761427508687274e-09, "-14": 9.139510640659237e-10, "-15": 8.890518579431189e-11, "-2": 0.1360501651347427, "-3": 0.06505657389658043, "-4": 0.024716797911356725, "-5": 0.007752376280433451, "-6": 0.002064962204056406, "-7": 0.00047725771073476545, "-8": 9.732503117668293e-05, "-9": 1.7746863269906642e-05, "0": 0.2596954329317287, "1": 0.16271423388624434, "10": 3.5562373413966027e-07, "11": 4.330668252342858e-08, "12": 4.846569984606757e-09, "13": 5.014444763018732e-10, "14": 4.782856618611791e-11, "15": 3.768553504156639e-12, "2": 0.08926175447341604, "3": 0.034573289792632106, "4": 0.010639590128292086, "5": 0.002703029017700305, "6": 0.0005831914437612084, "7": 0.0001091780072523711, "8": 1.803391148583845e-05, "9": 2.6636070659935175e-06} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 63.7% |
| Raw p btts yes | 61.7% |
| P home draw | 56.0% |
| P draw away | 69.9% |
| P home away | 74.0% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.9% |
| Raw p home away | 74.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Elo home rating | 1,365.4130 |
| Elo away rating | 1,478.9271 |
| Elo rating diff | -53.5141 |
| Elo home expectancy | 0.4236 |

</details>


---

## 2026-10-24 — Willem II vs SC Cambuur

The model's most likely 1X2 outcome is **SC Cambuur win** at **40.3%**. Expected goals are 1.50 for Willem II and 1.65 for SC Cambuur (3.14 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.8%; Under 3.5 goals: 61.5%; Double Chance 1X: 59.7%; Double Chance X2: 66.0%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 63.8%; BTTS No (at least one team does not score): 36.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II win | 34.0% | 2.94 |
| Draw | 25.7% | 3.89 |
| SC Cambuur win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II expected goals | 1.50 |
| SC Cambuur expected goals | 1.65 |
| Expected total goals | 3.14 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 38.5% |
| Under 3.5 | 61.5% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 1-2 | 8.74% |
| 3 | 2-1 | 7.97% |
| 4 | 2-2 | 6.55% |
| 5 | 0-1 | 6.02% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:45:00+00:00 |
| Fixture id | d962e99711c241eb444793ef2e07098b |
| Matched home-team name | Willem II |
| Matched away-team name | Cambuur |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4994 |
| Dc lambda away | 1.6450 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.8% |
| P btts no | 36.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.59 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.96 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.60 |
| Fair Under 3.5 odds | 1.63 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1919108992385381, "-10": 2.151813185399997e-06, "-11": 3.159820892797957e-07, "-12": 4.2649513831352496e-08, "-13": 5.322207931921818e-09, "-14": 6.115867447962267e-10, "-15": 5.759951754739652e-11, "-2": 0.12371810217256023, "-3": 0.0572751473559692, "-4": 0.021136108590794605, "-5": 0.006451662418946011, "-6": 0.0016745222183738244, "-7": 0.0003774280718290086, "-8": 7.510350599138094e-05, "-9": 1.3368853489604478e-05, "0": 0.2573678142687498, "1": 0.17398043839086863, "10": 8.519423358335111e-07, "11": 1.1403250529374263e-07, "12": 1.4029456540692931e-08, "13": 1.5958025863920238e-09, "14": 1.6714983588065973e-10, "15": 1.434918714292977e-11, "2": 0.10279083086970797, "3": 0.04337584077181065, "4": 0.014590402941742273, "5": 0.0040595178276105785, "6": 0.0009604047424313806, "7": 0.00019731411029378452, "8": 3.578860084873021e-05, "9": 5.806831662388e-06} |
| Raw goal margin distribution | {"-1": 0.1919108992385381, "-10": 2.151813185399997e-06, "-11": 3.159820892797957e-07, "-12": 4.2649513831352496e-08, "-13": 5.322207931921818e-09, "-14": 6.115867447962267e-10, "-15": 5.759951754739652e-11, "-2": 0.12371810217256023, "-3": 0.0572751473559692, "-4": 0.021136108590794605, "-5": 0.006451662418946011, "-6": 0.0016745222183738244, "-7": 0.0003774280718290086, "-8": 7.510350599138094e-05, "-9": 1.3368853489604478e-05, "0": 0.2573678142687498, "1": 0.17398043839086863, "10": 8.519423358335111e-07, "11": 1.1403250529374263e-07, "12": 1.4029456540692931e-08, "13": 1.5958025863920238e-09, "14": 1.6714983588065973e-10, "15": 1.434918714292977e-11, "2": 0.10279083086970797, "3": 0.04337584077181065, "4": 0.014590402941742273, "5": 0.0040595178276105785, "6": 0.0009604047424313806, "7": 0.00019731411029378452, "8": 3.578860084873021e-05, "9": 5.806831662388e-06} |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 40.3% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 61.5% |
| Raw p btts yes | 63.8% |
| P home draw | 59.7% |
| P draw away | 66.0% |
| P home away | 74.3% |
| Raw p home draw | 59.7% |
| Raw p draw away | 66.0% |
| Raw p home away | 74.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Elo home rating | 1,340.9350 |
| Elo away rating | 1,415.8533 |
| Elo rating diff | -14.9183 |
| Elo home expectancy | 0.4785 |

</details>


---

## 2026-10-25 — AZ Alkmaar vs FC Twente Enschede

The model's most likely 1X2 outcome is **AZ Alkmaar win** at **42.5%**. Expected goals are 1.47 for AZ Alkmaar and 1.30 for FC Twente Enschede (2.77 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.7%; Double Chance 1X: 68.7%; Double Chance X2: 57.5%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AZ Alkmaar win | 42.5% | 2.35 |
| Draw | 26.1% | 3.83 |
| FC Twente Enschede win | 31.3% | 3.19 |

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
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 2-1 | 9.36% |
| 3 | 1-0 | 8.51% |
| 4 | 1-2 | 7.56% |
| 5 | 2-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AZ Alkmaar win | 42.5% | 45.1% | 2.18 | -7.3% |
| Draw | 26.1% | 24.5% | 3.90 | +1.9% |
| FC Twente Enschede win | 31.3% | 30.4% | 3.14 | -1.6% |

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
| Market best home last update utc | 2026-10-25T10:24:07Z |
| Market best draw last update utc | 2026-10-25T10:24:07Z |
| Market best away last update utc | 2026-10-25T10:24:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | AZ Alkmaar |
| Matched away-team name | Twente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.4697 |
| Dc lambda away | 1.2998 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.20 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.1713603791493336, "-10": 2.745623480699785e-07, "-11": 3.1986577526727195e-08, "-12": 3.4232258806733426e-09, "-13": 3.3865182118066136e-10, "-14": 3.095371051862961e-11, "-15": 2.3792786767048806e-12, "-2": 0.09312000372803678, "-3": 0.035204989333626105, "-4": 0.010495243719547671, "-5": 0.0025715520394298435, "-6": 0.0005336056402700946, "-7": 9.589651921818626e-05, "-8": 1.518641336708911e-05, "-9": 2.1484655547341417e-06, "0": 0.2613775823162764, "1": 0.21373316972583367, "10": 1.0263504659455575e-06, "11": 1.3519747408009519e-07, "12": 1.6359968387394203e-08, "13": 1.8299803171553529e-09, "14": 1.8912625359657858e-10, "15": 1.6437301274085698e-11, "2": 0.1302953417438455, "3": 0.05569756660981688, "4": 0.018774597386899114, "5": 0.00520139123608789, "6": 0.0012203677311266275, "7": 0.00024798148003386984, "8": 4.4403552869779704e-05, "9": 7.1029212373788745e-06} |
| Raw goal margin distribution | {"-1": 0.17638272714839112, "-10": 2.8260941044397157e-07, "-11": 3.29240621683669e-08, "-12": 3.5235561421811028e-09, "-13": 3.4857726196765717e-10, "-14": 3.186092318271439e-11, "-15": 2.4490122146467836e-12, "-2": 0.0958492289241842, "-3": 0.036236801404854614, "-4": 0.010802845550006717, "-5": 0.0026469208574951193, "-6": 0.0005492449218414831, "-7": 9.870712044236024e-05, "-8": 1.563150722814198e-05, "-9": 2.211434262748377e-06, "0": 0.2774993564827685, "1": 0.20101286818314248, "10": 9.652673526784124e-07, "11": 1.271512141555594e-07, "12": 1.5386307016145677e-08, "13": 1.7210692787738725e-09, "14": 1.7787042943753986e-10, "15": 1.5459037446236053e-11, "2": 0.12254083158187234, "3": 0.05238273324361632, "4": 0.017657229687677124, "5": 0.004891831119380596, "6": 0.0011477377057879622, "7": 0.00023322289479845698, "8": 4.176088124892197e-05, "9": 6.680191812230019e-06} |
| Unadjusted home-win probability | 40.0% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 32.3% |
| Raw p over 1 5 | 77.6% |
| Raw p under 3 5 | 69.9% |
| Raw p btts yes | 57.2% |
| P home draw | 68.7% |
| P draw away | 57.5% |
| P home away | 73.9% |
| Raw p home draw | 67.7% |
| Raw p draw away | 60.0% |
| Raw p home away | 72.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.72, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.09, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.83, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:28Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.18 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:14Z |
| Market reference home last update utc | 2026-10-25T10:24:14Z |
| Market reference draw last update utc | 2026-10-25T10:24:14Z |
| Market reference away last update utc | 2026-10-25T10:24:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:09Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:09Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.6% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0506 |
| Raw ev home | -0.1282 |
| Raw edge prob draw | 0.0322 |
| Raw ev draw | 0.0822 |
| Raw edge prob away | 0.0184 |
| Raw ev away | 0.0129 |
| Elo home rating | 1,554.0981 |
| Elo away rating | 1,560.3337 |
| Elo rating diff | 53.7643 |
| Elo home expectancy | 0.5768 |
| Market p home draw | 68.9% |
| Market reference home draw last update utc | 2026-10-25T10:24:07Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.1% |
| Market reference draw away last update utc | 2026-10-25T10:24:07Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.0% |
| Market reference home away last update utc | 2026-10-25T10:24:07Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 85.2% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 57.5% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.3% |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-25T10:24:07Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — Fortuna Sittard vs Excelsior

The model's most likely 1X2 outcome is **Fortuna Sittard win** at **39.3%**. Expected goals are 1.65 for Fortuna Sittard and 1.40 for Excelsior (3.04 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.8%; Double Chance 1X: 65.8%; Double Chance X2: 60.7%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 62.0%; BTTS No (at least one team does not score): 38.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fortuna Sittard win | 39.3% | 2.55 |
| Draw | 26.5% | 3.77 |
| Excelsior win | 34.2% | 2.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fortuna Sittard expected goals | 1.65 |
| Excelsior expected goals | 1.40 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.26% |
| 2 | 2-1 | 8.37% |
| 3 | 1-2 | 8.31% |
| 4 | 2-2 | 6.41% |
| 5 | 1-0 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fortuna Sittard win | 39.3% | 36.2% | 2.55 | +0.1% |
| Draw | 26.5% | 26.9% | 3.62 | -4.0% |
| Excelsior win | 34.2% | 36.9% | 2.74 | -6.2% |

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
| Market best home last update utc | 2026-10-25T10:24:07Z |
| Market best draw last update utc | 2026-10-25T10:24:07Z |
| Market best away last update utc | 2026-10-25T10:24:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
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
| P btts yes | 62.0% |
| P btts no | 38.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.77 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.18213456803773093, "-10": 5.015831640822857e-07, "-11": 6.269727982592322e-08, "-12": 7.202350643271166e-09, "-13": 7.649089641953702e-10, "-14": 7.488498760897651e-11, "-15": 6.05352489029689e-12, "-2": 0.10229819419506322, "-3": 0.04065061482141391, "-4": 0.012836777581254224, "-5": 0.0033468371352468797, "-6": 0.0007411024068680745, "-7": 0.00014239863001708558, "-8": 2.4142284402447695e-05, "-9": 3.660046878652024e-06, "0": 0.2653032873801669, "1": 0.18510358869758223, "10": 2.181381172271077e-06, "11": 3.2082124313175835e-07, "12": 4.336251748243914e-08, "13": 5.4184589334543496e-09, "14": 6.241465963732689e-10, "15": 5.936438669395596e-11, "2": 0.1211295511236217, "3": 0.05663371715886042, "4": 0.02104213361943986, "5": 0.006454968770440246, "6": 0.0016817583735540351, "7": 0.00038020427412721695, "8": 7.584297392466217e-05, "9": 1.3528493862382943e-05} |
| Raw goal margin distribution | {"-1": 0.16798952258212968, "-10": 4.626289077203718e-07, "-11": 5.782804559633691e-08, "-12": 6.642997312742804e-09, "-13": 7.055041395950287e-10, "-14": 6.906922421445344e-11, "-15": 5.583392363218754e-12, "-2": 0.09435344969924996, "-3": 0.037493582081050664, "-4": 0.011839839963389893, "-5": 0.0030869130367047835, "-6": 0.0006835464615835267, "-7": 0.00013133958111655094, "-8": 2.2267331646615364e-05, "-9": 3.375798094766917e-06, "0": 0.2611244558029657, "1": 0.19960624806624339, "10": 2.352289949984425e-06, "11": 3.459572290956602e-07, "12": 4.675992228069436e-08, "13": 5.842989137152089e-09, "14": 6.730477848753425e-10, "15": 6.401552006694803e-11, "2": 0.13061991612294516, "3": 0.061070905624600734, "4": 0.022690761279334466, "5": 0.006960708361831879, "6": 0.0018135222631882634, "7": 0.00040999285422430346, "8": 8.178518619658441e-05, "9": 1.4588436241877855e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 63.7% |
| Raw p btts yes | 61.9% |
| P home draw | 65.8% |
| P draw away | 60.7% |
| P home away | 73.5% |
| Raw p home draw | 68.4% |
| Raw p draw away | 57.7% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.0, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.89, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.84, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 4.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 4.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.59, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.05, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.59, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:14Z |
| Market reference home last update utc | 2026-10-25T10:24:14Z |
| Market reference draw last update utc | 2026-10-25T10:24:14Z |
| Market reference away last update utc | 2026-10-25T10:24:14Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:14Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:14Z |
| Home probability edge | +3.1% |
| Draw probability edge | -0.4% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0615 |
| Raw ev home | 0.0793 |
| Raw edge prob draw | -0.0084 |
| Raw ev draw | -0.0547 |
| Raw edge prob away | -0.0531 |
| Raw ev away | -0.1352 |
| Elo home rating | 1,433.5693 |
| Elo away rating | 1,444.5118 |
| Elo rating diff | 49.0575 |
| Elo home expectancy | 0.5701 |
| Market p home draw | 62.6% |
| Market reference home draw last update utc | 2026-10-25T10:24:07Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.2% |
| Market reference draw away last update utc | 2026-10-25T10:24:07Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.2% |
| Market reference home away last update utc | 2026-10-25T10:24:07Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 79.1% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference under 3 5 odds | 1.43 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-25T10:24:07Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — NEC Nijmegen vs Groningen

The model's most likely 1X2 outcome is **NEC Nijmegen win** at **47.0%**. Expected goals are 1.97 for NEC Nijmegen and 1.35 for Groningen (3.32 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.8%; Double Chance 1X: 71.2%; Double Chance X2: 53.0%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 76.1%; BTTS Yes (both teams score): 65.1%; BTTS No (at least one team does not score): 34.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| NEC Nijmegen win | 47.0% | 2.13 |
| Draw | 24.2% | 4.12 |
| Groningen win | 28.8% | 3.48 |

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
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.2% |
| Under 3.5 | 57.8% |
| Over 4.5 | 23.9% |
| Under 4.5 | 76.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.78% |
| 2 | 2-1 | 8.75% |
| 3 | 1-2 | 7.37% |
| 4 | 2-2 | 6.52% |
| 5 | 2-0 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| NEC Nijmegen win | 47.0% | 43.2% | 2.22 | +4.3% |
| Draw | 24.2% | 24.7% | 3.99 | -3.2% |
| Groningen win | 28.8% | 32.1% | 3.01 | -13.4% |

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
| Market best home last update utc | 2026-10-25T10:24:07Z |
| Market best draw last update utc | 2026-10-25T10:24:07Z |
| Market best away last update utc | 2026-10-25T10:24:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nijmegen |
| Matched away-team name | Groningen |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9677 |
| Dc lambda away | 1.3549 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.1% |
| P btts no | 34.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.47 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.18 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.15920566254400487, "-10": 2.9815436948026225e-07, "-11": 3.6008524685639464e-08, "-12": 3.998220924301726e-09, "-13": 4.1074377582784125e-10, "-14": 3.923223043552614e-11, "-15": 3.4666353055105504e-12, "-16": 2.516255271425637e-13, "-2": 0.08409047047015282, "-3": 0.03170491957824131, "-4": 0.009562837479668532, "-5": 0.0023909634105646416, "-6": 0.0005090172667006283, "-7": 9.419338998853394e-05, "-8": 1.5398367593700414e-05, "-9": 2.2529044726751655e-06, "0": 0.24248946006283498, "1": 0.19298691707055413, "10": 1.0171872737307933e-05, "11": 1.7841574292503449e-06, "12": 2.877151542120984e-07, "13": 4.29274455027317e-08, "14": 5.954909405509305e-09, "15": 7.642024400578565e-10, "16": 8.056066953791746e-11, "2": 0.14493113135865301, "3": 0.07936146221069358, "4": 0.03476465188958339, "5": 0.012623859287203209, "6": 0.0039031912762015676, "7": 0.0010490008789849083, "8": 0.00024905669045148336, "9": 5.292177620408675e-05} |
| Raw goal margin distribution | {"-1": 0.14059511798340815, "-10": 2.633012424590087e-07, "-11": 3.17992632654421e-08, "-12": 3.53084390086036e-09, "-13": 3.6272936967618235e-10, "-14": 3.4646129909546747e-11, "-15": 3.0613986462258377e-12, "-16": 2.2221144719942123e-13, "-2": 0.07426061000665478, "-3": 0.027998733446589708, "-4": 0.008444977661133973, "-5": 0.00211146875953255, "-6": 0.00044951505821965294, "-7": 8.31825361427372e-05, "-8": 1.3598356201619428e-05, "-9": 1.989548393440861e-06, "0": 0.23814969533670974, "1": 0.208574354528181, "10": 1.0993448792962321e-05, "11": 1.928262753928042e-06, "12": 3.1095373452608407e-07, "13": 4.6394669510175114e-08, "14": 6.435883863950317e-09, "15": 8.259266124535054e-10, "16": 8.706750646255598e-11, "2": 0.1566371318482624, "3": 0.08577143987929768, "4": 0.03757257195634593, "5": 0.01364348082476694, "6": 0.004218449692815913, "7": 0.0011337280503516333, "8": 0.00026917284985101804, "9": 5.719623630350451e-05} |
| Unadjusted home-win probability | 50.8% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 25.4% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 64.8% |
| P home draw | 71.2% |
| P draw away | 53.0% |
| P home away | 75.8% |
| Raw p home draw | 74.6% |
| Raw p draw away | 49.2% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.8, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 9.1, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.67, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.08, "price": 1.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.11, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.48, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:48Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.65, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.65, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.28 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:14Z |
| Market reference home last update utc | 2026-10-25T10:24:14Z |
| Market reference draw last update utc | 2026-10-25T10:24:14Z |
| Market reference away last update utc | 2026-10-25T10:24:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:09Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:09Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | 0.0759 |
| Raw ev home | 0.1275 |
| Raw edge prob draw | -0.0087 |
| Raw ev draw | -0.0498 |
| Raw edge prob away | -0.0672 |
| Raw ev away | -0.2356 |
| Elo home rating | 1,487.2038 |
| Elo away rating | 1,481.0181 |
| Elo rating diff | 66.1857 |
| Elo home expectancy | 0.5941 |
| Market p home draw | 67.0% |
| Market reference home draw last update utc | 2026-10-25T10:24:07Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.9% |
| Market reference draw away last update utc | 2026-10-25T10:24:07Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.1% |
| Market reference home away last update utc | 2026-10-25T10:24:07Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.30 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 1.96 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 71.2% |
| Market reference btts yes odds | 1.35 |
| Market reference btts yes opposite odds | 3.00 |
| Market reference btts yes last update utc | 2026-10-25T10:24:07Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — PSV Eindhoven vs Feyenoord

The model's most likely 1X2 outcome is **PSV Eindhoven win** at **48.8%**. Expected goals are 2.34 for PSV Eindhoven and 1.69 for Feyenoord (4.03 combined). The most likely exact score is 1-1 at 8.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 76.4%; Under 3.5 goals: 42.9%; Double Chance 1X: 70.8%; Double Chance X2: 51.2%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 62.5%; BTTS Yes (both teams score): 74.7%; BTTS No (at least one team does not score): 25.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| PSV Eindhoven win | 48.8% | 2.05 |
| Draw | 22.0% | 4.55 |
| Feyenoord win | 29.2% | 3.43 |

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
| Over 2.5 | 76.4% |
| Under 2.5 | 23.6% |
| Over 3.5 | 57.1% |
| Under 3.5 | 42.9% |
| Over 4.5 | 37.5% |
| Under 4.5 | 62.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.05% |
| 2 | 2-1 | 7.74% |
| 3 | 2-2 | 7.25% |
| 4 | 1-2 | 6.39% |
| 5 | 3-1 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| PSV Eindhoven win | 48.8% | 45.8% | 2.13 | +4.0% |
| Draw | 22.0% | 22.9% | 4.07 | -10.5% |
| Feyenoord win | 29.2% | 31.3% | 3.15 | -8.1% |

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
| Market best home last update utc | 2026-10-25T10:24:07Z |
| Market best draw last update utc | 2026-10-25T10:24:07Z |
| Market best away last update utc | 2026-10-25T10:24:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | PSV Eindhoven |
| Matched away-team name | Feyenoord |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3444 |
| Dc lambda away | 1.6902 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 74.7% |
| P btts no | 25.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 38.72 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.07 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.23 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.67 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.14780499181203952, "-10": 1.4267634519510523e-06, "-11": 2.1299075999003093e-07, "-12": 2.927187966334545e-08, "-13": 3.726159248617877e-09, "-14": 4.416532734593249e-10, "-15": 4.896445542328958e-11, "-16": 5.0920264201274026e-12, "-17": 4.907415256182637e-13, "-18": 3.776669624036248e-14, "-2": 0.08665875899732219, "-3": 0.038124720790400336, "-4": 0.013690691968964263, "-5": 0.004127156809483641, "-6": 0.0010681905689268283, "-7": 0.00024167936302344568, "-8": 4.850063612274535e-05, "-9": 8.73679082758008e-06, "0": 0.2200060762863019, "1": 0.18157422690036973, "10": 3.284054212424326e-05, "11": 6.8001526136653246e-06, "12": 1.2963075843112096e-06, "13": 2.2888557189924608e-07, "14": 3.7630328847904636e-08, "15": 5.786780950027179e-09, "16": 8.347305670614984e-10, "17": 1.1158556895041046e-10, "18": 1.1911426442818072e-11, "2": 0.1455708343305194, "3": 0.08883173244324843, "4": 0.044247263231727424, "5": 0.01850169593523459, "6": 0.006642152813871024, "7": 0.002084487263801996, "8": 0.0005802386681011291, "9": 0.0001449808779933732} |
| Raw goal margin distribution | {"-1": 0.1370657481208718, "-10": 1.3230973970207888e-06, "-11": 1.9751523614298288e-07, "-12": 2.714503776748468e-08, "-13": 3.4554232490252953e-09, "-14": 4.095635444688911e-10, "-15": 4.540678654790594e-11, "-16": 4.722048979330587e-12, "-17": 4.550851329052763e-13, "-18": 3.502263631814188e-14, "-2": 0.08036229012007408, "-3": 0.035354647451155456, "-4": 0.012695951023121292, "-5": 0.0038272850515319815, "-6": 0.0009905777719050577, "-7": 0.00022411937710676194, "-8": 4.4976667519836584e-05, "-9": 8.101991389307664e-06, "0": 0.21087364873283826, "1": 0.19285515239118567, "10": 3.4880874142205647e-05, "11": 7.222635563313394e-06, "12": 1.3768451667722842e-06, "13": 2.4310587797789984e-07, "14": 3.9968242896471907e-08, "15": 6.146304687747672e-09, "16": 8.86591084342369e-10, "17": 1.1851820752290228e-10, "18": 1.2651464919008284e-11, "2": 0.15461492480388578, "3": 0.09435071039523629, "4": 0.046996277165095426, "5": 0.019651177647821677, "6": 0.00705481948067174, "7": 0.002213993228998301, "8": 0.0006162879978627297, "9": 0.00015398831539325115} |
| Unadjusted home-win probability | 51.9% |
| Unadjusted draw probability | 21.1% |
| Unadjusted away-win probability | 27.1% |
| Raw p over 1 5 | 91.8% |
| Raw p under 3 5 | 42.7% |
| Raw p btts yes | 74.4% |
| P home draw | 70.8% |
| P draw away | 51.2% |
| P home away | 78.0% |
| Raw p home draw | 72.9% |
| Raw p draw away | 48.1% |
| Raw p home away | 78.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.8, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.0, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.36, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.72, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.7, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.87, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 5.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 9.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:23:42Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 2.14 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:14Z |
| Market reference home last update utc | 2026-10-25T10:24:14Z |
| Market reference draw last update utc | 2026-10-25T10:24:14Z |
| Market reference away last update utc | 2026-10-25T10:24:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:09Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:09Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.9% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.0607 |
| Raw ev home | 0.1045 |
| Raw edge prob draw | -0.0183 |
| Raw ev draw | -0.1417 |
| Raw edge prob away | -0.0424 |
| Raw ev away | -0.1477 |
| Elo home rating | 1,681.3663 |
| Elo away rating | 1,658.8042 |
| Elo rating diff | 82.5621 |
| Elo home expectancy | 0.6166 |
| Market p home draw | 69.2% |
| Market reference home draw last update utc | 2026-10-25T10:24:07Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.7% |
| Market reference draw away last update utc | 2026-10-25T10:24:07Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market reference home away last update utc | 2026-10-25T10:24:07Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 91.2% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.1% |
| Market under 3 5 odds | 2.05 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference under 3 5 odds | 2.03 |
| Market reference under 3 5 opposite odds | 1.76 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 73.5% |
| Market reference btts yes odds | 1.30 |
| Market reference btts yes opposite odds | 3.10 |
| Market reference btts yes last update utc | 2026-10-25T10:24:07Z |
| Market btts yes bookmakers | 0 |

</details>


---

## 2026-10-25 — Sparta Rotterdam vs Ajax

The model's most likely 1X2 outcome is **Ajax win** at **62.9%**. Expected goals are 1.13 for Sparta Rotterdam and 2.02 for Ajax (3.15 combined). The most likely exact score is 1-2 at 10.9%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.3%; Under 3.5 goals: 60.7%; Double Chance 1X: 37.1%; Double Chance X2: 83.2%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sparta Rotterdam win | 16.8% | 5.95 |
| Draw | 20.3% | 4.93 |
| Ajax win | 62.9% | 1.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sparta Rotterdam expected goals | 1.13 |
| Ajax expected goals | 2.02 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 83.7% |
| Under 1.5 | 16.3% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 39.3% |
| Under 3.5 | 60.7% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.93% |
| 2 | 0-2 | 9.65% |
| 3 | 1-1 | 9.40% |
| 4 | 0-1 | 8.47% |
| 5 | 1-3 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sparta Rotterdam win | 16.8% | 13.7% | 6.32 | +6.2% |
| Draw | 20.3% | 17.3% | 5.41 | +9.8% |
| Ajax win | 62.9% | 68.9% | 1.44 | -9.4% |

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
| Market best home last update utc | 2026-10-25T10:24:07Z |
| Market best draw last update utc | 2026-10-25T10:24:07Z |
| Market best away last update utc | 2026-10-25T10:24:07Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sparta Rotterdam |
| Matched away-team name | Ajax |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1328 |
| Dc lambda away | 2.0175 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.76 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.12 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.54 |
| Fair Under 3.5 odds | 1.65 |
| Fair Over 4.5 odds | 4.59 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.24452342880969072, "-10": 1.7935177418995396e-05, "-11": 3.234344297462899e-06, "-12": 5.360291316101434e-07, "-13": 8.216852379122142e-08, "-14": 1.1714867127011523e-08, "-15": 1.5603960128423594e-09, "-16": 1.9368651244455365e-10, "-17": 2.0262476622685026e-11, "-2": 0.19448043596580897, "-3": 0.11158549941762182, "-4": 0.05086233593312476, "-5": 0.019137951497899524, "-6": 0.0061151845845288716, "-7": 0.0016954076618067274, "-8": 0.0004147250766424184, "-9": 9.071211103112709e-05, "0": 0.2030257694763718, "1": 0.10125332373602634, "10": 4.267141444449358e-08, "11": 4.320587967299654e-09, "12": 4.020409006173684e-10, "13": 3.4602905777749073e-11, "14": 2.769935739672241e-12, "15": 2.0715355944513828e-13, "16": 1.4437173930690053e-14, "17": 8.480092265026442e-16, "2": 0.04684954211724099, "3": 0.015092543424937425, "4": 0.0038625686904715743, "5": 0.0008160196273434908, "6": 0.0001463996259299981, "7": 2.2789236700375746e-05, "8": 3.1299772082284084e-06, "9": 3.8438939224063786e-07} |
| Raw goal margin distribution | {"-1": 0.2209920771855205, "-10": 1.620921206531665e-05, "-11": 2.9230919430046135e-06, "-12": 4.844451584991913e-07, "-13": 7.42611570608331e-08, "-14": 1.0587504162497033e-08, "-15": 1.4102336033346634e-09, "-16": 1.750473765082618e-10, "-17": 1.8312547061718417e-11, "-2": 0.1757648979700813, "-3": 0.10084723341286082, "-4": 0.04596767403060202, "-5": 0.017296238954215688, "-6": 0.005526698812814749, "-7": 0.0015322526053342602, "-8": 0.00037481462039967923, "-9": 8.19825647801397e-05, "0": 0.23284631032840303, "1": 0.11975304537822497, "10": 5.0467793468653446e-08, "11": 5.109990939730049e-09, "12": 4.754967090369572e-10, "13": 4.092510934874966e-11, "14": 3.2760232265808947e-12, "15": 2.4500202748078223e-13, "16": 1.7074951034324457e-14, "17": 1.0029467047153544e-15, "2": 0.05540929557770977, "3": 0.017850061320962746, "4": 0.004568288196370333, "5": 0.0009651123721879147, "6": 0.00017314790666088847, "7": 2.6952996662411664e-05, "8": 3.701846900621025e-06, "9": 4.5462014118083826e-07} |
| Unadjusted home-win probability | 19.9% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 56.8% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 61.4% |
| Raw p btts yes | 59.8% |
| P home draw | 37.1% |
| P draw away | 83.2% |
| P home away | 79.7% |
| Raw p home draw | 43.2% |
| Raw p draw away | 80.1% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.15, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.27, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:24:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.69, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:24:07Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (NL) |
| Reference home odds | 6.75 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.43 |
| Market reference 1x2 last update utc | 2026-10-25T10:24:14Z |
| Market reference home last update utc | 2026-10-25T10:24:14Z |
| Market reference draw last update utc | 2026-10-25T10:24:14Z |
| Market reference away last update utc | 2026-10-25T10:24:14Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.14 |
| Market reference over 2 5 last update utc | 2026-10-25T10:24:09Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:24:09Z |
| Home probability edge | +3.1% |
| Draw probability edge | +3.0% |
| Away probability edge | -6.1% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0614 |
| Raw ev home | 0.2561 |
| Raw edge prob draw | 0.0596 |
| Raw ev draw | 0.2597 |
| Raw edge prob away | -0.1210 |
| Raw ev away | -0.1815 |
| Elo home rating | 1,400.1683 |
| Elo away rating | 1,618.3103 |
| Elo rating diff | -158.1420 |
| Elo home expectancy | 0.2869 |
| Market p home draw | 35.0% |
| Market reference home draw last update utc | 2026-10-25T10:24:07Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.3% |
| Market reference draw away last update utc | 2026-10-25T10:24:07Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.7% |
| Market reference home away last update utc | 2026-10-25T10:24:07Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.12 |
| Market reference dc home draw odds | 2.70 |
| Market reference dc home away odds | 1.17 |
| Market p over 1 5 | 89.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-25T10:24:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 50.4% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:24:07Z |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market reference under 3 5 last update utc | 2026-10-25T10:24:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.5% |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-25T10:24:07Z |
| Market btts yes bookmakers | 0 |

</details>


---
