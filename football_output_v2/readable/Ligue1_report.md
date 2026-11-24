# Ligue 1 — football model report

Fixtures in this report: **1**.

> Each match shows the two models the shortlists use, side by side, and the master's verdict on them: **Research** (the value shortlist's model, independent of bookmaker odds) and **Cagey** (the cagey tier's market view, built from Pinnacle's prices). Probabilities are model estimates, not guarantees. No probability here is blended or averaged. The production model (70% Pinnacle blend) is kept only as a benchmark at the end of this report.

## Quick reference

- **Research:** The value shortlist's model: team form, goal rates and xG, never bookmaker odds. Live research v5 (C6 grid) for domestic leagues and v6 (CE3n) for UCL/UEL, exactly as the forecast carries it.
- **Cagey:** The cagey tier's market view: Pinnacle's 1X2, O/U 2.5 and main AH line with the margin removed, plus the narrow-margin correction (D_pow2 for domestic leagues, D for UCL/UEL, D where D_pow2's power fit fails). Blank without Pinnacle 1X2 and O/U 2.5.
- **No-loss:** The chance a bet does not lose: a win, a half win or a refund (push) on that exact line.
- **Gap:** Research minus cagey no-loss on the same Pinnacle offer, in percentage points (the master's g). +4 or more: research too optimistic; -4 or less: research too pessimistic; -8 or less with cagey no-loss of 85% or more: flagged for inspection.
- **Cagey tier:** The master's market classes from the cagey no-loss: safe (75% or more), risky (below 50%), in between otherwise; fair price when the Pinnacle price is within its 2.70% margin of the cagey fair odds.
- **Best offer:** The fixture's master pick, or else the Pinnacle offer the master's own rule would choose for it (safe first, then chance of profit), shown with both views and the master's labels.
- **Expected goals:** A view's average goal expectation for each team, from its score grid. It is not a prediction that the team will score exactly that many goals.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-27 — Stade Brestois 29 vs Paris FC

Research leans **Stade Brestois 29 win** at **38.7%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Stade Brestois 29 win | 38.7% | — |
| Draw | 26.7% | — |
| Paris FC win | 34.6% | — |
| Stade Brestois 29 expected goals | 1.45 | — |
| Paris FC expected goals | 1.36 | — |
| Expected total goals | 2.80 | — |
| Most likely score | 1-1 | — |
| Most likely score probability | 12.6% | — |
| Over 1.5 | 77.3% | — |
| Under 1.5 | 22.7% | — |
| Over 2.5 | 53.0% | — |
| Under 2.5 | 47.0% | — |
| Over 3.5 | 31.0% | — |
| Under 3.5 | 69.0% | — |
| BTTS Yes | 57.4% | — |
| BTTS No | 42.6% | — |
| Double Chance 1X | 65.4% | — |
| Double Chance X2 | 61.3% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 1-1 (12.57%) | — |
| 2 | 2-1 (8.52%) | — |
| 3 | 1-0 (8.43%) | — |
| 4 | 1-2 (7.93%) | — |
| 5 | 0-1 (7.84%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

_No Pinnacle Asian handicap quotes in this forecast._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

_No Pinnacle offer of this match in the run's decision rows._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)._


---

## Benchmark (70% Pinnacle blend), display only

The production forecasting model blends 70% of Pinnacle's prices into its score grid, so it is neither independent research nor the cagey tier's market view. It is shown for comparison only: no list, probability or stake reads it, and its EV is not a recommendation.

- **Benchmark EV:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Probability edge:** Model probability minus the de-vigged market probability.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,779 |
| Training data through | 2026-11-22 |
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
| Training sha256 | b012bf647b3154853737559e0d2adb26161c4f5a61849359a75b0ca6c5ab885e |
| Training as of utc | 2026-11-24T16:33:54.961405+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 99, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 99, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 361, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-24T16:33:54.961405+00:00', 'observations': 1098, 'observations_sha256': '9dc5b59457cb166942eab82dd775b1f2ea483d9ab552a10718155387f4c80092', 'eligible_training_matches': 415, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 360, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 41, 'retrospective_eligible_training_matches': 415, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'a4dbb89e42d6bf57ff095f91c0c405c7535d75f7f653eeae0ddb96bfcd786b53', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 354, 'tuning_matches': 20, 'audit_matches': 41, 'tuning_origin_utc': '2025-10-05T00:00:00+00:00', 'audit_origin_utc': '2026-10-17T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 39, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1777, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1489, 'tuning_matches': 189, 'audit_matches': 95, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8570386247465478, 'audit_candidate_poisson_score': 0.8512583220862963, 'audit_gain': 0.005780302660251535, 'audit_gain_lower95': -0.001751997875908252, 'audit_baseline_briers': [0.5856033518783379, 0.1628934403909076, 0.22821994719896568, 0.24145086484005113], 'audit_candidate_briers': [0.5842469461303595, 0.1621985137454303, 0.22431109193006557, 0.240208566981081], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1602.566 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.196 |
| Dixon-Coles low-score adjustment | -0.048 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1779, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-22'} |
| Training data health | {'training_end': '2026-11-22', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261124T163354961405Z_f8708c866b420ac9ebf274321399436dbf3e6b1932c7d1a92bbc3863cae1e184.json |
| Over 1 5 in window quote fixtures | 0 |
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

### 2026-11-27 — Stade Brestois 29 vs Paris FC

The model's most likely 1X2 outcome is **Paris FC win** at **38.4%**. Expected goals are 1.39 for Stade Brestois 29 and 1.46 for Paris FC (2.84 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 54.1%; Under 3.5 goals: 68.2%; Double Chance 1X: 61.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Stade Brestois 29 win | 35.4% | 2.83 |
| Draw | 26.2% | 3.82 |
| Paris FC win | 38.4% | 2.60 |

| Measure | Benchmark estimate |
| --- | --- |
| Stade Brestois 29 expected goals | 1.39 |
| Paris FC expected goals | 1.46 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 78.2% |
| Under 1.5 | 21.8% |
| Over 2.5 | 54.1% |
| Under 2.5 | 45.9% |
| Over 3.5 | 31.8% |
| Under 3.5 | 68.2% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 1-1 | 12.33% |
| 2 | 1-2 | 8.56% |
| 3 | 2-1 | 8.16% |
| 4 | 0-1 | 7.92% |
| 5 | 1-0 | 7.52% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T19:45:00+00:00 |
| Fixture id | fdorg:559616 |
| Matched home-team name | Brest |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3877 |
| Dc lambda away | 1.4550 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T16:33:54.961405+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.65 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.58 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.29 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.0639010049873494,0.07915021620629545,0.06167890320270038,0.029914296351640113,0.010881335591436517,0.0031664716525273418,0.0007678701021277512,0.00015960743649916288,2.9028629973792855e-05,4.692966285216117e-06,6.828272404399563e-07,9.031950678956356e-08,1.0951250557900196e-08,1.225698818082499e-09,1.2738524766891712e-10,1.2356380712775814e-11],[0.07522735721083706,0.12328174228867944,0.08559048591631205,0.041511424938395165,0.015099795105447613,0.004394044532364142,0.0010655568070938877,0.00022148380299379542,4.0282404775851676e-05,6.5123282659626096e-06,9.475446590559925e-07,1.2533443482992967e-07,1.5196814599013882e-08,1.700875858345961e-09,1.7676976535592846e-10,1.7146683459947222e-11],[0.05610318710290547,0.08163021445528963,0.059386037194235325,0.028802255285565796,0.010476830270997982,0.0030487604929273077,0.0007393251189217556,0.0001536741522342904,2.7949512877295825e-05,4.5185088562491666e-06,6.574436605129023e-07,8.696194826848319e-08,1.0544146202106563e-08,1.1801344028502562e-09,1.226497986062111e-10,1.1897041719167763e-11],[0.02595106157995158,0.03775883031793336,0.027469575041969126,0.013322756498418162,0.0048461572606681574,0.0014102330969069442,0.00034198184950797367,7.108343739124926e-05,1.2928312405460312e-05,2.090079149389466e-06,3.041068039151654e-07,4.0225074388173185e-08,4.87729488339013e-09,5.458823668040838e-10,5.673282821812468e-11,5.503089542971555e-12],[0.009002932345329654,0.013099278954112462,0.009529734454056405,0.004621925582467192,0.0016812270210298235,0.0004892375259286647,0.00011864021226898642,2.4660238878292832e-05,4.485085188791048e-06,7.250894581081187e-07,1.0550061595621914e-07,1.3954867402509223e-08,1.692029273180344e-09,1.8937730164542893e-10,1.968173103953378e-11,1.909129716833589e-12],[0.002498635073247255,0.003635517470702103,0.002644841461903292,0.0012827493224784878,0.0004666005074463659,0.00013578087611290545,3.292689360556716e-05,6.844096502393724e-06,1.2447712289017269e-06,2.012382057064601e-07,2.9280186628765098e-08,3.872973804197529e-09,4.695985179898255e-10,5.2558960771671505e-11,5.462382876075869e-12,5.298516402084924e-13],[0.000577883681837286,0.000840821552473746,0.0006116982580790576,0.00029667393581599605,0.00010791524623874891,3.140336636243702e-05,7.615323546835852e-06,1.5829008917708399e-06,2.878903720293975e-07,4.6542320839530806e-08,6.771914088247995e-09,8.957403926617946e-10,1.0860862535184598e-10,1.2155823028931536e-11,1.2633385170285328e-12,1.2254395207591363e-13],[0.00011455953462960529,0.00016668428056609572,0.00012126292882415774,5.881257611524584e-05,2.1393094799363607e-05,6.2253964757162745e-06,1.5096600734696523e-06,3.1379392639973047e-07,5.70713243522907e-08,9.226539498410193e-09,1.3424627669618046e-09,1.7757137942712912e-10,2.153055012301238e-11,2.4097676972064746e-12,2.5044395116039137e-13,2.429308624333528e-14],[1.9871474941502376e-05,2.891302339103204e-05,2.103424441495341e-05,1.0201618191780668e-05,3.7108421276431946e-06,1.0798560806665823e-06,2.618653472810654e-07,5.443063438943519e-08,9.899580994385596e-09,1.6004337747375831e-09,2.32863334508409e-10,3.0801497474853737e-11,3.7346851017639785e-12,4.179978433458597e-13,4.344195981439026e-14,4.213874088237088e-15],[3.063913100845847e-06,4.457997778908096e-06,3.243196452155093e-06,1.5729517672763624e-06,5.721617466004292e-07,1.6649922576568672e-07,4.0376100443168395e-08,8.392468816938876e-09,1.5263817100075501e-09,2.4676527655294005e-10,3.590438170328494e-11,4.749174981559753e-12,5.758380112454468e-13,6.444962299591949e-14,6.698163583405649e-15,6.497224822149179e-16],[4.251726238466394e-07,6.186267529054863e-07,4.500513884784194e-07,2.1827512989597264e-07,7.939765360826397e-08,2.3104739056629235e-08,5.602904521469022e-09,1.1646048272269623e-09,2.1181270332251568e-10,3.4243086097086344e-11,4.982373740352691e-12,6.590327863604014e-13,7.990780093739196e-14,8.943535411476565e-15,9.294897381144338e-16,9.016058988722823e-17],[5.363662685256699e-08,7.804136589606765e-08,5.6775147397551434e-08,2.7535972536295764e-08,1.0016219485222351e-08,2.91472262746944e-09,7.068209057998824e-10,1.4691791297268998e-10,2.6720720699179245e-11,4.319853932863373e-12,6.285393418173577e-13,8.31386915879385e-14,1.008057589106221e-14,1.1282501381865e-15,1.1725753599911167e-16,1.1373991751484233e-17],[6.2025326824960725e-09,9.024693590212742e-09,6.565470797684793e-09,3.184256349120411e-09,1.1582743426970808e-09,3.370581525751708e-10,8.173667932075468e-11,1.698956870203726e-11,3.0899807307434475e-12,4.995473573654069e-13,7.268420925448544e-14,9.614147682545224e-15,1.1657165092532834e-15,1.3047070195834954e-16,1.3559646494970489e-17,1.315286954247485e-18],[6.620862347522843e-10,9.633363828616656e-10,7.008278815011232e-10,3.399018440684408e-10,1.2363941274032502e-10,3.597910314295181e-11,8.724940765786549e-12,1.8135429747498512e-12,3.298384405532452e-13,5.3323931666155396e-14,7.758639396944423e-15,1.026257363778558e-15,1.244338230700764e-16,1.3927029525998122e-17,1.4474176521088737e-18,1.4039964506983778e-19],[6.56259151467489e-11,9.548579686618769e-11,6.94659829335922e-11,3.3691033593841095e-11,1.2255125062864691e-11,3.566244766890369e-12,8.648151740688985e-13,1.7975818122913438e-13,3.269355013849813e-14,5.285462272332912e-15,7.690354881167403e-16,1.0172251761019639e-16,1.2333866927829565e-17,1.3804456427966326e-18,1.4346787930841473e-19,1.3916397457551955e-20],[6.071177960318627e-12,8.833572288647604e-12,6.4264299192662446e-12,3.1168214592953477e-12,1.1337448783188277e-12,3.2992007168861634e-13,8.00056930682866e-14,1.66297705049123e-14,3.0245423717379572e-15,4.889681459851288e-16,7.114493254252974e-17,9.410543161221614e-18,1.1410294376893161e-18,1.2770764633489438e-19,1.3272485799598796e-20,1.2874323404465194e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.19891292069759922, "-10": 8.192719154214764e-07, "-11": 1.0675509774936266e-07, "-12": 1.2780279304395339e-08, "-13": 1.414365625157595e-09, "-14": 1.4453193112886435e-10, "-15": 1.2356380712775814e-11, "-2": 0.11520317317237695, "-3": 0.048430786725800215, "-4": 0.016090481956793704, "-5": 0.0043993862116014455, "-6": 0.001019502981800477, "-7": 0.0002047268938115803, "-8": 3.6240372850522096e-05, "-9": 5.732545149652457e-06, "0": 0.26171648813471127, "1": 0.18944864181634274, "10": 5.101319474295948e-07, "11": 6.339697310275301e-08, "12": 7.2384518697506255e-09, "13": 7.639984615377382e-10, "14": 7.44594874353965e-11, "15": 6.071177960318627e-12, "2": 0.10478891231411055, "3": 0.042014370450596764, "4": 0.013312843744545985, "5": 0.003471517163368266, "6": 0.0007672575545452521, "7": 0.00014694439178804968, "8": 2.4808255216315973e-05, "9": 3.7426265431612054e-06} |
| Raw goal margin distribution | {"-1": 0.19891292069759922, "-10": 8.192719154214764e-07, "-11": 1.0675509774936266e-07, "-12": 1.2780279304395339e-08, "-13": 1.414365625157595e-09, "-14": 1.4453193112886435e-10, "-15": 1.2356380712775814e-11, "-2": 0.11520317317237695, "-3": 0.048430786725800215, "-4": 0.016090481956793704, "-5": 0.0043993862116014455, "-6": 0.001019502981800477, "-7": 0.0002047268938115803, "-8": 3.6240372850522096e-05, "-9": 5.732545149652457e-06, "0": 0.26171648813471127, "1": 0.18944864181634274, "10": 5.101319474295948e-07, "11": 6.339697310275301e-08, "12": 7.2384518697506255e-09, "13": 7.639984615377382e-10, "14": 7.44594874353965e-11, "15": 6.071177960318627e-12, "2": 0.10478891231411055, "3": 0.042014370450596764, "4": 0.013312843744545985, "5": 0.003471517163368266, "6": 0.0007672575545452521, "7": 0.00014694439178804968, "8": 2.4808255216315973e-05, "9": 3.7426265431612054e-06} |
| Research history json | {"away": [{"away": "Angers", "away_goals": 0.0, "away_xg": 0.46, "date": "2026-11-22T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": 3.51, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 1.0, "away_xg": 0.76, "date": "2026-11-07T00:00:00+00:00", "home": "Auxerre", "home_goals": 0.0, "home_xg": 0.81, "source": "pipeline training history"}, {"away": "Monaco", "away_goals": 1.0, "away_xg": 0.67, "date": "2026-11-01T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.15, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 1.0, "away_xg": 0.42, "date": "2026-10-24T00:00:00+00:00", "home": "Lens", "home_goals": 2.0, "home_xg": 1.06, "source": "pipeline training history"}, {"away": "Rennes", "away_goals": 3.0, "away_xg": 3.35, "date": "2026-10-18T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": 3.62, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 0.0, "away_xg": 0.97, "date": "2026-10-10T00:00:00+00:00", "home": "Lorient", "home_goals": 1.0, "home_xg": 0.55, "source": "pipeline training history"}, {"away": "Strasbourg", "away_goals": 1.0, "away_xg": 0.24, "date": "2026-09-19T00:00:00+00:00", "home": "Paris FC", "home_goals": 2.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-09-12T00:00:00+00:00", "home": "Paris FC", "home_goals": 0.0, "home_xg": 0.3, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 3.0, "away_xg": 3.29, "date": "2026-09-06T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.42, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 0.0, "away_xg": 0.65, "date": "2026-08-30T00:00:00+00:00", "home": "Paris FC", "home_goals": 3.0, "home_xg": 2.88, "source": "pipeline training history"}], "h2h": [{"away": "Brest", "away_goals": 0.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 2.0, "away_xg": null, "date": "2025-09-14T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Brest", "away_goals": 1.0, "away_xg": 1.41, "date": "2026-11-21T00:00:00+00:00", "home": "Strasbourg", "home_goals": 0.0, "home_xg": 1.86, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 0.0, "away_xg": 0.64, "date": "2026-11-08T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 2.0, "away_xg": 1.31, "date": "2026-11-02T00:00:00+00:00", "home": "Lorient", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Nice", "away_goals": 2.0, "away_xg": 0.47, "date": "2026-10-23T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": 2.46, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 1.0, "away_xg": 0.78, "date": "2026-10-17T00:00:00+00:00", "home": "Lille", "home_goals": 1.0, "home_xg": 2.17, "source": "pipeline training history"}, {"away": "Angers", "away_goals": 1.0, "away_xg": 1.39, "date": "2026-10-10T00:00:00+00:00", "home": "Brest", "home_goals": 5.0, "home_xg": 3.82, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 1.0, "away_xg": 0.34, "date": "2026-09-20T00:00:00+00:00", "home": "Auxerre", "home_goals": 2.0, "home_xg": 0.96, "source": "pipeline training history"}, {"away": "Paris SG", "away_goals": 1.0, "away_xg": 1.16, "date": "2026-09-13T00:00:00+00:00", "home": "Brest", "home_goals": 0.0, "home_xg": 1.25, "source": "pipeline training history"}, {"away": "Brest", "away_goals": 2.0, "away_xg": 2.37, "date": "2026-09-05T00:00:00+00:00", "home": "Le Havre", "home_goals": 1.0, "home_xg": 2.01, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-08-29T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 2.73, "source": "pipeline training history"}], "teams": {"away": "Paris FC", "home": "Brest"}} |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 58.1% |
| P home draw | 61.6% |
| P draw away | 64.6% |
| P home away | 73.8% |
| Raw p home draw | 61.6% |
| Raw p draw away | 64.6% |
| Raw p home away | 73.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5407 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.015570913305566664, "mu": 8.882982703112878, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-22 |
| Elo home rating | 1,519.1581 |
| Elo away rating | 1,513.5245 |
| Elo rating diff | 65.6336 |
| Elo home expectancy | 0.5933 |
| Research p home | 0.3872 |
| Research p draw | 0.2666 |
| Research p away | 0.3462 |
| Research p over 1 5 | 0.7727 |
| Research v4 p home | 0.3921 |
| Research v4 p draw | 0.2520 |
| Research v4 p away | 0.3559 |
| Research v4 p over 1 5 | 0.7709 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.3876784681956664, 1.4550013764024141], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Paris Saint-Germain drop one of this season's best kits in latest Jordan collab", "published_at_utc": "2026-11-24T13:21:57+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/soccer/story/_/id/50581189/psg-kit-nike-jordan-champions-league"}], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T16:35:24.268745+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 4.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-22", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T16:35:24.052416+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T16:35:24.102149+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T16:35:24.268244+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Stade+Brestois+29_vs_Paris+FC&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 0.9312494032006584, "goals_for": 2.213236948620373, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 2.2686762445488604, "results": "WWWLWLWDWW", "xg_against": 0.9528064296311309, "xg_for": 1.9202236507517008, "xg_matches": 10}, "venue": {"goals_against": 1.1612768438259973, "goals_for": 1.1708095557758593, "last_match": "2026-11-07T00:00:00+00:00", "matches": 4, "points_per_game": 1.514299067924793, "results": "WLLW", "xg_against": 0.9386567683674618, "xg_for": 1.226017240444295, "xg_matches": 4}}, "home": {"all": {"goals_against": 0.7849059493921307, "goals_for": 1.667360393435035, "last_match": "2026-11-21T00:00:00+00:00", "matches": 10, "points_per_game": 1.9393909626348576, "results": "WWWLDWLLWD", "xg_against": 1.3513413427138565, "xg_for": 1.7558598510679808, "xg_matches": 10}, "venue": {"goals_against": 1.1151840416711334, "goals_for": 2.021622295578943, "last_match": "2026-11-08T00:00:00+00:00", "matches": 5, "points_per_game": 1.5140209424328015, "results": "WLWLD", "xg_against": 0.909037295991237, "xg_for": 2.399795463650609, "xg_matches": 5}}}, "goal_rates": [1.445898782911896, 1.365857211351295], "h2h": [{"away": "Brest", "away_goals": 0.0, "away_xg": null, "date": "2026-05-03T00:00:00+00:00", "home": "Paris FC", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Paris FC", "away_goals": 2.0, "away_xg": null, "date": "2025-09-14T00:00:00+00:00", "home": "Brest", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.1884888380470456, "-10": 4.374302276201251e-07, "-11": 5.352344571019966e-08, "-12": 6.014347986168063e-09, "-13": 6.201818090655231e-10, "-14": 5.302570023414022e-11, "-2": 0.10110611515066431, "-3": 0.04000760347292605, "-4": 0.01249998014043033, "-5": 0.003212363967347478, "-6": 0.0006994737057456846, "-7": 0.00013195132194713995, "-8": 2.1939261484941767e-05, "-9": 3.2592686397838076e-06, "0": 0.2665785613257782, "1": 0.20260142602552225, "10": 7.845403530701657e-07, "11": 1.016209270693942e-07, "12": 1.208816091964339e-08, "13": 1.3195422369428044e-09, "14": 1.1943270730373665e-10, "2": 0.11498023234781868, "3": 0.048163815895973176, "4": 0.015930164692099964, "5": 0.00433379416734492, "6": 0.0009989586699314201, "7": 0.00019949061299660294, "8": 3.5112626419843553e-05, "9": 5.521970238799704e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T16:35:24.268745+00:00", "p_over_1_5": 0.7726720235570883, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.1946776986147956, "-10": 4.4725799538105924e-07, "-11": 5.472595975927817e-08, "-12": 6.1494726563653685e-09, "-13": 6.341154661477333e-10, "-14": 5.4217031409622224e-11, "-2": 0.10337767151821813, "-3": 0.0409064563888359, "-4": 0.012780817846833926, "-5": 0.003284536316310295, "-6": 0.0007151888180102133, "-7": 0.000134915879186131, "-8": 2.2432172018110637e-05, "-9": 3.3324947984710116e-06, "0": 0.25196729583670824, "1": 0.20608614513133386, "10": 7.904675296064724e-07, "11": 1.0238866982751536e-07, "12": 1.2179486577386327e-08, "13": 1.329511335096731e-09, "14": 1.2033501747507206e-10, "2": 0.1158489042174607, "3": 0.048527691939264574, "4": 0.016050516561845116, "5": 0.004366535839588224, "6": 0.0010065057697918503, "7": 0.0002009977580095264, "8": 3.5377901156355657e-05, "9": 5.563688542141928e-06}, "p_over_1_5": 0.7709158831411523, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
