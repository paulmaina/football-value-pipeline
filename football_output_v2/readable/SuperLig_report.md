# Super Lig — football model report

Fixtures in this report: **9**.

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
| Training as of utc | 2026-11-06T12:16:40.043755+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-06', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-07', 'audit_start_date': '2026-05-08', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325688020301171, 'audit_candidate_poisson_score': 0.824985919365649, 'audit_gain': 0.007582882664468049, 'audit_gain_lower95': -0.0033653303999722837, 'audit_baseline_briers': [0.5922589538722137, 0.1664907523353062, 0.2201651393758508, 0.2497293837734222], 'audit_candidate_briers': [0.5911030741495769, 0.16507679461400995, 0.21631943856751462, 0.24937701251274844], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1669.788 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 34.00 |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 9} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'None': 9} |
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

The model's most likely 1X2 outcome is **Kasimpasa SK win** at **36.7%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 53.2%; Under 3.5 goals: 69.1%; Double Chance 1X: 63.3%; Double Chance X2: 64.3%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 84.7%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 35.7% | 2.80 |
| Draw | 27.5% | 3.63 |
| Kasimpasa SK win | 36.7% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 78.1% |
| Under 1.5 | 21.9% |
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.3% |
| Under 4.5 | 84.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.04% |
| 2 | 1-2 | 8.41% |
| 3 | 2-1 | 8.28% |
| 4 | 0-1 | 7.40% |
| 5 | 1-0 | 7.26% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3920 |
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
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.91 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.52 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07190766378964188,0.07398760766141022,0.06043574930543924,0.028491001913392888,0.010073555793026719,0.0028493635042724317,0.0006716324525231898,0.000135696516263851,2.3989090163598206e-05,3.7696960359085498e-06,5.331401606150699e-07,6.85462623639405e-08,8.078627776652688e-09,8.788794536884347e-10,8.878433407539896e-11],[0.07264056284358875,0.13044390095302535,0.08412583642890377,0.039659132123078665,0.014022268551989825,0.003966279740745053,0.0009349042990391809,0.0001888879191931753,3.3392525092750966e-05,5.247371559849061e-06,7.421246937621116e-07,9.541557309561796e-08,1.1245352737729957e-08,1.2233896329810746e-09,1.2358672560057e-10],[0.05854566567052167,0.0827999003144437,0.05855107644231458,0.027602517551628358,0.00975941461902822,0.002760506856751778,0.0006506877720681335,0.0001314648562817679,2.324099672946393e-05,3.6521390617209884e-06,5.165143256663715e-07,6.640866529547304e-08,7.826697905393988e-09,8.514718302973017e-10,8.601561809147322e-11],[0.027164954244370945,0.03841882191823573,0.027167464820798733,0.01280745752451104,0.0045283292715421995,0.0012808641185660314,0.00030191651855284167,6.099916645811035e-05,1.0783729342193624e-05,1.6945778883795975e-06,2.396605771339601e-07,3.08133545587064e-08,3.631556461943072e-09,3.950795169119286e-10,3.991090207951402e-11],[0.00945332242763692,0.013369634552515587,0.009454196100687779,0.0044569567232956376,0.0015758449757472038,0.00044573686338178676,0.00010506604098923006,2.1227526582898747e-05,3.7527053985467144e-06,5.897080117819806e-07,8.34011604974576e-08,1.0722954771068966e-08,1.263770733426877e-09,1.3748648439919289e-10,1.3888873963911504e-11],[0.0026317822328563284,0.0037220741114495286,0.002632025461332896,0.001240806034784867,0.00043871145204809356,0.0001240920709683796,2.9250133174726675e-05,5.909692358004487e-06,1.044744159383135e-06,1.6417329249699584e-07,2.3218682540131614e-08,2.985244824371835e-09,3.5183073338460863e-10,3.8275906663444215e-11,3.866629115044403e-12],[0.0006105682044767289,0.0008635137355914801,0.0006106246329959131,0.00028786451375205547,0.00010178017778836716,2.8789111809882226e-05,6.785972285334224e-06,1.3710367852588298e-06,2.423785515262018e-07,3.8087874890063415e-08,5.386687823884724e-09,6.925708174425774e-10,8.162402514938562e-11,8.879933648937963e-12,8.970502067672346e-13],[0.00012141479998843743,0.00017171439116119906,0.00012142602110562,5.724342031686441e-05,2.023954054330911e-05,5.724871073555609e-06,1.3494274050137458e-06,2.7263810306279324e-07,4.8198289952326854e-08,7.573980560820264e-09,1.0711720982877388e-09,1.377214644671594e-10,1.6231380237458076e-11,1.7658229825780106e-12,1.7838330040060478e-13],[2.112599273042367e-05,2.9878046002020218e-05,2.1127945187949843e-05,9.960269107174993e-06,3.521649637653586e-06,9.961189632076672e-07,2.347983404928373e-07,4.7438620200252204e-08,8.386430017169883e-09,1.3178612350676932e-09,1.8638233529696954e-10,2.3963327843340263e-11,2.8242357680771797e-12,3.0725054521121555e-13,3.103842618734324e-14],[3.267458654232655e-06,4.621097868706146e-06,3.2677606317218236e-06,1.540508316366936e-06,5.446771061866091e-07,1.540650689655368e-07,3.631516300476363e-08,7.337109886199493e-09,1.2970899728776302e-09,2.0382744387668423e-10,2.8826885544893522e-11,3.706296028076227e-12,4.3681135934065657e-13,4.752100721507514e-14,4.80056845392857e-15],[4.548263162833707e-07,6.432512674906814e-07,4.5486835118680274e-07,2.144369055227167e-07,7.58183983291812e-08,2.1445672371329447e-08,5.055027029428696e-09,1.0213168749307768e-09,1.8055336476494038e-10,2.8372535130872004e-11,4.012667809988055e-12,5.159119511189288e-13,6.080361605258013e-14,6.6148670709909835e-15,6.682333571805373e-16],[5.7555705818238934e-08,8.139982097218107e-08,5.75610250982573e-08,2.7135781305911708e-08,9.594390811646971e-09,2.71382891861858e-09,6.39685168146199e-10,1.292418918963685e-10,2.2848010273067926e-11,3.5903843441915276e-12,5.077804861979435e-13,6.528574847945839e-14,7.69435477437743e-15,8.370741303533338e-16,8.45611635626093e-17],[6.67640421006509e-09,9.442297678590834e-09,6.677021241217853e-09,3.147723444245964e-09,1.1129397215660734e-09,3.1480143558451226e-10,7.42028386067346e-11,1.4991929973001136e-11,2.650346300338161e-12,4.164809867333073e-13,5.890202765555415e-14,7.573081414065147e-15,8.925374448819456e-16,9.709976045948474e-17,9.809010251742958e-18],[7.148826455101393e-10,1.0110434497044109e-09,7.149487147367725e-10,3.370456300061113e-10,1.1916913167825042e-10,3.370767796559936e-11,7.945343016765482e-12,1.605275867546269e-12,2.8378847581567907e-13,4.4595117406421564e-14,6.306993410140368e-15,8.108952522360503e-16,9.556933788582652e-17,1.0397053780990369e-17,1.0503095645453316e-18],[7.107914626360681e-11,1.005257376042739e-10,7.108571537568818e-11,3.35116760536525e-11,1.1848714182480798e-11,3.351477319209047e-12,7.899872824583634e-13,1.5960890769888085e-13,2.8216439029701695e-14,4.433990519537376e-15,6.270899285337502e-16,8.062546013691567e-17,9.50224066644569e-18,1.0337552758498445e-18,1.0442987758796272e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.19072069849232806, "-10": 6.367914000069577e-07, "-11": 8.068299783404727e-08, "-12": 9.388033027725236e-09, "-13": 1.0024661792890049e-09, "-14": 8.878433407539896e-11, "-2": 0.11124638604214176, "-3": 0.045598005294883434, "-4": 0.014755444878270772, "-5": 0.003927130024744146, "-6": 0.0008855424161604171, "-7": 0.00017299192483927832, "-8": 2.9785092347362644e-05, "-9": 4.582002304541592e-06, "0": 0.27541710296093314, "1": 0.18753378345798793, "10": 5.432520528409583e-07, "11": 6.77464638876202e-08, "12": 7.75853337514519e-09, "13": 8.154083831144132e-10, "14": 7.107914626360681e-11, "2": 0.1077672370927458, "3": 0.043475751791228756, "4": 0.013846945494070336, "5": 0.0036272490364044822, "6": 0.0008050296572058234, "7": 0.00015478496082490132, "8": 2.6230242169009344e-05, "9": 3.971541190874838e-06} |
| Raw goal margin distribution | {"-1": 0.19072069849232806, "-10": 6.367914000069577e-07, "-11": 8.068299783404727e-08, "-12": 9.388033027725236e-09, "-13": 1.0024661792890049e-09, "-14": 8.878433407539896e-11, "-2": 0.11124638604214176, "-3": 0.045598005294883434, "-4": 0.014755444878270772, "-5": 0.003927130024744146, "-6": 0.0008855424161604171, "-7": 0.00017299192483927832, "-8": 2.9785092347362644e-05, "-9": 4.582002304541592e-06, "0": 0.27541710296093314, "1": 0.18753378345798793, "10": 5.432520528409583e-07, "11": 6.77464638876202e-08, "12": 7.75853337514519e-09, "13": 8.154083831144132e-10, "14": 7.107914626360681e-11, "2": 0.1077672370927458, "3": 0.043475751791228756, "4": 0.013846945494070336, "5": 0.0036272490364044822, "6": 0.0008050296572058234, "7": 0.00015478496082490132, "8": 2.6230242169009344e-05, "9": 3.971541190874838e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 63.3% |
| P draw away | 64.3% |
| P home away | 72.5% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5320 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |
| Research p home | 0.3687 |
| Research p draw | 0.2525 |
| Research p away | 0.3788 |
| Research p over 1 5 | 0.7700 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.3919879772439983, 1.4142789114469714], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:18.987603+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:18.990306+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Gazi%C5%9Fehir+Gaziantep%22+%22Kasimpasa+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.073155+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Gazi%C5%9Fehir+Gaziantep_vs_Kasimpasa+SK&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.3919879772439983, 1.4142789114469714], "h2h": [], "margin_distribution": {"-1": 0.20219819791309374, "-10": 6.367914000069577e-07, "-11": 8.068299783404728e-08, "-12": 9.388033027725236e-09, "-13": 1.0024661792890049e-09, "-14": 8.878433407539897e-11, "-2": 0.11124638604214176, "-3": 0.04559800529488344, "-4": 0.014755444878270773, "-5": 0.003927130024744146, "-6": 0.0008855424161604172, "-7": 0.00017299192483927835, "-8": 2.978509234736265e-05, "-9": 4.582002304541593e-06, "0": 0.25246210411940184, "1": 0.19901128287875358, "10": 5.432520528409583e-07, "11": 6.77464638876202e-08, "12": 7.75853337514519e-09, "13": 8.154083831144133e-10, "14": 7.107914626360682e-11, "2": 0.1077672370927458, "3": 0.04347575179122876, "4": 0.013846945494070336, "5": 0.0036272490364044827, "6": 0.0008050296572058235, "7": 0.00015478496082490135, "8": 2.6230242169009348e-05, "9": 3.971541190874838e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.073579+00:00", "p_over_1_5": 0.7699866662845936, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Draw** at **37.0%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 0-0 at 20.1%. Goal-market probabilities: at least one goal: 79.9%; Over 2.5 goals: 23.4%; Under 3.5 goals: 91.2%; Double Chance 1X: 66.5%; Double Chance X2: 70.5%; Double Chance 12 (either team wins): 63.0%; Under 4.5 goals: 97.2%; BTTS Yes (both teams score): 33.2%; BTTS No (at least one team does not score): 66.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 29.5% | 3.39 |
| Draw | 37.0% | 2.71 |
| Kocaelispor win | 33.5% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 79.9% |
| Under 0.5 | 20.1% |
| Over 1.5 | 50.9% |
| Under 1.5 | 49.1% |
| Over 2.5 | 23.4% |
| Under 2.5 | 76.6% |
| Over 3.5 | 8.8% |
| Under 3.5 | 91.2% |
| Over 4.5 | 2.8% |
| Under 4.5 | 97.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-0 | 20.14% |
| 2 | 0-1 | 15.14% |
| 3 | 1-1 | 14.36% |
| 4 | 1-0 | 13.81% |
| 5 | 0-2 | 7.13% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7984 |
| Dc lambda away | 0.8689 |
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
| P btts yes | 33.2% |
| P btts no | 66.8% |
| Fair Over 0.5 odds | 1.25 |
| Fair Under 0.5 odds | 4.97 |
| Fair Over 1.5 odds | 1.96 |
| Fair Under 1.5 odds | 2.04 |
| Fair Over 2.5 odds | 4.27 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 11.32 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 36.26 |
| Fair Under 4.5 odds | 1.03 |
| Score matrix json | [[0.20140152243866283,0.15138234511777113,0.07125408328143597,0.020636861319790055,0.004482690944006601,0.0007789757478365702,0.0001128048649232379,1.4001834279389752e-05,1.5207229130214525e-06,1.4681239500757677e-07,1.2756098582438504e-08,1.0075818253783362e-09,7.295485900978182e-11],[0.13807278086221764,0.14357692442395753,0.056886647611352814,0.01647571344180229,0.0035788160950032634,0.0006219056764781097,9.005926824415901e-05,1.117855112131832e-05,1.2140894175267524e-06,1.1720963340146762e-07,1.0184001414890316e-08,8.044163871073792e-10,5.824448459512551e-11],[0.06015900413539392,0.05227039497126969,0.02270810687211059,0.006576802770779731,0.0014285977777453878,0.00024825334518427085,3.595000890339519e-05,4.462272680796693e-06,4.846422386119646e-07,4.678793694972905e-08,4.065266670221266e-09,3.2110827505444297e-10,2.325013050396653e-11],[0.016009581071459705,0.013910255629338505,0.006043106650007467,0.0017502260661235174,0.00038018002907508065,6.606545625395982e-05,9.567056342277245e-06,1.1875049674258824e-06,1.2897353141434543e-07,1.2451257804687185e-08,1.0818532864595637e-09,8.54536911985906e-11,6.187350581594415e-12],[0.0031953656368728686,0.002776359521195952,0.0012061486957841527,0.000349329080098181,7.588044904544639e-05,1.3186059507488613e-05,1.9094967535807013e-06,2.3701510674086165e-07,2.574193468948574e-08,2.4851569286762702e-09,2.159279996310159e-10,1.705577348845803e-11,1.2349384623784857e-12],[0.0005102125537318391,0.00044330872969309935,0.0001925889792251164,5.577830592936876e-05,1.2116033682982307e-05,2.105453290647449e-06,3.048944395422963e-07,3.784483424614443e-08,4.1102833692528945e-09,3.968116350669578e-10,3.447779961161654e-11,2.7233408430636484e-12,1.9718591804361523e-13],[6.78891660528721e-05,5.898690603101191e-05,2.56259966457802e-05,7.421892396981429e-06,1.6121661777818527e-06,2.801527853829654e-07,4.056942363194665e-08,5.03565468467537e-09,5.4691659023002e-10,5.279997676993903e-11,4.587635184297932e-12,3.6236924662282994e-13,2.6237667880643598e-14],[7.742888724053811e-06,6.727569008855453e-06,2.922693737565187e-06,8.464809673309732e-07,1.838706239155511e-07,3.1951958892301955e-08,4.627020054076401e-09,5.743260102184179e-10,6.237687904712198e-11,6.0219379399044574e-12,5.232285326779358e-13,4.132890292737783e-14,2.9924560071968897e-15],[7.727048087185235e-07,6.713805543890949e-07,2.916714401967736e-07,8.447492108641656e-08,1.83494455809816e-08,3.188659060456197e-09,4.617553955947863e-10,5.7315103662700025e-11,6.224926653386048e-12,6.009618076407673e-13,5.2215809585767234e-14,4.1244351002795026e-15,2.986333949829858e-16],[6.854435428953423e-08,5.955617988125356e-08,2.5873309325125565e-08,7.493519975798456e-09,1.6277249536019091e-09,2.828564982155563e-10,4.096095310089186e-11,5.084253038508769e-12,5.52194800836923e-13,5.330954148677111e-14,4.631909768618328e-15,3.6586641828539674e-16,2.649088370803287e-17],[5.472329933451467e-09,4.754747043199823e-09,2.065630153860127e-09,5.982551604069836e-10,1.299515923572085e-10,2.2582225744193656e-11,3.270172315138975e-12,4.0590812154052576e-13,4.4085208315654837e-14,4.256038336642018e-15,3.6979469335706516e-16,2.920943341257139e-17,2.1149350282986694e-18],[3.9717341634206714e-10,3.450923372595229e-10,1.4992030727035704e-10,4.3420453224253744e-11,9.431689704982939e-12,1.6389837338941798e-12,2.373441525320839e-13,2.9460196536717355e-14,3.1996376332954208e-15,3.0889681484916825e-16,2.683913862868248e-17,2.1199764266717144e-18,1.534987803633932e-19],[2.6424057793769037e-11,2.2959089125136505e-11,9.974239716888973e-12,2.888774822837516e-12,6.274929378524187e-13,1.0904204341351858e-13,1.5790572443850278e-14,1.9599950648045483e-15,2.128727811644367e-16,2.0550990957702407e-17,1.7856153535927605e-18,1.410426209682556e-19,1.0212316526496989e-20]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21523947158156298, "-10": 1.358376510004985e-08, "-11": 1.0658263099734617e-09, "-12": 7.295485900978182e-11, "-2": 0.08922640785181654, "-3": 0.024473738995037336, "-4": 0.005141760277731119, "-5": 0.0008736287822930303, "-6": 0.000124480728218551, "-7": 1.52638107401121e-05, "-8": 1.6420845017228023e-06, "-9": 1.5732369204810314e-07, "0": 0.3695148068532188, "1": 0.19674801243495296, "10": 5.827396510427879e-09, "11": 4.201325054672037e-10, "12": 2.6424057793769037e-11, "2": 0.07533283135146668, "3": 0.01898613856493081, "4": 0.0036651654797810033, "5": 0.0005722082789679861, "6": 7.49160316282668e-05, "7": 8.440750383660186e-06, "8": 8.343706666997994e-07, "9": 7.345191041482725e-08} |
| Raw goal margin distribution | {"-1": 0.21523947158156298, "-10": 1.358376510004985e-08, "-11": 1.0658263099734617e-09, "-12": 7.295485900978182e-11, "-2": 0.08922640785181654, "-3": 0.024473738995037336, "-4": 0.005141760277731119, "-5": 0.0008736287822930303, "-6": 0.000124480728218551, "-7": 1.52638107401121e-05, "-8": 1.6420845017228023e-06, "-9": 1.5732369204810314e-07, "0": 0.3695148068532188, "1": 0.19674801243495296, "10": 5.827396510427879e-09, "11": 4.201325054672037e-10, "12": 2.6424057793769037e-11, "2": 0.07533283135146668, "3": 0.01898613856493081, "4": 0.0036651654797810033, "5": 0.0005722082789679861, "6": 7.49160316282668e-05, "7": 8.440750383660186e-06, "8": 8.343706666997994e-07, "9": 7.345191041482725e-08} |
| Research history json | {"away": [{"away": "Rizespor", "away_goals": 0.0, "away_xg": 1.17, "date": "2026-10-31T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 0.0, "home_xg": 0.62, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.83, "date": "2026-10-18T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.61, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 1.0, "away_xg": 1.65, "date": "2026-10-11T00:00:00+00:00", "home": "Besiktas", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-09-19T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-29T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 0.0, "away_xg": 0.59, "date": "2026-08-24T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 2.0, "home_xg": 1.3, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.44, "date": "2026-08-16T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.96, "source": "pipeline training history"}], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Eyupspor", "away_goals": 1.0, "away_xg": 0.98, "date": "2026-11-01T00:00:00+00:00", "home": "Amedspor", "home_goals": 5.0, "home_xg": 4.95, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.59, "date": "2026-10-24T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.43, "date": "2026-10-17T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 4.0, "away_xg": 3.21, "date": "2026-10-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Rizespor", "away_goals": 2.0, "away_xg": 2.05, "date": "2026-09-12T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 1.43, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-06T00:00:00+00:00", "home": "Corum", "home_goals": 3.0, "home_xg": 2.58, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Gaziantep", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-08-23T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.09, "date": "2026-08-16T00:00:00+00:00", "home": "Besiktas", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 66.5% |
| P draw away | 70.5% |
| P home away | 63.0% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.2342 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |
| Research p home | 0.3260 |
| Research p draw | 0.3098 |
| Research p away | 0.3642 |
| Research p over 1 5 | 0.5894 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7983633357075784, 0.8688706823276178], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.080934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.082356+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Ey%C3%BCpspor%22+%22Kocaelispor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.165185+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Ey%C3%BCpspor_vs_Kocaelispor&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 0.890448735118826, "goals_for": 1.0632630221502812, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.513167850691485, "results": "DWLLWLWWWL", "xg_against": 1.2372826932614873, "xg_for": 1.1882938425185394, "xg_matches": 10}, "venue": {"goals_against": 1.3740829150788851, "goals_for": 1.0848014184490722, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 1.2891252875508328, "results": "WLLWL", "xg_against": 1.5093258702129508, "xg_for": 1.1284305210338508, "xg_matches": 5}}, "home": {"all": {"goals_against": 3.0933035323073734, "goals_for": 0.3034050194301704, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.19620865573750387, "results": "LLLLLLLWLL", "xg_against": 2.5307266426055373, "xg_for": 0.8256655613941696, "xg_matches": 10}, "venue": {"goals_against": 1.8723623359830541, "goals_for": 0.3416191115517185, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.5124286673275777, "results": "LLLWL", "xg_against": 1.563686916043823, "xg_for": 1.0291416727227958, "xg_matches": 5}}}, "goal_rates": [0.9553201476276768, 1.0279333610646908], "h2h": [{"away": "Kocaelispor", "away_goals": 1.0, "away_xg": null, "date": "2026-03-09T00:00:00+00:00", "home": "Eyupspor", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": null, "date": "2025-10-04T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.2232704713885614, "-10": 5.4600652123997135e-08, "-11": 5.064567424257179e-09, "-12": 4.300833490023067e-10, "-13": 3.161899943832405e-11, "-2": 0.09962902849243076, "-3": 0.031663845016978984, "-4": 0.007767518653641219, "-5": 0.001547384949056795, "-6": 0.000259145389219358, "-7": 3.7407644250885167e-05, "-8": 4.742578909326027e-06, "-9": 5.358770844239826e-07, "0": 0.30979448829846046, "1": 0.2074986451134338, "10": 2.624445687520027e-08, "11": 2.2623828138778026e-09, "12": 1.7855019983995532e-10, "13": 1.2199437618377107e-11, "2": 0.08605058900946139, "3": 0.025416490263848457, "4": 0.005794529908293316, "5": 0.0010727987237632267, "6": 0.00016697341978454027, "7": 2.2400008915769526e-05, "8": 2.6392855101657563e-06, "9": 2.7715388433052176e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.165605+00:00", "p_over_1_5": 0.5894423913944926, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **52.5%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 72.2%; Under 3.5 goals: 48.5%; Double Chance 1X: 74.4%; Double Chance X2: 47.5%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 67.9%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 52.5% | 1.90 |
| Draw | 21.9% | 4.57 |
| Amed SK win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 89.5% |
| Under 1.5 | 10.5% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 51.5% |
| Under 3.5 | 48.5% |
| Over 4.5 | 32.1% |
| Under 4.5 | 67.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.88% |
| 2 | 1-1 | 8.79% |
| 3 | 2-2 | 6.78% |
| 4 | 3-1 | 6.55% |
| 5 | 1-2 | 6.12% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2145 |
| Dc lambda away | 1.5273 |
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
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.80 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.55 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.94 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Score matrix json | [[0.03144875427971582,0.028476987357707147,0.027654417582530497,0.014078612870004432,0.005375470476423902,0.0016419619239318394,0.0004179539526612002,9.118995513792909e-05,1.7408991784792354e-05,2.954253210645654e-06,4.511950448624341e-07,6.264526368436727e-08,7.973033719834117e-09,9.366920921769657e-10,1.021845939245256e-10,1.0404249772020404e-11,9.931329527142956e-13,8.922264139268997e-14],[0.04477266745038333,0.08793391362079941,0.061241181312316005,0.031177329293765328,0.011904071423787143,0.003636152798782889,0.0009255661855374921,0.00020194171726081473,3.8552510432567625e-05,6.542244325909505e-06,9.991791534634977e-07,1.387290092153562e-07,1.765641970901674e-08,2.074320678771392e-09,2.2628953313449722e-10,2.3040389290621992e-11,2.199309930968598e-12,1.975850672821687e-13],[0.05814192303379267,0.08879857514274135,0.06780982237892384,0.034521364812965825,0.013180885011287221,0.004026161320609737,0.00102484108399479,0.00022360169554072314,4.268759727807991e-05,7.243956047108928e-06,1.10634967303378e-06,1.5360888330554695e-07,1.9550221903955577e-08,2.296809332711701e-09,2.5056102314234666e-10,2.5511668322833847e-11,2.435204752413747e-12,2.187777575485323e-13],[0.04291876140864776,0.0655486551032055,0.05005533762879347,0.025482717849690646,0.009729765192414825,0.0029720010638716507,0.0007565093768946695,0.0001650565946348849,3.1510805062665697e-05,5.347288239157486e-06,8.16676765642488e-07,1.1338983419946123e-07,1.4431433733182717e-08,1.6954411998811164e-09,1.849572255169965e-10,1.883200879420309e-11,1.7976008755215237e-12,1.6149569687069126e-13],[0.023761083028443573,0.03628965480807779,0.027712100591395207,0.014107978766015793,0.005386682909671438,0.0016453868127016362,0.00041882574254737114,9.138016384418355e-05,1.7445304356715123e-05,2.9604153441865148e-06,4.521361707311979e-07,6.277593240265265e-08,7.989664284313275e-09,9.386458927983422e-10,1.0239773581477135e-10,1.0425951492190036e-11,9.952044805902413e-13,8.940874657458462e-14],[0.010523865053958987,0.016072812404964717,0.012273784264651148,0.006248472114673398,0.0023857803098448513,0.0007287474547228141,0.0001854993558339255,4.0472587539619504e-05,7.72658504898708e-06,1.3111780952321843e-06,2.0025265856328966e-07,2.780367546593444e-08,3.5386496757701187e-09,4.1572948074116715e-10,4.535230790009087e-11,4.617689624314963e-12,4.407794729848678e-13,3.959944007889694e-14],[0.00388421323014338,0.005932253052360349,0.004530084239986438,0.002306224750275193,0.0008805585586855113,0.0002689706196871859,6.846525002163107e-05,1.4937873031770521e-05,2.8517758178411374e-06,4.839377242545641e-07,7.391049027850314e-08,1.0261952575187053e-08,1.3060667175980347e-09,1.5344000906283115e-10,1.6738910415503665e-11,1.7043254583269854e-12,1.6268561519604244e-13,1.4615606364399222e-14],[0.0012288081020639234,0.0018767251389967463,0.001433135589449074,0.0007295963147249504,0.00027857314394002646,8.509143476568813e-05,2.1659638375029915e-05,4.725739376662445e-06,9.021866263773075e-07,1.5309833966979045e-07,2.338229234608445e-08,3.246467101632347e-09,4.131867303179069e-10,4.8542218242279336e-11,5.295514823611736e-12,5.391797019518163e-13,5.1467154400988255e-14,4.623787226142538e-15],[0.0003401520731360383,0.0005195049948515511,0.00039671291312073524,0.0002019629416417985,7.71131247198553e-05,2.3554554932583845e-05,5.995705012254267e-06,1.3081538471079501e-06,2.4973846673244464e-07,4.2379861871756706e-08,6.472560852125467e-09,8.986696239497468e-10,1.1437613625257974e-10,1.3437196696538693e-11,1.4658760326764598e-12,1.4925283541322286e-13,1.4246861848082138e-14,1.2799319992036466e-15],[8.369695455433261e-05,0.00012782807861191418,9.761417108077957e-05,4.969448809295538e-05,1.8974259470819354e-05,5.795773918307281e-06,1.4752879360847937e-06,3.218810106962992e-07,6.145001236612946e-08,1.0427881095643724e-08,1.5926218720232233e-09,2.2112436352842621e-10,2.8143101377494128e-11,3.3063224659461094e-12,3.606897307962002e-13,3.672477332716366e-14,3.5055466152161224e-15,3.149368145321879e-16],[1.8534833915245745e-05,2.830774691137384e-05,2.1616825347953787e-05,1.1004929488899844e-05,4.201882252813823e-06,1.28348405934416e-06,3.2670503984403143e-07,7.128110103282737e-08,1.3608210470270303e-08,2.309272126146698e-09,3.5268884088937426e-10,4.896836897396576e-11,6.232337994486503e-12,7.321907720880698e-13,7.987535855802772e-14,8.132763943664772e-15,7.76309301110876e-16,6.974329690050215e-17],[3.7314279191140777e-06,5.698908209014572e-06,4.351893628764582e-06,2.21550952819629e-06,8.459218368330105e-07,2.583906753453728e-07,6.577217322603309e-08,1.4350292628211926e-08,2.7396013749106144e-09,4.6490206082979455e-10,7.100322526073982e-11,9.858299242306039e-12,1.2546926560185499e-12,1.4740445485404785e-13,1.6080486306786555e-14,1.6372859113667804e-15,1.562863855850555e-16,1.4040702302249124e-17],[6.886092522298613e-07,1.0516941517840873e-06,8.031119138431517e-07,4.0885698252523013e-07,1.5610903282430027e-07,4.7684214619638304e-08,1.2137800328584316e-08,2.6482473975643206e-09,5.055745133174105e-10,8.579446458773709e-11,1.3103154854540195e-11,1.8192810411072637e-12,2.315448644240093e-13,2.720247412858923e-14,2.9675426917633787e-15,3.0214980740682426e-16,2.884157310399935e-17,2.591114641021764e-18],[1.1730284471881603e-07,1.7915343916586715e-07,1.3680808356308217e-07,6.964775302982921e-08,2.659277896324402e-08,8.12288537360371e-09,2.0676435911387508e-09,4.511222471199104e-10,8.612333981488065e-11,1.4614870080063773e-11,2.2320892933858784e-12,3.099099246398958e-13,3.9443082109362117e-14,4.633872676471626e-15,5.055133930326265e-16,5.147045559624838e-17,4.913089041875794e-18,4.413898265238066e-19],[1.8554939886797306e-08,2.8338454213996106e-08,2.164027456133592e-08,1.1016867270497592e-08,4.206440314969891e-09,1.2848763401761357e-09,3.2705943860837387e-10,7.135842440114475e-11,1.3622972204518045e-11,2.3117771477662832e-12,3.5307142601713427e-13,4.9021488232439765e-14,6.239098627518871e-15,7.329850282924273e-16,7.9962004691151e-17,8.141586095578006e-18,7.771514156285847e-19,6.981895211002847e-20],[2.739348808571074e-09,4.183732809778204e-09,3.1948505734005158e-09,1.6264694154626186e-09,6.210156074575689e-10,1.8969204390293422e-10,4.828524850793339e-11,1.053496352224104e-11,2.011220349153321e-12,3.4129800549348353e-13,5.2125514612349896e-14,7.237261678194179e-15,9.211060502552383e-16,1.0821385982403586e-16,1.1805148581349967e-17,1.2019787887682564e-18,1.1473434123040674e-19,1.0307684338787677e-20],[3.7914592795780356e-10,5.790592470472203e-10,4.4219070661918267e-10,2.2511527334200056e-10,8.595310609188163e-11,2.6254767478591576e-11,6.683031855940651e-12,1.4581160705581084e-12,2.783676190565598e-13,4.723814236364962e-14,7.21455279668693e-15,1.001689995179447e-15,1.2748782012676226e-16,1.4977590357425722e-17,1.6339189808728415e-18,1.6636266320931116e-19,1.588007271593912e-20,1.4266589678166478e-21],[4.9389714720762166e-11,7.543156581458655e-11,5.7602287778030105e-11,2.9324801639133535e-11,1.1196742668732818e-11,3.4200960110849404e-12,8.705699112016032e-13,1.8994252989218067e-13,3.6261756434402225e-14,6.1535103062983736e-15,9.398088656405164e-16,1.3048586164971435e-16,1.6607291815971703e-17,1.951066490261825e-18,2.128436213908892e-19,2.1671350976525763e-20,2.0686289983641364e-21,1.858447479676565e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13581606892633205, "-10": 6.112768999164685e-07, "-11": 8.279433129818425e-08, "-12": 1.031778223446273e-08, "-13": 1.1903803032563928e-09, "-14": 1.2782168366443203e-10, "-15": 1.2822337460537534e-11, "-16": 1.1907180199964643e-12, "-17": 8.922264139268997e-14, "-2": 0.07544694285576717, "-3": 0.030864969987767058, "-4": 0.010220354711009795, "-5": 0.0028258119670209535, "-6": 0.0006684118513977764, "-7": 0.00013786957185367858, "-8": 2.517939830435207e-05, "-9": 4.122458436421124e-06, "0": 0.2188640900120535, "1": 0.2004123415418353, "10": 2.5110904796466556e-05, "11": 4.931595162676591e-06, "12": 8.911188085746301e-07, "13": 1.4907246152222337e-07, "14": 2.3210188204833826e-08, "15": 3.3760103433963247e-09, "16": 4.545774937723901e-10, "17": 4.9389714720762166e-11, "2": 0.15862313250907287, "3": 0.09409210232723951, "4": 0.04517682646264013, "5": 0.018111542889849258, "6": 0.006211818646176168, "7": 0.0018578279445980203, "8": 0.0004919770564212236, "9": 0.00011679337951192601} |
| Raw goal margin distribution | {"-1": 0.13581606892633205, "-10": 6.112768999164685e-07, "-11": 8.279433129818425e-08, "-12": 1.031778223446273e-08, "-13": 1.1903803032563928e-09, "-14": 1.2782168366443203e-10, "-15": 1.2822337460537534e-11, "-16": 1.1907180199964643e-12, "-17": 8.922264139268997e-14, "-2": 0.07544694285576717, "-3": 0.030864969987767058, "-4": 0.010220354711009795, "-5": 0.0028258119670209535, "-6": 0.0006684118513977764, "-7": 0.00013786957185367858, "-8": 2.517939830435207e-05, "-9": 4.122458436421124e-06, "0": 0.2188640900120535, "1": 0.2004123415418353, "10": 2.5110904796466556e-05, "11": 4.931595162676591e-06, "12": 8.911188085746301e-07, "13": 1.4907246152222337e-07, "14": 2.3210188204833826e-08, "15": 3.3760103433963247e-09, "16": 4.545774937723901e-10, "17": 4.9389714720762166e-11, "2": 0.15862313250907287, "3": 0.09409210232723951, "4": 0.04517682646264013, "5": 0.018111542889849258, "6": 0.006211818646176168, "7": 0.0018578279445980203, "8": 0.0004919770564212236, "9": 0.00011679337951192601} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 74.4% |
| P draw away | 47.5% |
| P home away | 78.1% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7216 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |
| Research p home | 0.5329 |
| Research p draw | 0.2034 |
| Research p away | 0.2637 |
| Research p over 1 5 | 0.8876 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.214517124779461, 1.5272727579225531], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.080934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.282533+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.365873+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.214517124779461, 1.5272727579225531], "h2h": [], "margin_distribution": {"-1": 0.1435531991047053, "-10": 6.112768999164686e-07, "-11": 8.279433129818427e-08, "-12": 1.031778223446273e-08, "-13": 1.190380303256393e-09, "-14": 1.2782168366443203e-10, "-15": 1.2822337460537537e-11, "-16": 1.1907180199964643e-12, "-17": 8.922264139268997e-14, "-2": 0.07544694285576718, "-3": 0.03086496998776706, "-4": 0.010220354711009797, "-5": 0.0028258119670209543, "-6": 0.0006684118513977765, "-7": 0.00013786957185367858, "-8": 2.5179398304352073e-05, "-9": 4.122458436421125e-06, "0": 0.20338982965530705, "1": 0.20814947172020856, "10": 2.5110904796466556e-05, "11": 4.931595162676592e-06, "12": 8.911188085746302e-07, "13": 1.490724615222234e-07, "14": 2.3210188204833826e-08, "15": 3.3760103433963247e-09, "16": 4.5457749377239015e-10, "17": 4.938971472076217e-11, "2": 0.15862313250907287, "3": 0.09409210232723951, "4": 0.04517682646264014, "5": 0.01811154288984926, "6": 0.006211818646176168, "7": 0.0018578279445980207, "8": 0.0004919770564212236, "9": 0.00011679337951192603}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.366249+00:00", "p_over_1_5": 0.8875644607338203, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **40.2%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 54.6%; Under 3.5 goals: 67.7%; Double Chance 1X: 67.3%; Double Chance X2: 59.8%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 83.7%; BTTS Yes (both teams score): 58.9%; BTTS No (at least one team does not score): 41.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 40.2% | 2.49 |
| Draw | 27.1% | 3.69 |
| Basaksehir win | 32.7% | 3.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 54.6% |
| Under 2.5 | 45.4% |
| Over 3.5 | 32.3% |
| Under 3.5 | 67.7% |
| Over 4.5 | 16.3% |
| Under 4.5 | 83.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.77% |
| 2 | 2-1 | 8.83% |
| 3 | 1-2 | 7.86% |
| 4 | 1-0 | 7.51% |
| 5 | 0-0 | 6.81% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5170 |
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
| P btts yes | 58.9% |
| P btts no | 41.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.68 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.79 |
| Fair Over 2.5 odds | 1.83 |
| Fair Under 2.5 odds | 2.20 |
| Fair Over 3.5 odds | 3.10 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.14 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06812726377767661,0.06554411553925138,0.051813900183018596,0.023310161468084657,0.007865123438144401,0.0021230283379013,0.0004775565358233531,9.20761190187604e-05,1.5533784327906915e-05,2.3294586948991837e-06,3.143947364676275e-07,3.857472457403088e-08,4.338522361911739e-09,4.5042111404842077e-10,4.342211339876376e-11,3.906968867564204e-12],[0.07506418141360367,0.1277138150431139,0.07860111058486179,0.035361255818074665,0.011931304822480561,0.003220610387806048,0.000724447956054021,0.00013967844898096315,2.3564578143055213e-05,3.5337629445746066e-06,4.769333202307256e-07,5.851742836023169e-08,6.581490193538515e-09,6.832838228742271e-10,6.587086332102093e-11,5.926828340007342e-12],[0.06545918227647529,0.08834680093818775,0.05961850549129751,0.026821315990096045,0.009049828390267047,0.0024428150780826828,0.0005494897479792634,0.00010594532717952837,1.7873601542882285e-05,2.6803395518006892e-06,3.61751272464012e-07,4.4385144154731495e-08,4.992023730005247e-09,5.182669817643455e-10,4.996268370000793e-11,4.495466352898566e-12],[0.033100283943973574,0.04467370496998495,0.03014687002569678,0.013562546065325238,0.00457616302166557,0.0012352411059099867,0.00027785661308134897,5.357262786094793e-05,9.038018282478063e-06,1.3553484346343545e-06,1.8292421963168615e-07,2.2443923424075493e-08,2.5242815014145193e-09,2.6206841666201335e-10,2.5264278586436558e-11,2.273190827728961e-12],[0.012553190695357435,0.016942378455289966,0.011433116674808095,0.0051435579030310605,0.0017354971081590936,0.00046846175650573017,0.00010537634830807439,2.0317270230315916e-05,3.427643315692174e-06,5.14012127129106e-07,6.937350192290653e-08,8.511795583726859e-09,9.57326744074318e-10,9.938871869368363e-11,9.581407440884362e-12,8.621013038957466e-13],[0.0038086101472902655,0.0051402799551124026,0.0034687821797315397,0.0015605440320367366,0.0005265459640609266,0.0001421302553863851,3.197094979198816e-05,6.164214616212068e-06,1.0399393612545736e-06,1.5595013656075305e-07,2.1047766244350783e-08,2.5824598557107732e-09,2.9045080571445754e-10,3.0154316279361114e-11,2.906977715089636e-12,2.6155961888030723e-13],[0.0009629365424605403,0.0012996245916051018,0.0008770173342829296,0.0003945546581174826,0.0001331273956826798,3.5935002903401275e-05,8.08326257119808e-06,1.5585075079798113e-06,2.6292940841098437e-07,3.942910392204438e-08,5.3215379022903584e-09,6.529271488368366e-10,7.343510724208607e-11,7.62396043054406e-12,7.349754796956164e-13,6.613050569932861e-14],[0.00020868057576606808,0.0002816451511569958,0.00019006079238340228,8.550500432432641e-05,2.8850397047256326e-05,7.787571418647664e-06,1.75174563748062e-06,3.37748366335671e-07,5.698014138380703e-08,8.544787476200209e-09,1.1532448343618791e-09,1.4149760378228846e-10,1.5914320191404982e-11,1.652209031550852e-12,1.5927851889898385e-13,1.4331320285939456e-14],[3.9570764203147895e-05,5.3406570422188816e-05,3.6040013652722365e-05,1.6213767629719303e-05,5.470716450408635e-06,1.4767074088770467e-06,3.321723323321875e-07,6.404506464103989e-08,1.0804780131947882e-08,1.6202934515849139e-09,2.1868244920020283e-10,2.6831286496238527e-11,3.0177308522160944e-12,3.132978417459441e-13,3.020296781739649e-14,2.7175566948330803e-15],[6.669823267228815e-06,9.001908181406115e-06,6.074700007766069e-06,2.732900583647063e-06,9.221128932972246e-07,2.489054137052469e-07,5.5989081725711e-08,1.0795072344344555e-08,1.8211923720094515e-09,2.7310746155010654e-10,3.6859871604250325e-11,4.522529260328453e-12,5.086515728888544e-13,5.280770479240419e-14,5.0908407139584334e-15,4.58055921795142e-16],[1.011804775083799e-06,1.3655794640862944e-06,9.215252381961562e-07,4.145779804915688e-07,1.3988350084006234e-07,3.7758674561674485e-08,8.493481457143385e-09,1.6376004742208068e-09,2.7627285829283393e-10,4.143009831536709e-11,5.591601546835522e-12,6.860626612911342e-13,7.716187816122714e-14,8.010870112960243e-15,7.722748770394743e-16,6.948657413531377e-17],[1.3953605418226373e-07,1.8832444240555247e-07,1.2708577655863772e-07,5.717365342919432e-08,1.9291065068167036e-08,5.2072263239239155e-09,1.1713197229197267e-09,2.2583833771771865e-10,3.810025952945813e-11,5.713545325807331e-12,7.711270351933767e-13,9.461358459236294e-14,1.0641246490478856e-14,1.1047637189066636e-15,1.0650294576565558e-16,9.582760046454619e-18],[1.7639553586030932e-08,2.380717380063618e-08,1.6065642523474684e-08,7.227649723103794e-09,2.4386942714967157e-09,6.582753705753142e-10,1.4807324988442802e-10,2.8549520647533193e-11,4.816472513503171e-12,7.222820620192481e-13,9.748259500847851e-14,1.1960646337350667e-14,1.3452210526591243e-15,1.3965952336664214e-16,1.3463648731599454e-17,1.21141170525516e-18],[2.0583851306693008e-09,2.7780936924218206e-09,1.874723162561032e-09,8.434049448680219e-10,2.845747769190988e-10,7.681510918457062e-11,1.7278882616017915e-11,3.331485034584789e-12,5.62041173872082e-13,8.428414298346828e-14,1.1375385611992646e-14,1.3957051948011621e-15,1.5697579866474911e-16,1.629707264711692e-17,1.5710927274047117e-18,1.4136139154851682e-19],[2.2303909721755254e-10,3.0102408918104863e-10,2.031381569368834e-10,9.138828039970199e-11,3.083548379223085e-11,8.32340476518284e-12,1.872276631901039e-12,3.609875544845045e-13,6.090072948533288e-14,9.132721996818614e-15,1.2325952512955627e-15,1.5123351893291165e-16,1.7009324395870264e-17,1.765891288439261e-18,1.7023787159377167e-19,1.5317404251820557e-20],[2.2556522069973053e-11,3.044334646218027e-11,2.0543888391599276e-11,9.24233369615046e-12,3.118472408536159e-12,8.417675000721374e-13,1.8934818915348024e-13,3.650760714733796e-14,6.159048641474069e-15,9.236158496428655e-16,1.2465555293237762e-16,1.529463780156231e-17,1.7201970682142129e-18,1.7858916359404384e-19,1.7216597249784574e-20,1.5490887982024123e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17604475498767203, "-10": 3.7817609994158623e-07, "-11": 4.570060812922407e-08, "-12": 5.074042059313704e-09, "-13": 5.207874437223402e-10, "-14": 4.93489417387711e-11, "-15": 3.906968867564204e-12, "-2": 0.09757203775767374, "-3": 0.03798353580101762, "-4": 0.01169238526134974, "-5": 0.0029629953684706285, "-6": 0.0006365359658615888, "-7": 0.00011851277096559393, "-8": 1.9452730698736763e-05, "-9": 2.85340380261297e-06, "0": 0.27090818983547144, "1": 0.19926570890159143, "10": 1.2170699422089865e-06, "11": 1.6531245789826918e-07, "12": 2.0630027769085788e-08, "13": 2.3799531082419486e-09, "14": 2.534824436797328e-10, "15": 2.2556522069973053e-11, "2": 0.12326780616989637, "3": 0.05393638400708496, "4": 0.018661721335163004, "5": 0.005315470370916889, "6": 0.0012834998500476287, "7": 0.00026859639116298245, "8": 4.9553888694344275e-05, "9": 8.170009245126723e-06} |
| Raw goal margin distribution | {"-1": 0.17604475498767203, "-10": 3.7817609994158623e-07, "-11": 4.570060812922407e-08, "-12": 5.074042059313704e-09, "-13": 5.207874437223402e-10, "-14": 4.93489417387711e-11, "-15": 3.906968867564204e-12, "-2": 0.09757203775767374, "-3": 0.03798353580101762, "-4": 0.01169238526134974, "-5": 0.0029629953684706285, "-6": 0.0006365359658615888, "-7": 0.00011851277096559393, "-8": 1.9452730698736763e-05, "-9": 2.85340380261297e-06, "0": 0.27090818983547144, "1": 0.19926570890159143, "10": 1.2170699422089865e-06, "11": 1.6531245789826918e-07, "12": 2.0630027769085788e-08, "13": 2.3799531082419486e-09, "14": 2.534824436797328e-10, "15": 2.2556522069973053e-11, "2": 0.12326780616989637, "3": 0.05393638400708496, "4": 0.018661721335163004, "5": 0.005315470370916889, "6": 0.0012834998500476287, "7": 0.00026859639116298245, "8": 4.9553888694344275e-05, "9": 8.170009245126723e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 67.3% |
| P draw away | 59.8% |
| P home away | 72.9% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5463 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |
| Research p home | 0.4133 |
| Research p draw | 0.2484 |
| Research p away | 0.3383 |
| Research p over 1 5 | 0.7800 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.516988883431369, 1.349647182652598], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.080934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.379345+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.461833+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.516988883431369, 1.349647182652598], "h2h": [], "margin_distribution": {"-1": 0.1872820395787621, "-10": 3.7817609994158623e-07, "-11": 4.570060812922407e-08, "-12": 5.074042059313704e-09, "-13": 5.207874437223402e-10, "-14": 4.93489417387711e-11, "-15": 3.906968867564204e-12, "-2": 0.09757203775767374, "-3": 0.03798353580101762, "-4": 0.01169238526134974, "-5": 0.0029629953684706285, "-6": 0.0006365359658615888, "-7": 0.00011851277096559393, "-8": 1.9452730698736763e-05, "-9": 2.85340380261297e-06, "0": 0.24843362065329133, "1": 0.2105029934926815, "10": 1.2170699422089865e-06, "11": 1.6531245789826918e-07, "12": 2.0630027769085788e-08, "13": 2.3799531082419486e-09, "14": 2.534824436797328e-10, "15": 2.2556522069973053e-11, "2": 0.12326780616989637, "3": 0.05393638400708496, "4": 0.018661721335163004, "5": 0.005315470370916889, "6": 0.0012834998500476287, "7": 0.00026859639116298245, "8": 4.9553888694344275e-05, "9": 8.170009245126723e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.462202+00:00", "p_over_1_5": 0.7800271546783782, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **43.3%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 45.5%; Under 3.5 goals: 75.9%; Double Chance 1X: 72.3%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 43.3% | 2.31 |
| Draw | 29.0% | 3.45 |
| Torku Konyaspor win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 72.4% |
| Under 1.5 | 27.6% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 24.1% |
| Under 3.5 | 75.9% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.83% |
| 2 | 1-0 | 10.44% |
| 3 | 0-0 | 9.47% |
| 4 | 2-1 | 8.91% |
| 5 | 2-0 | 8.23% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4121 |
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
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.56 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.14 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.25 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.0946952397843403,0.07716884000290665,0.04835913664784076,0.01745101681998351,0.004723068004745055,0.0010226279239798474,0.0001845142235676571,2.8536142367355107e-05,3.861612832776817e-06,4.645042293165189e-07,5.0286698733596874e-08,4.949073383317234e-09,4.4648420568659083e-10,3.718143961740699e-11,2.8751573559761086e-12],[0.10435940907850691,0.1383254553583337,0.06828669804762047,0.0246421338099585,0.006669323338980732,0.0014440266948602526,0.0002605478084112638,4.029515562847614e-05,5.452884558484377e-06,6.55914523043828e-07,7.100855909068659e-08,6.988459744497716e-09,6.304689092937566e-10,5.2502958409268256e-11,4.0599360496586066e-12],[0.08227478984638288,0.0890697502682119,0.04821294850861548,0.01739826294856765,0.004708790319680574,0.001019536552138057,0.00018395644291081085,2.8449878512321264e-05,3.849939299426894e-06,4.631000477356824e-07,5.013468363520543e-08,4.934112491147775e-09,4.451344980667442e-10,3.7069041302462536e-11,2.8664658463052306e-12],[0.03872604103808123,0.04192437088661936,0.0226934231737041,0.008189213806508194,0.002216387395217229,0.00047988714929130926,8.658672687812038e-05,1.3391114882866101e-05,1.8121335536936927e-06,2.179772380681184e-07,2.359796748813624e-08,2.322444617305801e-09,2.0952100724638054e-10,1.7448081209345124e-11,1.349220997167395e-12],[0.01367101262686256,0.014800082538791845,0.00801120038191789,0.0028909447584058493,0.0007824259659343443,0.00016940908756924732,3.0566724734538846e-05,4.727312571698402e-06,6.39716842466458e-07,7.695001849188565e-08,8.330521345607372e-09,8.198661375469569e-10,7.396481176171766e-11,6.159497127344346e-12,4.763001017988248e-13],[0.0038608973441938144,0.004179763484059076,0.002262482167383504,0.0008164458072409608,0.00022096873262836462,4.784364656303524e-05,8.632497794376505e-06,1.3350633966485534e-06,1.8066555313259396e-07,2.173182997777455e-08,2.3526631579438983e-09,2.3154239407472014e-10,2.0888763187409056e-11,1.73953362121873e-12,1.3451423448040193e-13],[0.0009086457058974889,0.0009836894905193197,0.0005324655184511079,0.0001921470349278127,5.200404780052467e-05,1.1259797950690299e-05,2.0316214995526173e-06,3.142014703628254e-07,4.251886658017431e-08,5.114493401461416e-09,5.536892295527546e-10,5.4492513877793804e-11,4.916081231813238e-12,4.093918108342645e-13,3.1657350777925663e-14],[0.00018329647494015364,0.00019843467577913,0.00010741155978156381,3.876084368624535e-05,1.049051195926833e-05,2.271381749238948e-06,4.09828667943582e-07,6.338226391730335e-08,8.577114613554234e-09,1.0317207306522135e-09,1.116929110330261e-10,1.0992497559388519e-11,9.916960532166698e-13,8.258452695945795e-14,6.386076295607726e-15],[3.235353209616896e-05,3.5025565297472946e-05,1.895913900159309e-05,6.841649304423203e-06,1.851672900366732e-06,4.009199977830906e-07,7.233857043116653e-08,1.1187558902296734e-08,1.5139404783029822e-09,1.821083017790593e-10,1.9714837304980448e-11,1.9402780261914696e-12,1.7504357406690626e-13,1.457693686963773e-14,1.1272018431668546e-15],[5.076177097190531e-06,5.495411500997653e-06,2.9746349454603915e-06,1.0734353022999601e-06,2.9052220760289015e-07,6.29032065031684e-08,1.1349715801498928e-08,1.7552961483309987e-09,2.375329518776491e-10,2.8572274209547095e-11,3.0932018582981677e-12,3.0442409964572146e-13,2.7463838540028185e-14,2.2870799041322965e-15,1.768547608090085e-16],[7.167939642850782e-07,7.759929804966906e-07,4.200405805458545e-07,1.515770492256842e-07,4.10238967067921e-08,8.882400651585584e-09,1.6026642938379843e-09,2.47860872575321e-10,3.354141964805569e-11,4.034617647724838e-12,4.3678311057560284e-13,4.2986947269775683e-14,3.878098286304375e-15,3.2295269446510267e-16,2.4973207726172505e-17],[9.201512680941145e-08,9.961452810897025e-08,5.3920776694283054e-08,1.9458006206579438e-08,5.266253966656418e-09,1.1402373109305223e-09,2.0573465399851987e-10,3.181799897528004e-11,4.305725405154306e-12,5.179254750745098e-13,5.607002194544001e-14,5.518251549624879e-15,4.978330222821701e-16,4.145756607240192e-17,3.205820626647502e-18],[1.0827683618514249e-08,1.1721926943659918e-08,6.345012290419815e-09,2.289679342488061e-09,6.196951934197535e-10,1.3417499144845357e-10,2.420938621836062e-11,3.744115106118675e-12,5.066670454280288e-13,6.094577464084841e-14,6.597920137260292e-15,6.493484710451201e-16,5.858143815076234e-17,4.878430586259924e-18,3.7723809863288572e-19],[1.1761149742808464e-09,1.2732486736397895e-09,6.892022550417609e-10,2.487075034587359e-10,6.73119775336441e-11,1.457423602096202e-11,2.629650316054329e-12,4.0668992527706796e-13,5.503473504560215e-14,6.6199974712673926e-15,7.16673385180215e-16,7.05329493573929e-17,6.363180625836659e-18,5.299005277249951e-19,4.0976019645857723e-20],[1.1862584476590722e-10,1.2842298823713797e-10,6.95146320782871e-11,2.5085249607890155e-11,6.789251367771093e-12,1.4699932384259327e-12,2.65232989123043e-13,4.101974466677917e-14,5.550938538338407e-15,6.677092032243272e-16,7.228543773131514e-17,7.114126496406387e-18,6.418060254691384e-19,5.344706862669972e-20,4.132941975852746e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1652485529435056, "-10": 5.7738217357472485e-08, "-11": 5.617960554910621e-09, "-12": 5.018536299421643e-10, "-13": 4.124137566706559e-11, "-14": 2.8751573559761086e-12, "-2": 0.07822189328551281, "-3": 0.02523137664425963, "-4": 0.006365104270930512, "-5": 0.0013135171026377396, "-6": 0.00022888586279716088, "-7": 3.447656611174192e-05, "-8": 4.57006022007589e-06, "-9": 5.406627159169615e-07, "0": 0.29025522361701356, "1": 0.21924617706725893, "10": 8.230090014392947e-07, "11": 1.0445134125772103e-07, "12": 1.2170446924232325e-08, "13": 1.3045379625179845e-09, "14": 1.1862584476590722e-10, "2": 0.13308115647964347, "3": 0.055991655813085496, "4": 0.01842391868416151, "5": 0.004959139657941848, "6": 0.0011271551447361568, "7": 0.00022145365533194082, "8": 3.828907671858148e-05, "9": 5.908449315694765e-06} |
| Raw goal margin distribution | {"-1": 0.1652485529435056, "-10": 5.7738217357472485e-08, "-11": 5.617960554910621e-09, "-12": 5.018536299421643e-10, "-13": 4.124137566706559e-11, "-14": 2.8751573559761086e-12, "-2": 0.07822189328551281, "-3": 0.02523137664425963, "-4": 0.006365104270930512, "-5": 0.0013135171026377396, "-6": 0.00022888586279716088, "-7": 3.447656611174192e-05, "-8": 4.57006022007589e-06, "-9": 5.406627159169615e-07, "0": 0.29025522361701356, "1": 0.21924617706725893, "10": 8.230090014392947e-07, "11": 1.0445134125772103e-07, "12": 1.2170446924232325e-08, "13": 1.3045379625179845e-09, "14": 1.1862584476590722e-10, "2": 0.13308115647964347, "3": 0.055991655813085496, "4": 0.01842391868416151, "5": 0.004959139657941848, "6": 0.0011271551447361568, "7": 0.00022145365533194082, "8": 3.828907671858148e-05, "9": 5.908449315694765e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 5.0, "home_xg": 3.89, "source": "pipeline training history"}, {"away": "Amedspor", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-10-24T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-10-18T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 4.0, "home_xg": 2.41, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 0.36, "date": "2026-09-20T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 5.0, "away_xg": 1.73, "date": "2026-09-12T00:00:00+00:00", "home": "Samsunspor", "home_goals": 1.0, "home_xg": 1.24, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 0.0, "away_xg": 1.74, "date": "2026-09-06T00:00:00+00:00", "home": "Kocaelispor", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Samsunspor", "away_goals": 2.0, "away_xg": 0.32, "date": "2026-08-22T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.85, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 3.0, "away_xg": 1.89, "date": "2026-08-17T00:00:00+00:00", "home": "Samsunspor", "home_goals": 3.0, "home_xg": 2.74, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 72.3% |
| P draw away | 56.7% |
| P home away | 71.0% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4548 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |
| Research p home | 0.4453 |
| Research p draw | 0.2659 |
| Research p away | 0.2888 |
| Research p over 1 5 | 0.7116 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4120743830663378, 1.0825886086675645], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.080934+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.186111+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Samsunspor%22+%22Torku+Konyaspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.269183+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Samsunspor_vs_Torku+Konyaspor&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.913613856180298, "goals_for": 0.9751316584067636, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.22037567410820427, "results": "LLLLLLLLWD", "xg_against": 2.102762810589968, "xg_for": 1.119679917641185, "xg_matches": 10}, "venue": {"goals_against": 2.9627088822913965, "goals_for": 0.9012025941363605, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.148698354997035, "results": "LLLLD", "xg_against": 1.764225747400591, "xg_for": 1.383053774479519, "xg_matches": 5}}}, "goal_rates": [1.4120743830663378, 1.0825886086675645], "h2h": [], "margin_distribution": {"-1": 0.17741953466172442, "-10": 5.7738217357472485e-08, "-11": 5.617960554910621e-09, "-12": 5.018536299421643e-10, "-13": 4.124137566706559e-11, "-14": 2.8751573559761086e-12, "-2": 0.07822189328551281, "-3": 0.02523137664425963, "-4": 0.006365104270930512, "-5": 0.0013135171026377396, "-6": 0.00022888586279716088, "-7": 3.447656611174192e-05, "-8": 4.57006022007589e-06, "-9": 5.406627159169615e-07, "0": 0.2659132601805759, "1": 0.23141715878547775, "10": 8.230090014392947e-07, "11": 1.0445134125772103e-07, "12": 1.2170446924232325e-08, "13": 1.3045379625179845e-09, "14": 1.1862584476590722e-10, "2": 0.13308115647964347, "3": 0.055991655813085496, "4": 0.01842391868416151, "5": 0.004959139657941848, "6": 0.0011271551447361568, "7": 0.00022145365533194082, "8": 3.828907671858148e-05, "9": 5.908449315694765e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.269579+00:00", "p_over_1_5": 0.7116055294160273, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **46.3%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.5%; Double Chance 1X: 53.7%; Double Chance X2: 73.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 26.8% | 3.73 |
| Draw | 26.9% | 3.71 |
| Trabzonspor win | 46.3% | 2.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.81% |
| 2 | 1-2 | 9.39% |
| 3 | 0-1 | 8.80% |
| 4 | 0-2 | 7.98% |
| 5 | 0-0 | 7.30% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | a85eafd97e49ac329956fa1022be891d |
| Matched home-team name | Alanyaspor |
| Matched away-team name | Trabzonspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1770 |
| Dc lambda away | 1.6080 |
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
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.70 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07299863009787619,0.08798949335333146,0.07980790753354723,0.04277829012643664,0.017197375824309965,0.005530837896857219,0.001482307928538247,0.0003405172705137835,6.844597409557033e-05,1.2229371868596244e-05,1.9665405372480876e-06,2.8748088292481964e-07,3.852356550756794e-08,4.7652081476767435e-09,5.473342079054578e-10,5.867594393966772e-11],[0.06138077651683436,0.12809891520816719,0.09393225656957939,0.050349162732718895,0.02024095566687471,0.006509681815100384,0.0017446457746063365,0.00040078178477274913,8.055949590204893e-05,1.4393717759896282e-05,2.3145775400967406e-06,3.383590534859264e-07,4.53414398530721e-08,5.608551435167885e-09,6.442010426682571e-10,6.906037247357151e-11],[0.042754918513889614,0.0687519206445996,0.05527816163169318,0.029629961604276195,0.01191159309693188,0.003830880431148404,0.0010267059968617068,0.0002358559358285594,4.740843026742933e-05,8.470554055338203e-06,1.3621049471517804e-06,1.9912080398374176e-07,2.6682968474788312e-08,3.300574521205323e-09,3.7910565188586996e-10,4.0641315042945044e-11],[0.016773884942708577,0.026973196220876832,0.021687084323485352,0.01162461733251907,0.004673232905996246,0.0015029556789,0.0004028039079469276,9.253251948914068e-05,1.859958063917117e-05,3.323222311348302e-06,5.34389783855994e-07,7.812035601559737e-08,1.0468434011413604e-08,1.2949026495173378e-09,1.4873317051927643e-10,1.5944662418880913e-11],[0.004935628914480688,0.007936723522214867,0.006381312428418916,0.003420483544636133,0.001375074619488429,0.0004422369374356732,0.00011852296720282884,2.7227215417313072e-05,5.472830433346519e-06,9.778409822864485e-07,1.572414308200703e-07,2.2986510833777486e-08,3.0802825804838783e-09,3.810184092847013e-10,4.3763966395657736e-11,4.6916344743661135e-12],[0.0011618266306063834,0.0018682718874620946,0.0015021345498249768,0.0008051676778312477,0.0003236868775335576,0.00010410074579211652,2.7899816218096334e-05,6.4091738858814475e-06,1.2882816460532222e-06,2.3017972246364388e-07,3.701398239754635e-08,5.410929568276667e-09,7.250857780858239e-10,8.969015749127192e-11,1.0301856663141761e-11,1.1043913486682894e-12],[0.00022790765252932412,0.00036648622861724597,0.00029466354963401416,0.00015794428403765543,6.349546005389576e-05,2.04207374620518e-05,5.472917776852141e-06,1.257244184720671e-06,2.5271347549966404e-07,4.515279545551517e-08,7.260781958994773e-09,1.0614253653867562e-09,1.422351607482861e-10,1.7593910063976158e-11,2.0208453713656123e-12,2.1664096270311573e-13],[3.832037048737704e-05,6.162095876674194e-05,4.954470052140168e-05,2.6556736526904093e-05,1.06761204660237e-05,3.433540806930996e-06,9.202158616808247e-07,2.1139291470433407e-07,4.249121914435844e-08,7.591986627888538e-09,1.2208271710443919e-09,1.784679575034745e-10,2.3915406067835545e-11,2.9582383236842396e-12,3.3978474381621494e-13,3.642599035790283e-14],[5.63778543960162e-06,9.06582425198282e-06,7.289135977977865e-06,3.9070912052908106e-06,1.5706966229517043e-06,5.051508146031643e-07,1.3538437964694425e-07,3.110063606894468e-08,6.2514107655064786e-09,1.116951405322645e-09,1.796110413768398e-10,2.6256636860543025e-11,3.5184922900423743e-12,4.3522316553886956e-13,4.998995199999029e-14,5.359079660529404e-15],[7.372840956675248e-07,1.1855875160045432e-06,9.532402545813771e-07,5.109517268516213e-07,2.0540860442940394e-07,6.6061340132647e-08,1.7704957200811714e-08,4.067200602865967e-09,8.175312420577611e-10,1.4606985590357417e-10,2.3488720106876422e-11,3.433724282413271e-12,4.601325172744349e-13,5.691651827753085e-14,6.537459956152607e-15,7.008362136964981e-16],[8.677681319962045e-08,1.3954119858638897e-07,1.1219440646047608e-07,6.013796149350416e-08,2.4176167912623868e-08,7.775283104699423e-09,2.0838368449153923e-09,4.787010991207385e-10,9.622173636157123e-11,1.7192119936296424e-11,2.764573776906394e-12,4.0414224636732776e-13,5.4156645631212037e-14,6.698956485790403e-15,7.69445515980417e-16,8.248697287360879e-17],[9.284955855158613e-09,1.4930645884288016e-08,1.200459054407634e-08,6.4346488088001925e-09,2.5868045107768093e-09,8.319406731660262e-10,2.2296662438944058e-10,5.122011755522044e-11,1.0295544875204138e-11,1.8395245086714337e-12,2.9580419619531796e-13,4.3242460495676357e-14,5.794659257566187e-15,7.167757486450819e-16,8.232922350344112e-17,8.825951006005294e-18],[9.106834174059029e-10,1.46442178402242e-09,1.1774295658243895e-09,6.311207138103166e-10,2.537179507134002e-10,8.159808050103666e-11,2.1868925456831416e-11,5.023751585119776e-12,1.0098036153610304e-12,1.8042352511865533e-13,2.901295175512243e-14,4.241290138106917e-15,5.683495083556302e-16,7.03025193089221e-17,8.074982776663654e-18,8.656634828845573e-19],[8.245042672424678e-11,1.3258416557190367e-10,1.0660078824812505e-10,5.713969440269128e-11,2.2970829274030073e-11,7.387634855978992e-12,1.979944074366327e-12,4.548347472161315e-13,9.142445926090105e-14,1.633498134785469e-14,2.6267418589369427e-15,3.8399313643414127e-16,5.145658589668949e-17,6.364970093912082e-18,7.310836707923852e-19,7.837446273781994e-20],[6.931603357436472e-12,1.1146344339669228e-11,8.961923074059484e-12,4.803731324390026e-12,1.9311564978491798e-12,6.210781023909429e-13,1.664538018622299e-13,3.823793503733269e-14,7.686049835546984e-15,1.3732810860171577e-15,2.2083006009684862e-16,3.22822842705399e-17,4.325952669191228e-18,5.351027256717545e-19,6.146216858258198e-20,6.588937263692679e-21],[5.43890252759387e-13,8.74601117177588e-13,7.031998737681766e-13,3.7692616116120893e-13,1.5152875050276551e-13,4.873307208646442e-14,1.3060845478194093e-14,3.000350579803426e-15,6.03088112837854e-16,1.077548957244129e-16,1.7327494233219534e-17,2.5330387280047494e-18,3.3943712144858184e-19,4.1986989403485184e-20,4.822646750215026e-21,5.170028590745715e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21669638206309108, "-10": 2.3329223302160637e-06, "-11": 3.362763221040907e-07, "-12": 4.4527167257040574e-08, "-13": 5.4500505053879455e-09, "-14": 6.163945803790293e-10, "-15": 5.867594393966772e-11, "-2": 0.1436968116717485, "-3": 0.06728149202981623, "-4": 0.02483200660874311, "-5": 0.007530955128678584, "-6": 0.0019339841634942521, "-7": 0.0004301054397906924, "-8": 8.428308918864332e-05, "-9": 1.475393018359505e-05, "0": 0.26948519034651675, "1": 0.15558532479607226, "10": 1.0294400823370548e-07, "11": 1.086093368750405e-08, "12": 1.0526064322130272e-09, "13": 9.429997093768418e-11, "14": 7.80620447461406e-12, "15": 5.43890252759387e-13, "2": 0.07698166339154837, "3": 0.02638188676420363, "4": 0.00712675998215011, "5": 0.0015819780629210468, "6": 0.0002973537294410354, "7": 4.840224337681112e-05, "8": 6.942263285915162e-06, "9": 8.894846104800223e-07} |
| Raw goal margin distribution | {"-1": 0.21669638206309108, "-10": 2.3329223302160637e-06, "-11": 3.362763221040907e-07, "-12": 4.4527167257040574e-08, "-13": 5.4500505053879455e-09, "-14": 6.163945803790293e-10, "-15": 5.867594393966772e-11, "-2": 0.1436968116717485, "-3": 0.06728149202981623, "-4": 0.02483200660874311, "-5": 0.007530955128678584, "-6": 0.0019339841634942521, "-7": 0.0004301054397906924, "-8": 8.428308918864332e-05, "-9": 1.475393018359505e-05, "0": 0.26948519034651675, "1": 0.15558532479607226, "10": 1.0294400823370548e-07, "11": 1.086093368750405e-08, "12": 1.0526064322130272e-09, "13": 9.429997093768418e-11, "14": 7.80620447461406e-12, "15": 5.43890252759387e-13, "2": 0.07698166339154837, "3": 0.02638188676420363, "4": 0.00712675998215011, "5": 0.0015819780629210468, "6": 0.0002973537294410354, "7": 4.840224337681112e-05, "8": 6.942263285915162e-06, "9": 8.894846104800223e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 53.7% |
| P draw away | 73.2% |
| P home away | 73.1% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5270 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,452.1266 |
| Elo away rating | 1,593.6095 |
| Elo rating diff | -81.4829 |
| Elo home expectancy | 0.3848 |
| Research p home | 0.2847 |
| Research p draw | 0.2480 |
| Research p away | 0.4673 |
| Research p over 1 5 | 0.7654 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.1769793178714154, 1.6080470512945653], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.469506+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.658062+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.740210+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.1876924601452241, 1.5915280376976866], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.22672673069404517, "-10": 2.1158458587201307e-06, "-11": 3.0185832384141636e-07, "-12": 3.955978715886248e-08, "-13": 4.79237678906986e-09, "-14": 5.364587689859076e-10, "-15": 5.054924478114866e-11, "-2": 0.14148067992882804, "-3": 0.06557302631013309, "-4": 0.023955182779710624, "-5": 0.0071909008914463075, "-6": 0.0018277800505572708, "-7": 0.00040232644201505905, "-8": 7.803207160934821e-05, "-9": 1.3519695064385087e-05, "0": 0.24803978199014287, "1": 0.16919691150916735, "10": 1.133394448138597e-07, "11": 1.2066738935715855e-08, "12": 1.1801315267738117e-09, "13": 1.0668838175272593e-10, "14": 8.912349844848331e-12, "15": 6.267008074722588e-13, "2": 0.07879098853828047, "3": 0.027251746733584298, "4": 0.007429478170335349, "5": 0.0016643008336539593, "6": 0.0003156909746798118, "7": 5.185689570679267e-05, "8": 7.505692725782433e-06, "9": 9.704524167289507e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.740618+00:00", "p_over_1_5": 0.7653599701180481, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Besiktas JK vs Genclerbirligi SK

