# Eredivisie — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Eredivisie |
| Training matches | 1,629 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 615de97a97f0d322c268f8b3f3257e878336d0e9922ced304f9c92ec61ef9060 |
| Training as of utc | 2026-11-05T16:27:01.877094+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6639999435984515, 'audit_candidate_poisson_score': 0.6541517901162848, 'audit_gain': 0.009848153482166722, 'audit_gain_lower95': -0.0021828454332282108, 'audit_baseline_briers': [0.6216633755590796, 0.09847259899912482, 0.27967453202176307, 0.2302451960138092], 'audit_candidate_briers': [0.6176749252028129, 0.0975895815214795, 0.2767941288032132, 0.2243749218030424], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1636.348 |
| Base scoring parameter | 0.290 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.081 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 25, 'matches': 1629, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
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

## 2026-11-06 — Willem II Tilburg vs PEC Zwolle

The model's most likely 1X2 outcome is **PEC Zwolle win** at **46.4%**. Expected goals are 1.22 for Willem II Tilburg and 1.64 for PEC Zwolle (2.86 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.5%; Under 3.5 goals: 67.8%; Double Chance 1X: 53.6%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 83.8%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Willem II Tilburg win | 27.4% | 3.65 |
| Draw | 26.2% | 3.82 |
| PEC Zwolle win | 46.4% | 2.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Willem II Tilburg expected goals | 1.22 |
| PEC Zwolle expected goals | 1.64 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 54.5% |
| Under 2.5 | 45.5% |
| Over 3.5 | 32.2% |
| Under 3.5 | 67.8% |
| Over 4.5 | 16.2% |
| Under 4.5 | 83.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.37% |
| 2 | 1-2 | 9.41% |
| 3 | 0-1 | 8.47% |
| 4 | 0-2 | 7.72% |
| 5 | 2-1 | 6.97% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:00:00+00:00 |
| Fixture id | fdorg:558845 |
| Matched home-team name | Willem II |
| Matched away-team name | Zwolle |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.2184 |
| Dc lambda away | 1.6440 |
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
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.06 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.73 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.11 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.17 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06638917565794031,0.08466587731700176,0.07720339988990607,0.04230668484155689,0.017387727595240595,0.005716979660468529,0.0015664236101385453,0.00036787900586729183,7.559774496612378e-05,1.3808934043384259e-05,2.270146993802349e-06,3.39277545528833e-07,4.64801686615294e-08,5.877845504661601e-09,6.902143031108879e-10,7.564609599185533e-11],[0.06035355636955617,0.1236953410033686,0.09406637079221243,0.051547422898087676,0.021185601068609568,0.006965697486380788,0.0019085660001902757,0.00044823211182319433,9.211000447103708e-05,1.682511795882736e-05,2.765998507531505e-06,4.1338344483141865e-07,5.6632490098038304e-08,7.161700073951365e-09,8.40972737665741e-10,9.216891645575709e-11],[0.0424076985024389,0.06971697378445449,0.057306298211193735,0.03140327370704604,0.012906508058049104,0.004243581782114924,0.0011627200182331681,0.0002730680779076007,5.61144576961678e-05,1.0250052373306774e-05,1.6850776105145529e-06,2.5183787538065664e-07,3.450115422406984e-08,4.362988777823267e-09,5.123301142191697e-10,5.6150347544326565e-11],[0.01722350007669515,0.028314913228654665,0.02327443050414176,0.012754153283528939,0.005241860567247973,0.0017234920481599611,0.00047222813381542607,0.00011090411002884474,2.279037534607236e-05,4.162965312244556e-06,6.843789071049341e-07,1.022816568478487e-07,1.4012329209286456e-08,1.771988110723279e-09,2.0807820450429825e-10,2.2804951680661215e-11],[0.0052463756352196965,0.008624882875994253,0.007089523301118317,0.003884987298551621,0.0015967004058855332,0.000524985435521089,0.00014384336310752343,3.3782019804925735e-05,6.94207735946364e-06,1.2680628029825721e-06,2.0846568975558414e-07,3.115557174946869e-08,4.268234808774339e-09,5.397576107411851e-10,6.338179913899818e-11,6.946517393504181e-12],[0.0012784605769216356,0.002101750523447489,0.0017276071482189158,0.000946711300978269,0.00038909118675676884,0.00012793082871650718,3.5052402224167434e-05,8.232155593177402e-06,1.69167685333741e-06,3.0900728720048607e-07,5.0799863472248355e-08,7.59213083519156e-09,1.0401027900919911e-09,1.3153057928097106e-10,1.5445163886017018e-11,1.6927588209424199e-12],[0.000259617553206703,0.00042680340575084505,0.00035082594553128486,0.00019224908142644924,7.901291889916167e-05,2.59789698099711e-05,7.118106779145015e-06,1.6717074670098287e-06,3.43529564703029e-07,6.275024609612857e-08,1.0315950680040475e-08,1.5417373571296381e-09,2.1121413231008018e-10,2.670997274472788e-11,3.1364562422561556e-12,3.437492803417685e-13],[4.51891294553164e-05,7.42895621510191e-05,6.106489670316983e-05,3.346294778969967e-05,1.375301853312608e-05,4.521909306046993e-06,1.2389803568614963e-06,2.909780336693189e-07,5.97948858979265e-08,1.0922331557193431e-08,1.7955982751437948e-09,2.6835538721050475e-10,3.676401171593089e-11,4.649147953214427e-12,5.459327592129438e-13,5.983312968506541e-14],[6.882432336501359e-06,1.1314510612962225e-05,9.300356629144285e-06,5.0965016745944555e-06,2.0946236543566244e-06,6.886995878386597e-07,1.8870021563007449e-07,4.431677822246022e-08,9.106930388385308e-09,1.6635020148717085e-09,2.734747002470041e-10,4.0871285127061297e-11,5.599263055143223e-12,7.08078393986801e-13,8.314710464333877e-14,9.112755025426287e-15],[9.317457133305103e-07,1.531761773544613e-06,1.2590850150014358e-06,6.899658952112697e-07,2.835707662008902e-07,9.323635269727344e-08,2.5546290674793928e-08,5.999618466047533e-09,1.2328989136551162e-09,2.252053918863943e-10,3.702308532814763e-11,5.533166597727421e-12,7.580298787349458e-13,9.58598611714842e-14,1.1256479474036739e-14,1.2336874547303192e-15],[1.1352600776544475e-07,1.8663332335241227e-07,1.5340976958131133e-07,8.406700718553414e-08,3.4550904334942674e-08,1.1360128357872864e-08,3.112617908547557e-09,7.310071007803098e-10,1.502191956916148e-10,2.7439534952865175e-11,4.510976559731258e-12,6.741735488063161e-13,9.236007707735666e-14,1.1679782571629695e-14,1.3715149508047852e-15,1.503152733219662e-16],[1.2574787163462673e-08,2.0672569792246655e-08,1.6992539764690132e-08,9.311740486915532e-09,3.8270549354181444e-09,1.2583125141246207e-09,3.4477128625923114e-10,8.097050964995054e-11,1.663913362999077e-11,3.0393591626120773e-12,4.996614542738775e-13,7.46753017598507e-14,1.0230328138098057e-14,1.2937192353069684e-15,1.519168068827897e-16,1.6649775735501383e-17],[1.2767837876292031e-09,2.0989939325625616e-09,1.7253412721958643e-09,9.454696237602452e-10,3.8858086680830036e-10,1.2776303860421417e-10,3.500642857915677e-11,8.221358552892034e-12,1.6894581023761856e-12,3.086020028140805e-13,5.0733235944841596e-14,7.582173231554027e-15,1.038738623489643e-15,1.3135806784733983e-16,1.5424906487477363e-17,1.690538650905999e-18],[1.1966632932256575e-10,1.9672782628803626e-10,1.6170729834828184e-10,8.86139693013032e-11,3.641967138561006e-11,1.197456766055343e-11,3.280971180358397e-12,7.705453418202288e-13,1.5834415475389723e-13,2.8923666838631516e-14,4.7549633532298344e-15,7.106378133079719e-16,9.735558941376485e-17,1.2311511125453585e-17,1.4456965677232634e-18,1.5844542896921115e-19],[1.0414583259889353e-11,1.7121259906711693e-11,1.4073416740646795e-11,7.712090497821197e-12,3.1696108846193314e-12,1.0421488868924075e-12,2.8554354198525973e-13,6.706070674462812e-14,1.378072171793687e-14,2.5172321920250072e-15,4.138253593995425e-16,6.184694321467716e-17,8.472875348521782e-18,1.071473140330643e-18,1.2581924554989242e-19,1.3789535632038167e-20],[8.459576063300681e-13,1.3907287201610669e-12,1.1431579777806258e-12,6.264390474907007e-13,2.5746171210491496e-13,8.465185363589983e-14,2.3194181202736478e-14,5.447218918012757e-15,1.1193828948399529e-15,2.0447018057303324e-16,3.361427929858774e-17,5.0237144142122674e-18,6.882362135577837e-19,8.703380926743889e-20,1.0220067874014277e-20,1.1200988330094856e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21593915342481598, "-10": 2.719868655526521e-06, "-11": 4.004880491265924e-07, "-12": 5.41770038013806e-08, "-13": 6.774968589871668e-09, "-14": 7.82383219566645e-10, "-15": 7.564609599185533e-11, "-2": 0.14353325314390133, "-3": 0.06824363411024058, "-4": 0.02563431088453264, "-5": 0.007922724555799787, "-6": 0.002075149418738404, "-7": 0.0004709556645582984, "-8": 9.421462515399097e-05, "-9": 1.6841338302029616e-05, "0": 0.26187701781216893, "1": 0.15764630267125165, "10": 1.3601578706192683e-07, "11": 1.4843457946583442e-08, "12": 1.4882114697053768e-09, "13": 1.3793074720705807e-10, "14": 1.180531198005042e-11, "15": 8.459576063300681e-13, "2": 0.07884257601453948, "3": 0.027782707194706064, "4": 0.007734606107302444, "5": 0.0017717206650983437, "6": 0.0003439332828898858, "7": 5.7850750257590886e-05, "8": 8.577316466539427e-06, "9": 1.1363545310858268e-06} |
| Raw goal margin distribution | {"-1": 0.21593915342481598, "-10": 2.719868655526521e-06, "-11": 4.004880491265924e-07, "-12": 5.41770038013806e-08, "-13": 6.774968589871668e-09, "-14": 7.82383219566645e-10, "-15": 7.564609599185533e-11, "-2": 0.14353325314390133, "-3": 0.06824363411024058, "-4": 0.02563431088453264, "-5": 0.007922724555799787, "-6": 0.002075149418738404, "-7": 0.0004709556645582984, "-8": 9.421462515399097e-05, "-9": 1.6841338302029616e-05, "0": 0.26187701781216893, "1": 0.15764630267125165, "10": 1.3601578706192683e-07, "11": 1.4843457946583442e-08, "12": 1.4882114697053768e-09, "13": 1.3793074720705807e-10, "14": 1.180531198005042e-11, "15": 8.459576063300681e-13, "2": 0.07884257601453948, "3": 0.027782707194706064, "4": 0.007734606107302444, "5": 0.0017717206650983437, "6": 0.0003439332828898858, "7": 5.7850750257590886e-05, "8": 8.577316466539427e-06, "9": 1.1363545310858268e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 27.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 46.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 67.8% |
| Raw p btts yes | 57.7% |
| P home draw | 53.6% |
| P draw away | 72.6% |
| P home away | 73.8% |
| Raw p home draw | 53.6% |
| Raw p draw away | 72.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5453 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-01 |
| Elo home rating | 1,319.6939 |
| Elo away rating | 1,410.7310 |
| Elo rating diff | -31.0371 |
| Elo home expectancy | 0.4555 |
| Research p home | 0.2834 |
| Research p draw | 0.2434 |
| Research p away | 0.4732 |
| Research p over 1 5 | 0.7793 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.2184226462351837, 1.6439697565866496], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:27:41.652669+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:27:41.714859+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:27:41.941199+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Willem+II+Tilburg%22+%22PEC+Zwolle%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:27:13.451062+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:27:13.702984+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:27:42.017675+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Willem+II+Tilburg_vs_PEC+Zwolle&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.2184226462351837, 1.6439697565866496], "h2h": [], "margin_distribution": {"-1": 0.22519641499840107, "-10": 2.719868655526521e-06, "-11": 4.004880491265924e-07, "-12": 5.41770038013806e-08, "-13": 6.774968589871668e-09, "-14": 7.82383219566645e-10, "-15": 7.564609599185533e-11, "-2": 0.14353325314390133, "-3": 0.06824363411024058, "-4": 0.02563431088453264, "-5": 0.007922724555799787, "-6": 0.002075149418738404, "-7": 0.0004709556645582984, "-8": 9.421462515399097e-05, "-9": 1.6841338302029616e-05, "0": 0.24336249466499874, "1": 0.16690356424483674, "10": 1.3601578706192683e-07, "11": 1.4843457946583442e-08, "12": 1.4882114697053768e-09, "13": 1.3793074720705807e-10, "14": 1.180531198005042e-11, "15": 8.459576063300681e-13, "2": 0.07884257601453948, "3": 0.027782707194706064, "4": 0.007734606107302444, "5": 0.0017717206650983437, "6": 0.0003439332828898858, "7": 5.7850750257590886e-05, "8": 8.577316466539427e-06, "9": 1.1363545310858268e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:27:42.018095+00:00", "p_over_1_5": 0.7793341290819167, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
