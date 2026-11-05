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
| Training as of utc | 2026-11-05T13:33:35.017473+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 71, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-05T13:33:35.017473+00:00', 'observations': 409, 'observations_sha256': '8854068cc055d5834e5fc899e9c0017f55af39edc70799b735d70a84a86c9420', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 116, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'e16127c25c5c339405940fbf757bda96bd6dc7da54933740f733b123431bd62f', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694716449928761, 'audit_candidate_poisson_score': 0.6673753164537862, 'audit_gain': 0.00209632853908992, 'audit_gain_lower95': -0.006062801738558959, 'audit_baseline_briers': [0.5838692910520525, 0.13632337444950357, 0.27438171226499136, 0.23546961438971004], 'audit_candidate_briers': [0.5818232810954291, 0.13599221629469402, 0.27350506640901034, 0.2362671929723898], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1586.458 |
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
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261105T133335017473Z_fa8fcbae1c6e0ddf92a1747d9737c56d4d27e7764edf4b055035148335a9642f.json |
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
| Market best home last update utc | 2026-11-05T13:33:39Z |
| Market best draw last update utc | 2026-11-05T13:33:39Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
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
| Dc lambda home | 1.4420 |
| Dc lambda away | 1.3956 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Score matrix json | [[0.05785307780819588,0.0613560495318478,0.0520508060202116,0.025871266825960373,0.009644266319144073,0.002876144363869945,0.0007147775794170003,0.00015225949050458792,2.8379574257452782e-05,4.7019159046042995e-06,7.011103012353495e-07,9.503972122918379e-08,1.1809605724598897e-08,1.354576500144798e-09,1.4427364099035982e-10,1.43419176278079e-11],[0.06668391325951419,0.12142488904740449,0.08019479123161086,0.039859917658135,0.014858942313890237,0.004431281942549769,0.0011012593875323327,0.00023458653165342902,4.372447243054568e-05,7.24425216800513e-06,1.0802021820001797e-06,1.46427907374294e-07,1.8195085494816222e-08,2.0869989908355424e-09,2.222827157557097e-10,2.2096624009557235e-11],[0.058193665581935984,0.08677351793167401,0.06465505139485332,0.030706131369628503,0.011446602539855657,0.003413642913936773,0.0008483563793489939,0.00018071399244412638,3.368319538527754e-05,5.580617618262524e-06,8.321349379277369e-07,1.1280089935402137e-07,1.4016604105337982e-08,1.6077219659734912e-09,1.7123573434677205e-10,1.702215858753227e-11],[0.029886369486339815,0.0445640499288388,0.033225088563663754,0.016504035331560606,0.005878601896760273,0.001753135713313938,0.00043568817938816653,9.280881510947958e-05,1.7298591052794286e-05,2.8660232764774203e-06,4.273573759051979e-07,5.793086451547018e-08,7.198470916839989e-09,8.256735887986988e-10,8.794109074890324e-11,8.742025715595715e-12],[0.011511498787824455,0.017164982416845685,0.012797491742876012,0.006360849118348082,0.0023697381209410694,0.0006752650116277724,0.00016781643388263424,3.574768635315569e-05,6.662994313388588e-06,1.1039220902400434e-06,1.6460761207376144e-07,2.2313552569584096e-08,2.772674990559438e-09,3.1802927822796363e-10,3.3872757948022695e-11,3.367214558269015e-12],[0.0035471582964308177,0.005289225226901164,0.003943424730866573,0.0019600348432784053,0.0007306599305918234,0.00021776623324997398,5.171102970134782e-05,1.1015307785978338e-05,2.0531379964879783e-06,3.40163038122359e-07,5.072226193870425e-08,6.875707896851879e-09,8.543732903374503e-10,9.799768158490372e-11,1.0437566523084266e-11,1.0375749740650289e-12],[0.0009108524305313263,0.0013581868219408608,0.0010126071916049925,0.0005033049984610525,0.00018762156014888538,5.595310984844251e-05,1.38969095609772e-05,2.8285514858484394e-06,5.272123705894405e-07,8.734832340649498e-08,1.3024650074230604e-08,1.7655697113299417e-09,2.1938913435804454e-10,2.516420723255012e-11,2.6801969469334986e-12,2.6643234048408687e-13],[0.00020047890593910718,0.00029893734593734744,0.00022287516079923212,0.00011077758818329855,4.129556429606881e-05,1.2315297045167895e-05,3.060589837674952e-06,6.51556893558417e-07,1.1603960829492354e-07,1.9225393406409936e-08,2.866729570670733e-09,3.886024477973642e-10,4.828761735352903e-11,5.538649912657955e-12,5.899121895180401e-13,5.864184179196567e-14],[3.860978637363828e-05,5.7571678235560055e-05,4.292303125927042e-05,2.1334409197360376e-05,7.953020833694807e-06,2.371775652976954e-06,5.894321861764866e-07,1.2555884087388142e-07,2.338851040985565e-08,3.702575734307438e-09,5.52097068747011e-10,7.484008067305783e-11,9.299604772773569e-12,1.0666762616464343e-12,1.1360987586102834e-13,1.129370181635066e-14],[6.6095758579686925e-06,9.855645687496242e-06,7.347956510731021e-06,3.6522190154146286e-06,1.3614707419412695e-06,4.060222179094429e-07,1.0090438496499493e-07,2.149430912058001e-08,4.006314087736714e-09,6.633576423896289e-10,9.451301857855007e-11,1.2811808530565027e-11,1.5919912791007367e-12,1.8260338451549442e-13,1.9448776158745498e-14,1.9333590232815988e-15],[1.0183388050772377e-06,1.5184614971275963e-06,1.1321012745282247e-06,5.626981863826754e-07,2.0976209643233965e-07,6.25559323480981e-08,1.554636076813044e-08,3.3116329301861087e-09,6.172536919976801e-10,1.0226633159648074e-10,1.523975305585724e-11,1.9739181560590466e-12,2.4527844625586364e-13,2.8133743584526506e-14,2.996477217192924e-15,2.978730496269621e-16],[1.4263243955164978e-07,2.1268154235184272e-07,1.5856644743420666e-07,7.881366658610492e-08,2.938008390767723e-08,8.761823859359312e-09,2.1774829275413105e-09,4.638400121619611e-10,8.645491998629489e-11,1.4323814713608668e-11,2.1358472274809142e-12,2.8934951072194215e-13,3.435464011042825e-14,3.940520052044206e-15,4.1969809401179487e-16,4.172124201999823e-17],[1.831284275767406e-08,2.730657664407761e-08,2.0358639504683622e-08,1.0119032443699063e-08,3.772163320628978e-09,1.1249467730570554e-09,2.7957106100778724e-10,5.955327717972392e-11,1.110010710265523e-11,1.8390610674886942e-12,2.74225376458687e-13,3.717290030781186e-14,4.6162620370533736e-15,5.059306587153754e-16,5.388581465403818e-17,5.356667439530266e-18],[2.1703566987973548e-09,3.236254049954207e-09,2.412815432976645e-09,1.199262732724924e-09,4.470600244986001e-10,1.3332368966427754e-10,3.313351908697335e-11,7.05798961814304e-12,1.3155353391280764e-12,2.1795734065640264e-13,3.2499972322862384e-14,4.405566861702952e-15,5.474343459468626e-16,6.275292032755556e-17,6.3863071589764806e-18,6.348484074512312e-19],[2.38848095414695e-10,3.561502662387146e-10,2.655307171733539e-10,1.3197905200186425e-10,4.919902587750045e-11,1.4672292977287147e-11,3.646348976965533e-12,7.76732865470588e-13,1.4477487058951125e-13,2.3986239555129613e-14,3.576627056118193e-15,4.848333247354814e-16,6.024523571007982e-17,6.910203646221225e-18,7.355429934068297e-19,6.986516690127563e-20],[2.4532919036081156e-11,3.658143319561747e-11,2.7273583968489415e-11,1.3556027698688007e-11,5.053403153209823e-12,1.5070422691061648e-12,3.745291921791438e-13,7.978093552794927e-14,1.487033075338095e-14,2.463710133272589e-15,3.673678110669433e-16,4.979891793182711e-17,6.1879978042901375e-18,7.097710629898037e-19,7.559650969597565e-20,7.510273235686851e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.17886549846136823, "-10": 8.624153966367022e-07, "-11": 1.1493383699528068e-07, "-12": 1.4076582475496806e-08, "-13": 1.59388137448804e-09, "-14": 1.6637026499991706e-10, "-15": 1.43419176278079e-11, "-2": 0.10528984067610694, "-3": 0.04461743134903879, "-4": 0.015023730036241594, "-5": 0.004176572794195129, "-6": 0.0009860850380954823, "-7": 0.00020201513162057435, "-8": 3.651676563941205e-05, "-9": 5.9024461901524325e-06, "0": 0.2630391304700617, "1": 0.19383317217307286, "10": 1.2526289557346357e-06, "11": 1.7248886408385908e-07, "12": 2.182818355250031e-08, "13": 2.553780549004559e-09, "14": 2.754295286103125e-10, "15": 2.4532919036081156e-11, "2": 0.11771579051247474, "3": 0.05154185327680705, "4": 0.017932483859087984, "5": 0.005150980953418655, "6": 0.0012565838374399396, "7": 0.00026599177782758395, "8": 4.968025621538906e-05, "9": 8.29718494182086e-06} |
| Raw goal margin distribution | {"-1": 0.1874204990456011, "-10": 5.423240536584432e-07, "-11": 6.778270776683943e-08, "-12": 7.78030854944411e-09, "-13": 8.193326925216081e-10, "-14": 7.140917937577266e-11, "-2": 0.10632333996974871, "-3": 0.04288921969623673, "-4": 0.013670968294729913, "-5": 0.0035858451636622164, "-6": 0.0007971418407427168, "-7": 0.00015355195753129883, "-8": 2.607333211882914e-05, "-9": 3.956103210394642e-06, "0": 0.269335006493095, "1": 0.19396124955410118, "10": 7.521959314472004e-07, "11": 9.714003109893937e-08, "12": 1.1520819063340018e-08, "13": 1.2535857046723476e-09, "14": 1.128898771358357e-10, "2": 0.11351232871968611, "3": 0.04731183350613406, "4": 0.015582176570517269, "5": 0.004223063282077448, "6": 0.0009700159444133254, "7": 0.00019306601670350765, "8": 3.387304405958304e-05, "9": 5.310464561450242e-06} |
| Research history json | {"away": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 3.0, "away_xg": 2.6, "date": "2026-10-23T00:00:00+00:00", "home": "Stuttgart", "home_goals": 2.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-18T00:00:00+00:00", "home": "M'gladbach", "home_goals": 1.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-11T00:00:00+00:00", "home": "FC Koln", "home_goals": 2.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Mainz", "away_goals": 4.0, "away_xg": 2.82, "date": "2026-09-19T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 3.24, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-09-12T00:00:00+00:00", "home": "Freiburg", "home_goals": 5.0, "home_xg": 2.6, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": 3.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 0.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "M'gladbach", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.5% |
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
| Totals anchor scale | 1.0685 |
| Totals anchor target over 2 5 | 0.5824 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.29 |
| Totals anchor reference last update utc | 2026-11-05T13:34:00Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5417 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.36, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.57, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.62, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:21:18Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.18, "under": 4.6}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.82, "draw": 3.86, "home": 2.49}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.6, "home_away": 1.3, "home_draw": 1.49}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:33:59Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.58, "home_away": 1.31, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.8, "draw": 3.7, "home": 2.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.48 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:39Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:39Z |
| Market best over 2 5 last update utc | 2026-11-05T13:33:39Z |
| Market best under 2 5 last update utc | 2026-11-05T13:33:39Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0171 |
| Raw ev home | -0.0643 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0396 |
| Raw edge prob away | 0.0081 |
| Raw ev away | 0.0007 |
| Market p home draw | 65.0% |
| Market home draw odds | 1.49 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-05T13:33:39Z |
| Market reference home draw last update utc | 2026-11-05T13:34:06Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.5% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-05T13:33:39Z |
| Market reference draw away last update utc | 2026-11-05T13:34:06Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-05T13:33:59Z |
| Market reference home away last update utc | 2026-11-05T13:34:06Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home draw odds | 1.49 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.3% |
| Market over 1 5 odds | 1.18 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-11-05T13:21:18Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-11-05T13:33:41Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 64.2% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-05T13:34:00Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market reference under 3 5 last update utc | 2026-11-05T13:34:00Z |
| Market under 3 5 bookmakers | 2 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 9.857583967086907, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---

