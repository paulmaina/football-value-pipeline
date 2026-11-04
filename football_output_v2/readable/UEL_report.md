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
| Training as of utc | 2026-11-04T09:30:58.349973+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 794.162 |
| Base scoring parameter | 0.103 |
| Home-advantage parameter | 0.267 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 108, 'matches': 714, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-22'} |
| Training data health | {'training_end': '2026-10-22', 'verified_at_utc': '2026-11-04T00:36:38.177871+00:00', 'official_source_health': {'2025': {'status': 'REVIEWED_HISTORICAL_FACTS', 'recorded_at_utc': '2026-10-22T08:05:26.556956+00:00', 'original_source_sha256': 'd6f3819c7189cf41ed644ab2c1aa144448031564a9334a678413508ec72c083b'}}, 'status': 'VERIFIED_WITHIN_24_HOURS'} |
| Training source | verified .football_cache/europa/training.json |
| Fixture provider mode | auto |
| Fixture sources | ['Fixture Download UTC'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 18} |
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

## 2026-11-04 — rennes vs olympiacos

The model's most likely 1X2 outcome is **rennes win** at **55.8%**. Expected goals are 1.47 for rennes and 0.71 for olympiacos (2.18 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 37.1%; Under 3.5 goals: 82.4%; Double Chance 1X: 81.3%; Double Chance X2: 44.2%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 38.6%; BTTS No (at least one team does not score): 61.4%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| rennes win | 55.8% | 1.79 |
| Draw | 25.4% | 3.93 |
| olympiacos win | 18.7% | 5.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| rennes expected goals | 1.47 |
| olympiacos expected goals | 0.71 |
| Expected total goals | 2.18 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 63.4% |
| Under 1.5 | 36.6% |
| Over 2.5 | 37.1% |
| Under 2.5 | 62.9% |
| Over 3.5 | 17.6% |
| Under 3.5 | 82.4% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.20% |
| 2 | 2-0 | 12.17% |
| 3 | 1-1 | 11.23% |
| 4 | 0-0 | 10.75% |
| 5 | 2-1 | 8.66% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-04T15:30:00+00:00 |
| Fixture id | uel-fd-130 |
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
| P btts yes | 38.6% |
| P btts no | 61.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.31 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.69 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.68 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.28 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.13666473678135133, "-10": 1.145784183860303e-09, "-11": 7.356173813816408e-11, "-12": 4.334411397779098e-12, "-13": 2.3595658939471953e-13, "-14": 1.1911976124766576e-14, "-15": 5.284881990520688e-16, "-2": 0.040095347256945336, "-3": 0.008785859390450084, "-4": 0.001488301616097744, "-5": 0.00020491007288226269, "-6": 2.372935658364652e-05, "-7": 2.3693167303907925e-06, "-8": 2.0782359103133463e-07, "-9": 1.6249204304218988e-08, "0": 0.2544264892343288, "1": 0.27510706358698833, "10": 1.5677096538360006e-06, "11": 2.0721971541839078e-07, "12": 2.5137697820614654e-08, "13": 2.8173692008082215e-09, "14": 2.9282742451833756e-10, "15": 2.674727288734451e-11, "2": 0.1699521022729241, "3": 0.07667134667786353, "4": 0.026739672091155034, "5": 0.007579572520827852, "6": 0.001807106085323517, "7": 0.00037148141220183723, "8": 6.708494878304097e-05, "9": 1.0798877828126175e-05} |
| Raw goal margin distribution | {"-1": 0.13666473678135133, "-10": 1.145784183860303e-09, "-11": 7.356173813816408e-11, "-12": 4.334411397779098e-12, "-13": 2.3595658939471953e-13, "-14": 1.1911976124766576e-14, "-15": 5.284881990520688e-16, "-2": 0.040095347256945336, "-3": 0.008785859390450084, "-4": 0.001488301616097744, "-5": 0.00020491007288226269, "-6": 2.372935658364652e-05, "-7": 2.3693167303907925e-06, "-8": 2.0782359103133463e-07, "-9": 1.6249204304218988e-08, "0": 0.2544264892343288, "1": 0.27510706358698833, "10": 1.5677096538360006e-06, "11": 2.0721971541839078e-07, "12": 2.5137697820614654e-08, "13": 2.8173692008082215e-09, "14": 2.9282742451833756e-10, "15": 2.674727288734451e-11, "2": 0.1699521022729241, "3": 0.07667134667786353, "4": 0.026739672091155034, "5": 0.007579572520827852, "6": 0.001807106085323517, "7": 0.00037148141220183723, "8": 6.708494878304097e-05, "9": 1.0798877828126175e-05} |
| Unadjusted home-win probability | 55.8% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 18.7% |
| Raw p over 1 5 | 63.4% |
| Raw p under 3 5 | 82.4% |
| Raw p btts yes | 38.6% |
| Home training matches | 19 |
| Away training matches | 25 |
| P home draw | 81.3% |
| P draw away | 44.2% |
| P home away | 74.6% |
| Raw p home draw | 81.3% |
| Raw p draw away | 44.2% |
| Raw p home away | 74.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.3712 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,490.6687 |
| Elo away rating | 1,481.7280 |
| Elo rating diff | 68.9408 |
| Elo home expectancy | 0.5979 |

</details>


---

## 2026-11-05 — anderlecht vs salzburg

The model's most likely 1X2 outcome is **anderlecht win** at **52.1%**. Expected goals are 1.85 for anderlecht and 1.24 for salzburg (3.09 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 59.6%; Under 3.5 goals: 62.8%; Double Chance 1X: 73.8%; Double Chance X2: 47.9%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| anderlecht win | 52.1% | 1.92 |
| Draw | 21.7% | 4.60 |
| salzburg win | 26.2% | 3.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| anderlecht expected goals | 1.85 |
| salzburg expected goals | 1.24 |
| Expected total goals | 3.09 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 59.6% |
| Under 2.5 | 40.4% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.93% |
| 2 | 2-1 | 9.65% |
| 3 | 1-0 | 8.95% |
| 4 | 2-0 | 7.78% |
| 5 | 1-2 | 6.48% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-131 |
| Matched home-team name | anderlecht |
| Matched away-team name | salzburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8459 |
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
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.72 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.21 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.15677242654129675, "-10": 1.332212805306001e-07, "-11": 1.4767975348256417e-08, "-12": 1.5044975294000873e-09, "-13": 1.4176581308110847e-10, "-14": 1.2419356614718756e-11, "-15": 1.0088016387344516e-12, "-16": 6.840829497905256e-14, "-2": 0.0708995954200495, "-3": 0.025000855939055704, "-4": 0.007004146348996489, "-5": 0.0016198897863647776, "-6": 0.00031815806328351664, "-7": 5.421993972901147e-05, "-8": 8.152717974838881e-06, "-9": 1.0961469009262206e-06, "0": 0.21725859005551107, "1": 0.2307835211856345, "10": 7.107454493154114e-06, "11": 1.1726691255202522e-06, "12": 1.7781158760072494e-07, "13": 2.4937570577595095e-08, "14": 3.2515899701423317e-09, "15": 3.9311218445127807e-10, "16": 3.967651697595422e-11, "2": 0.15706226412757973, "3": 0.0824322250670212, "4": 0.034372522544974714, "5": 0.011831933200212884, "6": 0.0034588141313459174, "7": 0.0008773186652561166, "8": 0.0001963427214185866, "9": 3.9291191222239696e-05} |
| Raw goal margin distribution | {"-1": 0.15677242654129675, "-10": 1.332212805306001e-07, "-11": 1.4767975348256417e-08, "-12": 1.5044975294000873e-09, "-13": 1.4176581308110847e-10, "-14": 1.2419356614718756e-11, "-15": 1.0088016387344516e-12, "-16": 6.840829497905256e-14, "-2": 0.0708995954200495, "-3": 0.025000855939055704, "-4": 0.007004146348996489, "-5": 0.0016198897863647776, "-6": 0.00031815806328351664, "-7": 5.421993972901147e-05, "-8": 8.152717974838881e-06, "-9": 1.0961469009262206e-06, "0": 0.21725859005551107, "1": 0.2307835211856345, "10": 7.107454493154114e-06, "11": 1.1726691255202522e-06, "12": 1.7781158760072494e-07, "13": 2.4937570577595095e-08, "14": 3.2515899701423317e-09, "15": 3.9311218445127807e-10, "16": 3.967651697595422e-11, "2": 0.15706226412757973, "3": 0.0824322250670212, "4": 0.034372522544974714, "5": 0.011831933200212884, "6": 0.0034588141313459174, "7": 0.0008773186652561166, "8": 0.0001963427214185866, "9": 3.9291191222239696e-05} |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 21.7% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 62.8% |
| Raw p btts yes | 59.3% |
| Home training matches | 13 |
| Away training matches | 13 |
| P home draw | 73.8% |
| P draw away | 47.9% |
| P home away | 78.3% |
| Raw p home draw | 73.8% |
| Raw p draw away | 47.9% |
| Raw p home away | 78.3% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5958 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,445.9180 |
| Elo away rating | 1,427.7213 |
| Elo rating diff | 78.1968 |
| Elo home expectancy | 0.6107 |

</details>


---

## 2026-11-05 — az alkmaar vs juventus

