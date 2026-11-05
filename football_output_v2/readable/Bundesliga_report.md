# Bundesliga — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,604 |
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
| Training sha256 | 7293b4234bd116739f5796bbb73debf914fb73b1c84db63d4b9410518b6b98d7 |
| Training as of utc | 2026-11-05T12:27:56.921923+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 71, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-05T12:27:56.921923+00:00', 'observations': 409, 'observations_sha256': '8854068cc055d5834e5fc899e9c0017f55af39edc70799b735d70a84a86c9420', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 116, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'e16127c25c5c339405940fbf757bda96bd6dc7da54933740f733b123431bd62f', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694716449928761, 'audit_candidate_poisson_score': 0.6673753164537862, 'audit_gain': 0.00209632853908992, 'audit_gain_lower95': -0.006062801738558959, 'audit_baseline_briers': [0.5838692910520525, 0.13632337444950357, 0.27438171226499136, 0.23546961438971004], 'audit_candidate_briers': [0.5818232810954291, 0.13599221629469402, 0.27350506640901034, 0.2362671929723898], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1586.562 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261105T122756921923Z_b4e450daf8f69fe8fcaaaf4887248da41641bff6c60bf0be0368274c36043ffa.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5} |
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

## 2026-11-06 — Hamburger SV vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **38.8%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Monchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.0%; Double Chance 1X: 65.1%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 38.8% | 2.58 |
| Draw | 26.3% | 3.80 |
| Borussia Monchengladbach win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Monchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.2% |
| Under 2.5 | 41.8% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 2-1 | 8.68% |
| 3 | 1-2 | 8.02% |
| 4 | 1-0 | 6.67% |
| 5 | 2-2 | 6.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 38.8% | 39.3% | 2.49 | -3.4% |
| Draw | 26.3% | 26.0% | 3.86 | +1.5% |
| Borussia Monchengladbach win | 34.9% | 34.7% | 2.82 | -1.5% |
| Over 2.5 | 58.2% | 58.5% | 1.69 | -1.6% |
| Under 2.5 | 41.8% | 41.5% | 2.36 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | 295076c39e49863cb54db085ac3cd340 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4419 |
| Dc lambda away | 1.3952 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.29 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.39 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Score matrix json | [[0.05784912526603558,0.06136041504054694,0.052045079967631434,0.025865886561694893,0.009641316067319473,0.0028749828555302117,0.0007144189273434829,0.00015216818307475292,2.835977697718032e-05,4.69817559868568e-06,7.00483948673567e-07,9.494551314123271e-08,1.1796743678655192e-08,1.3529686511678247e-09,1.440882747681755e-10,1.432208759153363e-11],[0.06668653225281075,0.12142504461629282,0.08019498517404165,0.039856109177248855,0.014856067077960193,0.004429990454780004,0.0011008305746095053,0.0002344722151110191,4.369888365314404e-05,7.23930336385242e-06,1.0793585083060335e-06,1.4629920875207475e-07,1.8177312533674586e-08,2.084756157331825e-09,2.220220828937839e-10,2.206855293101083e-11],[0.0581962041057925,0.08676880204571877,0.0646594438747119,0.030706649759711387,0.011445674401908372,0.003413031731944486,0.0008481213946144961,0.00018064623809058812,3.366726815354671e-05,5.577432355715487e-06,8.315785048741603e-07,1.1271442837770138e-07,1.4004487168129688e-08,1.6061747741832374e-09,1.7105418664982758e-10,1.7002445535828335e-11],[0.029891033749665504,0.04456663849848023,0.03322376341494792,0.016505395297137796,0.005878786169853866,0.0017530189168828896,0.0004356164739567949,9.278445016276287e-05,1.7292355474032323e-05,2.864709500264025e-06,4.2711962982162636e-07,5.789296457527514e-08,7.19305674693749e-09,8.249717506608625e-10,8.785773135438335e-11,8.73288354708532e-12],[0.011514589899189543,0.017167909607715557,0.012798420216400291,0.0063606874212163555,0.0023699676705229893,0.0006752959460177182,0.0001678076808233374,3.5742319974395684e-05,6.661341435764691e-06,1.1035401235068222e-06,1.6453453622508828e-07,2.230146172646374e-08,2.770901108882207e-09,3.1779467605005744e-10,3.3844454979085885e-11,3.364071431058902e-12],[0.0035485097412665217,0.005290722032961821,0.003944154260666755,0.001960205397929659,0.0007306519246200236,0.00021779047767434145,5.171414659786261e-05,1.101489255935508e-05,2.0528594749498695e-06,3.4008357331232805e-07,5.0705444977297e-08,6.8727549025787846e-09,8.539226896519159e-10,9.793640186574431e-11,1.0430017849753864e-11,1.0367230051561925e-12],[0.0009113019145062835,0.001358723934639061,0.001012908401252087,0.0005034053904897203,0.0001876406002217363,5.595330604993583e-05,1.3898657761938107e-05,2.8287628918382544e-06,5.272001223438858e-07,8.733773726123334e-08,1.3021795754521837e-08,1.7650098653574696e-09,2.1929808247966092e-10,2.515129928550087e-11,2.678559713189051e-12,2.662435017225971e-13],[0.00020060039040978447,0.0002990891903210577,0.00022296652460189494,0.00011081214278073547,4.130439875307323e-05,1.2316724962019041e-05,3.0606448378724523e-06,6.516482832177616e-07,1.1604995960484223e-07,1.9225224827495726e-08,2.8664235975063813e-09,3.885229060005318e-10,4.82730039971114e-11,5.536431314004465e-12,5.89618122872866e-13,5.860686731746445e-14],[3.863752669998963e-05,5.760739823637198e-05,4.2945455040796435e-05,2.1343463572665584e-05,7.955616668486025e-06,2.3723173649079173e-06,5.895090552960074e-07,1.255629133232339e-07,2.339212930037664e-08,3.7029595808276066e-09,5.521002130449051e-10,7.483317516724489e-11,9.297835747064047e-12,1.0663688753572453e-12,1.1356601010975375e-13,1.1288235262930142e-14],[6.615068412901512e-06,9.862869416612134e-06,7.352621851908827e-06,3.6541798546720136e-06,1.3620682539410263e-06,4.0616061653823014e-07,1.0092889125869115e-07,2.1497423171153393e-08,4.0065019795792714e-09,6.634698795337608e-10,9.452418392170345e-11,1.2812066805665907e-11,1.5918674100525803e-12,1.8257128927144591e-13,1.9443452788516278e-14,1.9326404897762314e-15],[1.019299641057023e-06,1.5197453191168857e-06,1.1329474385876273e-06,5.630635968874661e-07,2.0987775117026968e-07,6.258429162145702e-08,1.555188491046054e-08,3.3124851255160897e-09,6.173520475940399e-10,1.0227260701446232e-10,1.5242552016997386e-11,1.974179899748875e-12,2.4528693860707397e-13,2.813196145617449e-14,2.995993875073305e-15,2.977958253128819e-16],[1.427830706018574e-07,2.1288529344647273e-07,1.587028069040604e-07,7.887371492091134e-08,2.9399588262414814e-08,8.76678159121791e-09,2.178501582576368e-09,4.640115413497993e-10,8.647841856042584e-11,1.4326304336611716e-11,2.136009185015652e-12,2.894068390693873e-13,3.4359692539995734e-14,3.940713483034557e-15,4.1967757836519517e-16,4.1715115592990694e-17],[1.833424382148061e-08,2.7335809908015137e-08,2.037843803657874e-08,1.0127880808070603e-08,3.7750919431987666e-09,1.125709865641214e-09,2.7973329759667547e-10,5.958199875677407e-11,1.1104372559713504e-11,1.839587534159371e-12,2.7427700663617476e-13,3.7176256768231036e-14,4.617243431786205e-15,5.06012383148817e-16,5.38892392194844e-17,5.356483069731585e-18],[2.1731373771107348e-09,3.240082919324041e-09,2.415433426959195e-09,1.2004463641502563e-09,4.4745741813377524e-10,1.3342912904545795e-10,3.31564743301578e-11,7.0621875525409426e-12,1.316188837338559e-12,2.180442492133205e-13,3.2509746276243545e-14,4.4064600596974365e-15,5.474916942853168e-16,6.276716913468119e-17,6.387431143176865e-18,6.348979364535645e-19],[2.391809999097186e-10,3.566117267122202e-10,2.6584871640446684e-10,1.3212416515387824e-10,4.924829594921827e-11,1.4685547650285203e-11,3.649285483420203e-12,7.772822363455392e-13,1.4486307469580886e-13,2.399850193582511e-14,3.578104956945371e-15,4.84986146868416e-16,6.025832156802269e-17,6.911027506771997e-18,7.357206485266741e-19,6.987847380522163e-20],[2.4569875133380125e-11,3.663294994052871e-11,2.7309317081593674e-11,1.3572458686761166e-11,5.059032625755304e-12,1.5085733071147269e-12,3.748729568299119e-13,7.984634020935188e-14,1.4881063537894e-14,2.4652468054484676e-15,3.675609351890833e-16,4.982021596395188e-17,6.190037825881777e-18,7.09935500515665e-19,7.56066161456794e-20,7.512195839932688e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17887079484911367, "-10": 8.616474975224164e-07, "-11": 1.1482022225187597e-07, "-12": 1.4061286906183931e-08, "-13": 1.5919931795974367e-09, "-14": 1.6615682769918634e-10, "-15": 1.432208759153363e-11, "-2": 0.10527925202756298, "-3": 0.04460848730562016, "-4": 0.015019227211687917, "-5": 0.0041749080836418016, "-6": 0.0009855947523494531, "-7": 0.0002018947998500558, "-8": 3.6491423385159505e-05, "-9": 5.897770083053752e-06, "0": 0.26304134157955644, "1": 0.19382958068406328, "10": 1.253814575773481e-06, "11": 1.7267149713461138e-07, "12": 2.185374791589588e-08, "13": 2.5570584209045487e-09, "14": 2.7581394985024735e-10, "15": 2.4569875133380125e-11, "2": 0.117722037182222, "3": 0.05155028405438292, "4": 0.017937410280691703, "5": 0.005152970556049841, "6": 0.0012572096711983846, "7": 0.00026615403334171844, "8": 4.9716129520314365e-05, "9": 8.30410693756927e-06} |
| Raw goal margin distribution | {"-1": 0.18741198237494658, "-10": 5.411918431561736e-07, "-11": 6.76250693166949e-08, "-12": 7.76036125560687e-09, "-13": 8.170397829080842e-10, "-14": 7.119453012599638e-11, "-2": 0.10629569490400151, "-3": 0.042869107596833426, "-4": 0.013661549544907763, "-5": 0.0035825624957785524, "-6": 0.0007962283374000566, "-7": 0.0001533401864418761, "-8": 2.6031245830784723e-05, "-9": 3.948782634663552e-06, "0": 0.2693423768580773, "1": 0.19399502449930214, "10": 7.522065721187829e-07, "11": 9.713867889791724e-08, "12": 1.1520332033565366e-08, "13": 1.2535014746005918e-09, "14": 1.1288256309901965e-10, "2": 0.11353057873384649, "3": 0.047319506569618086, "4": 0.015584551698832008, "5": 0.004223638264930674, "6": 0.000970128266256941, "7": 0.00019308391847464699, "8": 3.387533966744174e-05, "9": 5.310684743730099e-06} |
| Research history json | {"away": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 3.0, "away_xg": 2.6, "date": "2026-10-23T00:00:00+00:00", "home": "Stuttgart", "home_goals": 2.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-18T00:00:00+00:00", "home": "M'gladbach", "home_goals": 1.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-11T00:00:00+00:00", "home": "FC Koln", "home_goals": 2.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Mainz", "away_goals": 4.0, "away_xg": 2.82, "date": "2026-09-19T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 3.24, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-09-12T00:00:00+00:00", "home": "Freiburg", "home_goals": 5.0, "home_xg": 2.6, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": 3.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 0.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "M'gladbach", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 65.1% |
| P draw away | 61.2% |
| P home away | 73.7% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0686 |
| Totals anchor target over 2 5 | 0.5824 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.29 |
| Totals anchor reference last update utc | 2026-11-05T12:28:30Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5416 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.36, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.57, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:43Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:43Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.62, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:25:18Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.18, "under": 4.6}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.8, "draw": 3.7, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.82, "draw": 3.86, "home": 2.49}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.6, "home_away": 1.3, "home_draw": 1.49}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:30Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:43Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.58, "home_away": 1.31, "home_draw": 1.48}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.48 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:05Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:05Z |
| Market best over 2 5 last update utc | 2026-11-05T12:28:05Z |
| Market best under 2 5 last update utc | 2026-11-05T12:28:05Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0170 |
| Raw ev home | -0.0641 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0397 |
| Raw edge prob away | 0.0080 |
| Raw ev away | 0.0005 |
| Market p home draw | 65.2% |
| Market home draw odds | 1.49 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T12:28:05Z |
| Market reference home draw last update utc | 2026-11-05T12:28:43Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.1% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:28:05Z |
| Market reference draw away last update utc | 2026-11-05T12:28:43Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.7% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T12:28:43Z |
| Market reference home away last update utc | 2026-11-05T12:28:43Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home draw odds | 1.48 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T12:25:18Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T12:27:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.2% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T12:28:30Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market reference under 3 5 last update utc | 2026-11-05T12:28:30Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 9.857583967086907, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---

