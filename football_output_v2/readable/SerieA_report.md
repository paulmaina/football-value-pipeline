# Serie A — football model report

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

## 2026-11-27 — Venezia FC vs Bologna FC 1909

Research leans **Bologna FC 1909 win** at **58.2%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Venezia FC win | 15.6% | — |
| Draw | 26.2% | — |
| Bologna FC 1909 win | 58.2% | — |
| Venezia FC expected goals | 0.76 | — |
| Bologna FC 1909 expected goals | 1.64 | — |
| Expected total goals | 2.40 | — |
| Most likely score | 0-1 | — |
| Most likely score probability | 14.7% | — |
| Over 1.5 | 69.7% | — |
| Under 1.5 | 30.3% | — |
| Over 2.5 | 43.0% | — |
| Under 2.5 | 57.0% | — |
| Over 3.5 | 22.4% | — |
| Under 3.5 | 77.6% | — |
| BTTS Yes | 44.1% | — |
| BTTS No | 55.9% | — |
| Double Chance 1X | 41.8% | — |
| Double Chance X2 | 84.4% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 0-1 (14.74%) | — |
| 2 | 1-1 (12.21%) | — |
| 3 | 0-2 (12.05%) | — |
| 4 | 0-0 (9.61%) | — |
| 5 | 1-2 (9.53%) | — |

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
| League | Serie A |
| Training matches | 2,020 |
| Training data through | 2026-11-23 |
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
| Training sha256 | 9c4c07c85e419e74e3984551571def1749c90a2698793624852f2b1119cf00c5 |
| Training as of utc | 2026-11-24T15:47:01.195795+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 120, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 120, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 469, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T15:47:01.195795+00:00', 'observations': 1400, 'observations_sha256': 'bf01b8a10efbe5bbd065ec9ba202d782d13e5caf450aca8fab7056d7f90e8604', 'eligible_training_matches': 524, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 476, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 56, 'retrospective_eligible_training_matches': 524, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'd0c3910ee6fa9ec1316aa103e88d490fda33db8a9f5e8306a0fbbfb6c0e8c85d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 463, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-11T00:00:00+00:00', 'audit_origin_utc': '2026-10-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 12, 'selected_ridge': 100.0, 'proposed_weight': 0.1, 'audit_baseline_poisson_score': 0.7094780779673389, 'audit_candidate_poisson_score': 0.7070100099803158, 'audit_gain': 0.002468067987023037, 'audit_gain_lower95': -0.010614842818177508, 'audit_baseline_briers': [0.5007532400208159, 0.1358907727526044, 0.23200423255135286, 0.24981366604730523], 'audit_candidate_briers': [0.5031315230734997, 0.13150955786368718, 0.23122434572190703, 0.24837029371690855], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2019, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1640, 'tuning_matches': 260, 'audit_matches': 119, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7914041527938047, 'audit_candidate_poisson_score': 0.7919836238113748, 'audit_gain': -0.0005794710175700546, 'audit_gain_lower95': -0.004659587474034871, 'audit_baseline_briers': [0.5234850644280002, 0.14284282552626335, 0.21194126949690395, 0.24164736411874121], 'audit_candidate_briers': [0.528160446595363, 0.1411986936591641, 0.21182952260223228, 0.24228022472550598], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1833.550 |
| Base scoring parameter | 0.148 |
| Home-advantage parameter | 0.118 |
| Dixon-Coles low-score adjustment | -0.019 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 2020, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-23'} |
| Training data health | {'training_end': '2026-11-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261124T154701195795Z_28856c8b2175fb0dc9a29f13ee7b26681c8a3b83777d40880359dcf2f197af25.json |
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

### 2026-11-27 — Venezia FC vs Bologna FC 1909

The model's most likely 1X2 outcome is **Bologna FC 1909 win** at **56.7%**. Expected goals are 0.79 for Venezia FC and 1.61 for Bologna FC 1909 (2.40 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 43.2%; Under 3.5 goals: 77.8%; Double Chance 1X: 43.3%; Double Chance X2: 82.0%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 90.4%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Venezia FC win | 18.0% | 5.54 |
| Draw | 25.2% | 3.96 |
| Bologna FC 1909 win | 56.7% | 1.76 |

| Measure | Benchmark estimate |
| --- | --- |
| Venezia FC expected goals | 0.79 |
| Bologna FC 1909 expected goals | 1.61 |
| Expected total goals | 2.40 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 69.5% |
| Under 1.5 | 30.5% |
| Over 2.5 | 43.2% |
| Under 2.5 | 56.8% |
| Over 3.5 | 22.2% |
| Under 3.5 | 77.8% |
| Over 4.5 | 9.6% |
| Under 4.5 | 90.4% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 0-1 | 14.35% |
| 2 | 0-2 | 11.75% |
| 3 | 1-1 | 11.75% |
| 4 | 1-2 | 9.30% |
| 5 | 0-0 | 9.25% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T19:45:00+00:00 |
| Fixture id | fdorg:558515 |
| Matched home-team name | Venezia |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 0.7912 |
| Dc lambda away | 1.6137 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T15:47:01.195795+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.81 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.32 |
| Fair Under 2.5 odds | 1.76 |
| Fair Over 3.5 odds | 4.50 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.37 |
| Fair Under 4.5 odds | 1.11 |
| Score matrix json | [[0.09249665013691534,0.14346365856768456,0.11753930492502107,0.0632227388174963,0.02550496644166264,0.0082312576184734,0.0022137388462703505,0.0005103167087463436,0.00010293456733001634,1.8455685298204375e-05,2.9781160575620204e-06,4.3687820109245414e-07,5.87476598154661e-08,7.292201509211638e-09,8.405084185891201e-10,9.041953116238785e-11],[0.0692110006828831,0.11747715384632529,0.09299528400163647,0.05002085519771335,0.020179135815101463,0.006512443989768899,0.0017514760092012629,0.0004037547039343114,8.14402410201995e-05,1.4601853370208152e-05,2.356239461680349e-06,3.456512900993704e-07,4.6480241757902473e-08,5.7694772891407475e-09,6.649972887139527e-10,7.153853755647917e-11],[0.028256336095448382,0.0455960572008191,0.03678821672487218,0.019787864315189856,0.00798271041006251,0.002576272587113059,0.0006928703934467949,0.00015972224518138656,3.2217130889392234e-05,5.77638051364594e-06,9.321101484078214e-07,1.3673698304081252e-07,1.8387224960612846e-08,2.282360693671336e-09,2.630677957629636e-10,2.83000934086276e-11],[0.007451992340542713,0.012024965581938432,0.009702089765988206,0.005218617616041396,0.0021052657581510995,0.0006794357032513216,0.0001827294539360341,4.212325843256468e-05,8.496565577753237e-06,1.5233943706765163e-06,2.458237212005739e-07,3.6061396879165494e-08,4.8492295358984835e-09,6.019228519275106e-10,6.93783933078586e-11,7.463532377494171e-12],[0.0014739753321853853,0.0023784917949693824,0.0019190359211605692,0.0010322224289340746,0.0004164134440029887,0.0001343897605677816,3.6143180945057775e-05,8.331817989542992e-06,1.6805878881233066e-06,3.0132152865360205e-07,4.8622983567006074e-08,7.132805163372714e-09,9.59158891929108e-10,1.1905801765158722e-10,1.372277850663916e-11,1.4762579069682945e-12],[0.00023323730681481538,0.00037636519989604696,0.0003036623206365064,0.00016333569097216796,6.589197802702685e-05,2.1265420888587133e-05,5.719185388840399e-06,1.3184011606700517e-06,2.659310399111744e-07,4.768018859873983e-08,7.69395083407215e-09,1.128673072074602e-09,1.5177434240323568e-10,1.883937321433708e-11,2.171450112505815e-12,2.3359849440279204e-13],[3.07556262432904e-05,4.9629056247741005e-05,4.004215691395285e-05,2.153811297314502e-05,8.688786010718992e-06,2.8041454674956047e-06,7.541552020017138e-07,1.738497751068729e-07,3.5066755750577445e-08,6.287304890365376e-09,1.0145558590884247e-09,1.4883145252210498e-10,2.0013586214066972e-11,2.4842368879608532e-12,2.863363026190524e-13,3.0803253917487244e-14],[3.476196687649613e-06,5.609391906861606e-06,4.525819507934597e-06,2.434374653379187e-06,9.820619132002522e-07,3.169423736875608e-07,8.523942235590163e-08,1.9649608419434564e-08,3.963467991921271e-09,7.106312276408089e-10,1.14671562493971e-10,1.6821878318549604e-11,2.2620629329733484e-12,2.807842692896053e-13,3.2363551918743116e-14,3.481579870615028e-15],[3.437891461283309e-07,5.547580379472192e-07,4.4759481812169805e-07,2.4075495682252353e-07,9.712402862121957e-08,3.134498931232966e-08,8.430014427066661e-09,1.9433083646486633e-09,3.9197933807677807e-10,7.028005746359149e-11,1.1340796306223709e-11,1.6636513129293254e-12,2.237136600982348e-13,2.776902254360315e-14,3.200692848984753e-15,3.443215325383714e-16],[3.022229627903673e-08,4.8768444189798424e-08,3.93477902329877e-08,2.1164622902379033e-08,8.538114719038972e-09,2.755519086419467e-09,7.410774787993442e-10,1.7083506509544908e-10,3.445866695918021e-11,6.178277421182823e-12,9.96962556458828e-13,1.462505825171981e-13,1.9666532795752507e-14,2.4411580067124884e-15,2.8137097598800514e-16,3.026909804692376e-17],[2.3911414377033073e-09,3.858484037013247e-09,3.1131364354142692e-09,1.6745122993961972e-09,6.75522459182553e-10,2.1801241735857775e-10,5.863290637299929e-11,1.3516206690284284e-11,2.7263165476696792e-12,4.888157742555172e-13,7.887813879453196e-14,1.1571120371408961e-14,1.5559857222527937e-15,1.9314065390459093e-16,2.226163736336004e-17,2.3948443213465352e-18],[1.7198492741652206e-10,2.775248199792488e-10,2.239150455260051e-10,1.204407534112009e-10,4.8587540359943125e-11,1.568073271789783e-11,4.21722278229835e-12,9.721649208706019e-13,1.960926886933955e-13,3.5158499672915395e-14,5.673378730936945e-15,8.32262895797608e-16,1.1191562627086885e-16,1.3891809501183627e-17,1.6011876276912537e-18,1.7225126054285695e-19],[1.1339318352063044e-11,1.8297779529959967e-11,1.4763177350343454e-11,7.940905438674679e-12,3.2034760043290797e-12,1.0338628096823137e-12,2.780501315341433e-13,6.409682344873274e-14,1.2928792406448953e-14,2.31807185990528e-15,3.7405747426990654e-16,5.487279652828656e-17,7.378826353674865e-18,9.159154397212743e-19,1.0556957824451476e-19,1.1356878240319398e-20],[6.901148979698231e-13,1.1136092894944798e-12,8.984921592741991e-13,4.83286294330201e-13,1.9496467488048952e-13,6.292125375322011e-14,1.692222867340786e-14,3.900955189820923e-15,7.868508472404107e-16,1.410786676426806e-16,2.2765269275966713e-17,3.3395776713992383e-18,4.490779637805041e-19,5.574293538704932e-20,6.425001614464375e-21,6.911835989372134e-22],[3.90005897367104e-14,6.293360591740611e-14,5.077665210327973e-14,2.7312046944639985e-14,1.1018074411280993e-14,3.555880347704207e-15,9.563290111022009e-16,2.2045539574215909e-16,4.4467446170895644e-17,7.972804606189652e-18,1.2865378357859184e-18,1.887301651352202e-19,2.5378825289418092e-20,3.150210725990342e-21,3.630972940311517e-22,3.906098543038841e-23],[2.0571109786695224e-15,3.3194731806349613e-15,2.678246898492925e-15,1.4405913346195278e-15,5.811553617075029e-16,1.8755717673705387e-16,5.0442183598745734e-17,1.1628060446000356e-17,2.345463807831668e-18,4.2053066368742164e-19,6.785925865058904e-20,9.954692924561925e-21,1.3386223254838713e-21,1.6615987381999566e-22,1.9151798342516022e-23,2.060296588050512e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.25849235947315047, "-10": 3.3427704518509323e-06, "-11": 4.857116581952428e-07, "-12": 6.478766843274732e-08, "-13": 7.985498891334218e-09, "-14": 9.120469561455993e-10, "-15": 9.041953116238785e-11, "-2": 0.17625980360702959, "-3": 0.08616948082633627, "-4": 0.03275413338299154, "-5": 0.010151261605034857, "-6": 0.0026512838474189713, "-7": 0.0005977864410978402, "-8": 0.00011850557053359451, "-9": 2.0953632232732456e-05, "0": 0.2524190913920935, "1": 0.12561015341980292, "10": 2.683923926958817e-09, "11": 1.9120909230806256e-10, "12": 1.2505144884995423e-11, "13": 7.557267507857221e-13, "14": 4.232006291734536e-14, "15": 2.0571109786695224e-15, "2": 0.042372687621515304, "3": 0.010156698730816378, "4": 0.0018929170028146147, "5": 0.0002876416979365644, "6": 3.6834469076363953e-05, "7": 4.072026666677415e-06, "8": 3.9579443487216994e-07, "9": 3.431283483801207e-08} |
| Raw goal margin distribution | {"-1": 0.25849235947315047, "-10": 3.3427704518509323e-06, "-11": 4.857116581952428e-07, "-12": 6.478766843274732e-08, "-13": 7.985498891334218e-09, "-14": 9.120469561455993e-10, "-15": 9.041953116238785e-11, "-2": 0.17625980360702959, "-3": 0.08616948082633627, "-4": 0.03275413338299154, "-5": 0.010151261605034857, "-6": 0.0026512838474189713, "-7": 0.0005977864410978402, "-8": 0.00011850557053359451, "-9": 2.0953632232732456e-05, "0": 0.2524190913920935, "1": 0.12561015341980292, "10": 2.683923926958817e-09, "11": 1.9120909230806256e-10, "12": 1.2505144884995423e-11, "13": 7.557267507857221e-13, "14": 4.232006291734536e-14, "15": 2.0571109786695224e-15, "2": 0.042372687621515304, "3": 0.010156698730816378, "4": 0.0018929170028146147, "5": 0.0002876416979365644, "6": 3.6834469076363953e-05, "7": 4.072026666677415e-06, "8": 3.9579443487216994e-07, "9": 3.431283483801207e-08} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Venezia", "away_goals": 0.0, "away_xg": 0.88, "date": "2026-11-22T00:00:00+00:00", "home": "Juventus", "home_goals": 4.0, "home_xg": 1.84, "source": "pipeline training history"}, {"away": "Udinese", "away_goals": 1.0, "away_xg": 1.03, "date": "2026-11-06T00:00:00+00:00", "home": "Venezia", "home_goals": 2.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-11-01T00:00:00+00:00", "home": "Como", "home_goals": 1.0, "home_xg": 1.63, "source": "pipeline training history"}, {"away": "Inter", "away_goals": 2.0, "away_xg": 2.33, "date": "2026-10-28T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 0.0, "away_xg": 1.98, "date": "2026-10-25T00:00:00+00:00", "home": "Genoa", "home_goals": 1.0, "home_xg": 0.34, "source": "pipeline training history"}, {"away": "Napoli", "away_goals": 0.0, "away_xg": 2.36, "date": "2026-10-17T00:00:00+00:00", "home": "Venezia", "home_goals": 1.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 1.0, "away_xg": 2.63, "date": "2026-10-12T00:00:00+00:00", "home": "Atalanta", "home_goals": 3.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Lazio", "away_goals": 2.0, "away_xg": 1.6, "date": "2026-09-19T00:00:00+00:00", "home": "Venezia", "home_goals": 0.0, "home_xg": 1.89, "source": "pipeline training history"}, {"away": "Fiorentina", "away_goals": 4.0, "away_xg": 3.31, "date": "2026-09-11T00:00:00+00:00", "home": "Venezia", "home_goals": 2.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Venezia", "away_goals": 2.0, "away_xg": 2.17, "date": "2026-09-06T00:00:00+00:00", "home": "Frosinone", "home_goals": 3.0, "home_xg": 1.9, "source": "pipeline training history"}], "teams": {"away": null, "home": "Venezia"}} |
| Unadjusted home-win probability | 18.0% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 56.7% |
| Raw p over 1 5 | 69.5% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 44.0% |
| P home draw | 43.3% |
| P draw away | 82.0% |
| P home away | 74.8% |
| Raw p home draw | 43.3% |
| Raw p draw away | 82.0% |
| Raw p home away | 74.8% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4316 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.02187428345353809, "mu": 9.030781199511445, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-23 |
| Elo home rating | 1,360.7604 |
| Elo away rating | 1,536.6009 |
| Elo rating diff | -115.8405 |
| Elo home expectancy | 0.3392 |
| Research p home | 0.1559 |
| Research p draw | 0.2624 |
| Research p away | 0.5818 |
| Research p over 1 5 | 0.6966 |
| Research v4 p home | 0.1826 |
| Research v4 p draw | 0.2480 |
| Research v4 p away | 0.5694 |
| Research v4 p over 1 5 | 0.6926 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [0.7911845663963951, 1.6136578021580037], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:50:03.373452+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 0, "venue_matches": 0, "xg_matches": 0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:50:02.841862+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:50:02.890201+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:50:03.100176+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Venezia+FC%22+%22Bologna+FC+1909%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:50:01.200490+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:50:01.389360+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:50:03.372885+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Venezia+FC_vs_Bologna+FC+1909&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.030972210604443, "goals_for": 0.6749458317875972, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.7096679935714522, "results": "LWLLLWLLLL", "xg_against": 1.731803085477299, "xg_for": 1.3231303025323111, "xg_matches": 10}, "venue": {"goals_against": 1.6460805251113106, "goals_for": 1.0114031125470773, "last_match": "2026-11-06T00:00:00+00:00", "matches": 5, "points_per_game": 1.3653225874357666, "results": "WLWLL", "xg_against": 2.020351136422765, "xg_for": 1.338377491547629, "xg_matches": 5}}}, "goal_rates": [0.7911845663963951, 1.6136578021580037], "h2h": [], "margin_distribution": {"-1": 0.26530246529142454, "-10": 3.426604478149648e-06, "-11": 4.978929205682502e-07, "-12": 6.641249166768285e-08, "-13": 8.185768857132733e-09, "-14": 9.349203689654464e-10, "-15": 9.268718114391376e-11, "-2": 0.18068025940076082, "-3": 0.08833054292311941, "-4": 0.03357558101721389, "-5": 0.010405847178474517, "-6": 0.0027177759392306624, "-7": 0.0006127784499557209, "-8": 0.00012147759606144867, "-9": 2.147913267643771e-05, "0": 0.2623726886394748, "1": 0.10862668048875286, "10": 2.315151101502316e-09, "11": 1.6493684348791214e-10, "12": 1.0786930160031855e-11, "13": 6.518894227746782e-13, "14": 3.6505259815526375e-14, "15": 1.7744626441688e-15, "2": 0.036550653852444284, "3": 0.008761161975600779, "4": 0.001632829023244503, "5": 0.0002481195488168736, "6": 3.1773389997691065e-05, "7": 3.512527656991851e-06, "8": 3.4141203208433976e-07, "9": 2.9598229880123436e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:50:03.373452+00:00", "p_over_1_5": 0.6965790864267244, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.2607092841962125, "-10": 3.3427704518509323e-06, "-11": 4.857116581952428e-07, "-12": 6.478766843274732e-08, "-13": 7.985498891334218e-09, "-14": 9.120469561455993e-10, "-15": 9.041953116238785e-11, "-2": 0.17625980360702959, "-3": 0.08616948082633627, "-4": 0.03275413338299154, "-5": 0.010151261605034857, "-6": 0.0026512838474189713, "-7": 0.0005977864410978402, "-8": 0.00011850557053359451, "-9": 2.0953632232732456e-05, "0": 0.24798524194596946, "1": 0.12782707814286492, "10": 2.683923926958817e-09, "11": 1.9120909230806256e-10, "12": 1.2505144884995423e-11, "13": 7.557267507857221e-13, "14": 4.232006291734536e-14, "15": 2.0571109786695224e-15, "2": 0.042372687621515304, "3": 0.010156698730816378, "4": 0.0018929170028146147, "5": 0.0002876416979365644, "6": 3.6834469076363953e-05, "7": 4.072026666677415e-06, "8": 3.9579443487216994e-07, "9": 3.431283483801207e-08}, "p_over_1_5": 0.6926117658894548, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "away team 'Bologna FC 1909' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
