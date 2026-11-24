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
| Training as of utc | 2026-11-24T15:18:19.234237+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 120, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 120, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 469, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T15:18:19.234237+00:00', 'observations': 1400, 'observations_sha256': 'bf01b8a10efbe5bbd065ec9ba202d782d13e5caf450aca8fab7056d7f90e8604', 'eligible_training_matches': 524, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 476, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 56, 'retrospective_eligible_training_matches': 524, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'd0c3910ee6fa9ec1316aa103e88d490fda33db8a9f5e8306a0fbbfb6c0e8c85d', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 463, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-11T00:00:00+00:00', 'audit_origin_utc': '2026-10-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 12, 'selected_ridge': 100.0, 'proposed_weight': 0.1, 'audit_baseline_poisson_score': 0.7094780779702862, 'audit_candidate_poisson_score': 0.707010009982578, 'audit_gain': 0.0024680679877081557, 'audit_gain_lower95': -0.010614842817769506, 'audit_baseline_briers': [0.5007532400199668, 0.13589077275468245, 0.2320042325524207, 0.24981366604904326], 'audit_candidate_briers': [0.5031315230725493, 0.1315095578653705, 0.23122434572276224, 0.24837029371836508], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2019, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1640, 'tuning_matches': 260, 'audit_matches': 119, 'audit_matchdays': 40, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7914043978248803, 'audit_candidate_poisson_score': 0.7919838630923187, 'audit_gain': -0.0005794652674384615, 'audit_gain_lower95': -0.0046598965622487495, 'audit_baseline_briers': [0.5234851426701006, 0.14284242820734283, 0.21194206718764858, 0.24164713374709632], 'audit_candidate_briers': [0.5281604695213433, 0.14119840340223602, 0.21183017308373364, 0.24228008703124398], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1833.603 |
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
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261124T151819234237Z_52b48216aa315d39b949d0a3b655738bbcaf11a1fa093c6d7cf5708af4bd02c1.json |
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
| Bbs statistics cutoff utc | 2026-11-24T15:18:19.234237+00:00 |
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
| Score matrix json | [[0.09249683897937828,0.14346375401693956,0.1175394169427789,0.06322278755593938,0.025504981458407322,0.008231260965747665,0.00221373934332304,0.000510316730387704,0.00010293455294847011,1.845567935845412e-05,2.97811455670598e-06,4.368779013570505e-07,5.87476088103021e-08,7.292193849989647e-09,8.405073827016013e-10,9.041940325705643e-11],[0.06921093246207798,0.11747720551576003,0.09299525234025227,0.05002082905754919,0.020179121594696318,0.0065124382143295955,0.0017514741369534933,0.000403754198806008,8.144012430003911e-05,1.4601829783499426e-05,2.3562352264677092e-06,3.4565060585894567e-07,4.64801412819677e-08,5.769463766558907e-09,6.649956089728791e-10,7.153834382587156e-11],[0.028256300218352307,0.04559599100337759,0.03678815661488823,0.019787828379053355,0.00798269445907229,0.002576266970027239,0.000692868756583628,0.00015972183875848225,3.221704304348658e-05,5.776363711277385e-06,9.321072673221975e-07,1.3673653549371512e-07,1.8387161429562942e-08,2.282352392050257e-09,2.6306679099700893e-10,2.8299980164651345e-11],[0.00745197323971421,0.012024932569718894,0.009702061363805416,0.0052186013884786536,0.002105258828301423,0.0006794333430295813,0.0001827287858918543,4.212309676173039e-05,8.496531420162783e-06,1.5233879689364867e-06,2.458226434088049e-07,3.6061232203662344e-08,4.849206508586507e-09,6.019198839807631e-10,6.93780385831955e-11,7.463492857938014e-12],[0.0014739696475553358,0.0023784821887450824,0.0019190278210817822,0.0010322178840248579,0.0004164115346827539,0.00013438911989451302,3.614300205801064e-05,8.331775234636804e-06,1.6805789580774806e-06,3.0131987266093114e-07,4.862270749113601e-08,7.132763365060309e-09,9.591530965640467e-10,1.1905727660418966e-10,1.3722690593354166e-11,1.476248180645447e-12],[0.00023323610560874476,0.00037636319301604884,0.00030366064612408954,0.00016333476052845147,6.589159067220216e-05,2.1265292004058154e-05,5.719149684663214e-06,1.3183926899424972e-06,2.6592928287234493e-07,4.767986488630869e-08,7.693897196726335e-09,1.1286649981257068e-09,1.5177322904593123e-10,1.883923158499221e-11,2.1714333926591405e-12,2.3359665318536517e-13],[3.0755428065608106e-05,4.962872741823758e-05,4.004188431225186e-05,2.15379624219629e-05,8.688723693778853e-06,2.8041248451562223e-06,7.541495184204872e-07,1.7384843325145014e-07,3.5066478702225873e-08,6.2872540718404114e-09,1.0145474739449115e-09,1.4883019534829428e-10,2.0013413515133686e-11,2.484214998836939e-12,2.8633372750279547e-13,3.0802971283790546e-14],[3.4761697919674705e-06,5.60934748484224e-06,4.525782842715701e-06,2.434354488321365e-06,9.820535994698365e-07,3.169396328623264e-07,8.523866970629594e-08,1.9649431338117038e-08,3.963431551507429e-09,7.106245646242799e-10,1.1467046642696354e-10,1.6821714466100666e-11,2.2620404875215214e-12,2.8078143205446314e-13,3.2363219001321444e-14,3.4815434222257185e-15],[3.4378604151464326e-07,5.547529271297688e-07,4.475906130498587e-07,2.4075265112689826e-07,9.712308078192441e-08,3.1344677706083455e-08,8.42992908747302e-09,1.943288338030713e-09,3.9197522717547705e-10,7.027930759877395e-11,1.1340673238303229e-11,1.663632956351424e-12,2.237111509189925e-13,2.7768706028074235e-14,3.2006557840888978e-15,3.4431748249296233e-16],[3.0221984262592574e-08,4.876793182025955e-08,3.9347369672368795e-08,2.1164392834211813e-08,8.538020351244549e-09,2.75548812911574e-09,7.410690180844046e-10,1.7083308359726509e-10,3.445826100103263e-11,6.1782035095964786e-12,9.969504480902734e-13,1.462487796306923e-13,1.9666286777243356e-14,2.441127024458534e-15,2.813673536905088e-16,3.0268702857717885e-17],[2.3911136585705105e-09,3.858438508287899e-09,3.1130991345554077e-09,1.6744919308251422e-09,6.755141191798936e-10,2.1800968607189468e-10,5.863216113438107e-11,1.3516032434400359e-11,2.7262809024799817e-12,4.888092942166442e-13,7.887707877266127e-14,1.1570962762926753e-14,1.5559642450292661e-15,1.931379528151361e-16,2.2261321978052714e-17,2.3948099569320852e-18],[1.7198270692092363e-10,2.775211863161691e-10,2.239120730020436e-10,1.2043913259761916e-10,4.8586877651527424e-11,1.5680515985191753e-11,4.217163725518184e-12,9.721511299002217e-13,1.9608987124252147e-13,3.51579881141002e-14,5.673295149611217e-15,8.322504831656752e-16,1.1191393674371977e-16,1.3891597254381718e-17,1.601162872246149e-18,1.7224856605126336e-19],[1.1339157283195371e-11,1.829751628752366e-11,1.476296227006066e-11,7.940788303814493e-12,3.203428167015391e-12,1.0338471827839144e-12,2.7804587815113117e-13,6.40958312747291e-14,1.2928589923188183e-14,2.318035133438139e-15,3.7405147975144754e-16,5.4871907161979974e-17,7.378705415435153e-18,9.159002611504733e-19,1.0556780951680134e-19,1.1356685897252375e-20],[6.90104202621475e-13,1.1135918280513196e-12,8.984779072435762e-13,4.832785403471872e-13,1.9496151130468797e-13,6.292022130823623e-14,1.692194792271214e-14,3.900889760014224e-15,7.868375062743268e-16,1.4107624997676196e-16,2.276487500140868e-17,3.3395192246303146e-18,4.490700225707329e-19,5.574193951245131e-20,6.42488565857145e-21,6.911709988502208e-22],[3.899993486263852e-14,6.293253771327858e-14,5.0775780997872216e-14,2.7311573415224422e-14,1.1017881376060737e-14,3.5558174015496896e-15,9.563119080101049e-16,2.2045141294456762e-16,4.4466634713441106e-17,7.972657663667173e-18,1.2865138899871681e-18,1.887266180069173e-19,2.5378343679829078e-20,3.1501503712695804e-21,3.630902713421464e-22,3.9060222835490665e-23],[2.0570737761217604e-15,3.319412543911637e-15,2.6781974872703173e-15,1.4405644946577593e-15,5.8114442823922e-16,1.8755361400391894e-16,5.0441216240212507e-17,1.162783533035314e-17,2.345417973224195e-18,4.20522369170346e-19,6.785790784087363e-20,9.954492953014981e-21,1.3385951912241196e-21,1.6615647545059705e-22,1.915140315422395e-23,2.0602536995859018e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2584923797172784, "-10": 3.3427682001657163e-06, "-11": 4.857112493178322e-07, "-12": 6.478760286071595e-08, "-13": 7.985489439127177e-09, "-14": 9.120457265274728e-10, "-15": 9.041940325705643e-11, "-2": 0.1762598709857697, "-3": 0.08616950901468032, "-4": 0.032754140816500604, "-5": 0.010151262637769947, "-6": 0.002651283744811386, "-7": 0.000597786328095946, "-8": 0.00011850552951363882, "-9": 2.0953621586437094e-05, "0": 0.25241925352237493, "1": 0.12560998564571402, "10": 2.6838922911320777e-09, "11": 1.912065938335343e-10, "12": 1.250496545673922e-11, "13": 7.557149378220238e-13, "14": 4.231934740655016e-14, "15": 2.0570737761217604e-15, "2": 0.04237260963653206, "3": 0.010156668190066002, "4": 0.0018929090175582523, "5": 0.00028764012883291664, "6": 3.683422203296123e-05, "7": 4.071994218570012e-06, "8": 3.9579077891838387e-07, "9": 3.431247419995625e-08} |
| Raw goal margin distribution | {"-1": 0.2584923797172784, "-10": 3.3427682001657163e-06, "-11": 4.857112493178322e-07, "-12": 6.478760286071595e-08, "-13": 7.985489439127177e-09, "-14": 9.120457265274728e-10, "-15": 9.041940325705643e-11, "-2": 0.1762598709857697, "-3": 0.08616950901468032, "-4": 0.032754140816500604, "-5": 0.010151262637769947, "-6": 0.002651283744811386, "-7": 0.000597786328095946, "-8": 0.00011850552951363882, "-9": 2.0953621586437094e-05, "0": 0.25241925352237493, "1": 0.12560998564571402, "10": 2.6838922911320777e-09, "11": 1.912065938335343e-10, "12": 1.250496545673922e-11, "13": 7.557149378220238e-13, "14": 4.231934740655016e-14, "15": 2.0570737761217604e-15, "2": 0.04237260963653206, "3": 0.010156668190066002, "4": 0.0018929090175582523, "5": 0.00028764012883291664, "6": 3.683422203296123e-05, "7": 4.071994218570012e-06, "8": 3.9579077891838387e-07, "9": 3.431247419995625e-08} |
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
| Count model | {"corners": {"alpha": 0.02187259349786676, "mu": 9.030867476750299, "version": "count-markets-nb2-v1"}} |
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
| Team research json | {"base_rates": [0.7911835430111472, 1.6136575082736153], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T15:19:59.670194+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 0, "venue_matches": 0, "xg_matches": 0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T15:19:58.574454+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T15:19:58.699809+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T15:19:59.146902+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Venezia+FC%22+%22Bologna+FC+1909%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-24T15:19:56.781766+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-24T15:19:56.994775+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-24T15:19:59.669659+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Venezia+FC_vs_Bologna+FC+1909&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 2.030972210604443, "goals_for": 0.6749458317875972, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 0.7096679935714522, "results": "LWLLLWLLLL", "xg_against": 1.731803085477299, "xg_for": 1.3231303025323111, "xg_matches": 10}, "venue": {"goals_against": 1.6460805251113106, "goals_for": 1.0114031125470773, "last_match": "2026-11-06T00:00:00+00:00", "matches": 5, "points_per_game": 1.3653225874357666, "results": "WLWLL", "xg_against": 2.020351136422765, "xg_for": 1.338377491547629, "xg_matches": 5}}}, "goal_rates": [0.7911835430111472, 1.6136575082736153], "h2h": [], "margin_distribution": {"-1": 0.2653025583817088, "-10": 3.4266021746084636e-06, "-11": 4.978925021070169e-07, "-12": 6.64124245405928e-08, "-13": 8.18575917889538e-09, "-14": 9.349191097685035e-10, "-15": 9.26870501556373e-11, "-2": 0.18068032871262324, "-3": 0.08833057193735702, "-4": 0.03357558868236475, "-5": 0.010405848251123046, "-6": 0.0027177758377097123, "-7": 0.0006127783349450404, "-8": 0.00012147755417633548, "-9": 2.147912179206706e-05, "0": 0.262372710922048, "1": 0.10862657130750179, "10": 2.3151232789749548e-09, "11": 1.6493465029880375e-10, "12": 1.0786772899691583e-11, "13": 6.518790827045076e-13, "14": 3.6504634204454825e-14, "15": 1.7744301443854177e-15, "2": 0.03655057816015254, "3": 0.008761133612306007, "4": 0.0016328217589097957, "5": 0.00024811813813420636, "6": 3.1773169576589474e-05, "7": 3.512498857875718e-06, "8": 3.4140879978871253e-07, "9": 2.9597911973598277e-08}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T15:19:59.670194+00:00", "p_over_1_5": 0.6965788050045411, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.26070937435998404, "-10": 3.3427682001657163e-06, "-11": 4.857112493178322e-07, "-12": 6.478760286071595e-08, "-13": 7.985489439127177e-09, "-14": 9.120457265274728e-10, "-15": 9.041940325705643e-11, "-2": 0.1762598709857697, "-3": 0.08616950901468032, "-4": 0.032754140816500604, "-5": 0.010151262637769947, "-6": 0.002651283744811386, "-7": 0.000597786328095946, "-8": 0.00011850552951363882, "-9": 2.0953621586437094e-05, "0": 0.24798526423696376, "1": 0.1278269802884196, "10": 2.6838922911320777e-09, "11": 1.912065938335343e-10, "12": 1.250496545673922e-11, "13": 7.557149378220238e-13, "14": 4.231934740655016e-14, "15": 2.0570737761217604e-15, "2": 0.04237260963653206, "3": 0.010156668190066002, "4": 0.0018929090175582523, "5": 0.00028764012883291664, "6": 3.683422203296123e-05, "7": 4.071994218570012e-06, "8": 3.9579077891838387e-07, "9": 3.431247419995625e-08}, "p_over_1_5": 0.6926114798988988, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "away team 'Bologna FC 1909' has no reviewed training-history name; no history form", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: away form/venue evidence is thin", "Research review: away xG sample below five; goals are not verified xG", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