## 2026-11-07 — Borussia Dortmund vs Elversberg

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **73.9%**. Expected goals are 2.88 for Borussia Dortmund and 1.30 for Elversberg (4.18 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.4%; Under 3.5 goals: 39.3%; Double Chance 1X: 88.6%; Double Chance X2: 26.1%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 58.7%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 73.9% | 1.35 |
| Draw | 14.7% | 6.78 |
| Elversberg win | 11.4% | 8.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.88 |
| Elversberg expected goals | 1.30 |
| Expected total goals | 4.18 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 41.3% |
| Under 4.5 | 58.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.75% |
| 2 | 3-1 | 8.41% |
| 3 | 2-0 | 6.76% |
| 4 | 3-0 | 6.50% |
| 5 | 4-1 | 6.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 73.9% | 75.7% | 1.32 | -2.5% |
| Draw | 14.7% | 14.1% | 6.45 | -4.9% |
| Elversberg win | 11.4% | 10.2% | 9.75 | +10.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | 3ef62ef56758041178c5280225fe5db7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8827 |
| Dc lambda away | 1.2951 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.3% |
| P btts no | 31.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 55.79 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.80 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.85 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.42 |
| Fair Under 4.5 odds | 1.70 |
| Score matrix json | [[0.01792275938954127,0.012424639059980876,0.010401727570798382,0.004490354866008087,0.0014538416829399,0.00037656812472508294,8.128094586854429e-05,1.5037898614588767e-05,2.4344093598496817e-06,3.50305973709764e-07,4.5367410065285955e-08,5.341309521334149e-09,5.764517248873045e-10,5.742698745690816e-11,5.312322623034638e-12,4.586586906412793e-13,3.712496799221385e-14,2.828222742009891e-15,2.0348741215180198e-16,1.3870125521908378e-17],[0.04212536278135273,0.055800015453529805,0.02998533774682916,0.012944465844151662,0.00419102823032553,0.0010855429857893329,0.00023431075248425963,4.3350151779297996e-05,7.017736849219562e-06,1.0098363819783152e-06,1.3078184409727644e-07,1.5397535545652226e-08,1.6617527759536735e-09,1.6554630977959208e-10,1.5313974240106792e-11,1.3221876515981066e-12,1.070211362977766e-13,8.152993198986528e-15,5.865985951919794e-16,3.9983781110834794e-17],[0.06759723860454658,0.08754380093998296,0.04828602463512945,0.018657678623445702,0.006040794480409613,0.001564661872080549,0.0003377269306051891,6.248331989235064e-05,1.0115108678339755e-05,1.455541148167737e-06,1.88504156627753e-07,2.2193443380566816e-08,2.3951895442151675e-09,2.3861238326496896e-10,2.2073001177466823e-11,1.9057528198084247e-12,1.5425634328990398e-13,1.1751425571149037e-14,8.455017149279631e-16,5.763115659602138e-17],[0.06495478808733925,0.08412161732941466,0.05447209290099888,0.020029903442642733,0.005804653170074667,0.0015034975159842667,0.00032452481287263864,6.004077809072047e-05,9.719697938042304e-06,1.3986424413685853e-06,1.811353215028336e-07,2.132587723215249e-08,2.3015589465668296e-09,2.2928476236525688e-10,2.1210143247441964e-11,1.831254842844712e-12,1.4822629291323812e-13,1.1292049401065106e-14,8.124501215488098e-16,5.537829120243161e-17],[0.04681172540368425,0.06062490798435724,0.03925703909028012,0.016946996093128674,0.0046736779878066665,0.0010835431064564638,0.00023387908534855278,4.327028845398055e-05,7.0048081793538865e-06,1.0079759757702375e-06,1.3054090669493628e-07,1.5369168900095135e-08,1.6586913540878677e-09,1.6524132633085264e-10,1.528576153827204e-11,1.3197518053965089e-12,1.0682397288604261e-13,8.137973063613609e-15,5.855179135215418e-16,3.9910119599001264e-17],[0.026989082095976426,0.03495300813078039,0.022633462913741235,0.009770711608968887,0.003163462183498208,0.0006979409679934541,0.00013484189656694812,2.4947283128964728e-05,4.038589506984291e-06,5.811438507390245e-07,7.526275131477096e-08,8.861022694945337e-09,9.563107691783664e-10,9.526911652011905e-11,8.812934569240934e-12,7.608967521491134e-13,6.158886366988848e-14,4.6919104394179485e-15,3.3757762399106094e-16,2.3009993437091048e-17],[0.012967024573826594,0.01679332827064019,0.010874347958540951,0.004694381864737835,0.0015198994810537785,0.00039367814533538057,7.237958758880134e-05,1.1986033175678915e-05,1.9403582972712775e-06,2.792131487341164e-07,3.616032373097744e-08,4.257317778573914e-09,4.5946376390472266e-10,4.577247090694136e-11,4.2342136246237795e-12,3.655762299798005e-13,2.959064357363083e-14,2.254249246038501e-15,1.6219067140926096e-16,1.1055253723757797e-17],[0.005340055414162872,0.006915796530104255,0.0044782533079106455,0.0019332314171394821,0.0006259221154841553,0.00016212378556597546,3.499386637733064e-05,5.51467518734707e-06,7.990746660320087e-07,1.149850282240254e-07,1.4891475790618065e-08,1.7532405158831697e-09,1.892154939694862e-10,1.8849931971255123e-11,1.7437258071164338e-12,1.505509081962654e-13,1.2185962594910111e-14,9.283406399551603e-16,6.679305403137256e-17,4.552753576302935e-18],[0.0019242400371788325,0.002492043909678269,0.001613697544945998,0.000696622226826634,0.00022554529894501003,5.8419820576702844e-05,1.2609719097737445e-05,2.332941322519768e-06,3.2169171592380615e-07,4.143380130438086e-08,5.366006849477351e-09,6.317641548285942e-10,6.818206945662049e-11,6.7924002625490595e-12,6.28335616708467e-13,5.424964025964187e-14,4.391099960217473e-15,3.345190431552804e-16,2.406826499061046e-17,1.6405430340098007e-18],[0.0006163397915079832,0.0007982090560654404,0.0005168721101277696,0.0002231301655440255,7.224282825503536e-05,1.871204181312464e-05,4.038930429422013e-06,7.47248025475192e-07,1.209682040003398e-07,1.4827050676881485e-08,1.718747910310689e-09,2.0235593270377694e-10,2.1838919085732962e-11,2.175625951425511e-12,2.0125776177431503e-13,1.7376320688157116e-14,1.4064823419530724e-15,1.0714744175890677e-16,7.709136666764562e-18,5.254707999028624e-19],[0.00017767391704298023,0.00023010185544460287,0.00014900010299835064,6.432232847672977e-05,2.0825632956344935e-05,5.394170246051398e-06,1.164313256983993e-06,2.154111831137393e-07,3.487182709688199e-08,5.017976659014352e-09,5.535472345821094e-10,5.833368491818375e-11,6.29556350475648e-12,6.271735009423359e-13,5.801711225273433e-14,5.009118351593335e-15,4.054504193785287e-16,3.08876790704385e-17,2.222333406792514e-18,1.514788702543804e-19],[4.656230397633443e-05,6.030188739598943e-05,3.9047870412155404e-05,1.685669940104162e-05,5.4576916429344444e-06,1.4136289607212618e-06,3.0512699161267563e-07,5.645196073218472e-08,9.138722444569116e-09,1.315041388357845e-09,1.703083201426731e-10,1.7079267030131648e-11,1.6498535434431684e-12,1.643608903478761e-13,1.5204316207468127e-14,1.3127199266052262e-15,1.0625479523743753e-16,8.094612455993255e-18,5.823981670804516e-19,3.969747118858181e-20],[1.1185533056070957e-05,1.4486155048387027e-05,9.380361536369224e-06,4.049438113338095e-06,1.3110861162049249e-06,3.3959216187419654e-07,7.329981035126078e-08,1.3561297850957023e-08,2.1953699294162962e-09,3.159087429834718e-10,4.0912695077288444e-11,4.816835861806742e-12,4.427990190610021e-13,3.948396052407184e-14,3.652490684739922e-15,3.1535106466958255e-16,2.552529456228109e-17,1.9445462846644156e-18,1.3990789530055316e-19,9.536413328000068e-21],[2.4803719033262528e-06,3.212278913229382e-06,2.0800783548911374e-06,8.979556423670691e-07,2.9073099593682926e-07,7.530395312232446e-08,1.625410154375541e-08,3.0071934876537653e-09,4.868193462962466e-10,7.005219743962352e-11,9.07231679083751e-12,1.068124717406758e-12,1.1527553931944683e-13,9.781824327480872e-15,8.099332616671944e-16,6.992853327324618e-17,5.660188311011754e-18,4.3119965271402738e-19,3.102432497561266e-20,2.1146825599374753e-21],[5.107310214492032e-07,6.614372983072704e-07,4.2830695730074654e-07,1.8489719296819715e-07,5.986414308380033e-08,1.5505765424028384e-08,3.3468666021610497e-09,6.192083532252385e-10,1.0024050895822924e-10,1.4424381402289325e-11,1.8680721287325977e-12,2.199365454933312e-13,2.3736276751795168e-14,2.3646435745604304e-15,1.8632181289912625e-16,1.4398917831311976e-17,1.1654839960899325e-18,8.878791070961814e-20,6.3881892724707734e-21,4.354322762765231e-22],[9.815319664739092e-08,1.2711619714513384e-07,8.231279330967185e-08,3.5533871605179254e-08,1.1504797557741865e-08,2.9799255947180476e-09,6.432067800040052e-10,1.1900056332463993e-10,1.9264399409093258e-11,2.7721032888868424e-12,3.5900942629786463e-13,4.226779673280889e-14,4.5616799094855124e-15,4.544414105026191e-16,4.203841247407147e-17,3.0915843247219832e-18,2.2398478857423357e-19,1.706341869554697e-20,1.227693583409912e-21,8.368214979132888e-23],[1.7684302513516565e-08,2.2902578433161113e-08,1.4830330415524908e-08,6.402152516742815e-09,2.0728241903192443e-09,5.368944413912321e-10,1.1588683471205198e-10,2.1440381291624046e-11,3.4708749029894244e-12,4.994510095835194e-13,6.468287856852219e-14,7.615406624891504e-15,8.218797781897509e-16,8.187689909752014e-17,7.574078367005784e-18,6.539355971269784e-19,4.508593129042445e-20,3.074323286799116e-21,2.2119406666824204e-22,1.5077047945851128e-23],[2.998765349741263e-09,3.883639661366436e-09,2.514811140631554e-09,1.085626821656847e-09,3.514932722556549e-10,9.104234934242605e-11,1.9651180710128547e-11,3.635691735844315e-12,5.885637493712796e-13,8.469298578711778e-14,1.0968415340359103e-14,1.2913609396502883e-15,1.3936792805962716e-16,1.388404251568534e-17,1.2843528177513247e-18,1.1088927076020686e-19,8.975651637379234e-21,5.824291671211965e-22,3.7508355344300353e-23,2.556647564802115e-24],[4.802567181666856e-10,6.219706515118796e-10,4.027507338354886e-10,1.7386474555857873e-10,5.629216884399942e-11,1.4580567270177035e-11,3.147165734978598e-12,5.822614235131748e-13,9.425935734828964e-14,1.3563707280187283e-14,1.7566079837838906e-15,2.0681336967515818e-16,2.2319980372383013e-17,2.2235500000175375e-18,2.0569100855944146e-19,1.7759081169785058e-20,1.4374639213258599e-21,1.0950765409320103e-22,6.711166583665815e-24,4.09450899213122e-25],[7.286572958494825e-11,9.436691583585323e-11,6.110633115935015e-11,2.6379186495482187e-11,8.540786203668438e-12,2.212199500216309e-12,4.774957199544552e-13,8.834213417235874e-14,1.4301261353740527e-14,2.057919003445351e-15,2.6651688043379654e-16,3.1378232722757484e-17,3.3864422768802205e-18,3.3736247071853783e-19,3.1207945335905987e-20,2.6944514407512733e-21,2.1809555893207938e-22,1.6614770410911343e-23,1.1954138491970506e-24,6.940499552852787e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.06810352192376859, "-10": 6.340549711938697e-08, "-11": 7.264268487152143e-09, "-12": 7.660139733139585e-10, "-13": 7.480342741567797e-11, "-14": 6.800667195230672e-12, "-15": 5.782836127513527e-13, "-16": 4.617884119733077e-14, "-17": 3.4724524937978917e-15, "-18": 2.4347119326263677e-16, "-19": 1.3870125521908378e-17, "-2": 0.031151372697973367, "-3": 0.010618173418118066, "-4": 0.0029447763134365337, "-5": 0.0006841695872988684, "-6": 0.000136284729656762, "-7": 2.370868498503249e-05, "-8": 3.6558341254235527e-06, "-9": 5.057572524996465e-07, "0": 0.1474885532292654, "1": 0.20468284601342018, "10": 0.00024831708530522823, "11": 6.332549651232333e-05, "12": 1.4863819900253794e-05, "13": 3.2308906987951837e-06, "14": 6.538216801998629e-07, "15": 1.2375299175294583e-07, "16": 2.199707209521397e-08, "17": 3.681842332412493e-09, "18": 5.746236340025389e-10, "19": 7.286572958494825e-11, "2": 0.20244202309582673, "3": 0.15359614659177706, "4": 0.09481779328345424, "5": 0.04903524208975494, "6": 0.021741964486420386, "7": 0.008419107939335377, "8": 0.002889695755137514, "9": 0.0008898458574889957} |
| Raw goal margin distribution | {"-1": 0.08418385164956299, "-10": 7.837654812096241e-08, "-11": 8.979478349879316e-09, "-12": 9.468821122516506e-10, "-13": 9.246571188328669e-11, "-14": 8.40641338523111e-12, "-15": 7.148256138900626e-13, "-16": 5.708240347769816e-14, "-17": 4.292354012546502e-15, "-18": 3.009586323231036e-16, "-19": 1.7145083782952464e-17, "-2": 0.03850670954758929, "-3": 0.013125293825783991, "-4": 0.003640085054470119, "-5": 0.0008457129589389014, "-6": 0.00016846373196921998, "-7": 2.9306684341821357e-05, "-8": 4.5190349775824906e-06, "-9": 6.251746211125284e-07, "0": 0.16318434906358706, "1": 0.19289956126655555, "10": 0.00023402184278416646, "11": 5.9679942565450985e-05, "12": 1.4008132060642068e-05, "13": 3.0448931624535013e-06, "14": 6.161821457614796e-07, "15": 1.1662871745002873e-07, "16": 2.0730733615250577e-08, "17": 3.4698841862323675e-09, "18": 5.415434124128601e-10, "19": 6.867095871523312e-11, "2": 0.19078773916666408, "3": 0.1447538465819687, "4": 0.08935927499973331, "5": 0.046212356677378275, "6": 0.020490312169240313, "7": 0.007934432510514764, "8": 0.0027233403004534467, "9": 0.0008386187648242628} |
| Research history json | {"away": [{"away": "Mainz", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-30T00:00:00+00:00", "home": "Elversberg", "home_goals": 4.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 0.8, "date": "2026-10-24T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 4.0, "home_xg": 2.87, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 3.0, "away_xg": 3.92, "date": "2026-10-17T00:00:00+00:00", "home": "Elversberg", "home_goals": 4.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 0.24, "date": "2026-10-10T00:00:00+00:00", "home": "Union Berlin", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 1.01, "date": "2026-09-20T00:00:00+00:00", "home": "Schalke 04", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 2.0, "away_xg": 2.83, "date": "2026-09-13T00:00:00+00:00", "home": "Elversberg", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "Leverkusen", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-08-29T00:00:00+00:00", "home": "Elversberg", "home_goals": 3.0, "home_xg": 1.27, "source": "pipeline training history"}, {"away": "Heidenheim", "away_goals": 2.0, "away_xg": null, "date": "2025-05-26T00:00:00+00:00", "home": "Elversberg", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 2.0, "away_xg": null, "date": "2025-05-22T00:00:00+00:00", "home": "Heidenheim", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 69.6% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.0% |
| Raw p btts yes | 69.0% |
| P home draw | 88.6% |
| P draw away | 26.1% |
| P home away | 85.3% |
| Raw p home draw | 85.9% |
| Raw p draw away | 30.4% |
| Raw p home away | 83.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7937 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.59, "draw": 6.35, "home": 1.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.75, "draw": 6.45, "home": 1.32}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.35 |
| Reference away odds | 8.59 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:06Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:06Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +7.7% |
| Under 2.5 probability edge | -7.7% |
| Raw edge prob home | -0.0608 |
| Raw ev home | -0.0809 |
| Raw edge prob draw | 0.0224 |
| Raw ev draw | 0.0525 |
| Raw edge prob away | 0.0383 |
| Raw ev away | 0.3699 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.850572490037669, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,639.4058 |
| Elo away rating | 1,432.5460 |
| Elo rating diff | 266.8598 |
| Elo home expectancy | 0.8229 |

</details>


---

## 2026-11-07 — FSV Mainz 05 vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **72.2%**. Expected goals are 1.19 for FSV Mainz 05 and 2.70 for Bayern Munich (3.88 combined). The most likely exact score is 1-2 at 9.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 75.5%; Under 3.5 goals: 45.1%; Double Chance 1X: 27.8%; Double Chance X2: 86.7%; Double Chance 12 (either team wins): 85.5%; Under 4.5 goals: 64.3%; BTTS Yes (both teams score): 64.5%; BTTS No (at least one team does not score): 35.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 13.3% | 7.50 |
| Draw | 14.5% | 6.90 |
| Bayern Munich win | 72.2% | 1.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.19 |
| Bayern Munich expected goals | 2.70 |
| Expected total goals | 3.88 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 90.7% |
| Under 1.5 | 9.3% |
| Over 2.5 | 75.5% |
| Under 2.5 | 24.5% |
| Over 3.5 | 54.9% |
| Under 3.5 | 45.1% |
| Over 4.5 | 35.7% |
| Under 4.5 | 64.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.30% |
| 2 | 1-3 | 8.37% |
| 3 | 0-2 | 7.85% |
| 4 | 0-3 | 7.06% |
| 5 | 1-1 | 5.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 13.3% | 13.1% | 7.95 | +6.0% |
| Draw | 14.5% | 13.3% | 6.85 | -0.8% |
| Bayern Munich win | 72.2% | 73.6% | 1.36 | -1.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | fe97f5adf397dd6b0a8a9e0a5272f307 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1852 |
| Dc lambda away | 2.6991 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 64.5% |
| P btts no | 35.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.20 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.77 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.08 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.80 |
| Fair Under 4.5 odds | 1.55 |
| Score matrix json | [[0.021643701850532143,0.052739667003518495,0.0784843352254071,0.07061240578280745,0.04764751943284993,0.025721101927464168,0.011570645793627722,0.004461478843074287,0.0015052482458145393,0.0004514242646087818,0.00012184400846823397,2.989721756734676e-05,6.724636363993042e-06,1.3961906694619656e-06,2.6917577652116816e-07,4.843552309903991e-08,8.17077573875715e-09,1.2972797775919186e-09,1.9452723868625956e-10,2.76341493217923e-11],[0.018428377678118158,0.05967618278068937,0.09301818832968989,0.08368852256509123,0.05647096230500567,0.030484176189613656,0.013713316248863149,0.005287662538800059,0.0017839924923870169,0.0005350197226156553,0.0001444072743177615,3.543363151673747e-05,7.9699151424053e-06,1.6547394618706892e-06,3.1902217177895013e-07,5.740488973416249e-08,9.683852889682563e-09,1.537512094888453e-09,2.3055009985630123e-10,3.2751484720649424e-11],[0.013860214673540648,0.03741013158692259,0.044247875743962245,0.04959304764852699,0.03346417212912433,0.018064642031668708,0.00812638490087136,0.0031334201178194335,0.0010571775193038062,0.00031704775975633775,8.557442067954433e-05,2.0997643670948382e-05,4.722898305494683e-06,9.805833639209443e-07,1.8904960060281346e-07,3.40176089215879e-08,5.7385620280943916e-09,9.111155059845151e-10,1.3662186566447408e-10,1.9408228183833277e-11],[0.005475623702872691,0.014779266271826907,0.019945372745297178,0.01572729699084029,0.013220373451866321,0.007136626987556403,0.0032104138954516656,0.0012378906007093826,0.0004176491071162698,0.0001252530548158539,3.380707566723517e-05,8.295340158663563e-06,1.865830689995922e-06,3.873897797830103e-07,7.468603470157824e-08,1.3439014482343325e-08,2.2670793347396185e-09,3.599457712691556e-10,5.3973906146720626e-11,7.667424839893308e-12],[0.0016224020862045984,0.004379028533207209,0.00590972208976334,0.0053169806824190395,0.0031444035424211996,0.0021145497100177103,0.0009512308522640847,0.00036678128411751825,0.0001237475070340271,3.711190331251748e-05,1.0016880828064143e-05,2.4578710863808706e-06,5.528370407129728e-07,1.1478180769883131e-07,2.212912812957169e-08,3.981918100261126e-09,6.717251662752558e-10,1.0665027436440306e-10,1.599221982458547e-11,2.271822669175315e-12],[0.0003845682131794558,0.0010379887900766537,0.0014008187512653642,0.001260317511875854,0.0008504313437977624,0.00040234854926079366,0.00022547625664864803,8.694048427336184e-05,2.9332653150623803e-05,8.796868831678604e-06,2.3743645267936275e-06,5.826047069047835e-07,1.310424553408735e-07,2.7207456812084536e-08,5.245407002598871e-09,9.438591961051279e-10,1.5922325861061e-10,2.5279988109091327e-11,3.790736867887832e-12,5.385044755392135e-13],[7.596386033892878e-05,0.00020503419882485712,0.0002767040965281719,0.00024895084974214417,0.00016798592711029573,9.068222658837049e-05,3.575231026159311e-05,1.717337673475012e-05,5.794086695003164e-06,1.7376478149994111e-06,4.690088497327039e-07,1.1508206105288624e-07,2.5884850684055985e-08,5.374296103058776e-09,1.0361266254221605e-09,1.8644075535979268e-10,3.145141216900675e-11,4.9935627029909255e-12,7.487852509523081e-13,1.0637093074736267e-13],[1.28615668463615e-05,3.471467935160576e-05,4.684922828145643e-05,4.215028016126539e-05,2.8441975185795923e-05,1.5353557781811834e-05,6.906802798197835e-06,2.334061000046163e-06,9.81006402372203e-07,2.942040258135213e-07,7.940866413921575e-08,1.9484734114943804e-08,4.3826068856385215e-09,9.099309628714073e-10,1.7542831281486192e-10,3.156659268298476e-11,5.325090618345636e-12,8.454683611320152e-13,1.2677806940990026e-13,1.8009838233771196e-14],[1.9054115125231738e-06,5.142899809972418e-06,6.9406052922367485e-06,6.244466948291973e-06,4.213613131688167e-06,2.2745942314120258e-06,1.0232269305614531e-06,3.945419628071146e-07,1.1666387557007953e-07,4.358564897358014e-08,1.1764210741380383e-08,2.886618492487166e-09,6.492731184708922e-10,1.3480417689132182e-10,2.598930059244816e-11,4.6765180189771695e-12,7.888999132555404e-13,1.2525419087883367e-13,1.878187905678256e-14,2.6681160638694345e-15],[2.5091762495366834e-07,6.772522351269551e-07,9.139863930824895e-07,8.223141329151843e-07,5.548774070734629e-07,2.995341313559314e-07,1.3474552322040165e-07,5.195598515148351e-08,1.7529312198855273e-08,4.607396120010848e-09,1.5491917621368417e-09,3.8012967357538696e-10,8.550072662111968e-11,1.77519363544799e-11,3.4224489229776016e-12,6.15835889865557e-13,1.0388773829654697e-13,1.6494328854554005e-14,2.473326341381392e-15,3.513557787631486e-16],[2.973829468791011e-08,8.026668732405733e-08,1.0832398363106596e-07,9.745915622778782e-08,6.576304813287232e-08,3.5500233469030524e-08,1.5969791194001802e-08,6.15772765074114e-09,2.0775417906262723e-09,6.230552187223934e-10,1.473871848624712e-10,4.50522686658272e-11,1.0133388616119712e-11,2.1039267954494085e-12,4.056223417730088e-13,7.29877352202538e-14,1.2312583368719756e-14,1.954877471228251e-15,2.9313408180454353e-16,4.1642039657788115e-17],[3.2041162770533695e-09,8.64823629125989e-09,1.1671235448771889e-08,1.0500617876528527e-08,7.085559382691974e-09,3.824929340805762e-09,1.7206456672395256e-09,6.634568526023254e-10,2.2384220539419403e-10,6.713032434314621e-11,1.8119158514507733e-11,3.896534492496851e-12,1.091809592559332e-12,2.2668502554616157e-13,4.370328430902832e-14,7.863974477983476e-15,1.3266042723132367e-15,2.1062588796504907e-16,3.158337398717323e-17,4.486670754912661e-18],[3.1645496564505686e-10,8.541441950907693e-10,1.1527111045960826e-09,1.0370949060639712e-09,6.998062046262158e-10,3.7776964956234507e-10,1.6993979569753623e-10,6.552640333337981e-11,2.2107804865020992e-11,6.630135315591112e-12,1.7895410744890327e-12,4.3910488108777794e-13,8.65605893053994e-14,2.2388576371338888e-14,4.316360624499068e-15,7.766864739229977e-16,1.3102224548652932e-16,2.0802493535358357e-17,3.1193360870340875e-18,4.431266273870366e-19],[2.8850507368221512e-11,7.787045889376075e-11,1.0509015129148289e-10,9.454967523721322e-11,6.379980172452428e-11,3.444043305173884e-11,1.549303964288232e-11,5.973898934811227e-12,2.0155202363576955e-12,6.044549415897432e-13,1.631485473771624e-13,4.003223201576851e-14,9.00425608298284e-15,1.6384668966394533e-15,3.9351316149257826e-16,7.080880779683051e-17,1.1945011673635236e-17,1.8965178561691227e-18,2.8438305140667635e-19,4.039888583332946e-20],[2.4423635621745046e-12,6.592188100699353e-12,8.896493672774743e-12,8.004180954861245e-12,5.401024980849129e-12,2.9155833440811595e-12,1.311576084543344e-12,5.057253550614233e-13,1.7062553255224908e-13,5.117063299695148e-14,1.3811475210816922e-14,3.388961710098891e-15,7.622627457078614e-16,1.5826344736413713e-16,2.674150044662306e-17,5.994378186724337e-18,1.0112148423972148e-18,1.6055128763603133e-19,2.4074682416875702e-20,3.420001092266895e-21],[1.9297628683349882e-13,5.208626600407998e-13,7.029306944299726e-13,6.32427188046204e-13,4.267463542451771e-13,2.3036637804792865e-13,1.0363038763543006e-13,3.9958424981748605e-14,1.3481482536369712e-14,4.043099440068484e-15,1.0912737330159746e-15,2.6776899932683377e-16,6.022798429208655e-17,1.2504728160376123e-17,2.4108239557656314e-18,3.8019589635293633e-19,7.98982135579345e-20,1.2685495236734405e-20,1.9021913409844978e-21,2.7022148625758964e-22],[1.4294496268179948e-14,3.8582301858733004e-14,5.2068781886076473e-14,4.6846315823363136e-14,3.161074486566481e-14,1.7064124226628133e-14,7.676301651522655e-15,2.959874325267624e-15,9.986252972726245e-16,2.994879360892899e-16,8.083484535910232e-17,1.9834680335176113e-17,4.46131859426877e-18,9.262733414356074e-19,1.7857900887410197e-19,3.213352932835326e-20,4.750853420657875e-21,9.396634544946424e-22,1.4090263353718464e-22,2.0016345480954865e-23],[9.965631561514884e-16,2.689825495811195e-15,3.630056536434965e-15,3.2659641497772355e-15,2.2037925003171448e-15,1.1896520994660302e-15,5.351653711954361e-16,2.0635226621917423e-16,6.962072390602948e-17,2.087926970066217e-17,5.635527625930218e-18,1.382805750215901e-18,3.110278008745735e-19,6.45765941857556e-20,1.2449914804072994e-20,2.2402392364839515e-21,3.779146219820169e-22,5.258694723767803e-23,9.823247392106397e-24,1.3954708198793208e-24],[6.561712748516354e-17,1.7710731264949222e-16,2.3901534093379244e-16,2.1504225262099714e-16,1.451052374870014e-16,7.833076407832676e-17,3.523711886257792e-17,1.3586939147585438e-17,4.584066637375139e-18,1.3747625459446558e-18,3.71062418266457e-19,9.104866123039888e-20,2.04791344486697e-20,4.251943880414012e-21,8.197449823783178e-22,1.4750501528202953e-22,2.4883191572990355e-23,3.9507217260250224e-24,5.192029141028983e-25,9.188257274477035e-26],[4.0930637234730234e-18,1.1047596021806024e-17,1.490929363756199e-17,1.3413900866293482e-17,9.051371286837778e-18,4.886114665007481e-18,2.1980202191681665e-18,8.475257889122275e-19,2.859448070729027e-19,8.575490761109263e-20,2.314612329980485e-20,5.6794313715910995e-21,1.2774469945964863e-21,2.65227661102671e-22,5.1134034336239013e-23,9.201064572930599e-24,1.552163172255065e-24,2.464380322345872e-25,3.695340877575112e-26,4.6008078010859705e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2109295019644128, "-10": 0.0001624110333735886, "-11": 3.892654837274234e-05, "-12": 8.582562212898363e-06, "-13": 1.751608076879406e-06, "-14": 3.326957047789943e-07, "-15": 5.9086737223522886e-08, "-16": 9.85257712414997e-09, "-17": 1.5472381056320531e-09, "-18": 2.27278723406909e-10, "-19": 2.76341493217923e-11, "-2": 0.2038179286891422, "-3": 0.14875635798294842, "-4": 0.08762900466093256, "-5": 0.04302509327207123, "-6": 0.018051365213481725, "-7": 0.0065989206389334065, "-8": 0.002134718842264837, "-9": 0.0006188152323958041, "0": 0.14488001725161131, "1": 0.08204929577883896, "10": 3.963943103768594e-08, "11": 4.17179916390721e-09, "12": 4.038871818812483e-10, "13": 3.619475680045881e-11, "14": 3.0187109596033103e-12, "15": 2.354127388525746e-13, "16": 1.723675100579123e-14, "17": 1.1885797624385427e-15, "18": 7.666472350696957e-17, "19": 4.0930637234730234e-18, "2": 0.03599393736131703, "3": 0.011535279540394426, "4": 0.0029837750562081234, "5": 0.0006432882731144767, "6": 0.00011851122318160567, "7": 1.9023391547228143e-05, "8": 2.7022239483497918e-06, "9": 3.439594646789107e-07} |
| Raw goal margin distribution | {"-1": 0.20129826409511353, "-10": 0.00015499519405072498, "-11": 3.7149125853288816e-05, "-12": 8.190674414223192e-06, "-13": 1.67162801773596e-06, "-14": 3.1750450847416796e-07, "-15": 5.6388781670503376e-08, "-16": 9.402699259628606e-09, "-17": 1.476589770064938e-09, "-18": 2.1690096483176227e-10, "-19": 2.637234827947618e-11, "-2": 0.19451141189110702, "-3": 0.1419640038790349, "-4": 0.08362778254511036, "-5": 0.04106052736833141, "-6": 0.01722712303485102, "-7": 0.0062976077653794805, "-8": 0.0020372455881090645, "-9": 0.0005905595514936836, "0": 0.17224298343821218, "1": 0.08549127912437633, "10": 4.130231260373932e-08, "11": 4.346806921216918e-09, "12": 4.208303249066126e-10, "13": 3.771313363624253e-11, "14": 3.14534645049104e-12, "15": 2.452883473970039e-13, "16": 1.7959835943083396e-14, "17": 1.2384409063803943e-15, "18": 7.988082303587344e-17, "19": 4.264768514290385e-18, "2": 0.03750388978396685, "3": 0.012019186680452976, "4": 0.0031089449793965077, "5": 0.0006702743368146186, "6": 0.00012348279121979902, "7": 1.9821426390302117e-05, "8": 2.8155827497611148e-06, "9": 3.583886287287271e-07} |
| Research history json | {"away": [{"away": "Dortmund", "away_goals": 2.0, "away_xg": 0.74, "date": "2026-10-31T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 2.0, "home_xg": 4.48, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 3.0, "away_xg": 2.91, "date": "2026-10-25T00:00:00+00:00", "home": "Freiburg", "home_goals": 1.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-10-17T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 6.0, "home_xg": 3.4, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 2.0, "away_xg": 4.96, "date": "2026-10-10T00:00:00+00:00", "home": "Augsburg", "home_goals": 2.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "Union Berlin", "away_goals": 0.0, "away_xg": 0.34, "date": "2026-09-18T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 7.0, "home_xg": 3.77, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 2.0, "away_xg": 2.83, "date": "2026-09-13T00:00:00+00:00", "home": "Elversberg", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 0.0, "away_xg": 1.94, "date": "2026-09-05T00:00:00+00:00", "home": "Schalke 04", "home_goals": 0.0, "home_xg": 0.21, "source": "pipeline training history"}, {"away": "Stuttgart", "away_goals": 1.0, "away_xg": 0.78, "date": "2026-08-28T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 5.0, "home_xg": 4.06, "source": "pipeline training history"}, {"away": "FC Koln", "away_goals": 1.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Wolfsburg", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 13.9% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 68.9% |
| Raw p over 1 5 | 90.5% |
| Raw p under 3 5 | 45.6% |
| Raw p btts yes | 65.3% |
| P home draw | 27.8% |
| P draw away | 86.7% |
| P home away | 85.5% |
| Raw p home draw | 31.1% |
| Raw p draw away | 86.1% |
| Raw p home away | 82.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7552 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.34, "draw": 6.85, "home": 6.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.36, "draw": 6.41, "home": 7.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.96 |
| Reference draw odds | 6.85 |
| Reference away odds | 1.34 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.40 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:06Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:06Z |
| Home probability edge | +0.2% |
| Draw probability edge | +1.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0080 |
| Raw ev home | 0.1046 |
| Raw edge prob draw | 0.0391 |
| Raw ev draw | 0.1799 |
| Raw edge prob away | -0.0471 |
| Raw ev away | -0.0632 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.004345485842363, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,435.5993 |
| Elo away rating | 1,723.5717 |
| Elo rating diff | -227.9724 |
| Elo home expectancy | 0.2121 |

</details>


---

## 2026-11-07 — RB Leipzig vs Augsburg

The model's most likely 1X2 outcome is **RB Leipzig win** at **66.6%**. Expected goals are 2.32 for RB Leipzig and 1.02 for Augsburg (3.34 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.6%; Under 3.5 goals: 57.0%; Double Chance 1X: 84.2%; Double Chance X2: 33.4%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 57.9%; BTTS No (at least one team does not score): 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 66.6% | 1.50 |
| Draw | 17.6% | 5.67 |
| Augsburg win | 15.8% | 6.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.32 |
| Augsburg expected goals | 1.02 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.87% |
| 2 | 2-0 | 9.66% |
| 3 | 1-1 | 8.08% |
| 4 | 1-0 | 7.66% |
| 5 | 3-1 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 66.6% | 67.0% | 1.50 | -0.1% |
| Draw | 17.6% | 16.7% | 5.60 | -1.3% |
| Augsburg win | 15.8% | 16.3% | 6.00 | -5.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | cdb5f9dd39e79db69659c76cd96d0bbe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3173 |
| Dc lambda away | 1.0223 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.66 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.84 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Score matrix json | [[0.03751203516409338,0.032046157290731944,0.020026809701655792,0.006824298588142544,0.0017440765122068052,0.0003565849695635177,6.0754616950895876e-05,8.872556042717229e-06,1.1337734125693905e-06,1.2878084284573037e-07,1.3164936459239389e-08,1.2234707369793077e-09,1.0422690567523728e-10,8.196038623786734e-12,5.984714879907572e-13,4.0786807198764463e-14,2.6059569172014544e-15,1.5670606824270912e-16,8.899811604155787e-18],[0.0766467079602056,0.08080448554054614,0.046408458662667434,0.015814060434365052,0.004041577461765501,0.0008263202709889845,0.00014078768267812176,2.0560521444741078e-05,2.627311955019359e-06,2.9842598550559047e-07,3.0507325858034235e-08,2.8351690542799243e-09,2.4152673918737394e-10,1.8992816396422057e-11,1.3868479166158848e-12,9.451594557816907e-14,6.038827235604925e-15,3.631375740105838e-16,2.0623681209835593e-17],[0.09656450753322254,0.0987154283044643,0.04436858375134572,0.01832309241687348,0.0046828072808522535,0.0009574228424197251,0.00016312481741013774,2.382261887354587e-05,3.044156809668164e-06,3.457737457568422e-07,3.534756638931987e-08,3.2849921634384247e-09,2.798469616101501e-10,2.2006184403602483e-11,1.6068828527479695e-12,1.0951168505297991e-13,6.9969373132703816e-15,4.207523650394041e-16,2.3895799459750025e-17],[0.0745901789134505,0.07625163371971441,0.03897504825448958,0.011678469599561448,0.003617182356320787,0.0007395506168489689,0.00012600394934608814,1.8401516761770716e-05,2.3514250408787804e-06,2.6708908084788225e-07,2.7303834177659285e-08,2.537455628983084e-09,2.1616467031331436e-10,1.69984321755316e-11,1.241218772209762e-12,8.459108206402735e-14,5.4047063395780005e-15,3.250054806705153e-16,1.845804429095717e-17],[0.043212265037646434,0.04417479424031337,0.022579381623179864,0.007694108269249607,0.0017290948993465712,0.0004284432311271715,7.299776102228225e-05,1.0660535086354916e-05,1.3622490730383474e-06,1.5473249050189414e-07,1.5817907078598027e-08,1.470022015741704e-09,1.2523049497163747e-10,9.847687283949817e-12,7.190742177554746e-13,4.900607977108489e-14,3.131103936182911e-15,1.8828514925159206e-16,1.0693283131857827e-17],[0.02002729986048691,0.02047339684127447,0.010464715192268482,0.003565936970280752,0.000911341558923396,0.00016384443638723926,3.383178474592258e-05,4.9407669943167595e-06,6.313524793630037e-07,7.17128339081889e-08,7.331019745260157e-09,6.813012852977725e-10,5.8039741084833026e-11,4.564041852380267e-12,3.3326452497659476e-13,2.2712520477864638e-14,1.4511518285295932e-15,8.726326055931148e-17,4.95594451224044e-18],[0.007734932419310952,0.00790722374279876,0.004041676379911426,0.0013772341588125343,0.00035197782118845145,7.196358633183335e-05,1.0781571709214269e-05,1.9082202327235295e-06,2.4384059731747175e-07,2.7696890132029316e-08,2.8313822976255616e-09,2.6313179688117175e-10,2.2416075958957267e-11,1.7627216615814853e-12,1.2871323625276044e-13,8.772016806674402e-15,5.604630380544483e-16,3.370276711373847e-17,1.914082085107543e-18],[0.002560612476031065,0.0026176486967139194,0.0013379776837666537,0.00045592679784339725,0.00011652057850838577,2.3823201935311343e-05,4.058975087747957e-06,5.212413651141688e-07,8.072226644090145e-08,9.168923343438054e-09,9.373156018290554e-10,8.710852602309129e-11,7.42073500485467e-12,5.835405965728977e-13,4.260990280358682e-14,2.9039343148036977e-15,1.8553861492229282e-16,1.1157140265731761e-17,6.336477426793786e-19],[0.000741718726143218,0.0007582400988010917,0.0003875647379292921,0.0001320658424015499,3.375188392218948e-05,6.900737678002862e-06,1.1757412961597029e-06,1.71704325785567e-07,1.9293533670310674e-08,2.6559122889773742e-09,2.715071260061986e-10,2.5232254221539133e-11,2.1495240558143776e-12,1.6903103925111554e-13,1.2342579411918527e-14,8.411669008651843e-16,5.374396414870491e-17,3.231828299972467e-18,1.8354530446252983e-19],[0.00019097745779747302,0.0001952313745968126,9.979002251506909e-05,3.40042632803364e-05,8.69042233954671e-06,1.776799334061513e-06,3.02729425392355e-07,4.421036502862267e-08,5.649390794277731e-09,5.642604828968146e-10,6.990755237929634e-11,6.496791298213284e-12,5.534586429932985e-13,4.352204822021682e-14,3.177962690801052e-15,2.1658333630853114e-16,1.3837975614352155e-17,8.321299314849639e-19,4.725917575141384e-20],[4.425552340951516e-05,4.5241290612966725e-05,2.3124507616679143e-05,7.879864393326092e-06,2.0138459990091664e-06,4.117406600205079e-07,7.015199242210099e-08,1.0244941298476692e-08,1.309142709454193e-09,1.4870034846450033e-10,1.3366955860947432e-11,1.5055122353221354e-12,1.2825389034743194e-13,1.0085436501529025e-14,7.364345712804473e-16,5.018921615491273e-17,3.206697066785256e-18,1.9283085075749893e-19,1.0951447269756046e-20],[9.323096295514059e-06,9.530763087242988e-06,4.871527770707478e-06,1.6600127820152802e-06,4.242471611817247e-07,8.673940621216044e-08,1.4778579718092307e-08,2.1582520532804485e-09,2.757907398783002e-10,3.13259806032022e-11,3.2023749421996846e-12,2.616977697069537e-13,2.701862452103148e-14,2.124649951961276e-15,1.5514109639740538e-16,1.0573118543391044e-17,6.755393054000929e-19,4.062273930696593e-20,2.3070882367923332e-21],[1.80038048780622e-06,1.8404829632010072e-06,9.407393494807061e-07,3.205645986609905e-07,8.1926249261876e-08,1.675022219210712e-08,2.8538873479988097e-09,4.167794433661999e-10,5.3257871747334e-11,6.049351251100817e-12,6.184097190275762e-13,5.747131382186319e-14,4.305171009237765e-15,4.1029055108762995e-16,2.99592532306191e-17,2.0417719304200076e-18,1.304532041328051e-19,7.84464569401593e-21,4.455211566533701e-22],[3.2092704610291274e-07,3.2807551780488385e-07,1.6769160887179863e-07,5.714228210659791e-08,1.4603773675609129e-08,2.985812924594962e-09,5.08720041517309e-10,7.42930711268224e-11,9.493488502769932e-12,1.0783278540306547e-12,1.102347008052075e-13,1.0244556139895934e-14,8.727289948216109e-16,6.034712438502829e-17,5.340390382961423e-18,3.6395630750474015e-19,2.325395200656472e-20,1.3983482865736534e-21,7.941642877686441e-23],[5.312068377580709e-08,5.43039175025119e-08,2.775675355164245e-08,9.458339940097054e-09,2.41725480222294e-09,4.942195620691479e-10,8.420467138562915e-11,1.2297183381658464e-11,1.5713870389196996e-12,1.7848764582539556e-13,1.8246335900017464e-14,1.6957057179792982e-15,1.444563850845727e-16,1.135954390985111e-17,7.293792209414964e-19,6.02429996285509e-20,3.8490549365615104e-21,2.3145826455430854e-22,1.3145214935567978e-23],[8.20649617144078e-09,8.389291315590353e-09,4.288079060023699e-09,1.4611978797972948e-09,3.734363127470491e-10,7.635087983974238e-11,1.3008592213534538e-11,1.8997644828330726e-12,2.427600851896272e-13,2.757415902810132e-14,2.8188358105155185e-15,2.6196580114100606e-16,2.2316745321652425e-17,1.7549106483445333e-18,1.2814287916573216e-19,7.679337349196986e-21,5.946319278168466e-22,3.575747198454431e-23,2.0307749895839088e-24],[1.188565615327889e-09,1.2150402542537174e-09,6.210523005285097e-10,2.1162863185887144e-10,5.408563552257759e-11,1.1058072602697248e-11,1.8840641713374183e-12,2.7514723632901347e-13,3.5159498524423604e-14,3.993628536188104e-15,4.0825843936821776e-16,3.794110630448982e-17,3.2321852811744798e-18,2.541677240835032e-19,1.8559226354792295e-20,1.2648415209094005e-21,7.106187441587391e-23,5.178836473449314e-24,2.941217877475134e-25],[1.6201663742851698e-10,1.6562546803961755e-10,8.465734167407805e-11,2.8847678979770106e-11,7.37256125160157e-12,1.5073561917195216e-12,2.568219522785241e-13,3.7506074088706e-14,4.792687632166228e-15,5.443824541342381e-16,5.565082709380366e-17,5.171856214329027e-18,4.405880365783347e-19,3.464629926006073e-20,2.5298590237684495e-21,1.7241401522555375e-22,1.1015902603259397e-23,5.824943186148875e-25,4.009254721050481e-26],[2.0857991342542115e-11,2.1322591514708063e-11,1.0898770198829901e-11,3.713844750530365e-12,9.491421448992521e-13,1.9405675180047356e-13,3.3063209693903676e-14,4.8285249036854656e-15,6.170097017557076e-16,7.008369446238854e-17,7.164476983050607e-18,6.65823793503569e-19,5.672122072421815e-20,4.46035803166394e-21,3.256935735312735e-22,2.219654779895183e-23,1.4181852232950327e-24,8.528085361485387e-26,4.25892077525524e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.10085915741231868, "-10": 1.6297693265846955e-08, "-11": 1.4882953709105083e-09, "-12": 1.2491441628775013e-10, "-13": 9.697996172888942e-12, "-14": 7.003200696459991e-13, "-15": 4.726484484369975e-14, "-16": 2.992990290671788e-15, "-17": 1.7732974945254472e-16, "-18": 8.899811604155787e-18, "-2": 0.04134141984939366, "-3": 0.011960623389241264, "-4": 0.002753359999959261, "-5": 0.000523709030391103, "-6": 8.464290650669587e-05, "-7": 1.1874475445614678e-05, "-8": 1.4702143463018657e-06, "-9": 1.6279951545015975e-07, "0": 0.176267836075782, "1": 0.2230188344144297, "10": 5.4786663656214775e-05, "11": 1.1341113963562788e-05, "12": 2.1577295830974676e-06, "13": 3.7973823791531063e-07, "14": 6.216082421305062e-08, "15": 9.509907612119105e-09, "16": 1.3650898535663365e-09, "17": 1.8333922894322503e-10, "18": 2.0857991342542115e-11, "2": 0.19933848216228003, "3": 0.13073065707735002, "4": 0.06821886610453118, "5": 0.029413684497487432, "6": 0.010776253632419514, "7": 0.0034269639803879612, "8": 0.0009618196193410583, "9": 0.00024142595206164813} |
| Raw goal margin distribution | {"-1": 0.09329161530061733, "-10": 1.5074864488796063e-08, "-11": 1.376627395656931e-09, "-12": 1.1554198913419267e-10, "-13": 8.970347872820035e-12, "-14": 6.477745025930222e-13, "-15": 4.371852626505531e-14, "-16": 2.7684238690827285e-15, "-17": 1.6402455852026666e-16, "-18": 8.232051721676027e-18, "-2": 0.038239540518904595, "-3": 0.011063208384966912, "-4": 0.002546773228039423, "-5": 0.00048441472887754595, "-6": 7.829208248753754e-05, "-7": 1.0983524189481367e-05, "-8": 1.3599030045822096e-06, "-9": 1.5058453943269017e-07, "0": 0.1975956167506115, "1": 0.21983599259507486, "10": 5.400476877865528e-05, "11": 1.1179257805108388e-05, "12": 2.1269352693796417e-06, "13": 3.743187550845511e-07, "14": 6.127368805995241e-08, "15": 9.37418574931981e-09, "16": 1.3456077991267816e-09, "17": 1.8072267968835629e-10, "18": 2.0560313851369246e-11, "2": 0.19649359751879816, "3": 0.12886491778447795, "4": 0.06724527183175785, "5": 0.028993903337184424, "6": 0.010622458950426412, "7": 0.003378055625634691, "8": 0.0009480928876273326, "9": 0.0002379804107085288} |
| Research history json | {"away": [{"away": "Freiburg", "away_goals": 2.0, "away_xg": 1.19, "date": "2026-10-31T00:00:00+00:00", "home": "Augsburg", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Union Berlin", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-10-24T00:00:00+00:00", "home": "Augsburg", "home_goals": 1.0, "home_xg": 1.92, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 3.0, "away_xg": 3.92, "date": "2026-10-17T00:00:00+00:00", "home": "Elversberg", "home_goals": 4.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 2.0, "away_xg": 4.96, "date": "2026-10-10T00:00:00+00:00", "home": "Augsburg", "home_goals": 2.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-09-19T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 3.0, "home_xg": 2.78, "source": "pipeline training history"}, {"away": "Leverkusen", "away_goals": 2.0, "away_xg": 2.64, "date": "2026-09-12T00:00:00+00:00", "home": "Augsburg", "home_goals": 2.0, "home_xg": 1.11, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 4.0, "away_xg": 1.13, "date": "2026-09-06T00:00:00+00:00", "home": "Ein Frankfurt", "home_goals": 1.0, "home_xg": 2.22, "source": "pipeline training history"}, {"away": "Schalke 04", "away_goals": 0.0, "away_xg": 1.54, "date": "2026-08-30T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": 3.52, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 0.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "Union Berlin", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [{"away": "Augsburg", "away_goals": 1.0, "away_xg": null, "date": "2026-03-07T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 6.0, "away_xg": null, "date": "2025-10-25T00:00:00+00:00", "home": "Augsburg", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 0.0, "away_xg": null, "date": "2025-02-14T00:00:00+00:00", "home": "Augsburg", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 0.0, "away_xg": null, "date": "2024-09-28T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 2.0, "away_xg": null, "date": "2024-02-10T00:00:00+00:00", "home": "Augsburg", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 0.0, "away_xg": null, "date": "2023-09-16T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 2.0, "away_xg": null, "date": "2023-04-15T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "RB Leipzig", "away_goals": 2.0, "away_xg": 3.66, "date": "2026-10-31T00:00:00+00:00", "home": "Schalke 04", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 0.8, "date": "2026-10-24T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 4.0, "home_xg": 2.87, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-10-17T00:00:00+00:00", "home": "Bayern Munich", "home_goals": 6.0, "home_xg": 3.4, "source": "pipeline training history"}, {"away": "Ein Frankfurt", "away_goals": 0.0, "away_xg": 1.46, "date": "2026-10-10T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 6.0, "home_xg": 4.03, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 0.0, "away_xg": 0.97, "date": "2026-09-20T00:00:00+00:00", "home": "Leverkusen", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Hamburg", "away_goals": 0.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 5.0, "home_xg": 2.43, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 1.0, "away_xg": 1.5, "date": "2026-09-05T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 3.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": 3.96, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 1.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "Freiburg", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "St Pauli", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 19.8% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 58.4% |
| P home draw | 84.2% |
| P draw away | 33.4% |
| P home away | 82.4% |
| Raw p home draw | 85.4% |
| Raw p draw away | 34.3% |
| Raw p home away | 80.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6564 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.75, "draw": 5.6, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.0, "draw": 5.49, "home": 1.5}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 5.60 |
| Reference away odds | 5.75 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:06Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:06Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0136 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | 0.0305 |
| Raw ev draw | 0.1065 |
| Raw edge prob away | -0.0169 |
| Raw ev away | -0.1257 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.789691261495657, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,597.4693 |
| Elo away rating | 1,452.7722 |
| Elo rating diff | 204.6971 |
| Elo home expectancy | 0.7646 |

</details>


---

## 2026-11-07 — SC Paderborn vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **42.7%**. Expected goals are 0.92 for SC Paderborn and 1.09 for Eintracht Frankfurt (2.01 combined). The most likely exact score is 0-1 at 15.2%. Goal-market probabilities: at least one goal: 88.0%; Over 2.5 goals: 34.3%; Under 3.5 goals: 85.3%; Double Chance 1X: 57.3%; Double Chance X2: 69.7%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 39.6%; BTTS No (at least one team does not score): 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 30.3% | 3.30 |
| Draw | 27.0% | 3.70 |
| Eintracht Frankfurt win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.92 |
| Eintracht Frankfurt expected goals | 1.09 |
| Expected total goals | 2.01 |
| Over 0.5 | 88.0% |
| Under 0.5 | 12.0% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 14.7% |
| Under 3.5 | 85.3% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.22% |
| 2 | 0-0 | 11.95% |
| 3 | 1-1 | 11.95% |
| 4 | 1-0 | 11.73% |
| 5 | 0-2 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 30.3% | 30.8% | 3.14 | -4.7% |
| Draw | 27.0% | 24.5% | 4.16 | +12.3% |
| Eintracht Frankfurt win | 42.7% | 44.6% | 2.25 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | 4ca4c7a2a1c15e9121f9a7eaa7f42ddb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9186 |
| Dc lambda away | 1.0879 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.6% |
| P btts no | 60.4% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.37 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.91 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.81 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 17.59 |
| Fair Under 4.5 odds | 1.06 |
| Score matrix json | [[0.11954508043972979,0.15219977172807228,0.08923293465896018,0.032359937985458054,0.008801393709829708,0.0019150724274005994,0.000347246368312292,5.39688832566179e-05,7.339343323754014e-06,8.87193709058098e-07,9.652108893179513e-08,9.546260624895058e-09,8.654775363918978e-10,7.242962007026836e-11],[0.11733022721313384,0.11947298498885887,0.08196696255248645,0.029724964613034636,0.008084722433264286,0.0017591337833052214,0.0003189711307458666,4.9574357828771886e-05,6.741722455696236e-06,8.149521676620612e-07,8.866166412922341e-08,8.768937053875968e-09,7.950042782587061e-10,6.653189182537291e-11],[0.058925830773816454,0.06410759335227657,0.027674154311937878,0.013652274637287985,0.0037132037821423327,0.0008079463792829226,0.0001464991307811112,2.2768832759141385e-05,3.096382037513894e-06,3.742965199123166e-07,4.072110444028444e-08,4.027454313069537e-09,3.651347238222573e-10,3.0557199013115887e-11],[0.018042558624313847,0.0196291676525006,0.01067764918360156,0.0030729059876153098,0.001136949552404042,0.00024738590397594665,4.485671429351705e-05,6.971611506689991e-06,9.480842900553721e-07,1.1460622302155853e-07,1.246843539517998e-08,1.2331702344465127e-09,1.1180096358120532e-10,9.356339102035207e-12],[0.004143351702940081,0.00450770574804646,0.002452050002966515,0.0008892253329614216,0.00019193170259280078,5.6810501651402594e-05,1.0301041411381789e-05,1.6009834863196495e-06,2.1772115249984702e-07,2.6318544903271107e-08,2.863291958935343e-09,2.831892137528409e-10,2.567433602351095e-11,2.148620068744642e-12],[0.0007611941827861164,0.0008281313388602108,0.0004504773748350522,0.00016336367249634618,4.443234718713475e-05,7.672274488555265e-06,1.8924516577771427e-06,2.941240338488294e-07,3.999855349831236e-08,4.835100835285013e-09,5.260285244946212e-10,5.202599190010251e-11,4.716750261418778e-12,3.9473286715809815e-13],[0.00011653540125825254,0.0001267831783939492,6.896605731013285e-05,2.501024253194107e-05,6.8023922481205516e-06,1.4801148845540392e-06,2.1298011448483105e-07,4.5029064960550496e-08,6.123598402466049e-09,7.402321624446444e-10,8.053259806964633e-11,7.964945054816077e-12,7.221132225912624e-13,6.043182423664796e-14],[1.5292324373091967e-05,1.6637085968025172e-05,9.05005095217893e-06,3.2819618529528966e-06,8.9264195813544e-07,1.9422764824812465e-07,3.52179084795994e-08,4.34370578248035e-09,8.035674317844006e-10,9.713675172759731e-11,1.0567866922770473e-11,1.0451976144328649e-12,9.47590990783356e-14,7.930148681914438e-15],[1.7558894930727196e-06,1.910297200993547e-06,1.0391415321182306e-06,3.768401842433773e-07,1.0249459775544691e-07,2.2301533665032407e-08,4.043777385217864e-09,6.284821657869854e-10,6.782625711245922e-11,1.1153399417149268e-11,1.2134196241961847e-12,1.2001128570072752e-13,1.088039348272368e-14,9.105525366424491e-16],[1.7921251569161105e-07,1.9497193215138075e-07,1.0605859244857989e-07,3.846169004278501e-08,1.046097421336564e-08,2.2761762443817354e-09,4.127227373708791e-10,6.414519275976622e-11,8.723241316552072e-12,8.368165442949613e-13,1.2384605312560036e-13,1.2248791570689873e-14,1.1104928273938735e-15,9.29343283873235e-17],[1.6461977428819355e-08,1.7909594840197708e-08,9.742255714022099e-09,3.5329869173205905e-09,9.609168239132506e-10,2.090833991946519e-10,3.791159540805435e-11,5.8922040757221935e-12,8.012933756609647e-13,9.68618595202485e-14,8.36272243936736e-15,1.1251408953713393e-15,1.020068703844408e-16,8.53669628134247e-18],[1.3746843305057842e-09,1.495569988416196e-09,8.135429860571209e-10,2.950278468138366e-10,8.024292989494581e-11,1.7459850973832107e-11,3.1658697369302094e-12,4.920381315100941e-13,6.691331296146809e-14,8.08860788941611e-15,8.799896048154083e-16,6.906845434827684e-17,8.518250430591339e-18,7.128707752753943e-19],[1.0522898997504434e-10,1.1448251487679476e-10,6.227488364006794e-11,2.2583717327533393e-11,6.1424155917865896e-12,1.336512275814739e-12,2.4234019943120566e-13,3.766441099169668e-14,5.122063431266923e-15,6.191647199428459e-16,6.736122268098713e-17,6.6622516886303814e-18,4.793300649087064e-19,5.456865259921643e-20],[7.435423594253638e-12,8.089272665700637e-12,4.400309641445513e-12,1.5957532682098303e-12,4.340197680098675e-13,9.443723551807612e-14,1.7123627596485054e-14,2.6613469369775673e-15,3.6192223547083194e-16,4.374984468143509e-17,4.759707610790207e-18,4.707511058335385e-19,4.267896334907066e-20,2.8344277435290713e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.24901470726747071, "-10": 1.0566451704859539e-07, "-11": 1.037182210216688e-08, "-12": 9.320094282172708e-10, "-13": 7.242962007026836e-11, "-2": 0.12292909034551924, "-3": 0.04129910524525975, "-4": 0.010714220873264835, "-5": 0.002257787327829705, "-6": 0.0004000346304495936, "-7": 6.109765863401748e-05, "-8": 8.196275835159697e-06, "-9": 9.799967770840407e-07, "0": 0.269964947097715, "1": 0.19305064339925673, "10": 1.802141805414383e-08, "11": 1.4935671550240245e-09, "12": 1.1331826264074498e-10, "13": 7.435423594253638e-12, "2": 0.08117741283040832, "3": 0.023026667351901575, "4": 0.0050438358701461765, "5": 0.0008974149255779966, "6": 0.00013425106907011516, "7": 1.731229475001721e-05, "8": 1.9609049456377635e-06, "9": 1.9795867125496142e-07} |
| Raw goal margin distribution | {"-1": 0.22205528810368458, "-10": 9.422481520483112e-08, "-11": 9.248923368140718e-09, "-12": 8.311060192755599e-10, "-13": 6.458807324447885e-11, "-2": 0.10962025043636457, "-3": 0.036827883839849536, "-4": 0.009554252553700982, "-5": 0.002013349416424474, "-6": 0.0003567251351966211, "-7": 5.448295941759266e-05, "-8": 7.30891123630997e-06, "-9": 8.738980482881156e-07, "0": 0.3274851816435986, "1": 0.18584318936346772, "10": 1.7348596974670124e-08, "11": 1.437805535017731e-09, "12": 1.0908757915263294e-10, "13": 7.15782558759291e-12, "2": 0.07814669269699026, "3": 0.02216697766833498, "4": 0.00485552665470907, "5": 0.0008639103657731502, "6": 0.0001292388692009998, "7": 1.6665948452135556e-05, "8": 1.887695491292635e-06, "9": 1.9056797833141997e-07} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Hamburg", "away_goals": 0.0, "away_xg": 0.46, "date": "2026-10-24T00:00:00+00:00", "home": "Paderborn", "home_goals": 1.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 2.0, "away_xg": 1.15, "date": "2026-10-17T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 2.0, "home_xg": 3.21, "source": "pipeline training history"}, {"away": "Stuttgart", "away_goals": 2.0, "away_xg": 2.47, "date": "2026-10-10T00:00:00+00:00", "home": "Paderborn", "home_goals": 0.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 1.0, "away_xg": 1.5, "date": "2026-09-20T00:00:00+00:00", "home": "Paderborn", "home_goals": 3.0, "home_xg": 0.68, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-09-12T00:00:00+00:00", "home": "Dortmund", "home_goals": 3.0, "home_xg": 1.76, "source": "pipeline training history"}, {"away": "Freiburg", "away_goals": 1.0, "away_xg": 1.24, "date": "2026-09-05T00:00:00+00:00", "home": "Paderborn", "home_goals": 0.0, "home_xg": 0.77, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.73, "date": "2026-08-29T00:00:00+00:00", "home": "Mainz", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.2% |
| Unadjusted draw probability | 32.7% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 60.6% |
| Raw p under 3 5 | 85.6% |
| Raw p btts yes | 40.9% |
| P home draw | 57.3% |
| P draw away | 69.7% |
| P home away | 73.0% |
| Raw p home draw | 62.0% |
| Raw p draw away | 70.8% |
| Raw p home away | 67.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3433 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.19, "draw": 3.92, "home": 3.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.25, "draw": 4.16, "home": 3.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.14 |
| Reference draw odds | 3.92 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:06Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:06Z |
| Home probability edge | -0.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -31.6% |
| Under 2.5 probability edge | +31.6% |
| Raw edge prob home | -0.0162 |
| Raw ev home | -0.0830 |
| Raw edge prob draw | 0.0822 |
| Raw ev draw | 0.3623 |
| Raw edge prob away | -0.0660 |
| Raw ev away | -0.1439 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.369614949115634, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,409.3829 |
| Elo away rating | 1,482.9965 |
| Elo rating diff | -13.6136 |
| Elo home expectancy | 0.4804 |

</details>


---

## 2026-11-07 — VfB Stuttgart vs Werder Bremen

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **60.8%**. Expected goals are 2.28 for VfB Stuttgart and 1.18 for Werder Bremen (3.47 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.4%; Double Chance 1X: 80.6%; Double Chance X2: 39.2%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 73.1%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 60.8% | 1.64 |
| Draw | 19.8% | 5.06 |
| Werder Bremen win | 19.4% | 5.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.28 |
| Werder Bremen expected goals | 1.18 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 45.6% |
| Under 3.5 | 54.4% |
| Over 4.5 | 26.9% |
| Under 4.5 | 73.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.54% |
| 2 | 1-1 | 8.72% |
| 3 | 2-0 | 8.06% |
| 4 | 3-1 | 7.26% |
| 5 | 1-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 60.8% | 60.6% | 1.63 | -0.9% |
| Draw | 19.8% | 19.4% | 4.99 | -1.4% |
| Werder Bremen win | 19.4% | 20.0% | 4.93 | -4.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 716d6e3f3e91c47a6efaa2e93d570533 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:05Z |
| Market best draw last update utc | 2026-11-05T12:28:05Z |
| Market best away last update utc | 2026-11-05T12:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2831 |
| Dc lambda away | 1.1838 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:27:56.921923+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.58 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.19 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.71 |
| Fair Under 4.5 odds | 1.37 |
| Score matrix json | [[0.036262445279613885,0.032733529378297,0.023611337798937974,0.009317171018405467,0.0027574573450297912,0.0006528652093763985,0.0001288122015687014,2.1784304064178828e-05,3.223579836061247e-06,4.2401444142111954e-07,5.019556831513282e-08,5.402035300398425e-09,5.329186254700443e-10,4.85291041240754e-11,4.103542782929648e-12,3.2385636269723524e-13,2.396167528453699e-14,1.6686028632016423e-15,1.0974006337293061e-16],[0.0640329599449355,0.08719240545078401,0.05390709421196413,0.021272052441719622,0.006295556573278092,0.0014905579111722425,0.000294091404084983,4.973578970957681e-05,7.359761797578355e-06,9.6806824905744e-07,1.1460160594155983e-07,1.2333397978323456e-08,1.216707617126899e-09,1.107968980968295e-10,9.368807023385346e-12,7.39397132162886e-13,5.470695045064867e-14,3.80959065153055e-15,2.505477658846409e-16],[0.08059421960299276,0.09540884131984068,0.05462304834363458,0.024283133484905708,0.007186699123158474,0.0017015479264704074,0.0003357203467660158,5.6775942227661234e-05,8.401543698585263e-06,1.1050993118208206e-06,1.308235818940325e-07,1.4079203229243439e-08,1.3889338398230084e-09,1.264803137153844e-10,1.0694971355796317e-11,8.440595616177582e-13,6.245077591759793e-14,4.3488421518053984e-15,2.860130615036132e-16],[0.061334943210681794,0.07260937438163463,0.04297812121536467,0.016403762728833943,0.005469322548968676,0.001294935864562182,0.0002554946062508849,4.320842374826146e-05,6.39386060406314e-06,8.41018175578644e-07,9.956119688998761e-08,1.0714752680417135e-08,1.0570259084160796e-09,9.625582203310085e-11,8.139237081504997e-12,6.423580442031569e-13,4.75271652636816e-14,3.309616840105223e-15,2.1766567095322965e-16],[0.03500848395693627,0.04144365324397893,0.024530859381399466,0.009680019574970267,0.0027709810217607864,0.0007391176883309066,0.00014583006612224476,2.4662310428814065e-05,3.6494590956309645e-06,4.80032584461726e-07,5.682709368596089e-08,6.115718506927654e-09,6.033245099737164e-10,5.494046664121898e-11,4.6456772579181966e-12,3.666422451529847e-13,2.7127342352580633e-14,1.8890482649089892e-15,1.242382359981516e-16],[0.01598558844022369,0.018924018104655074,0.011201291168118603,0.004420094546485632,0.0013081462333208104,0.00029957364099491153,6.658898517594715e-05,1.1261314399818411e-05,1.6664175233623285e-06,2.1919267748187338e-07,2.5948411049025735e-08,2.7925619169417023e-09,2.7549028756009833e-10,2.5086938626668404e-11,2.1213110731255544e-12,1.6741633379568174e-13,1.2386898297533524e-14,8.62578000912567e-16,5.672971476425053e-17],[0.0060827883438804515,0.007200910818943099,0.004262281842712664,0.0016819211683543208,0.0004977718955977071,0.00011785420848915174,2.2491123599412174e-05,4.28512170347293e-06,6.341002162698403e-07,8.34065426265928e-08,9.873811831291193e-09,1.0626173156813575e-09,1.0482874098060983e-10,9.546006919455474e-12,8.071949504770367e-13,6.370476304926825e-14,4.713425524673095e-15,3.282256032837814e-16,2.1586621537894237e-17],[0.0019839466658970305,0.0023486306284249683,0.0013901749284882623,0.0005485711002282696,0.00016235200648430205,3.843902677120364e-05,7.584131599364085e-06,1.240581005359248e-06,2.068165023658532e-07,2.7203664307093888e-08,3.2204171762925663e-09,3.4658054191403817e-10,3.4190673651812294e-11,3.1135011658817452e-12,2.6327263751318017e-13,2.0777782343932244e-14,1.5373187962452855e-15,1.0705322205596995e-16,7.04063718922126e-18],[0.0005661940925411786,0.0006702704312740381,0.00039673890716866755,0.00015655547683164452,4.6333275265772624e-05,1.097002770034005e-05,2.16441831951832e-06,3.66039445178791e-07,5.2390821524211236e-08,7.763592787503534e-09,9.190676403140919e-10,9.890984409740853e-11,9.757599725044313e-12,8.885551197240753e-13,7.513478797087497e-14,5.929724735781491e-15,4.3873196580767985e-16,3.055167911390571e-17,2.0093116678922368e-18],[0.00014363098943201462,0.0001700328677023622,0.00010064393559293015,3.9714681475053627e-05,1.1753732964928116e-05,2.7828547726888465e-06,5.490653273719646e-07,9.285615723437054e-08,1.374059209020377e-08,1.7481562403338684e-09,2.3314724804137597e-10,2.5091252203843643e-11,2.4752884592976203e-12,2.2540689260471083e-13,1.906004332999383e-14,1.5042407578596283e-15,1.1129665105049966e-16,7.750289092994284e-18,5.097181809887288e-19],[3.2792420933546103e-05,3.8820239227503385e-05,2.2978037771815528e-05,9.067267149810354e-06,2.6834972066307334e-06,6.353541492947468e-07,1.2535721856681367e-07,2.1200008482447385e-08,3.1371174248673844e-09,4.126415848918134e-10,4.72487474501008e-11,5.728588985371207e-12,5.651336206080876e-13,5.146269431719684e-14,4.3516024387246244e-15,3.434335188540756e-16,2.5410161443394503e-17,1.7694701073854115e-18,1.1637386342990803e-19],[6.806222193130871e-06,8.0573244137212e-06,4.769200509900205e-06,1.8819542183588371e-06,5.569725480161344e-07,1.3187076124056277e-07,2.6018484112765996e-08,4.400162114294764e-09,6.511235715978291e-10,8.564571425180373e-11,1.013888886948328e-11,1.0553948845206701e-12,1.1729615811110604e-13,1.0681325812748951e-14,9.031956851905148e-16,7.128125253779084e-17,5.27399929079795e-18,3.67261896868616e-19,2.4153946229896986e-20],[1.2949416650206726e-06,1.5329745041891296e-06,9.07380963163461e-07,3.580577976830989e-07,1.0596876479094861e-07,2.5089534000335927e-08,4.950237912053906e-09,8.371682694103584e-10,1.2388179786285263e-10,1.6294825626916315e-11,1.929009847395059e-12,2.0759958777681014e-13,1.9808999813125317e-14,2.0322130897444033e-15,1.7184066156413292e-16,1.3561864603715718e-17,1.0034232249773433e-18,6.987469975777084e-20,4.595493720338669e-21],[2.2742184587403223e-07,2.692259434056866e-07,1.5935718119804047e-07,6.288326916825336e-08,1.8610577406484144e-08,4.40630515536358e-09,8.693768019711854e-10,1.4702620070027124e-10,2.1756522244354475e-11,2.861750009572542e-12,3.3877895202079703e-13,3.6459311434802455e-14,3.596764007444779e-15,3.1680052924217086e-16,3.0179213091043825e-17,2.3817785503268144e-18,1.7622443402775114e-19,1.2271620898499973e-20,8.0707547900643055e-22],[3.7087663368054896e-08,4.3905022055390934e-08,2.5987765022488965e-08,1.0254923001929884e-08,3.034989129052812e-09,7.185746016218975e-10,1.4177685546252561e-10,2.397684451508694e-11,3.548025784229866e-12,4.666905265439726e-13,5.5247637624439845e-14,5.945737815680202e-15,5.865556679912585e-16,5.3413447618588483e-17,4.368575866479411e-18,3.8841739566524653e-19,2.873845501222143e-20,2.0012402199744968e-21,1.3161683550216907e-22],[5.644994734615081e-09,6.6826431168300175e-09,3.95551467506911e-09,1.5608690624505453e-09,4.6194599759752056e-10,1.0937194404319466e-10,2.1579402148737057e-11,3.649438890154831e-12,5.400336675701054e-13,7.103347382366064e-14,8.409066389405202e-15,9.049817544403794e-16,8.927776399688943e-17,8.12989018942295e-18,6.874504035253034e-19,5.247680907577116e-20,4.374188409094983e-21,3.0460237929646745e-22,2.0032977974999613e-23],[8.055061978493209e-10,9.535722709560206e-10,5.644277339913886e-10,2.227264617494642e-10,6.591686646840829e-11,1.560670699254952e-11,3.079248607638589e-12,5.207525928529517e-13,7.705949902975091e-14,1.0136041946835881e-14,1.1999223051984251e-15,1.291353573232313e-16,1.273939048847085e-17,1.1600855701880673e-18,9.809496497101817e-20,7.741768572897877e-21,5.540353928062687e-22,4.346489517490837e-23,2.8585833430970326e-24],[1.0817958046892088e-10,1.2806487211922755e-10,7.580271341330385e-11,2.991219093746978e-11,8.852643194326106e-12,2.095982649746417e-12,4.1354346300903783e-13,6.993713663947891e-14,1.0349100104308647e-14,1.3612716678676692e-15,1.6114971171947205e-16,1.7342894215128766e-17,1.7109016940554127e-18,1.5579963335610456e-19,1.3174165742003774e-20,1.0397204621636357e-21,7.692744985326932e-23,5.181431029019002e-24,3.839080911076109e-25],[1.3721390229765944e-11,1.6243620815093022e-11,9.614740662798863e-12,3.794032503187664e-12,1.1228604447132952e-12,2.6585235150040053e-13,5.24534409203592e-14,8.870756747466283e-15,1.3126695485653781e-15,1.7266234239929247e-16,2.0440068914414226e-17,2.1997554271131468e-18,2.170090666569593e-19,1.9761470303979763e-20,1.6709980600228056e-21,1.3187710776266568e-22,9.7574011125021e-24,6.794694962014838e-25,4.322298602940037e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.11720328623843619, "-10": 6.401897387139215e-08, "-11": 6.753741832731904e-09, "-12": 6.550808644738482e-10, "-13": 5.879144365232187e-11, "-14": 4.908824546086235e-12, "-15": 3.8312982097064254e-13, "-16": 2.805727899757115e-14, "-17": 1.9191506290862832e-15, "-18": 1.0974006337293061e-16, "-2": 0.05352277885751578, "-3": 0.017596185580754344, "-4": 0.004630822908869227, "-5": 0.0010106334950045696, "-6": 0.00018785028082695198, "-7": 3.035512739458485e-05, "-8": 4.333815659561068e-06, "-9": 5.538094035511964e-07, "0": 0.19757600235752892, "1": 0.21353390683154944, "10": 4.182315709117053e-05, "11": 8.509286776638782e-06, "12": 1.5917843078138577e-06, "13": 2.7551422756178755e-07, "14": 4.436576927025849e-08, "15": 6.678163751487594e-09, "16": 9.431858106313473e-10, "17": 1.244232012840139e-10, "18": 1.3721390229765944e-11, "2": 0.18269301933408733, "3": 0.11583570175841736, "4": 0.05879260101875114, "5": 0.02474564562948505, "6": 0.008870693029801402, "7": 0.002764511255899805, "8": 0.0007611974728083971, "9": 0.00018759783822978592} |
| Raw goal margin distribution | {"-1": 0.10856620283252477, "-10": 5.9301211813396674e-08, "-11": 6.256037089260568e-09, "-12": 6.068058694146938e-10, "-13": 5.445891494364714e-11, "-14": 4.547077632750729e-12, "-15": 3.548957643565359e-13, "-16": 2.5989648757648095e-14, "-17": 1.7777223075441383e-15, "-18": 1.0165296862719327e-16, "-2": 0.049578514836044044, "-3": 0.016299466628883943, "-4": 0.004289562821498127, "-5": 0.0009361566943165392, "-6": 0.0001740069954089516, "-7": 2.8118161388608516e-05, "-8": 4.014442982234223e-06, "-9": 5.129974249542936e-07, "0": 0.2061837218436591, "1": 0.21553589478622145, "10": 4.221527025935665e-05, "11": 8.589065627138244e-06, "12": 1.6067080876386391e-06, "13": 2.7809731224891686e-07, "14": 4.478172070858853e-08, "15": 6.740774901108681e-09, "16": 9.520286527818968e-10, "17": 1.2558973148031117e-10, "18": 1.3850035175989947e-11, "2": 0.18440585843086854, "3": 0.1169217198202902, "4": 0.059343811272943844, "5": 0.024977648524088077, "6": 0.008953860246000303, "7": 0.0027904299416813224, "8": 0.00076833408260635, "9": 0.00018935666247475616} |
| Research history json | {"away": [{"away": "Hoffenheim", "away_goals": 0.0, "away_xg": 1.06, "date": "2026-10-31T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Werder Bremen", "away_goals": 3.0, "away_xg": 2.69, "date": "2026-10-24T00:00:00+00:00", "home": "Mainz", "home_goals": 2.0, "home_xg": 1.7, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 2.0, "away_xg": 1.15, "date": "2026-10-17T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 2.0, "home_xg": 3.21, "source": "pipeline training history"}, {"away": "Werder Bremen", "away_goals": 2.0, "away_xg": 1.13, "date": "2026-10-09T00:00:00+00:00", "home": "Dortmund", "home_goals": 2.0, "home_xg": 2.42, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-09-19T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 3.0, "home_xg": 2.78, "source": "pipeline training history"}, {"away": "Werder Bremen", "away_goals": 1.0, "away_xg": 1.12, "date": "2026-09-12T00:00:00+00:00", "home": "FC Koln", "home_goals": 1.0, "home_xg": 1.65, "source": "pipeline training history"}, {"away": "RB Leipzig", "away_goals": 1.0, "away_xg": 1.5, "date": "2026-09-05T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 3.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Werder Bremen", "away_goals": 1.0, "away_xg": 0.48, "date": "2026-08-30T00:00:00+00:00", "home": "Freiburg", "home_goals": 4.0, "home_xg": 1.94, "source": "pipeline training history"}, {"away": "Dortmund", "away_goals": 2.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Werder Bremen", "away_goals": 0.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Hoffenheim", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 61.4% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 18.0% |
| Raw p over 1 5 | 86.7% |
| Raw p under 3 5 | 54.4% |
| Raw p btts yes | 63.0% |
| P home draw | 80.6% |
| P draw away | 39.2% |
| P home away | 80.2% |
| Raw p home draw | 82.0% |
| Raw p draw away | 38.6% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6756 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.7, "draw": 4.85, "home": 1.62}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.99, "home": 1.63}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.85 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-11-05T12:28:05Z |
| Market reference home last update utc | 2026-11-05T12:28:05Z |
| Market reference draw last update utc | 2026-11-05T12:28:05Z |
| Market reference away last update utc | 2026-11-05T12:28:05Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.45 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:06Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:06Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0081 |
| Raw ev home | 0.0007 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0289 |
| Raw edge prob away | -0.0204 |
| Raw ev away | -0.1132 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.72072662191211, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,547.4698 |
| Elo away rating | 1,475.4921 |
| Elo rating diff | 131.9777 |
| Elo home expectancy | 0.6813 |

</details>


---
