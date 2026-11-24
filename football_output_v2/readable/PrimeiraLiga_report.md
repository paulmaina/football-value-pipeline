# Primeira Liga — football model report

Fixtures in this report: **1**.

> Each match shows the two models the shortlists use, side by side, and the master's verdict on them: **Research** (the value shortlist's model, independent of bookmaker odds) and **Cagey** (the cagey tier's market view, built from Pinnacle's prices). Probabilities are model estimates, not guarantees. No probability here is blended or averaged. The production model (70% Pinnacle blend) is kept only as a benchmark at the end of this report.

## Quick reference

- **Research:** The value shortlist's model: team form, goal rates and xG, never bookmaker odds. Live research v5 (C6 grid) for domestic leagues and v6 (CE3n) for UCL/UEL, exactly as the forecast carries it.
- **Cagey:** The cagey tier's market view: Pinnacle's 1X2, O/U 2.5 and main AH line with the margin removed, plus the narrow-margin correction (D_pow2 for domestic leagues, D for UCL/UEL, D where D_pow2's power fit fails). Blank without Pinnacle 1X2 and O/U 2.5.
- **No-loss:** The chance a bet does not lose: a win, a half win or a refund (push) on that exact line.
- **Gap:** Research minus cagey no-loss on the same Pinnacle offer, in percentage points (the master's g). +4 or more: research too optimistic; -4 or less: research too pessimistic; -8 or less with cagey no-loss of 85% or more: flagged for inspection.
- **Cagey tier:** The master's market classes from the cagey no-loss: safe (75% or more), risky (below 50%), in between otherwise; fair price when the Pinnacle price is within its 2.70% margin of the cagey fair odds.
- **Best offer:** The fixture's master pick, or else the Pinnacle offer the master's own rule would choose for it (safe first, then chance of profit), shown with both views and the master's labels.
- **Expected goals:** A view's average goal expectation for each team, from its score grid. It is not a prediction that the team will score exactly that many goals.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-27 — CS Maritimo vs Nacional

Research leans **Nacional win** at **38.6%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote). Only one view is available.

**Fixture source:** The Odds API

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| CS Maritimo win | 33.1% | — |
| Draw | 28.3% | — |
| Nacional win | 38.6% | — |
| CS Maritimo expected goals | 1.21 | — |
| Nacional expected goals | 1.32 | — |
| Expected total goals | 2.53 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 13.4% | — |
| Over 1.5 | 72.2% | — |
| Under 1.5 | 27.8% | — |
| Over 2.5 | 46.2% | — |
| Under 2.5 | 53.8% | — |
| Over 3.5 | 25.0% | — |
| Under 3.5 | 75.0% | — |
| BTTS Yes | 52.1% | — |
| BTTS No | 47.9% | — |
| Double Chance 1X | 61.4% | — |
| Double Chance X2 | 66.9% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (13.45%) | — |
| 2 | 0-1 (10.17%) | — |
| 3 | 1-0 (9.18%) | — |
| 4 | 0-0 (8.46%) | — |
| 5 | 1-2 (8.33%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

| Line | Pinnacle odds | Research no-loss | Cagey no-loss |
| --- | --- | --- | --- |
| CS Maritimo -0.25 | 1.79 | 33.1% | — |
| Nacional +0.25 | 2.08 | 66.9% | — |

_No-loss: win, half win or refund, from each view's own goal-margin distribution._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

| Offer | Pinnacle odds | Research no-loss | Cagey no-loss | Gap (points) | Gap label | Cagey tier | Master labels | Master check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home win | 2.08 | 33.1% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Away win | 3.68 | 38.6% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Away +0.25 | 2.08 | 66.9% | — | — | one view missing (no cagey view) | no market view | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Home -0.25 | 1.79 | 33.1% | — | — | one view missing (no cagey view) | no market view | one view missing | eligible |

_Best offer: none (no offer passes the master checks with a market view). Gap = research minus cagey no-loss, in points; the cagey tier decides safety (safe at 75% or more, risky below 50%) and fair price; the research view only labels. No probability is blended._

_Views the master could not use: cagey: cagey settlement probabilities unavailable._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,628 |
| Training data through | 2026-11-08 |
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
| Training sha256 | 7c73b44b6e1c6ee16fc6ee45d20634ecf277c8dff8e4ce224e38cad97bc36515 |
| Training as of utc | 2026-11-24T22:39:44.061744+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1628, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1323, 'tuning_matches': 207, 'audit_matches': 92, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8715376387866776, 'audit_candidate_poisson_score': 0.8661166852473193, 'audit_gain': 0.005420953539358231, 'audit_gain_lower95': -0.0037314460101351495, 'audit_baseline_briers': [0.5256825537476439, 0.20162598270462478, 0.2218871197329721, 0.25436800146761224], 'audit_candidate_briers': [0.5292164683546622, 0.20093844348934414, 0.21876001120007932, 0.2532888353944095], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1448.223 |
| Base scoring parameter | 0.083 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1628, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-08'} |
| Training data health | {'training_end': '2026-11-08', 'days_since_latest_result': 16, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 9.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

### 2026-11-27 — CS Maritimo vs Nacional

The model's most likely 1X2 outcome is **CS Maritimo win** at **42.7%**. Expected goals are 1.21 for CS Maritimo and 1.36 for Nacional (2.57 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 46.7%; Under 3.5 goals: 74.5%; Double Chance 1X: 69.8%; Double Chance X2: 57.3%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 88.4%; BTTS Yes (both teams score): 52.1%; BTTS No (at least one team does not score): 47.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| CS Maritimo win | 42.7% | 2.34 |
| Draw | 27.2% | 3.68 |
| Nacional win | 30.2% | 3.31 |

| Measure | Benchmark estimate |
| --- | --- |
| CS Maritimo expected goals | 1.21 |
| Nacional expected goals | 1.36 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 46.7% |
| Under 2.5 | 53.3% |
| Over 3.5 | 25.5% |
| Under 3.5 | 74.5% |
| Over 4.5 | 11.6% |
| Under 4.5 | 88.4% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 1-0 | 12.47% |
| 3 | 2-1 | 9.60% |
| 4 | 0-1 | 8.14% |
| 5 | 0-0 | 7.57% |

| Selection | Benchmark | Market fair | Best quoted odds | Benchmark EV (display only) |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 42.7% | 46.4% | 2.08 | -11.3% |
| Draw | 27.2% | 28.0% | 3.37 | -8.4% |
| Nacional win | 30.2% | 25.5% | 3.68 | +11.0% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:15:00+00:00 |
| Fixture id | 1,640,277,271 |
| Odds source | — |
| Odds schedule provider | — |
| Odds provider | — |
| Odds match method | — |
| Odds event id | 1640277271.00 |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-24T22:38:51Z |
| Market best draw last update utc | 2026-11-24T22:38:51Z |
| Market best away last update utc | 2026-11-24T22:38:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Nacional |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2090 |
| Dc lambda away | 1.3610 |
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
| P btts yes | 52.1% |
| P btts no | 47.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.21 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.87 |
| Fair Over 3.5 odds | 3.92 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.65 |
| Fair Under 4.5 odds | 1.13 |
| Score matrix json | [[0.07568704190557728,0.08135937496755268,0.0522102644295278,0.023686597272956043,0.008059548680248121,0.0021938592253080637,0.000497651759775825,9.675992925462194e-05,1.646165869960913e-05,2.48942543082246e-06,3.388185346228479e-07,4.192205010354417e-08,4.754767709516446e-09,4.977989662452271e-10,4.839427552573042e-11],[0.12465372717878223,0.1289193540280289,0.06312107929465034,0.028636583266204097,0.009743819857715998,0.002652328304310465,0.0006016502029468124,0.00011698065952662686,1.9901788957648762e-05,3.009661447494889e-06,4.0962427262350166e-07,5.068285092391838e-08,5.748411215674529e-09,6.018281723811626e-10,5.850763132965833e-11],[0.07055074112727626,0.09602175035788163,0.05582401715227167,0.01731050458012662,0.005890033622620769,0.0016033037472717936,0.00036369103453889255,7.071354231395806e-05,1.203041597880397e-05,1.8193077640297943e-06,2.4761343842819687e-07,3.0637234718143795e-08,3.4748523506580807e-09,3.637986151353556e-10,3.536722976653705e-11],[0.028431439511299107,0.038696072407575194,0.026333278326924274,0.010206224982144388,0.002373641041685902,0.000646119839146147,0.0001465648621697693,2.8497047214599643e-05,4.8481708162367055e-06,7.331678990038539e-07,9.978642866636399e-08,1.234658448322961e-08,1.4003404193897925e-09,1.4660821637373734e-10,1.4252738351472173e-11],[0.00859324870053141,0.01169567843372525,0.007959090839338026,0.0036108566281011375,0.0010496190789598863,0.0001952862241084779,4.4298436274512314e-05,8.613078273737091e-06,1.465333387358857e-06,2.215960290326621e-07,3.0159907947225914e-08,3.731688331304836e-09,4.2324531209334836e-10,4.431153984799698e-11,4.307813020481357e-12],[0.0020778103254276135,0.0028279644008176526,0.0019244737006122255,0.000873089496995858,0.0002970754820611384,6.90841262288618e-05,1.0711170070730852e-05,2.082605030363017e-06,3.5431126789799187e-07,5.358096026818692e-08,7.292535143643288e-09,9.023060796068236e-10,1.023388837334602e-10,1.071433845805854e-11,1.041610534722934e-12],[0.00041867128282021914,0.000569824622089398,0.0003877745062332758,0.00017592438311176848,5.9859637642033105e-05,1.629416527831298e-05,3.1576379260890035e-06,4.196373985630681e-07,7.139244195351767e-08,1.079637014779217e-08,1.4694195164192011e-09,1.8181141908019282e-10,2.0620915783667245e-11,2.158900536737973e-12,2.0988076410764654e-13],[7.230921661543761e-05,9.841509012493056e-05,6.697299747975971e-05,3.0384110036581093e-05,1.033842941322065e-05,2.814184719669948e-06,6.383654711852942e-07,1.060358717241424e-07,1.2330273801317091e-08,1.8646539653219473e-09,2.537851972936327e-10,3.1400867040300555e-11,3.561462960071647e-12,3.7286628667389374e-13,3.62487570989917e-14],[1.092753466580739e-05,1.4872714147882748e-05,1.0121112990689757e-05,4.5917163987579556e-06,1.5623671654997874e-06,4.252860495464613e-07,9.64712541823124e-08,1.8757196265095283e-08,2.726210577625802e-09,2.817907840733074e-10,3.835260110538754e-11,4.745371049228541e-12,5.382164512187945e-13,5.6348408460975695e-14,5.477995314183728e-15],[1.4679058688556207e-06,1.997865488526094e-06,1.3595784971400636e-06,6.168095234644029e-07,2.0987423071011677e-07,5.7129069562695124e-08,1.2959073068254203e-08,2.519671574867133e-09,4.28668910985051e-10,5.5381018826546734e-11,5.151940485225384e-12,6.374500952036521e-13,7.229911518201894e-14,7.569333981557178e-15,7.358641923520959e-16],[1.7746664139229296e-07,2.4153761199872384e-07,1.6437009669068902e-07,7.457093593702008e-08,2.537334009567819e-08,6.906780820395623e-09,1.5667238763568106e-09,3.046228380787819e-10,5.182514323014214e-11,7.83729221139761e-12,9.1127090103188e-13,7.706633637154312e-14,8.740806491216113e-15,9.151160900601513e-16,8.896438764114191e-17],[1.9504847920536398e-08,2.654670394483068e-08,1.8065444375818244e-08,8.19587700163015e-09,2.788710801757159e-09,7.591044066952443e-10,1.721941132263969e-10,3.3480219624570296e-11,5.695952372984041e-12,8.61374236266768e-13,1.1723570944535557e-13,1.2392207978531516e-14,9.606768910284433e-16,1.0057777634278425e-16,9.777819863330548e-18],[1.965078236490063e-09,2.674532525711539e-09,1.8200609263948551e-09,8.257198205526906e-10,2.8095758176242385e-10,7.64783993650079e-11,1.7348246227371386e-11,3.373071720691544e-12,5.738569246904979e-13,8.6781900174617e-14,1.1811286204799344e-14,1.4614115860458246e-15,1.416031005855232e-16,1.013302949969041e-17,9.850977096581585e-19],[1.827490032423154e-10,2.487270705750385e-10,1.692626349234045e-10,7.679056811140395e-11,2.6128587181426415e-11,7.112363769539716e-12,1.6133580064054673e-12,3.136900523219135e-13,5.3367738262781004e-14,8.070572184806531e-15,1.0984299458693363e-15,1.35908843585626e-16,1.541467984801687e-17,1.378709028904351e-18,9.161244636135719e-20],[1.5781399159610185e-11,2.1478974510960973e-11,1.46167757806687e-11,6.631295304261848e-12,2.256349728157018e-12,6.141924148643796e-13,1.3932249278907216e-13,2.7088891541187045e-14,4.608602864190799e-15,6.969390740041414e-16,9.485557303778036e-17,1.1736489238750364e-17,1.331143871009774e-18,1.3936370468447666e-19,1.1574523200233479e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1643710295328879, "-10": 3.931271539268186e-07, "-11": 4.8048512672705525e-08, "-12": 5.391963111664146e-09, "-13": 5.563065975748854e-10, "-14": 4.839427552573042e-11, "-2": 0.0874294554948985, "-3": 0.03518926418462917, "-4": 0.011105585482025964, "-5": 0.0028713002153792134, "-6": 0.0006274270863935466, "-7": 0.0001185846486273312, "-8": 1.9731714339546758e-05, "-9": 2.931132631733878e-06, "0": 0.27175860772952426, "1": 0.2509336396983211, "10": 2.0591245318135807e-07, "11": 2.2355274376475604e-08, "12": 2.22842208284577e-09, "13": 2.0422797775327636e-10, "14": 1.5781399159610185e-11, "2": 0.11814176673717126, "3": 0.04223829301369087, "4": 0.0118409928146401, "5": 0.002719416618028309, "6": 0.0005278504455703512, "7": 8.861894702604546e-05, "8": 1.309825433729383e-05, "9": 1.7283613878303115e-06} |
| Raw goal margin distribution | {"-1": 0.2231693537704609, "-10": 5.337554503417802e-07, "-11": 6.523628618298587e-08, "-12": 7.320760395574981e-09, "-13": 7.553069676076379e-10, "-14": 6.570573431315018e-11, "-2": 0.11870446476333493, "-3": 0.04777706491258811, "-4": 0.015078243059677716, "-5": 0.0038984133357816185, "-6": 0.0008518684698054703, "-7": 0.0001610044025182892, "-8": 2.679008551843936e-05, "-9": 3.97964882922801e-06, "0": 0.2521938245020109, "1": 0.19894061199080212, "10": 1.6324773952856686e-07, "11": 1.7723299159989468e-08, "12": 1.7666967787504722e-09, "13": 1.6191228457342845e-10, "14": 1.251151982117042e-11, "2": 0.0936629915567462, "3": 0.033486589807937596, "4": 0.009387559037342385, "5": 0.002155958072815252, "6": 0.0004184807218658688, "7": 7.025725038913511e-05, "8": 1.0384318089057897e-05, "9": 1.370247817907592e-06} |
| Research history json | {"away": [{"away": "Academico Viseu", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-11-08T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-10-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 5.0, "home_xg": 1.78, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 2.0, "away_xg": 2.13, "date": "2026-10-10T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 0.19, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 3.0, "away_xg": 1.31, "date": "2026-09-05T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 0.13, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "teams": {"away": "Nacional", "home": "Maritimo"}} |
| Unadjusted home-win probability | 33.8% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.5% |
| P home draw | 69.8% |
| P draw away | 57.3% |
| P home away | 72.8% |
| Raw p home draw | 59.0% |
| Raw p draw away | 66.2% |
| Raw p home away | 74.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4666 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:38:51Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.7937, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:38:51Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.7937, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:38:51Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.68, "draw": 3.37, "home": 2.08}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.37 |
| Reference away odds | 3.68 |
| Market reference 1x2 last update utc | 2026-11-24T22:38:51Z |
| Market reference home last update utc | 2026-11-24T22:38:51Z |
| Market reference draw last update utc | 2026-11-24T22:38:51Z |
| Market reference away last update utc | 2026-11-24T22:38:51Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | -3.8% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.6% |
| Raw edge prob home | -0.1262 |
| Raw ev home | -0.2967 |
| Raw edge prob draw | -0.0279 |
| Raw ev draw | -0.1501 |
| Raw edge prob away | 0.1542 |
| Raw ev away | 0.5076 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-08 |
| Elo home rating | 1,397.7708 |
| Elo away rating | 1,372.3069 |
| Elo rating diff | 85.4639 |
| Elo home expectancy | 0.6206 |
| Research p home | 0.3314 |
| Research p draw | 0.2826 |
| Research p away | 0.3860 |
| Research p over 1 5 | 0.7219 |
| Research v4 p home | 0.3422 |
| Research v4 p draw | 0.2674 |
| Research v4 p away | 0.3904 |
| Research v4 p over 1 5 | 0.7201 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2089783490725219, 1.3610310653527327], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T22:40:12.685710+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-08", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T22:40:12.335575+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T22:40:12.392934+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T22:40:12.647069+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22CS+Maritimo%22+%22Nacional%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T22:39:50.001310+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T22:39:50.385468+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T22:40:12.685420+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=CS+Maritimo_vs_Nacional&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 1.5507048527234875, "goals_for": 0.8473887254235924, "last_match": "2026-11-08T00:00:00+00:00", "matches": 10, "points_per_game": 1.0589134132875462, "results": "WLWLLLLLLW", "xg_against": 1.4473966787066475, "xg_for": 0.943443703024997, "xg_matches": 10}, "venue": {"goals_against": 1.7599865214626136, "goals_for": 0.5295057548750894, "last_match": "2026-11-01T00:00:00+00:00", "matches": 4, "points_per_game": 0.0, "results": "LLLL", "xg_against": 1.9738427187746768, "xg_for": 0.5203791930565782, "xg_matches": 4}}, "home": {"all": {"goals_against": 2.3662591888570916, "goals_for": 0.7131841570421359, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.49878383320263503, "results": "LLLDLLLDWW", "xg_against": 1.4454419451949967, "xg_for": 0.932195130990825, "xg_matches": 10}, "venue": {"goals_against": 1.8988119457434338, "goals_for": 0.7157020266306037, "last_match": "2026-11-01T00:00:00+00:00", "matches": 5, "points_per_game": 0.6169046207669643, "results": "LLLDW", "xg_against": 1.3603430415604811, "xg_for": 1.0106319966707003, "xg_matches": 5}}}, "goal_rates": [1.2172257562079754, 1.3190675753403123], "h2h": [], "margin_distribution": {"-1": 0.21055205733892599, "-10": 3.9974036328888434e-07, "-11": 4.7364303309247885e-08, "-12": 5.152666572988558e-09, "-13": 5.154695576304418e-10, "-14": 4.35701958055724e-11, "-2": 0.11327659801238908, "-3": 0.04429959947182904, "-4": 0.013572411677338383, "-5": 0.0034048889726178712, "-6": 0.000721709424219345, "-7": 0.0001322861394246659, "-8": 2.1344047472894262e-05, "-9": 3.074185158044491e-06, "0": 0.2826456443646624, "1": 0.1902932911606628, "10": 1.7544373384013516e-07, "11": 1.9182937011993623e-08, "12": 1.925750751644415e-09, "13": 1.7777682521821772e-10, "14": 1.3866463868119917e-11, "2": 0.09455126602578562, "3": 0.03412172974616685, "4": 0.009647001630583508, "5": 0.002233275857992376, "6": 0.0004368233862590191, "7": 7.388596257925895e-05, "8": 1.1000906156055068e-05, "9": 1.4621293389654565e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T22:40:12.685710+00:00", "p_over_1_5": 0.7218845456491382, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.21392962565096846, "-10": 4.0218009166630653e-07, "-11": 4.765338103437341e-08, "-12": 5.184114752887344e-09, "-13": 5.186156139783702e-10, "-14": 4.383611702063837e-11, "-2": 0.11396795709455647, "-3": 0.04456997244355157, "-4": 0.013655247940473835, "-5": 0.0034256699720148828, "-6": 0.0007261142207428536, "-7": 0.00013309351910891545, "-8": 2.1474316225041844e-05, "-9": 3.092947778626068e-06, "0": 0.2673512449260875, "1": 0.19741266878697042, "10": 1.8007832966600124e-07, "11": 1.9689681583929423e-08, "12": 1.976622197434335e-09, "13": 1.8247305297202758e-10, "14": 1.4232766238435806e-11, "2": 0.09704897223199732, "3": 0.03502310378097286, "4": 0.009901840903042027, "5": 0.0022922710169696135, "6": 0.00044836269745745415, "7": 7.58377653952658e-05, "8": 1.1291510742697386e-05, "9": 1.5007535655646255e-06}, "p_over_1_5": 0.7200695877669315, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