The model's most likely 1X2 outcome is **juventus win** at **66.4%**. Expected goals are 0.79 for az alkmaar and 2.01 for juventus (2.80 combined). The most likely exact score is 0-1 at 12.7%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 53.1%; Under 3.5 goals: 69.2%; Double Chance 1X: 33.6%; Double Chance X2: 85.7%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 84.8%; BTTS Yes (both teams score): 46.8%; BTTS No (at least one team does not score): 53.2%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| az alkmaar win | 14.3% | 7.01 |
| Draw | 19.4% | 5.17 |
| juventus win | 66.4% | 1.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| az alkmaar expected goals | 0.79 |
| juventus expected goals | 2.01 |
| Expected total goals | 2.80 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 30.8% |
| Under 3.5 | 69.2% |
| Over 4.5 | 15.2% |
| Under 4.5 | 84.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.70% |
| 2 | 0-2 | 12.28% |
| 3 | 1-2 | 9.70% |
| 4 | 1-1 | 9.17% |
| 5 | 0-3 | 8.23% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-138 |
| Matched home-team name | az alkmaar |
| Matched away-team name | juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7901 |
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
| P btts yes | 46.8% |
| P btts no | 53.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.87 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.25 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.56 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.2534593387387703, "-10": 2.081991829639762e-05, "-11": 3.759611614930584e-06, "-12": 6.234468115572318e-07, "-13": 9.556741155911972e-08, "-14": 1.3618481293016792e-08, "-15": 1.8127386900004136e-09, "-16": 2.2556590163848534e-10, "-17": 2.43914021853099e-11, "-2": 0.20221625853361785, "-3": 0.12064116411012887, "-4": 0.056364327196586836, "-5": 0.0215578864386408, "-6": 0.006965664539796922, "-7": 0.0019461342094443796, "-8": 0.00047859353770206915, "-9": 0.00010505883479508691, "0": 0.1935284529062962, "1": 0.10256160531271596, "10": 1.8338181540867934e-09, "11": 1.3016911561629457e-10, "12": 8.485005036988974e-12, "13": 5.112699223794449e-13, "14": 2.8638932392519195e-14, "15": 1.4984804266102919e-15, "16": 7.329545477273194e-17, "17": 3.115502377187002e-18, "2": 0.031245790753289083, "3": 0.007327548358650115, "4": 0.001345721608725361, "5": 0.00020232278909378023, "6": 2.5697383362424696e-05, "7": 2.8221939702203393e-06, "8": 2.728152402958366e-07, "9": 2.354084793402039e-08} |
| Raw goal margin distribution | {"-1": 0.2534593387387703, "-10": 2.081991829639762e-05, "-11": 3.759611614930584e-06, "-12": 6.234468115572318e-07, "-13": 9.556741155911972e-08, "-14": 1.3618481293016792e-08, "-15": 1.8127386900004136e-09, "-16": 2.2556590163848534e-10, "-17": 2.43914021853099e-11, "-2": 0.20221625853361785, "-3": 0.12064116411012887, "-4": 0.056364327196586836, "-5": 0.0215578864386408, "-6": 0.006965664539796922, "-7": 0.0019461342094443796, "-8": 0.00047859353770206915, "-9": 0.00010505883479508691, "0": 0.1935284529062962, "1": 0.10256160531271596, "10": 1.8338181540867934e-09, "11": 1.3016911561629457e-10, "12": 8.485005036988974e-12, "13": 5.112699223794449e-13, "14": 2.8638932392519195e-14, "15": 1.4984804266102919e-15, "16": 7.329545477273194e-17, "17": 3.115502377187002e-18, "2": 0.031245790753289083, "3": 0.007327548358650115, "4": 0.001345721608725361, "5": 0.00020232278909378023, "6": 2.5697383362424696e-05, "7": 2.8221939702203393e-06, "8": 2.728152402958366e-07, "9": 2.354084793402039e-08} |
| Unadjusted home-win probability | 14.3% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 66.4% |
| Raw p over 1 5 | 76.4% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 46.8% |
| Home training matches | 15 |
| Away training matches | 11 |
| P home draw | 33.6% |
| P draw away | 85.7% |
| P home away | 80.6% |
| Raw p home draw | 33.6% |
| Raw p draw away | 85.7% |
| Raw p home away | 80.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5306 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,483.3792 |
| Elo away rating | 1,491.7497 |
| Elo rating diff | 51.6295 |
| Elo home expectancy | 0.5738 |

</details>


---

## 2026-11-05 — benfica vs lech poznan

The model's most likely 1X2 outcome is **benfica win** at **98.8%**. Expected goals are 5.16 for benfica and 0.20 for lech poznan (5.35 combined). The most likely exact score is 5-0 at 14.4%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 90.2%; Under 3.5 goals: 21.9%; Double Chance 1X: 99.8%; Double Chance X2: 1.2%; Double Chance 12 (either team wins): 99.0%; Under 4.5 goals: 38.1%; BTTS Yes (both teams score): 17.6%; BTTS No (at least one team does not score): 82.4%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| benfica win | 98.8% | 1.01 |
| Draw | 1.0% | 96.41 |
| lech poznan win | 0.2% | 541.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| benfica expected goals | 5.16 |
| lech poznan expected goals | 0.20 |
| Expected total goals | 5.35 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 97.0% |
| Under 1.5 | 3.0% |
| Over 2.5 | 90.2% |
| Under 2.5 | 9.8% |
| Over 3.5 | 78.1% |
| Under 3.5 | 21.9% |
| Over 4.5 | 61.9% |
| Under 4.5 | 38.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-0 | 14.40% |
| 2 | 4-0 | 13.96% |
| 3 | 6-0 | 12.38% |
| 4 | 3-0 | 10.82% |
| 5 | 7-0 | 9.12% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-137 |
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
| P btts yes | 17.6% |
| P btts no | 82.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 222.46 |
| Fair Over 1.5 odds | 1.03 |
| Fair Under 1.5 odds | 32.99 |
| Fair Over 2.5 odds | 1.11 |
| Fair Under 2.5 odds | 10.22 |
| Fair Over 3.5 odds | 1.28 |
| Fair Under 3.5 odds | 4.57 |
| Fair Over 4.5 odds | 1.62 |
| Fair Under 4.5 odds | 2.63 |
| Goal margin distribution | {"-1": 0.0017145452901781298, "-10": 1.1585221603506567e-16, "-11": 2.04227292629215e-18, "-12": 3.3039649712114177e-20, "-13": 4.938436397390801e-22, "-14": 6.859225026977567e-24, "-15": 8.897229453455995e-26, "-16": 1.0824754635350923e-27, "-17": 1.2400222465356475e-29, "-18": 1.3420434572027164e-31, "-19": 1.376415555539917e-33, "-2": 0.00012479036830746122, "-20": 1.3414209801155927e-35, "-21": 1.24533285869583e-37, "-22": 1.1037845477260435e-39, "-23": 9.359435780090156e-42, "-24": 7.606602696463057e-44, "-25": 5.93145271882419e-46, "-26": 4.290987093173606e-48, "-3": 7.524745591912526e-06, "-4": 3.5045270609509855e-07, "-5": 1.3259284359156218e-08, "-6": 4.218259122114197e-10, "-7": 1.156853703349978e-11, "-8": 2.786775562384524e-13, "-9": 5.983442567228098e-15, "0": 0.010371841011092547, "1": 0.03920297144001806, "10": 0.0190376957395619, "11": 0.008859206400175316, "12": 0.0037834454591308114, "13": 0.0014928374171216687, "14": 0.0005473550148691606, "15": 0.000187421688074188, "16": 6.019412681735637e-05, "17": 1.8202730458378893e-05, "18": 5.200494534362028e-06, "19": 1.4079869869309543e-06, "2": 0.08696070935959921, "20": 3.622306264286602e-07, "21": 8.877210605729158e-08, "22": 2.077047313698875e-08, "23": 4.64924841821727e-09, "24": 9.974584640183538e-10, "25": 2.0532232025539586e-10, "26": 3.921058324597441e-11, "3": 0.1384219082698909, "4": 0.1701819251854139, "5": 0.16997110691514986, "6": 0.14274446462591886, "7": 0.10334166787684648, "8": 0.06571583378084916, "9": 0.037246902263298395} |
| Raw goal margin distribution | {"-1": 0.0017145452901781298, "-10": 1.1585221603506567e-16, "-11": 2.04227292629215e-18, "-12": 3.3039649712114177e-20, "-13": 4.938436397390801e-22, "-14": 6.859225026977567e-24, "-15": 8.897229453455995e-26, "-16": 1.0824754635350923e-27, "-17": 1.2400222465356475e-29, "-18": 1.3420434572027164e-31, "-19": 1.376415555539917e-33, "-2": 0.00012479036830746122, "-20": 1.3414209801155927e-35, "-21": 1.24533285869583e-37, "-22": 1.1037845477260435e-39, "-23": 9.359435780090156e-42, "-24": 7.606602696463057e-44, "-25": 5.93145271882419e-46, "-26": 4.290987093173606e-48, "-3": 7.524745591912526e-06, "-4": 3.5045270609509855e-07, "-5": 1.3259284359156218e-08, "-6": 4.218259122114197e-10, "-7": 1.156853703349978e-11, "-8": 2.786775562384524e-13, "-9": 5.983442567228098e-15, "0": 0.010371841011092547, "1": 0.03920297144001806, "10": 0.0190376957395619, "11": 0.008859206400175316, "12": 0.0037834454591308114, "13": 0.0014928374171216687, "14": 0.0005473550148691606, "15": 0.000187421688074188, "16": 6.019412681735637e-05, "17": 1.8202730458378893e-05, "18": 5.200494534362028e-06, "19": 1.4079869869309543e-06, "2": 0.08696070935959921, "20": 3.622306264286602e-07, "21": 8.877210605729158e-08, "22": 2.077047313698875e-08, "23": 4.64924841821727e-09, "24": 9.974584640183538e-10, "25": 2.0532232025539586e-10, "26": 3.921058324597441e-11, "3": 0.1384219082698909, "4": 0.1701819251854139, "5": 0.16997110691514986, "6": 0.14274446462591886, "7": 0.10334166787684648, "8": 0.06571583378084916, "9": 0.037246902263298395} |
| Unadjusted home-win probability | 98.8% |
| Unadjusted draw probability | 1.0% |
| Unadjusted away-win probability | 0.2% |
| Raw p over 1 5 | 97.0% |
| Raw p under 3 5 | 21.9% |
| Raw p btts yes | 17.6% |
| Home training matches | 9 |
| Away training matches | 3 |
| P home draw | 99.8% |
| P draw away | 1.2% |
| P home away | 99.0% |
| Raw p home draw | 99.8% |
| Raw p draw away | 1.2% |
| Raw p home away | 99.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.9021 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,490.8432 |
| Elo away rating | 1,407.9321 |
| Elo rating diff | 142.9112 |
| Elo home expectancy | 0.6948 |

</details>


---

## 2026-11-05 — celta vs union sg

The model's most likely 1X2 outcome is **union sg win** at **44.0%**. Expected goals are 1.05 for celta and 1.34 for union sg (2.39 combined). The most likely exact score is 0-1 at 12.9%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.1%; Double Chance 1X: 56.0%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 90.5%; BTTS Yes (both teams score): 47.3%; BTTS No (at least one team does not score): 52.7%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| celta win | 29.9% | 3.35 |
| Draw | 26.1% | 3.84 |
| union sg win | 44.0% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| celta expected goals | 1.05 |
| union sg expected goals | 1.34 |
| Expected total goals | 2.39 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.9% |
| Under 3.5 | 78.1% |
| Over 4.5 | 9.5% |
| Under 4.5 | 90.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.94% |
| 2 | 1-1 | 12.25% |
| 3 | 1-0 | 10.26% |
| 4 | 1-2 | 8.64% |
| 5 | 0-0 | 8.52% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-142 |
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
| P btts yes | 47.3% |
| P btts no | 52.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.73 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.57 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.58 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.23858382985008192, "-10": 5.383262581269558e-07, "-11": 6.492568002099134e-08, "-12": 7.188342686121774e-09, "-13": 7.325724758579109e-10, "-14": 6.37514488182933e-11, "-2": 0.12848429379321905, "-3": 0.05173920819521485, "-4": 0.016248850757318047, "-5": 0.004167776139954464, "-6": 0.000901816406439156, "-7": 0.0001685692869700342, "-8": 2.7716761564302838e-05, "-9": 4.066097467953265e-06, "0": 0.2607540031584911, "1": 0.18801522968819676, "10": 4.613300689171225e-08, "11": 4.351904185946045e-09, "12": 3.7686708693134043e-10, "13": 3.0040465289950215e-11, "14": 2.0447618632329553e-12, "2": 0.07860375284718332, "3": 0.02475766245916386, "4": 0.006081477847007221, "5": 0.0012200776825685104, "6": 0.00020648944213451985, "7": 3.0189421330499127e-05, "8": 3.882535580337883e-06, "9": 4.4549964598581887e-07} |
| Raw goal margin distribution | {"-1": 0.23858382985008192, "-10": 5.383262581269558e-07, "-11": 6.492568002099134e-08, "-12": 7.188342686121774e-09, "-13": 7.325724758579109e-10, "-14": 6.37514488182933e-11, "-2": 0.12848429379321905, "-3": 0.05173920819521485, "-4": 0.016248850757318047, "-5": 0.004167776139954464, "-6": 0.000901816406439156, "-7": 0.0001685692869700342, "-8": 2.7716761564302838e-05, "-9": 4.066097467953265e-06, "0": 0.2607540031584911, "1": 0.18801522968819676, "10": 4.613300689171225e-08, "11": 4.351904185946045e-09, "12": 3.7686708693134043e-10, "13": 3.0040465289950215e-11, "14": 2.0447618632329553e-12, "2": 0.07860375284718332, "3": 0.02475766245916386, "4": 0.006081477847007221, "5": 0.0012200776825685104, "6": 0.00020648944213451985, "7": 3.0189421330499127e-05, "8": 3.882535580337883e-06, "9": 4.4549964598581887e-07} |
| Unadjusted home-win probability | 29.9% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 68.3% |
| Raw p under 3 5 | 78.1% |
| Raw p btts yes | 47.3% |
| Home training matches | 17 |
| Away training matches | 29 |
| P home draw | 56.0% |
| P draw away | 70.1% |
| P home away | 73.9% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.1% |
| Raw p home away | 73.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4275 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,446.1006 |
| Elo away rating | 1,494.2964 |
| Elo rating diff | 11.8042 |
| Elo home expectancy | 0.5170 |

