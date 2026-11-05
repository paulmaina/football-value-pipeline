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
| Training as of utc | 2026-11-05T16:17:19.617329+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1629, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1323, 'tuning_matches': 189, 'audit_matches': 114, 'audit_matchdays': 36, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.6639999435984515, 'audit_candidate_poisson_score': 0.6541517901162848, 'audit_gain': 0.009848153482166722, 'audit_gain_lower95': -0.0021828454332282108, 'audit_baseline_briers': [0.6216633755590796, 0.09847259899912482, 0.27967453202176307, 0.2302451960138092], 'audit_candidate_briers': [0.6176749252028129, 0.0975895815214795, 0.2767941288032132, 0.2243749218030424], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1636.364 |
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
| Dc lambda home | 1.2183 |
| Dc lambda away | 1.6439 |
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
| Score matrix json | [[0.06640017874918273,0.08467474269365999,0.07721200167472707,0.04231078110848925,0.01738915737690742,0.0057173663327748595,0.0015665066969910162,0.00036789315053038324,7.559954844671448e-05,1.380906196295195e-05,2.2701348962149766e-06,3.392707866787536e-07,4.647856447286069e-08,5.8775568713722195e-09,6.901703385577767e-10,7.564017377844543e-11],[0.06035371115741294,0.12370177808664293,0.09406784797919894,0.05154748016974783,0.021185315457929753,0.006965501934512007,0.0019084845702061494,0.0004482064472628241,9.210338647274502e-05,1.6823663592333543e-05,2.7657190550380824e-06,4.1333564851131727e-07,5.662511581480653e-08,7.160663035191187e-09,8.408386919006098e-10,9.215288055975849e-11],[0.042405543445081496,0.06971241364975467,0.05730171366826543,0.0314003032115781,0.012905098887885774,0.004243056538249031,0.0011625591392973914,0.000273026310870895,5.61050560092102e-05,1.0248185482379609e-05,1.6847461144609406e-06,2.517846585064824e-07,3.449336029851465e-08,4.361939512086966e-09,5.121994283864334e-10,5.613520548177967e-11],[0.017220976565585376,0.028310351530987484,0.023270341282786638,0.012751726350569408,0.005240786639432152,0.0017231138024742263,0.00047211760697927325,0.00011087653451217016,2.2784376198285205e-05,4.161808756451661e-06,6.841787888809148e-07,1.0225025672243727e-07,1.4007823060640704e-08,1.7713924174897739e-09,2.080052190481258e-10,2.2796619959793786e-11],[0.00524510493993277,0.008622668064200353,0.007087599332791774,0.003883876307439186,0.001596220503926158,0.0005248199881698571,0.00014379593301026304,3.377038791485294e-05,6.939585783406476e-06,1.2675891860362713e-06,2.0838478768550156e-07,3.114302633196919e-08,4.26645385952729e-09,5.395245202355479e-10,6.335350366490886e-11,6.943314945555176e-12],[0.001278028605457172,0.002101009716223394,0.0017269730148512829,0.000946349992575797,0.00038893701613166204,0.00012787827227063437,3.503749073471826e-05,8.228533512071245e-06,1.6909078546159794e-06,3.088623122463766e-07,5.0775289084607725e-08,7.588347415080075e-09,1.0395693010498512e-09,1.3146119631601217e-10,1.5436791230477676e-11,1.6918165067697505e-12],[0.00025950499482725603,0.0004266121377975976,0.0003506636090711595,0.00019215731860736172,7.897405263731998e-05,2.596581190938098e-05,7.11439776312408e-06,1.6708120126326145e-06,3.433405419814689e-07,6.271480340861293e-08,1.0309973560051988e-08,1.5408215812144174e-09,2.1108559302944034e-10,2.6693328243438016e-11,3.1344559983315505e-12,3.4352504471595957e-13],[4.516521464794015e-05,7.424916344238849e-05,6.1030798977349135e-05,3.344377454796708e-05,1.374493790131722e-05,4.519186496490731e-06,1.2382162519693261e-06,2.907943380324602e-07,5.975626513954261e-08,1.0915117681796038e-08,1.7943861510808495e-09,2.6817031978922993e-10,3.6738121840809655e-11,4.645806145601691e-12,5.455323820006063e-13,5.978837668179618e-14],[6.8781317238550554e-06,1.1307275533253393e-05,9.294273875381008e-06,5.093094065353229e-06,2.0931926075940696e-06,6.882190254120251e-07,1.8856579228172772e-07,4.428456229266952e-08,9.100177341327593e-09,1.6622442244984785e-09,2.7326393568148903e-10,4.083919003411136e-11,5.594784465828939e-12,7.075017108194154e-13,8.30781744817793e-14,9.105067552061623e-15],[9.310743801292318e-07,1.530635786104667e-06,1.2581411107988322e-06,6.894385845202748e-07,2.833499106810372e-07,9.316237725663955e-08,2.552564929127067e-08,5.994683300835621e-09,1.2318667797181638e-09,2.250135753551513e-10,3.699101147538277e-11,5.528292430648341e-12,7.573510784057367e-13,9.577262304484472e-14,1.124607130445251e-14,1.2325287545262495e-15],[1.1343335407400974e-07,1.8647828228230486e-07,1.5328009141063807e-07,8.399471915371318e-08,3.4520690753686034e-08,1.1350028688644704e-08,3.1098052699332307e-09,7.3033588716173e-10,1.5007907378611967e-10,2.741353978741961e-11,4.506637269581459e-12,6.735152057597822e-13,9.226853930102447e-14,1.1668036509537135e-14,1.3701156593337469e-15,1.5015972257680301e-16],[1.2563321852188686e-08,2.0653419780105745e-08,1.697655101222096e-08,9.30284305905118e-09,3.823342367320525e-09,1.257073500215667e-09,3.4442677661027955e-10,8.088842021395261e-11,1.662202200265721e-11,3.036189190283708e-12,4.991330367598933e-13,7.459524027458853e-14,1.0219210791508204e-14,1.2922944864767107e-15,1.5174728935285467e-16,1.6630954267092268e-17],[1.2754975742890933e-09,2.096848838248135e-09,1.7235528859837794e-09,9.444758237841966e-10,3.8816675816869833e-10,1.2762501980707056e-10,3.496810184880274e-11,8.212237574173062e-12,1.6875591498498201e-12,3.082506356879628e-13,5.06747327757015e-14,7.57331931340867e-15,1.037510519038948e-15,1.3120084816429793e-16,1.540621992747817e-17,1.6884660024922877e-18],[1.1953433833882647e-10,1.9650796953982974e-10,1.6152422236700416e-10,8.851235388353134e-11,3.6377377376576784e-11,1.1960487111565536e-11,3.2770653599957006e-12,7.696168181716475e-13,1.5815103881899692e-13,2.8887970092785116e-14,4.749025615526111e-15,7.097400507888225e-16,9.72311793552531e-17,1.2295598902689575e-17,1.4438069836079138e-18,1.582360252844934e-19],[1.0402100453724187e-11,1.7100489010250618e-11,1.405613826220101e-11,7.702509666153527e-12,3.1656270405043527e-12,1.0408238347153389e-12,2.851763229028783e-13,6.69734869891919e-14,1.376259755579946e-14,2.513884888520987e-15,4.1326904215578156e-16,6.176289932194823e-17,8.461238075543819e-18,1.0699858860801845e-18,1.2564276916568467e-19,1.376999323610009e-20],[8.448627872364933e-13,1.3889086028903714e-12,1.1416452093320214e-12,6.256009364851543e-13,2.5711350286318184e-13,8.453613094122237e-14,2.3162135771849798e-14,5.439613580003215e-15,1.1178037149645072e-15,2.0417874285641438e-16,3.35658780058487e-17,5.016407551636945e-18,6.872251633963156e-19,8.690468449511698e-20,1.020475630144749e-20,1.1184043950963803e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21594527027097063, "-10": 2.7198003427624702e-06, "-11": 4.0047279053964077e-07, "-12": 5.417422355639811e-08, "-13": 6.7745307687546085e-09, "-14": 7.823232191175351e-10, "-15": 7.564017377844543e-11, "-2": 0.1435400735359027, "-3": 0.0682467965582147, "-4": 0.025635354017160467, "-5": 0.007922981532803913, "-6": 0.002075196197970312, "-7": 0.0004709611111179875, "-8": 9.421460951953162e-05, "-9": 1.684112880439366e-05, "0": 0.2618869101527317, "1": 0.1576365289860359, "10": 1.3590208925715425e-07, "11": 1.4829654535972841e-08, "12": 1.4866872830276093e-09, "13": 1.3777647255840913e-10, "14": 1.1791009056614558e-11, "15": 8.448627872364933e-13, "2": 0.0788335322542126, "3": 0.027777234393091366, "4": 0.007732411587170697, "5": 0.0017710596890365543, "6": 0.0003437736842454851, "7": 5.781858032368987e-05, "8": 8.57175086229063e-06, "9": 1.135511130610889e-06} |
| Raw goal margin distribution | {"-1": 0.21594527027097063, "-10": 2.7198003427624702e-06, "-11": 4.0047279053964077e-07, "-12": 5.417422355639811e-08, "-13": 6.7745307687546085e-09, "-14": 7.823232191175351e-10, "-15": 7.564017377844543e-11, "-2": 0.1435400735359027, "-3": 0.0682467965582147, "-4": 0.025635354017160467, "-5": 0.007922981532803913, "-6": 0.002075196197970312, "-7": 0.0004709611111179875, "-8": 9.421460951953162e-05, "-9": 1.684112880439366e-05, "0": 0.2618869101527317, "1": 0.1576365289860359, "10": 1.3590208925715425e-07, "11": 1.4829654535972841e-08, "12": 1.4866872830276093e-09, "13": 1.3777647255840913e-10, "14": 1.1791009056614558e-11, "15": 8.448627872364933e-13, "2": 0.0788335322542126, "3": 0.027777234393091366, "4": 0.007732411587170697, "5": 0.0017710596890365543, "6": 0.0003437736842454851, "7": 5.781858032368987e-05, "8": 8.57175086229063e-06, "9": 1.135511130610889e-06} |
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
| Team research json | {"base_rates": [1.2183060397201062, 1.643945767138622], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:17:46.692206+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:17:46.740704+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ned.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:17:46.917808+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Willem+II+Tilburg%22+%22PEC+Zwolle%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:17:31.417352+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:17:31.500974+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:17:47.001756+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Willem+II+Tilburg_vs_PEC+Zwolle&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.2183060397201062, 1.643945767138622], "h2h": [], "margin_distribution": {"-1": 0.22520550185461766, "-10": 2.7198003427624702e-06, "-11": 4.0047279053964077e-07, "-12": 5.417422355639811e-08, "-13": 6.7745307687546085e-09, "-14": 7.823232191175351e-10, "-15": 7.564017377844543e-11, "-2": 0.1435400735359027, "-3": 0.0682467965582147, "-4": 0.025635354017160467, "-5": 0.007922981532803913, "-6": 0.002075196197970312, "-7": 0.0004709611111179875, "-8": 9.421460951953162e-05, "-9": 1.684112880439366e-05, "0": 0.2433664469854376, "1": 0.1668967605696829, "10": 1.3590208925715425e-07, "11": 1.4829654535972841e-08, "12": 1.4866872830276093e-09, "13": 1.3777647255840913e-10, "14": 1.1791009056614558e-11, "15": 8.448627872364933e-13, "2": 0.0788335322542126, "3": 0.027777234393091366, "4": 0.007732411587170697, "5": 0.0017710596890365543, "6": 0.0003437736842454851, "7": 5.781858032368987e-05, "8": 8.57175086229063e-06, "9": 1.135511130610889e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:17:47.002185+00:00", "p_over_1_5": 0.7793111358160971, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
