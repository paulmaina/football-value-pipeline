# La Liga — football model report

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

## 2026-11-27 — Levante UD vs Real Racing Club de Santander

Research leans **Levante UD win** at **64.2%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote). Only one view is available.

**Fixture source:** football-data.org

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle 1X2 or O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Levante UD win | 64.2% | — |
| Draw | 18.1% | — |
| Real Racing Club de Santander win | 17.8% | — |
| Levante UD expected goals | 2.83 | — |
| Real Racing Club de Santander expected goals | 1.56 | — |
| Expected total goals | 4.39 | — |
| Most likely score | 2-1 | — |
| Most likely score probability | 7.9% | — |
| Over 1.5 | 93.5% | — |
| Under 1.5 | 6.5% | — |
| Over 2.5 | 81.3% | — |
| Under 2.5 | 18.7% | — |
| Over 3.5 | 64.1% | — |
| Under 3.5 | 35.9% | — |
| BTTS Yes | 75.1% | — |
| BTTS No | 24.9% | — |
| Double Chance 1X | 82.2% | — |
| Double Chance X2 | 35.8% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 2-1 (7.95%) | — |
| 2 | 3-1 (7.38%) | — |
| 3 | 2-2 (6.48%) | — |
| 4 | 3-2 (5.92%) | — |
| 5 | 1-1 (5.89%) | — |

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
| League | La Liga |
| Training matches | 2,029 |
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
| Training sha256 | 4f6d95381b8cfd91e9023a94d1b173af4893896e324bce797e4744fa47776118 |
| Training as of utc | 2026-11-24T16:31:11.442282+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 129, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 129, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 287, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T16:31:11.442282+00:00', 'observations': 1222, 'observations_sha256': '75490ae45f9f75061afffb0ea8fc0037b3ff850230a9cc5b781378654644af46', 'eligible_training_matches': 356, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 327, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 50, 'retrospective_eligible_training_matches': 356, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '1dbad689d7a4cd7380d2dda26e8a5d145c84af2d92b37e29f5b1409df2e19cfd', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 296, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-09T00:00:00+00:00', 'audit_origin_utc': '2026-10-23T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 15, 'selected_ridge': 100.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8952429070490318, 'audit_candidate_poisson_score': 0.8915402222885241, 'audit_gain': 0.003702684760507613, 'audit_gain_lower95': -0.01156682491656295, 'audit_baseline_briers': [0.5455469722916333, 0.19765564273440522, 0.16234436270737604, 0.23199920913785804], 'audit_candidate_briers': [0.5429958888588804, 0.19682851871692997, 0.16600724404619635, 0.2338107027776007], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2029, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1650, 'tuning_matches': 250, 'audit_matches': 115, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.7949635929533156, 'audit_candidate_poisson_score': 0.7996383655023083, 'audit_gain': -0.004674772548992623, 'audit_gain_lower95': -0.013813793914599394, 'audit_baseline_briers': [0.5433894114865379, 0.19395445083491153, 0.19963971369955807, 0.2540491251783392], 'audit_candidate_briers': [0.5523965859420397, 0.1910833424526641, 0.2002061771832245, 0.24984601360867045], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1846.080 |
| Base scoring parameter | 0.084 |
| Home-advantage parameter | 0.280 |
| Dixon-Coles low-score adjustment | -0.028 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2029, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-23'} |
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
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261124T163111442282Z_f31393a3e9fdbc004173eb5b4c446f3c6c8f6bcab11c708d687542416c057d0e.json |
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

### 2026-11-27 — Levante UD vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Levante UD win** at **62.3%**. Expected goals are 2.79 for Levante UD and 1.60 for Real Racing Club de Santander (4.39 combined). The most likely exact score is 2-1 at 7.7%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 81.4%; Under 3.5 goals: 36.1%; Double Chance 1X: 79.7%; Double Chance X2: 37.7%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 55.3%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Levante UD win | 62.3% | 1.61 |
| Draw | 17.4% | 5.75 |
| Real Racing Club de Santander win | 20.3% | 4.92 |