</details>


---

## 2026-11-05 — celtic vs besiktas

The model's most likely 1X2 outcome is **besiktas win** at **48.6%**. Expected goals are 2.00 for celtic and 2.43 for besiktas (4.43 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 81.9%; Under 3.5 goals: 35.3%; Double Chance 1X: 51.4%; Double Chance X2: 67.2%; Double Chance 12 (either team wins): 81.4%; Under 4.5 goals: 54.5%; BTTS Yes (both teams score): 78.6%; BTTS No (at least one team does not score): 21.4%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| celtic win | 32.8% | 3.05 |
| Draw | 18.6% | 5.37 |
| besiktas win | 48.6% | 2.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| celtic expected goals | 2.00 |
| besiktas expected goals | 2.43 |
| Expected total goals | 4.43 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 93.3% |
| Under 1.5 | 6.7% |
| Over 2.5 | 81.9% |
| Under 2.5 | 18.1% |
| Over 3.5 | 64.7% |
| Under 3.5 | 35.3% |
| Over 4.5 | 45.5% |
| Under 4.5 | 54.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.03% |
| 2 | 1-2 | 7.03% |
| 3 | 2-1 | 5.78% |
| 4 | 2-3 | 5.70% |
| 5 | 1-3 | 5.70% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-139 |
| Matched home-team name | celtic |
| Matched away-team name | besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0016 |
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
| P btts yes | 78.6% |
| P btts no | 21.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 111.45 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.85 |
| Fair Over 2.5 odds | 1.22 |
| Fair Under 2.5 odds | 5.52 |
| Fair Over 3.5 odds | 1.55 |
| Fair Under 3.5 odds | 2.83 |
| Fair Over 4.5 odds | 2.20 |
| Fair Under 4.5 odds | 1.84 |
| Goal margin distribution | {"-1": 0.1888378935193766, "-10": 3.669076857595341e-05, "-11": 7.834696508627363e-06, "-12": 1.541564290749657e-06, "-13": 2.8114948058234195e-07, "-14": 4.7772273972893557e-08, "-15": 7.595668575205219e-09, "-16": 1.1322051057215163e-09, "-17": 1.553520674125182e-10, "-18": 1.6526835223944496e-11, "-2": 0.14066686188616162, "-3": 0.08546944648975814, "-4": 0.04288010134843778, "-5": 0.018197205941820786, "-6": 0.006664487219487316, "-7": 0.002141382886896966, "-8": 0.0006118933787179926, "-9": 0.0001572525863199266, "0": 0.1863805190212347, "1": 0.1558691438411089, "10": 5.211673454210428e-06, "11": 9.15555348305187e-07, "12": 1.4820610931145295e-07, "13": 2.2237388779336225e-08, "14": 3.108597235906867e-09, "15": 4.0662735137735426e-10, "16": 4.9865218763926276e-11, "17": 5.629005792494923e-12, "18": 4.926589696393022e-13, "2": 0.09520853364522207, "3": 0.04759233441996714, "4": 0.019643730084916006, "5": 0.00685827513403934, "6": 0.0020664217856370248, "7": 0.0005462464137596063, "8": 0.00012841390816892506, "9": 2.715039457444997e-05} |
| Raw goal margin distribution | {"-1": 0.1888378935193766, "-10": 3.669076857595341e-05, "-11": 7.834696508627363e-06, "-12": 1.541564290749657e-06, "-13": 2.8114948058234195e-07, "-14": 4.7772273972893557e-08, "-15": 7.595668575205219e-09, "-16": 1.1322051057215163e-09, "-17": 1.553520674125182e-10, "-18": 1.6526835223944496e-11, "-2": 0.14066686188616162, "-3": 0.08546944648975814, "-4": 0.04288010134843778, "-5": 0.018197205941820786, "-6": 0.006664487219487316, "-7": 0.002141382886896966, "-8": 0.0006118933787179926, "-9": 0.0001572525863199266, "0": 0.1863805190212347, "1": 0.1558691438411089, "10": 5.211673454210428e-06, "11": 9.15555348305187e-07, "12": 1.4820610931145295e-07, "13": 2.2237388779336225e-08, "14": 3.108597235906867e-09, "15": 4.0662735137735426e-10, "16": 4.9865218763926276e-11, "17": 5.629005792494923e-12, "18": 4.926589696393022e-13, "2": 0.09520853364522207, "3": 0.04759233441996714, "4": 0.019643730084916006, "5": 0.00685827513403934, "6": 0.0020664217856370248, "7": 0.0005462464137596063, "8": 0.00012841390816892506, "9": 2.715039457444997e-05} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 18.6% |
| Unadjusted away-win probability | 48.6% |
| Raw p over 1 5 | 93.3% |
| Raw p under 3 5 | 35.3% |
| Raw p btts yes | 78.6% |
| Home training matches | 13 |
| Away training matches | 11 |
| P home draw | 51.4% |
| P draw away | 67.2% |
| P home away | 81.4% |
| Raw p home draw | 51.4% |
| Raw p draw away | 67.2% |
| Raw p home away | 81.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8189 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,392.0962 |
| Elo away rating | 1,450.5156 |
| Elo rating diff | 1.5806 |
| Elo home expectancy | 0.5023 |

</details>


---

## 2026-11-05 — crystal palace vs hoffenheim

The model's most likely 1X2 outcome is **crystal palace win** at **64.1%**. Expected goals are 2.71 for crystal palace and 1.47 for hoffenheim (4.18 combined). The most likely exact score is 2-1 at 8.2%. Goal-market probabilities: at least one goal: 98.8%; Over 2.5 goals: 78.8%; Under 3.5 goals: 39.8%; Double Chance 1X: 80.7%; Double Chance X2: 35.9%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 59.3%; BTTS Yes (both teams score): 71.6%; BTTS No (at least one team does not score): 28.4%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| crystal palace win | 64.1% | 1.56 |
| Draw | 16.5% | 6.05 |
| hoffenheim win | 19.3% | 5.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| crystal palace expected goals | 2.71 |
| hoffenheim expected goals | 1.47 |
| Expected total goals | 4.18 |
| Over 0.5 | 98.8% |
| Under 0.5 | 1.2% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 78.8% |
| Under 2.5 | 21.2% |
| Over 3.5 | 60.2% |
| Under 3.5 | 39.8% |
| Over 4.5 | 40.7% |
| Under 4.5 | 59.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.25% |
| 2 | 3-1 | 7.46% |
| 3 | 2-2 | 6.06% |
| 4 | 1-1 | 5.77% |
| 5 | 2-0 | 5.61% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-132 |
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
| P btts yes | 71.6% |
| P btts no | 28.4% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 82.01 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.19 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.71 |
| Fair Over 3.5 odds | 1.66 |
| Fair Under 3.5 odds | 2.51 |
| Fair Over 4.5 odds | 2.46 |
| Fair Under 4.5 odds | 1.69 |
| Goal margin distribution | {"-1": 0.11195986942977795, "-10": 2.829381352006845e-07, "-11": 3.6729921449419856e-08, "-12": 4.389769173793582e-09, "-13": 4.859528152928153e-10, "-14": 5.0091658593271286e-11, "-15": 4.8301018763118665e-12, "-16": 4.374253642834766e-13, "-17": 3.7299406552553326e-14, "-18": 2.960795913286667e-15, "-19": 1.8932606010696102e-16, "-2": 0.052720339206321985, "-3": 0.020146742652765184, "-4": 0.006286655992952513, "-5": 0.001647204011848816, "-6": 0.00037061109843502865, "-7": 7.290074663187767e-05, "-8": 1.2720321678974673e-05, "-9": 1.9924484312423253e-06, "0": 0.16535029069260276, "1": 0.20413849258006975, "10": 0.00013022410552990927, "11": 3.121187690305646e-05, "12": 6.887182002586028e-06, "13": 1.4076476758304856e-06, "14": 2.6789540629522346e-07, "15": 4.769316405697678e-08, "16": 7.974506128678681e-09, "17": 1.2554567200887672e-09, "18": 1.8399595939098823e-10, "19": 2.1722519718976503e-11, "2": 0.1797124542237136, "3": 0.12679578238381708, "4": 0.07304990488859284, "5": 0.035338437202763, "6": 0.014679739823908649, "7": 0.0053312850487803355, "8": 0.00171750500429107, "9": 0.0004966918070761909} |
| Raw goal margin distribution | {"-1": 0.11195986942977795, "-10": 2.829381352006845e-07, "-11": 3.6729921449419856e-08, "-12": 4.389769173793582e-09, "-13": 4.859528152928153e-10, "-14": 5.0091658593271286e-11, "-15": 4.8301018763118665e-12, "-16": 4.374253642834766e-13, "-17": 3.7299406552553326e-14, "-18": 2.960795913286667e-15, "-19": 1.8932606010696102e-16, "-2": 0.052720339206321985, "-3": 0.020146742652765184, "-4": 0.006286655992952513, "-5": 0.001647204011848816, "-6": 0.00037061109843502865, "-7": 7.290074663187767e-05, "-8": 1.2720321678974673e-05, "-9": 1.9924484312423253e-06, "0": 0.16535029069260276, "1": 0.20413849258006975, "10": 0.00013022410552990927, "11": 3.121187690305646e-05, "12": 6.887182002586028e-06, "13": 1.4076476758304856e-06, "14": 2.6789540629522346e-07, "15": 4.769316405697678e-08, "16": 7.974506128678681e-09, "17": 1.2554567200887672e-09, "18": 1.8399595939098823e-10, "19": 2.1722519718976503e-11, "2": 0.1797124542237136, "3": 0.12679578238381708, "4": 0.07304990488859284, "5": 0.035338437202763, "6": 0.014679739823908649, "7": 0.0053312850487803355, "8": 0.00171750500429107, "9": 0.0004966918070761909} |
| Unadjusted home-win probability | 64.1% |
| Unadjusted draw probability | 16.5% |
| Unadjusted away-win probability | 19.3% |
| Raw p over 1 5 | 91.8% |
| Raw p under 3 5 | 39.8% |
| Raw p btts yes | 71.6% |
| Home training matches | 3 |
| Away training matches | 11 |
| P home draw | 80.7% |
| P draw away | 35.9% |
| P home away | 83.5% |
| Raw p home draw | 80.7% |
| Raw p draw away | 35.9% |
| Raw p home away | 83.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7877 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,446.0302 |
| Elo away rating | 1,431.4646 |
| Elo rating diff | 74.5656 |
| Elo home expectancy | 0.6057 |

