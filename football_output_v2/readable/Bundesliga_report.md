# Bundesliga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,595 |
| Training data through | 2026-10-25 |
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
| Training sha256 | d416c800c8cd5396cd2db39cef51d74d5912c40efad2b0935eb158da772490ea |
| Training as of utc | 2026-10-27T11:16:39.568817+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 44, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-27T11:16:39.568817+00:00', 'observations': 244, 'observations_sha256': '05b2bdee66ed9f00c42c7ebcab62d7126dfe2cc10cc19b9613387901fab98719', 'eligible_training_matches': 54, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 88, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 54, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'ea2c4718386038287fc35a5b9134b8fb08f7ffb65b196a19b723516e9afa60b8', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-27', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-10-28', 'audit_start_date': '2026-04-28', 'training_shot_matches': 1295, 'tuning_matches': 207, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7186137182435159, 'audit_candidate_poisson_score': 0.7073850582948938, 'audit_gain': 0.0112286599486221, 'audit_gain_lower95': 0.0026023292935761426, 'audit_baseline_briers': [0.6258342320050883, 0.15383815738674458, 0.2944585981957748, 0.2450746250555013], 'audit_candidate_briers': [0.6198817111628098, 0.15130525608300216, 0.2911944534960592, 0.24282563076420938], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1582.206 |
| Base scoring parameter | 0.225 |
| Home-advantage parameter | 0.227 |
| Dixon-Coles low-score adjustment | -0.074 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1595, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261027T111639568817Z_2d6883f1e8fdee4c63cea3b8366bab090e838a70c850f48f22a06addda88ef58.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 1} |
| Shot features applied fixtures | 1 |
| Goal rate features used | {'shot_features': 1} |
| Legacy comparison status | {'AVAILABLE': 1} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — SV 07 Elversberg vs 1. FSV Mainz 05