| Measure | Benchmark estimate |
| --- | --- |
| Levante UD expected goals | 2.79 |
| Real Racing Club de Santander expected goals | 1.60 |
| Expected total goals | 4.39 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 93.5% |
| Under 1.5 | 6.5% |
| Over 2.5 | 81.4% |
| Under 2.5 | 18.6% |
| Over 3.5 | 63.9% |
| Under 3.5 | 36.1% |
| Over 4.5 | 44.7% |
| Under 4.5 | 55.3% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-1 | 7.72% |
| 2 | 3-1 | 7.17% |
| 3 | 2-2 | 6.19% |
| 4 | 3-2 | 5.75% |
| 5 | 1-1 | 5.69% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:00:00+00:00 |
| Fixture id | fdorg:564765 |
| Matched home-team name | Levante |
| Matched away-team name | Santander |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7872 |
| Dc lambda away | 1.6040 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T16:31:11.442282+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 71.67 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 15.33 |
| Fair Over 2.5 odds | 1.23 |
| Fair Under 2.5 odds | 5.37 |
| Fair Over 3.5 odds | 1.56 |
| Fair Under 3.5 odds | 2.77 |
| Fair Over 4.5 odds | 2.24 |
| Fair Under 4.5 odds | 1.81 |
| Score matrix json | [[0.013952376447383197,0.01830209453005515,0.015933797570507578,0.008519151660436985,0.0034161321881542362,0.001095879927212831,0.0002929611494134651,6.712901889634295e-05,1.3459180640954114e-05,2.3986916405861605e-06,3.8474477504219166e-07,5.6102001387152355e-08,7.498862969676436e-09,9.252314237681501e-10,1.0600360807904375e-10,1.1335161122548764e-11,1.1363340597773528e-12,1.0721496590900422e-13,9.55391153935159e-15,8.065400241280535e-16],[0.032957733817245136,0.05694067330048783,0.04441006091611297,0.02374424819440953,0.009521310779938012,0.0030543939138745397,0.000816529922257071,0.0001870993907907744,3.7512904849003914e-05,6.685540054467311e-06,1.0723456741038297e-06,1.5636531643472629e-07,2.0900539234998305e-08,2.5787690416689883e-09,2.954491339109019e-10,3.159292025135915e-11,3.1671460988793408e-12,2.988253833443282e-13,2.662829068665285e-14,2.247956988552922e-15],[0.04811127033793368,0.07716940172701416,0.06188899732928004,0.033089522571593755,0.013268713558936607,0.004256543965013231,0.0011379002220532908,0.00026073807281716413,5.227725475087556e-05,9.31683861810692e-06,1.4944000794333e-06,2.1790766442541996e-07,2.912658506230526e-08,3.5937223917379614e-09,4.1173216794475694e-10,4.402727933100208e-11,4.413673217544852e-12,4.1643724350326603e-13,3.7108668107942626e-14,3.1327091472286395e-15],[0.044697953872464724,0.07169451844717019,0.05749820215526783,0.030741943481812885,0.012327347468451152,0.003954557933471744,0.0010571704151553652,0.000242239672112501,4.8568377118725665e-05,8.655843420143348e-06,1.3883779278397266e-06,2.024479225871604e-07,2.7060161713311674e-08,3.3387610962684457e-09,3.825212953500877e-10,4.0903706903694505e-11,4.100539447415177e-12,3.8689256322149294e-13,3.447594552600336e-14,2.9104550342390305e-15],[0.03114509967755494,0.049956043396137885,0.04006418822918871,0.021420687326196546,0.008589575862023564,0.0027554975194181443,0.0007366260668244859,0.00016879024832610416,3.384197296493336e-05,6.0313075377650875e-06,9.674082414614358e-07,1.4106374413651328e-07,1.8855257586433565e-08,2.3264162704074436e-09,2.665371194945254e-10,2.8501305279699814e-11,2.8572160190125835e-12,2.6958297644718737e-13,2.4022503646342412e-14,2.0279767706381988e-15],[0.017361282114927296,0.027847108268236827,0.02233306946369356,0.01194058133112198,0.004788106358048686,0.0015360031047220062,0.00041061910514820257,9.408912316148292e-05,1.8864606183725514e-05,3.36204516181043e-06,5.392645255337395e-07,7.863347632522945e-08,1.0510528131127016e-08,1.296819390705235e-09,1.4857637874183295e-10,1.5887545929452652e-11,1.5927042739604799e-12,1.5027423755058113e-13,1.3390917583467556e-14,1.1304595972425865e-15],[0.008064781720469488,0.012935729529820592,0.010374310444383066,0.005546720651939309,0.002224203971598009,0.0007135146862739806,0.00019074360011853486,4.3706924151373806e-05,8.76311611707269e-06,1.5617602539301397e-06,2.5050285222211925e-07,3.6527361187191707e-08,4.882422541334786e-09,6.024074286493879e-10,6.90177174380709e-11,7.380191690151898e-12,7.398539019019851e-13,6.980641844494857e-14,6.2204407849929614e-15,5.251288375604794e-16],[0.003211120852625603,0.005150566038470978,0.004130696372725974,0.0022085148695251385,0.0008856021156236913,0.00028409719781177334,7.594759202110808e-05,1.7402605601882512e-05,3.4891737771513415e-06,6.218396346014163e-07,9.974168679246156e-08,1.4543948647967892e-08,1.9440140325207375e-09,2.398580796059052e-10,2.748049970199434e-11,2.9385404656979784e-12,2.9458457459101296e-13,2.7794533526771467e-14,2.4767672343214837e-15,2.0908838193668235e-16],[0.0011187388948167174,0.0017944321693305545,0.0014391145356825595,0.0007694358442780525,0.00030853947190125005,9.897808263447716e-05,2.645977185574082e-05,6.062983192321233e-06,1.2156111820213964e-06,2.166459057429725e-07,3.474951880372711e-08,5.067041006380889e-09,6.772850384849761e-10,8.356538891140179e-11,9.574072505082633e-12,1.0237732131075468e-12,1.0263183372202646e-13,9.683480363020762e-15,8.628936641165214e-16,7.284537582433145e-17],[0.0003464561710427529,0.0005557079506778535,0.0004456715628951406,0.00023828240683032204,9.554991298302252e-05,3.0651984735287245e-05,8.194183009348766e-06,1.8776123290612104e-06,3.7645602343063774e-07,6.709189367023499e-08,1.0761389709517351e-08,1.5691844037253608e-09,2.097447243724291e-10,2.5878911342119682e-11,2.9649425051410668e-12,3.17046764953574e-13,3.178349506142372e-14,2.998824430332774e-15,2.672248513678779e-16,2.255908872320282e-17],[9.65629166097267e-05,0.00015488475884023413,0.0001242158447737952,6.641314574097168e-05,2.6631300148807802e-05,8.543201978500512e-06,2.283850820827039e-06,5.233208062388905e-07,1.0492435879653064e-07,1.8699591680438243e-08,2.999372688318094e-09,4.373569743790693e-10,5.845923387061182e-11,7.212869525049511e-12,8.263772442409201e-13,8.836604131902643e-14,8.858572136107774e-15,8.358206826620534e-16,7.447987132403763e-17,6.287581475641395e-18],[2.4466945981842812e-05,3.9244434209364386e-05,3.147359743132783e-05,1.682764881570417e-05,6.747793097433111e-06,2.1646618459626108e-06,5.786781988949772e-07,1.3259812717930705e-07,2.6585553843923754e-08,4.738070426941867e-09,7.599759009050209e-10,1.1081675908945171e-10,1.4812300285346807e-11,1.827584493504106e-12,2.0938604699757048e-13,2.2390035797283778e-14,2.24456979490794e-15,2.1177880920737986e-16,1.887158189085057e-17,1.5931365965540602e-18],[5.682776692523879e-06,9.115046732917393e-06,7.310165561544187e-06,3.908447362038038e-06,1.5672655413766608e-06,5.027717760345308e-07,1.3440578090917045e-07,3.0797695272882954e-08,6.174851812490471e-09,1.1004804690272149e-09,1.7651460626707961e-10,2.573868010179578e-11,3.4403556082030354e-12,4.2448103539406073e-13,4.863272058966969e-14,5.200386417986289e-15,5.213314700049551e-16,4.9188471737636725e-17,4.383178260170579e-18,3.700273636776281e-19],[1.2183703224395336e-06,1.9542387512157765e-06,1.567277627505956e-06,8.379594220179222e-07,3.360170434829081e-07,1.077927647036633e-07,2.8816197342309216e-08,6.602933732972694e-09,1.3238697560820514e-09,2.3593972039249954e-10,3.784420352744759e-11,5.518296014701474e-12,7.376019503260427e-13,9.100746412276094e-14,1.0426709806123292e-14,1.1149472906840783e-15,1.1177190756825507e-16,1.0545861189677661e-17,9.39740306385714e-19,7.933275980885606e-20],[2.4255674141035496e-07,3.890555890130562e-07,3.120182322333802e-07,1.6682342231695227e-07,6.689525969605241e-08,2.1459700119567944e-08,5.7368131827054884e-09,1.3145314363957288e-09,2.6355987844813933e-10,4.697157234845168e-11,7.5341351638541e-12,1.0985985745152338e-12,1.4684396216314314e-13,1.8118033191613803e-14,2.0757800051635565e-15,2.2196698055738746e-16,2.225187956539448e-17,2.0995010124773384e-18,1.8708625964598685e-19,1.579379877523362e-20],[4.506964776802869e-08,7.229070714359792e-08,5.7976338823626195e-08,3.099758365636238e-08,1.2429857749248187e-08,3.987442773071326e-09,1.065961506376347e-09,2.4425405978770735e-10,4.897225621672617e-11,8.727822646964441e-12,1.3999232348572739e-12,2.0413141479376024e-13,2.728518536764964e-14,3.3665251662249886e-15,3.857022201595439e-16,4.1243849054393865e-17,4.134638222618003e-18,3.901098380971806e-19,3.476263646788348e-20,2.934657447902679e-21],[7.85102309253727e-09,1.2592865470824614e-08,1.00993373027411e-08,5.3997037285832205e-09,2.1652510072538608e-09,6.946028389811645e-10,1.8568790342872832e-10,4.254846351827048e-11,8.530847998415274e-12,1.520365490797016e-12,2.438632247851859e-13,3.555919628453342e-14,4.7530129702397496e-15,5.864405011034837e-16,6.718838924371567e-17,7.184578255809401e-18,7.202439285112038e-19,6.795618557506429e-20,6.055566776815057e-21,5.112101942920992e-22],[1.2871803666925755e-09,2.0646085234233887e-09,1.6557929507367047e-09,8.852849550265187e-10,3.5499431763838776e-10,1.1388058937635013e-10,3.0443653114835296e-11,6.9758483993903856e-12,1.3986381042792316e-12,2.4926491578034426e-13,3.998153506900279e-14,5.829953468908576e-15,7.792595825814309e-16,9.614730339683771e-17,1.101558032435489e-17,1.1779163001870065e-18,1.180844627613419e-19,1.114146103463709e-20,9.928141303929276e-22,8.381324543184221e-23],[1.993099477241186e-10,3.1968869905282315e-10,2.5638676209867666e-10,1.3707954430711554e-10,5.4968130902018924e-11,1.763353054686013e-11,4.7139647774772276e-12,1.0801562980535584e-12,2.165683183663975e-13,3.859674884670054e-14,6.190832202489749e-15,9.027233099490956e-16,1.206623334901425e-16,1.4887668045371552e-17,1.7056776155150676e-18,1.823912501220825e-19,1.8284467902869102e-20,1.7251692721896384e-21,1.537296074029079e-22,1.2977834340755522e-23],[2.9237312370789894e-11,4.689599521924799e-11,3.7610063806701305e-11,2.010856709520716e-11,8.063422985014999e-12,2.5867100297073e-12,6.915041736641059e-13,1.5845103295687784e-13,3.176898918492273e-14,5.661860912682142e-15,9.081498289783289e-16,1.3242291064120947e-16,1.7700282278548873e-17,2.1839120730574664e-18,2.5021043765314964e-19,2.675546310864288e-20,2.682197781466653e-21,2.5306972120284705e-22,2.255100963901268e-23,1.9037534295189495e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.11134256606860776, "-10": 5.738586308348038e-07, "-11": 8.100895067482343e-08, "-12": 1.0533281805979606e-08, "-13": 1.2690918754803374e-09, "-14": 1.4242224707441283e-10, "-15": 1.495524838722801e-11, "-16": 1.4751785662638628e-12, "-17": 1.3697596574288571e-13, "-18": 1.1801868527904511e-14, "-19": 8.065400241280535e-16, "-2": 0.0577414537821029, "-3": 0.023543498461207443, "-4": 0.007888135765135432, "-5": 0.0022283254294653025, "-6": 0.00054204481227386, "-7": 0.00011549934550790126, "-8": 2.186179283638366e-05, "-9": 3.718487818211129e-06, "0": 0.1738590015482286, "1": 0.1946300525873456, "10": 0.00014402655139110433, "11": 3.532924978074974e-05, "12": 7.982315263641838e-06, "13": 1.671175273357158e-06, "14": 3.2588962565265226e-07, "15": 5.946344915688214e-08, "16": 1.0192126945154544e-08, "17": 1.6444791295521e-09, "18": 2.462059429433666e-10, "19": 2.9237312370789894e-11, "2": 0.17434730674362153, "3": 0.12352711281131425, "4": 0.07191664758381916, "5": 0.035301847824885206, "6": 0.014921681944700277, "7": 0.005524918476728039, "8": 0.0018171713872438295, "9": 0.0005370815613680684} |
| Raw goal margin distribution | {"-1": 0.11134256606860776, "-10": 5.738586308348038e-07, "-11": 8.100895067482343e-08, "-12": 1.0533281805979606e-08, "-13": 1.2690918754803374e-09, "-14": 1.4242224707441283e-10, "-15": 1.495524838722801e-11, "-16": 1.4751785662638628e-12, "-17": 1.3697596574288571e-13, "-18": 1.1801868527904511e-14, "-19": 8.065400241280535e-16, "-2": 0.0577414537821029, "-3": 0.023543498461207443, "-4": 0.007888135765135432, "-5": 0.0022283254294653025, "-6": 0.00054204481227386, "-7": 0.00011549934550790126, "-8": 2.186179283638366e-05, "-9": 3.718487818211129e-06, "0": 0.1738590015482286, "1": 0.1946300525873456, "10": 0.00014402655139110433, "11": 3.532924978074974e-05, "12": 7.982315263641838e-06, "13": 1.671175273357158e-06, "14": 3.2588962565265226e-07, "15": 5.946344915688214e-08, "16": 1.0192126945154544e-08, "17": 1.6444791295521e-09, "18": 2.462059429433666e-10, "19": 2.9237312370789894e-11, "2": 0.17434730674362153, "3": 0.12352711281131425, "4": 0.07191664758381916, "5": 0.035301847824885206, "6": 0.014921681944700277, "7": 0.005524918476728039, "8": 0.0018171713872438295, "9": 0.0005370815613680684} |
| Research history json | {"away": [{"away": "Sociedad", "away_goals": 2.0, "away_xg": 3.69, "date": "2026-11-22T00:00:00+00:00", "home": "Santander", "home_goals": 3.0, "home_xg": 3.05, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 2.31, "date": "2026-11-07T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.36, "date": "2026-11-01T00:00:00+00:00", "home": "Santander", "home_goals": 0.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-10-24T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.28, "date": "2026-10-18T00:00:00+00:00", "home": "Osasuna", "home_goals": 2.0, "home_xg": 3.65, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-11T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.61, "date": "2026-09-19T00:00:00+00:00", "home": "Celta", "home_goals": 5.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-09-16T00:00:00+00:00", "home": "Barcelona", "home_goals": 7.0, "home_xg": 6.74, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.98, "date": "2026-09-12T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 0.48, "date": "2026-09-05T00:00:00+00:00", "home": "Vallecano", "home_goals": 3.0, "home_xg": 1.61, "source": "pipeline training history"}], "h2h": [], "home": [], "teams": {"away": "Santander", "home": null}} |
| Unadjusted home-win probability | 62.3% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 20.3% |
| Raw p over 1 5 | 93.5% |
| Raw p under 3 5 | 36.1% |
| Raw p btts yes | 75.1% |
| P home draw | 79.7% |
| P draw away | 37.7% |
| P home away | 82.6% |
| Raw p home draw | 79.7% |
| Raw p draw away | 37.7% |
| Raw p home away | 82.6% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8138 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.01461751547454114, "mu": 10.442937166769775, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-23 |
| Elo home rating | 1,462.0242 |
| Elo away rating | 1,414.7133 |
| Elo rating diff | 107.3109 |
| Elo home expectancy | 0.6497 |
| Research p home | 0.6418 |
| Research p draw | 0.1806 |
| Research p away | 0.1776 |
| Research p over 1 5 | 0.9350 |
| Research v4 p home | 0.6243 |
| Research v4 p draw | 0.1707 |
| Research v4 p away | 0.2050 |
| Research v4 p over 1 5 | 0.9332 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.787161109559538, 1.6039776373597305], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T16:35:22.243602+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}, "home": {"matches": 0, "venue_matches": 0, "xg_matches": 0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T16:35:21.105786+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T16:35:21.159583+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T16:35:21.553171+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Levante+UD%22+%22Real+Racing+Club+de+Santander%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T16:35:21.826042+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T16:35:22.061091+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T16:35:22.243203+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Levante+UD_vs_Real+Racing+Club+de+Santander&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 2.411704945971278, "goals_for": 1.5624668612378825, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 1.5672951587760322, "results": "WWLWLDLLWL", "xg_against": 2.7459202910925207, "xg_for": 1.7112432801849509, "xg_matches": 10}, "venue": {"goals_against": 3.332473227681091, "goals_for": 1.156813568361292, "last_match": "2026-11-07T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 3.1444041299909373, "xg_for": 1.19042948522948, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [2.787161109559538, 1.6039776373597305], "h2h": [], "margin_distribution": {"-1": 0.09744453156177108, "-10": 4.992951593361009e-07, "-11": 7.04831726169156e-08, "-12": 9.164655430899332e-09, "-13": 1.1041943017539368e-09, "-14": 1.2391682328203072e-10, "-15": 1.3012060331913907e-11, "-16": 1.2835034235181632e-12, "-17": 1.1917819645113642e-13, "-18": 1.0268410215477095e-14, "-19": 7.017434403175937e-16, "-2": 0.05023890348132178, "-3": 0.020484408848948317, "-4": 0.0068632025242674555, "-5": 0.0019387912642161598, "-6": 0.00047161502218390954, "-7": 0.00010049210906646425, "-8": 1.9021213154424507e-05, "-9": 3.235331609428281e-06, "0": 0.18061451806001547, "1": 0.2010650850151577, "10": 0.00014829013374894075, "11": 3.637509281889739e-05, "12": 8.218613766966646e-06, "13": 1.720646661399975e-06, "14": 3.3553685559125893e-07, "15": 6.122373092654648e-08, "16": 1.0493841956813663e-08, "17": 1.693160238256488e-09, "18": 2.534943165424629e-10, "19": 3.01028172933937e-11, "2": 0.17950846691852457, "3": 0.127183855361975, "4": 0.0740455783046588, "5": 0.03634687968971469, "6": 0.015363404802563548, "7": 0.0056884712711145115, "8": 0.0018709646621156207, "9": 0.0005529806539148996}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T16:35:22.243602+00:00", "p_over_1_5": 0.9349802926112343, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.11290832655021699, "-10": 5.738586308348037e-07, "-11": 8.100895067482342e-08, "-12": 1.0533281805979602e-08, "-13": 1.2690918754803372e-09, "-14": 1.4242224707441278e-10, "-15": 1.4955248387228005e-11, "-16": 1.4751785662638624e-12, "-17": 1.369759657428857e-13, "-18": 1.180186852790451e-14, "-19": 8.065400241280533e-16, "-2": 0.05774145378210289, "-3": 0.02354349846120744, "-4": 0.007888135765135428, "-5": 0.002228325429465302, "-6": 0.0005420448122738599, "-7": 0.00011549934550790123, "-8": 2.1861792836383655e-05, "-9": 3.7184878182111277e-06, "0": 0.17072748058501003, "1": 0.19619581306895478, "10": 0.0001440265513911043, "11": 3.5329249780749734e-05, "12": 7.982315263641835e-06, "13": 1.6711752733571578e-06, "14": 3.258896256526522e-07, "15": 5.946344915688213e-08, "16": 1.0192126945154543e-08, "17": 1.6444791295520996e-09, "18": 2.462059429433666e-10, "19": 2.923731237078989e-11, "2": 0.17434730674362148, "3": 0.12352711281131422, "4": 0.07191664758381915, "5": 0.0353018478248852, "6": 0.014921681944700275, "7": 0.005524918476728038, "8": 0.001817171387243829, "9": 0.0005370815613680681}, "p_over_1_5": 0.9332220347237072, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "home team 'Levante UD' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: home form/venue evidence is thin", "Research review: home xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