</details>


---

## 2026-11-05 — h. beer-sheva vs ofi crete

The model's most likely 1X2 outcome is **ofi crete win** at **62.0%**. Expected goals are 0.34 for h. beer-sheva and 1.31 for ofi crete (1.65 combined). The most likely exact score is 0-1 at 25.6%. Goal-market probabilities: at least one goal: 81.2%; Over 2.5 goals: 23.0%; Under 3.5 goals: 91.4%; Double Chance 1X: 38.0%; Double Chance X2: 90.0%; Double Chance 12 (either team wins): 72.1%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 20.7%; BTTS No (at least one team does not score): 79.3%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| h. beer-sheva win | 10.0% | 9.98 |
| Draw | 27.9% | 3.58 |
| ofi crete win | 62.0% | 1.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| h. beer-sheva expected goals | 0.34 |
| ofi crete expected goals | 1.31 |
| Expected total goals | 1.65 |
| Over 0.5 | 81.2% |
| Under 0.5 | 18.8% |
| Over 1.5 | 48.7% |
| Under 1.5 | 51.3% |
| Over 2.5 | 23.0% |
| Under 2.5 | 77.0% |
| Over 3.5 | 8.6% |
| Under 3.5 | 91.4% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 25.56% |
| 2 | 0-0 | 18.78% |
| 3 | 0-2 | 16.44% |
| 4 | 1-1 | 8.15% |
| 5 | 0-3 | 7.17% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-144 |
| Matched home-team name | h. beer-sheva |
| Matched away-team name | ofi crete |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.3415 |
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
| P btts yes | 20.7% |
| P btts no | 79.3% |
| Fair Over 0.5 odds | 1.23 |
| Fair Under 0.5 odds | 5.33 |
| Fair Over 1.5 odds | 2.05 |
| Fair Under 1.5 odds | 1.95 |
| Fair Over 2.5 odds | 4.35 |
| Fair Under 2.5 odds | 1.30 |
| Fair Over 3.5 odds | 11.65 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.68 |
| Fair Under 4.5 odds | 1.03 |
| Goal margin distribution | {"-1": 0.31607495658041973, "-10": 8.10661337795566e-07, "-11": 9.610348621989953e-08, "-12": 1.0448942527866097e-08, "-13": 1.048630694371805e-09, "-14": 9.497409766151227e-11, "-2": 0.19030160401278812, "-3": 0.08008197343836661, "-4": 0.025631384639999196, "-5": 0.006610029410333405, "-6": 0.001426421310752068, "-7": 0.0002645300957173466, "-8": 4.2999873103164284e-05, "-9": 6.220686097621842e-06, "0": 0.27937375579777535, "1": 0.08566939805919323, "10": 1.1895692669985542e-12, "11": 3.680818848344117e-14, "12": 1.0445582650104702e-15, "13": 2.7361375262820974e-17, "14": 6.46808264277538e-19, "2": 0.012964402435809107, "3": 0.0014239667519781653, "4": 0.00011895759565247281, "5": 8.00716041139858e-06, "6": 4.5100149680283644e-07, "7": 2.183032901305178e-08, "8": 9.262055807838104e-10, "9": 3.497305202396215e-11} |
| Raw goal margin distribution | {"-1": 0.31607495658041973, "-10": 8.10661337795566e-07, "-11": 9.610348621989953e-08, "-12": 1.0448942527866097e-08, "-13": 1.048630694371805e-09, "-14": 9.497409766151227e-11, "-2": 0.19030160401278812, "-3": 0.08008197343836661, "-4": 0.025631384639999196, "-5": 0.006610029410333405, "-6": 0.001426421310752068, "-7": 0.0002645300957173466, "-8": 4.2999873103164284e-05, "-9": 6.220686097621842e-06, "0": 0.27937375579777535, "1": 0.08566939805919323, "10": 1.1895692669985542e-12, "11": 3.680818848344117e-14, "12": 1.0445582650104702e-15, "13": 2.7361375262820974e-17, "14": 6.46808264277538e-19, "2": 0.012964402435809107, "3": 0.0014239667519781653, "4": 0.00011895759565247281, "5": 8.00716041139858e-06, "6": 4.5100149680283644e-07, "7": 2.183032901305178e-08, "8": 9.262055807838104e-10, "9": 3.497305202396215e-11} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 62.0% |
| Raw p over 1 5 | 48.7% |
| Raw p under 3 5 | 91.4% |
| Raw p btts yes | 20.7% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 38.0% |
| P draw away | 90.0% |
| P home away | 72.1% |
| Raw p home draw | 38.0% |
| Raw p draw away | 90.0% |
| Raw p home away | 72.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.2296 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,422.3390 |
| Elo away rating | 1,425.2946 |
| Elo rating diff | 57.0445 |
| Elo home expectancy | 0.5814 |

</details>


---

## 2026-11-05 — leverkusen vs marseille

The model's most likely 1X2 outcome is **leverkusen win** at **84.7%**. Expected goals are 2.87 for leverkusen and 0.55 for marseille (3.42 combined). The most likely exact score is 2-0 at 13.5%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 66.4%; Under 3.5 goals: 55.4%; Double Chance 1X: 95.1%; Double Chance X2: 15.3%; Double Chance 12 (either team wins): 89.6%; Under 4.5 goals: 74.1%; BTTS Yes (both teams score): 39.8%; BTTS No (at least one team does not score): 60.2%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| leverkusen win | 84.7% | 1.18 |
| Draw | 10.4% | 9.62 |
| marseille win | 4.9% | 20.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| leverkusen expected goals | 2.87 |
| marseille expected goals | 0.55 |
| Expected total goals | 3.42 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 85.3% |
| Under 1.5 | 14.7% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.6% |
| Under 3.5 | 55.4% |
| Over 4.5 | 25.9% |
| Under 4.5 | 74.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.46% |
| 2 | 3-0 | 12.86% |
| 3 | 1-0 | 9.65% |
| 4 | 4-0 | 9.21% |
| 5 | 2-1 | 7.43% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-136 |
| Matched home-team name | leverkusen |
| Matched away-team name | marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8661 |
| Dc lambda away | 0.5521 |
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
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.14 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.79 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.97 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.86 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.039317849169944484, "-10": 2.743508750271002e-11, "-11": 1.3609383287569722e-12, "-12": 6.199552130823084e-14, "-13": 2.610562392774833e-15, "-14": 1.0219177293191926e-16, "-15": 3.737110898771033e-18, "-16": 1.2822058669009776e-19, "-17": 4.142760514959364e-21, "-18": 1.2611196231328767e-22, "-19": 3.3830415183449954e-24, "-2": 0.008209861416095535, "-3": 0.0013459312289015868, "-4": 0.00017277660545442908, "-5": 1.815554045286374e-05, "-6": 1.6116433143051986e-06, "-7": 1.2370010338267573e-07, "-8": 8.356923243937904e-09, "-9": 5.039510023589184e-10, "0": 0.10394499628925134, "1": 0.19322983353166187, "10": 0.0003897285660572411, "11": 0.00010035521006997874, "12": 2.37305270609207e-05, "13": 5.187125243801308e-06, "14": 1.054032930933388e-06, "15": 2.0008743670201895e-07, "16": 3.563585503201974e-08, "17": 5.9767465716402564e-09, "18": 9.444454641935214e-10, "19": 1.3151446375450894e-10, "2": 0.22122133263916222, "3": 0.18826068601350437, "4": 0.1254490258152449, "5": 0.06842851675937928, "6": 0.031531342709340174, "7": 0.01256287925015857, "8": 0.004405661492394699, "9": 0.0013791090685399423} |
| Raw goal margin distribution | {"-1": 0.039317849169944484, "-10": 2.743508750271002e-11, "-11": 1.3609383287569722e-12, "-12": 6.199552130823084e-14, "-13": 2.610562392774833e-15, "-14": 1.0219177293191926e-16, "-15": 3.737110898771033e-18, "-16": 1.2822058669009776e-19, "-17": 4.142760514959364e-21, "-18": 1.2611196231328767e-22, "-19": 3.3830415183449954e-24, "-2": 0.008209861416095535, "-3": 0.0013459312289015868, "-4": 0.00017277660545442908, "-5": 1.815554045286374e-05, "-6": 1.6116433143051986e-06, "-7": 1.2370010338267573e-07, "-8": 8.356923243937904e-09, "-9": 5.039510023589184e-10, "0": 0.10394499628925134, "1": 0.19322983353166187, "10": 0.0003897285660572411, "11": 0.00010035521006997874, "12": 2.37305270609207e-05, "13": 5.187125243801308e-06, "14": 1.054032930933388e-06, "15": 2.0008743670201895e-07, "16": 3.563585503201974e-08, "17": 5.9767465716402564e-09, "18": 9.444454641935214e-10, "19": 1.3151446375450894e-10, "2": 0.22122133263916222, "3": 0.18826068601350437, "4": 0.1254490258152449, "5": 0.06842851675937928, "6": 0.031531342709340174, "7": 0.01256287925015857, "8": 0.004405661492394699, "9": 0.0013791090685399423} |
| Unadjusted home-win probability | 84.7% |
| Unadjusted draw probability | 10.4% |
| Unadjusted away-win probability | 4.9% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 55.4% |
| Raw p btts yes | 39.8% |
| Home training matches | 24 |
| Away training matches | 17 |
| P home draw | 95.1% |
| P draw away | 15.3% |
| P home away | 89.6% |
| Raw p home draw | 95.1% |
| Raw p draw away | 15.3% |
| Raw p home away | 89.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6638 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,523.2260 |
| Elo away rating | 1,423.2467 |
| Elo rating diff | 159.9793 |
| Elo home expectancy | 0.7152 |

</details>


---

## 2026-11-05 — levski sofia vs jagiellonia

