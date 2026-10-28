# Super Lig — football model report

Fixtures in this report: **4**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-10-28T16:15:29.997224+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1503, 'tuning_matches': 189, 'audit_matches': 94, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8834174290444695, 'audit_candidate_poisson_score': 0.8729949930531874, 'audit_gain': 0.01042243599128212, 'audit_gain_lower95': 0.002954801922451648, 'audit_baseline_briers': [0.6143643810373778, 0.1743720840360049, 0.20593319507460298, 0.24831013667275378], 'audit_candidate_briers': [0.6098501623735598, 0.17317012147102395, 0.20306904372515894, 0.24810655492785746], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1659.900 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 4.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2, 'ANCHORED_MAIN': 2} |
| Shot features applied fixtures | 4 |
| Goal rate features used | {'shot_features': 4} |
| Legacy comparison status | {'AVAILABLE': 4} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Torku Konyaspor vs Galatasaray

The model's most likely 1X2 outcome is **Galatasaray win** at **57.9%**. Expected goals are 0.95 for Torku Konyaspor and 1.80 for Galatasaray (2.75 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.7%; Under 3.5 goals: 70.0%; Double Chance 1X: 42.1%; Double Chance X2: 81.0%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 85.2%; BTTS Yes (both teams score): 51.9%; BTTS No (at least one team does not score): 48.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torku Konyaspor win | 19.0% | 5.26 |
| Draw | 23.1% | 4.32 |
| Galatasaray win | 57.9% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torku Konyaspor expected goals | 0.95 |
| Galatasaray expected goals | 1.80 |
| Expected total goals | 2.75 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.3% |
| Under 1.5 | 22.7% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.0% |
| Under 3.5 | 70.0% |
| Over 4.5 | 14.8% |
| Under 4.5 | 85.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 0-1 | 10.71% |
| 3 | 0-2 | 10.62% |
| 4 | 1-2 | 10.11% |
| 5 | 0-0 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torku Konyaspor win | 19.0% | 19.2% | 4.78 | -9.2% |
| Draw | 23.1% | 22.3% | 4.14 | -4.3% |
| Galatasaray win | 57.9% | 58.5% | 1.66 | -3.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T17:00:00+00:00 |
| Fixture id | feb03ec355aa5c94e0d7ae612a59b813 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:15:13Z |
| Market best draw last update utc | 2026-10-28T16:15:13Z |
| Market best away last update utc | 2026-10-28T16:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Konyaspor |
| Matched away-team name | Galatasaray |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9032 |
| Dc lambda away | 1.8387 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.1490 |
| Shot lambda away | 1.6581 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.9% |
| P btts no | 48.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.62 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.41 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.75 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.24166285263647563, "-10": 7.6184457211607295e-06, "-11": 1.2325668273435258e-06, "-12": 1.8315056397576446e-07, "-13": 2.5159746814983064e-08, "-14": 3.2127435319086767e-09, "-15": 3.814966226880306e-10, "-16": 3.881474256343987e-11, "-2": 0.181626101825762, "-3": 0.09637985332840697, "-4": 0.040164818020161655, "-5": 0.013724477601013762, "-6": 0.003965804214806433, "-7": 0.0009915251194627355, "-8": 0.00021830078208663433, "-9": 4.291594075780153e-05, "0": 0.23127295690307795, "1": 0.1217230195041501, "10": 1.2819929078197677e-08, "11": 1.095826695574535e-09, "12": 8.6030375269021e-11, "13": 6.243986846066979e-12, "14": 4.212538925902074e-13, "15": 2.642839095536285e-14, "16": 1.4206558736127353e-15, "2": 0.050338498648399524, "3": 0.014113034840810536, "4": 0.0031073638732993804, "5": 0.0005609889249042646, "6": 8.564497575228188e-05, "7": 1.1313226912007118e-05, "8": 1.3159828345359645e-06, "9": 1.3668653238262268e-07} |
| Raw goal margin distribution | {"-1": 0.23515976147864429, "-10": 7.41343511872352e-06, "-11": 1.1993987406935211e-06, "-12": 1.7822202489684256e-07, "-13": 2.448270387991553e-08, "-14": 3.126289350693811e-09, "-15": 3.712306373010378e-10, "-16": 3.7770246868698135e-11, "-2": 0.17673858566873304, "-3": 0.09378629389163302, "-4": 0.03908399210888383, "-5": 0.013355155100847529, "-6": 0.0038590853457637305, "-7": 0.0009648434091096543, "-8": 0.00021242635881368405, "-9": 4.1761082773517575e-05, "0": 0.2506341909762234, "1": 0.11929662187533727, "10": 1.2564379670668996e-08, "11": 1.0739827476790328e-09, "12": 8.431546629445755e-11, "13": 6.119520702034799e-12, "14": 4.128567180025839e-13, "15": 2.590157371562748e-14, "16": 1.3923368583834471e-15, "2": 0.04933506302664098, "3": 0.013831708971532965, "4": 0.0030454224232372147, "5": 0.0005498063055219748, "6": 8.393774923973234e-05, "7": 1.1087711745974128e-05, "8": 1.2897503466936175e-06, "9": 1.339618556582457e-07} |
| Unadjusted home-win probability | 18.6% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 56.3% |
| Raw p over 1 5 | 77.2% |
| Raw p under 3 5 | 70.2% |
| Raw p btts yes | 52.3% |
| P home draw | 42.1% |
| P draw away | 81.0% |
| P home away | 76.9% |
| Raw p home draw | 43.7% |
| Raw p draw away | 81.4% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5274 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.78 |
| Reference draw odds | 4.14 |
| Reference away odds | 1.66 |
| Market reference 1x2 last update utc | 2026-10-28T16:15:13Z |
| Market reference home last update utc | 2026-10-28T16:15:13Z |
| Market reference draw last update utc | 2026-10-28T16:15:13Z |
| Market reference away last update utc | 2026-10-28T16:15:13Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-28T16:14:47Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:14:47Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | -0.0054 |
| Raw ev home | -0.1102 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0376 |
| Raw edge prob away | -0.0222 |
| Raw ev away | -0.0651 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.07150356633009777, 0.10892995985552882, 0.10922834212762712, 0.06677185450738614, 0.030613486853618494, 0.011228510386609117, 0.003432023444031124, 0.0008991487751007007, 0.00020612037368939338, 4.2000819368886635e-05, 7.702595898086878e-06, 1.2841737258880766e-06, 1.962555219574252e-07, 2.7685851428632254e-08, 3.6266796841042873e-09, 4.434016364158567e-10, 5.082257437446263e-11], [0.05120028280595085, 0.11196190445336036, 0.09854781709649382, 0.06024279392155353, 0.027620050294375486, 0.010130568369816519, 0.003096434607036963, 0.0008112285447638265, 0.00018596558814807463, 3.789391090667314e-05, 6.94942353739961e-06, 1.1586051293452e-06, 1.7706533767068374e-07, 2.497868382513392e-08, 3.2720570432084016e-09, 4.0004510289773783e-10, 4.585306035292016e-11], [0.02795862269228757, 0.051273755060431726, 0.04230182883852231, 0.027176077751991413, 0.012459658416428656, 0.004569992455006292, 0.001396830096299482, 0.00036595264880716333, 8.389078516656821e-05, 1.7094291318357037e-05, 3.1349487978564974e-06, 5.226574172496355e-07, 7.987580041501877e-08, 1.1268113737523419e-08, 1.4760549905931313e-09, 1.8046402088869076e-10, 2.068473674943359e-11], [0.008408261023590598, 0.015420041285749215, 0.0141395273402604, 0.007776920371839915, 0.0037471109139796403, 0.0013743770521332688, 0.00042008192551391626, 0.00011005640110783468, 2.5229269228238724e-05, 5.140927899058978e-06, 9.428028010564443e-07, 1.5718370817182303e-07, 2.4021804891804285e-08, 3.388766413545097e-09, 4.4390797725183435e-10, 5.427265175753424e-11, 6.220716510526513e-12], [0.0018965218946658403, 0.0034780611392801726, 0.0031892353372230168, 0.0019495961742058527, 0.0008042270706357693, 0.00030999705689250417, 9.475140781848761e-05, 2.4823726780546867e-05, 5.690577557419991e-06, 1.1595599009247096e-06, 2.1265350225679317e-07, 3.545350735381061e-08, 5.418228430216257e-09, 7.64351829845077e-10, 1.0012548322571216e-10, 1.224144588886515e-11, 1.4031111819224675e-12], [0.0003422153795516648, 0.0006275941323062745, 0.0005754773432761544, 0.00035179229757634006, 0.00016128934798218352, 5.3226719079012136e-05, 1.7097292196234597e-05, 4.479284476485555e-06, 1.0268287248135316e-06, 2.092352493920237e-07, 3.837197935467107e-08, 6.39736114286188e-09, 9.776850475384468e-10, 1.3792245283175636e-10, 1.806701011006161e-11, 2.2088914780798123e-12, 2.5318253747836935e-13], [5.1458833813571025e-05, 9.437115946989525e-05, 8.653437203763137e-05, 5.289891237965883e-05, 2.425303551403183e-05, 8.895604165518882e-06, 2.4463478725227915e-06, 6.73548791936687e-07, 1.544039568718545e-07, 3.1462647705988685e-08, 5.769984128991175e-09, 9.619694600728084e-10, 1.4701423544788042e-10, 2.0739361827418812e-11, 2.7167314104344875e-12, 3.321504125023166e-13, 3.8070989496924974e-14], [6.6324436155345995e-06, 1.216334199069306e-05, 1.115327147569214e-05, 6.818052949903121e-06, 3.125933462369919e-06, 1.1465396450231832e-06, 3.504428286341015e-07, 8.260629654681299e-08, 1.990086953151931e-08, 4.055168402404918e-09, 7.436836702655887e-10, 1.239866458480942e-10, 1.8948420611736555e-11, 2.6730618972218083e-12, 3.50154998916951e-13, 4.2810314955431305e-14, 4.9069065991809e-15], [7.479890608002661e-07, 1.3717488273102503e-06, 1.257835805254852e-06, 7.689215797537474e-07, 3.525343252320638e-07, 1.2930364160842334e-07, 3.952199482559518e-08, 1.0354286273531607e-08, 2.1356210656492675e-09, 4.573309296738411e-10, 8.387063385681197e-11, 1.3982878733031786e-11, 2.136951651398067e-12, 3.0146069440844496e-13, 3.9489534168214313e-14, 4.8280315871928576e-15, 5.533876609156983e-16], [7.49832748107668e-08, 1.375129994274309e-07, 1.2609361927210305e-07, 7.7081686276158e-08, 3.53403272513403e-08, 1.296223568080537e-08, 3.961941095644766e-09, 1.0379808125628333e-09, 2.3794615406544935e-10, 4.3624473162398144e-11, 8.40773631142427e-12, 1.4017344552643437e-12, 2.1422189351628839e-13, 3.0220375240900814e-14, 3.958687028813463e-15, 4.839932002618077e-16, 5.547516832790889e-17], [6.7651288185931e-09, 1.240667545803306e-08, 1.1376397999836668e-08, 6.954451356367159e-09, 3.1884692546426865e-09, 1.1694767183604073e-09, 3.5745360483863663e-10, 9.364853596934676e-11, 2.146793919316023e-11, 4.3744876847201406e-12, 7.218072055661023e-13, 1.2646705793065822e-13, 1.9327492818338866e-14, 2.726537777482605e-15, 3.571600169504891e-16, 4.366675575796678e-17, 5.0050716098832085e-18], [5.548748649453037e-10, 1.0175936857663506e-09, 9.330904810525338e-10, 5.704030714873235e-10, 2.615177766001569e-10, 9.592030744092443e-11, 2.931829179127122e-11, 7.681039066913608e-12, 1.760797196901868e-12, 3.5879483278912214e-13, 6.57999450682983e-14, 9.870220635321176e-15, 1.58523810187215e-15, 2.236302251763411e-16, 2.92942117561154e-17, 3.581540847708536e-18, 4.1051523304963067e-19], [4.171819147923107e-11, 7.65076432774474e-11, 7.015428128977261e-11, 4.288567758244982e-11, 1.966217857156598e-11, 7.211755308039866e-12, 2.2042917927320203e-12, 5.774978806880055e-13, 1.323852984829047e-13, 2.6975940850250576e-14, 4.947159947410387e-15, 8.247885396413146e-16, 1.134110540267627e-16, 1.6813608155362738e-17, 2.20248133855411e-18, 2.692776629738324e-19, 3.086453213049005e-20], [2.8953014486126235e-12, 5.309738571035825e-12, 4.868806269940443e-12, 2.9763266341738714e-12, 1.3645829812511411e-12, 5.005060106884686e-13, 1.5298096572185273e-13, 4.0079169092435473e-14, 9.1877268136944e-15, 1.87216841986791e-15, 3.433398921280288e-16, 5.724149031751373e-17, 8.74800529976243e-18, 1.1103494968643789e-18, 1.5285531764320678e-19, 1.8688250378142446e-20, 2.1420421504284685e-21], [1.8658529726371812e-13, 3.421816923913343e-13, 3.1376617644826027e-13, 1.9180689805455728e-13, 8.793941691969931e-14, 3.225469418092371e-14, 9.858731282913678e-15, 2.5828687657992596e-15, 5.920954239609359e-16, 1.2065033895388922e-16, 2.2126254199160718e-17, 3.688880303579238e-18, 5.637579361910308e-19, 7.952957607217378e-20, 9.373345961831162e-21, 1.2043487747417062e-21, 1.3804212738560479e-22], [1.1222712218870208e-14, 2.05815073137633e-14, 1.8872373943361085e-14, 1.1536780496793452e-14, 5.2893705091357115e-15, 1.940051846574746e-15, 5.929818997202829e-16, 1.5535411033326957e-16, 3.561329132933589e-17, 7.256863499136689e-18, 1.330847537294327e-18, 2.218783723264915e-19, 3.390885118902886e-20, 4.783536314146163e-21, 6.266144284350095e-22, 6.892918548853424e-23, 8.302942903050007e-24], [6.328335722721244e-16, 1.1605633773815936e-15, 1.0641876568616909e-15, 6.505434579378489e-16, 2.982604533633983e-16, 1.093969012585644e-16, 3.343744779107191e-17, 8.760208289405638e-18, 2.0081853595440708e-18, 4.092047236075502e-19, 7.504469372024166e-20, 1.2511421502300042e-20, 1.912074283925393e-21, 2.6973714684446344e-22, 3.533394062417673e-23, 4.3199643912445844e-24, 4.455066584541089e-25]] |
| Legacy trial inputs | {"lambda_home": 0.9022183727859413, "lambda_away": 1.833915626844368, "rho": -0.09481858246728825, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1813 |
| Legacy p draw | 0.2344 |
| Legacy p away | 0.5843 |
| Legacy p over 1 5 | 0.7684 |
| Legacy p under 3 5 | 0.7058 |
| Legacy p btts yes | 0.5073 |
| Legacy p over 2 5 | 0.5192 |
| Legacy goal margin distribution | {"-1": 0.23872875388261064, "-10": 8.944567966706336e-06, "-11": 1.472963579901962e-06, "-12": 2.227659365360917e-07, "-13": 3.114459320923988e-08, "-14": 4.047409523751459e-09, "-15": 4.892546967687769e-10, "-16": 5.082257437446263e-11, "-2": 0.18340456075445474, "-3": 0.09940786195831842, "-4": 0.04225684742978745, "-5": 0.014717325824785105, "-6": 0.004332502902451253, "-7": 0.0011031879096549905, "-8": 0.00024731197601307294, "-9": 4.949770488432496e-05, "0": 0.23440420491768155, "1": 0.11873370737249872, "10": 7.855943025189611e-09, "11": 6.364485201581566e-10, "12": 4.735353126766531e-11, "13": 3.257006058405257e-12, "14": 2.082309922343431e-13, "15": 1.2383275596251802e-14, "16": 6.328335722721244e-16, "2": 0.04694513176980257, "3": 0.012517957713008312, "4": 0.0026178343137894865, "5": 0.0004485452717860751, "6": 6.496037993032757e-05, "7": 8.137509398605085e-06, "8": 8.974690339996969e-07, "9": 8.836732386685239e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1711 |
| Legacy raw p draw | 0.2458 |
| Legacy raw p away | 0.5831 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9022 |
| Legacy lambda away | 1.8339 |
| Legacy model home team | Konyaspor |
| Legacy model away team | Galatasaray |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,456.7365 |
| Elo away rating | 1,677.5170 |
| Elo rating diff | -160.7805 |
| Elo home expectancy | 0.2838 |

</details>


---

## 2026-10-31 — Erzurum BB vs Çorum FK

The model's most likely 1X2 outcome is **Çorum FK win** at **37.1%**. Expected goals are 1.26 for Erzurum BB and 1.48 for Çorum FK (2.74 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 47.4%; Under 3.5 goals: 74.3%; Double Chance 1X: 62.9%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 88.2%; BTTS Yes (both teams score): 53.3%; BTTS No (at least one team does not score): 46.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Erzurum BB win | 34.1% | 2.93 |
| Draw | 28.8% | 3.47 |
| Çorum FK win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Erzurum BB expected goals | 1.26 |
| Çorum FK expected goals | 1.48 |
| Expected total goals | 2.74 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 47.4% |
| Under 2.5 | 52.6% |
| Over 3.5 | 25.7% |
| Under 3.5 | 74.3% |
| Over 4.5 | 11.8% |
| Under 4.5 | 88.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.75% |
| 2 | 0-0 | 8.85% |
| 3 | 1-0 | 8.69% |
| 4 | 0-1 | 8.64% |
| 5 | 2-1 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Erzurum BB win | 34.1% | 35.4% | 2.70 | -7.8% |
| Draw | 28.8% | 29.2% | 3.24 | -6.7% |
| Çorum FK win | 37.1% | 35.4% | 2.70 | +0.1% |
| Over 2.5 | 47.4% | 47.4% | 2.02 | -4.3% |
| Under 2.5 | 52.6% | 52.6% | 1.83 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T10:30:00+00:00 |
| Fixture id | 7ef8c62daf5d4e448691625fb8c2de1b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:15:13Z |
| Market best draw last update utc | 2026-10-28T16:15:13Z |
| Market best away last update utc | 2026-10-28T16:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Erzurumspor |
| Matched away-team name | Corum |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2394 |
| Dc lambda away | 1.5081 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3507 |
| Shot lambda away | 1.3444 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.3% |
| P btts no | 46.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.11 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.89 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.46 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19155545571636368, "-10": 5.864086831935114e-07, "-11": 7.296523842116297e-08, "-12": 8.33586239515898e-09, "-13": 8.755760760809302e-10, "-14": 7.755932556526141e-11, "-2": 0.11296322230151726, "-3": 0.046296667956341506, "-4": 0.014876669893102365, "-5": 0.0039160418320836575, "-6": 0.0008712121384124114, "-7": 0.00016763814170341892, "-8": 2.839796556119486e-05, "-9": 4.2946903317657046e-06, "0": 0.2879517317084414, "1": 0.19502311256835908, "10": 1.4748036896145945e-07, "11": 1.5692823717537167e-08, "12": 1.5331579328878033e-09, "13": 1.3771508404369798e-10, "14": 1.0432128217181721e-11, "2": 0.09932549925316626, "3": 0.034811656302600025, "4": 0.009566034556589921, "5": 0.002153400496218154, "6": 0.00040968746044505117, "7": 6.74144287821688e-05, "8": 9.76604039976088e-06, "9": 1.2630321636809043e-06} |
| Raw goal margin distribution | {"-1": 0.2051872508154225, "-10": 1.0316638833812417e-06, "-11": 1.364693053670672e-07, "-12": 1.6582500826732552e-08, "-13": 1.862540177693122e-09, "-14": 1.9333749219036942e-10, "-15": 1.69169355652327e-11, "-2": 0.12575834522477358, "-3": 0.05412824834688017, "-4": 0.018352577925337482, "-5": 0.005111272542333838, "-6": 0.0012051021266557306, "-7": 0.0002460200826751319, "-8": 4.425008946497578e-05, "-9": 7.109286071306766e-06, "0": 0.27762484122751746, "1": 0.17379254298335986, "10": 2.157997315691925e-07, "11": 2.4411750435622553e-08, "12": 2.5366773751745988e-09, "13": 2.436532030665818e-10, "14": 2.162886965623429e-11, "15": 1.6184180181551961e-12, "2": 0.09196855199417753, "3": 0.033851488888200866, "4": 0.009815267633536868, "5": 0.0023376816916197253, "6": 0.00047133691697069636, "7": 8.228665935000667e-05, "8": 1.2656810902328411e-05, "9": 1.7389512057323152e-06} |
| Unadjusted home-win probability | 31.2% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 41.0% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 56.4% |
| P home draw | 62.9% |
| P draw away | 65.9% |
| P home away | 71.2% |
| Raw p home draw | 59.0% |
| Raw p draw away | 68.8% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9391 |
| Totals anchor target over 2 5 | 0.4738 |
| Totals anchor reference over odds | 2.02 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-10-28T16:15:13Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5112 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.70 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-28T16:15:13Z |
| Market reference home last update utc | 2026-10-28T16:15:13Z |
| Market reference draw last update utc | 2026-10-28T16:15:13Z |
| Market reference away last update utc | 2026-10-28T16:15:13Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.02 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market best over 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market best under 2 5 last update utc | 2026-10-28T16:15:13Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0415 |
| Raw ev home | -0.1567 |
| Raw edge prob draw | -0.0148 |
| Raw ev draw | -0.1005 |
| Raw edge prob away | 0.0562 |
| Raw ev away | 0.1071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.07825667564250269, 0.07870808318128421, 0.06685246375046039, 0.03340614701796966, 0.012519777835919892, 0.0037536765189107426, 0.0009378552607776486, 0.00020084822799432389, 3.763641451788042e-05, 6.2689666472459354e-06, 9.397799709387837e-07, 1.2807481149525933e-07, 1.5999731880038365e-08, 1.8450136273018994e-09, 1.97561251275436e-10, 1.974425424258446e-11], [0.07458326406665507, 0.1353498830827557, 0.08286214811911984, 0.04140617932384028, 0.015517987329993106, 0.004652598905887025, 0.001162450823397187, 0.00024894693005856206, 4.664950219477473e-05, 7.770245309386035e-06, 1.1648364590119591e-06, 1.5874589214934426e-07, 1.9831313290990153e-08, 2.2868535262656154e-09, 2.448727952179787e-10, 2.447256582281647e-11], [0.053880915254960526, 0.08077280965389606, 0.05742813725576971, 0.025661021088061717, 0.009617100795628183, 0.002883396647261266, 0.0007204160243747726, 0.0001542821029701443, 2.891051237075768e-05, 4.815523479819454e-06, 7.21894495627585e-07, 9.838100864674714e-08, 1.2290236792532419e-08, 1.417252147411306e-09, 1.5175720302122232e-10, 1.516660165012365e-11], [0.022261400354246664, 0.03337203618264813, 0.025013987917510416, 0.011856355602801238, 0.00397339447642202, 0.0011913020935342426, 0.0002976465686288625, 6.374308315776597e-05, 1.1944646583793615e-05, 1.9895782317778383e-06, 2.9825741275271155e-07, 4.0647027066568066e-08, 5.077825430255064e-09, 5.855508821100481e-10, 6.269989730334242e-11, 6.266222274605791e-12], [0.00689812816913539, 0.01034097492474304, 0.0077510709986972895, 0.003873206802006894, 0.0013768931203379518, 0.00036914813976609846, 9.223158232781927e-05, 1.9752034935854556e-05, 3.7012812203575255e-06, 6.165095378964862e-07, 9.242086426833611e-08, 1.259527244188005e-08, 1.5734630383084824e-09, 1.814443372864846e-10, 1.9428783495534908e-11, 1.9417109300707605e-12], [0.0017100154161233388, 0.002563481875877045, 0.0019214561652455059, 0.0009601508088672876, 0.0003598402057421054, 0.00010233618374326426, 2.286380069591953e-05, 4.896441963958401e-06, 9.175312187643045e-07, 1.5282998345944125e-07, 2.2910722850501375e-08, 3.122312244393673e-09, 3.9005451714374533e-10, 4.4979247459685994e-11, 4.816309363827261e-12, 4.813415382643375e-13], [0.0003532543722589297, 0.0005295631678648993, 0.00039693372648980503, 0.00019834761023923618, 7.433566083347117e-05, 2.22872984045896e-05, 5.281967357263731e-06, 1.0115052273631946e-06, 1.8954327057901623e-07, 3.1571563250406116e-08, 4.7328889214928765e-09, 6.450061452604487e-10, 8.057732246224111e-11, 9.291796831909026e-12, 9.949514635258049e-13, 9.943536259292525e-14], [6.255013860950216e-05, 9.376883105683678e-05, 7.02843660559842e-05, 3.512106710524689e-05, 1.3162486451418652e-05, 3.9463732480473944e-06, 9.860004965871256e-07, 2.002943179054289e-07, 3.356209796187778e-08, 5.590321911101688e-09, 8.380444272201732e-10, 1.142101187085927e-10, 1.426768664338401e-11, 1.6452823387596464e-12, 1.7617432887044174e-13, 1.7606847080479006e-14], [9.691188924761856e-06, 1.4528048653881548e-05, 1.088948937680193e-05, 5.441473098582082e-06, 2.0393263029626347e-06, 6.114302792071427e-07, 1.5276572210318392e-07, 3.271584205568819e-08, 5.8151062098206954e-09, 8.661350237598363e-10, 1.2984218823618647e-10, 1.769511406576337e-11, 2.2105601978527138e-12, 2.5491137723988283e-13, 2.7295522323865976e-14, 2.7279121232897265e-15], [1.3346682249296263e-06, 2.000799392015136e-06, 1.4996978770882234e-06, 7.49398375975353e-07, 2.8085553155123547e-07, 8.420603207234207e-08, 2.1038858774962886e-08, 4.505617956943953e-09, 8.442957489848526e-10, 1.3339563803139655e-10, 1.788183516383444e-11, 2.4369668843970053e-12, 3.044378226731005e-13, 3.510633401293239e-14, 3.759132817588366e-15, 3.7568740632559444e-16], [1.6542917035460738e-07, 2.4799465311652196e-07, 1.8588423021935066e-07, 9.288626887721818e-08, 3.4811421075430896e-08, 1.0437151169396803e-08, 2.6077199466806637e-09, 5.584613663754228e-10, 1.0464858807577479e-10, 1.7430951293639784e-11, 2.4786238529502406e-12, 3.0205664774008225e-13, 3.773439382812129e-14, 4.351352344705262e-15, 4.65936186724765e-16, 4.6565621912812344e-17], [1.864052660023207e-08, 2.7943989069308076e-08, 2.0945398750051607e-08, 1.0466406632461669e-08, 3.922544126634293e-09, 1.1760561549498568e-09, 2.9383737419380013e-10, 6.292731767201955e-11, 1.1791782462075797e-11, 1.9641161867641115e-12, 2.944404009117641e-13, 3.8062231876968597e-14, 4.2519041254270415e-15, 4.903095321979386e-16, 5.250159850307068e-17, 5.247005180897064e-18], [1.9253766546938393e-09, 2.8863296272110556e-09, 2.1634464863294595e-09, 1.0810732669120826e-09, 4.05158880454272e-10, 1.2147462965564848e-10, 3.035040976483128e-11, 6.499751374336233e-12, 1.2179710990260505e-12, 2.0287320922869337e-13, 3.0412696286549515e-14, 4.144693933061195e-15, 4.911348531989447e-16, 5.064398378402118e-17, 5.4228807082447345e-18, 5.419622255860014e-19], [1.835739783673874e-10, 2.7519551109912347e-10, 2.062726155488766e-10, 1.0307433614605491e-10, 3.862965065798739e-11, 1.1581931765002283e-11, 2.8937431291834336e-12, 6.19715220539811e-13, 1.1612678466814833e-13, 1.934283457290212e-14, 2.899681803344984e-15, 3.951735638594851e-16, 4.936701443487982e-17, 5.39986679070649e-18, 5.170415790579633e-19, 5.167309037071815e-20], [1.6252562874949005e-11, 2.4364195769027413e-11, 1.8262167020638457e-11, 9.125596905977363e-12, 3.42004259939159e-12, 1.025396278373131e-12, 2.561950368416737e-13, 5.486594928083494e-14, 1.0281184109370705e-14, 1.7125010737996737e-15, 2.567208122051692e-16, 3.498634855693115e-17, 4.370665783827334e-18, 5.04004566576789e-19, 5.1191277911693614e-20, 4.574832215665572e-21], [1.3429794472858218e-12, 2.0132587345892467e-12, 1.509036769174496e-12, 7.540650162832329e-13, 2.8260447014817624e-13, 8.473039838541816e-14, 2.1169871584088938e-14, 4.533675261368206e-15, 8.495533325349321e-16, 1.4150714341260954e-16, 2.1213317378607416e-17, 2.8909869421245942e-18, 3.611562289466857e-19, 4.164683314618158e-20, 4.459479510756274e-21, 4.2274886401396184e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2394778512340048, "lambda_away": 1.4990986933255512, "rho": -0.09481858246728825, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T16:15:13Z", "over": 2.02, "under": 1.83, "bookmaker": "pinnacle", "event_id": "7ef8c62daf5d4e448691625fb8c2de1b", "kickoff_utc": "2026-10-31T10:30:00Z", "home_team": "Erzurum BB", "away_team": "\u00c7orum FK"}} |
| Legacy p home | 0.3282 |
| Legacy p draw | 0.2844 |
| Legacy p away | 0.3875 |
| Legacy p over 1 5 | 0.7685 |
| Legacy p under 3 5 | 0.7069 |
| Legacy p btts yes | 0.5656 |
| Legacy p over 2 5 | 0.5124 |
| Legacy goal margin distribution | {"-1": 0.19159770475699836, "-10": 1.111421560887804e-06, "-11": 1.493880185418942e-07, "-12": 1.844460883159981e-08, "-13": 2.105053024170002e-09, "-14": 2.2203381709825247e-10, "-15": 1.974425424258446e-11, "-2": 0.11916436925366475, "-3": 0.052125879557619145, "-4": 0.017960394809888452, "-5": 0.0050829941716551644, "-6": 0.0012177979068655352, "-7": 0.00025262450587932884, "-8": 4.6170820804804685e-05, "-9": 7.53744830041691e-06, "0": 0.2843757691006047, "1": 0.18462641552257908, "10": 1.9564318501938873e-07, "11": 2.1742537044368128e-08, "12": 2.2195883978298843e-09, "13": 2.094472109055893e-10, "14": 1.8265821609538252e-11, "15": 1.3429794472858218e-12, "2": 0.09604261265723829, "3": 0.0347359745805228, "4": 0.00989579104282736, "5": 0.002315596016280511, "6": 0.0004586981095263218, "7": 7.867481837756407e-05, "8": 1.1888755955169734e-05, "9": 1.60472902627992e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3025 |
| Legacy raw p draw | 0.2764 |
| Legacy raw p away | 0.4211 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2395 |
| Legacy lambda away | 1.4991 |
| Legacy model home team | Erzurumspor |
| Legacy model away team | Corum |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,438.6446 |
| Elo away rating | 1,451.6385 |
| Elo rating diff | 47.0060 |
| Elo home expectancy | 0.5672 |

</details>


---

## 2026-10-31 — Fenerbahce vs Goztepe

The model's most likely 1X2 outcome is **Fenerbahce win** at **72.2%**. Expected goals are 2.45 for Fenerbahce and 1.04 for Goztepe (3.49 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 69.0%; Under 3.5 goals: 53.1%; Double Chance 1X: 88.6%; Double Chance X2: 27.8%; Double Chance 12 (either team wins): 83.6%; Under 4.5 goals: 71.9%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 72.2% | 1.39 |
| Draw | 16.4% | 6.08 |
| Goztepe win | 11.4% | 8.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 2.45 |
| Goztepe expected goals | 1.04 |
| Expected total goals | 3.49 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 46.9% |
| Under 3.5 | 53.1% |
| Over 4.5 | 28.1% |
| Under 4.5 | 71.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.17% |
| 2 | 2-0 | 9.76% |
| 3 | 3-1 | 8.31% |
| 4 | 3-0 | 7.97% |
| 5 | 1-1 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 72.2% | 74.2% | 1.32 | -4.7% |
| Draw | 16.4% | 15.4% | 5.69 | -6.5% |
| Goztepe win | 11.4% | 10.5% | 8.12 | -7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:00:00+00:00 |
| Fixture id | dc20aff5555a04cd21c2355e222a3297 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:15:13Z |
| Market best draw last update utc | 2026-10-28T16:15:13Z |
| Market best away last update utc | 2026-10-28T16:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fenerbahce |
| Matched away-team name | Goztep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5517 |
| Dc lambda away | 1.0230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 2.0453 |
| Shot lambda away | 1.1229 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.41 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.01 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.56 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.07245522500391509, "-10": 1.3496836920020323e-08, "-11": 1.2557550303962162e-09, "-12": 1.074050779890627e-10, "-13": 8.498837596581806e-12, "-14": 6.255973388807363e-13, "-15": 4.304286713875848e-14, "-16": 2.7786759641636315e-15, "-17": 1.676780432854594e-16, "-18": 8.50759443766505e-18, "-2": 0.030235820985758704, "-3": 0.008829818487516534, "-4": 0.0020587798113148987, "-5": 0.0003974462481937599, "-6": 6.528142351957943e-05, "-7": 9.315503406719947e-06, "-8": 1.1739050118529217e-06, "-9": 1.3236092505248613e-07, "0": 0.16435453001680705, "1": 0.22723752314356183, "10": 8.798499376828786e-05, "11": 1.923374492304052e-05, "12": 3.865147383053747e-06, "13": 7.185931828217245e-07, "14": 1.2427986517910158e-07, "15": 2.0090437379562717e-08, "16": 3.047252359152273e-09, "17": 4.320450495608215e-10, "18": 5.150411546474854e-11, "2": 0.21224615209168696, "3": 0.1456304375767417, "4": 0.07977973652378771, "5": 0.036186236473675464, "6": 0.013964871687703747, "7": 0.0046820492860008165, "8": 0.001386260750737127, "9": 0.0003672434702066648} |
| Raw goal margin distribution | {"-1": 0.08619593397983513, "-10": 1.6056432976804788e-08, "-11": 1.493901615639581e-09, "-12": 1.2777382184575432e-10, "-13": 1.011059236018827e-11, "-14": 7.442382094212079e-13, "-15": 5.1205694744509665e-14, "-16": 3.3056355831544408e-15, "-17": 1.994772019287832e-16, "-18": 1.0121009884884969e-17, "-2": 0.035969867312864535, "-3": 0.010504341838187341, "-4": 0.0024492153421030362, "-5": 0.0004728196009051295, "-6": 7.766166306845739e-05, "-7": 1.1082134057152872e-05, "-8": 1.39652922056076e-06, "-9": 1.5746239911224508e-07, "0": 0.18923689590243392, "1": 0.2125904219791486, "10": 8.231372483855128e-05, "11": 1.79939910137343e-05, "12": 3.616010691402743e-06, "13": 6.722746571696123e-07, "14": 1.1626912939569884e-07, "15": 1.8795463448035327e-08, "16": 2.8508349147066994e-09, "17": 4.041966226771007e-10, "18": 4.8184302877638117e-11, "2": 0.19856535317063756, "3": 0.13624350304983834, "4": 0.07463735574279362, "5": 0.033853771927076566, "6": 0.013064734749366227, "7": 0.004380257360969593, "8": 0.0012969062234767929, "9": 0.0003435719735908137} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.8% |
| Raw p btts yes | 59.9% |
| P home draw | 88.6% |
| P draw away | 27.8% |
| P home away | 83.6% |
| Raw p home draw | 86.4% |
| Raw p draw away | 32.5% |
| Raw p home away | 81.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6897 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.32 |
| Reference draw odds | 5.69 |
| Reference away odds | 8.12 |
| Market reference 1x2 last update utc | 2026-10-28T16:15:13Z |
| Market reference home last update utc | 2026-10-28T16:15:13Z |
| Market reference draw last update utc | 2026-10-28T16:15:13Z |
| Market reference away last update utc | 2026-10-28T16:15:13Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.42 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-10-28T16:14:25Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:14:25Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.0664 |
| Raw ev home | -0.1089 |
| Raw edge prob draw | 0.0355 |
| Raw ev draw | 0.0768 |
| Raw edge prob away | 0.0309 |
| Raw ev away | 0.1017 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.03177190233553234, 0.019734620595174945, 0.013577837564448365, 0.004717827137966169, 0.0012294608473964136, 0.0002563169749254254, 4.453062479517501e-05, 6.631219729485091e-06, 8.640444837704677e-07, 1.0007515297369075e-07, 1.0431792329839414e-08, 9.885506312850323e-10, 8.587175559791728e-11, 6.885566226042604e-12, 5.126775428913039e-13, 3.562752924974591e-14, 2.3211242708288464e-15, 1.4232531103195278e-16, 8.242184020084903e-18], [0.06515397107657594, 0.07401432266441713, 0.034720982508636096, 0.01206433592673099, 0.003143953400155299, 0.000655448790045514, 0.0001138728488445225, 1.695722629951263e-05, 2.209517772272507e-06, 2.5591023750693734e-07, 2.667597673774306e-08, 2.527902474516254e-09, 2.1958958559851442e-10, 1.7607636220546704e-11, 1.311009055367403e-12, 9.11060258332532e-14, 5.935533904075935e-15, 3.6395152110345577e-16, 2.1076752895000076e-17], [0.09244206986036255, 0.09636122920315002, 0.0450513370883852, 0.015425342758081335, 0.004019828286228067, 0.0008380504578308223, 0.00014559671870326499, 2.1681344873427286e-05, 2.825067966804443e-06, 3.2720434450934135e-07, 3.4107644804100655e-08, 3.2321515552311985e-09, 2.8076511169230595e-10, 2.2512952682272983e-11, 1.6762434468674716e-12, 1.1648727989169493e-13, 7.589116009254962e-15, 4.65344880517356e-16, 2.6948531573329148e-17], [0.07879702187354325, 0.0821376879244658, 0.04280999216191292, 0.013343176874393934, 0.003426475606574638, 0.000714348784666744, 0.00012410570042089167, 1.8481038003799887e-05, 2.4080696452469395e-06, 2.7890686491947656e-07, 2.9073135616104884e-08, 2.7550650605386683e-09, 2.393223635165765e-10, 1.9189895116181803e-11, 1.4288190620105795e-12, 9.929300323413852e-14, 6.4689133539028615e-15, 3.9665696348270476e-16, 2.2970753846717897e-17], [0.05037455348131982, 0.05251022506692235, 0.027368220123294266, 0.009509506282030358, 0.0022229685974256004, 0.0004566797094852258, 7.934017167834038e-05, 1.1814837860329132e-05, 1.5394672317173461e-06, 1.7830380449836206e-07, 1.8586314433475728e-08, 1.7612997158617112e-09, 1.5299762495579118e-10, 1.2268006770387725e-11, 9.134370886490029e-13, 6.347753484600137e-14, 4.135544897054246e-15, 2.5358087076900504e-16, 1.4685091398692106e-17], [0.025763365955782346, 0.026855625535644388, 0.013997096189771789, 0.004863504953817812, 0.0012674243347574686, 0.0002370213058150343, 4.0577429211390924e-05, 6.042534781311114e-06, 7.87339141028353e-07, 9.119100516301425e-08, 9.505712456517223e-09, 9.007922850251705e-10, 7.824851099798401e-11, 6.2743017283660805e-12, 4.671647164311915e-13, 3.2464703847249095e-14, 2.1150670178920122e-15, 1.2969041552756332e-16, 7.510486101656734e-18], [0.010980263173576666, 0.011445780670837295, 0.0059655170870662865, 0.002072810068007736, 0.0005401721487835665, 0.00011261464031845545, 1.755007404267021e-05, 2.5753087639309505e-06, 3.355613932661922e-07, 3.88653112124952e-08, 4.051303878695205e-09, 3.839147559864524e-10, 3.3349262094595807e-11, 2.6740870865293123e-12, 1.9910408991696636e-13, 1.3836351690490791e-14, 9.014347164910675e-16, 5.5273635286135715e-17, 3.2009448648604024e-18], [0.004011216532407123, 0.004181275432783039, 0.0021792720616734497, 0.0007572213782034733, 0.00019733110393571152, 4.1139424428688653e-05, 7.147260824439723e-06, 9.547220223116679e-07, 1.2258443964676626e-07, 1.4197945569088524e-08, 1.4799879419223327e-09, 1.4024847964971704e-10, 1.2182869330430345e-11, 9.76874794439815e-13, 7.27350159572415e-14, 5.054578544406361e-15, 3.293044784551267e-16, 2.0192095231335784e-17, 1.169342005585954e-18], [0.001282175626264, 0.001336534540904893, 0.000696599023737817, 0.00024204397518173815, 6.307640829808424e-05, 1.3150117141479877e-05, 2.2846045706111084e-06, 3.402089005575709e-07, 3.976408869581707e-08, 4.538338831781768e-09, 4.730745525619098e-10, 4.4830086028673763e-11, 3.894224604240731e-12, 3.122556564132299e-13, 2.3249571266683416e-14, 1.6156837603542817e-15, 1.0526137706192712e-16, 6.4543542188892654e-18, 3.737773331895509e-19], [0.0003643060676488557, 0.00037975112995454496, 0.00019792549933694007, 6.877223914596579e-05, 1.792197402429589e-05, 3.7363582389203422e-06, 6.491273817745822e-07, 9.666395476757407e-08, 1.2595263059220902e-08, 1.3085794093979814e-09, 1.3441522863037617e-10, 1.2737625032737376e-11, 1.1064706137381013e-12, 8.872156665501415e-14, 6.605928009540322e-15, 4.59066125764577e-16, 2.990803877973454e-17, 1.8338832501033716e-18, 1.0620179298473436e-19], [9.315964005745417e-05, 9.710922139259086e-05, 5.0613124276024216e-05, 1.758630342374276e-05, 4.582972389116872e-06, 9.554542720354159e-07, 1.659935933206729e-07, 2.471871877071526e-08, 3.2208362067604825e-09, 3.7304291867961576e-10, 3.488141946059988e-11, 3.2572407341301635e-12, 2.829445163382408e-13, 2.2687706708418602e-14, 1.6892550804490124e-15, 1.173914980741395e-16, 7.648025588829915e-18, 4.689570629158334e-19, 2.71577162350488e-20], [2.1656911108350594e-05, 2.2575074079327118e-05, 1.1766081671051406e-05, 4.088304868262571e-06, 1.0654079983769483e-06, 2.2211537340422713e-07, 3.8588690262053726e-08, 5.746384322648132e-09, 7.487508902068538e-10, 8.672164603106643e-11, 9.039828319180872e-12, 7.684274081755927e-13, 6.577638379832087e-14, 5.2742329954637484e-15, 3.927027529738359e-16, 2.729011444333424e-17, 1.7779438631313935e-18, 1.090188993746411e-19, 6.313380408571044e-21], [4.615052705158554e-06, 4.8107117482133034e-06, 2.5073329605238376e-06, 8.712111504448542e-07, 2.2703672007552383e-07, 4.733242657542363e-08, 8.223187438477695e-09, 1.2245451985482957e-09, 1.5955760283868994e-10, 1.8480242408953453e-11, 1.926372783721601e-12, 1.8254936172292533e-13, 1.4224415251959452e-14, 1.1239305149092104e-15, 8.368432106351026e-17, 5.815479218420649e-18, 3.7887695960485983e-19, 2.3231751008034878e-20, 1.3453711467669168e-21], [9.078094725583567e-07, 9.462968190795057e-07, 4.932079345219801e-07, 1.7137263331538277e-07, 4.465953007920406e-08, 9.31058168768329e-09, 1.6175519388822383e-09, 2.408756306456536e-10, 3.138596946330876e-11, 3.6351782278174943e-12, 3.789294667829799e-13, 3.590859094551988e-14, 3.119247156345382e-15, 2.2435811623308727e-16, 1.6461224653220818e-17, 1.1439408083135115e-18, 7.452744634507591e-20, 4.5698294205042344e-21, 2.646428435750109e-22], [1.658166251135362e-07, 1.7284656047180805e-07, 9.008726792768236e-08, 3.1302197820313695e-08, 8.157320209515701e-09, 1.700631332855245e-09, 2.9545517155205483e-10, 4.399732031127205e-11, 5.73282796626449e-12, 6.639862257927192e-13, 6.921364805871912e-14, 6.558910810203992e-15, 5.697484461167453e-16, 4.5684877764591387e-17, 3.0512639708997204e-18, 2.0894737265699065e-19, 1.3612867022023978e-20, 8.347056455768016e-22, 4.8338538546409474e-23], [2.826820354802725e-08, 2.9466657825461948e-08, 1.5357960790250722e-08, 5.3363581539509254e-09, 1.3906493871234994e-09, 2.8992142762758787e-10, 5.0368815087341895e-11, 7.500606198414674e-12, 9.773250887552797e-13, 1.1319551203592027e-13, 1.1799453102399885e-14, 1.1181546223682442e-15, 9.712997737695257e-17, 7.788298807987197e-18, 5.798921635638683e-19, 3.614858735429372e-20, 2.3207039438133385e-21, 1.422995376711857e-22, 8.24069146208016e-24], [4.517931317684259e-09, 4.709472817788278e-09, 2.4545674404867825e-09, 8.528769642242496e-10, 2.2225885020706025e-10, 4.633634023898981e-11, 8.0501347293302e-12, 1.1987752807800626e-12, 1.5619979594897776e-13, 1.8091335304682963e-14, 1.885833268899021e-15, 1.7870770520765732e-16, 1.552368072954257e-17, 1.2447554028789325e-18, 9.268056111856175e-20, 6.44065543326226e-21, 3.763963751208462e-22, 2.2742850872867258e-23, 1.3170585096661886e-24], [6.795980127951895e-10, 7.084101424371297e-10, 3.6922189328048797e-10, 1.2829178871685119e-10, 3.3432706764626804e-11, 6.970022900383535e-12, 1.2109204810998594e-12, 1.803226391284997e-13, 2.3495946144739068e-14, 2.721341839294697e-15, 2.8367154166118236e-16, 2.6881639580250054e-17, 2.3351091092884553e-18, 1.872390788459784e-19, 1.394123122553398e-20, 9.6881876366972e-22, 6.311829065172184e-23, 3.471695743326438e-24, 1.9811508475142533e-25], [9.654749105814586e-11, 1.0064070318737216e-10, 5.245372524465087e-11, 1.8225848355602198e-11, 4.749637133474367e-12, 9.902003993243794e-13, 1.7203012975311326e-13, 2.5617641695616392e-14, 3.337965396605011e-15, 3.8660902761445333e-16, 4.029996426760788e-17, 3.8189559241466684e-18, 3.317386478538243e-19, 2.6600229768572876e-20, 1.9805692067148923e-21, 1.376358069936786e-22, 8.96693705332992e-24, 5.498292879697471e-25, 2.856213806485102e-26]] |
| Legacy trial inputs | {"lambda_home": 2.557180577822498, "lambda_away": 1.042395841511419, "rho": -0.09481858246728825, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7177 |
| Legacy p draw | 0.1667 |
| Legacy p away | 0.1156 |
| Legacy p over 1 5 | 0.8833 |
| Legacy p under 3 5 | 0.5113 |
| Legacy p btts yes | 0.5994 |
| Legacy p over 2 5 | 0.7033 |
| Legacy goal margin distribution | {"-1": 0.07380738117644543, "-10": 1.3260596634957243e-08, "-11": 1.2321476376726715e-09, "-12": 1.0525919670482303e-10, "-13": 8.319792566012477e-12, "-14": 6.117840267886935e-13, "-15": 4.205137878818592e-14, "-16": 2.7120243235056315e-15, "-17": 1.6340206392695284e-16, "-18": 8.242184020084903e-18, "-2": 0.030462083513973136, "-3": 0.008836579264633337, "-4": 0.0020506222479228947, "-5": 0.0003944674442221831, "-6": 6.461134738298334e-05, "-7": 9.198857278578074e-06, "-8": 1.1569769073345192e-06, "-9": 1.3023535297388514e-07, "0": 0.1666592747703666, "1": 0.21522223814600167, "10": 0.00011842187520605299, "11": 2.6993571211171676e-05, "12": 5.6570025512229304e-06, "13": 1.0969012936918035e-06, "14": 1.9787089180533522e-07, "15": 3.3365124107451616e-08, "16": 5.278795185366039e-09, "17": 7.802387159825617e-10, "18": 9.654749105814586e-11, "2": 0.20739517901319876, "3": 0.1475883090330396, "4": 0.08401990215201173, "5": 0.03964937993706855, "6": 0.015931723426917014, "7": 0.005564377279042615, "8": 0.0017168648357793342, "9": 0.0004740989936158278} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6939 |
| Legacy raw p draw | 0.1796 |
| Legacy raw p away | 0.1265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5572 |
| Legacy lambda away | 1.0424 |
| Legacy model home team | Fenerbahce |
| Legacy model away team | Goztep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,643.4256 |
| Elo away rating | 1,515.6231 |
| Elo rating diff | 187.8026 |
| Elo home expectancy | 0.7467 |

</details>


---

## 2026-10-31 — Kocaelispor vs Çaykur Rizespor

The model's most likely 1X2 outcome is **Kocaelispor win** at **38.8%**. Expected goals are 1.18 for Kocaelispor and 0.89 for Çaykur Rizespor (2.07 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 91.8%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.2%; Double Chance 1X: 66.9%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kocaelispor win | 38.8% | 2.58 |
| Draw | 28.2% | 3.55 |
| Çaykur Rizespor win | 33.1% | 3.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kocaelispor expected goals | 1.18 |
| Çaykur Rizespor expected goals | 0.89 |
| Expected total goals | 2.07 |
| Over 0.5 | 91.8% |
| Under 0.5 | 8.2% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.8% |
| Under 3.5 | 72.2% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.45% |
| 2 | 1-2 | 8.35% |
| 3 | 0-0 | 8.18% |
| 4 | 0-1 | 8.13% |
| 5 | 1-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kocaelispor win | 38.8% | 37.7% | 2.54 | -1.6% |
| Draw | 28.2% | 26.4% | 3.57 | +0.6% |
| Çaykur Rizespor win | 33.1% | 35.9% | 2.66 | -12.1% |
| Over 2.5 | 49.7% | 49.7% | 1.93 | -4.0% |
| Under 2.5 | 50.3% | 50.3% | 1.91 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 7d597f0fe7ec1c85b6e7f9f2ce731746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:15:13Z |
| Market best draw last update utc | 2026-10-28T16:15:13Z |
| Market best away last update utc | 2026-10-28T16:15:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Kocaelispor |
| Matched away-team name | Rizespor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1503 |
| Dc lambda away | 0.8781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.2855 |
| Shot lambda away | 0.9313 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.23 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.60 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.59 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19308985810212123, "-10": 1.086542911845035e-07, "-11": 1.1217689694300148e-08, "-12": 1.0637217010763957e-09, "-13": 9.323323815399493e-11, "-14": 7.556299428322429e-12, "-15": 5.189391766469055e-13, "-2": 0.0947116507059006, "-3": 0.03200572484986504, "-4": 0.008500589593274521, "-5": 0.0018520777014543852, "-6": 0.00034133256408028993, "-7": 5.4439510824888376e-05, "-8": 7.646906170392493e-06, "-9": 9.59200166883674e-07, "0": 0.28186291261258944, "1": 0.1878859386155074, "10": 1.3051814670324734e-06, "11": 1.7850506393491766e-07, "12": 2.24232335975841e-08, "13": 2.603539034641308e-09, "14": 2.795281739409392e-10, "15": 2.5430563879491784e-11, "2": 0.11996169551610308, "3": 0.053701938149686004, "4": 0.018894458286448715, "5": 0.005453404374384051, "6": 0.001331402369702411, "7": 0.00028129947381699957, "8": 5.2343597796592945e-05, "9": 8.697814833624968e-06} |
| Raw goal margin distribution | {"-1": 0.16997580974659643, "-10": 1.179768614140493e-08, "-11": 9.45652357704752e-10, "-12": 6.93795578857789e-11, "-13": 4.389727432385027e-12, "-2": 0.06992851932608687, "-3": 0.019128259877531844, "-4": 0.004045285532838173, "-5": 0.0006953577566464168, "-6": 0.00010053785440232376, "-7": 1.2533521259346322e-05, "-8": 1.3726391718539618e-06, "-9": 1.3400126843485624e-07, "0": 0.323682078438281, "1": 0.22930401097155656, "10": 1.963486278703208e-07, "11": 2.0849019969376447e-08, "12": 2.0263234335522464e-09, "13": 1.698391849125844e-10, "2": 0.12271581584352893, "3": 0.04446771087064017, "4": 0.012457806882358407, "5": 0.0028367680030892974, "6": 0.0005433356883288101, "7": 8.972941259358548e-05, "8": 1.3017908491545958e-05, "9": 1.683514411651758e-06} |
| Unadjusted home-win probability | 41.2% |
| Unadjusted draw probability | 32.4% |
| Unadjusted away-win probability | 26.4% |
| Raw p over 1 5 | 62.4% |
| Raw p under 3 5 | 84.5% |
| Raw p btts yes | 42.0% |
| P home draw | 66.9% |
| P draw away | 61.2% |
| P home away | 71.8% |
| Raw p home draw | 73.6% |
| Raw p draw away | 58.8% |
| Raw p home away | 67.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2946 |
| Totals anchor target over 2 5 | 0.4972 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.91 |
| Totals anchor reference last update utc | 2026-10-28T16:15:13Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3536 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:14:47Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:15:13Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.54 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.66 |
| Market reference 1x2 last update utc | 2026-10-28T16:15:13Z |
| Market reference home last update utc | 2026-10-28T16:15:13Z |
| Market reference draw last update utc | 2026-10-28T16:15:13Z |
| Market reference away last update utc | 2026-10-28T16:15:13Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market best over 2 5 last update utc | 2026-10-28T16:15:13Z |
| Market best under 2 5 last update utc | 2026-10-28T16:15:13Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.8% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0355 |
| Raw ev home | 0.0476 |
| Raw edge prob draw | 0.0597 |
| Raw ev draw | 0.1555 |
| Raw edge prob away | -0.0953 |
| Raw ev away | -0.2981 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.12853916769732948, 0.11966027663242845, 0.0593404484951268, 0.017455609649878513, 0.0038510617459432575, 0.0006796979019828505, 9.997010098287657e-05, 1.260310465412621e-05, 1.3902503317597595e-06, 1.3631886131770307e-07, 1.202988294539004e-08, 9.651041167937514e-10, 7.097385156949896e-11, 4.817929862334313e-12], [0.132308428526874, 0.13158203161519813, 0.0689894040242221, 0.020293950200316997, 0.004477257274773111, 0.0007902190556945636, 0.00011622557398797457, 1.4652411651632044e-05, 1.6163096886680836e-06, 1.5848476440721958e-07, 1.3985982174566292e-08, 1.1220332762465055e-09, 8.251443737378298e-11, 5.601341382855291e-12], [0.08393437097563221, 0.0740705026561629, 0.030827013795486784, 0.01179690721188339, 0.0026026371461876975, 0.0004593556594489556, 6.756212065419413e-05, 8.51747141283131e-06, 9.395635267986257e-07, 9.21274587625609e-08, 8.130074842592075e-09, 6.522398211225921e-10, 4.7965780527246774e-11, 3.256069119288284e-12], [0.032527460204104394, 0.028704871430391986, 0.012665754391290647, 0.003514195902094617, 0.0010086115522676855, 0.00017801614235715067, 2.6182649197695335e-05, 3.300813590428894e-06, 3.6411323361251983e-07, 3.570256396482034e-08, 3.15068407405566e-09, 2.5276539966275105e-10, 1.8588392325139162e-11, 1.2618389518902947e-12], [0.00945413352448394, 0.008343094898993274, 0.0036813121114347264, 0.0010828962174401467, 0.00022534244697292022, 5.1740540724593054e-05, 7.610008896682917e-06, 9.593842318930365e-07, 1.0582981600789135e-07, 1.0376980089187813e-08, 9.157489623437818e-10, 7.346647490416914e-11, 5.4027317824581695e-12, 3.667545471644419e-13], [0.002198281455432981, 0.0019399420105371892, 0.0008559811563132675, 0.00025179575333818195, 5.5551253317490726e-05, 9.247833839196363e-06, 1.7694843625736941e-06, 2.2307666378346373e-07, 2.460761965753292e-08, 2.4128623563843762e-09, 2.1293056169970013e-10, 1.7082473921023142e-11, 1.256246810487529e-12, 8.527801280142397e-14], [0.00042595489623539366, 0.00037589717902537323, 0.00016586109286222196, 4.8789764259078024e-05, 1.0764012171470197e-05, 1.8998076303432916e-06, 2.635569893061917e-07, 4.322494598659456e-08, 4.768150161990949e-09, 4.675336418382155e-10, 4.125896394657775e-11, 3.3100235588531825e-12, 2.434194577244721e-13, 1.6524083849325158e-14], [7.074522685312906e-05, 6.243133120109824e-05, 2.7547237382056885e-05, 8.10330617425676e-06, 1.7877537965890068e-06, 3.1553181563070363e-07, 4.64084814443163e-08, 5.518429243217381e-09, 7.919239052329612e-10, 7.765088239538776e-11, 6.852544224571305e-12, 5.4974920966952e-13, 4.042861089139072e-14, 2.744422169559039e-15], [1.0281079689169731e-05, 9.07285932536451e-06, 4.0033137971183934e-06, 1.1776163598461913e-06, 2.5980606840805354e-07, 4.585479311137714e-08, 6.744331981193828e-09, 8.502494340354359e-10, 8.846521250937682e-11, 1.1284646969875654e-11, 9.958488562435265e-13, 7.98925338864812e-14, 5.875304791371082e-15, 3.988342999385349e-16], [1.3280908506551418e-06, 1.1720151796888634e-06, 5.171406687816267e-07, 1.5212230236295754e-07, 3.356126718489473e-08, 5.9234373267291e-09, 8.712203259585603e-10, 1.0983364862998804e-10, 1.211576596693843e-11, 1.120532679338596e-12, 1.2864191258099495e-13, 1.032036969833664e-14, 7.589610015813809e-16, 5.1520676883168166e-17], [1.5440428678971768e-07, 1.3625887704693765e-07, 6.012294723195752e-08, 1.7685789785823424e-08, 3.901844155380308e-09, 6.886608060932188e-10, 1.0128836668062177e-10, 1.2769296749435517e-11, 1.4085830062856327e-12, 1.3811644356543521e-13, 1.1496391568826417e-14, 1.1998496352051599e-15, 8.823706005697961e-17, 5.989811137652894e-18], [1.631917641729578e-08, 1.4401366044842667e-08, 6.35446724314275e-09, 1.8692325815223433e-09, 4.1239064308599246e-10, 7.278539618280055e-11, 1.0705290372746862e-11, 1.349602467078115e-12, 1.4887484703896747e-13, 1.4597694504061606e-14, 1.288219065644581e-15, 9.747947866416476e-17, 9.325881939887078e-18, 6.330704068777846e-19], [1.5810607600534005e-09, 1.3952563635830384e-09, 6.15643740362392e-10, 1.810980046104572e-10, 3.9953895155236883e-11, 7.0517121003484996e-12, 1.0371672013661725e-12, 1.3075436209556327e-13, 1.442353295248389e-14, 1.4142773738972492e-15, 1.2480731643324005e-16, 1.0012737068390069e-17, 6.945247493248953e-19, 6.133414781916836e-20], [1.4139588701667858e-10, 1.247792090784834e-10, 5.505765177036338e-11, 1.619578048220062e-11, 3.5731178636394025e-12, 6.306418529932682e-13, 9.275492765807615e-14, 1.1693496845230478e-14, 1.2899113603084241e-15, 1.2648027755939387e-16, 1.11616464459299e-17, 8.95449355913415e-19, 6.585143361085045e-20, 4.216363474046826e-21]] |
| Legacy trial inputs | {"lambda_home": 1.162603346853499, "lambda_away": 0.8824811789876521, "rho": -0.09481858246728825, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T16:15:13Z", "over": 1.93, "under": 1.91, "bookmaker": "pinnacle", "event_id": "7d597f0fe7ec1c85b6e7f9f2ce731746", "kickoff_utc": "2026-10-31T13:00:00Z", "home_team": "Kocaelispor", "away_team": "\u00c7aykur Rizespor"}} |
| Legacy p home | 0.3933 |
| Legacy p draw | 0.2947 |
| Legacy p away | 0.3120 |
| Legacy p over 1 5 | 0.6195 |
| Legacy p under 3 5 | 0.8484 |
| Legacy p btts yes | 0.4094 |
| Legacy p over 2 5 | 0.3446 |
| Legacy goal margin distribution | {"-1": 0.20150875347417316, "-10": 1.3201143841115684e-08, "-11": 1.0508746232868227e-09, "-12": 7.657519295235425e-11, "-13": 4.817929862334313e-12, "-2": 0.0824228899163564, "-3": 0.022419389699616665, "-4": 0.004712252020375449, "-5": 0.0008048156538787709, "-6": 0.0001155987118028722, "-7": 1.4314767224876709e-05, "-8": 1.5571234244190293e-06, "-9": 1.5097603846026425e-07, "0": 0.29469726845593713, "1": 0.22018508012370155, "10": 1.6943749235540493e-07, "11": 1.7769490432649182e-08, "12": 1.705839969131884e-09, "13": 1.4139588701667858e-10, "2": 0.11658343667037313, "3": 0.041777160516399646, "4": 0.011568305766215863, "5": 0.0026029377489655827, "6": 0.0004925456392143855, "7": 8.035333217217115e-05, "8": 1.1515127633209085e-05, "9": 1.4708888660676962e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4097 |
| Legacy raw p draw | 0.3255 |
| Legacy raw p away | 0.2649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1626 |
| Legacy lambda away | 0.8825 |
| Legacy model home team | Kocaelispor |
| Legacy model away team | Rizespor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,459.3997 |
| Elo away rating | 1,449.0338 |
| Elo rating diff | 70.3660 |
| Elo home expectancy | 0.5999 |

</details>


---
