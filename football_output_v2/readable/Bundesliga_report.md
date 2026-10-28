# Bundesliga — football model report

Fixtures in this report: **6**.

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
| Training sha256 | 157145a543f3ae14e59f10e73d35c6980ff24d7eaab3b250d7dd1b775467ecae |
| Training as of utc | 2026-10-28T16:04:41.599646+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 51, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-28T16:04:41.599646+00:00', 'observations': 262, 'observations_sha256': '71a31c0c6acb88e6ff92aa936a5c23b55f083658064152074249d035f64249f4', 'eligible_training_matches': 59, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 59, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'c1f0ef7e4785a136a353ea55d0261f2f82942dfd7d64beb26b52203d2ee89021', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1295, 'tuning_matches': 207, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7186312149690913, 'audit_candidate_poisson_score': 0.7073931745812553, 'audit_gain': 0.011238040387836046, 'audit_gain_lower95': 0.0026129711351637174, 'audit_baseline_briers': [0.6258589840085264, 0.15383203970219236, 0.29445155359603986, 0.24507738272494933], 'audit_candidate_briers': [0.6198990730161955, 0.15129996655980035, 0.29118797323657974, 0.24282660793240185], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1579.467 |
| Base scoring parameter | 0.225 |
| Home-advantage parameter | 0.227 |
| Dixon-Coles low-score adjustment | -0.074 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1595, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
| Training data health | {'training_end': '2026-10-25', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261028T160441599646Z_54474c2b544bc31025fc1ffd074f977c260a579a3b627a5ce3101f3e1925ce0d.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 6} |
| Shot features applied fixtures | 6 |
| Goal rate features used | {'shot_features': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
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

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **42.2%**. Expected goals are 1.83 for Elversberg and 1.67 for FSV Mainz 05 (3.51 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 67.8%; Under 3.5 goals: 53.6%; Double Chance 1X: 57.8%; Double Chance X2: 66.3%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 69.1%; BTTS No (at least one team does not score): 30.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 33.7% | 2.97 |
| Draw | 24.0% | 4.16 |
| FSV Mainz 05 win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.83 |
| FSV Mainz 05 expected goals | 1.67 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 87.1% |
| Under 1.5 | 12.9% |
| Over 2.5 | 67.8% |
| Under 2.5 | 32.2% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.09% |
| 2 | 1-2 | 9.30% |
| 3 | 2-2 | 7.21% |
| 4 | 2-1 | 6.85% |
| 5 | 0-1 | 5.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 33.7% | 30.4% | 3.17 | +6.9% |
| Draw | 24.0% | 24.3% | 3.94 | -5.3% |
| FSV Mainz 05 win | 42.2% | 45.4% | 2.15 | -9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | b275fe870ec88a9f0054c9220beb2673 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8830 |
| Dc lambda away | 1.7409 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.6418 |
| Shot lambda away | 1.4043 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 69.1% |
| P btts no | 30.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.65 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.75 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.11 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.64 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.20728894858749283, "-10": 2.26594580456558e-06, "-11": 3.3705053200728775e-07, "-12": 4.611286403041195e-08, "-13": 5.838891373444009e-09, "-14": 6.873841322734937e-10, "-15": 7.465948283666449e-11, "-16": 6.551791729535859e-12, "-2": 0.12716137423396873, "-3": 0.05793453540088578, "-4": 0.021260129514590883, "-5": 0.006494416243352647, "-6": 0.0016938134314787977, "-7": 0.0003846962162264337, "-8": 7.728579867644986e-05, "-9": 1.3909313594809168e-05, "0": 0.24046890566985502, "1": 0.15316155531952677, "10": 3.817098574217441e-06, "11": 6.224635508970713e-07, "12": 9.336327070289838e-08, "13": 1.2960429930186507e-08, "14": 1.672721223053796e-09, "15": 1.9917925046838926e-10, "16": 1.9162591953004062e-11, "2": 0.10264992928694928, "3": 0.05127149987288598, "4": 0.02062716067387814, "5": 0.006907942560058794, "6": 0.001975191562809389, "7": 0.0004918091631437346, "8": 0.00010832119749910616, "9": 2.1372459550316117e-05} |
| Raw goal margin distribution | {"-1": 0.17146210036742884, "-10": 1.874310375044374e-06, "-11": 2.7879630121012533e-07, "-12": 3.8142933207434644e-08, "-13": 4.82972481422667e-09, "-14": 5.685798875529974e-10, "-15": 6.175568850510772e-11, "-16": 5.419410821325132e-12, "-2": 0.10518339959914523, "-3": 0.047921402425630304, "-4": 0.017585628589923123, "-5": 0.005371951844676294, "-6": 0.0014010626739675593, "-7": 0.00031820712916465985, "-8": 6.392808425117316e-05, "-9": 1.1505293166309736e-05, "0": 0.23536983622969307, "1": 0.1886289818174648, "10": 4.7010192345555076e-06, "11": 7.666066434181011e-07, "12": 1.149832845135049e-07, "13": 1.5961660199568356e-08, "14": 2.060071148473611e-09, "15": 2.453029360836485e-10, "16": 2.3600048991000734e-11, "2": 0.12642044281045128, "3": 0.06314437586573497, "4": 0.02540376602719724, "5": 0.008507606029718182, "6": 0.002432584159973477, "7": 0.0006056967853242662, "8": 0.00013340499938694435, "9": 2.6321652816208403e-05} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 34.9% |
| Raw p over 1 5 | 87.2% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 68.9% |
| P home draw | 57.8% |
| P draw away | 66.3% |
| P home away | 76.0% |
| Raw p home draw | 65.1% |
| Raw p draw away | 58.5% |
| Raw p home away | 76.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6785 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.17 |
| Reference draw odds | 3.94 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | +3.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +1.8% |
| Under 2.5 probability edge | -1.8% |
| Raw edge prob home | 0.1116 |
| Raw ev home | 0.3165 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | -0.0726 |
| Raw edge prob away | -0.1043 |
| Raw ev away | -0.2490 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0419853468190243, 0.04851686514427641, 0.05059778582974108, 0.028260618863685194, 0.011838402097958457, 0.003967294981300972, 0.0011079359456916725, 0.0002652088565292057, 5.554813039793252e-05, 1.0341852685337082e-05, 1.732885059841281e-06, 2.639662985300923e-07, 3.685858399376764e-08, 4.750799529243368e-09, 5.686042210515804e-10, 6.351703700827164e-11, 6.651837914465022e-12], [0.040449634188274255, 0.10429402855095224, 0.08977721187427122, 0.050143687630136664, 0.021005241948285312, 0.007039293839902259, 0.0019658449180797156, 0.0004705682533950032, 9.856076091423611e-05, 1.8349868170679186e-05, 3.074711405250556e-06, 4.683635444156845e-07, 6.539932232862753e-08, 8.429490123229221e-09, 1.0088920056250197e-09, 1.1270023768047382e-10, 1.1802561159686472e-11], [0.044069800622178315, 0.07384353791524506, 0.06978414793919581, 0.044485745716979025, 0.018635124303730728, 0.006245018078821646, 0.0017440296331965512, 0.00041747188235178494, 8.7439698891781e-05, 1.6279368509991983e-05, 2.727777636458978e-06, 4.1551594078327995e-07, 5.8020017287790046e-08, 7.478352148962988e-09, 8.950541003121928e-10, 9.998375374138778e-11, 1.047082413307293e-11], [0.026064802130719628, 0.04367428890578035, 0.03659040843393708, 0.023052619519577534, 0.011021625258128909, 0.0036935760595507594, 0.0010314951884874833, 0.00024691107867554687, 5.171565148486306e-05, 9.628328538715213e-06, 1.6133266624111852e-06, 2.457542495262751e-07, 3.4315568685965816e-08, 4.423023618774144e-09, 5.293740314583125e-10, 5.913475261434156e-11, 6.192902062660153e-12], [0.01156189557001879, 0.01937315943896334, 0.016230872540517353, 0.009065505440022572, 0.004283574369745309, 0.0016384064788320855, 0.0004575534312694153, 0.00010952548545775394, 2.294016884550835e-05, 4.270960067916826e-06, 7.156438133532106e-07, 1.090123360484795e-07, 1.5221792959837432e-08, 1.9619768041024975e-09, 2.3482116758474186e-10, 2.6231153831783808e-11, 2.7470642809692332e-12], [0.004102925577615484, 0.006874878855285869, 0.005759787544370395, 0.003217041177947647, 0.0013476218342540543, 0.0005094156867489968, 0.00016237023288370365, 3.8866889340416445e-05, 8.140689815182367e-06, 1.5156192336722375e-06, 2.539577778131063e-07, 3.8684789975852915e-08, 5.401699340204542e-09, 6.962391904935135e-10, 8.333008794399652e-11, 9.30854904673882e-12, 9.74840175080758e-13], [0.0012133245649833633, 0.002033051596624595, 0.0017032947794123371, 0.0009513492296965822, 0.0003985211637103743, 0.00013355273791579054, 4.207032094939785e-05, 1.1493786740490775e-05, 2.4073795007539654e-06, 4.482016582042245e-07, 7.51008529061129e-08, 1.1439935987384693e-08, 1.5974002886822096e-09, 2.0589311137855602e-10, 2.4642524167702663e-11, 2.752740942799317e-12, 2.8828149791729303e-13], [0.000307548456508437, 0.0005153294498347859, 0.00043174406544247763, 0.00024114403980412782, 0.00010101548449796063, 3.385239167974842e-05, 9.45386762678478e-06, 2.552617585353575e-06, 6.102125276735707e-07, 1.1360828929324557e-07, 1.903625135460674e-08, 2.899747319896821e-09, 4.049023710461854e-10, 5.218892820410576e-11, 6.246284375156227e-12, 6.977533073659626e-13, 7.307239322696753e-14], [6.821158892819952e-05, 0.0001142956170022636, 9.575710133126308e-05, 5.348366336266529e-05, 2.2404361192977648e-05, 7.508167824058174e-06, 2.0967861118892204e-06, 5.019119104158144e-07, 1.185800951503115e-07, 2.5197336433045136e-08, 4.222075983979762e-09, 6.431388875301479e-10, 8.980384555790491e-11, 1.1575053107652719e-11, 1.3853718759115406e-12, 1.5475565156683854e-13, 1.6206825114275683e-14], [1.3447769548419219e-05, 2.2533137579579273e-05, 1.8878308679818686e-05, 1.0544190375970174e-05, 4.416972114809566e-06, 1.4802193031314805e-06, 4.1337691832238143e-07, 9.895086466880904e-08, 2.0725309122570274e-08, 4.352439943296852e-09, 8.323732922896718e-10, 1.267934625630253e-10, 1.7704636977387198e-11, 2.281997079210044e-12, 2.7312311615743177e-13, 3.0509747262696395e-14, 3.1951410702032617e-15], [2.386079224982923e-06, 3.998124094760105e-06, 3.3496365312882086e-06, 1.8708882175427204e-06, 7.837169846292372e-07, 2.6263987607044477e-07, 7.33467415057274e-08, 1.7557157090641545e-08, 3.677355516144094e-09, 6.846435469048552e-10, 1.2940134752931577e-10, 2.249735510383192e-11, 3.141388341427511e-12, 4.0490177962745175e-13, 4.8461076833552064e-14, 5.413438551343774e-15, 5.669237341591631e-16], [3.848812688633393e-07, 6.44908626064322e-07, 5.40305763905399e-07, 3.017795149171826e-07, 1.2641574693564915e-07, 4.2364548376144744e-08, 1.183103504784832e-08, 2.8320186638930467e-09, 5.931677549915672e-10, 1.1043492365754277e-10, 1.850452091260191e-11, 3.1795044726030585e-12, 5.067147470133875e-13, 6.531179228097641e-14, 7.816907564045695e-15, 8.732028160422131e-16, 9.144638780947552e-17], [5.6908892116105277e-08, 9.535677206071494e-08, 7.989009836360739e-08, 4.462139170345159e-08, 1.8691946545967605e-08, 6.264060395055482e-09, 1.7493475303390968e-09, 4.18744838090606e-10, 8.770632012116307e-11, 1.6329007578981343e-11, 2.7360951791327443e-12, 4.1678293246284423e-13, 6.564519757730098e-14, 9.657060609377965e-15, 1.155815014218835e-15, 1.2911255723195571e-16, 1.352134551423131e-17], [7.767323261367687e-09, 1.3014958580550507e-08, 1.0903958877051991e-08, 6.09023934301356e-09, 2.551207479325496e-09, 8.549627344327986e-10, 2.3876317495159307e-10, 5.7153221588693355e-11, 1.1970771440361214e-11, 2.228697057474033e-12, 3.734413892091808e-13, 5.688544699930173e-14, 7.943123943936931e-15, 1.154841193341839e-15, 1.5775370969204502e-16, 1.762218401785801e-17, 1.8454877196239846e-18], [9.844143723688874e-10, 1.6494887429500011e-09, 1.3819450373176857e-09, 7.718642495861992e-10, 3.2333472227610093e-10, 1.0835619624607384e-10, 3.0260347497548176e-11, 7.243480265450766e-12, 1.517150639634844e-12, 2.8246042313518556e-13, 4.7329183864840145e-14, 7.209543071712046e-15, 1.006694984720143e-15, 1.2975555600043668e-16, 1.7517503265311197e-17, 2.233398898947608e-18, 2.338932698042802e-19], [1.1644511873520434e-10, 1.951159165453753e-10, 1.63468513334223e-10, 9.130283619715772e-11, 3.8246851309222966e-11, 1.2817316052798364e-11, 3.5794578545630196e-12, 8.568220286512162e-13, 1.7946181133697364e-13, 3.341188267174904e-14, 5.598508706774963e-15, 8.528076413511453e-16, 1.1908066391166463e-16, 1.534861898517811e-17, 1.8370149042417377e-18, 2.314705271231726e-19, 2.766693613806626e-20], [1.291326033958362e-11, 2.163751176617735e-11, 1.8127951544364184e-11, 1.0125089882361977e-11, 4.2414104901077726e-12, 1.421384948053393e-12, 3.9694640404506267e-13, 9.501785940743163e-14, 1.9901539162645546e-14, 3.7052333671199026e-15, 6.20850416309929e-16, 9.457268120784034e-17, 1.3205530907642017e-17, 1.7020955018250977e-18, 2.0371701247617096e-19, 2.2756603875949237e-20, 2.688201053719183e-21]] |
| Legacy trial inputs | {"lambda_home": 1.774330840807281, "lambda_away": 1.6756040842645197, "rho": -0.11083277065839049, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3508 |
| Legacy p draw | 0.2440 |
| Legacy p away | 0.4053 |
| Legacy p over 1 5 | 0.8690 |
| Legacy p under 3 5 | 0.5479 |
| Legacy p btts yes | 0.6855 |
| Legacy p over 2 5 | 0.6701 |
| Legacy goal margin distribution | {"-1": 0.19561435475736313, "-10": 2.2639360631616593e-06, "-11": 3.37400553033148e-07, "-12": 4.624501003420437e-08, "-13": 5.8658681906724355e-09, "-14": 6.917752828651272e-10, "-15": 7.531959816795811e-11, "-16": 6.651837914465022e-12, "-2": 0.12356911948363643, "-3": 0.05666050815371851, "-4": 0.020893170530547414, "-5": 0.006406864207755104, "-6": 0.0016763282061261662, "-7": 0.00038177693894858025, "-8": 7.688747384323159e-05, "-9": 1.3868443732762265e-05, "0": 0.24395387888896172, "1": 0.16144023775806804, "10": 3.1173047377385987e-06, "11": 4.919535322869498e-07, "12": 7.140133998066072e-08, "13": 9.590405607534272e-09, "14": 1.197658240458627e-09, "15": 1.3808263050138168e-10, "16": 1.291326033958362e-11, "2": 0.10762657632937479, "3": 0.05225805354002491, "4": 0.02040517409376062, "5": 0.006625896777074914, "6": 0.001835783196110323, "7": 0.00044272619640521496, "8": 9.441572060033564e-05, "9": 1.803348403693946e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3977 |
| Legacy raw p draw | 0.2453 |
| Legacy raw p away | 0.3570 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7743 |
| Legacy lambda away | 1.6756 |
| Legacy model home team | Elversberg |
| Legacy model away team | Mainz |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.093593341434618, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,430.0448 |
| Elo away rating | 1,516.7168 |
| Elo rating diff | -26.6720 |
| Elo home expectancy | 0.4617 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **42.2%**. Expected goals are 1.51 for Augsburg and 1.46 for SC Freiburg (2.97 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.3%; Under 3.5 goals: 65.4%; Double Chance 1X: 57.8%; Double Chance X2: 67.4%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 32.6% | 3.07 |
| Draw | 25.2% | 3.96 |
| SC Freiburg win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.51 |
| SC Freiburg expected goals | 1.46 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.3% |
| Under 2.5 | 42.7% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.74% |
| 2 | 1-2 | 9.73% |
| 3 | 0-1 | 7.84% |
| 4 | 2-1 | 7.30% |
| 5 | 0-2 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 32.6% | 30.2% | 3.19 | +4.0% |
| Draw | 25.2% | 24.9% | 3.85 | -2.8% |
| SC Freiburg win | 42.2% | 44.9% | 2.17 | -8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 24400b6372faf9f4996cd5704d707374 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 1.4609 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.5703 |
| Shot lambda away | 1.4329 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.34 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.21887119351422052, "-10": 8.690420509186883e-07, "-11": 1.1311012675941408e-07, "-12": 1.352813961643071e-08, "-13": 1.4957964288499091e-09, "-14": 1.5255142566901967e-10, "-15": 1.2903975522653544e-11, "-2": 0.12656832586262748, "-3": 0.052631964896211136, "-4": 0.017360235037923714, "-5": 0.004722502151167557, "-6": 0.0010903115286080348, "-7": 0.00021832855169961226, "-8": 3.85633016101524e-05, "-9": 6.0893581426816266e-06, "0": 0.2523390788340894, "1": 0.1644626427958818, "10": 9.349975875861008e-07, "11": 1.2667114879051564e-07, "12": 1.5769605106128624e-08, "13": 1.8149378367349215e-09, "14": 1.9266909372622015e-10, "15": 1.6963905155950165e-11, "2": 0.09881948007737504, "3": 0.042773386288949146, "4": 0.014685413250006838, "5": 0.004158237178398848, "6": 0.0009992961589832465, "7": 0.0002082862826238304, "8": 3.829401168642647e-05, "9": 6.294115313143757e-06} |
| Raw goal margin distribution | {"-1": 0.18505497002949325, "-10": 7.347725760753364e-07, "-11": 9.563428965418232e-08, "-12": 1.143800347171192e-08, "-13": 1.2646916154960267e-09, "-14": 1.2898179541979205e-10, "-15": 1.0910274510157577e-11, "-2": 0.10701315862139658, "-3": 0.04450017624557284, "-4": 0.014678029223791859, "-5": 0.003992862103124362, "-6": 0.0009218552885364585, "-7": 0.00018459616792252455, "-8": 3.260516155243335e-05, "-9": 5.148534946512203e-06, "0": 0.2609423753979639, "1": 0.1929633923951109, "10": 1.0970291083415366e-06, "11": 1.4862277641701502e-07, "12": 1.850241760851747e-08, "13": 2.129459651194319e-09, "14": 2.2605791384032146e-10, "15": 1.9903685308181267e-11, "2": 0.11594451959596531, "3": 0.0501858512196353, "4": 0.01723033943314687, "5": 0.0048788438437242935, "6": 0.0011724703772645428, "7": 0.00024438150209189974, "8": 4.493021805931909e-05, "9": 7.384861524191968e-06} |
| Unadjusted home-win probability | 38.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 35.6% |
| Raw p over 1 5 | 80.5% |
| Raw p under 3 5 | 65.4% |
| Raw p btts yes | 60.6% |
| P home draw | 57.8% |
| P draw away | 67.4% |
| P home away | 74.8% |
| Raw p home draw | 64.4% |
| Raw p draw away | 61.7% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5729 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.19 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.17 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | +2.4% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | 0.0807 |
| Raw ev home | 0.2207 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0046 |
| Raw edge prob away | -0.0930 |
| Raw ev away | -0.2266 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.0700078736542545, 0.08126500856866445, 0.06864441060039538, 0.032804064638436256, 0.011757402904955219, 0.0033712047477794313, 0.0008055223833105691, 0.00016497696357237784, 2.9564943432098933e-05, 4.7095376831389955e-06, 6.751837938016463e-07, 8.799805186137922e-08, 1.0513214972890023e-08, 1.1594070207230034e-09, 1.1872758211712616e-10], [0.06552350745569097, 0.12512521428585974, 0.09375874178411622, 0.04480580136100532, 0.016058981253910937, 0.004604597995435594, 0.0011002318248138116, 0.0002253356448488616, 4.038161115912039e-05, 6.4325751170984755e-06, 9.222073935252627e-07, 1.20193130799914e-07, 1.4359593145933761e-08, 1.5835891448098977e-09, 1.6216540599604144e-10], [0.05320149501255978, 0.07627242768882059, 0.05514250395768066, 0.030599254356571796, 0.010967170258525947, 0.0031446210310327773, 0.0007513820183109784, 0.00015388861493130848, 2.7577839334472693e-05, 4.393002606737318e-06, 6.298036804794124e-07, 8.208357108997262e-08, 9.806606059538478e-09, 1.081481539587329e-09, 1.107477236246505e-10], [0.024221953833207462, 0.03472585162858897, 0.0248923926540878, 0.01199759775178772, 0.004993211029506367, 0.0014317053575022144, 0.00034209453238737234, 7.006349963365525e-05, 1.2555834211454242e-05, 2.0000773719691678e-06, 2.867414847826186e-07, 3.7371590195665366e-08, 4.4648211329120804e-09, 4.923845827484014e-10, 5.0422008782569245e-11], [0.008270957151103434, 0.011857673944612656, 0.008499888755800633, 0.0040619607295920976, 0.0014683332653400365, 0.0004888777241690409, 0.00011681341804572534, 2.392425513303761e-05, 4.287381912887785e-06, 6.82957054429246e-07, 9.791227208225449e-08, 1.2761101903892729e-08, 1.5245815648046288e-09, 1.681322577781783e-10, 1.7217367227471397e-11], [0.002259396006332176, 0.0032391875166796983, 0.0023219337687611654, 0.0011096149674882701, 0.00039770041871098685, 0.00011500982767829858, 3.1910184685615486e-05, 6.535442695993872e-06, 1.1711937801911025e-06, 1.8656491783033384e-07, 2.674691604272689e-08, 3.485978968492976e-09, 4.1647338221159633e-10, 4.592906779948052e-11, 4.703307010617696e-12], [0.0005143369161279332, 0.0007373801287688895, 0.0005285732340549903, 0.0002525966846306832, 9.053393310837057e-05, 2.5958830159801075e-05, 6.255798843690572e-06, 1.4877513425568656e-06, 2.6661470384273366e-07, 4.247029924173797e-08, 6.08876278208591e-09, 7.935606097012412e-10, 9.480747706720951e-11, 1.0455455806069319e-11, 1.0706774804701242e-12], [0.00010035898186339071, 0.00014387985122019646, 0.00010313681547369997, 4.928743260827473e-05, 1.766525611119933e-05, 5.065165815463872e-06, 1.2102808179251623e-06, 2.499982789685093e-07, 5.202267111002151e-08, 8.286933832052961e-09, 1.1880578944597013e-09, 1.5484195736146365e-10, 1.849912299341014e-11, 2.040100305290545e-12, 2.0891384319245524e-13], [1.7134555792573635e-05, 2.4564989524459852e-05, 1.7608822710138816e-05, 8.414974407061643e-06, 3.01603614153306e-06, 8.647892261585582e-07, 2.0663446175299514e-07, 4.232027163456042e-08, 7.64904768607791e-09, 1.4148502451724668e-09, 2.028402829468435e-10, 2.6436579050321462e-11, 3.1584044512900214e-12, 3.48311749027406e-13, 3.5668415876266475e-14], [2.6003806801685773e-06, 3.728040863226503e-06, 2.672356548385372e-06, 1.2770764026296006e-06, 4.5772077245982363e-07, 1.3124245666732156e-07, 3.1359334242700784e-08, 6.422624436268953e-09, 1.150976015270173e-09, 1.849152261772006e-10, 3.078352070051966e-11, 4.0120777126886734e-12, 4.793269235991904e-13, 5.286061417706288e-14, 5.4131230864509086e-15], [3.5517592561414655e-07, 5.091986624965988e-07, 3.6500683068537046e-07, 1.7443091961233458e-07, 6.251830751976703e-08, 1.7925898843268046e-08, 4.283250006907679e-09, 8.772413963927694e-10, 1.572073561001708e-10, 2.5042292718090385e-11, 3.6209539073556936e-12, 5.479941556663574e-13, 6.546940802147752e-14, 7.220026556901453e-15, 7.393575169035899e-16], [4.4101912776194733e-08, 6.322679376522917e-08, 4.53226084559835e-08, 2.165894884038901e-08, 7.762848623212729e-09, 2.2258446313716296e-09, 5.318477536917668e-10, 1.0892636791326558e-10, 1.9520312629628773e-11, 3.1094816104427153e-12, 4.457914410604796e-13, 5.859869572520075e-14, 8.129284430186907e-15, 8.965049669503696e-16, 9.180543603715271e-17], [5.019757879778294e-09, 7.196585731479719e-09, 5.1586996256505625e-09, 2.465259946002702e-09, 8.835811894066433e-10, 2.5334958109846437e-10, 6.053585398857584e-11, 1.2398192260345379e-11, 2.2218365819091236e-12, 3.539267082417985e-13, 5.074077195601732e-14, 6.61314611378805e-15, 7.968485397284393e-16, 1.0204178433137323e-16, 1.044945744853796e-17], [5.27407143738659e-10, 7.561182862225505e-10, 5.420052321508022e-10, 2.5901562143711023e-10, 9.283456344447171e-11, 2.661849079868934e-11, 6.360275258396606e-12, 1.3026315858565484e-12, 2.3344004105044825e-13, 3.718575253172908e-14, 5.331142706348955e-15, 6.948184726298818e-16, 8.301065552451153e-17, 9.23292696072029e-18, 1.0978853240617791e-18], [5.145464219403316e-11, 7.376804871878169e-11, 5.2878853877324075e-11, 2.5269957530790915e-11, 9.057081046368133e-12, 2.596940401835761e-12, 6.20518116907658e-13, 1.2708671650854177e-13, 2.277476505316964e-14, 3.6278985105747845e-15, 5.201143816444821e-16, 6.778754577638194e-17, 8.098645664955935e-18, 8.931260957290854e-19, 9.22430495167698e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3658612691704897, "lambda_away": 1.4336519616754044, "rho": -0.11083277065839049, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3235 |
| Legacy p draw | 0.2639 |
| Legacy p away | 0.4126 |
| Legacy p over 1 5 | 0.7832 |
| Legacy p under 3 5 | 0.6908 |
| Legacy p btts yes | 0.5770 |
| Legacy p over 2 5 | 0.5362 |
| Legacy goal margin distribution | {"-1": 0.21113854486791717, "-10": 8.056931326110747e-07, "-11": 1.0348954855568286e-07, "-12": 1.2207551841324572e-08, "-13": 1.3215724267190449e-09, "-14": 1.1872758211712616e-10, "-2": 0.12597271154672696, "-3": 0.05237490058996093, "-4": 0.017187926611982905, "-5": 0.004638591538119935, "-6": 0.0010605374400001692, "-7": 0.0002100515070626739, "-8": 3.666626540118258e-05, "-9": 5.718466304451931e-06, "0": 0.2638630463773669, "1": 0.1711752015546226, "10": 4.238294917075098e-07, "11": 5.1865773697356045e-08, "12": 5.8287550198781685e-09, "13": 6.011751924574407e-10, "14": 5.145464219403316e-11, "2": 0.09763266268081597, "3": 0.038672720533004606, "4": 0.012091157007480516, "5": 0.003108804116136144, "6": 0.0006771674724743095, "7": 0.00012777878154141456, "8": 2.125017325552422e-05, "9": 3.1574626425710087e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3451 |
| Legacy raw p draw | 0.2791 |
| Legacy raw p away | 0.3758 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3659 |
| Legacy lambda away | 1.4337 |
| Legacy model home team | Augsburg |
| Legacy model away team | Freiburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 9.859744839060301, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,473.6758 |
| Elo away rating | 1,485.3747 |
| Elo rating diff | 48.3011 |
| Elo home expectancy | 0.5691 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **53.4%**. Expected goals are 2.13 for Bayer Leverkusen and 1.42 for VfB Stuttgart (3.54 combined). The most likely exact score is 2-1 at 9.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.9%; Under 3.5 goals: 52.7%; Double Chance 1X: 74.8%; Double Chance X2: 46.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 71.6%; BTTS Yes (both teams score): 67.2%; BTTS No (at least one team does not score): 32.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 53.4% | 1.87 |
| Draw | 21.5% | 4.66 |
| VfB Stuttgart win | 25.2% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.13 |
| VfB Stuttgart expected goals | 1.42 |
| Expected total goals | 3.54 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.5% |
| Under 1.5 | 12.5% |
| Over 2.5 | 68.9% |
| Under 2.5 | 31.1% |
| Over 3.5 | 47.3% |
| Under 3.5 | 52.7% |
| Over 4.5 | 28.4% |
| Under 4.5 | 71.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.30% |
| 2 | 1-1 | 9.08% |
| 3 | 3-1 | 6.59% |
| 4 | 2-0 | 6.57% |
| 5 | 2-2 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 53.4% | 53.5% | 1.83 | -2.3% |
| Draw | 21.5% | 21.2% | 4.47 | -4.0% |
| VfB Stuttgart win | 25.2% | 25.3% | 3.76 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | a7ba9b844f121a4a8777d87b1f863137 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1730 |
| Dc lambda away | 1.3808 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9415 |
| Shot lambda away | 1.5542 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 67.2% |
| P btts no | 32.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.12 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.01 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.90 |
| Fair Over 4.5 odds | 3.52 |
| Fair Under 4.5 odds | 1.40 |
| Goal margin distribution | {"-1": 0.13878954992043366, "-10": 3.4396119923246335e-07, "-11": 4.329192150932753e-08, "-12": 5.011404631593673e-09, "-13": 5.368984362792381e-10, "-14": 5.35234600770641e-11, "-15": 4.985046569081686e-12, "-16": 4.3086479081668945e-13, "-17": 3.0478290796036667e-14, "-2": 0.07289299779013053, "-3": 0.028178886465149437, "-4": 0.008765591069061296, "-5": 0.0022684028191367455, "-6": 0.000501000690056421, "-7": 9.633103178315821e-05, "-8": 1.6381010571279683e-05, "-9": 2.4950478068967498e-06, "0": 0.2146682592153174, "1": 0.20863932494180157, "10": 1.985897735716504e-05, "11": 3.755384119712537e-06, "12": 6.531411551614744e-07, "13": 1.0513317881185475e-07, "14": 1.5746785616220234e-08, "15": 2.2035201711799347e-09, "16": 2.8614680010152784e-10, "17": 3.0411551209413385e-11, "2": 0.16208119212034153, "3": 0.09413924590640403, "4": 0.04399751731856159, "5": 0.017106738632553062, "6": 0.005676562744814278, "7": 0.0016398850529313494, "8": 0.0004189748584941113, "9": 9.587960158287104e-05} |
| Raw goal margin distribution | {"-1": 0.1362386518240782, "-10": 3.376393258000237e-07, "-11": 4.2496232783274124e-08, "-12": 4.919296958198032e-09, "-13": 5.27030451262887e-10, "-14": 5.2539719640559955e-11, "-15": 4.893423346651728e-12, "-16": 4.229456630775262e-13, "-17": 2.991811163257407e-14, "-2": 0.07155325276316643, "-3": 0.02766096946143716, "-4": 0.00860448290505098, "-5": 0.0022267104551480974, "-6": 0.0004917924916922764, "-7": 9.456050478212328e-05, "-8": 1.6079933950549866e-05, "-9": 2.449189795940034e-06, "0": 0.2211353019367762, "1": 0.20791847526095195, "10": 1.9790364512995297e-05, "11": 3.7424092529422497e-06, "12": 6.508845499247616e-07, "13": 1.0476994326930123e-07, "14": 1.56923804105428e-08, "15": 2.1959070004002466e-09, "16": 2.8515816179191454e-10, "17": 3.030647918145527e-11, "2": 0.1615212009698513, "3": 0.09381399444488796, "4": 0.0438455057247448, "5": 0.017047634783903753, "6": 0.0056569501984064345, "7": 0.0016342192436819886, "8": 0.0004175272987250517, "9": 9.554833718570967e-05} |
| Unadjusted home-win probability | 53.2% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 52.8% |
| Raw p btts yes | 67.3% |
| P home draw | 74.8% |
| P draw away | 46.6% |
| P home away | 78.5% |
| Raw p home draw | 75.3% |
| Raw p draw away | 46.8% |
| Raw p home away | 77.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6890 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.47 |
| Reference away odds | 3.76 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.57 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | -0.0026 |
| Raw ev home | -0.0265 |
| Raw edge prob draw | 0.0092 |
| Raw ev draw | -0.0115 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0717 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.038632441403415, 0.03200883705050853, 0.02647710415240949, 0.010892463476552757, 0.0033608025986833225, 0.0008295639737791416, 0.00017063790726205532, 3.0085300900004614e-05, 4.641317258697142e-06, 6.364666169991245e-07, 7.855114373310894e-08, 8.813262609795513e-09, 9.064259872782341e-10, 8.605297302378865e-11, 7.586032987338278e-12, 6.241663496949084e-13, 4.8145671880857516e-14, 3.4953060898396355e-15, 2.396567093326824e-16], [0.05496154328484105, 0.09240657919511028, 0.060675597886569725, 0.02496144329429312, 0.007701699773511323, 0.0019010496693471484, 0.0003910381205452199, 6.894423231473425e-05, 1.0636159378746721e-05, 1.4585429093366285e-06, 1.8000977687155896e-07, 2.0196694287355776e-08, 2.0771885928856817e-09, 1.972011575767465e-10, 1.7384344014528616e-11, 1.4303553073786547e-12, 1.1033183274900531e-13, 8.009931357175563e-15, 5.492033434844142e-16], [0.07295491757711284, 0.09003916409090784, 0.05881859991901407, 0.028601135669421643, 0.008824704465615287, 0.002178246620848961, 0.00044805639665020867, 7.899716850542312e-05, 1.2187045188315545e-05, 1.671216809772666e-06, 2.0625746634221517e-07, 2.314162633049997e-08, 2.3800688147580466e-09, 2.2595556657210696e-10, 1.991920001665559e-11, 1.6389191009306462e-12, 1.264196016194184e-13, 9.177880090840339e-15, 6.292840983553605e-16], [0.05572844141459109, 0.06877867109856153, 0.04244247172544773, 0.018483858583084174, 0.006740971577321108, 0.0016639082494775432, 0.00034225910302429393, 6.034396615306647e-05, 9.309379769720722e-06, 1.2766008264768923e-06, 1.575549327051822e-07, 1.767731100284608e-08, 1.8180751882248663e-09, 1.7260182003090581e-10, 1.5215779936703794e-11, 1.251929412474875e-12, 9.656877968585198e-14, 7.0107536261955e-15, 4.806944229806409e-16], [0.03192717453779094, 0.039403733190825393, 0.02431555895332892, 0.01000322151117867, 0.0032673308882190492, 0.00095326349970431, 0.0001960823924378288, 3.457143768544489e-05, 5.333402212620168e-06, 7.313726414631862e-07, 9.026421173966666e-08, 1.0127442638273902e-08, 1.0415867083999328e-09, 9.8884668111753e-11, 8.717216011007369e-12, 7.172382332338852e-13, 5.53248611601118e-14, 4.016504839957524e-15, 2.7539285779895053e-16], [0.014633023254796084, 0.018059717230055384, 0.011144429307274557, 0.00458472680765073, 0.001414589252704302, 0.00036963541429835836, 8.986946856204109e-05, 1.5844955243504346e-05, 2.444431733602811e-06, 3.35206388457102e-07, 4.13703476296957e-08, 4.641660459558134e-09, 4.773852602541414e-10, 4.532131856232187e-11, 3.9953182971191135e-12, 3.287282353694454e-13, 2.5356768697650482e-14, 1.8408647046587688e-15, 1.2621944004493237e-16], [0.005588900695496643, 0.006897683713749813, 0.00425647575499653, 0.0017510792129400157, 0.0005402847190644557, 0.00013336122112463575, 2.9039660645602732e-05, 6.051783000584636e-06, 9.336202080830489e-07, 1.2802789860726713e-07, 1.5800888211174116e-08, 1.772824311078786e-09, 1.8233134510872457e-10, 1.7309912273307283e-11, 1.5259619847990627e-12, 1.2555364884583994e-13, 9.684701496213206e-15, 7.030953104520293e-16, 4.8207940626425915e-17], [0.0018296664883198394, 0.002258129357754868, 0.001393463844068352, 0.0005732595959150642, 0.00017687572180698582, 4.365913270381966e-05, 8.98050454568024e-06, 1.6761617308471202e-06, 3.0564393619020174e-07, 4.1913136127195235e-08, 5.172816126249718e-09, 5.803783978973205e-10, 5.969072812199392e-11, 5.666832911836561e-12, 4.995618383927593e-13, 4.110312855703668e-14, 3.1705293656908844e-15, 2.3017584274944727e-16, 1.578207562466736e-17], [0.0005241137185584358, 0.0006468482547142704, 0.00039916209957042645, 0.00016421201373713362, 5.066660665796791e-05, 1.2506295839438867e-05, 2.5724937643087124e-06, 4.535583576031308e-07, 7.407239906416888e-08, 1.2006149630167009e-08, 1.481769444133719e-09, 1.6625121694844002e-10, 1.7098596754760053e-11, 1.6232821056909462e-12, 1.4310105936866677e-13, 1.1774120414806494e-14, 9.08208105826381e-16, 6.593459389230835e-17, 4.520825185911652e-18], [0.00013345246456893334, 0.00016470374794073998, 0.00010163665644299321, 4.1812486811685464e-05, 1.2900985588486682e-05, 3.1844157924197324e-06, 6.55021268818274e-07, 1.154873045766819e-07, 1.7816448692792863e-08, 2.5863771571445813e-09, 3.7729557010352444e-10, 4.233171896430727e-11, 4.35373049167512e-12, 4.133282339774347e-13, 3.643710969386617e-14, 2.997985612376465e-15, 2.3125250450871336e-16, 1.6788597099656404e-17, 1.151115190429708e-18], [3.058230246988475e-05, 3.7743925177534295e-05, 2.329131184955997e-05, 9.581854653815872e-06, 2.9564223088808353e-06, 7.297487331405105e-07, 1.5010632161731873e-07, 2.6465361216101377e-08, 4.082862198327771e-09, 5.598853399159219e-10, 7.314966135355582e-11, 9.700843199998675e-12, 9.977118309418181e-13, 9.471933779321012e-14, 8.350019712154436e-15, 6.870259241312152e-16, 5.299440563085874e-17, 3.847317141764089e-18, 2.637924525793693e-19], [6.371197601268952e-06, 7.863175305076615e-06, 4.852268737203515e-06, 1.996183558978759e-06, 6.15910157229917e-07, 1.5202823210228353e-07, 3.127158385688319e-08, 5.513517043485604e-09, 8.505808831729733e-10, 1.166406662209504e-10, 1.4395504010322764e-11, 1.7098082707872792e-12, 2.078528662226694e-13, 1.9732837916181864e-14, 1.7395559282370573e-15, 1.4312780812186117e-16, 1.1040301179693143e-17, 8.015098853026505e-19, 5.495576543857476e-20], [1.2166997237979477e-06, 1.501620860096393e-06, 9.266317577676574e-07, 3.812087046830449e-07, 1.1761960075398334e-07, 2.9032643403101737e-08, 5.971895681561673e-09, 1.0529095287561193e-09, 1.6243437896483534e-10, 2.227472372641109e-11, 2.7490915914777917e-12, 3.0844192691063615e-13, 3.358190938424923e-14, 3.76835564440605e-15, 3.3220084352674344e-16, 2.733294044670501e-17, 2.108352657795985e-18, 1.5306335120964218e-19, 1.0494834537371947e-20], [2.144784378606269e-07, 2.647040103922054e-07, 1.6334558806151122e-07, 6.719903512764359e-08, 2.0733848901320444e-08, 5.1178412243117826e-09, 1.0527189509419794e-09, 1.856056893242818e-10, 2.8633746826611825e-11, 3.926562861134556e-12, 4.846067263296736e-13, 5.4371790640351004e-14, 5.5920271746457265e-15, 5.620036611378674e-16, 5.855998532915805e-17, 4.818219528190154e-18, 3.7165799881325377e-19, 2.698183275548133e-20, 1.8500174473246536e-21], [3.5107441659947506e-08, 4.332874061698151e-08, 2.673763274518919e-08, 1.0999642802702453e-08, 3.3938721204333305e-09, 8.37726691781282e-10, 1.7231694487878091e-10, 3.038133331585017e-11, 4.68698674910259e-12, 6.42729301585911e-13, 7.932406885438434e-14, 8.899983079387314e-15, 9.15345009750073e-16, 8.689971441353226e-17, 8.109676632342964e-18, 7.886823620968217e-19, 6.083577277482791e-20, 4.416589046387382e-21, 3.028247512882433e-22], [5.363539760550251e-09, 6.619548793237143e-09, 4.0848421175451435e-09, 1.6804705422740058e-09, 5.184988480927772e-10, 1.279837039498437e-10, 2.632572302550596e-11, 4.641508509690023e-12, 7.160544487826828e-13, 9.819297565791018e-14, 1.2118735434786802e-14, 1.3596950064572062e-15, 1.3984184327554654e-16, 1.327610476297346e-17, 1.1703601297706962e-18, 1.0193926154866701e-19, 9.29418581114799e-21, 6.747444369703144e-22, 4.6264054491507546e-23], [7.682014144335704e-10, 9.480952827606366e-10, 5.850579342240341e-10, 2.4068803535007287e-10, 7.42628126702253e-11, 1.8330667206358282e-11, 3.770543068017705e-12, 6.647873533957971e-13, 1.0255802416385457e-13, 1.4063843311587404e-14, 1.7357249349810664e-15, 1.947444549290579e-16, 2.0029067853922557e-17, 1.901490976555784e-18, 1.6762666955493382e-19, 1.3792047387909957e-20, 1.1262167490728036e-21, 9.664133277695727e-23, 6.626241938059535e-24], [1.0355468734255952e-10, 1.2780464697481146e-10, 7.886667522022987e-11, 3.244510330165114e-11, 1.0010737031660671e-11, 2.471001062572358e-12, 5.082747846905885e-13, 8.961431889701688e-14, 1.382497340829488e-14, 1.895826888108548e-15, 2.3397828951822625e-16, 2.625184068001956e-17, 2.6999479829195454e-18, 2.5632379719988127e-19, 2.259632308648499e-20, 1.8591883954312684e-21, 1.4341028556711695e-22, 1.1021598925979556e-23, 8.932272178356522e-25], [1.318380701953433e-11, 1.6271130212983946e-11, 1.0040714264688555e-11, 4.1306674920742635e-12, 1.2744920441131827e-12, 3.1458934394975937e-13, 6.47097378807117e-14, 1.1409023742373045e-14, 1.7600920454929986e-15, 2.413624769353644e-16, 2.9788362988965816e-17, 3.342187691495224e-18, 3.4373715070802956e-19, 3.2633225627138116e-20, 2.8767945765486513e-21, 2.366979385224774e-22, 1.8257923209972662e-23, 1.32549879751528e-24, 9.620996503929968e-26]] |
| Legacy trial inputs | {"lambda_home": 2.2916251542202013, "lambda_away": 1.2341753932589543, "rho": -0.11083277065839049, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5682 |
| Legacy p draw | 0.2120 |
| Legacy p away | 0.2198 |
| Legacy p over 1 5 | 0.8744 |
| Legacy p under 3 5 | 0.5348 |
| Legacy p btts yes | 0.6493 |
| Legacy p over 2 5 | 0.6826 |
| Legacy goal margin distribution | {"-1": 0.12907604497238187, "-10": 1.0130956451889821e-07, "-11": 1.1132365863069323e-08, "-12": 1.1248554882179165e-09, "-13": 1.0517694764321375e-10, "-14": 9.150094042820343e-12, "-15": 7.441567569577346e-13, "-16": 5.678488733638844e-14, "-17": 4.04450943332405e-15, "-18": 2.396567093326824e-16, "-2": 0.062140064567939926, "-3": 0.02115181821477255, "-4": 0.005775937638221853, "-5": 0.001309683219764055, "-6": 0.00025314087960811216, "-7": 4.25608546706111e-05, "-8": 6.324883421396167e-06, "-9": 8.41539104167081e-07, "0": 0.21200923795918725, "1": 0.19900380354015115, "10": 3.944283428559853e-05, "11": 8.047701041428666e-06, "12": 1.5098986360010868e-06, "13": 2.621430339568793e-07, "14": 4.234576798275445e-08, "15": 6.394632386023191e-09, "16": 9.060467756730703e-10, "17": 1.1982581755554347e-10, "18": 1.318380701953433e-11, "2": 0.17122051047179843, "3": 0.10821774750325676, "4": 0.05487063392748861, "5": 0.023102045914455187, "6": 0.008291119252462918, "7": 0.002588379280762192, "8": 0.00071422787641263, "9": 0.000176451465768524} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6019 |
| Legacy raw p draw | 0.2121 |
| Legacy raw p away | 0.1860 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2916 |
| Legacy lambda away | 1.2342 |
| Legacy model home team | Leverkusen |
| Legacy model away team | Stuttgart |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.79641364538342, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,573.7454 |
| Elo away rating | 1,532.5206 |
| Elo rating diff | 101.2247 |
| Elo home expectancy | 0.6417 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **48.2%**. Expected goals are 1.45 for Borussia Monchengladbach and 0.99 for SC Paderborn (2.44 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.8%; Double Chance 1X: 73.3%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 48.2% | 2.07 |
| Draw | 25.0% | 3.99 |
| SC Paderborn win | 26.7% | 3.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.45 |
| SC Paderborn expected goals | 0.99 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.2% |
| Under 3.5 | 76.8% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.07% |
| 2 | 1-1 | 11.87% |
| 3 | 2-0 | 9.44% |
| 4 | 2-1 | 9.36% |
| 5 | 0-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 48.2% | 48.9% | 2.00 | -3.5% |
| Draw | 25.0% | 23.6% | 4.04 | +1.2% |
| SC Paderborn win | 26.7% | 27.5% | 3.49 | -6.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | aecb9d8c01176616c87d893bee4bc0de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3261 |
| Dc lambda away | 0.8763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9455 |
| Shot lambda away | 1.4505 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.75 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.32 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.59 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16729814147526353, "-10": 2.684012015109319e-08, "-11": 2.3926561205829208e-09, "-12": 1.958369793804756e-10, "-13": 1.481324059879356e-11, "-14": 1.0376112379321261e-12, "-15": 6.256873259092271e-14, "-2": 0.07225326362874847, "-3": 0.02146617676986326, "-4": 0.004977355197071534, "-5": 0.000942969302206041, "-6": 0.00015074268579851315, "-7": 2.082053416754764e-05, "-8": 2.5298776429177065e-06, "-9": 2.742918908372358e-07, "0": 0.25049216206674835, "1": 0.2395398596023842, "10": 1.1572588501689957e-06, "11": 1.5091341738403743e-07, "12": 1.806940216842146e-08, "13": 1.9994045331577385e-09, "14": 2.0487396658802314e-10, "15": 1.807219818676711e-11, "2": 0.1485564167930937, "3": 0.06456396030703043, "4": 0.021899571044651643, "5": 0.006069264188685673, "6": 0.0014193066901789769, "7": 0.00028676977926632576, "8": 5.0973275886178324e-05, "9": 8.084580874897105e-06} |
| Raw goal margin distribution | {"-1": 0.1558499794331034, "-10": 2.5003458715340205e-08, "-11": 2.2289273741781097e-09, "-12": 1.8243591315209577e-10, "-13": 1.3799574952247395e-11, "-14": 9.6660780965812e-13, "-15": 5.828717283683911e-14, "-2": 0.06730899429734567, "-3": 0.01999725268068929, "-4": 0.004636756261931012, "-5": 0.0008784421934333852, "-6": 0.00014042740866229353, "-7": 1.9395791209541376e-05, "-8": 2.3567588685693225e-06, "-9": 2.555221783618616e-07, "0": 0.2834439032418272, "1": 0.2322536263439327, "10": 1.1220577861926907e-06, "11": 1.4632298987558277e-07, "12": 1.7519773896707397e-08, "13": 1.9385873988788154e-09, "14": 1.986421874109693e-10, "15": 1.7522484866819758e-11, "2": 0.1440376836411626, "3": 0.06260007807186797, "4": 0.02123343813818577, "5": 0.005884651595778024, "6": 0.001376134753670829, "7": 0.0002780469240944248, "8": 4.942278997259971e-05, "9": 7.83866713783015e-06} |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 24.9% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.1% |
| P home draw | 73.3% |
| P draw away | 51.8% |
| P home away | 75.0% |
| Raw p home draw | 75.1% |
| Raw p draw away | 53.2% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4525 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.52, "price": 2.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.79, "price": 1.52, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.00 |
| Reference draw odds | 4.04 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.69 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | -0.6% |
| Draw probability edge | +1.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -20.3% |
| Under 2.5 probability edge | +20.3% |
| Raw edge prob home | -0.0210 |
| Raw ev home | -0.0646 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1451 |
| Raw edge prob away | -0.0261 |
| Raw ev away | -0.1316 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.10682482571289528, 0.08660520312047901, 0.04332092943480874, 0.012203428026770843, 0.0025782628203190393, 0.0004357752038890648, 6.137854618879168e-05, 7.410096959483896e-06, 7.827791274584967e-07, 7.350249150104535e-08, 6.211655958382639e-09, 4.772215441872184e-10, 3.360811300272878e-11, 2.1847719415316324e-12, 1.31881356975392e-13], [0.13471840426273346, 0.12418862776408798, 0.06068723268939374, 0.017095484467464797, 0.0036118254560205953, 0.0006104668469424411, 8.59837072586656e-05, 1.0380623968557604e-05, 1.0965761739706346e-06, 1.0296784633133804e-07, 8.701757221070358e-09, 6.685280134643398e-10, 4.708078521531485e-11, 3.0605936880581636e-12, 1.8474937409186157e-13], [0.10411357450687662, 0.08798582091941136, 0.033088574333645024, 0.011974323466168882, 0.0025298590628445197, 0.00042759405295432604, 6.022623842542209e-05, 7.270981376207111e-06, 7.680833987131518e-07, 7.212257136864037e-08, 6.095039651404478e-09, 4.68262288480465e-10, 3.2977161441801794e-11, 2.1437554980714793e-12, 1.2940544444694874e-13], [0.048616721791341924, 0.04108572967052749, 0.01736066440066186, 0.004352516716141569, 0.0011813392711965088, 0.0001996686907598178, 2.8123155812639787e-05, 3.3952467811365153e-06, 3.586630954191211e-07, 3.3678249966086785e-08, 2.8461307609792744e-09, 2.186590702726111e-10, 1.5398966857855346e-11, 1.0010449178413037e-12, 6.042697622053815e-14], [0.01702649473614481, 0.014388998973815752, 0.006080032757093201, 0.0017127343092500195, 0.0003220515300829596, 6.992774886768287e-05, 9.849260640460691e-06, 1.1890795865472905e-06, 1.2561059407528e-07, 1.1794759593853688e-08, 9.967687790258116e-10, 7.657853865560212e-11, 5.393009205199753e-12, 3.505848480985992e-13, 2.1162669028897143e-14], [0.004770400180319769, 0.004031439492568955, 0.0017034738981956024, 0.0004798655380512055, 0.00010138294525076946, 1.5250716922521123e-05, 2.7595177670673363e-06, 3.3315051406547506e-07, 3.5192963079755095e-08, 3.304598166873647e-09, 2.792698107795312e-10, 2.1455401142303662e-11, 1.5109869931323405e-12, 9.82251513599336e-14, 5.9292533029236345e-15], [0.0011137895298401043, 0.0009412575312929451, 0.00039772583440557174, 0.00011203865332251737, 2.3670815582832378e-05, 4.0008157452128235e-06, 5.015250858883403e-07, 7.778373729687846e-08, 8.216827167663973e-09, 7.715551524958125e-10, 6.520371027359363e-11, 5.009391297904778e-12, 3.5278413320925483e-13, 2.2933536184865755e-14, 1.3843577056303747e-15], [0.00022289722393268037, 0.000188369243119968, 7.959491627474516e-05, 2.2421744979350125e-05, 4.737123972060695e-06, 8.006635896479641e-07, 1.1277274769264245e-07, 1.2117177861630904e-08, 1.6443932324178513e-09, 1.5440754019923458e-10, 1.3048898037478655e-11, 1.0025048574983442e-12, 7.06009545188745e-14, 4.589575870137784e-15, 2.770447030141534e-16], [3.9031410080255e-05, 3.298523438292475e-05, 1.3937821936990248e-05, 3.926259410338047e-06, 8.295151688849659e-07, 1.4020376006709335e-07, 1.974757371764333e-08, 2.384081165953299e-09, 2.241436348856213e-10, 2.703821929527478e-11, 2.2849853462064133e-12, 1.7554807327830743e-13, 1.2362894249036894e-14, 8.036781020471314e-16, 4.851314531029676e-17], [6.0753499691185935e-06, 5.134245528860539e-06, 2.1694616182291144e-06, 6.111334419715386e-07, 1.2911639485497566e-07, 2.182311393932508e-08, 3.0737660035588377e-09, 3.710890128788287e-10, 3.9200665699650456e-11, 3.2760181062943878e-12, 3.55664466745314e-13, 2.732455679611014e-14, 1.9243196451182894e-15, 1.2509478193111262e-16, 7.551209020036299e-18], [8.510809487599549e-07, 7.192439247253982e-07, 3.0391458298304645e-07, 8.561219226149913e-08, 1.8087600614319864e-08, 3.0571467669823763e-09, 4.305963771424481e-10, 5.198495407847732e-11, 5.4915255788170835e-12, 5.15650964653726e-13, 3.8783874710422525e-14, 3.827830469139635e-15, 2.695732423003604e-16, 1.752422267556991e-17, 1.0578304409992041e-18], [1.0838713894134178e-07, 9.159738719978704e-08, 3.870422922764091e-08, 1.0902911869006203e-08, 2.303498020671509e-09, 3.893347535035126e-10, 5.483745045048634e-11, 6.6204048495889776e-12, 6.993585589930261e-13, 6.566935005723401e-14, 5.549681394954231e-15, 3.7946412779639827e-16, 3.433077959346743e-17, 2.2317505294220006e-18, 1.3471716779939317e-19], [1.2653074790268376e-08, 1.069304533870307e-08, 4.5183175042757435e-09, 1.2728019270339864e-09, 2.6890951287648185e-10, 4.5450796124406506e-11, 6.401703824225422e-12, 7.728636305183735e-13, 8.164286130794636e-14, 7.666215805845594e-15, 6.4786776769261895e-16, 4.9773596380553496e-17, 3.1197021794365127e-18, 2.6053373710030354e-19, 1.5726832688344732e-20], [1.3634910495148138e-09, 1.1522789403403574e-09, 4.868923623753762e-10, 1.3715670412782236e-10, 2.8977597936785345e-11, 4.897762380778311e-12, 6.898454336719352e-13, 8.328352279382797e-14, 8.797807054438743e-15, 8.261088160925786e-16, 6.981401099418398e-17, 5.363585870783284e-18, 3.77728126990022e-19, 2.1854019864030213e-20, 1.694718158488038e-21], [1.364343808464146e-10, 1.1529996023343265e-10, 4.871968761596983e-11, 1.3724248511402503e-11, 2.8995721199112252e-12, 4.900825555049529e-13, 6.902768790176374e-14, 8.333561024201448e-15, 8.803309407169875e-16, 8.266254837203537e-17, 6.985767429706025e-18, 5.366940381877031e-19, 3.779643669278052e-20, 2.457043463569609e-21, 1.3200189438929913e-22]] |
| Legacy trial inputs | {"lambda_home": 1.4008755924943532, "lambda_away": 0.8450946126491888, "rho": -0.11083277065839049, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4874 |
| Legacy p draw | 0.2688 |
| Legacy p away | 0.2438 |
| Legacy p over 1 5 | 0.6719 |
| Legacy p under 3 5 | 0.8093 |
| Legacy p btts yes | 0.4373 |
| Legacy p over 2 5 | 0.4002 |
| Legacy goal margin distribution | {"-1": 0.16052086526940115, "-10": 6.914183340875651e-09, "-11": 5.265065118768253e-10, "-12": 3.67981121352339e-11, "-13": 2.369521315623494e-12, "-14": 1.31881356975392e-13, "-2": 0.06315613244057969, "-3": 0.016272195748889575, "-4": 0.003252480133878985, "-5": 0.0005294006347295648, "-6": 7.256195038763091e-05, "-7": 8.58171994832038e-06, "-8": 8.920661651302262e-07, "-9": 8.268826649155543e-08, "0": 0.26879236064349793, "1": 0.24188312284960348, "10": 9.473367097402654e-07, "11": 1.1958080089093165e-07, "12": 1.3854073418224703e-08, "13": 1.4787910097482465e-09, "14": 1.364343808464146e-10, "2": 0.15178369407594158, "3": 0.06482611377086596, "4": 0.02147893358368077, "5": 0.005795311116458614, "6": 0.0013167262117602697, "7": 0.0002581398817730915, "8": 4.448074698027053e-05, "9": 6.834600392679159e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4861 |
| Legacy raw p draw | 0.3012 |
| Legacy raw p away | 0.2127 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4009 |
| Legacy lambda away | 0.8451 |
| Legacy model home team | M'gladbach |
| Legacy model away team | Paderborn |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.201945309097006, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,420.8820 |
| Elo away rating | 1,406.2048 |
| Elo rating diff | 74.6772 |
| Elo home expectancy | 0.6058 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **52.1%**. Expected goals are 0.87 for FC Schalke 04 and 1.62 for RB Leipzig (2.49 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.6%; Under 3.5 goals: 76.1%; Double Chance 1X: 47.9%; Double Chance X2: 77.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 22.1% | 4.52 |
| Draw | 25.8% | 3.88 |
| RB Leipzig win | 52.1% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.87 |
| RB Leipzig expected goals | 1.62 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 23.9% |
| Under 3.5 | 76.1% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 0-1 | 12.05% |
| 3 | 0-2 | 10.45% |
| 4 | 1-2 | 9.10% |
| 5 | 0-0 | 8.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 22.1% | 23.3% | 4.08 | -9.8% |
| Draw | 25.8% | 25.5% | 3.75 | -3.3% |
| RB Leipzig win | 52.1% | 51.2% | 1.91 | -0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 3966f2fe1c2f73bfa12e61db83bd0bf9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7504 |
| Dc lambda away | 1.5473 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.3531 |
| Shot lambda away | 1.9245 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.27 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.18 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.28 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.23559939099660643, "-10": 3.146344200164503e-06, "-11": 4.5929358970419966e-07, "-12": 6.155761911471743e-08, "-13": 7.624436900414609e-09, "-14": 8.745925543785169e-10, "-15": 8.64705799332551e-11, "-2": 0.16323566897367772, "-3": 0.079525087861215, "-4": 0.030220533226406835, "-5": 0.009380402101580983, "-6": 0.002456398331920171, "-7": 0.000555699065528944, "-8": 0.00011058491899950734, "-9": 1.963503729820794e-05, "0": 0.2577470980700128, "1": 0.1466342002978235, "10": 7.463223495092652e-09, "11": 5.847309092609642e-10, "12": 4.20622919170718e-11, "13": 2.7961749781839965e-12, "14": 1.7215030551947088e-13, "15": 9.135153414268232e-15, "2": 0.056230463994607516, "3": 0.014703008655401624, "4": 0.0029988146912683345, "5": 0.0004995907786368851, "6": 7.021618080527625e-05, "7": 8.52557202755935e-06, "8": 9.105949072462221e-07, "9": 8.677737227075486e-08} |
| Raw goal margin distribution | {"-1": 0.2453011695802365, "-10": 3.2759079254727936e-06, "-11": 4.782069013784858e-07, "-12": 6.409250848034838e-08, "-13": 7.938404599226477e-09, "-14": 9.106075172253184e-10, "-15": 9.003136341814372e-11, "-2": 0.16995757224615335, "-3": 0.08279986200646886, "-4": 0.03146498857411212, "-5": 0.009766678924411432, "-6": 0.0025575506847708247, "-7": 0.0005785822710842999, "-8": 0.00011513871005254678, "-9": 2.044359110449208e-05, "0": 0.2648864129468656, "1": 0.1276718141908628, "10": 6.498097179205564e-09, "11": 5.09114898483394e-10, "12": 3.662289634458442e-11, "13": 2.434580278917004e-12, "14": 1.4988823735896474e-13, "15": 7.953817096848115e-15, "2": 0.04895887409897846, "3": 0.012801650537776666, "4": 0.0026110151061540803, "5": 0.00043498488710033624, "6": 6.113599126776373e-05, "7": 7.42306532556942e-06, "8": 7.928389391080629e-07, "9": 7.555552883311624e-08} |
| Unadjusted home-win probability | 19.3% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 54.3% |
| Raw p over 1 5 | 72.0% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 47.5% |
| P home draw | 47.9% |
| P draw away | 77.9% |
| P home away | 74.2% |
| Raw p home draw | 45.7% |
| Raw p draw away | 80.7% |
| Raw p home away | 73.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4556 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.08 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.91 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -20.9% |
| Under 2.5 probability edge | +20.9% |
| Raw edge prob home | -0.0409 |
| Raw ev home | -0.2144 |
| Raw edge prob draw | 0.0102 |
| Raw ev draw | -0.0067 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.0363 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.06789893605930342, 0.0885572986451453, 0.10073596918789647, 0.06887961092482972, 0.0353230393230234, 0.014491569743360222, 0.00495440552991978, 0.0014518471037951264, 0.00037227019469041566, 8.484829657801899e-05, 1.7404858571502293e-05, 3.2456761507013003e-06, 5.548189793838936e-07, 8.754580240822583e-08, 1.282728259810623e-08, 1.7541663453545388e-09, 2.2489415214505135e-10, 2.7136673676685367e-11], [0.047811987195128865, 0.11424555447119022, 0.08939192035603326, 0.06112296078138829, 0.0313452517839688, 0.012859649425877615, 0.004396481496256778, 0.00128835213199284, 0.0003303482148726773, 7.529338558206554e-05, 1.5444867843875305e-05, 2.8801750388065704e-06, 4.923398704249497e-07, 7.768712069255036e-08, 1.1382780486833446e-08, 1.556626689546037e-09, 1.9956843914997084e-10, 2.4080766697238318e-11], [0.02745603786340718, 0.05632033584870015, 0.0468027857846143, 0.027119900101935494, 0.013907704832749127, 0.005705751215538415, 0.0019506931184982356, 0.0005716343035267449, 0.00014657357025361432, 3.340723468264799e-05, 6.852797502915408e-06, 1.2779168144012193e-06, 2.1844832009823377e-07, 3.446932094674485e-08, 5.050473107630966e-09, 6.906661551864739e-10, 8.854734888586122e-11, 1.0684495300266524e-11], [0.008121388913229157, 0.016659335677876093, 0.01708657645837359, 0.009466082019610321, 0.004113844845315046, 0.0016877389554184946, 0.0005770074161646722, 0.00016908719743830749, 4.335589040021805e-05, 9.881729720911491e-06, 2.0270307734007177e-06, 3.7800280944175754e-07, 6.461616107121624e-08, 1.0195890695376974e-08, 1.493910246880251e-09, 2.0429635489940143e-10, 2.6191960439270273e-11, 3.1604320370887423e-12], [0.0018017063735139502, 0.0036958248878396958, 0.003790607005217861, 0.0025918799192901506, 0.0010769396063960083, 0.0003744199502442269, 0.00012800740739989387, 3.751150013367353e-05, 9.618377459574937e-06, 2.1922328323061914e-06, 4.4969084755883983e-07, 8.38588175315693e-08, 1.4334906316870941e-08, 2.2619285254999755e-09, 3.314196182475075e-10, 4.532254872172669e-11, 5.810609806087358e-12, 7.01132602454867e-13], [0.0003197626308547355, 0.0006559263521997407, 0.0006727480605848389, 0.00046000078261107443, 0.00023589891862956533, 7.841378350513883e-05, 2.2718455105008304e-05, 6.657453260076585e-06, 1.7070471227945376e-06, 3.89072352859126e-07, 7.981007926739016e-08, 1.4883066690807922e-08, 2.544125626862766e-09, 4.014417813867186e-10, 5.88195782651343e-11, 8.043739884227615e-12, 1.0312534305137883e-12, 1.2443537350746889e-13], [4.7292269518424316e-05, 9.70102283357782e-05, 9.949812620108509e-05, 6.80332186778006e-05, 3.4888990027112905e-05, 1.4313497421037621e-05, 3.9648884873195925e-06, 9.846243541350068e-07, 2.524689404639182e-07, 5.754304223854176e-08, 1.1803755082046754e-08, 2.2011765393628024e-09, 3.762712187872353e-10, 5.937245659553566e-11, 8.699300918431847e-12, 1.1896534423805325e-12, 1.5252037127444557e-13, 1.840374907415128e-14], [5.995229515517899e-06, 1.2297963074053928e-05, 1.2613353281915933e-05, 8.624554600703446e-06, 4.422868788220633e-06, 1.81451859009352e-06, 6.203510797041553e-07, 1.4729091699739856e-07, 3.2005426236335207e-08, 7.294717482458703e-09, 1.4963591636104862e-09, 2.790426150411802e-10, 4.7699810977231487e-11, 7.526631895973774e-12, 1.1028082636261745e-12, 1.5081207782211912e-13, 1.933497040623248e-14, 2.333038798287156e-15], [6.650120653126494e-07, 1.3641335668379023e-06, 1.3991177643514112e-06, 9.566661047037585e-07, 4.906002513912723e-07, 2.0127282066899307e-07, 6.881153618309053e-08, 2.0164645165154883e-08, 4.189257547321975e-09, 8.091558673985294e-10, 1.6598145163023945e-10, 3.09523939422939e-11, 5.291031766321205e-12, 8.348806345168248e-13, 1.2232739366184976e-13, 1.672860915282502e-14, 2.1447033127466304e-15, 2.587889163688601e-16], [6.556932505778477e-08, 1.345017961804616e-07, 1.3795119257234596e-07, 9.432603416239453e-08, 4.83725469578986e-08, 1.984523844321205e-08, 6.784728005789399e-09, 1.9882077972334484e-09, 5.097992080752484e-10, 9.414410056395905e-11, 1.63655553382922e-11, 3.0518658015095004e-12, 5.216888532900145e-13, 8.231814513522636e-14, 1.2061321977240313e-14, 1.6494191136074012e-15, 2.1146495830850417e-16, 2.5516250702555338e-17], [5.818545183629008e-09, 1.1935532013873615e-08, 1.2241627413585877e-08, 8.370381901639914e-09, 4.292523216819854e-09, 1.7610432387394449e-09, 6.020688244926779e-10, 1.764312335448212e-10, 4.523898521374126e-11, 1.0310927087504913e-11, 1.7136975639267487e-12, 2.7081900026889063e-13, 4.629405841814694e-14, 7.304815879677547e-15, 1.0703075994304176e-15, 1.463675221730308e-16, 1.8765152967304698e-17, 2.2642822310399363e-18], [4.693917194316699e-10, 9.628592229698306e-10, 9.875524480710664e-10, 6.752526325936325e-10, 3.4628498874812606e-10, 1.4206628766090717e-10, 4.856989364626051e-11, 1.4233001113072468e-11, 3.649504194719996e-12, 8.317996409404701e-13, 1.7062634954707872e-13, 2.5780413437215185e-14, 3.734618705291415e-15, 5.892916489745405e-16, 8.634349456131323e-17, 1.1807711504081108e-17, 1.5138161067313051e-18, 1.826634143353899e-19], [3.471105995991719e-11, 7.120250067881809e-11, 7.302854059731202e-11, 4.9934273758447765e-11, 2.5607437264144602e-11, 1.0505663447261654e-11, 3.5916962758597848e-12, 1.052516554070454e-12, 2.6987727665983216e-13, 6.15107723806476e-14, 1.261765217554632e-14, 2.3529529168980916e-15, 3.258880641464494e-16, 4.357754283820809e-17, 6.38501723144014e-18, 8.731687523244156e-19, 1.1194522500878492e-19, 1.3507781379602937e-20], [2.3693991121428117e-12, 4.860328151475498e-12, 4.984974802042005e-12, 3.408545404415374e-12, 1.7479800152453113e-12, 7.171232936463844e-13, 2.451714807020004e-13, 7.184545189947852e-14, 1.8421995192417964e-14, 4.198764590716137e-15, 8.612889925167699e-16, 1.606140682148583e-16, 2.745552213593713e-17, 3.510126907965106e-18, 4.358453523649443e-19, 5.960305645801006e-20, 7.641452524086939e-21, 9.220497802374443e-22], [1.5018407485843287e-13, 3.080713093867946e-13, 3.159720221892922e-13, 2.160502363454213e-13, 1.1079550089948019e-13, 4.5454772842517656e-14, 1.5540164517746614e-14, 4.553915239949185e-15, 1.167675927133137e-15, 2.66138183463218e-16, 5.459269815033437e-17, 1.0180503200359021e-17, 1.7402649349403536e-18, 2.7459927614847373e-19, 3.259926557234257e-20, 3.777932492253609e-21, 4.843525398584104e-22, 5.844401329801605e-23], [8.884772716054889e-15, 1.8225258349257043e-14, 1.8692658355623796e-14, 1.2781363450075719e-14, 6.554575406089154e-15, 2.6890689039191232e-15, 9.193440106111672e-16, 2.6940607326886105e-16, 6.907879699206378e-17, 1.5744527329967028e-17, 3.2296614370007274e-18, 6.022706279312309e-19, 1.0295271604023139e-19, 1.624507897306789e-20, 2.380242262723447e-21, 2.637341487380413e-22, 2.8653918434044003e-23, 3.45750223688118e-24], [4.92765209275457e-16, 1.0108050629525449e-15, 1.0367278939931717e-15, 7.088770232604035e-16, 3.635283450590557e-16, 1.4914051755104507e-16, 5.0988444866612724e-17, 1.494173732036178e-17, 3.831232260424751e-18, 8.732193329689699e-19, 1.7912273557845108e-19, 3.340299425743469e-20, 5.70993972342915e-21, 9.009808124179674e-22, 1.320124458105452e-22, 1.8053066800211176e-23, 1.8752858214381403e-24, 1.917591893204474e-25], [2.5722004759738937e-17, 5.276332856100552e-17, 5.4116482498949573e-17, 3.7002892702558804e-17, 1.8975929399841213e-17, 7.785032364517984e-18, 2.661561727296282e-18, 7.799484039025823e-19, 1.999876870025189e-19, 4.558144815448645e-20, 9.350083509144074e-21, 1.7436133093539425e-21, 2.9805492347931926e-22, 4.70305782738276e-23, 6.890958808712203e-24, 9.423576612596e-25, 1.2081563861239021e-25, 1.1811653439411803e-26]] |
| Legacy trial inputs | {"lambda_home": 0.8873882991019438, "lambda_away": 2.0512914546844607, "rho": -0.11083277065839049, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1881 |
| Legacy p draw | 0.2396 |
| Legacy p away | 0.5723 |
| Legacy p over 1 5 | 0.7957 |
| Legacy p under 3 5 | 0.6694 |
| Legacy p btts yes | 0.5317 |
| Legacy p over 2 5 | 0.5533 |
| Legacy goal margin distribution | {"-1": 0.20958111980935473, "-10": 2.0514017439314018e-05, "-11": 3.774025624525776e-06, "-12": 6.37766804584154e-07, "-13": 9.964614214328747e-08, "-14": 1.4475617068575217e-08, "-15": 1.964419279804776e-09, "-16": 2.4897491884228966e-10, "-17": 2.7136673676685367e-11, "-2": 0.1775892985508505, "-3": 0.10654689895864095, "-4": 0.050312488602822114, "-5": 0.019505315726178973, "-6": 0.006399677919723242, "-7": 0.0018177160475592179, "-8": 0.0004548091257852199, "-9": 0.00010163801935471769, "0": 0.23957282818916517, "1": 0.12406163287355136, "10": 6.857955028938763e-09, "11": 5.458019515263608e-10, "12": 3.990051281040948e-11, "13": 2.69689093283789e-12, "14": 1.6948306399438564e-13, "15": 9.949694261506383e-15, "16": 5.455285378364625e-16, "17": 2.5722004759738937e-17, "2": 0.04840275568355696, "3": 0.01256262618681151, "4": 0.002566266468581271, "5": 0.00043039306180843163, "6": 6.108811464522185e-05, "7": 7.5060416972773395e-06, "8": 8.124570819132958e-07, "9": 7.854413816276172e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1428 |
| Legacy raw p draw | 0.2245 |
| Legacy raw p away | 0.6328 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8874 |
| Legacy lambda away | 2.0513 |
| Legacy model home team | Schalke 04 |
| Legacy model away team | RB Leipzig |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.282019492259554, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,439.0953 |
| Elo away rating | 1,517.4051 |
| Elo rating diff | -18.3098 |
| Elo home expectancy | 0.4737 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.7%**. Expected goals are 1.77 for Werder Bremen and 1.65 for TSG Hoffenheim (3.41 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.3%; Under 3.5 goals: 55.6%; Double Chance 1X: 59.3%; Double Chance X2: 64.5%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 74.2%; BTTS Yes (both teams score): 67.6%; BTTS No (at least one team does not score): 32.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 35.5% | 2.82 |
| Draw | 23.8% | 4.19 |
| TSG Hoffenheim win | 40.7% | 2.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.77 |
| TSG Hoffenheim expected goals | 1.65 |
| Expected total goals | 3.41 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.1% |
| Under 1.5 | 13.9% |
| Over 2.5 | 66.3% |
| Under 2.5 | 33.7% |
| Over 3.5 | 44.4% |
| Under 3.5 | 55.6% |
| Over 4.5 | 25.8% |
| Under 4.5 | 74.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 9.04% |
| 3 | 2-1 | 7.41% |
| 4 | 2-2 | 6.93% |
| 5 | 0-1 | 5.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 35.5% | 33.3% | 2.90 | +2.9% |
| Draw | 23.8% | 23.8% | 4.02 | -4.2% |
| TSG Hoffenheim win | 40.7% | 42.9% | 2.27 | -7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 2fad25b09c01b71e47a5b0fd1d0b4e61 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T16:04:27Z |
| Market best draw last update utc | 2026-10-28T16:04:27Z |
| Market best away last update utc | 2026-10-28T16:04:27Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7768 |
| Dc lambda away | 1.6720 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T16:04:41.599646+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.7215 |
| Shot lambda away | 1.5413 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.6% |
| P btts no | 32.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.11 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.21 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.88 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.2005123830322828, "-10": 1.9725036670559275e-06, "-11": 2.8889265855840525e-07, "-12": 3.891009244934339e-08, "-13": 4.849685812753389e-09, "-14": 5.619948165912536e-10, "-15": 6.015326579297146e-11, "-16": 5.236677171509137e-12, "-2": 0.12270147054170571, "-3": 0.055464158069159886, "-4": 0.020139338637114885, "-5": 0.006077116681132201, "-6": 0.0015639725821335918, "-7": 0.00035024068779537733, "-8": 6.934364836659544e-05, "-9": 1.2294346300561311e-05, "0": 0.23839415002961345, "1": 0.16495900763661878, "10": 3.0463501438557763e-06, "11": 4.786547604739305e-07, "12": 6.916271238018357e-08, "13": 9.24798751981465e-09, "14": 1.1497139963730146e-09, "15": 1.3202026380450982e-10, "16": 1.2329942866398171e-11, "2": 0.10799925272088322, "3": 0.052372979890613555, "4": 0.020401586526886756, "5": 0.006604503720168917, "6": 0.00182345742050066, "7": 0.00043808356998302543, "8": 9.305097605590621e-05, "9": 1.7698789527117416e-05} |
| Raw goal margin distribution | {"-1": 0.17507770409742385, "-10": 1.7222946938708544e-06, "-11": 2.5224708133294356e-07, "-12": 3.3974408708477403e-08, "-13": 4.2345108309545675e-09, "-14": 4.907066621796026e-10, "-15": 5.2522919082259165e-11, "-16": 4.5724129473819116e-12, "-2": 0.1071369828982624, "-3": 0.04842861726341213, "-4": 0.01758469535549299, "-5": 0.005306244033284874, "-6": 0.0013655851315037433, "-7": 0.0003058132100043157, "-8": 6.0547516149204406e-05, "-9": 1.0734827900052339e-05, "0": 0.23973153047660467, "1": 0.188339950119023, "10": 3.4781334002855046e-06, "11": 5.464982785934321e-07, "12": 7.896568963651113e-08, "13": 1.0558777802665377e-08, "14": 1.3126720379225156e-09, "15": 1.5073253807645967e-10, "16": 1.4077563012159707e-11, "2": 0.12330683944916966, "3": 0.0597962158084242, "4": 0.02329326445323385, "5": 0.007540612174132573, "6": 0.002081910436669114, "7": 0.0005001766129699404, "8": 0.00010623982551775128, "9": 2.0207378696453866e-05} |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 86.2% |
| Raw p under 3 5 | 55.6% |
| Raw p btts yes | 67.6% |
| P home draw | 59.3% |
| P draw away | 64.5% |
| P home away | 76.2% |
| Raw p home draw | 64.5% |
| Raw p draw away | 59.5% |
| Raw p home away | 76.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6627 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T16:04:45Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T16:04:27Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.90 |
| Reference draw odds | 4.02 |
| Reference away odds | 2.27 |
| Market reference 1x2 last update utc | 2026-10-28T16:04:27Z |
| Market reference home last update utc | 2026-10-28T16:04:27Z |
| Market reference draw last update utc | 2026-10-28T16:04:27Z |
| Market reference away last update utc | 2026-10-28T16:04:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.99 |
| Market reference over 2 5 last update utc | 2026-10-28T16:03:59Z |
| Market reference under 2 5 last update utc | 2026-10-28T16:03:59Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.0718 |
| Raw ev home | 0.1745 |
| Raw edge prob draw | 0.0019 |
| Raw ev draw | -0.0363 |
| Raw edge prob away | -0.0737 |
| Raw ev away | -0.1935 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.04209930979497023, 0.047302267389862596, 0.04760892491268639, 0.025462397675717018, 0.01021342684043046, 0.003277431737681412, 0.000876424645304509, 0.00020088555927998873, 4.028941007707644e-05, 7.182581720997155e-06, 1.1524252172493308e-06, 1.680940127026926e-07, 2.2475179843866204e-08, 2.773907662516798e-09, 3.1790410913314937e-10, 3.400455214789281e-11, 3.409959757396703e-12], [0.043277081709579, 0.10363941169495855, 0.08717042861689936, 0.04662084100989109, 0.018700459986451538, 0.006000873362720875, 0.0016047056748649691, 0.00036781507537709423, 7.376862954964397e-05, 1.3151078885807586e-05, 2.1100539514551937e-06, 3.077747956313058e-07, 4.11513400864394e-08, 5.0789367818901825e-09, 5.82072321587455e-10, 6.226125439912321e-11, 6.2435279553947865e-12], [0.04818880366081512, 0.07731759231566451, 0.06852187656723871, 0.042680639194916985, 0.017119973989559417, 0.005493704216840259, 0.0014690825484769076, 0.00033672885736424926, 6.753400825703384e-05, 1.2039603764976263e-05, 1.9317208663130123e-06, 2.8176293522551724e-07, 3.7673398003352474e-08, 4.649685925564004e-09, 5.328779619773722e-10, 5.699918914521796e-11, 5.7158506409407475e-12], [0.029410722725852587, 0.04718868485368941, 0.03785646478288413, 0.02236658721027162, 0.01044870944762988, 0.0033529326147334975, 0.0008966144874390595, 0.0002055132791309802, 4.121754101623746e-05, 7.348043967914066e-06, 1.178973173577116e-06, 1.7196632688099977e-07, 2.299293152442926e-08, 2.837809057921506e-09, 3.2522753826275034e-10, 3.4787901342145e-11, 3.488513629148095e-12], [0.013462524677081027, 0.021600245605775992, 0.01732849600729601, 0.009267696283187273, 0.004106697594685422, 0.0015347782673413033, 0.00041041815855705996, 9.407207084158649e-05, 1.886700195136434e-05, 3.363508750479093e-06, 5.396656039651383e-07, 7.871621995971638e-08, 1.0524831740158804e-08, 1.298984551560517e-09, 1.488703219006552e-10, 1.5923885470206876e-11, 1.5968393995791637e-12], [0.004929890975353766, 0.007909872659964446, 0.006345585106206465, 0.0033937714778407304, 0.0013613029355488528, 0.00048257597747983677, 0.00015029252124130262, 3.44485944649226e-05, 6.908976204913449e-06, 1.2316955275662e-06, 1.9762211431455133e-07, 2.8825379466454447e-08, 3.85412649242964e-09, 4.756798870544874e-10, 5.4515365731175694e-11, 5.831225654559841e-12, 5.847524393753997e-13], [0.0015044122859467558, 0.0024137875805805105, 0.0019364274469807548, 0.0010356479549921277, 0.0004154170693375463, 0.00013330502178092573, 3.938004264701279e-05, 1.0512380295166274e-05, 2.1083526467316497e-06, 3.758658951039569e-07, 6.030663522498099e-08, 8.796392300196772e-09, 1.1761305221132099e-09, 1.4515912620383733e-10, 1.66359837142192e-11, 1.779464811839622e-12, 1.7844385574278538e-13], [0.0003935044412756524, 0.0006313669079461766, 0.0005065053029100085, 0.00027089121359506936, 0.00010865935042744365, 3.486817982354498e-05, 9.324170442031283e-06, 2.360984228391707e-06, 5.51475242534375e-07, 9.831407283035856e-08, 1.5774218956531844e-08, 2.300844967609423e-09, 3.076368016232618e-10, 3.796882103828055e-11, 4.351422504114254e-12, 4.65449074760758e-13, 4.667500419205101e-14], [9.006176591773771e-05, 0.0001445015931391285, 0.00011592438926202407, 6.19991504768832e-05, 2.486897721216486e-05, 7.980316153651491e-06, 2.1340324724290957e-06, 4.891422314996947e-07, 1.0837424771909011e-07, 2.250124289566696e-08, 3.6102617052881864e-09, 5.265967525400481e-10, 7.04091509759283e-11, 8.689963095300082e-12, 9.959145408988857e-13, 1.0652780812800622e-13, 1.068255618189898e-14], [1.8322247938553767e-05, 2.939753612459077e-05, 2.358376365975634e-05, 1.2613163815316988e-05, 5.059367444290658e-06, 1.6235228090997354e-06, 4.341495158387737e-07, 9.951154245566224e-08, 1.9957937025282046e-08, 3.930556657215957e-09, 7.344749396517015e-10, 1.0713132443448725e-10, 1.4324102000202355e-11, 1.7678940312407513e-12, 2.026097640660019e-13, 2.1672114609154016e-14, 2.173268989207489e-15], [3.3547453738096013e-06, 5.3825954460452525e-06, 4.318112182518122e-06, 2.309430212954388e-06, 9.263541015850217e-07, 2.97261867177397e-07, 7.949139672633243e-08, 1.8220247199653457e-08, 3.654234847759252e-09, 6.514575510421821e-10, 1.154694360348418e-10, 1.961540506612422e-11, 2.6226975576528924e-12, 3.2369577917406223e-13, 3.7097203954916346e-14, 3.968095316118165e-15, 3.9791864579271583e-16], [5.584029248753082e-07, 8.959419286951731e-07, 7.187569260792044e-07, 3.8440848470257915e-07, 1.5419317478867257e-07, 4.947973022979561e-08, 1.3231474668970447e-08, 3.0327903296827306e-09, 6.082534439425548e-10, 1.0843618856263932e-10, 1.739828421257979e-11, 2.803461899727897e-12, 4.3655235318011993e-13, 5.387969867153527e-14, 6.174891052788685e-15, 6.604960388359275e-16, 6.623421777634001e-17], [8.520150089432106e-08, 1.367034333783752e-07, 1.0966842427233264e-07, 5.8653309992036635e-08, 2.352690026218774e-08, 7.54965114189915e-09, 2.0188674711781072e-09, 4.627452265663759e-10, 9.280772725110242e-11, 1.654526795120126e-11, 2.6546421264336697e-12, 3.872090272260166e-13, 5.719329925367728e-14, 8.221001341591563e-15, 9.421691078605848e-16, 1.007789381764809e-16, 1.0106062331900628e-17], [1.2000095433596398e-08, 1.925381864663995e-08, 1.5446107680103657e-08, 8.26094974868766e-09, 3.313615903939725e-09, 1.0633208716067152e-09, 2.843447834559859e-10, 6.517475422323012e-11, 1.307138456832802e-11, 2.330296911495754e-12, 3.7388964425358627e-13, 5.4535955713098625e-14, 7.291785072541017e-15, 9.9419466709879e-16, 1.3269859204636364e-16, 1.4194079483579725e-17, 1.4233753063939813e-18], [1.5694138146047334e-09, 2.5180807215359726e-09, 2.0200951658400176e-09, 1.0803954626101154e-09, 4.3336610152094415e-10, 1.3906476615052992e-10, 3.718759019342851e-11, 8.523778848877925e-12, 1.7095206976530693e-12, 3.047642566902592e-13, 4.8898575521858893e-14, 7.13240013485109e-15, 9.536447680187127e-16, 1.1769972688552737e-16, 1.4901443543443158e-17, 1.856350605742763e-18, 1.8615392532361516e-19], [1.9156978815390538e-10, 3.0736838550167334e-10, 2.465820036560377e-10, 1.3187798397632135e-10, 5.2898637369494666e-11, 1.6974877844973608e-11, 4.5392863940754704e-12, 1.0404512137938197e-12, 2.086718715271383e-13, 3.7200911287849e-14, 5.96878252668466e-15, 8.706131997483617e-16, 1.1640621771220774e-16, 1.436696398069605e-17, 1.6465280899391023e-18, 1.9456235192059117e-19, 2.272279478261406e-20], [2.1922387154890686e-11, 3.517385915115137e-11, 2.821773830659283e-11, 1.509152486827787e-11, 6.05348275192833e-12, 1.9425288695601743e-12, 5.194555712401955e-13, 1.1906456933720353e-13, 2.3879472854447992e-14, 4.257105400731442e-15, 6.830406957917818e-16, 9.962906892034729e-17, 1.332100534492076e-17, 1.6440909062975726e-18, 1.8842128812111347e-19, 2.0154446997110023e-20, 2.2327074732530377e-21]] |
| Legacy trial inputs | {"lambda_home": 1.8309682223819972, "lambda_away": 1.6044721271745443, "rho": -0.11083277065839049, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3788 |
| Legacy p draw | 0.2413 |
| Legacy p away | 0.3799 |
| Legacy p over 1 5 | 0.8673 |
| Legacy p under 3 5 | 0.5515 |
| Legacy p btts yes | 0.6816 |
| Legacy p over 2 5 | 0.6679 |
| Legacy goal margin distribution | {"-1": 0.18929820254920726, "-10": 1.5008660999333213e-06, "-11": 2.1423677489086832e-07, "-12": 2.812337932847548e-08, "-13": 3.416467686878619e-09, "-14": 3.858812141732134e-10, "-15": 4.0248080103287594e-11, "-16": 3.409959757396703e-12, "-2": 0.11514974966668247, "-3": 0.050654549594859266, "-4": 0.01790905740793316, "-5": 0.00526365405471737, "-6": 0.0013196914790073104, "-7": 0.000287955485733888, "-8": 5.55551937798206e-05, "-9": 9.598746865259403e-06, "0": 0.24125831228961525, "1": 0.1692232769885057, "10": 4.369067536960732e-06, "11": 7.116877025626362e-07, "12": 1.0661334617352927e-07, "13": 1.4779849683656685e-08, "14": 1.904999938413e-09, "15": 2.2674364730505674e-10, "16": 2.1922387154890686e-11, "2": 0.11655227855819844, "3": 0.058509294054351145, "4": 0.02360629111701742, "5": 0.00791755334623475, "6": 0.002265294666591718, "7": 0.0005640612641949135, "8": 0.00012418645118260387, "9": 2.4485710959691313e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4244 |
| Legacy raw p draw | 0.2447 |
| Legacy raw p away | 0.3309 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8310 |
| Legacy lambda away | 1.6045 |
| Legacy model home team | Werder Bremen |
| Legacy model away team | Hoffenheim |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 9.899897913813646, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,429.1271 |
| Elo away rating | 1,502.6430 |
| Elo rating diff | -13.5159 |
| Elo home expectancy | 0.4806 |

</details>


---
