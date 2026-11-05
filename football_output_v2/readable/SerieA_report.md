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
| Training as of utc | 2026-11-05T13:34:25.291682+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 100, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 100, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 191, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-05T13:34:25.291682+00:00', 'observations': 695, 'observations_sha256': '13377d2c377d012ea62a498d6a4cdfd527fc649cf2fabe7d3a6866654d8a9903', 'eligible_training_matches': 251, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 236, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 36, 'retrospective_eligible_training_matches': 251, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '3cfe277da88929df0bcfc8e0be5de15bf2b494e5848ae22e0064e69194622fea', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 190, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-11T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 24, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1999, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1620, 'tuning_matches': 250, 'audit_matches': 129, 'audit_matchdays': 42, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8311477877010042, 'audit_candidate_poisson_score': 0.8301690994125219, 'audit_gain': 0.0009786882884822434, 'audit_gain_lower95': -0.0035260819529456993, 'audit_baseline_briers': [0.5470516271063433, 0.1544999061324679, 0.2090980014289932, 0.23872219104127412], 'audit_candidate_briers': [0.5497540597359728, 0.15368329188971547, 0.2092140547665856, 0.23948201814979928], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1825.555 |
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
| Additional event odds calls used before this league | 5.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261105T133425291682Z_eedac8a9c6a3ab36497966dfd5eb3cbfc4e928e851e1260ea9bb24af2d1b058e.json |
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
| Market best home last update utc | 2026-11-05T13:29:44Z |
| Market best draw last update utc | 2026-11-05T13:29:44Z |
| Market best away last update utc | 2026-11-05T13:29:44Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.06625689396905957,0.06753349326505045,0.057681400798827755,0.03197253634175848,0.01329167286986867,0.0044205080458095715,0.001225133684223516,0.00029103685342397634,6.0495148202162486e-05,1.1177394547793386e-05,1.8586735850878956e-06,2.8097843384062467e-07,3.893626482196296e-08,4.980506146863854e-09,5.915725182108264e-10,6.558118761105251e-11],[0.09191353179177095,0.12870713935499506,0.0688253160237084,0.03814955752332821,0.01585959378731062,0.005274540129482647,0.0014618267209226183,0.00034726451046691555,7.21826730151034e-05,1.3336841710147737e-05,2.2177650873068477e-06,3.3526282713509703e-07,4.645866248117992e-08,5.942728587875994e-09,7.058629810118718e-10,7.825132365080373e-11],[0.05694201353546995,0.09468809210191975,0.06245422971625654,0.022759982562360608,0.009461815587889456,0.0031467846330350603,0.0008721241565396,0.00020717761137650434,4.306410049772458e-05,7.956744572314094e-06,1.3231161248370987e-06,2.0001742077182616e-07,2.7717185115336124e-08,3.54542510618088e-09,4.2111705042508474e-10,4.6684650554199995e-11],[0.02264769360851264,0.037660538592705115,0.03131259614355446,0.013768743454787387,0.003763272267871001,0.0012515787517166123,0.00034687218557151716,8.240128463451335e-05,1.7127995535161988e-05,3.1646564988910222e-06,5.262463819465608e-07,7.955344359544844e-08,1.1024027378159674e-08,1.410131053175625e-09,1.6749196839354747e-10,1.8568006228185006e-11],[0.006755794104456282,0.011234117212695497,0.009340529595575827,0.00517741278488313,0.001707455078168265,0.00037334522880209264,0.00010347177539540291,2.458025627493595e-05,5.1092713129123016e-06,9.44015231193395e-07,1.5697899601174933e-07,2.3730746914966863e-08,3.288461088185258e-09,4.20641290024069e-10,4.996275877697282e-11,5.538825682484939e-12],[0.0016121996268847875,0.0026809046129367357,0.0022290197267794947,0.0012355354279537938,0.0005136387226823242,0.00013551402321228557,2.469245733459202e-05,5.8658211577295455e-06,1.2192741781305814e-06,2.252793646419211e-07,3.746139608250528e-08,5.663094631136043e-09,7.847568557337053e-10,1.0038164579080508e-10,1.1923089989559862e-11,1.3217828371637114e-12],[0.0003206121536490876,0.0005331415460889724,0.00044327687664211663,0.0002457063429740647,0.00010214542562260177,3.3971245021456484e-05,7.468900939988644e-06,1.166514073653517e-06,2.4247252860027037e-07,4.480047077675324e-08,7.449808743549483e-09,1.1261986020400336e-09,1.560616820721109e-10,1.9962525178111714e-11,2.371100635404033e-12,2.6285804500421405e-13],[5.46505273310329e-05,9.087761117045676e-05,7.555956561977275e-05,4.188232123854324e-05,1.7411384163676646e-05,5.790630309499517e-06,1.6048599327352324e-06,3.024374589892677e-07,4.133109553232136e-08,7.63654566666195e-09,1.2698706886699385e-09,1.9196822946495017e-10,2.6601777644224173e-11,3.4027485091438336e-12,4.041702680479353e-13,4.4805945779608966e-14],[8.151110588356876e-06,1.355436982646383e-05,1.1269687694765295e-05,6.246736285719232e-06,2.5969029896973108e-06,8.636708616390524e-07,2.3936440194456617e-07,5.686225369585776e-08,9.376279993799658e-09,1.138988611490541e-09,1.894008515885612e-10,2.8632006757075582e-11,3.967647560132934e-12,5.075189711234148e-13,6.028188038203687e-14,6.682794053446e-15],[1.0806540649124124e-06,1.7970047997161321e-06,1.494107298094763e-06,8.281768338710704e-07,3.4429097011739955e-07,1.1450334494416312e-07,3.1734339897953395e-08,7.538656840735673e-09,1.5669911128443358e-09,2.296785882351341e-10,2.5110296069275957e-11,3.7959605814734285e-12,5.260208921863969e-13,6.728560890194499e-14,7.992022481999456e-15,8.859882933185312e-16],[1.2894339683132898e-07,2.1441820330947482e-07,1.7827654242195688e-07,9.881787114270118e-08,4.1080720118226945e-08,1.3662513032647905e-08,3.7865342069237795e-09,8.995108167838878e-10,1.8697302259352492e-10,3.4546096760311915e-11,4.5571725334717176e-12,4.5293315178773867e-13,6.276469301788792e-14,8.02850352520933e-15,9.53606301813969e-16,1.0571592131339704e-16],[1.3986815212817976e-08,2.3258482882043913e-08,1.9338105842657408e-08,1.071902352010323e-08,4.456129241381426e-09,1.4820072204266132e-09,4.1073490811271437e-10,9.757220521144491e-11,2.0281434963424792e-11,3.747302177424981e-12,6.231337314559756e-13,7.472829302339118e-14,6.8082444289783884e-15,8.708720105260719e-16,1.0344007880215889e-16,1.1467272406337227e-17],[1.390753003937359e-09,2.3126640656255e-09,1.9228486529576333e-09,1.065826203680523e-09,4.430869382405828e-10,1.473606365926893e-10,4.0840663052172026e-11,9.70191108081921e-12,2.0166468327753326e-12,3.7260603508500945e-13,6.196014572945025e-14,9.366606835796032e-15,1.0296687471447555e-15,8.659354157865385e-17,1.0285372197509406e-17,1.1402269425470128e-18],[1.2764948583785716e-10,2.1226657649274433e-10,1.7648758708351747e-10,9.78262613901655e-11,4.0668486559262737e-11,1.3525413528169055e-11,3.7485373931442825e-12,8.90484476830195e-13,1.85096800504131e-13,3.419943632264576e-14,5.686977286701055e-15,8.597087644245522e-16,1.191331578863587e-16,1.2088872235135793e-17,9.440371287684106e-19,1.0465509155294537e-19],[1.0879362549383399e-11,1.8091142534755986e-11,1.5041756202499507e-11,8.337576587392104e-12,3.4661103936991188e-12,1.1527494720205617e-12,3.194818769715914e-13,7.589457493263588e-14,1.5775505762500435e-14,2.914763536229379e-15,4.846920244607865e-16,7.327160993768213e-17,1.0153529470106544e-17,1.2987818983012418e-18,1.2237837367963249e-19,8.919586915451048e-21],[8.654153739079892e-13,1.4390873371552381e-12,1.1965192821850304e-12,6.63225159296983e-13,2.75717001685866e-13,9.169720292182488e-14,2.5413669850708864e-14,6.037148927134292e-15,1.2548865024096214e-15,2.318592807353668e-16,3.855556129092557e-17,5.828501203377341e-18,8.07677882134377e-19,1.0331357347834692e-19,1.2271337294991522e-20,1.0791880321088117e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.16328131081485506, "-10": 2.2231150129331184e-06, "-11": 3.311555522220615e-07, "-12": 4.531867846649222e-08, "-13": 5.733053778429926e-09, "-14": 6.698238418616302e-10, "-15": 6.558118761105251e-11, "-2": 0.1066539405606499, "-3": 0.05135163257763637, "-4": 0.019526080637015854, "-5": 0.006107623003587128, "-6": 0.0016187897533032885, "-7": 0.00037172705327048934, "-8": 7.523805073938332e-05, "-9": 1.3606633910488276e-05, "0": 0.2730377565454696, "1": 0.22364090611418833, "10": 1.542261124353173e-07, "11": 1.648458015911607e-08, "12": 1.6187245617918999e-09, "13": 1.469371476547982e-10, "14": 1.2318449886538637e-11, "15": 8.654153739079892e-13, "2": 0.10528680030147873, "3": 0.03637484460049753, "4": 0.009924573207766067, "5": 0.0022275058489872714, "6": 0.0004236302338226743, "7": 6.980242964229903e-05, "8": 1.0137567891885863e-05, "9": 1.3155180469179262e-06} |
| Raw goal margin distribution | {"-1": 0.23920858416389063, "-10": 5.097407198620578e-07, "-11": 6.054523357185537e-08, "-12": 6.6007637933155765e-09, "-13": 6.628452703209308e-10, "-14": 5.732960640115968e-11, "-2": 0.13421317499028637, "-3": 0.05372860722526173, "-4": 0.01671203221234928, "-5": 0.0042367033933895576, "-6": 0.000904915859917976, "-7": 0.0001668308464105604, "-8": 2.7039736847922423e-05, "-9": 3.908628337966121e-06, "0": 0.2856380066466749, "1": 0.17082906575347365, "10": 1.8443699002841127e-08, "11": 1.5719130767161416e-09, "12": 1.229681472507129e-10, "13": 8.8605456875184e-12, "14": 5.498916656801906e-13, "2": 0.06910267984499353, "3": 0.019849756893414713, "4": 0.004430255192915838, "5": 0.0008058930485501212, "6": 0.00012351150644447558, "7": 1.6338998836218873e-05, "8": 1.9002092120488835e-06, "9": 1.970939097395581e-07} |
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
| Totals anchor reference last update utc | 2026-11-05T13:35:35Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.3949 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.45, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.1, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.42, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.0, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.0, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.25, "draw": 3.64, "home": 2.31}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.69, "home_away": 1.33, "home_draw": 1.39}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.12}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:31:08Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.25, "under": 3.85}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.16, "draw": 3.6, "home": 2.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:15Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.67, "home_away": 1.32, "home_draw": 1.4}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:35Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.83, "under": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.29 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-11-05T13:34:51Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:34:51Z |
| Market best over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best under 2 5 last update utc | 2026-11-05T13:29:44Z |
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
| Market p home draw | 70.3% |
| Market home draw odds | 1.40 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-05T13:35:15Z |
| Market reference home draw last update utc | 2026-11-05T13:35:36Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.8% |
| Market draw away odds | 1.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:29:44Z |
| Market reference draw away last update utc | 2026-11-05T13:35:36Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.0% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-05T13:29:44Z |
| Market reference home away last update utc | 2026-11-05T13:35:36Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home draw odds | 1.35 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 78.0% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T13:31:08Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.90 |
| Market reference over 1 5 last update utc | 2026-11-05T13:35:36Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.3% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-11-05T13:31:08Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.02 |
| Market reference under 3 5 last update utc | 2026-11-05T13:35:35Z |
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
| Market best home last update utc | 2026-11-05T13:29:44Z |
| Market best draw last update utc | 2026-11-05T13:35:10Z |
| Market best away last update utc | 2026-11-05T13:35:10Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.034042573750132796,0.027086238331562137,0.013065471729584433,0.003980313239283837,0.0009094329204515886,0.00016623178872221962,2.5320730974553522e-05,3.305914446400341e-06,3.776722143473697e-07,3.8351816298440835e-08,3.5050914040312382e-09,2.9121924654365137e-10,2.2179524906232216e-11,1.5592735002807304e-12,1.0179059987738323e-13,6.201972354494992e-15,3.5426092695679634e-16,1.9045296779777117e-17,9.6700484666246e-19],[0.09288474633374649,0.07182431447881045,0.030925608363951716,0.00942129078471927,0.0021526024404834284,0.0003934660226635415,5.9933466300717335e-05,7.82500759024328e-06,8.939396320766961e-07,9.077768299832569e-08,8.296453911838319e-09,6.893078606768769e-10,5.249831886249597e-11,3.6907570273778226e-12,2.409355201321759e-13,1.4679896148324385e-14,8.385257656567483e-16,4.507968801868522e-17,2.288873589325626e-18],[0.11220924708545248,0.10255151003839877,0.03799813798233607,0.011149966687823625,0.002547575067149702,0.0004656615686466861,7.093042429203723e-05,9.260787715489175e-06,1.0579651288066547e-06,1.0743412601920919e-07,9.81873788399555e-09,8.157862717354988e-10,6.213103064741195e-11,4.367959640398669e-12,2.851438390739861e-13,1.7373453041063785e-14,9.92383588151094e-16,5.3351184162691063e-17,2.7088500776362013e-18],[0.08853205614513154,0.08091219111000177,0.03697408009754818,0.009133271639397098,0.0020100131204612228,0.0003674026625333559,5.596344747807128e-05,7.306675690921075e-06,8.347246828220206e-07,8.476452987330384e-08,7.746893203536363e-09,6.436478087827595e-10,4.902080743347841e-11,3.446279679864088e-12,2.2497584669748072e-13,1.3707493455462956e-14,7.82981454966827e-16,4.209358991691314e-17,2.137257609253881e-18],[0.05238822892632761,0.04787922674983122,0.02187915492796611,0.006665346022442896,0.0012348464579700815,0.00021740797210658905,3.311598109933803e-05,4.32367455872599e-06,4.939425297256124e-07,5.015882143927109e-08,4.584170212305549e-09,3.808741174966443e-10,2.900772210427999e-11,2.039312048924995e-12,1.3312789370169996e-13,8.111313985227263e-15,4.63323834257597e-16,2.4908589282995746e-17,1.2647073363413024e-18],[0.024800296295282506,0.022665759734971598,0.010357470294844465,0.0031553377477148113,0.0007209402502783249,0.00010685122860438931,1.567692132764241e-05,2.046803496479568e-06,2.3382964725269413e-07,2.374490718641082e-08,2.1701206905288533e-09,1.8030368956363127e-10,1.3732094361293177e-11,9.653989853904543e-13,6.302200468758e-14,3.839850941718146e-15,2.193349270580171e-16,1.1791587674866951e-17,5.987054212538825e-19],[0.009783601980493554,0.0089415371974665,0.004085974041722197,0.0012447661217475407,0.0002844075883795884,5.1985782655674656e-05,6.420717880313396e-06,8.074544958419628e-07,9.224471243090478e-08,9.367255867011337e-09,8.561025575249593e-10,7.112897012607824e-11,5.41724760018404e-12,3.8084542672295216e-13,2.4861888847407342e-14,1.514803405205274e-15,8.652661247294913e-17,4.651726703399757e-18,2.361865146839363e-19],[0.003308216271971083,0.00302348142453779,0.0013816267095316684,0.00042090382938450376,9.61692650237948e-05,1.757841462025412e-05,2.677576358769688e-06,2.8346149698868544e-07,3.1191524274561474e-08,3.167433461086098e-09,2.89481564859945e-10,2.4051470700545238e-11,1.831782067172878e-12,1.2877864822206124e-13,8.406771391652646e-15,5.122139355146263e-16,2.9258012326366735e-17,1.5729296841420726e-18,7.986384489632704e-20],[0.000978806993422313,0.0008945620598912021,0.0004087840015317101,0.00012453345787889452,2.8453747100847638e-05,5.200952340800334e-06,7.92218600576707e-07,1.0343330605208871e-07,9.581216877900756e-09,9.371533684717978e-10,8.564935205488456e-11,7.116145314695227e-12,5.419721536845357e-13,3.810193503707161e-14,2.4873242719858563e-15,1.515495182276475e-16,8.656612725509958e-18,4.653851043669819e-19,2.3629437581946296e-20],[0.0002574232158451831,0.00023526705854964015,0.00010750892971496441,3.275191475228266e-05,7.483247597093417e-06,1.3678344004727605e-06,2.0835104487738085e-07,2.7202639997832224e-08,3.1076670163869994e-09,2.5588346350176816e-10,2.252551502920434e-11,1.871524236791092e-12,1.425370023279122e-13,1.0020691222151255e-14,6.541586004669241e-16,3.985705517442811e-17,2.2766624075045256e-18,1.2239484492619037e-19,6.21446909537271e-21],[6.09313595542895e-05,5.5687058716528124e-05,2.54470647888222e-05,7.752287171577245e-06,1.7712639028116774e-06,3.237626000137288e-07,4.9316113106793625e-08,6.438789264176725e-09,7.355761434678136e-10,7.469620495259932e-11,5.535397190120266e-12,4.4298458401307043e-13,3.3738112198302456e-14,2.371869754772298e-15,1.5483752217030973e-16,9.434054157216281e-18,5.388796627372578e-19,2.8970519536490987e-20,1.4709475586572676e-21],[1.3111166743077977e-05,1.1982701807489444e-05,5.475681357001138e-06,1.6681316565111524e-06,3.811393106216037e-07,6.966700669415182e-08,1.0611806248760213e-08,1.38549410818486e-09,1.582807529617613e-10,1.6073076415372898e-11,1.4689682893102286e-12,9.896234714009668e-14,7.259743059474798e-15,5.10377251962923e-16,3.331782822687808e-17,2.0300130839569113e-18,1.1595574371365588e-19,6.233855851158194e-21,3.165174526377559e-22],[2.5861472658808443e-06,2.363560171612103e-06,1.0800654623448706e-06,3.2903510474330515e-07,7.517884604771425e-08,1.3741655675251272e-08,2.093154198559586e-09,2.7328550311267936e-10,3.122051183810392e-11,3.1703770869862457e-12,2.8975059195787967e-13,2.4073822719288673e-14,1.486668239709186e-15,1.0067073057617371e-16,6.571864431479293e-18,4.0041537794866284e-19,2.2872001816815547e-20,1.2296136248804465e-21,6.24323342676471e-23],[4.708722064210442e-07,4.3034470917371604e-07,1.9665268642784503e-07,5.9908995827308e-08,1.3688172201832467e-08,2.502008997341437e-09,3.811105998712435e-10,4.975839911797253e-11,5.684467968530474e-12,5.772457252651747e-13,5.275627662314907e-14,4.383236086503207e-15,3.338312803989812e-16,1.902978700568015e-17,1.1965708008884959e-18,7.290554369701942e-20,4.164414804538159e-21,2.238816359112594e-22,1.1367353814868809e-23],[7.961010159687806e-08,7.275814021684704e-08,3.324796013086593e-08,1.0128780546699478e-08,2.3142516479068687e-09,4.230132672059806e-10,6.443415678747284e-11,8.412624816376854e-12,9.610698323830506e-13,9.759461316268999e-14,8.919474295933294e-15,7.41071283059758e-16,5.64406685855966e-17,3.967913615630196e-18,2.1003149540899171e-19,1.2326099654107671e-20,7.040752908324749e-22,3.785154344963281e-23,1.921872176248543e-24],[1.256232648798907e-08,1.1481099681183718e-08,5.246466489121533e-09,1.5983027982697741e-09,3.651846209616304e-10,6.67507095808163e-11,1.0167590523138503e-11,1.3274966046322627e-12,1.5165503836797348e-13,1.5400249081792224e-14,1.4074765131455947e-15,1.1693967501524609e-16,8.906232899474871e-18,6.261294146827017e-19,4.08742204045361e-20,2.0193354751128557e-21,1.1110177600766005e-22,5.972903404851806e-24,3.0326786754362144e-25],[1.85841734778299e-09,1.698465235682079e-09,7.761400205023917e-10,2.3644614316898896e-10,5.402386535547589e-11,9.874817119298643e-12,1.5041502568350505e-12,1.9638422242332036e-13,2.2435203738034076e-14,2.2782475906151304e-15,2.0821611117397367e-16,1.729955998996064e-17,1.3175503549923423e-18,9.262693238518187e-20,6.0467589621653725e-21,3.684213666371856e-22,1.7063773512304692e-23,8.836060195395828e-25,4.4864163227016944e-26],[2.587542469541123e-10,2.3648352914965073e-10,1.0806481481440456e-10,3.292126162827889e-11,7.521940437266547e-12,1.3749069177393762e-12,2.0942834368044016e-13,2.7343293823336033e-14,3.123735502911898e-15,3.172087477486658e-16,2.8990690984889885e-17,2.4086810334502232e-18,1.8344735661065125e-19,1.2896786701646707e-20,8.4191237433004965e-22,5.1296654865891703e-23,2.9301002106858603e-24,1.2772732117573293e-25,6.2466015961817866e-27],[3.402578384306012e-11,3.10972188476466e-11,1.4210356248055441e-11,4.3290950590785824e-12,9.891235502858945e-13,1.8079813621619305e-13,2.7539503743660245e-14,3.595600907586675e-15,4.107663941988247e-16,4.171246041784958e-17,3.81223109001859e-18,3.1673783582609306e-19,2.412304407015873e-20,1.6959075329036222e-21,1.1071017693801185e-22,6.745430890061572e-24,3.8530365232993714e-25,2.0714173792727195e-26,8.527964073549467e-28]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.07140575100338228, "-10": 4.260113630903206e-09, "-11": 3.483188362737463e-10, "-12": 2.6169608617747938e-11, "-13": 1.818390962203641e-12, "-14": 1.1750623791111197e-13, "-15": 7.095986561923686e-15, "-16": 4.0204946505311774e-16, "-17": 2.1334170369102743e-17, "-18": 9.6700484666246e-19, "-2": 0.0254369985282836, "-3": 0.006659107864096521, "-4": 0.001381654611241178, "-5": 0.00023631316936289576, "-6": 3.4293238245932604e-05, "-7": 4.315430093317693e-06, "-8": 4.789422815424466e-07, "-9": 4.751518116803476e-08, "0": 0.1543467095593644, "1": 0.23985139271859177, "10": 7.405641835421294e-05, "11": 1.5681883654126648e-05, "12": 3.0513936642954735e-06, "13": 5.491209620087552e-07, "14": 9.190125168374275e-08, "15": 1.4373185633544633e-08, "16": 2.1091112331806963e-09, "17": 2.8985146580175887e-10, "18": 3.402578384306012e-11, "2": 0.21845873704731897, "3": 0.14811510448025816, "4": 0.07959073884732124, "5": 0.03525581156123191, "6": 0.013250462396114122, "7": 0.00431843481939231, "8": 0.0012412669950567412, "9": 0.0003189291125760649} |
| Raw goal margin distribution | {"-1": 0.08580779965685871, "-10": 5.119349237552032e-09, "-11": 4.1857234886125727e-10, "-12": 3.144783860985865e-11, "-13": 2.1851479074174552e-12, "-14": 1.412064375687369e-13, "-15": 8.527198225874944e-15, "-16": 4.831400757593186e-16, "-17": 2.5637125737821145e-17, "-18": 1.1620430705321397e-18, "-2": 0.030567466106243765, "-3": 0.008002204100741702, "-4": 0.001660324839532076, "-5": 0.0002839759096155742, "-6": 4.1209948437521883e-05, "-7": 5.1858226498177145e-06, "-8": 5.755416442556069e-07, "-9": 5.7098666270353336e-08, "0": 0.17865289069378099, "1": 0.2251084289956474, "10": 6.950438687808833e-05, "11": 1.471796412378864e-05, "12": 2.8638334188150086e-06, "13": 5.153681022457031e-07, "14": 8.625235048575702e-08, "15": 1.3489707943560522e-08, "16": 1.9794703332634736e-09, "17": 2.7203514379952964e-10, "18": 3.193431841041393e-11, "2": 0.2050307173108332, "3": 0.139010902134706, "4": 0.07469852887426887, "5": 0.03308873992166867, "6": 0.012435995220401922, "7": 0.004052993259263877, "8": 0.0011649699426561312, "9": 0.00029932547265717406} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.03, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.39, "draw": 6.38, "home": 1.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.9, "draw": 6.12, "home": 1.35}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.38 |
| Reference away odds | 9.39 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-11-05T13:34:50Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:34:50Z |
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
| Market best home last update utc | 2026-11-05T13:29:44Z |
| Market best draw last update utc | 2026-11-05T13:29:44Z |
| Market best away last update utc | 2026-11-05T13:29:44Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.04203349273643184,0.05798069397955292,0.057688559470264744,0.037089796956548356,0.017884651448790163,0.006899164378159033,0.002217845343214593,0.0006111097804403786,0.0001473381673257343,3.157612046618594e-05,6.0903855505527666e-06,1.0679185181352934e-06,1.7164963628616988e-07,2.5467455229813583e-08,3.5086781459947403e-09,4.511680000881321e-10,5.438815448273414e-11],[0.05821390381235104,0.10803820520447287,0.07965783226766332,0.051214536329847106,0.024695582249851085,0.00952654189789059,0.0030624573393355273,0.0008438359500472522,0.00020344829420654618,4.360111139636727e-05,8.409759492805485e-06,1.4746090901611207e-06,2.3701818977013864e-07,3.516611084779105e-08,4.844872151451945e-09,6.229842659545372e-10,7.510054899822091e-11],[0.041993541276333375,0.0809969221139137,0.070369817334971,0.03535916810968332,0.01705014448856971,0.006577245848756092,0.0021143595480955448,0.0005825950863354072,0.00014046329327568576,3.0102762577090816e-05,5.8062050538338235e-06,1.018088895294503e-06,1.6364037669225103e-07,2.4279130776902888e-08,3.3449614337965807e-09,4.301162710465937e-10,5.185037544916751e-11],[0.01932858379565756,0.03728087102650337,0.03595357422945364,0.02082421887182107,0.007847757927982098,0.0030273428643649535,0.0009731871725365885,0.000268154044715409,6.465176433746504e-05,1.3855553765359598e-05,2.6724519415809645e-06,4.686010259205848e-07,7.531960004124977e-08,1.1175080725367937e-08,1.539602648439113e-09,1.9797183409928742e-10,2.3865439690135262e-11],[0.0066723502029877434,0.012869594068093857,0.012411402762054696,0.00797968284557062,0.0034663590268533577,0.0010450580336929336,0.0003359504088281117,9.256848373396173e-05,2.2318200725989865e-05,4.783025386452507e-06,9.225474273437893e-07,1.6176405801256525e-07,2.600080553946717e-08,3.857709024862185e-09,5.314806378179193e-10,6.834113773689946e-11,8.238501746653625e-12],[0.0018426702215529173,0.003554132656606031,0.003427596211466394,0.0022037098637876515,0.0010626260061298214,0.00036928217021175,9.277777626073848e-05,2.5564184019372614e-05,6.163508003223098e-06,1.3209046558439254e-06,2.54775397067056e-07,4.467358630004752e-08,7.180514908002093e-09,1.06536457579017e-09,1.4677640034548863e-10,1.8873436732748522e-11,2.275186609955313e-12],[0.0004240676625803046,0.0008179394829081545,0.0007888186918442145,0.0005071564515510642,0.00024455017579692124,9.433741923132538e-05,2.7319996801131854e-05,5.883279404022643e-06,1.4184548063185592e-06,3.039897987948728e-07,5.863339291723216e-08,1.0281070969592712e-08,1.6525063126017595e-09,2.4518042358683705e-10,3.377876534196484e-11,4.343487025784164e-12,5.236059368260914e-13],[8.365191852386957e-05,0.000161347381607368,0.00015560299160458145,0.00010004207796903303,4.8240158790433905e-05,1.8609073041018693e-05,5.982180409589913e-06,1.4849415850840809e-06,2.798055035981001e-07,5.996526527429034e-08,1.1566068908075552e-08,2.0280520939830647e-09,3.2597468663568586e-10,4.8364481962003017e-11,6.663225649015069e-12,8.567996450839413e-13,1.0328691628944047e-13],[1.4438587468277237e-05,2.784907176337794e-05,2.685757175990266e-05,1.72675811715176e-05,8.326404994292095e-06,3.2119852544641825e-06,1.0325433847668675e-06,2.8450918053892094e-07,6.179512301865287e-08,1.035019570381083e-08,1.9963403175949735e-09,3.500482483356527e-10,5.6264268751835125e-11,8.347863569525154e-12,1.150093961404127e-12,1.4788634662100898e-13,1.7827650596539234e-14],[2.215241036989414e-06,4.272745290897828e-06,4.1206243510413995e-06,2.6492795437735166e-06,1.2774791214497002e-06,4.927990055486307e-07,1.5841802277632577e-07,4.365083589476968e-08,1.0524187909964584e-08,2.0318609686909193e-09,3.0628861757074145e-10,5.3706170797046966e-11,8.632348374043394e-12,1.2807714044764188e-12,1.7645322614097294e-13,2.2689470459979035e-14,2.735208224580894e-15],[3.0588612469670606e-07,5.899915526235723e-07,5.689863057899628e-07,3.658192672272218e-07,1.763975708811631e-07,6.804694186530706e-08,2.187476408211571e-08,6.027418600807897e-09,1.4532066721434504e-09,3.1143748951635116e-10,5.411514086351406e-11,7.415884855462167e-12,1.1919766504310488e-12,1.7685217770707146e-13,2.4365110899104224e-14,3.1330198721199207e-15,3.776845183369567e-16],[3.8397759275043394e-08,7.406139665344873e-08,7.142461666799e-08,4.5921141977561876e-08,2.2143114435521315e-08,8.541904591905372e-09,2.7459301276129104e-09,7.566193749821722e-10,1.8242043515108157e-10,3.9094619814906165e-11,7.540549760697644e-12,1.1911274368477193e-12,1.496283380951174e-13,2.220018104317908e-14,3.058542338071651e-15,3.9328669442874996e-16,4.741058206348038e-17],[4.418383667796533e-09,8.522155239419992e-09,8.218744159104801e-09,5.284090206068305e-09,2.5479813672264467e-09,9.829066188578591e-10,3.1597085501395116e-10,8.706327536493658e-11,2.0990898598287143e-11,4.49857056636024e-12,8.676819308705839e-13,1.521436687606722e-13,2.203030662552735e-14,2.5545479526734126e-15,3.5194276356077125e-16,4.525502373663472e-17,5.45547827334183e-18],[4.693089774250985e-10,9.052006936429586e-10,8.729731745888746e-10,5.612620264977161e-10,2.7063981307616816e-10,1.044017303347015e-10,3.356158496228629e-11,9.247629858539425e-12,2.2295974947121133e-12,4.778262168043104e-13,9.216287002757879e-14,1.6160296383537613e-14,2.5974912405812533e-15,3.471831528303154e-16,3.738242554233406e-17,4.806868418418806e-18,5.794664117758092e-19],[4.628812782282165e-11,8.928029811519921e-11,8.610168531820462e-11,5.5357492982900694e-11,2.6693310514422448e-11,1.0297183457198393e-11,3.31019223879802e-12,9.120973463980505e-13,2.1990607210395528e-13,4.7128186470848363e-14,9.090059882853027e-15,1.5938963468374235e-15,2.5619157601108065e-16,3.801084367834034e-17,4.717668023820684e-18,4.741033103607425e-19,5.715299861612236e-20],[4.261055058348896e-12,8.218700642869871e-12,7.926093342159632e-12,5.095935752579842e-12,2.4572535365208487e-12,9.479075460772684e-13,3.0471985035185105e-13,8.396314982650565e-14,2.024346036389501e-14,4.33838668353766e-15,8.367857475849011e-16,1.467261781935129e-16,2.3583723563997153e-17,3.499089406848862e-18,4.82073235111452e-19,5.58431186626435e-20,5.261221079954026e-21],[3.677358347110734e-13,7.092869488331122e-13,6.840344729801181e-13,4.3978736767017613e-13,2.120648919048167e-13,8.180593020093936e-14,2.6297808169038704e-14,7.246153491005375e-15,1.7470428549782712e-15,3.7440967706911437e-16,7.22159420962045e-17,1.2662702751572655e-17,2.035312886513655e-18,3.0197698601313925e-19,4.160368760272938e-20,5.349664959563654e-21,5.809710668362576e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18198946184379539, "-10": 7.740360975811995e-06, "-11": 1.330826057655121e-06, "-12": 2.1036691890360349e-07, "-13": 3.076630909200226e-08, "-14": 4.183512787398445e-09, "-15": 5.26268549086353e-10, "-16": 5.438815448273414e-11, "-2": 0.1293435782172266, "-3": 0.06943486013415756, "-4": 0.029817406763888353, "-5": 0.010613916984524106, "-6": 0.0032169690633604897, "-7": 0.0008475024857327881, "-8": 0.0001972411856253639, "-9": 4.108329738652633e-05, "0": 0.24513024416546075, "1": 0.184307323959561, "10": 3.88755195051626e-07, "11": 4.7850784241501885e-08, "12": 5.414994047402181e-09, "13": 5.669551562501276e-10, "14": 5.519086293867164e-11, "15": 4.970342007182008e-12, "16": 3.677358347110734e-13, "2": 0.09415376186492307, "3": 0.036184547303267936, "4": 0.011124185486268284, "5": 0.0028348286385714637, "6": 0.0006151071604096235, "7": 0.0001160105944208707, "8": 1.932889598594258e-05, "9": 2.882222545449582e-06} |
| Raw goal margin distribution | {"-1": 0.21436248470332867, "-10": 9.117247748663035e-06, "-11": 1.5675587890454172e-06, "-12": 2.477878388050055e-07, "-13": 3.62391448125328e-08, "-14": 4.92769299282069e-09, "-15": 6.198833309381119e-10, "-16": 6.406293977260232e-11, "-2": 0.15235173798613724, "-3": 0.08178621439169648, "-4": 0.03512144789352187, "-5": 0.012501963543308419, "-6": 0.003789216554899138, "-7": 0.000998259661814158, "-8": 0.0002323272469082526, "-9": 4.839136078736529e-05, "0": 0.2256577705852999, "1": 0.15284733680332213, "10": 3.2239736845799184e-07, "11": 3.968298588540451e-08, "12": 4.490691965843227e-09, "13": 4.701798271389202e-10, "14": 4.577016384820405e-11, "15": 4.121938957597451e-12, "16": 3.0496586774308946e-13, "2": 0.07808236505145752, "3": 0.03000809501174155, "4": 0.009225363860501498, "5": 0.002350942970635857, "6": 0.0005101126167828968, "7": 9.62083872591574e-05, "8": 1.6029586949284594e-05, "9": 2.390247064968074e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.09, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.86, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.48, "draw": 3.8, "home": 2.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.5, "draw": 3.83, "home": 2.82}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.75 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-11-05T13:34:50Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:34:50Z |
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
| Market best home last update utc | 2026-11-05T13:29:44Z |
| Market best draw last update utc | 2026-11-05T13:29:44Z |
| Market best away last update utc | 2026-11-05T13:29:44Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.11040221333691058,0.15949687571477206,0.10612567330216868,0.046169010665717145,0.015064056694711767,0.003932088659980655,0.0008553097362421283,0.00015946917234876194,2.6015855859613517e-05,3.7726539654557284e-06,4.923776568368571e-07,5.841938982526149e-08,6.353706289918243e-09,6.378743623301397e-10,5.946459645730327e-11],[0.08540981330029286,0.1244032959579821,0.09188618325743034,0.03997424980066204,0.013042825840166613,0.003404497780350599,0.0007405479251230587,0.00013807227919890753,2.2525159320393116e-05,3.266455352888229e-06,4.2631252363560797e-07,5.058092535240994e-08,5.501193088848795e-09,5.522871019663629e-10,5.148589061807398e-11],[0.03808060648178662,0.04969986635963203,0.0343793184129384,0.017305337758864753,0.005646397558920394,0.0014738483969572013,0.0003205921820868987,5.977316493964069e-05,9.751414774647942e-06,1.4140881551965081e-06,1.8455586406592242e-07,2.1897096299350253e-08,2.3815332358703634e-09,2.390917875145264e-10,2.2288866743084697e-11],[0.010990371059968676,0.014343783447473701,0.009360199144568595,0.004316541007321665,0.0016295960085172731,0.0004253645691395954,9.25254969808651e-05,1.725101889933294e-05,2.8143371819537675e-06,4.081172799742407e-07,5.326431521902755e-08,6.3196791149014105e-09,6.873297558005488e-10,6.900382386064738e-11,6.432747233945931e-12],[0.0023789324907463366,0.003104798946025934,0.0020260718899634453,0.0008814241812242096,0.0003048575861743523,9.20727415313841e-05,2.0027705142000847e-05,3.734087696782386e-06,6.091803566534343e-07,8.833946115814832e-08,1.1529384165511547e-08,1.3679328837485913e-09,1.4877669543719035e-10,1.493629629719701e-11,1.3924071640613207e-12],[0.00041194749583238895,0.0005376420540950963,0.0003508444416533186,0.00015263168905962202,4.980077294814282e-05,1.3779647760061518e-05,3.4680946233696375e-06,6.466127483194978e-07,1.0548862710893228e-07,1.5297289834342826e-08,1.9964841179591567e-09,2.3687789717404716e-10,2.5762894643698266e-11,2.5864415575368163e-12,2.411159823346588e-13],[5.944568974483468e-05,7.758392286602621e-05,5.0628271899263545e-05,2.2025370040749226e-05,7.186452952569429e-06,1.8758406671559213e-06,4.3253049630245664e-07,9.330883476785432e-08,1.5222435534060373e-08,2.2074607920402358e-09,2.881007328782957e-10,3.41824386002497e-11,3.717689893522927e-12,3.732339774558034e-13,3.479401142959981e-14],[7.352788675373788e-06,9.596291873961462e-06,6.262169483986788e-06,2.72429998039698e-06,8.888864796181527e-07,2.3202119570777017e-07,5.046935734769838e-08,9.974744305562758e-09,1.8828505832278987e-09,2.730390173402847e-10,3.5634943679974505e-11,4.227997833239287e-12,4.598380179451476e-13,4.6165004973135244e-14,4.303642775591101e-15],[7.957778578173073e-07,1.0385877967671187e-06,6.777422876229455e-07,2.9484562907580516e-07,9.620243554155211e-08,2.5111197702027424e-08,5.462199289105216e-09,1.0184058042699747e-09,1.7611766380432436e-10,2.9550475868742245e-11,3.856699872262943e-12,4.575878904095303e-13,4.976736433197484e-14,4.99634769685249e-15,4.657747937515306e-16],[7.655597557164472e-08,9.991494638515765e-08,6.520063546056157e-08,2.8364944507058197e-08,9.254933688972532e-09,2.4157649260611816e-09,5.254782992971831e-10,9.797338429038375e-11,1.5983411754359274e-11,2.4569652564366404e-12,3.710249265014243e-13,4.4021188848050116e-14,4.787754636091543e-15,4.806621200504629e-16,4.480879102383404e-17],[6.628402140543811e-09,8.650878517927176e-09,5.645229238142907e-09,2.45590572758149e-09,8.013146173960854e-10,2.0916278954565975e-10,4.5497186311878894e-11,8.482773360244817e-12,1.383882576045814e-12,2.0068185019233458e-13,2.7763878387663918e-14,3.8114613550529124e-15,4.1453541465967556e-16,4.161689275893536e-17,3.879653862677318e-18],[5.217301292966269e-10,6.809218680442441e-10,4.4434331500649696e-10,1.9330752504498688e-10,6.307251281332748e-11,1.6463474442235218e-11,3.5811425429269192e-12,6.676900930563356e-13,1.0892719240967715e-13,1.579592870624217e-14,2.0615626121973403e-15,2.592840975030679e-16,3.262862012634007e-17,3.27571960476463e-18,3.0537258731177857e-19],[3.76438838814047e-11,4.91298897526262e-11,3.206026873727482e-11,1.394752884217274e-11,4.550809345924159e-12,1.1878729737603888e-12,2.5838667632716845e-13,4.8175190429699973e-14,7.859317207011499e-15,1.1397081989847268e-15,1.4874591140140955e-16,1.7648334083428876e-17,2.034672462771213e-18,2.3634979370664815e-19,2.2033249704835535e-20],[2.5071529349776714e-12,3.27214236651263e-12,2.1352737436462425e-12,9.289314562361847e-13,3.0309239726971065e-13,7.911455741194582e-14,1.720903496444991e-14,3.208557609503057e-15,5.234451966900529e-16,7.590669350444419e-17,9.906755357945191e-18,1.1754119934630953e-18,1.2783807907699902e-19,1.3604698479419498e-20,1.4674555590121269e-21],[1.5505384651824777e-13,2.0236430462811952e-13,1.3205513022472138e-13,5.744938548892333e-14,1.8744625184791148e-14,4.8928074036377835e-15,1.064285719821372e-15,1.9843193137050242e-16,3.237225382464206e-17,4.6944183739834706e-18,6.12679228033747e-19,7.269287337342172e-20,7.906093647442038e-21,7.937248298503506e-22,7.843573450113076e-23]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2704136287973499, "-10": 5.454105116561621e-07, "-11": 6.416610744885876e-08, "-12": 6.9282822586276905e-09, "-13": 6.893602529482137e-10, "-14": 5.946459645730327e-11, "-2": 0.1521923750481567, "-3": 0.06078205221970386, "-4": 0.01880702244607407, "-5": 0.004735314457817901, "-6": 0.0010035533175220413, "-7": 0.0001834630782128866, "-8": 2.947333815361358e-05, "-9": 4.221566092558766e-06, "0": 0.2738204486329304, "1": 0.14540303110328232, "10": 7.34233195340675e-09, "11": 5.730527421783882e-10, "12": 4.1048081378142044e-11, "13": 2.709517239605791e-12, "14": 1.5505384651824777e-13, "2": 0.05461051754400416, "3": 0.014468954349437147, "4": 0.002970025781094373, "5": 0.0004960979015378022, "6": 6.974890689064558e-05, "7": 8.459097291122304e-06, "8": 9.015359719538418e-07, "9": 8.566545291862524e-08} |
| Raw goal margin distribution | {"-1": 0.24754293467844074, "-10": 4.992814868847299e-07, "-11": 5.8739149411312216e-08, "-12": 6.342310963426124e-09, "-13": 6.310564331554336e-10, "-14": 5.4435276735039777e-11, "-2": 0.13932044521075496, "-3": 0.055641306428084826, "-4": 0.01721638642833858, "-5": 0.004334817156689776, "-6": 0.0009186760831195421, "-7": 0.00016794637529158194, "-8": 2.6980580282745946e-05, "-9": 3.8645199361387985e-06, "0": 0.2900284120717044, "1": 0.1632558677685473, "10": 8.243836221314462e-09, "11": 6.434131530244728e-10, "12": 4.608803609370734e-11, "13": 3.0421964716229137e-12, "14": 1.7409162705973508e-13, "2": 0.06131569172449404, "3": 0.016245477691197423, "4": 0.003334690704233702, "5": 0.000557009663410524, "6": 7.831279880439098e-05, "7": 9.497719946565577e-06, "8": 1.0122281241946045e-06, "9": 9.618360599430509e-08} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.3, "price": 3.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.4, "price": 1.3, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.86, "draw": 3.59, "home": 4.6}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.89, "draw": 3.69, "home": 4.63}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.19, "under": 1.79}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.60 |
| Reference draw odds | 3.59 |
| Reference away odds | 1.86 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best under 2 5 last update utc | 2026-11-05T13:29:44Z |
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
| Market best home last update utc | 2026-11-05T13:29:44Z |
| Market best draw last update utc | 2026-11-05T13:29:44Z |
| Market best away last update utc | 2026-11-05T13:35:10Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.0737702690973297,0.06127620190023178,0.032530459816631246,0.011079802738368557,0.002830317249121629,0.0005783998809245926,9.850086074196778e-05,1.4378218085876432e-05,1.8364459919112547e-06,2.084964824223155e-07,2.1304032373701067e-08,1.9789380970352838e-09,1.685054858599294e-10,1.3244445271281497e-11,9.666490277470383e-13,6.58477046131225e-14],[0.10871642858581021,0.1255632967637035,0.05504847623909682,0.018749389378908674,0.004789500447138546,0.00097877596201378,0.00016668446504136496,2.4331011646391352e-05,3.1076583030168873e-06,3.528205172400378e-07,3.6050966587353926e-08,3.3487853361850057e-09,2.8514722161337036e-10,2.2412426228399367e-11,1.635776325801392e-12,1.114283604728313e-13],[0.09412531245350304,0.0961766203629504,0.053096408799333236,0.015863982887735776,0.004052428140389458,0.000828148842531399,0.00014103283299680015,2.0586630561625198e-05,2.629410331381119e-06,2.985237830856671e-07,3.0502962281612475e-08,2.8334295157206673e-09,2.41264958167038e-10,1.8963302696136293e-11,1.384041214156438e-12,9.428027590796879e-14],[0.05309336803415652,0.054250451532194995,0.02771637589042806,0.010200954723788321,0.0022858575773223107,0.00046713482417708467,7.955254449644237e-05,1.1612323236977501e-05,1.4831743640244945e-06,1.6838863711762542e-07,1.720583932562949e-08,1.5982556886736846e-09,1.3609058906482487e-10,1.069665091084227e-11,7.80697642772221e-13,5.318077843955472e-14],[0.02246132567105345,0.022950833687597517,0.011725504867118926,0.003993681050553064,0.0011023995274219622,0.00019762293873279392,3.3654968144910804e-05,4.9126319101755765e-06,6.274618403541445e-07,7.123737215485376e-08,7.2789874676655995e-09,6.761473769345091e-10,5.7573575663612526e-11,4.5252536916368135e-12,3.3027673048825043e-13,2.2498304933348976e-14],[0.007601870735743233,0.007767541129395628,0.003968411019748404,0.0013516320252288903,0.00034527216104876437,7.624602212425687e-05,1.1390276834055143e-05,1.6626441956438002e-06,2.123598523007415e-07,2.410976549675014e-08,2.4635198574943984e-09,2.2883711464956137e-10,1.9485353910047645e-11,1.5315388821685042e-12,1.1177973415127603e-13,7.614386095521664e-15],[0.0021439977738202903,0.002190722713973319,0.0011192329740545945,0.0003812082780478408,9.737902292524264e-05,1.9900248031203326e-05,3.6621225293125356e-06,4.68924765762544e-07,5.989302717827402e-08,6.799810908295812e-09,6.948001714098694e-10,6.454020088361181e-11,5.495562455280049e-12,4.3194840691637333e-13,3.152585850371324e-14,2.147527550165651e-15],[0.0005183002162724818,0.0005295957254760577,0.0002705687009544502,9.215510173081803e-05,2.35408680264734e-05,4.810780582141246e-06,8.192706184934999e-07,1.2922750876060074e-07,1.4478825173591356e-08,1.6438186211834703e-09,1.6796429712061702e-10,1.5602255041823233e-11,1.328523398620529e-12,1.0442126174617743e-13,7.621210936023962e-15,5.191535211898343e-16],[0.000109634313890053,0.00011202361523065247,5.723249375159294e-05,1.9493260918136903e-05,4.979521199161277e-06,1.0176083509897006e-06,1.7329757798440475e-07,2.5296330927921708e-08,3.4913483209417206e-09,3.477114634241205e-10,3.5528926854938583e-11,3.300292905431938e-12,2.8101811792042703e-13,2.2087880783474838e-14,1.6120892983442072e-15,1.098148106296179e-16],[2.0613849150699226e-05,2.1063094424948622e-05,1.0761065134195301e-05,3.6651950084229284e-06,9.362679912892904e-07,1.9133448550451212e-07,3.2584051507218564e-08,4.756309692759946e-09,6.074957146558837e-10,7.452917972391753e-11,6.680280221467956e-12,6.205332773270474e-13,5.283806580150149e-14,4.153045031009117e-15,3.031109917543716e-16,2.0647786815190977e-17],[3.4883029368937517e-06,3.564324818983475e-06,1.8210017370989217e-06,6.202291682015311e-07,1.5843651323233162e-07,3.237787580743042e-08,5.51391648098251e-09,8.048690445310624e-10,1.028012318365397e-10,1.1671290808989523e-11,1.2886783205136054e-12,1.0500746551096308e-13,8.941327685465814e-15,7.027837970876829e-16,5.129284467989265e-17,3.494045913562128e-18],[5.366320517022127e-07,5.48327073407065e-07,2.801384845327876e-07,9.541454887342033e-08,2.4373488397805555e-08,4.980933777435296e-09,8.482475196776221e-10,1.23819099009479e-10,1.581469183037225e-11,1.7954830317628446e-12,1.8346126606408663e-13,1.8415237876506404e-14,1.3755121351547524e-15,1.0811455247922519e-16,7.89076664962029e-18,5.375155372847961e-19],[7.567465721302313e-08,7.732386313690755e-08,3.950450540915215e-08,1.345514725821501e-08,3.4370950705215322e-09,7.024001921103106e-10,1.196179767492193e-10,1.746069368060643e-11,2.2301526332555477e-12,2.531950198081925e-13,2.587129929572512e-14,2.4031929213229116e-15,2.2112254394170217e-16,1.524607349235422e-17,1.1127383455085339e-18,7.579924438295187e-20],[9.850589246496702e-09,1.0065266798234314e-08,5.142311448813487e-09,1.7514599176670321e-09,4.4740753361535646e-10,9.143161044868688e-11,1.5570702251569272e-11,2.272862907358566e-12,2.9029953165632306e-13,3.2958459691045396e-14,3.3676735649819358e-15,3.1282422966782226e-16,2.663681036203463e-17,2.262374507931454e-18,1.4484543153694727e-19,9.866806789879779e-21],[1.1906641413561845e-09,1.216612727416558e-09,6.215634103274695e-10,2.1170312422989818e-10,5.407921227025807e-11,1.1051556127610925e-11,1.882067799474126e-12,2.747263431954445e-13,3.5089194559463157e-14,3.9837673794405045e-15,4.070587102231661e-16,3.781180835911044e-17,3.2196545957348577e-18,2.5306320959239867e-19,1.9958440713229802e-20,1.1926243943810465e-21],[1.3432384512577307e-10,1.3725121459474556e-10,7.012119065715466e-11,2.388312260694206e-11,6.100904093105552e-12,1.2467726725969463e-12,2.1232400878791607e-13,3.099303782956174e-14,3.958560077424445e-15,4.494256053462475e-16,4.5922010456143236e-17,4.265709626704197e-18,3.632228184711899e-19,2.854912833236292e-20,2.0836650067439046e-21,1.5337771776054782e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1346840155780426, "-10": 2.4905117210080534e-08, "-11": 2.283851817292496e-09, "-12": 1.9235513408092478e-10, "-13": 1.497450187299086e-11, "-14": 1.0780773882198696e-12, "-15": 6.58477046131225e-14, "-2": 0.05583479134545133, "-3": 0.01678213653542647, "-4": 0.003962390649662687, "-5": 0.0007672279176747384, "-6": 0.00012563718478305667, "-7": 1.7802302083714895e-05, "-8": 2.2214268642811367e-06, "-9": 2.475216082954082e-07, "0": 0.2638133698509239, "1": 0.23696912348512403, "10": 4.077941301612579e-06, "11": 6.193160303162568e-07, "12": 8.638537054419186e-08, "13": 1.1137323164570415e-08, "14": 1.32791535595093e-09, "15": 1.3432384512577307e-10, "2": 0.16155526884006383, "3": 0.08041841290091961, "4": 0.03144543137191826, "5": 0.010083624923458774, "6": 0.002734654727429752, "7": 0.0006417302175435082, "8": 0.0001326173550407158, "9": 2.4472226272887456e-05} |
| Raw goal margin distribution | {"-1": 0.15287930063692548, "-10": 4.16425844373379e-09, "-11": 3.0296535629124163e-10, "-12": 2.022856086701081e-11, "-13": 1.244853670491697e-12, "-14": 6.660891779935534e-14, "-2": 0.053885540779825714, "-3": 0.013351322863500516, "-4": 0.002559618336336021, "-5": 0.00039902582340429105, "-6": 5.233630711997738e-05, "-7": 5.919718451552518e-06, "-8": 5.882867836842855e-07, "-9": 5.2117326996013735e-08, "0": 0.28784705298529295, "1": 0.25503246389175815, "10": 6.463352828055961e-07, "11": 7.787627651491272e-08, "12": 8.61130980067654e-09, "13": 8.776362441821264e-10, "14": 7.777152995338301e-11, "2": 0.1477938231005603, "3": 0.0606457477206701, "4": 0.0192549895990715, "5": 0.004971198410866739, "6": 0.001079829502554621, "7": 0.00020227638530952532, "8": 3.3290877534812666e-05, "9": 4.884389666407128e-06} |
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
| Totals anchor reference last update utc | 2026-11-05T13:35:10Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3706 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.15, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.34, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.59, "draw": 3.78, "home": 1.82}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.53, "draw": 3.85, "home": 1.87}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.01, "under": 1.93}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 3.78 |
| Reference away odds | 4.59 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-11-05T13:35:10Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:35:10Z |
| Market best over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best under 2 5 last update utc | 2026-11-05T13:35:10Z |
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
| Market best home last update utc | 2026-11-05T13:35:10Z |
| Market best draw last update utc | 2026-11-05T13:29:44Z |
| Market best away last update utc | 2026-11-05T13:29:44Z |
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
| Bbs statistics cutoff utc | 2026-11-05T13:34:25.291682+00:00 |
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
| Score matrix json | [[0.08776270432396019,0.09598105319672127,0.05099388472572331,0.01749878163182645,0.0045035894045725245,0.0009272562148253253,0.00015909607698310317,2.3397658572885028e-05,3.0108795417218987e-06,3.44398966684647e-07,3.5454617811464375e-08,3.3181123843288004e-09,2.846563090629762e-10,2.2541791579699337e-11,1.6575680337452758e-12],[0.11608620488947569,0.12537332513907667,0.07144348523766093,0.024516154317613868,0.006309621729598471,0.0012991050995960934,0.00022289688829253782,3.278060269066962e-05,4.218304395681294e-06,4.825100622269028e-07,4.967265149231748e-08,4.64874395080384e-09,3.9880936554906347e-10,3.1581515364376586e-11,2.3222870347346246e-12],[0.08322563909455165,0.08567776072667707,0.04422266437925039,0.017173819159840634,0.004419955150684972,0.0009100365318740389,0.00015614157103249212,2.2963150552355417e-05,2.9549657713054525e-06,3.3800327914948445e-07,3.479620510081195e-08,3.2564931227467765e-09,2.793700771523373e-10,2.2123177503082423e-11,1.6267860389147986e-12],[0.038866946170947034,0.04001210384732315,0.020595500959188977,0.0070869260114167585,0.0020641494711083463,0.0004249933227639115,7.291918815393348e-05,1.072394932792025e-05,1.37998934967432e-06,1.5784985731838757e-07,1.625006723072466e-08,1.5208046977454096e-09,1.3046774850376665e-10,1.0331676133669984e-11,7.597202748340187e-13],[0.013613348492335468,0.014014445878752573,0.0072136805062716185,0.002475407014389211,0.0006388419390919696,0.00014885610472853268,2.5540321993697018e-05,3.756118599414211e-06,4.833483919781332e-07,5.528772720371103e-08,5.691669915685205e-09,5.326696944012752e-10,4.5697002269753526e-11,3.6187228885692398e-12,2.660959472483396e-13],[0.0038145164553689834,0.0039269055991240955,0.002021303062243642,0.0006936192660784168,0.00017851393561233223,3.685606063765976e-05,7.156503675435244e-06,1.0524799401006865e-06,1.354362151174475e-07,1.5491849438603946e-08,1.5948294105695912e-09,1.4925624769791288e-10,1.2804488713203001e-11,1.0139810946321864e-12,7.456118309593444e-14],[0.0008907027170472253,0.0009169459688146648,0.0004719812197905789,0.00016196248518544844,4.168361818360991e-05,8.582352995571757e-06,1.476596777228213e-06,2.4575768731208736e-07,3.162482222927885e-08,3.6174001471744354e-09,3.723981547442954e-10,3.4851847387808664e-11,2.9898921713125035e-12,2.3676807443108665e-13,1.741029279774869e-14],[0.00017827041351211828,0.0001835228902980806,9.446506181204272e-05,3.2416112194175977e-05,8.342801372502608e-06,1.7177219605881415e-06,2.9472202063242927e-07,4.346316407985164e-08,6.329575545419445e-09,7.2400746930852e-10,7.453392896060455e-11,6.975451097850951e-12,5.984143794952239e-13,4.738813717243876e-14,3.4845970906105957e-15],[3.1220066201487254e-05,3.213991975289202e-05,1.654343772136412e-05,5.676955299305552e-06,1.4610546193504208e-06,3.008204910102192e-07,5.1613954407275e-08,7.590669146079152e-09,9.794829230301948e-10,1.2679367639794427e-10,1.3052946647531295e-11,1.221593873990425e-12,1.0479886244552195e-13,8.298969809637691e-15,6.102490576596855e-16],[4.8599952518960625e-06,5.003187898042788e-06,2.5752997529530456e-06,8.837257301695552e-07,2.2744085380784979e-07,4.682841312851099e-08,8.034690629162943e-09,1.1816315753648605e-09,1.5205582751094873e-10,1.7440838192609486e-11,2.0319386359031076e-12,1.901642485004071e-13,1.631392997703132e-14,1.2918920033727085e-15,9.499683644357019e-17],[6.808953679475008e-07,7.009569532849377e-07,3.608048119343253e-07,1.2381179919336718e-07,3.18649331559268e-08,6.560757353640513e-09,1.1256767442630498e-09,1.6554902311325312e-10,2.13033353440493e-11,2.4367785485138384e-12,2.5154915115313283e-13,2.6642403797129023e-14,2.2856152688722976e-15,1.8099673670292444e-16,1.3309252900783827e-17],[8.672258792312204e-08,8.927774203372722e-08,4.595409001001249e-08,1.576935333520229e-08,4.058493562100917e-09,8.356142268355509e-10,1.4337239614603016e-10,2.1085236276174835e-11,2.713310237370443e-12,3.10361550203647e-13,3.195058989802264e-14,2.9984236108444406e-15,2.9110856152643256e-16,2.3052742244132558e-17,1.695139825019761e-18],[1.0125011334499534e-08,1.0423329972709508e-08,5.3652190664611555e-09,1.8410991309229748e-09,4.738361054641581e-10,9.755939854423148e-11,1.6738973902851832e-11,2.4617376095386403e-12,3.167836380960291e-13,3.623524492131697e-14,3.730286337259705e-15,3.4910852398898614e-16,3.003212066032578e-17,2.6914473161254294e-18,1.9791049082969702e-19],[1.0911807618594925e-09,1.1233308057621285e-09,5.782140518239268e-10,1.9841676082811831e-10,5.106570506199553e-11,1.0514056262566177e-11,1.8039729233510875e-12,2.6530347784616226e-13,3.4140032059463635e-14,3.90510201452158e-15,4.020160129180039e-16,3.762371147970415e-17,3.227686588810142e-18,2.563036545804486e-19,2.1328975645458804e-20],[1.0919762672220816e-10,1.1241497495257833e-10,5.786355881953767e-11,1.9856141293598474e-11,5.110293357961708e-12,1.052172134284598e-12,1.8052880767928013e-13,2.6549689249084535e-14,3.416492122497273e-15,3.9079489576703164e-16,4.023090953341361e-17,3.76511403579329e-18,3.2300396746414745e-19,2.5578523581509517e-20,1.8860544674570094e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.18681877188985055, "-10": 4.0393329611501466e-08, "-11": 3.7398046476557806e-09, "-12": 3.1786461046626753e-10, "-13": 2.4864078614433963e-11, "-14": 1.6575680337452758e-12, "-2": 0.080381612680795, "-3": 0.024795254329439586, "-4": 0.005970059244250156, "-5": 0.0011745531610351627, "-6": 0.00019499533926645057, "-7": 2.7970762029382315e-05, "-8": 3.529753342141016e-06, "-9": 3.9746227233228673e-07, "0": 0.2651228389105533, "1": 0.22502227234555355, "10": 7.757418561018755e-07, "11": 9.774398808894906e-08, "12": 1.13062056990812e-08, "13": 1.2035957368120708e-09, "14": 1.0919762672220816e-10, "2": 0.13118849687157247, "3": 0.05507330942198181, "4": 0.01804616045355951, "5": 0.004831838588774823, "6": 0.0010916854883519162, "7": 0.00021311360270063998, "8": 3.66003127954901e-05, "9": 5.608799512199131e-06} |
| Raw goal margin distribution | {"-1": 0.17082384309735016, "-10": 3.6934959639939397e-08, "-11": 3.4196124719338176e-09, "-12": 2.906498838163059e-10, "-13": 2.2735282011684163e-11, "-14": 1.515651445812064e-12, "-2": 0.0734995517505705, "-3": 0.022672350279812504, "-4": 0.00545891857282399, "-5": 0.0010739910280989685, "-6": 0.00017830035441623822, "-7": 2.5575979415161256e-05, "-8": 3.227545203250541e-06, "-9": 3.634326045459645e-07, "0": 0.2743515282148762, "1": 0.2334971441055323, "10": 8.049581318099771e-07, "11": 1.0142525819491734e-07, "12": 1.1732024185370909e-08, "13": 1.2489260030742272e-09, "14": 1.1331026798797408e-10, "2": 0.13612936639431736, "3": 0.057147500700399714, "4": 0.01872582160003063, "5": 0.0050138170746284365, "6": 0.0011328009495885916, "7": 0.0002211399657551444, "8": 3.7978767266168265e-05, "9": 5.82004018672367e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:35:10Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.12, "draw": 3.69, "home": 2.28}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.27, "draw": 3.77, "home": 2.25}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:29:44Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.16}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.28 |
| Reference draw odds | 3.69 |
| Reference away odds | 3.12 |
| Market reference 1x2 last update utc | 2026-11-05T13:35:10Z |
| Market reference home last update utc | 2026-11-05T13:35:10Z |
| Market reference draw last update utc | 2026-11-05T13:35:10Z |
| Market reference away last update utc | 2026-11-05T13:35:10Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.81 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best over 2 5 last update utc | 2026-11-05T13:29:44Z |
| Market best under 2 5 last update utc | 2026-11-05T13:29:44Z |
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