The model's most likely 1X2 outcome is **levski sofia win** at **81.4%**. Expected goals are 2.26 for levski sofia and 0.35 for jagiellonia (2.61 combined). The most likely exact score is 2-0 at 18.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.3%; Double Chance 1X: 95.3%; Double Chance X2: 18.6%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 26.3%; BTTS No (at least one team does not score): 73.7%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| levski sofia win | 81.4% | 1.23 |
| Draw | 13.9% | 7.22 |
| jagiellonia win | 4.7% | 21.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| levski sofia expected goals | 2.26 |
| jagiellonia expected goals | 0.35 |
| Expected total goals | 2.61 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 18.74% |
| 2 | 1-0 | 16.87% |
| 3 | 3-0 | 14.12% |
| 4 | 4-0 | 7.98% |
| 5 | 0-0 | 7.04% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-135 |
| Matched home-team name | levski sofia |
| Matched away-team name | jagiellonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2604 |
| Dc lambda away | 0.3519 |
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
| P btts yes | 26.3% |
| P btts no | 73.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.20 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.75 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.04 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.040461039526463016, "-10": 6.333301030755642e-13, "-11": 2.0142010310686854e-14, "-12": 5.877380264161615e-16, "-13": 1.584218604447303e-17, "-14": 3.9674551101231533e-19, "-15": 9.27774512853577e-21, "-16": 2.032784938602286e-22, "-17": 4.020150836659927e-24, "-2": 0.005874218778800327, "-3": 0.0006477725932969298, "-4": 5.486635597610863e-05, "-5": 3.763892761287966e-06, "-6": 2.1672576093981274e-07, "-7": 1.074518868334383e-08, "-8": 4.675788906367642e-10, "-9": 1.812505551534953e-11, "0": 0.13856971298299453, "1": 0.24405294574904743, "10": 7.567240678585393e-05, "11": 1.5457561086505238e-05, "12": 2.897027977924153e-06, "13": 5.015505948862686e-07, "14": 8.067563713075175e-08, "15": 1.211723586442037e-08, "16": 1.705231316033058e-09, "17": 2.1660324330738675e-10, "2": 0.2423324652935423, "3": 0.17163853310401006, "4": 0.09337467070856834, "5": 0.04114252571134957, "6": 0.01521580682678819, "7": 0.004845395561632452, "8": 0.0013542561888723922, "9": 0.00033717550743678914} |
| Raw goal margin distribution | {"-1": 0.040461039526463016, "-10": 6.333301030755642e-13, "-11": 2.0142010310686854e-14, "-12": 5.877380264161615e-16, "-13": 1.584218604447303e-17, "-14": 3.9674551101231533e-19, "-15": 9.27774512853577e-21, "-16": 2.032784938602286e-22, "-17": 4.020150836659927e-24, "-2": 0.005874218778800327, "-3": 0.0006477725932969298, "-4": 5.486635597610863e-05, "-5": 3.763892761287966e-06, "-6": 2.1672576093981274e-07, "-7": 1.074518868334383e-08, "-8": 4.675788906367642e-10, "-9": 1.812505551534953e-11, "0": 0.13856971298299453, "1": 0.24405294574904743, "10": 7.567240678585393e-05, "11": 1.5457561086505238e-05, "12": 2.897027977924153e-06, "13": 5.015505948862686e-07, "14": 8.067563713075175e-08, "15": 1.211723586442037e-08, "16": 1.705231316033058e-09, "17": 2.1660324330738675e-10, "2": 0.2423324652935423, "3": 0.17163853310401006, "4": 0.09337467070856834, "5": 0.04114252571134957, "6": 0.01521580682678819, "7": 0.004845395561632452, "8": 0.0013542561888723922, "9": 0.00033717550743678914} |
| Unadjusted home-win probability | 81.4% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 4.7% |
| Raw p over 1 5 | 73.2% |
| Raw p under 3 5 | 73.3% |
| Raw p btts yes | 26.3% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 95.3% |
| P draw away | 18.6% |
| P home away | 86.1% |
| Raw p home draw | 95.3% |
| Raw p draw away | 18.6% |
| Raw p home away | 86.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4847 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,427.6479 |
| Elo away rating | 1,424.2193 |
| Elo rating diff | 63.4285 |
| Elo home expectancy | 0.5903 |

</details>


---

## 2026-11-05 — lillestrøm vs viktoria plzen

The model's most likely 1X2 outcome is **viktoria plzen win** at **82.0%**. Expected goals are 0.46 for lillestrøm and 2.49 for viktoria plzen (2.95 combined). The most likely exact score is 0-2 at 16.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 56.5%; Under 3.5 goals: 65.9%; Double Chance 1X: 18.0%; Double Chance X2: 94.6%; Double Chance 12 (either team wins): 87.4%; Under 4.5 goals: 82.4%; BTTS Yes (both teams score): 33.6%; BTTS No (at least one team does not score): 66.4%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| lillestrøm win | 5.4% | 18.68 |
| Draw | 12.6% | 7.91 |
| viktoria plzen win | 82.0% | 1.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| lillestrøm expected goals | 0.46 |
| viktoria plzen expected goals | 2.49 |
| Expected total goals | 2.95 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 79.0% |
| Under 1.5 | 21.0% |
| Over 2.5 | 56.5% |
| Under 2.5 | 43.5% |
| Over 3.5 | 34.1% |
| Under 3.5 | 65.9% |
| Over 4.5 | 17.6% |
| Under 4.5 | 82.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 16.20% |
| 2 | 0-3 | 13.42% |
| 3 | 0-1 | 13.33% |
| 4 | 0-4 | 8.34% |
| 5 | 1-2 | 7.49% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-134 |
| Matched home-team name | lillestrøm |
| Matched away-team name | viktoria plzen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.4626 |
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
| P btts yes | 33.6% |
| P btts no | 66.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.24 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.76 |
| Fair Over 2.5 odds | 1.77 |
| Fair Under 2.5 odds | 2.30 |
| Fair Over 3.5 odds | 2.93 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.68 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.2240727115935616, "-10": 0.00014442430113084166, "-11": 3.235743215627692e-05, "-12": 6.654098207480407e-06, "-13": 1.264420071158413e-06, "-14": 2.2328986603874697e-07, "-15": 3.682784373598499e-08, "-16": 5.697434750359674e-09, "-17": 8.284898830629827e-10, "-18": 1.075444435881495e-10, "-2": 0.23369577228532218, "-3": 0.17752318571674217, "-4": 0.10452841107206362, "-5": 0.05009736026233025, "-6": 0.020212915631191885, "-7": 0.007035670996377795, "-8": 0.002152215782565979, "-9": 0.0005870187936047578, "0": 0.1263872231846382, "1": 0.04414918071270036, "10": 7.189423132395646e-12, "11": 2.997320584639154e-13, "12": 1.1469744148229269e-14, "13": 4.055657597443766e-16, "14": 1.33273649749835e-17, "15": 4.090316807845898e-19, "16": 1.1775121368715658e-20, "17": 3.186240976450232e-22, "18": 7.696349176271988e-24, "2": 0.008092106871050107, "3": 0.0011438556294059822, "4": 0.0001253302358053988, "5": 1.1177424050851e-05, "6": 8.39191787807715e-07, "7": 5.4355458280288145e-08, "8": 3.094060687996499e-09, "9": 1.5703642455668773e-10} |
| Raw goal margin distribution | {"-1": 0.2240727115935616, "-10": 0.00014442430113084166, "-11": 3.235743215627692e-05, "-12": 6.654098207480407e-06, "-13": 1.264420071158413e-06, "-14": 2.2328986603874697e-07, "-15": 3.682784373598499e-08, "-16": 5.697434750359674e-09, "-17": 8.284898830629827e-10, "-18": 1.075444435881495e-10, "-2": 0.23369577228532218, "-3": 0.17752318571674217, "-4": 0.10452841107206362, "-5": 0.05009736026233025, "-6": 0.020212915631191885, "-7": 0.007035670996377795, "-8": 0.002152215782565979, "-9": 0.0005870187936047578, "0": 0.1263872231846382, "1": 0.04414918071270036, "10": 7.189423132395646e-12, "11": 2.997320584639154e-13, "12": 1.1469744148229269e-14, "13": 4.055657597443766e-16, "14": 1.33273649749835e-17, "15": 4.090316807845898e-19, "16": 1.1775121368715658e-20, "17": 3.186240976450232e-22, "18": 7.696349176271988e-24, "2": 0.008092106871050107, "3": 0.0011438556294059822, "4": 0.0001253302358053988, "5": 1.1177424050851e-05, "6": 8.39191787807715e-07, "7": 5.4355458280288145e-08, "8": 3.094060687996499e-09, "9": 1.5703642455668773e-10} |
| Unadjusted home-win probability | 5.4% |
| Unadjusted draw probability | 12.6% |
| Unadjusted away-win probability | 82.0% |
| Raw p over 1 5 | 79.0% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 33.6% |
| Home training matches | 3 |
| Away training matches | 25 |
| P home draw | 18.0% |
| P draw away | 94.6% |
| P home away | 87.4% |
| Raw p home draw | 18.0% |
| Raw p draw away | 94.6% |
| Raw p home away | 87.4% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5651 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,400.8156 |
| Elo away rating | 1,451.8117 |
| Elo rating diff | 9.0039 |
| Elo home expectancy | 0.5130 |

</details>


---

## 2026-11-05 — milan vs ferencvaros