## 2026-11-07 — Borussia Dortmund vs Elversberg

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **73.9%**. Expected goals are 2.88 for Borussia Dortmund and 1.29 for Elversberg (4.18 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.4%; Under 3.5 goals: 39.3%; Double Chance 1X: 88.6%; Double Chance X2: 26.1%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 58.7%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

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
| Elversberg expected goals | 1.29 |
| Expected total goals | 4.18 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.7% |
| Under 1.5 | 7.3% |
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 41.3% |
| Under 4.5 | 58.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.76% |
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
| Market best home last update utc | 2026-11-05T13:33:39Z |
| Market best draw last update utc | 2026-11-05T13:33:39Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8823 |
| Dc lambda away | 1.2947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Fair Under 0.5 odds | 55.75 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.79 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.85 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.42 |
| Fair Under 4.5 odds | 1.70 |
| Score matrix json | [[0.017936657520163407,0.01243035369939804,0.01040538432910156,0.004490715124285247,0.001453563969118585,0.0003763940760158662,8.122134254707363e-05,1.5022795610488227e-05,2.4313047933890137e-06,3.49764341937318e-07,4.528497854367694e-08,5.330158405156324e-09,5.750922360918315e-10,5.7276014050364515e-11,5.29691966100772e-12,4.572047794003043e-13,3.6997247401151324e-14,2.817728385609289e-15,2.0267736838888615e-16,1.3811164258621748e-17],[0.04215102603423533,0.05581851246885416,0.02999107941281017,0.0129434329048349,0.0041895571610471305,0.0010848676288420995,0.00023410146682728713,4.32996842698525e-05,7.007665726612511e-06,1.0081136672168574e-06,1.3052332761149315e-07,1.5362931243665423e-08,1.6575684642500774e-09,1.650846745784768e-10,1.5267128360868014e-11,1.3177855246116442e-12,1.066358867456768e-13,8.12144108316989e-15,5.841699699193434e-16,3.98074411249983e-17],[0.06763100586330367,0.08756377601110257,0.04827868333657222,0.01865320452593033,0.006037707861018576,0.0015634382248617903,0.00033737128107015,6.240059129074377e-05,1.0098976292373551e-05,1.4528255802181698e-06,1.8810143670870656e-07,2.2140022721395004e-08,2.388776131240997e-09,2.3790892428999374e-10,2.2001958053378977e-11,1.8991038229671992e-12,1.5367646434262757e-13,1.1704074389188754e-14,8.418664512674797e-16,5.736780546690639e-17],[0.06497683646154195,0.08412734782221638,0.05446102824495853,0.020018222577100737,0.005800758857274914,0.001502081309568233,0.0003241311921520669,5.9951688780104115e-05,9.702643374916844e-06,1.3958096427514754e-06,1.8071942203412432e-07,2.127114061456654e-08,2.2950289448097702e-09,2.2857222170519355e-10,2.1138494275209605e-11,1.8245737580458496e-12,1.4764545291196005e-13,1.1244749620568344e-14,8.088275196886688e-16,5.51164139346817e-17],[0.04682012217610091,0.060619336334092055,0.03924278458484573,0.016936247684899385,0.004668938322082736,0.001082349253399669,0.00023355803150907785,4.31991698304581e-05,6.991398365687105e-06,1.0057734658547729e-06,1.3022033512265657e-07,1.532726824871636e-08,1.6537206402358516e-09,1.6470145253430558e-10,1.5231687759528034e-11,1.3147264613532865e-12,1.0638834576342006e-13,8.102588241369429e-15,5.828138972821494e-16,3.971503346208168e-17],[0.026989603802979562,0.03494420335562137,0.02262162418301625,0.009762952202587157,0.0031600925823960626,0.0006969325264383572,0.00013463524746314066,2.4902294657762213e-05,4.0302131465819235e-06,5.797812157958476e-07,7.506591372898491e-08,8.835451045149176e-09,9.532923624782454e-10,9.494266018693121e-11,8.780353377424491e-12,7.578781227386699e-13,6.132788997451157e-14,4.670761976884989e-15,3.359648682536948e-16,2.2893853504525928e-17],[0.012965200281159538,0.016786411481934466,0.010866920846965122,0.004689903251857157,0.0015180375946551878,0.0003930892412970736,7.224384278566116e-05,1.1962503786835626e-05,1.9360239965963607e-06,2.7851389138278097e-07,3.6059981201987484e-08,4.244352499983461e-09,4.5794026826973005e-10,4.56083243583495e-11,4.217884816267539e-12,3.640676507052431e-13,2.946054273878148e-14,2.2437292869505998e-15,1.6138998690531575e-16,1.0997693706824129e-17],[0.005338449772554548,0.006911841900966422,0.004474478593913469,0.0019310779938017683,0.000625055323186374,0.0001618553609114263,3.4926452219489866e-05,5.501959187718614e-06,7.971621448307971e-07,1.1467870822375876e-07,1.4847776684623252e-08,1.7476214903601634e-09,1.8855791410647377e-10,1.877932801016859e-11,1.7367233632931535e-12,1.499056570630973e-13,1.213044336165981e-14,9.23860475877212e-16,6.645268258132994e-17,4.528324606997054e-18],[0.0019233536456481602,0.002490220360733315,0.001612079364354493,0.0006957349151254217,0.0002251969177949247,5.831376368419499e-05,1.2583413175725573e-05,2.327442988420053e-06,3.208115505651837e-07,4.1316809361838804e-08,5.3494041590419545e-09,6.296386231782131e-10,6.793424439000719e-11,6.7658759621328424e-12,6.257122113324312e-13,5.400848641451649e-14,4.370394675796027e-15,3.3285138758520045e-16,2.3941783617220485e-17,1.6314791770305189e-18],[0.0006159572999381793,0.0007974973365501205,0.0005162711781063142,0.00022281029844043913,7.211969871126681e-05,1.867508271784587e-05,4.029859626316636e-06,7.453676042110008e-07,1.2063106467945853e-07,1.4780107171954827e-08,1.713155846059267e-09,2.0164284771402405e-10,2.1756058144838892e-11,2.1667833675733383e-12,2.003854075940308e-13,1.729631029681109e-14,1.3996263818972997e-15,1.0659622708571887e-16,7.66739721836104e-18,5.224840013498547e-19],[0.00017753524245789286,0.00022985989940887063,0.00014880305629680105,6.421984179700271e-05,2.078681135523517e-05,5.382654509601121e-06,1.1615125040342945e-06,2.1483472693178568e-07,3.4769074606260645e-08,5.001833802366255e-09,5.515567309842477e-10,5.811882067539774e-11,6.27067340229533e-12,6.245244768662872e-13,5.775639305809103e-14,4.9852557027565025e-15,4.0340947186686396e-16,3.0723861901886824e-17,2.209947384858205e-18,1.505937568551039e-19],[4.65185172557582e-05,6.022883991382418e-05,3.8989991205233826e-05,1.682714810556262e-05,5.446646138160654e-06,1.4103853590987812e-06,3.0434430208702536e-07,5.6291882183801684e-08,9.110336486693286e-09,1.310601145014883e-09,1.6968723684804254e-10,1.7010513515223125e-11,1.6430677359121197e-12,1.6364048203352172e-13,1.513356857999837e-14,1.3062572829056634e-15,1.0570301545973817e-16,8.050393151576275e-18,5.790595384531983e-19,3.9459197959160805e-20],[1.1173226131924532e-05,1.446629187084289e-05,9.364958608260476e-06,4.041692255691228e-06,1.308223317343793e-06,3.387587455491313e-07,7.310008808933309e-08,1.3520678777727278e-08,2.188200650164679e-09,3.147916964227374e-10,4.0756971220313985e-11,4.797200301401136e-12,4.4082634167521657e-13,3.9304608529227095e-14,3.634913447426772e-15,3.1374834946123894e-16,2.538867883652883e-17,1.9336141485103804e-18,1.390836068874178e-19,9.477656808321947e-21],[2.4772464067372826e-06,3.2073609835448345e-06,2.076330487509849e-06,8.960946014456466e-07,2.9004975589280665e-07,7.510712441097521e-08,1.6207219688686985e-08,2.9977065283833777e-09,4.851519278171941e-10,6.979332465185149e-11,9.036339130068865e-12,1.0636003486128351e-12,1.1475612098133653e-13,9.734047005375027e-15,8.059065636119912e-16,6.956200135445868e-17,5.6289931553336196e-18,4.287068609242092e-19,3.083660541098979e-20,2.101317112487424e-21],[5.100058321438221e-07,6.603189747090379e-07,4.274668257497856e-07,1.8448446292906092e-07,5.971431292216678e-08,1.5462761952534065e-08,3.3366792021925608e-09,6.171561328631571e-10,9.988118743039037e-11,1.4368777575111192e-11,1.8603662699966946e-12,2.1896989309883994e-13,2.3625542786342003e-14,2.3529737243086957e-15,1.8533181268403308e-16,1.432115363650734e-17,1.1588751649856601e-18,8.82604971216352e-20,6.3485200989093205e-21,4.3261097468446405e-22],[9.799814486456598e-08,1.2688096971038107e-07,8.21381899468365e-08,3.544887917729817e-08,1.1474166606362032e-08,2.971185602841127e-09,6.411463383635188e-10,1.1858718528403717e-10,1.9192272829319314e-11,2.7609753802489545e-12,3.574712909888373e-13,4.2075290030854563e-14,4.539672330309823e-15,4.521263196698016e-16,4.1812909498418424e-17,3.0738315302116796e-18,2.2267905412145627e-19,1.69593452419687e-20,1.21987466243931e-21,8.312664345213555e-23],[1.7653541498230282e-08,2.285653944994025e-08,1.4796504023825648e-08,6.385817409983032e-09,2.066974600620848e-09,5.352340945962711e-10,1.1549711993406625e-10,2.1362483947663304e-11,3.4573265168027986e-12,4.973664911532499e-13,6.439544624664811e-14,7.579509588026277e-15,8.177837854201013e-16,8.14467534846056e-17,7.532243942088891e-18,6.501472837662151e-19,4.480770511641395e-20,3.0550833939323126e-21,2.1975015961550763e-22,1.4974565608552418e-23],[2.9930701273910395e-09,3.875212543047468e-09,2.508673638542924e-09,1.0826835697930568e-09,3.5044525948600583e-10,9.074627772891259e-11,1.9581962039118803e-11,3.621902866177384e-12,5.86172509301702e-13,8.432601397205909e-14,1.091792751727349e-14,1.2850681394704642e-15,1.3865117200710366e-16,1.3808891822198562e-17,1.27705448436782e-18,1.1022923721227034e-19,8.919806930565625e-21,5.785853920576069e-22,3.725754621533159e-23,2.538863094303686e-24],[4.792679178800021e-10,6.20521727791171e-10,4.017035151905863e-10,1.733656339919808e-10,5.611534735110862e-11,1.4530825450590662e-11,3.13557844455663e-12,5.799602988084814e-13,9.386137514138485e-14,1.3502775217210479e-14,1.748242495517318e-15,2.0577263656524823e-16,2.22016376801e-17,2.2111606311156245e-18,2.0448944317779476e-19,1.765055102610484e-20,1.4282917250689869e-21,1.0877939358625101e-22,6.664001099456559e-24,4.065376276532311e-25],[7.270407082443727e-11,9.413201669118841e-11,6.093769211181414e-11,2.629925113291705e-11,8.512596057335915e-12,2.204299773225777e-12,4.756615429570698e-13,8.797892174057624e-14,1.4238599771384908e-14,2.0483464239814272e-15,2.652052045849772e-16,3.121533443913258e-17,3.367948026758244e-18,3.354290431956026e-19,3.102067633780265e-20,2.677556464802994e-21,2.166692550519794e-22,1.6501636017110354e-23,1.1869519358715586e-24,6.888750632081631e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.06810518375197516, "-10": 6.328127811503831e-08, "-11": 7.248152654136381e-09, "-12": 7.641146675077849e-10, "-13": 7.459834123791502e-11, "-14": 6.7802321073333476e-12, "-15": 5.763932830883207e-13, "-16": 4.601567134952338e-14, "-17": 3.4592661609955387e-15, "-18": 2.4248480951388445e-16, "-19": 1.3811164258621748e-17, "-2": 0.031149122990879952, "-3": 0.010615365099026, "-4": 0.0029433636251552306, "-5": 0.000683684056770166, "-6": 0.00013615534590123533, "-7": 2.3680334300451376e-05, "-8": 3.6505440734992803e-06, "-9": 5.04896579559691e-07, "0": 0.14749602871386072, "1": 0.20470263950159695, "10": 0.0002480879402948807, "11": 6.325765365390189e-05, "12": 1.4845663764832165e-05, "13": 3.2264548405496202e-06, "14": 6.528243090949463e-07, "15": 1.2354523618309847e-07, "16": 2.1956756807601252e-08, "17": 3.6745295472940246e-09, "18": 5.733999345711905e-10, "19": 7.270407082443727e-11, "2": 0.20245734833081988, "3": 0.15359532344611934, "4": 0.09480741643728541, "5": 0.049024049512040535, "6": 0.02173420524213771, "7": 0.008414963402151478, "8": 0.002887867975852218, "9": 0.0008891550584345831} |
| Raw goal margin distribution | {"-1": 0.0841790465293226, "-10": 7.821662554028897e-08, "-11": 8.958827300814451e-09, "-12": 9.444573908518418e-10, "-13": 9.220468827961448e-11, "-14": 8.380470363627322e-12, "-15": 7.124308947316157e-13, "-16": 5.68760720728135e-14, "-17": 4.2757057698314995e-15, "-18": 2.9971492532873796e-16, "-19": 1.707080980773244e-17, "-2": 0.03850079141032831, "-3": 0.013120753272627966, "-4": 0.0036380423618998328, "-5": 0.000845043928459304, "-6": 0.0001682900855179575, "-7": 2.9269254601340076e-05, "-8": 4.512128188943131e-06, "-9": 6.240598779974433e-07, "0": 0.16320926734557142, "1": 0.19291687914712888, "10": 0.0002338042699999198, "11": 5.961559242613247e-05, "12": 1.3990924246761822e-05, "13": 3.0406916103449866e-06, "14": 6.152379307302247e-07, "15": 1.1643211565795351e-07, "16": 2.069259590315085e-08, "17": 3.4629684029665158e-09, "18": 5.403864168531105e-10, "19": 6.851813185649149e-11, "2": 0.19080086068006105, "3": 0.14475206828287143, "4": 0.08934887671021273, "5": 0.046201488451952315, "6": 0.02048285775046719, "7": 0.007930471642343942, "8": 0.0027215988941168487, "9": 0.0008379619303821659} |
| Research history json | {"away": [{"away": "Mainz", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-30T00:00:00+00:00", "home": "Elversberg", "home_goals": 4.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 0.8, "date": "2026-10-24T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 4.0, "home_xg": 2.87, "source": "pipeline training history"}, {"away": "Augsburg", "away_goals": 3.0, "away_xg": 3.92, "date": "2026-10-17T00:00:00+00:00", "home": "Elversberg", "home_goals": 4.0, "home_xg": 3.78, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 0.24, "date": "2026-10-10T00:00:00+00:00", "home": "Union Berlin", "home_goals": 1.0, "home_xg": 1.13, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 0.0, "away_xg": 1.01, "date": "2026-09-20T00:00:00+00:00", "home": "Schalke 04", "home_goals": 0.0, "home_xg": 1.01, "source": "pipeline training history"}, {"away": "Bayern Munich", "away_goals": 2.0, "away_xg": 2.83, "date": "2026-09-13T00:00:00+00:00", "home": "Elversberg", "home_goals": 1.0, "home_xg": 0.93, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "Leverkusen", "away_goals": 2.0, "away_xg": 1.88, "date": "2026-08-29T00:00:00+00:00", "home": "Elversberg", "home_goals": 3.0, "home_xg": 1.27, "source": "pipeline training history"}, {"away": "Heidenheim", "away_goals": 2.0, "away_xg": null, "date": "2025-05-26T00:00:00+00:00", "home": "Elversberg", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 2.0, "away_xg": null, "date": "2025-05-22T00:00:00+00:00", "home": "Heidenheim", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 69.6% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.0% |
| Raw p btts yes | 69.0% |
| P home draw | 88.6% |
| P draw away | 26.1% |
| P home away | 85.3% |
| Raw p home draw | 86.0% |
| Raw p draw away | 30.4% |
| Raw p home away | 83.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7936 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.86, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.59, "draw": 6.35, "home": 1.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.75, "draw": 6.45, "home": 1.32}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.35 |
| Reference away odds | 8.59 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:40Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +7.7% |
| Under 2.5 probability edge | -7.7% |
| Raw edge prob home | -0.0608 |
| Raw ev home | -0.0809 |
| Raw edge prob draw | 0.0224 |
| Raw ev draw | 0.0527 |
| Raw edge prob away | 0.0383 |
| Raw ev away | 0.3697 |
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
| Market best home last update utc | 2026-11-05T13:33:39Z |
| Market best draw last update utc | 2026-11-05T13:34:00Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
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
| Dc lambda away | 2.6993 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Fair Under 1.5 odds | 10.78 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.08 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.80 |
| Fair Under 4.5 odds | 1.55 |
| Score matrix json | [[0.021643265788935627,0.05272666043483405,0.07847750792301185,0.07061242301558487,0.04765168787937993,0.0257255962708169,0.011573677186494933,0.004463037031525772,0.0015059053247149005,0.00045166072260478265,0.00012191846625168538,2.991809734657024e-05,6.72991982534016e-06,1.3974095395021825e-06,2.694342697877842e-07,4.848626603131828e-08,8.180049333709384e-09,1.2988654571842246e-09,1.9478200300184368e-10,2.7672754617624295e-11],[0.018422501723659612,0.059673132902932094,0.09300905354021052,0.0836876043426797,0.056475269240233446,0.030489160833872975,0.013716755151703439,0.005289449948185762,0.0017847512322932192,0.0005352939643798283,0.0001444938996567994,3.545798014710439e-05,7.976087543076054e-06,1.6561654685144247e-06,3.1932495166441544e-07,5.746438479794554e-08,9.69473504672089e-09,1.539374147396361e-09,2.3084945260545984e-10,3.279687115397059e-11],[0.013858638091124939,0.0374091395564102,0.04424666880574342,0.049591947291421606,0.033466349018216164,0.018067393240721482,0.00812833159504959,0.0031344441639998524,0.001057615279292281,0.00031720671508578816,8.562479368354339e-05,2.1011836774716896e-05,4.726503000472035e-06,9.814173946732673e-07,1.892269027911616e-07,3.405248321321985e-08,5.744946258380199e-09,9.122087097494392e-10,1.367977250129624e-10,1.943490578283622e-11],[0.005474939450066621,0.014778708600638027,0.0199463601282307,0.015728063621869282,0.01322108516614399,0.007137633825421849,0.0032111469410157313,0.0012382812722776637,0.0004178173625371378,0.00012531444625582636,3.382659665108507e-05,8.300854190710753e-06,1.8672338196575325e-06,3.877149237715694e-07,7.475524133707694e-08,1.3452641052527499e-08,2.269576036382753e-09,3.6037361094665674e-10,5.404277508570384e-11,7.677877990545086e-12],[0.0016221811507451662,0.004378814184697287,0.005909948360359868,0.005317648134690886,0.003144795879177464,0.0021148243114139918,0.0009514373788965528,0.00036689292320577643,0.00012379597183555282,3.7129676864242955e-05,1.0022552391987104e-05,2.459477283002856e-06,5.532465763151938e-07,1.14876857897887e-07,2.2149385307802167e-08,3.985910883979762e-09,6.724573851420819e-10,1.067758436847233e-10,1.6012445777262887e-11,2.2748943741892627e-12],[0.00038451153074226506,0.001037926340236705,0.0014008566735015018,0.0012604615848726202,0.0008506027616846132,0.000402429343500478,0.00022552268148157804,8.696597137474645e-05,2.934381194624825e-05,8.800983096417763e-06,2.375682247582049e-06,5.829788950998716e-07,1.3113805929698597e-07,2.722968175094844e-08,5.250149803424242e-09,9.447950339561547e-10,1.5939503328660116e-10,2.5309468725271532e-11,3.79548858271137e-12,5.39226533173972e-13],[7.595181196103552e-05,0.00020501956357689747,0.0002767084837345625,0.00024897651598002144,0.0001680179028293207,9.070740044712755e-05,3.576220814311909e-05,1.7178218536418786e-05,5.79622588393929e-06,1.7384410083125203e-06,4.692638761683006e-07,1.15154682962049e-07,2.5903444823702897e-08,5.3786258740134796e-09,1.03705184046673e-09,1.866235184735134e-10,3.1484989727971796e-11,4.9993299440063735e-12,7.497154495675686e-13,1.0651236433136397e-13],[1.285938268378043e-05,3.471181210330445e-05,4.6849445619767925e-05,4.2154152950346775e-05,2.844706998322693e-05,1.5357647756961112e-05,6.9092453917034785e-06,2.3348846692803756e-06,9.813575850099128e-07,2.94335021401944e-07,7.945095195909342e-08,1.9496811172827337e-08,4.3857058997759475e-09,9.10653829592709e-10,1.7558299315257935e-10,3.159718221173766e-11,5.3307159006896875e-12,8.464353285665054e-13,1.2693413917337185e-13,1.8033582321826944e-14],[1.9050665664981573e-06,5.142417356004125e-06,6.94055964457503e-06,6.24497064902237e-06,4.214320646062847e-06,2.2751746332850326e-06,1.0235773146457293e-06,3.947114980210613e-07,1.1671391760041242e-07,4.360456659631184e-08,1.1770343567473891e-08,2.888375284571731e-09,6.497249429162052e-10,1.349097547737465e-10,2.6011924376630928e-11,4.680997284811773e-12,7.897244282739192e-13,1.253960384263859e-13,1.8804789516950947e-14,2.671603730934689e-15],[2.5086938633128646e-07,6.771811069738593e-07,9.139701307292422e-07,8.223712398968568e-07,5.54964352885818e-07,2.9960720222910794e-07,1.3479015237762222e-07,5.1977727722377834e-08,1.7538177790326518e-08,4.609722848756804e-09,1.5499819899250937e-09,3.8035675386761656e-10,8.555926631641728e-11,1.7765640311669845e-11,3.4253897582468248e-12,6.164188364387443e-13,1.0399514965824988e-13,1.6512823101098855e-14,2.4763155729923707e-15,3.5181111268565682e-16],[2.9732244056190822e-08,8.025735717390433e-08,1.0832084131232034e-07,9.746483126927581e-08,6.577261507985505e-08,3.550849542839346e-08,1.5974901383823478e-08,6.160235446533007e-09,2.078569210809372e-09,6.234177250923459e-10,1.4747282582212918e-10,4.507867619797389e-11,1.0140212899588434e-11,2.1055273474601535e-12,4.05966330803233e-13,7.305600557266662e-14,1.2325175325362387e-14,1.9570474248708597e-15,2.9348506827822974e-16,4.1695537335260335e-17],[3.203428429230197e-09,8.64713403871829e-09,1.16707659832951e-08,1.0501111545702918e-08,7.086510678892097e-09,3.82577660534242e-09,1.7211769535583855e-09,6.637196076717404e-10,2.2395039168403702e-10,6.716862878135186e-11,1.8131078908131992e-11,3.8990950196649066e-12,1.092532612728392e-12,2.2685493064796376e-13,4.373985639790823e-14,7.871241899373232e-15,1.327946082976247e-15,2.1085732198130796e-16,3.162083593489431e-17,4.492384409981677e-18],[3.163834816836927e-10,8.540257521572584e-10,1.1526518095482547e-09,1.0371320308150916e-09,6.998923094764848e-10,3.778490917723181e-10,1.6999036163620254e-10,6.555161914055362e-11,2.2118241818328687e-11,6.6338440527826435e-12,1.7906983091284638e-12,4.3942716782744553e-13,8.662405582191999e-14,2.240510577374221e-14,4.319924219078133e-15,7.773955224267977e-16,1.3115329856806234e-16,2.0825117570357856e-17,3.1230009934184107e-18,4.436859608669626e-19],[2.8843666819037734e-11,7.785878744051928e-11,1.050835668665202e-10,9.455199931736628e-11,6.380693605214565e-11,3.444728926098831e-11,1.549747580812176e-11,5.976130776096836e-12,2.0164491339298104e-12,6.047862757235092e-13,1.6325221888023064e-13,4.006116486422593e-14,9.011549916521754e-15,1.6397928803612135e-15,3.938336293522235e-16,7.087265528580242e-17,1.1956825387922747e-17,1.8985591455979326e-18,2.8471397953620607e-19,4.0449425360094276e-20],[2.441757082897175e-12,6.591126117612531e-12,8.895836486471547e-12,8.004287925101272e-12,5.401568358862755e-12,2.9161310546032745e-12,1.311936916998799e-12,5.059086191226868e-13,1.7070225453530766e-13,5.1198108120295784e-14,1.3820096600421823e-14,3.3913730064227146e-15,7.628716547933874e-16,1.5840368912124635e-16,2.676517653655544e-17,5.9997159554490816e-18,1.0122035892002147e-18,1.607222920077267e-19,2.4102427076765318e-20,3.424241151161163e-21],[1.929262037543863e-13,5.20772909493766e-13,7.028708853045994e-13,6.324285466245502e-13,4.2678450083934325e-13,2.304070695465558e-13,1.0365773513452741e-13,3.997245672700433e-14,1.3487393226166684e-14,4.045224935862809e-15,1.0919426798486985e-15,2.679565155055954e-16,6.027541942726196e-17,1.2515668580181594e-17,2.4131436987387723e-18,3.8056143956569533e-19,7.99754395139335e-20,1.2698864220745423e-20,1.9043621455046596e-21,2.705534676894362e-22],[1.4290626137033295e-14,3.857522102775156e-14,5.2063767642892164e-14,4.684589103149912e-14,3.161321595453184e-14,1.706694697839561e-14,7.678241266308404e-15,2.9608805011868334e-15,9.990519193737117e-16,2.9964201893598693e-16,8.088348963033597e-17,1.9848347759683568e-17,4.4647822199647174e-18,9.27073342313268e-19,1.7874883630383698e-19,3.2166894124651365e-20,4.7557827035044e-21,9.406431962692653e-22,1.4106185122251413e-22,2.0040711845187827e-23],[9.962821695330558e-16,2.6893016812014827e-15,3.629666250025745e-15,3.265897904194982e-15,2.2039400565856835e-15,1.1898355467349385e-15,5.352945905688661e-16,2.0642009812335122e-16,6.964968533677106e-17,2.0889777525926088e-17,5.6388556915284585e-18,1.3837430759188047e-18,3.1126578177508013e-19,6.463164258440724e-20,1.246161481845789e-20,2.24254016292534e-21,3.783357776757883e-22,5.264551123283086e-23,9.83423720043458e-24,1.3971538884758399e-24],[6.559789061412947e-17,1.770708368639494e-16,2.3898696264591365e-16,2.15035478931342e-16,1.4511332549468972e-16,7.834196418480794e-17,3.5245231795053854e-17,1.3591252991709991e-17,4.585922121010571e-18,1.375438990081949e-18,3.712773852161893e-19,9.110935607200896e-20,2.049457405663801e-20,4.255520725067827e-21,8.205061484938009e-22,1.476548600426274e-22,2.4910642505044373e-23,3.955425174849776e-24,5.198206456519647e-25,9.199235994587666e-26],[4.0918178722251976e-18,1.1045196852316437e-17,1.4907356255335633e-17,1.3413327892349135e-17,9.05177427502992e-18,4.88675849475526e-18,2.1985016289328287e-18,8.477853689617631e-19,2.8605733994961886e-19,8.579614053261101e-20,2.3159272747307134e-20,5.683153650402224e-21,1.2783957475384314e-21,2.6544780015695553e-22,5.118094029008971e-23,9.210308282583652e-24,1.5538580776985848e-24,2.4672865653417295e-25,3.7000215574186127e-26,4.6066318880329455e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.21090729820236975, "-10": 0.0001625137908539568, "-11": 3.895450796050959e-05, "-12": 8.589463372301172e-06, "-13": 1.7531672282608323e-06, "-14": 3.33020526127367e-07, "-15": 5.914952745724851e-08, "-16": 9.86389908410925e-09, "-17": 1.5491498155725205e-09, "-18": 2.2757887415581427e-10, "-19": 2.7672754617624295e-11, "-2": 0.20381360118157796, "-3": 0.14876429004075245, "-4": 0.08764054796410402, "-5": 0.04303423798696756, "-6": 0.018056689232255427, "-7": 0.006601417749894012, "-8": 0.0021357064826826072, "-9": 0.0006191540119458062, "0": 0.14487657491007142, "1": 0.08204428184218805, "10": 3.963222176853623e-08, "11": 4.170986436798796e-09, "12": 4.0380337330182646e-10, "13": 3.618679419350877e-11, "14": 3.0180096580220176e-12, "15": 2.3535517828536996e-13, "16": 1.7232328108773042e-14, "17": 1.1882603626523407e-15, "18": 7.66430874664459e-17, "19": 4.0918178722251976e-18, "2": 0.03599220989019348, "3": 0.011534450250000708, "4": 0.0029835007168731846, "5": 0.0006432177722335991, "6": 0.00011849632948181923, "7": 1.902071537873093e-05, "8": 2.70180531885847e-06, "9": 3.439014712760716e-07} |
| Raw goal margin distribution | {"-1": 0.201284982131671, "-10": 0.00015509935297166143, "-11": 3.717726937668915e-05, "-12": 8.197582521565191e-06, "-13": 1.673181711690751e-06, "-14": 3.178269847575789e-07, "-15": 5.6450922650884696e-08, "-16": 9.413874094524946e-09, "-17": 1.478472274807665e-09, "-18": 2.171959434710741e-10, "-19": 2.641022840944077e-11, "-2": 0.19451492395802017, "-3": 0.14197715165812655, "-4": 0.08364208484638545, "-5": 0.041070868092697964, "-6": 0.017232880988235194, "-7": 0.006300238375611517, "-8": 0.002038268210106123, "-9": 0.0005909060771888628, "0": 0.17223150896641248, "1": 0.08547486920433842, "10": 4.128939757750489e-08, "11": 4.345391441468172e-09, "12": 4.2068794731647285e-10, "13": 3.7699903407820294e-11, "14": 3.144204263656729e-12, "15": 2.451962846015357e-13, "16": 1.7952878105713673e-14, "17": 1.2379461041998178e-15, "18": 7.984783009268182e-17, "19": 4.2629125343453135e-18, "2": 0.03749718278547293, "3": 0.012016750032124672, "4": 0.003108252370790504, "5": 0.0006701131842109934, "6": 0.00012345111732630862, "7": 1.9816044734198335e-05, "8": 2.8147782034245744e-06, "9": 3.582813160951648e-07} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.34, "draw": 6.85, "home": 6.96}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.36, "draw": 6.41, "home": 7.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.96 |
| Reference draw odds | 6.85 |
| Reference away odds | 1.34 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.40 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:40Z |
| Home probability edge | +0.2% |
| Draw probability edge | +1.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0080 |
| Raw ev home | 0.1044 |
| Raw edge prob draw | 0.0391 |
| Raw ev draw | 0.1798 |
| Raw edge prob away | -0.0470 |
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
| Market best home last update utc | 2026-11-05T13:33:39Z |
| Market best draw last update utc | 2026-11-05T13:34:00Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3172 |
| Dc lambda away | 1.0223 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Score matrix json | [[0.03751592679998952,0.03204256229072919,0.020028038038623817,0.006824859238585102,0.0017442561099846857,0.00035662911375732996,6.076340321206947e-05,8.874023926857303e-06,1.1339845931958077e-06,1.288075116221315e-07,1.316793687926108e-08,1.22377505552537e-09,1.0425500088357883e-10,8.19841861283309e-12,5.986577371148781e-13,4.0800349789825645e-14,2.606876454244998e-15,1.5676462712476163e-16,8.90332269568375e-18],[0.07664510099481504,0.0808073405325162,0.04640988863433818,0.015814876953845293,0.004041870284949567,0.0008263973446286542,0.00014080374576267294,2.0563295385682154e-05,2.627721126841286e-06,2.984786756506532e-07,3.051334748475909e-08,2.83578770575952e-09,2.4158447129213596e-10,1.8997751755089705e-11,1.3872371750046608e-12,9.45444424629204e-14,6.040773723900014e-15,3.6326218637258254e-16,2.063118783704141e-17],[0.0965657540199653,0.0987187577509786,0.04436740533789914,0.018323479233918874,0.004683003633136685,0.0009574829211419849,0.00016313844989562283,2.3825105758339287e-05,3.044537977799383e-06,3.458242407458349e-07,3.535346437573069e-08,3.285608689206582e-09,2.799053104161146e-10,2.201123099417428e-11,1.6072848143492957e-12,1.0954135989850629e-13,6.998979012591784e-15,4.208839024098485e-16,2.3903767509945185e-17],[0.07458886522508702,0.07625187823369937,0.03897598466353483,0.011678046127585434,0.003617223625348653,0.000739574451472893,0.00012601063364325188,1.840287605495003e-05,2.3516476954323353e-06,2.671199323854086e-07,2.7307556558985586e-08,2.5378543997174773e-09,2.162031424732329e-10,1.7001811446771055e-11,1.2414913714756673e-12,8.461142164698624e-14,5.406118427610337e-15,3.250971629731821e-16,1.846363559489717e-17],[0.04321018516369624,0.04417358767444535,0.022579234972491303,0.007694218480362929,0.0017290154265197496,0.00042844396270201476,7.299940541913844e-05,1.06609971807359e-05,1.3623364835055003e-06,1.54745640712676e-07,1.5819580733948597e-08,1.4702081631000634e-09,1.2524896029788733e-10,9.849344382921874e-12,7.192101914771044e-13,4.901636705823186e-14,3.131826413620579e-15,1.8833251539452071e-16,1.069619587914288e-17],[0.020025724711016886,0.020472212810826586,0.010464327843805913,0.003565879215061118,0.0009113457715249834,0.00016383531628396558,3.383151429352801e-05,4.940830359267124e-06,6.313737207813955e-07,7.171673968538241e-08,7.331571656580742e-09,6.813667618084605e-10,5.8046527450983537e-11,4.564670538882779e-12,3.3331737064572715e-13,2.271659492602697e-14,1.4514423709192954e-15,8.728254908272661e-17,4.957143167041819e-18],[0.007734088014245227,0.007906525132555436,0.0040414034309274325,0.0013771698200903681,0.00035196870575709266,7.196322081713587e-05,1.0780866980615121e-05,1.9081864658313477e-06,2.438413588956624e-07,2.7697553263394266e-08,2.8315090361522206e-09,2.631490536224545e-10,2.2418012766361035e-11,1.7629106668149594e-12,1.2872971732367073e-13,8.77332266757839e-15,5.60558142403655e-16,3.370918787983319e-17,1.914486596933197e-18],[0.002560254798348787,0.002617337541492387,0.0013378464929591288,0.0004558915845712153,0.00011651400476997939,2.3822353852496973e-05,4.0589150934683565e-06,5.212022380887448e-07,8.072005490481009e-08,9.168863027484785e-09,9.373289498418182e-10,8.711158005661523e-11,7.42114967515294e-12,5.835853542731805e-13,4.261405816186266e-14,2.9042779724975525e-15,1.8556443516016792e-16,1.1158925248694129e-17,6.337623113603789e-19],[0.0007415924854805552,0.0007581268294033601,0.00038751490927577755,0.00013205161202310085,3.374894969297157e-05,6.900281415296768e-06,1.1756880348241317e-06,1.7170012211358262e-07,1.9291898236798326e-08,2.655813759618193e-09,2.7150270593160554e-10,2.5232368750949192e-11,2.149578563926253e-12,1.6903884474491268e-13,1.234340633949803e-14,8.412407708560708e-16,5.3749802861799785e-17,3.232246695058605e-18,1.8357288813158863e-19],[0.00019093912575538952,0.00019519625245957063,9.977414745019844e-05,3.3999561548876935e-05,8.689401626504988e-06,1.7766276313454808e-06,3.0270647279405003e-07,4.420793340053431e-08,5.649197679252367e-09,5.642071791272326e-10,6.990428075496274e-11,6.496622504099218e-12,5.534557857239321e-13,4.352272962067512e-14,3.1780786098176876e-15,2.1659574561757035e-16,1.3839056582816036e-17,8.322122597835024e-19,4.7264835416346067e-20],[4.4245290253375284e-05,4.523177118506862e-05,2.3120123213366534e-05,7.878534392918139e-06,2.0135480120789883e-06,4.116883059460045e-07,7.014453270047063e-08,1.0244065154641642e-08,1.3090580048922206e-09,1.486938228181761e-10,1.3365563462330685e-11,1.5054271733113673e-12,1.282493139365076e-13,1.0085286591041122e-14,7.36438956568638e-16,5.019055992103356e-17,3.206849685297127e-18,1.9284404304704997e-19,1.0952424514886076e-20],[9.320656050887363e-06,9.528466857696818e-06,4.87045547880629e-06,1.6596819422124764e-06,4.24171439605474e-07,8.672573008157566e-08,1.4776557220153687e-08,2.1580016160479626e-09,2.7576447898497927e-10,3.132364984935499e-11,3.2022033408610074e-12,2.6166797077252246e-13,2.7016835851207306e-14,2.1245535276503166e-15,1.551372852871503e-16,1.0573078927642907e-17,6.755508383464775e-19,4.0624278570914136e-20,2.307223689616828e-21],[1.7998543195895628e-06,1.8399833809186502e-06,9.405035744306414e-07,3.2049092859204137e-07,8.19091267451879e-08,1.6747070061878493e-08,2.8534096952138836e-09,4.167183628619576e-10,5.3251175237093625e-11,6.048716547297669e-12,6.18357708275707e-13,5.746767665415085e-14,4.304639027120044e-15,4.102594091085054e-16,2.995760293363604e-17,2.0417019655464844e-18,1.304514497543872e-19,7.844703513022391e-21,4.455337157968474e-22],[3.208234620850246e-07,3.2797645454985695e-07,1.676444640925086e-07,5.7127406456534946e-08,1.460027588496427e-08,2.985159931309077e-09,5.086193739136894e-10,7.42799161202469e-11,9.492005110478377e-12,1.078181807690714e-12,1.1022206553984504e-13,1.0243595151840828e-14,8.7266529644021645e-16,6.03390820137098e-17,5.3399332292234136e-18,3.6393272833425445e-19,2.3252929578076633e-20,1.398315915174912e-21,7.941624364917787e-23],[5.31019175572578e-08,5.4285863437296184e-08,2.77481031259858e-08,9.455589090023965e-09,2.4166020817739363e-09,4.940963966207486e-10,8.41854392009241e-11,1.2294630686742075e-11,1.5710935526782353e-12,1.784580251445393e-13,1.82436876631434e-14,1.6954949046052577e-15,1.4444143307189684e-16,1.135860460721022e-17,7.29274942504932e-19,6.023725824413626e-20,3.848768233454531e-21,2.3144584240831206e-22,1.3144783101455693e-23],[8.203346646168295e-09,8.386246227031553e-09,4.286611843548695e-09,1.4607283242748352e-09,3.7332408121171567e-10,7.632952263413459e-11,1.3005224144315602e-11,1.8993121538636148e-12,2.4270733749459703e-13,2.7568741570824606e-14,2.81834067185648e-15,2.619252388445618e-16,2.231375438147692e-17,1.7547119820906425e-18,1.2813104015479636e-19,7.678164953216132e-21,5.945694888653421e-22,3.575446165465872e-23,2.0306462992351625e-24],[1.1880732012520917e-09,1.2145621575179316e-09,6.208208521663327e-10,2.115541682236993e-10,5.4067730573944537e-11,1.10546419915509e-11,1.8835188793777377e-12,2.7507332898966916e-13,3.515078611962169e-14,3.992722051778726e-15,4.0817426943618213e-16,3.793407379025357e-17,3.2316534633260817e-18,2.541311944694655e-19,1.8556945308116893e-20,1.264712393513333e-21,7.10503361737177e-23,5.178242435596336e-24,2.9409417319575475e-25],[1.6194457241339743e-10,1.6555524445921724e-10,8.462320953241073e-11,2.883664851555678e-11,7.369895642736859e-12,1.5068425654397332e-12,2.567397860939271e-13,3.749485519799181e-14,4.791353783704325e-15,5.442422779668857e-16,5.563765554540742e-17,5.1707397771337976e-18,4.405020984860765e-19,3.4640262554437515e-20,2.529470886183328e-21,1.723911519741305e-22,1.1014671131902873e-23,5.82394089450778e-25,4.0087559484773195e-26],[2.0848077402919685e-11,2.1312900454202027e-11,1.0894043536770224e-11,3.7123113873705934e-12,9.48770017552669e-13,1.939847070521687e-13,3.305162286780306e-14,4.8269332632127795e-15,6.168191564484695e-16,7.006350980402658e-17,7.162562672163241e-18,6.656597470204749e-19,5.67084262752762e-20,4.459444760821318e-21,3.2563366612229367e-22,2.2192927039015944e-23,1.4179834057014605e-24,8.527049277763662e-26,4.258146636428783e-27]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.10085742089510207, "-10": 1.630137420557053e-08, "-11": 1.4886627513355352e-09, "-12": 1.249478698981141e-10, "-13": 9.700796555822428e-12, "-14": 7.005369519492425e-13, "-15": 4.72804710517304e-14, "-16": 2.9940424081275254e-15, "-17": 1.7739581496180306e-16, "-18": 8.90332269568375e-18, "-2": 0.04134368660120875, "-3": 0.011961544109899703, "-4": 0.002753631754601568, "-5": 0.0005237719609286149, "-6": 8.465488046959355e-05, "-7": 1.187640691207396e-05, "-8": 1.4704845329413343e-06, "-9": 1.6283286256249061e-07, "0": 0.17627289147974973, "1": 0.22302160729840115, "10": 5.477388294519424e-05, "11": 1.1338124125278468e-05, "12": 2.157095213214443e-06, "13": 3.7961505541444297e-07, "14": 6.21387700549888e-08, "15": 9.506244324606009e-09, "16": 1.3645224892480793e-09, "17": 1.8325747286759946e-10, "18": 2.0848077402919685e-11, "2": 0.19933975873780532, "3": 0.130727678082077, "4": 0.06821529092422797, "5": 0.029411264241435902, "6": 0.010775043229593115, "7": 0.003426475749265692, "8": 0.0009616535235028349, "9": 0.00024137695100529696} |
| Raw goal margin distribution | {"-1": 0.09329278419188392, "-10": 1.5078717780947034e-08, "-11": 1.3770081721531184e-09, "-12": 1.1557637066452521e-10, "-13": 8.973205060567463e-12, "-14": 6.47994387488989e-13, "-15": 4.373428095992396e-14, "-16": 2.769479427134096e-15, "-17": 1.6409054817084428e-16, "-18": 8.235544350306337e-18, "-2": 0.03824277477603793, "-3": 0.011064389147995414, "-4": 0.0025471003595575613, "-5": 0.00048448734939885915, "-6": 7.830548733398212e-05, "-7": 1.0985637518685758e-05, "-8": 1.3601933796411524e-06, "-9": 1.5061986487031864e-07, "0": 0.19761246809717065, "1": 0.21983333826810944, "10": 5.399084727085562e-05, "11": 1.1176036736311436e-05, "12": 2.126257843028691e-06, "13": 3.7418816005990015e-07, "14": 6.125044753527141e-08, "15": 9.370345096088769e-09, "16": 1.3450155686124236e-09, "17": 1.8063766336846182e-10, "18": 2.055003776303888e-11, "2": 0.19649004033164563, "3": 0.12885882325460118, "4": 0.06724009976638175, "5": 0.028990807120448384, "6": 0.010621005524255437, "7": 0.003377491587386648, "8": 0.0009479059311327705, "9": 0.00023792627792102155} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.75, "draw": 5.6, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.0, "draw": 5.49, "home": 1.5}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 5.60 |
| Reference away odds | 5.75 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:40Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0136 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | 0.0305 |
| Raw ev draw | 0.1066 |
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
| SC Paderborn win | 30.3% | 30.8% | 3.14 | -4.8% |
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
| Market best home last update utc | 2026-11-05T13:34:00Z |
| Market best draw last update utc | 2026-11-05T13:33:39Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
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
| Dc lambda away | 1.0882 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Fair Over 4.5 odds | 17.58 |
| Fair Under 4.5 odds | 1.06 |
| Score matrix json | [[0.11952058072492004,0.15216193801291053,0.08923649674259196,0.032368586349017445,0.00880574725991338,0.0019164552685588835,0.0003475761045579559,5.4032410971739116e-05,7.349652989639263e-06,8.886419275911427e-07,9.670062367944438e-08,9.56619137754647e-09,8.674816441094909e-10,7.261384211579965e-11],[0.11730185788392263,0.11948149466780637,0.0819760185126728,0.029735006758839187,0.00808929223744435,0.0017605282402251463,0.0003192965459412329,4.963621482004603e-05,6.751669009131132e-06,8.163400600259026e-07,8.88328476161433e-08,8.78786494413365e-09,7.96901423887721e-10,6.670581973574902e-11],[0.05892093879935174,0.06411684338505753,0.027682925492064858,0.013657850506885845,0.0037155647880485008,0.0008086438894451604,0.00014665893729901442,2.2798851442612732e-05,3.1011691622123226e-06,3.749604159515332e-07,4.0802605584799264e-08,4.036432433162347e-09,3.6603188304127534e-10,3.063924354479285e-11],[0.01804233374651796,0.019633385188681986,0.010682371232644735,0.003074795652222213,0.001137752746796337,0.0002476169462461531,4.4908814210672115e-05,6.981295531724066e-06,9.49617066007438e-07,1.1481760311675802e-07,1.2494271861408046e-08,1.2360064620217129e-09,1.1208357385795382e-10,9.38212236669387e-12],[0.00414359241791717,0.004508992414663124,0.002453307485984497,0.0008898836025560629,0.00019210694230707272,5.6867571314679785e-05,1.0313733504508791e-05,1.6033204816463222e-06,2.180885316675047e-07,2.6368947410134196e-08,2.8694275851269912e-09,2.838605624130089e-10,2.5741051758368458e-11,2.1546930485146665e-12],[0.0007612921196132623,0.0008284261690015548,0.00045074019538993084,0.00016349614191531065,4.447848565746395e-05,7.681567210418245e-06,1.8949170789149688e-06,2.94574158069686e-07,4.006887352592351e-08,4.8447023358350465e-09,5.271929253737132e-10,5.215300817222705e-11,4.729340600553908e-12,3.958764937706483e-13],[0.00011655861889294663,0.00012683726473176784,6.901116312733733e-05,2.5032289189667093e-05,6.8099363242028465e-06,1.482093224101624e-06,2.1330160235067132e-07,4.5101159123514195e-08,6.134796930710847e-09,7.417544444033257e-10,8.071655766371051e-11,7.984954063041434e-12,7.24091836068047e-13,6.061118482288977e-14],[1.5296450361786974e-05,1.664535786732564e-05,9.0566089510381e-06,3.2850867028831127e-06,8.93694983172132e-07,1.9450097855769287e-07,3.527548676397204e-08,4.3515584549679365e-09,8.050937598741586e-10,9.734338092896659e-11,1.0592754353165886e-11,1.04789722653323e-12,9.502544670645819e-14,7.954246445421238e-15],[1.75648717706431e-06,1.9113818539655254e-06,1.0399679084975552e-06,3.772256002329528e-07,1.0262274848222828e-07,2.2334493734344824e-08,4.050674417929483e-09,6.296972144866804e-10,6.796911759405971e-11,1.117791358974094e-11,1.2163630614334514e-12,1.2032974956628085e-13,1.091174584213816e-14,9.133839259528427e-16],[1.7928616728253348e-07,1.9509640109277924e-07,1.0615042503355128e-07,3.850374369350895e-08,1.0474792808979611e-08,2.2797011171575633e-09,4.1345584572599185e-10,6.427374000104693e-11,8.742709733997764e-12,8.388289233195443e-13,1.2415523105208977e-13,1.2282161743908775e-14,1.1137713476894028e-15,9.322988831336224e-17],[1.6469904920868843e-08,1.7922292751889323e-08,9.75137922858998e-09,3.5370994167678695e-09,9.622540558738473e-10,2.0942196052646288e-10,3.798161660376968e-11,5.904428672724587e-12,8.031383583697467e-13,9.710695456100815e-14,8.385330424735784e-15,1.1282857970081521e-15,1.0231524538714099e-16,8.564449893585786e-18],[1.3754433749126197e-09,1.4967359524702226e-09,8.143623184630425e-10,2.9539210958262223e-10,8.03602675603461e-11,1.748935707590837e-11,3.1719407717971364e-12,4.930937573448194e-13,6.707211361968143e-14,8.10964713825643e-15,8.824791085599395e-16,6.927580710693548e-17,8.544604665081341e-18,7.152388506491896e-19],[1.0529452230945945e-10,1.145798511325542e-10,6.234200031305353e-11,2.2613196326211286e-11,6.151831576464965e-12,1.3388653669034732e-12,2.4282205611081257e-13,3.774788012388927e-14,5.134581541256693e-15,6.208190297730233e-16,6.75565551288504e-17,6.683089628383923e-18,4.809123013336511e-19,5.475378666246993e-20],[7.44057905350416e-12,8.096721667865121e-12,4.405362895512975e-12,1.5979489837380572e-12,4.347157683474151e-13,9.461017900975071e-14,1.715888599709816e-14,2.6674330250393676e-15,3.6283235847826684e-16,4.3869832614558995e-17,4.773846521106875e-18,4.72256824106196e-19,4.282520702848854e-20,2.8446311758870293e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2489923681852152, "-10": 1.05863902628986e-07, "-11": 1.0393732044978982e-08, "-12": 9.3418746384524e-10, "-13": 7.261384211579965e-11, "-2": 0.12294529977675743, "-3": 0.04131307543194146, "-4": 0.010720138747978728, "-5": 0.002259527187229965, "-6": 0.00040043122845597037, "-7": 6.117182331919739e-05, "-8": 8.20805779864024e-06, "-9": 9.816254459073547e-07, "0": 0.2699598027685082, "1": 0.1930369525970872, "10": 1.8030580822635857e-08, "11": 1.494428588940687e-09, "12": 1.1339124397732458e-10, "13": 7.44057905350416e-12, "2": 0.08117813616899575, "3": 0.023028015094665556, "4": 0.005044419777678434, "5": 0.0008975739063211222, "6": 0.0001342834284013658, "7": 1.7317601456494632e-05, "8": 1.961636595937017e-06, "9": 1.9804587026498042e-07} |
| Raw goal margin distribution | {"-1": 0.2220581387209179, "-10": 9.441229603486691e-08, "-11": 9.269411785967499e-09, "-12": 8.33133685782609e-10, "-13": 6.475899138247771e-11, "-2": 0.10964594871680541, "-3": 0.03684411977008752, "-4": 0.009560510125496682, "-5": 0.0020151075522618768, "-6": 0.00035711541652762714, "-7": 5.4554689075134436e-05, "-8": 7.3201682869410665e-06, "-9": 8.754401631986305e-07, "0": 0.3274680338795759, "1": 0.18581365864657437, "10": 1.7355890388352948e-08, "11": 1.4385082232244929e-09, "12": 1.0914823104304924e-10, "13": 7.162158321398694e-12, "2": 0.078140512895242, "3": 0.022166324522535554, "4": 0.0048556614784319415, "5": 0.000863987382702507, "6": 0.00012925864603210478, "7": 1.6669590160444062e-05, "8": 1.888233666778104e-06, "9": 1.9063514647680002e-07} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Hamburg", "away_goals": 0.0, "away_xg": 0.46, "date": "2026-10-24T00:00:00+00:00", "home": "Paderborn", "home_goals": 1.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 2.0, "away_xg": 1.15, "date": "2026-10-17T00:00:00+00:00", "home": "Werder Bremen", "home_goals": 2.0, "home_xg": 3.21, "source": "pipeline training history"}, {"away": "Stuttgart", "away_goals": 2.0, "away_xg": 2.47, "date": "2026-10-10T00:00:00+00:00", "home": "Paderborn", "home_goals": 0.0, "home_xg": 1.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 1.0, "away_xg": 1.5, "date": "2026-09-20T00:00:00+00:00", "home": "Paderborn", "home_goals": 3.0, "home_xg": 0.68, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.49, "date": "2026-09-12T00:00:00+00:00", "home": "Dortmund", "home_goals": 3.0, "home_xg": 1.76, "source": "pipeline training history"}, {"away": "Freiburg", "away_goals": 1.0, "away_xg": 1.24, "date": "2026-09-05T00:00:00+00:00", "home": "Paderborn", "home_goals": 0.0, "home_xg": 0.77, "source": "pipeline training history"}, {"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.73, "date": "2026-08-29T00:00:00+00:00", "home": "Mainz", "home_goals": 0.0, "home_xg": 1.23, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 29.2% |
| Unadjusted draw probability | 32.7% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 60.6% |
| Raw p under 3 5 | 85.6% |
| Raw p btts yes | 40.9% |
| P home draw | 57.3% |
| P draw away | 69.7% |
| P home away | 73.0% |
| Raw p home draw | 61.9% |
| Raw p draw away | 70.8% |
| Raw p home away | 67.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3434 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.19, "draw": 3.92, "home": 3.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.25, "draw": 4.16, "home": 3.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.14 |
| Reference draw odds | 3.92 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.71 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:40Z |
| Home probability edge | -0.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -31.6% |
| Under 2.5 probability edge | +31.6% |
| Raw edge prob home | -0.0162 |
| Raw ev home | -0.0832 |
| Raw edge prob draw | 0.0822 |
| Raw ev draw | 0.3623 |
| Raw edge prob away | -0.0659 |
| Raw ev away | -0.1438 |
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
| Market best home last update utc | 2026-11-05T13:33:39Z |
| Market best draw last update utc | 2026-11-05T13:33:39Z |
| Market best away last update utc | 2026-11-05T13:33:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2832 |
| Dc lambda away | 1.1838 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T13:33:35.017473+00:00 |
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
| Score matrix json | [[0.036264242165602346,0.03272755875151906,0.023610931438669845,0.009317032318372647,0.0027574227041958694,0.0006528585248864226,0.0001288111820470088,2.1784182270775015e-05,3.2235693047519636e-06,4.2401404155955795e-07,5.019563762974649e-08,5.4020553139949724e-09,5.329218383110449e-10,4.852950947358996e-11,4.103586595060401e-12,3.238605730293238e-13,2.396204248706853e-14,1.6686323116114163e-15,1.0974225515800811e-16],[0.06402517425201346,0.08719255615304257,0.05390770617122994,0.02127234335974089,0.0062956573023721174,0.0014905852241525372,0.0002940974764759282,4.973693223767261e-05,7.359947969632269e-06,9.68094987029281e-07,1.1460503756281924e-07,1.2333795951422158e-08,1.216749705386548e-09,1.1080098826815234e-10,9.369174654940106e-12,7.39427864447456e-13,5.470935142947457e-14,3.809766700471856e-15,2.5055992648968226e-16],[0.08059266275472657,0.0954072200150098,0.05462197910873004,0.02428415919103252,0.007187019387451873,0.0017016277078164847,0.0003357368680847288,5.6778868209654124e-05,8.401996202756087e-06,1.1051614003914793e-06,1.3083123608924596e-07,1.4080059692948486e-08,1.389021559193597e-09,1.264885956438564e-10,1.0695696518313631e-11,8.441187539549925e-13,6.245530061656949e-14,4.349167342327074e-15,2.860351132393044e-16],[0.061335510271643696,0.07261021441900932,0.04297871832014369,0.016403948281437205,0.0054697225081535555,0.001295033569853981,0.00025551447758527697,4.321188474544229e-05,6.394387612738776e-06,8.410894504358617e-07,9.956986592471363e-08,1.0715710542415969e-08,1.0571228595677198e-09,9.626487439645409e-11,8.140021451554969e-12,6.424214405381098e-13,4.753196632979508e-14,3.309958860774268e-15,2.1768867073586302e-16],[0.03500980757763466,0.04144531648505003,0.024531900878588205,0.009680453052461076,0.002771097954176757,0.0007391945691226439,0.0001458455738599444,2.4664990366995752e-05,3.64986414733215e-06,4.800869787326362e-07,5.6833665051722876e-08,6.1164399299218644e-09,6.033970816493701e-10,5.494720292011864e-11,4.6462576643551374e-12,3.666889036608216e-13,2.7130857599827707e-14,1.889297444374037e-15,1.2425491270131395e-16],[0.01598664944590389,0.018925318122693924,0.011202086692935431,0.004420418737922159,0.0013082452194529243,0.0002995955359974285,6.65979685082617e-05,1.1262859806052034e-05,1.666650081385971e-06,2.1922377652383287e-07,2.595215291866504e-08,2.7929711067322618e-09,2.7553129504122943e-10,2.5090731194936527e-11,2.1216366971077238e-12,1.6744242154227904e-13,1.2388857283873333e-14,8.627164223988703e-16,5.673895027507327e-17],[0.006083365828739149,0.007201611191587902,0.004262706305594101,0.0016820925729302172,0.0004978237804338927,0.00011786676683734417,2.2493462146750518e-05,4.285832169515161e-06,6.342068228791068e-07,8.342075901926612e-08,9.875517742591841e-09,1.0628033753316685e-09,1.0484733969265375e-10,9.54772275990982e-12,8.073419153812171e-13,6.371650976262736e-14,4.71430560311382e-15,3.2828765162284094e-16,2.159075248568415e-17],[0.001984191689705896,0.0023489261506081964,0.0013903530817198553,0.0005486426755327818,0.0001623735668514993,3.844422082037325e-05,7.585174027726771e-06,1.2407483183689326e-06,2.0685718119508834e-07,2.7209078239717273e-08,3.221065572585357e-09,3.466511277625315e-10,3.419771652119317e-11,3.1141497468935526e-12,2.6332809243245346e-13,2.0782207206873352e-14,1.5376497589938841e-15,1.0707651792134828e-16,7.04218566869758e-18],[0.000566280193529754,0.0006703739170234451,0.0003968010834213857,0.000156580375823183,4.634075192322395e-05,1.0971823397510761e-05,2.1647776465663203e-06,3.661010642017874e-07,5.239950571185244e-08,7.765359653147796e-09,9.192789412831517e-10,9.893281417067643e-11,9.759888437375399e-12,8.887656018823993e-13,7.51527606521593e-14,5.931156944230557e-15,4.3883895271887803e-16,3.055920030588418e-17,2.009810989548908e-18],[0.0001436569345134984,0.00017006397715786328,0.0001006625834829876,3.9722132352043994e-05,1.1755965404414363e-05,2.7833898012310685e-06,5.491721662921326e-07,9.287444132123767e-08,1.3743329656251443e-08,1.7485000151049726e-09,2.33207511363565e-10,2.5097796053865003e-11,2.4759397735026362e-12,2.2546672711900406e-13,1.9065147146010158e-14,1.5046470536353685e-15,1.1132697101721193e-16,7.752418479910369e-18,5.098594106045959e-19],[3.279928127922077e-05,3.882845085866433e-05,2.298295171850071e-05,9.069227297918611e-06,2.684083558611256e-06,6.354944528745602e-07,1.2538519225636237e-07,2.1204788580947528e-08,3.1378320624410362e-09,4.127365441063972e-10,4.7259498570532235e-11,5.730246681422023e-12,5.652984684417896e-13,5.147782546610486e-14,4.3528920200713525e-15,3.4353609246409216e-16,2.5417809789154954e-17,1.7700068233943625e-18,1.164094324991079e-19],[6.807840537070099e-06,8.059258966589445e-06,4.770356674548792e-06,1.8824148222353936e-06,5.571101604221247e-07,1.3190364936756927e-07,2.6025033515962186e-08,4.401279956485843e-09,6.512905002811044e-10,8.566787034683788e-11,1.0141535314787376e-11,1.0556676375942937e-12,1.1733372436547143e-13,1.0684771534624736e-14,9.034891495169593e-16,7.130457878982131e-17,5.275737427690894e-18,3.6738378809625834e-19,2.41620188783472e-20],[1.2952865649196064e-06,1.5333863661741772e-06,9.076268571174374e-07,3.581556611924396e-07,1.0599797425418962e-07,2.509650805704819e-08,4.951625420902714e-09,8.374048664981768e-10,1.2391709680628748e-10,1.6299506561781155e-11,1.9295684687930808e-12,2.0766018906757835e-13,1.98147311897704e-14,2.0329267324453433e-15,1.719014055261073e-16,1.3566690115725908e-17,1.003782590517686e-18,6.989988709329475e-20,4.597160915276998e-21],[2.2748891588823542e-07,2.693059679040328e-07,1.594049188408801e-07,6.290225289950352e-08,1.8616238987186065e-08,4.407655854002165e-09,8.696453197256004e-10,1.4707195334109439e-10,2.1763343167409057e-11,2.862653854116764e-12,3.388867382601972e-13,3.6470996120508233e-14,3.5979250799641705e-15,3.1690197760337413e-16,3.019074345546479e-17,2.3826940772829517e-18,1.7629258226616884e-19,1.2276395020395065e-20,8.073913380279996e-22],[3.7099660707006376e-08,4.3919326779508635e-08,2.5996292526753276e-08,1.0258311844188505e-08,3.035999127115556e-09,7.188154027560132e-10,1.4182469581553955e-10,2.398499086061822e-11,3.5492395056192573e-12,4.668512586411615e-13,5.526679380605189e-14,5.9478132217314536e-15,5.867617734020882e-16,5.3432340343383015e-17,4.370109781610186e-18,3.8857779725505563e-19,2.875038971327353e-20,2.002075961299146e-21,1.3167210622837972e-22],[5.646982101321949e-09,6.6850113316307855e-09,3.956925637640173e-09,1.5614294651209971e-09,4.621129251247537e-10,1.0941172065088872e-10,2.1587300356214124e-11,3.6507830936767265e-12,5.402338344768642e-13,7.105996796969065e-14,8.412222361949704e-15,9.053235033704909e-16,8.93116855787246e-17,8.132998086795001e-18,6.87714800513004e-19,5.2496856402098904e-20,4.376129943588016e-21,3.0473828880079487e-22,2.004196299764545e-23],[8.058127986791512e-10,9.539374472396833e-10,5.64645197208201e-10,2.2281279179806387e-10,6.594256946793124e-11,1.5612828807329624e-11,3.080463618238869e-12,5.209592821973867e-13,7.709026348765331e-14,1.014011212295193e-14,1.2004069293945793e-15,1.2918781268851718e-16,1.2744594903903938e-17,1.160562196299198e-18,9.813549576591146e-20,7.744985309076207e-21,5.542641658608587e-22,4.348553067058214e-23,2.8599471371400254e-24],[1.0822384810598986e-10,1.2811757465494114e-10,7.583408473606076e-11,2.992463978625201e-11,8.856348066838813e-12,2.096864701229499e-12,4.137184557787749e-13,6.996689345013032e-14,1.0353527493996092e-14,1.3618571906165594e-15,1.61219401584491e-16,1.7350434543189752e-17,1.7116495361122368e-18,1.5586809623242097e-19,1.3179985481720794e-20,1.0401821800876207e-21,7.696179056440538e-23,5.183730657501046e-24,3.8410221960775954e-25],[1.3727397177051447e-11,1.6250769709523728e-11,9.618994509514806e-12,3.795719916776286e-12,1.123362452725236e-12,2.6597182676526464e-13,5.247713568999684e-14,8.87478455482142e-15,1.3132686240690069e-15,1.7274154339539025e-16,2.0449492389417035e-17,2.2007746937212866e-18,2.171101233354506e-19,1.9770718761707893e-20,1.671783979794924e-21,1.31939440081356e-22,9.762035679048912e-24,6.797938101459942e-25,4.3243504923418295e-26]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.11719943985333349, "-10": 6.401953853823653e-08, "-11": 6.753813049567713e-09, "-12": 6.550889597028237e-10, "-13": 5.879228088520951e-11, "-14": 4.908903973897903e-12, "-15": 3.831367804718613e-13, "-16": 2.8057844300779687e-14, "-17": 1.9191922381010985e-15, "-18": 1.0974225515800811e-16, "-2": 0.05352309855023659, "-3": 0.017596250189880647, "-4": 0.004630836001261084, "-5": 0.0010106363942256663, "-6": 0.00018785093461220448, "-7": 3.0355263295043567e-05, "-8": 4.333840554796581e-06, "-9": 5.538133957997391e-07, "0": 0.19757720760579248, "1": 0.21352564306742924, "10": 4.18322179184187e-05, "11": 8.511368282276518e-06, "12": 1.5922183467268183e-06, "13": 2.755971034170759e-07, "14": 4.4380365238084343e-08, "15": 6.680549353214468e-09, "16": 9.435493678436071e-10, "17": 1.244746178155136e-10, "18": 1.3727397177051447e-11, "2": 0.182693725669055, "3": 0.1158389224576982, "4": 0.05879572873648807, "5": 0.02474761243956924, "6": 0.008871636284647643, "7": 0.0027648805183595744, "8": 0.0007613200884124131, "9": 0.00018763325488107985} |
| Raw goal margin distribution | {"-1": 0.10855763474147216, "-10": 5.929900082840549e-08, "-11": 6.255814627311176e-09, "-12": 6.067853916331444e-10, "-13": 5.4457179675446005e-11, "-14": 4.5469415659857566e-12, "-15": 3.54885848622978e-13, "-16": 2.5988974154218227e-14, "-17": 1.777678888595146e-15, "-18": 1.0165031220334483e-16, "-2": 0.04957652519431508, "-3": 0.0162987750054361, "-4": 0.004289377183045143, "-5": 0.000936116219310308, "-6": 0.0001739995785901005, "-7": 2.81169909121441e-05, "-8": 4.014280960422225e-06, "-9": 5.129774716619725e-07, "0": 0.2061877393378711, "1": 0.2155293810412518, "10": 4.222477406468862e-05, "11": 8.591239493955766e-06, "12": 1.6071598231608504e-06, "13": 2.7818332385251987e-07, "14": 4.479683335798871e-08, "15": 6.743240045689304e-09, "16": 9.524036940564427e-10, "17": 1.2564269540521663e-10, "18": 1.385621592973267e-11, "2": 0.18440813500389355, "3": 0.11692596214267821, "4": 0.059347471528011564, "5": 0.024979845580723848, "6": 0.008954888273767645, "7": 0.0027908263298702307, "8": 0.0007684643636829209, "9": 0.00018939401706662408} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-05T13:34:00Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.7, "draw": 4.85, "home": 1.62}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-05T13:33:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.99, "home": 1.63}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.85 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-11-05T13:34:00Z |
| Market reference home last update utc | 2026-11-05T13:34:00Z |
| Market reference draw last update utc | 2026-11-05T13:34:00Z |
| Market reference away last update utc | 2026-11-05T13:34:00Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.45 |
| Market reference over 2 5 last update utc | 2026-11-05T13:33:40Z |
| Market reference under 2 5 last update utc | 2026-11-05T13:33:40Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0082 |
| Raw ev home | 0.0007 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0289 |
| Raw edge prob away | -0.0205 |
| Raw ev away | -0.1133 |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 10.72072662191211, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,547.4698 |
| Elo away rating | 1,475.4921 |
| Elo rating diff | 131.9777 |
| Elo home expectancy | 0.6813 |

</details>


---
