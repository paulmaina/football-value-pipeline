# Primeira Liga — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-10-28T16:14:56.548861+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1305, 'tuning_matches': 197, 'audit_matches': 103, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8910498907299429, 'audit_candidate_poisson_score': 0.8787218636487978, 'audit_gain': 0.01232802708114511, 'audit_gain_lower95': 0.0008780097625350776, 'audit_baseline_briers': [0.6072179100258951, 0.18432497321758096, 0.24265429789867352, 0.251145870738951], 'audit_candidate_briers': [0.602848996497705, 0.1834923655776512, 0.24110273505676244, 0.24950419867956106], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1464.589 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
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
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 2 |
| Goal rate features used | {'shot_features': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Casa Pia vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **76.0%**. Expected goals are 0.73 for Casa Pia and 2.38 for Sporting Lisbon (3.11 combined). The most likely exact score is 0-2 at 12.9%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.0%; Double Chance 1X: 24.0%; Double Chance X2: 91.2%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 46.4%; BTTS No (at least one team does not score): 53.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Casa Pia win | 8.8% | 11.33 |
| Draw | 15.2% | 6.59 |
| Sporting Lisbon win | 76.0% | 1.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Casa Pia expected goals | 0.73 |
| Sporting Lisbon expected goals | 2.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.91% |
| 2 | 0-1 | 11.27% |
| 3 | 0-3 | 10.22% |
| 4 | 1-2 | 9.42% |
| 5 | 1-3 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Casa Pia win | 8.8% | 8.3% | 10.08 | -11.0% |
| Draw | 15.2% | 15.0% | 5.82 | -11.6% |
| Sporting Lisbon win | 76.0% | 76.7% | 1.28 | -2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:15:00+00:00 |
| Fixture id | 75daf3f21fd7945dcc4215b1fe8a5da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:14:41Z |
| Market best draw last update utc | 2026-10-28T16:14:41Z |
| Market best away last update utc | 2026-10-28T16:14:41Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Casa Pia |
| Matched away-team name | Sp Lisbon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6959 |
| Dc lambda away | 2.5772 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 0.8098 |
| Shot lambda away | 1.9042 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.4% |
| P btts no | 53.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.05 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.2384423391574805, "-10": 8.431532777714558e-05, "-11": 1.7973076317865576e-05, "-12": 3.518846637965704e-06, "-13": 6.369236889528615e-07, "-14": 1.0718367287400239e-07, "-15": 1.6851719356153347e-08, "-16": 2.485631784301783e-09, "-17": 3.4397915926075553e-10, "-18": 4.140284736975088e-11, "-2": 0.22189548480430213, "-3": 0.1549908197032252, "-4": 0.08505071235273436, "-5": 0.03827664296477888, "-6": 0.014569111098333832, "-7": 0.004798520953775893, "-8": 0.0013918331881638002, "-9": 0.00036049368349134244, "0": 0.15183574766104746, "1": 0.06556776921991612, "10": 5.470426526399193e-10, "11": 3.5841072551786674e-11, "12": 2.1567650681362765e-12, "13": 1.199868979991546e-13, "14": 6.2061030317688635e-15, "15": 2.999013955271917e-16, "16": 1.359611986994619e-17, "17": 5.783014007821101e-19, "18": 2.1394209565588186e-20, "2": 0.018076391658504918, "3": 0.0038807277391270083, "4": 0.0006545292776255336, "5": 9.053758080285234e-05, "6": 1.0591854887051216e-05, "7": 1.072235754590277e-06, "8": 9.559033857935143e-08, "9": 7.609715034133712e-09} |
| Raw goal margin distribution | {"-1": 0.2334835838439251, "-10": 8.256186787943441e-05, "-11": 1.7599300049745296e-05, "-12": 3.4456671031345403e-06, "-13": 6.236779342849441e-07, "-14": 1.049546324725856e-07, "-15": 1.6501263337330783e-08, "-16": 2.4339394554079276e-09, "-17": 3.3682561224488743e-10, "-18": 4.0541814928463344e-11, "-2": 0.21728084539833417, "-3": 0.15176756013669293, "-4": 0.08328195906298302, "-5": 0.03748062449189641, "-6": 0.014266125238826187, "-7": 0.004698728729958513, "-8": 0.0013628879922653833, "-9": 0.000352996692919818, "0": 0.15567403480550185, "1": 0.07445398591068167, "10": 6.211818159557417e-10, "11": 4.0698513042958423e-11, "12": 2.4490654159222602e-12, "13": 1.362483872698526e-13, "14": 7.047198847619247e-15, "15": 3.4054619430903163e-16, "16": 1.5438764034226623e-17, "17": 6.566769749561683e-19, "18": 2.429370705329162e-20, "2": 0.020526234548932702, "3": 0.004406671934240367, "4": 0.0007432358031125108, "5": 0.00010280788633930277, "6": 1.2027339406400881e-05, "7": 1.2175528726230424e-06, "8": 1.08545430269458e-07, "9": 8.64103846564293e-09} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 74.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 62.4% |
| Raw p btts yes | 46.6% |
| P home draw | 24.0% |
| P draw away | 91.2% |
| P home away | 84.8% |
| Raw p home draw | 25.6% |
| Raw p draw away | 90.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6036 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.08 |
| Reference draw odds | 5.82 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-28T16:14:41Z |
| Market reference home last update utc | 2026-10-28T16:14:41Z |
| Market reference draw last update utc | 2026-10-28T16:14:41Z |
| Market reference away last update utc | 2026-10-28T16:14:41Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-28T16:14:41Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:14:41Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0171 |
| Raw ev home | 0.0105 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0940 |
| Raw edge prob away | -0.0226 |
| Raw ev away | -0.0476 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03789402444322738, 0.10487793253221135, 0.12656771073997197, 0.10541982124462204, 0.06585411069463017, 0.032910424959399893, 0.013705751237897641, 0.004892438895496448, 0.001528114963518655, 0.00042426198950096375, 0.00010601192713195104, 2.408145089664863e-05, 5.014435028479389e-06, 9.638273846061336e-07, 1.7202510475868523e-07, 2.8656370076101398e-08, 4.4752963551295675e-09, 6.577994158916305e-10, 9.131488649130965e-11], [0.03135049518735471, 0.06957590606157327, 0.0892698374359142, 0.07435395844651609, 0.04644775292075915, 0.023212146833470743, 0.00966684297117337, 0.0034507002008070625, 0.0010777991762603361, 0.0002992374485685271, 7.477157835919114e-05, 1.6984957649912293e-05, 3.5367456455379987e-06, 6.797998750000221e-07, 1.213315232370248e-07, 2.0211707103185096e-08, 3.1564841914596227e-09, 4.639544049487181e-10, 6.440556619772813e-11], [0.00982806632096262, 0.024557756208407788, 0.03226841979182819, 0.026221402537941963, 0.01638009934863343, 0.008185913145808719, 0.0034090744610529708, 0.0012169116600322543, 0.00038009282419191416, 0.00010552801434218333, 2.6368678891036055e-05, 5.989854755999412e-06, 1.247256140541238e-06, 2.3973580613653836e-07, 4.278834345622868e-08, 7.127788741911021e-09, 1.1131544885864939e-09, 1.6361651034574734e-10, 2.271303791000555e-11], [0.0023106206094543726, 0.005773633974780229, 0.007213397374354804, 0.006318843698520551, 0.003851031719142436, 0.0019245433439501352, 0.0008014880497979814, 0.0002861011586336603, 8.936145569249002e-05, 2.4810089477495788e-05, 6.199389676457203e-06, 1.4082405831277432e-06, 2.932352763489319e-07, 5.636291783071602e-08, 1.0059723347968867e-08, 1.6757737513195097e-09, 2.61707401927938e-10, 3.8466944412607445e-11, 5.339932778662505e-12], [0.00040742762308041417, 0.0010180546114995966, 0.0012719255314103148, 0.0010594026025580936, 0.0006960173319131648, 0.00033935130541659755, 0.00014132496253188833, 5.044770852718671e-05, 1.5756946570468952e-05, 4.374718957698326e-06, 1.0931273572534507e-06, 2.483125577437825e-07, 5.1705654817294185e-08, 9.93837307071712e-09, 1.7738131287062926e-09, 2.954862055358722e-10, 4.6146400786769195e-11, 6.78280790237388e-12, 9.415808508405056e-13], [5.7472790598246945e-05, 0.00014360940738853076, 0.00017942109366718366, 0.00014944206157578541, 9.33541145228186e-05, 4.906620509059979e-05, 1.9935663459659934e-05, 7.116283786610484e-06, 2.2227154945102717e-06, 6.171091313863928e-07, 1.5419936239385233e-07, 3.502760938550011e-08, 7.293732932469991e-09, 1.4019325200928911e-09, 2.5021865168537406e-10, 4.168204572639374e-11, 6.5095302307406526e-12, 9.568003644277411e-13, 1.3282182160976065e-13], [6.756049974750157e-06, 1.6881594282473607e-05, 2.109133492078591e-05, 1.7567235309546516e-05, 1.0973976667907786e-05, 5.4842170340755025e-06, 2.4020519353535974e-06, 8.365344434538595e-07, 2.6128498032286173e-07, 7.25425038200303e-08, 1.8126466238429927e-08, 4.117570715483663e-09, 8.573939716745081e-10, 1.6480017880433158e-10, 2.9413739924654954e-11, 4.899813999738635e-12, 7.65209259777482e-13, 1.1247393785208257e-13, 1.5613490404627485e-14], [6.807327301374311e-07, 1.700972285274678e-06, 2.1251414741644926e-06, 1.7700567784323584e-06, 1.1057267375950093e-06, 5.525841354378792e-07, 2.3012710129582033e-07, 8.6395025518865e-08, 2.6326809106480035e-08, 7.3093089691422e-09, 1.8264043185510468e-09, 4.148822411262262e-10, 8.63901453249607e-11, 1.6605098550763472e-11, 2.963698545347599e-12, 4.937002795529254e-13, 7.710170742987013e-14, 1.1332759684949982e-14, 1.5731994271563547e-15], [6.001619587787444e-08, 1.4996470910877307e-07, 1.8736120849647075e-07, 1.5605548202142258e-07, 9.748541466121014e-08, 4.871808896973453e-08, 2.028895126783322e-08, 7.242394277309627e-09, 2.379091730275319e-09, 6.444187261796264e-10, 1.6102331279447335e-10, 3.657772389562671e-11, 7.616510348627037e-12, 1.4639737492757751e-12, 2.6129184707284954e-13, 4.3526646172320546e-14, 6.7976034804371015e-15, 9.991426810806105e-16, 1.3869972868223033e-16], [4.703355152060216e-09, 1.1752449099726912e-08, 1.4683141648485869e-08, 1.2229771391480158e-08, 7.639746581581703e-09, 3.817943996660459e-09, 1.5900065320641525e-09, 5.675726683302418e-10, 1.7727687680637745e-10, 5.176409107327082e-11, 1.2619090842991838e-11, 2.866526670320927e-12, 5.968914334695692e-13, 1.147288390311917e-13, 2.0476945216957356e-14, 3.41110049599059e-15, 5.327152593349043e-16, 7.830091207823783e-17, 1.0869634003700973e-17], [3.317336999879736e-10, 8.289153801334765e-10, 1.0356209023182376e-09, 8.625815364858591e-10, 5.388411715769419e-10, 2.6928451018721424e-10, 1.1214520971388789e-10, 4.003163171608768e-11, 1.2503566574072498e-11, 3.4714587300152355e-12, 9.122860137506101e-13, 2.0217982008933206e-13, 4.2099522003829865e-14, 8.091972865470443e-15, 1.4442653343532448e-15, 2.4058931379445256e-16, 3.757309373964925e-17, 5.522664233588437e-18, 7.666492937458386e-19], [2.1270550325703848e-11, 5.314951815121058e-11, 6.640334256637023e-11, 5.53081703261097e-11, 3.4550147476738354e-11, 1.7266348658810675e-11, 7.190678327502881e-12, 2.5668023389482427e-12, 8.017206032255371e-13, 2.2258768892961421e-13, 5.5618816776472134e-14, 1.3287646646224578e-14, 2.699394126984999e-15, 5.188520674126836e-16, 9.260535929615804e-17, 1.5426431222022315e-17, 2.4091624737268813e-18, 3.5410965939476806e-19, 4.9157056956761864e-20], [1.2501994378125553e-12, 3.1239200065432667e-12, 3.9029277698109354e-12, 3.2507971062970285e-12, 2.0307220213085785e-12, 1.0148481847333856e-12, 4.2263984076009334e-13, 1.5086656395773614e-13, 4.712198942140639e-14, 1.3082830453498916e-14, 3.2690556850199435e-15, 7.425919525001374e-16, 1.626252595035803e-16, 3.049608745681357e-17, 5.442979441419573e-18, 9.067050615009492e-19, 1.416011115900823e-19, 2.081317550887979e-20, 2.8892588123401008e-21], [6.782936727245381e-14, 1.6948777214644625e-13, 2.1175271171099095e-13, 1.7637146856909009e-13, 1.1017649316224646e-13, 5.506042329414696e-14, 2.2930255858254448e-14, 8.185240903425128e-15, 2.5565958761473044e-15, 7.098068395761597e-16, 1.7736208478968007e-16, 4.0289205670921435e-17, 8.389345187419528e-18, 1.695913596746173e-18, 2.953079648111452e-19, 4.91931357223676e-20, 7.682545291362912e-21, 1.1292154539502468e-21, 1.567562672002845e-22], [3.4172090599862024e-15, 8.538707846253523e-15, 1.0667994027261217e-14, 8.885504974511655e-15, 5.5506357463021086e-15, 2.7739161500898325e-15, 1.1552146395806138e-15, 4.1236827790244143e-16, 1.2880000126791515e-16, 3.575970793442547e-17, 8.935411716386043e-18, 2.029749711291087e-18, 4.2265094802740525e-19, 8.123797706520257e-20, 1.524930584474492e-20, 2.4783251833144243e-21, 3.870427283797064e-22, 5.68893008306492e-23, 7.897301095774348e-24], [1.6068010579002604e-16, 4.014973786975975e-16, 5.016182442389462e-16, 4.1780407760832176e-16, 2.6099566144815387e-16, 1.3043192050149126e-16, 5.431918482000903e-17, 1.9389910700424828e-17, 6.0562867141548706e-18, 1.6814521889237641e-18, 4.2015073548708923e-19, 9.544057522159429e-20, 1.9873410683738638e-20, 3.819879474701253e-21, 6.817768174013478e-22, 1.1944555173821197e-22, 1.819908160420324e-23, 2.6749837997404346e-24, 3.7133788224529474e-25], [7.083109328990904e-18, 1.769882970039016e-17, 2.21123632442957e-17, 1.8417662505557298e-17, 1.150522521341483e-17, 5.7497071486223775e-18, 2.394501315829166e-18, 8.54747118165047e-19, 2.6697356659779354e-19, 7.412186858516106e-20, 1.8521108008230594e-20, 4.2072167266291106e-21, 8.76060791227052e-22, 1.6838813871727493e-22, 3.005412345157276e-23, 5.006490681399364e-24, 8.223040697421325e-25, 1.1791878411880607e-25, 1.636933710621592e-26], [2.9387107577952602e-19, 7.343066275716049e-19, 9.174196913821453e-19, 7.6413027703801465e-19, 4.773402122586786e-19, 2.385495615981984e-19, 9.934544914591298e-20, 3.5462597493239203e-20, 1.1076464526627284e-20, 3.0752417121045848e-21, 7.68422126809517e-22, 1.745531867525549e-22, 3.6346880332967286e-23, 6.986254365836178e-24, 1.2469153277325775e-24, 2.0771425853913894e-25, 3.2438960750436955e-26, 5.014608367802922e-27, 6.791473181858556e-28], [1.1515058711165902e-20, 2.877310707103745e-20, 3.5948218384618263e-20, 2.994171842101797e-20, 1.8704122393735845e-20, 9.347337774020965e-21, 3.892756973675715e-21, 1.3895681672716161e-21, 4.340207317032789e-22, 1.2050042275163496e-22, 3.010989047390634e-23, 6.839700669230718e-24, 1.424217949628505e-24, 2.737497352549843e-25, 4.885919163227035e-26, 8.139085739826041e-27, 1.2710898361794883e-27, 1.8683056616491903e-28, 2.7276863786342726e-29]] |
| Legacy trial inputs | {"lambda_home": 0.7053128867860723, "lambda_away": 2.498737331068647, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0855 |
| Legacy p draw | 0.1468 |
| Legacy p away | 0.7677 |
| Legacy p over 1 5 | 0.8259 |
| Legacy p under 3 5 | 0.6017 |
| Legacy p btts yes | 0.4618 |
| Legacy p over 2 5 | 0.6199 |
| Legacy goal margin distribution | {"-1": 0.2245803547125815, "-10": 0.00012430232011209042, "-11": 2.786829418145404e-05, "-12": 5.738746139501601e-06, "-13": 1.0925553196167212e-06, "-14": 1.9338937487572025e-07, "-15": 3.1981810710685426e-08, "-16": 4.961963797988292e-09, "-17": 7.222049820893587e-10, "-18": 9.131488649130965e-11, "-2": 0.21937502188361188, "-3": 0.16090772019110053, "-4": 0.09277782575257056, "-5": 0.04388807417006365, "-6": 0.017562483381604564, "-7": 0.006082221249874042, "-8": 0.0018551824690630002, "-9": 0.0005053268514621514, "0": 0.14680476841089557, "1": 0.06428012725453255, "10": 3.8896820087562894e-10, "11": 2.4615375395036232e-11, "12": 1.4307847557314032e-12, "13": 7.688859771300185e-14, "14": 3.841601636327527e-15, "15": 1.793262969002194e-16, "16": 7.853364174947127e-18, "17": 3.226441828505635e-19, "18": 1.1515058711165902e-20, "2": 0.017034615318785692, "3": 0.0035268196256104107, "4": 0.0005739998402866741, "5": 7.66434982121359e-05, "6": 8.657169778388604e-06, "7": 8.462787507755927e-07, "8": 7.286166100756493e-08, "9": 5.6020376774608014e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0878 |
| Legacy raw p draw | 0.1434 |
| Legacy raw p away | 0.7687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7053 |
| Legacy lambda away | 2.4987 |
| Legacy model home team | Casa Pia |
| Legacy model away team | Sp Lisbon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,356.0841 |
| Elo away rating | 1,692.9144 |
| Elo rating diff | -276.8303 |
| Elo home expectancy | 0.1689 |

</details>


---

## 2026-10-31 — Moreirense FC vs CF Estrela

The model's most likely 1X2 outcome is **Moreirense FC win** at **36.2%**. Expected goals are 1.42 for Moreirense FC and 1.07 for CF Estrela (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.0%; Double Chance 1X: 64.3%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Moreirense FC win | 36.2% | 2.76 |
| Draw | 28.1% | 3.56 |
| CF Estrela win | 35.7% | 2.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Moreirense FC expected goals | 1.42 |
| CF Estrela expected goals | 1.07 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.31% |
| 2 | 0-1 | 10.60% |
| 3 | 1-0 | 8.80% |
| 4 | 1-2 | 8.47% |
| 5 | 0-0 | 7.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Moreirense FC win | 36.2% | 32.1% | 2.97 | +7.6% |
| Draw | 28.1% | 29.3% | 3.25 | -8.8% |
| CF Estrela win | 35.7% | 38.6% | 2.49 | -11.1% |
| Over 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |
| Under 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 853df01a49c2a57a62c1ac2d356b395b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:14:41Z |
| Market best draw last update utc | 2026-10-28T16:14:41Z |
| Market best away last update utc | 2026-10-28T16:14:41Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Moreirense |
| Matched away-team name | Estrela |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4765 |
| Dc lambda away | 1.0418 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2893 |
| Shot lambda away | 1.1236 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.42 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.72 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.21872996657801275, "-10": 9.982083185191333e-08, "-11": 1.0176408241512424e-08, "-12": 9.528387958050414e-10, "-13": 8.246216455196655e-11, "-14": 6.600269316144197e-12, "-15": 4.484223426430618e-13, "-2": 0.0957669161586748, "-3": 0.03201902173557846, "-4": 0.008407549660867866, "-5": 0.0018102193611761349, "-6": 0.0003295979748923705, "-7": 5.192528720027135e-05, "-8": 7.20369288314964e-06, "-9": 8.923705897941869e-07, "0": 0.28068750647868057, "1": 0.183289642722991, "10": 1.1136046104316675e-06, "11": 1.5122119616318007e-07, "12": 1.886018255023945e-08, "13": 2.174149997280563e-09, "14": 2.3179536209102695e-10, "15": 2.0976771183972706e-11, "2": 0.10780994855980419, "3": 0.048013095589747805, "4": 0.016793043084940784, "5": 0.004816144170637705, "6": 0.001168049157502607, "7": 0.0002451115665314033, "8": 4.5294805580365805e-05, "9": 7.473891206761343e-06} |
| Raw goal margin distribution | {"-1": 0.18144174138798785, "-10": 4.996429089500423e-08, "-11": 4.789046113861454e-09, "-12": 4.2142153783622436e-10, "-13": 3.411709660847204e-11, "-14": 2.344899710685362e-12, "-2": 0.0761759267126866, "-3": 0.024224654874291377, "-4": 0.006022975765295864, "-5": 0.0012247629761651271, "-6": 0.00021027999090511107, "-7": 3.1205717994682775e-05, "-8": 4.075131656593047e-06, "-9": 4.7494157618237995e-07, "0": 0.253115843622346, "1": 0.23959117436808156, "10": 8.785021981292213e-07, "11": 1.1216063403015002e-07, "12": 1.3146691646829439e-08, "13": 1.4176862489447205e-09, "14": 1.2978982506966096e-10, "2": 0.13515570155374906, "3": 0.05725092866213206, "4": 0.01896026335939899, "5": 0.005135628633555707, "6": 0.001174485945490466, "7": 0.00023216265756403114, "8": 4.0383889383776515e-05, "9": 6.269241518573579e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 28.9% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.1% |
| P home draw | 64.3% |
| P draw away | 63.8% |
| P home away | 71.9% |
| Raw p home draw | 71.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0652 |
| Totals anchor target over 2 5 | 0.4793 |
| Totals anchor reference over odds | 2.00 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-28T16:14:41Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4414 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:41Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:14:41Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.12, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.97 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.49 |
| Market reference 1x2 last update utc | 2026-10-28T16:14:41Z |
| Market reference home last update utc | 2026-10-28T16:14:41Z |
| Market reference draw last update utc | 2026-10-28T16:14:41Z |
| Market reference away last update utc | 2026-10-28T16:14:41Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-28T16:14:41Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:14:41Z |
| Market best over 2 5 last update utc | 2026-10-28T16:14:41Z |
| Market best under 2 5 last update utc | 2026-10-28T16:14:41Z |
| Home probability edge | +4.1% |
| Draw probability edge | -1.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1362 |
| Raw ev home | 0.3589 |
| Raw edge prob draw | -0.0394 |
| Raw ev draw | -0.1774 |
| Raw edge prob away | -0.0968 |
| Raw ev away | -0.2796 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.08557426875032603, 0.11250128302696014, 0.05225125634242329, 0.0173640226831399, 0.004327780394858163, 0.0008629190821919302, 0.00014338168654453483, 2.0420694421942486e-05, 2.5448101105766145e-06, 2.818952345359488e-07, 2.8103641458915942e-08, 2.5470928283354654e-09, 2.1161107283927203e-10, 1.6228183084785948e-11, 1.1556244586885131e-12, 7.680691611453806e-14], [0.10893454899406592, 0.12811103179245906, 0.07656024761253077, 0.02544233324187929, 0.0063412052041700384, 0.0012643772270132564, 0.00021008753077654245, 2.9921068521646108e-05, 3.7287389018133926e-06, 4.130421059242948e-07, 4.11783734884374e-08, 3.732083614440048e-09, 3.100594563307029e-10, 2.3778063959467938e-11, 1.6932587060582466e-12, 1.1254000243645048e-13], [0.07601791388677767, 0.07578631826982206, 0.04924752241661003, 0.018639468877778027, 0.0046456705022703704, 0.0009263034073420574, 0.00015391355636647374, 2.1920663494064476e-05, 2.731735020249944e-06, 3.0260139293809173e-07, 3.016794897615116e-08, 2.7341854113487863e-09, 2.2715462184984822e-10, 1.742019801929064e-11, 1.2405089837298317e-12, 8.244864387934324e-14], [0.03712797686636336, 0.037014863045304214, 0.018451046917989888, 0.007993248803110682, 0.002268996057875806, 0.0004524166702371382, 7.517305682323012e-05, 1.0706290734512303e-05, 1.3342091284948554e-06, 1.4779381519819605e-07, 1.4734354764857515e-08, 1.33540592618871e-09, 1.109447906935477e-10, 8.508214393136488e-12, 6.058780949847696e-13, 4.02688154159902e-14], [0.013600281128232023, 0.013558846611844822, 0.006758769164775142, 0.0022460593161274267, 0.0007297679782134703, 0.0001657239209254657, 2.753650460795039e-05, 3.9218017279543515e-06, 4.887316994593036e-07, 5.413808145119968e-08, 5.397314477070653e-09, 4.891700962280967e-10, 4.063998285110173e-11, 3.1166284137275244e-12, 2.2193809403861653e-13, 1.4750795938318886e-14], [0.003985515234136411, 0.003973372992757483, 0.001980633871920887, 0.0006581998957813859, 0.0001640486572058124, 4.2640888791533e-05, 8.069477209705325e-06, 1.1492703999756552e-06, 1.43221130154215e-07, 1.5864977079243882e-08, 1.5816642956840425e-09, 1.4334960080744248e-10, 1.190940608072298e-11, 9.133171516777438e-13, 6.503818902610372e-14, 4.322669610539866e-15], [0.0009732845183962188, 0.000970319316945847, 0.0004836815746281949, 0.00016073599796760963, 4.006157521480462e-05, 7.987904782921677e-06, 1.7302354340445941e-06, 2.806580886121511e-07, 3.497537971812862e-08, 3.87431377596647e-09, 3.862510320131545e-10, 3.500675295107567e-11, 2.908341802932055e-12, 2.2303702078466432e-13, 1.5882679845620938e-14, 1.0556194526733217e-15], [0.00020372689561357543, 0.00020310622275282908, 0.00010124372041472605, 3.364509068042144e-05, 8.385646948695584e-06, 1.6720198596840094e-06, 2.7782098271426053e-07, 5.1581097208123484e-08, 7.321009836488155e-09, 8.109673002003286e-10, 8.084966131922543e-11, 7.327576848736736e-12, 6.087710589200292e-13, 4.668587549942138e-14, 3.324545903909476e-15, 2.2096115778848597e-16], [3.731341278976073e-05, 3.719973402098216e-05, 1.854320079255194e-05, 6.162235737831769e-06, 1.5358654789467367e-06, 3.062372644965094e-07, 5.088404738340011e-08, 7.2470034884497725e-09, 1.1773133162374412e-09, 1.4853197237525804e-10, 1.480794559614143e-11, 1.3420756198249785e-12, 1.1149890517660815e-13, 8.550708725594538e-15, 6.089041570945939e-16, 4.046993827807502e-17], [6.074759031696568e-06, 6.056251715540828e-06, 3.018900391819137e-06, 1.0032343440348423e-06, 2.5004447441652767e-07, 4.985653815221951e-08, 8.284107598338182e-09, 1.179838471014302e-09, 1.4703049797651518e-10, 2.1231881984714053e-11, 2.410787288685539e-12, 2.184947819886576e-13, 1.8152426449497736e-14, 1.3920864154368108e-15, 9.91318068006636e-17, 6.588652837844999e-18], [8.900935369003544e-07, 8.873817844819221e-07, 4.423391468342247e-07, 1.4699717321503188e-07, 3.6637333177253545e-08, 7.305142829529297e-09, 1.213814505858451e-09, 1.7287378678836816e-10, 2.1543388847736233e-11, 2.3864172130924554e-12, 3.1014868614867793e-13, 3.2014569183699986e-14, 2.659752819404349e-15, 2.0397304892619468e-16, 1.4525116152612625e-17, 9.653909360431307e-19], [1.1856310233840132e-07, 1.1820188886344158e-07, 5.8920887929398056e-08, 1.9580459995296696e-08, 4.880201577496803e-09, 9.730667182578165e-10, 1.616836967259573e-10, 2.302730176650056e-11, 2.8696433698024613e-12, 3.1787785949251133e-13, 3.1690941514536125e-14, 3.744260269641618e-15, 3.542869739511348e-16, 2.716981583568055e-17, 1.9347886053375197e-18, 1.2859293950750308e-19], [1.4476877540275788e-08, 1.4432772391711403e-08, 7.1944008067840094e-09, 2.3908274660789507e-09, 5.958858971793212e-10, 1.1881409511813894e-10, 1.9742019495070634e-11, 2.8116962291111717e-12, 3.503912670092059e-13, 3.8813751950446226e-14, 3.869550225942305e-15, 3.5070557115489596e-16, 3.798262639700014e-17, 3.3175084734401095e-18, 2.362429554672695e-19, 1.570154796119277e-20], [1.6316918360132834e-09, 1.6267207356749374e-09, 8.108823901271473e-10, 2.694706539351601e-10, 6.716242165604631e-11, 1.339156102330888e-11, 2.2251270653428604e-12, 3.1690685851464584e-13, 3.9492671551491216e-14, 4.374705941000954e-15, 4.3613779940789183e-16, 3.952809683619925e-17, 3.2839725689420762e-18, 3.2830669662707506e-19, 2.662699195176378e-20, 1.7697246902705502e-21], [1.7077201273927654e-10, 1.7025173998214707e-10, 8.486652614208512e-11, 2.8202657469386087e-11, 7.029183865177856e-12, 1.401553761069799e-12, 2.3288063294946e-13, 3.316730578958822e-14, 4.13328231498513e-15, 4.578544319450292e-16, 4.5645953600247226e-17, 4.136989906723919e-18, 3.4369884864352874e-19, 2.635782602006728e-20, 2.4468374793962325e-21, 1.8521845895258515e-22], [1.6681382095935167e-11, 1.6630560720016668e-11, 8.289947088063994e-12, 2.7548969987598363e-12, 6.866259874598642e-13, 1.369068235560072e-13, 2.274828737249929e-14, 3.2398546582310882e-15, 4.037480176093316e-16, 4.4724217985607694e-17, 4.4587961512262804e-18, 4.0411018324442843e-19, 3.357325201120061e-20, 2.5746898452863386e-21, 1.8334612958238524e-22, 1.588561600166414e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4652326656186216, "lambda_away": 0.99695340736, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T16:14:41Z", "over": 2.0, "under": 1.85, "bookmaker": "pinnacle", "event_id": "853df01a49c2a57a62c1ac2d356b395b", "kickoff_utc": "2026-10-31T15:30:00Z", "home_team": "Moreirense FC", "away_team": "CF Estrela"}} |
| Legacy p home | 0.4036 |
| Legacy p draw | 0.2717 |
| Legacy p away | 0.3247 |
| Legacy p over 1 5 | 0.6930 |
| Legacy p under 3 5 | 0.7702 |
| Legacy p btts yes | 0.4861 |
| Legacy p over 2 5 | 0.4366 |
| Legacy goal margin distribution | {"-1": 0.21014407710335348, "-10": 3.2071614170362625e-08, "-11": 2.875193111576382e-09, "-12": 2.366699145978858e-10, "-13": 1.800389043472354e-11, "-14": 1.2681644611249636e-12, "-15": 7.680691611453806e-14, "-2": 0.08282039833319416, "-3": 0.024710773330857205, "-4": 0.005757282459340458, "-5": 0.0010963172409609535, "-6": 0.00017618782752135015, "-7": 2.4467270377363173e-05, "-8": 2.989397140806893e-06, "-9": 3.259219209486508e-07, "0": 0.2717002636449012, "1": 0.2055902952774292, "10": 1.015766463315204e-06, "11": 1.3383564640369672e-07, "12": 1.6191219699091572e-08, "13": 1.8102335230834944e-09, "14": 1.874025734592932e-10, "15": 1.6681382095935167e-11, "2": 0.12049153167346395, "3": 0.05283689369220017, "4": 0.018092567745511837, "5": 0.00506349802138741, "6": 0.0011959748067486343, "7": 0.00024409752847396248, "8": 4.383219362570977e-05, "9": 7.023521118297671e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4858 |
| Legacy raw p draw | 0.2509 |
| Legacy raw p away | 0.2633 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4652 |
| Legacy lambda away | 0.9970 |
| Legacy model home team | Moreirense |
| Legacy model away team | Estrela |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,438.8922 |
| Elo away rating | 1,379.1640 |
| Elo rating diff | 119.7282 |
| Elo home expectancy | 0.6658 |

</details>


---
