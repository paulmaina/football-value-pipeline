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

## 2026-11-27 — Levante vs Real Racing Club de Santander

Research leans **Levante win** at **63.7%**. Cagey: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote). Only one view is available.

**Fixture source:** The Odds API

### The two views

- **Research:** research v5, C6
- **Cagey:** unavailable: no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)

| Measure | Research | Cagey |
| --- | --- | --- |
| Levante win | 63.7% | — |
| Draw | 18.7% | — |
| Real Racing Club de Santander win | 17.6% | — |
| Levante expected goals | 2.69 | — |
| Real Racing Club de Santander expected goals | 1.47 | — |
| Expected total goals | 4.16 | — |
| Most likely score | 2-1 | — |
| Most likely score probability | 8.5% | — |
| Over 1.5 | 92.1% | — |
| Under 1.5 | 7.9% | — |
| Over 2.5 | 78.3% | — |
| Under 2.5 | 21.7% | — |
| Over 3.5 | 59.9% | — |
| Under 3.5 | 40.1% | — |
| BTTS Yes | 72.5% | — |
| BTTS No | 27.5% | — |
| Double Chance 1X | 82.4% | — |
| Double Chance X2 | 36.3% | — |

### 5 most likely scorelines

| Rank | Research | Cagey |
| --- | --- | --- |
| 1 | 2-1 (8.53%) | — |
| 2 | 3-1 (7.53%) | — |
| 3 | 1-1 (6.65%) | — |
| 4 | 2-2 (6.53%) | — |
| 5 | 3-2 (5.67%) | — |

### No-loss on the quoted Pinnacle Asian handicap lines

| Line | Pinnacle odds | Research no-loss | Cagey no-loss |
| --- | --- | --- | --- |
| Levante -0.25 | 1.84 | 63.7% | — |
| Real Racing Club de Santander +0.25 | 2.05 | 36.3% | — |

_No-loss: win, half win or refund, from each view's own goal-margin distribution._

### On the lists

- **Value shortlist:** no
- **Cagey tier:** no
- **Master shortlist:** no

### The master's verdict on every Pinnacle offer

| Offer | Pinnacle odds | Research no-loss | Cagey no-loss | Gap (points) | Gap label | Cagey tier | Master labels | Master check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Home win | 2.10 | 63.7% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Away win | 3.27 | 17.6% | — | — | one view missing (no cagey view) | risky, below fair price (Pinnacle stand-in: no cagey view) | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Away +0.25 | 2.05 | 36.3% | — | — | one view missing (no cagey view) | no market view | one view missing | offered odds outside (1.20, 2.00] |
| Asian Handicap Home -0.25 | 1.84 | 63.7% | — | — | one view missing (no cagey view) | no market view | one view missing | eligible |

_Best offer: none (no offer passes the master checks with a market view). Gap = research minus cagey no-loss, in points; the cagey tier decides safety (safe at 75% or more, risky below 50%) and fair price; the research view only labels. No probability is blended._

_Views the master could not use: cagey: cagey settlement probabilities unavailable._

### Safest Asian handicap (cagey tier)