The model's most likely 1X2 outcome is **SV 07 Elversberg win** at **41.5%**. Expected goals are 1.83 for SV 07 Elversberg and 1.67 for 1. FSV Mainz 05 (3.51 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.1%; Under 3.5 goals: 53.5%; Double Chance 1X: 65.1%; Double Chance X2: 58.5%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 69.0%; BTTS No (at least one team does not score): 31.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SV 07 Elversberg win | 41.5% | 2.41 |
| Draw | 23.5% | 4.25 |
| 1. FSV Mainz 05 win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SV 07 Elversberg expected goals | 1.83 |
| 1. FSV Mainz 05 expected goals | 1.67 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.1% |
| Under 2.5 | 31.9% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.87% |
| 2 | 2-1 | 8.43% |
| 3 | 1-2 | 7.70% |
| 4 | 2-2 | 7.06% |
| 5 | 3-1 | 5.16% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | fdorg:565846 |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.8830 |
| Dc lambda away | 1.7413 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-27T11:16:39.568817+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.6418 |
| Shot lambda away | 1.4043 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 69.0% |
| P btts no | 31.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.24 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.80 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.13 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.17147568365863713, "-10": 1.8772233635335481e-06, "-11": 2.792795176743775e-07, "-12": 3.821589852973095e-08, "-13": 4.8398342291825556e-09, "-14": 5.698724639002887e-10, "-15": 6.190694664146846e-11, "-16": 5.433507123481411e-12, "-2": 0.10520434829118315, "-3": 0.04793818858626584, "-4": 0.01759461888518904, "-5": 0.00537559552868991, "-6": 0.0014022526250071531, "-7": 0.000318532684159765, "-8": 6.400472150821394e-05, "-9": 1.1521123813473116e-05, "0": 0.2353565235401223, "1": 0.18861056987928512, "10": 4.700355330863166e-06, "11": 7.665055422350976e-07, "12": 1.1496926706559544e-07, "13": 1.595988097907386e-08, "14": 2.059862863714642e-09, "15": 2.452796364761875e-10, "16": 2.359738206259634e-11, "2": 0.1264027837094396, "3": 0.0631343976692527, "4": 0.025399534652252316, "5": 0.008506167959098483, "6": 0.00243217659809932, "7": 0.0006055978421315155, "8": 0.00013338402051912758, "9": 2.6317710757808798e-05} |
| Raw goal margin distribution | {"-1": 0.17147568365863713, "-10": 1.8772233635335481e-06, "-11": 2.792795176743775e-07, "-12": 3.821589852973095e-08, "-13": 4.8398342291825556e-09, "-14": 5.698724639002887e-10, "-15": 6.190694664146846e-11, "-16": 5.433507123481411e-12, "-2": 0.10520434829118315, "-3": 0.04793818858626584, "-4": 0.01759461888518904, "-5": 0.00537559552868991, "-6": 0.0014022526250071531, "-7": 0.000318532684159765, "-8": 6.400472150821394e-05, "-9": 1.1521123813473116e-05, "0": 0.2353565235401223, "1": 0.18861056987928512, "10": 4.700355330863166e-06, "11": 7.665055422350976e-07, "12": 1.1496926706559544e-07, "13": 1.595988097907386e-08, "14": 2.059862863714642e-09, "15": 2.452796364761875e-10, "16": 2.359738206259634e-11, "2": 0.1264027837094396, "3": 0.0631343976692527, "4": 0.025399534652252316, "5": 0.008506167959098483, "6": 0.00243217659809932, "7": 0.0006055978421315155, "8": 0.00013338402051912758, "9": 2.6317710757808798e-05} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 34.9% |
| Raw p over 1 5 | 87.2% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 69.0% |
| P home draw | 65.1% |
| P draw away | 58.5% |
| P home away | 76.5% |
| Raw p home draw | 65.1% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.6807 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04221987312008366, 0.04272725449582134, 0.04455009550698248, 0.024874808075921184, 0.010416746638347844, 0.0034897510829864074, 0.0009742615300164666, 0.0002331362830262578, 4.881488100488084e-05, 9.085358721285112e-06, 1.5218590572321595e-06, 2.3174698996784865e-07, 3.2349324013902284e-08, 4.168254344174552e-09, 4.987220035735569e-10, 5.569287329669927e-11, 5.830583184025631e-12], [0.045888973232443446, 0.10486102457754874, 0.07906008111868283, 0.04414366168947412, 0.018485905021044673, 0.006193028332827567, 0.001728956912827302, 0.0004137314014259581, 8.66285113000453e-05, 1.612317974457661e-05, 2.700741696437414e-06, 4.1126591575986707e-07, 5.740818625793557e-08, 7.397122785563767e-09, 8.850486538691617e-10, 9.883442516704501e-11, 1.0347146829933183e-11], [0.050003587520329615, 0.0837593923326681, 0.07015132465331134, 0.03916940507454711, 0.016402850924157875, 0.0054951770225375686, 0.0015341322192834567, 0.0003671107523546824, 7.686691860737842e-05, 1.430636549698915e-05, 2.396413017425353e-06, 3.64923085925016e-07, 5.093923829767632e-08, 6.5635900531332014e-09, 7.853183879023339e-10, 8.769742895164252e-11, 9.181195443152579e-12], [0.029579343138653166, 0.04954740109168738, 0.04149762459958948, 0.023170442976034177, 0.009703014923490868, 0.0032506413003106404, 0.0009075073526634384, 0.0002171623167912392, 4.547019672486856e-05, 8.462850669072172e-06, 1.4175847466052469e-06, 2.1586821492365414e-07, 3.013282213433191e-08, 3.882655065981913e-09, 4.645507096748394e-10, 5.187692467632753e-11, 5.4310849261692904e-12], [0.013123121518408108, 0.02198211645199929, 0.018410766182094827, 0.010279759675004307, 0.004304823245702943, 0.00144217404006474, 0.0004026231824021976, 9.634586742213342e-05, 2.017323083508955e-05, 3.7546140629893764e-06, 6.289232592197948e-07, 9.577172836887888e-08, 1.336867707669524e-08, 1.7225722020297547e-09, 2.0610178481479383e-10, 2.3015628958951545e-11, 2.4095459837908822e-12], [0.004657745578179802, 0.007802038985900756, 0.006534471593154659, 0.0036485606800058393, 0.001527896500035668, 0.0005118660029669586, 0.00014290169795928246, 3.4195716113110814e-05, 7.160017270886078e-06, 1.3326125971728288e-06, 2.2322162646565002e-07, 3.3991938861425266e-08, 4.744899790247793e-09, 6.113867836890073e-10, 7.315101635914132e-11, 8.16886011931005e-12, 8.552120877399517e-13], [0.001377631701460534, 0.002307626310325051, 0.0019327151017426553, 0.0010791428542223428, 0.0004519093238712915, 0.0001513957387218956, 4.2266350962471147e-05, 1.0114142513979047e-05, 2.1177341290574078e-06, 3.9414977242023945e-07, 6.602275369253545e-08, 1.005387086597971e-08, 1.4034094953407227e-09, 1.8083121993819145e-10, 2.1636037743777554e-11, 2.416121807485248e-12, 2.5294796887622626e-13], [0.00034925586203150355, 0.0005850271995081859, 0.0004899800710195647, 0.00027358325698151673, 0.00011456761651275297, 3.83817018577274e-05, 1.0715324585427173e-05, 2.5641276682906138e-06, 5.368859166156965e-07, 9.992447066237557e-08, 1.6738024923594345e-08, 2.5488476581429446e-09, 3.55791023507064e-10, 4.58441567036854e-11, 5.48514744916071e-12, 6.12532873446328e-13, 6.412712543223597e-14], [7.747513352428844e-05, 0.00012977609061046722, 0.00010869186620282676, 6.0688743322340616e-05, 2.5414437814316096e-05, 8.51418057529592e-06, 2.376971421991989e-06, 5.687982796297876e-07, 1.1909695039953001e-07, 2.2166161111457816e-08, 3.712981962121992e-09, 5.654087278566055e-10, 7.892482288662808e-11, 1.0169570644475115e-11, 1.2167656358071484e-12, 1.3587765107859437e-13, 1.4225266188783767e-14], [1.527666095488447e-05, 2.558944071629055e-05, 2.143202228897999e-05, 1.1966695807278011e-05, 5.011256285561438e-06, 1.6788386678505385e-06, 4.68694726441967e-07, 1.1215648265906801e-07, 2.348371211833962e-08, 4.370756300341545e-09, 7.321312527865091e-10, 1.1148812584737312e-10, 1.5562512838849567e-11, 2.005250920202517e-12, 2.3992364045365435e-13, 2.679255539744283e-14, 2.8049589419668838e-15], [2.7110470596555286e-06, 4.541187254008388e-06, 3.8033979532964217e-06, 2.123649636391275e-06, 8.893142067022044e-07, 2.97932293421552e-07, 8.31761249234425e-08, 1.990366241891058e-08, 4.1674976538551456e-09, 7.75648949171919e-10, 1.299264470168242e-10, 1.9785053596308747e-11, 2.7617752856604918e-12, 3.5585849729475064e-13, 4.2577647164825034e-14, 4.7546959866037405e-15, 4.977773424789155e-16], [4.373740250136232e-07, 7.326310845664854e-07, 6.136033181855578e-07, 3.4260902476004544e-07, 1.4347332433859074e-07, 4.80655051306565e-08, 1.3418828866594588e-08, 3.2110637525330994e-09, 6.723436307052005e-10, 1.2513567467914593e-10, 2.09610721750762e-11, 3.19192855605662e-12, 4.4555802473822055e-13, 5.741075675642495e-14, 6.8690644265155616e-15, 7.670765116269262e-16, 8.030656607939938e-17], [6.468154090220049e-08, 1.083459573556857e-07, 9.074340462195688e-08, 5.066711414284296e-08, 2.1217711079875355e-08, 7.1082203292631484e-09, 1.984458332127135e-09, 4.748717106430218e-10, 9.943028063552207e-11, 1.8505827500459187e-11, 3.0998513165109377e-12, 4.720418809714347e-13, 6.589184074319734e-14, 8.49025319062173e-15, 1.0158391816927802e-15, 1.1343995739200305e-16, 1.1876225247757098e-17], [8.829693357063961e-09, 1.4790333788966482e-08, 1.2387404904273108e-08, 6.916580448278129e-09, 2.8964350564459774e-09, 9.703449383919454e-10, 2.7089890420277666e-10, 6.482485621766693e-11, 1.3573252525723409e-11, 2.526235149450763e-12, 4.2316148000660025e-13, 6.443855546007343e-14, 8.99491169164668e-15, 1.1590065906187065e-15, 1.3867246125135043e-16, 1.5485717010426264e-17, 1.621226484626755e-18], [1.1192476775998263e-09, 1.874815588129496e-09, 1.5702214799457774e-09, 8.767424066289219e-10, 3.6715071284467007e-10, 1.2300045707669576e-10, 3.4339014633019636e-11, 8.217167554784972e-12, 1.7205389533418033e-12, 3.2022435092060856e-13, 5.363974541292349e-14, 8.16820025679317e-15, 1.1401906741231061e-15, 1.469151172543356e-16, 1.7578054404171937e-17, 1.9629620303882278e-18, 2.0550588841572175e-19], [1.324169434819289e-10, 2.2180733964510777e-10, 1.857711506804051e-10, 1.0372641554705183e-10, 4.343719103921609e-11, 1.4552046789057172e-11, 4.0626104935385365e-12, 9.721639217665064e-13, 2.0355504318015307e-13, 3.788538553711641e-14, 6.3460584094842955e-15, 9.663706553962354e-16, 1.3489468602494888e-16, 1.738136354218452e-17, 2.0796399967083282e-18, 2.3223584684356617e-19, 2.43131722818528e-20], [1.4686969486306347e-11, 2.460166760797545e-11, 2.060472889446718e-11, 1.150477167048782e-11, 4.817817739849051e-12, 1.6140341374316064e-12, 4.506027309223561e-13, 1.0782715171658637e-13, 2.257722183701268e-14, 4.202041572093196e-15, 7.038703942832915e-16, 1.0718459401838797e-16, 1.4961787256354207e-17, 1.9278466128415053e-18, 2.3066239388259075e-19, 2.5758341089359546e-20, 2.696685258164212e-21]] |
| Legacy trial inputs | {"lambda_home": 1.7746332576614003, "lambda_away": 1.675067659867697, "rho": -0.11085966878002378, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3979 |
| Legacy p draw | 0.2453 |
| Legacy p away | 0.3568 |
| Legacy p over 1 5 | 0.8692 |
| Legacy p under 3 5 | 0.5475 |
| Legacy p btts yes | 0.6854 |
| Legacy p over 2 5 | 0.6697 |
| Legacy goal margin distribution | {"-1": 0.17225550529752837, "-10": 1.9881613899485874e-06, "-11": 2.9620718782963896e-07, "-12": 4.058605165802851e-08, "-13": 5.146431511921526e-09, "-14": 6.067376241837545e-10, "-15": 6.604002012663246e-11, "-16": 5.830583184025631e-12, "-2": 0.10878628980533044, "-3": 0.04986731482599131, "-4": 0.018382644003257145, "-5": 0.005635277200658935, "-6": 0.0014739870664146645, "-7": 0.00033558944765310666, "-8": 6.756434430846271e-05, "-9": 1.2182954529249197e-05, "0": 0.2452643086551707, "1": 0.1831163504821313, "10": 3.541720282654614e-06, "11": 5.590291809053876e-07, "12": 8.115064040439967e-08, "13": 1.0901784867544351e-08, "14": 1.3616597461394012e-09, "15": 1.5701861108990437e-10, "16": 1.4686969486306347e-11, "2": 0.1221030999235501, "3": 0.059298645124787296, "4": 0.023158638628715016, "5": 0.00752136379902625, "6": 0.002084256893732974, "7": 0.0005027384854358387, "8": 0.00010723280460840949, "9": 2.0485142247172426e-05} |
| Legacy market blend applied | 0 |
| Legacy raw p home | 0.3979 |
| Legacy raw p draw | 0.2453 |
| Legacy raw p away | 0.3568 |
| Legacy market weight | 0 |
| Legacy lambda home | 1.7746 |
| Legacy lambda away | 1.6751 |
| Legacy model home team | Elversberg |
| Legacy model away team | Mainz |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 90/100 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.093446341951529, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,430.0448 |
| Elo away rating | 1,516.7168 |
| Elo rating diff | -26.6720 |
| Elo home expectancy | 0.4617 |

</details>


---
