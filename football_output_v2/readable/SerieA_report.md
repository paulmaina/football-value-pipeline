# Serie A — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 2,000 |
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
| Training sha256 | 079ee821e838fc2e9bc0f0bb96c5af05c9809c654a7f24f340352fccd328966d |
| Training as of utc | 2026-11-05T12:28:47.541976+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 191, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-05T12:28:47.541976+00:00', 'observations': 695, 'observations_sha256': '13377d2c377d012ea62a498d6a4cdfd527fc649cf2fabe7d3a6866654d8a9903', 'eligible_training_matches': 251, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 236, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 36, 'retrospective_eligible_training_matches': 251, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '3cfe277da88929df0bcfc8e0be5de15bf2b494e5848ae22e0064e69194622fea', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 190, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-11T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 24, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1620, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8311477877010042, 'audit_candidate_poisson_score': 0.8301690994125219, 'audit_gain': 0.0009786882884822434, 'audit_gain_lower95': -0.0035260819529456993, 'audit_baseline_briers': [0.5470516271063433, 0.1544999061324679, 0.2090980014289932, 0.23872219104127412], 'audit_candidate_briers': [0.5497540597359728, 0.15368329188971547, 0.2092140547665856, 0.23948201814979928], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1825.675 |
| Base scoring parameter | 0.153 |
| Home-advantage parameter | 0.106 |
| Dixon-Coles low-score adjustment | -0.022 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 2000, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 3.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261105T122847541976Z_f936e1c4f13eb585d0e7f77afce1823913ed0514c0e7dedc550c8bb847715f9e.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4, 'ANCHORED_MAIN': 1} |
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

## 2026-11-06 — Venezia vs Udinese