The model's most likely 1X2 outcome is **milan win** at **76.8%**. Expected goals are 2.92 for milan and 1.00 for ferencvaros (3.92 combined). The most likely exact score is 2-1 at 8.4%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 75.1%; Under 3.5 goals: 44.8%; Double Chance 1X: 89.8%; Double Chance X2: 23.2%; Double Chance 12 (either team wins): 86.9%; Under 4.5 goals: 64.4%; BTTS Yes (both teams score): 59.5%; BTTS No (at least one team does not score): 40.5%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| milan win | 76.8% | 1.30 |
| Draw | 13.1% | 7.66 |
| ferencvaros win | 10.2% | 9.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| milan expected goals | 2.92 |
| ferencvaros expected goals | 1.00 |
| Expected total goals | 3.92 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 90.0% |
| Under 1.5 | 10.0% |
| Over 2.5 | 75.1% |
| Under 2.5 | 24.9% |
| Over 3.5 | 55.2% |
| Under 3.5 | 44.8% |
| Over 4.5 | 35.6% |
| Under 4.5 | 64.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.45% |
| 2 | 2-0 | 8.45% |
| 3 | 3-1 | 8.23% |
| 4 | 3-0 | 8.23% |
| 5 | 1-0 | 6.07% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-127 |
| Matched home-team name | milan |
| Matched away-team name | ferencvaros |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9245 |
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
| P btts yes | 59.5% |
| P btts no | 40.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 59.30 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.98 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.01 |
| Fair Over 3.5 odds | 1.81 |
| Fair Under 3.5 odds | 2.23 |
| Fair Over 4.5 odds | 2.81 |
| Fair Under 4.5 odds | 1.55 |
| Goal margin distribution | {"-1": 0.0695870057824752, "-10": 7.081472904935827e-09, "-11": 6.300719076992183e-10, "-12": 5.155524186672562e-11, "-13": 3.903958134540332e-12, "-14": 2.7507261435840236e-13, "-15": 1.811993487644849e-14, "-16": 1.120574507180435e-15, "-17": 6.529700097216889e-17, "-18": 3.5955306461547655e-18, "-19": 1.8616315792304655e-19, "-2": 0.02380093902586712, "-20": 8.120803594554536e-21, "-3": 0.006530283927140145, "-4": 0.0014397039264972447, "-5": 0.0002638248810514851, "-6": 4.123733278644442e-05, "-7": 5.609282417493083e-06, "-8": 6.746089444122917e-07, "-9": 7.26564351544052e-08, "0": 0.1305259353708, "1": 0.1979451930369931, "10": 0.00032401204256851386, "11": 8.430851237126439e-05, "12": 2.0174273008763586e-05, "13": 4.467596809378304e-06, "14": 9.205765989199134e-07, "15": 1.7734255605550925e-07, "16": 3.207309161322547e-08, "17": 5.465590339653382e-09, "18": 8.801376355386158e-10, "19": 1.3326775760864954e-10, "2": 0.20355491937883513, "20": 1.7000986218201618e-11, "3": 0.16332901028892993, "4": 0.10530481045767415, "5": 0.056433180610858225, "6": 0.025796043464621235, "7": 0.010261564857758428, "8": 0.00360912678266415, "9": 0.001136757646951221} |
| Raw goal margin distribution | {"-1": 0.0695870057824752, "-10": 7.081472904935827e-09, "-11": 6.300719076992183e-10, "-12": 5.155524186672562e-11, "-13": 3.903958134540332e-12, "-14": 2.7507261435840236e-13, "-15": 1.811993487644849e-14, "-16": 1.120574507180435e-15, "-17": 6.529700097216889e-17, "-18": 3.5955306461547655e-18, "-19": 1.8616315792304655e-19, "-2": 0.02380093902586712, "-20": 8.120803594554536e-21, "-3": 0.006530283927140145, "-4": 0.0014397039264972447, "-5": 0.0002638248810514851, "-6": 4.123733278644442e-05, "-7": 5.609282417493083e-06, "-8": 6.746089444122917e-07, "-9": 7.26564351544052e-08, "0": 0.1305259353708, "1": 0.1979451930369931, "10": 0.00032401204256851386, "11": 8.430851237126439e-05, "12": 2.0174273008763586e-05, "13": 4.467596809378304e-06, "14": 9.205765989199134e-07, "15": 1.7734255605550925e-07, "16": 3.207309161322547e-08, "17": 5.465590339653382e-09, "18": 8.801376355386158e-10, "19": 1.3326775760864954e-10, "2": 0.20355491937883513, "20": 1.7000986218201618e-11, "3": 0.16332901028892993, "4": 0.10530481045767415, "5": 0.056433180610858225, "6": 0.025796043464621235, "7": 0.010261564857758428, "8": 0.00360912678266415, "9": 0.001136757646951221} |
| Unadjusted home-win probability | 76.8% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 10.2% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 59.5% |
| Home training matches | 9 |
| Away training matches | 33 |
| P home draw | 89.8% |
| P draw away | 23.2% |
| P home away | 86.9% |
| Raw p home draw | 89.8% |
| Raw p draw away | 23.2% |
| Raw p home away | 86.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7506 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,446.6112 |
| Elo away rating | 1,471.6144 |
| Elo rating diff | 34.9969 |
| Elo home expectancy | 0.5502 |

</details>


---

## 2026-11-05 — n.e.c. vs omonia

The model's most likely 1X2 outcome is **n.e.c. win** at **42.3%**. Expected goals are 2.30 for n.e.c. and 2.20 for omonia (4.50 combined). The most likely exact score is 2-2 at 7.1%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 82.6%; Under 3.5 goals: 34.3%; Double Chance 1X: 61.2%; Double Chance X2: 57.7%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 53.2%; BTTS Yes (both teams score): 79.7%; BTTS No (at least one team does not score): 20.3%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| n.e.c. win | 42.3% | 2.36 |
| Draw | 18.8% | 5.31 |
| omonia win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| n.e.c. expected goals | 2.30 |
| omonia expected goals | 2.20 |
| Expected total goals | 4.50 |
| Over 0.5 | 99.2% |
| Under 0.5 | 0.8% |
| Over 1.5 | 93.6% |
| Under 1.5 | 6.4% |
| Over 2.5 | 82.6% |
| Under 2.5 | 17.4% |
| Over 3.5 | 65.7% |
| Under 3.5 | 34.3% |
| Over 4.5 | 46.8% |
| Under 4.5 | 53.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.11% |
| 2 | 2-1 | 6.46% |
| 3 | 1-2 | 6.19% |
| 4 | 3-2 | 5.45% |
| 5 | 1-1 | 5.35% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-133 |
| Matched home-team name | n.e.c. |
| Matched away-team name | omonia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2974 |
| Dc lambda away | 2.2007 |
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
| P btts yes | 79.7% |
| P btts no | 20.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 120.25 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.62 |
| Fair Over 2.5 odds | 1.21 |
| Fair Under 2.5 odds | 5.75 |
| Fair Over 3.5 odds | 1.52 |
| Fair Under 3.5 odds | 2.92 |
| Fair Over 4.5 odds | 2.14 |
| Fair Under 4.5 odds | 1.88 |
| Goal margin distribution | {"-1": 0.17000532784736108, "-10": 1.2834079427460915e-05, "-11": 2.4757477525430035e-06, "-12": 4.40150636986823e-07, "-13": 7.254309594042017e-08, "-14": 1.1140504520364156e-08, "-15": 1.601021403444444e-09, "-16": 2.1567116406067653e-10, "-17": 2.6704432595842605e-11, "-18": 2.5489889842947703e-12, "-2": 0.11312443945568229, "-3": 0.06167672131253222, "-4": 0.027825766315816125, "-5": 0.0106342587236593, "-6": 0.0035108758146043394, "-7": 0.0010176489021537483, "-8": 0.00026245769533142645, "-9": 6.0901691463059775e-05, "0": 0.18843690887034456, "1": 0.17734895234586906, "10": 1.972653954753993e-05, "11": 3.9724752193506925e-06, "12": 7.372669339099046e-07, "13": 1.2684931500317328e-07, "14": 2.0335999281589036e-08, "15": 3.050889055956693e-09, "16": 4.2903228858130096e-10, "17": 5.5456169547014565e-11, "18": 5.525900888303216e-12, "2": 0.1232802984774737, "3": 0.07016606708184966, "4": 0.03304620612676106, "5": 0.013184094721201207, "6": 0.0045438834044332285, "7": 0.0013749227491356777, "8": 0.0003701760003997981, "9": 8.96699486466254e-05} |
| Raw goal margin distribution | {"-1": 0.17000532784736108, "-10": 1.2834079427460915e-05, "-11": 2.4757477525430035e-06, "-12": 4.40150636986823e-07, "-13": 7.254309594042017e-08, "-14": 1.1140504520364156e-08, "-15": 1.601021403444444e-09, "-16": 2.1567116406067653e-10, "-17": 2.6704432595842605e-11, "-18": 2.5489889842947703e-12, "-2": 0.11312443945568229, "-3": 0.06167672131253222, "-4": 0.027825766315816125, "-5": 0.0106342587236593, "-6": 0.0035108758146043394, "-7": 0.0010176489021537483, "-8": 0.00026245769533142645, "-9": 6.0901691463059775e-05, "0": 0.18843690887034456, "1": 0.17734895234586906, "10": 1.972653954753993e-05, "11": 3.9724752193506925e-06, "12": 7.372669339099046e-07, "13": 1.2684931500317328e-07, "14": 2.0335999281589036e-08, "15": 3.050889055956693e-09, "16": 4.2903228858130096e-10, "17": 5.5456169547014565e-11, "18": 5.525900888303216e-12, "2": 0.1232802984774737, "3": 0.07016606708184966, "4": 0.03304620612676106, "5": 0.013184094721201207, "6": 0.0045438834044332285, "7": 0.0013749227491356777, "8": 0.0003701760003997981, "9": 8.96699486466254e-05} |
| Unadjusted home-win probability | 42.3% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 38.8% |
| Raw p over 1 5 | 93.6% |
| Raw p under 3 5 | 34.3% |
| Raw p btts yes | 79.7% |
| Home training matches | 3 |
| Away training matches | 9 |
| P home draw | 61.2% |
| P draw away | 57.7% |
| P home away | 81.2% |
| Raw p home draw | 61.2% |
| Raw p draw away | 57.7% |
| Raw p home away | 81.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8262 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,432.8516 |
| Elo away rating | 1,467.0936 |
| Elo rating diff | 25.7579 |
| Elo home expectancy | 0.5370 |

</details>


---

## 2026-11-05 — real sociedad vs lyon

The model's most likely 1X2 outcome is **real sociedad win** at **56.5%**. Expected goals are 1.96 for real sociedad and 1.16 for lyon (3.12 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.0%; Double Chance 1X: 77.3%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| real sociedad win | 56.5% | 1.77 |
| Draw | 20.8% | 4.81 |
| lyon win | 22.7% | 4.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| real sociedad expected goals | 1.96 |
| lyon expected goals | 1.16 |
| Expected total goals | 3.12 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.84% |
| 2 | 1-1 | 9.53% |
| 3 | 1-0 | 9.15% |
| 4 | 2-0 | 8.48% |
| 5 | 3-1 | 6.44% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-128 |
| Matched home-team name | real sociedad |
| Matched away-team name | lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9624 |
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
| P btts yes | 58.5% |
| P btts no | 41.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.62 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.36 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.1410443758546341, "-10": 6.575650265548778e-08, "-11": 6.8184699211567e-09, "-12": 6.49758931115076e-10, "-13": 5.726937340152023e-11, "-14": 4.692875334991903e-12, "-15": 3.565879818981109e-13, "-16": 2.2632821330749723e-14, "-2": 0.059597372757325386, "-3": 0.019671099065889108, "-4": 0.005157173536895613, "-5": 0.0011159915033470082, "-6": 0.0002050674631447577, "-7": 3.269371002912875e-05, "-8": 4.598752811504133e-06, "-9": 5.783959227939723e-07, "0": 0.20805852302502745, "1": 0.23513436332339585, "10": 1.262204117281061e-05, "11": 2.2140983253942687e-06, "12": 3.5692857717042036e-07, "13": 5.321947463697015e-08, "14": 7.377449708988088e-09, "15": 9.483158969232e-10, "16": 1.0182258359078699e-10, "2": 0.17055532851434438, "3": 0.09523265479672592, "4": 0.0422365172508364, "5": 0.015461667550031824, "6": 0.0048063045955190654, "7": 0.0012962770332994315, "8": 0.00030845568224062523, "9": 6.562918636832938e-05} |
| Raw goal margin distribution | {"-1": 0.1410443758546341, "-10": 6.575650265548778e-08, "-11": 6.8184699211567e-09, "-12": 6.49758931115076e-10, "-13": 5.726937340152023e-11, "-14": 4.692875334991903e-12, "-15": 3.565879818981109e-13, "-16": 2.2632821330749723e-14, "-2": 0.059597372757325386, "-3": 0.019671099065889108, "-4": 0.005157173536895613, "-5": 0.0011159915033470082, "-6": 0.0002050674631447577, "-7": 3.269371002912875e-05, "-8": 4.598752811504133e-06, "-9": 5.783959227939723e-07, "0": 0.20805852302502745, "1": 0.23513436332339585, "10": 1.262204117281061e-05, "11": 2.2140983253942687e-06, "12": 3.5692857717042036e-07, "13": 5.321947463697015e-08, "14": 7.377449708988088e-09, "15": 9.483158969232e-10, "16": 1.0182258359078699e-10, "2": 0.17055532851434438, "3": 0.09523265479672592, "4": 0.0422365172508364, "5": 0.015461667550031824, "6": 0.0048063045955190654, "7": 0.0012962770332994315, "8": 0.00030845568224062523, "9": 6.562918636832938e-05} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 81.3% |
| Raw p under 3 5 | 62.0% |
| Raw p btts yes | 58.5% |
| Home training matches | 23 |
| Away training matches | 25 |
| P home draw | 77.3% |
| P draw away | 43.5% |
| P home away | 79.2% |
| Raw p home draw | 77.3% |
| Raw p draw away | 43.5% |
| Raw p home away | 79.2% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6037 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,487.8577 |
| Elo away rating | 1,510.1036 |
| Elo rating diff | 37.7541 |
| Elo home expectancy | 0.5541 |

