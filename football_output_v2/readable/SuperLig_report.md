# Super Lig — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
| Training data through | 2026-11-02 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-05T13:37:10.873510+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325677188807528, 'audit_candidate_poisson_score': 0.8249863531892144, 'audit_gain': 0.007581365691538333, 'audit_gain_lower95': -0.0033666616245295734, 'audit_baseline_briers': [0.5922611421709056, 0.1664906883092837, 0.22016705451566723, 0.2497257630051956], 'audit_candidate_briers': [0.5911071175486112, 0.16507678151874086, 0.21632127980415214, 0.24937363636848253], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1672.066 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 26.00 |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 3, 'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 7} |
| Legacy comparison status | {'None': 7} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **36.9%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 64.7%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 2.71 |
| Draw | 27.8% | 3.59 |
| Kasimpasa SK win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 2-1 | 8.54% |
| 3 | 1-0 | 8.08% |
| 4 | 1-2 | 8.08% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 37.4% | 2.61 | -3.8% |
| Draw | 27.8% | 28.0% | 3.46 | -3.6% |
| Kasimpasa SK win | 35.3% | 34.7% | 2.79 | -1.5% |
| Over 2.5 | 51.0% | 51.0% | 1.93 | -1.6% |
| Under 2.5 | 49.0% | 49.0% | 1.96 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:36:39Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:36:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3918 |
| Dc lambda away | 1.4143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.89 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.07760656822200959,0.07664841592014196,0.06012224195051573,0.0273643435370768,0.009341060058498864,0.002550922601837908,0.0005805199552491698,0.00011323749013105776,1.9327308085331812e-05,2.9322431595794582e-06,4.0037882761765904e-07,4.969921625942994e-08,5.655088629121096e-09,5.939736582802547e-10,5.7930899411329424e-11],[0.0808098185481256,0.13265482312164414,0.0807920066496142,0.036772085559109324,0.012552475787277459,0.003427918672426879,0.0007801001852746504,0.0001521680456158632,2.597195235391377e-05,3.940335575676203e-06,5.380273232304699e-07,6.678559016174604e-08,7.59928344828116e-09,7.981792127607506e-10,7.784729009790547e-11],[0.0625318071080635,0.08538313590040325,0.05549776544028393,0.024707084139152423,0.008433981122240423,0.0023032110845516585,0.0005241476141886805,0.0001022413781855831,1.745049817842717e-05,2.647502884986913e-06,3.6149938580041087e-07,4.487309246457592e-08,5.1059419855896444e-09,5.362948733517516e-10,5.230542454172797e-11],[0.028009989934868702,0.038245828607589155,0.02611110195473803,0.011314551336864532,0.0037778490222836413,0.0010316816717719807,0.00023478242636485735,4.579717277251056e-05,7.816634460787243e-06,1.1859009453039905e-06,1.6192709959960566e-07,2.0100088681382876e-08,2.2871141941769873e-09,2.4022357100195183e-10,2.3429267163525054e-11],[0.009409925593493804,0.012848644440636343,0.008771996245966062,0.003992531066591477,0.0012975428362411187,0.0003465923333110667,7.88749002727409e-05,1.5385510283430405e-05,2.6259898285783616e-06,3.9840213018687126e-07,5.439923264326914e-08,6.752602887549965e-09,7.68353521049913e-10,8.070284688384478e-11,7.871036770506139e-12],[0.0025290033986013235,0.0034531904779625936,0.0023575540633291436,0.0010730291686272789,0.0003662879723421003,9.523268855503861e-05,2.1198349431373064e-05,4.134996330142525e-06,7.057587368978761e-07,1.070742091679503e-07,1.4620290338029256e-08,1.8148236648998125e-09,2.0650202243958932e-10,2.1689626768904807e-11,2.1154129801928826e-12],[0.000566410623777873,0.0007733970518696559,0.0005280118122177443,0.00024032198654622697,8.203603008654049e-05,2.2402978034854933e-05,4.853867246074215e-06,9.260983405441669e-07,1.5806591901936267e-07,2.3980975920745222e-08,3.2744470706352763e-09,4.064586882924921e-10,4.6249419595912005e-11,4.857737650522347e-12,4.737804568872961e-13],[0.00010873430387837053,0.0001484696552754106,0.00010136285308018653,4.613480541639505e-05,1.5748522802960726e-05,4.300717746384789e-06,9.787252940845016e-07,1.8175910008048446e-07,3.034404184870219e-08,4.603647272140136e-09,6.285982428036608e-10,7.802820192887465e-11,8.878538349083517e-12,9.325438112905906e-13,9.09520160960459e-14],[1.8264585444960956e-05,2.4939109444200477e-05,1.702637001381826e-05,7.749468801096653e-06,2.6453495365027094e-06,7.224107200002987e-07,1.644008479692564e-07,3.2068388400990834e-08,5.210993595978086e-09,7.732951420236287e-10,1.055884473135768e-10,1.3106744701660709e-11,1.4913676412973842e-12,1.566435385611059e-13,1.5277615344242263e-14],[2.7270967002643835e-06,3.7236740619029594e-06,2.54221797817889e-06,1.1570780437342492e-06,3.9497879728952564e-07,1.078635973800304e-07,2.4546793649856315e-08,4.788151171274815e-09,8.172388202817393e-10,1.180428999458407e-10,1.576547724680704e-11,1.9569762661636482e-12,2.2267703724889373e-13,2.3388544920168695e-14,2.281110322418306e-15],[3.664660657918306e-07,5.003856972231197e-07,3.416221437098876e-07,1.5548764312621905e-07,5.307707860152106e-08,1.4494663196278147e-08,3.298587430286077e-09,6.434296671561058e-10,1.098201964206004e-10,1.666137458544318e-11,2.1659290184287226e-12,2.629776175664954e-13,2.992324319664638e-14,3.1429424708917663e-15,3.0653461075022677e-16],[4.476868197460456e-08,6.112873805987743e-08,4.173366795690788e-08,1.899487427589724e-08,6.484067895668053e-09,1.7707150198506794e-09,4.02966128153843e-10,7.860345290005705e-11,1.3415991020394408e-11,2.0354075034581084e-12,2.779217225885255e-13,3.2844541166386086e-14,3.65552034244933e-15,3.8395203561291927e-16,3.7447261244323447e-17],[5.013329973572422e-09,6.845377644490006e-09,4.67346008967094e-09,2.127102437494454e-09,7.261051810833089e-10,1.9828992706794354e-10,4.51253438677079e-11,8.802248113395009e-12,1.5023625208773156e-12,2.2793097753713533e-13,3.1122499942042164e-14,3.8632508725729334e-15,4.1850924561402473e-16,4.299608931181621e-17,4.193455535073788e-18],[5.182223818841804e-10,7.075991260348834e-10,4.83090407389268e-10,2.1987622946840088e-10,7.50566905476007e-11,2.049701073946388e-11,4.6645569523129775e-12,9.09878664940266e-13,1.552975543454555e-13,2.3560973386380576e-14,3.2170984425871573e-15,3.993399755361152e-16,4.543940779708554e-17,4.5438365624180756e-18,4.33472866770585e-19],[4.9741784125208465e-11,6.79191872154216e-11,4.6369627398081964e-11,2.1104908477160984e-11,7.204346683748085e-12,1.9674138343996824e-12,4.477293784920859e-13,8.733507025890424e-14,1.490629832570782e-14,2.2615095235833553e-15,3.0879449023195455e-16,3.833080845227354e-17,4.361519865664724e-18,4.581056248933646e-19,4.253740381784622e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1862941036456444, "-10": 4.725184543727672e-07, "-11": 5.785822384822637e-08, "-12": 6.505573266423575e-09, "-13": 6.718209483781602e-10, "-14": 5.7930899411329424e-11, "-2": 0.10644316297738236, "-3": 0.04247092872719786, "-4": 0.013341659935915016, "-5": 0.0034414942376756043, "-6": 0.0007513806612423135, "-7": 0.0001420258365231577, "-8": 2.3650033652418084e-05, "-9": 3.517513507728545e-06, "0": 0.27847152460318025, "1": 0.19668629004809984, "10": 4.324953445175311e-07, "11": 5.2118254934960994e-08, "12": 5.767298727005387e-09, "13": 5.86141569099602e-10, "14": 4.9741784125208465e-11, "2": 0.1107091671789652, "3": 0.04347300656277388, "4": 0.013440019280941535, "5": 0.0034119226577386842, "6": 0.0007331186209545863, "7": 0.00013637780605359087, "8": 2.23496235747709e-05, "9": 3.271420191986288e-06} |
| Raw goal margin distribution | {"-1": 0.19073437979343377, "-10": 6.367928941969443e-07, "-11": 8.068220055159464e-08, "-12": 9.387824295018447e-09, "-13": 1.002432906461092e-09, "-14": 8.878142303233073e-11, "-2": 0.11125392961444144, "-3": 0.04560109886870277, "-4": 0.014756377758956676, "-5": 0.003927349506676584, "-6": 0.0008855839099143945, "-7": 0.00017299827366134418, "-8": 2.978585969298326e-05, "-9": 4.582067658551438e-06, "0": 0.27542181527938137, "1": 0.18752971999772744, "10": 5.427742935299617e-07, "11": 6.768008620021634e-08, "12": 7.750152125496667e-09, "13": 8.144467515552741e-10, "14": 7.098908670084804e-11, "2": 0.1077555311876142, "3": 0.04346719613715096, "4": 0.01384293530978084, "5": 0.0036258520847905745, "6": 0.0008046413642033827, "7": 0.00015469508408551182, "8": 2.621241222236381e-05, "9": 3.9684458037971345e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.7% |
| P draw away | 63.1% |
| P home away | 72.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9655 |
| Totals anchor target over 2 5 | 0.5096 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-05T13:37:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5309 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.84, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.84, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.79, "draw": 3.46, "home": 2.61}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.95}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.34, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.39, "home": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.89, "under": 1.96}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.27, "under": 3.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:37:01Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0163 |
| Raw ev home | -0.0677 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | -0.0470 |
| Raw edge prob away | 0.0206 |
| Raw ev away | 0.0250 |
| Market p home draw | 66.0% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:36:39Z |
| Market reference home draw last update utc | 2026-11-05T13:37:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.5% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:36:39Z |
| Market reference draw away last update utc | 2026-11-05T13:37:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:36:39Z |
| Market reference home away last update utc | 2026-11-05T13:37:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.42 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **45.0%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 1-1 at 14.3%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.5%; Double Chance 1X: 55.0%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 69.9%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 24.9% | 4.02 |
| Draw | 30.1% | 3.32 |
| Kocaelispor win | 45.0% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.32% |
| 2 | 0-1 | 12.03% |
| 3 | 0-0 | 10.25% |
| 4 | 1-2 | 9.83% |
| 5 | 0-2 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 24.9% | 22.8% | 4.09 | +1.7% |
| Draw | 30.1% | 27.2% | 3.50 | +5.5% |
| Kocaelispor win | 45.0% | 49.9% | 2.00 | -10.0% |
| Over 2.5 | 43.4% | 43.7% | 2.20 | -4.6% |
| Under 2.5 | 56.6% | 56.3% | 1.73 | -2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:37:01Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:36:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7984 |
| Dc lambda away | 0.8688 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.76 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.31 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.45 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.24 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.10248152706194086,0.12028427320666998,0.08509054190833493,0.035657208803110026,0.011206620422616368,0.0028176819333239223,0.0005903750921313639,0.00010602720077511749,1.666151997651094e-05,2.327337772430871e-06,2.925814093286562e-07,3.343808148473232e-08,3.503058702931231e-09,3.3875941343985667e-10,3.0419400159294564e-11],[0.06952884549843172,0.14315290598902217,0.09831057890458693,0.04119706798120773,0.012947729754715117,0.0032554492640613514,0.0006820983363909918,0.00012250004823172525,1.9250126248880803e-05,2.6889230998278403e-06,3.3803813071030136e-07,3.863316738262281e-08,4.047309152090224e-09,3.9139055055645846e-10,3.514549058592371e-11],[0.04570824495535907,0.05746214789016256,0.04740831769498879,0.02379881189831411,0.007479672705912707,0.0018806150164677306,0.00039403605157840426,7.076609448835268e-05,1.1120454830059553e-05,1.5533429488483333e-06,1.9527860310112141e-07,2.2317692220099847e-08,2.338058360096351e-09,2.2609934512134877e-10,2.0302923497126198e-11],[0.017603225620989378,0.022129905774441565,0.013910312238506008,0.007651001874603701,0.0028805824056891568,0.0007242651839604428,0.00015175173593982432,2.7253540992688484e-05,4.282725700204508e-06,5.982256903990849e-07,7.520597898033365e-08,8.595022011322173e-09,9.004364282201778e-10,8.707570786881418e-11,7.819091357251861e-12],[0.005084534845399793,0.006392026067165644,0.0040178697251225595,0.0016836891212506887,0.0006945517326677792,0.0002091975439300077,4.383213655546945e-05,7.871942439494105e-06,1.237027152001882e-06,1.7279215944495398e-07,2.1722576812965887e-08,2.4825955114406795e-09,2.600830378435781e-10,2.5151042222564817e-11,2.2584748568982414e-12],[0.0011748980624668802,0.0014770238123838061,0.0009284206911398707,0.0003890548784700987,0.00012227514415545784,4.035253879756145e-05,1.0128417619046822e-05,1.8189923368074018e-06,2.8584341504137255e-07,3.99275803026544e-08,5.019498181319837e-09,5.736604714037087e-10,6.009813415270112e-11,5.811723525318986e-12,5.218722683945474e-13],[0.00022623922331153635,0.0002844167769114663,0.00017877736186645997,7.491668966227488e-05,2.3545390470687534e-05,5.920020384417065e-06,1.6280758577613267e-06,3.502664840768209e-07,5.504221538326032e-08,7.688483831026975e-09,9.665582115022693e-10,1.1046447657118632e-10,1.1572540314375488e-11,1.1191096985119218e-12,1.0049210262676752e-13],[3.734124769730824e-05,4.694357220850469e-05,2.9507570148144073e-05,1.2365153240864794e-05,3.886214975575155e-06,9.771115030890372e-07,2.0472938653451956e-07,4.82597235357747e-08,9.08483050971519e-09,1.2690000210785202e-09,1.5953241467715497e-10,1.823238835875121e-11,1.910071507676296e-12,1.847113504056249e-13,1.6586427591479887e-14],[5.392843311094182e-06,6.779616241954076e-06,4.26149933687224e-06,1.7857821593481236e-06,5.612492813949347e-07,1.4111497495587818e-07,2.9567129403570695e-08,5.3100478109579896e-09,1.0952446212012116e-09,1.8326967355043658e-10,2.3039758134713208e-11,2.633131447636407e-12,2.758535664737904e-13,2.66761137333382e-14,2.3954208980035816e-15],[6.922998803720504e-07,8.703252148301198e-07,5.470649360520056e-07,2.292476721405817e-07,7.204971254575114e-08,1.8115467972096105e-08,3.7956452595103874e-09,6.816711059884684e-10,1.0712040558277753e-10,1.9639588478668703e-11,2.9577016946977957e-12,3.3802513461729106e-13,3.541237526355295e-14,3.424514542892256e-15,3.0750932401781913e-16],[7.998586034188319e-08,1.005542728795651e-07,6.32059325930855e-08,2.6486458841628126e-08,8.32436695245447e-09,2.0929965934202334e-09,4.3853532297502575e-10,7.875784963791816e-11,1.237630980971038e-11,1.728765043288533e-12,2.8525854114911964e-13,3.905421909796484e-14,4.091419603716659e-15,3.95656202943909e-16,3.5528531120787974e-17],[8.401164708083465e-09,1.056152931220577e-08,6.638716492800934e-09,2.7819554895238684e-09,8.743342580698213e-10,2.1983396864925178e-10,4.606073452080628e-11,8.272182908760396e-12,1.2999224706119852e-12,1.8157759144135827e-13,2.2827037929662415e-14,3.42420344503394e-15,4.297345785090788e-16,4.1557006632160165e-17,3.731672579456079e-18],[8.088671856681505e-10,1.0168678734385179e-09,6.391780321618804e-10,2.678476837027247e-10,8.418121953706144e-11,2.1165694247666466e-11,4.434744228476357e-12,7.96448771240389e-13,1.2515700702534774e-13,1.7482356372355692e-14,2.197795492515504e-15,2.511781761327137e-16,3.453848956623664e-17,4.001123673602675e-18,3.592867896370803e-19],[7.188740866859775e-11,9.037329944279998e-11,5.680642412518683e-11,2.3804743523338668e-11,7.481536942412723e-12,1.881083741677245e-12,3.941342612753466e-13,7.078373225694175e-14,1.1123226496495518e-14,1.5537301046419282e-15,1.9532727441521323e-16,2.232325469028654e-17,2.3386410986606487e-18,2.968403328256765e-19,3.1931319175142916e-20],[5.9325821007511415e-12,7.45814918898838e-12,4.6880083899863165e-12,1.964510864351419e-12,6.174215063903755e-13,1.5523836430569856e-13,3.25263339858889e-14,5.841500073368622e-15,9.179556703723002e-16,1.2822316980001813e-16,1.6119583574451364e-17,1.8422494795525114e-18,1.9299875428749105e-19,1.866373085393795e-20,2.1997489134401448e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.24549393191439065, "-10": 3.3364196925410105e-07, "-11": 3.7719309073301144e-08, "-12": 3.9147521769848156e-09, "-13": 3.739049040257804e-10, "-14": 3.0419400159294564e-11, "-2": 0.13453725524290538, "-3": 0.050645470946772415, "-4": 0.01488463721905103, "-5": 0.003575007013962629, "-6": 0.0007246161288804793, "-7": 0.0001269084197811687, "-8": 1.9554582696704696e-05, "-9": 2.6886197047039838e-06, "0": 0.3014303343427751, "1": 0.1427134000611974, "10": 9.121098985128056e-08, "11": 9.476803516511522e-09, "12": 9.039284935009368e-10, "13": 7.934555785758612e-11, "14": 5.9325821007511415e-12, "2": 0.07226962809672768, "3": 0.02500262027462841, "4": 0.006753280984574523, "5": 0.0014906823812634125, "6": 0.00027768209123642083, "7": 4.469531123408403e-05, "8": 6.329242508836523e-06, "9": 7.997683542034259e-07} |
| Raw goal margin distribution | {"-1": 0.21522083315018156, "-10": 1.3570556961229089e-08, "-11": 1.0646858544244548e-09, "-12": 7.286966058726285e-11, "-2": 0.08920942418930883, "-3": 0.024466685098541836, "-4": 0.0051397753767608075, "-5": 0.0008732061143894046, "-6": 0.0001244083362811014, "-7": 1.5253442425170706e-05, "-8": 1.640808635085324e-06, "-9": 1.5718608568184218e-07, "0": 0.36951209576902466, "1": 0.19677264677562617, "10": 5.833298730261146e-09, "11": 4.20600402546913e-10, "12": 2.6456147377945966e-11, "2": 0.07534840184512065, "3": 0.018991973516542728, "4": 0.00366666098644953, "5": 0.0005724994065232, "6": 7.496169698353682e-05, "7": 8.446746274792475e-06, "8": 8.350474791111009e-07, "9": 7.351889823014741e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 55.0% |
| P draw away | 75.1% |
| P home away | 69.9% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.4470 |
| Totals anchor target over 2 5 | 0.4338 |
| Totals anchor reference over odds | 2.18 |
| Totals anchor reference under odds | 1.70 |
| Totals anchor reference last update utc | 2026-11-05T13:37:01Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.2528 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.51, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.03, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.0, "draw": 3.5, "home": 4.07}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.2, "under": 1.73}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.26, "home_away": 1.33, "home_draw": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.94, "draw": 3.46, "home": 4.09}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.18, "under": 1.7}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.37, "under": 3.07}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.09 |
| Reference draw odds | 3.46 |
| Reference away odds | 1.94 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Home probability edge | +2.0% |
| Draw probability edge | +2.9% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0670 |
| Raw ev home | 0.2083 |
| Raw edge prob draw | 0.0973 |
| Raw ev draw | 0.2933 |
| Raw edge prob away | -0.1642 |
| Raw ev away | -0.3299 |
| Market p home draw | 53.0% |
| Market home draw odds | 1.86 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:36:39Z |
| Market reference home draw last update utc | 2026-11-05T13:37:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 75.5% |
| Market draw away odds | 1.26 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:36:39Z |
| Market reference draw away last update utc | 2026-11-05T13:37:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:36:39Z |
| Market reference home away last update utc | 2026-11-05T13:37:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.25 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 69.6% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 2.94 |
| Market reference over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.5% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 3 5 odds | 1.24 |
| Market reference under 3 5 opposite odds | 3.90 |
| Market reference under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.6%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 73.5%; Under 3.5 goals: 47.6%; Double Chance 1X: 83.3%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 66.8%; BTTS Yes (both teams score): 69.4%; BTTS No (at least one team does not score): 30.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.6% | 1.55 |
| Draw | 18.7% | 5.35 |
| Amed SK win | 16.7% | 5.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 52.4% |
| Under 3.5 | 47.6% |
| Over 4.5 | 33.2% |
| Under 4.5 | 66.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.92% |
| 2 | 3-1 | 8.06% |
| 3 | 1-1 | 7.51% |
| 4 | 2-0 | 7.15% |
| 5 | 3-2 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.6% | 69.8% | 1.45 | -6.3% |
| Draw | 18.7% | 17.3% | 5.15 | -3.7% |
| Amed SK win | 16.7% | 12.9% | 6.79 | +13.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:36:39Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:37:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2145 |
| Dc lambda away | 1.5274 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.4% |
| P btts no | 30.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.23 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Score matrix json | [[0.0268594720409792,0.018580813592489604,0.018045125222618797,0.009187648622251151,0.003508408205730216,0.0010717804865305524,0.0002728477189530699,5.95371469705768e-05,1.1367468629103798e-05,1.9292432388287976e-06,2.946813962198761e-07,4.091907104976033e-08,5.208471015248091e-09,6.11973520957381e-10,6.676830137914359e-11,6.79899623425404e-12,6.490685255750743e-13,5.831863637125808e-14],[0.05507253258166338,0.07511002399004338,0.03996085775455113,0.020346011189347334,0.007769355963146859,0.0023734536079952685,0.0006042201841897245,0.00013184477424522684,2.5173213890893435e-05,4.272301449265244e-06,6.525707753191219e-07,9.061511945720603e-08,1.1534138266779279e-08,1.3552129186599617e-09,1.4785813681029954e-10,1.5056350013586936e-11,1.4373596582721648e-12,1.2914638738832915e-13],[0.07151563459107385,0.10923623640968123,0.057927746880117786,0.022528080270423908,0.008602603879374142,0.0026280017690661584,0.0006690215926728328,0.00014598486306679698,2.7872990824634914e-05,4.730497250433452e-06,7.225576881732528e-07,1.003334101140575e-07,1.2771151569021968e-08,1.500556798625571e-09,1.6371562679773596e-10,1.6671113493895865e-11,1.5915136120626077e-12,1.4299707960658357e-13],[0.052790362417623915,0.08063440312286727,0.06158232932314953,0.021771319985433586,0.0063501439807415305,0.0019398998081529316,0.0004938485485637148,0.00010776096545671011,2.0574875629772266e-05,3.4918890910201694e-06,5.333670384722758e-07,7.406264536144217e-08,9.427221385562939e-09,1.1076590130343409e-09,1.2084920061884849e-10,1.23060380891586e-11,1.1748001797617164e-12,1.0555548727572319e-13],[0.029226011697852362,0.04464114093923154,0.0340934555997385,0.017358632123876134,0.004602623089675854,0.0010739750948709434,0.00027340640973648716,5.965905693343465e-05,1.1390744982588566e-05,1.933193612394827e-06,2.9528479426455937e-07,4.1002858108524165e-08,5.219136029282586e-09,6.132266154203517e-10,6.690501806033149e-11,6.812918053161456e-12,6.503975768291454e-13,5.843805127700515e-14],[0.012944177242137587,0.01977152567317694,0.015099964259317413,0.007688124305685788,0.0029357977769651597,0.0006227389595424696,0.00012109148053977004,2.642294867424221e-05,5.044951856549436e-06,8.562099071508173e-07,1.3078139957596266e-07,1.816013311285838e-08,2.311551179555039e-09,2.71597578268966e-10,2.963217907098101e-11,3.0174359651940192e-12,2.880605673935286e-13,2.5882166244060763e-14],[0.004777471469823831,0.007297327443184296,0.005573135093469672,0.002837553429607356,0.0010835520758295093,0.0003310133550357577,5.8511895791723204e-05,9.752252389504926e-06,1.862004290457282e-06,3.160122367822304e-07,4.8269147862395337e-08,6.702590378046814e-09,8.531534762527811e-10,1.0024195877272724e-10,1.0936723706121347e-11,1.1136833161405447e-12,1.0631816271982563e-13,9.55265896743995e-15],[0.0015113844991915544,0.0023085574980023023,0.0017630979159947015,0.0008976786771464562,0.00034278882078513827,0.00010471825043570232,2.6658570596511058e-05,4.039138294493586e-06,5.890572952242202e-07,9.997254808203519e-08,1.527026217303599e-08,2.120408518563894e-09,2.699007095247796e-10,3.1712202493442734e-11,3.459904425547966e-12,3.5232103669373357e-13,3.363444954767992e-14,3.0220464487638957e-15],[0.00041836936734666674,0.0006390364202089232,0.00048804666190469003,0.00024848823078392344,9.488805936682563e-05,2.8987268433591333e-05,7.37941226788725e-06,1.6102357550779053e-06,2.1347616025427548e-07,2.76736010694088e-08,4.226991826347363e-09,5.869545247437564e-10,7.471175544720678e-11,8.77831822507629e-12,9.577430669500169e-13,9.752669112547077e-14,9.310419278378994e-15,8.365387242874914e-16],[0.00010294192150173179,0.0001572381778883572,0.00012008637601171427,6.114179943357811e-05,2.334769206632081e-05,7.132465578360086e-06,1.8157421113967657e-06,3.9620673891537527e-07,7.564802655871055e-08,8.914664377362548e-09,1.0400729468698251e-09,1.4442316127124898e-10,1.8383209347471407e-11,2.1599500732429152e-12,2.3565757751834127e-13,2.399694089898057e-14,2.2908762574601457e-15,2.0583462942067114e-16],[2.279644741370145e-05,3.4820331711001415e-05,2.6593080019464854e-05,1.3539827071745462e-05,5.17033708577339e-06,1.5794816544626676e-06,4.020953655756587e-07,8.773982413458784e-08,1.6752225276530557e-08,2.843123513649976e-09,3.015404863088638e-10,3.198245139794835e-11,4.070954369912814e-12,4.783200812904426e-13,5.218627644760608e-14,5.314112980532516e-15,5.073136325088786e-16,4.558199649914362e-17],[4.589331070502637e-06,7.0099532311539254e-06,5.353660865611018e-06,2.7258084534806364e-06,1.040880984747224e-06,3.179778015655928e-07,8.094896196116807e-08,1.7663590019701242e-08,3.372521453295958e-09,5.72371424445203e-10,8.742661739961104e-11,8.4294821268514e-12,8.195556543257813e-13,9.629435547015116e-14,1.0506027347528314e-14,1.0698256342811155e-15,1.0213127396171417e-16,9.176468113331174e-18],[8.469212776045752e-07,1.2936261200757037e-06,9.879717175575888e-07,5.030243280475149e-07,1.9208556538935378e-07,5.868004766157156e-08,1.4938429420697256e-08,3.2596624642576443e-09,6.223696077043808e-10,1.0562618617148278e-10,1.6133824596057203e-11,2.240321660678716e-12,1.9800631236678257e-13,1.7770288808551247e-14,1.938796301035387e-15,1.9742704962452252e-16,1.8847441533034667e-17,1.6934376664154884e-18],[1.4426952212700414e-07,2.2036383674548507e-07,1.6829687874907499e-07,8.568810507504516e-08,3.272097827627867e-08,9.995902403667538e-09,2.5446994081287088e-09,5.55269962450218e-10,1.0601807778857604e-10,1.7992982117722477e-11,2.748330011423843e-12,3.8162949018243986e-13,4.857652158725597e-14,3.9630811438653114e-15,3.3026589749062117e-16,3.363087793098603e-17,3.2105833861894145e-18,2.8847007312963018e-19],[2.2820305764857563e-08,3.4856774042837474e-08,2.6620911857904988e-08,1.3553997610821504e-08,5.175748267417146e-09,1.5811347115058525e-09,4.025161913410096e-10,8.78316510537823e-11,1.6769757853692277e-11,2.846099075496867e-12,4.34726131193632e-13,6.036549873079443e-14,7.683750935547685e-15,9.028085402454157e-16,6.839392484116065e-17,5.31967463543742e-18,5.078445778167606e-19,4.562970179546184e-20],[3.3690317332601396e-09,5.1460124627357625e-09,3.9301268677879535e-09,2.0010182393660304e-09,7.641115914909121e-10,2.3342776702955284e-10,5.942469990332907e-11,1.2966856037508089e-11,2.475770787225048e-12,4.2017833591508583e-13,6.417995211633827e-14,8.911943727384603e-15,1.1343757177956904e-15,1.332843938414273e-16,1.454176083177403e-17,1.0281953661054082e-18,7.497465265621272e-20,6.736452828990726e-21],[4.662942075854417e-10,7.122390032266572e-10,5.439531410266874e-10,2.7695293133564335e-10,1.0575762927478303e-10,3.230780362824202e-11,8.224735041486749e-12,1.7946906825461665e-12,3.426615326876617e-13,5.815520294921663e-14,8.882890481414399e-15,1.2334664875315909e-15,1.5700440610627668e-16,1.8447359873827393e-17,2.0126669562080705e-18,2.0494927642925955e-19,1.3585521387485776e-20,9.323654932722452e-22],[6.0741568286417e-11,9.277943698842611e-11,7.085776817038701e-11,3.607712709526817e-11,1.377646163281306e-11,4.2085589491467715e-12,1.0713907593814846e-12,2.337844323895003e-13,4.463662329123419e-14,7.575556748692857e-15,1.1571250296063983e-15,1.6067685950758575e-16,2.045209590776503e-17,2.4030355755059986e-18,2.6217899637092647e-19,2.6697609078059442e-20,2.5486964786614543e-21,1.5900804622296e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.08862533222979574, "-10": 3.9924535805337316e-07, "-11": 5.408172584706355e-08, "-12": 6.740381878538021e-09, "-13": 7.777360094926152e-10, "-14": 8.352172049206886e-11, "-15": 8.379352972132788e-12, "-16": 7.782149129634035e-13, "-17": 5.831863637125808e-14, "-2": 0.049235435810326675, "-3": 0.020143890800143577, "-4": 0.006670941793226129, "-5": 0.0018446313659392984, "-6": 0.0004363717038892644, "-7": 9.001764336139038e-05, "-8": 1.644189244407229e-05, "-9": 2.692218652596336e-06, "0": 0.1869566986808751, "1": 0.2465448889575893, "10": 3.088547810204193e-05, "11": 6.0656055577241155e-06, "12": 1.0960170106355553e-06, "13": 1.8334715243059804e-07, "14": 2.854634849571528e-08, "15": 4.152128504657183e-09, "16": 5.590736445738678e-10, "17": 6.0741568286417e-11, "2": 0.19512768090575738, "3": 0.11574270409789199, "4": 0.05557079206635259, "5": 0.02227810232337533, "6": 0.007640721254950102, "7": 0.0022851493185824887, "8": 0.0006051289310090469, "9": 0.00014365330178340674} |
| Raw goal margin distribution | {"-1": 0.13582974427235672, "-10": 6.118949686496442e-07, "-11": 8.288721527798865e-08, "-12": 1.0330503974709407e-08, "-13": 1.1919806744066473e-09, "-14": 1.2800780149640874e-10, "-15": 1.2842438417285378e-11, "-16": 1.1927146556999378e-12, "-17": 8.938082673790393e-14, "-2": 0.07545965117416317, "-3": 0.030873108931645778, "-4": 0.010224078094062679, "-5": 0.002827135316826111, "-6": 0.0006687958787368483, "-7": 0.000137963640531969, "-8": 2.5199319312465155e-05, "-9": 4.126172076390668e-06, "0": 0.21886237528100685, "1": 0.20040578466119002, "10": 2.5105482818345737e-05, "11": 4.930471065048448e-06, "12": 8.909053030753123e-07, "13": 1.490350503861773e-07, "14": 2.3204104508853578e-08, "15": 3.375087492213462e-09, "16": 4.544470294960795e-10, "17": 4.937422027063254e-11, "2": 0.15861093761210934, "3": 0.0940822887532504, "4": 0.045171117662946014, "5": 0.018108915564038826, "6": 0.006210815178322814, "7": 0.0018575000446968716, "8": 0.0004918834000282857, "9": 0.00011676961864752604} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.3% |
| P draw away | 35.4% |
| P home away | 81.3% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7348 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.79, "draw": 5.15, "home": 1.4}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.79 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:21Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:21Z |
| Home probability edge | -5.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | +4.7% |
| Under 2.5 probability edge | -4.7% |
| Raw edge prob home | -0.1727 |
| Raw ev home | -0.2386 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1271 |
| Raw edge prob away | 0.1271 |
| Raw ev away | 0.7386 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.6%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 58.6%; BTTS No (at least one team does not score): 41.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 44.9% | 2.23 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.15% |
| 2 | 2-1 | 9.87% |
| 3 | 1-0 | 8.39% |
| 4 | 2-0 | 7.31% |
| 5 | 1-2 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 55.1% | 58.4% | 1.67 | -7.9% |
| Under 2.5 | 44.9% | 41.6% | 2.31 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:36:39Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:36:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5168 |
| Dc lambda away | 1.3496 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.6% |
| P btts no | 41.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.43 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Score matrix json | [[0.06482395535950398,0.05876311051455164,0.04644775303553761,0.02089453310191705,0.0070495581327649146,0.0019027472736463256,0.0004279756640043178,8.251069606419253e-05,1.3919046327626612e-05,2.0871621354657225e-06,2.8167311965676615e-07,3.455746963740808e-08,3.886421549309731e-09,4.034556202465817e-10,3.8891702095963033e-11,3.4990883464793154e-12],[0.0838696497910722,0.12150649833480631,0.07045419053320257,0.031693834901732464,0.010693109556466582,0.0028861787749224826,0.0006491741151022739,0.00012515620071192754,2.1113080351955242e-05,3.1659081259168583e-06,4.2725536421957227e-07,5.2418435576775594e-08,5.895111527093978e-09,6.119809308923027e-10,5.899280827498954e-11,5.307585856020709e-12],[0.07312820108407873,0.09869021761284283,0.05671251986879793,0.02403736819288183,0.008109911985487136,0.0021889475381693256,0.0004923492936207801,9.492147881323043e-05,1.6012668952159713e-05,2.4011010192818347e-06,3.240407648355706e-07,3.9755404795931976e-08,4.470994650985386e-09,4.641410863813373e-10,4.47415674889029e-11,4.0254010230086685e-12],[0.036974793366832674,0.04989935961048923,0.03367085875009202,0.012899348365374947,0.004100501796042016,0.001106767043559465,0.0002489397130800994,4.7993824723763145e-05,8.096262686359247e-06,1.214035252128828e-06,1.638402168330404e-07,2.010097138659693e-08,2.260606727824877e-09,2.346771902986622e-10,2.2622055353287708e-11,2.0353074304843935e-12],[0.0140212871804557,0.018922438437400664,0.012768395362314408,0.00574386578726681,0.0016503616592577406,0.00041969939914610825,9.440093885277381e-05,1.8199836647200246e-05,3.070200368332039e-06,4.60376796387041e-07,6.213018445114242e-08,7.622530560790566e-09,8.572493108598552e-10,8.899241835470635e-11,8.578555979305078e-12,7.718131025158353e-13],[0.00425363284108386,0.005740493332374574,0.0038735435015402244,0.0017425144947856377,0.0005879029298362163,0.00013513581141368213,2.8638378813966885e-05,5.521277887582394e-06,9.314055797707786e-07,1.3966434287962783e-07,1.8848411675951995e-08,2.3124443503831257e-09,2.6006341463091526e-10,2.699759789876512e-11,2.6024734372113797e-12,2.3414466288204805e-13],[0.0010753525522706386,0.0014512428286331917,0.0009792629139216543,0.0004405216621514644,0.00014862658337142022,4.011582300271369e-05,7.684211141100034e-06,1.3958234032005195e-06,2.3546681268108877e-07,3.5308267823731623e-08,4.765029883683627e-09,5.846045079750427e-10,6.574612034552385e-11,6.825209624396243e-12,6.579261909706103e-13,5.919365169434817e-14],[0.00023302094029353847,0.00031447358153221936,0.00021219902674224096,9.545778425638789e-05,3.220628075573495e-05,8.692801981083592e-06,1.955229552258349e-06,3.2102181528268334e-07,5.10239158153416e-08,7.65104035048718e-09,1.0325467137993288e-09,1.266794707099012e-10,1.424669774690822e-11,1.4789724179471274e-12,1.425677368226801e-13,1.2826826279530491e-14],[4.418217419771078e-05,5.9626085717154736e-05,4.023421393931416e-05,1.8099371014597924e-05,6.106504869552786e-06,1.6482076285102458e-06,3.7072330308842144e-07,7.147284380341229e-08,1.0268001156360376e-08,1.4506833468833634e-09,1.9577707788359131e-10,2.4019190872408715e-11,2.7012597271434447e-12,2.8042208104144984e-13,2.70317018519374e-14,2.4320435424047826e-15],[7.446405705962471e-06,1.0049302302815e-05,6.781021660725493e-06,3.0504442582279458e-06,1.0291823236367917e-06,2.777867525176134e-07,6.248121939625845e-08,1.2045939376760448e-08,2.0320757943244865e-09,2.594969314602146e-10,3.299601199627177e-11,4.048162934774113e-12,4.552667724199454e-13,4.7261969838802456e-14,4.55588758514678e-15,4.098934296504244e-16],[1.1295067083094562e-06,1.5243266097857728e-06,1.0285780492524477e-06,4.627060878825949e-07,1.5611133539104114e-07,4.2136033522442664e-08,9.47745251039972e-09,1.8271861447255568e-09,3.0823505085748033e-10,4.6219871091037734e-11,5.312067236221484e-12,6.140448656317277e-13,6.905705837475011e-14,7.168923382471903e-15,6.910589877753554e-16,6.21746110491146e-17],[1.55753656009383e-07,2.1019746113935904e-07,1.4183606921808196e-07,6.380499054616344e-08,2.15270179918223e-08,5.810360595978252e-09,1.3068960700192975e-09,2.5196036478317616e-10,4.25041619745188e-11,6.373502565103136e-12,8.601365079155274e-13,8.98689214778409e-14,9.522643146776134e-15,9.885607745901364e-16,9.5293780083213e-17,8.573586071352339e-18],[1.9687887715350553e-08,2.6569803361239613e-08,1.79286488439415e-08,8.065207082369828e-09,2.7211015389827927e-09,7.34452917062992e-10,1.6519691249252478e-10,3.184880212552507e-11,5.372696794603567e-12,8.056363238606097e-13,1.0872470940068639e-13,1.3339046510823075e-14,1.2775513767121877e-15,1.249580525336631e-16,1.2045516556841423e-17,1.0837357158441895e-18],[2.297195155419407e-09,3.1001814132806333e-09,2.091926054383474e-09,9.410534489501664e-10,3.1749984371770696e-10,8.569642956899174e-11,1.927527993631259e-11,3.716138318465861e-12,6.268896504563862e-13,9.400215436821631e-14,1.268606766356664e-14,1.5564083595765926e-15,1.75037670629578e-16,1.5474727366379333e-17,1.4054784687402242e-18,1.2645096681708328e-19],[2.488925952811018e-10,3.3589318520601485e-10,2.2665244769619872e-10,1.0195965921958258e-10,3.439993329161306e-11,9.284891060052912e-12,2.0884052609986883e-12,4.0262983679227376e-13,6.792117408434379e-14,1.0184785610192771e-14,1.374488491867072e-15,1.686310869228241e-16,1.8964683959121635e-17,1.9687540922746243e-18,1.6162117942039436e-19,1.3700494375786836e-20],[2.5168818990836666e-11,3.396659819934656e-11,2.2919823803729064e-11,1.0310488362929271e-11,3.4786317902933828e-12,9.389180187388772e-13,2.111862505761659e-13,4.0715222849798824e-14,6.868407371634473e-15,1.0299182472419799e-15,1.3899269288312622e-16,1.7052517364749688e-17,1.9177697803603504e-18,1.9908673992476687e-19,1.9191261174347477e-20,1.4704392620109558e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1578049571462602, "-10": 3.3880603977546796e-07, "-11": 4.0940116119339205e-08, "-12": 4.545179355121421e-09, "-13": 4.664738295445799e-10, "-14": 4.4199287951983745e-11, "-15": 3.4990883464793154e-12, "-2": 0.08745843250080537, "-3": 0.03404469751715629, "-4": 0.010479294785201728, "-5": 0.0026554189545924976, "-6": 0.0005704230788018698, "-7": 0.00010619660721644746, "-8": 1.7429981107427412e-05, "-9": 2.556525165294495e-06, "0": 0.2577358351650123, "1": 0.22260463947567816, "10": 1.3586092105930172e-06, "11": 1.8452082371601596e-07, "12": 2.302503206469031e-08, "13": 2.656008164429151e-09, "14": 2.8285919348044835e-10, "15": 2.5168818990836666e-11, "2": 0.13769617302098183, "3": 0.06024521580803746, "4": 0.020842895237511348, "5": 0.005936246725213135, "6": 0.001433272882678389, "7": 0.0002999130349149884, "8": 5.532666846741343e-05, "9": 9.120960587969723e-06} |
| Raw goal margin distribution | {"-1": 0.17605287803319172, "-10": 3.7798418678454525e-07, "-11": 4.5674263978554265e-08, "-12": 5.0707653366333825e-09, "-13": 5.204149584627549e-10, "-14": 4.931031313390478e-11, "-15": 3.903708635205473e-12, "-2": 0.0975717685203485, "-3": 0.03798148732494913, "-4": 0.011691077644557407, "-5": 0.0029624807597558906, "-6": 0.0006363844744531414, "-7": 0.00011847674924741156, "-8": 1.9445512951679018e-05, "-9": 2.852151296471764e-06, "0": 0.2709176523075331, "1": 0.19927018579895245, "10": 1.2161934740476009e-06, "11": 1.6517849274064075e-07, "12": 2.0611441110862313e-08, "13": 2.3775930351494718e-09, "14": 2.532085772001589e-10, "15": 2.253050632034203e-11, "2": 0.12326221971979033, "3": 0.053930032077688525, "4": 0.018658046015347252, "5": 0.005313981733120573, "6": 0.001283030552753275, "7": 0.0002684747556556081, "8": 4.9527069746195055e-05, "9": 8.164859076210915e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 70.7% |
| P draw away | 55.1% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0673 |
| Raw ev home | -0.1597 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.1%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.71% |
| 2 | 1-0 | 9.05% |
| 3 | 0-0 | 8.61% |
| 4 | 2-1 | 8.58% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.37 | -1.8% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.9% | 30.8% | 3.18 | -5.0% |
| Over 2.5 | 48.5% | 48.5% | 1.98 | -4.0% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:37:01Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:36:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4119 |
| Dc lambda away | 1.0826 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.61 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.02 |
| Fair Under 4.5 odds | 1.14 |
| Score matrix json | [[0.0861077232817139,0.07585768720379021,0.05037866350676984,0.019111569769643684,0.005437601064152035,0.0012376798217729485,0.0002347621256676971,3.816813733370454e-05,5.42977648314658e-06,6.866104607775858e-07,7.814143614957952e-08,8.084621209850956e-09,7.667422652669494e-10,6.712387567078241e-11,5.456572898388618e-12,4.1399936557144913e-13],[0.0904500409841616,0.13714088426969662,0.07477662554507493,0.028367141896314466,0.008070985419908137,0.0018370777256719825,0.00034845544405639545,5.6652644482557374e-05,8.059371460283875e-06,1.019130118725709e-06,1.1598467493537799e-07,1.1999935107479733e-08,1.1380690806087905e-09,9.963140279602239e-11,8.09914515353072e-12,6.144957682546461e-13],[0.07540476437252422,0.0858162949325989,0.05282083250681354,0.021052554789188372,0.005989847809709457,0.0013633794907174544,0.0002586047390463868,4.204452130852159e-05,5.981228558527829e-06,7.56343121919257e-07,8.607753762110556e-08,8.905701259588102e-09,8.446131711461087e-10,7.394102563288087e-11,6.010746437322531e-12,4.560454442745996e-13],[0.0373075520290526,0.04245880104235225,0.0241606549868267,0.009914091578345061,0.0029635602029447956,0.0006745508948744687,0.00012794827803278868,2.08021095126694e-05,2.9592957089889303e-06,3.742112399346016e-07,4.258805448243359e-08,4.40621910116792e-09,4.178840699147951e-10,3.6583347005131316e-11,2.9739000885408664e-12,2.256348028067909e-13],[0.013843821242424309,0.01575531011362661,0.008965364129950129,0.0034010862963202246,0.0010467022011393476,0.0002503075516798157,4.747813761628123e-05,7.71909894635996e-06,1.098114418410862e-06,1.3885964719760612e-07,1.580327256149939e-08,1.6350284667303382e-09,1.5506545054074067e-10,1.357508838945597e-11,1.1035337077739397e-12,8.372695891958781e-14],[0.004109653433019745,0.004677094796509925,0.002661442879803428,0.0010096407436145961,0.0002872617816360741,7.07250596886071e-05,1.4094279883519007e-05,2.291478698635093e-06,3.2598439480286094e-07,4.122164074646912e-08,4.6913328479196315e-09,4.853717939373402e-10,4.6032468203548655e-11,4.0298778513774384e-12,3.275931559061357e-13,2.4855043859258244e-14],[0.0010166539909620459,0.0011570287296672852,0.0006583928717029302,0.00024976687405960514,7.106337347200325e-05,1.617509309266133e-05,3.318646665339495e-06,5.66870419158454e-07,8.064264818655415e-08,1.0197488976122178e-08,1.16055096628045e-09,1.200722103333704e-10,1.1387600749239716e-11,9.969189537430132e-13,8.104062661047855e-14,6.148688678228546e-15],[0.00021557299261042214,0.000245338284222526,0.00013960671273425317,5.2960980800388735e-05,1.5068395167421055e-05,3.4297934742158956e-06,6.505605023556974e-07,1.1440766700699104e-07,1.7099600410907064e-08,2.1622924173191143e-09,2.4608514509567653e-10,2.5460309939292837e-11,2.414645684755824e-12,2.1138834269963082e-13,1.7183988413710832e-14,1.3037781101328824e-15],[3.999664695326466e-05,4.5519193380134337e-05,2.5902133351317615e-05,9.826192166844588e-06,2.7957364898337543e-06,6.363516925273323e-07,1.20702683668183e-07,1.9624105011363934e-08,3.0197107807890735e-09,4.0118405083110874e-10,4.565776329237094e-11,4.723815426187848e-12,4.480047792672036e-13,3.922024188007722e-14,3.1882561424299402e-15,2.4189835723354157e-16],[6.596298432924513e-06,7.507083889112357e-06,4.271813130594243e-06,1.6205482441442896e-06,4.610764559416403e-07,1.0494793918879454e-07,1.9906441758994276e-08,3.2364326260964272e-09,4.604129776841036e-10,6.29753405154997e-11,7.52993701717594e-12,7.790577127526983e-13,7.388552412596018e-14,6.468252710152673e-15,5.258113016485243e-16,3.989418804559024e-17],[9.790830156422826e-07,1.1142701331014557e-06,6.340616217856882e-07,2.4053660973721967e-07,6.84371896625744e-08,1.5577334141452985e-08,2.9546963689243706e-09,4.803809663409485e-10,6.833871014412816e-11,8.641621511796406e-12,1.06380179386766e-12,1.1563487954912238e-13,1.096676605965556e-14,9.600772969552997e-16,7.804572823861537e-17,5.921460700339993e-18],[1.321131514848677e-07,1.503547059213627e-07,8.555748363662652e-08,3.245695109829198e-08,9.234613062058976e-09,2.1019368861282338e-09,3.986937192689631e-10,6.482049260655982e-11,9.221324669419348e-12,1.1660623600072447e-12,1.3270666943778181e-13,1.4851336618985967e-14,1.4798071282933312e-15,1.2954860348244423e-16,1.0531146953632973e-17,7.990158362644198e-19],[1.634120308497306e-08,1.8597518540944146e-08,1.0582687641854595e-08,4.0146315749418735e-09,1.1422381932622003e-09,2.5999060004220413e-10,4.931481053968809e-11,8.017709227632158e-12,1.140594539164509e-12,1.442313775763945e-13,1.641461589281345e-14,1.6982788944980281e-15,1.7421808819757007e-16,1.602399166992659e-17,1.302607720373117e-18,9.883103916419713e-20],[1.8657776908286836e-09,2.123395383928281e-09,1.2082918502700477e-09,4.583756771440502e-10,1.3041650161981258e-10,2.968475814549899e-11,5.63058135034156e-12,9.15432170488322e-13,1.3022883531819666e-13,1.6467801373020445e-14,1.8741596917362936e-15,1.9390315741644457e-16,1.8389698453496183e-17,1.741392753557236e-18,1.4872689678572568e-19,1.1284159867246327e-20],[1.9781129269806654e-10,2.2512413342095647e-10,1.2810410052244703e-10,4.859736810174009e-11,1.3826865280566471e-11,3.147202590670157e-12,5.969588879894898e-13,9.705487524682752e-14,1.3806968744177926e-14,1.745929910891659e-15,1.9869995936134638e-16,2.055777299478144e-17,1.949691027658305e-18,1.7068423649687808e-19,1.5008277648095223e-20,1.196355954583334e-21],[1.9573975611960952e-11,2.2276656894263934e-11,1.2676255764861504e-11,4.808844252794508e-12,1.3682066382569223e-12,3.1142441826972656e-13,5.907073633397176e-14,9.603848876327997e-15,1.3662378208414966e-15,1.7276460322288017e-16,1.9661911641077112e-17,2.0342486101149395e-18,1.9292733041532648e-19,1.6889678222949717e-20,1.3729803223202e-21,1.1267784468732248e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17491541395141233, "-10": 9.102369616396214e-08, "-11": 9.299688943140088e-09, "-12": 8.726100493031011e-10, "-13": 7.567906626858772e-11, "-14": 6.0710686666432644e-12, "-15": 4.1399936557144913e-13, "-2": 0.08546005657537166, "-3": 0.028681938490016025, "-4": 0.007555226160908058, "-5": 0.001631282756353508, "-6": 0.00029778651019528963, "-7": 4.702812204566989e-05, "-8": 6.53954953626736e-06, "-9": 8.119326298727009e-07, "0": 0.28710439503549434, "1": 0.20413218472843253, "10": 1.1404929231723428e-06, "11": 1.519689274508219e-07, "12": 1.8597511413676583e-08, "13": 2.1035780800145017e-09, "14": 2.2008794959233048e-10, "15": 1.9573975611960952e-11, "2": 0.1279131874640251, "3": 0.055989797039592365, "4": 0.019235173596540703, "5": 0.005416592128221633, "6": 0.001289585546150805, "7": 0.00026561403606355254, "8": 4.817142194477514e-05, "9": 7.800274304012484e-06} |
| Raw goal margin distribution | {"-1": 0.16526461296935366, "-10": 5.7753150441674434e-08, "-11": 5.619507754930615e-09, "-12": 5.020002141569235e-10, "-13": 4.125413254381802e-11, "-14": 2.8761134155512757e-12, "-2": 0.07823031598800995, "-3": 0.025234680300903093, "-4": 0.006366069553300803, "-5": 0.0013137416260579637, "-6": 0.0002289291978897051, "-7": 3.4483707928539366e-05, "-8": 4.571086524675837e-06, "-9": 5.407933984491656e-07, "0": 0.2902618960649866, "1": 0.2192420806885948, "10": 8.223527678924473e-07, "11": 1.0435878188669977e-07, "12": 1.215858055821034e-08, "13": 1.3031508199223639e-09, "14": 1.1848993950141584e-10, "2": 0.13306737207316544, "3": 0.05598124471500521, "4": 0.018418928866117897, "5": 0.004957368467867584, "6": 0.0011266542873913038, "7": 0.00022133581443512686, "8": 3.8265326629680395e-05, "9": 5.904261879866229e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.1% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0512 |
| Totals anchor target over 2 5 | 0.4847 |
| Totals anchor reference over odds | 1.97 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-11-05T13:37:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4555 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.22, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.06, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.22, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.65, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 3.32, "home": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.3, "under": 3.53}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0264 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | 0.0101 |
| Raw edge prob away | -0.0313 |
| Raw ev away | -0.1202 |
| Market p home draw | 70.3% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:36:39Z |
| Market reference home draw last update utc | 2026-11-05T13:37:01Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.9% |
| Market draw away odds | 1.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:36:39Z |
| Market reference draw away last update utc | 2026-11-05T13:37:01Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:36:39Z |
| Market reference home away last update utc | 2026-11-05T13:37:01Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 73.5% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.31 |
| Market reference over 1 5 last update utc | 2026-11-05T13:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market under 3 5 odds | 1.32 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.51 |
| Market reference under 3 5 last update utc | 2026-11-05T13:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.0%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 52.6%; Under 3.5 goals: 69.5%; Double Chance 1X: 75.8%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.2% | 4.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.6% |
| Under 2.5 | 47.4% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.75% |
| 2 | 2-1 | 9.49% |
| 3 | 1-0 | 9.11% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.0% | 49.9% | 2.01 | -1.5% |
| Draw | 26.8% | 25.7% | 3.71 | -0.6% |
| Erzurum BB win | 24.2% | 24.5% | 3.82 | -7.6% |
| Over 2.5 | 52.6% | 52.6% | 1.86 | -2.1% |
| Under 2.5 | 47.4% | 47.4% | 2.03 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:36:39Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:37:01Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4172 |
| Dc lambda away | 0.9323 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.57 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07367324110552154,0.05766781150451258,0.03809478269378739,0.01405421646428391,0.003888741182998557,0.0008607983533926324,0.00015878613205283048,2.5105965177154817e-05,3.4733562333922703e-06,4.2713898430703665e-07,4.727500713711481e-08,4.756651245368089e-09,4.3871497302444957e-10,3.735093663957887e-11,2.952812385074604e-12,2.1787479283888847e-13],[0.09107395462051388,0.12751093698163768,0.06408932062874947,0.02364431876158817,0.0065422811969488345,0.001448176830689127,0.00026713619579702764,4.223739153118463e-05,5.843452188429097e-06,7.18603582499408e-07,7.95338068861352e-08,8.002422516331927e-09,7.38078618187853e-10,6.283790022691123e-11,4.967707552626393e-12,3.665448774813748e-13],[0.08576599470155855,0.0949243258190503,0.054134994804794036,0.019889184541888833,0.005503251726686865,0.0012181808461175165,0.0002247102633659619,3.5529349912863256e-05,4.915409071805458e-06,6.044766782628653e-07,6.690243768186448e-08,6.731496889987003e-09,6.208587353089163e-10,5.285813503192207e-11,4.178748106916686e-12,3.083310957114424e-13],[0.04809656287804672,0.05323244744375572,0.029458378013802217,0.011200003279628574,0.003086158956441324,0.0006831415162384701,0.00012601487744567631,1.992444229261762e-05,2.7565036972528274e-06,3.3898342420617207e-07,3.751810157227646e-08,3.774944423593941e-09,3.481702894612056e-10,2.964222153576825e-11,2.3433928770394685e-12,1.729084584600865e-13],[0.02022899083195614,0.022389098656233408,0.012389934396694759,0.004570988667637755,0.0013034090347243826,0.00028732330632350267,5.3000747828951475e-05,8.380044983488217e-06,1.1593611826559943e-06,1.4257344330070012e-07,1.577978315544867e-08,1.5877083842696202e-09,1.4643735793197445e-10,1.2467257363198523e-11,9.856104093238669e-13,7.272377508192554e-14],[0.006806508333944124,0.00753332619798383,0.004168877846091195,0.0015380140669939669,0.0004255618701725526,9.707854939028128e-05,1.7833318270783196e-05,2.8196585036181733e-06,3.900936837310467e-07,4.797210785682508e-08,5.3094702769711254e-09,5.342209326790782e-10,4.9272210632978946e-11,4.194894933166134e-12,3.3163124749096853e-13,2.4469583543883504e-14],[0.0019085049803400892,0.002112300442751009,0.001168928875326023,0.00043125011572419503,0.00011932505020478338,2.6413382094914505e-05,5.021151638941542e-06,7.90615692068841e-07,1.0937997893679299e-07,1.3451097430613116e-08,1.488744297282785e-09,1.4979241346629608e-10,1.3815638617005205e-11,1.176223913812767e-12,9.298745500927876e-14,6.861127581002816e-15],[0.0004586859367885066,0.0005076656950559136,0.0002809378239728295,0.00010364571502761051,2.8678323084995805e-05,6.348134814822277e-06,1.1710010469034524e-06,1.9080502899411274e-07,2.6288146282746245e-08,3.2328075060589096e-09,3.5780156702342837e-10,3.600078291771387e-11,3.3204205420743843e-12,2.8269109765912815e-13,2.2348402728773438e-14,1.648988482784537e-15],[9.645963302584686e-05,0.00010675986054371643,5.907998748170499e-05,2.1796237543848154e-05,6.030925081208384e-06,1.3349848022890215e-06,2.4625636453569993e-07,3.893604329771706e-08,5.551270666012291e-09,6.798451852720054e-10,7.524409423318874e-11,7.570806145048724e-12,6.982698210075232e-13,5.944869321870303e-14,4.699770699369165e-15,3.467750178409875e-16],[1.8031143233261966e-05,1.9956558786731123e-05,1.1043787780288354e-05,4.074358037356609e-06,1.1273573261387154e-06,2.4954793450075876e-07,4.603255933863839e-08,7.278291981989034e-09,1.0069360267851495e-09,1.276115382986111e-10,1.4065334876529567e-11,1.4152063999253943e-12,1.3052717248755373e-13,1.1112709729773232e-14,8.785254099101335e-16,6.482245287759246e-17],[3.033496028231419e-06,3.3574211592441492e-06,1.8579679577019686e-06,6.854556454919857e-07,1.8966262576911006e-07,4.198306554212084e-08,7.744355647150212e-09,1.2244742074337192e-09,1.6940337051403304e-10,2.0832525879121565e-11,2.3761426178296878e-12,2.3808934008033663e-13,2.1959431756210426e-14,1.869563143726261e-15,1.478000206191391e-16,1.0905501154339267e-17],[4.639497156393053e-07,5.134915548318226e-07,2.8416180460448216e-07,1.0483513044016499e-07,2.9007429208432022e-08,6.420984612691026e-09,1.184439197172698e-09,1.872738434662619e-10,2.590893307486793e-11,3.1861734341224522e-12,3.5264018825767276e-13,3.656534650498411e-14,3.3585249573688683e-15,2.859351984736977e-16,2.260486807945867e-17,1.667911911659781e-18],[6.504438836203541e-08,7.199000880318005e-08,3.9838650942768004e-08,1.4697577578937607e-08,4.066756433329424e-09,9.002031960274486e-10,1.6605489891497966e-10,2.6255243173681978e-11,3.632356370012015e-12,4.466921635080391e-13,4.9439119335350075e-14,4.974396891666901e-15,4.728133832991416e-16,4.008727555802219e-17,3.1691361556431642e-18,2.3383635441218206e-19],[8.417568306569471e-09,9.316419628983698e-09,5.155626396020647e-09,1.902052833877087e-09,5.262898295421844e-10,1.1649770384766942e-10,2.148960870348001e-11,3.3977612578959153e-12,4.70072955228602e-13,5.78076278834357e-14,6.398048694156806e-15,6.43750009401775e-16,5.93742852777372e-17,5.209374937213422e-18,4.1012638806694647e-19,3.0261388190293007e-20],[1.0115300310853845e-09,1.1195440171902798e-09,6.195460183627264e-10,2.2856762096913014e-10,6.32436765878395e-11,1.3999402404901222e-11,2.5823829125186893e-12,4.083052760187073e-13,5.6488155925469474e-14,6.946679789253154e-15,7.688465550597696e-16,7.735873868860535e-17,7.134943304919689e-18,6.074486436417816e-19,4.94893904531497e-20,3.636478116004623e-21],[1.1345083307766174e-10,1.2556542812778633e-10,6.948682664199274e-11,2.5635607660310936e-11,7.093262261413719e-12,1.5701401012496476e-12,2.896340036848926e-13,4.5794561002427444e-14,6.335578926795508e-15,7.79123293422023e-16,8.623202426014607e-17,8.676374482566986e-18,8.002384872710672e-19,6.813001349955822e-20,5.386080397341911e-21,4.0955491905432693e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14503844985417685, "-10": 5.592894069028429e-08, "-11": 5.550004115239985e-09, "-12": 5.059045298167376e-10, "-13": 4.262697528791671e-11, "-14": 3.3193572625559786e-12, "-15": 2.1787479283888847e-13, "-2": 0.06798142779410143, "-3": 0.02194947734006538, "-4": 0.0055827615780913884, "-5": 0.0011663684388865257, "-6": 0.0002062942441872092, "-7": 3.159305032493305e-05, "-8": 4.262787924886446e-06, "-9": 5.137652641223584e-07, "0": 0.2679248813936598, "1": 0.22048083333848803, "10": 3.5887931006565757e-06, "11": 5.413310117217366e-07, "12": 7.500598961704214e-08, "13": 9.606599150401743e-09, "14": 1.1370954592131709e-09, "15": 1.1345083307766174e-10, "2": 0.15305231750131873, "3": 0.07511585008737845, "4": 0.029041180028629748, "5": 0.009222713389775039, "6": 0.0024795212740353735, "7": 0.0005772049702946573, "8": 0.00011838318078303478, "9": 2.1687964353555484e-05} |
| Raw goal margin distribution | {"-1": 0.1500339840049227, "-10": 1.470184920982501e-08, "-11": 1.2338061748319013e-09, "-12": 9.50457796643158e-11, "-13": 6.742023587508826e-12, "-14": 4.102565704257948e-13, "-2": 0.06303030940784604, "-3": 0.01774998523520649, "-4": 0.003890619236339014, "-5": 0.0006957235725686972, "-6": 0.00010488002810948564, "-7": 1.365223822229791e-05, "-8": 1.5627417936367002e-06, "-9": 1.5956880532817087e-07, "0": 0.294101790571401, "1": 0.2343832281938126, "10": 9.681657460879328e-07, "11": 1.2350440945383662e-07, "12": 1.4461926049403344e-08, "13": 1.5593418738503456e-09, "14": 1.4423291932655828e-10, "2": 0.14563474135424986, "3": 0.062340649237053056, "4": 0.020770637648285094, "5": 0.005645801346210682, "6": 0.001293717475186589, "7": 0.000255981324677072, "8": 4.453991934347887e-05, "9": 6.913022457197248e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.8% |
| P draw away | 51.0% |
| P home away | 73.2% |
| Raw p home draw | 76.4% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1871 |
| Totals anchor target over 2 5 | 0.5262 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.02 |
| Totals anchor reference last update utc | 2026-11-05T13:37:01Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4265 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.82, "draw": 3.65, "home": 1.94}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.02}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.94 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.82 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:37:01Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0282 |
| Raw ev home | -0.0545 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.0911 |
| Raw edge prob away | -0.0092 |
| Raw ev away | -0.1003 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **52.0%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 8.5%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 77.7%; Under 3.5 goals: 40.6%; Double Chance 1X: 48.0%; Double Chance X2: 75.1%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 60.5%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 24.9% | 4.02 |
| Draw | 23.1% | 4.33 |
| Fenerbahce win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 77.7% |
| Under 2.5 | 22.3% |
| Over 3.5 | 59.4% |
| Under 3.5 | 40.6% |
| Over 4.5 | 39.5% |
| Under 4.5 | 60.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.51% |
| 2 | 1-1 | 8.05% |
| 3 | 2-2 | 7.79% |
| 4 | 1-3 | 6.43% |
| 5 | 2-3 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 24.9% | 21.9% | 4.24 | +5.6% |
| Draw | 23.1% | 23.9% | 4.11 | -5.0% |
| Fenerbahce win | 52.0% | 54.2% | 1.81 | -5.9% |
| Over 2.5 | 77.7% | 59.2% | 1.65 | +28.2% |
| Under 2.5 | 22.3% | 40.8% | 2.35 | -47.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | 6692a3ca274d09ffbfabd943320d62f5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T13:37:01Z |
| Market best draw last update utc | 2026-11-05T13:36:39Z |
| Market best away last update utc | 2026-11-05T13:36:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8739 |
| Dc lambda away | 2.2662 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.04 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.26 |
| Fair Over 2.5 odds | 1.29 |
| Fair Under 2.5 odds | 4.48 |
| Fair Over 3.5 odds | 1.68 |
| Fair Under 3.5 odds | 2.47 |
| Fair Over 4.5 odds | 2.53 |
| Fair Under 4.5 odds | 1.65 |
| Score matrix json | [[0.024365372306575022,0.032853225202802254,0.0454400138944776,0.03432605051411031,0.019447800125570326,0.00881469144418257,0.0033293733633307575,0.001077881696157737,0.00030534284416538745,7.688681549322775e-05,1.7424427192860264e-05,3.5898182525198674e-06,6.779502915570636e-07,1.1818466704131576e-07,1.9131090969456177e-08,2.890381136469689e-09,4.093942777197345e-10,5.457572115843335e-11],[0.01817667864888597,0.08048415416105409,0.08514923175373201,0.06432297395867448,0.03644288586350319,0.016517693114296288,0.006238853376394022,0.0020198232897194416,0.0005721765108294133,0.00014407683251247712,3.2651323405541526e-05,6.726896410010562e-06,1.2703989621868982e-06,2.214641401080571e-07,3.584941022339626e-08,5.416233670557557e-09,7.671566367290645e-10,1.0226847068836975e-10],[0.02179473691124379,0.049392188252478916,0.0779304890617835,0.06026683694920785,0.03414483698632142,0.015476105292269376,0.005845438045615227,0.0018924554226292596,0.0005360956803159838,0.000134991503638597,3.0592366346771686e-05,6.302705614587732e-06,1.1902889807885744e-06,2.0749885150776447e-07,3.3588785276731155e-08,5.074691846680101e-09,7.187805708417211e-10,9.581953178938233e-11],[0.013613589618588372,0.030851713602765236,0.03495875294078929,0.036771708375416906,0.021327800386779262,0.009666799246121089,0.0036512207060795214,0.0011820794901110233,0.00033486004524122757,8.431939050312507e-05,1.910882992543065e-05,3.936842553924346e-06,7.434870986501269e-07,1.2960946591182808e-07,2.0980475259070515e-08,3.1697915199820008e-09,4.489700314852506e-10,5.985150399099226e-11],[0.006377565707425206,0.014453118993659057,0.01637714593843077,0.012371535362313162,0.009759840931747196,0.004528610682405632,0.0017104893432029417,0.0005537694194401942,0.00015687206689419446,3.95011505715923e-05,8.951923912488548e-06,1.8442947650748733e-06,3.483018040877145e-07,6.071821674632518e-08,9.828734616403519e-09,1.4849539514487462e-09,2.103292339995523e-10,2.8038666515228424e-11],[0.002390161330968255,0.005416688391043415,0.006137768347582344,0.004636559901418159,0.0026268938279382934,0.0016578744774632455,0.0006410510957804827,0.0002075397280623337,5.8791953764275064e-05,1.4804100334874004e-05,3.3549701179070287e-06,6.911982145878723e-07,1.3053530795734244e-07,2.275575672759425e-08,3.6835781064749296e-09,5.565257460050918e-10,7.88264402031328e-11,1.050823143987174e-11],[0.0007464801161521306,0.0016917059643283502,0.0019169091097135616,0.0014480611534096095,0.0008204149169312855,0.0003718520502195813,0.00019556811955842316,6.481749926369722e-05,1.8361532297482235e-05,4.623523271974194e-06,1.0478031130591616e-06,2.1587066815304983e-07,4.0767964314139976e-08,7.106934458797749e-09,1.150431888069639e-09,1.7381061191850134e-10,2.4618576778186136e-11,3.2818645855220344e-12],[0.00019983082549665494,0.00045286537716760064,0.0005131516855005591,0.00038764228194995665,0.0002196229833223542,9.954384658098363e-05,3.75984381743659e-05,1.6949265973048795e-05,4.91533542152862e-06,1.2377054018586956e-06,2.8049422417288526e-07,5.778802795163414e-08,1.091348019382808e-08,1.902508250283719e-09,3.0796768580474825e-10,4.6528658042211577e-11,6.5903302897020845e-12,8.785467892616334e-13],[4.680742756612077e-05,0.0001060770443513544,0.00012019822412184488,9.079949496701691e-05,5.144344901827233e-05,2.33166798811549e-05,8.806880355280127e-06,2.851219763983116e-06,1.1246563398548935e-06,2.899142602334246e-07,6.570164061553828e-08,1.3535994388315006e-08,2.5563219908504683e-09,4.456345356016807e-10,7.213689434642752e-11,1.0898652826193109e-11,1.543687801445857e-12,2.0578664527660792e-13],[9.745733761044435e-06,2.208620909462383e-05,2.5026367646183646e-05,1.8905283832054417e-05,1.0710995753264278e-05,4.854745627544631e-06,1.833672894898757e-06,5.936499858864239e-07,1.6816945289585497e-07,5.896356476648945e-08,1.3679681418047352e-08,2.818317612373811e-09,5.322495771667644e-10,9.27851788600352e-11,1.5019559997305325e-11,2.26919902077702e-12,3.2140989379968554e-13,4.284665833454016e-14],[1.8262356709582623e-06,4.13869533826894e-06,4.689646406375697e-06,3.5426274255195993e-06,2.007114394431948e-06,9.097221261973521e-07,3.4360869398247697e-07,1.1124301226278016e-07,3.151297389956941e-08,7.935120328370052e-09,2.503990326538901e-09,5.281195117785968e-10,9.973729916157985e-11,1.738684921270406e-11,2.814488565121363e-12,4.2522115808368215e-13,6.022842686326247e-14,8.028958901449885e-15],[3.111045871366128e-07,7.050388539507444e-07,7.988949795875248e-07,6.034969418907516e-07,3.4191780663667387e-07,1.5497382456184483e-07,5.853474585888333e-08,1.8950572454696244e-08,5.368327259388228e-09,1.3517709531659495e-09,3.063442594645898e-10,8.78812430798698e-11,1.6990540580944153e-11,2.9619006089649743e-12,4.794563576744474e-13,7.243766778356814e-14,1.0260088646363525e-14,1.3677566285088105e-15],[4.858111152001656e-08,1.100966446845902e-07,1.2475292136750159e-07,9.424017982450751e-08,5.339280673351683e-08,2.42002238636758e-08,9.140601373124454e-09,2.9592616497984302e-09,8.383010603111479e-10,2.1108829037109863e-10,4.78377537584519e-11,9.855637703373583e-12,2.5916873815267417e-12,4.62521061228024e-13,7.487039325117706e-14,1.1311637829686259e-14,1.6021830964368375e-15,2.1358456303522773e-16],[7.002713737107507e-09,1.5869856864525712e-08,1.7982482674249816e-08,1.3584230191453133e-08,7.69629449547426e-09,3.488335997034876e-09,1.3175699937336581e-09,4.2656212586244733e-10,1.208367237224272e-10,3.042727563191265e-11,6.895562594500375e-12,1.4206387497933755e-12,2.682928178727764e-13,6.512456336590258e-14,1.0792176525369052e-14,1.6305135708245713e-15,2.3094633341513674e-16,3.078710031129366e-17],[9.373043142905176e-10,2.1241601277331456e-09,2.4069324014936632e-09,1.8182319087662362e-09,1.0301392153776738e-09,4.669093300772617e-10,1.7635506546015027e-10,5.709479723055949e-11,1.6173841559393095e-11,4.072652087828822e-12,9.229622703319555e-13,1.9015068717911458e-13,3.591065194522498e-14,6.260176441012365e-15,1.4110346159175442e-15,2.1824216465463746e-16,3.091187256913294e-17,4.1208141628519435e-18],[1.1709318937362945e-10,2.6536171903235033e-10,3.0068718046065375e-10,2.2714349008357537e-10,1.286906337550828e-10,5.832887118249805e-11,2.203124082764408e-11,7.132594827995994e-12,2.0205248858228295e-12,5.087780082758038e-13,1.1530150267845405e-13,2.3754665463418197e-14,4.486155354929281e-15,7.820555334524935e-16,1.2659489532949197e-16,2.6632017342020282e-17,3.861680452597489e-18,5.147946785133436e-19],[1.3713677473108213e-11,3.1078537086451366e-11,3.5215771602036083e-11,2.6602508478805088e-11,1.5071942736957803e-11,6.831339474534807e-12,2.5802468329616374e-12,8.353526412657913e-13,2.366390971053641e-13,5.958687732589933e-14,1.3503839363804579e-14,2.782090251273531e-15,5.254079076747122e-16,9.159249491108688e-17,1.4826494807916898e-17,2.24003016770909e-18,4.417870837954744e-19,6.029153551772967e-20],[1.5116362162074213e-12,3.425736262118568e-12,3.881776849405602e-12,2.932350956727903e-12,1.6613555725272544e-12,7.530073661980093e-13,2.8441638408864263e-13,9.207955403049834e-14,2.608434025494238e-14,6.568163933647111e-15,1.4885061049600275e-15,3.0666525363670323e-16,5.791485347969527e-17,1.0096090761350831e-17,1.6343002491496333e-18,2.469148580711648e-19,3.4973079744694533e-20,6.4917843820802754e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20483679304491798, "-10": 2.5481632807057205e-05, "-11": 5.090263603729839e-06, "-12": 9.363938459272733e-07, "-13": 1.595857778093926e-07, "-14": 2.532595671484645e-08, "-15": 3.753357304988136e-09, "-16": 5.116627484081043e-10, "-17": 5.457572115843335e-11, "-2": 0.15551232101729315, "-3": 0.09051374185278485, "-4": 0.04316579518595867, "-5": 0.017323943654374716, "-6": 0.005979297590936639, "-7": 0.0018061407967544466, "-8": 0.00048432114168645647, "-9": 0.0001166489140135888, "0": 0.23118314291400588, "1": 0.11793852716161136, "10": 2.6707028168809085e-06, "11": 4.411377527938328e-07, "12": 6.710086922622266e-08, "13": 9.455824909352638e-09, "14": 1.2408141558816318e-09, "15": 1.5205350330948641e-10, "16": 1.713941373522678e-11, "17": 1.5116362162074213e-12, "2": 0.07458954856175135, "3": 0.0358974282788559, "4": 0.014155467113719983, "5": 0.0046975008126786694, "6": 0.001340620673352553, "7": 0.00033484435969660415, "8": 7.424384488260915e-05, "9": 1.4785750355228767e-05} |
| Raw goal margin distribution | {"-1": 0.1842972734986496, "-10": 2.2926523017788953e-05, "-11": 4.579849594457876e-06, "-12": 8.424991924544909e-07, "-13": 1.4358369559604883e-07, "-14": 2.2786456973418326e-08, "-15": 3.3769983775515607e-09, "-16": 4.6035698997572585e-10, "-17": 4.910327123953855e-11, "-2": 0.13991869494192388, "-3": 0.08143769285614053, "-4": 0.038837448306607784, "-5": 0.015586826635414879, "-6": 0.00537973782476188, "-7": 0.0016250343478260267, "-8": 0.0004357569974794216, "-9": 0.00010495222313194774, "0": 0.21293777958272841, "1": 0.15126022808180087, "10": 3.4252684592758398e-06, "11": 5.657743801705498e-07, "12": 8.605917869177213e-08, "13": 1.2127421521300882e-08, "14": 1.591386943204714e-09, "15": 1.9501386141369498e-10, "16": 2.1981889151678406e-11, "17": 1.938725574611636e-12, "2": 0.0956636681795147, "3": 0.046039689656029816, "4": 0.018154874711057582, "5": 0.006024706781072138, "6": 0.0017193922435932354, "7": 0.0004294494380976033, "8": 9.52202912897549e-05, "9": 1.896323470300589e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 48.0% |
| P draw away | 75.1% |
| P home away | 76.9% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7769 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.36, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.81, "draw": 4.11, "home": 4.22}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:36:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.65, "under": 2.35}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:37:01Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.79, "draw": 3.9, "home": 4.24}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.24 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-11-05T13:37:01Z |
| Market reference home last update utc | 2026-11-05T13:37:01Z |
| Market reference draw last update utc | 2026-11-05T13:37:01Z |
| Market reference away last update utc | 2026-11-05T13:37:01Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best over 2 5 last update utc | 2026-11-05T13:36:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:36:39Z |
| Home probability edge | +3.0% |
| Draw probability edge | -0.8% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | +18.5% |
| Under 2.5 probability edge | -18.5% |
| Raw edge prob home | 0.1005 |
| Raw ev home | 0.3543 |
| Raw edge prob draw | -0.0261 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | -0.0745 |
| Raw ev away | -0.1535 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |

</details>


---