The model's most likely 1X2 outcome is **Venezia win** at **37.8%**. Expected goals are 0.95 for Venezia and 1.32 for Udinese (2.27 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.1%; Under 3.5 goals: 68.7%; Double Chance 1X: 65.1%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 37.8% | 2.65 |
| Draw | 27.3% | 3.66 |
| Udinese win | 34.9% | 2.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.95 |
| Udinese expected goals | 1.32 |
| Expected total goals | 2.27 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.87% |
| 2 | 2-1 | 9.47% |
| 3 | 1-0 | 9.19% |
| 4 | 1-2 | 6.88% |
| 5 | 0-1 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 37.8% | 42.6% | 2.31 | -12.7% |
| Draw | 27.3% | 26.8% | 3.64 | -0.6% |
| Udinese win | 34.9% | 30.6% | 3.25 | +13.4% |
| Over 2.5 | 53.1% | 53.3% | 1.84 | -2.3% |
| Under 2.5 | 46.9% | 46.7% | 2.12 | -0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fa069801a5c9b49143447a1a1d173fd1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:31Z |
| Market best draw last update utc | 2026-11-05T12:28:31Z |
| Market best away last update utc | 2026-11-05T12:28:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9463 |
| Dc lambda away | 1.3188 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.09 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.20 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.47 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.06625689394905245,0.06753349201701624,0.057681403416924716,0.03197254012028334,0.013291675408202502,0.004420509211776684,0.0012251340965478488,0.0002910369725587438,6.0495177369136715e-05,1.1177400750452049e-05,1.8586747518150063e-06,2.8097863066931244e-07,3.893629493150014e-08,4.9805103608433646e-09,5.915730617985824e-10,6.558125264644419e-11],[0.09191353402458886,0.12870713925129681,0.06882531373513184,0.03814955903174021,0.015859595568832062,0.005274541105917346,0.0014618270979476894,0.00034726462530904967,7.21827021405587e-05,1.3336848062324327e-05,2.2177663050358628e-06,3.3526303562525547e-07,4.6458694754258005e-08,5.942733148644926e-09,7.058635741098043e-10,7.82513950971256e-11],[0.05694201005629451,0.09468809320892481,0.06245422963844298,0.022759981672412295,0.009461815906657503,0.003146784968108922,0.0008721243128876967,0.00020717766359855505,4.306411448733779e-05,7.9567477362897e-06,1.3231167472817644e-06,2.0001752942726089e-07,2.7717202189712326e-08,3.5454275483148547e-09,4.211173711495912e-10,4.668468950766874e-11],[0.022647690443696716,0.037660536071339054,0.03131259632646944,0.013768743357092356,0.003763272098708373,0.0012515787865611328,0.00034687222047790825,8.24012989248126e-05,1.7127999752325722e-05,3.1646575084357014e-06,5.262465881285803e-07,7.95534805550977e-08,1.1024033302255489e-08,1.4101319135978291e-09,1.6749208278440463e-10,1.856802026104277e-11],[0.006755792629111958,0.0112341155771126,0.009340528915591766,0.005177412784842162,0.0017074550560654098,0.00037334520983599415,0.00010347177767084688,2.4580258604710683e-05,5.109272169092137e-06,9.440154581017832e-07,1.5697904517075665e-07,2.373075607380144e-08,3.288462596732044e-09,4.206415136078999e-10,4.996278897058222e-11,5.538829432899948e-12],[0.001612199148024514,0.0026809040117932994,0.002229019389216339,0.0012355353307804187,0.0005136387196737342,0.00013551402066538034,2.4692455935766223e-05,5.8658212524125205e-06,1.2192742865641318e-06,2.2527940107506283e-07,3.746140486779015e-08,5.663096371445212e-09,7.847571540186216e-10,1.0038169125264303e-10,1.1923096257306147e-11,1.321783628214799e-12],[0.00032061203320670763,0.0005331413846150969,0.00044327677465250565,0.0002457063043269943,0.00010214541699148827,3.3971244623758665e-05,7.468900755925839e-06,1.1665140007470707e-06,2.4247253109579254e-07,4.480047449892773e-08,7.4498099047867944e-09,1.1261988595635768e-09,1.5606172911809157e-10,1.9962532649067313e-11,2.371101695381919e-12,2.628581816462056e-13],[5.46505025030441e-05,9.087757649944057e-05,7.555954229287875e-05,4.188231135722446e-05,1.7411381323198017e-05,5.790629786328945e-06,1.6048599045596937e-06,3.024374497669259e-07,4.1331092707386295e-08,7.63654570058723e-09,1.2698707867469885e-09,1.9196825826503942e-10,2.6601783571544427e-11,3.402749515023905e-12,4.041704169440719e-13,4.480596554758704e-14],[8.15110624425916e-06,1.3554363589364412e-05,1.1269683329307763e-05,6.246734320674599e-06,2.596902361818018e-06,8.636707156884764e-07,2.3936437891836455e-07,5.686225236494675e-08,9.376279653038668e-09,1.1389885269794148e-09,1.8940085132207365e-10,2.8632008800954022e-11,3.967648132171678e-12,5.075190812383884e-13,6.028189784923112e-14,6.6827964762932344e-15],[1.0806534039991481e-06,1.7970038314989546e-06,1.4941066018353413e-06,8.281765082217816e-07,3.4429085979937846e-07,1.1450331658975463e-07,3.173433434958038e-08,7.538656071440185e-09,1.5669910670014351e-09,2.2967857854445136e-10,2.511029405924989e-11,3.795960553928068e-12,5.260209266591254e-13,6.728561820931492e-14,7.992024169256959e-15,8.859885448586951e-16],[1.289433078310923e-07,2.1441807091999372e-07,1.7827644532462278e-07,9.881782451518053e-08,4.108070372448267e-08,1.36625085749745e-08,3.786533247116829e-09,8.995106542534065e-10,1.8697300241983696e-10,3.454609554757608e-11,4.5571723145366824e-12,4.529331128819692e-13,6.276469219529473e-14,8.028504004393882e-15,9.536064281446912e-16,1.0571594301351617e-16],[1.398680445880327e-08,2.325846669235676e-08,1.9338093789499995e-08,1.0719017619345482e-08,4.456127112676872e-09,1.4820066203452267e-09,4.1073477169948795e-10,9.757217990819104e-11,2.028143118018425e-11,3.747301751185328e-12,6.231337059359387e-13,7.472828899618266e-14,6.8082438043432856e-15,8.708719940182802e-16,1.0344008437095049e-16,1.1467273858407228e-17],[1.3907518252619097e-09,2.3126622739641933e-09,1.9228473032598785e-09,1.065825533132162e-09,4.4308669173206544e-10,1.473605653361446e-10,4.084064627643131e-11,9.701907801870469e-12,2.016646298004972e-12,3.7260596340059603e-13,6.19601383193123e-14,9.366606397402836e-15,1.0296686856314773e-15,8.659353312743967e-17,1.0285371942381052e-17,1.140226997262431e-18],[1.2764936761533097e-10,2.1226639535329603e-10,1.764874493231344e-10,9.782619215112073e-11,4.0668460735412513e-11,1.3525405924277025e-11,3.7485355586041384e-12,8.904841058452571e-13,1.850967368643606e-13,3.419942705365861e-14,5.686976159336823e-15,8.597086565786238e-16,1.191331516136005e-16,1.2088871442222658e-17,9.440370311116844e-19,1.0465508834480001e-19],[1.0879351617903758e-11,1.8091125673826877e-11,1.504174327850525e-11,8.337570030584593e-12,3.4661079201956547e-12,1.152748733299761e-12,3.194816954923303e-13,7.589453734576623e-14,1.5775499097984826e-14,2.9147625170288434e-15,4.846918902607267e-16,7.327159498400203e-17,1.0153528137006882e-17,1.298781822318836e-18,1.2237836493694298e-19,8.919585940581775e-21],[8.654144362899201e-13,1.4390858827560957e-12,1.196518160031076e-12,6.632245855692252e-13,2.7571678324467276e-13,9.169713694801525e-14,2.5413653416113794e-14,6.037145462463313e-15,1.2548858735852891e-15,2.3185918142790375e-16,3.8555547583735914e-17,5.828499555505809e-18,8.076777125744505e-19,1.03313559309541e-19,1.227133650530252e-20,1.0791879486991094e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1632813061986926, "-10": 2.223116406116171e-06, "-11": 3.3115578388410256e-07, "-12": 4.53187134715557e-08, "-13": 5.733058624460838e-09, "-14": 6.69824456895708e-10, "-15": 6.558125264644419e-11, "-2": 0.1066539450431441, "-3": 0.051351638510104956, "-4": 0.019526084323316584, "-5": 0.006107624603254484, "-6": 0.0016187902955198607, "-7": 0.0003717272049103345, "-8": 7.523808691949356e-05, "-9": 1.3606641445685474e-05, "0": 0.2730377562214123, "1": 0.22364090963344943, "10": 1.5422600582391725e-07, "11": 1.6484567468904426e-08, "12": 1.61872318847928e-09, "13": 1.469370114491889e-10, "14": 1.2318437500659855e-11, "15": 8.654144362899201e-13, "2": 0.10528679351460171, "3": 0.03637483942089634, "4": 0.009924571018750156, "5": 0.0022275051832462687, "6": 0.0004236300740011604, "7": 6.980239783212203e-05, "8": 1.013756247631858e-05, "9": 1.315517240864896e-06} |
| Raw goal margin distribution | {"-1": 0.23920859890619775, "-10": 5.097408989962441e-07, "-11": 6.054525661434903e-08, "-12": 6.6007664972568274e-09, "-13": 6.628455614269158e-10, "-14": 5.732963364566295e-11, "-2": 0.13421318839360882, "-3": 0.0537286145412426, "-4": 0.01671203504696717, "-5": 0.00423670424701943, "-6": 0.0009049160702146152, "-7": 0.00016683089023353427, "-8": 2.7039744758067517e-05, "-9": 3.908629596904667e-06, "0": 0.2856380055664835, "1": 0.17082905024132375, "10": 1.8443677554662958e-08, "11": 1.5719110565386923e-09, "12": 1.2296797416741337e-10, "13": 8.860532135825922e-12, "14": 5.498907612046452e-13, "2": 0.0691026658172446, "3": 0.019849750578585065, "4": 0.0044302532608210725, "5": 0.0008058926007340386, "6": 0.00012351142292600737, "7": 1.633898580837374e-05, "8": 1.9002074659085025e-06, "9": 1.9709370460463514e-07} |
| Research history json | {"away": [{"away": "Roma", "away_goals": 5.0, "away_xg": 2.76, "date": "2026-10-31T00:00:00+00:00", "home": "Udinese", "home_goals": 2.0, "home_xg": 1.77, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 0.0, "away_xg": 1.37, "date": "2026-10-28T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 1.12, "source": "pipeline training history"}, {"away": "Milan", "away_goals": 2.0, "away_xg": 3.59, "date": "2026-10-25T00:00:00+00:00", "home": "Udinese", "home_goals": 0.0, "home_xg": 0.55, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 3.0, "away_xg": 3.47, "date": "2026-10-18T00:00:00+00:00", "home": "Udinese", "home_goals": 0.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 1.0, "away_xg": 0.7, "date": "2026-10-12T00:00:00+00:00", "home": "Torino", "home_goals": 2.0, "home_xg": 2.42, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 1.0, "away_xg": 1.12, "date": "2026-09-19T00:00:00+00:00", "home": "Udinese", "home_goals": 0.0, "home_xg": 2.13, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 3.0, "away_xg": 0.9, "date": "2026-09-14T00:00:00+00:00", "home": "Inter", "home_goals": 5.0, "home_xg": 3.1, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-09-07T00:00:00+00:00", "home": "Udinese", "home_goals": 1.0, "home_xg": 0.77, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 3.0, "away_xg": 0.89, "date": "2026-08-29T00:00:00+00:00", "home": "Monza", "home_goals": 2.0, "home_xg": 1.65, "source": "pipeline training history"}, {"away": "Como", "away_goals": 1.0, "away_xg": 1.51, "date": "2026-08-22T00:00:00+00:00", "home": "Udinese", "home_goals": 1.0, "home_xg": 2.14, "source": "pipeline training history"}], "h2h": [{"away": "Venezia", "away_goals": 2.0, "away_xg": null, "date": "2025-02-01T00:00:00+00:00", "home": "Udinese", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 2.0, "away_xg": null, "date": "2024-10-30T00:00:00+00:00", "home": "Venezia", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Venezia", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-11-01T00:00:00+00:00", "home": "Como", "home_goals": 1.0, "home_xg": 1.63, "source": "pipeline training history"}, {"away": "Inter", "away_goals": 2.0, "away_xg": 2.33, "date": "2026-10-28T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 0.0, "away_xg": 1.98, "date": "2026-10-25T00:00:00+00:00", "home": "Genoa", "home_goals": 1.0, "home_xg": 0.34, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 0.0, "away_xg": 2.36, "date": "2026-10-17T00:00:00+00:00", "home": "Venezia", "home_goals": 1.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 1.0, "away_xg": 2.63, "date": "2026-10-12T00:00:00+00:00", "home": "Atalanta", "home_goals": 3.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": 1.6, "date": "2026-09-19T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 1.89, "source": "pipeline training history"}, {"away": "Fiorentina", "away_goals": 4.0, "away_xg": 3.31, "date": "2026-09-11T00:00:00+00:00", "home": "Venezia", "home_goals": 2.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-06T00:00:00+00:00", "home": "Frosinone", "home_goals": 3.0, "home_xg": 1.9, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 0.0, "away_xg": 0.8, "date": "2026-08-28T00:00:00+00:00", "home": "Milan", "home_goals": 2.0, "home_xg": 2.21, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 2.0, "away_xg": 2.7, "date": "2026-08-23T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 2.05, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 45.1% |
| P home draw | 65.1% |
| P draw away | 62.2% |
| P home away | 72.7% |
| Raw p home draw | 55.1% |
| Raw p draw away | 73.5% |
| Raw p home away | 71.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2609 |
| Totals anchor target over 2 5 | 0.5310 |
| Totals anchor reference over odds | 1.83 |
| Totals anchor reference under odds | 2.06 |
| Totals anchor reference last update utc | 2026-11-05T12:29:58Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3949 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.45, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.1, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:20:23Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.25, "under": 3.85}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 3.64, "home": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.16, "draw": 3.6, "home": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:56Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.67, "home_away": 1.32, "home_draw": 1.4}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:58Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.29 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:17Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:17Z |
| Market best over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best under 2 5 last update utc | 2026-11-05T12:28:31Z |
| Home probability edge | -4.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.1611 |
| Raw ev home | -0.3875 |
| Raw edge prob draw | 0.0180 |
| Raw ev draw | 0.0397 |
| Raw edge prob away | 0.1431 |
| Raw ev away | 0.4599 |
| Market p home draw | 69.0% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-05T12:29:56Z |
| Market reference home draw last update utc | 2026-11-05T12:29:56Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 57.8% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T12:28:31Z |
| Market reference draw away last update utc | 2026-11-05T12:29:56Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T12:28:31Z |
| Market reference home away last update utc | 2026-11-05T12:29:56Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home draw odds | 1.40 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 77.6% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T12:20:23Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market reference over 1 5 last update utc | 2026-11-05T12:29:41Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-05T12:20:23Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-05T12:29:58Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 9.549611485246825, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,353.0341 |
| Elo away rating | 1,444.2839 |
| Elo rating diff | -31.2498 |
| Elo home expectancy | 0.4551 |

</details>


---

## 2026-11-07 — AS Roma vs Sassuolo

The model's most likely 1X2 outcome is **AS Roma win** at **74.0%**. Expected goals are 2.37 for AS Roma and 0.91 for Sassuolo (3.28 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 64.9%; Under 3.5 goals: 57.7%; Double Chance 1X: 89.5%; Double Chance X2: 26.0%; Double Chance 12 (either team wins): 84.6%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 74.0% | 1.35 |
| Draw | 15.4% | 6.48 |
| Sassuolo win | 10.5% | 9.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 2.37 |
| Sassuolo expected goals | 0.91 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 84.6% |
| Under 1.5 | 15.4% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.22% |
| 2 | 2-1 | 10.26% |
| 3 | 1-0 | 9.29% |
| 4 | 3-0 | 8.85% |
| 5 | 3-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 74.0% | 76.0% | 1.35 | -0.0% |
| Draw | 15.4% | 14.4% | 6.38 | -1.5% |
| Sassuolo win | 10.5% | 9.6% | 9.39 | -1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T19:45:00+00:00 |
| Fixture id | f110107bca066ac1a598c89661c88fa3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:31Z |
| Market best draw last update utc | 2026-11-05T12:29:20Z |
| Market best away last update utc | 2026-11-05T12:29:20Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Roma |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3670 |
| Dc lambda away | 0.9139 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.37 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.49 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Score matrix json | [[0.03404257004630673,0.02708623584975916,0.013065469624626113,0.003980312352870895,0.0009094326619088138,0.00016623173122581867,2.5320720657072207e-05,3.3059128957198563e-06,3.7767201393436767e-07,3.835179358480491e-08,3.5050891122803023e-09,2.9121903819793556e-10,2.2179507672377287e-11,1.5592721926627671e-12,1.0179050824569307e-13,6.201966389507927e-15,3.5426056441343104e-16,1.9045276116196923e-17,9.67003737932421e-19],[0.09288473309168446,0.07182431017849646,0.03092560667763412,0.009421289690728293,0.002152602057944826,0.00039346592850687286,5.993344826725037e-05,7.825004753816983e-06,8.939392529809994e-07,9.077763891088824e-08,8.296449371565568e-09,6.893074409949489e-10,5.249828366572293e-11,3.6907543256441345e-12,2.409353289214707e-13,1.4679883593952124e-14,8.385249968969215e-16,4.507964391316701e-17,2.288871208941011e-18],[0.11220924232542892,0.1025514993718343,0.03799813762234361,0.011149966581467217,0.002547574885941862,0.0004656615068439174,7.093041050946369e-05,9.260785345635298e-06,1.0579647929103648e-06,1.0743408529269608e-07,9.818733557129361e-09,8.157858619944669e-10,6.213099561446002e-11,4.36795690847253e-12,2.8514364316946736e-13,1.7373440034805053e-14,9.923827841029727e-16,5.335113765060322e-17,2.7088475491938627e-18],[0.08853206182529018,0.08091219131782634,0.03697407791525289,0.009133271963770053,0.0020100131917177113,0.0003674026529294266,5.596344256834859e-05,7.306674599875848e-06,8.347245067681434e-07,8.476450677468839e-08,7.746890615344908e-09,6.436475541010274e-10,4.902078501745361e-11,3.446277891704988e-12,2.2497571610860858e-13,1.3707484654593072e-14,7.829809040306443e-16,4.2093557705650575e-17,2.13725584212566e-18],[0.052388237871075743,0.04787923197579254,0.02187915596849489,0.00666534592890925,0.0012348465573814042,0.00021740798959493781,3.311598172355479e-05,4.3236743739260415e-06,4.939424781914881e-07,5.015881311676693e-08,4.584169169343336e-09,3.8087400738416257e-10,2.9007711931403533e-11,2.039311208144661e-12,1.3312783061544566e-13,8.111309641879435e-15,4.633235576261005e-16,2.4908572876967983e-17,1.2647064254482406e-18],[0.024800303172900114,0.02266576462463645,0.010357471891327394,0.003155338039733357,0.0007209402725962205,0.00010685124201362947,1.5676923293994228e-05,2.046803627145229e-06,2.3382964777835855e-07,2.3744905777322633e-08,2.1701204280884117e-09,1.8030365665381116e-10,1.3732091009080302e-11,9.653986902621941e-13,6.302198153979922e-14,3.839849294853695e-15,2.1933481947897396e-16,1.1791581165094799e-17,5.987050538523316e-19],[0.009783605736421406,0.008941540079408599,0.004085975107011741,0.0012447663696150686,0.00028440762749614324,5.198578660379366e-05,6.420718974942878e-06,8.074546334477127e-07,9.224472246974654e-08,9.367256309497502e-09,8.561025452370816e-10,7.112896472425262e-11,5.417246855123354e-12,3.808453508868303e-13,2.4861882365501793e-14,1.5148029169730184e-15,8.65265792555433e-17,4.651724631106982e-18,2.3618639491854204e-19],[0.0033082178945871787,0.0030234827212781575,0.0013816272170017233,0.0004209039580582213,9.616928850037415e-05,1.7578417828779625e-05,2.677576682584024e-06,2.8346155806711414e-07,3.1191530993486805e-08,3.1674339482939194e-09,2.894815915579689e-10,2.405147143739085e-11,1.8317820104707535e-12,1.2877863630418446e-13,8.406770095864359e-15,5.122138250162155e-16,2.925800421259684e-17,1.5729291510625545e-18,7.986381291089878e-20],[0.00097880757782981,0.0008945625389024895,0.0004087841952459884,0.00012453350922260142,2.8453757079508727e-05,5.200953844430853e-06,7.92218780819058e-07,1.0343332321426975e-07,9.581219373452719e-09,9.371536125048255e-10,8.564936908260444e-11,7.1161462911478164e-12,5.419721946715469e-13,3.8101935571826686e-14,2.4873241536987365e-15,1.5154950168650448e-16,8.656611247500647e-18,4.653849962448011e-19,2.3629430636800496e-20],[0.0002574233969788106,0.00023526720960297717,0.00010750899211956108,3.2751931746229446e-05,7.483251019017543e-06,1.3678349417071908e-06,2.0835111448668517e-07,2.720264741069895e-08,3.107667671839282e-09,2.5588354166199497e-10,2.252552190821879e-11,1.871524693062757e-12,1.4253702829900774e-13,1.0020692430798516e-14,6.541586390781961e-16,3.9857055072135175e-17,2.2766622614399718e-18,1.2239482953526756e-19,6.214467931160627e-21],[6.0931408922202974e-05,5.568710040558053e-05,2.544708227197422e-05,7.75229202023876e-06,1.771264901553537e-06,3.237627626291438e-07,4.931613483925054e-08,6.438791705029973e-09,7.355763770094923e-10,7.469622406766195e-11,5.535399129955521e-12,4.4298473922474817e-13,3.3738121941407477e-14,2.371870293650375e-15,1.5483754781212163e-16,9.434055138488187e-18,5.388796855981387e-19,2.897051898118873e-20,1.4709474398655127e-21],[1.3111178763423886e-05,1.1982712055231162e-05,5.475685702613588e-06,1.6681328776327926e-06,3.811395661521361e-07,6.966704911075614e-08,1.0611812056144934e-08,1.3854947810723734e-09,1.582808200847106e-10,1.6073082241612362e-11,1.4689687313133246e-12,9.896238627291798e-14,7.259745929735087e-15,5.103774223145016e-16,3.331783729548989e-17,2.0300135114657423e-18,1.1595576099144316e-19,6.2338563960749e-21,3.1651746081075456e-22],[2.5861499124988426e-06,2.363562444864593e-06,1.0800664346206558e-06,3.290353806754069e-07,7.517890446310944e-08,1.3741665506418939e-08,2.0931555671419017e-09,2.732856649650487e-10,3.1220528405443215e-11,3.170378574098359e-12,2.8975071002368187e-13,2.407383104601582e-14,1.4866688944689711e-15,1.006707749071486e-16,6.5718669206734635e-18,4.0041550495019106e-19,2.2872007662524338e-20,1.2296138634166098e-21,6.243234253380948e-23],[4.7087273848920034e-07,4.3034516894198754e-07,1.9665288441407114e-07,5.990905245271033e-08,1.3688184296693646e-08,2.502011054014243e-09,3.811108896744839e-10,4.975843389047625e-11,5.6844715908778534e-12,5.772460575538461e-13,5.275630374273685e-14,4.383238069757055e-15,3.338314108844617e-16,1.90297962429369e-17,1.1965713816389164e-18,7.290557459109279e-20,4.164416312739036e-21,2.2388170320405737e-22,1.1367356531464728e-23],[7.961020003822336e-08,7.275822570420567e-08,3.324799714786819e-08,1.0128791199854251e-08,2.314253939432176e-09,4.2301366001142645e-10,6.443421265176261e-11,8.41263159196544e-12,9.610705472424858e-13,9.759467974422025e-14,8.91947983166768e-15,7.410716973510209e-16,5.644069666217017e-17,3.967915345093109e-18,2.10031606809678e-19,1.2326106191071473e-20,7.04075620863744e-22,3.785155886101896e-23,1.921872840375675e-24],[1.2562343360749098e-08,1.1481114394590965e-08,5.246472889506485e-09,1.5983046496656255e-09,3.651850214816022e-10,6.675077867910494e-11,1.0167600422085682e-11,1.3274978152926848e-12,1.5165516733491904e-13,1.5400261229598594e-14,1.4074775366835838e-15,1.1693975285311221e-16,8.906238279135597e-18,6.261297543218344e-19,4.087424005896744e-20,2.0193366370170996e-21,1.111018399272489e-22,5.972906473334078e-24,3.0326800466404367e-25],[1.8584200419385625e-09,1.6984675933443725e-09,7.761410500695601e-10,2.364464422571769e-10,5.402393036458962e-11,9.874828393868762e-12,1.5041518815562976e-12,1.9638442245400224e-13,2.2435225208010376e-14,2.2782496305266415e-15,2.0821628478359915e-16,1.7299573348758302e-17,1.3175512912615556e-18,9.26269925021679e-20,6.046762514224378e-21,3.684215603682556e-22,1.706378409830988e-23,8.836065676528939e-25,4.486418829366948e-26],[2.5875464964939644e-10,2.364838826201195e-10,1.0806496968240451e-10,3.292130678018412e-11,7.521950290414974e-12,1.3749086340771903e-12,2.0942859221728465e-13,2.7343324588599292e-14,3.123738825184251e-15,3.172090655812441e-16,2.899071824703249e-17,2.4086831501626546e-18,1.8344750652272845e-19,1.2896796446498972e-20,8.419129586275509e-22,5.129668730699337e-23,2.930101883276504e-24,1.2772740616145859e-25,6.2466057520686034e-27],[3.402584042335207e-11,3.109726864282332e-11,1.4210378127504509e-11,4.329101457881285e-12,9.891249513809216e-13,1.8079838118150917e-13,2.7539539361043606e-14,3.5956053363919475e-15,4.107668748521619e-16,4.171250665807392e-17,3.812235081257367e-18,3.1673814792855314e-19,2.412306635440882e-20,1.6959089950871217e-21,1.1071026557176336e-22,6.745435874946867e-24,3.8530391333882745e-25,2.0714186548930385e-26,8.52797013145631e-28]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.07140574681976107, "-10": 4.2601108825844645e-09, "-11": 3.483185898642894e-10, "-12": 2.616958847717067e-11, "-13": 1.8183894498010045e-12, "-14": 1.1750613288787924e-13, "-15": 7.095979779897577e-15, "-16": 4.020490558757919e-16, "-17": 2.1334147325137935e-17, "-18": 9.67003737932421e-19, "-2": 0.025436995139287964, "-3": 0.006659106528248681, "-4": 0.0013816542436151614, "-5": 0.00023631309127852967, "-6": 3.4293224731953456e-05, "-7": 4.315428120113266e-06, "-8": 4.789420324499847e-07, "-9": 4.75151534811046e-08, "0": 0.1543467016335837, "1": 0.23985136656074402, "10": 7.405647900113159e-05, "11": 1.568189815677648e-05, "12": 3.0513968096169016e-06, "13": 5.491215862738413e-07, "14": 9.190136591461545e-08, "15": 1.4373205025233755e-08, "16": 2.1091143026861864e-09, "17": 2.8985191829221977e-10, "18": 3.402584042335207e-11, "2": 0.21845873387018033, "3": 0.1481151172557809, "4": 0.07959075388623982, "5": 0.03525582188319589, "6": 0.013250467660533128, "7": 0.0043184369885386105, "8": 0.0012412677492823782, "9": 0.0003189293400327871} |
| Raw goal margin distribution | {"-1": 0.08580778106699358, "-10": 5.119345125772998e-09, "-11": 4.1857198659488635e-10, "-12": 3.144780943654995e-11, "-13": 2.1851457445981744e-12, "-14": 1.4120628904453686e-13, "-15": 8.527188728187326e-15, "-16": 4.831395076906341e-16, "-17": 2.5637093993950164e-17, "-18": 1.162041554511218e-18, "-2": 0.030567457202340415, "-3": 0.00800220123066647, "-4": 0.001660324135334197, "-5": 0.0002839757708980489, "-6": 4.120992568438932e-05, "-7": 5.18581945898155e-06, "-8": 5.755412539551497e-07, "-9": 5.7098623974378656e-08, "0": 0.17865286427451205, "1": 0.22510841786181413, "10": 6.950444793959268e-05, "11": 1.4717978612175316e-05, "12": 2.863836541483649e-06, "13": 5.153687188543432e-07, "14": 8.62524628357263e-08, "15": 1.348972694726935e-08, "16": 1.9794733320694662e-09, "17": 2.720355846896911e-10, "18": 3.193437341612779e-11, "2": 0.20503072654854776, "3": 0.13901092240982435, "4": 0.07469854744072507, "5": 0.03308875158121814, "6": 0.01243600090240192, "7": 0.004052995536632343, "8": 0.0011649707199524592, "9": 0.00029932570397221816} |
| Research history json | {"away": [{"away": "Fiorentina", "away_goals": 4.0, "away_xg": 2.54, "date": "2026-11-02T00:00:00+00:00", "home": "Sassuolo", "home_goals": 2.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 6.0, "away_xg": 3.57, "date": "2026-10-27T00:00:00+00:00", "home": "Sassuolo", "home_goals": 2.0, "home_xg": 0.76, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 0.0, "away_xg": 0.33, "date": "2026-10-24T00:00:00+00:00", "home": "Como", "home_goals": 2.0, "home_xg": 2.07, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 2.0, "away_xg": 1.92, "date": "2026-10-16T00:00:00+00:00", "home": "Frosinone", "home_goals": 4.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Milan", "away_goals": 1.0, "away_xg": 1.18, "date": "2026-10-11T00:00:00+00:00", "home": "Sassuolo", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 1.0, "away_xg": 1.58, "date": "2026-09-18T00:00:00+00:00", "home": "Monza", "home_goals": 2.0, "home_xg": 1.45, "source": "pipeline training history"}, {"away": "Juventus", "away_goals": 2.0, "away_xg": 1.1, "date": "2026-09-13T00:00:00+00:00", "home": "Sassuolo", "home_goals": 3.0, "home_xg": 1.03, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 2.0, "away_xg": 1.62, "date": "2026-09-06T00:00:00+00:00", "home": "Bologna", "home_goals": 2.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-29T00:00:00+00:00", "home": "Sassuolo", "home_goals": 2.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 1.0, "away_xg": 2.71, "date": "2026-08-23T00:00:00+00:00", "home": "Atalanta", "home_goals": 2.0, "home_xg": 0.89, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.9% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 54.5% |
| P home draw | 89.5% |
| P draw away | 26.0% |
| P home away | 84.6% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6489 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.03, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.39, "draw": 6.38, "home": 1.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.9, "draw": 6.12, "home": 1.35}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.38 |
| Reference away odds | 9.39 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:37Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:37Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.0650 |
| Raw ev home | -0.0618 |
| Raw edge prob draw | 0.0347 |
| Raw ev draw | 0.1398 |
| Raw edge prob away | 0.0303 |
| Raw ev away | 0.1866 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 9.516317310840313, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,639.5286 |
| Elo away rating | 1,399.3804 |
| Elo rating diff | 300.1481 |
| Elo home expectancy | 0.8491 |

</details>


---

## 2026-11-07 — Cagliari vs Frosinone

The model's most likely 1X2 outcome is **Frosinone win** at **42.6%**. Expected goals are 1.38 for Cagliari and 1.93 for Frosinone (3.31 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.3%; Double Chance 1X: 57.4%; Double Chance X2: 67.1%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.9% | 3.04 |
| Draw | 24.5% | 4.08 |
| Frosinone win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.38 |
| Frosinone expected goals | 1.93 |
| Expected total goals | 3.31 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 84.2% |
| Under 1.5 | 15.8% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.7% |
| Under 3.5 | 58.3% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.80% |
| 2 | 2-1 | 8.10% |
| 3 | 1-2 | 7.97% |
| 4 | 2-2 | 7.04% |
| 5 | 1-0 | 5.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.9% | 35.3% | 2.82 | -7.1% |
| Draw | 24.5% | 25.3% | 3.83 | -6.1% |
| Frosinone win | 42.6% | 39.3% | 2.50 | +6.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:00:00+00:00 |
| Fixture id | 52b256088d29b4abb82e0c63ea9852fe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:31Z |
| Market best draw last update utc | 2026-11-05T12:28:31Z |
| Market best away last update utc | 2026-11-05T12:28:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3808 |
| Dc lambda away | 1.9288 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.79 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.32 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.72 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.30 |
| Score matrix json | [[0.04203348224631008,0.05798068169677825,0.0576885520770717,0.037089795499434974,0.017884652335597353,0.0068991653333879575,0.0022178458473899993,0.0006111099736718338,0.00014733822700779378,3.157613606287965e-05,6.090389100093299e-06,1.0679192354363553e-06,1.71649766834718e-07,2.5467476862466465e-08,3.5086814381678505e-09,4.511684635122998e-10,5.4388215181895695e-11],[0.05821389233941523,0.10803819688738864,0.07965782882511799,0.0512145386680087,0.024695585572028743,0.009526544026083009,0.0030624582956400503,0.0008438362885419172,0.00020344839389803196,4.360113663617503e-05,8.409765108429858e-06,1.4746102058826048e-06,2.3701839016732416e-07,3.516614370573371e-08,4.8448771088939885e-09,6.229849587789923e-10,7.510063919224384e-11],[0.04199353626644931,0.08099691964914572,0.07036982452942062,0.0353591727274004,0.017050148230489046,0.006577247876760984,0.0021143603879348796,0.0005825953695222898,0.00014046337403496537,3.0102782559916435e-05,5.806209424113872e-06,1.0180897520797252e-06,1.6364052894870394e-07,2.4279155524724938e-08,3.3449651406002136e-09,4.3011678591569153e-10,5.185044212446433e-11],[0.019328583131509022,0.03728087305868233,0.035953579384509084,0.020824224620326313,0.007847760316886119,0.003027344054948889,0.0009731876417566694,0.0002681541978364074,6.465180700050229e-05,1.385556413985427e-05,2.672454180111494e-06,4.686014600807096e-07,7.531967651879224e-08,1.1175093065391935e-08,1.5396044853632813e-09,1.9797208789656073e-10,2.3865472406259555e-11],[0.0066723505404712325,0.012869595862762961,0.012411405595841803,0.007979685376663766,0.0034663605862308585,0.0010450585334577276,0.0003359505993416332,9.256854445511001e-05,2.231821734925919e-05,4.783029374066322e-06,9.225482784603563e-07,1.617642216277146e-07,2.6000834148521777e-08,3.857713612392593e-09,5.314813170800485e-10,6.83412311542624e-11,8.238513740250299e-12],[0.0018426704712711528,0.0035541334541203343,0.003427597285200792,0.002203710749971192,0.0010626265278829508,0.0003692824005225954,9.277783675450505e-05,2.5564202959866606e-05,6.163513117520802e-06,1.320905869281877e-06,2.547756537564762e-07,4.4673635279434885e-08,7.180523418740528e-09,1.0653659331984924e-09,1.4677660040123433e-10,1.8873464134482014e-11,2.2751901154235134e-12],[0.0004240677560703185,0.0008179397359222531,0.0007888190059534115,0.0005071566985732661,0.00024455031664411263,9.433748194824817e-05,2.7320018588367895e-05,5.8832842626702935e-06,1.4184561037948068e-06,3.039901038735706e-07,5.8633456971460115e-08,1.0281083114869117e-08,1.6525084116071371e-09,2.4518075680324074e-10,3.3778814251494034e-11,4.3434937008906306e-12,5.236067880413984e-13],[8.365194407120826e-05,0.00016134744522203537,0.00015560306678298624,0.0001000421351944397,4.824019067159967e-05,1.8609086993270278e-05,5.9821854264037945e-06,1.4849430273997283e-06,2.798057833060801e-07,5.996533054782888e-08,1.1566082525889725e-08,2.028054662033454e-09,3.259751283755687e-10,4.836455180063321e-11,6.66323586292461e-12,8.568010345976398e-13,1.0328709297407905e-13],[1.4438593104248392e-05,2.784908510898312e-05,2.685758701722754e-05,1.7267592515520344e-05,8.326411204331095e-06,3.2119879354946082e-06,1.032544338389594e-06,2.8450946858675314e-07,6.17951937806183e-08,1.0350207849381685e-08,1.996342837643117e-09,3.500487213225872e-10,5.626434977665892e-11,8.347876332966622e-12,1.150095822046975e-12,1.4788659901703685e-13,1.7827682607159997e-14],[2.215242089852025e-06,4.272747701376693e-06,4.120627041904776e-06,2.649281509258634e-06,1.2774801827348747e-06,4.927994587444232e-07,1.5841818254203857e-07,4.3650883796244816e-08,1.0524200394274097e-08,2.031863648547855e-09,3.062890302255575e-10,5.37062479269197e-11,8.632361538517045e-12,1.280773471497442e-12,1.764535265982238e-13,2.268951111110786e-14,2.7352133681420428e-15],[3.058862960607455e-07,5.899919355827538e-07,5.689867256811621e-07,3.6581956969925455e-07,1.7639773240940792e-07,6.804701022367312e-08,2.1874788001024375e-08,6.02742572713723e-09,1.4532085194447432e-09,3.114379130902384e-10,5.411522164275338e-11,7.415896135660245e-12,1.1919785694621756e-12,1.7685247814851017e-13,2.4365154456591398e-14,3.1330257514516274e-15,3.7768526065369836e-16],[3.839778404782198e-08,7.406145101696277e-08,7.142467544359639e-08,4.5921183847313084e-08,2.2143136592941177e-08,8.541913898456084e-09,2.7459333633842105e-09,7.56620333814956e-10,1.8242068253692908e-10,3.909467630667736e-11,7.540561326937397e-12,1.1911294219098708e-12,1.496285916998097e-13,2.220022064316371e-14,3.058548065619228e-15,3.932874658648137e-16,4.741067927327506e-17],[4.418386893669499e-09,8.52216221883917e-09,8.218751620446298e-09,5.284095472802798e-09,2.547984133280585e-09,9.829077732399114e-10,3.159712541889456e-10,8.70633930918591e-11,2.0990928847653917e-11,4.498577448910694e-12,8.676833354851139e-13,1.5214392857394525e-13,2.203034716904849e-14,2.5545527263802987e-15,3.51943452516936e-16,4.525511634883393e-17,5.455489922546425e-18],[4.693093599320578e-10,9.052015118664589e-10,8.729740412634708e-10,5.612626335901095e-10,2.7064012986735913e-10,1.0440186181802757e-10,3.356163021233056e-11,9.247643148678484e-12,2.2296008971025877e-12,4.778269884373303e-13,9.21630270503631e-14,1.616032535287707e-14,2.59749612774893e-15,3.4718385211402195e-16,3.738250189671071e-17,4.806878663738572e-18,5.794676983435686e-19],[4.6288169481365975e-11,8.928038640041031e-11,8.610177811217415e-11,5.535755756275117e-11,2.669334402700347e-11,1.02971973000978e-11,3.310196982996869e-12,9.120987346836477e-13,2.1990642636198673e-13,4.7128266580406254e-14,9.090076142185881e-15,1.5938993394810672e-15,2.5619207979538393e-16,3.80109218022919e-17,4.717678345962021e-18,4.741043611312263e-19,5.715313036541028e-20],[4.261059255163365e-12,8.218709468067806e-12,7.926102557557331e-12,5.095942130331109e-12,2.4572568302427997e-12,9.479089009015208e-13,3.047203129622748e-13,8.396328475705062e-14,2.0243494694618725e-14,4.338394426530263e-15,8.36787315415304e-16,1.467264661444147e-16,2.3583771943090832e-17,3.499096895766186e-18,4.820743097098684e-19,5.58432505521959e-20,5.261233655029884e-21],[3.677362281384868e-13,7.092877707088941e-13,6.840353263858095e-13,4.3978795543600603e-13,2.1206519417115618e-13,8.180605407306397e-14,2.6297850326803314e-14,7.246165751218056e-15,1.7470459661690743e-15,3.744103771042505e-16,7.221608353652349e-17,1.2662728677770474e-17,2.035317234587012e-18,3.0197765796871383e-19,4.160378387612333e-20,5.349677814435546e-21,5.809725399457419e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18198945369050598, "-10": 7.740365806378e-06, "-11": 1.3308270020350372e-06, "-12": 2.1036708628268874e-07, "-13": 3.07663362296824e-08, "-14": 4.183516839071307e-09, "-15": 5.262691027045436e-10, "-16": 5.4388215181895695e-11, "-2": 0.12934357830551782, "-3": 0.06943486456260144, "-4": 0.029817410789751714, "-5": 0.010613919226164375, "-6": 0.0032169699980666017, "-7": 0.0008475028010495547, "-8": 0.00019724127538168807, "-9": 4.108331953690162e-05, "0": 0.24513024011420104, "1": 0.18430731829779365, "10": 3.887554288825229e-07, "11": 4.7850816928371685e-08, "12": 5.414998190972633e-09, "13": 5.669556368454615e-10, "14": 5.519091427581959e-11, "15": 4.970347025872259e-12, "16": 3.677362281384868e-13, "2": 0.09415376276299149, "3": 0.03618454978927444, "4": 0.011124186999288825, "5": 0.0028348292289592063, "6": 0.0006151073349083624, "7": 0.00011601063633050844, "8": 1.932890449705597e-05, "9": 2.8822240456448246e-06} |
| Raw goal margin distribution | {"-1": 0.21436247878614895, "-10": 9.117253595301587e-06, "-11": 1.567559928373214e-06, "-12": 2.4778804021943903e-07, "-13": 3.623917740078845e-08, "-14": 4.927697849964498e-09, "-15": 6.198839936964631e-10, "-16": 6.406301237088573e-11, "-2": 0.15235174071016835, "-3": 0.08178622101438979, "-4": 0.0351214532395153, "-5": 0.012501966398700461, "-6": 0.003789217721038769, "-7": 0.0009982600503880984, "-8": 0.0002323273566261922, "-9": 4.839138771013894e-05, "0": 0.22565775708110103, "1": 0.1528473321814137, "10": 3.2239756253046325e-07, "11": 3.9683013011916827e-08, "12": 4.4906954042923444e-09, "13": 4.701802259258446e-10, "14": 4.5770206444445394e-11, "15": 4.121943121612297e-12, "16": 3.049661941616796e-13, "2": 0.07808236583374593, "3": 0.030008097087821074, "4": 0.009225365119692141, "5": 0.0023509434613779826, "6": 0.0005101127617409862, "7": 9.620842206133208e-05, "8": 1.6029594015311015e-05, "9": 2.3902483102387275e-06} |
| Research history json | {"away": [{"away": "Torino", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Frosinone", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 1.0, "away_xg": 1.45, "date": "2026-10-29T00:00:00+00:00", "home": "Frosinone", "home_goals": 5.0, "home_xg": 3.08, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 4.0, "away_xg": 1.95, "date": "2026-10-25T00:00:00+00:00", "home": "Atalanta", "home_goals": 4.0, "home_xg": 3.88, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 2.0, "away_xg": 1.92, "date": "2026-10-16T00:00:00+00:00", "home": "Frosinone", "home_goals": 4.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 0.0, "away_xg": 1.01, "date": "2026-10-10T00:00:00+00:00", "home": "Napoli", "home_goals": 3.0, "home_xg": 3.12, "source": "pipeline training history"}, {"away": "Como", "away_goals": 0.0, "away_xg": 2.12, "date": "2026-09-20T00:00:00+00:00", "home": "Frosinone", "home_goals": 2.0, "home_xg": 2.18, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 1.0, "away_xg": 1.93, "date": "2026-09-12T00:00:00+00:00", "home": "Genoa", "home_goals": 1.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-06T00:00:00+00:00", "home": "Frosinone", "home_goals": 3.0, "home_xg": 1.9, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 3.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "Fiorentina", "home_goals": 0.0, "home_xg": 1.9, "source": "pipeline training history"}, {"away": "Juventus", "away_goals": 1.0, "away_xg": 2.18, "date": "2026-08-23T00:00:00+00:00", "home": "Frosinone", "home_goals": 0.0, "home_xg": 0.41, "source": "pipeline training history"}], "h2h": [{"away": "Cagliari", "away_goals": 1.0, "away_xg": null, "date": "2024-01-21T00:00:00+00:00", "home": "Frosinone", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 3.0, "away_xg": null, "date": "2023-10-29T00:00:00+00:00", "home": "Cagliari", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Cagliari", "away_goals": 1.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": 1.02, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 2.0, "away_xg": 2.61, "date": "2026-10-27T00:00:00+00:00", "home": "Roma", "home_goals": 4.0, "home_xg": 2.87, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 2.0, "away_xg": 1.66, "date": "2026-10-24T00:00:00+00:00", "home": "Cagliari", "home_goals": 0.0, "home_xg": 0.52, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 0.0, "away_xg": 2.37, "date": "2026-10-19T00:00:00+00:00", "home": "Monza", "home_goals": 4.0, "home_xg": 2.06, "source": "pipeline training history"}, {"away": "Juventus", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-10-11T00:00:00+00:00", "home": "Cagliari", "home_goals": 1.0, "home_xg": 0.52, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 1.0, "away_xg": 1.12, "date": "2026-09-19T00:00:00+00:00", "home": "Udinese", "home_goals": 0.0, "home_xg": 2.13, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 2.0, "away_xg": 1.32, "date": "2026-09-12T00:00:00+00:00", "home": "Atalanta", "home_goals": 1.0, "home_xg": 1.31, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 0.0, "away_xg": 0.41, "date": "2026-09-07T00:00:00+00:00", "home": "Cagliari", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Inter", "away_goals": 1.0, "away_xg": 3.91, "date": "2026-08-30T00:00:00+00:00", "home": "Cagliari", "home_goals": 0.0, "home_xg": 0.45, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 1.0, "away_xg": 0.94, "date": "2026-08-22T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 0.75, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 27.3% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 50.1% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 57.8% |
| Raw p btts yes | 64.2% |
| P home draw | 57.4% |
| P draw away | 67.1% |
| P home away | 75.5% |
| Raw p home draw | 49.9% |
| Raw p draw away | 72.7% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6341 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.48, "draw": 3.8, "home": 2.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.5, "draw": 3.83, "home": 2.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.75 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:37Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:37Z |
| Home probability edge | -2.4% |
| Draw probability edge | -0.8% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +0.9% |
| Under 2.5 probability edge | -0.9% |
| Raw edge prob home | -0.0803 |
| Raw ev home | -0.2297 |
| Raw edge prob draw | -0.0278 |
| Raw ev draw | -0.1357 |
| Raw edge prob away | 0.1081 |
| Raw ev away | 0.2530 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 10.415320416673183, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,408.9297 |
| Elo away rating | 1,456.3373 |
| Elo rating diff | 12.5924 |
| Elo home expectancy | 0.5181 |

</details>


---

## 2026-11-07 — Parma vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **50.8%**. Expected goals are 0.87 for Parma and 1.31 for Bologna (2.17 combined). The most likely exact score is 0-1 at 15.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 37.6%; Under 3.5 goals: 82.3%; Double Chance 1X: 49.2%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 92.9%; BTTS Yes (both teams score): 42.0%; BTTS No (at least one team does not score): 58.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 21.8% | 4.59 |
| Draw | 27.4% | 3.65 |
| Bologna win | 50.8% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 0.87 |
| Bologna expected goals | 1.31 |
| Expected total goals | 2.17 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 64.5% |
| Under 1.5 | 35.5% |
| Over 2.5 | 37.6% |
| Under 2.5 | 62.4% |
| Over 3.5 | 17.7% |
| Under 3.5 | 82.3% |
| Over 4.5 | 7.1% |
| Under 4.5 | 92.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.95% |
| 2 | 1-1 | 12.44% |
| 3 | 0-0 | 11.04% |
| 4 | 0-2 | 10.61% |
| 5 | 1-2 | 9.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 21.8% | 20.7% | 4.63 | +0.9% |
| Draw | 27.4% | 26.7% | 3.69 | +1.0% |
| Bologna win | 50.8% | 52.7% | 1.89 | -4.0% |
| Over 2.5 | 37.6% | 44.9% | 2.19 | -17.6% |
| Under 2.5 | 62.4% | 55.1% | 1.79 | +11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:00:00+00:00 |
| Fixture id | 813cc4970b2dcab8457490a332fb5a6c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:31Z |
| Market best draw last update utc | 2026-11-05T12:28:31Z |
| Market best away last update utc | 2026-11-05T12:28:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8658 |
| Dc lambda away | 1.3051 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.0% |
| P btts no | 58.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.06 |
| Fair Over 1.5 odds | 1.55 |
| Fair Under 1.5 odds | 2.81 |
| Fair Over 2.5 odds | 2.66 |
| Fair Under 2.5 odds | 1.60 |
| Fair Over 3.5 odds | 5.64 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 14.05 |
| Fair Under 4.5 odds | 1.08 |
| Score matrix json | [[0.1104022206129277,0.1594968849147786,0.10612567637508045,0.04616901095788374,0.015064056449182555,0.00393208850691932,0.0008553096835948864,0.00015946915892454684,2.601585308091633e-05,3.7726534771421232e-06,4.923775819648074e-07,5.841937962001069e-08,6.353705036226216e-09,6.378742220335979e-10,5.946458203291357e-11],[0.08540981803349078,0.12440329397581111,0.09188618022371482,0.03997424757636608,0.013042824819299085,0.00340449743684484,0.0007405478336469981,0.00013807225901936234,2.252515551861379e-05,3.2664547276676214e-06,4.263124323903836e-07,5.05809133818851e-08,5.5011916624551544e-09,5.522869462682058e-10,5.148587493843456e-11],[0.03808060592340514,0.049699864506306514,0.034379315142681485,0.01730533572350381,0.005646396767059227,0.0014738481569129265,0.00032059212261825287,5.977315249944358e-05,9.751412524502658e-06,1.4140877968978917e-06,1.8455581312757178e-07,2.1897089760171048e-08,2.3815324707802995e-09,2.390917052940525e-10,2.228885857390632e-11],[0.010990370217726413,0.014343782023684418,0.009360198003663556,0.00431654023154683,0.0016295956789913763,0.0004253644735004355,9.252547408379783e-05,1.7251014239921567e-05,2.8143363581352155e-06,4.0811715127476226e-07,5.326429721694339e-08,6.319676836002049e-09,6.873294923945829e-10,6.90037958548903e-11,6.43274447760866e-12],[0.002378932161012082,0.0031047984454293355,0.0020260715174490974,0.0008814239992210615,0.00030485750559438977,9.207271512383073e-05,2.002769894464677e-05,3.7340864568178844e-06,6.091801405811518e-07,8.833942782584556e-08,1.152937955435918e-08,1.3679323056942908e-09,1.487766292014719e-10,1.493628930955792e-11,1.3924064811459882e-12],[0.0004119474132050394,0.0005376419340909262,0.00035084435540460354,0.0001526316480842737,4.980075845182576e-05,1.3779642952085896e-05,3.4680933352830614e-06,6.466124935297328e-07,1.0548858315553001e-07,1.5297283114365163e-08,1.9964831957447363e-09,2.368777823957066e-10,2.5762881577437462e-11,2.5864401872379487e-12,2.4111584913543406e-13],[5.9445674137441e-05,7.758390074095446e-05,5.0628256315720124e-05,2.20253627628977e-05,7.186450415337698e-06,1.8758399624311241e-06,4.3253030879304257e-07,9.330879221818222e-08,1.5222428248051137e-08,2.207459685520865e-09,2.881005819450223e-10,3.41824199189378e-11,3.71768777761825e-12,3.7323375658630825e-13,3.4793990052179946e-14],[7.352786289245439e-06,9.596288542633826e-06,6.262167168395671e-06,2.7242989113768122e-06,8.888861107045032e-07,2.3202109416226044e-07,5.0469334117492225e-08,9.97473913749018e-09,1.882849565344522e-09,2.7303886355520393e-10,3.563492280281477e-11,4.2279952605482466e-12,4.598377277338339e-13,4.6164974793059226e-14,4.30363986473287e-15],[7.957775502558639e-07,1.0385873718613462e-06,6.77741995010439e-07,2.9484549510586073e-07,9.620238965295466e-08,2.5111185155780812e-08,5.462196436445621e-09,1.0184052493590262e-09,1.7611755765567708e-10,2.9550457393601587e-11,3.85669737376399e-12,4.575875836148861e-13,4.9767329838823013e-14,4.9963441208916766e-15,4.65774449850365e-16],[7.655594123912422e-08,9.991489931620846e-08,6.52006032698755e-08,2.836492986097334e-08,9.254928700824654e-09,2.4157635693701304e-09,5.254779922990209e-10,9.797332483490822e-11,1.598340169311272e-11,2.456963567732619e-12,3.71024663146163e-13,4.402115660552455e-14,4.787751021053604e-15,4.806617462460998e-16,4.480875516275246e-17],[6.6283987571795865e-09,8.650873906476393e-09,5.645226101152512e-09,2.4559043072920445e-09,8.013141358515625e-10,2.0916265911794928e-10,4.54971569117096e-11,8.48276768675631e-12,1.383881619157563e-12,2.0068170688961934e-13,2.7763856956406732e-14,3.811458327215322e-15,4.145350759715909e-16,4.161685781499072e-17,3.879650517310399e-18],[5.217298306553031e-10,6.809214628733032e-10,4.443430405533459e-10,1.933074012726287e-10,6.307247100164305e-11,1.64634631558368e-11,3.5811400068731384e-12,6.676896051110248e-13,1.0892711034139436e-13,1.5795916447804248e-14,2.0615609656733367e-15,2.5928387542362934e-16,3.262859144572157e-17,3.27571665128062e-18,3.0537230506925476e-19],[3.764386000098573e-11,4.912985747407635e-11,3.2060246948105885e-11,1.3947519047399213e-11,4.550806047106652e-12,1.1878720858097974e-12,2.583864773331823e-13,4.8175152237976393e-14,7.859310798566268e-15,1.139707243884363e-15,1.4874578338338532e-16,1.7648318495075095e-17,2.034670547923433e-18,2.3634956595988555e-19,2.2033227975036218e-20],[2.507151189125476e-12,3.272140013921799e-12,2.135272160121074e-12,9.289307463188284e-13,3.0309215877925594e-13,7.911449336994154e-14,1.720902064461156e-14,3.2085548670242786e-15,5.2344473743702525e-16,7.590662518893589e-17,9.906746217770697e-18,1.175410882407756e-18,1.2783795534574855e-19,1.3604684524982972e-20,1.4674540208267228e-21],[1.5505372893783368e-13,2.0236414659230906e-13,1.3205502410861823e-13,5.7449338024158e-14,1.8744609273816556e-14,4.8928031397722886e-15,1.064284768261593e-15,1.9843174946592784e-16,3.237222341617393e-17,4.6944138581193344e-18,6.12678624794833e-19,7.269280015578304e-20,7.906085505382163e-21,7.937239944761575e-22,7.843564741348845e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.27041363257101486, "-10": 5.454104240198088e-07, "-11": 6.41660957322375e-08, "-12": 6.928280841068327e-09, "-13": 6.893600969720324e-10, "-14": 5.946458203291357e-11, "-2": 0.1521923750028126, "-3": 0.06078205122677654, "-4": 0.018807021792688096, "-5": 0.0047353141999822174, "-6": 0.0010035532423116815, "-7": 0.00018346306061000012, "-8": 2.94733346964109e-05, "-9": 4.2215655061902304e-06, "0": 0.2738204497951641, "1": 0.1454030326450217, "10": 7.342328142356588e-09, "11": 5.730524096275246e-10, "12": 4.104805503901615e-11, "13": 2.709515335717785e-12, "14": 1.5505372893783368e-13, "2": 0.05461051514570201, "3": 0.014468952912689945, "4": 0.0029700253146561096, "5": 0.0004960977943306986, "6": 6.974888764417265e-05, "7": 8.459094446434492e-06, "8": 9.015356140593228e-07, "9": 8.566541369016326e-08} |
| Raw goal margin distribution | {"-1": 0.24754294035533772, "-10": 4.992814111428298e-07, "-11": 5.873913921299366e-08, "-12": 6.342309722699384e-09, "-13": 6.310562960367144e-10, "-14": 5.443526401932751e-11, "-2": 0.13932044642003996, "-3": 0.05564130601867372, "-4": 0.01721638598477947, "-5": 0.0043348169595781956, "-6": 0.0009186760225179355, "-7": 0.000167946360685282, "-8": 2.6980577360168886e-05, "-9": 3.864519434058345e-06, "0": 0.29002841594581663, "1": 0.16325586523990343, "10": 8.243831727238449e-09, "11": 6.43412762854477e-10, "12": 4.608800531808716e-11, "13": 3.0421942545951394e-12, "14": 1.740914905001892e-13, "2": 0.06131568743187203, "3": 0.016245475654166102, "4": 0.003334690093516429, "5": 0.0005570095285068242, "6": 7.831277515146162e-05, "7": 9.497716504787136e-06, "8": 1.0122276959460763e-06, "9": 9.618355943967794e-08} |
| Research history json | {"away": [{"away": "Monza", "away_goals": 1.0, "away_xg": 1.79, "date": "2026-10-31T00:00:00+00:00", "home": "Bologna", "home_goals": 2.0, "home_xg": 2.03, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 4.0, "away_xg": 2.09, "date": "2026-10-28T00:00:00+00:00", "home": "Milan", "home_goals": 2.0, "home_xg": 1.8, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 2.0, "away_xg": 1.66, "date": "2026-10-24T00:00:00+00:00", "home": "Cagliari", "home_goals": 0.0, "home_xg": 0.52, "source": "pipeline training history"}, {"away": "Inter", "away_goals": 3.0, "away_xg": 3.16, "date": "2026-10-17T00:00:00+00:00", "home": "Bologna", "home_goals": 1.0, "home_xg": 1.0, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-10-11T00:00:00+00:00", "home": "Lecce", "home_goals": 1.0, "home_xg": 1.49, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-09-19T00:00:00+00:00", "home": "Bologna", "home_goals": 1.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-09-13T00:00:00+00:00", "home": "Napoli", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Sassuolo", "away_goals": 2.0, "away_xg": 1.62, "date": "2026-09-06T00:00:00+00:00", "home": "Bologna", "home_goals": 2.0, "home_xg": 1.88, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 0.0, "away_xg": 1.35, "date": "2026-08-31T00:00:00+00:00", "home": "Atalanta", "home_goals": 1.0, "home_xg": 0.16, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 1.0, "away_xg": 0.63, "date": "2026-08-24T00:00:00+00:00", "home": "Bologna", "home_goals": 0.0, "home_xg": 1.78, "source": "pipeline training history"}], "h2h": [{"away": "Parma", "away_goals": 1.0, "away_xg": null, "date": "2026-02-08T00:00:00+00:00", "home": "Bologna", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 3.0, "away_xg": null, "date": "2025-11-02T00:00:00+00:00", "home": "Parma", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 0.0, "away_xg": null, "date": "2025-02-22T00:00:00+00:00", "home": "Parma", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 0.0, "away_xg": null, "date": "2024-10-06T00:00:00+00:00", "home": "Bologna", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Parma", "away_goals": 3.0, "away_xg": 0.36, "date": "2026-11-02T00:00:00+00:00", "home": "Atalanta", "home_goals": 0.0, "home_xg": 2.8, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 0.0, "away_xg": 1.37, "date": "2026-10-28T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 1.12, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 1.0, "away_xg": 0.81, "date": "2026-10-24T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 3.0, "away_xg": 1.35, "date": "2026-10-19T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 0.0, "away_xg": 0.46, "date": "2026-10-10T00:00:00+00:00", "home": "Inter", "home_goals": 3.0, "home_xg": 2.42, "source": "pipeline training history"}, {"away": "Genoa", "away_goals": 1.0, "away_xg": 0.7, "date": "2026-09-20T00:00:00+00:00", "home": "Parma", "home_goals": 2.0, "home_xg": 0.53, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 1.0, "away_xg": 1.22, "date": "2026-09-14T00:00:00+00:00", "home": "Como", "home_goals": 2.0, "home_xg": 3.24, "source": "pipeline training history"}, {"away": "Monza", "away_goals": 1.0, "away_xg": 1.72, "date": "2026-09-06T00:00:00+00:00", "home": "Parma", "home_goals": 1.0, "home_xg": 0.73, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 0.0, "away_xg": 0.22, "date": "2026-08-29T00:00:00+00:00", "home": "Juventus", "home_goals": 2.0, "home_xg": 1.69, "source": "pipeline training history"}, {"away": "Cagliari", "away_goals": 1.0, "away_xg": 0.94, "date": "2026-08-22T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 0.75, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 24.5% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 46.5% |
| Raw p over 1 5 | 64.1% |
| Raw p under 3 5 | 82.5% |
| Raw p btts yes | 42.5% |
| P home draw | 49.2% |
| P draw away | 78.2% |
| P home away | 72.6% |
| Raw p home draw | 53.5% |
| Raw p draw away | 75.5% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3761 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.3, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.4, "price": 1.3, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.86, "draw": 3.59, "home": 4.6}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.89, "draw": 3.69, "home": 4.63}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.19, "under": 1.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.60 |
| Reference draw odds | 3.59 |
| Reference away odds | 1.86 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best under 2 5 last update utc | 2026-11-05T12:28:31Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0382 |
| Raw ev home | 0.1334 |
| Raw edge prob draw | 0.0232 |
| Raw ev draw | 0.0702 |
| Raw edge prob away | -0.0614 |
| Raw ev away | -0.1208 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 8.405658243943016, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,382.0338 |
| Elo away rating | 1,530.3171 |
| Elo rating diff | -88.2833 |
| Elo home expectancy | 0.3756 |

</details>


---

## 2026-11-07 — Torino vs Lecce

The model's most likely 1X2 outcome is **Torino win** at **52.4%**. Expected goals are 1.34 for Torino and 0.81 for Lecce (2.14 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.1%; Double Chance 1X: 78.8%; Double Chance X2: 47.6%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 52.4% | 1.91 |
| Draw | 26.4% | 3.79 |
| Lecce win | 21.2% | 4.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.34 |
| Lecce expected goals | 0.81 |
| Expected total goals | 2.14 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.56% |
| 2 | 1-0 | 10.87% |
| 3 | 2-1 | 9.62% |
| 4 | 2-0 | 9.41% |
| 5 | 0-0 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 52.4% | 53.9% | 1.87 | -2.0% |
| Draw | 26.4% | 25.4% | 3.85 | +1.6% |
| Lecce win | 21.2% | 20.7% | 4.59 | -2.6% |
| Over 2.5 | 50.4% | 50.4% | 2.01 | +1.3% |
| Under 2.5 | 49.6% | 49.6% | 1.96 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:00:00+00:00 |
| Fixture id | 0d53a5dbd9d4f4716e923b97e92dfb0d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:28:31Z |
| Market best draw last update utc | 2026-11-05T12:28:31Z |
| Market best away last update utc | 2026-11-05T12:29:20Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3361 |
| Dc lambda away | 0.8068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.56 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.29 |
| Fair Under 4.5 odds | 1.16 |
| Score matrix json | [[0.07377026965999221,0.06127620269696131,0.032530457772570805,0.011079801287385936,0.0028303166856632023,0.0005783997263751289,9.850082771227433e-05,1.437821228504106e-05,1.8364451259017333e-06,2.0849636989878015e-07,2.1304019424844707e-08,1.978936759402571e-09,1.6850536048229172e-10,1.3244434514423416e-11,9.666481768049845e-13,6.584764216164146e-14],[0.10871642705438384,0.12556329616770703,0.055048475605668314,0.01874938788591526,0.004789499739484727,0.0009787757507222525,0.00016668441770374624,2.4331003079015475e-05,3.1076569970555587e-06,3.5282034493596874e-07,3.605094652556953e-08,3.3487832445133055e-09,2.8514702408384595e-10,2.2412409175897403e-11,1.6357749697878807e-12,1.1142826051105506e-13],[0.09412531526559453,0.09617661668456669,0.053096407942837064,0.015863982438779133,0.004052427749644046,0.000828148706263895,0.00014103280018313378,2.0586624369392867e-05,2.6294093613622994e-06,2.9852365262083207e-07,3.0502946872875063e-08,2.8334278913790554e-09,2.4126480341976466e-10,1.8963289241259004e-11,1.384040137865154e-12,9.428019616891041e-14],[0.05309337234558117,0.05425045224192141,0.027716374364925273,0.010200954387926014,0.0022858574742438383,0.00046713477128986885,7.955253007051665e-05,1.161232034016164e-05,1.4831738929940626e-06,1.6838857216932212e-07,1.7205831517156268e-08,1.5982548544656169e-09,1.3609050876168768e-10,1.0696643870377988e-11,7.806970757394568e-13,5.318073619074617e-14],[0.02246132864792309,0.022950835165882408,0.011725504823602904,0.003993680763673388,0.001102399472612612,0.00019762292650237712,3.365496376943504e-05,4.912630936826163e-06,6.274616732898452e-07,7.123734833476715e-08,7.278984537884691e-09,6.761470587256545e-10,5.757354464626942e-11,4.525250945419524e-12,3.302765075557661e-13,2.2498288214654405e-14],[0.007601872133435882,0.007767542028406866,0.00396841120871347,0.001351631997513864,0.0003452721304483193,7.624601705299223e-05,1.1390275937853707e-05,1.6626439515619202e-06,2.1235980665917447e-07,2.41097586725354e-08,2.4635189923803913e-09,2.2883701869998066e-10,1.9485344412609867e-11,1.5315380313430356e-12,1.1177966443890041e-13,7.614380828037288e-15],[0.0021439982780675957,0.002190723079973056,0.0011192330847980562,0.0003812082897980819,9.737901929315192e-05,1.9900245933306078e-05,3.6621222242376205e-06,4.689247209919973e-07,5.989301737995062e-08,6.799809332648934e-09,6.947999630800324e-10,6.454017713517214e-11,5.495560058744043e-12,4.319481891246152e-13,3.152584046052049e-14,2.1475261747771877e-15],[0.000518300364775222,0.0005295958411379537,0.00027056874161399884,9.215510930156406e-05,2.3540868356752835e-05,4.810780321915903e-06,8.192705183669225e-07,1.2922749582504013e-07,1.4478823548074889e-08,1.6438183246538906e-09,1.67964255379331e-10,1.560225010160317e-11,1.328522887461655e-12,1.0442121445595033e-13,7.621206965362155e-15,5.19153215344262e-16],[0.00010963435092971254,0.00011202364544623687,5.7232505289832216e-05,1.9493263520112217e-05,4.979521524615736e-06,1.0176083481774502e-06,1.7329756570007464e-07,2.5296327411531257e-08,3.4913479128283964e-09,3.47711418547727e-10,3.552891984919122e-11,3.300292029842846e-12,2.8101802422094134e-13,2.2087871914069162e-14,1.6120885411895204e-15,1.0981475157175586e-16],[2.061385717311212e-05,2.1063101187332705e-05,1.0761067856007587e-05,3.6651956857850814e-06,9.36268100539713e-07,1.9133449479666205e-07,3.258405086996504e-08,4.756309275729604e-09,6.074956200071081e-10,7.452916976038098e-11,6.680279247110384e-12,6.205331445466066e-13,5.2838050895877513e-14,4.153043576520312e-15,3.0311086494958444e-16,2.0647776770733518e-17],[3.488304473506695e-06,3.5643261462747505e-06,1.8210022911570015e-06,6.202293146611197e-07,1.5843653985214953e-07,3.237787904176965e-08,5.513916656166914e-09,8.048690152733855e-10,1.0280122109658472e-10,1.167128879458101e-11,1.288678126593277e-12,1.050074484315595e-13,8.941325622061515e-15,7.027835870300105e-16,5.1292825854603976e-17,3.494044393169891e-18],[5.366323156355673e-07,5.483273057391694e-07,2.8013858414684054e-07,9.541457630189827e-08,2.4373493743989455e-08,4.980934530662266e-09,8.482475901668729e-10,1.2381910086400224e-10,1.5814690989908605e-11,1.7954828140306363e-12,1.8346123131857608e-13,1.8415234796122463e-14,1.3755118883286583e-15,1.0811452571382341e-16,7.890764158604977e-18,5.375153309812224e-19],[7.56746983165887e-08,7.73238998687863e-08,3.950452148421339e-08,1.3455151816751158e-08,3.4370960008495906e-09,7.02400334381882e-10,1.1961799282927302e-10,1.7460694838359093e-11,2.2301526292057066e-12,2.531950021002102e-13,2.587129572392633e-14,2.403192425826732e-15,2.2112250324027868e-16,1.5246070500515336e-17,1.1127380513463161e-18,7.579921918114419e-20],[9.85059510257483e-09,1.0065272096267915e-08,5.1423138052557035e-09,1.7514606009527405e-09,4.474076776811755e-10,9.143163366126507e-11,1.557070514393541e-11,2.272863174726259e-12,2.9029954602980456e-13,3.295845907770228e-14,3.3676732728977196e-15,3.1282418122576625e-16,2.6636804422663357e-17,2.262374053508862e-18,1.4484540068047931e-19,9.866804015802697e-21],[1.190664910309353e-09,1.2166134302494576e-09,6.215637270601965e-10,2.1170321768668175e-10,5.4079232459643786e-11,1.105155950063077e-11,1.882068245685099e-12,2.7472638961411574e-13,3.5089198097897094e-14,3.983767509785206e-15,4.070586958119781e-16,3.7811804444628413e-17,3.21965404308905e-18,2.5306314891550777e-19,1.995843636918456e-20,1.1926241202874007e-21],[1.3432393876927592e-10,1.372513009291991e-10,7.012122998833024e-11,2.3883134376082524e-11,6.100906683905966e-12,1.24677311711659e-12,2.1232407002514304e-13,3.099304465707562e-14,3.958560679797248e-15,4.494256431193453e-16,4.592201118746612e-17,4.265709404047602e-18,3.6322277476857953e-19,2.854912295253167e-20,2.0836644721518698e-21,1.5337768180142345e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.13468401517613546, "-10": 2.4905102007536538e-08, "-11": 2.2838502680916305e-09, "-12": 1.92354990532245e-10, "-13": 1.4974489680380208e-11, "-14": 1.0780764373160395e-12, "-15": 6.584764216164146e-14, "-2": 0.05583478736013518, "-3": 0.01678213422507599, "-4": 0.003962389839028148, "-5": 0.0007672277090996838, "-6": 0.00012563714214799206, "-7": 1.780229483831696e-05, "-8": 2.2214258096927137e-06, "-9": 2.4752147400262647e-07, "0": 0.2638133685650324, "1": 0.23696911643012936, "10": 4.077943087336606e-06, "11": 6.193163334339799e-07, "12": 8.63854172742929e-08, "13": 1.1137329762812618e-08, "14": 1.327916211238552e-09, "15": 1.3432393876927592e-10, "2": 0.16155527228674563, "3": 0.08041841889167124, "4": 0.031445435366448275, "5": 0.010083626730525241, "6": 0.002734655359581944, "7": 0.0006417303991355961, "8": 0.00013261739942519994, "9": 2.4472235726911714e-05} |
| Raw goal margin distribution | {"-1": 0.15287928830364286, "-10": 4.164254725904878e-09, "-11": 3.0296505793831954e-10, "-12": 2.022853908443787e-11, "-13": 1.2448522157256806e-12, "-14": 6.66088341091079e-14, "-2": 0.05388553172245738, "-3": 0.013351319449836276, "-4": 0.002559617453146761, "-5": 0.0003990256496740912, "-6": 5.233627957486963e-05, "-7": 5.919714795463657e-06, "-8": 5.882863664876459e-07, "-9": 5.2117285254410466e-08, "0": 0.28784704869898825, "1": 0.25503247375769694, "10": 6.463354778125685e-07, "11": 7.787630215035516e-08, "12": 8.611312871343213e-09, "13": 8.776365814002476e-10, "14": 7.777156229600703e-11, "2": 0.14779383356674045, "3": 0.06064575394730539, "4": 0.019254992155278004, "5": 0.004971199215542723, "6": 0.0010798297081481127, "7": 0.00020227642951558213, "8": 3.329088573879147e-05, "9": 4.8843910054139845e-06} |
| Research history json | {"away": [{"away": "Genoa", "away_goals": 2.0, "away_xg": 1.34, "date": "2026-11-01T00:00:00+00:00", "home": "Lecce", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 1.0, "away_xg": 1.45, "date": "2026-10-29T00:00:00+00:00", "home": "Frosinone", "home_goals": 5.0, "home_xg": 3.08, "source": "pipeline training history"}, {"away": "Juventus", "away_goals": 2.0, "away_xg": 1.06, "date": "2026-10-25T00:00:00+00:00", "home": "Lecce", "home_goals": 0.0, "home_xg": 0.86, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 3.0, "away_xg": 3.47, "date": "2026-10-18T00:00:00+00:00", "home": "Udinese", "home_goals": 0.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-10-11T00:00:00+00:00", "home": "Lecce", "home_goals": 1.0, "home_xg": 1.49, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 0.0, "away_xg": 0.21, "date": "2026-09-20T00:00:00+00:00", "home": "Milan", "home_goals": 3.0, "home_xg": 2.19, "source": "pipeline training history"}, {"away": "Monza", "away_goals": 2.0, "away_xg": 2.47, "date": "2026-09-13T00:00:00+00:00", "home": "Lecce", "home_goals": 3.0, "home_xg": 1.07, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 0.0, "away_xg": 0.41, "date": "2026-09-07T00:00:00+00:00", "home": "Cagliari", "home_goals": 1.0, "home_xg": 1.36, "source": "pipeline training history"}, {"away": "Roma", "away_goals": 4.0, "away_xg": 3.26, "date": "2026-08-31T00:00:00+00:00", "home": "Lecce", "home_goals": 0.0, "home_xg": 0.8, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 2.0, "away_xg": 2.7, "date": "2026-08-23T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 2.05, "source": "pipeline training history"}], "h2h": [{"away": "Lecce", "away_goals": 0.0, "away_xg": null, "date": "2026-02-01T00:00:00+00:00", "home": "Torino", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": null, "date": "2025-11-30T00:00:00+00:00", "home": "Lecce", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 0.0, "away_xg": null, "date": "2025-05-18T00:00:00+00:00", "home": "Lecce", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 0.0, "away_xg": null, "date": "2024-09-15T00:00:00+00:00", "home": "Torino", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Lecce", "away_goals": 0.0, "away_xg": null, "date": "2024-02-16T00:00:00+00:00", "home": "Torino", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": null, "date": "2023-10-28T00:00:00+00:00", "home": "Lecce", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 2.0, "away_xg": null, "date": "2023-03-12T00:00:00+00:00", "home": "Lecce", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Torino", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Frosinone", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Como", "away_goals": 3.0, "away_xg": 2.26, "date": "2026-10-27T00:00:00+00:00", "home": "Torino", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Monza", "away_goals": 2.0, "away_xg": 0.58, "date": "2026-10-23T00:00:00+00:00", "home": "Torino", "home_goals": 3.0, "home_xg": 1.22, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 3.0, "away_xg": 1.35, "date": "2026-10-19T00:00:00+00:00", "home": "Parma", "home_goals": 0.0, "home_xg": 1.39, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 1.0, "away_xg": 0.7, "date": "2026-10-12T00:00:00+00:00", "home": "Torino", "home_goals": 2.0, "home_xg": 2.42, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": 1.14, "date": "2026-09-19T00:00:00+00:00", "home": "Bologna", "home_goals": 1.0, "home_xg": 0.92, "source": "pipeline training history"}, {"away": "Roma", "away_goals": 2.0, "away_xg": 1.91, "date": "2026-09-14T00:00:00+00:00", "home": "Torino", "home_goals": 0.0, "home_xg": 0.87, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 2.0, "away_xg": 0.58, "date": "2026-09-05T00:00:00+00:00", "home": "Fiorentina", "home_goals": 1.0, "home_xg": 1.67, "source": "pipeline training history"}, {"away": "Torino", "away_goals": 1.0, "away_xg": 1.26, "date": "2026-08-29T00:00:00+00:00", "home": "Sassuolo", "home_goals": 2.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Milan", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-23T00:00:00+00:00", "home": "Torino", "home_goals": 1.0, "home_xg": 1.29, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 22.3% |
| Raw p over 1 5 | 63.4% |
| Raw p under 3 5 | 83.0% |
| Raw p btts yes | 41.1% |
| P home draw | 78.8% |
| P draw away | 47.6% |
| P home away | 73.6% |
| Raw p home draw | 77.7% |
| Raw p draw away | 51.1% |
| Raw p home away | 71.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2665 |
| Totals anchor target over 2 5 | 0.5040 |
| Totals anchor reference over odds | 1.93 |
| Totals anchor reference under odds | 1.96 |
| Totals anchor reference last update utc | 2026-11-05T12:29:20Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3706 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.59, "draw": 3.78, "home": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.53, "draw": 3.85, "home": 1.87}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.01, "under": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 3.78 |
| Reference away odds | 4.59 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T12:29:20Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:29:20Z |
| Market best over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best under 2 5 last update utc | 2026-11-05T12:29:20Z |
| Home probability edge | -1.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0500 |
| Raw ev home | -0.0855 |
| Raw edge prob draw | 0.0343 |
| Raw ev draw | 0.1082 |
| Raw edge prob away | 0.0157 |
| Raw ev away | 0.0242 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 9.02701796233303, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,432.4444 |
| Elo away rating | 1,399.8995 |
| Elo rating diff | 92.5448 |
| Elo home expectancy | 0.6301 |

</details>


---

## 2026-11-08 — Napoli vs Lazio

The model's most likely 1X2 outcome is **Napoli win** at **43.6%**. Expected goals are 1.40 for Napoli and 1.03 for Lazio (2.43 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.1%; Under 3.5 goals: 77.3%; Double Chance 1X: 70.1%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.6% | 2.30 |
| Draw | 26.5% | 3.77 |
| Lazio win | 29.9% | 3.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.40 |
| Lazio expected goals | 1.03 |
| Expected total goals | 2.43 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.1% |
| Under 2.5 | 55.9% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.54% |
| 2 | 1-0 | 11.61% |
| 3 | 0-1 | 9.60% |
| 4 | 0-0 | 8.78% |
| 5 | 2-1 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.6% | 42.8% | 2.28 | -0.7% |
| Draw | 26.5% | 26.1% | 3.77 | -0.0% |
| Lazio win | 29.9% | 31.0% | 3.27 | -2.1% |
| Over 2.5 | 44.1% | 54.5% | 1.81 | -20.3% |
| Under 2.5 | 55.9% | 45.5% | 2.16 | +20.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T11:30:00+00:00 |
| Fixture id | 23bf8ea47358ef82f65aa7398a2b3921 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-05T12:29:20Z |
| Market best draw last update utc | 2026-11-05T12:28:31Z |
| Market best away last update utc | 2026-11-05T12:28:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4010 |
| Dc lambda away | 1.0295 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T12:28:47.541976+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.39 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 9.98 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.0877627078650189,0.0959810574447241,0.05099388331892399,0.017498780023998413,0.0045035887012156335,0.000927256010391641,0.0001590960316779037,2.3397650405676172e-05,3.0108782971579668e-06,3.443988021823921e-07,3.545459859701494e-08,3.318110372757853e-09,2.8465611819118933e-10,2.2541775015341303e-11,1.657566709143792e-12],[0.11608620896734942,0.12537332435687426,0.07144348425407375,0.024516152403833265,0.0063096208313815644,0.0012991048311342512,0.00022289682789951076,3.27805917012778e-05,4.218302710319583e-06,4.825098384242603e-07,4.967262525896587e-08,4.648741196798239e-09,3.988091036453962e-10,3.158149259383354e-11,2.322285211035192e-12],[0.0832256425580112,0.08567775878355813,0.04422266211044421,0.017173818056564243,0.00441995458255969,0.0009100363563906888,0.0001561415308844702,2.2963143171529676e-05,2.954964631530565e-06,3.3800312704471534e-07,3.47961872049708e-08,3.256491238542989e-09,2.793698975470803e-10,2.2123161857829883e-11,1.6267847838771141e-12],[0.03886694832555792,0.040012103492851,0.02059549945254981,0.007086925290119614,0.002064149234317015,0.0004249932466854977,7.291917041229307e-05,1.0723946029231591e-05,1.3799888364634126e-06,1.578497884659392e-07,1.6250059097823778e-08,1.5208038388271835e-09,1.304676664299731e-10,1.0331668970015763e-11,7.597196992223092e-13],[0.013613349435139107,0.014014445948280194,0.007213680078258424,0.002475406708359065,0.0006388418418263838,0.00014885608013890563,2.554031613256976e-05,3.7561174959420107e-06,4.833482189033631e-07,5.5287703851876176e-08,5.6916671457550294e-09,5.326694009223642e-10,4.56969741545279e-11,3.618720429474042e-12,2.660957493148805e-13],[0.003814516772264079,0.003926905672876891,0.0020213029702475156,0.0006936191899135058,0.0001785139045325877,3.685605316592704e-05,7.156502132027926e-06,1.052479645448765e-06,1.3543616849294575e-07,1.5491843109424746e-08,1.5948286564646702e-09,1.4925616752666977e-10,1.280448101216199e-11,1.0139804195970345e-12,7.45611286646164e-14],[0.000890702803353067,0.0009169459987086303,0.00047198120483207107,0.00016196246963904345,4.168361150246106e-05,8.582351068172404e-06,1.4765964033512664e-06,2.457576219062847e-07,3.1624811779360464e-08,3.6173987192827145e-09,3.7239798380483945e-10,3.485182914920897e-11,2.9898904144139995e-12,2.367679200802508e-13,1.7410280328463274e-14],[0.00017827043324961483,0.00018352289881756715,9.446506012369206e-05,3.2416109530627375e-05,8.342800150598378e-06,1.717721598566608e-06,2.9472193956871436e-07,4.346315088112355e-08,6.329573541388474e-09,7.240071935279499e-10,7.453389577786735e-11,6.9754475438742254e-12,5.984140361295954e-13,4.738810693468237e-14,3.4845946430934266e-15],[3.122007008953688e-05,3.213992168907128e-05,1.6543437654322035e-05,5.676954911301744e-06,1.4610544255534473e-06,3.008204317676818e-07,5.161394092410102e-08,7.590666675120243e-09,9.794825761457384e-10,1.267936298534817e-10,1.3052941016713902e-11,1.221593268473821e-12,1.0479880376107733e-13,8.298964628866454e-15,6.102486374657226e-16],[4.859995924311115e-06,5.003188268591166e-06,2.575299778107987e-06,8.837256819827251e-07,2.2744082678296783e-07,4.682840455346751e-08,8.034688641292756e-09,1.181631207043707e-09,1.520557703379214e-10,1.744083113561045e-11,2.0319377874415273e-12,1.9016415686838503e-13,1.631392106714747e-14,1.2918912147417086e-15,9.499677234529293e-17],[6.808954715643932e-07,7.009570148869415e-07,3.608048204450023e-07,1.2381179415340443e-07,3.186492981006678e-08,6.560756242930602e-09,1.1256764813154784e-09,1.6554897379862965e-10,2.130332762840775e-11,2.4367775092895955e-12,2.515490366732683e-13,2.6642391327498444e-14,2.285614052166965e-15,1.8099662871551445e-16,1.330924410442012e-17],[8.672260231886978e-08,8.927775111353995e-08,4.5954091729076835e-08,1.576935291122144e-08,4.05849319204318e-09,8.356140969178189e-10,1.4337236463702155e-10,2.108523028659592e-11,2.713309292162443e-12,3.103614221315943e-13,3.195057465921978e-14,2.9984220949200796e-15,2.9110841058332813e-16,2.3052728808855425e-17,1.6951387280936451e-18],[1.0125013155158167e-08,1.042333117684642e-08,5.3652193413136035e-09,1.8410991068669506e-09,4.738360688078186e-10,9.755938472440887e-11,1.6738970455457793e-11,2.461736944266843e-12,3.167835321194e-13,3.623523046946482e-14,3.730284609656759e-15,3.4910833986097315e-16,3.00321039610199e-17,2.6914457847301928e-18,1.979103654968587e-19],[1.0911809731537716e-09,1.1233309510576776e-09,5.782140894360704e-10,1.9841676097775255e-10,5.106570181725318e-11,1.0514054918499574e-11,1.803972576753984e-12,2.653034098158387e-13,3.4140021110099584e-14,3.905100511003153e-15,4.020158322887841e-16,3.762369215604671e-17,3.2276847235371135e-18,2.5630349912650046e-19,2.1328962433008052e-20],[1.0919764937618059e-10,1.1241499104633077e-10,5.786356338318388e-11,1.9856141582989957e-11,5.110293103876531e-12,1.052172014321248e-12,1.8052877548925733e-13,2.6549682808016223e-14,3.416491073979439e-15,3.9079475070646494e-16,4.0230892013324814e-17,3.765112154053641e-18,3.230037852648584e-19,2.557850750867654e-20,1.8860532283249924e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18681877378799797, "-10": 4.039330745607959e-08, "-11": 3.739802357960301e-09, "-12": 3.178643955689e-10, "-13": 2.4864060226376495e-11, "-14": 1.657566709143792e-12, "-2": 0.08038160870984486, "-3": 0.024795251629018092, "-4": 0.005970058228805134, "-5": 0.0011745528882902902, "-6": 0.00019499528176038005, "-7": 2.797075201627274e-05, "-8": 3.529751854990879e-06, "-9": 3.9746207962788904e-07, "0": 0.26512283857418156, "1": 0.22502227263454827, "10": 7.757419690733284e-07, "11": 9.774400372673525e-08, "12": 1.1306207669599028e-08, "13": 1.2035959642001023e-09, "14": 1.0919764937618059e-10, "2": 0.1311884994693247, "3": 0.05507331153729461, "4": 0.018046161452291248, "5": 0.0048318389334593625, "6": 0.0010916855830585364, "7": 0.0002131136243940465, "8": 3.660031706213677e-05, "9": 5.608800247907832e-06} |
| Raw goal margin distribution | {"-1": 0.17082383557856778, "-10": 3.693493738044848e-08, "-11": 3.4196101930179393e-09, "-12": 2.9064967157187803e-10, "-13": 2.2735263966276037e-11, "-14": 1.5156501525088032e-12, "-2": 0.0734995441377501, "-3": 0.02267234658231504, "-4": 0.005458917348580745, "-5": 0.001073990720522128, "-6": 0.00017830029217423126, "-7": 2.5575968873764392e-05, "-8": 3.2275436685734396e-06, "-9": 3.63432408651384e-07, "0": 0.274351527093637, "1": 0.2334971520762091, "10": 8.049582754805176e-07, "11": 1.0142527775366084e-07, "12": 1.1732026615521104e-08, "13": 1.2489262800556861e-09, "14": 1.1331029521759404e-10, "2": 0.1361293735619998, "3": 0.05714750477277764, "4": 0.01872582325155366, "5": 0.005013817597007461, "6": 0.001132801085076623, "7": 0.00022113999553041928, "8": 3.7978772941177366e-05, "9": 5.820041141339633e-06} |
| Research history json | {"away": [{"away": "Cagliari", "away_goals": 1.0, "away_xg": 0.99, "date": "2026-11-01T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": 1.02, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 6.0, "away_xg": 3.57, "date": "2026-10-27T00:00:00+00:00", "home": "Sassuolo", "home_goals": 2.0, "home_xg": 0.76, "source": "pipeline training history"}, {"away": "Parma", "away_goals": 1.0, "away_xg": 0.81, "date": "2026-10-24T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 3.0, "away_xg": 0.57, "date": "2026-10-18T00:00:00+00:00", "home": "Juventus", "home_goals": 0.0, "home_xg": 0.75, "source": "pipeline training history"}, {"away": "Monza", "away_goals": 1.0, "away_xg": 1.76, "date": "2026-10-11T00:00:00+00:00", "home": "Lazio", "home_goals": 3.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": 1.6, "date": "2026-09-19T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 1.89, "source": "pipeline training history"}, {"away": "Milan", "away_goals": 2.0, "away_xg": 1.25, "date": "2026-09-12T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-09-07T00:00:00+00:00", "home": "Udinese", "home_goals": 1.0, "home_xg": 0.77, "source": "pipeline training history"}, {"away": "Genoa", "away_goals": 0.0, "away_xg": 0.58, "date": "2026-08-30T00:00:00+00:00", "home": "Lazio", "home_goals": 1.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 1.0, "away_xg": 0.63, "date": "2026-08-24T00:00:00+00:00", "home": "Bologna", "home_goals": 0.0, "home_xg": 1.78, "source": "pipeline training history"}], "h2h": [{"away": "Lazio", "away_goals": 2.0, "away_xg": null, "date": "2026-04-18T00:00:00+00:00", "home": "Napoli", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 2.0, "away_xg": null, "date": "2026-01-04T00:00:00+00:00", "home": "Lazio", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 2.0, "away_xg": null, "date": "2025-02-15T00:00:00+00:00", "home": "Lazio", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 1.0, "away_xg": null, "date": "2024-12-08T00:00:00+00:00", "home": "Napoli", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 0.0, "away_xg": null, "date": "2024-01-28T00:00:00+00:00", "home": "Lazio", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": null, "date": "2023-09-02T00:00:00+00:00", "home": "Napoli", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 1.0, "away_xg": null, "date": "2023-03-03T00:00:00+00:00", "home": "Napoli", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Napoli", "away_goals": 0.0, "away_xg": 0.52, "date": "2026-11-01T00:00:00+00:00", "home": "Juventus", "home_goals": 2.0, "home_xg": 0.79, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 4.0, "away_xg": 1.78, "date": "2026-10-28T00:00:00+00:00", "home": "Monza", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Roma", "away_goals": 3.0, "away_xg": 1.9, "date": "2026-10-24T00:00:00+00:00", "home": "Napoli", "home_goals": 3.0, "home_xg": 2.44, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 0.0, "away_xg": 2.36, "date": "2026-10-17T00:00:00+00:00", "home": "Venezia", "home_goals": 1.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Frosinone", "away_goals": 0.0, "away_xg": 1.01, "date": "2026-10-10T00:00:00+00:00", "home": "Napoli", "home_goals": 3.0, "home_xg": 3.12, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 1.0, "away_xg": 1.4, "date": "2026-09-20T00:00:00+00:00", "home": "Fiorentina", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Bologna", "away_goals": 0.0, "away_xg": 0.3, "date": "2026-09-13T00:00:00+00:00", "home": "Napoli", "home_goals": 1.0, "home_xg": 1.19, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 2.0, "away_xg": 2.44, "date": "2026-09-05T00:00:00+00:00", "home": "Inter", "home_goals": 3.0, "home_xg": 3.86, "source": "pipeline training history"}, {"away": "Como", "away_goals": 2.0, "away_xg": 1.03, "date": "2026-08-30T00:00:00+00:00", "home": "Napoli", "home_goals": 1.0, "home_xg": 1.35, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 2.0, "away_xg": 0.77, "date": "2026-08-22T00:00:00+00:00", "home": "Genoa", "home_goals": 0.0, "home_xg": 0.67, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 70.1% |
| Raw p under 3 5 | 77.2% |
| Raw p btts yes | 48.7% |
| P home draw | 70.1% |
| P draw away | 56.4% |
| P home away | 73.5% |
| Raw p home draw | 72.6% |
| Raw p draw away | 54.8% |
| Raw p home away | 72.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4406 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T12:29:20Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.12, "draw": 3.69, "home": 2.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.27, "draw": 3.77, "home": 2.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T12:28:31Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.28 |
| Reference draw odds | 3.69 |
| Reference away odds | 3.12 |
| Market reference 1x2 last update utc | 2026-11-05T12:29:20Z |
| Market reference home last update utc | 2026-11-05T12:29:20Z |
| Market reference draw last update utc | 2026-11-05T12:29:20Z |
| Market reference away last update utc | 2026-11-05T12:29:20Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market reference under 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best over 2 5 last update utc | 2026-11-05T12:28:31Z |
| Market best under 2 5 last update utc | 2026-11-05T12:28:31Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0234 |
| Raw ev home | 0.0304 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0343 |
| Raw edge prob away | -0.0366 |
| Raw ev away | -0.1049 |
| Count model | {"corners": {"alpha": 0.02175182809361759, "mu": 8.942018965993816, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,559.3191 |
| Elo away rating | 1,592.8613 |
| Elo rating diff | 26.4578 |
| Elo home expectancy | 0.5380 |

</details>


---
