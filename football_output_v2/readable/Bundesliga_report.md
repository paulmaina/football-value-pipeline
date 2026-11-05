# Bundesliga — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,604 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 41513a19c037d196c0471de355bef57470d3db9823799f63c3ec917eec59ff81 |
| Training as of utc | 2026-11-05T16:24:28.982095+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 71, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-05T16:24:28.982095+00:00', 'observations': 416, 'observations_sha256': '91f23680ed1446cd230e90bc5e605decba7de0db10fe0c7ca8f00f6c389f8a69', 'eligible_training_matches': 84, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 116, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 84, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '8027abac6d7b568c9fa4f84916d00ce57861bd11f0fd5faea914c7bc7430cc4f', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694716449928761, 'audit_candidate_poisson_score': 0.6673753164537862, 'audit_gain': 0.00209632853908992, 'audit_gain_lower95': -0.006062801738558959, 'audit_baseline_briers': [0.5838692910520525, 0.13632337444950357, 0.27438171226499136, 0.23546961438971004], 'audit_candidate_briers': [0.5818232810954291, 0.13599221629469402, 0.27350506640901034, 0.2362671929723898], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1586.186 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261105T162428982095Z_32b745ada61ac2d63911c24e504a7d25937e1680408684d259b31117b86547c3.json |
| Over 1 5 in window quote fixtures | 0 |
| Odds provider health | — |
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

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Hamburger SV vs Borussia Mönchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **37.6%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Mönchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.9%; Under 3.5 goals: 68.4%; Double Chance 1X: 64.5%; Double Chance X2: 62.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 37.6% | 2.66 |
| Draw | 26.9% | 3.71 |
| Borussia Mönchengladbach win | 35.5% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Mönchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 31.6% |
| Under 3.5 | 68.4% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.71% |
| 2 | 2-1 | 8.50% |
| 3 | 1-2 | 8.22% |
| 4 | 1-0 | 7.52% |
| 5 | 0-1 | 7.25% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | fdorg:565852 |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4419 |
| Dc lambda away | 1.3956 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T16:24:28.982095+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.74 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.64 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.32 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.06784689542751338,0.07247668191605647,0.057041832891608205,0.02653522280280789,0.009257916692464526,0.002584007592370208,0.0006010257184230311,0.00011982447572827658,2.0902877323744107e-05,3.24126159631704e-06,4.5233959496300054e-07,5.738817855923346e-08,6.674084733612297e-09,7.164714430429678e-10,7.142025075246368e-11],[0.07518824446371306,0.12713836093451414,0.0822461957793074,0.03826001057564807,0.013348596813917845,0.0037257707819652263,0.0008665934525587759,0.00017276982155583137,3.0138970884514177e-05,4.673437410912163e-06,6.522092471459267e-07,8.274557688511706e-08,9.623079270461494e-09,1.033049738895469e-09,1.0297782571531854e-10],[0.06088875918194849,0.08497430968687611,0.0592936479883286,0.027582742005350776,0.009623387356983412,0.00268601531217115,0.0006247521437087323,0.00012455473332561326,2.1728050925930827e-05,3.3692154404523765e-06,4.701964042053964e-07,5.965366619001362e-08,6.937554611736606e-09,7.447552679137243e-10,7.423967626358909e-11],[0.029264305128212764,0.04084028251101588,0.02849766410430832,0.013256794672154553,0.004625184480114009,0.0012909504599944584,0.0003002678591029272,5.986339301662994e-05,1.0442917883048207e-05,1.6193095411495114e-06,2.2598540728572707e-07,2.8670695754934308e-08,3.334321765283882e-09,3.579436615048069e-10,3.568101186469082e-11],[0.01054873961314481,0.014721467126880286,0.010272392831545468,0.0047786022763501804,0.0016672142574280541,0.0004653416575684376,0.00010823586775752962,2.1578620866790653e-05,3.764299923305804e-06,5.837034102750423e-07,8.145968979558683e-08,1.0334764578261795e-08,1.2019042288659017e-09,1.2902594012900975e-10,1.286173383051863e-11],[0.0030419559101344416,0.004245251620076047,0.0029622653730312946,0.001378012726621066,0.00048077708331372115,0.00013419127378100674,3.121213999853304e-05,6.222659358895211e-06,1.0855168313141224e-06,1.6832343045411923e-07,2.349065328170803e-08,2.9802516074542882e-09,3.4659493043683473e-10,3.7207404441665205e-11,3.708957531909186e-12],[0.0007310111680444305,0.0010201746629842337,0.0007118607679956393,0.00033114966903739106,0.0001155353422682004,3.224744956401695e-05,7.5005764684096095e-06,1.4953646997755326e-06,2.6086010127469444e-07,4.044973403315141e-08,5.645029185458903e-09,7.161830325591951e-10,8.32900845448845e-11,8.94129598992154e-12,8.91298052215456e-13],[0.00015057342153505598,0.00021013521582692468,0.00014662882891436382,6.821009156474438e-05,2.3797928888125214e-05,6.642318242035476e-06,1.5449660849300702e-06,3.080146913354112e-07,5.373187128725866e-08,8.331821892472672e-09,1.1627611126566742e-09,1.475191274386058e-10,1.7156062120661185e-11,1.8417249817971765e-12,1.8358925717733387e-13],[2.713817754214005e-05,3.78731301768242e-05,2.642723497485014e-05,1.2293654193271399e-05,4.289152844619428e-06,1.1971595644573087e-06,2.7845262119952453e-07,5.5514162418775566e-08,9.684212843138146e-09,1.5016625076476098e-09,2.095669819592069e-10,2.658769542776452e-11,3.0920746504129308e-12,3.3193812712936204e-13,3.3088693909689363e-14],[4.347709489057036e-06,6.067517510871372e-06,4.233811945967369e-06,1.96952197354727e-06,6.871496987449265e-07,1.9179261356899436e-07,4.46098895757504e-08,8.893723624233133e-09,1.5514727916707223e-09,2.405759312217194e-10,3.3573969904289986e-11,4.2595187360667025e-12,4.953701212101694e-13,5.317860946481018e-14,5.301020242360598e-15],[6.268777626904471e-07,8.748495758223046e-07,6.104553597751423e-07,2.8397700707798826e-07,9.907719613438583e-08,2.765376223901317e-08,6.4321104805876904e-09,1.282348229930986e-09,2.2370027136486205e-10,3.468762158580921e-11,4.840888102393083e-12,6.141619126402736e-13,7.142531350577385e-14,7.667597802520037e-15,7.643315906621261e-16],[8.216985609316638e-08,1.1467349462192348e-07,8.001724107861697e-08,3.722312577370672e-08,1.2986836402581114e-08,3.6247986431390093e-09,8.431078976177118e-10,1.6808758546885598e-10,2.932217443343854e-11,4.546782552450539e-12,6.345337199864634e-13,8.050308845374543e-14,9.362284134932463e-15,1.0050530510275372e-15,1.0018702297337836e-16],[9.873102085502248e-09,1.3778570058828436e-08,9.614455073082827e-09,4.472536988364763e-09,1.5604306453332525e-09,4.3553693221178423e-10,1.0130345528212645e-10,2.0196529111088642e-11,3.5231998121306066e-12,5.463177183860004e-13,7.62422680528567e-14,9.672831964082585e-15,1.1249233163176197e-15,1.2076194173797046e-16,1.2037951050287727e-17],[1.0950466538321491e-09,1.5282103746974855e-09,1.0663595661244805e-09,4.960585458182474e-10,1.730706663327684e-10,4.8306323190881106e-11,1.1235780686520084e-11,2.2400398001147734e-12,3.9076554983877856e-13,6.059325471031745e-14,8.45619135595187e-15,1.0728342706901588e-15,1.2476762649504291e-16,1.3393962613292515e-17,1.3351546355394745e-18],[1.1277866099440936e-10,1.5739011591241763e-10,1.0982418291059618e-10,5.108898180404937e-11,1.782451728254099e-11,4.975059672540512e-12,1.1571710635506977e-12,2.307013024030042e-13,4.024487479080204e-14,6.240488574261478e-15,8.709016505363729e-16,1.1049101158743493e-16,1.2849795761960644e-17,1.3794418380715409e-18,1.3750733951806707e-19]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1874289086108268, "-10": 5.423935318551896e-07, "-11": 6.779169410947337e-08, "-12": 7.781374148771355e-09, "-13": 8.194492687582864e-10, "-14": 7.142025075246368e-11, "-2": 0.10633090921717268, "-3": 0.042892808565283894, "-4": 0.013672241430203206, "-5": 0.0035862066238775358, "-6": 0.000797227425552244, "-7": 0.0001535693379449228, "-8": 2.6076421837547958e-05, "-9": 3.956591566315925e-06, "0": 0.26934492307459074, "1": 0.19395344713117746, "10": 7.516795954485543e-07, "11": 9.706587469992335e-08, "12": 1.1511136643110331e-08, "13": 1.2524367697445668e-09, "14": 1.1277866099440936e-10, "2": 0.11350191248631034, "3": 0.047304228307729186, "4": 0.01557854964202216, "5": 0.004221768723388727, "6": 0.00096964594639827, "7": 0.00019297777450474231, "8": 3.385498343269986e-05, "9": 5.307226888672326e-06} |
| Raw goal margin distribution | {"-1": 0.1874289086108268, "-10": 5.423935318551896e-07, "-11": 6.779169410947337e-08, "-12": 7.781374148771355e-09, "-13": 8.194492687582864e-10, "-14": 7.142025075246368e-11, "-2": 0.10633090921717268, "-3": 0.042892808565283894, "-4": 0.013672241430203206, "-5": 0.0035862066238775358, "-6": 0.000797227425552244, "-7": 0.0001535693379449228, "-8": 2.6076421837547958e-05, "-9": 3.956591566315925e-06, "0": 0.26934492307459074, "1": 0.19395344713117746, "10": 7.516795954485543e-07, "11": 9.706587469992335e-08, "12": 1.1511136643110331e-08, "13": 1.2524367697445668e-09, "14": 1.1277866099440936e-10, "2": 0.11350191248631034, "3": 0.047304228307729186, "4": 0.01557854964202216, "5": 0.004221768723388727, "6": 0.00096964594639827, "7": 0.00019297777450474231, "8": 3.385498343269986e-05, "9": 5.307226888672326e-06} |
| Research history json | {"away": [{"away": "Paderborn", "away_goals": 0.0, "away_xg": 0.99, "date": "2026-10-31T00:00:00+00:00", "home": "M'gladbach", "home_goals": 0.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 3.0, "away_xg": 2.6, "date": "2026-10-23T00:00:00+00:00", "home": "Stuttgart", "home_goals": 2.0, "home_xg": 1.55, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 2.0, "away_xg": 1.8, "date": "2026-10-18T00:00:00+00:00", "home": "M'gladbach", "home_goals": 1.0, "home_xg": 0.47, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": 1.17, "date": "2026-10-11T00:00:00+00:00", "home": "FC Koln", "home_goals": 2.0, "home_xg": 1.32, "source": "pipeline training history"}, {"away": "Mainz", "away_goals": 4.0, "away_xg": 2.82, "date": "2026-09-19T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 3.24, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 0.19, "date": "2026-09-12T00:00:00+00:00", "home": "Freiburg", "home_goals": 5.0, "home_xg": 2.6, "source": "pipeline training history"}, {"away": "Elversberg", "away_goals": 4.0, "away_xg": 2.31, "date": "2026-09-05T00:00:00+00:00", "home": "M'gladbach", "home_goals": 3.0, "home_xg": 2.37, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 0.0, "away_xg": 1.09, "date": "2026-08-29T00:00:00+00:00", "home": "RB Leipzig", "home_goals": 3.0, "home_xg": 3.96, "source": "pipeline training history"}, {"away": "Hoffenheim", "away_goals": 0.0, "away_xg": null, "date": "2026-05-16T00:00:00+00:00", "home": "M'gladbach", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "M'gladbach", "away_goals": 1.0, "away_xg": null, "date": "2026-05-09T00:00:00+00:00", "home": "Augsburg", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 64.5% |
| P draw away | 62.4% |
| P home away | 73.1% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5394 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.011823964613419384, "mu": 9.857583967086907, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-01 |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |
| Research p home | 0.3850 |
| Research p draw | 0.2508 |
| Research p away | 0.3642 |
| Research p over 1 5 | 0.7752 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4418575212264466, 1.395566453127332], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:27:19.381965+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:27:19.469781+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:27:19.731538+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Hamburger+SV%22+%22Borussia+M%C3%B6nchengladbach%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:27:19.838221+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Bundesliga/2026"}, {"observed_at_utc": "2026-11-05T16:27:30.319255+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Bundesliga/2025"}, {"observed_at_utc": "2026-11-05T16:27:13.451062+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:27:13.702984+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:27:30.411556+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Hamburger+SV_vs_Borussia+M%C3%B6nchengladbach&d=2026-11-06"}]}, "form": {"away": {"all": {"goals_against": 2.2633171886423034, "goals_for": 1.4955413906153532, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 0.7941779248780608, "results": "DWLLLLLLWL", "xg_against": 1.9317425773677326, "xg_for": 1.5670287632962654, "xg_matches": 8}, "venue": {"goals_against": 2.908133877985406, "goals_for": 1.1507795353021404, "last_match": "2026-10-23T00:00:00+00:00", "matches": 5, "points_per_game": 0.7766966202232553, "results": "WLLLL", "xg_against": 2.2146664815541426, "xg_for": 1.362970544404023, "xg_matches": 4}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4418575212264466, 1.395566453127332], "h2h": [], "margin_distribution": {"-1": 0.19669943803505854, "-10": 5.423935318551895e-07, "-11": 6.779169410947336e-08, "-12": 7.781374148771354e-09, "-13": 8.194492687582863e-10, "-14": 7.142025075246366e-11, "-2": 0.10633090921717267, "-3": 0.04289280856528389, "-4": 0.013672241430203203, "-5": 0.0035862066238775353, "-6": 0.0007972274255522438, "-7": 0.0001535693379449228, "-8": 2.6076421837547954e-05, "-9": 3.956591566315925e-06, "0": 0.25080386422612727, "1": 0.2032239765554092, "10": 7.516795954485542e-07, "11": 9.706587469992333e-08, "12": 1.1511136643110331e-08, "13": 1.2524367697445666e-09, "14": 1.1277866099440935e-10, "2": 0.11350191248631032, "3": 0.04730422830772918, "4": 0.015578549642022158, "5": 0.004221768723388726, "6": 0.0009696459463982699, "7": 0.00019297777450474231, "8": 3.385498343269986e-05, "9": 5.3072268886723255e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:27:30.411954+00:00", "p_over_1_5": 0.7752176487684853, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