</details>


---

## 2026-11-05 — sparta praha vs bournemouth

The model's most likely 1X2 outcome is **bournemouth win** at **94.5%**. Expected goals are 0.26 for sparta praha and 3.59 for bournemouth (3.85 combined). The most likely exact score is 0-3 at 16.5%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 73.8%; Under 3.5 goals: 46.4%; Double Chance 1X: 5.5%; Double Chance X2: 99.0%; Double Chance 12 (either team wins): 95.6%; Under 4.5 goals: 65.9%; BTTS Yes (both teams score): 21.9%; BTTS No (at least one team does not score): 78.1%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| sparta praha win | 1.0% | 95.75 |
| Draw | 4.4% | 22.67 |
| bournemouth win | 94.5% | 1.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| sparta praha expected goals | 0.26 |
| bournemouth expected goals | 3.59 |
| Expected total goals | 3.85 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 73.8% |
| Under 2.5 | 26.2% |
| Over 3.5 | 53.6% |
| Under 3.5 | 46.4% |
| Over 4.5 | 34.1% |
| Under 4.5 | 65.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-3 | 16.47% |
| 2 | 0-4 | 14.77% |
| 3 | 0-2 | 13.76% |
| 4 | 0-5 | 10.61% |
| 5 | 0-1 | 7.77% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T17:45:00+00:00 |
| Fixture id | uel-fd-129 |
| Matched home-team name | sparta praha |
| Matched away-team name | bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.2567 |
| Dc lambda away | 3.5893 |
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
| P btts yes | 21.9% |
| P btts no | 78.1% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 49.07 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.57 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.82 |
| Fair Over 3.5 odds | 1.87 |
| Fair Under 3.5 odds | 2.15 |
| Fair Over 4.5 odds | 2.93 |
| Fair Under 4.5 odds | 1.52 |
| Goal margin distribution | {"-1": 0.11886590685113471, "-10": 0.0022711064743400236, "-11": 0.0007359443125556031, "-12": 0.0002188378882712289, "-13": 6.0117262946107386e-05, "-14": 1.5345488939614395e-05, "-15": 3.6579237198435948e-06, "-16": 8.178131923574574e-07, "-17": 1.7214987428233637e-07, "-18": 3.4235151745379114e-08, "-19": 6.451595624871301e-09, "-2": 0.18507424560791183, "-20": 1.1542760861341797e-09, "-21": 1.889917130939657e-10, "-3": 0.20626432256946606, "-4": 0.1771590583563078, "-5": 0.12346139979481863, "-6": 0.0722948074938881, "-7": 0.03647644042055594, "-8": 0.016160630828129744, "-9": 0.006380164007952809, "0": 0.04411284250650496, "1": 0.00941676217925153, "10": 7.966361502906148e-15, "11": 1.8465867701647645e-16, "12": 3.927801513504751e-18, "13": 7.718421097496026e-20, "14": 1.4093285547014791e-21, "15": 2.4030810405653073e-23, "16": 3.84317478019168e-25, "17": 5.7868867754936346e-27, "18": 8.232140688348715e-29, "19": 1.1097110664067154e-30, "2": 0.0009470011159526874, "20": 1.420217068993187e-32, "21": 1.663374513582017e-34, "3": 7.549720420688026e-05, "4": 4.638444549672067e-06, "5": 2.3122908151611553e-07, "6": 9.68546808828903e-09, "7": 3.495652161585517e-10, "8": 1.1078381619234035e-11, "9": 3.128614877613219e-13} |
| Raw goal margin distribution | {"-1": 0.11886590685113471, "-10": 0.0022711064743400236, "-11": 0.0007359443125556031, "-12": 0.0002188378882712289, "-13": 6.0117262946107386e-05, "-14": 1.5345488939614395e-05, "-15": 3.6579237198435948e-06, "-16": 8.178131923574574e-07, "-17": 1.7214987428233637e-07, "-18": 3.4235151745379114e-08, "-19": 6.451595624871301e-09, "-2": 0.18507424560791183, "-20": 1.1542760861341797e-09, "-21": 1.889917130939657e-10, "-3": 0.20626432256946606, "-4": 0.1771590583563078, "-5": 0.12346139979481863, "-6": 0.0722948074938881, "-7": 0.03647644042055594, "-8": 0.016160630828129744, "-9": 0.006380164007952809, "0": 0.04411284250650496, "1": 0.00941676217925153, "10": 7.966361502906148e-15, "11": 1.8465867701647645e-16, "12": 3.927801513504751e-18, "13": 7.718421097496026e-20, "14": 1.4093285547014791e-21, "15": 2.4030810405653073e-23, "16": 3.84317478019168e-25, "17": 5.7868867754936346e-27, "18": 8.232140688348715e-29, "19": 1.1097110664067154e-30, "2": 0.0009470011159526874, "20": 1.420217068993187e-32, "21": 1.663374513582017e-34, "3": 7.549720420688026e-05, "4": 4.638444549672067e-06, "5": 2.3122908151611553e-07, "6": 9.68546808828903e-09, "7": 3.495652161585517e-10, "8": 1.1078381619234035e-11, "9": 3.128614877613219e-13} |
| Unadjusted home-win probability | 1.0% |
| Unadjusted draw probability | 4.4% |
| Unadjusted away-win probability | 94.5% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 46.4% |
| Raw p btts yes | 21.9% |
| Home training matches | 13 |
| Away training matches | 3 |
| P home draw | 5.5% |
| P draw away | 99.0% |
| P home away | 95.6% |
| Raw p home draw | 5.5% |
| Raw p draw away | 99.0% |
| Raw p home away | 95.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7385 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,456.4745 |
| Elo away rating | 1,460.7151 |
| Elo rating diff | 55.7595 |
| Elo home expectancy | 0.5796 |

</details>


---

## 2026-11-05 — sturm graz vs celje

The model's most likely 1X2 outcome is **sturm graz win** at **48.4%**. Expected goals are 1.01 for sturm graz and 0.48 for celje (1.48 combined). The most likely exact score is 1-0 at 23.4%. Goal-market probabilities: at least one goal: 77.8%; Over 2.5 goals: 18.6%; Under 3.5 goals: 93.7%; Double Chance 1X: 82.3%; Double Chance X2: 51.6%; Double Chance 12 (either team wins): 66.1%; Under 4.5 goals: 98.2%; BTTS Yes (both teams score): 23.4%; BTTS No (at least one team does not score): 76.6%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| sturm graz win | 48.4% | 2.06 |
| Draw | 33.9% | 2.95 |
| celje win | 17.7% | 5.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| sturm graz expected goals | 1.01 |
| celje expected goals | 0.48 |
| Expected total goals | 1.48 |
| Over 0.5 | 77.8% |
| Under 0.5 | 22.2% |
| Over 1.5 | 43.0% |
| Under 1.5 | 57.0% |
| Over 2.5 | 18.6% |
| Under 2.5 | 81.4% |
| Over 3.5 | 6.3% |
| Under 3.5 | 93.7% |
| Over 4.5 | 1.8% |
| Under 4.5 | 98.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 23.42% |
| 2 | 0-0 | 22.20% |
| 3 | 2-0 | 11.50% |
| 4 | 0-1 | 11.35% |
| 5 | 1-1 | 10.32% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-140 |
| Matched home-team name | sturm graz |
| Matched away-team name | celje |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0056 |
| Dc lambda away | 0.4751 |
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
| P btts yes | 23.4% |
| P btts no | 76.6% |
| Fair Over 0.5 odds | 1.29 |
| Fair Under 0.5 odds | 4.50 |
| Fair Over 1.5 odds | 2.32 |
| Fair Under 1.5 odds | 1.76 |
| Fair Over 2.5 odds | 5.37 |
| Fair Under 2.5 odds | 1.23 |
| Fair Over 3.5 odds | 15.81 |
| Fair Under 3.5 odds | 1.07 |
| Fair Over 4.5 odds | 56.55 |
| Fair Under 4.5 odds | 1.02 |
| Goal margin distribution | {"-1": 0.14147386323307368, "-10": 3.8380392743159646e-11, "-11": 1.6518079454007504e-12, "-12": 6.516319770295503e-14, "-13": 2.297178169546454e-15, "-2": 0.030017354834051966, "-3": 0.0045760211527617, "-4": 0.0005310591886245046, "-5": 4.96818125137274e-05, "-6": 3.8903202175898e-06, "-7": 2.6183786029760724e-07, "-8": 1.5448835625692516e-08, "-9": 8.112866431694233e-10, "0": 0.33898372757017164, "1": 0.29335389395956274, "10": 6.92097531060284e-08, "11": 6.304101904094018e-09, "12": 5.263466346577837e-10, "13": 3.927081654885201e-11, "2": 0.13445717927663836, "3": 0.04338158235353466, "4": 0.0106553098137739, "5": 0.00210972755064351, "6": 0.0003496391706753381, "7": 4.9805002144885264e-05, "8": 6.219307938565384e-06, "9": 6.912361184763666e-07} |
| Raw goal margin distribution | {"-1": 0.14147386323307368, "-10": 3.8380392743159646e-11, "-11": 1.6518079454007504e-12, "-12": 6.516319770295503e-14, "-13": 2.297178169546454e-15, "-2": 0.030017354834051966, "-3": 0.0045760211527617, "-4": 0.0005310591886245046, "-5": 4.96818125137274e-05, "-6": 3.8903202175898e-06, "-7": 2.6183786029760724e-07, "-8": 1.5448835625692516e-08, "-9": 8.112866431694233e-10, "0": 0.33898372757017164, "1": 0.29335389395956274, "10": 6.92097531060284e-08, "11": 6.304101904094018e-09, "12": 5.263466346577837e-10, "13": 3.927081654885201e-11, "2": 0.13445717927663836, "3": 0.04338158235353466, "4": 0.0106553098137739, "5": 0.00210972755064351, "6": 0.0003496391706753381, "7": 4.9805002144885264e-05, "8": 6.219307938565384e-06, "9": 6.912361184763666e-07} |
| Unadjusted home-win probability | 48.4% |
| Unadjusted draw probability | 33.9% |
| Unadjusted away-win probability | 17.7% |
| Raw p over 1 5 | 43.0% |
| Raw p under 3 5 | 93.7% |
| Raw p btts yes | 23.4% |
| Home training matches | 23 |
| Away training matches | 3 |
| P home draw | 82.3% |
| P draw away | 51.6% |
| P home away | 66.1% |
| Raw p home draw | 82.3% |
| Raw p draw away | 51.6% |
| Raw p home away | 66.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.1863 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,441.2526 |
| Elo away rating | 1,413.6182 |
| Elo rating diff | 87.6344 |
| Elo home expectancy | 0.6235 |

