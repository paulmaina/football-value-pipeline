# UEFA Champions League — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 557 |
| Training data through | 2026-10-21 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 47edf6adf265e8fdf87d822df1b1a85f5f0ce0cfc84ab39fc30fc515eb43bb29 |
| Training as of utc | 2026-11-01T09:33:34.428047+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 42, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 52, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-01T09:33:34.428047+00:00', 'observations': 356, 'observations_sha256': '4d8cb4d3918c784a4a3ed649310146c48327d251cb27dc5f29610ef6b58abcb0', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 94, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': 'a494ba0252a3a3a8e49424297244a2e11601b497aac91695981925a4b3e4bd8c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'NO_SHOT_DATA', 'cutoff_date': '2026-11-01', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 0} |
| Optimizer objective | 812.263 |
| Base scoring parameter | 0.213 |
| Home-advantage parameter | 0.300 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 71, 'matches': 557, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-21'} |
| Training data health | {'completed_matches': 54, 'latest_completed_utc': '2026-10-21T19:00:00+00:00', 'latest_completed_date': '2026-10-21', 'next_fixture_utc': '2026-11-03T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-11-01T09:33:05.624664+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '95733e3417eba966b8b1d89373f9be3aea64bc0329be8978cfc76e0872e37d6c', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.008000939722222222, 'training_end': '2026-10-21', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 21.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261101T093334428047Z_0bc4b98fbb2e025f638cabdc45ba848070689f69f961360a6ca28dc823c01952.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_NO_PINNACLE': 9} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 9} |
| Legacy comparison status | {'AVAILABLE': 9} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-03 — Atlético Madrid vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **41.7%**. Expected goals are 1.85 for Atlético Madrid and 2.03 for Bayern Munich (3.89 combined). The most likely exact score is 1-1 at 8.6%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 73.7%; Under 3.5 goals: 45.6%; Double Chance 1X: 58.3%; Double Chance X2: 65.2%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 65.8%; BTTS Yes (both teams score): 73.7%; BTTS No (at least one team does not score): 26.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 34.8% | 2.87 |
| Draw | 23.5% | 4.25 |
| Bayern Munich win | 41.7% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 1.85 |
| Bayern Munich expected goals | 2.03 |
| Expected total goals | 3.89 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 89.7% |
| Under 1.5 | 10.3% |
| Over 2.5 | 73.7% |
| Under 2.5 | 26.3% |
| Over 3.5 | 54.4% |
| Under 3.5 | 45.6% |
| Over 4.5 | 34.2% |
| Under 4.5 | 65.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.55% |
| 2 | 2-2 | 8.48% |
| 3 | 1-2 | 7.54% |
| 4 | 2-1 | 6.86% |
| 5 | 1-3 | 5.11% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | 61b42fd619617a7a2a3770c2444e8a40 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Club Atlético de Madrid |
| Matched away-team name | FC Bayern München |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8533 |
| Dc lambda away | 2.0329 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 73.7% |
| P btts no | 26.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.55 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.69 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.80 |
| Fair Over 3.5 odds | 1.84 |
| Fair Under 3.5 odds | 2.19 |
| Fair Over 4.5 odds | 2.92 |
| Fair Under 4.5 odds | 1.52 |
| Goal margin distribution | {"-1": 0.18456436802448767, "-10": 9.169895470496588e-06, "-11": 1.648694782243713e-06, "-12": 2.7284186599094214e-07, "-13": 4.181498514420584e-08, "-14": 5.96584312392817e-09, "-15": 7.950605029499489e-10, "-16": 9.781805326310247e-11, "-17": 9.575167145803483e-12, "-2": 0.12296470494626748, "-3": 0.06568139245868307, "-4": 0.028559168378405324, "-5": 0.010406226206571962, "-6": 0.003251646171859316, "-7": 0.00088746789095853, "-8": 0.0002147165365403901, "-9": 4.661094544039651e-05, "0": 0.23502731887623665, "1": 0.16815031022953691, "10": 3.626984226008418e-06, "11": 5.945005679499846e-07, "12": 8.96920086314758e-08, "13": 1.2531567982737595e-08, "14": 1.6299565419788176e-09, "15": 1.980318770687459e-10, "16": 2.221184677808997e-11, "17": 1.982178430743427e-12, "2": 0.10193326252166723, "3": 0.049637343705603215, "4": 0.019676256113182147, "5": 0.00653613329954853, "6": 0.0018619227091068679, "7": 0.00046327807229537885, "8": 0.00010218456904164769, "9": 2.0222668613634104e-05} |
| Raw goal margin distribution | {"-1": 0.19234994356303434, "-10": 9.556713980647236e-06, "-11": 1.7182425389670646e-06, "-12": 2.843512975268748e-07, "-13": 4.357888859408641e-08, "-14": 6.217503413450033e-09, "-15": 8.285989571471886e-10, "-16": 1.01944363508493e-10, "-17": 9.979081443594553e-12, "-2": 0.12815178958877688, "-3": 0.06845206508600277, "-4": 0.029763894757110488, "-5": 0.010845197504605615, "-6": 0.003388812067782835, "-7": 0.0009249044144708888, "-8": 0.00022377403681795465, "-9": 4.857715939888462e-05, "0": 0.2018154847899438, "1": 0.17569843003016644, "10": 3.7897963636460695e-06, "11": 6.211871765105233e-07, "12": 9.371820415490552e-08, "13": 1.3094099067540921e-08, "14": 1.7031238601471954e-09, "15": 2.0692135417061964e-10, "16": 2.3208917079330484e-11, "17": 2.0711566802694106e-12, "2": 0.10650895718516369, "3": 0.05186552048602944, "4": 0.020559505975566765, "5": 0.006829534585044406, "6": 0.0019455027848656735, "7": 0.0004840742182312189, "8": 0.00010677154463419446, "9": 2.1130446453447615e-05} |
| Unadjusted home-win probability | 36.4% |
| Unadjusted draw probability | 20.2% |
| Unadjusted away-win probability | 43.4% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 45.6% |
| Raw p btts yes | 72.9% |
| P home draw | 58.3% |
| P draw away | 65.2% |
| P home away | 76.5% |
| Raw p home draw | 56.6% |
| Raw p draw away | 63.6% |
| Raw p home away | 79.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7368 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 2.92 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:35Z |
| Market reference home last update utc | 2026-11-01T09:33:35Z |
| Market reference draw last update utc | 2026-11-01T09:33:35Z |
| Market reference away last update utc | 2026-11-01T09:33:35Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.87 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +0.7% |
| Draw probability edge | -1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +5.7% |
| Under 2.5 probability edge | -5.7% |
| Raw edge prob home | 0.0223 |
| Raw edge prob draw | -0.0474 |
| Raw edge prob away | 0.0251 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.017130407321948392, 0.04173906467344942, 0.039592191372133496, 0.02740203314441751, 0.014223854397010861, 0.005906657592627067, 0.002044019559369623, 0.0006062915414005412, 0.00015735698445386103, 3.630262394405023e-05, 7.537590141406073e-06, 1.4227688091033194e-06, 2.461770661886942e-07, 3.931866298327691e-08, 5.8312976205793164e-09, 8.071763907796377e-10, 1.0474733201953428e-10, 1.2793475761614018e-11], [0.03832899818833746, 0.07940458953404525, 0.0747931486585205, 0.051764862400585136, 0.026870118059733366, 0.011158198222674663, 0.003861333598030082, 0.0011453383057319425, 0.0002972612508384105, 6.857886505501104e-05, 1.4239173949082774e-05, 2.6877360246563306e-06, 4.6505023515138824e-07, 7.427642935754047e-08, 1.1015836575164632e-08, 1.5248275404053816e-09, 1.9787696775063004e-10, 2.4168006400652373e-11], [0.032798429143275264, 0.06810006806807577, 0.08196129036041162, 0.048894200025763716, 0.025380013897489628, 0.010539411301910637, 0.0036472002156070753, 0.0010818226422445567, 0.00028077638738662364, 6.477576854336743e-05, 1.3449529023769355e-05, 2.5386854462982618e-06, 4.392604976626654e-07, 7.015736980237853e-08, 1.0404944434878572e-08, 1.4402669940166067e-09, 1.869035402203935e-10, 2.2827750029218226e-11], [0.020653043791908944, 0.042882349087450776, 0.04451876153911991, 0.03572013209880318, 0.015981696445714795, 0.006636626474043499, 0.002296627848905285, 0.000681219527549736, 0.00017680380359371228, 4.078905055289884e-05, 8.469116331609786e-06, 1.5986003923309866e-06, 2.7660063397099653e-07, 4.4177824020903096e-08, 6.551953208709893e-09, 9.069305474821774e-10, 1.1769243533500303e-10, 1.4374545773661227e-11], [0.009753856259560332, 0.020252136841696144, 0.021024968778516447, 0.0145515282524814, 0.008756687519732903, 0.003134293488573957, 0.0010846332456187992, 0.00032172097342517554, 8.349950272570501e-05, 1.926353035734023e-05, 3.999727312657843e-06, 7.549743563407217e-07, 1.306307608815172e-07, 2.0863953502526915e-08, 3.0943046681650655e-09, 4.2831798967138484e-10, 5.5582853000338016e-11, 6.788696847081193e-12], [0.003685179303960438, 0.0076516152754292814, 0.00794360484173218, 0.005497824586504341, 0.0028538121973141098, 0.0013738731062901573, 0.0004097936121648373, 0.00012155187049782357, 3.154758806642767e-05, 7.278102271037958e-06, 1.5111676778755811e-06, 2.852426567472395e-07, 4.935461048950004e-08, 7.882770424358386e-09, 1.1690829985415513e-09, 1.618261074437935e-10, 2.1000184345668646e-11, 2.564889665787713e-12], [0.0011602715668676533, 0.0024090962507983603, 0.002501028600260754, 0.001730979423576884, 0.000898517243425616, 0.0003731220490489253, 0.00014968934916677839, 3.827037102011194e-05, 9.932697005378133e-06, 2.2914964047380025e-06, 4.757882167427034e-07, 8.980809805534629e-08, 1.553920352891727e-08, 2.4818750017669394e-09, 3.6808351796027084e-10, 5.095063652455573e-11, 6.611867370760668e-12, 8.075505439227633e-13], [0.000313122219225085, 0.0006501422476578352, 0.0006749520095310436, 0.0004671390164343969, 0.00024248264053645168, 0.0001006943610239628, 3.484563650822095e-05, 1.1982338900742701e-05, 2.680534642084456e-06, 6.18405604418048e-07, 1.2840085593911172e-07, 2.4236490637610947e-08, 4.193561260059604e-09, 6.697830323382984e-10, 9.933461380515155e-11, 1.3750036487207419e-11, 1.7843431171408336e-12, 2.1793347839434117e-13], [7.393944323094191e-05, 0.0001535220206719919, 0.00015938049978004467, 0.0001103083609719193, 5.725889232263567e-05, 2.3777568417319157e-05, 8.228310877528527e-06, 2.440659269717628e-06, 7.343589689080353e-07, 1.4602785517656255e-07, 3.032007061654641e-08, 5.723109104335721e-09, 9.902509808822084e-10, 1.5815991793615364e-10, 2.345648308347559e-11, 3.2468792690129378e-12, 4.213477310580682e-13, 5.146195020506283e-14], [1.551979366986554e-05, 3.22240739244987e-05, 3.345376112530991e-05, 2.3153582547248887e-05, 1.2018567570718145e-05, 4.990880911224894e-06, 1.7271118294993179e-06, 5.122912295424348e-07, 1.3296013145217583e-07, 3.556068868606907e-08, 6.364143675721302e-09, 1.201273211809224e-09, 2.0785240235948232e-10, 3.3197562572188457e-11, 4.923485514209155e-12, 6.815157664719504e-13, 8.844034474079869e-14, 1.0801796904757346e-14], [2.9318261881225777e-06, 6.087412360596266e-06, 6.319711140800907e-06, 4.37391637446107e-06, 2.2704136341689835e-06, 9.428215135193217e-07, 3.262666888010416e-07, 9.677634088875344e-08, 2.5117343932516776e-08, 5.794629926470705e-09, 1.3948160682007806e-09, 2.2693112655942396e-10, 3.9265155804548846e-11, 6.2713129698343015e-12, 9.300899273827534e-13, 1.2874435152063502e-13, 1.6707162757010345e-14, 2.0405549015538788e-15], [5.034980712786196e-07, 1.0454236322244433e-06, 1.0853175346212666e-06, 7.511558725400971e-07, 3.8991018309335415e-07, 1.6191574232473575e-07, 5.6031510053118426e-08, 1.6619914638968477e-08, 4.3135347780498074e-09, 9.95142550936716e-10, 2.0662354029270218e-10, 4.521456428794621e-11, 6.7432135970873165e-12, 1.0770058598590245e-12, 1.5972927946754138e-13, 2.2109950767636088e-14, 2.8692097296802624e-15, 3.5043532301907253e-16], [7.926269631567943e-08, 1.645748029814931e-07, 1.7085506193560722e-07, 1.182499858632788e-07, 6.138123300936633e-08, 2.5489428946613534e-08, 8.820706212778406e-09, 2.6163739683763357e-09, 6.79054035483059e-10, 1.5665935244875858e-10, 3.2527510749546055e-11, 6.139777682790549e-12, 1.2315800255014117e-12, 1.6954660458465597e-13, 2.5145227148550618e-14, 3.480637589731676e-15, 4.516825633355636e-16, 5.516694138710449e-17], [1.1518018351906947e-08, 2.391510368828233e-08, 2.4827716320082307e-08, 1.7183436478889452e-08, 8.919582617386988e-09, 3.703983387310614e-09, 1.281776431512383e-09, 3.8019705086980454e-10, 9.867639136927967e-11, 2.2764874024929172e-11, 4.72671866047799e-12, 8.92198667395334e-13, 1.5437423774792358e-13, 2.8583980746542607e-14, 3.653965878304126e-15, 5.057870788952224e-16, 6.563602167929605e-17, 8.016555994822365e-18], [1.5541824734880076e-09, 3.2269817488025726e-09, 3.3501250286700217e-09, 2.3186450128691566e-09, 1.2035628483328485e-09, 4.997965697541898e-10, 1.7295635446324225e-10, 5.1301845063986096e-11, 1.3314887450911813e-11, 3.0717756422787435e-12, 6.377992354915249e-13, 1.2038872394274398e-13, 2.083046990684565e-14, 3.3269802046579505e-15, 5.720229033392559e-16, 6.824832096273791e-17, 8.856588990114934e-18, 1.081713055512311e-18], [1.9573253673428667e-10, 4.064035816018652e-10, 4.2191215087310527e-10, 2.9200835673861083e-10, 1.5157577275635756e-10, 6.294399281799473e-11, 2.1781989297195666e-11, 6.46091462541565e-12, 1.6768666109389106e-12, 3.868570447795945e-13, 8.032394163458447e-14, 1.516166263195147e-14, 2.6233732433513896e-15, 4.189973096665999e-16, 6.214092315212162e-17, 9.971894576558962e-18, 1.1153919564912185e-18, 1.3623010424178137e-19], [2.310975379538572e-11, 4.7983267723811546e-11, 4.981433384882468e-11, 3.4476849598007403e-11, 1.789625193740799e-11, 7.431672838824339e-12, 2.5717564296183867e-12, 7.62827421426903e-13, 1.979843268424409e-13, 4.5675446750089963e-14, 9.48368904843921e-15, 1.7901075436873014e-15, 3.0973649439568775e-16, 4.9470184308033576e-17, 7.336855990442791e-18, 1.01557789078295e-18, 1.5278632744329191e-19, 1.6084419182801193e-20], [2.568021609338688e-12, 5.332037264111189e-12, 5.53551054291785e-12, 3.831165644321184e-12, 1.988682445877438e-12, 8.258286355022484e-13, 2.857808933704175e-13, 8.47675539845664e-14, 2.200058183844775e-14, 5.075585629728767e-15, 1.0538545165073686e-15, 1.9892184468650939e-16, 3.4418800730268083e-17, 5.497267666536708e-18, 8.152923174726803e-19, 1.1285390543701775e-19, 1.464505854921572e-20, 2.0736403149926513e-21]] |
| Legacy trial inputs | {"lambda_home": 1.8890883799668332, "lambda_away": 2.076321026552532, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3528 |
| Legacy p draw | 0.2245 |
| Legacy p away | 0.4227 |
| Legacy p over 1 5 | 0.9028 |
| Legacy p under 3 5 | 0.4399 |
| Legacy p btts yes | 0.7444 |
| Legacy p over 2 5 | 0.7510 |
| Legacy goal margin distribution | {"-1": 0.18499330043569587, "-10": 1.071202744832243e-05, "-11": 1.964978492990357e-06, "-12": 3.318235182712615e-07, "-13": 5.189924768464023e-08, "-14": 7.557403246978754e-09, "-15": 1.027881108559486e-09, "-16": 1.2891533842018665e-10, "-17": 1.2793475761614018e-11, "-2": 0.12459046192468982, "-3": 0.06746388475111517, "-4": 0.02980175101694766, "-5": 0.011047486499405023, "-6": 0.0035152245061521106, "-7": 0.0009776045906277348, "-8": 0.0002411228747219823, "-9": 5.337916979634492e-05, "0": 0.224509422990248, "1": 0.16876371555783798, "10": 4.1665574821266515e-06, "11": 6.953785288195527e-07, "12": 1.0683865546994329e-07, "13": 1.5203377783626508e-08, "14": 2.0142315545830186e-09, "15": 2.4925131500101604e-10, "16": 2.8441791059496908e-11, "17": 2.568021609338688e-12, "2": 0.10321154994823092, "3": 0.05084785347108222, "4": 0.02043623251399425, "5": 0.006892556064060336, "6": 0.001995389440843967, "7": 0.0005048886518107604, "8": 0.0001132996490055073, "9": 2.2820215496950794e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3639 |
| Legacy raw p draw | 0.1998 |
| Legacy raw p away | 0.4363 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8891 |
| Legacy lambda away | 2.0763 |
| Legacy model home team | Club Atlético de Madrid |
| Legacy model away team | FC Bayern München |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,542.1549 |
| Elo away rating | 1,571.2653 |
| Elo rating diff | 30.8896 |
| Elo home expectancy | 0.5443 |

</details>


---

## 2026-11-03 — Barcelona vs Aston Villa

The model's most likely 1X2 outcome is **Barcelona win** at **67.0%**. Expected goals are 1.89 for Barcelona and 1.89 for Aston Villa (3.78 combined). The most likely exact score is 2-1 at 13.0%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 74.2%; Under 3.5 goals: 47.8%; Double Chance 1X: 81.9%; Double Chance X2: 33.0%; Double Chance 12 (either team wins): 85.0%; Under 4.5 goals: 66.1%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 67.0% | 1.49 |
| Draw | 15.0% | 6.69 |
| Aston Villa win | 18.1% | 5.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.89 |
| Aston Villa expected goals | 1.89 |
| Expected total goals | 3.78 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 74.2% |
| Under 2.5 | 25.8% |
| Over 3.5 | 52.2% |
| Under 3.5 | 47.8% |
| Over 4.5 | 33.9% |
| Under 4.5 | 66.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 12.96% |
| 2 | 3-1 | 8.18% |
| 3 | 1-0 | 7.93% |
| 4 | 3-2 | 7.72% |
| 5 | 2-0 | 6.87% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | bd680c6ad693dae859030f86e1be2769 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | FC Barcelona |
| Matched away-team name | Aston Villa FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8945 |
| Dc lambda away | 1.8870 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 73.36 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.74 |
| Fair Over 2.5 odds | 1.35 |
| Fair Under 2.5 odds | 3.88 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.09 |
| Fair Over 4.5 odds | 2.95 |
| Fair Under 4.5 odds | 1.51 |
| Goal margin distribution | {"-1": 0.08506803178762994, "-10": 2.26420584243664e-06, "-11": 3.7839288025135354e-07, "-12": 5.819388585389657e-08, "-13": 8.286248964163823e-09, "-14": 1.0968474982501536e-09, "-15": 1.3345475040221265e-10, "-16": 1.2864943891161204e-11, "-2": 0.053254784366879505, "-3": 0.026657163770277846, "-4": 0.010831791739703165, "-5": 0.0036817832540572966, "-6": 0.0010719254672550294, "-7": 0.0002723675441249719, "-8": 6.131347511541915e-05, "-9": 1.2378823651853575e-05, "0": 0.14955045336225337, "1": 0.3136982882626188, "10": 8.65266820108936e-06, "11": 1.4517567857817664e-06, "12": 2.241532453443814e-07, "13": 3.2043682186918675e-08, "14": 4.2584097913841594e-09, "15": 5.201780291148832e-10, "16": 5.0343409954368906e-11, "2": 0.19717809034848324, "3": 0.09909020583083955, "4": 0.04042349470043586, "5": 0.013794581773806875, "6": 0.004032103522292753, "7": 0.0010285826734911113, "8": 0.00023246444934186148, "9": 4.711907487117411e-05} |
| Raw goal margin distribution | {"-1": 0.18613727238264216, "-10": 4.954306462339991e-06, "-11": 8.279610699684792e-07, "-12": 1.273339814565483e-07, "-13": 1.8131132789382715e-08, "-14": 2.4000108766322343e-09, "-15": 2.9201220134478757e-10, "-16": 2.8149770424154754e-11, "-2": 0.11652673860050643, "-3": 0.05832851247862578, "-4": 0.02370103230410421, "-5": 0.008056106130740035, "-6": 0.002345479006384559, "-7": 0.0005959671416349069, "-8": 0.00013415995149360785, "-9": 2.7086091231239924e-05, "0": 0.205324459067912, "1": 0.18685839475664193, "10": 5.154072403046848e-06, "11": 8.64757484239574e-07, "12": 1.3351974547428204e-07, "13": 1.9087228842405918e-08, "14": 2.536576218636736e-09, "15": 3.098506913965313e-10, "16": 2.9987695574460985e-11, "2": 0.11745164963365266, "3": 0.05902434756722361, "4": 0.024078771267803434, "5": 0.008216918941026751, "6": 0.002401773997049912, "7": 0.0006126884156987832, "8": 0.00013847042036022202, "9": 2.806707917218431e-05} |
| Unadjusted home-win probability | 39.9% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 39.6% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 47.7% |
| Raw p btts yes | 71.7% |
| P home draw | 81.9% |
| P draw away | 33.0% |
| P home away | 85.0% |
| Raw p home draw | 60.4% |
| Raw p draw away | 60.1% |
| Raw p home away | 79.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7420 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.4, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.27 |
| Reference draw odds | 7.80 |
| Reference away odds | 11.00 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.61 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | -11.6% |
| Draw probability edge | +2.4% |
| Away probability edge | +9.2% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.3867 |
| Raw edge prob draw | 0.0797 |
| Raw edge prob away | 0.3071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.013447335925080864, 0.02704317757820591, 0.02458442608823856, 0.016313988400089977, 0.008119354196931937, 0.003232755152620932, 0.0010726125936578177, 0.0003050465947353015, 7.590974348155736e-05, 1.6790991583683863e-05, 3.3427020944769168e-06, 6.049595233974931e-07, 1.0036132846672653e-07, 1.5368956401790687e-08, 2.185433884853849e-09, 2.9004657598028005e-10, 3.608852149205633e-11, 4.226116821835304e-12], [0.06539166191741529, 0.059541875711096565, 0.046679244554765444, 0.0309758971577428, 0.01541648028817183, 0.006138136713594623, 0.0020366042059378362, 0.0005792018306687181, 0.00014413228388358967, 3.188159852251995e-05, 6.346896526352646e-06, 1.1486562036083397e-06, 1.905592987416014e-07, 2.9181534352511578e-08, 4.149553965718511e-09, 5.507208101527787e-10, 6.85224423910196e-11, 8.024264627346138e-12], [0.0564606224044289, 0.11240017590750787, 0.059227580180004825, 0.029407468645796228, 0.014635884745944346, 0.005827339302859374, 0.0019334831215709624, 0.0005498746198774919, 0.00013683431338789112, 3.026731087575667e-05, 6.025528805391645e-06, 1.0904953332067765e-06, 1.8091055036666808e-07, 2.7703961313456376e-08, 3.939446128694425e-09, 5.228357026975448e-10, 6.505288824680889e-11, 7.617965324218832e-12], [0.035734536320827855, 0.07113928251912453, 0.07081101419505667, 0.024875198441660314, 0.009263209167180077, 0.003688185838268077, 0.0012237223022193505, 0.00034802157218819977, 8.66039114246742e-05, 1.915650720383615e-05, 3.813622110045532e-06, 6.901862472049911e-07, 1.1450023675954991e-07, 1.753413564404596e-08, 2.493317905024245e-09, 3.3090835014254833e-10, 4.117267395989595e-11, 4.821492342382522e-12], [0.016962579825781338, 0.03376861385986791, 0.03361279044015752, 0.02230512403939034, 0.00587667462173296, 0.0017507194197864764, 0.0005808802736272293, 0.00016519995240278241, 4.110941156691914e-05, 9.093269875138481e-06, 1.8102618958373927e-06, 3.2761973480673086e-07, 5.4351325246459306e-08, 8.323157543389023e-09, 1.1835358269465813e-09, 1.5707659542343098e-10, 1.954397175929059e-11, 2.288680843730121e-12], [0.0064414797329451065, 0.01282351175482052, 0.012764338361958595, 0.008470292014318724, 0.004215603157797911, 0.0008885394422906045, 0.00022058723073187085, 6.273409800958756e-05, 1.5611153737306648e-05, 3.453137094033203e-06, 6.874405563967466e-07, 1.2441243628890037e-07, 2.0639723652274618e-08, 3.16068965808861e-09, 4.4944354695997207e-10, 5.964928190947761e-11, 7.421754195513298e-12, 8.691184608405055e-13], [0.0020384409671221344, 0.00405806938578179, 0.004039343646794142, 0.002680469544469169, 0.0013340503322605002, 0.0005311577720184229, 9.329519660877002e-05, 1.9852543316119477e-05, 4.940233710495302e-06, 1.092763838340613e-06, 2.1754426788822188e-07, 3.9370985777333995e-08, 6.5315517531932294e-09, 1.0002172715773382e-09, 1.4222883196327453e-10, 1.8876336640758722e-11, 2.3486541023591567e-12, 2.750372196000696e-13], [0.0005529219658542213, 0.0011007410754342738, 0.001095661766010984, 0.0007270705965219456, 0.0003618577845319361, 0.000144075204639261, 4.780345916535281e-05, 7.196946567382426e-06, 1.3400259213014008e-06, 2.964094322352256e-07, 5.900833342791919e-08, 1.067928049167675e-08, 1.7716669227624504e-09, 2.7130640965417347e-10, 3.857921158310963e-11, 5.1201586564802536e-12, 6.370664955882425e-13, 7.46031514265765e-14], [0.00013123135136027556, 0.0002612515829495688, 0.00026004605182445694, 0.00017256405570447665, 8.588388415894738e-05, 3.419503107117176e-05, 1.134574665752919e-05, 3.2266835230845915e-06, 4.2506307382528686e-07, 7.03502713770215e-08, 1.4005128780333548e-08, 2.53463688734635e-09, 4.2049015736827474e-10, 6.439228131697831e-11, 9.156449522933745e-12, 1.2152263450609066e-12, 1.5120234370367222e-13, 1.7706426913822633e-14], [2.7685912127241196e-05, 5.511631400325495e-05, 5.486198279009178e-05, 3.640588344959083e-05, 1.811894524687905e-05, 7.214134546444372e-06, 2.393615105859366e-06, 6.807342571462601e-07, 1.6939826154729108e-07, 1.983596958543641e-08, 2.954665639908846e-09, 5.347329994711702e-10, 8.871091722059235e-11, 1.358485623850786e-11, 1.9317385233160105e-12, 2.5637661622258627e-13, 3.189919754556432e-14, 3.735529464126997e-15], [5.2568136358794724e-06, 1.0465112714370107e-05, 1.0416822024750008e-05, 6.912502779915386e-06, 3.440302707160201e-06, 1.3697710474744934e-06, 4.5448343799184176e-07, 1.292532140147816e-07, 3.2164195533940376e-08, 7.114616803277268e-09, 7.497880386110087e-10, 1.0153148324157756e-10, 1.6843828628558676e-11, 2.5794005697859777e-12, 3.667854381553717e-13, 4.8679056911166544e-14, 6.0568037585491336e-15, 7.092770552042166e-16], [9.073892715926957e-07, 1.8064043469631326e-06, 1.7980687930108267e-06, 1.193181135343889e-06, 5.938376331627763e-07, 2.364389607676671e-07, 7.844930870967946e-08, 2.231065962000113e-08, 5.551927075692199e-09, 1.2280684471529415e-09, 2.444803185088918e-10, 2.342276772176426e-11, 2.907447447971594e-12, 4.4523556783315753e-13, 6.3311578954792e-14, 8.402590818697139e-15, 1.045477190429318e-15, 1.2242975213852956e-16], [1.4357411192971235e-07, 2.8582319410276293e-07, 2.845042786233636e-07, 1.8879429947148584e-07, 9.396155925685096e-08, 3.74111915145495e-08, 1.2412853206565005e-08, 3.5301642214540163e-09, 8.784686179856404e-10, 1.9431443836601756e-10, 3.868355700591018e-11, 7.000918881847662e-12, 6.148381309022581e-13, 7.044859714834804e-14, 1.0017645136300838e-14, 1.329522568175918e-15, 1.654234448851163e-16, 1.9371777347786837e-17], [2.0969908280224948e-08, 4.174628757327867e-08, 4.15536516150224e-08, 2.7574603043232012e-08, 1.3723680773645956e-08, 5.464141440053584e-09, 1.8129758195195672e-09, 5.15602840533417e-10, 1.2830590486419424e-10, 2.8380854286973662e-11, 5.649978477762853e-12, 1.0225285384423038e-12, 1.69635022748094e-13, 1.3751787828321878e-14, 1.4631405123711357e-15, 1.9418519074515987e-16, 2.4161141726845332e-17, 2.8293707601471996e-18], [2.84401733900934e-09, 5.661787553436122e-09, 5.635661544772834e-09, 3.7397707287640225e-09, 1.8612568807506265e-09, 7.410672851138077e-10, 2.4588255690086435e-10, 6.992798437284228e-11, 1.740132637943693e-11, 3.849117535920133e-12, 7.662711987605689e-13, 1.386791422308784e-13, 2.3006535820367827e-14, 3.5231343723862302e-15, 2.6520894377189204e-16, 2.6336121363910247e-17, 3.276824346733532e-18, 3.8372983767091393e-19], [3.6000184401056553e-10, 7.166812704253975e-10, 7.13374183943746e-10, 4.733882385543933e-10, 2.3560190722359663e-10, 9.380589404908621e-11, 3.1124343962395676e-11, 8.851634966098407e-12, 2.2026973953010834e-12, 4.872295930612473e-13, 9.699625975630715e-14, 1.7554304695733698e-14, 2.91221688631215e-15, 4.459659416836924e-16, 6.341543660913372e-17, 4.455441255427908e-18, 4.14787487805437e-19, 4.8573349841644645e-20], [4.272169618791519e-11, 8.504911852002718e-11, 8.465666401934376e-11, 5.617734698564369e-11, 2.7959059846939213e-11, 1.1132017718451484e-11, 3.693549877401784e-12, 1.0504303410648219e-12, 2.613957969426491e-13, 5.781991118888064e-14, 1.1510620874907082e-14, 2.0831828627500535e-15, 3.4559502158186904e-16, 5.2923121888811904e-17, 7.52555872008226e-18, 9.987776588557701e-19, 6.578635597571847e-20, 5.764236848473362e-21], [4.771592095103648e-12, 9.499147689283232e-12, 9.45531439238154e-12, 6.274455574552253e-12, 3.122751221425586e-12, 1.2433365827582082e-12, 4.125330913913195e-13, 1.1732270857962227e-13, 2.919533234117428e-14, 6.457913795250959e-15, 1.285622821127083e-15, 2.326709790929445e-16, 3.859955526657411e-17, 5.910990728038904e-18, 8.405306835672993e-19, 1.1155361343331738e-19, 1.38798569240084e-20, 8.604448946039452e-22]] |
| Legacy trial inputs | {"lambda_home": 1.8987323270115823, "lambda_away": 1.9907711095067728, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5832 |
| Legacy p draw | 0.1640 |
| Legacy p away | 0.2528 |
| Legacy p over 1 5 | 0.8941 |
| Legacy p under 3 5 | 0.4576 |
| Legacy p btts yes | 0.7220 |
| Legacy p over 2 5 | 0.7535 |
| Legacy goal margin distribution | {"-1": 0.1143856725751513, "-10": 4.691048592462081e-06, "-11": 8.258808747444138e-07, "-12": 1.3383363038829522e-07, "-13": 2.008480742501037e-08, "-14": 2.8060290755958192e-09, "-15": 3.6618698369551846e-10, "-16": 4.411278611940247e-11, "-17": 4.226116821835304e-12, "-2": 0.07453325940213439, "-3": 0.03896349579764426, "-4": 0.016583786810945425, "-5": 0.005915659809318932, "-6": 0.0018097467315275576, "-7": 0.00048360911110747025, "-8": 0.00011456471657550698, "-9": 2.4351675812202747e-05, "0": 0.16395814213792537, "1": 0.27570594389640773, "10": 7.3772557381565866e-06, "11": 1.2387530344972784e-06, "12": 1.9145865168274797e-07, "13": 2.740437011581189e-08, "14": 3.6516297290286335e-09, "15": 4.5450627692297424e-10, "16": 5.222084387719842e-11, "17": 4.771592095103648e-12, "2": 0.17117317282783764, "3": 0.08534653952307965, "4": 0.0346460815443546, "5": 0.011787345768463782, "6": 0.0034393236658547305, "7": 0.0008765811683640815, "8": 0.00019805734922636686, "9": 4.015238488612202e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3809 |
| Legacy raw p draw | 0.2023 |
| Legacy raw p away | 0.4168 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8987 |
| Legacy lambda away | 1.9908 |
| Legacy model home team | FC Barcelona |
| Legacy model away team | Aston Villa FC |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,563.5732 |
| Elo away rating | 1,514.0790 |
| Elo rating diff | 109.4942 |
| Elo home expectancy | 0.6526 |

</details>


---

## 2026-11-03 — Bodø/Glimt vs Lille

The model's most likely 1X2 outcome is **Bodø/Glimt win** at **54.7%**. Expected goals are 2.82 for Bodø/Glimt and 1.81 for Lille (4.63 combined). The most likely exact score is 2-2 at 8.1%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 83.1%; Under 3.5 goals: 32.2%; Double Chance 1X: 76.1%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 51.9%; BTTS Yes (both teams score): 79.4%; BTTS No (at least one team does not score): 20.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bodø/Glimt win | 54.7% | 1.83 |
| Draw | 21.4% | 4.68 |
| Lille win | 23.9% | 4.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bodø/Glimt expected goals | 2.82 |
| Lille expected goals | 1.81 |
| Expected total goals | 4.63 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 94.3% |
| Under 1.5 | 5.7% |
| Over 2.5 | 83.1% |
| Under 2.5 | 16.9% |
| Over 3.5 | 67.8% |
| Under 3.5 | 32.2% |
| Over 4.5 | 48.1% |
| Under 4.5 | 51.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 8.07% |
| 2 | 2-1 | 6.47% |
| 3 | 3-1 | 6.09% |
| 4 | 1-1 | 6.01% |
| 5 | 3-2 | 5.51% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | 1a5a84045050d0d7baf1301909d3b465 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | FK Bodø/Glimt |
| Matched away-team name | Lille OSC |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8234 |
| Dc lambda away | 1.8090 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 79.4% |
| P btts no | 20.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 108.51 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 17.55 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 5.93 |
| Fair Over 3.5 odds | 1.47 |
| Fair Under 3.5 odds | 3.11 |
| Fair Over 4.5 odds | 2.08 |
| Fair Under 4.5 odds | 1.93 |
| Goal margin distribution | {"-1": 0.12483464668184079, "-10": 1.5909817303399144e-06, "-11": 2.5218810573570454e-07, "-12": 3.684335220126512e-08, "-13": 4.990124581541867e-09, "-14": 6.297924113144664e-10, "-15": 7.43977207832745e-11, "-16": 8.257562419301574e-12, "-17": 8.623953965812568e-13, "-18": 8.319115422844684e-14, "-19": 6.242577883907666e-15, "-2": 0.06783654996581963, "-3": 0.03033510533504594, "-4": 0.011231618308958706, "-5": 0.0035240768448320417, "-6": 0.0009554668962879314, "-7": 0.00022748086468634971, "-8": 4.8196419771305996e-05, "-9": 9.188394727351564e-06, "0": 0.21386470085639886, "1": 0.17798999816956768, "10": 0.00012555580808591252, "11": 3.106190619084521e-05, "12": 7.082629617331193e-06, "13": 1.4971960439041672e-06, "14": 2.949148186849904e-07, "15": 5.437392603248139e-08, "16": 9.419217289721597e-09, "17": 1.5353283499423356e-09, "18": 2.3115531239978364e-10, "19": 2.707214001875009e-11, "2": 0.15204783950801443, "3": 0.10611918297205641, "4": 0.06132289024930524, "5": 0.030030152572946906, "6": 0.012707487841230748, "7": 0.004721943841395538, "8": 0.0015614303432809765, "9": 0.00046460017566492083} |
| Raw goal margin distribution | {"-1": 0.12456704713854194, "-10": 1.587571250991815e-06, "-11": 2.516475072423049e-07, "-12": 3.676437361251016e-08, "-13": 4.979427590806369e-09, "-14": 6.284423681484026e-10, "-15": 7.42382394482985e-11, "-16": 8.239861244260012e-12, "-17": 8.605467382127484e-13, "-18": 8.30128230081505e-14, "-19": 6.229196094195083e-15, "-2": 0.06769113336656343, "-3": 0.030270078032535373, "-4": 0.01120754185254317, "-5": 0.003516522520938047, "-6": 0.0009534187268743917, "-7": 0.00022699322942548795, "-8": 4.8093104383613103e-05, "-9": 9.168698190388108e-06, "0": 0.16816392457639254, "1": 0.1930238213390828, "10": 0.00013616080744588172, "11": 3.368553229221946e-05, "12": 7.680859868115773e-06, "13": 1.6236558495428486e-06, "14": 3.198246297967129e-07, "15": 5.896658852706633e-08, "16": 1.0214806078896184e-08, "17": 1.6650089789526626e-09, "18": 2.506797133607953e-10, "19": 2.9358772807377364e-11, "2": 0.16489047311651978, "3": 0.1150824789330768, "4": 0.06650249302323945, "5": 0.0325666321963982, "6": 0.013780818517664734, "7": 0.005120780121287463, "8": 0.0016933156621966939, "9": 0.0005038423631883898} |
| Unadjusted home-win probability | 59.3% |
| Unadjusted draw probability | 16.8% |
| Unadjusted away-win probability | 23.8% |
| Raw p over 1 5 | 94.3% |
| Raw p under 3 5 | 32.0% |
| Raw p btts yes | 78.4% |
| P home draw | 76.1% |
| P draw away | 45.3% |
| P home away | 78.6% |
| Raw p home draw | 76.2% |
| Raw p draw away | 40.7% |
| Raw p home away | 83.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8313 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.01, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 1.88 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:35Z |
| Market reference home last update utc | 2026-11-01T09:33:35Z |
| Market reference draw last update utc | 2026-11-01T09:33:35Z |
| Market reference away last update utc | 2026-11-01T09:33:35Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +2.0% |
| Draw probability edge | -2.0% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | +18.0% |
| Under 2.5 probability edge | -18.0% |
| Raw edge prob home | 0.0660 |
| Raw edge prob draw | -0.0653 |
| Raw edge prob away | -0.0007 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.007526841379696619, 0.017827927313636954, 0.011926513950357282, 0.006207644652595301, 0.0024232679574240096, 0.0007567736778905813, 0.00019694699114662984, 4.393249748986441e-05, 8.574928126104168e-06, 1.4877246598059778e-06, 2.3230424415934373e-07, 3.297608104780872e-08, 4.290939373232508e-09, 5.153990441103149e-10, 5.748442024889068e-11, 5.984026102696621e-12, 5.839935886548791e-13, 5.364061401620605e-14, 4.6532439144361995e-15, 3.824166561676405e-16, 2.985667128639009e-17, 2.2200189142408742e-18], [0.023178216244425183, 0.050470153981256, 0.03984805882737496, 0.02074056093219485, 0.008096458405520247, 0.002528480842022527, 0.0006580259178626375, 0.00014678427843176894, 2.8649967780339946e-05, 4.970684645122901e-06, 7.761591715434247e-07, 1.1017744354795328e-07, 1.4336595360637317e-08, 1.7220163003846908e-09, 1.9206304283631177e-10, 1.9993421812721648e-11, 1.951199736351485e-12, 1.7922037837303333e-13, 1.5547102700116617e-14, 1.2777045727666015e-15, 9.975508340172011e-17, 7.41737649918276e-18], [0.03591660060445858, 0.056082815467211, 0.06929138866976679, 0.034648477148433506, 0.013525668614461325, 0.004223994276793091, 0.0010992757646563721, 0.0002452128336171398, 4.786166377976622e-05, 8.303857060648185e-06, 1.2966251687544658e-06, 1.8405869771431006e-07, 2.3950229618346806e-08, 2.876741985338144e-09, 3.2085400064772147e-10, 3.3400331893712636e-11, 3.259608054865156e-12, 2.993994812817492e-13, 2.597246209446341e-14, 2.134489893339046e-15, 1.6664745659406868e-16, 1.2391217430109528e-17], [0.04000070262841898, 0.06246003202736065, 0.04876483842170341, 0.0401665922600024, 0.015063681946293232, 0.004704307649571091, 0.0012242751883147012, 0.00027309615813066597, 5.330404737463212e-05, 9.248094512336785e-06, 1.4440653325479944e-06, 2.049881422388906e-07, 2.6673627145184698e-08, 3.2038583484405284e-09, 3.573385356924573e-10, 3.7198307225240185e-11, 3.630260389165965e-12, 3.334444077752575e-13, 2.892580910453833e-14, 2.377204246780025e-15, 1.8559705659266097e-16, 1.3800231516463838e-17], [0.03341190808370752, 0.05217180479027216, 0.040732441982287294, 0.021200874514628758, 0.013097042506638885, 0.0039294283464231215, 0.0010226162885467115, 0.0002281125863772387, 4.4523966189170724e-05, 7.724776403705125e-06, 1.2062032661317066e-06, 1.712231165127031e-07, 2.2280028096327016e-08, 2.6761285081842808e-09, 2.9847881474063305e-10, 3.1071114760774946e-11, 3.0322948966542097e-12, 2.7852045518065284e-13, 2.416123746689057e-14, 1.9856383655916965e-15, 1.55026071743924e-16, 1.1527099192362308e-17], [0.02232671985118565, 0.034862578538313115, 0.027218494038556827, 0.014166984558390822, 0.005530342288409875, 0.0027331373704453064, 0.0006833392254175077, 0.00015243085781914604, 2.9752090700082233e-05, 5.161899710919949e-06, 8.060168949057943e-07, 1.144158108195611e-07, 1.4888103497022445e-08, 1.7882597826592552e-09, 1.9945143095487014e-10, 2.0762539900142214e-11, 2.026259574705082e-12, 1.8611472772114492e-13, 1.614517730713743e-14, 1.3268560240039013e-15, 1.0359251751755473e-16, 7.70271227012617e-18], [0.01243275346782723, 0.019413413484318607, 0.015156764110556591, 0.007888961189596094, 0.0030796007081554393, 0.0009617429006170125, 0.0003960839018267187, 8.488193916466536e-05, 1.656761097429698e-05, 2.874431486544956e-06, 4.4883482267258296e-07, 6.371305674199252e-08, 8.290520130844336e-09, 9.958020328298312e-10, 1.1106559702434656e-10, 1.1561731488769769e-11, 1.1283334910835513e-12, 1.036389824350264e-13, 8.990528411334847e-15, 7.388668798505086e-16, 5.768604792785698e-17, 4.289296561536819e-18], [0.00593421027701522, 0.00926611133315768, 0.0072343930557226006, 0.00376543737374186, 0.0014699075485354355, 0.0004590442993546548, 0.00011946424169100616, 4.217152862851104e-05, 7.907796737358221e-06, 1.3719793376561027e-06, 2.1423092030887187e-07, 3.041053432586571e-08, 3.9571032989248126e-09, 4.753008794377833e-10, 5.3012119076458425e-11, 5.518467489787556e-12, 5.385587525736272e-13, 4.946736185647335e-14, 4.291220463142057e-15, 3.5266455199174127e-16, 2.7533815364369655e-17, 2.0473009299593357e-18], [0.0024783725696878077, 0.003869912774193461, 0.0030213828750033805, 0.0015726029689418078, 0.0006138944152986122, 0.00019171595657785907, 4.989322687339361e-05, 1.112956360295281e-05, 3.437697050837112e-06, 5.729955289578308e-07, 8.947172609116509e-08, 1.2700701624055674e-08, 1.6526506162854052e-09, 1.9850537931048658e-10, 2.2140061717900822e-11, 2.304741122231104e-12, 2.2492449327480032e-13, 2.0659623942677165e-14, 1.792191814895306e-15, 1.472873577370419e-16, 1.1499264359102764e-17, 8.550378617961036e-19], [0.000920063355051167, 0.001436654429736655, 0.0011216488186116106, 0.000583808254442667, 0.00022790026095953936, 7.117203780547338e-05, 1.852220698086812e-05, 4.131704713822749e-06, 8.064433616024139e-07, 2.2141692480794623e-07, 3.3215206420730334e-08, 4.7149691255679315e-09, 6.135248950638871e-10, 7.369252206786531e-11, 8.219207924730103e-12, 8.556049543880543e-13, 8.350027209253071e-14, 7.669614791285946e-15, 6.653277373528733e-16, 5.467850240661534e-17, 4.268951277244458e-18, 3.174216070019673e-19], [0.00030740532270867387, 0.000480005225911298, 0.0003747576894114316, 0.00019505805102623078, 7.614448818229707e-05, 2.3779518148735263e-05, 6.188514065875353e-06, 1.380457132562352e-06, 2.694433817613258e-07, 4.6747629551265004e-08, 1.1551517667727608e-08, 1.5753334785581574e-09, 2.0498677327109823e-10, 2.4621645241189272e-11, 2.7461459590147836e-12, 2.8586891942911145e-13, 2.7898544103453605e-14, 2.5625196319609514e-15, 2.2229478729387896e-16, 1.8268810061017843e-17, 1.4263130226895712e-18, 1.0605475264224505e-19], [9.337107247790734e-05, 0.00014579644341686435, 0.00011382863208536282, 5.924679266868023e-05, 2.312807228650439e-05, 7.222773805577387e-06, 1.8796948285862991e-06, 4.192990604111181e-07, 8.184053973252602e-08, 1.419909150739753e-08, 2.2171503299579072e-09, 4.98060279971096e-10, 6.226253564986829e-11, 7.478560885294449e-12, 8.341124061052141e-13, 8.682962077560496e-14, 8.473883797972895e-15, 7.783378770856112e-16, 6.751965942876015e-17, 5.5489552791803e-18, 4.3322729562474586e-19, 3.221299458425476e-20], [2.599709077020573e-05, 4.059376499480833e-05, 3.169304156029388e-05, 1.6495946827810925e-05, 6.439495430604589e-06, 2.0110201291806767e-06, 5.233590638107611e-07, 1.1674446318423738e-07, 2.27866713281303e-08, 3.953420058012211e-09, 6.173160150082399e-10, 8.762931997513934e-11, 1.8044616158802815e-11, 2.082238331486576e-12, 2.3223997924199434e-13, 2.4175769571245426e-14, 2.3593637775147287e-15, 2.167108067144841e-16, 1.8799341898511254e-17, 1.5449827258522206e-18, 1.2062246935368702e-19, 8.968989237915902e-21], [6.68151653639896e-06, 1.0433010158134653e-05, 8.145433777404444e-06, 4.2396259830693525e-06, 1.655015770263036e-06, 5.168526111987544e-07, 1.345085982979859e-07, 3.0004513512429797e-08, 5.856406112289995e-09, 1.0160691335206232e-09, 1.5865648964031457e-10, 2.252162581046586e-11, 2.930576583652567e-12, 5.570435830345581e-13, 5.968803492030338e-14, 6.2134184781772345e-15, 6.063804690374064e-16, 5.569687975773937e-17, 4.831621925645444e-18, 3.9707626220480606e-19, 3.100120051015842e-20, 2.305121385989805e-21], [1.594559250247679e-06, 2.4898618098081824e-06, 1.9439264583546635e-06, 1.0117964674734103e-06, 3.9497331053542915e-07, 1.2334806143364303e-07, 3.210078557547039e-08, 7.1606459865490614e-09, 1.3976447545532879e-09, 2.4248722979583613e-10, 3.7863735244773855e-11, 5.37483766912148e-12, 6.993888250617081e-13, 8.400592517034114e-14, 1.482727479009433e-14, 1.4828465747354348e-15, 1.4471409010299983e-16, 1.3292188134806547e-17, 1.1530776573352196e-18, 9.47631609535299e-20, 7.39850762517135e-21, 5.501225072107368e-22], [3.5517554177793915e-07, 5.545971509766472e-07, 4.3299434180030917e-07, 2.253697116918385e-07, 8.797720093214296e-08, 2.7474811324914866e-08, 7.15019771544657e-09, 1.5949776199018924e-09, 3.113143853603764e-10, 5.4012124794729355e-11, 8.433849464803592e-12, 1.1972028513849051e-12, 1.557833644727496e-13, 1.8711659651592407e-14, 2.0869827355289468e-15, 3.438009324125937e-16, 3.223392630110848e-17, 2.9607304472761984e-18, 2.5683898644246674e-19, 2.1107749384058376e-20, 1.6479594306139979e-21, 1.22535465215521e-22], [7.41680256575944e-08, 1.158113971400145e-07, 9.041820642119796e-08, 4.7061873899119806e-08, 1.8371465735943324e-08, 5.73731091134052e-09, 1.4931097027724819e-09, 3.3306443468489996e-10, 6.500890575236333e-11, 1.1278852810482287e-11, 1.7611628333600935e-12, 2.500008062333757e-13, 3.253080016547167e-14, 3.907382941371442e-15, 4.358053155936135e-16, 4.5366559720265216e-17, 7.006406276145649e-18, 6.182619745705738e-19, 5.3633311688577003e-20, 4.4077362141948935e-21, 3.4412813652824956e-22, 2.5587948659348022e-23], [1.4576774866367215e-08, 2.276124580776915e-08, 1.7770539624544592e-08, 9.249408145012272e-09, 3.610676131980928e-09, 1.1275949272137524e-09, 2.9345157559650304e-10, 6.54595459074153e-11, 1.277666723711761e-11, 2.2167139641590125e-12, 3.461339829028441e-13, 4.9134454322650094e-14, 6.393511840587965e-15, 7.679460380407626e-16, 8.565194926856926e-17, 8.916215871201312e-18, 8.701521040320953e-19, 1.264811210098739e-19, 1.0540940019508746e-20, 8.662840610221072e-22, 6.763397470647292e-23, 5.02898336031528e-24], [2.7057183720897908e-09, 4.2249071909471625e-09, 3.2985400395405027e-09, 1.7168608130636265e-09, 6.702081108838322e-10, 2.0930242380822683e-10, 5.447002692221946e-11, 1.2150499518175567e-11, 2.37158518221406e-12, 4.114630124618085e-13, 6.424885376433347e-14, 9.120261304861114e-15, 1.1867537646593077e-15, 1.425449540758594e-16, 1.5898582153174643e-17, 1.6550141792949483e-18, 1.6151628573371666e-19, 1.4835492903833198e-20, 2.036614952257689e-21, 1.6079830558158397e-22, 1.2554113623788604e-23, 9.334721017290436e-25], [4.75798029367795e-10, 7.429459534481725e-10, 5.800451616817633e-10, 3.019083582315105e-10, 1.1785546556293914e-10, 3.680563425118828e-11, 9.578502972275603e-12, 2.1366539053793393e-12, 4.1704102238245313e-13, 7.235538351164662e-14, 1.1298100469561748e-14, 1.6037893673393253e-15, 2.086895326558297e-16, 2.5066396024517966e-17, 2.795750709405857e-18, 2.9103268588744434e-19, 2.840248684254336e-20, 2.6088074653874203e-21, 2.2631018836924843e-22, 2.943269011913268e-23, 2.2076290660082717e-24, 1.6415019059409843e-25], [7.948520390415103e-11, 1.2411402938775807e-10, 9.690037600860201e-11, 5.043578563426343e-11, 1.968853406966829e-11, 6.148624337861375e-12, 1.60015219663576e-12, 3.569421495236918e-13, 6.966945774136619e-14, 1.2087444791707148e-14, 1.8874223181334685e-15, 2.6792360836731136e-16, 3.486296502289248e-17, 4.187507043268704e-18, 4.670486245972265e-19, 4.8618932725033306e-20, 4.744823052470868e-21, 4.358185207461182e-22, 3.780661196099965e-23, 3.1070535723044655e-24, 3.838823976699362e-25, 2.7422373706788426e-26], [1.2646217511920054e-11, 1.9746731905111925e-11, 1.5416998029838656e-11, 8.024410634771718e-12, 3.1324758836389015e-12, 9.782555363315813e-13, 2.545866618802961e-13, 5.6790041923930454e-14, 1.1084517284465654e-14, 1.923130953826122e-15, 3.002917775835472e-16, 4.262705587416322e-17, 5.546751057235879e-18, 6.662387752786234e-19, 7.430815051342108e-20, 7.73534655807896e-21, 7.549086047445544e-22, 6.93393932249927e-23, 6.015089787328219e-24, 4.943369755197732e-25, 3.859470121074459e-26, 4.5413799810979615e-27]] |
| Legacy trial inputs | {"lambda_home": 3.3411321190112924, "lambda_away": 1.5614733722948446, "rho": 0.05, "max_goals": 21, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6235 |
| Legacy p draw | 0.1837 |
| Legacy p away | 0.1928 |
| Legacy p over 1 5 | 0.9515 |
| Legacy p under 3 5 | 0.2890 |
| Legacy p btts yes | 0.7760 |
| Legacy p over 2 5 | 0.8532 |
| Legacy goal margin distribution | {"-1": 0.11209431039395613, "-10": 3.699561966779069e-07, "-11": 5.057996238567739e-08, "-12": 6.374235746124186e-09, "-13": 7.447881121177261e-10, "-14": 8.109644235109249e-11, "-15": 8.265644649614066e-12, "-16": 7.917263621531699e-13, "-17": 7.151933076544675e-14, "-18": 6.111396175313334e-15, "-19": 4.945629569994702e-16, "-2": 0.052090132282661517, "-20": 3.727404778557285e-17, "-21": 2.2200189142408742e-18, "-3": 0.02001333920241459, "-4": 0.006374287562669194, "-5": 0.0017219151472227944, "-6": 0.00040217043579282607, "-7": 8.251755008843518e-05, "-8": 1.5071411186985999e-05, "-9": 2.477503857781941e-06, "0": 0.18372708278043165, "1": 0.15585027914107671, "10": 0.000489558442805881, "11": 0.0001432160882609409, "12": 3.8618952837323455e-05, "13": 9.655264486992e-06, "14": 2.24953268647791e-06, "15": 4.905985980321246e-07, "16": 1.0055038665274156e-07, "17": 1.9435295480514042e-08, "18": 3.5535891121813368e-09, "19": 6.153290567853918e-10, "2": 0.15686901339462409, "20": 9.923193580926295e-11, "21": 1.2646217511920054e-11, "3": 0.12896157477422168, "4": 0.08788838621438416, "5": 0.05080081168615244, "6": 0.025387978009464542, "7": 0.011146111005455197, "8": 0.004356021592601081, "9": 0.0015321790201691876} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7196 |
| Legacy raw p draw | 0.1340 |
| Legacy raw p away | 0.1464 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 3.3411 |
| Legacy lambda away | 1.5615 |
| Legacy model home team | FK Bodø/Glimt |
| Legacy model away team | Lille OSC |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,472.3301 |
| Elo away rating | 1,454.8649 |
| Elo rating diff | 77.4652 |
| Elo home expectancy | 0.6097 |

</details>


---

## 2026-11-03 — Feyenoord vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **49.6%**. Expected goals are 1.38 for Feyenoord and 1.58 for Inter Milan (2.96 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 57.0%; Under 3.5 goals: 65.4%; Double Chance 1X: 50.4%; Double Chance X2: 72.4%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 58.7%; BTTS No (at least one team does not score): 41.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Feyenoord win | 27.6% | 3.63 |
| Draw | 22.8% | 4.39 |
| Inter Milan win | 49.6% | 2.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Feyenoord expected goals | 1.38 |
| Inter Milan expected goals | 1.58 |
| Expected total goals | 2.96 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 57.0% |
| Under 2.5 | 43.0% |
| Over 3.5 | 34.6% |
| Under 3.5 | 65.4% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.53% |
| 2 | 1-2 | 10.34% |
| 3 | 0-1 | 10.13% |
| 4 | 0-2 | 7.50% |
| 5 | 2-1 | 6.34% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | f6f3cf01c2b20b7f746b5a06097a0569 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Feyenoord Rotterdam |
| Matched away-team name | FC Internazionale Milano |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3781 |
| Dc lambda away | 1.5827 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.7% |
| P btts no | 41.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.08 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.89 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.24988727726124918, "-10": 1.9817181328328533e-06, "-11": 2.805653264320883e-07, "-12": 3.649987552964834e-08, "-13": 4.3897865808778984e-09, "-14": 4.87041568404836e-10, "-15": 4.4866423495702677e-11, "-2": 0.14678082097506193, "-3": 0.06647408725210906, "-4": 0.023868210181660635, "-5": 0.007066127609964866, "-6": 0.00177513540246781, "-7": 0.0003867354569461218, "-8": 7.43132243895934e-05, "-9": 1.2765187285336705e-05, "0": 0.22790604703722694, "1": 0.15374364112231537, "10": 3.492775851652211e-07, "11": 4.305512590698106e-08, "12": 4.876904848663541e-09, "13": 5.106911579935471e-10, "14": 4.9333621165633536e-11, "15": 3.9569489722032586e-12, "2": 0.07832526620716311, "3": 0.030884955726487463, "4": 0.00965553821479431, "5": 0.002488858137374378, "6": 0.0005443925650735708, "7": 0.00010326585001172432, "8": 1.7277100979571975e-05, "9": 2.5840088118236566e-06} |
| Raw goal margin distribution | {"-1": 0.21605427505872302, "-10": 1.7134072580746156e-06, "-11": 2.425787293905536e-07, "-12": 3.155804582658796e-08, "-13": 3.795439959124165e-09, "-14": 4.210995219062648e-10, "-15": 3.879182129271578e-11, "-2": 0.1269077170148869, "-3": 0.057473957413324804, "-4": 0.02063662025640713, "-5": 0.006109422996542972, "-6": 0.0015347943949555031, "-7": 0.00033437416144497563, "-8": 6.42517298148961e-05, "-9": 1.1036869564347112e-05, "0": 0.23214346597902644, "1": 0.1888458217992854, "10": 4.2902335423498865e-07, "11": 5.2885313338630105e-08, "12": 5.9903817631720475e-09, "13": 6.27290278237868e-10, "14": 6.05972914609633e-11, "15": 4.860384956533341e-12, "2": 0.09620820189091123, "3": 0.03793649482233125, "4": 0.011860055061637122, "5": 0.0030571050409842473, "6": 0.0006686862661913205, "7": 0.00012684312773463563, "8": 2.1221744905864194e-05, "9": 3.173980166224937e-06} |
| Unadjusted home-win probability | 33.9% |
| Unadjusted draw probability | 23.2% |
| Unadjusted away-win probability | 42.9% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 65.6% |
| Raw p btts yes | 58.9% |
| P home draw | 50.4% |
| P draw away | 72.4% |
| P home away | 77.2% |
| Raw p home draw | 57.1% |
| Raw p draw away | 66.1% |
| Raw p home away | 76.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5703 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Matchbook |
| Reference home odds | 4.00 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.90 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:35Z |
| Market reference home last update utc | 2026-11-01T09:33:35Z |
| Market reference draw last update utc | 2026-11-01T09:33:35Z |
| Market reference away last update utc | 2026-11-01T09:33:35Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.98 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +2.7% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | 0.0899 |
| Raw edge prob draw | 0.0061 |
| Raw edge prob away | -0.0960 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.055612493331519026, 0.11175270055659749, 0.07484067520203856, 0.03563022700588959, 0.012722156832471795, 0.0036340666466874844, 0.0008650551269510736, 0.00017650129308123208, 3.1510845150415846e-05, 5.0005720500063435e-06, 7.142032730999984e-07, 9.273235691033744e-08, 1.1037029391393407e-08, 1.2125816557056998e-09, 1.2370438803881054e-10], [0.07685762241087028, 0.11058028759505535, 0.09928677642983369, 0.04726855247267494, 0.01687774646234755, 0.004821105123740888, 0.0011476183874238105, 0.00023415401288703905, 4.1803607852528144e-05, 6.633968464473864e-06, 9.474919956334585e-07, 1.230226312565046e-07, 1.4642185772302222e-08, 1.608661645929272e-09, 1.6411142584486225e-10], [0.04758324910749408, 0.06796044915953509, 0.05513786924007911, 0.031354221409994075, 0.011195362916774386, 0.0031979400591548167, 0.0007612393257497661, 0.00015531926365511058, 2.7729209120639698e-05, 4.400450303238597e-06, 6.284912962473763e-07, 8.160348936190341e-08, 9.712468662890039e-09, 1.0670589806910067e-09, 1.0885854786486643e-10], [0.021041977521746365, 0.030053060066415345, 0.021461538451463234, 0.011608158524181678, 0.0049507458877048015, 0.001414173771291082, 0.00033663066481463117, 6.868434829117855e-05, 1.2262243666761516e-05, 1.945940601011323e-06, 2.779276315994091e-07, 3.6086203045323514e-08, 4.294989331718654e-09, 4.718683887128996e-10, 4.813877068478105e-11], [0.006978792321833269, 0.009967412265426977, 0.0071179441003114685, 0.0033887182795275216, 0.0013746723844440553, 0.0004690255488879122, 0.00011164708718437032, 2.277988378179851e-05, 4.0669015952328425e-06, 6.45391589789815e-07, 9.217761113121301e-08, 1.1968367349340221e-08, 1.4244782145393283e-09, 1.565000953290684e-10, 1.596572769314319e-11], [0.0018516716775671912, 0.0026446373726849402, 0.0018885925938531053, 0.0008991231393753521, 0.00032104161415942773, 0.00010418736639360691, 2.9623141037655385e-05, 6.04414971413678e-06, 1.0790644214738958e-06, 1.712407065066428e-07, 2.44573364511057e-08, 3.1755475482714422e-09, 3.7795450036849114e-10, 4.152391713259593e-11, 4.236160701996272e-12], [0.0004094175423897943, 0.0005847477966825362, 0.0004175810148842369, 0.0001988024067595511, 7.09845434622067e-05, 2.0276637461969082e-05, 5.4836334899339505e-06, 1.3364037219865415e-06, 2.3858868117513587e-07, 3.7862516376096443e-08, 5.407687931139013e-09, 7.0213574507085e-10, 8.356838015653841e-11, 9.181228134979667e-12, 9.366447220590513e-13], [7.759292445102334e-05, 0.00011082156212957963, 7.91400679877217e-05, 3.767708642461917e-05, 1.345301006376879e-05, 3.842833869608454e-06, 9.147501859813581e-07, 2.1204508027719782e-07, 4.5217392018015034e-08, 7.175714444348437e-09, 1.0248664936200828e-09, 1.3306895816832372e-10, 1.5837902230889652e-11, 1.7400288636553683e-12, 1.7751316353461014e-13], [1.2867253204404359e-05, 1.8377566131419647e-05, 1.3123816386822119e-05, 6.248000245638468e-06, 2.230915873794341e-06, 6.372580589345327e-07, 1.516932419427952e-07, 3.095069033224959e-08, 6.277751021125799e-09, 1.1899504411154507e-09, 1.6995385555345892e-10, 2.2066857133073698e-11, 2.6264031117952033e-12, 2.885494022816191e-13, 2.9437050329974294e-14], [1.8966930434002526e-06, 2.708938829629979e-06, 1.9345116512689333e-06, 9.209843323056086e-07, 3.2884738887306273e-07, 9.393480551219386e-08, 2.2360290277434527e-08, 4.562275888184074e-09, 8.145049055242917e-10, 1.4685033078177678e-10, 2.505198976087289e-11, 3.2527575038067814e-12, 3.8714404948537246e-13, 4.253352563214619e-14, 4.339158303030373e-15], [2.516232485179019e-07, 3.5937917878677853e-07, 2.5664042354232364e-07, 1.2218164153403532e-07, 4.362627286623535e-08, 1.2461784996850267e-08, 2.9664098241878884e-09, 6.052506406422875e-10, 1.080556345028675e-10, 1.7147746534929402e-11, 2.7824719168216433e-12, 4.315244433445867e-13, 5.1360152194815505e-14, 5.642675775988269e-15, 5.756509266700164e-16], [3.0346722496826677e-08, 4.334249825490157e-08, 3.0951812921026104e-08, 1.4735571500962983e-08, 5.261494730874571e-09, 1.5029387520510754e-09, 3.577603273017344e-10, 7.299553336499947e-11, 1.3031921230616148e-11, 2.0680835678202486e-12, 2.953726170548169e-13, 4.357137647419028e-14, 6.1942300452414716e-15, 6.805281980981155e-16, 6.942569508021139e-17], [3.3549361624841866e-09, 4.791664562226861e-09, 3.4218310222480974e-09, 1.6290688956153884e-09, 5.816766190542307e-10, 1.6615512827727182e-10, 3.955165371457421e-11, 8.069911161301395e-12, 1.4407244079755707e-12, 2.2863386151321615e-13, 3.265447444838308e-14, 4.2398662864192356e-15, 5.733167741608544e-16, 7.523476914610182e-17, 7.67525307072478e-18], [3.423691480413862e-10, 4.889863873460348e-10, 3.4919572686032855e-10, 1.6624546724000187e-10, 5.93597370728301e-11, 1.6956027463984546e-11, 4.036221653725885e-12, 8.235294131554001e-13, 1.4702502945861989e-13, 2.3331943318328653e-14, 3.3323688008280625e-15, 4.326757166121166e-16, 5.1497177040453136e-17, 6.427821450688844e-18, 7.832548005564211e-19], [3.244294722115767e-11, 4.6336416839213225e-11, 3.3089834762254825e-11, 1.5753443177573063e-11, 5.6249367909833644e-12, 1.6067554779440965e-12, 3.8247291507964246e-13, 7.803775964895619e-14, 1.3932111868732284e-14, 2.2109381349749323e-15, 3.1577572262331464e-16, 4.100040999087518e-17, 4.879879528631109e-18, 5.361272665529086e-19, 6.213890470710564e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3266419117919617, "lambda_away": 1.4282431409004337, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3021 |
| Legacy p draw | 0.2344 |
| Legacy p away | 0.4635 |
| Legacy p over 1 5 | 0.7558 |
| Legacy p under 3 5 | 0.7011 |
| Legacy p btts yes | 0.5499 |
| Legacy p over 2 5 | 0.5228 |
| Legacy goal margin distribution | {"-1": 0.24784447581060984, "-10": 8.47426207135799e-07, "-11": 1.0848974043401546e-07, "-12": 1.2754549585187546e-08, "-13": 1.376693081550562e-09, "-14": 1.2370438803881054e-10, "-2": 0.13483670153733174, "-3": 0.05606644205025244, "-4": 0.018377429315981766, "-5": 0.004949937108625944, "-6": 0.0011289797280562889, "-7": 0.00022299563454918924, "-8": 3.881085805295881e-05, "-9": 6.034123260589456e-06, "0": 0.234423370547671, "1": 0.17001059308584618, "10": 2.9855944819908255e-07, "11": 3.550333622909144e-08, "12": 3.877012384592477e-09, "13": 3.887055648805994e-10, "14": 3.244294722115767e-11, "2": 0.08572836015660269, "3": 0.03311089803471355, "4": 0.010081015687376101, "5": 0.002522149217636432, "6": 0.0005343290748392351, "7": 9.803261563936452e-05, "8": 1.5848167044197063e-05, "9": 2.2887140704962235e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3554 |
| Legacy raw p draw | 0.2428 |
| Legacy raw p away | 0.4018 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3266 |
| Legacy lambda away | 1.4282 |
| Legacy model home team | Feyenoord Rotterdam |
| Legacy model away team | FC Internazionale Milano |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,466.8088 |
| Elo away rating | 1,507.3319 |
| Elo rating diff | 19.4769 |
| Elo home expectancy | 0.5280 |

</details>


---

## 2026-11-03 — Galatasaray vs VfB Stuttgart

The model's most likely 1X2 outcome is **Galatasaray win** at **44.4%**. Expected goals are 1.65 for Galatasaray and 1.43 for VfB Stuttgart (3.08 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 67.3%; Double Chance X2: 55.6%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 44.4% | 2.25 |
| Draw | 23.0% | 4.35 |
| VfB Stuttgart win | 32.7% | 3.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 1.65 |
| VfB Stuttgart expected goals | 1.43 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 80.7% |
| Under 1.5 | 19.3% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.42% |
| 2 | 2-1 | 9.16% |
| 3 | 1-0 | 8.32% |
| 4 | 1-2 | 7.46% |
| 5 | 0-1 | 6.85% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T17:45:00+00:00 |
| Fixture id | 9b8076d3ffa027df6f6cb3189de46706 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Galatasaray SK |
| Matched away-team name | VfB Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6454 |
| Dc lambda away | 1.4340 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.38 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.19 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.17892080836697144, "-10": 5.52711628207334e-07, "-11": 7.080508222132797e-08, "-12": 8.336353832107121e-09, "-13": 9.07411125318047e-10, "-14": 9.10169748102857e-11, "-15": 7.51840433110821e-12, "-2": 0.09336341302251432, "-3": 0.03791012157737737, "-4": 0.01224610397402423, "-5": 0.003268232717747882, "-6": 0.0007410925654944701, "-7": 0.00014585989226604672, "-8": 2.5335420069779953e-05, "-9": 3.935652409029077e-06, "0": 0.229688745313344, "1": 0.21886390652314067, "10": 2.3405875635261332e-06, "11": 3.4405960355187353e-07, "12": 4.6482379753141136e-08, "13": 5.805762634400856e-09, "14": 6.682216376497379e-10, "15": 6.333835463742173e-11, "2": 0.1315404485223588, "3": 0.06128874629379559, "4": 0.022717810075521472, "5": 0.006957039304159496, "6": 0.0018102014220052493, "7": 0.0004088210932245789, "8": 8.148327534449663e-05, "9": 1.4524462351038723e-05} |
| Raw goal margin distribution | {"-1": 0.1865426310541945, "-10": 5.762565141589019e-07, "-11": 7.38212980934268e-08, "-12": 8.691473012185689e-09, "-13": 9.460658059262552e-10, "-14": 9.489419429002682e-11, "-15": 7.838679793898568e-12, "-2": 0.09734058809804867, "-3": 0.03952504958575752, "-4": 0.012767774057851887, "-5": 0.00340745570976659, "-6": 0.0007726622648523722, "-7": 0.00015207335757606876, "-8": 2.6414680113598436e-05, "-9": 4.103306719860479e-06, "0": 0.22714985254883957, "1": 0.21325278780144288, "10": 2.280580799934505e-06, "11": 3.3523878282570366e-07, "12": 4.529068873653975e-08, "13": 5.6569175190543684e-09, "14": 6.510901197086399e-10, "15": 6.171451892529625e-11, "2": 0.12816808308719152, "3": 0.05971745737173598, "4": 0.022135382705674386, "5": 0.006778678357819406, "6": 0.0017637924217711995, "7": 0.0003983399511922592, "8": 7.939424961588745e-05, "9": 1.4152091758211483e-05} |
| Unadjusted home-win probability | 43.2% |
| Unadjusted draw probability | 22.7% |
| Unadjusted away-win probability | 34.1% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 60.9% |
| P home draw | 67.3% |
| P draw away | 55.6% |
| P home away | 77.0% |
| Raw p home draw | 65.9% |
| Raw p draw away | 56.8% |
| Raw p home away | 77.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5938 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.22 |
| Reference draw odds | 4.30 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.97 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0162 |
| Raw edge prob draw | -0.0036 |
| Raw edge prob away | 0.0199 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.046935344862344935, 0.07819458130036604, 0.06167422576492057, 0.03449322466554637, 0.014468554729363797, 0.004855192936848134, 0.0013577086593970001, 0.0003254317289511589, 6.825292251820761e-05, 1.2724188326115633e-05, 2.1349191554946162e-06, 3.2564176080743323e-07, 4.5531315053831535e-08, 5.8764925142779205e-09, 7.042737430647886e-10, 7.877738923930296e-11], [0.09066573412374562, 0.10660288752401025, 0.07849786971077839, 0.043902369622299105, 0.018415321959256187, 0.006179604167713332, 0.0017280676997352903, 0.0004142037803009024, 8.687111921981356e-05, 1.61951230844141e-05, 2.7172875481216377e-06, 4.1447110515313124e-07, 5.7951456909718905e-08, 7.479496305319314e-09, 8.963872320755865e-10, 1.0026647533821768e-10], [0.05323304125468399, 0.08931669083096165, 0.05990883608915925, 0.027939081908717227, 0.011719348933131996, 0.003932645743055716, 0.0010997270858516468, 0.0002635956428841436, 5.528401624479802e-05, 1.0306433895708867e-05, 1.7292578972308353e-06, 2.6376576606899473e-07, 3.687979749748513e-08, 4.759885666948669e-09, 5.704529508167492e-10, 6.380870306713383e-11], [0.022584692848550508, 0.03789357100631035, 0.03178973327729898, 0.014215229744178302, 0.004972060393346118, 0.0016684674423191616, 0.0004665710969313736, 0.00011183329921490751, 2.3454841145548443e-05, 4.3726159244751635e-06, 7.336563447133934e-07, 1.1190547581398434e-07, 1.564665251441283e-08, 2.019432917009878e-09, 2.4202082719840744e-10, 2.7071531625271875e-11], [0.007186349948846206, 0.012057567658276822, 0.010115353334363114, 0.005657325257125904, 0.0018973148712688776, 0.0005308990031064958, 0.00014846087131006026, 3.5584864026341315e-05, 7.463227310497863e-06, 1.3913471587103274e-06, 2.3344622265430404e-07, 3.560783030277297e-08, 4.9786960243642014e-09, 6.425746737921073e-10, 7.700996293463504e-11, 8.614042316849442e-12], [0.0018293319615580754, 0.0030693320048345444, 0.0025749287592061157, 0.0014401088151088108, 0.0006040691587891304, 0.00016207085096291718, 3.7791677118626446e-05, 9.058357799780657e-06, 1.8998128886916856e-06, 3.541764379927622e-07, 5.9425249180230315e-08, 9.064204014314248e-09, 1.2673593450196264e-09, 1.635715483970251e-10, 1.9603385245293943e-11, 2.1927603081667972e-12], [0.0003880569238206939, 0.0006510986310904642, 0.0005462206720008916, 0.0003054908614192756, 0.00012814143329951453, 4.30002438744451e-05, 9.614084213902978e-06, 1.9215530786747674e-06, 4.030080712046844e-07, 7.513159005880014e-08, 1.2605901978839008e-08, 1.9227932385121148e-09, 2.6884544693836995e-10, 3.469849826571359e-11, 4.158473986471832e-12, 4.651511249705514e-13], [7.055886096579892e-05, 0.00011838669784271524, 9.93171519087863e-05, 5.5546199266282335e-05, 2.3299451758568225e-05, 7.81856486197972e-06, 2.186387514408064e-06, 4.1900321208385365e-07, 7.327736916598658e-08, 1.3660880895782592e-08, 2.2920814717491685e-09, 3.496139160368194e-10, 4.888310798592412e-11, 6.309091178550284e-12, 7.56118934697669e-13, 8.457659570080803e-14], [1.1225759639338166e-05, 1.883506332566019e-05, 1.5801140496472678e-05, 8.837278171827517e-06, 3.706891545440643e-06, 1.243916478579534e-06, 3.47849446252991e-07, 8.337668462620706e-08, 1.398114978974748e-08, 2.173416113845931e-09, 3.646651224728327e-10, 5.5622805332691675e-11, 7.777194999502398e-12, 1.0037625344803115e-12, 1.2029686000434084e-13, 1.3455950414377587e-14], [1.5875499343420752e-06, 2.6636596993576436e-06, 2.2346015203995626e-06, 1.249770245595119e-06, 5.242295950249331e-07, 1.7591500150918883e-07, 4.919296183972282e-08, 1.1791153067285765e-08, 2.472963098268035e-09, 3.6860683168904716e-10, 5.1571039273803815e-11, 7.866192025383756e-12, 1.0998529994851616e-12, 1.419523664238372e-13, 1.7012414156117507e-14, 1.902944110971077e-15], [2.0206056316027663e-07, 3.3902592118627886e-07, 2.844161508770875e-07, 1.590685585273021e-07, 6.672302074071169e-08, 2.23901519595468e-08, 6.261193653083918e-09, 1.5007572218962486e-09, 3.147543932328065e-10, 5.867872067892897e-11, 7.871706455691717e-12, 1.0011950844460397e-12, 1.3998735514520518e-13, 1.8067447505782872e-14, 2.1653101491422235e-15, 2.422033791867463e-16], [2.337992096067582e-08, 3.9227839005220447e-08, 3.2909079453428015e-08, 1.840542393592657e-08, 7.720353377110902e-09, 2.5907083248921505e-09, 7.244670134491902e-10, 1.7364885398872146e-10, 3.641944138288531e-11, 6.789567593448326e-12, 1.1391829122041388e-12, 1.3892775904352518e-13, 1.619758575151974e-14, 2.090539034632396e-15, 2.5054260638746325e-16, 2.80247455180208e-17], [2.479796012376954e-09, 4.160708622707803e-09, 3.490508121771178e-09, 1.9521749863562727e-09, 8.188608315187034e-10, 2.747839988041444e-10, 7.684073928528853e-11, 1.8418100574391857e-11, 3.862835364849097e-12, 7.201368504331448e-13, 1.2082766437932953e-13, 1.8429987515671838e-14, 2.060307524699319e-15, 2.2173344257746927e-16, 2.6573851866101473e-17, 2.9724502619301436e-18], [2.427877496319768e-10, 4.073597498906024e-10, 3.4174287228756986e-10, 1.911303064686222e-10, 8.017166636042411e-11, 2.69030954044428e-11, 7.523195487862063e-12, 1.803248802979475e-12, 3.781960696563802e-13, 7.050596277720976e-14, 1.182979429821177e-14, 1.8044126098849505e-15, 2.5229343688619056e-16, 2.6034596697292305e-17, 2.6017485556967434e-18, 2.910217237164013e-19], [2.207256979442175e-11, 3.7034308874842306e-11, 3.106887975916253e-11, 1.7376235150878658e-11, 7.28864905234283e-12, 2.445841900592914e-12, 6.839564917695643e-13, 1.639388112489416e-13, 3.4382950359398964e-14, 6.409910659338702e-15, 1.0754824355707168e-15, 1.6404461646023124e-16, 2.2936760618219984e-17, 2.9603296525785652e-18, 2.836614335481408e-19, 2.64576664933063e-20], [1.8729052386851774e-12, 3.142441127100046e-12, 2.636261577286805e-12, 1.474411096932211e-12, 6.184576204860636e-13, 2.0753496993240278e-13, 5.803518613368195e-14, 1.3910562352805871e-14, 2.9174676283431697e-15, 5.438947691724321e-16, 9.125700842515144e-17, 1.391954015359437e-17, 1.946233697319134e-18, 2.5119036732871355e-19, 3.010414457103242e-20, 2.692298973359254e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2727824101105594, "lambda_away": 1.6778430975536767, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3725 |
| Legacy p draw | 0.2297 |
| Legacy p away | 0.3977 |
| Legacy p over 1 5 | 0.7842 |
| Legacy p under 3 5 | 0.6622 |
| Legacy p btts yes | 0.5816 |
| Legacy p over 2 5 | 0.5627 |
| Legacy goal margin distribution | {"-1": 0.19017428104988554, "-10": 2.5883686937854857e-06, "-11": 3.8860373825361604e-07, "-12": 5.360833584159287e-08, "-13": 6.8366884494206404e-09, "-14": 8.045402184030064e-10, "-15": 7.877738923930296e-11, "-2": 0.11912234803340618, "-3": 0.057345325622117194, "-4": 0.02186754964932941, "-5": 0.00687176386571837, "-6": 0.0018318118575705823, "-7": 0.0004233798490691157, "-8": 8.629435548628987e-05, "-9": 1.572155093603084e-05, "0": 0.22973173138711983, "1": 0.21807882518879446, "10": 2.449775367777592e-07, "11": 2.790036714844256e-08, "12": 2.919699053123651e-09, "13": 2.824583200841059e-10, "14": 2.5215010921521795e-11, "15": 1.8729052386851774e-12, "2": 0.1028183943708937, "3": 0.03754727422656051, "4": 0.010861338070271813, "5": 0.002589132385745949, "6": 0.0005235639248134575, "7": 9.179559719781366e-05, "8": 1.41930873753028e-05, "9": 1.9615197855115857e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2965 |
| Legacy raw p draw | 0.2287 |
| Legacy raw p away | 0.4748 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2728 |
| Legacy lambda away | 1.6778 |
| Legacy model home team | Galatasaray SK |
| Legacy model away team | VfB Stuttgart |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,464.0831 |
| Elo away rating | 1,479.0805 |
| Elo rating diff | 45.0026 |
| Elo home expectancy | 0.5644 |

</details>


---

## 2026-11-03 — LASK vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **LASK win** at **76.0%**. Expected goals are 5.26 for LASK and 1.09 for ŠK Slovan Bratislava (6.35 combined). The most likely exact score is 2-2 at 5.3%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 91.9%; Under 3.5 goals: 16.1%; Double Chance 1X: 90.2%; Double Chance X2: 24.0%; Double Chance 12 (either team wins): 85.8%; Under 4.5 goals: 30.6%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| LASK win | 76.0% | 1.32 |
| Draw | 14.2% | 7.03 |
| ŠK Slovan Bratislava win | 9.8% | 10.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| LASK expected goals | 5.26 |
| ŠK Slovan Bratislava expected goals | 1.09 |
| Expected total goals | 6.35 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 97.8% |
| Under 1.5 | 2.2% |
| Over 2.5 | 91.9% |
| Under 2.5 | 8.1% |
| Over 3.5 | 83.9% |
| Under 3.5 | 16.1% |
| Over 4.5 | 69.4% |
| Under 4.5 | 30.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 5.31% |
| 2 | 5-1 | 5.17% |
| 3 | 4-1 | 4.92% |
| 4 | 5-0 | 4.73% |
| 5 | 6-1 | 4.53% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | adf608a0e9be02eb1d8b0a6f464a12b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | LASK Linz |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.2600 |
| Dc lambda away | 1.0938 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 26 |
| Score grid omitted mass | 0 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 218.67 |
| Fair Over 1.5 odds | 1.02 |
| Fair Under 1.5 odds | 44.56 |
| Fair Over 2.5 odds | 1.09 |
| Fair Under 2.5 odds | 12.29 |
| Fair Over 3.5 odds | 1.19 |
| Fair Under 3.5 odds | 6.20 |
| Fair Over 4.5 odds | 1.44 |
| Fair Under 4.5 odds | 3.27 |
| Goal margin distribution | {"-1": 0.0691021539267444, "-10": 8.201823664040827e-09, "-11": 7.826414931107409e-10, "-12": 6.887489728690043e-11, "-13": 5.622051669552729e-12, "-14": 4.2780005187430285e-13, "-15": 3.047998683532356e-14, "-16": 2.0413351017051562e-15, "-17": 1.2895937510038496e-16, "-18": 7.708813189396716e-18, "-19": 4.372611264914428e-19, "-2": 0.021654376726484098, "-20": 2.359500465639101e-20, "-21": 1.2140366788343965e-21, "-22": 5.968890745825641e-23, "-23": 2.80940737013502e-24, "-24": 1.2665476471858982e-25, "-25": 5.39006504275254e-27, "-26": 1.8567333492731118e-28, "-3": 0.005701166517370372, "-4": 0.001251440659598528, "-5": 0.0002338986872055253, "-6": 3.7901384691038324e-05, "-7": 5.40597471157095e-06, "-8": 6.873711924707157e-07, "-9": 7.8746721108828e-08, "0": 0.14228717092525936, "1": 0.06284539519748311, "10": 0.010509016583001022, "11": 0.004822262425086357, "12": 0.002040728633748714, "13": 0.0008010422977523866, "14": 0.0002931148161511988, "15": 0.0001004264326257138, "16": 3.2343267043227624e-05, "17": 9.825594236146722e-06, "18": 2.8244230617789875e-06, "19": 7.704055789187533e-07, "2": 0.0970301626560629, "20": 1.999101934574236e-07, "21": 4.9463290301248145e-08, "22": 1.16944862136198e-08, "23": 2.6469062305796057e-09, "24": 5.738279441037397e-10, "25": 1.1743309019191814e-10, "26": 1.9452809937825258e-11, "3": 0.12284602816658576, "4": 0.12967133352202168, "5": 0.11654612071268873, "6": 0.09081580505909909, "7": 0.062289765007151464, "8": 0.03808643575499566, "9": 0.020982044640635127} |
| Raw goal margin distribution | {"-1": 0.016531857533083196, "-10": 1.9621874662421457e-09, "-11": 1.872375451176599e-10, "-12": 1.6477489120814445e-11, "-13": 1.3450081070295958e-12, "-14": 1.0234600672113626e-13, "-15": 7.291969516695501e-15, "-16": 4.883648216587723e-16, "-17": 3.085197632153522e-17, "-18": 1.844240651765503e-18, "-19": 1.0460945480187538e-19, "-2": 0.005180548661181413, "-20": 5.644820505673462e-21, "-21": 2.904436442850153e-22, "-22": 1.4279851760501722e-23, "-23": 6.721168553545003e-25, "-24": 3.030062606201233e-26, "-25": 1.2895081023856459e-27, "-26": 4.4420107714222197e-29, "-3": 0.0013639353809067512, "-4": 0.00029939209590373514, "-5": 5.595744205247393e-05, "-6": 9.067449513702096e-06, "-7": 1.2933142989129395e-06, "-8": 1.6444527385235943e-07, "-9": 1.883920399859977e-08, "0": 0.03856720573079893, "1": 0.07759167086872706, "10": 0.01297489105287489, "11": 0.005953775893272055, "12": 0.002519572738537871, "13": 0.0009890018214353004, "14": 0.000361892359338081, "15": 0.0001239908617382177, "16": 3.993241069375869e-05, "17": 1.2131107962088066e-05, "18": 3.4871561220188555e-06, "19": 9.511763897267858e-07, "2": 0.11979767843754133, "20": 2.4681785969058845e-07, "21": 6.106953944801435e-08, "22": 1.4438523656581192e-08, "23": 3.2679860858244863e-09, "24": 7.084730525484681e-10, "25": 1.4498802425597244e-10, "26": 2.4017289117597748e-11, "3": 0.15167107399165242, "4": 0.1600978942074119, "5": 0.14389293298179537, "6": 0.11212516101905749, "7": 0.07690566555811575, "8": 0.04702317772651852, "9": 0.025905349099854192} |
| Unadjusted home-win probability | 93.8% |
| Unadjusted draw probability | 3.9% |
| Unadjusted away-win probability | 2.3% |
| Raw p over 1 5 | 98.7% |
| Raw p under 3 5 | 12.2% |
| Raw p btts yes | 66.1% |
| P home draw | 90.2% |
| P draw away | 24.0% |
| P home away | 85.8% |
| Raw p home draw | 97.7% |
| Raw p draw away | 6.2% |
| Raw p home away | 96.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.9186 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.46 |
| Reference draw odds | 5.30 |
| Reference away odds | 7.60 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.97 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +7.6% |
| Draw probability edge | -4.4% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +22.8% |
| Under 2.5 probability edge | -22.8% |
| Raw edge prob home | 0.2547 |
| Raw edge prob draw | -0.1482 |
| Raw edge prob away | -0.1065 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.006172879367781287, 0.011196365544029634, 0.004299977083182802, 0.00136824905710838, 0.0003265317662272733, 6.234127846919141e-05, 9.918470939996837e-06, 1.35259244234614e-06, 1.6139766254191595e-07, 1.71188663970751e-08, 1.63416262599416e-09, 1.4181522549734352e-10, 1.1281371087373786e-11, 8.283975465943419e-13, 5.648472771458976e-14, 3.594678480439965e-15, 2.1446693259885383e-16, 1.2042916917625961e-17, 6.386743230880859e-19, 3.208825695162149e-20, 1.5315684177719996e-21, 6.962053860071796e-23, 3.0208904009479398e-24, 1.2537975140733815e-25, 4.98696630600977e-27, 1.9042181334543836e-28], [0.013203659060961234, 0.035385256567724836, 0.020880678641983463, 0.00664421421579525, 0.0015856374918036054, 0.0003027291021937405, 4.8164071647709556e-05, 6.5681857311900065e-06, 7.837466711823794e-07, 8.31291751182522e-08, 7.935489883324395e-09, 6.886544027715141e-10, 5.478231157038034e-11, 4.022696545498919e-12, 2.742897054500756e-13, 1.745575027943222e-14, 1.0414509222486046e-15, 5.848037633794137e-17, 3.1014010166346038e-18, 1.5582050058095995e-19, 7.437292648554483e-21, 3.380771723386405e-22, 1.4669436709685113e-23, 6.088437790953464e-25, 2.421669669855831e-26, 9.246878794867339e-28], [0.03059802871927324, 0.02920880028053462, 0.043165571185865, 0.016132144332944666, 0.0038499259726896807, 0.0007350259055107312, 0.00011694230954143614, 1.5947547261382595e-05, 1.9029359995530728e-06, 2.0183753980993002e-07, 1.9267360141110228e-08, 1.6720520832421979e-09, 1.330113883211008e-10, 9.767102500300583e-12, 6.659750835309095e-13, 4.238254123086472e-14, 2.528641619268129e-15, 1.4199028524484055e-16, 7.530198035419959e-18, 3.7833199288305375e-19, 1.805773783867515e-20, 8.208509784159591e-22, 3.561737514739543e-23, 1.478271982446311e-24, 5.879811121675704e-26, 2.245141088218072e-27], [0.04952798525865723, 0.04727928857737677, 0.02256634422649107, 0.022232777536398584, 0.006231743834601677, 0.001189761358382415, 0.0001892905270538993, 2.581375071316219e-05, 3.080217585215448e-06, 3.2670754015121054e-07, 3.1187418568604205e-08, 2.7064936663179145e-09, 2.1530099668974637e-10, 1.58096756197231e-11, 1.0779911484616496e-12, 6.860317364119913e-14, 4.093025926361497e-15, 2.2983483083174363e-16, 1.2188874672770346e-17, 6.123930903623051e-19, 2.9229444213027145e-20, 1.3286834760349104e-21, 5.765263009054933e-23, 2.3928284278251338e-24, 9.517449677227442e-26, 3.634133288162737e-27], [0.06012694509556707, 0.057397028641549774, 0.027395528673897072, 0.008717233964721512, 0.006441284469646481, 0.0014443695922353823, 0.00022979858897634724, 3.133787824671626e-05, 3.7393823443742188e-06, 3.966227623916108e-07, 3.786150787587626e-08, 3.2856817257219722e-09, 2.61375283879985e-10, 1.919293694264817e-11, 1.3086806228551635e-12, 8.328421261967291e-14, 4.968931077325683e-15, 2.7901935001593185e-16, 1.4797286713743463e-17, 7.434448530224189e-19, 3.5484528154987406e-20, 1.6130209616991026e-21, 6.99902591628957e-23, 2.9048923099048444e-24, 1.15541783338027e-25, 4.4118356833248974e-27], [0.0583952609038287, 0.05574396732281242, 0.026606524611683367, 0.008466173542004211, 0.0020204469248454, 0.0011943488910744113, 0.000223180281939766, 3.04353326695843e-05, 3.6316863807371796e-06, 3.851998409937998e-07, 3.677107870872294e-08, 3.1910525524873607e-09, 2.53847553234653e-10, 1.8640171365687804e-11, 1.2709900077236174e-12, 8.088558827270773e-14, 4.8258235340642376e-15, 2.709834619986088e-16, 1.4371117922994452e-17, 7.22033292908032e-19, 3.4462557117549526e-20, 1.5665652022076246e-21, 6.797450690447947e-23, 2.821230050267851e-24, 1.1221412583981704e-25, 4.284772748442409e-27], [0.047261208356839585, 0.04511542912050868, 0.021533536863463217, 0.006851953147581356, 0.001635214255593702, 0.0003121942726815899, 0.00015378977079768692, 2.4632317356640845e-05, 2.9392434260956096e-06, 3.117549209037926e-07, 2.9760045343761113e-08, 2.5826239531509964e-09, 2.0544718729923965e-10, 1.5086104746955693e-11, 1.0286540833067608e-12, 6.546337119235888e-14, 3.9056979625857984e-15, 2.1931584276788936e-16, 1.1631019160919971e-17, 5.843653297979206e-19, 2.789168277070245e-20, 1.2678728252972798e-21, 5.501400771300265e-23, 2.2833144190908784e-24, 9.081858869729774e-26, 3.4678077380174476e-27], [0.032785759579661275, 0.03129720258758866, 0.014938114937196862, 0.004753295490279082, 0.0011343709420280042, 0.00021657352239079066, 3.445675547490377e-05, 1.4548898345711451e-05, 2.0389941701548708e-06, 2.1626873793312303e-07, 2.064495863824368e-08, 1.791602266564332e-09, 1.4252158002929524e-10, 1.0465441329658613e-11, 7.135916883735717e-13, 4.541285387757541e-14, 2.7094371651540612e-15, 1.5214245980992196e-16, 8.068600256623992e-18, 4.053823817788918e-19, 1.934884945573113e-20, 8.795410670401702e-22, 3.816398465256571e-23, 1.5839670671106279e-24, 6.300212199214407e-26, 2.405666607351466e-27], [0.019900946463577165, 0.01899739280531153, 0.009067431392266328, 0.0028852489706015253, 0.0006885628296115913, 0.00013146006466786836, 2.091524048263987e-05, 2.852233613206487e-06, 1.053777388039712e-06, 1.3127506059131994e-07, 1.2531483847558223e-08, 1.0875020511356001e-09, 8.651055734047864e-11, 6.352519822308648e-12, 4.331499458681388e-13, 2.7565589004578992e-14, 1.6446275657925243e-15, 9.235042854985394e-17, 4.897637992889168e-18, 2.460669870239583e-19, 1.1744745953337393e-20, 5.338811701206528e-22, 2.3165527507822273e-23, 9.614675458729639e-25, 3.824226959912242e-26, 1.4602389261652561e-27], [0.010737661044816793, 0.010250143883961284, 0.004892380621970991, 0.0015567513601891774, 0.00037151772082603897, 7.092997400484128e-05, 1.1284928753737737e-05, 1.5389377492822676e-06, 1.8363325696308466e-07, 6.030628782650946e-08, 6.761428467231303e-09, 5.867674902803658e-10, 4.6677229307679617e-11, 3.4275357082775254e-12, 2.3370834692838034e-13, 1.4873159513976914e-14, 8.873675118297863e-16, 4.9828162742248773e-17, 2.6425465132580382e-18, 1.3276674583383948e-19, 6.336939870434299e-21, 2.880584123703687e-22, 1.2499083033996755e-23, 5.187649055822856e-25, 2.063381906440583e-26, 7.878796449358118e-28], [0.005214205687752317, 0.004977467468656016, 0.0023757388838460593, 0.00075595809579339, 0.0001804089181942474, 3.4443578759332846e-05, 5.479958758990883e-06, 7.473078105103532e-07, 8.917226655982005e-08, 9.458179836808221e-09, 2.7955118396734542e-09, 2.849341558127231e-10, 2.2666451616304936e-11, 1.6644105369392175e-12, 1.1348871851541526e-13, 7.222402775515169e-15, 4.30905455852787e-16, 2.419654415393354e-17, 1.283219967744401e-18, 6.447150067242447e-20, 3.0772165164696455e-21, 1.398810975609545e-22, 6.069551793033559e-24, 2.51912116614927e-25, 1.0019777703600697e-26, 3.8259417099701153e-28], [0.0023018336912659565, 0.002197324578783846, 0.0010487802230994773, 0.00033372097655637, 7.96422985536984e-05, 1.5205267069197921e-05, 2.419151535932346e-06, 3.299022706410421e-07, 3.936548340930975e-08, 4.175354466272001e-09, 3.9857827386428454e-10, 1.0709635880833302e-10, 1.000620326781761e-11, 7.347612425462759e-13, 5.01000864754897e-14, 3.1883609961194286e-15, 1.90225080372659e-16, 1.0681669247639048e-17, 5.664830142772043e-19, 2.8461223292906615e-20, 1.3584505631543771e-21, 6.175111654942447e-23, 2.6794299352066514e-24, 1.1120769528221608e-25, 4.423274277675387e-27, 1.6889785436571802e-28], [0.0009314749176724795, 0.0008891835838916455, 0.00042440619219142223, 0.0001350456900265728, 3.22285679326178e-05, 6.153061772103828e-06, 9.789495159098686e-07, 1.3350038777837296e-07, 1.5929891267538797e-08, 1.689625958852457e-09, 1.6129126367491207e-10, 1.3997111771476098e-11, 3.4475530135051475e-12, 2.973332393676583e-13, 2.027382521257437e-14, 1.2902227939574227e-15, 7.697771205265178e-17, 4.322513403467097e-18, 2.29236682514849e-19, 1.1517302802635515e-20, 5.497193960092036e-22, 2.49886064411649e-23, 1.08427545733469e-24, 4.500202564616117e-26, 1.789950794131646e-27, 6.834729875894769e-29], [0.0003479415398435011, 0.00033214410770812197, 0.00015853195961431434, 5.044473495269743e-05, 1.2038603875073756e-05, 2.2984041192301453e-06, 3.6567511967562805e-07, 4.9867505406779226e-08, 5.950424205749658e-09, 6.31139976749634e-10, 6.024846142565233e-11, 5.228457074612734e-12, 4.159226505211593e-13, 9.456338030083045e-14, 7.573049825761871e-15, 4.819476049795017e-16, 2.875412226037724e-17, 1.6146242277297015e-18, 8.562867640294046e-20, 4.302153494380957e-21, 2.0534123839557334e-22, 9.334201102706758e-24, 4.050183908142552e-25, 1.6809979315951542e-26, 6.6861514329390435e-28, 2.55303325115339e-29], [0.0001206859501660968, 0.0001152065006347181, 5.498791603426358e-05, 1.7497108196340917e-05, 4.175673729529447e-06, 7.972175013070431e-07, 1.268369660317195e-07, 1.7296892101865917e-08, 2.0639461430366854e-09, 2.1891530346189139e-10, 2.089759910952493e-11, 1.813526807509398e-12, 1.4426567260788965e-13, 1.0593511047599018e-14, 2.2364832850838648e-15, 1.6716688861981604e-16, 9.973567880818698e-18, 5.6004367622332615e-19, 2.970090371446381e-20, 1.492231949261626e-21, 7.122404089836255e-23, 3.237632763332252e-24, 1.4048345406572442e-25, 5.830658583998154e-27, 2.319138263863523e-28, 8.855373918839117e-30], [3.9070046084298504e-05, 3.729616647848756e-05, 1.78014127624753e-05, 5.664394427289662e-06, 1.3518041231906427e-06, 2.5808575457547673e-07, 4.1061333993159336e-08, 5.599577834909268e-09, 6.68167842345964e-10, 7.087014671586032e-11, 6.7652461544748874e-12, 5.87098795236626e-13, 4.67035845466291e-14, 3.4294709885831347e-15, 2.338403050462709e-16, 4.607675420491209e-17, 3.2287748175506486e-18, 1.8130471864497207e-19, 9.615167923626279e-21, 4.830849899750172e-22, 2.3057585049288625e-23, 1.0481291409094007e-24, 4.5479154921308916e-26, 1.887577628258285e-27, 7.50781998404167e-29, 2.8667783335721895e-30], [1.1857753265772462e-05, 1.1319381065148286e-05, 5.402726166848215e-06, 1.719142879276266e-06, 4.1027235345111137e-07, 7.832898872357849e-08, 1.2462108854538381e-08, 1.6994710529795536e-09, 2.0278884231585498e-10, 2.15090791511375e-11, 2.0532512172853132e-12, 1.781843983886659e-13, 1.4174531071352714e-14, 1.0408439428763916e-15, 7.097049834159247e-17, 4.5165504634047686e-18, 8.343353658408198e-19, 5.502595556129546e-20, 2.9182020569243784e-21, 1.4661622372193752e-22, 6.997973686263636e-24, 3.181070407942132e-25, 1.380291685935454e-26, 5.728795337887708e-28, 2.278622265827827e-29, 8.70066804472563e-31], [3.3871307104906374e-06, 3.2333463490237613e-06, 1.5432720946324082e-06, 4.910678702453678e-07, 1.1719303453975195e-07, 2.2374434454892e-08, 3.559763023618156e-09, 4.854486736330245e-10, 5.7926008423158896e-11, 6.14400223333081e-12, 5.865048882821662e-13, 5.089782477213924e-14, 4.04891115732411e-15, 2.9731386753687223e-16, 2.0272504333979572e-17, 1.2901387334679398e-18, 7.697269680707968e-20, 1.338263243584334e-20, 8.335754324520093e-22, 4.1880472876611954e-23, 1.9989496368058238e-24, 9.086629675517932e-26, 3.942760701862445e-27, 1.6364127493768503e-28, 6.508814343836334e-30, 2.4853190377253887e-31], [9.137721552666422e-07, 8.722845719889552e-07, 4.163403153316303e-07, 1.3247913485786627e-07, 3.1616061175895735e-08, 6.036122294128217e-09, 9.603444946058434e-10, 1.3096320121425907e-10, 1.562714228857035e-11, 1.6575144694963718e-12, 1.5822590907995538e-13, 1.3731095436138212e-14, 1.0923057274560512e-15, 8.020863578969334e-17, 5.469068530641243e-18, 3.4805059262186217e-19, 2.0765513075786394e-20, 1.1660415230133595e-21, 1.9146759379931252e-22, 1.1298415453977101e-23, 5.3927193073365095e-25, 2.4513695786795066e-26, 1.0636687072875288e-27, 4.414675820666205e-29, 1.7559326224928105e-30, 6.704835235893751e-32], [2.3354081290508688e-07, 2.2293746515773598e-07, 1.0640776820271611e-07, 3.385886149993323e-08, 8.08039573685748e-09, 1.542705037837218e-09, 2.454437166272896e-10, 3.347142096194169e-11, 3.993966649586974e-12, 4.23625598982243e-13, 4.0439191779045124e-14, 3.5093772246729256e-15, 2.791702133411254e-16, 2.0499628814873396e-17, 1.3977781037843928e-18, 8.895436117692592e-20, 5.307225412986277e-21, 2.980155212610545e-22, 1.5804714307426118e-23, 2.458593999634984e-24, 1.3782648590740017e-25, 6.265181542641296e-27, 2.718511974017696e-28, 1.1282976548677665e-29, 4.487791947915819e-31, 1.7136139051297472e-32], [5.6703682016476916e-08, 5.4129190425492074e-08, 2.5835793655055716e-08, 8.220927605970186e-09, 1.9619191383746456e-09, 3.7456860247502045e-10, 5.959370564592634e-11, 8.12685708873047e-12, 9.697346346680486e-13, 1.02856245809554e-13, 9.818631026921274e-15, 8.520763790635306e-16, 6.77824950973372e-17, 4.9773074749328746e-18, 3.3938035986367803e-19, 2.1598108473679038e-20, 1.2885937085867888e-21, 7.235813365276409e-23, 3.8373827824850975e-24, 1.9279767527013491e-25, 2.849217255214834e-26, 1.5211853446524263e-27, 6.600543888460824e-29, 2.739505384335541e-30, 1.0896353592557926e-31, 4.1606525543344964e-33], [1.311204509652741e-08, 1.2516724852035794e-08, 5.974216831478961e-09, 1.9009907235555837e-09, 4.5367022569422313e-10, 8.661448838487379e-11, 1.378032833337893e-11, 1.8792380468256597e-12, 2.2423948162197315e-13, 2.3784270889542745e-14, 2.270440441129469e-15, 1.970324238330821e-16, 1.567388749487513e-17, 1.1509425446417895e-18, 7.847763011430505e-20, 4.994303054681345e-21, 2.9797181095192045e-22, 1.673194892846481e-23, 8.87348657217033e-25, 4.4582145686995783e-26, 2.1279001359798864e-27, 2.9949233797075876e-28, 1.5262964599363769e-29, 6.3347770134485285e-31, 2.5196508341700263e-32, 9.621009074430725e-34], [2.8941845577246185e-09, 2.762781207154631e-09, 1.318671951696087e-09, 4.1960029545272226e-10, 1.001373433234606e-10, 1.9118170576236776e-11, 3.04169282283836e-12, 4.147988887600627e-13, 4.949574533680993e-14, 5.249834714455361e-15, 5.011478846797637e-16, 4.3490408569429245e-17, 3.4596527706570024e-18, 2.5404428638006566e-19, 1.7322144908104297e-20, 1.1023783605872243e-21, 6.577047344984204e-23, 3.693195672597617e-24, 1.9586195457147732e-25, 9.840490682243335e-27, 4.696853670495786e-28, 2.135049786051118e-29, 2.8683959080825493e-30, 1.3982573789200268e-31, 5.56155388532346e-33, 2.1236180693368947e-34], [6.110501492103489e-10, 5.833069160574302e-10, 2.784116481766072e-10, 8.859035007313745e-11, 2.1142030633815114e-11, 4.036425718622033e-12, 6.421936183325718e-13, 8.757662747962191e-14, 1.0450053191187295e-14, 1.1083993510488666e-15, 1.0580751973563593e-16, 9.182144440180986e-18, 7.304376412636182e-19, 5.363645476037613e-20, 3.657230221372617e-21, 2.327455102768802e-22, 1.388614195590814e-23, 7.7974563190192935e-25, 4.135239967544581e-26, 2.0776260738586863e-27, 9.916482791380808e-29, 4.5077377213419365e-30, 1.955943157879041e-31, 2.5135189396773524e-32, 1.1742127233724433e-33, 4.483601899784486e-35], [1.236357538750843e-10, 1.1802237574200317e-10, 5.633192963687535e-11, 1.7924772183599487e-11, 4.277735467767705e-12, 8.167030763801046e-13, 1.2993711275403608e-13, 1.771966241113406e-14, 2.1143930755876654e-15, 2.2426602716433783e-16, 2.1408377831301337e-17, 1.8578529954026617e-18, 1.4779181144635964e-19, 1.085243744405528e-20, 7.399792244523144e-22, 4.709215219292498e-23, 2.809628033564457e-24, 1.577684567389126e-25, 8.366964830995487e-27, 4.203728061338306e-28, 2.0064340501120065e-29, 9.120651589226811e-31, 3.9575230801218936e-32, 1.6425397618489673e-33, 2.0228254936508467e-34, 9.071816800502742e-36], [2.4014997246581867e-11, 2.29246552040513e-11, 1.094190873370677e-11, 3.481706069181805e-12, 8.309069363854112e-13, 1.5863632902145219e-13, 2.523897260471852e-14, 3.441865566199303e-15, 4.1069951285881574e-16, 4.356141210005427e-17, 4.158361303736867e-18, 3.6086919172448305e-19, 2.87070676055216e-20, 2.107976432133126e-21, 1.4373349521291945e-22, 9.147175228868934e-24, 5.4574188594459e-25, 3.064493025221887e-26, 1.6251984646902123e-27, 8.165317446959233e-29, 3.897295618674456e-30, 1.7715945099798104e-31, 7.687089122167304e-33, 3.190467694163789e-34, 1.2690051393957608e-35, 1.5002966545345234e-36]] |
| Legacy trial inputs | {"lambda_home": 4.855997657207927, "lambda_away": 0.9545974529442947, "rho": 0.05, "max_goals": 25, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8080 |
| Legacy p draw | 0.1148 |
| Legacy p away | 0.0772 |
| Legacy p over 1 5 | 0.9694 |
| Legacy p under 3 5 | 0.2018 |
| Legacy p btts yes | 0.6451 |
| Legacy p over 2 5 | 0.8991 |
| Legacy goal margin distribution | {"-1": 0.05613529187099587, "-10": 2.473031721791593e-09, "-11": 2.0753096838962936e-10, "-12": 1.6043897853024667e-11, "-13": 1.1494568139303984e-12, "-14": 7.671450255904683e-14, "-15": 4.7910877770356145e-15, "-16": 2.8112700779293954e-16, "-17": 1.555356271460203e-17, "-18": 8.139541496972243e-19, "-19": 4.040707378292596e-20, "-2": 0.016247281205533426, "-20": 1.9077756202419474e-21, "-21": 8.5867833625305e-23, "-22": 3.6921664245482065e-24, "-23": 1.5184158919411453e-25, "-24": 5.911654185496504e-27, "-25": 1.9042181334543836e-28, "-3": 0.003913506081878722, "-4": 0.0007761731525634393, "-5": 0.00012996924054377776, "-6": 1.8757569132413045e-05, "-7": 2.3729194293601773e-06, "-8": 2.6678178268554714e-07, "-9": 2.6962241555148994e-08, "0": 0.11476157367746245, "1": 0.07606618122376248, "10": 0.007890827916782703, "11": 0.0033684801709055337, "12": 0.0013247049774400056, "13": 0.0004827920790769754, "14": 0.0001639091309714613, "15": 5.2073647549082106e-05, "16": 1.5543350456681955e-05, "17": 4.374517427008529e-06, "18": 1.1645507119510097e-06, "19": 2.9408580443019346e-07, "2": 0.11561335498305622, "20": 7.063210554207871e-08, "21": 1.617199363097863e-08, "22": 3.537305109488106e-09, "23": 7.400144336860588e-10, "24": 1.465604090791356e-10, "25": 2.4014997246581867e-11, "3": 0.14166139601995098, "4": 0.14292306401929827, "5": 0.12174257405993193, "6": 0.08937923883609009, "7": 0.057517670125352215, "8": 0.03289520982563124, "9": 0.016911833068405116} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.9327 |
| Legacy raw p draw | 0.0428 |
| Legacy raw p away | 0.0245 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 4.8560 |
| Legacy lambda away | 0.9546 |
| Legacy model home team | LASK Linz |
| Legacy model away team | ŠK Slovan Bratislava |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,423.1110 |
| Elo away rating | 1,382.3668 |
| Elo rating diff | 100.7442 |
| Elo home expectancy | 0.6411 |

</details>


---

## 2026-11-03 — Manchester United vs AS Roma

The model's most likely 1X2 outcome is **Manchester United win** at **47.2%**. Expected goals are 2.49 for Manchester United and 1.45 for AS Roma (3.94 combined). The most likely exact score is 1-1 at 8.3%. Goal-market probabilities: at least one goal: 98.0%; Over 2.5 goals: 73.5%; Under 3.5 goals: 45.8%; Double Chance 1X: 69.4%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 65.8%; BTTS Yes (both teams score): 71.4%; BTTS No (at least one team does not score): 28.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 47.2% | 2.12 |
| Draw | 22.2% | 4.50 |
| AS Roma win | 30.6% | 3.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 2.49 |
| AS Roma expected goals | 1.45 |
| Expected total goals | 3.94 |
| Over 0.5 | 98.0% |
| Under 0.5 | 2.0% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 54.2% |
| Under 3.5 | 45.8% |
| Over 4.5 | 34.2% |
| Under 4.5 | 65.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.34% |
| 2 | 2-2 | 7.91% |
| 3 | 1-2 | 7.22% |
| 4 | 2-1 | 6.80% |
| 5 | 3-1 | 5.65% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | bc0b6614c9714816038d5a0ff8963144 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 7.00 |
| Matched home-team name | Manchester United FC |
| Matched away-team name | AS Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4919 |
| Dc lambda away | 1.4460 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 71.4% |
| P btts no | 28.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 50.07 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.48 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.85 |
| Fair Under 3.5 odds | 2.18 |
| Fair Over 4.5 odds | 2.92 |
| Fair Under 4.5 odds | 1.52 |
| Goal margin distribution | {"-1": 0.17635405734391213, "-10": 4.218709626885773e-07, "-11": 5.401577125875893e-08, "-12": 6.364783134785344e-09, "-13": 6.944490789019141e-10, "-14": 7.053485954300494e-11, "-15": 6.699958259525481e-12, "-16": 5.970483225012552e-13, "-17": 4.9426263339527155e-14, "-18": 3.3083397864494022e-15, "-2": 0.08386837797595859, "-3": 0.03212458618264258, "-4": 0.009992858795379202, "-5": 0.00260093333129625, "-6": 0.0005799544264897188, "-7": 0.00011287449241049894, "-8": 1.9464592670623287e-05, "-9": 3.0105473290112688e-06, "0": 0.2223569003797397, "1": 0.16409054687952723, "10": 5.325335379538783e-05, "11": 1.1750379622949662e-05, "12": 2.3860465548485413e-06, "13": 4.48641759095534e-07, "14": 7.852845998681911e-08, "15": 1.2854623409574391e-08, "16": 1.974061731958261e-09, "17": 2.8162617199201127e-10, "18": 3.248548292741633e-11, "2": 0.13609860831868661, "3": 0.08983735743522368, "4": 0.04815852352155735, "5": 0.021601137398222753, "6": 0.008300519091632189, "7": 0.0027840125058179745, "8": 0.000827341248700848, "9": 0.00022052041596310655} |
| Raw goal margin distribution | {"-1": 0.12397637617475013, "-10": 2.965740281522848e-07, "-11": 3.7972926043237017e-08, "-12": 4.474423554940075e-09, "-13": 4.881956306355687e-10, "-14": 4.9585795823702476e-11, "-15": 4.7100506676646044e-12, "-16": 4.197231894731589e-13, "-17": 3.474651566844154e-14, "-18": 2.3257529997106275e-15, "-2": 0.05895921950259858, "-3": 0.02258348824530156, "-4": 0.007024949920268219, "-5": 0.0018284483722277186, "-6": 0.0004077062315753004, "-7": 7.93504314126917e-05, "-8": 1.3683550576415364e-05, "-9": 2.1164057905712524e-06, "0": 0.17789100775938824, "1": 0.21111037451755676, "10": 6.851299893780126e-05, "11": 1.5117428091367193e-05, "12": 3.069763562798194e-06, "13": 5.771991841578202e-07, "14": 1.0103063773853952e-07, "15": 1.65380907912373e-08, "16": 2.5397252887483705e-09, "17": 3.6232560481884263e-10, "18": 4.1794134991978624e-11, "2": 0.17509740030649462, "3": 0.11558007779535243, "4": 0.061958254940260644, "5": 0.027790901382588808, "6": 0.010679016722463195, "7": 0.003581765884394911, "8": 0.0010644142772910136, "9": 0.000283710113032399} |
| Unadjusted home-win probability | 60.7% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 21.5% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.6% |
| Raw p btts yes | 69.8% |
| P home draw | 69.4% |
| P draw away | 52.8% |
| P home away | 77.8% |
| Raw p home draw | 78.5% |
| Raw p draw away | 39.3% |
| Raw p home away | 82.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.7351 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.40 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.88 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.55 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +5.8% |
| Draw probability edge | -1.9% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | +10.1% |
| Under 2.5 probability edge | -10.1% |
| Raw edge prob home | 0.1932 |
| Raw edge prob draw | -0.0635 |
| Raw edge prob away | -0.1297 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.026807285801520857, 0.05238703223735688, 0.03202835440859688, 0.014500210582162595, 0.00492351490131407, 0.0013374150035190097, 0.00030274423311558014, 5.874065402943974e-05, 9.972630527954283e-06, 1.50497109393197e-06, 2.044038620000754e-07, 2.5238140313794495e-08, 2.8565185131237977e-09, 2.984383494199937e-10, 2.8952597464844505e-11, 2.6215443652524704e-12, 2.225349189523882e-13, 1.7779116879092187e-14], [0.05716798391092398, 0.09018855641555401, 0.07094901676942711, 0.032120778689708133, 0.010906540399843146, 0.002962633618381725, 0.0006706371922248762, 0.00013012194115921214, 2.2091310765975937e-05, 3.333802855391849e-06, 4.5279419753411986e-07, 5.590737561814699e-08, 6.327742515406926e-09, 6.610988247324968e-10, 6.413561860987648e-11, 5.807229205699391e-12, 4.929580051199318e-13, 3.9384192066443944e-14], [0.05929255439292122, 0.08053063048605297, 0.07140695818291674, 0.035576877238679784, 0.012080051129901384, 0.003281404027048823, 0.0007427957239131961, 0.00014412266811462124, 2.4468268928189935e-05, 3.692509950334384e-06, 5.015134824617255e-07, 6.192283998833677e-08, 7.00858845432469e-09, 7.322310569537825e-10, 7.10364170169218e-11, 6.432069488223245e-12, 5.459987941573671e-13, 4.362181190649068e-14], [0.04378150250096713, 0.059463655025976045, 0.04038150893713821, 0.02387100579107559, 0.008919885374658949, 0.0024229821111244523, 0.0005484788634455567, 0.0001064198872710343, 1.8067320395320638e-05, 2.7265418951947097e-06, 3.7031654330763925e-07, 4.572370007624468e-08, 5.1751275701135825e-09, 5.406779346840752e-10, 5.2453146961356246e-11, 4.749427129060585e-12, 4.031644076845459e-13, 3.221025787529148e-14], [0.024246129815976947, 0.03293088214732779, 0.022363218526665646, 0.01012450948290158, 0.004488729449307526, 0.0013418438256388215, 0.0003037467643812978, 5.8935172490211646e-05, 1.0005654687664395e-05, 1.5099547745792973e-06, 2.0508074116100815e-07, 2.5321715893394345e-08, 2.865977815093109e-09, 2.994266218409203e-10, 2.9048473392466756e-11, 2.63022555519153e-12, 2.2327183873337882e-13, 1.7837992056877434e-14], [0.010741975993906937, 0.014589658150377275, 0.009907773256317436, 0.00448555042148403, 0.0015230588697752875, 0.0005402019100943211, 0.0001345715986829685, 2.6110567455159416e-05, 4.432893136924031e-06, 6.689685349175973e-07, 9.085872323064716e-08, 1.1218502347213217e-08, 1.2697393407715514e-09, 1.3265760796316254e-10, 1.2869600476852406e-11, 1.165291945018382e-12, 9.891808507141652e-14, 7.902922400762509e-15], [0.003965926697355385, 0.005386487066875782, 0.003657939888421003, 0.0016560606892984772, 0.0005623117978211769, 0.0001527453963551673, 4.514673097816058e-05, 9.639995156594327e-06, 1.6366196729747398e-06, 2.4698250804370605e-07, 3.35449489323416e-08, 4.141859746139218e-09, 4.687864833345996e-10, 4.89770549968489e-11, 4.751443509499314e-12, 4.302246102191041e-13, 3.652045719135133e-14, 2.9177509756203136e-15], [0.001255042401168044, 0.0017045876482740775, 0.0011575780419627044, 0.0005240708017531266, 0.00017794709857174392, 4.833723960071858e-05, 1.0941869573273106e-05, 2.7720618968950974e-06, 5.179185700882397e-07, 7.815916520806586e-08, 1.0615509682309396e-08, 1.3107175189501543e-09, 1.4835042565756673e-10, 1.549909652802553e-11, 1.503624127786538e-12, 1.3614727882162504e-13, 1.1557127950890389e-14, 9.233406136565261e-16], [0.0003475202910476133, 0.0004719990297483643, 0.00032053248374621393, 0.0001451148083804198, 4.9273416921354415e-05, 1.33845450630562e-05, 3.0297954038604272e-06, 5.878631006992847e-07, 1.3031537067185764e-07, 2.164221369402857e-08, 2.939426597046871e-09, 3.629366890256752e-10, 4.107812059064606e-11, 4.291688098650375e-12, 4.1635238301771597e-13, 3.7699078467307166e-14, 3.200159982985441e-15, 2.5567231712280103e-16], [8.553609385090231e-05, 0.00011617437699647721, 7.889351303582612e-05, 3.5717493880329025e-05, 1.2127797204112505e-05, 3.2943736874010334e-06, 7.457316038508129e-07, 1.4469230904853024e-07, 2.4564979097004637e-08, 4.840423036156494e-09, 7.234888889937994e-10, 8.933057290223832e-11, 1.0110667113762232e-11, 1.0563246102215766e-12, 1.0247791978273539e-13, 9.278974485637482e-15, 7.876638909842571e-16, 6.292930765731112e-17], [1.894790372180352e-05, 2.5734877654183823e-05, 1.7476443241415512e-05, 7.912117619121812e-06, 2.6865422938489447e-06, 7.297676646460418e-07, 1.651940133799116e-07, 3.20521526960992e-08, 5.4416192966385955e-09, 8.211955434092913e-10, 1.4563173161392413e-10, 1.978845442387836e-11, 2.2397088575111615e-12, 2.3399638810182736e-13, 2.270084674475104e-14, 2.055472810079411e-15, 1.7448282823770087e-16, 1.394006213153614e-17], [3.815752873088004e-06, 5.182522287915307e-06, 3.519428296073445e-06, 1.593352276887156e-06, 5.410192930540606e-07, 1.4696153748425356e-07, 3.3266979842524653e-08, 6.454703144710442e-09, 1.095840192680875e-09, 1.6537339961915386e-10, 2.246087096990108e-11, 3.6211235050209405e-12, 4.5103540916215987e-13, 4.712248928963719e-14, 4.571525296919198e-15, 4.1393372036134905e-16, 3.5137573154670657e-17, 2.8072673848466928e-18], [7.043860551575438e-07, 9.56690999539613e-07, 6.496846877493881e-07, 2.9413202639733685e-07, 9.98718885298429e-08, 2.7129025671058824e-08, 6.141067694281216e-09, 1.1915349438330154e-09, 2.02291546669501e-10, 3.05278461315703e-11, 4.146265448550271e-12, 5.119474169656892e-13, 7.565777057847281e-14, 8.69878774750663e-15, 8.439012632764822e-16, 7.64119559310077e-17, 6.486378275907087e-18, 5.182201428533109e-19], [1.2002705574319058e-07, 1.630197007592195e-07, 1.1070596821305916e-07, 5.0119960311188545e-08, 1.701812329187589e-08, 4.622773339472679e-09, 1.046435075009171e-09, 2.0303699949229914e-10, 3.447038533868454e-11, 5.201930763001834e-12, 7.065217013813546e-13, 8.723560142027485e-14, 9.873552780127111e-15, 1.3469129528860795e-15, 1.4380038222985613e-16, 1.3020561703093307e-17, 1.1052758372957725e-18, 8.830447099011169e-20], [1.8991657655386736e-08, 2.579430386534604e-08, 1.7516799322387982e-08, 7.930388044910986e-09, 2.692745977106966e-09, 7.314528223499705e-10, 1.6557547446372802e-10, 3.212616657018545e-11, 5.454184921458416e-12, 8.230918236412736e-13, 1.1179161394615229e-13, 1.3803126863999741e-14, 1.5622738813469912e-15, 1.6322052048642083e-16, 2.067550625612356e-17, 2.060219246526142e-18, 1.7488573877546863e-19, 1.3972252106828615e-20], [2.8046803368488155e-09, 3.80929238334916e-09, 2.5868738535360774e-09, 1.1711565054898751e-09, 3.9766363901249827e-10, 1.0802065756464675e-10, 2.4452119236738357e-11, 4.744379311838121e-12, 8.054718277007725e-13, 1.2155386828663346e-13, 1.6509340424554024e-14, 2.038440203849673e-15, 2.3071597620882665e-16, 2.4104340583911592e-17, 2.338450374885879e-18, 2.7646892803307694e-19, 2.5827055312347202e-20, 2.063416551445765e-21], [3.883069313236346e-10, 5.273950890085128e-10, 3.581517061286713e-10, 1.621461750102464e-10, 5.5056380342233796e-11, 1.4955419163959493e-11, 3.385386655452316e-12, 6.56857520413566e-13, 1.1151726974830146e-13, 1.6829087067345248e-14, 2.2857119345153273e-15, 2.822212748611922e-16, 3.194253960137326e-17, 3.3372368325706264e-18, 3.237575695149482e-19, 2.93149805678171e-20, 3.2492195499165773e-21, 2.856792407346249e-22], [5.0598539014929345e-11, 6.872249459085341e-11, 4.666914652808845e-11, 2.1128542656735595e-11, 7.174150611402563e-12, 1.9487737637666213e-12, 4.4113458954395727e-13, 8.559216483878568e-14, 1.4531316515426795e-14, 2.1929230458495357e-15, 2.9784089637862215e-16, 3.677499172685504e-17, 4.162289431060783e-18, 4.348604015367116e-19, 4.2187400458292364e-20, 3.819903968560211e-21, 3.242600168498719e-22, 3.382625427754001e-23]] |
| Legacy trial inputs | {"lambda_home": 2.2151939454742435, "lambda_away": 1.358191282372333, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4936 |
| Legacy p draw | 0.2174 |
| Legacy p away | 0.2891 |
| Legacy p over 1 5 | 0.8636 |
| Legacy p under 3 5 | 0.5276 |
| Legacy p btts yes | 0.6667 |
| Legacy p over 2 5 | 0.6821 |
| Legacy goal margin distribution | {"-1": 0.16931940734412212, "-10": 2.678907552163664e-07, "-11": 3.23532990945078e-08, "-12": 3.593634356763411e-09, "-13": 3.694270399178349e-10, "-14": 3.5338035722576555e-11, "-15": 3.1581241822788928e-12, "-16": 2.6191911101883214e-13, "-17": 1.7779116879092187e-14, "-2": 0.07898374148105036, "-3": 0.02930025990943098, "-4": 0.008746073651926626, "-5": 0.002171847292358067, "-6": 0.00046027776905307365, "-7": 8.492143326347169e-05, "-8": 1.3856674092161035e-05, "-9": 2.0251759972842682e-06, "0": 0.21735079164846768, "1": 0.18989199222497866, "10": 2.4833034895392895e-05, "11": 4.8914932890783524e-06, "12": 8.861507168987471e-07, "13": 1.4857755378769436e-07, "14": 2.31802302875213e-08, "15": 3.3787445723854166e-09, "16": 4.57029425914488e-10, "17": 5.0598539014929345e-11, "2": 0.14621880750340951, "3": 0.08846832914839077, "4": 0.04307053830346098, "5": 0.017444047969819656, "6": 0.006029604176770093, "7": 0.0018144162892739216, "8": 0.00048286912865782645, "9": 0.00011510230652717922} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5731 |
| Legacy raw p draw | 0.1933 |
| Legacy raw p away | 0.2336 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.2152 |
| Legacy lambda away | 1.3582 |
| Legacy model home team | Manchester United FC |
| Legacy model away team | AS Roma |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,468.3262 |
| Elo away rating | 1,438.9525 |
| Elo rating diff | 89.3736 |
| Elo home expectancy | 0.6259 |

</details>


---

## 2026-11-03 — Shakhtar Donetsk vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **46.9%**. Expected goals are 1.08 for Shakhtar Donetsk and 1.38 for Sporting Lisbon (2.46 combined). The most likely exact score is 0-1 at 13.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 44.7%; Under 3.5 goals: 76.5%; Double Chance 1X: 53.1%; Double Chance X2: 72.5%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.8%; BTTS No (at least one team does not score): 51.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Shakhtar Donetsk win | 27.5% | 3.64 |
| Draw | 25.6% | 3.90 |
| Sporting Lisbon win | 46.9% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Shakhtar Donetsk expected goals | 1.08 |
| Sporting Lisbon expected goals | 1.38 |
| Expected total goals | 2.46 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.7% |
| Under 2.5 | 55.3% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.14% |
| 2 | 1-1 | 12.10% |
| 3 | 1-2 | 9.31% |
| 4 | 1-0 | 8.99% |
| 5 | 0-2 | 8.59% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T17:45:00+00:00 |
| Fixture id | 55e0f74a61f7d72defa7ea0c83532ea5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 11.00 |
| Matched home-team name | FK Shakhtar Donetsk |
| Matched away-team name | Sporting Clube de Portugal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0835 |
| Dc lambda away | 1.3790 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.8% |
| P btts no | 51.2% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.67 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.25 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.59 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.2507251576026549, "-10": 7.08788201311057e-07, "-11": 8.787098323955778e-08, "-12": 1.0001061238224743e-08, "-13": 1.0473150427279685e-09, "-14": 9.32132905604663e-11, "-2": 0.1375387237282628, "-3": 0.0566394509080859, "-4": 0.018227415654362613, "-5": 0.004796281438360231, "-6": 0.001065416062888039, "-7": 0.00020454005933029428, "-8": 3.455232421760336e-05, "-9": 5.208884197205578e-06, "0": 0.25622885743172874, "1": 0.17051791358377397, "10": 5.4587633339163286e-08, "11": 5.3169904999095685e-09, "12": 4.754546475992239e-10, "13": 3.911856941083508e-11, "14": 2.7354329512806738e-12, "2": 0.0729561452416298, "3": 0.02360470274786081, "4": 0.005968252803506067, "5": 0.0012338699416373684, "6": 0.00021534092682060654, "7": 3.248092041780809e-05, "8": 4.310918656726914e-06, "9": 5.105989019209029e-07} |
| Raw goal margin distribution | {"-1": 0.23648869749992407, "-10": 6.685423997100761e-07, "-11": 8.288156869879516e-08, "-12": 9.433189586794399e-09, "-13": 9.878473013838163e-10, "-14": 8.792053372347041e-11, "-2": 0.12972911829552428, "-3": 0.05342339835554778, "-4": 0.01719244222680388, "-5": 0.004523943113831603, "-6": 0.001004920524996498, "-7": 0.00019292604172668114, "-8": 3.2590403882667976e-05, "-9": 4.9131178179466484e-06, "0": 0.25606662589167023, "1": 0.18716766462149198, "10": 5.99176921331843e-08, "11": 5.836153362232032e-09, "12": 5.218791043960395e-10, "13": 4.293819415261983e-11, "14": 3.002526751937683e-12, "2": 0.08007974668276496, "3": 0.025909518798041594, "4": 0.006551006375961195, "5": 0.0013543477665732978, "6": 0.00023636729727307578, "7": 3.565243024376399e-05, "8": 4.731846410707988e-06, "9": 5.604549224318424e-07} |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 44.3% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.9% |
| P home draw | 53.1% |
| P draw away | 72.5% |
| P home away | 74.4% |
| Raw p home draw | 55.7% |
| Raw p draw away | 69.9% |
| Raw p home away | 74.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.4473 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.97, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.80 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.08 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | 0.0383 |
| Raw edge prob draw | -0.0002 |
| Raw edge prob away | -0.0381 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.09641412529589434, 0.1468259156178899, 0.0813620162221425, 0.031670058336461186, 0.009245646570781745, 0.002159313496771034, 0.00042025497636841765, 7.010729981404704e-05, 1.0233440513847518e-05, 1.3277844425232547e-06, 1.5505150697646883e-07, 1.6460071684245116e-08, 1.6017653404725615e-09, 1.4388116828255893e-10], [0.10724735087639922, 0.12245446540093798, 0.08731354067784437, 0.033986681442116945, 0.009921953454875511, 0.00231726443850375, 0.0004509960750483981, 7.523555656996765e-05, 1.098200322544314e-05, 1.4249101278061993e-06, 1.663933207430351e-07, 1.7664104274882052e-08, 1.718932368021268e-09, 1.5440588646813853e-10], [0.0543715675293218, 0.06349218451508216, 0.04038307107954017, 0.01823638124022803, 0.005323865648932776, 0.0012433846419206364, 0.0002419929223286001, 4.036946928070576e-05, 5.8926611573324765e-06, 7.645702145998444e-07, 8.928238663328952e-08, 9.478105132815407e-09, 9.223350047515338e-10, 8.285023697191399e-11], [0.019449592056272943, 0.02271218476300129, 0.013261032293536885, 0.005622961983830395, 0.0019044331392194264, 0.0004447788642722078, 8.656479541919368e-05, 1.4440814284313928e-05, 2.1079005230841363e-06, 2.734991733376924e-07, 3.193775858846529e-08, 3.3904720183083136e-09, 3.299341990087675e-10, 2.963687427257386e-11], [0.005218076032359623, 0.006093387800188693, 0.003557764840262247, 0.0013848553080454725, 0.00044040625446108427, 0.00011932846327285307, 2.3224224082238496e-05, 3.874285213114884e-06, 5.655226683562318e-07, 7.337631952045479e-08, 8.56849090384951e-09, 9.096201465785792e-10, 8.851711291025031e-11, 7.951193159647572e-12], [0.0011199542859596043, 0.0013078222203959191, 0.0007636021316244175, 0.0002972311304130388, 8.677262139643932e-05, 2.207607102746985e-05, 4.984609104522279e-06, 8.315368159738793e-07, 1.2137798152137453e-07, 1.5748740153507047e-08, 1.8390529483397874e-09, 1.9523153274085401e-10, 1.899840465524531e-11, 1.7065624959115713e-12], [0.00020031291144808065, 0.00023391461589839307, 0.00013657643717358354, 5.316219943301102e-05, 1.5519987417173666e-05, 3.624680874729363e-06, 7.684711985828486e-07, 1.4872710669728397e-07, 2.1709436866349768e-08, 2.8167899630700424e-09, 3.2892954204240327e-10, 3.49187437559414e-11, 3.3980188272597256e-12, 3.052325495868321e-13], [3.0709362487257746e-05, 3.586073747699126e-05, 2.0938117698263572e-05, 8.150134912453576e-06, 2.379322011478017e-06, 5.556887874975821e-07, 1.0815056665333942e-07, 1.965349663026813e-08, 3.3282076592240553e-09, 4.318334919155113e-10, 5.042718647702345e-11, 5.353286275202543e-12, 5.209399192018244e-13, 4.6794272722661865e-14], [4.1194639944162995e-06, 4.8104879061223496e-06, 2.8087141829999506e-06, 1.0932883199844578e-06, 3.191707858303087e-07, 7.454208641247356e-08, 1.4507704791625447e-08, 2.4201879017097747e-09, 3.8482933296055083e-10, 5.792769297204202e-11, 6.764483603917517e-12, 7.181090155046414e-13, 6.988074862499964e-14, 6.277151526863751e-15], [4.911997073880762e-07, 5.735965298116379e-07, 3.3490754784999674e-07, 1.3036232470900858e-07, 3.80575232164116e-08, 8.888304663794448e-09, 1.7298804791541192e-09, 2.885801625539995e-10, 4.2123543979097737e-11, 5.953761898664908e-12, 8.065885201034583e-13, 8.562641614703554e-14, 8.332492606607483e-15, 7.484796559468359e-16], [5.2713031981503474e-08, 6.155543614066543e-08, 3.594055944075737e-08, 1.3989815727109121e-08, 4.084138097538724e-09, 9.538472457471922e-10, 1.8564189605631508e-10, 3.0968942182040294e-11, 4.520482580805276e-12, 5.865306428828723e-13, 7.461047000592947e-14, 9.188987584746627e-15, 8.942003479467131e-16, 8.032299581615757e-17], [5.142629175224086e-09, 6.005285028979288e-09, 3.506324007671749e-09, 1.3648320312799463e-09, 3.9844431152085266e-10, 9.305635609061283e-11, 1.8111032412973595e-11, 3.021298142119236e-12, 4.410136304490834e-13, 5.722132616675882e-14, 6.681997897556038e-15, 7.727210067055078e-16, 8.723726609882511e-17, 7.836228845089336e-18], [4.599004778593873e-10, 5.370469774128823e-10, 3.1356724969146027e-10, 1.2205564157872503e-10, 3.563249906324618e-11, 8.321942176991852e-12, 1.619652550757846e-12, 2.7019184389389094e-13, 3.943943311393804e-14, 5.117249241812878e-15, 5.975647711382061e-16, 6.343671958252646e-17, 6.724632266473407e-18, 7.007865563853463e-19], [3.79647379092429e-11, 4.433317364080881e-11, 2.588494473166902e-11, 1.007568086132225e-11, 2.9414591919625936e-12, 6.869754846003169e-13, 1.3370215416988232e-13, 2.2304309372304918e-14, 3.255721212617589e-15, 4.2242840708918913e-16, 4.9328911388943985e-17, 5.236694782276568e-18, 5.095941476921215e-19, 4.9864348466094653e-20]] |
| Legacy trial inputs | {"lambda_home": 1.0731486845096418, "lambda_away": 1.1677460739170662, "rho": 0.05, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3011 |
| Legacy p draw | 0.2653 |
| Legacy p away | 0.4335 |
| Legacy p over 1 5 | 0.6495 |
| Legacy p under 3 5 | 0.8106 |
| Legacy p btts yes | 0.4442 |
| Legacy p over 2 5 | 0.3913 |
| Legacy goal margin distribution | {"-1": 0.2544047358616171, "-10": 1.7366758313037498e-07, "-11": 1.8261854289238297e-08, "-12": 1.7561712269407e-09, "-13": 1.4388116828255893e-10, "-2": 0.121141420086484, "-3": 0.042925959759814836, "-4": 0.011819926351660376, "-5": 0.0026528621924416513, "-6": 0.0005016654604363051, "-7": 8.188673993646228e-05, "-8": 1.1751113723980721e-05, "-9": 1.5039937537912734e-06, "0": 0.26533789460124513, "1": 0.18547593090880632, "10": 5.904195994103554e-08, "11": 5.705561097368637e-09, "12": 5.042336515001961e-10, "13": 3.79647379092429e-11, "2": 0.0809548387400663, "3": 0.026362199812912556, "4": 0.00667095307263513, "5": 0.0013759393376311874, "6": 0.00023911690426919134, "7": 3.586915465691305e-05, "8": 4.730402235174522e-06, "9": 5.563864646371841e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3392 |
| Legacy raw p draw | 0.2744 |
| Legacy raw p away | 0.3864 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0731 |
| Legacy lambda away | 1.1677 |
| Legacy model home team | FK Shakhtar Donetsk |
| Legacy model away team | Sporting Clube de Portugal |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,464.4999 |
| Elo away rating | 1,487.5305 |
| Elo rating diff | 36.9694 |
| Elo home expectancy | 0.5530 |

</details>


---

## 2026-11-03 — Villarreal vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **67.1%**. Expected goals are 1.05 for Villarreal and 3.83 for Paris Saint Germain (4.88 combined). The most likely exact score is 2-2 at 6.3%. Goal-market probabilities: at least one goal: 98.7%; Over 2.5 goals: 82.4%; Under 3.5 goals: 32.4%; Double Chance 1X: 32.9%; Double Chance X2: 84.3%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 51.5%; BTTS Yes (both teams score): 67.7%; BTTS No (at least one team does not score): 32.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 15.7% | 6.39 |
| Draw | 17.3% | 5.79 |
| Paris Saint Germain win | 67.1% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 1.05 |
| Paris Saint Germain expected goals | 3.83 |
| Expected total goals | 4.88 |
| Over 0.5 | 98.7% |
| Under 0.5 | 1.3% |
| Over 1.5 | 93.8% |
| Under 1.5 | 6.2% |
| Over 2.5 | 82.4% |
| Under 2.5 | 17.6% |
| Over 3.5 | 67.6% |
| Under 3.5 | 32.4% |
| Over 4.5 | 48.5% |
| Under 4.5 | 51.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.35% |
| 2 | 1-1 | 6.00% |
| 3 | 1-3 | 5.83% |
| 4 | 1-4 | 5.59% |
| 5 | 0-3 | 5.57% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-03T20:00:00+00:00 |
| Fixture id | a341241606cb5b1b59e425d00be64883 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 3.00 |
| Matched home-team name | Villarreal CF |
| Matched away-team name | Paris Saint-Germain FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 3.8347 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | NO_SHOT_DATA |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T09:33:34.428047+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 67.7% |
| P btts no | 32.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 79.57 |
| Fair Over 1.5 odds | 1.07 |
| Fair Under 1.5 odds | 16.19 |
| Fair Over 2.5 odds | 1.21 |
| Fair Under 2.5 odds | 5.67 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.08 |
| Fair Over 4.5 odds | 2.06 |
| Fair Under 4.5 odds | 1.94 |
| Goal margin distribution | {"-1": 0.11266794435572954, "-10": 0.0016079891553518679, "-11": 0.0005443895998985389, "-12": 0.00016968445683383248, "-13": 4.899084686956008e-05, "-14": 1.3170881289807228e-05, "-15": 3.312396897167409e-06, "-16": 7.824589671220959e-07, "-17": 1.7423626501947613e-07, "-18": 3.669203025148688e-08, "-19": 7.328272734017746e-09, "-2": 0.14047386030034537, "-20": 1.390708792078715e-09, "-21": 2.484493184816871e-10, "-22": 3.661730668526842e-11, "-3": 0.13983758521677436, "-4": 0.11371219463303413, "-5": 0.0776624266752381, "-6": 0.045554440462129434, "-7": 0.02336379872718578, "-8": 0.010630287387107744, "-9": 0.0043420639752107535, "0": 0.17284537467170744, "1": 0.1082432586373916, "10": 1.2768053714145972e-08, "11": 1.181236666048919e-09, "12": 1.0061313369875154e-10, "13": 7.938036176393061e-12, "14": 5.831744335131647e-13, "15": 4.007850596532412e-14, "16": 2.5871180160573624e-15, "17": 1.5742682437227572e-16, "18": 9.059358347683358e-18, "19": 4.944391300042547e-19, "2": 0.03587178538559048, "20": 2.564087985285164e-20, "21": 1.2517570525896342e-21, "22": 5.0414347246810035e-23, "3": 0.009758136860200028, "4": 0.0021683807562320797, "5": 0.00040469232987681077, "6": 6.486796102995653e-05, "7": 9.091352573024815e-06, "8": 1.1303568325152981e-06, "9": 1.2616889219217706e-07} |
| Raw goal margin distribution | {"-1": 0.14417212167427676, "-10": 0.0020576146079700594, "-11": 0.0006966116590090403, "-12": 0.0002171315745287829, "-13": 6.268965299929069e-05, "-14": 1.6853719225374135e-05, "-15": 4.238608339068639e-06, "-16": 1.0012499123697647e-06, "-17": 2.2295615797468845e-07, "-18": 4.695184491155223e-08, "-19": 9.377402191126098e-09, "-2": 0.17975311962143603, "-20": 1.7795783737032636e-09, "-21": 3.179206435234068e-10, "-22": 4.685622716382117e-11, "-3": 0.17893892948695303, "-4": 0.14550836490564886, "-5": 0.0993783714806245, "-6": 0.058292359647331524, "-7": 0.02989677722559643, "-8": 0.013602725206095324, "-9": 0.005556190621309974, "0": 0.08327553418592243, "1": 0.040503758913157835, "10": 4.777703257811678e-09, "11": 4.420092830104461e-10, "12": 3.764862737995774e-11, "13": 2.9703494479007083e-12, "14": 2.1821919403279173e-13, "15": 1.4997055370044843e-14, "16": 9.680788043651578e-16, "17": 5.890785459627723e-17, "18": 3.3899392076848968e-18, "19": 1.850151554103881e-19, "2": 0.013422934280921494, "20": 9.59461151627221e-21, "21": 4.683974458472321e-22, "22": 1.8864644249943494e-23, "3": 0.0036514165205537206, "4": 0.0008113906813963544, "5": 0.00015143262286887744, "6": 2.4273070561808342e-05, "7": 3.4019111901081607e-06, "8": 4.2297045752671775e-07, "9": 4.721138716648753e-08} |
| Unadjusted home-win probability | 5.9% |
| Unadjusted draw probability | 8.3% |
| Unadjusted away-win probability | 85.8% |
| Raw p over 1 5 | 95.4% |
| Raw p under 3 5 | 28.2% |
| Raw p btts yes | 63.4% |
| P home draw | 32.9% |
| P draw away | 84.3% |
| P home away | 82.7% |
| Raw p home draw | 14.2% |
| Raw p draw away | 94.1% |
| Raw p home away | 91.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.8235 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T09:33:35Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 5.00 |
| Reference draw odds | 4.70 |
| Reference away odds | 1.69 |
| Market reference 1x2 last update utc | 2026-11-01T09:33:37Z |
| Market reference home last update utc | 2026-11-01T09:33:37Z |
| Market reference draw last update utc | 2026-11-01T09:33:37Z |
| Market reference away last update utc | 2026-11-01T09:33:37Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.32 |
| Market reference over 2 5 last update utc | 2026-11-01T09:33:35Z |
| Market reference under 2 5 last update utc | 2026-11-01T09:33:35Z |
| Home probability edge | -4.2% |
| Draw probability edge | -3.8% |
| Away probability edge | +8.0% |
| Over 2.5 probability edge | +9.6% |
| Under 2.5 probability edge | -9.6% |
| Raw edge prob home | -0.1399 |
| Raw edge prob draw | -0.1280 |
| Raw edge prob away | 0.2679 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.00695918914857037, 0.018892561982393377, 0.03602429619107029, 0.04857198593086967, 0.04911763865049655, 0.03973553694155173, 0.026787947931638138, 0.015479360570011112, 0.007826627061333927, 0.003517578039489071, 0.0014228376604938412, 0.0005232078811543057, 0.0001763618483172932, 5.487479362288195e-05, 1.5854643268331662e-05, 4.27540072224508e-06, 1.080857534115375e-06, 2.5717641812955486e-07, 5.779233593205098e-08, 1.2303488235806762e-08, 2.488340872728951e-09, 4.792942170407377e-10, 8.812337440532656e-11, 1.549797276101276e-11], [0.015550093788471013, 0.04299398761063837, 0.04370603979649362, 0.05892937196689883, 0.05959137850139399, 0.04820865755964419, 0.032500152457018504, 0.018780146196579438, 0.009495560218599554, 0.0042676588312998125, 0.001726240509562225, 0.0006347756068371864, 0.00021396887034949122, 6.657617684424208e-05, 1.9235453372068384e-05, 5.187077996508371e-06, 1.311337274983221e-06, 3.120161655864971e-07, 7.011584961386873e-08, 1.492705766179981e-08, 3.018949340020459e-09, 5.814978872343475e-10, 1.0691461363553928e-10, 1.8802727211245297e-11], [0.007846127241050849, 0.031737079326363285, 0.05552412113340343, 0.03574767238625593, 0.0361492580798212, 0.029244284116779328, 0.019715207608006827, 0.011392392133050622, 0.005760186550250875, 0.0025888426206766854, 0.0010471701655055219, 0.0003850668974505397, 0.00012979756652433582, 4.038636895526802e-05, 1.1668590083261815e-05, 3.1465796880593513e-06, 7.95482010572201e-07, 1.8927491154779495e-07, 4.253360145240442e-08, 9.055035700779287e-09, 1.831351809049905e-09, 3.527476243566588e-10, 6.485642819497913e-11, 1.1406090203935847e-11], [0.003173072858262852, 0.012834875336221404, 0.02595812202473831, 0.030275877980155536, 0.014619216096737326, 0.01182675749951919, 0.007973078722032713, 0.004607227127153838, 0.0023294921226237773, 0.0010469606216688204, 0.00042348882806330425, 0.0001557259120809451, 5.249177368066442e-05, 1.633275719838915e-05, 4.718925063269083e-06, 1.2725165292125824e-06, 3.2170296242161803e-07, 7.654516248986715e-08, 1.720112511388716e-08, 3.661970693314391e-09, 7.40621779471492e-10, 1.4265559023905212e-10, 2.6228757916727262e-11, 4.612766799861294e-12], [0.0009624230261491315, 0.003892939151764597, 0.007873344063670263, 0.010615723206947304, 0.009286120742238535, 0.00358716747161319, 0.0024183102292787994, 0.0013974155879607764, 0.0007065570058399268, 0.0003175530644187977, 0.00012844816921984197, 4.7233142839596725e-05, 1.59212517109796e-05, 4.953879822614068e-06, 1.4312946290331265e-06, 3.8596630571541414e-07, 9.757555292457327e-08, 2.321687216501737e-08, 5.2172640291468945e-09, 1.1107103661838186e-09, 2.2463759455593988e-10, 4.32687905345241e-11, 7.955430490861593e-12, 1.3990958231174013e-12], [0.0002335296093438324, 0.0009446122283134416, 0.001910447810850268, 0.0025758794480843137, 0.002604816614217043, 0.0018228539775926743, 0.0005867971024917705, 0.00033907949776847357, 0.0001714443410743773, 7.705347967034984e-05, 3.116763623046577e-05, 1.1461007369646267e-05, 3.863253051214672e-06, 1.2020469048213464e-06, 3.473001647845426e-07, 9.365378647916528e-08, 2.3676470883244576e-08, 5.6335176316137605e-09, 1.2659564427145256e-09, 2.695111721785214e-10, 5.4507766621595816e-11, 1.0499066913161932e-11, 1.9303658830010604e-12, 3.3948720274754336e-13], [4.7221160340907016e-05, 0.0001910065520963393, 0.000386304600314178, 0.0005208590755519494, 0.0005267103531077355, 0.0004261018906534629, 0.0002484888705786079, 6.85640136915777e-05, 3.466712740265256e-05, 1.558069971753029e-05, 6.302292681520117e-06, 2.3174879973081093e-06, 7.811741401079179e-07, 2.4306146783420244e-07, 7.022628442617845e-08, 1.8937386485130653e-08, 4.787531786765419e-09, 1.139132806812901e-09, 2.559843795996385e-10, 5.449685935272547e-11, 1.1021814298817492e-11, 2.1229775681523227e-12, 3.90332160165612e-13, 6.864645421054456e-14], [8.184357032462504e-06, 3.3105197047473975e-05, 6.695419488697026e-05, 9.027513528130374e-05, 9.128927691329374e-05, 7.38518490468812e-05, 4.978766210792763e-05, 2.4886763734189625e-05, 6.0084958926217544e-06, 2.7004420980606137e-06, 1.0923114353027224e-06, 4.016663091606646e-07, 1.3539286245856117e-07, 4.212733908332637e-08, 1.2171598085640473e-08, 3.282222019474044e-09, 8.29773541443618e-10, 1.9743414882313844e-10, 4.4367134188397426e-11, 9.445378954489951e-12, 1.910297475025792e-12, 3.6795382121552223e-13, 6.765225032558668e-14, 1.1897782397036587e-14], [1.2411964701276618e-06, 5.020559777050959e-06, 1.0153920463675442e-05, 1.3690651422832427e-05, 1.3844450799966487e-05, 1.1199982354852119e-05, 7.550534540362702e-06, 4.363060841571902e-06, 1.9082972017419665e-06, 4.095348219294986e-07, 1.6565419768471354e-07, 6.09145963601029e-08, 2.053296823409519e-08, 6.388810307113805e-09, 1.8458804423838867e-09, 4.977644998364303e-10, 1.2583908382296814e-10, 2.994182287380088e-11, 6.7284858328999704e-12, 1.432436411416384e-12, 2.8970565109650363e-13, 5.580193804488493e-14, 1.0259783873950375e-14, 1.8043549975856337e-15], [1.673185046217472e-07, 6.767925743245614e-07, 1.3687911856980954e-06, 1.8455573944150114e-06, 1.8662901973299119e-06, 1.5098047283449543e-06, 1.0178438134442957e-06, 5.881589523940773e-07, 2.973831349397913e-07, 1.1561616435134533e-07, 2.233088258627642e-08, 8.211543794965386e-09, 2.7679304792264555e-09, 8.612385006125095e-10, 2.488324473710715e-10, 6.710074816588644e-11, 1.6963637776108173e-11, 4.036283658120868e-12, 9.070281901572289e-13, 1.930984530589906e-13, 3.9053540264218587e-14, 7.522335950331227e-15, 1.3830620186626288e-15, 2.432346427570429e-16], [2.02997143452884e-08, 8.211103703597935e-08, 1.6606692804741008e-07, 2.239100092315197e-07, 2.2642539136274957e-07, 1.8317522483155627e-07, 1.234886643754566e-07, 7.135767051119115e-08, 3.6079647639879075e-08, 1.621553898198798e-08, 5.673827395524832e-09, 9.962555770412798e-10, 3.3581580341599127e-10, 1.0448871501165748e-10, 3.018929444110767e-11, 8.140916769498712e-12, 2.058092748858942e-12, 4.896972122816821e-13, 1.1004409347872288e-13, 2.3427435276666402e-14, 4.738123337451913e-15, 9.126382724147903e-16, 1.6779831952323196e-16, 2.95101475955008e-17], [2.2389438059622952e-09, 9.056383486278791e-09, 1.8316243943266804e-08, 2.4696009004591194e-08, 2.4973441442632e-08, 2.0203192422633916e-08, 1.3620102012625501e-08, 7.870347911374018e-09, 3.979381297222966e-09, 1.7884823375600226e-09, 7.234295860506568e-10, 2.3011679266562385e-10, 3.7038585874337494e-11, 1.1524514940901562e-11, 3.3297086178445763e-12, 8.978971263284917e-13, 2.2699600269119828e-13, 5.4010835895804257e-14, 1.2137241799863461e-14, 2.5839137541582782e-15, 5.22588235372661e-16, 1.0065884535865344e-16, 1.8507206641290535e-17, 3.2548025577175156e-18], [2.2636428149880502e-10, 9.156289386941699e-10, 1.8518300409922182e-09, 2.4968444135691936e-09, 2.5248937082117527e-09, 2.042606484608058e-09, 1.3770352778922405e-09, 7.957170007391436e-10, 4.023280020502797e-10, 1.8082120606911548e-10, 7.314101319794029e-11, 2.6895517038459138e-11, 7.842298754254684e-12, 1.1651648144416888e-12, 3.366440447820064e-13, 9.07802318753746e-14, 2.295001192770411e-14, 5.460665885470415e-15, 1.2271134327207964e-15, 2.6124183146415636e-16, 5.283531909324435e-17, 1.0176926792639046e-17, 1.8711369721515e-18, 3.290708058130718e-19], [2.1125670389905573e-11, 8.545197603719207e-11, 1.7282386958356523e-10, 2.3302047366610843e-10, 2.356382018225322e-10, 1.906282698153567e-10, 1.2851317886111406e-10, 7.426107586389745e-11, 3.754765859554715e-11, 1.6875317844443105e-11, 6.82595737530957e-12, 2.510050720716627e-12, 8.46082791220767e-13, 2.277268510561611e-13, 3.141763833808216e-14, 8.4721548992635e-15, 2.1418325551137706e-15, 5.096220430273971e-16, 1.1452157442437295e-16, 2.4380652225806945e-17, 4.930908395613011e-18, 9.497717554199305e-19, 1.7462570802384821e-19, 3.0710858323221265e-20], [1.83074735746515e-12, 7.405255143761806e-12, 1.4976890044549632e-11, 2.019351852632083e-11, 2.0420370447063888e-11, 1.6519816639256854e-11, 1.113693237928448e-11, 6.435453450287262e-12, 3.253874337907287e-12, 1.4624124574461278e-12, 5.915364197383751e-13, 2.1752061067142306e-13, 7.332140498434999e-14, 2.281387389078201e-14, 5.70184926689982e-15, 7.34195644805353e-16, 1.8561088088740616e-16, 4.416376812468901e-17, 9.924422083682165e-18, 2.1128235843819956e-18, 4.273117656651838e-19, 8.230707472653353e-20, 1.513303708756624e-20, 2.6613982743756727e-21], [1.4807546632473683e-13, 5.989557238440855e-13, 1.2113686623104752e-12, 1.6333027385397118e-12, 1.651651094370306e-12, 1.3361644590021872e-12, 9.007831958708714e-13, 5.205157154954752e-13, 2.6318156788976154e-13, 1.1828361008548495e-13, 4.78449584229388e-14, 1.7593615923613667e-14, 5.930420268187761e-15, 1.845243693115964e-15, 5.331351348407314e-16, 1.2436288167525461e-16, 1.5012676451655643e-17, 3.572077017101668e-18, 8.0271230328553275e-19, 1.7089050340209028e-19, 3.456205396605264e-20, 6.657203913068283e-21, 1.2239982292005384e-21, 2.1526060870555132e-22], [1.1228172560518866e-14, 4.541723480838634e-14, 9.185489475345127e-14, 1.2384904432226176e-13, 1.2524035181283488e-13, 1.013178312875089e-13, 6.830401695763008e-14, 3.946933559694482e-14, 1.9956365037092548e-14, 8.969134577691258e-15, 3.6279571670939465e-15, 1.3340775515141895e-15, 4.496881474043812e-16, 1.3991996862652448e-16, 4.0426232924631406e-17, 1.0901433890275365e-17, 2.3840116541089363e-18, 2.7086119087089294e-19, 6.086755950493229e-20, 1.295817672418879e-20, 2.620749511102336e-21, 5.047982367488584e-22, 9.281256154273059e-23, 1.6322644932467718e-23], [8.013202341015685e-16, 3.2412887344528166e-15, 6.5554020808359516e-15, 8.838726396006173e-15, 8.938019743881279e-15, 7.230742834452667e-15, 4.874648173027041e-15, 2.816805412448671e-15, 1.4242245581056847e-15, 6.400996226897948e-16, 2.589161745401463e-16, 9.520902267283972e-17, 3.209286369696901e-17, 9.985658967295877e-18, 2.885096239517822e-18, 7.780018974516496e-19, 1.9668547278887544e-19, 4.0482571724452736e-20, 4.343931015380616e-21, 9.24785324609993e-22, 1.870348536628697e-22, 3.602590172758813e-23, 6.623747822018711e-24, 1.1648971003913198e-24], [5.4010668947210806e-17, 2.1846967710123408e-16, 4.418478861960318e-16, 5.957487468476352e-16, 6.024413273073754e-16, 4.873672732249246e-16, 3.2856153820036696e-16, 1.8985860851380062e-16, 9.599573034690598e-17, 4.314406069265807e-17, 1.7451494662237085e-17, 6.417288351810719e-18, 2.1631265041601923e-18, 6.730544141407559e-19, 1.9446155387321558e-19, 5.2438964018768004e-20, 1.3257014493632637e-20, 3.154339397147695e-21, 6.131696443283315e-22, 6.233247569337954e-23, 1.2606542469380408e-23, 2.4282215385651688e-24, 4.46454532882188e-25, 7.8516514333802e-26], [3.4488309514363837e-18, 1.3950299061718226e-17, 2.821403058771613e-17, 3.804131216030175e-17, 3.8468664368382905e-17, 3.1120653925951314e-17, 2.0980173445074338e-17, 1.212335003810119e-17, 6.12977125592975e-18, 2.7549477684292433e-18, 1.1143586278995393e-18, 4.0977353407062224e-19, 1.3812562934022528e-19, 4.2977636469533e-20, 1.241726938279282e-20, 3.3484703243714495e-21, 8.465216743374938e-22, 2.014191558125471e-22, 4.526263955509656e-23, 8.335487550965976e-24, 8.049860278807316e-25, 1.550531730561079e-25, 2.850818627923469e-26, 5.013642491597002e-27], [2.0921261308669554e-19, 8.462515446944147e-19, 1.7115164959029536e-18, 2.3076579961069812e-18, 2.3335819898950176e-18, 1.8878377689411964e-18, 1.2726970301713455e-18, 7.35425359071162e-19, 3.7184352614983013e-19, 1.6712034589877294e-19, 6.75991035053397e-20, 2.4857638151553888e-20, 8.378962104964139e-21, 2.607104771643348e-21, 7.532550628187624e-22, 2.0312454749724433e-22, 5.135160696957651e-23, 1.2218467215886258e-23, 2.7457173836192448e-24, 5.845394719453524e-25, 1.0226536636781495e-25, 9.405818945385418e-27, 1.729360536896407e-27, 3.0413704281813013e-28], [1.2086888652138386e-20, 4.889068608967134e-20, 9.887983810853994e-20, 1.3332085878877458e-19, 1.3481857167382367e-19, 1.0906648776973122e-19, 7.352781968845123e-20, 4.2487899251889336e-20, 2.1482601982171404e-20, 9.655082370909768e-21, 3.905418631308028e-21, 1.4361060743908153e-21, 4.840797143584312e-22, 1.5062086656435796e-22, 4.35179788475615e-23, 1.1735161431676208e-23, 2.9667482585882184e-24, 7.059003305743428e-25, 1.5862896503421675e-25, 3.377073402001567e-26, 6.830022198054539e-27, 1.1380138609024912e-27, 9.991074601323062e-29, 1.7570979671335863e-29], [6.665577658077316e-22, 2.6961832301626272e-21, 5.452943753345332e-21, 7.352268753968517e-21, 7.434863388800626e-21, 6.014708706646898e-21, 4.0548515525190136e-21, 2.343087622817881e-21, 1.1847048147034566e-21, 5.3245051882765935e-22, 2.1537280538842546e-22, 7.919719325283103e-23, 2.669562880588921e-23, 8.306315313279634e-24, 2.399893602723545e-24, 6.471610031674508e-25, 1.6360778591343149e-25, 3.89284091855458e-26, 8.747939322407329e-27, 1.8623605847553133e-27, 3.7665643059820935e-28, 7.255004769460792e-29, 1.1538776271483677e-29, 9.689898939134042e-31], [3.516057014089127e-23, 1.4222224155163873e-22, 2.8763990331955335e-22, 3.8782829407940677e-22, 3.921851174490311e-22, 3.1727270794124863e-22, 2.138912780507177e-22, 1.2359663473203915e-22, 6.24925533395523e-23, 2.8086483683987277e-23, 1.1360801747053054e-23, 4.177610120487453e-24, 1.4081803216968497e-24, 4.381537462563612e-25, 1.2659312017313936e-25, 3.413740115493944e-26, 8.630224306567375e-27, 2.053453026660128e-27, 4.6144917951865235e-28, 9.823853734352655e-29, 1.9868427803879423e-29, 3.8269767026119605e-30, 7.0363064859610375e-31, 1.0704383092769345e-31]] |
| Legacy trial inputs | {"lambda_home": 1.2132378538273145, "lambda_away": 4.044935590684186, "rho": 0.05, "max_goals": 23, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1313 |
| Legacy p draw | 0.1471 |
| Legacy p away | 0.7216 |
| Legacy p over 1 5 | 0.9586 |
| Legacy p under 3 5 | 0.2555 |
| Legacy p btts yes | 0.7171 |
| Legacy p over 2 5 | 0.8717 |
| Legacy goal margin distribution | {"-1": 0.11721446024576544, "-10": 0.002205273531361625, "-11": 0.0007826928732712951, "-12": 0.0002559826065717235, "-13": 7.760306893841035e-05, "-14": 2.1919246613374563e-05, "-15": 5.7943814444569615e-06, "-16": 1.4393048107390026e-06, "-17": 3.371331930265461e-07, "-18": 7.470169591083336e-08, "-19": 1.5702813053923724e-08, "-2": 0.1457246152472846, "-20": 3.1393079549581385e-09, "-21": 5.976149208802128e-10, "-22": 1.0692610161657186e-10, "-23": 1.549797276101276e-11, "-3": 0.14696632400170193, "-4": 0.12243906681511976, "-5": 0.08630875388176991, "-6": 0.0525159756933005, "-7": 0.028038604381537626, "-8": 0.013314378907330502, "-9": 0.005686698198202736, "0": 0.14713755605229784, "1": 0.08694640192420838, "10": 3.14627761007737e-08, "11": 3.3493481724996676e-09, "12": 3.285592624803401e-10, "13": 2.987559036494244e-11, "14": 2.531031580837647e-12, "15": 2.0068428439634396e-13, "16": 1.495179732025387e-14, "17": 1.0504526469582843e-15, "18": 6.981355749971748e-17, "19": 4.401706788110757e-18, "2": 0.03173896492853045, "20": 2.639440712237916e-19, "21": 1.5070711785620566e-20, "22": 8.087800073593703e-22, "23": 3.516057014089127e-23, "3": 0.009600901524433823, "4": 0.0023991010244115633, "5": 0.0005072449280504321, "6": 9.25739185024939e-05, "7": 1.4824769273418806e-05, "8": 2.111479181544681e-06, "9": 2.704957297540641e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0641 |
| Legacy raw p draw | 0.0830 |
| Legacy raw p away | 0.8529 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2132 |
| Legacy lambda away | 4.0449 |
| Legacy model home team | Villarreal CF |
| Legacy model away team | Paris Saint-Germain FC |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,415.1608 |
| Elo away rating | 1,614.2424 |
| Elo rating diff | -139.0817 |
| Elo home expectancy | 0.3099 |

</details>


---
