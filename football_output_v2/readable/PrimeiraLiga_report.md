# Primeira Liga — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,620 |
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
| Training sha256 | b3df8a6ba2e5ca811847821ea9d38323a7d64bb77cbc57ee92f21ada8c933425 |
| Training as of utc | 2026-11-05T16:49:22.844676+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1620, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1314, 'tuning_matches': 198, 'audit_matches': 105, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8711311490649736, 'audit_candidate_poisson_score': 0.864686593204381, 'audit_gain': 0.00644455586059256, 'audit_gain_lower95': -0.0029289421498967876, 'audit_baseline_briers': [0.5561732722331245, 0.18693068045547456, 0.2241322810942478, 0.24642823314838475], 'audit_candidate_briers': [0.5573866098793224, 0.18683238764085344, 0.22226394985720094, 0.24657985484456124], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1468.976 |
| Base scoring parameter | 0.087 |
| Home-advantage parameter | 0.174 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1620, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 35.00 |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'None': 6} |
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

## 2026-11-06 — Famalicão vs Arouca

The model's most likely 1X2 outcome is **Famalicão win** at **46.2%**. Expected goals are 1.47 for Famalicão and 1.00 for Arouca (2.47 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 44.5%; Under 3.5 goals: 76.2%; Double Chance 1X: 73.3%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.0%; BTTS No (at least one team does not score): 51.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Famalicão win | 46.2% | 2.17 |
| Draw | 27.1% | 3.69 |
| Arouca win | 26.7% | 3.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Famalicão expected goals | 1.47 |
| Arouca expected goals | 1.00 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.2% |
| Under 1.5 | 29.8% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.8% |
| Under 3.5 | 76.2% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.80% |
| 2 | 1-0 | 12.26% |
| 3 | 0-1 | 9.13% |
| 4 | 2-1 | 8.69% |
| 5 | 2-0 | 8.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Famalicão win | 46.2% | 45.1% | 2.14 | -1.2% |
| Draw | 27.1% | 28.0% | 3.38 | -8.4% |
| Arouca win | 26.7% | 26.9% | 3.51 | -6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:45:00+00:00 |
| Fixture id | d98d64a216d4db8db11c9b5017f76ca6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Famalicao |
| Matched away-team name | Arouca |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4703 |
| Dc lambda away | 0.9993 |
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
| P btts yes | 49.0% |
| P btts no | 51.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.94 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.36 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.20 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.57 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.0837597626331014,0.09131695552256715,0.04275909676847985,0.014335623081654576,0.003604673122283315,0.0007251121625897018,0.00012155231799087113,1.7465238114160936e-05,2.1958053042340356e-06,2.4539212768873243e-07,2.4681408043755405e-08,2.256766116856404e-09,1.8915360051847182e-10,1.463459020690266e-11,1.051385143827195e-12,7.049850101917254e-14],[0.12261661452189596,0.12796398935302894,0.06327908528091833,0.02121525439255371,0.005334547152617728,0.0010730917592386767,0.0001798849853607675,2.584676421163856e-05,3.2495670303621848e-06,3.631552242405646e-07,3.652595687206485e-08,3.3397827915044675e-09,2.79927962071091e-10,2.1657695127847966e-11,1.5559423656576203e-12,1.0433056344299681e-13],[0.08638570384450726,0.08688627568516726,0.05012393408126694,0.01569820217709092,0.003947291801243282,0.0007940329670056427,0.00013310568030744485,1.9125282342139276e-05,2.4045132472481327e-06,2.6871627491754767e-07,2.7027338210501537e-08,2.471268292074217e-09,2.0713236156882442e-10,1.602558567132174e-11,1.1513176971645227e-12,7.719927594895225e-14],[0.042613998998674886,0.04286093068953714,0.021554646627161556,0.008289791670510352,0.0019471959060313223,0.00039169583108102204,6.56609262285944e-05,9.434486567873452e-06,1.1861444724114222e-06,1.3255752469037882e-07,1.3332564442749426e-08,1.2190746829297697e-09,1.0217822921689707e-10,7.905408665537031e-12,5.679441042980541e-13,3.8082341424324155e-14],[0.015766088859399823,0.015857447264426706,0.007974667528089984,0.00267362588370859,0.0007711957181740288,0.0001449174314495077,2.4292862013318826e-05,3.490518540081916e-06,4.3884309362061805e-07,4.904289112400799e-08,4.932707576554793e-09,4.510264286135896e-10,3.780332940308691e-11,2.9247988552917058e-12,2.1012478119722584e-13,1.4089491551557216e-14],[0.004666439456765756,0.004693479673887865,0.0023603382893203077,0.0007913385131614004,0.00019898100366986713,4.591616170780542e-05,7.190189705744965e-06,1.0331220117600372e-06,1.2988856942661916e-07,1.4515691510801874e-08,1.459980434538723e-09,1.334945871037491e-10,1.1189011396349137e-11,8.656805694266584e-13,6.219263246372012e-14,4.170200985690577e-15],[0.0011509754362592777,0.0011576448950590785,0.0005821765004003328,0.00019518332957136044,4.907858542430685e-05,9.872595380110445e-06,1.8984713682391718e-06,2.5481913334813063e-07,3.2036963994923824e-08,3.580289538531762e-09,3.601035935732206e-10,3.292638682094499e-11,2.7597652112578204e-12,2.1351976818479994e-13,1.5339788064379135e-14,1.02857841471295e-15],[0.00024333225739959322,0.00024474227399444226,0.00012308023054585527,4.1264477672718095e-05,1.037589735197887e-05,2.0872043351704555e-06,3.498831465665547e-07,5.766986668608224e-08,6.77306093903311e-09,7.56923135029294e-10,7.613092127027671e-11,6.9610973273176845e-12,5.834528501587888e-13,4.514105649439868e-14,3.2430451077809645e-15,2.1745582023717116e-16],[4.501335338933614e-05,4.527418841362369e-05,2.2768267438145295e-05,7.633400255923225e-06,1.919408216680123e-06,3.8610608942199023e-07,6.472390421920093e-08,9.299850612074603e-09,1.341250661768308e-09,1.4002109268105102e-10,1.4083246091647944e-11,1.2877139156176589e-12,1.0793131009788121e-13,8.350517724468995e-15,5.99921839603771e-16,4.022654368766852e-17],[7.4016838083644685e-06,7.444573711705481e-06,3.7438560727483127e-06,1.2551834249793355e-06,3.1561418222195035e-07,6.348860893937982e-08,1.0642750157487378e-08,1.5292029700659487e-09,1.9225801394592487e-10,2.4647104483872343e-11,2.3157513652483755e-12,2.117427501255845e-13,1.774747647564308e-14,1.3731012506014543e-15,9.864698877403378e-17,6.6145740021675184e-18],[1.0953734206966457e-06,1.101720687258195e-06,5.54052366890879e-07,1.8575429556550495e-07,4.670766751886205e-08,9.395664088029585e-09,1.5750180563580034e-09,2.263063826595343e-10,2.8452217609498996e-11,3.1796763598279485e-12,3.6686550782147687e-13,3.1335759067506995e-14,2.6264448089351767e-15,2.0320492644315013e-16,1.459874433067868e-17,9.78889228288494e-19],[1.47367319239731e-07,1.482212560251248e-07,7.454007052244221e-08,2.4990667162019938e-08,6.283869610253758e-09,1.2640564422763997e-09,2.1189686031639646e-10,3.0446388701093334e-11,3.8278517228131e-12,4.2778140526705394e-13,4.302602335442424e-14,4.51297042419571e-15,3.53351764166163e-16,2.733840779812657e-17,1.964058809195941e-18,1.3169598483937922e-19],[1.8174045342684926e-08,1.827935692694661e-08,9.192639375613777e-09,3.081969058605552e-09,7.749569701983276e-10,1.558895093984354e-10,2.6132138164894485e-11,3.7547948325947325e-12,4.720690525849243e-13,5.275605674439699e-14,5.306175774879043e-15,4.851748197510561e-16,4.664885313458901e-17,3.3715037057280623e-18,2.4221716211014077e-19,1.6241381143853626e-20],[2.0689020259890967e-09,2.080890515394226e-09,1.0464742367361553e-09,3.50846050461253e-10,8.82197670065254e-11,1.774619330718706e-11,2.9748376089827655e-12,4.2743937796190127e-13,5.3739528040344186e-14,6.005658653515493e-15,6.04045912943656e-16,5.5231466006321865e-17,4.6292925877325696e-18,4.1086130591281006e-19,2.757358463511826e-20,1.8488908616542354e-21],[2.1869736940637481e-10,2.1996463632531199e-10,1.1061962328367271e-10,3.708687378070007e-11,9.325444478090566e-12,1.8758963665296726e-12,3.144610770945755e-13,4.518332253856938e-14,5.680642808566388e-15,6.348399936669557e-16,6.385186466154384e-17,5.838351053992282e-18,4.893485039077816e-19,3.7860314598409876e-20,3.1201835770161897e-21,1.954406553253566e-22],[2.1576647676960886e-11,2.170167602959629e-11,1.0913714436660124e-11,3.658985067713203e-12,9.200468687894303e-13,1.8507563711885234e-13,3.1024679844134944e-14,4.45777941424466e-15,5.604513158608013e-16,6.263321278978634e-17,6.2996148104512225e-18,5.760107862675222e-19,4.827904555379782e-20,3.735292615755518e-21,2.683526568581625e-22,2.0641374067147643e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17239380824232584, "-10": 2.8236442900476416e-08, "-11": 2.5533016981946663e-09, "-12": 2.1200069568490863e-10, "-13": 1.6267731848509233e-11, "-14": 1.1557157072701918e-12, "-15": 7.049850101917254e-14, "-2": 0.06833869758556772, "-3": 0.020533488192342176, "-4": 0.004820758774356451, "-5": 0.0009253591111548684, "-6": 0.0001499412219821247, "-7": 2.0997316416126467e-05, "-8": 2.5872456259352482e-06, "-9": 2.844945191021545e-07, "0": 0.2709565471252936, "1": 0.2339403756954617, "10": 1.2531476726679607e-06, "11": 1.6673115732406324e-07, "12": 2.0369214466430538e-08, "13": 2.2997803767510688e-09, "14": 2.4039904543597113e-10, "15": 2.1576647676960886e-11, "2": 0.13806387264704778, "3": 0.06103774075837242, "4": 0.021084994014128944, "5": 0.005955123208178957, "6": 0.0014197891594061264, "7": 0.00029254249896123183, "8": 5.3037763157176885e-05, "9": 8.581116661891766e-06} |
| Raw goal margin distribution | {"-1": 0.17011111583693744, "-10": 2.6441242542059313e-08, "-11": 2.3758280004985867e-09, "-12": 1.9601170574933162e-10, "-13": 1.4945090246999844e-11, "-14": 1.0550796604106112e-12, "-15": 6.401768520368676e-14, "-2": 0.06713638253056495, "-3": 0.020066849854991534, "-4": 0.004684540585618621, "-5": 0.0008939018729304652, "-6": 0.0001439669396746001, "-7": 2.0036631345635818e-05, "-8": 2.4535121033354414e-06, "-9": 2.680976008814571e-07, "0": 0.2503620508813877, "1": 0.2473664495952607, "10": 1.2574927832328847e-06, "11": 1.6624975041381622e-07, "12": 2.018135759319067e-08, "13": 2.2640670054592004e-09, "14": 2.3517889682543675e-10, "15": 2.0995945108041808e-11, "2": 0.1453458596859415, "3": 0.06392140225577275, "4": 0.021956163819163287, "5": 0.006164554094807495, "6": 0.0014608208463092083, "7": 0.0002991446613409001, "8": 5.3897313430227094e-05, "9": 8.665511538992125e-06} |
| Research history json | {"away": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 0.0, "away_xg": 1.45, "date": "2026-10-11T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.74, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 2.0, "away_xg": 2.08, "date": "2026-09-19T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-08-29T00:00:00+00:00", "home": "Arouca", "home_goals": 2.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 0.54, "date": "2026-08-23T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.99, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 0.49, "date": "2026-08-08T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.22, "source": "pipeline training history"}], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Famalicao", "away_goals": 0.0, "away_xg": 0.17, "date": "2026-11-01T00:00:00+00:00", "home": "Sp Braga", "home_goals": 3.0, "home_xg": 1.15, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.65, "date": "2026-10-25T00:00:00+00:00", "home": "Rio Ave", "home_goals": 0.0, "home_xg": 0.58, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Sp Lisbon", "away_goals": 1.0, "away_xg": 2.28, "date": "2026-09-13T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-09-05T00:00:00+00:00", "home": "Estrela", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 2.0, "away_xg": 1.61, "date": "2026-08-16T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 70.0% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 48.0% |
| P home draw | 73.3% |
| P draw away | 53.8% |
| P home away | 72.9% |
| Raw p home draw | 73.7% |
| Raw p draw away | 51.3% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0065 |
| Totals anchor target over 2 5 | 0.4452 |
| Totals anchor reference over odds | 2.14 |
| Totals anchor reference under odds | 1.74 |
| Totals anchor reference last update utc | 2026-11-05T16:49:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4414 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.6, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.24, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.02, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.6, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.51, "draw": 3.38, "home": 2.14}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.14, "under": 1.74}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.36, "under": 3.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.14 |
| Reference draw odds | 3.38 |
| Reference away odds | 3.51 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:09Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.9% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0353 |
| Raw ev home | 0.0413 |
| Raw edge prob draw | -0.0294 |
| Raw ev draw | -0.1538 |
| Raw edge prob away | -0.0059 |
| Raw ev away | -0.0767 |
| Market p home draw | 73.1% |
| Market reference home draw last update utc | 2026-11-05T16:49:13Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.0% |
| Market reference draw away last update utc | 2026-11-05T16:49:13Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market reference home away last update utc | 2026-11-05T16:49:13Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.70 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 71.6% |
| Market over 1 5 odds | 1.36 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference over 1 5 odds | 1.36 |
| Market reference over 1 5 opposite odds | 3.19 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.3% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.72 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,482.5254 |
| Elo away rating | 1,488.7246 |
| Elo rating diff | 53.8007 |
| Elo home expectancy | 0.5768 |
| Research p home | 0.4024 |
| Research p draw | 0.2768 |
| Research p away | 0.3207 |
| Research p over 1 5 | 0.6869 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4703181153436813, 0.9992840233762864], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.670883+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.672219+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Famalic%C3%A3o%22+%22Arouca%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.709143+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Famalic%C3%A3o_vs_Arouca&d=2026-11-06"}]}, "form": {"away": {"all": {"goals_against": 0.6319445048828116, "goals_for": 1.2081082699386303, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.1060493109621126, "results": "WWWDLDWLWW", "xg_against": 1.023157856687065, "xg_for": 1.2317353640143311, "xg_matches": 10}, "venue": {"goals_against": 0.792388231715419, "goals_for": 0.8583663485684871, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6443849010337144, "results": "WDDLW", "xg_against": 1.4009952478886567, "xg_for": 1.3739582889860773, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.5415943551474574, "goals_for": 1.5655575353063838, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.1025143978756544, "results": "LWLWDDDLLD", "xg_against": 1.3722444855381826, "xg_for": 0.8727767251907648, "xg_matches": 10}, "venue": {"goals_against": 1.8825279789738854, "goals_for": 0.7695192334124757, "last_match": "2026-10-12T00:00:00+00:00", "matches": 4, "points_per_game": 0.495233644025069, "results": "LDDL", "xg_against": 1.8678153299912186, "xg_for": 0.3735383586410355, "xg_matches": 4}}}, "goal_rates": [1.2733568631209002, 1.1053306349176863], "h2h": [{"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2026-03-06T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": null, "date": "2025-10-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2025-04-05T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2024-11-09T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 2.0, "away_xg": null, "date": "2024-02-23T00:00:00+00:00", "home": "Arouca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": null, "date": "2023-09-22T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": null, "date": "2023-04-03T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.1935595817138586, "-10": 7.89559514685906e-08, "-11": 7.850853820717921e-09, "-12": 7.166230865748567e-10, "-13": 6.021034365060361e-11, "-14": 4.3194822166997476e-12, "-2": 0.08830918200045784, "-3": 0.02931540436965566, "-4": 0.007589884171962072, "-5": 0.0016049529366991516, "-6": 0.00028630372035474305, "-7": 4.412064522777138e-05, "-8": 5.9808500070593594e-06, "-9": 7.233641782995323e-07, "0": 0.2768480986809188, "1": 0.22298343501219176, "10": 3.250604529105592e-07, "11": 3.7235233553389316e-08, "12": 3.915488140080678e-09, "13": 3.7898685775625793e-10, "14": 3.132150782570104e-11, "2": 0.11719840868680481, "3": 0.04481977464157343, "4": 0.013368012843117392, "5": 0.0032565063856916506, "6": 0.0006692286889059937, "7": 0.00011880845281289312, "8": 1.8553520254978868e-05, "9": 2.585105885989588e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.709373+00:00", "p_over_1_5": 0.6868898326911597, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Alverca vs Casa Pia

