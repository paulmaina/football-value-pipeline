# Ligue 1 — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,761 |
| Training data through | 2026-11-02 |
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
| Training sha256 | d64703b08d0b253f68ae6aa61e0d2f2d7176bb4a80991112dca66465573aba1b |
| Training as of utc | 2026-11-05T16:16:26.417824+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 81, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 81, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 144, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_CHRONOLOGICAL_PARTITIONS', 'cutoff_utc': '2026-11-05T16:16:26.417824+00:00', 'observations': 519, 'observations_sha256': '09b43855723986c152174c7192f211cb1392e9bbac8dd5825656ed47f8834ff7', 'eligible_training_matches': 186, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 183, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 23, 'retrospective_eligible_training_matches': 186, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '06a1f681686c8f3d51c6b57bb667afee75b8eb0993b69eaa4c9987b68b43cf8a', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 126, 'tuning_matches': 17, 'audit_matches': 43, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-05T00:00:00+00:00', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-05', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1759, 'tune_start_date': '2025-11-06', 'audit_start_date': '2026-05-07', 'training_shot_matches': 1471, 'tuning_matches': 187, 'audit_matches': 96, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8547734904983413, 'audit_candidate_poisson_score': 0.8530374480014693, 'audit_gain': 0.0017360424968719812, 'audit_gain_lower95': -0.004922765199428151, 'audit_baseline_briers': [0.5824614078047651, 0.17370432402916056, 0.21287468772376236, 0.2466063615696182], 'audit_candidate_briers': [0.5816260245758471, 0.17326240897441395, 0.21186772195909942, 0.24573349270218828], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1597.023 |
| Base scoring parameter | 0.200 |
| Home-advantage parameter | 0.202 |
| Dixon-Coles low-score adjustment | -0.054 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1761, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['football-data.org'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 0.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261105T161626417824Z_05b57736df1208ef3f5a8929cb8b01f5a1d393f7471b86e76dc7fef7490205c8.json |
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

## 2026-11-06 — Toulouse FC vs RC Strasbourg Alsace

The model's most likely 1X2 outcome is **Toulouse FC win** at **39.6%**. Expected goals are 1.50 for Toulouse FC and 1.39 for RC Strasbourg Alsace (2.89 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 55.2%; Under 3.5 goals: 67.1%; Double Chance 1X: 65.6%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 83.3%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** football-data.org

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse FC win | 39.6% | 2.53 |
| Draw | 26.0% | 3.84 |
| RC Strasbourg Alsace win | 34.4% | 2.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse FC expected goals | 1.50 |
| RC Strasbourg Alsace expected goals | 1.39 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.1% |
| Under 1.5 | 20.9% |
| Over 2.5 | 55.2% |
| Under 2.5 | 44.8% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.7% |
| Under 4.5 | 83.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.20% |
| 2 | 2-1 | 8.71% |
| 3 | 1-2 | 8.04% |
| 4 | 1-0 | 7.71% |
| 5 | 0-1 | 7.07% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:45:00+00:00 |
| Fixture id | fdorg:559638 |
| Matched home-team name | Toulouse |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 1.5046 |
| Dc lambda away | 1.3888 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_CHRONOLOGICAL_PARTITIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-05T16:16:26.417824+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.22 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.78 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.98 |
| Fair Under 4.5 odds | 1.20 |
| Score matrix json | [[0.06164266526545849,0.07067562974494969,0.05341613392204797,0.02472742366181682,0.008585123576754198,0.0023845378422323047,0.0005519257304221994,0.0001094990303806283,1.900850489337606e-05,2.933142224795239e-06,4.073435035118038e-07,5.142754367362476e-08,5.95171611521017e-09,6.358087907287833e-10,6.307048417458703e-11,5.839324070202703e-12],[0.07708985483489854,0.12199075482713251,0.08036769598756942,0.03720385436933419,0.012916820274548291,0.003587676574554184,0.0008304045248767016,0.00016474769210003814,2.859940677620838e-05,4.413083937423394e-06,6.128721127688254e-07,7.737574571347526e-08,8.95470480977837e-09,9.566114925892018e-10,9.489323029871723e-11,8.785604408057741e-12],[0.06269533669302887,0.08706887066880428,0.06045894829992916,0.02798768684648584,0.009717055585358333,0.002698934564098835,0.0006246960749666518,0.0001239362666406345,2.1514739653092295e-05,3.319871377887911e-06,4.6105095990421207e-07,5.8208166257286106e-08,6.736438421965654e-09,7.196389552154656e-10,7.138620603893869e-11,6.6092277022915944e-12],[0.03144293299434443,0.043666735210895855,0.030321340638315465,0.01403637030437383,0.00487329271662903,0.001353568273675381,0.00031329725403947677,6.215645266618332e-05,1.0790061159017033e-05,1.6649801849836512e-06,2.3122604014754781e-07,2.9192529586574698e-08,3.3784551307138134e-09,3.609129584828577e-10,3.580157331625579e-11,3.3146564760473883e-12],[0.0118269326807455,0.016424788928567698,0.01140505736483972,0.005279634908795049,0.0018330384415317037,0.0005091306480356351,0.00011784350821387386,2.3379504115888893e-05,4.058569439809407e-06,6.262650041622618e-07,8.6973273496855e-08,1.0980466811515039e-08,1.2707708089146276e-09,1.357536609054002e-10,1.3466389969163873e-11,1.2467736075721939e-12],[0.003558862315040272,0.004942411014610231,0.003431915100242381,0.001588703869488619,0.0005515826975330451,0.0001532033643580223,3.546048935725054e-05,7.0351661236581235e-06,1.221270994112173e-06,1.8845046156135915e-07,2.6171274819849352e-08,3.304150838760675e-09,3.8238979327769703e-10,4.084986369386615e-11,4.0521941803995046e-12,3.7516875483693044e-13],[0.0008924193983980236,0.00123935771430492,0.0008605861474797576,0.000398382973527764,0.00013831473530709741,3.8417236226064095e-05,8.892063186979165e-06,1.7641364469684727e-06,3.062456002415504e-07,4.725578925143524e-08,6.562702139763732e-09,8.2854801414529e-10,9.588796617060623e-11,1.0243501308903199e-11,1.016127170017584e-12,9.407722042922597e-14],[0.00019181387889960616,0.0002663837327513466,0.0001849717379201765,8.562721022995723e-05,2.972894351674978e-05,8.257282518008678e-06,1.9112326943773488e-06,3.791780584427304e-07,6.582348678627741e-08,1.0157013902937795e-08,1.4105669999447812e-09,1.7808556014477349e-10,2.0609864335081366e-11,2.201706644993371e-12,2.1840324659709235e-13,2.0220668218346817e-14],[3.607439918830648e-05,5.009873721167399e-05,3.4787599054705084e-05,1.610389290356434e-05,5.591116670088097e-06,1.5529455296672024e-06,3.5944516400086523e-07,7.13119442773447e-08,1.2379410457244362e-08,1.9102276446196674e-09,2.6528506346765925e-10,3.349251692938322e-11,3.876093208196377e-12,4.14074543837406e-13,4.107505643994266e-14,3.8028971696293806e-15],[6.030671372167503e-06,8.375164301616985e-06,5.815552925235011e-06,2.6921386938983992e-06,9.346846517038747e-07,2.5961081429002045e-07,6.008958455798011e-08,1.1921443198599148e-08,2.069505187296769e-09,3.1933879509946166e-10,4.4348542836900313e-11,5.599049951560647e-12,6.479787570266712e-13,6.922215071215968e-14,6.866647055977079e-15,6.357423438285508e-16],[9.073497609291478e-07,1.260092427169224e-06,8.749839330884088e-07,4.050480037049139e-07,1.406287696560128e-07,3.905996459495501e-08,9.040829257359954e-09,1.7936508174033713e-09,3.1136915296057006e-10,4.8046388454550785e-11,6.6724975143447265e-12,8.424097951059441e-13,9.749219182938196e-14,1.0414877220727293e-14,1.0331271893507825e-15,9.56511519343571e-17],[1.2410552322699258e-07,1.7235297425776162e-07,1.1967858868442277e-07,5.5401672647569576e-08,1.9234927687704018e-08,5.342545457135165e-09,1.2365869190747212e-09,2.4533204588318687e-10,4.2588462915718473e-11,6.5716909124583756e-12,9.126511417169183e-13,1.1522316188864973e-13,1.3334791056914799e-14,1.4245265083881776e-15,1.4130911354747484e-16,1.3082977225807534e-17],[1.5560334535567943e-08,2.1609593738593598e-08,1.500528605216197e-08,6.946254588923158e-09,2.4116727588400803e-09,6.698476620774685e-10,1.5504310882212961e-10,3.075970034996322e-11,5.339736001210263e-12,8.239577611318053e-13,1.1442808273253846e-13,1.4446665213714995e-14,1.6719143871460235e-15,1.7860695035113085e-16,1.7717318476644788e-17,1.640342001398571e-18],[1.8008794543155608e-09,2.5009920764225376e-09,1.7366407705244125e-09,8.0392662156735e-10,2.791155879071918e-10,7.752499725498966e-11,1.7943955419001777e-11,3.5599820977197296e-12,6.179957657123538e-13,9.536097054046769e-14,1.3243364576687632e-14,1.6719886392728549e-15,1.9349945608839505e-16,2.0671122882999824e-17,2.050518564187829e-18,1.8984541763013785e-19],[1.9353774367912604e-10,2.6877776981144606e-10,1.8663411118553375e-10,8.639675690056718e-11,2.9996122716476424e-11,8.331492155960843e-12,1.928409275895876e-12,3.825857977776837e-13,6.641505394078685e-14,1.02482967581348e-14,1.423244011557849e-15,1.7968604612960322e-16,2.0795088779953394e-17,2.2214937665609688e-18,2.2036607466094996e-19,2.0402394889847005e-20],[1.9412589922516512e-11,2.6959457759767664e-11,1.8720128679421418e-11,8.66593141194583e-12,3.0087280056641628e-12,8.356811317097876e-13,1.934269655318981e-13,3.837484648343576e-14,6.66168873484374e-15,1.0279441032430693e-15,1.4275692085083334e-16,1.8023210677166678e-17,2.0858284446926666e-18,2.2282448211845066e-19,2.2103576072066538e-20,2.0464397171566466e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1844507283483927, "-10": 4.918304421644517e-07, "-11": 6.113893578554244e-08, "-12": 6.9830284703143584e-09, "-13": 7.373112487297922e-10, "-14": 7.185608858264478e-11, "-15": 5.839324070202703e-12, "-2": 0.10181580749835058, "-3": 0.04068112523012073, "-4": 0.01286390644357665, "-5": 0.0033503219807665555, "-6": 0.0007399435179160328, "-7": 0.00014166090789718438, "-8": 2.391314497731069e-05, "-9": 3.6077408588843706e-06, "0": 0.2601242644495678, "1": 0.20035168564768993, "10": 1.0955427796644868e-06, "11": 1.475411632210168e-07, "12": 1.825662665458796e-08, "13": 2.0883773528064284e-09, "14": 2.204972014388937e-10, "15": 1.9412589922516512e-11, "2": 0.11950277684074231, "3": 0.05172936381238991, "4": 0.017721417072147663, "5": 0.0050002706727602375, "6": 0.001196428998883621, "7": 0.0002481531401487728, "8": 4.538244026019966e-05, "9": 7.417676283117102e-06} |
| Raw goal margin distribution | {"-1": 0.1844507283483927, "-10": 4.918304421644517e-07, "-11": 6.113893578554244e-08, "-12": 6.9830284703143584e-09, "-13": 7.373112487297922e-10, "-14": 7.185608858264478e-11, "-15": 5.839324070202703e-12, "-2": 0.10181580749835058, "-3": 0.04068112523012073, "-4": 0.01286390644357665, "-5": 0.0033503219807665555, "-6": 0.0007399435179160328, "-7": 0.00014166090789718438, "-8": 2.391314497731069e-05, "-9": 3.6077408588843706e-06, "0": 0.2601242644495678, "1": 0.20035168564768993, "10": 1.0955427796644868e-06, "11": 1.475411632210168e-07, "12": 1.825662665458796e-08, "13": 2.0883773528064284e-09, "14": 2.204972014388937e-10, "15": 1.9412589922516512e-11, "2": 0.11950277684074231, "3": 0.05172936381238991, "4": 0.017721417072147663, "5": 0.0050002706727602375, "6": 0.001196428998883621, "7": 0.0002481531401487728, "8": 4.538244026019966e-05, "9": 7.417676283117102e-06} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Toulouse", "away_goals": 0.0, "away_xg": 1.9, "date": "2026-11-01T00:00:00+00:00", "home": "Marseille", "home_goals": 2.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Troyes", "away_goals": 0.0, "away_xg": 0.39, "date": "2026-10-25T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 0.84, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 3.0, "away_xg": 1.81, "date": "2026-10-16T00:00:00+00:00", "home": "Le Mans", "home_goals": 0.0, "home_xg": 0.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.43, "date": "2026-10-10T00:00:00+00:00", "home": "Monaco", "home_goals": 2.0, "home_xg": 1.17, "source": "pipeline training history"}, {"away": "Le Havre", "away_goals": 2.0, "away_xg": 2.34, "date": "2026-09-19T00:00:00+00:00", "home": "Toulouse", "home_goals": 3.0, "home_xg": 1.95, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.63, "date": "2026-09-12T00:00:00+00:00", "home": "Lorient", "home_goals": 2.0, "home_xg": 0.94, "source": "pipeline training history"}, {"away": "Lille", "away_goals": 1.0, "away_xg": 1.07, "date": "2026-09-03T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 3.41, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 2.0, "away_xg": 1.12, "date": "2026-08-29T00:00:00+00:00", "home": "Brest", "home_goals": 2.0, "home_xg": 2.73, "source": "pipeline training history"}, {"away": "Lyon", "away_goals": 2.0, "away_xg": 0.7, "date": "2026-08-22T00:00:00+00:00", "home": "Toulouse", "home_goals": 0.0, "home_xg": 2.76, "source": "pipeline training history"}, {"away": "Toulouse", "away_goals": 0.0, "away_xg": null, "date": "2026-05-17T00:00:00+00:00", "home": "Nantes", "home_goals": 0.0, "home_xg": null, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 26.0% |
| Unadjusted away-win probability | 34.4% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.1% |
| Raw p btts yes | 59.0% |
| P home draw | 65.6% |
| P draw away | 60.4% |
| P home away | 74.0% |
| Raw p home draw | 65.6% |
| Raw p draw away | 60.4% |
| Raw p home away | 74.0% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_NO_PINNACLE |
| Unanchored p over 2 5 | 0.5525 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [] |
| Price edge quotes | [] |
| Count model | {"corners": {"alpha": 0.015413236227799179, "mu": 9.118241731788824, "version": "count-markets-nb2-v1"}} |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,453.8748 |
| Elo away rating | 1,507.0944 |
| Elo rating diff | 6.7804 |
| Elo home expectancy | 0.5098 |
| Research p home | 0.4021 |
| Research p draw | 0.2476 |
| Research p away | 0.3503 |
| Research p over 1 5 | 0.7843 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.5045584561558274, 1.3887615133979418], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-05T16:17:39.147676+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard?dates=20261106"}, {"observed_at_utc": "2026-11-05T16:17:39.195277+00:00", "reason": null, "status": "available", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/news?limit=20"}, {"observed_at_utc": "2026-11-05T16:17:39.343648+00:00", "reason": null, "status": "available", "url": "https://www.bing.com/news/search?q=%22Toulouse+FC%22+%22RC+Strasbourg+Alsace%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-05T16:17:39.527245+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Ligue_1/2026"}, {"observed_at_utc": "2026-11-05T16:17:39.710878+00:00", "reason": null, "status": "available", "url": "https://understat.com/league/Ligue_1/2025"}, {"observed_at_utc": "2026-11-05T16:17:31.417352+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-05T16:17:31.500974+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-05T16:17:39.804811+00:00", "reason": "HTTPError", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Toulouse+FC_vs_RC+Strasbourg+Alsace&d=2026-11-06"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.2636152888822214, "goals_for": 1.2209651152670602, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 1.1552120600883142, "results": "LDWDWDLDLD", "xg_against": 1.2106403766875036, "xg_for": 1.7616272267678712, "xg_matches": 9}, "venue": {"goals_against": 1.1612768438259973, "goals_for": 0.7942586323126342, "last_match": "2026-10-25T00:00:00+00:00", "matches": 4, "points_per_game": 1.0983798271058733, "results": "DWLL", "xg_against": 1.1251950322490534, "xg_for": 2.11144997355446, "xg_matches": 4}}}, "goal_rates": [1.5045584561558274, 1.3887615133979418], "h2h": [], "margin_distribution": {"-1": 0.1907013863882369, "-10": 4.918304421644517e-07, "-11": 6.113893578554244e-08, "-12": 6.9830284703143584e-09, "-13": 7.373112487297922e-10, "-14": 7.185608858264478e-11, "-15": 5.839324070202703e-12, "-2": 0.10181580749835058, "-3": 0.04068112523012073, "-4": 0.01286390644357665, "-5": 0.0033503219807665555, "-6": 0.0007399435179160328, "-7": 0.00014166090789718438, "-8": 2.391314497731069e-05, "-9": 3.6077408588843706e-06, "0": 0.24762294836987947, "1": 0.20660234368753413, "10": 1.0955427796644868e-06, "11": 1.475411632210168e-07, "12": 1.825662665458796e-08, "13": 2.0883773528064284e-09, "14": 2.204972014388937e-10, "15": 1.9412589922516512e-11, "2": 0.11950277684074231, "3": 0.05172936381238991, "4": 0.017721417072147663, "5": 0.0050002706727602375, "6": 0.001196428998883621, "7": 0.0002481531401487728, "8": 4.538244026019966e-05, "9": 7.417676283117102e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-05T16:17:39.805179+00:00", "p_over_1_5": 0.7843411921148492, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
