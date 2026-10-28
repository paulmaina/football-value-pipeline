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
| Training sha256 | b503b49ce85ac150be86a06eec2c967cda0f9fae8047e393c246966dba30bb37 |
| Training as of utc | 2026-10-28T11:55:30.932324+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 51, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-28T11:55:30.932324+00:00', 'observations': 260, 'observations_sha256': 'e6bab8164c20bd8257bd3373e3316e614981a1eff2a913b47788b32caf425504', 'eligible_training_matches': 59, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 14, 'retrospective_eligible_training_matches': 59, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '86afca44e1adf1be84b9cfb5e19a2b782fb50b436efbc71a1eb81cc00479ac30', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1295, 'tuning_matches': 207, 'audit_matches': 84, 'audit_matchdays': 27, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7190086120619453, 'audit_candidate_poisson_score': 0.7076402922761562, 'audit_gain': 0.011368319785789116, 'audit_gain_lower95': 0.00274138308502032, 'audit_baseline_briers': [0.6261395427176581, 0.15436575802266503, 0.29463586752978754, 0.24503067338840298], 'audit_candidate_briers': [0.6200888825660128, 0.15165219550089012, 0.2913539013203029, 0.24278841118449657], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1579.861 |
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
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261028T115530932324Z_a1c589e24d18d6e36750b72da1e6eb69325b0669940347df26d458feae34932a.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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
| Market best home last update utc | 2026-10-28T11:55:51Z |
| Market best draw last update utc | 2026-10-28T11:55:51Z |
| Market best away last update utc | 2026-10-28T11:55:51Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8827 |
| Dc lambda away | 1.7406 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T11:55:30.932324+00:00 |
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
| Fair Under 0.5 odds | 26.64 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.75 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.11 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.20730054253220653, "-10": 2.2638490849694974e-06, "-11": 3.3669667441913244e-07, "-12": 4.605867541169747e-08, "-13": 5.8312954174480235e-09, "-14": 6.864035014713424e-10, "-15": 7.454395899922992e-11, "-16": 6.541047337661959e-12, "-2": 0.12715915465404257, "-3": 0.057928174148586524, "-4": 0.021255588975717585, "-5": 0.006492309326382014, "-6": 0.0016930683610422994, "-7": 0.00038448137498906833, "-8": 7.723330034232508e-05, "-9": 1.389816259217555e-05, "0": 0.24047307542127744, "1": 0.1531693293340888, "10": 3.814562796430436e-06, "11": 6.219909695164383e-07, "12": 9.328346132413184e-08, "13": 1.2948104858438075e-08, "14": 1.6709698364257708e-09, "15": 1.989525592362657e-10, "16": 1.9139576494911274e-11, "2": 0.10265055033574186, "3": 0.051268598542905795, "4": 0.020624465633865195, "5": 0.006906479405488911, "6": 0.001974603794796861, "7": 0.0004916190868113259, "8": 0.00010826946195513779, "9": 2.1360269554751213e-05} |
| Raw goal margin distribution | {"-1": 0.17146595713578916, "-10": 1.8725134310971146e-06, "-11": 2.7849429064926055e-07, "-12": 3.809683644530925e-08, "-13": 4.823280430821476e-09, "-14": 5.677497604370985e-10, "-15": 6.165806959481639e-11, "-16": 5.410342533225475e-12, "-2": 0.10517804678656753, "-3": 0.04791453849655464, "-4": 0.01758128494835035, "-5": 0.005370029518840997, "-6": 0.0014003995526318401, "-7": 0.00031801878643488156, "-8": 6.388252343283285e-05, "-9": 1.1495685067616094e-05, "0": 0.23538373540110136, "1": 0.18863902446388484, "10": 4.6979079153983075e-06, "11": 7.660265291036561e-07, "12": 1.1488527905228911e-07, "13": 1.594652062374898e-08, "14": 2.0579193055315065e-09, "15": 2.45024358676028e-10, "16": 2.357176240405742e-11, "2": 0.12642152159443903, "3": 0.06314095946499584, "4": 0.02540050997269318, "5": 0.008505825175284532, "6": 0.0024318663218842315, "7": 0.0006054641966972097, "8": 0.00013334161461201513, "9": 2.6306705321566786e-05} |
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
| Unanchored p over 2 5 | 0.6784 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T11:55:51Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T11:55:51Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T11:55:51Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T11:55:51Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.17 |
| Reference draw odds | 3.94 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-28T11:55:51Z |
| Market reference home last update utc | 2026-10-28T11:55:51Z |
| Market reference draw last update utc | 2026-10-28T11:55:51Z |
| Market reference away last update utc | 2026-10-28T11:55:51Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-28T11:55:04Z |
| Market reference under 2 5 last update utc | 2026-10-28T11:55:04Z |
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
| Legacy trial matrix | [[0.04198562499367256, 0.04851987456568982, 0.05060927802716982, 0.02827344104009965, 0.011846456313091976, 0.003970893446721465, 0.0011091920900563356, 0.00026556968871131205, 5.5636307426075225e-05, 1.0360615806819116e-05, 1.7364222820722516e-06, 2.6456503410229016e-07, 3.6950556224825614e-08, 4.763732964265934e-09, 5.702813298820324e-10, 6.371881277592252e-11, 6.674480573495429e-12], [0.04044672664444625, 0.10429506984775568, 0.08977723890315904, 0.05015506187439985, 0.02101476606730741, 0.0070440809180070734, 0.0019676274220909035, 0.0004711016303388737, 9.869482945002371e-05, 1.8378991298261395e-05, 3.0802889140342656e-06, 4.6931944493008566e-07, 6.554764349769744e-08, 8.450521506632786e-09, 1.0116382843348297e-09, 1.1303261576145349e-10, 1.1840051080742567e-11], [0.044058672814211726, 0.0738416158070207, 0.069784992450991, 0.044485745970169556, 0.018639345859723613, 0.00624784782633729, 0.0017452151466241786, 0.00041785029606522897, 8.753878367208175e-05, 1.6301507914193884e-05, 2.7321060930521963e-06, 4.1626956135163954e-07, 5.8138415318557416e-08, 7.495310323829978e-09, 8.972869746091981e-10, 1.0025588730605013e-10, 1.0501701821657814e-11], [0.026052311283543003, 0.04366324806914662, 0.036589445197366045, 0.023052891687863702, 0.01102162206534968, 0.0036944117021028974, 0.0010319622755849624, 0.0002470788448148745, 5.1762513392645145e-05, 9.639236305700261e-06, 1.6155202562729263e-06, 2.4614414138000735e-07, 3.437779662129076e-08, 4.43204811335545e-09, 5.305743019487187e-10, 5.928225743700847e-11, 6.209755932015469e-12], [0.011553734143502569, 0.01936386965986366, 0.01622676459173386, 0.009065264114411243, 0.0042836236780336, 0.0016384055202697092, 0.00045765681395662755, 0.00010957504900066445, 2.2955748986305715e-05, 4.274828916726845e-06, 7.164543422376201e-07, 1.0916052474322186e-07, 1.5245938000621722e-08, 1.965534077019408e-09, 2.353002143023789e-10, 2.6290620989414418e-11, 2.7539157026680367e-12], [0.0040990995756468125, 0.006870023917788067, 0.005757023921958846, 0.0032162260116922114, 0.0013475855622421097, 0.0005094214001703297, 0.0001623700899277202, 3.887565970285842e-05, 8.144371314042913e-06, 1.516648139975771e-06, 2.5418775036364423e-07, 3.872859242688741e-08, 5.409040680049832e-09, 6.973433697676473e-10, 8.34811496107428e-11, 9.32753618896492e-12, 9.770498912268945e-13], [0.0012119182365899917, 0.0020311551642321363, 0.0017020914351430045, 0.0009508924788561248, 0.00039842006472577267, 0.00013354910382048097, 4.207078036819258e-05, 1.1493773226020369e-05, 2.4079220177254486e-06, 4.484042179036097e-07, 7.515181431884968e-08, 1.1450292088159314e-08, 1.5992085387618655e-09, 2.061728756255389e-10, 2.4681597935759426e-11, 2.7577303261963233e-12, 2.8886943568559123e-13], [0.0003071223225089385, 0.0005147319947674346, 0.00043134120677527617, 0.00024097360510416668, 0.00010096695628332075, 3.384379382700032e-05, 9.4536075858193e-06, 2.5526447066115824e-06, 6.102116299405443e-07, 1.1363385801739657e-07, 1.9044848948975888e-08, 2.9017141531066327e-09, 4.05268792705554e-10, 5.224799040785797e-11, 6.254769878363307e-12, 6.988594750565551e-13, 7.320481639028243e-14], [6.810162878033835e-05, 0.00011413721719297909, 9.564605562208227e-05, 5.3433742186506766e-05, 2.2388519726329044e-05, 7.504558655639893e-06, 2.0962529495905307e-06, 5.018979564257911e-07, 1.1858132002378096e-07, 2.5197291920561033e-08, 4.223024958607576e-09, 6.434291668127459e-10, 8.986473093725147e-11, 1.1585524680222695e-11, 1.386939291429534e-12, 1.549658395102117e-13, 1.6232513449421277e-14], [1.342304642556379e-05, 2.2496806503816553e-05, 1.8852140074040805e-05, 1.0531959586085006e-05, 4.412848048840345e-06, 1.4791722465689966e-06, 4.131780864278314e-07, 9.892567462269021e-08, 2.072472680277477e-08, 4.35248361622535e-09, 8.323715759948155e-10, 1.2682192382721464e-10, 1.771262269339122e-11, 2.2835435573611802e-12, 2.7337012097531643e-13, 3.0544257095985785e-14, 3.1994797413432417e-15], [2.3811524146008946e-06, 3.990772543656902e-06, 3.3442347910087856e-06, 1.8682942905661615e-06, 7.828076767097746e-07, 2.623945753342994e-07, 7.329483687727655e-08, 1.754870701670448e-08, 3.6764182812023833e-09, 6.846241082285136e-10, 1.2940260773641067e-10, 2.2497302070742046e-11, 3.1420925591793604e-12, 4.050842918267347e-13, 4.849390391740174e-14, 5.41833271155078e-15, 5.675648187476278e-16], [3.839994589631881e-07, 6.435768194478433e-07, 5.393121173255457e-07, 3.0129276578948716e-07, 1.2624043823719993e-07, 4.231538239442549e-08, 1.1819981590883055e-08, 2.830013718818371e-09, 5.928820945049465e-10, 1.1040674487734051e-10, 1.8503990059152626e-11, 3.179534497841217e-12, 5.067134028626914e-13, 6.532641419429022e-14, 7.820428777725373e-15, 8.7379405743196795e-16, 9.152903526427926e-17], [5.6765630911118515e-08, 9.513826997144301e-08, 7.972509305261966e-08, 4.4539317803142226e-08, 1.8661792238925315e-08, 6.2553717793000134e-09, 1.747316816997404e-09, 4.183534910950122e-10, 8.76442020031727e-11, 1.6321138958703454e-11, 2.735396224038845e-12, 4.167708527861429e-13, 6.564579809910051e-14, 9.657032139869309e-15, 1.1560734350034738e-15, 1.2917067927761536e-16, 1.3530496755103271e-17], [7.74601296359454e-09, 1.2982191172800157e-08, 1.0878970151433915e-08, 6.077658744478469e-09, 2.546514189773763e-09, 8.535832354339386e-10, 2.384319261272868e-10, 5.708685895627517e-11, 1.1959580365863623e-11, 2.2271179219816017e-12, 3.7326132506390114e-13, 5.687089840654788e-14, 7.942891381160418e-15, 1.1548514167069003e-15, 1.5775319802972884e-16, 1.7626118835309987e-17, 1.846317949553089e-18], [9.814909206487727e-10, 1.6449627474309202e-09, 1.378465344665063e-09, 7.700951321076926e-10, 3.226667149039183e-10, 1.0815682849149798e-10, 3.021151291465622e-11, 7.2334288642786245e-12, 1.51538857461676e-12, 2.8219627696372175e-13, 4.72956349674818e-14, 7.206064680953364e-15, 1.0064372227296999e-15, 1.2975171862664846e-16, 1.751765316676006e-17, 2.233390995398627e-18, 2.3394542619978904e-19], [1.1607297884136444e-10, 1.9453641614042844e-10, 1.6301992755989947e-10, 9.107291172483627e-11, 3.815917802591433e-11, 1.2790831785529288e-11, 3.5728708493711973e-12, 8.554390242947352e-13, 1.7921272857182241e-13, 3.337306723476398e-14, 5.593271543704803e-15, 8.522028840459544e-16, 1.1902317586580123e-16, 1.5344684473317822e-17, 1.8369600340123837e-18, 2.314724395005051e-19, 2.766683005826749e-20], [1.286907257653442e-11, 2.1568355383655522e-11, 1.8074105619852542e-11, 1.0097301908181591e-11, 4.230728257155639e-12, 1.4181262874900886e-12, 3.9612608141970583e-13, 9.484297722292636e-14, 1.986941003540145e-14, 3.700089621484655e-15, 6.201289753627875e-16, 9.448418464135298e-17, 1.3196162481536695e-17, 1.7012732861886e-18, 2.0366473087769175e-19, 2.2755917432083476e-20, 2.6882224692297705e-21]] |
| Legacy trial inputs | {"lambda_home": 1.7739284653490162, "lambda_away": 1.675983662022658, "rho": -0.11083009035464207, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3507 |
| Legacy p draw | 0.2440 |
| Legacy p away | 0.4054 |
| Legacy p over 1 5 | 0.8690 |
| Legacy p under 3 5 | 0.5479 |
| Legacy p btts yes | 0.6855 |
| Legacy p over 2 5 | 0.6701 |
| Legacy goal margin distribution | {"-1": 0.1956173871520988, "-10": 2.268557107054177e-06, "-11": 3.381658298966469e-07, "-12": 4.636040087920727e-08, "-13": 5.8818368918388296e-09, "-14": 6.938156474651437e-10, "-15": 7.555886385666508e-11, "-16": 6.674480573495429e-12, "-2": 0.12359715584598689, "-3": 0.05668620474026569, "-4": 0.020907381765390514, "-5": 0.006412674562362619, "-6": 0.0016782285761822362, "-7": 0.0003822963284830367, "-8": 7.700951763682913e-05, "-9": 1.3893603924988085e-05, "0": 0.2439563705500143, "1": 0.16143416336312882, "10": 3.1108678395186066e-06, "11": 4.908263715224862e-07, "12": 7.122159106856573e-08, "13": 9.56409294049354e-09, "14": 1.1941014424090536e-09, "15": 1.3764133422501997e-10, "16": 1.286907257653442e-11, "2": 0.10759937431357972, "3": 0.052233000195537865, "4": 0.020390767008280783, "5": 0.006619717182047452, "6": 0.0018336551755777557, "7": 0.0004421127157248089, "8": 9.42635093032489e-05, "9": 1.800032874308147e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3976 |
| Legacy raw p draw | 0.2453 |
| Legacy raw p away | 0.3572 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7739 |
| Legacy lambda away | 1.6760 |
| Legacy model home team | Elversberg |
| Legacy model away team | Mainz |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.011689239336050124, "mu": 10.093446341951529, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,430.0448 |
| Elo away rating | 1,516.7168 |
| Elo rating diff | -26.6720 |
| Elo home expectancy | 0.4617 |

</details>


---