The model's most likely 1X2 outcome is **Alverca win** at **52.9%**. Expected goals are 1.43 for Alverca and 0.91 for Casa Pia (2.33 combined). The most likely exact score is 1-0 at 12.3%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 49.0%; Under 3.5 goals: 72.2%; Double Chance 1X: 78.6%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alverca win | 52.9% | 1.89 |
| Draw | 25.7% | 3.89 |
| Casa Pia win | 21.4% | 4.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alverca expected goals | 1.43 |
| Casa Pia expected goals | 0.91 |
| Expected total goals | 2.33 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 49.0% |
| Under 2.5 | 51.0% |
| Over 3.5 | 27.8% |
| Under 3.5 | 72.2% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.26% |
| 2 | 1-1 | 12.21% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.47% |
| 5 | 0-0 | 7.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alverca win | 52.9% | 54.3% | 1.79 | -5.3% |
| Draw | 25.7% | 25.7% | 3.64 | -6.3% |
| Casa Pia win | 21.4% | 20.0% | 4.63 | -1.1% |
| Over 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |
| Under 2.5 | 51.0% | 51.0% | 1.88 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T18:00:00+00:00 |
| Fixture id | d9d924bf6388e1288f06e04041b3fe33 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Alverca |
| Matched away-team name | Casa Pia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4251 |
| Dc lambda away | 0.9058 |
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
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.24 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.60 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.75 |
| Fair Under 4.5 odds | 1.15 |
| Score matrix json | [[0.07022883222484433,0.06783213078818506,0.032380730650293774,0.011141702484620758,0.00287526404815725,0.0005936000073982967,0.0001021242347605966,1.5059721595280798e-05,1.943180413313743e-06,2.2287265300778225e-07,2.300609722419864e-08,2.158919423456178e-09,1.8571259373512259e-10,1.4746337562896387e-11,1.0872822634502392e-12,7.482336101058733e-14],[0.12258799215924945,0.1220716150062396,0.05258461501832436,0.01809354279648335,0.0046692786114449865,0.0009639754025633986,0.00016584442231782156,2.445620115628249e-05,3.155623480173835e-06,3.6193354569719976e-07,3.736070006183293e-08,3.505972362516653e-09,3.0158755066656585e-10,2.3947281858759625e-11,1.7656895966078033e-12,1.2150922953565716e-13],[0.09465295752811519,0.09770580257658294,0.05385044745653377,0.014691484150652122,0.003791332271773539,0.0007827228480168757,0.00013466133909550816,1.9857796547313955e-05,2.5622838415818843e-06,2.9388058546683367e-07,3.033591259542422e-08,2.84675798299429e-09,2.4488121372852473e-10,1.9444567370606156e-11,1.43369383294999e-12,9.866232058367361e-14],[0.051237152796371366,0.05288970642276521,0.0272977799586514,0.010030094607678161,0.002052308517174158,0.00042370033867287485,7.289432667702003e-05,1.074934140955671e-05,1.387005035313435e-06,1.5908223952726047e-07,1.6421312439259278e-08,1.540995416922319e-09,1.3255809952945636e-10,1.0525653877546869e-11,7.760812963530939e-13,5.340748484788444e-14],[0.02080161488270652,0.021472530072820274,0.011082542156654442,0.0038133292548662985,0.0010508561480403649,0.00017201680401276418,2.9594144637501345e-05,4.364092226845284e-06,5.631059301758887e-07,6.458531164828702e-08,6.666838389471574e-09,6.256240140085226e-10,5.381685721206806e-11,4.2732780101883955e-12,3.1507887076722953e-13,2.1682741351278885e-14],[0.006756147180123284,0.00697405342419846,0.003599493902876073,0.001238529500590122,0.0003196189586415927,7.0463057401122e-05,9.61186898076062e-06,1.4174115595568823e-06,1.8289092283077256e-07,2.0976634440661468e-08,2.1653194542512153e-09,2.0319614327515784e-10,1.747915294781687e-11,1.3879160508071443e-12,1.0233432530376104e-13,7.042327851169463e-15],[0.0018286050136358757,0.001887583073141554,0.0009742316770000926,0.0003352178681035939,8.650741534236811e-05,1.7859508388507083e-05,3.281082913238439e-06,3.836337212748324e-07,4.950088408682952e-08,5.677493086629383e-09,5.860609463654132e-10,5.499665363087119e-11,4.730871880429192e-12,3.7565052704570264e-13,2.769759973081099e-14,1.9060620902697767e-15],[0.00042422271663925063,0.00043790518630275793,0.0002260144785621208,7.776804373415211e-05,2.006907477138036e-05,4.143272664089187e-06,7.128176296343839e-07,1.1224819026230837e-07,1.1483835692654953e-08,1.31713602606915e-09,1.3596176589769145e-10,1.275881321301128e-11,1.0975269706810226e-12,8.714811886763591e-14,6.425636435737645e-15,4.4219218037118775e-16],[8.611444132245171e-05,8.889189331823036e-05,4.587946328370073e-05,1.5786405056194665e-05,4.073891128431917e-06,8.41057295425406e-07,1.4469732414862347e-07,2.13377502643589e-08,2.940069497282062e-09,2.6737001245285177e-10,2.7599350652997007e-11,2.5899557677631543e-12,2.2279080824634557e-13,1.769049905682188e-14,1.3043622373369625e-15,8.976212512024258e-17],[1.553837268001556e-05,1.6039532340909855e-05,8.278427960669674e-06,2.8484774594581436e-06,7.350873748847079e-07,1.517592345821635e-07,2.6108988386784485e-08,3.850154639211096e-09,4.967917259166665e-10,6.084582725290678e-11,4.979989297810017e-12,4.673280964985765e-13,4.0200070453351946e-14,3.192049591439376e-15,2.3535734822443136e-16,1.619655578378438e-17],[2.5233505513330764e-06,2.6047362622222206e-06,1.3443734546020723e-06,4.6257785907194176e-07,1.1937434961120102e-07,2.4644906911346174e-08,4.239963321595114e-09,6.252450003381687e-10,8.067638106671255e-11,9.253159902297719e-12,1.0199738152399398e-12,7.589164156615784e-14,6.528281437898464e-15,5.183721784972019e-16,3.822080385330383e-17,2.6302360490602105e-18],[3.7252631603975977e-07,3.845414199419079e-07,1.984720236987987e-07,6.829111620285668e-08,1.7623427972308348e-08,3.6383673984482176e-09,6.259526309188738e-10,9.230592890678841e-11,1.1910384395194237e-11,1.3660589363252486e-12,1.4101184815162885e-13,1.4130641391884942e-14,9.637807290969802e-16,7.652812166389229e-17,5.642598983334881e-18,3.8830599464419687e-19],[5.041360638395529e-08,5.203959813998622e-08,2.685901653162773e-08,9.241767100835685e-09,2.384960532122823e-09,4.923765490060227e-10,8.470953108928102e-11,1.2491667209667749e-11,1.611820171965623e-12,1.8486736251362027e-13,1.9082989582490472e-14,1.7907703538658602e-15,1.6449685741026176e-16,1.0356472648378315e-17,7.636071651324365e-19,5.254905419469333e-20],[6.297620244525497e-09,6.500737603799975e-09,3.355203057075025e-09,1.1544728450122487e-09,2.979270242065274e-10,6.150721492396137e-11,1.0581834868729022e-11,1.5604473067912844e-12,2.013470583357399e-13,2.3093456870570896e-14,2.383829091802665e-15,2.237013465751768e-16,1.9243032807592387e-17,1.6316579580787766e-18,9.538908812390072e-20,6.564378374495576e-21],[7.305004494062185e-10,7.540613051693451e-10,3.891910350061282e-10,1.339145422180448e-10,3.4558423122181086e-11,7.134607422976494e-12,1.2274533596827534e-12,1.810060649301099e-13,2.3355507459939004e-14,2.6787548259932022e-15,2.7651527962221103e-16,2.5948521482856664e-17,2.2321200021713906e-18,1.772394341756869e-19,1.3955046075067384e-20,7.614433971006754e-22],[7.908630458361889e-11,8.163707784686318e-11,4.2135060643326856e-11,1.4498014727630672e-11,3.741404922053049e-12,7.724153163721025e-13,1.328880089601081e-13,1.9596292916973404e-14,2.5285416021073224e-15,2.900105266814555e-16,2.993642460316407e-17,2.8092695564470526e-18,2.416564185585454e-19,1.9188505478457162e-20,1.4148137854472371e-21,1.0396974509852506e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13734256253731306, "-10": 2.676779857551998e-08, "-11": 2.480749305531054e-09, "-12": 2.1114697691168009e-10, "-13": 1.6610689480087865e-11, "-14": 1.2087914929858963e-12, "-15": 7.482336101058733e-14, "-2": 0.054720368459513995, "-3": 0.01667115106999485, "-4": 0.003985234812836111, "-5": 0.0007807560380419574, "-6": 0.00012930867685186155, "-7": 1.8526290458693608e-05, "-8": 2.3370460999363444e-06, "-9": 2.6321704667053646e-07, "0": 0.2573057048337905, "1": 0.2517431170779477, "10": 2.9359407914900627e-06, "11": 4.280587731839611e-07, "12": 5.731803303748902e-08, "13": 7.0938166103381694e-09, "14": 8.121375272530817e-10, "15": 7.908630458361889e-11, "2": 0.15995453492567194, "3": 0.07666533151856916, "4": 0.028831898011906682, "5": 0.008886291507813305, "6": 0.0023153612396924262, "7": 0.0005218737423471134, "8": 0.0001035690859489632, "9": 1.835112792755705e-05} |
| Raw goal margin distribution | {"-1": 0.16479359566199867, "-10": 1.1198898495537844e-08, "-11": 9.133586214010588e-10, "-12": 6.837653354462477e-11, "-13": 4.714113152580948e-12, "-14": 2.792669046538387e-13, "-2": 0.06006290965847007, "-3": 0.016467681126027634, "-4": 0.003511705371081566, "-5": 0.0006106983992541008, "-6": 8.950917415307571e-05, "-7": 1.1326462905997259e-05, "-8": 1.2602192132027847e-06, "-9": 1.2506665768887373e-07, "0": 0.25693990066180505, "1": 0.25565805552728316, "10": 1.0400020002101894e-06, "11": 1.3344001601552165e-07, "12": 1.5715844364056524e-08, "13": 1.7045766256351331e-09, "14": 1.5886267977293117e-10, "2": 0.14865452734022244, "3": 0.06411949729468232, "4": 0.02151105042643203, "5": 0.005885132088223793, "6": 0.0013570094434403978, "7": 0.0002701441164811862, "8": 4.7286066598229455e-05, "9": 7.382688142209725e-06} |
| Research history json | {"away": [{"away": "Sp Lisbon", "away_goals": 2.0, "away_xg": 2.65, "date": "2026-10-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.31, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 0.79, "date": "2026-10-24T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 4.0, "away_xg": 2.6, "date": "2026-09-12T00:00:00+00:00", "home": "Casa Pia", "home_goals": 1.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.21, "date": "2026-09-06T00:00:00+00:00", "home": "Guimaraes", "home_goals": 0.0, "home_xg": 2.48, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 7.0, "away_xg": 3.04, "date": "2026-08-17T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.12, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-08T00:00:00+00:00", "home": "Maritimo", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alverca", "away_goals": 0.0, "away_xg": 0.56, "date": "2026-11-02T00:00:00+00:00", "home": "Benfica", "home_goals": 1.0, "home_xg": 1.6, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 1.0, "away_xg": 2.04, "date": "2026-10-24T00:00:00+00:00", "home": "Alverca", "home_goals": 0.0, "home_xg": 0.39, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 4.0, "away_xg": 2.89, "date": "2026-10-12T00:00:00+00:00", "home": "Famalicao", "home_goals": 1.0, "home_xg": 0.36, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.29, "date": "2026-09-19T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 3.3, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 2.26, "date": "2026-09-05T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 1.0, "away_xg": 0.41, "date": "2026-08-22T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 3.0, "home_xg": 2.12, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 2.0, "away_xg": 1.29, "date": "2026-08-15T00:00:00+00:00", "home": "Alverca", "home_goals": 2.0, "home_xg": 1.75, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 0.0, "away_xg": 1.66, "date": "2026-08-09T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.59, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 49.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 44.6% |
| P home draw | 78.6% |
| P draw away | 47.1% |
| P home away | 74.3% |
| Raw p home draw | 75.4% |
| Raw p draw away | 50.2% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1396 |
| Totals anchor target over 2 5 | 0.4902 |
| Totals anchor reference over odds | 1.95 |
| Totals anchor reference under odds | 1.88 |
| Totals anchor reference last update utc | 2026-11-05T16:49:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4138 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.63, "draw": 3.64, "home": 1.79}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.95, "under": 1.88}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.79 |
| Reference draw odds | 3.64 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.95 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:08Z |
| Home probability edge | -1.4% |
| Draw probability edge | -0.0% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0450 |
| Raw ev home | -0.1095 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0647 |
| Raw edge prob away | 0.0456 |
| Raw ev away | 0.1369 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,417.0742 |
| Elo away rating | 1,403.5352 |
| Elo rating diff | 73.5391 |
| Elo home expectancy | 0.6043 |
| Research p home | 0.4732 |
| Research p draw | 0.2644 |
| Research p away | 0.2624 |
| Research p over 1 5 | 0.7046 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4250766782078805, 0.905841776772399], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.720600+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.766095+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alverca%22+%22Casa+Pia%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.802813+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alverca_vs_Casa+Pia&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.6404619578729738, "goals_for": 0.6273910578083026, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 0.8786878561846695, "results": "LWLWLDLLLL", "xg_against": 1.7424276306361413, "xg_for": 0.7986589891384444, "xg_matches": 10}, "venue": {"goals_against": 0.7157020266306037, "goals_for": 0.9685668669792039, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 1.6490589562063098, "results": "WWDLL", "xg_against": 1.6257944158120676, "xg_for": 0.9612876162123404, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.2097349947013118, "goals_for": 1.2751965627375945, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.1634978383066994, "results": "LLWWWLDLDL", "xg_against": 1.522332345560108, "xg_for": 1.3567986568754096, "xg_matches": 10}, "venue": {"goals_against": 1.1195224506526886, "goals_for": 0.8897994815892832, "last_match": "2026-10-24T00:00:00+00:00", "matches": 5, "points_per_game": 0.9956615910184449, "results": "LWLDD", "xg_against": 1.4696091377324454, "xg_for": 1.3868989962085467, "xg_matches": 5}}}, "goal_rates": [1.452166687475356, 1.0090439768390635], "h2h": [{"away": "Casa Pia", "away_goals": 1.0, "away_xg": null, "date": "2026-04-12T00:00:00+00:00", "home": "Alverca", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 2.0, "away_xg": null, "date": "2025-11-29T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.16661899037442665, "-10": 2.937533873701318e-08, "-11": 2.665322948376942e-09, "-12": 2.220489803684752e-10, "-13": 1.709606662445908e-11, "-14": 1.2187682979256737e-12, "-15": 7.468985117169786e-14, "-2": 0.06894923206781883, "-3": 0.020815395911081617, "-4": 0.004907576832557974, "-5": 0.0009457196279258321, "-6": 0.00015381340590226515, "-7": 2.161753137170896e-05, "-8": 2.6730892633011515e-06, "-9": 2.9495630357070774e-07, "0": 0.2643539572436939, "1": 0.2397898930832331, "10": 1.1195581050594393e-06, "11": 1.461907752465382e-07, "12": 1.752771444952498e-08, "13": 1.942133516699442e-09, "14": 1.9925554045097724e-10, "15": 1.7573457955234513e-11, "2": 0.14280459587077668, "3": 0.062044573303250826, "4": 0.021051963561304975, "5": 0.005838405837214912, "6": 0.0013665717602489836, "7": 0.00027640807504243197, "8": 4.918860041810591e-05, "9": 7.811151506965041e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.803054+00:00", "p_over_1_5": 0.7046494235447046, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Nacional vs Académico de Viseu

The model's most likely 1X2 outcome is **Académico de Viseu win** at **43.7%**. Expected goals are 0.92 for Nacional and 1.60 for Académico de Viseu (2.51 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 45.1%; Under 3.5 goals: 75.4%; Double Chance 1X: 56.3%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nacional win | 28.5% | 3.51 |
| Draw | 27.7% | 3.60 |
| Académico de Viseu win | 43.7% | 2.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nacional expected goals | 0.92 |
| Académico de Viseu expected goals | 1.60 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.12% |
| 2 | 0-1 | 10.67% |
| 3 | 1-0 | 10.05% |
| 4 | 0-0 | 8.44% |
| 5 | 0-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nacional win | 28.5% | 31.2% | 3.05 | -13.0% |
| Draw | 27.7% | 29.4% | 3.23 | -10.4% |
| Académico de Viseu win | 43.7% | 39.4% | 2.44 | +6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T15:30:00+00:00 |
| Fixture id | 406c4abcb4384570eada7fffa729be9d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nacional |
| Matched away-team name | Academico Viseu |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9186 |
| Dc lambda away | 1.5956 |
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
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.85 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.18 |
| Fair Under 4.5 odds | 1.12 |
| Score matrix json | [[0.08440871271008912,0.10667148041063533,0.08258808983575966,0.044616690046976576,0.018077507011362518,0.005859623551666963,0.0015827766952632057,0.0003664568031881698,7.423931965841273e-05,1.336880705633993e-05,2.1666753229796317e-06,3.1922899705159817e-07,4.311439229246878e-08,5.37502016975202e-09,6.222332924075889e-10,6.723000858711823e-11],[0.1005094653884252,0.1311750051672891,0.07705711208806444,0.04162868148162056,0.016866844684476277,0.005467200775712314,0.0014767771171341948,0.00034191495426109014,6.926746444477002e-05,1.247348940837284e-05,2.0215716764161553e-06,2.978500248217918e-07,4.022699357857099e-08,5.015051595452351e-09,5.80561926705517e-10,6.272757146558908e-11],[0.04337431490071615,0.07029651737098114,0.05219921622939771,0.01942039089042252,0.007868630597997578,0.0025505294033305297,0.0006889381996266121,0.00015950834440824128,3.231428879388833e-05,5.819065880938288e-06,9.430928574171154e-07,1.3895140808903826e-07,1.8766482911241928e-08,2.339595174599085e-09,2.7084065964702416e-10,2.926333273386277e-11],[0.013489836333924234,0.02186290472483613,0.017716545670951593,0.008770370926870052,0.0024472211072858493,0.0007932396003152132,0.00021426652106032386,4.96086558343972e-05,1.0050059996901948e-05,1.8097864261340545e-06,2.9331110643178766e-07,4.321524749797243e-08,5.836559807699918e-09,7.276369912752087e-10,8.423409521449545e-11,9.101182809885916e-12],[0.0031466033192559632,0.0050996829667046,0.00413251428957472,0.0022325145131619566,0.0008288853570996115,0.00018502895791553512,4.99792384195452e-05,1.1571583023567441e-05,2.344250246049787e-06,4.2214596490669237e-07,6.841696802146584e-08,1.0080273611446454e-08,1.3614204063958407e-09,1.6972666793607769e-10,1.9648220855719605e-11,2.1229176788990377e-12],[0.000587174652303428,0.0009516307805651641,0.0007711514274045034,0.00041660031469686323,0.00016879546873465833,5.0136146145187046e-05,9.32641930484132e-06,2.159325326101188e-06,4.3745085842659976e-07,7.877491536619672e-08,1.2767007891912502e-08,1.8810382346904955e-09,2.5404904039613466e-10,3.16719926601841e-11,3.666473361524995e-12,3.961489020074803e-13],[9.130853106421429e-05,0.00014798324203544556,0.00011991781966090536,6.478338706658422e-05,2.62485211852991e-05,8.508167239937104e-06,2.1059348698104464e-06,3.3578565226308205e-07,6.802574862354835e-08,1.2249884729489767e-08,1.985332187148563e-09,2.9251064808645047e-10,3.9505868664196196e-11,4.9251498073584406e-12,5.701545451827823e-13,6.160309233906149e-14],[1.2170505675998093e-05,1.9724672669176812e-05,1.598383511185799e-05,8.634971681340006e-06,3.4986629655401494e-06,1.1340528259421142e-06,3.063255460477363e-07,6.498982153533249e-08,9.067145753934803e-09,1.6327860046913837e-09,2.6462474394030714e-10,3.898871727902832e-11,5.265733587091655e-12,6.564727631358111e-13,7.599584669107361e-14,8.21107049071148e-15],[1.4194298807322433e-06,2.3004623242161306e-06,1.8641734181359566e-06,1.0070852559514196e-06,4.0804440572200833e-07,1.322630719153802e-07,3.572634078379159e-08,8.271641016967497e-09,1.5355425637162506e-09,1.9042965884901904e-10,3.086283172857456e-11,4.5472022108675275e-12,6.141355007322085e-13,7.656354474403654e-14,8.863294465865329e-15,9.576462242074275e-16],[1.4715219381477328e-07,2.3848876396909725e-07,1.932587244030528e-07,1.0440445617173733e-07,4.230193424198148e-08,1.3711703168450293e-08,3.7037471837616212e-09,8.575204302921367e-10,1.7372233994353839e-10,2.866641138527712e-11,3.1995475492266583e-12,4.714081266933444e-13,6.366738326352463e-14,7.937337186045759e-15,9.188571008562926e-16,9.927911530075776e-17],[1.3729731629995695e-08,2.2251701732606866e-08,1.8031606273904077e-08,9.74124222720009e-09,3.946894636876439e-09,1.2793421546263355e-09,3.4557048413704446e-10,8.000917329149236e-11,1.620880425718944e-11,2.9188357022314324e-12,4.334807516986893e-13,4.398376198078022e-14,5.9403537462213094e-15,7.405768585303464e-16,8.573206470134352e-17,9.263032879133045e-18],[1.1645675118262211e-09,1.8874082625203737e-09,1.529456177188012e-09,8.262604491003063e-10,3.347789593108669e-10,1.0851488943400822e-10,2.931158231766448e-11,6.786446113759576e-12,1.3748445601248283e-12,2.4757812627239727e-13,4.01248529089624e-14,5.41727567090575e-15,5.038658560878725e-16,6.281635888428762e-17,7.271866629559134e-18,7.85698325555678e-19],[9.054797274781692e-11,1.4675060928902287e-10,1.1891895905101118e-10,6.424377107206965e-11,2.602988300496771e-11,8.437298096865651e-12,2.279047225637637e-12,5.276627859896256e-13,1.0689752762160499e-13,1.9249804930170345e-14,3.119805464960494e-15,4.596592572097134e-16,5.688724908022981e-17,4.884125561301354e-18,5.65405418502981e-19,6.108996674555788e-20],[6.498762807502979e-12,1.0532509703801143e-11,8.534990731819713e-12,4.610871092825962e-12,1.868203455282951e-12,6.055574454486961e-13,1.6357061231803022e-13,3.78711437090176e-14,7.672194701212214e-15,1.381587158006192e-15,2.239130828339679e-16,3.299042920815643e-17,4.455617503153935e-18,5.090081276829352e-19,4.0579988633886e-20,4.384517861082617e-21],[4.331097473250128e-13,7.019386230322066e-13,5.688140633494058e-13,3.0729129114490193e-13,1.2450633304159777e-13,4.0357347999570736e-14,1.0901155907562675e-14,2.5239206243663693e-15,5.113130617159859e-16,9.20758123716566e-17,1.492267706970625e-17,2.1986456317488555e-18,2.969444228276707e-19,3.7019709130236453e-20,3.927038277912766e-21,2.922059904637668e-22],[2.6940273843703952e-14,4.366195598865021e-14,3.538134786258589e-14,1.9114119652949492e-14,7.744537563822074e-15,2.5103060215779706e-15,6.780732301142764e-16,1.569928019402841e-16,3.180467303626495e-17,5.727295714294991e-18,9.282197161851558e-19,1.367600608631162e-19,1.8470524195648976e-20,2.3026983524211262e-21,2.665693396485676e-22,2.6392413395598082e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.20579090492010024, "-10": 2.4840395120736987e-06, "-11": 3.618819428176616e-07, "-12": 4.840938573037804e-08, "-13": 5.9848454291914e-09, "-14": 6.84960863873178e-10, "-15": 6.723000858711823e-11, "-2": 0.13293084976931352, "-3": 0.0642603522088468, "-4": 0.024285679692640328, "-5": 0.007506394284032974, "-6": 0.001958886062921878, "-7": 0.0004418469839450651, "-8": 8.770051084246532e-05, "-9": 1.5535340155397213e-05, "0": 0.2774344990262301, "1": 0.19093266135336331, "10": 1.5740796739298972e-08, "11": 1.3201681476757726e-09, "12": 1.0166841063462042e-10, "13": 7.2360827783977716e-12, "14": 4.767717033136631e-13, "15": 2.6940273843703952e-14, "2": 0.06981375340415585, "3": 0.019429088826288056, "4": 0.004227208999737487, "5": 0.00075219242583009, "6": 0.00011300583933466052, "7": 1.4674311349228221e-05, "8": 1.6768031579229441e-06, "9": 1.7099950473451673e-07} |
| Raw goal margin distribution | {"-1": 0.2558508555178725, "-10": 2.723757965586566e-06, "-11": 3.9079837968922497e-07, "-12": 5.14836329658975e-08, "-13": 6.2680752542556245e-09, "-14": 7.066037955489394e-10, "-15": 6.847371918179126e-11, "-2": 0.16353259753661584, "-3": 0.07806676880003371, "-4": 0.029104453663672137, "-5": 0.008868862488402069, "-6": 0.00228094245466796, "-7": 0.0005069227761088592, "-8": 9.912093382660662e-05, "-9": 1.7295227814387712e-05, "0": 0.23891270159249914, "1": 0.14980908427278092, "10": 1.089205358322855e-08, "11": 8.996801442827734e-10, "12": 6.82336639874546e-11, "13": 4.782531448852661e-12, "14": 3.1037999664588746e-13, "15": 1.731553047968693e-14, "2": 0.054199163811193024, "3": 0.014895276895857333, "4": 0.0031969508070942066, "5": 0.0005608394427689614, "6": 8.3038420973383e-05, "7": 1.0624308763186741e-05, "8": 1.1959647780374022e-06, "9": 1.2013606900315954e-07} |
| Research history json | {"away": [{"away": "Rio Ave", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-11-01T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-10-25T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 1.0, "home_xg": 2.22, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 2.54, "date": "2026-09-20T00:00:00+00:00", "home": "Estrela", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Guimaraes", "away_goals": 1.0, "away_xg": 2.1, "date": "2026-09-12T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 1.83, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 3.0, "away_xg": 1.47, "date": "2026-08-29T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.84, "date": "2026-08-22T00:00:00+00:00", "home": "Maritimo", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 2.0, "away_xg": 1.18, "date": "2026-08-09T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 3.12, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Nacional", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-11-01T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.7, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 1.67, "date": "2026-10-25T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.21, "date": "2026-10-11T00:00:00+00:00", "home": "Rio Ave", "home_goals": 3.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 4.0, "away_xg": 1.45, "date": "2026-09-19T00:00:00+00:00", "home": "Nacional", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}, {"away": "Alverca", "away_goals": 3.0, "away_xg": 1.16, "date": "2026-09-12T00:00:00+00:00", "home": "Nacional", "home_goals": 1.0, "home_xg": 2.2, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.08, "date": "2026-09-05T00:00:00+00:00", "home": "Sp Lisbon", "home_goals": 2.0, "home_xg": 3.0, "source": "pipeline training history"}, {"away": "Estrela", "away_goals": 3.0, "away_xg": 2.1, "date": "2026-08-30T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-08-23T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 3.14, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 53.8% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 47.3% |
| P home draw | 56.3% |
| P draw away | 71.5% |
| P home away | 72.3% |
| Raw p home draw | 46.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0157 |
| Totals anchor target over 2 5 | 0.4513 |
| Totals anchor reference over odds | 2.10 |
| Totals anchor reference under odds | 1.75 |
| Totals anchor reference last update utc | 2026-11-05T16:49:08Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4421 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.53, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.53, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.44, "draw": 3.23, "home": 3.05}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 2.1, "under": 1.75}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.33, "under": 3.28}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.05 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:09Z |
| Home probability edge | -2.7% |
| Draw probability edge | -1.7% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | -0.0893 |
| Raw ev home | -0.3206 |
| Raw edge prob draw | -0.0550 |
| Raw ev draw | -0.2283 |
| Raw edge prob away | 0.1444 |
| Raw ev away | 0.3135 |
| Market p home draw | 60.9% |
| Market reference home draw last update utc | 2026-11-05T16:49:13Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.5% |
| Market reference draw away last update utc | 2026-11-05T16:49:13Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.6% |
| Market reference home away last update utc | 2026-11-05T16:49:13Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.53 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 73.0% |
| Market over 1 5 odds | 1.33 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.28 |
| Market reference over 1 5 last update utc | 2026-11-05T16:49:08Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market under 3 5 odds | 1.28 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.67 |
| Market reference under 3 5 last update utc | 2026-11-05T16:49:08Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,377.6402 |
| Elo away rating | 1,452.3265 |
| Elo rating diff | -14.6862 |
| Elo home expectancy | 0.4789 |
| Research p home | 0.2806 |
| Research p draw | 0.2544 |
| Research p away | 0.4650 |
| Research p over 1 5 | 0.7437 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.9185924118161947, 1.595617269071884], "coverage": {"form": "last ten, exponential rank half-life five matches", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.720600+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.721297+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Nacional%22+%22Acad%C3%A9mico+de+Viseu%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.757190+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Nacional_vs_Acad%C3%A9mico+de+Viseu&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.0650527153129232, "goals_for": 1.649570964958943, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.3738678769859316, "results": "WWWWWWLDLD", "xg_against": 1.584486958053463, "xg_for": 1.1369674333411801, "xg_matches": 10}, "venue": {"goals_against": 0.8979146949535403, "goals_for": 1.8037913442624962, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 2.3609841784542116, "results": "WWWDD", "xg_against": 1.8155259012043192, "xg_for": 1.326331413049327, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.8804243500740794, "goals_for": 0.874261798272425, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 0.6711447942719047, "results": "LWLLLLLLWD", "xg_against": 1.6090907760595652, "xg_for": 0.9211553615670336, "xg_matches": 10}, "venue": {"goals_against": 2.00259287486749, "goals_for": 1.0941233506910442, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.2227916852143603, "results": "WLLLW", "xg_against": 1.4674034895920058, "xg_for": 1.2859261160044595, "xg_matches": 5}}}, "goal_rates": [1.1293036107455927, 1.529367329821478], "h2h": [], "margin_distribution": {"-1": 0.23043296577038033, "-10": 1.5792789208268723e-06, "-11": 2.1676700012795465e-07, "-12": 2.7326442699868792e-08, "-13": 3.184090012007865e-09, "-14": 3.431158372998009e-10, "-15": 3.137121933802743e-11, "-2": 0.14051096734799715, "-3": 0.06322012449775119, "-4": 0.022343424044953368, "-5": 0.006475757931443599, "-6": 0.0015872729852496436, "-7": 0.0003366452573663887, "-8": 6.287648857955709e-05, "-9": 1.048641800416719e-05, "0": 0.2544271091440475, "1": 0.17015453070367498, "10": 7.611108620607441e-08, "11": 7.714027037244888e-09, "12": 7.180753147545276e-10, "13": 6.178330578694378e-11, "14": 4.916153991381648e-12, "15": 3.3190593704169395e-13, "2": 0.07661398281467025, "3": 0.025453767397781112, "4": 0.006642711031397811, "5": 0.0014216253096338855, "6": 0.00025730313251404, "7": 4.029627088988149e-05, "8": 5.557500941275839e-06, "9": 6.84411563285406e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.757402+00:00", "p_over_1_5": 0.7437421180271485, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Sporting Lisbon vs Moreirense FC

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **84.1%**. Expected goals are 2.87 for Sporting Lisbon and 0.69 for Moreirense FC (3.56 combined). The most likely exact score is 2-0 at 12.0%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 69.7%; Under 3.5 goals: 51.9%; Double Chance 1X: 94.3%; Double Chance X2: 15.9%; Double Chance 12 (either team wins): 89.8%; Under 4.5 goals: 71.0%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 84.1% | 1.19 |
| Draw | 10.2% | 9.80 |
| Moreirense FC win | 5.7% | 17.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 2.87 |
| Moreirense FC expected goals | 0.69 |
| Expected total goals | 3.56 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.1% |
| Under 1.5 | 12.9% |
| Over 2.5 | 69.7% |
| Under 2.5 | 30.3% |
| Over 3.5 | 48.1% |
| Under 3.5 | 51.9% |
| Over 4.5 | 29.0% |
| Under 4.5 | 71.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.99% |
| 2 | 3-0 | 11.47% |
| 3 | 1-0 | 8.64% |
| 4 | 2-1 | 8.28% |
| 5 | 4-0 | 8.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 84.1% | 84.9% | 1.16 | -2.5% |
| Draw | 10.2% | 9.7% | 8.30 | -15.3% |
| Moreirense FC win | 5.7% | 5.4% | 14.11 | -19.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T20:30:00+00:00 |
| Fixture id | ba0a2d492dfcc89ab465eddd7a9e98c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Lisbon |
| Matched away-team name | Moreirense |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8699 |
| Dc lambda away | 0.6904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.60 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.74 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.30 |
| Fair Over 3.5 odds | 2.08 |
| Fair Under 3.5 odds | 1.93 |
| Fair Over 4.5 odds | 3.44 |
| Fair Under 4.5 odds | 1.41 |
| Score matrix json | [[0.022933658626115086,0.01979677117934546,0.005976087531838772,0.001375254310779966,0.00023736153577601717,3.2773864862271974e-05,3.7710624796430413e-06,3.7192297543353344e-07,3.209595779751522e-08,2.462040260983446e-09,1.6997399038378003e-10,1.066785501765668e-11,6.137382326499318e-13,3.2593210819677604e-14,1.6072610852279433e-15,7.397457698644197e-17,3.1919040471730624e-18,1.2962483772645043e-19,4.9716785415681616e-21,1.8064949798527159e-22],[0.08642293124539525,0.04791396715958243,0.017150920699795968,0.003946876196269895,0.0006812097138114819,9.405852144633899e-05,1.0822665029210732e-05,1.0673909015067604e-06,9.211297927555736e-08,7.065869944317822e-09,4.878125386498678e-10,3.0615939687960786e-11,1.7613824601014716e-12,9.354005796297694e-14,4.61271814874685e-15,2.123014592634396e-16,9.160523988774123e-18,3.7201351230647455e-19,1.426834261664112e-20,5.184504406765329e-22],[0.11987566895998827,0.08275959628261867,0.02498252570107954,0.005663618570970722,0.000977510262296693,0.00013497043290209795,1.5530116375264635e-05,1.5316657102070094e-06,1.3217865322087585e-07,1.0139257034340924e-08,6.999926057120337e-10,4.393271943729269e-11,2.5275174379780896e-12,1.3422645734605833e-13,6.61907667501357e-15,3.0464459170646324e-16,1.3145006633771835e-17,5.338253677534196e-19,2.0474533834365974e-20,7.439568402775347e-22],[0.11467804430095374,0.07917126745707649,0.0273290743183166,0.005499860094471806,0.0009351269205572745,0.000129118322491547,1.4856754411739799e-05,1.4652550404369262e-06,1.264475900840511e-07,9.699634441673103e-09,6.696420027902259e-10,4.20278642830584e-11,2.417928168731471e-12,1.2840660457151757e-13,6.3320836893262594e-15,2.9143567069828493e-16,1.2575059360771262e-17,5.106795207343764e-19,1.9586789533433173e-20,7.11700015753998e-22],[0.0822793354905971,0.05680389228840738,0.019608095762281248,0.0045123365545762855,0.0006810664201505926,9.263996294168358e-05,1.0659441290583474e-05,1.0512928763853676e-06,9.07237627736263e-08,6.959304906422564e-09,4.804555165030322e-10,3.015420053924206e-11,1.7348178912532008e-12,9.212931874755089e-14,4.543150708616331e-15,2.090996011440695e-16,9.022368093789222e-18,3.6640293153596826e-19,1.4053152345149124e-20,5.106313481524852e-22],[0.04722709802066567,0.03260457772372905,0.01125475133023751,0.0025900131484358035,0.0004470224116179193,5.397681665370182e-05,6.118358585108494e-06,6.034262603780177e-07,5.207407196188789e-08,3.9945360886984585e-09,2.7577422249662356e-10,1.7308056465336194e-11,9.95759313194532e-13,5.288083989891936e-14,2.6077000082602783e-15,1.2002001839747e-16,5.1787032528064724e-18,2.103097583315552e-19,8.066297562400126e-21,2.9309469489308196e-22],[0.022589701838607007,0.015595446686782165,0.005383381310163916,0.0012388570806454117,0.000213820103644842,2.9523364679885487e-05,2.970725853466125e-06,2.886313128441704e-07,2.4908110141056505e-08,1.9106695733828134e-09,1.319085381499921e-10,8.278802876827871e-12,4.762923603359593e-13,2.5294004001028893e-14,1.2473170730362482e-15,5.740806748440477e-17,2.477081321836287e-18,1.0059552531431115e-19,3.8582776522996904e-21,1.4019327982454106e-22],[0.00926153447389528,0.00639396518632119,0.002207128360808908,0.0005079180611856307,8.766393975745728e-05,1.2104261566694627e-05,1.3927538552370509e-06,1.2012248400921286e-07,1.0212056909787033e-08,7.833539481191719e-10,5.408108005167975e-11,3.3942200208806693e-12,1.9527473830422443e-13,1.0370269236489401e-14,5.113865669559333e-16,2.3536689412068304e-17,1.0155766650102698e-18,4.1243082014735847e-20,1.5818522856978462e-21,5.747773491566815e-23],[0.003322488218126259,0.002293774758226077,0.0007917865009679857,0.0001822108181769827,3.144861230281431e-05,4.342289774746901e-06,4.996373212039449e-07,4.9276987624294455e-08,3.7187941492359116e-09,2.8102084709446455e-10,1.9401077845329918e-11,1.21764444767663e-12,7.005297223070188e-14,3.720236366246754e-15,1.8345511193724622e-16,8.443565532872648e-18,3.6432855847065886e-19,1.4795567026113115e-20,5.674746011971291e-22,2.0619595770027143e-23],[0.0010594767461245052,0.0007314400707065312,0.0002524852853034227,5.81034791026902e-05,1.0028349611878328e-05,1.3846715892564018e-06,1.593246051027543e-07,1.5713471073329486e-08,1.3560305163567127e-09,9.096512669900155e-11,6.186625648433602e-12,3.88283085647343e-13,2.2338527694521354e-14,1.1863108794853767e-15,5.850026013479586e-17,2.6924885053473456e-18,1.1617727748223933e-19,4.7180179975878704e-21,1.8095659172079814e-22,6.575187268881022e-24],[0.000304061839108776,0.00020991778621892013,7.246137348279364e-05,1.667526048042791e-05,2.8780607383478816e-06,3.973903075561188e-07,4.572496057136675e-08,4.509647739618857e-09,3.8917053554905624e-10,2.985277875036475e-11,1.8023234667138165e-12,1.1143431844882356e-13,6.410989045889156e-15,3.404622792246578e-16,1.6789133645447192e-17,7.727239032945659e-19,3.334200281706704e-20,1.3540355978009245e-21,5.19331776546758e-23,1.887029178104895e-24],[7.933041418829065e-05,5.4768020133820665e-05,1.8905334480286407e-05,4.3506127716893105e-06,7.508924865461856e-07,1.0368002043676786e-07,1.1929744526645823e-08,1.176577185995607e-09,1.0153546352767045e-10,7.788656774159083e-12,5.377121944807954e-13,2.951244397639765e-14,1.6726413872180708e-15,8.882737046367492e-17,4.38032253524395e-18,2.0160539540649408e-19,8.699003140604038e-21,3.532709172386794e-22,1.3549482255106847e-23,4.923301349594788e-25],[1.897269235622439e-05,1.3098340751028826e-05,4.52140706255052e-06,1.0404942230908645e-06,1.7958373576655232e-07,2.479615354793144e-08,2.853122287439301e-09,2.8139065214337117e-10,2.4283260493066663e-11,1.8627381484938066e-12,1.2859945515802243e-13,8.071119233465604e-15,4.060696135627089e-16,2.1243988070195033e-17,1.0475996215646515e-18,4.821602387356455e-20,2.0804569354797473e-21,8.448840838347692e-23,3.240499385293866e-24,1.1774586435555702e-25],[4.188476675128519e-06,2.8916346551400726e-06,9.981613397131408e-07,2.2970307546215458e-07,3.964552180407217e-08,5.474083952789298e-09,6.298650675326167e-10,6.21207660448386e-11,5.3608559218487265e-12,4.1122446621439945e-13,2.839005704885643e-14,1.7818079804820737e-15,1.0251017463704019e-16,4.760708564834687e-18,2.3127168761356533e-19,1.0644334898289244e-20,4.592888127976988e-22,1.8651950982424952e-23,7.153837650574054e-25,2.599398109590389e-26],[8.586151644886222e-07,5.927695335650668e-07,2.0461769978883425e-07,4.708789357539602e-08,8.127118488488705e-09,1.1221577337313193e-09,1.2911894717631692e-10,1.2734422534204918e-11,1.0989465970934916e-12,8.429880123173623e-14,5.8198088215681115e-15,3.652610414027941e-16,2.1014033808613474e-17,1.115972246243682e-18,4.812528710657042e-20,2.1820313370340473e-21,9.415173346667378e-23,3.823549515246404e-24,1.4664981967182778e-25,5.328626153490235e-27],[1.6427738627020622e-07,1.1341359163237657e-07,3.914915819819164e-08,9.009246984523996e-09,1.5549478257728642e-09,2.147005400144222e-10,2.470410963766206e-11,2.4364555112715125e-12,2.1025959252487493e-13,1.612874696932374e-14,1.1134941721753945e-15,6.988477687058104e-17,4.0205795236901085e-18,2.135170811619556e-19,1.0529115940178556e-20,4.237879696543054e-22,1.8013891818374967e-23,7.315532576384125e-25,2.8058261802344595e-26,1.0195170235873913e-27],[2.9466482143200242e-08,2.0343028632893007e-08,7.022195794318852e-09,1.6159912293497662e-09,2.789114398641609e-10,3.851089776936515e-11,4.431183268916252e-12,4.370277275869013e-13,3.771432373765762e-14,2.8930179944673672e-15,1.9972777072917453e-16,1.2535252577925766e-17,7.2117250846239915e-19,3.8298620413758455e-20,1.888610562166129e-21,8.692375415071538e-23,3.2799442899177224e-24,1.3121891875943346e-25,5.032818509835102e-27,1.8287106248947517e-28],[4.974504845573742e-09,3.4342916815173327e-09,1.185480738272236e-09,2.728101767200644e-10,4.708557683769483e-11,6.501374905565704e-12,7.480683488353179e-13,7.37786254214536e-14,6.3668979985046484e-15,4.883966793820661e-16,3.3717861482735346e-17,2.1161899946638877e-18,1.2174769015203365e-19,6.465538434522458e-21,3.1883352574087803e-22,1.467438950183528e-23,6.331802782635257e-25,2.2486736616964407e-26,8.496358656727286e-28,3.087212725456051e-29],[7.931363275595491e-10,5.475643459209065e-10,1.8901335275257517e-10,4.3496924498355265e-11,7.507336439183822e-12,1.0365808812662766e-12,1.1927220927057882e-13,1.1763282946890806e-14,1.0151398487376068e-15,7.7870091738285e-17,5.3759844768015e-18,3.3740587513537617e-19,1.9411482922156983e-20,1.030867105138141e-21,5.0834899062163216e-23,2.339688423264901e-24,1.0095442585243765e-25,4.099810293633077e-27,1.3751156714532967e-28,4.922259882090652e-30],[1.1980218254156967e-10,8.270886283209164e-11,2.8550214386136503e-11,6.57015232776308e-12,1.1339731383323267e-12,1.5657415710446044e-13,1.801590784668397e-14,1.7768281718072457e-15,1.5333551778909438e-16,1.1762173312201955e-17,8.120352721859943e-19,5.0964706619785366e-20,2.932078559052271e-21,1.557110988546753e-22,7.678543581110017e-24,3.534068101972468e-25,1.5249031136384346e-26,6.192708669579371e-28,2.3751741831842183e-29,7.547269153353451e-31]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.04364549482288657, "-10": 2.032505198039159e-10, "-11": 1.2570010399295931e-11, "-12": 7.14198039552228e-13, "-13": 3.7523523228914066e-14, "-14": 1.8332325768929293e-15, "-15": 8.368902376385109e-17, "-16": 3.585103793329657e-18, "-17": 1.4463713718336907e-19, "-18": 5.490128982244694e-21, "-19": 1.8064949798527159e-22, "-2": 0.011040880891707818, "-3": 0.0022073965448446142, "-4": 0.0003485102823109345, "-5": 4.526188674875982e-05, "-6": 4.98082991923413e-06, "-7": 4.7487602952002605e-07, "-8": 3.990563718178215e-08, "-9": 2.9962982426967164e-09, "0": 0.10206814947798216, "1": 0.20150192759447663, "10": 0.00036358931570562667, "11": 9.347559839131651e-05, "12": 2.2078239492001627e-05, "13": 4.822059498294753e-06, "14": 9.793314260026342e-07, "15": 1.8585052653900813e-07, "16": 3.309635732979791e-08, "17": 5.550619405880784e-09, "18": 8.758451903916408e-10, "19": 1.1980218254156967e-10, "2": 0.22147148544087525, "3": 0.18406771516745607, "4": 0.1208080927958059, "5": 0.0652223218429346, "6": 0.02983654166211599, "7": 0.011825246109357979, "8": 0.0041309254645006035, "9": 0.0012893811538739234} |
| Raw goal margin distribution | {"-1": 0.04948198082575506, "-10": 2.3043015927702025e-10, "-11": 1.4250932795733777e-11, "-12": 8.097040448807984e-13, "-13": 4.254134967337512e-14, "-14": 2.0783812759386666e-15, "-15": 9.48803235251111e-17, "-16": 4.0645211580201145e-18, "-17": 1.6397871253017992e-19, "-18": 6.22429550020593e-21, "-19": 2.0480681985078931e-22, "-2": 0.01251732071774916, "-3": 0.0025025802537026955, "-4": 0.0003951147575910933, "-5": 5.131452447333045e-05, "-6": 5.6468905109228455e-06, "-7": 5.383787417847988e-07, "-8": 4.524201138929573e-08, "-9": 3.396977690252175e-09, "0": 0.11399596657892257, "1": 0.19680634904045466, "10": 0.000355116631529946, "11": 9.129734620102498e-05, "12": 2.1563752563232187e-05, "13": 4.709691545110808e-06, "14": 9.56510167188315e-07, "15": 1.8151967096314223e-07, "16": 3.232511634193599e-08, "17": 5.4212738966098026e-09, "18": 8.554354606101821e-10, "19": 1.170104446868364e-10, "2": 0.21631055834812582, "3": 0.17977840426037853, "4": 0.11799291431857611, "5": 0.06370245283053716, "6": 0.02914126382121728, "7": 0.011549683623728163, "8": 0.00403466293614202, "9": 0.0012593348383554191} |
| Research history json | {"away": [{"away": "Estrela", "away_goals": 1.0, "away_xg": 0.68, "date": "2026-10-31T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.44, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-09-20T00:00:00+00:00", "home": "Guimaraes", "home_goals": 1.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-09-14T00:00:00+00:00", "home": "Moreirense", "home_goals": 3.0, "home_xg": 1.99, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 4.0, "away_xg": 2.99, "date": "2026-09-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 0.38, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.85, "date": "2026-09-04T00:00:00+00:00", "home": "Porto", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 1.0, "away_xg": 0.28, "date": "2026-08-30T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.78, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-08-16T00:00:00+00:00", "home": "Arouca", "home_goals": 4.0, "home_xg": 2.14, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 2.0, "away_xg": 1.5, "date": "2026-08-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 2.0, "home_xg": 0.2, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 82.1% |
| Unadjusted draw probability | 11.4% |
| Unadjusted away-win probability | 6.5% |
| Raw p over 1 5 | 86.8% |
| Raw p under 3 5 | 52.4% |
| Raw p btts yes | 46.8% |
| P home draw | 94.3% |
| P draw away | 15.9% |
| P home away | 89.8% |
| Raw p home draw | 93.5% |
| Raw p draw away | 17.9% |
| Raw p home away | 88.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6971 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -2.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 14.11, "draw": 8.3, "home": 1.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.16 |
| Reference draw odds | 8.30 |
| Reference away odds | 14.11 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-11-05T16:48:43Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:48:43Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | -0.0280 |
| Raw ev home | -0.0476 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | -0.0538 |
| Raw edge prob away | 0.0109 |
| Raw ev away | -0.0835 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,667.4354 |
| Elo away rating | 1,438.9672 |
| Elo rating diff | 288.4681 |
| Elo home expectancy | 0.8403 |
| Research p home | 0.8182 |
| Research p draw | 0.1196 |
| Research p away | 0.0621 |
| Research p over 1 5 | 0.8703 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.8699246134567296, 0.6903785980976834], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.720600+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.812610+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Sporting+Lisbon%22+%22Moreirense+FC%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.849147+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Sporting+Lisbon_vs_Moreirense+FC&d=2026-11-07"}]}, "form": {"away": {"all": {"goals_against": 1.4889998489640717, "goals_for": 1.4469006738231538, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.6256113882270293, "results": "WWLDWLLWLD", "xg_against": 1.5345832438249536, "xg_for": 0.827627807906664, "xg_matches": 10}, "venue": {"goals_against": 1.4714941649527495, "goals_for": 1.3690993918184686, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 1.514509847632683, "results": "WDLWL", "xg_against": 1.781999249674747, "xg_for": 0.7490016998175378, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.8699246134567296, 0.6903785980976834], "h2h": [], "margin_distribution": {"-1": 0.0466654936748083, "-10": 2.3043015927702022e-10, "-11": 1.4250932795733775e-11, "-12": 8.097040448807983e-13, "-13": 4.254134967337511e-14, "-14": 2.0783812759386666e-15, "-15": 9.488032352511109e-17, "-16": 4.0645211580201145e-18, "-17": 1.639787125301799e-19, "-18": 6.2242955002059294e-21, "-19": 2.048068198507893e-22, "-2": 0.012517320717749159, "-3": 0.0025025802537026955, "-4": 0.0003951147575910932, "-5": 5.131452447333044e-05, "-6": 5.6468905109228455e-06, "-7": 5.383787417847987e-07, "-8": 4.524201138929572e-08, "-9": 3.396977690252175e-09, "0": 0.11962894088081609, "1": 0.1939898618895079, "10": 0.00035511663152994595, "11": 9.129734620102498e-05, "12": 2.1563752563232187e-05, "13": 4.709691545110807e-06, "14": 9.565101671883147e-07, "15": 1.815196709631422e-07, "16": 3.232511634193598e-08, "17": 5.421273896609802e-09, "18": 8.55435460610182e-10, "19": 1.1701044468683638e-10, "2": 0.21631055834812582, "3": 0.1797784042603785, "4": 0.1179929143185761, "5": 0.06370245283053715, "6": 0.029141263821217275, "7": 0.011549683623728163, "8": 0.004034662936142019, "9": 0.0012593348383554187}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.849371+00:00", "p_over_1_5": 0.8703496537615097, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Estoril vs CS Maritimo

The model's most likely 1X2 outcome is **Estoril win** at **49.9%**. Expected goals are 2.02 for Estoril and 1.15 for CS Maritimo (3.17 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.4%; Double Chance 1X: 74.6%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 52.8%; BTTS No (at least one team does not score): 47.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Estoril win | 49.9% | 2.01 |
| Draw | 24.7% | 4.05 |
| CS Maritimo win | 25.4% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Estoril expected goals | 2.02 |
| CS Maritimo expected goals | 1.15 |
| Expected total goals | 3.17 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 75.3% |
| Under 1.5 | 24.7% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.70% |
| 2 | 1-0 | 10.40% |
| 3 | 2-1 | 8.78% |
| 4 | 2-0 | 8.72% |
| 5 | 0-1 | 7.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Estoril win | 49.9% | 46.4% | 2.08 | +3.7% |
| Draw | 24.7% | 26.5% | 3.55 | -12.4% |
| CS Maritimo win | 25.4% | 27.0% | 3.49 | -11.2% |
| Over 2.5 | 51.3% | 51.3% | 1.87 | -4.2% |
| Under 2.5 | 48.7% | 48.7% | 1.96 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 88fe8a3db780908444b4b21229766ad5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Estoril |
| Matched away-team name | Maritimo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 2.0186 |
| Dc lambda away | 1.1530 |
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
| P btts yes | 52.8% |
| P btts no | 47.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.82 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 7.01 |
| Fair Under 4.5 odds | 1.17 |
| Score matrix json | [[0.06320893352185213,0.07935376190100928,0.03671251736250496,0.012321220626639422,0.003101377036433622,0.0006245186131199885,0.00010479847434206577,1.5073626301279365e-05,1.8970928239648077e-06,2.1223005950515014e-07,2.1368189173307134e-08,1.9558514155940818e-09,1.6410259044965348e-10,1.270963002179412e-11,9.140410420037254e-13,6.135292346818714e-14,3.860789318854248e-15],[0.10397508124855785,0.11695452148292765,0.06471573694552542,0.021719482351154475,0.005467015472595116,0.00110088289193525,0.00018473564291018066,2.6571341455463425e-05,3.344138974309048e-06,3.7411285549423757e-07,3.766721022934543e-08,3.4477168772248888e-09,2.8927518019958647e-10,2.240415891516678e-11,1.6112444441671745e-12,1.0815111415000056e-13,6.805684924680354e-15],[0.08724976371424943,0.08784662553078122,0.05462481509380303,0.019143229713060317,0.004818546378992335,0.0009703018583393843,0.00016282325661557472,2.3419586389869066e-05,2.9474745089490233e-06,3.29737523921902e-07,3.3199320610519386e-08,3.0387665368462537e-09,2.5496285479166827e-10,1.9746693484992233e-11,1.4201269634285234e-12,9.532278847275665e-14,5.998429785825102e-15],[0.051267098733082266,0.05161780883676069,0.02598545904635963,0.0107721906368702,0.0028313302230913795,0.0005701397809545498,9.56733361512745e-05,1.3761117470410741e-05,1.7319068869736556e-06,1.9375050974659992e-07,1.950759263010793e-08,1.7855491801846598e-09,1.498136532802806e-10,1.1602961904430618e-11,8.344525663822734e-13,5.601072828289401e-14,3.5246180503195234e-15],[0.022593030347184365,0.02274758568991449,0.011451599160634282,0.0038433125789984358,0.0011949248915765934,0.0002512563747815724,4.216252997533648e-05,6.0644224522799855e-06,7.632385257378285e-07,8.538441329161197e-08,8.596851454130274e-09,7.86878286683121e-10,6.602176636923257e-11,5.113339293664071e-12,3.6773705985813873e-13,2.4683512723272858e-14,1.553273045305312e-15],[0.007965264785922565,0.008019753900928683,0.00403730788367078,0.001354975489182423,0.00034106116548186045,8.483150257647888e-05,1.486457151330323e-05,2.1380368132920177e-06,2.6908284806852463e-07,3.010262235774375e-08,3.0308549630184874e-09,2.774171419862342e-10,2.3276242393521685e-11,1.8027285755127754e-12,1.296471968724536e-13,8.702272854338873e-15,5.476127328016881e-16],[0.0023401554275403916,0.002356164060228761,0.0011861411027190977,0.0003980851020544179,0.00010020208479901585,2.0177510278586926e-05,4.182261835562917e-06,6.281446489700061e-07,7.905521087992948e-08,8.844001673136299e-09,8.904502088029393e-10,8.150378524254384e-11,6.838444977524577e-12,5.296327458974437e-13,3.8089705688463166e-14,2.5566847555413466e-15,1.6088591444203563e-16],[0.0005893080847795937,0.0005933394480636295,0.0002986991946327385,0.0001002475161735508,2.5233323389077006e-05,5.081188111676992e-06,8.52657952480404e-07,1.5148572123315593e-07,1.9908025923074725e-08,2.2271348417491028e-09,2.2423703185082233e-10,2.0524636534101237e-11,1.7220868601925724e-12,1.333744141300172e-13,9.591914812546865e-15,6.438354388523834e-16,4.051498844566088e-17],[0.00012985185208730049,0.00013074014804384515,6.581726034617815e-05,2.2089168600420227e-05,5.560069276183308e-06,1.1196209659197225e-06,1.878800192737146e-07,2.702361096179021e-08,4.200957472855385e-09,4.907409070375138e-10,4.940979878678994e-11,4.522527581423749e-12,3.794554563676893e-13,2.938855777333986e-14,2.1135428745028333e-15,1.418667524401777e-16,8.927327526708353e-18],[2.5433221586081337e-05,2.560720622729871e-05,1.2891190534947057e-05,4.326459042641116e-06,1.089013915951399e-06,2.1929273753842467e-07,3.679881407138546e-08,5.2929355615597316e-09,6.66142961942135e-10,9.204915929646094e-11,9.677569791020497e-12,8.857975012184207e-13,7.432142513730772e-14,5.756142018230067e-15,4.1396563387308843e-16,2.7786500481202304e-17,1.7485364706669636e-18],[4.483292882342928e-06,4.513962378968307e-06,2.27242084038161e-06,7.626553704952681e-07,1.9196814377732023e-07,3.865627348969266e-08,6.486785822492522e-09,9.330229852920776e-10,1.174257059723971e-10,1.3136555181244206e-11,1.6337153383166995e-12,1.561457567995647e-13,1.3101160432857832e-14,1.0146756458965011e-15,7.2972634378866e-17,4.8981219076378404e-18,3.0822682399575863e-19],[7.184559769890161e-07,7.233708205515522e-07,3.6415964289028793e-07,1.222169337794305e-07,3.076325011722777e-08,6.194739327910674e-09,1.0395194264403807e-09,1.4951865917377147e-10,1.8817686580390215e-11,2.1051572660313672e-12,2.1195583135116022e-13,2.3963352502478606e-14,2.0994851921339944e-15,1.62603649065765e-16,1.1693999634200169e-17,7.849330955875908e-19,4.939391866193846e-20],[1.0553940761461776e-07,1.0626138598868942e-07,5.349415165124213e-08,1.795336555708446e-08,4.519045421932897e-09,9.099918992039554e-10,1.5270283494639548e-10,2.1963921551136354e-11,2.7642716575274426e-12,3.09242400242368e-13,3.113578785302147e-14,2.849889349727434e-15,2.953531753516475e-16,2.3886074231432553e-17,1.7178196487575623e-18,1.1530473206250325e-19,7.255844592166705e-21],[1.4310902931664595e-08,1.440880155231849e-08,7.2536849409664354e-09,2.4344354169801137e-09,6.127722510364707e-10,1.2339282579320817e-10,2.0706156095623077e-11,2.9782576614867507e-12,3.748289313133085e-13,4.193256407486733e-14,4.221941810518335e-15,3.864384950772187e-16,3.242350496874275e-17,3.101783631693189e-18,2.3293242593556773e-19,1.5635058651584935e-20,9.838759757389346e-22],[1.8019168083612967e-09,1.8142434358923472e-09,9.133271939651347e-10,3.0652504022094357e-10,7.715548236980265e-11,1.553665816124133e-11,2.6071569965513058e-12,3.749988778129155e-13,4.719552321881281e-14,5.279820035464509e-15,5.315938448204837e-16,4.865730855715405e-17,4.082513791627532e-18,3.1618781707395885e-19,2.8087429065341684e-20,1.9686441252892078e-21,1.2388195674950643e-22],[2.117577010881277e-10,2.1320630198692207e-10,1.0733240626753094e-10,3.602221675381485e-11,9.067159758520349e-12,1.8258373525071702e-12,3.0638793611543647e-13,4.406912678089001e-14,5.546324587290982e-15,6.204740128295791e-16,6.247185772919081e-17,5.718110710432249e-18,4.797689500226266e-19,3.715776718712421e-20,2.6722826848626435e-21,2.2155728298346514e-22,1.4558362653507396e-23],[2.33300122552421e-11,2.3489609174495403e-11,1.1825148935499623e-11,3.9686809689048184e-12,9.9895752173132e-13,2.011582463881371e-13,3.375572301597972e-14,4.855234367358857e-15,6.110560320977333e-16,6.835957440503639e-17,6.8827211427989764e-18,6.299822498341941e-19,5.285765488667771e-20,4.093788133316882e-21,2.944137921169192e-22,1.976185534965779e-23,1.5360403542297786e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16631082828223293, "-10": 2.508284846744675e-08, "-11": 2.2657329729704986e-09, "-12": 1.87984440329577e-10, "-13": 1.441972187248437e-11, "-14": 1.028190585939551e-12, "-15": 6.815860839286749e-14, "-16": 3.860789318854248e-15, "-2": 0.06386506777304952, "-3": 0.018860553871862123, "-4": 0.004379638554963083, "-5": 0.0008344942478309461, "-6": 0.00013451992205878194, "-7": 1.876782108603778e-05, "-8": 2.3062584124871627e-06, "-9": 2.530910955083124e-07, "0": 0.24684455517182746, "1": 0.22201259744151539, "10": 5.262671305038148e-06, "11": 8.322868412768977e-07, "12": 1.2089855753517692e-07, "13": 1.6236447454793378e-08, "14": 2.0269482592837183e-09, "15": 2.352473102626231e-10, "16": 2.33300122552421e-11, "2": 0.15177962376625476, "3": 0.0784764681040452, "4": 0.03190495886813065, "5": 0.010643345941437447, "6": 0.003003836913604861, "7": 0.0007337337730576673, "8": 0.00015785834117884514, "9": 3.0329925593649384e-05} |
| Raw goal margin distribution | {"-1": 0.1360922067330201, "-10": 5.917383382968357e-08, "-11": 6.0964352056214e-09, "-12": 5.772492062910362e-10, "-13": 5.0556988914164177e-11, "-14": 4.1183760407834484e-12, "-15": 3.134288584506235e-13, "-16": 2.2224091538396057e-14, "-17": 1.325776885698732e-15, "-2": 0.056868034466971716, "-3": 0.018600935017848905, "-4": 0.004837305390572538, "-5": 0.0010389347735351685, "-6": 0.00018954760766736397, "-7": 3.0011374617183958e-05, "-8": 4.193106278974648e-06, "-9": 5.239003384404723e-07, "0": 0.20360664125252137, "1": 0.23460532332438783, "10": 1.6013225841511457e-05, "11": 2.888417684960948e-06, "12": 4.788310333464369e-07, "13": 7.342349569364297e-08, "14": 1.0471641557183432e-08, "15": 1.395284154846962e-09, "16": 1.7321384835561414e-10, "17": 1.8091057275807964e-11, "2": 0.17431631728201388, "3": 0.09982504435450283, "4": 0.04545096983622887, "5": 0.017090817747003016, "6": 0.005459184599549958, "7": 0.001513318260757688, "8": 0.00037018188875176156, "9": 8.097722461578636e-05} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Estoril", "away_goals": 0.0, "away_xg": 0.63, "date": "2026-10-31T00:00:00+00:00", "home": "Porto", "home_goals": 4.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Moreirense", "away_goals": 3.0, "away_xg": 1.33, "date": "2026-10-25T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 1.36, "date": "2026-10-10T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 2.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-20T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.75, "date": "2026-09-14T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.79, "source": "pipeline training history"}, {"away": "Arouca", "away_goals": 0.0, "away_xg": 1.08, "date": "2026-09-07T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 1.0, "away_xg": 0.36, "date": "2026-08-31T00:00:00+00:00", "home": "Benfica", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 2.0, "away_xg": 0.71, "date": "2026-08-22T00:00:00+00:00", "home": "Estoril", "home_goals": 0.0, "home_xg": 1.16, "source": "pipeline training history"}, {"away": "Estoril", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-08-16T00:00:00+00:00", "home": "Nacional", "home_goals": 2.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 1.0, "away_xg": 1.47, "date": "2026-08-07T00:00:00+00:00", "home": "Estoril", "home_goals": 1.0, "home_xg": 1.22, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 57.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 21.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 58.9% |
| P home draw | 74.6% |
| P draw away | 50.1% |
| P home away | 75.3% |
| Raw p home draw | 78.2% |
| Raw p draw away | 42.1% |
| Raw p home away | 79.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.8733 |
| Totals anchor target over 2 5 | 0.5125 |
| Totals anchor reference over odds | 1.87 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-05T16:49:08Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5971 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.49, "draw": 3.55, "home": 2.08}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.87, "under": 1.96}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market best over 2 5 last update utc | 2026-11-05T16:49:08Z |
| Market best under 2 5 last update utc | 2026-11-05T16:49:08Z |
| Home probability edge | +3.4% |
| Draw probability edge | -1.9% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1143 |
| Raw ev home | 0.2038 |
| Raw edge prob draw | -0.0618 |
| Raw ev draw | -0.2772 |
| Raw edge prob away | -0.0525 |
| Raw ev away | -0.2404 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,378.3893 |
| Elo away rating | 1,388.6236 |
| Elo rating diff | 49.7657 |
| Elo home expectancy | 0.5711 |
| Research p home | 0.5739 |
| Research p draw | 0.2134 |
| Research p away | 0.2128 |
| Research p over 1 5 | 0.8251 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.018623591117528, 1.152976438292012], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.855262+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.855973+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Estoril%22+%22CS+Maritimo%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.891435+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Estoril_vs_CS+Maritimo&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.1741572673293668, "goals_for": 0.5196294860897706, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.13586574280159558, "results": "LLLLLDLLLD", "xg_against": 1.7383780696529123, "xg_for": 1.0563300250269338, "xg_matches": 10}, "venue": {"goals_against": 1.7177832069357093, "goals_for": 0.6329817884866369, "last_match": "2026-10-25T00:00:00+00:00", "matches": 5, "points_per_game": 0.34490701073453883, "results": "LLDLD", "xg_against": 1.3851867116529304, "xg_for": 1.284754675915346, "xg_matches": 5}}}, "goal_rates": [2.018623591117528, 1.152976438292012], "h2h": [], "margin_distribution": {"-1": 0.1312120093294585, "-10": 5.917383382968357e-08, "-11": 6.0964352056214e-09, "-12": 5.772492062910362e-10, "-13": 5.0556988914164177e-11, "-14": 4.1183760407834484e-12, "-15": 3.134288584506235e-13, "-16": 2.2224091538396057e-14, "-17": 1.325776885698732e-15, "-2": 0.056868034466971716, "-3": 0.018600935017848905, "-4": 0.004837305390572538, "-5": 0.0010389347735351685, "-6": 0.00018954760766736397, "-7": 3.0011374617183958e-05, "-8": 4.193106278974648e-06, "-9": 5.239003384404723e-07, "0": 0.21336703605964458, "1": 0.22972512592082622, "10": 1.6013225841511457e-05, "11": 2.888417684960948e-06, "12": 4.788310333464369e-07, "13": 7.342349569364297e-08, "14": 1.0471641557183432e-08, "15": 1.395284154846962e-09, "16": 1.7321384835561414e-10, "17": 1.8091057275807964e-11, "2": 0.17431631728201388, "3": 0.09982504435450283, "4": 0.04545096983622887, "5": 0.017090817747003016, "6": 0.005459184599549958, "7": 0.001513318260757688, "8": 0.00037018188875176156, "9": 8.097722461578636e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.891650+00:00", "p_over_1_5": 0.8250579262659294, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Santa Clara vs Gil Vicente

The model's most likely 1X2 outcome is **Santa Clara win** at **41.7%**. Expected goals are 1.02 for Santa Clara and 0.85 for Gil Vicente (1.88 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 85.2%; Over 2.5 goals: 29.0%; Under 3.5 goals: 87.8%; Double Chance 1X: 72.5%; Double Chance X2: 58.3%; Double Chance 12 (either team wins): 69.2%; Under 4.5 goals: 95.8%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Santa Clara win | 41.7% | 2.40 |
| Draw | 30.8% | 3.25 |
| Gil Vicente win | 27.5% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Santa Clara expected goals | 1.02 |
| Gil Vicente expected goals | 0.85 |
| Expected total goals | 1.88 |
| Over 0.5 | 85.2% |
| Under 0.5 | 14.8% |
| Over 1.5 | 55.4% |
| Under 1.5 | 44.6% |
| Over 2.5 | 29.0% |
| Under 2.5 | 71.0% |
| Over 3.5 | 12.2% |
| Under 3.5 | 87.8% |
| Over 4.5 | 4.2% |
| Under 4.5 | 95.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.33% |
| 2 | 0-0 | 14.76% |
| 3 | 1-1 | 12.80% |
| 4 | 0-1 | 12.54% |
| 5 | 2-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Santa Clara win | 41.7% | 42.7% | 2.26 | -5.8% |
| Draw | 30.8% | 30.9% | 3.08 | -5.1% |
| Gil Vicente win | 27.5% | 26.4% | 3.58 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | 3145127655251c9de0251675640e2101 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T16:49:08Z |
| Market best draw last update utc | 2026-11-05T16:49:08Z |
| Market best away last update utc | 2026-11-05T16:49:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Santa Clara |
| Matched away-team name | Gil Vicente |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0243 |
| Dc lambda away | 0.8519 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.17 |
| Fair Under 0.5 odds | 6.77 |
| Fair Over 1.5 odds | 1.81 |
| Fair Under 1.5 odds | 2.24 |
| Fair Over 2.5 odds | 3.45 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.22 |
| Fair Under 3.5 odds | 1.14 |
| Fair Over 4.5 odds | 23.69 |
| Fair Under 4.5 odds | 1.04 |
| Score matrix json | [[0.14763089018066683,0.12541881902449784,0.050818239881101394,0.01443035324675157,0.003073233576859969,0.0005236054561625173,7.43415328042632e-05,9.04715580564696e-06,9.633867765245745e-07,9.118780665515148e-08,7.768110022557105e-09,6.015909317066314e-10,4.2706957555398934e-11,2.7985552116432317e-12],[0.17330517663069003,0.12796266459740593,0.05205347102424509,0.014781109624356477,0.0031479341928823683,0.0005363326534775985,7.614854101162567e-05,9.267063630753757e-06,9.8680367077436e-07,9.340429465077958e-08,7.95692827847623e-09,6.162137099849719e-10,4.3745029006216e-11,2.866579262875954e-12],[0.08513269593538511,0.07252287041445286,0.029383826570689147,0.007570195891650339,0.0016122252726463511,0.0002746846044104626,3.899973594482242e-05,4.74615836077656e-06,5.05394877936085e-07,4.783732923965873e-08,4.075168055354953e-09,3.155959609432868e-10,2.2404166350088816e-11,1.468128382131418e-12],[0.029067334428587274,0.02476189089157926,0.01054708408218284,0.0028488823615340953,0.000550471128152695,9.3787106951754e-05,1.331589884332049e-05,1.6205075007660596e-06,1.7255981117540507e-07,1.6333367948725313e-08,1.391407512897321e-09,1.0775570114697776e-10,7.649580325589712e-12,5.012713176604239e-13],[0.007443467414311185,0.006340943591543395,0.0027008626083208326,0.000766937257177742,0.00015536858391514884,2.401669393500792e-05,3.409891587274014e-06,4.1497423185581277e-07,4.418854899335346e-08,4.182595153022446e-09,3.563070603437628e-10,2.7593725601648352e-11,1.9588793745973467e-12,1.2836391062623965e-13],[0.0015248789264535336,0.0012990143864920628,0.000553302412093099,0.00015711581663323994,3.346096903357113e-05,5.422903452942826e-06,6.985550595584235e-07,8.501218934089054e-08,9.052526651889657e-09,8.568521700609653e-10,7.299355225498631e-11,5.652888409425343e-12,4.0129871087296106e-13,2.6296806493003406e-14],[0.00026032398734307424,0.00022176488824205396,9.445857479164627e-05,2.682246777175504e-05,5.712383277170173e-06,9.732534077913693e-07,1.314431763867169e-07,1.4513094592667252e-08,1.5454275042217102e-09,1.462799240019752e-10,1.2461299217733084e-11,9.650487164706031e-13,6.850883615596223e-14,4.489333154186319e-15],[3.8093091782408275e-05,3.245075618324429e-05,1.3822080692209351e-05,3.92491962453546e-06,8.358904713101412e-07,1.4241573267575643e-07,2.022019392263895e-08,2.3407263236040584e-09,2.2614171042099305e-10,2.1405075374738393e-11,1.8234563002585617e-12,1.412151438913031e-13,1.0024867128958677e-14,6.569220978428502e-16],[4.877376838411771e-06,4.154941465533545e-06,1.7697564852946245e-06,5.025402552957811e-07,1.0702604155906174e-07,1.823467624906614e-08,2.5889603834157122e-09,3.150692093621486e-10,3.191386025109856e-11,2.740670656337229e-12,2.3347234652253433e-13,1.8080954835136337e-14,1.28356750410894e-15,8.41112252836156e-17],[5.551033874770617e-07,4.7288166543178604e-07,2.014192982300799e-07,5.719504711247906e-08,1.2180834121696018e-08,2.0753226356608984e-09,2.9465442726503633e-10,3.585861646556716e-11,3.818406322330759e-12,3.4379772128155896e-13,2.6571924772390447e-14,2.0578273138050653e-15,1.460852202304644e-16,9.572855989324209e-18],[5.6859620016558606e-08,4.84375927364699e-08,2.0631516614258626e-08,5.858527832851881e-09,1.2476911783806888e-09,2.1257671838710903e-10,3.01816547123467e-11,3.673022634249217e-12,3.911219737701991e-13,3.702101356570609e-14,2.999933775012431e-15,2.1078466059169308e-16,1.496360912170209e-17,9.8055419279657e-19],[5.294699823432003e-09,4.510450714137234e-09,1.921182156033359e-09,5.455391061906318e-10,1.1618351054660699e-10,1.9794889817804008e-11,2.8104795957097528e-12,3.420274755152705e-13,3.642081049536336e-14,3.4473525136561686e-15,2.9367318498944353e-16,2.1633907625847577e-17,1.3933933879879766e-18,9.13080338903703e-20],[4.5194977316203793e-10,3.8500712884446935e-10,1.6399000294211527e-10,4.656662011370837e-11,9.917297106122261e-12,1.6896700967506597e-12,2.398994575927107e-13,2.919509039779961e-14,3.1088404613441308e-15,2.9426223176266445e-16,2.5067621161896205e-17,1.9413285247844398e-18,1.3109349819122675e-19,7.79395368590993e-21],[3.561040360061314e-11,3.0335802917527446e-11,1.2921237133004892e-11,3.6691159837601e-12,7.814119478484352e-13,1.3313389599955684e-13,1.890235821709707e-14,2.3003639208582655e-15,2.4495435141791513e-16,2.3185755275794047e-17,1.975148921166392e-18,1.5296277682646617e-19,1.085883192911806e-20,6.768666583107376e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1856176870595443, "-10": 8.407229170209827e-09, "-11": 6.468040890949788e-10, "-12": 4.5573536818274885e-11, "-13": 2.7985552116432317e-12, "-2": 0.06730885835590071, "-3": 0.017866712117767834, "-4": 0.0036502315317881273, "-5": 0.0006046769719099579, "-6": 8.413068671001628e-05, "-7": 1.0083216212687524e-05, "-8": 1.0609759801080373e-06, "-9": 9.946810883880721e-08, "0": 0.3079871890138275, "1": 0.25717652314606365, "10": 6.153772984962173e-08, "11": 5.6926281894094774e-09, "12": 4.822855760795653e-10, "13": 3.561040360061314e-11, "2": 0.11275842267614188, "3": 0.035989257323507245, "4": 0.008840974427110439, "5": 0.0017609808318938525, "6": 0.0002946029627869936, "7": 4.245542896608776e-05, "8": 5.3714456099950084e-06, "9": 6.055095104016264e-07} |
| Raw goal margin distribution | {"-1": 0.20300614974685682, "-10": 9.194809238929159e-09, "-11": 7.073959914475889e-10, "-12": 4.9842816093580296e-11, "-13": 3.0607208147542756e-12, "-2": 0.07361427887152071, "-3": 0.019540446242604228, "-4": 0.003992181244641666, "-5": 0.0006613224518235209, "-6": 9.201195777792813e-05, "-7": 1.1027800921504509e-05, "-8": 1.1603670539571864e-06, "-9": 1.087861729011307e-07, "0": 0.30560743218881964, "1": 0.24274335212627252, "10": 5.8084130865452963e-08, "11": 5.373148498165784e-09, "12": 4.552189134045225e-10, "13": 3.361188896574686e-11, "2": 0.10643023385665801, "3": 0.033969480792309506, "4": 0.008344804347792535, "5": 0.0016621516806230624, "6": 0.0002780693581918849, "7": 4.007276020810739e-05, "8": 5.06999121530855e-06, "9": 5.715273171173151e-07} |
| Research history json | {"away": [{"away": "Guimaraes", "away_goals": 0.0, "away_xg": 0.42, "date": "2026-11-02T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.65, "source": "pipeline training history"}, {"away": "Porto", "away_goals": 1.0, "away_xg": 1.08, "date": "2026-10-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 0.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": 1.52, "date": "2026-10-19T00:00:00+00:00", "home": "Sp Braga", "home_goals": 1.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.49, "date": "2026-10-09T00:00:00+00:00", "home": "Moreirense", "home_goals": 0.0, "home_xg": 1.09, "source": "pipeline training history"}, {"away": "Maritimo", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.2, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Benfica", "home_goals": 3.0, "home_xg": 2.91, "source": "pipeline training history"}, {"away": "Academico Viseu", "away_goals": 1.0, "away_xg": 0.33, "date": "2026-09-06T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 0.0, "away_xg": 0.27, "date": "2026-08-30T00:00:00+00:00", "home": "Famalicao", "home_goals": 0.0, "home_xg": 0.23, "source": "pipeline training history"}, {"away": "Casa Pia", "away_goals": 0.0, "away_xg": 0.76, "date": "2026-08-24T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-08-09T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": 1.53, "source": "pipeline training history"}], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Santa Clara", "away_goals": 2.0, "away_xg": 0.82, "date": "2026-11-01T00:00:00+00:00", "home": "Maritimo", "home_goals": 0.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Benfica", "away_goals": 2.0, "away_xg": 1.81, "date": "2026-10-26T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.56, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 0.61, "date": "2026-10-10T00:00:00+00:00", "home": "Casa Pia", "home_goals": 0.0, "home_xg": 0.43, "source": "pipeline training history"}, {"away": "Sp Braga", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-20T00:00:00+00:00", "home": "Santa Clara", "home_goals": 0.0, "home_xg": 1.04, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Arouca", "home_goals": 1.0, "home_xg": 0.72, "source": "pipeline training history"}, {"away": "Rio Ave", "away_goals": 0.0, "away_xg": 0.32, "date": "2026-09-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 4.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-08-29T00:00:00+00:00", "home": "Alverca", "home_goals": 1.0, "home_xg": 0.41, "source": "pipeline training history"}, {"away": "Famalicao", "away_goals": 0.0, "away_xg": 1.05, "date": "2026-08-23T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-15T00:00:00+00:00", "home": "Academico Viseu", "home_goals": 0.0, "home_xg": 0.69, "source": "pipeline training history"}, {"away": "Nacional", "away_goals": 2.0, "away_xg": 1.24, "date": "2026-08-10T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": 1.44, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 30.1% |
| Raw p over 1 5 | 55.3% |
| Raw p under 3 5 | 87.9% |
| Raw p btts yes | 36.1% |
| P home draw | 72.5% |
| P draw away | 58.3% |
| P home away | 69.2% |
| Raw p home draw | 69.9% |
| Raw p draw away | 60.7% |
| Raw p home away | 69.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2897 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T16:49:08Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.58, "draw": 3.08, "home": 2.26}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.08 |
| Reference away odds | 3.58 |
| Market reference 1x2 last update utc | 2026-11-05T16:49:08Z |
| Market reference home last update utc | 2026-11-05T16:49:08Z |
| Market reference draw last update utc | 2026-11-05T16:49:08Z |
| Market reference away last update utc | 2026-11-05T16:49:08Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.53 |
| Reference Under 2.5 odds | 1.51 |
| Market reference over 2 5 last update utc | 2026-11-05T16:49:09Z |
| Market reference under 2 5 last update utc | 2026-11-05T16:49:09Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.1% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0334 |
| Raw ev home | -0.1107 |
| Raw edge prob draw | -0.0034 |
| Raw ev draw | -0.0587 |
| Raw edge prob away | 0.0368 |
| Raw ev away | 0.0773 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,480.8777 |
| Elo away rating | 1,467.9622 |
| Elo rating diff | 72.9156 |
| Elo home expectancy | 0.6034 |
| Research p home | 0.4001 |
| Research p draw | 0.3088 |
| Research p away | 0.2911 |
| Research p over 1 5 | 0.5865 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.0243068462432732, 0.8518803453551739], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:50:21.855262+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-05T16:50:21.671560+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/por.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:50:21.897475+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Santa+Clara%22+%22Gil+Vicente%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:49:35.505992+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:49:35.684657+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:50:21.932913+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Santa+Clara_vs_Gil+Vicente&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7142214406459612, "goals_for": 0.7243555948174364, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 1.390678704648646, "results": "DLWWDLLDWW", "xg_against": 0.9698401540895999, "xg_for": 1.0809685833604397, "xg_matches": 10}, "venue": {"goals_against": 0.9955634945558121, "goals_for": 1.1034760336115474, "last_match": "2026-10-19T00:00:00+00:00", "matches": 4, "points_per_game": 1.9072673778740439, "results": "WWLD", "xg_against": 1.4159916672192816, "xg_for": 1.1644490402329988, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.5739054067991304, "goals_for": 1.4663234401593819, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.0720961954158974, "results": "WLWDWWDWWD", "xg_against": 1.0399163493907206, "xg_for": 1.1824774148588095, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.5119397621276964, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.4751375496189745, "results": "LDWWD", "xg_against": 1.0078220045059325, "xg_for": 1.437884392379623, "xg_matches": 5}}}, "goal_rates": [1.0898624982714105, 0.8825817453138558], "h2h": [{"away": "Gil Vicente", "away_goals": 0.0, "away_xg": null, "date": "2026-03-21T00:00:00+00:00", "home": "Santa Clara", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2025-11-03T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 1.0, "away_xg": null, "date": "2025-03-15T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 1.0, "away_xg": null, "date": "2024-10-25T00:00:00+00:00", "home": "Santa Clara", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Gil Vicente", "away_goals": 2.0, "away_xg": null, "date": "2023-05-06T00:00:00+00:00", "home": "Santa Clara", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Santa Clara", "away_goals": 0.0, "away_xg": null, "date": "2022-12-29T00:00:00+00:00", "home": "Gil Vicente", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.19209634691508035, "-10": 1.1995097212611671e-08, "-11": 9.554431461821098e-10, "-12": 6.967895312058438e-11, "-13": 4.404658678886521e-12, "-2": 0.07378323529081524, "-3": 0.02016241368241369, "-4": 0.004250532097376464, "-5": 0.000727476970091437, "-6": 0.00010465282247878002, "-7": 1.2974993715714461e-05, "-8": 1.4127605146289793e-06, "-9": 1.3708928714259953e-07, "0": 0.30876451898828705, "1": 0.23721157351065622, "10": 9.889434439540528e-08, "11": 9.727232611800724e-09, "12": 8.759974410879219e-10, "13": 6.83801814696946e-11, "2": 0.11251002760789781, "3": 0.03796582366147248, "4": 0.009883491054768509, "5": 0.0020888299756240476, "6": 0.0003710663360212458, "7": 5.680996670948259e-05, "8": 7.638405239834364e-06, "9": 9.152809713152993e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:50:21.933129+00:00", "p_over_1_5": 0.5864842399988973, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