</details>


---

## 2026-11-05 — sunderland vs gnk dinamo

The model's most likely 1X2 outcome is **sunderland win** at **54.4%**. Expected goals are 1.48 for sunderland and 0.78 for gnk dinamo (2.25 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 39.2%; Under 3.5 goals: 80.9%; Double Chance 1X: 79.7%; Double Chance X2: 45.6%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| sunderland win | 54.4% | 1.84 |
| Draw | 25.3% | 3.96 |
| gnk dinamo win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| sunderland expected goals | 1.48 |
| gnk dinamo expected goals | 0.78 |
| Expected total goals | 2.25 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 65.2% |
| Under 1.5 | 34.8% |
| Over 2.5 | 39.2% |
| Under 2.5 | 60.8% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.10% |
| 2 | 2-0 | 11.45% |
| 3 | 1-1 | 11.45% |
| 4 | 0-0 | 9.89% |
| 5 | 2-1 | 8.90% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-141 |
| Matched home-team name | sunderland |
| Matched away-team name | gnk dinamo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4771 |
| Dc lambda away | 0.7773 |
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
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.11 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.88 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.22 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.74 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.14428726008662307, "-10": 2.584179241310571e-09, "-11": 1.8105066080313192e-10, "-12": 1.1642802839102868e-11, "-13": 6.917865663770088e-13, "-14": 3.8105724279627444e-14, "-15": 1.8342994010781058e-15, "-2": 0.04571648894915994, "-3": 0.01086086008519719, "-4": 0.001999922460692186, "-5": 0.00029974621949392443, "-6": 3.782004904485991e-05, "-7": 4.116699210507683e-06, "-8": 3.938014796619965e-07, "-9": 3.358842386526693e-08, "0": 0.2526945038249842, "1": 0.2687596512809428, "10": 1.586524965216262e-06, "11": 2.112208660220076e-07, "12": 2.5811109633031754e-08, "13": 2.9142961621768685e-09, "14": 3.050452090585702e-10, "15": 2.7903368832473306e-11, "2": 0.16508124074143024, "3": 0.0745249171739524, "4": 0.026077314736206142, "5": 0.007427041537503381, "6": 0.001780724171689302, "7": 0.0003683291832666615, "8": 6.695403657344406e-05, "9": 1.0851792336318616e-05} |
| Raw goal margin distribution | {"-1": 0.14428726008662307, "-10": 2.584179241310571e-09, "-11": 1.8105066080313192e-10, "-12": 1.1642802839102868e-11, "-13": 6.917865663770088e-13, "-14": 3.8105724279627444e-14, "-15": 1.8342994010781058e-15, "-2": 0.04571648894915994, "-3": 0.01086086008519719, "-4": 0.001999922460692186, "-5": 0.00029974621949392443, "-6": 3.782004904485991e-05, "-7": 4.116699210507683e-06, "-8": 3.938014796619965e-07, "-9": 3.358842386526693e-08, "0": 0.2526945038249842, "1": 0.2687596512809428, "10": 1.586524965216262e-06, "11": 2.112208660220076e-07, "12": 2.5811109633031754e-08, "13": 2.9142961621768685e-09, "14": 3.050452090585702e-10, "15": 2.7903368832473306e-11, "2": 0.16508124074143024, "3": 0.0745249171739524, "4": 0.026077314736206142, "5": 0.007427041537503381, "6": 0.001780724171689302, "7": 0.0003683291832666615, "8": 6.695403657344406e-05, "9": 1.0851792336318616e-05} |
| Unadjusted home-win probability | 54.4% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 20.3% |
| Raw p over 1 5 | 65.2% |
| Raw p under 3 5 | 80.9% |
| Raw p btts yes | 41.1% |
| Home training matches | 3 |
| Away training matches | 13 |
| P home draw | 79.7% |
| P draw away | 45.6% |
| P home away | 74.7% |
| Raw p home draw | 79.7% |
| Raw p draw away | 45.6% |
| Raw p home away | 74.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.3918 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,448.0520 |
| Elo away rating | 1,437.3148 |
| Elo rating diff | 70.7371 |
| Elo home expectancy | 0.6004 |

</details>


---

## 2026-11-05 — torreense vs ararat-armenia

The model's most likely 1X2 outcome is **torreense win** at **93.3%**. Expected goals are 4.80 for torreense and 0.93 for ararat-armenia (5.73 combined). The most likely exact score is 4-0 at 7.2%. Goal-market probabilities: at least one goal: 99.7%; Over 2.5 goals: 92.5%; Under 3.5 goals: 17.7%; Double Chance 1X: 97.6%; Double Chance X2: 6.7%; Double Chance 12 (either team wins): 95.7%; Under 4.5 goals: 32.2%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** Fixture Download UTC

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| torreense win | 93.3% | 1.07 |
| Draw | 4.3% | 23.22 |
| ararat-armenia win | 2.4% | 41.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| torreense expected goals | 4.80 |
| ararat-armenia expected goals | 0.93 |
| Expected total goals | 5.73 |
| Over 0.5 | 99.7% |
| Under 0.5 | 0.3% |
| Over 1.5 | 97.8% |
| Under 1.5 | 2.2% |
| Over 2.5 | 92.5% |
| Under 2.5 | 7.5% |
| Over 3.5 | 82.3% |
| Under 3.5 | 17.7% |
| Over 4.5 | 67.8% |
| Under 4.5 | 32.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-0 | 7.18% |
| 2 | 5-0 | 6.90% |
| 3 | 4-1 | 6.67% |
| 4 | 5-1 | 6.41% |
| 5 | 3-0 | 5.98% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-05T20:00:00+00:00 |
| Fixture id | uel-fd-143 |
| Matched home-team name | torreense |
| Matched away-team name | ararat-armenia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.8045 |
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
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 398.33 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 44.46 |
| Fair Over 2.5 odds | 1.08 |
| Fair Under 2.5 odds | 13.35 |
| Fair Over 3.5 odds | 1.21 |
| Fair Under 3.5 odds | 5.67 |
| Fair Over 4.5 odds | 1.48 |
| Fair Under 4.5 odds | 3.10 |
| Goal margin distribution | {"-1": 0.01779364912350564, "-10": 6.428429339562094e-10, "-11": 5.2616167428995723e-11, "-12": 3.966752429109999e-12, "-13": 2.771078324125135e-13, "-14": 1.8030897499512802e-14, "-15": 1.0977888486820174e-15, "-16": 6.279132385879351e-17, "-17": 3.3861955399316125e-18, "-18": 1.7272053705096086e-19, "-19": 8.356866644465086e-21, "-2": 0.005062674881801008, "-20": 3.8453712648285083e-22, "-21": 1.6867536069257645e-23, "-22": 7.068087392405593e-25, "-23": 2.832918860384844e-26, "-24": 1.0757617598446783e-27, "-25": 3.3950111244633313e-29, "-3": 0.0011969896108582666, "-4": 0.00023254524586882887, "-5": 3.8090491922825184e-05, "-6": 5.372445544859185e-06, "-7": 6.637598731897634e-07, "-8": 7.284652342495035e-08, "-9": 7.184205266787479e-09, "0": 0.04306688418299737, "1": 0.08891614527509625, "10": 0.00870534863016469, "11": 0.0036810238724870625, "12": 0.0014336813933482938, "13": 0.0005174096009622692, "14": 0.00017392866192848992, "15": 5.4706729904151776e-05, "16": 1.6165521132426812e-05, "17": 4.503708080044171e-06, "18": 1.186780245084818e-06, "19": 2.966456130300152e-07, "2": 0.13511896105294074, "20": 7.051814251211064e-08, "21": 1.598020566831194e-08, "22": 3.459399807967136e-09, "23": 7.163101605369275e-10, "24": 1.4052422778589436e-10, "25": 2.291102061745296e-11, "3": 0.16504211070604405, "4": 0.16564562992507922, "5": 0.14017069552921055, "6": 0.10213645931821096, "7": 0.06519103854667027, "8": 0.03696186402977836, "9": 0.018831802762787852} |
| Raw goal margin distribution | {"-1": 0.01779364912350564, "-10": 6.428429339562094e-10, "-11": 5.2616167428995723e-11, "-12": 3.966752429109999e-12, "-13": 2.771078324125135e-13, "-14": 1.8030897499512802e-14, "-15": 1.0977888486820174e-15, "-16": 6.279132385879351e-17, "-17": 3.3861955399316125e-18, "-18": 1.7272053705096086e-19, "-19": 8.356866644465086e-21, "-2": 0.005062674881801008, "-20": 3.8453712648285083e-22, "-21": 1.6867536069257645e-23, "-22": 7.068087392405593e-25, "-23": 2.832918860384844e-26, "-24": 1.0757617598446783e-27, "-25": 3.3950111244633313e-29, "-3": 0.0011969896108582666, "-4": 0.00023254524586882887, "-5": 3.8090491922825184e-05, "-6": 5.372445544859185e-06, "-7": 6.637598731897634e-07, "-8": 7.284652342495035e-08, "-9": 7.184205266787479e-09, "0": 0.04306688418299737, "1": 0.08891614527509625, "10": 0.00870534863016469, "11": 0.0036810238724870625, "12": 0.0014336813933482938, "13": 0.0005174096009622692, "14": 0.00017392866192848992, "15": 5.4706729904151776e-05, "16": 1.6165521132426812e-05, "17": 4.503708080044171e-06, "18": 1.186780245084818e-06, "19": 2.966456130300152e-07, "2": 0.13511896105294074, "20": 7.051814251211064e-08, "21": 1.598020566831194e-08, "22": 3.459399807967136e-09, "23": 7.163101605369275e-10, "24": 1.4052422778589436e-10, "25": 2.291102061745296e-11, "3": 0.16504211070604405, "4": 0.16564562992507922, "5": 0.14017069552921055, "6": 0.10213645931821096, "7": 0.06519103854667027, "8": 0.03696186402977836, "9": 0.018831802762787852} |
| Unadjusted home-win probability | 93.3% |
| Unadjusted draw probability | 4.3% |
| Unadjusted away-win probability | 2.4% |
| Raw p over 1 5 | 97.8% |
| Raw p under 3 5 | 17.7% |
| Raw p btts yes | 60.0% |
| Home training matches | 3 |
| Away training matches | 3 |
| P home draw | 97.6% |
| P draw away | 6.7% |
| P home away | 95.7% |
| Raw p home draw | 97.6% |
| Raw p draw away | 6.7% |
| Raw p home away | 95.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.9251 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Elo home rating | 1,421.4152 |
| Elo away rating | 1,403.0006 |
| Elo rating diff | 78.4146 |
| Elo home expectancy | 0.6110 |

</details>


---