The model's most likely 1X2 outcome is **Besiktas JK win** at **62.6%**. Expected goals are 1.92 for Besiktas JK and 0.81 for Genclerbirligi SK (2.73 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 51.4%; Under 3.5 goals: 70.7%; Double Chance 1X: 85.9%; Double Chance X2: 37.4%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 85.8%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 62.6% | 1.60 |
| Draw | 23.3% | 4.29 |
| Genclerbirligi SK win | 14.1% | 7.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.92 |
| Genclerbirligi SK expected goals | 0.81 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 76.7% |
| Under 1.5 | 23.3% |
| Over 2.5 | 51.4% |
| Under 2.5 | 48.6% |
| Over 3.5 | 29.3% |
| Under 3.5 | 70.7% |
| Over 4.5 | 14.2% |
| Under 4.5 | 85.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 12.04% |
| 2 | 1-0 | 11.56% |
| 3 | 1-1 | 11.11% |
| 4 | 2-1 | 9.73% |
| 5 | 3-0 | 7.71% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | 1fa78d1150755a8ec1d24cc1e19eeb0a |
| Matched home-team name | Besiktas |
| Matched away-team name | Genclerbirligi |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9218 |
| Dc lambda away | 0.8083 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.34 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.28 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.42 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.06 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.07498630311809729,0.04293908275245669,0.02130397637671627,0.0057400752930034885,0.0011599406533335974,0.00018751842100690804,2.5262181960105193e-05,2.917097808122412e-06,2.947400656499943e-07,2.6471273699946576e-08,2.139700609677692e-09,1.5723111609247117e-10,1.0590962325701659e-11,6.585219307263631e-13,3.8020723699878097e-14,2.0488364507417007e-15,1.0350598946601563e-16],[0.11555217104275577,0.1110751494111648,0.040941677193819574,0.011031194625770213,0.0022291573625980647,0.00036037022032893093,4.85485000890514e-05,5.6060368586155506e-06,5.664272439353525e-07,5.087211530693167e-08,4.112046037968139e-09,3.021645107960897e-10,2.0353559966612085e-11,1.2655380308399145e-12,7.306768318130049e-14,3.93742459651221e-15,1.989163306140357e-16],[0.12042433138178021,0.09734024066931969,0.03934056492089702,0.010599796053193314,0.002141981373333262,0.00034627716840453265,4.664990665926647e-05,5.386800739530999e-06,5.442758892732262e-07,4.88826519104552e-08,3.951235640605933e-09,2.9034771823073063e-10,1.955759026302781e-11,1.2160464464225107e-12,7.021021440341522e-14,3.7834431458906784e-15,1.9113728002157659e-16],[0.07714325273571855,0.0623556942450677,0.025201378389532552,0.006790178832599933,0.0013721430589835894,0.0002218235037083329,2.9883707870500556e-05,3.450758880023705e-06,3.486605406265512e-07,3.1313993837053886e-08,2.531142719616205e-09,1.8599536448911724e-10,1.2528499110194346e-11,7.789935578495332e-13,4.4976328721980394e-14,2.42365564720773e-15,1.224416306134721e-16],[0.037063200025875286,0.029958570407638357,0.012107912164125517,0.003262317148413297,0.0006592412279198336,0.00010657430944152748,1.4357520626121536e-05,1.6579047690604575e-06,1.6751271044587902e-07,1.5044696406149587e-08,1.2160784719897714e-09,8.936080802247394e-11,6.019272613975918e-12,3.742646703316583e-13,2.160871636516368e-14,1.164436692267065e-15,5.882664375675527e-17],[0.014245505575079349,0.011514790451592712,0.004653762495310812,0.0012538948901593412,0.000253384073180345,4.096259681434935e-05,5.518415570726233e-06,6.37227536049584e-07,6.438470636338605e-08,5.782536488472539e-09,4.674084439651714e-10,3.434646463308682e-11,2.3135504090432726e-12,1.4385129843194004e-13,8.30546442928137e-15,4.475595571870939e-16,2.2610440572185146e-17],[0.004562801488357276,0.003688159941656315,0.0014905890372337426,0.0004016195452600324,8.115831482006681e-05,1.3120222144902787e-05,1.7675353568027625e-06,2.0410246127000556e-07,2.062226801807753e-08,1.8521326573511792e-09,1.497098107578511e-10,1.1001090773627116e-11,7.41024682777075e-13,4.607522808706819e-14,2.660220464601683e-15,1.4335225962314925e-16,7.242070234113502e-18],[0.0012526752372587376,0.0010125504345852743,0.00040922752844641067,0.00011026095709622595,2.2281269858476466e-05,3.6020364747822057e-06,4.852605966084353e-07,5.603445596940614e-08,5.6616542596200215e-09,5.084860084100103e-10,4.110145339208482e-11,3.020248421966675e-12,2.0344152001373864e-13,1.2649530649754018e-14,7.303390932431751e-16,3.935604612499936e-17,1.988243861125922e-18],[0.00030092167000682075,0.0002432381184514451,9.830595162265687e-05,2.6487241352798836e-05,5.352478229200032e-06,8.652927743578116e-07,1.1657085953057382e-07,1.3460777036781604e-08,1.3600607756359668e-09,1.2215014257062205e-10,9.873523181889978e-12,7.255337791801133e-13,4.8871375541221326e-14,3.0387108922631436e-15,1.7544440336422919e-16,9.454235840661156e-18,4.776223280186412e-19],[6.425632920032659e-05,5.193905979894976e-05,2.0991441359718764e-05,5.655866857097293e-06,1.1429240144960737e-06,1.8476747574390105e-07,2.489157901121511e-08,2.87430320504346e-09,2.904161502550991e-10,2.60829330526672e-11,2.1083106308967318e-12,1.549244936727146e-13,1.0435590082888772e-14,6.488612383197693e-16,3.7462949539896114e-17,2.0187794734133972e-18,1.0198752898685077e-19],[1.2348689471205046e-05,9.981574249036316e-06,4.034105186681901e-06,1.0869364057668568e-06,2.196455029386169e-07,3.5508349305584796e-08,4.783628064080235e-09,5.523794802301078e-10,5.581176051533328e-11,5.012580780353393e-12,4.0517212255647827e-13,2.977316768101811e-14,2.0054967811906287e-15,1.2469722503027263e-16,7.19957607757727e-18,3.879661527241145e-19,1.9599817497631696e-20],[2.1574122602395505e-06,1.7438587885440528e-06,7.04789606147104e-07,1.8989625849529874e-07,3.837378063892736e-08,6.203585272054101e-09,8.357370924208352e-10,9.650499882858353e-11,9.75074939588578e-12,8.757369157425447e-13,7.078672653879008e-14,5.201604358986949e-15,3.5037591265864085e-16,2.1785576738768514e-17,1.2578220332215416e-18,6.77807095559992e-20,3.424240820570405e-21],[3.4550700289787494e-07,2.792769071591694e-07,1.1287121566020084e-07,3.041165953462491e-08,6.145515246559381e-09,9.934967896821065e-10,1.3384229956162623e-10,1.5455160575672514e-11,1.5615708976302405e-12,1.4024822360638618e-13,1.1336409912055098e-14,8.330307403252404e-16,5.611228493568165e-17,3.488934156969051e-18,2.0143869991219547e-19,1.0854999873962113e-20,5.483880873952547e-22],[5.107618600509451e-08,4.12854128493758e-08,1.6685714492986946e-08,4.495745574144661e-09,9.084894870370855e-10,1.4686830194369888e-10,1.9785862892567288e-11,2.284731278037167e-12,2.3084650950209473e-13,2.0732848526144667e-14,1.6758577291970847e-15,1.2314665892138203e-16,8.29506052991022e-18,5.157679828954196e-19,2.9778616407323166e-20,1.6046910424320559e-21,8.106802964875688e-23],[7.011248855057911e-09,5.667265436418985e-09,2.2904548241544336e-09,6.17132825975092e-10,1.2470872189214723e-10,2.0160671623843434e-11,2.7160134575829216e-12,3.136259930538923e-13,3.168839437774856e-14,2.8460065611892367e-15,2.3004567302462716e-16,1.6904392024898396e-17,1.1386663373253465e-18,7.079968107231712e-20,4.087722802368765e-21,2.2027659294786094e-22,1.1128241447001435e-23],[8.982745201283809e-10,7.260846456287103e-10,2.9345088878977825e-10,7.906646940770562e-11,1.5977562575414675e-11,2.5829660311243148e-12,3.479730552585517e-13,4.0181463279118635e-14,4.0598868820319254e-15,3.6462764778206826e-16,2.9473232346436316e-17,2.165774592820699e-18,1.4588484575175139e-19,9.070787652131166e-21,5.237151489875785e-22,2.8221627118970685e-23,1.4257396866560668e-24],[1.0789319557123792e-10,8.721119314493653e-11,3.524685764238766e-11,9.496800650333124e-12,1.919090706763599e-12,3.10244199189943e-13,4.1795602639565393e-14,4.826260100634783e-15,4.87639535069491e-16,4.3796012500954134e-17,3.540077281960653e-18,2.6013466537270307e-19,1.752246316785657e-20,1.0895068759121499e-21,6.290426782367277e-23,3.389744967552321e-24,1.7124788402555772e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09596500167186953, "-10": 2.4622237678126514e-09, "-11": 1.788468858813606e-10, "-12": 1.1929193053235952e-11, "-13": 7.354954986841677e-13, "-14": 4.2149285576411883e-14, "-15": 2.2477527813557365e-15, "-16": 1.0350598946601563e-16, "-2": 0.034713991768474756, "-3": 0.00834711771532222, "-4": 0.0015705849872283393, "-5": 0.00024181790568857597, "-6": 3.1445059880619345e-05, "-7": 3.535030567861391e-06, "-8": 3.4975557778598757e-07, "-9": 3.088657867073091e-08, "0": 0.23289422506386012, "1": 0.24162311056222058, "10": 1.4210042554466967e-05, "11": 2.454008302524457e-06, "12": 3.8916385613151964e-07, "13": 5.704639913095361e-08, "14": 7.77258035832901e-09, "15": 9.854857132733175e-10, "16": 1.0789319557123792e-10, "2": 0.1962267125342893, "3": 0.11218037720041178, "4": 0.0501843825992185, "5": 0.018370559570324647, "6": 0.005679539726669601, "7": 0.0015180311208566894, "8": 0.0003570910263911787, "9": 7.497403371800261e-05} |
| Raw goal margin distribution | {"-1": 0.09596500167186953, "-10": 2.4622237678126514e-09, "-11": 1.788468858813606e-10, "-12": 1.1929193053235952e-11, "-13": 7.354954986841677e-13, "-14": 4.2149285576411883e-14, "-15": 2.2477527813557365e-15, "-16": 1.0350598946601563e-16, "-2": 0.034713991768474756, "-3": 0.00834711771532222, "-4": 0.0015705849872283393, "-5": 0.00024181790568857597, "-6": 3.1445059880619345e-05, "-7": 3.535030567861391e-06, "-8": 3.4975557778598757e-07, "-9": 3.088657867073091e-08, "0": 0.23289422506386012, "1": 0.24162311056222058, "10": 1.4210042554466967e-05, "11": 2.454008302524457e-06, "12": 3.8916385613151964e-07, "13": 5.704639913095361e-08, "14": 7.77258035832901e-09, "15": 9.854857132733175e-10, "16": 1.0789319557123792e-10, "2": 0.1962267125342893, "3": 0.11218037720041178, "4": 0.0501843825992185, "5": 0.018370559570324647, "6": 0.005679539726669601, "7": 0.0015180311208566894, "8": 0.0003570910263911787, "9": 7.497403371800261e-05} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 62.6% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 48.3% |
| P home draw | 85.9% |
| P draw away | 37.4% |
| P home away | 76.7% |
| Raw p home draw | 85.9% |
| Raw p draw away | 37.4% |
| Raw p home away | 76.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5137 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,572.0567 |
| Elo away rating | 1,407.1890 |
| Elo rating diff | 224.8678 |
| Elo home expectancy | 0.7849 |
| Research p home | 0.6360 |
| Research p draw | 0.2133 |
| Research p away | 0.1506 |
| Research p over 1 5 | 0.7567 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.9217857018732858, 0.8083104099679224], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.469506+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.766707+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Besiktas+JK%22+%22Genclerbirligi+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.848800+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Besiktas+JK_vs_Genclerbirligi+SK&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.9217857018732858, 0.8083104099679224], "h2h": [], "margin_distribution": {"-1": 0.10573828316463321, "-10": 2.4622237678126514e-09, "-11": 1.788468858813606e-10, "-12": 1.1929193053235952e-11, "-13": 7.354954986841677e-13, "-14": 4.2149285576411883e-14, "-15": 2.2477527813557365e-15, "-16": 1.0350598946601563e-16, "-2": 0.034713991768474756, "-3": 0.00834711771532222, "-4": 0.0015705849872283393, "-5": 0.00024181790568857597, "-6": 3.1445059880619345e-05, "-7": 3.535030567861391e-06, "-8": 3.4975557778598757e-07, "-9": 3.088657867073091e-08, "0": 0.21334766207833275, "1": 0.25139639205498426, "10": 1.4210042554466967e-05, "11": 2.454008302524457e-06, "12": 3.8916385613151964e-07, "13": 5.704639913095361e-08, "14": 7.77258035832901e-09, "15": 9.854857132733175e-10, "16": 1.0789319557123792e-10, "2": 0.1962267125342893, "3": 0.11218037720041178, "4": 0.0501843825992185, "5": 0.018370559570324647, "6": 0.005679539726669601, "7": 0.0015180311208566894, "8": 0.0003570910263911787, "9": 7.497403371800261e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.849174+00:00", "p_over_1_5": 0.7567491615939266, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **47.0%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 41.7%; Under 3.5 goals: 78.9%; Double Chance 1X: 76.4%; Double Chance X2: 53.0%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 47.0% | 2.13 |
| Draw | 29.4% | 3.40 |
| Erzurum BB win | 23.6% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 69.3% |
| Under 1.5 | 30.7% |
| Over 2.5 | 41.7% |
| Under 2.5 | 58.3% |
| Over 3.5 | 21.1% |
| Under 3.5 | 78.9% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.82% |
| 2 | 1-0 | 12.30% |
| 3 | 0-0 | 10.75% |
| 4 | 2-0 | 9.58% |
| 5 | 2-1 | 8.93% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4174 |
| Dc lambda away | 0.9324 |
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
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.30 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.25 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.74 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.15 |
| Fair Under 4.5 odds | 1.10 |
| Score matrix json | [[0.10754403448975394,0.07677409368278666,0.04146297877324985,0.012886985995292548,0.0030040245471342694,0.0005602031992946477,8.705755106632388e-05,1.1596328730934465e-05,1.351582758648553e-06,1.4002714869599948e-07,1.3056427378804002e-08,1.1067353560654239e-09,8.599528697701658e-11,6.1679864324706775e-12,4.107972105968282e-13],[0.12303658580913038,0.1382241514380875,0.05877147576403627,0.018266588834240847,0.004258038401726576,0.0007940570051740256,0.00012339925649219763,1.643715365191294e-05,1.9157936958029293e-06,1.9848072713008804e-07,1.85067626099584e-08,1.5687360648136797e-09,1.2189355598473657e-10,8.74277912137672e-12,5.82282291838167e-13],[0.09581830167293892,0.08934301019505093,0.041652655762773286,0.012945938940303697,0.0030177667902005715,0.0005627659108871916,8.745580547761082e-05,1.1649377421315263e-05,1.3577657237016484e-06,1.4066771839943195e-07,1.3116155452194153e-08,1.1117982395520553e-09,8.638868194355304e-11,6.1962025696741924e-12,4.126764479433958e-13],[0.04527237840547511,0.04221292273829659,0.01968011079680648,0.006116717122790847,0.0014258390900286748,0.0002658965023023599,4.1321253353587844e-05,5.5041157440481935e-06,6.415192354297905e-07,6.646289973445076e-08,6.197141281877577e-09,5.253041405737732e-10,4.0817057186511594e-11,2.927591310987419e-12,1.9498200222846558e-13],[0.016042772184726897,0.014958619948716239,0.006973866741782839,0.0021675269286820656,0.0005052619831133495,9.42233909813006e-05,1.4642646957969898e-05,1.9504447981344594e-06,2.2732949556888433e-07,2.355186974332213e-08,2.1960261263787483e-09,1.8614738062667409e-10,1.4463979423157135e-11,1.0374246307871711e-12,6.909404701156341e-14],[0.004547948191560824,0.004240603042956432,0.0019770139643740985,0.0006144698722857793,0.00014323617488955272,2.671128753072357e-05,4.1510282004479165e-06,5.529294931246221e-07,6.444539362375431e-08,6.6766941631815856e-09,6.225490791169375e-10,5.277072025562012e-11,4.100377933618353e-12,2.940983901747957e-13,1.9587396899709062e-14],[0.0010744107748832455,0.0010018033208490508,0.00046705129784892896,0.00014516283471523,3.383822400175163e-05,6.31029508807237e-06,9.806420912360572e-07,1.3062448826180308e-07,1.522462930194257e-08,1.577307358697169e-09,1.4707147274413585e-10,1.2466595496007538e-11,9.686764332865282e-13,6.947802964553436e-14,4.627341692241139e-15],[0.00021755968020805086,0.00020285724530170253,9.457419208385179e-05,2.9394325370733086e-05,6.851972601847254e-06,1.2777848225960375e-06,1.9857226375178064e-07,2.645042525440642e-08,3.0828669626630325e-09,3.1939225905962454e-10,2.978080946872327e-11,2.5243869410089084e-12,1.9614931270006455e-13,1.4068751230469113e-14,9.370000769833699e-16],[3.8547349499730476e-05,3.594236361130632e-05,1.6756709848188e-05,5.208103506545388e-06,1.2140364537831753e-06,2.263986511423354e-07,3.518314811123397e-08,4.686501587624468e-09,5.462241448291432e-10,5.659010449779199e-11,5.2765809817240105e-12,4.4727233278965343e-13,3.4753848247757776e-14,2.492709449595834e-15,1.6601821355047083e-16],[6.070970307379748e-06,5.660701062282186e-06,2.6390786722816948e-06,8.202442491206425e-07,1.9120326970978372e-07,3.565639418932175e-08,5.541129293596144e-09,7.380951570783129e-10,8.60269410859185e-11,8.912593175829492e-12,8.310290300181372e-13,7.044263968648338e-14,5.47351720721536e-15,3.9258639698501276e-16,2.614684687869877e-17],[8.605264137813078e-07,8.023730207825952e-07,3.7407478385864026e-07,1.1626507895492771e-07,2.7102004400616876e-08,5.054096374480986e-09,7.85424384883024e-10,1.0462090018425486e-10,1.2193842393077397e-11,1.2633107155482864e-12,1.1779376190991712e-13,9.984853991628432e-15,7.758407461439572e-16,5.564694722459397e-17,3.7061707168728906e-18],[1.1088622970130747e-07,1.0339266484298989e-07,4.820275327301888e-08,1.4981755405492006e-08,3.49232636814376e-09,6.512637875351381e-10,1.0120868733412369e-10,1.3481302820690754e-11,1.5712814701396814e-12,1.6278845128397298e-13,1.5178739352263118e-14,1.2866343153658313e-15,9.997375305485519e-17,7.170587762679662e-18,4.775719732036812e-19],[1.309792404829226e-08,1.2212781288640489e-08,5.693727733274423e-09,1.7696507036068212e-09,4.125149321517239e-10,7.692752876092968e-11,1.1954809026337384e-11,1.5924166679043798e-12,1.8560037084691211e-13,1.9228634399420487e-14,1.7929185230690825e-15,1.5197773958031386e-16,1.1808938114881004e-17,8.469925810461993e-19,5.641098492990901e-20],[1.4281216800342158e-09,1.3316108466896883e-09,6.208110526615444e-10,1.9295245006694153e-10,4.497823592285462e-11,8.387731613794433e-12,1.3034830472548937e-12,1.7362787863918037e-13,2.0236788093409716e-14,2.0965787831732396e-15,1.954894381651058e-16,1.6570771366286772e-17,1.2875781290121919e-18,9.235115911196069e-20,6.150726655113741e-21],[1.4459166981092045e-10,1.34820329775109e-10,6.285466287386477e-11,1.9535672162486113e-11,4.553868433031045e-12,8.492246402528717e-13,1.319725013685784e-13,1.7579135762132998e-14,2.048894728610072e-15,2.1227030678639617e-16,1.9792532169957758e-17,1.6777250394020966e-18,1.3036219132352444e-19,9.350189477308737e-21,6.227367387855395e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.15001585566112352, "-10": 1.4714548810919234e-08, "-11": 1.2350200966220632e-09, "-12": 9.51507425463367e-11, "-13": 6.750268724308845e-12, "-14": 4.107972105968282e-13, "-2": 0.0630284420258141, "-3": 0.01775112805899263, "-4": 0.003891275629350696, "-5": 0.0006959175395276764, "-6": 0.00010492118312143076, "-7": 1.3659177604592294e-05, "-8": 1.563719708076564e-06, "-9": 1.5968758361472415e-07, "0": 0.29407053973182196, "1": 0.2343769835457184, "10": 9.698103126760722e-07, "11": 1.23739357714772e-07, "12": 1.4492389557855813e-08, "13": 1.5629420098093248e-09, "14": 1.4459166981092045e-10, "2": 0.1456547129677302, "3": 0.06236025917187456, "4": 0.02078107134284437, "5": 0.00564973016818791, "6": 0.0012948727396809307, "7": 0.0002562609581455529, "8": 4.459752813591306e-05, "9": 6.923361559599531e-06} |
| Raw goal margin distribution | {"-1": 0.15001585566112352, "-10": 1.4714548810919234e-08, "-11": 1.2350200966220632e-09, "-12": 9.51507425463367e-11, "-13": 6.750268724308845e-12, "-14": 4.107972105968282e-13, "-2": 0.0630284420258141, "-3": 0.01775112805899263, "-4": 0.003891275629350696, "-5": 0.0006959175395276764, "-6": 0.00010492118312143076, "-7": 1.3659177604592294e-05, "-8": 1.563719708076564e-06, "-9": 1.5968758361472415e-07, "0": 0.29407053973182196, "1": 0.2343769835457184, "10": 9.698103126760722e-07, "11": 1.23739357714772e-07, "12": 1.4492389557855813e-08, "13": 1.5629420098093248e-09, "14": 1.4459166981092045e-10, "2": 0.1456547129677302, "3": 0.06236025917187456, "4": 0.02078107134284437, "5": 0.00564973016818791, "6": 0.0012948727396809307, "7": 0.0002562609581455529, "8": 4.459752813591306e-05, "9": 6.923361559599531e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 76.4% |
| P draw away | 53.0% |
| P home away | 70.6% |
| Raw p home draw | 76.4% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4171 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2697 |
| Research p away | 0.2477 |
| Research p over 1 5 | 0.6805 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4174446096948812, 0.9324211412138111], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.469506+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.470918+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.553904+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4174446096948812, 0.9324211412138111], "h2h": [], "margin_distribution": {"-1": 0.16217792384887098, "-10": 1.4714548810919232e-08, "-11": 1.235020096622063e-09, "-12": 9.515074254633668e-11, "-13": 6.750268724308844e-12, "-14": 4.1079721059682814e-13, "-2": 0.06302844202581409, "-3": 0.01775112805899263, "-4": 0.0038912756293506957, "-5": 0.0006959175395276764, "-6": 0.00010492118312143073, "-7": 1.3659177604592292e-05, "-8": 1.5637197080765636e-06, "-9": 1.5968758361472412e-07, "0": 0.269746403356327, "1": 0.24653905173346585, "10": 9.698103126760722e-07, "11": 1.2373935771477197e-07, "12": 1.4492389557855811e-08, "13": 1.5629420098093246e-09, "14": 1.4459166981092043e-10, "2": 0.1456547129677302, "3": 0.06236025917187455, "4": 0.020781071342844362, "5": 0.005649730168187908, "6": 0.0012948727396809303, "7": 0.0002562609581455529, "8": 4.459752813591306e-05, "9": 6.92336155959953e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.554276+00:00", "p_over_1_5": 0.6804832178305815, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **46.8%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 7.7%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 78.2%; Under 3.5 goals: 40.7%; Double Chance 1X: 53.2%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 78.7%; Under 4.5 goals: 60.1%; BTTS Yes (both teams score): 76.5%; BTTS No (at least one team does not score): 23.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 31.9% | 3.13 |
| Draw | 21.3% | 4.70 |
| Fenerbahce win | 46.8% | 2.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 92.5% |
| Under 1.5 | 7.5% |
| Over 2.5 | 78.2% |
| Under 2.5 | 21.8% |
| Over 3.5 | 59.3% |
| Under 3.5 | 40.7% |
| Over 4.5 | 39.9% |
| Under 4.5 | 60.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 7.66% |
| 2 | 1-1 | 7.41% |
| 3 | 2-2 | 7.18% |
| 4 | 2-1 | 6.33% |
| 5 | 1-3 | 5.79% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | 6692a3ca274d09ffbfabd943320d62f5 |
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
| P btts yes | 76.5% |
| P btts no | 23.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.56 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.28 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.58 |
| Fair Over 3.5 odds | 1.69 |
| Fair Under 3.5 odds | 2.46 |
| Fair Over 4.5 odds | 2.51 |
| Fair Under 4.5 odds | 1.66 |
| Score matrix json | [[0.022442698489638417,0.029555732381000777,0.04088108713325515,0.03088203583475688,0.01749647950023711,0.007930223163789751,0.0029952901585456656,0.0009697183203238264,0.00027470107222423947,6.917076616727462e-05,1.5675713851731465e-05,3.22953044494818e-06,6.099059609473927e-07,1.0632227645859393e-07,1.721079659783166e-08,2.6002461018048183e-09,3.6829787436322396e-10,4.9097008586115304e-11],[0.0233105005087735,0.07413172043194108,0.0766089256548038,0.057871249353576,0.03278744747871717,0.014860805310790617,0.005613010249033442,0.0018171991969205244,0.0005147748138576954,0.00012962223987639387,2.937543204609129e-05,6.051963758950568e-06,1.1429304770281452e-06,1.9924214212102226e-07,3.225209331458037e-08,4.872719251521951e-09,6.901701117669834e-10,9.20051139635014e-11],[0.027952897085685727,0.06334780432855985,0.07178047235941917,0.054223781095002706,0.030720943380497447,0.013924168962458575,0.005259237400735136,0.001702666048521112,0.00048232995021932465,0.00012145250082919106,2.752397804834942e-05,5.670524858643777e-06,1.0708946616054284e-06,1.8668444901305979e-07,3.021933114076345e-08,4.5656049417154155e-09,6.466705570864603e-10,8.620628057806742e-11],[0.017460734411599517,0.03957010908559368,0.04483756227360045,0.033870801927625205,0.019189790296024096,0.008697710845872494,0.003285174598550362,0.0010635677430408082,0.00030128666569778715,7.586511888562096e-05,1.719281079094399e-05,3.5420846800832763e-06,6.689327124760679e-07,1.1661215554870149e-07,1.887645897767255e-08,2.8518981439101717e-09,4.0394177442415873e-10,5.384862131361221e-11],[0.00818011578346933,0.018538056089418296,0.02100578602254617,0.015868008464917097,0.008990154868726017,0.004074758832773308,0.001539059466319011,0.0004982669730007068,0.00014114869119056413,3.5541772859151775e-05,8.0545972235723e-06,1.6594183334399538e-06,3.133858468043194e-07,5.4631203456975906e-08,8.843363422141731e-09,1.3360753602866013e-09,1.8924120868447333e-10,2.5227344207980003e-11],[0.0030658180877666434,0.0069478610297697705,0.007872739266823024,0.0059471563308293885,0.0033694118931742027,0.0015271751236148184,0.0005768226850192714,0.00018674502156183667,5.290098844213287e-05,1.3320668433945721e-05,3.0187751018885714e-06,6.219318743767343e-07,1.1745359393620508e-07,2.047517860973615e-08,3.3143960616162947e-09,5.007464581936201e-10,7.092553894018553e-11,9.45493318510681e-12],[0.0009575292897311872,0.002169985382868165,0.0024588472709714364,0.0018574410530429505,0.0010523489928370734,0.00047697380260264814,0.0001801557039836278,5.8324996049325694e-05,1.652226076008748e-05,4.160367581884898e-06,9.428366251421155e-07,1.9424439705323722e-07,3.668360390555243e-08,6.394894501252661e-09,1.0351662153181405e-09,1.5639525461826445e-10,2.2151764710433394e-11,2.953004776544413e-12],[0.00025633680270993267,0.0005809191644966525,0.0006582493658964806,0.0004972490198110465,0.0002817206523620843,0.00012768898126331552,4.8228850693522664e-05,1.561397981836236e-05,4.423116391530536e-06,1.1137573915235752e-06,2.524034810826544e-07,5.200048522685285e-08,9.820438745708519e-09,1.7119547440461398e-09,2.7712071134919277e-10,4.1868024255536244e-11,5.930171119725559e-12,7.905385359220299e-13],[6.004514690798443e-05,0.00013607635035276766,0.00015419042236423374,0.00011647718988752377,6.599114048105075e-05,2.9910272568869656e-05,1.1297279183016053e-05,3.6574682296899206e-06,1.0360848333631568e-06,2.608900691858995e-07,5.912379315600863e-08,1.218075883651437e-08,2.3003707659340383e-09,4.0101371718516876e-10,6.491363568670532e-11,9.807298993330685e-12,1.3891021199805667e-12,1.8517825776104174e-13],[1.2502369726376598e-05,2.833329470795303e-05,3.2104937166994876e-05,2.425243283849063e-05,1.37404216567858e-05,6.2278020044777825e-06,2.3522760542931213e-06,7.61543978568882e-07,2.1572960216831437e-07,5.4321527564925646e-08,1.2310528989045434e-08,2.5362307923953327e-09,4.789743602014759e-10,8.349753503444123e-11,1.3516067749525083e-11,2.0420381054215846e-12,2.892335048876569e-13,3.855710516226506e-14],[2.342875838293759e-06,5.309504761363193e-06,6.016289969396948e-06,4.544773523795746e-06,2.5748800117257117e-06,1.1670560990678009e-06,4.408036918771832e-07,1.4270918443748721e-07,4.0426549813076945e-08,1.0179557733168826e-08,2.3069259313456867e-09,4.752758056181542e-10,8.975718045761843e-11,1.5646982265815164e-11,2.5328373142170153e-12,3.826667937978147e-13,5.420077993667704e-14,7.22539103036132e-15],[3.991292206483392e-07,9.045201895866863e-07,1.0249271802762698e-06,7.742415901547923e-07,4.386531439461673e-07,1.9881812926674504e-07,7.509473234654231e-08,2.4311747397325188e-08,6.887013411750222e-09,1.7341759551130845e-09,3.9300484217806813e-10,8.096735592592703e-11,1.5290914225199218e-11,2.665599147499573e-12,4.3149080575635505e-13,6.519060749192385e-14,9.233572987979059e-15,1.2309080334909425e-15],[6.232886430596605e-08,1.4125178824836774e-07,1.6005479889236427e-07,1.2090720627871984e-07,6.850100386535008e-08,3.1047860090282095e-08,1.1726952426378184e-08,3.796573956943911e-09,1.0754905985511788e-09,2.7081258950004736e-10,6.137246839485777e-11,1.2644033760600985e-11,2.3878615459636445e-12,4.1626560763633975e-13,6.738251796641968e-14,1.0180303315771582e-14,1.441934311128906e-15,1.9222120512238095e-16],[8.984683790518508e-09,2.036139542069893e-08,2.3071842768443913e-08,1.742873111046419e-08,9.874395529525883e-09,4.475538073565424e-09,1.6904360531943227e-09,5.472747958796612e-10,1.550315901830558e-10,3.903753919219923e-11,8.846819657495466e-12,1.8226330038355363e-12,3.4420939904673433e-13,6.000454041840401e-14,9.713166181968501e-15,1.467487129795491e-15,2.0785432201356963e-16,2.770861887325738e-17],[1.202629068854816e-09,2.725438823035831e-09,3.0882409923718806e-09,2.3328921924684557e-09,1.3217198710665533e-09,5.990652883873661e-10,2.2627034896398683e-10,7.325450661614029e-11,2.075148121981598e-11,5.225301246399079e-12,1.18417550746171e-12,2.439653396127244e-13,4.607354456964817e-14,8.031802370897e-15,1.3001387999186042e-15,1.9642791239072963e-16,2.7821975215691196e-17,3.708888514247358e-18],[1.502440816962502e-10,3.4048823846928056e-10,3.8581300250579887e-10,2.9144750798975443e-10,1.6512205918752296e-10,7.484104322837123e-11,2.8267885481561004e-11,9.151663103515552e-12,2.5924762010593143e-12,6.52795286329701e-13,1.479386839162243e-13,3.047851525053448e-14,5.755953829512595e-15,1.0034106133242521e-15,1.624259425705077e-16,2.4539679009055644e-17,3.475790853149572e-18,4.633503075619863e-19],[1.7596825469722096e-11,3.98785232615694e-11,4.518703161146505e-11,3.413479502007661e-11,1.933935782308077e-11,8.765501847347937e-12,3.3107796433723676e-12,1.0718573175869575e-12,3.0363493010445477e-13,7.645642072094815e-14,1.732681362023429e-14,3.569692112892751e-15,6.741464542642254e-16,1.1752104467469582e-16,1.9023584362855222e-17,2.874126180080559e-18,4.070901450599767e-19,5.426832392635817e-20],[1.9397347263415736e-12,4.395892687506891e-12,4.981060620727827e-12,3.7627495590566705e-12,2.131817697409247e-12,9.662395274856657e-13,3.6495413656083576e-13,1.1815306483457355e-13,3.347031082778642e-14,8.42795051751722e-15,1.909970757728235e-15,3.9349459739996196e-16,7.431256792461731e-17,1.2954589555012904e-17,2.0970093311212218e-18,3.168209157374657e-19,4.487439467323057e-20,5.9821103892537876e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1842928327486559, "-10": 2.2924551480019744e-05, "-11": 4.57943178387106e-06, "-12": 8.424180284949581e-07, "-13": 1.4356914383352184e-07, "-14": 2.2784035027753682e-08, "-15": 3.376622494149869e-09, "-16": 4.603029883267254e-10, "-17": 4.9097008586115304e-11, "-2": 0.13991449297174915, "-3": 0.08143442028281085, "-4": 0.038835556538006355, "-5": 0.01558595115476081, "-6": 0.00537939941623884, "-7": 0.0016249219998480033, "-8": 0.0004357243143163789, "-9": 0.00010494376389460836, "0": 0.2129398856814701, "1": 0.15126237390571215, "10": 3.426279547730277e-06, "11": 5.659599963727909e-07, "12": 8.609025382437717e-08, "13": 1.2132202228777624e-08, "14": 1.5920670884946183e-09, "15": 1.9510366557854743e-10, "16": 2.1992718157228987e-11, "17": 1.9397347263415736e-12, "2": 0.0956680875458849, "3": 0.04604310389797613, "4": 0.018156758277689866, "5": 0.006025516555889445, "6": 0.001719677303220776, "7": 0.0004295343311189298, "8": 9.524218545150307e-05, "9": 1.8968211708325806e-05} |
| Raw goal margin distribution | {"-1": 0.1842928327486559, "-10": 2.2924551480019744e-05, "-11": 4.57943178387106e-06, "-12": 8.424180284949581e-07, "-13": 1.4356914383352184e-07, "-14": 2.2784035027753682e-08, "-15": 3.376622494149869e-09, "-16": 4.603029883267254e-10, "-17": 4.9097008586115304e-11, "-2": 0.13991449297174915, "-3": 0.08143442028281085, "-4": 0.038835556538006355, "-5": 0.01558595115476081, "-6": 0.00537939941623884, "-7": 0.0016249219998480033, "-8": 0.0004357243143163789, "-9": 0.00010494376389460836, "0": 0.2129398856814701, "1": 0.15126237390571215, "10": 3.426279547730277e-06, "11": 5.659599963727909e-07, "12": 8.609025382437717e-08, "13": 1.2132202228777624e-08, "14": 1.5920670884946183e-09, "15": 1.9510366557854743e-10, "16": 2.1992718157228987e-11, "17": 1.9397347263415736e-12, "2": 0.0956680875458849, "3": 0.04604310389797613, "4": 0.018156758277689866, "5": 0.006025516555889445, "6": 0.001719677303220776, "7": 0.0004295343311189298, "8": 9.524218545150307e-05, "9": 1.8968211708325806e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 53.2% |
| P draw away | 68.1% |
| P home away | 78.7% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7817 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |
| Research p home | 0.3259 |
| Research p draw | 0.1999 |
| Research p away | 0.4742 |
| Research p over 1 5 | 0.9182 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.873945411605394, 2.2662339482872187], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-06T12:17:19.469506+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-06T12:17:18.988893+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-06T12:17:19.562015+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-06T12:16:47.162626+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-06T12:16:47.283065+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-06T12:17:19.644655+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.873945411605394, 2.2662339482872187], "h2h": [], "margin_distribution": {"-1": 0.19081553539785345, "-10": 2.292455148001974e-05, "-11": 4.57943178387106e-06, "-12": 8.424180284949581e-07, "-13": 1.4356914383352184e-07, "-14": 2.2784035027753682e-08, "-15": 3.3766224941498688e-09, "-16": 4.6030298832672533e-10, "-17": 4.9097008586115304e-11, "-2": 0.13991449297174915, "-3": 0.08143442028281085, "-4": 0.03883555653800635, "-5": 0.01558595115476081, "-6": 0.005379399416238839, "-7": 0.0016249219998480033, "-8": 0.00043572431431637877, "-9": 0.00010494376389460834, "0": 0.19989448038307495, "1": 0.15778507655490973, "10": 3.426279547730277e-06, "11": 5.659599963727907e-07, "12": 8.609025382437715e-08, "13": 1.2132202228777622e-08, "14": 1.592067088494618e-09, "15": 1.9510366557854743e-10, "16": 2.1992718157228987e-11, "17": 1.9397347263415732e-12, "2": 0.09566808754588489, "3": 0.046043103897976126, "4": 0.018156758277689866, "5": 0.006025516555889444, "6": 0.0017196773032207757, "7": 0.00042953433111892977, "8": 9.524218545150305e-05, "9": 1.8968211708325802e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-06T12:17:19.645036+00:00", "p_over_1_5": 0.9181683659713897, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
