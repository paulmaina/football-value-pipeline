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
| Training as of utc | 2026-11-24T16:32:48.720110+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 120, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 120, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 469, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T16:32:48.720110+00:00', 'observations': 1400, 'observations_sha256': 'bf01b8a10efbe5bbd065ec9ba202d782d13e5caf450aca8fab7056d7f90e8604', 'eligible_training_matches': 524, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 476, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 56, 'retrospective_eligible_training_matches': 524, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'd0c3910ee6fa9ec1316aa103e88d490fda33db8a9f5e8306a0fbbfb6c0e8c85d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 463, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-11T00:00:00+00:00', 'audit_origin_utc': '2026-10-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 12, 'selected_ridge': 100.0, 'proposed_weight': 0.1, 'audit_baseline_poisson_score': 0.7094780779673389, 'audit_candidate_poisson_score': 0.7070100099803158, 'audit_gain': 0.002468067987023037, 'audit_gain_lower95': -0.010614842818177508, 'audit_baseline_briers': [0.5007532400208159, 0.1358907727526044, 0.23200423255135286, 0.24981366604730523], 'audit_candidate_briers': [0.5031315230734997, 0.13150955786368718, 0.23122434572190703, 0.24837029371690855], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2019, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1640, 'tuning_matches': 260, 'audit_matches': 119, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7914041527938047, 'audit_candidate_poisson_score': 0.7919836238113748, 'audit_gain': -0.0005794710175700546, 'audit_gain_lower95': -0.004659587474034871, 'audit_baseline_briers': [0.5234850644280002, 0.14284282552626335, 0.21194126949690395, 0.24164736411874121], 'audit_candidate_briers': [0.528160446595363, 0.1411986936591641, 0.21182952260223228, 0.24228022472550598], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1833.466 |
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
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261124T163248720110Z_bfd064a2e516f5c0e8d1474910e08fd32de52934f483adce3e7391d8952c6c44.json |
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
| Bbs statistics cutoff utc | 2026-11-24T16:32:48.720110+00:00 |
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
| Score matrix json | [[0.09249660743201515,0.14346362577101524,0.11753926839020704,0.06322271958411428,0.025504958851338487,0.00823125522328108,0.0022137382167427776,0.0005103165670014868,0.000102934539419905,1.845568041612558e-05,2.978115289460023e-06,4.3687809130452554e-07,5.8747645440701085e-08,7.292199773141196e-09,8.405082240468935e-10,9.041951083215353e-11],[0.06921101927729713,0.117477149462888,0.09299529193102639,0.05002085979367879,0.020179137802653294,0.006512444674290536,0.0017514762048835121,0.00040375475171407834,8.144025119640231e-05,1.4601855291336156e-05,2.3562397872697885e-06,3.4565134014836954e-07,4.6480248795504746e-08,5.7694782008625315e-09,6.649973981987257e-10,7.153854980772787e-11],[0.028256349323231615,0.045596078847525576,0.03678823443339279,0.019787873971238976,0.007982714358253153,0.0025762738783592994,0.0006928707453013164,0.00015972232734825367,3.221714767614019e-05,5.776383561638469e-06,9.321106464148699e-07,1.367370570009701e-07,1.8387235027765548e-08,2.2823619583785254e-09,2.630679432747598e-10,2.830010946472e-11],[0.007451998780797572,0.012024976053843974,0.009702098279197834,0.0052186222296951796,0.002105267633290795,0.000679436312912147,0.00018272961910867269,4.2123296787201914e-05,8.496573370360442e-06,1.5233957779308053e-06,2.4582394990923893e-07,3.6061430668374143e-08,4.849234111658286e-09,6.01923423886605e-10,6.937845969148822e-11,7.463539568225158e-12],[0.0014739771898811252,0.0023784948083869304,0.001919038365166231,0.0010322237503578872,0.00041641397983877986,0.00013438993438781178,3.61432279317983e-05,8.331828876155997e-06,1.6805900951479074e-06,3.0132192635582975e-07,4.862304806414878e-08,7.1328146720354394e-09,9.591601769173632e-10,1.190581779414953e-10,1.37227970726259e-11,1.4762599140094971e-12],[0.00023323769315564252,0.00037636582580737233,0.00030366282764840154,0.0001633359647671047,6.589208891569767e-05,2.1265456816519193e-05,5.719195089234108e-06,1.3184034055499322e-06,2.659314944786441e-07,4.768027041593236e-08,7.69396408745824e-09,1.1286750237610108e-09,1.5177460585330086e-10,1.8839406040352564e-11,2.1714539104369726e-12,2.335989045186591e-13],[3.075568937001494e-05,4.9629158440939854e-05,4.004223963123468e-05,2.153815760806948e-05,8.688804074563773e-06,2.8041513158162046e-06,7.54156779854705e-07,1.7385013998747227e-07,3.506682958157682e-08,6.287318169504253e-09,1.014558008597726e-09,1.4883176883130693e-10,2.0013628881012817e-11,2.4842422005349407e-12,2.8633691684704486e-13,3.080332019815233e-14],[3.476205199548933e-06,5.609405679257226e-06,4.525830649837088e-06,2.43438066255379e-06,9.820643438838929e-07,3.169431602422747e-07,8.523963445806943e-08,1.9649657443736474e-08,3.963477906693217e-09,7.106330100133452e-10,1.1467185086639182e-10,1.6821920732944462e-11,2.2620686514621818e-12,2.807849809686853e-13,3.236363416184497e-14,3.4815887411251922e-15],[3.437901241130437e-07,5.547596197492852e-07,4.475960973259017e-07,2.407556464809264e-07,9.712430748180455e-08,3.1345079516770377e-08,8.430038742676259e-09,1.943313982798691e-09,3.919804738909479e-10,7.028026157460867e-11,1.1340829317770066e-11,1.6636561666006312e-12,2.2371431425835246e-13,2.7769103926554357e-14,3.2007022504579287e-15,3.443225461998958e-16],[3.0222394224086865e-08,4.876860256216795e-08,3.9347918272655554e-08,2.1164691913107177e-08,8.538142615438667e-09,2.755528107694244e-09,7.410799099095501e-10,1.708356266511324e-10,3.445878045694316e-11,6.178297811665322e-12,9.969658533792794e-13,1.4625106713014433e-13,1.966659809245713e-14,2.4411661279775615e-15,2.813719139164516e-16,3.026919914684016e-17],[2.391150134092278e-09,3.858498095530823e-09,3.11314779882417e-09,1.6745184226904855e-09,6.755249338761482e-10,2.1801321746233052e-10,5.86331219430996e-11,1.3516256473454024e-11,2.726326607327733e-12,4.888175811382765e-13,7.887843088531194e-14,1.1571163296542215e-14,1.5559915047510976e-15,1.931413729492981e-16,2.2261720388615308e-17,2.394853268810457e-18],[1.719856210348779e-10,2.7752594107758884e-10,2.2391595154161717e-10,1.204412415409016e-10,4.858773759989701e-11,1.5680796477175032e-11,4.217239957802061e-12,9.721688866417155e-13,1.9609348991512414e-13,3.5158643560768126e-14,5.673401987038735e-15,8.322663128834711e-16,1.119160865117323e-16,1.3891866721628482e-17,1.6011942335834326e-18,1.7225197232549798e-19],[1.1339368575232906e-11,1.8297860693999293e-11,1.476324293348615e-11,7.94094076744923e-12,3.20349027765643e-12,1.0338674229739375e-12,2.7805137408562423e-13,6.409711030882435e-14,1.2928850353718689e-14,2.31808226491178e-15,3.7405915575607665e-16,5.487304355880969e-17,7.378859621042537e-18,9.159195751754878e-19,1.0557005560050891e-19,1.1356929668053669e-20],[6.901182279234528e-13,1.1136146702660312e-12,8.98496506579215e-13,4.832886358810861e-13,1.9496562078553444e-13,6.292155944281984e-14,1.692231099840678e-14,3.900974193391661e-15,7.868546856025079e-16,1.4107935677616363e-16,2.276538062910828e-17,3.3395940285673587e-18,4.490801663235647e-19,5.574320915197223e-20,6.425033211455265e-21,6.911870026243946e-22],[3.900079337109366e-14,6.293393492988786e-14,5.0776917895917823e-14,2.731219009141522e-14,1.1018132231637041e-14,3.555899031678088e-15,9.563340423511508e-16,2.2045655701665118e-16,4.4467680702478347e-17,7.972846709338417e-18,1.2865446383030934e-18,1.8873116428673823e-19,2.5378959814671652e-20,3.150227445113748e-21,3.630992235002599e-22,3.90611932556136e-23],[2.057122534315331e-15,3.319491849449437e-15,2.6782619787470967e-15,1.4405994556048345e-15,5.811586416743458e-16,1.8755823652645698e-16,5.044246895529905e-17,1.1628126304031866e-17,2.345477107386394e-18,4.2053305101680226e-19,6.785964433270822e-20,9.954749568493996e-21,1.3386299513316872e-21,1.6616082149665207e-22,1.915190769961093e-23,2.06030836600685e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.25849234632095525, "-10": 3.3427697444560217e-06, "-11": 4.857115567780143e-07, "-12": 6.47876551244066e-08, "-13": 7.985497280804642e-09, "-14": 9.120467738546214e-10, "-15": 9.041951083215353e-11, "-2": 0.1762597762753397, "-3": 0.0861694650482797, "-4": 0.03275412686968922, "-5": 0.01015125949589554, "-6": 0.0026512832839316594, "-7": 0.000597786312815665, "-8": 0.00011850554507772587, "-9": 2.095362775494317e-05, "0": 0.2524190671993222, "1": 0.12561020361251168, "10": 2.6839338124297025e-09, "11": 1.9120987158418952e-10, "12": 1.250520076285046e-11, "13": 7.557304248320877e-13, "14": 4.23202852205431e-14, "15": 2.057122534315331e-15, "2": 0.04237271405787996, "3": 0.010156708738658975, "4": 0.0018929195754362376, "5": 0.0002876421983308652, "6": 3.683454732623877e-05, "7": 4.0720368947436995e-06, "8": 3.9579558309537596e-07, "9": 3.431294778388904e-08} |
| Raw goal margin distribution | {"-1": 0.25849234632095525, "-10": 3.3427697444560217e-06, "-11": 4.857115567780143e-07, "-12": 6.47876551244066e-08, "-13": 7.985497280804642e-09, "-14": 9.120467738546214e-10, "-15": 9.041951083215353e-11, "-2": 0.1762597762753397, "-3": 0.0861694650482797, "-4": 0.03275412686968922, "-5": 0.01015125949589554, "-6": 0.0026512832839316594, "-7": 0.000597786312815665, "-8": 0.00011850554507772587, "-9": 2.095362775494317e-05, "0": 0.2524190671993222, "1": 0.12561020361251168, "10": 2.6839338124297025e-09, "11": 1.9120987158418952e-10, "12": 1.250520076285046e-11, "13": 7.557304248320877e-13, "14": 4.23202852205431e-14, "15": 2.057122534315331e-15, "2": 0.04237271405787996, "3": 0.010156708738658975, "4": 0.0018929195754362376, "5": 0.0002876421983308652, "6": 3.683454732623877e-05, "7": 4.0720368947436995e-06, "8": 3.9579558309537596e-07, "9": 3.431294778388904e-08} |
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
| Team research json | {"base_rates": [0.7911848797824782, 1.613657812831387], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T16:35:23.982813+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 0, "venue_matches": 0, "xg_matches": 0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T16:35:23.344896+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T16:35:23.427190+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T16:35:23.754465+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Venezia+FC%22+%22Bologna+FC+1909%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T16:35:21.826042+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T16:35:22.061091+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T16:35:23.982304+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Venezia+FC_vs_Bologna+FC+1909&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.030972210604443, "goals_for": 0.6749458317875972, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.7096679935714522, "results": "LWLLLWLLLL", "xg_against": 1.731803085477299, "xg_for": 1.3231303025323111, "xg_matches": 10}, "venue": {"goals_against": 1.6460805251113106, "goals_for": 1.0114031125470773, "last_match": "2026-11-06T00:00:00+00:00", "matches": 5, "points_per_game": 1.3653225874357666, "results": "WLWLL", "xg_against": 2.020351136422765, "xg_for": 1.338377491547629, "xg_matches": 5}}}, "goal_rates": [0.7911848797824782, 1.613657812831387], "h2h": [], "margin_distribution": {"-1": 0.26530243757679317, "-10": 3.4266037492242993e-06, "-11": 4.978928160569305e-07, "-12": 6.641247795213292e-08, "-13": 8.185767197159586e-09, "-14": 9.349201810688126e-10, "-15": 9.268716020130912e-11, "-2": 0.18068023118379678, "-3": 0.08833052665167564, "-4": 0.03357557430343135, "-5": 0.010405845004931673, "-6": 0.002717775358605906, "-7": 0.0006127783177786494, "-8": 0.0001214775698328231, "-9": 2.1479128062594927e-05, "0": 0.26237269172506467, "1": 0.10862672112829058, "10": 2.3151598220781723e-09, "11": 1.6493752946749952e-10, "12": 1.0786979261222374e-11, "13": 6.518926464544268e-13, "14": 3.6505454623261626e-14, "15": 1.7744727602753514e-15, "2": 0.036550679709349235, "3": 0.008761171340140646, "4": 0.0016328313787693427, "5": 0.0002481200011810287, "6": 3.177346014987789e-05, "7": 3.5125367731017775e-06, "8": 3.414130510576508e-07, "9": 2.95983297793812e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T16:35:23.982813+00:00", "p_over_1_5": 0.6965791551761995, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.260709257595112, "-10": 3.342769744456021e-06, "-11": 4.857115567780142e-07, "-12": 6.478765512440659e-08, "-13": 7.98549728080464e-09, "-14": 9.120467738546213e-10, "-15": 9.041951083215352e-11, "-2": 0.1762597762753397, "-3": 0.0861694650482797, "-4": 0.03275412686968921, "-5": 0.010151259495895536, "-6": 0.002651283283931659, "-7": 0.000597786312815665, "-8": 0.00011850554507772585, "-9": 2.0953627754943165e-05, "0": 0.2479852446510087, "1": 0.12782711488666842, "10": 2.683933812429702e-09, "11": 1.912098715841895e-10, "12": 1.2505200762850459e-11, "13": 7.557304248320876e-13, "14": 4.2320285220543095e-14, "15": 2.0571225343153308e-15, "2": 0.04237271405787996, "3": 0.010156708738658973, "4": 0.0018929195754362374, "5": 0.00028764219833086514, "6": 3.683454732623876e-05, "7": 4.0720368947436995e-06, "8": 3.9579558309537596e-07, "9": 3.4312947783889034e-08}, "p_over_1_5": 0.6926118362455159, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "away team 'Bologna FC 1909' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