_no cagey grid: needs Pinnacle 1X2 and O/U 2.5 (no Pinnacle O/U 2.5 quote)._


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
| Training sha256 | 24378a59b0a3db56fedb8c6dbe9c91db37a4424f691b4658425cfd90a62588d9 |
| Training as of utc | 2026-11-24T22:37:17.876598+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 129, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 129, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 287, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_utc': '2026-11-24T22:37:17.876598+00:00', 'observations': 1224, 'observations_sha256': 'ab9b2bcc3a9d446715fa7e1c58b417d19a51f8b19e98ef74537752b24c28b275', 'eligible_training_matches': 356, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 327, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 50, 'retrospective_eligible_training_matches': 356, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': '69b35d1c2108f3a44d026ff2d38850df251a3f12c076e62fb3c232dbfbcc31a3', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 296, 'tuning_matches': 20, 'audit_matches': 40, 'tuning_origin_utc': '2026-10-09T00:00:00+00:00', 'audit_origin_utc': '2026-10-23T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_red_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_red_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 40, 'audit_matchdays': 15, 'selected_ridge': 100.0, 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8952371648431244, 'audit_candidate_poisson_score': 0.8915362622731108, 'audit_gain': 0.0037009025700136533, 'audit_gain_lower95': -0.011568438870258373, 'audit_baseline_briers': [0.5455405803287083, 0.1976540459878047, 0.1623441719552971, 0.23199911626112096], 'audit_candidate_briers': [0.5429922292316874, 0.19682774508012907, 0.1660066427284999, 0.23381083080780965], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-24', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 2029, 'tune_start_date': '2025-11-25', 'audit_start_date': '2026-05-26', 'training_shot_matches': 1650, 'tuning_matches': 250, 'audit_matches': 115, 'audit_matchdays': 53, 'selected_shrinkage': 40.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.7949749477503751, 'audit_candidate_poisson_score': 0.7996477569248229, 'audit_gain': -0.0046728091744477895, 'audit_gain_lower95': -0.013811683564063338, 'audit_baseline_briers': [0.5433888906595042, 0.1939622888379839, 0.1996416083959726, 0.25405140114965663], 'audit_candidate_briers': [0.5523955343982682, 0.19108907706222616, 0.20020832835092672, 0.2498487273640876], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1845.402 |
| Base scoring parameter | 0.084 |
| Home-advantage parameter | 0.280 |
| Dixon-Coles low-score adjustment | -0.028 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 2029, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-23'} |
| Training data health | {'training_end': '2026-11-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261124T223717876598Z_692f9c344d538a1a11a3aeda7ed379208484a7996dfa2db643bf8db5e3b8f75b.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

### 2026-11-27 — Levante vs Real Racing Club de Santander

The model's most likely 1X2 outcome is **Levante win** at **51.3%**. Expected goals are 2.79 for Levante and 1.60 for Real Racing Club de Santander (4.39 combined). The most likely exact score is 2-2 at 7.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.9%; Under 3.5 goals: 37.1%; Double Chance 1X: 73.2%; Double Chance X2: 48.7%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 57.0%; BTTS Yes (both teams score): 76.6%; BTTS No (at least one team does not score): 23.4%.

| Outcome | Benchmark probability | Benchmark fair odds |
| --- | --- | --- |
| Levante win | 51.3% | 1.95 |
| Draw | 22.0% | 4.55 |
| Real Racing Club de Santander win | 26.8% | 3.74 |

| Measure | Benchmark estimate |
| --- | --- |
| Levante expected goals | 2.79 |
| Real Racing Club de Santander expected goals | 1.60 |
| Expected total goals | 4.39 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 93.1% |
| Under 1.5 | 6.9% |
| Over 2.5 | 79.9% |
| Under 2.5 | 20.1% |
| Over 3.5 | 62.9% |
| Under 3.5 | 37.1% |
| Over 4.5 | 43.0% |
| Under 4.5 | 57.0% |

| Rank | Score | Benchmark probability |
| --- | --- | --- |
| 1 | 2-2 | 7.82% |
| 2 | 1-1 | 7.19% |
| 3 | 2-1 | 6.36% |
| 4 | 3-1 | 5.90% |
| 5 | 1-2 | 5.84% |

| Selection | Benchmark | Market fair | Best quoted odds | Benchmark EV (display only) |
| --- | --- | --- | --- | --- |
| Levante win | 51.3% | 46.6% | 2.10 | +7.7% |
| Draw | 22.0% | 23.9% | 4.01 | -11.9% |
| Real Racing Club de Santander win | 26.8% | 29.5% | 3.27 | -12.5% |

<details>
<summary>Additional technical details (forecast row)</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-27T20:00:00+00:00 |
| Fixture id | 1,640,273,345 |
| Odds source | — |
| Odds schedule provider | — |
| Odds provider | — |
| Odds match method | — |
| Odds event id | 1640273345.00 |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-24T22:37:12Z |
| Market best draw last update utc | 2026-11-24T22:37:12Z |
| Market best away last update utc | 2026-11-24T22:37:12Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 0.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Santander |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7861 |
| Dc lambda away | 1.6041 |
| Bbs statistics applied | 0 |
| Bbs statistics status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-24T22:37:17.876598+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 76.6% |
| P btts no | 23.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 56.70 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 14.52 |
| Fair Over 2.5 odds | 1.25 |
| Fair Under 2.5 odds | 4.96 |
| Fair Over 3.5 odds | 1.59 |
| Fair Under 3.5 odds | 2.69 |
| Fair Over 4.5 odds | 2.33 |
| Fair Under 4.5 odds | 1.75 |
| Score matrix json | [[0.017635491664844637,0.024084596864310494,0.02097266051784544,0.011214314354638448,0.004497313764900304,0.0014428581514907128,0.0003857561339487999,8.840060842851466e-05,1.772579493220113e-05,3.1593930963347683e-06,5.068087664227212e-07,7.390807431306991e-08,9.879866910393937e-09,1.2191248831658663e-09,1.396884870228766e-10,1.493859688297959e-11,1.4977187919280244e-12,1.4132591668908865e-13,1.2594756038544667e-14,1.0633509225978399e-15],[0.027158060276912508,0.07194271108543412,0.058432095322411594,0.031244289907241585,0.012530001445541205,0.004019958506117332,0.0010747582153881584,0.00024629363422246466,4.938597743774959e-05,8.802410090456544e-06,1.4120239120186056e-06,2.0591587031519063e-07,2.7526375329904293e-08,3.3966134779351302e-09,3.891871983632674e-10,4.1620542911406356e-11,4.172806170282491e-12,3.937492541052385e-13,3.509034939942685e-14,2.9626104145223827e-15],[0.03963360857959896,0.063577591203862,0.0781688885178632,0.04352498159657802,0.017454968057887443,0.005600019092039314,0.0014971961815876812,0.0003431003210094559,6.879733114398182e-05,1.2262232181626754e-05,1.9670254938421096e-06,2.8685191734297526e-07,3.8345725993820706e-08,4.7316658357964684e-09,5.421587655432325e-10,5.797966187219006e-11,5.81294413497097e-12,5.485139553331541e-13,4.8882749979654923e-14,4.127076152242158e-15],[0.03680783676322674,0.05904467654341942,0.04735776582773837,0.03881770130373316,0.016210474847167172,0.005200752492591278,0.001390450040493471,0.00031863817254397823,6.389226278519607e-05,1.1387967350679992e-05,1.8267817612679886e-06,2.6640013178647793e-07,3.5611776810918264e-08,4.394310534513927e-09,5.035042747063873e-10,5.3845864816789974e-11,5.3984965412385556e-12,5.094063562167539e-13,4.539753876246639e-14,3.8328265016809224e-15],[0.025637651271408435,0.041126210062027914,0.03298596147050894,0.017637959709762233,0.010842969040884451,0.0036224644119040752,0.0009684859634049923,0.00022194008308586185,4.45026846528659e-05,7.93202647319402e-06,1.272402777854861e-06,1.8555487847148975e-07,2.480456324848997e-08,3.06075583270078e-09,3.5070431037887913e-10,3.750509744597235e-11,3.76019847633245e-12,3.548152693714321e-13,3.1620610438458395e-14,2.669667056665503e-15],[0.01428585259041406,0.022916411816699848,0.0183804896217734,0.009828251805980789,0.003941456493384407,0.0019384142582027123,0.0005396612803029514,0.00012366980412144011,2.4797856328498152e-05,4.419896336825653e-06,7.090102883308825e-07,1.0339518285874056e-07,1.3821637964656773e-08,1.7055192060427488e-09,1.9542001050942024e-10,2.0898649717566013e-11,2.095263742177966e-12,1.9771072558121559e-13,1.7619686560231008e-14,1.48759609970749e-15],[0.006633654479321715,0.010641266031250986,0.008535004581625004,0.004563761679887006,0.001830220517600435,0.0005871835346368987,0.0002406481245432297,5.742623654240383e-05,1.1514917270075949e-05,2.0523846894930984e-06,3.292298618723896e-07,4.8011689436821525e-08,6.418095806009643e-09,7.919600912252432e-10,9.074353944648528e-11,9.70431554107819e-12,9.729384802686383e-13,9.180723600926948e-14,8.181724677248216e-15,6.907672095726199e-16],[0.002640296743480116,0.004235387920247898,0.0033970633943473856,0.0018164475009945153,0.0007284559796616088,0.00023370809847869368,6.24831570924154e-05,2.1949507898331227e-05,4.5831145810194695e-06,8.168807448336009e-07,1.310385602487635e-07,1.9109392517226817e-08,2.554501068569873e-09,3.152123247218068e-10,3.6117327551391e-11,3.862467181654006e-12,3.8724451342277935e-13,3.6540695180730844e-14,3.256452546439857e-15,2.7493599789115334e-16],[0.0009195189545885766,0.0014750309723028155,0.001183073148408386,0.0006326023433934095,0.0002536946207036385,8.139199766945854e-05,2.1760602262184444e-05,4.986700950303843e-06,1.5327919132950145e-06,2.8448973789320114e-07,4.563594612169118e-08,6.655103701375111e-09,8.896394535451813e-10,1.0977694382927362e-10,1.2578346488741318e-11,1.3451562949420139e-12,1.3486312515135583e-13,1.2725789976257837e-14,1.134103523993623e-15,9.575016974282169e-17],[0.0002846532256684369,0.00045662171740082526,0.0003662410505141144,0.00019583315462258914,7.853562099797356e-05,2.5196320929105408e-05,6.736376227491894e-06,1.5437207725456528e-06,3.0954173656905357e-07,8.457394094478567e-08,1.4127407820301794e-08,2.0602041168384563e-09,2.754035018743565e-10,3.3983379036495345e-11,3.8938478469946206e-12,4.164167323280151e-13,4.17492466104042e-14,3.939491565501935e-15,3.510816440876626e-16,2.9641145013470247e-17],[7.930746030975551e-05,0.00012721973778551072,0.00010203870871037859,5.456123007597916e-05,2.1880871472904654e-05,7.019966899530067e-06,1.8768271079270351e-06,4.3009726522689715e-07,8.624166801382948e-08,1.5371459028012872e-08,3.779853386595899e-09,5.739950982198825e-10,7.673038744872392e-11,9.468136107712747e-12,1.0848680279402667e-12,1.1601819509991957e-13,1.1631790613795815e-14,1.0975848604490436e-15,9.781513449771304e-17,8.258342852680902e-18],[2.008719475812505e-05,3.2222537955370724e-05,2.5844623024460126e-05,1.3819406780880712e-05,5.5420426405921964e-06,1.7780350266632613e-06,4.753675315917471e-07,1.0893612653596621e-07,2.1843508478183625e-08,3.893322141526864e-09,6.245407683274943e-10,1.3961367882738882e-10,1.9434467205594246e-11,2.3981135349591716e-12,2.7477812653418915e-13,2.938538280454259e-14,2.946129437665354e-15,2.7799907813587386e-16,2.4774865432250724e-17,2.091694029959571e-18],[4.6637576805761365e-06,7.481288984676689e-06,6.000492382499875e-06,3.2085298764412536e-06,1.28672740232618e-06,4.128164540536466e-07,1.1036876991799854e-07,2.529231696819313e-08,5.07153097595434e-09,9.039346339368033e-10,1.450031644633761e-10,2.1145854935450535e-11,4.333151418513568e-12,5.567835903535276e-13,6.379679260887308e-14,6.822570617827146e-15,6.840195437108289e-16,6.454461916962491e-17,5.7521207085505686e-18,4.856404398475476e-19],[9.995178580968266e-07,1.6033598771460344e-06,1.2860014830233817e-06,6.876392663145534e-07,2.7576626085956467e-07,8.847316824828157e-08,2.365379251342054e-08,5.420548024534467e-09,1.086910196786078e-09,1.9372764861583444e-10,3.107649716993685e-11,4.5318948968413684e-12,6.058136252207595e-13,1.145923292874527e-13,1.3672672953709497e-14,1.462185996293554e-15,1.4659632769380008e-16,1.3832944145616332e-17,1.2327714611052908e-18,1.0408051307280976e-19],[1.989117577656156e-07,3.1908097380195444e-07,2.5592420726172666e-07,1.3684551412790845e-07,5.487961144033255e-08,1.760684240786614e-08,4.707287026993616e-09,1.0787308369518257e-09,2.1630350676050248e-10,3.855329527313175e-11,6.184462465773669e-12,9.018820150509144e-13,1.205615808610671e-13,1.4876680477032873e-14,2.6129906908242525e-15,2.909862833834866e-16,2.9173799134595515e-17,2.7528625054456767e-18,2.45331022617892e-19,2.0712824324999874e-20],[3.694597475482948e-08,5.9266268295333776e-08,4.753549718153453e-08,2.5417757939874483e-08,1.0193367961780036e-08,3.2703041912675253e-09,8.743339741030931e-10,2.003640343686492e-10,4.0176327382171734e-11,7.1609093895546275e-12,1.1487053188776455e-12,1.675160409530389e-13,2.2393171589906354e-14,2.76320247487719e-15,3.166103640269541e-16,5.1903151787899626e-17,5.418756831857592e-18,5.113181330867206e-19,4.556791348099969e-20,3.847210910047809e-21],[6.433467027277837e-09,1.0320138673780443e-08,8.277439038272639e-09,4.426038525134229e-09,1.7749889430228086e-09,5.694637730714607e-10,1.5224929997240787e-10,3.4889738790680266e-11,6.995973964837254e-12,1.2469416424586786e-12,2.0002606081172576e-13,2.916986040192712e-14,3.899362028362925e-15,4.811612666814578e-16,5.5131914937379854e-17,5.895929365326719e-18,9.061334279510726e-19,8.903671838385255e-20,7.934820256529832e-21,6.699215462853842e-22],[1.0543725506541993e-09,1.6913541159754844e-09,1.3565787272498069e-09,7.253777021398872e-10,2.909006312308465e-10,9.332867773670337e-11,2.495193992082171e-11,5.718033950343217e-12,1.1465610816594105e-12,2.043596453516595e-13,3.278201116771857e-14,4.780610514331094e-15,6.390613755129138e-16,7.885689471569352e-17,9.035497893827188e-18,9.662762017802538e-19,9.68772393375185e-20,1.4013050784828815e-20,1.3004273803513907e-21,1.0979257164142167e-22],[1.6319976119158095e-10,2.617941709942382e-10,2.0997637332969346e-10,1.1227669734903093e-10,4.5026697174445475e-11,1.444576483853416e-11,3.862155396418618e-12,8.850588670981241e-13,1.7746904981761562e-13,3.163155688934966e-14,5.074123364300335e-15,7.399609310814413e-16,9.89163306705583e-17,1.2205767665258186e-17,1.3985484519724077e-18,1.4956387595428266e-19,1.4995024590665714e-20,1.4149422491542722e-21,1.9329742661949542e-22,1.6994108449970578e-23],[2.3931165539679863e-11,3.8388779478860946e-11,3.079035969713012e-11,1.6463947072532878e-11,6.602591424884253e-12,2.1182873502640988e-12,5.663358785382208e-13,1.2978260572344127e-13,2.6023574901984256e-14,4.638364778660462e-15,7.440555385205605e-16,1.0850584219800396e-16,1.4504819532646225e-17,1.7898203061294306e-18,2.0507931062549417e-19,2.193163671371062e-20,2.1988292944224204e-21,2.0748325209770374e-22,1.84905996258519e-23,2.3930802188446514e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14647658288494378, "-10": 7.558372868692631e-07, "-11": 1.0670931527410394e-07, "-12": 1.3876451384551679e-08, "-13": 1.6720633656657037e-09, "-14": 1.8766448863200888e-10, "-15": 1.9707984214414367e-11, "-16": 1.944183622514599e-12, "-17": 1.8054334224075764e-13, "-18": 1.555736645306705e-14, "-19": 1.0633509225978399e-15, "-2": 0.07597720631645112, "-3": 0.030983713235633627, "-4": 0.010382378470131159, "-5": 0.002933300667415376, "-6": 0.0007136176109414495, "-7": 0.0001520758057910423, "-8": 2.8788235475649944e-05, "-9": 4.897146982995663e-06, "0": 0.21961039479317557, "1": 0.16032781246384237, "10": 0.0001182764379790136, "11": 2.9002119434710244e-05, "12": 6.5503318324825335e-06, "13": 1.3708662803373977e-06, "14": 2.6722798778588664e-07, "15": 4.8741571444633646e-08, "16": 8.351261463655549e-09, "17": 1.3469570813455676e-09, "18": 2.015885406704419e-10, "19": 2.3931165539679863e-11, "2": 0.14357982162327057, "3": 0.10169533535718323, "4": 0.05918639714720959, "5": 0.029042841733793925, "6": 0.01227172362208742, "7": 0.004542109629447827, "8": 0.0014933789029078133, "9": 0.000441220399860766} |
| Raw goal margin distribution | {"-1": 0.1114058649235498, "-10": 5.748680439335593e-07, "-11": 8.116002796740062e-08, "-12": 1.0554028760896728e-08, "-13": 1.2717231777948365e-09, "-14": 1.427321982784569e-10, "-15": 1.4989324464451182e-11, "-16": 1.4786899978856797e-12, "-17": 1.3731605968934392e-13, "-18": 1.1832484288618024e-14, "-19": 8.087540473436577e-16, "-2": 0.05778607213146059, "-3": 0.02356531879413339, "-4": 0.007896537662522818, "-5": 0.0022309838985725408, "-6": 0.0005427569759328493, "-7": 0.0001156644723983271, "-8": 2.189550172198389e-05, "-9": 3.7246287737810346e-06, "0": 0.17393148626169694, "1": 0.1946496341250983, "10": 0.0001435962047035787, "11": 3.521068397344901e-05, "12": 7.952579624188763e-06, "13": 1.6643314456890458e-06, "14": 3.2443422791812774e-07, "15": 5.917581549065254e-08, "16": 1.0139039280849599e-08, "17": 1.6353039378320826e-09, "18": 2.447431614160104e-10, "19": 2.905417684493373e-11, "2": 0.1743163542072238, "3": 0.1234655392305631, "4": 0.07185659414198815, "5": 0.035260123808594016, "6": 0.014898765700195325, "7": 0.005514451697065941, "8": 0.0018130706868261111, "9": 0.0005356736805773881} |
| Research history json | {"away": [{"away": "Sociedad", "away_goals": 2.0, "away_xg": 3.69, "date": "2026-11-22T00:00:00+00:00", "home": "Santander", "home_goals": 3.0, "home_xg": 3.05, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 2.31, "date": "2026-11-07T00:00:00+00:00", "home": "Malaga", "home_goals": 1.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Real Madrid", "away_goals": 3.0, "away_xg": 3.36, "date": "2026-11-01T00:00:00+00:00", "home": "Santander", "home_goals": 0.0, "home_xg": 0.97, "source": "pipeline training history"}, {"away": "Espanol", "away_goals": 1.0, "away_xg": 0.52, "date": "2026-10-24T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.28, "date": "2026-10-18T00:00:00+00:00", "home": "Osasuna", "home_goals": 2.0, "home_xg": 3.65, "source": "pipeline training history"}, {"away": "Valencia", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-11T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 1.28, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 0.0, "away_xg": 0.61, "date": "2026-09-19T00:00:00+00:00", "home": "Celta", "home_goals": 5.0, "home_xg": 2.08, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 1.98, "date": "2026-09-16T00:00:00+00:00", "home": "Barcelona", "home_goals": 7.0, "home_xg": 6.74, "source": "pipeline training history"}, {"away": "Alaves", "away_goals": 1.0, "away_xg": 1.98, "date": "2026-09-12T00:00:00+00:00", "home": "Santander", "home_goals": 2.0, "home_xg": 2.02, "source": "pipeline training history"}, {"away": "Santander", "away_goals": 2.0, "away_xg": 0.48, "date": "2026-09-05T00:00:00+00:00", "home": "Vallecano", "home_goals": 3.0, "home_xg": 1.61, "source": "pipeline training history"}], "h2h": [], "home": [{"away": "Elche", "away_goals": 1.0, "away_xg": 0.34, "date": "2026-11-23T00:00:00+00:00", "home": "Levante", "home_goals": 1.0, "home_xg": 0.81, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 0.0, "away_xg": 0.28, "date": "2026-11-08T00:00:00+00:00", "home": "Celta", "home_goals": 0.0, "home_xg": 3.16, "source": "pipeline training history"}, {"away": "Ath Madrid", "away_goals": 2.0, "away_xg": 0.7, "date": "2026-10-31T00:00:00+00:00", "home": "Levante", "home_goals": 0.0, "home_xg": 1.4, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 1.0, "away_xg": 0.48, "date": "2026-10-25T00:00:00+00:00", "home": "Sociedad", "home_goals": 2.0, "home_xg": 2.22, "source": "pipeline training history"}, {"away": "Ath Bilbao", "away_goals": 1.0, "away_xg": 1.9, "date": "2026-10-21T00:00:00+00:00", "home": "Levante", "home_goals": 3.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 1.0, "away_xg": 0.83, "date": "2026-10-16T00:00:00+00:00", "home": "La Coruna", "home_goals": 1.0, "home_xg": 1.08, "source": "pipeline training history"}, {"away": "Sevilla", "away_goals": 3.0, "away_xg": 2.53, "date": "2026-10-12T00:00:00+00:00", "home": "Levante", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 1.0, "away_xg": 0.45, "date": "2026-09-20T00:00:00+00:00", "home": "Villarreal", "home_goals": 3.0, "home_xg": 4.27, "source": "pipeline training history"}, {"away": "Barcelona", "away_goals": 4.0, "away_xg": 2.59, "date": "2026-09-13T00:00:00+00:00", "home": "Levante", "home_goals": 2.0, "home_xg": 2.42, "source": "pipeline training history"}, {"away": "Levante", "away_goals": 0.0, "away_xg": 0.98, "date": "2026-09-06T00:00:00+00:00", "home": "Malaga", "home_goals": 0.0, "home_xg": 1.59, "source": "pipeline training history"}], "teams": {"away": "Santander", "home": "Levante"}} |
| Unadjusted home-win probability | 62.2% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 20.4% |
| Raw p over 1 5 | 93.5% |
| Raw p under 3 5 | 36.1% |
| Raw p btts yes | 75.1% |
| P home draw | 73.2% |
| P draw away | 48.7% |
| P home away | 78.0% |
| Raw p home draw | 79.6% |
| Raw p draw away | 37.8% |
| Raw p home away | 82.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7986 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:37:12Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8403, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:37:12Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.8403, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-24T22:37:12Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.27, "draw": 4.01, "home": 2.1}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.10 |
| Reference draw odds | 4.01 |
| Reference away odds | 3.27 |
| Market reference 1x2 last update utc | 2026-11-24T22:37:12Z |
| Market reference home last update utc | 2026-11-24T22:37:12Z |
| Market reference draw last update utc | 2026-11-24T22:37:12Z |
| Market reference away last update utc | 2026-11-24T22:37:12Z |
| O/U 2.5 market source | The Odds API / unavailable reference |
| Home probability edge | +4.7% |
| Draw probability edge | -2.0% |
| Away probability edge | -2.7% |
| Raw edge prob home | 0.1568 |
| Raw ev home | 0.3072 |
| Raw edge prob draw | -0.0653 |
| Raw ev draw | -0.3025 |
| Raw edge prob away | -0.0915 |
| Raw ev away | -0.3343 |
| Count model | {"corners": {"alpha": 0.014629289567137405, "mu": 10.44265537711092, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-23 |
| Elo home rating | 1,462.0242 |
| Elo away rating | 1,414.7133 |
| Elo rating diff | 107.3109 |
| Elo home expectancy | 0.6497 |
| Research p home | 0.6367 |
| Research p draw | 0.1868 |
| Research p away | 0.1765 |
| Research p over 1 5 | 0.9212 |
| Research v4 p home | 0.6196 |
| Research v4 p draw | 0.1765 |
| Research v4 p away | 0.2039 |
| Research v4 p over 1 5 | 0.9192 |
| Research version | team-form-research-v5 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.7861079080878777, 1.6041332970268065], "c6_fit": {"candidate_version": "research-low-score-then-sharpen-walk-forward-v1", "delta": 0.055466179703356835, "end_exclusive": "2026-11-30", "expected_origin": "2026-11-16", "fits_version": "research-c6-live-fits-v1", "low_score_status": "fitted", "origin": "2026-11-16", "rho": -0.016463701485858812, "slope": 1.1507759984871408, "slope_status": "fitted", "stale": false}, "coverage": {"form": "last ten, exponential rank half-life five matches", "team_news": "dated news leads; absences and tactics require confirmation", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [{"headline": "Levante vs. Elche - Game Highlights", "published_at_utc": "2026-11-23T22:03:25+00:00", "source": "ESPN league news; unconfirmed context lead", "url": "https://www.espn.com/video/clip/_/id/50576820/levante-vs-elche-game-highlights"}], "quality_review": {"absence_note": "Reported absences only; not proof of complete coverage or a fitted player-value effect", "assessed_at_utc": "2026-11-24T22:39:49.304391+00:00", "availability": "UNAVAILABLE_OR_STALE", "form": {"away": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}, "home": {"matches": 10.0, "venue_matches": 5.0, "xg_matches": 10.0}}, "lineups": "UNCONFIRMED_OR_STALE", "probability_effect": "NONE; factual coverage/freshness review, not a calibrated confidence score", "status": "REVIEW_REQUIRED", "summary_max_age_minutes": 180, "training": {"cutoff": "2026-11-23", "status": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "version": "pre-match-research-quality-v1", "warnings": ["Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"], "weather": "UNAVAILABLE_INCOMPLETE_OR_STALE", "weather_max_age_minutes": 180}, "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-24T22:39:49.041799+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard?dates=20261127"}, {"observed_at_utc": "2026-11-24T22:39:49.113032+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/news?limit=20"}, {"observed_at_utc": "2026-11-24T22:39:49.303848+00:00", "reason": null, "status": "available", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Levante_vs_Real+Racing+Club+de+Santander&d=2026-11-27"}]}, "evidence_quality_version": "pre-match-research-quality-v1", "form": {"away": {"all": {"goals_against": 2.411704945971278, "goals_for": 1.5624668612378825, "last_match": "2026-11-22T00:00:00+00:00", "matches": 10, "points_per_game": 1.5672951587760322, "results": "WWLWLDLLWL", "xg_against": 2.7459202910925207, "xg_for": 1.7112432801849509, "xg_matches": 10}, "venue": {"goals_against": 3.332473227681091, "goals_for": 1.156813568361292, "last_match": "2026-11-07T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 3.1444041299909373, "xg_for": 1.19042948522948, "xg_matches": 5}}, "home": {"all": {"goals_against": 1.4967280156107592, "goals_for": 1.074829103097319, "last_match": "2026-11-23T00:00:00+00:00", "matches": 10, "points_per_game": 0.831246261816017, "results": "DDLLWDDLLD", "xg_against": 1.855031254163991, "xg_for": 1.0498672630030268, "xg_matches": 10}, "venue": {"goals_against": 2.0130987366246735, "goals_for": 1.6573502179419108, "last_match": "2026-11-23T00:00:00+00:00", "matches": 5, "points_per_game": 1.0183343963961224, "results": "DLWDL", "xg_against": 1.4358681704724323, "xg_for": 1.606668262790877, "xg_matches": 5}}}, "goal_rates": [2.649250670855554, 1.50713847396819], "h2h": [], "margin_distribution": {"-1": 0.09908975214919455, "-10": 3.247345508258031e-07, "-11": 4.321741709032522e-08, "-12": 5.295213295532327e-09, "-13": 6.00951993268955e-10, "-14": 6.350614552146082e-11, "-15": 6.27786424705167e-12, "-16": 5.828614433689485e-13, "-17": 5.095285829028879e-14, "-18": 4.146415868614447e-15, "-19": 2.717905714513979e-16, "-2": 0.04960603057966657, "-3": 0.019431927738474138, "-4": 0.0062158610331568215, "-5": 0.0016695897576080793, "-6": 0.00038509550458675244, "-7": 7.765589499592586e-05, "-8": 1.3891092507121109e-05, "-9": 2.2306107484786434e-06, "0": 0.1868226990218561, "1": 0.20686774408716024, "10": 0.0001082012442695266, "11": 2.531234960321036e-05, "12": 5.451637968773914e-06, "13": 1.0875599985532234e-06, "14": 2.0202219993919978e-07, "15": 3.5104691315776946e-08, "16": 5.729127165798912e-09, "17": 8.803625964972339e-10, "18": 1.2593190857567486e-10, "19": 1.4509993259113273e-11, "2": 0.18133392483315855, "3": 0.12486202332241864, "4": 0.07020785009041797, "5": 0.03314851259691349, "6": 0.013439794230364833, "7": 0.00476396427870592, "8": 0.0014979605185640274, "9": 0.0004228220722834402}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-24T22:39:49.304391+00:00", "p_over_1_5": 0.9212373362446077, "shadow_v4": {"grid": "independent Poisson (C)", "margin_distribution": {"-1": 0.11492683598821223, "-10": 3.7326098298383333e-07, "-11": 4.9675575155568964e-08, "-12": 6.086499002872378e-09, "-13": 6.907547446467792e-10, "-14": 7.299613251061335e-11, "-15": 7.2159915658330196e-12, "-16": 6.699608487671356e-13, "-17": 5.856695544993403e-14, "-18": 4.766032006889903e-15, "-19": 3.1240536495947605e-16, "-2": 0.057018865682774075, "-3": 0.022335721377626024, "-4": 0.007144722954261831, "-5": 0.0019190834868656464, "-6": 0.00044264192467100114, "-7": 8.926033779576938e-05, "-8": 1.596689613329371e-05, "-9": 2.5639401736406945e-06, "0": 0.17648285724496615, "1": 0.2020185952385844, "10": 0.00010512634361236642, "11": 2.459301443331805e-05, "12": 5.29671142161679e-06, "13": 1.0566533396064716e-06, "14": 1.9628106267642854e-07, "15": 3.4107073967427394e-08, "16": 5.566314833962996e-09, "17": 8.553441455100582e-10, "18": 1.2235313172286714e-10, "19": 1.4097643215367956e-11, "2": 0.17618071418018322, "3": 0.1213136508414879, "4": 0.06821265894600681, "5": 0.03220648661693278, "6": 0.013057857475477764, "7": 0.004628580282059905, "8": 0.001455390954655327, "9": 0.00041080616732131636}, "p_over_1_5": 0.9192302357581298, "version": "team-form-research-v4"}, "version": "team-form-research-v5", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing", "Research review: starting XIs not freshly confirmed for both teams; check before betting tight AH", "Research review: missing absence reports do not mean both teams have full squads", "Research review: match-window weather missing, incomplete or stale; no numerical weather adjustment", "Research review: inspect training status RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED; completeness/freshness not established by this review"]} |

</details>
