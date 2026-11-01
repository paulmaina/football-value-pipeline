# Super Lig — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-11-01T07:36:54.611521+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1506, 'tuning_matches': 191, 'audit_matches': 88, 'audit_matchdays': 34, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8780955557855701, 'audit_candidate_poisson_score': 0.8666990331242214, 'audit_gain': 0.011396522661348718, 'audit_gain_lower95': 0.0022198618746951896, 'audit_baseline_briers': [0.6107115695633953, 0.18205798184491676, 0.19529197364928902, 0.24988099071843453], 'audit_candidate_briers': [0.6061884405970215, 0.180352561937539, 0.19191664845636447, 0.2495646095484467], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1651.200 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 6, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 31.00 |
| Over 1 5 in window quote fixtures | 5 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'ANCHORED_MAIN': 1} |
| Shot features applied fixtures | 5 |
| Goal rate features used | {'shot_features': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-01 — Amed SK vs Eyüpspor

The model's most likely 1X2 outcome is **Amed SK win** at **77.8%**. Expected goals are 2.68 for Amed SK and 0.81 for Eyüpspor (3.50 combined). The most likely exact score is 2-0 at 14.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 64.0%; Double Chance 1X: 92.3%; Double Chance X2: 22.2%; Double Chance 12 (either team wins): 85.5%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 44.5%; BTTS No (at least one team does not score): 55.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Amed SK win | 77.8% | 1.29 |
| Draw | 14.5% | 6.90 |
| Eyüpspor win | 7.7% | 12.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Amed SK expected goals | 2.68 |
| Eyüpspor expected goals | 0.81 |
| Expected total goals | 3.50 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.17% |
| 2 | 1-0 | 11.54% |
| 3 | 3-0 | 10.82% |
| 4 | 2-1 | 9.86% |
| 5 | 3-1 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Amed SK win | 77.8% | 78.4% | 1.26 | -2.0% |
| Draw | 14.5% | 14.0% | 6.47 | -6.3% |
| Eyüpspor win | 7.7% | 7.5% | 11.68 | -9.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T10:30:00+00:00 |
| Fixture id | 5706f8b2f4d8a94519bbea0efc91e36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:59Z |
| Market best draw last update utc | 2026-11-01T07:36:59Z |
| Market best away last update utc | 2026-11-01T07:36:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Amedspor |
| Matched away-team name | Eyupspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0102 |
| Dc lambda away | 0.7474 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.9146 |
| Shot lambda away | 0.9697 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 44.5% |
| P btts no | 55.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.91 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.22 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.05564435282645459, "-10": 3.7206785488237083e-10, "-11": 2.3256938923390783e-11, "-12": 1.3349917182349905e-12, "-13": 7.083715457118764e-14, "-14": 3.4942618137346744e-15, "-15": 1.6102374498106169e-16, "-16": 6.961212425849271e-18, "-17": 2.824889400709344e-19, "-18": 1.0031102735317003e-20, "-2": 0.01754900192386786, "-3": 0.0036227214917443026, "-4": 0.0005857475143017036, "-5": 7.753810135382762e-05, "-6": 8.67154887627354e-06, "-7": 8.385841768835304e-07, "-8": 7.138229941091789e-08, "-9": 5.4239206387127754e-09, "0": 0.1448866751242718, "1": 0.2439257062996215, "10": 6.86680738695557e-05, "11": 1.4138354200689674e-05, "12": 2.6732431754803093e-06, "13": 4.6723416660287417e-07, "14": 7.591760825799747e-08, "15": 1.1523664035552752e-08, "16": 1.640964334641831e-09, "17": 2.193457855519736e-10, "18": 2.565606892437009e-11, "2": 0.23370952718507848, "3": 0.15891779581212306, "4": 0.08463726666562896, "5": 0.036904551151720796, "6": 0.013594869139070343, "7": 0.004330505641938892, "8": 0.0012142163284682005, "9": 0.0003039012256973196} |
| Raw goal margin distribution | {"-1": 0.057081678160966674, "-10": 1.3009936244908389e-09, "-11": 9.473756728426208e-11, "-12": 6.339324843629856e-12, "-13": 3.923203964335015e-13, "-14": 2.258023230751776e-14, "-15": 1.2145138695239498e-15, "-16": 6.13054377065342e-17, "-17": 2.9144198835235995e-18, "-18": 1.3024979361549838e-19, "-19": 5.005610669775946e-21, "-2": 0.0196778669771477, "-3": 0.004583249029627213, "-4": 0.0008463872561882302, "-5": 0.0001288748785584382, "-6": 1.6651819862650938e-05, "-7": 1.8659137487916744e-06, "-8": 1.8441395036429405e-07, "-9": 1.6293220166455146e-08, "0": 0.15546487671740397, "1": 0.20260987662373908, "10": 0.00019561901526703586, "11": 4.6921481769566915e-05, "12": 1.0342036990797204e-05, "13": 2.108227904833342e-06, "14": 3.996857510326641e-07, "15": 7.081191327834027e-08, "16": 1.1773794127794973e-08, "17": 1.8436698401627825e-09, "18": 2.71407387047501e-10, "19": 3.43570033946302e-11, "2": 0.21350359907426947, "3": 0.16380012361708002, "4": 0.0996376499461643, "5": 0.0499730917203031, "6": 0.021268812572520585, "7": 0.00785030797394337, "8": 0.0025556565601041414, "9": 0.0007437538658901556} |
| Unadjusted home-win probability | 76.2% |
| Unadjusted draw probability | 15.5% |
| Unadjusted away-win probability | 8.2% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 53.8% |
| Raw p btts yes | 52.5% |
| P home draw | 92.3% |
| P draw away | 22.2% |
| P home away | 85.5% |
| Raw p home draw | 91.8% |
| Raw p draw away | 23.8% |
| Raw p home away | 84.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.8547 |
| Totals anchor target over 2 5 | 0.5937 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.35 |
| Totals anchor reference last update utc | 2026-11-01T07:36:59Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6837 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.27, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.25, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 6.47 |
| Reference away odds | 11.68 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:59Z |
| Market reference home last update utc | 2026-11-01T07:36:59Z |
| Market reference draw last update utc | 2026-11-01T07:36:59Z |
| Market reference away last update utc | 2026-11-01T07:36:59Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:37Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:37Z |
| Home probability edge | -0.7% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0220 |
| Raw ev home | -0.0396 |
| Raw edge prob draw | 0.0151 |
| Raw ev draw | 0.0059 |
| Raw edge prob away | 0.0069 |
| Raw ev away | -0.0383 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.02963350776196383, 0.013951115440518507, 0.007103145597143217, 0.0017044401489385004, 0.00030674257428447185, 4.416277423986441e-05, 5.298554314669089e-06, 5.448935212722904e-07, 4.9031361274283076e-08, 3.921784584499566e-09, 2.823163488580693e-10, 1.8475476038862283e-11, 1.10832386513565e-12, 6.137275601011926e-14, 3.155730331946915e-15, 1.5144708505360261e-16, 6.813860370244306e-18, 2.885337379253221e-19, 1.1539218329810803e-20, 4.371948961066083e-22, 1.5736109945461297e-23], [0.06188588666909782, 0.05960486283284139, 0.021952504084852612, 0.0052676280980369725, 0.0009479979711645357, 0.00013648650004991582, 1.637535562883118e-05, 1.6840112719005131e-06, 1.5153302771837878e-07, 1.2120403690692201e-08, 8.725079215636531e-10, 5.709906374097701e-11, 3.425311201070602e-12, 1.8967451231080843e-13, 9.75288793610254e-15, 4.68052176012745e-16, 2.105845861748391e-17, 8.917229660857416e-19, 3.56623321395886e-20, 1.3511651438648558e-21, 4.863296311937668e-23], [0.10263636601100096, 0.07388453773522013, 0.030280440091625508, 0.00813988857177226, 0.0014649093876656079, 0.00021090799906157417, 2.5304286419062587e-05, 2.6022459922686892e-06, 2.3415889231636168e-07, 1.8729252265150955e-08, 1.3482571524294609e-09, 8.823326319815153e-11, 5.293018220240044e-12, 2.9309764591972326e-13, 1.5070809779156772e-14, 7.232652889711541e-16, 3.2540927994418406e-17, 1.377949514608509e-18, 5.510780268143112e-20, 2.0879100628271734e-21, 7.515088258686281e-23], [0.10573368344568825, 0.07611419449115575, 0.027396050219007748, 0.007485232885728955, 0.001509116812022073, 0.000217272692668696, 2.606790861793977e-05, 2.680775486194216e-06, 2.4122524168010276e-07, 1.929445582636522e-08, 1.3889442942970327e-09, 9.08959298049729e-11, 5.452748715899935e-12, 3.0194262440108986e-13, 1.552561038929173e-14, 7.450916871231929e-16, 3.352293454370732e-17, 1.4195327001945848e-18, 5.677082296036627e-20, 2.150918141649455e-21, 7.74187545694258e-23], [0.08169335282531394, 0.05880835267386233, 0.02116709759488367, 0.005079165347776254, 0.0010408088535382698, 0.00016787209300815864, 2.0140931316719758e-05, 2.0712561078193228e-06, 1.8637862729020323e-07, 1.4907536898639708e-08, 1.0731444568182337e-09, 7.022921194036423e-11, 4.212974618864998e-12, 2.332908922147777e-13, 1.1995601836876053e-14, 5.756825649096937e-16, 2.590093175771855e-17, 1.0967780743554133e-18, 4.3863021878613667e-20, 1.6618707389911052e-21, 5.981629908491002e-23], [0.05049519644717067, 0.03634982796398357, 0.0130835216612494, 0.0031394653684008378, 0.0005649994161308438, 9.262252425948636e-05, 1.244924156364894e-05, 1.2802569663211382e-06, 1.1520185024963993e-07, 9.21444619674128e-09, 6.633176175190326e-10, 4.340913587965531e-11, 2.6040672055831305e-12, 1.4419862846014423e-13, 7.414560062803614e-15, 3.558331639109629e-16, 1.6009535562426996e-17, 6.779257113115472e-19, 2.711202111221012e-20, 1.0272131885026237e-21, 3.697284624238507e-23], [0.026009509709749093, 0.018723388953760852, 0.006739175359818729, 0.0016171034222685538, 0.00029102486639956724, 4.189984224710672e-05, 5.724001719001412e-06, 6.594460134706407e-07, 5.9339181812747675e-08, 4.746257954949131e-09, 3.416674699257577e-10, 2.2359559336202463e-11, 1.3413258296621338e-12, 7.427509725584543e-14, 3.819156781551924e-15, 1.8328567434084132e-16, 8.246332323811565e-18, 3.491919353020801e-19, 1.3965098187244764e-20, 5.291059997814569e-22, 1.9044298685806128e-23], [0.011483320218377578, 0.008266463817604331, 0.00297537744956381, 0.0007139587263032338, 0.0001284888400308497, 1.8498976374117635e-05, 2.2194672497626924e-06, 2.598898503446459e-07, 2.6198526379637854e-08, 2.0954950917538288e-09, 1.5084778641135775e-10, 9.871850052720727e-12, 5.922016289841032e-13, 3.2792802923167395e-14, 1.6861755863975538e-15, 8.092148269554811e-17, 3.6407943001705814e-18, 1.541698730770675e-19, 6.1656561832500184e-21, 2.3360277424521666e-22, 8.408146965629549e-24], [0.004436197149453588, 0.003193472142754434, 0.0011494376808529278, 0.0002758141030836295, 4.963737099042478e-05, 7.14646153708535e-06, 8.574170274330243e-07, 8.817518053619852e-08, 9.034309997861236e-09, 8.095245256554997e-10, 5.827500299159954e-11, 3.813659484443108e-12, 2.287773160062781e-13, 1.2668403918366215e-14, 6.513976086710488e-16, 3.1261311540284413e-17, 1.4064992518727773e-18, 5.955838019578776e-20, 2.3818952937384042e-21, 9.024462799117997e-23, 3.2482066938635442e-24], [0.0015233569520986204, 0.0010966144709320343, 0.00039470831055087274, 9.47125020065992e-05, 1.70451022879981e-05, 2.454041490641434e-06, 2.944306002605659e-07, 3.027869811622633e-08, 2.724579625731632e-09, 2.481393345790147e-10, 2.001120057339098e-11, 1.3095821697822469e-12, 7.856042080175654e-14, 4.3502352422307475e-15, 2.236850713164727e-16, 1.0734900786020921e-17, 4.829813331731236e-19, 2.0451902715405976e-20, 8.17925045403879e-22, 3.0989330908535193e-23, 1.1154099067846385e-24], [0.0004707984548012542, 0.00033891229348200267, 0.00012198589598357914, 2.9271208913733865e-05, 5.267844682143355e-06, 7.584295592838552e-07, 9.099474122458085e-08, 9.357730810808774e-09, 8.420402559034565e-10, 6.735078140411125e-11, 5.520536133663004e-12, 4.0473065824748407e-13, 2.4279355321843736e-14, 1.3444544479497704e-15, 6.913060382389355e-17, 3.3176562430367478e-18, 1.492669627052948e-19, 6.320727510971017e-21, 2.5278241385835247e-22, 9.577354202482803e-24, 3.4472108448435553e-25], [0.00013227436749768356, 9.521995835021543e-05, 3.427285512582605e-05, 8.223966339462994e-06, 1.4800405912561885e-06, 2.1308649003142734e-07, 2.5565657062697645e-08, 2.6291248656197136e-09, 2.365775442152547e-10, 1.8922708687445402e-11, 1.3621834427772729e-12, 1.0150361975634828e-13, 6.821467521179812e-15, 3.777345909240003e-16, 1.9422763185148208e-17, 9.32120478831397e-19, 4.193767604542824e-20, 1.77585594241562e-21, 7.102112075063289e-23, 2.6908297096461062e-24, 9.685198187944901e-26], [3.406652204414485e-05, 2.452336663214039e-05, 8.826781762386295e-06, 2.1180364411761602e-06, 3.811761596905091e-07, 5.4879231307548646e-08, 6.584291698954363e-09, 6.771163747429133e-10, 6.092922066174133e-11, 4.873437573965938e-12, 3.50822711606266e-13, 2.295870086301238e-14, 1.568211670474688e-15, 9.728342695551991e-17, 5.002223807395214e-18, 2.400624054427229e-19, 1.0800813434294486e-20, 4.573617455444404e-22, 1.829109162584866e-23, 6.9300811150961855e-25, 2.4943685145749403e-26], [8.098746307893456e-06, 5.830020590649058e-06, 2.098419853839874e-06, 5.035277679867368e-07, 9.061826188039353e-08, 1.3046620120366246e-08, 1.5653053169883329e-09, 1.6097310235712456e-10, 1.4484903983966114e-11, 1.1585783399831838e-12, 8.340223685484059e-14, 5.458047452199761e-15, 3.274223752390166e-16, 2.0644464420153916e-17, 1.1891951147493687e-18, 5.707082505293293e-20, 2.5677128944917594e-21, 1.0873011172962909e-22, 4.3484013595583144e-24, 1.6475109719612194e-25, 5.929944293039902e-27], [1.7878171918420292e-06, 1.2869906828167475e-06, 4.6323109130373335e-07, 1.1115493262199561e-07, 2.0004193281953846e-08, 2.8800719098818033e-09, 3.4554481024623973e-10, 3.553518888938633e-11, 3.1975764371672934e-12, 2.557588786672963e-13, 1.8411238878026915e-14, 1.204876742394274e-15, 7.227925523182926e-17, 4.002419541325373e-18, 2.3433285977136e-19, 1.2598518129009234e-20, 5.668286277855858e-22, 2.400242650293584e-23, 9.599197717886934e-25, 3.636919008748125e-26, 1.309049073858425e-27], [3.6835383863985026e-07, 2.651657901448121e-07, 9.544205718440935e-08, 2.290186396120293e-08, 4.121574296256288e-09, 5.933971036886116e-10, 7.119450347445127e-11, 7.321510998957993e-12, 6.588143129786961e-13, 5.269541268157054e-14, 3.7933691127832635e-15, 2.4824740201291484e-16, 1.4892093688416827e-17, 8.246405776953838e-19, 4.240225554737138e-20, 2.3170548682383287e-21, 1.1678682912801317e-22, 4.9453523432772265e-24, 1.977775660386967e-25, 7.493344866620925e-27, 2.6971060213761393e-28], [7.115060008294642e-08, 5.121897238790151e-08, 1.843542520663434e-08, 4.4236850357647065e-09, 7.96116271104761e-10, 1.1461957386090198e-10, 1.3751809031009806e-11, 1.4142105943928585e-12, 1.2725545058727984e-13, 1.0178556161533727e-14, 7.327207168717262e-16, 4.7951045352131895e-17, 2.87653145229823e-18, 1.5928616944084851e-19, 8.190347461033706e-21, 3.9306408281865695e-22, 2.0136407726156755e-23, 9.55235835589616e-25, 3.820237779673693e-26, 1.4474017315992364e-27, 5.209684053160284e-29], [1.2934897625114386e-08, 9.31140655916772e-09, 3.351487372492635e-09, 8.042084395164727e-10, 1.447307886711144e-10, 2.0837385095791427e-11, 2.5000244800306284e-12, 2.5709789147945963e-13, 2.3134537497439795e-14, 1.8504212440573968e-15, 1.3320572770274973e-16, 8.717310351901085e-18, 5.229420385425146e-19, 2.8957595472309025e-20, 1.4889727676095715e-21, 7.145749530491193e-23, 3.2149935090710124e-24, 1.5501359813329504e-25, 6.945041155811319e-27, 2.6313190892028406e-28, 9.470999514868559e-30], [2.220873594890715e-09, 1.598733716948527e-09, 5.75437860035845e-10, 1.380795843828417e-10, 2.484973567191598e-11, 3.5777011683463767e-12, 4.292448626342578e-13, 4.414274739833985e-14, 3.972113653092698e-15, 3.1771041406410495e-16, 2.2870925763559984e-17, 1.4967296178220353e-18, 8.978719420263854e-20, 4.971910951278929e-21, 2.5565106110116613e-22, 1.2268984964486932e-23, 5.520023736544813e-25, 2.3374606986328256e-26, 1.0644136381361884e-27, 4.517876564864421e-29, 1.626135231171445e-30], [3.612464513230496e-10, 2.6004941622379177e-10, 9.360050269097276e-11, 2.2459972496056306e-11, 4.042048520207284e-12, 5.819475065725455e-13, 6.982080552986444e-14, 7.180242444228234e-15, 6.461024908093345e-16, 5.167865469384462e-17, 3.7201760557495904e-18, 2.434574683909107e-19, 1.4604750740688933e-20, 8.087291377482036e-22, 4.1584104026556684e-23, 1.9956684117246453e-24, 8.978849542060226e-26, 3.8021046512093634e-27, 1.5205610268858485e-28, 6.559773923737818e-30, 2.6450653606918943e-31], [5.582219940343901e-11, 4.018456185251438e-11, 1.4463770941808075e-11, 3.470664026397353e-12, 6.246041661226131e-13, 8.992639134654387e-14, 1.078917430059788e-14, 1.109538720778488e-15, 9.984004533449105e-17, 7.985728736312145e-18, 5.7486629651136e-19, 3.762066394562456e-20, 2.2568230223393815e-21, 1.2497019424110532e-22, 6.4258517654141016e-24, 3.0838392907232814e-25, 1.3874714276491006e-26, 5.875264468764341e-28, 2.3496718247901556e-29, 8.902375359948664e-31, 3.6485014594817975e-32]] |
| Legacy trial inputs | {"lambda_home": 3.09053274843213, "lambda_away": 0.719867047195542, "rho": -0.0948261506055015, "max_goals": 20, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8086 |
| Legacy p draw | 0.1281 |
| Legacy p away | 0.0632 |
| Legacy p over 1 5 | 0.8945 |
| Legacy p under 3 5 | 0.4781 |
| Legacy p btts yes | 0.5007 |
| Legacy p over 2 5 | 0.7252 |
| Legacy goal margin distribution | {"-1": 0.04573363271822448, "-10": 3.4502273328160367e-10, "-11": 2.2210002543791324e-11, "-12": 1.3138408719721563e-12, "-13": 7.188355659734627e-14, "-14": 3.657787877933639e-15, "-15": 1.7394196285224063e-16, "-16": 7.762901873452213e-18, "-17": 3.263613988823073e-19, "-18": 1.2965534356262522e-20, "-19": 4.85827859225985e-22, "-2": 0.014074438458083685, "-20": 1.5736109945461297e-23, "-3": 0.0028916053867399445, "-4": 0.000471410081085649, "-5": 6.339719492181694e-05, "-6": 7.2371368630859435e-06, "-7": 7.166176548222867e-07, "-8": 6.25952791219625e-08, "-9": 4.888219410416404e-09, "0": 0.12814346812959976, "1": 0.16885484966522607, "10": 0.0005753693342851595, "11": 0.00015901154765497728, "12": 4.0383492980239987e-05, "13": 9.485751112350561e-06, "14": 2.0722480581053454e-06, "15": 4.230665099595388e-07, "16": 8.106052907881217e-08, "17": 1.4630702508780284e-08, "18": 2.495386782056315e-09, "19": 4.01431013175564e-10, "2": 0.20336753586525977, "20": 5.582219940343901e-11, "3": 0.17937860053450316, "4": 0.1255484999738731, "5": 0.0724876067429442, "6": 0.03552561138990094, "7": 0.015102308401928818, "8": 0.005663416058483924, "9": 0.0018987537081135853} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8330 |
| Legacy raw p draw | 0.1159 |
| Legacy raw p away | 0.0511 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 3.0905 |
| Legacy lambda away | 0.7199 |
| Legacy model home team | Amedspor |
| Legacy model away team | Eyupspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 93.0% |
| Market reference home draw last update utc | 2026-11-01T07:36:15Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 22.2% |
| Market reference draw away last update utc | 2026-11-01T07:36:15Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.8% |
| Market reference home away last update utc | 2026-11-01T07:36:15Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.03 |
| Market reference dc draw away odds | 4.32 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.76 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.5% |
| Market reference btts yes odds | 2.22 |
| Market reference btts yes opposite odds | 1.73 |
| Market reference btts yes last update utc | 2026-11-01T07:36:37Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,486.7305 |
| Elo away rating | 1,373.7821 |
| Elo rating diff | 172.9484 |
| Elo home expectancy | 0.7302 |

</details>


---

## 2026-11-01 — Basaksehir vs Samsunspor

The model's most likely 1X2 outcome is **Basaksehir win** at **53.3%**. Expected goals are 1.75 for Basaksehir and 1.05 for Samsunspor (2.80 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.0%; Under 3.5 goals: 63.4%; Double Chance 1X: 77.7%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Basaksehir win | 53.3% | 1.87 |
| Draw | 24.3% | 4.11 |
| Samsunspor win | 22.3% | 4.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Basaksehir expected goals | 1.75 |
| Samsunspor expected goals | 1.05 |
| Expected total goals | 2.80 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 59.0% |
| Under 2.5 | 41.0% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 2-1 | 9.68% |
| 3 | 2-0 | 8.43% |
| 4 | 1-0 | 7.83% |
| 5 | 3-1 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Basaksehir win | 53.3% | 53.6% | 1.83 | -2.4% |
| Draw | 24.3% | 23.7% | 4.03 | -2.0% |
| Samsunspor win | 22.3% | 22.6% | 4.22 | -5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | f4e049de3ce6858d46dd45ab5cfa0e8c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:59Z |
| Market best draw last update utc | 2026-11-01T07:36:59Z |
| Market best away last update utc | 2026-11-01T07:36:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Buyuksehyr |
| Matched away-team name | Samsunspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8390 |
| Dc lambda away | 1.0100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5499 |
| Shot lambda away | 1.1464 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.55 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.54 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.13 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.1332262257863296, "-10": 6.482398561008207e-08, "-11": 6.658948856588801e-09, "-12": 6.285746172628562e-10, "-13": 5.487634061191909e-11, "-14": 4.454023954441463e-12, "-15": 3.353647347332209e-13, "-16": 2.116417549552056e-14, "-2": 0.06266790182177685, "-3": 0.020572747408702557, "-4": 0.005356467160964279, "-5": 0.0011501382759646866, "-6": 0.00020958861909531676, "-7": 3.312502834828501e-05, "-8": 4.6178646818138025e-06, "-9": 5.755121005134367e-07, "0": 0.2432834769002246, "1": 0.2178046062449083, "10": 1.0240683436027687e-05, "11": 1.7539783451848636e-06, "12": 2.760582455524417e-07, "13": 4.018411084327412e-08, "14": 5.438098936607464e-09, "15": 6.827116041417247e-10, "16": 7.183673452127112e-11, "2": 0.16574318394143753, "3": 0.09072106774307268, "4": 0.039383983602827195, "5": 0.01409991803669227, "6": 0.004284099645261477, "7": 0.0011289467615675812, "8": 0.0002624120307366012, "9": 5.4528347327192225e-05} |
| Raw goal margin distribution | {"-1": 0.13267306103010462, "-10": 3.241861519871272e-08, "-11": 3.0551380409653882e-09, "-12": 2.6447226518909176e-10, "-13": 2.1167808647721747e-11, "-14": 1.5749409026330103e-12, "-15": 1.0890493626657101e-13, "-16": 6.414937260909539e-15, "-2": 0.05937894452083429, "-3": 0.018227725589502475, "-4": 0.004405927794349021, "-5": 0.0008745737590046187, "-6": 0.0001469444373090486, "-7": 2.1375617408994313e-05, "-8": 2.739373439515553e-06, "-9": 3.135671840371655e-07, "0": 0.256890080824999, "1": 0.22836607277671073, "10": 5.383290549364651e-06, "11": 8.458815157497543e-07, "12": 1.2209114538158898e-07, "13": 1.6293158040601293e-08, "14": 2.0212450411131726e-09, "15": 2.330384626256847e-10, "16": 2.2887470139817494e-11, "2": 0.1650756993250835, "3": 0.08449061865740293, "4": 0.034051693832670815, "5": 0.011269979418874577, "6": 0.0031572223369321817, "7": 0.0007657658951150602, "8": 0.00016362660868665045, "9": 3.1229039764708116e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 21.6% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 54.8% |
| P home draw | 77.7% |
| P draw away | 46.7% |
| P home away | 75.7% |
| Raw p home draw | 78.4% |
| Raw p draw away | 47.3% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0929 |
| Totals anchor target over 2 5 | 0.5899 |
| Totals anchor reference over odds | 1.65 |
| Totals anchor reference under odds | 2.33 |
| Totals anchor reference last update utc | 2026-11-01T07:36:59Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5364 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.83 |
| Reference draw odds | 4.03 |
| Reference away odds | 4.22 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:59Z |
| Market reference home last update utc | 2026-11-01T07:36:59Z |
| Market reference draw last update utc | 2026-11-01T07:36:59Z |
| Market reference away last update utc | 2026-11-01T07:36:59Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:37Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:37Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0087 |
| Raw ev home | -0.0349 |
| Raw edge prob draw | 0.0194 |
| Raw ev draw | 0.0353 |
| Raw edge prob away | -0.0107 |
| Raw ev away | -0.0896 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06312635720383158, 0.04925923130513663, 0.03053286367563665, 0.010330591297058782, 0.002621465128867609, 0.0005321731718358018, 9.002862613705469e-05, 1.3054537163692322e-05, 1.6563434252727167e-06, 1.8680425956591375e-07, 1.8961193538472432e-08, 1.749652824438989e-09, 1.4799584828532175e-10, 1.155540246635805e-11, 8.377914748407135e-13, 5.6692234378562955e-14, 3.5965200642315835e-15], [0.08960289324927975, 0.11323351363346852, 0.05834955691437913, 0.019742184396804772, 0.00500972756309047, 0.0010170047954956947, 0.00017204840333725753, 2.4947756860145212e-05, 3.165340335889501e-06, 3.5699061480719294e-07, 3.6235619864915456e-08, 3.3436584312748138e-09, 2.828261464222497e-10, 2.2082848862202466e-11, 1.6010539287412753e-12, 1.083411890747357e-13, 6.87309760430493e-15], [0.09473586388265523, 0.09615974787125142, 0.05015552146907257, 0.018864062740939554, 0.004786897597838671, 0.0009717689737095257, 0.00016439578365795134, 2.3838094164070944e-05, 3.024547714300061e-06, 3.411118658550976e-07, 3.462387914375027e-08, 3.1949343175037985e-09, 2.702461928048333e-10, 2.1100615720248984e-11, 1.5298399182357637e-12, 1.0352223173766861e-13, 6.567385950117748e-15], [0.060348042688013644, 0.06125507628864684, 0.031087871321079368, 0.01080998672861065, 0.0030493193257343353, 0.0006190301444968044, 0.00010472236556799781, 1.5185192441968388e-05, 1.9266783147784436e-06, 2.1729293003027452e-07, 2.2055885183881458e-08, 2.0352169144405653e-09, 1.7215052580150858e-10, 1.3441381183859083e-11, 9.745289788656494e-13, 6.594507933976911e-14, 4.183514789681766e-15], [0.028831897237871915, 0.02926524185685071, 0.014852549831770659, 0.0050252614252378185, 0.0013105515191173377, 0.0002957480096835321, 5.0032185769018696e-05, 7.254881658508229e-06, 9.204903540833753e-07, 1.0381392916979092e-07, 1.0537425685858694e-08, 9.723457848879667e-10, 8.224668188518649e-11, 6.421757919003125e-12, 4.655912291843625e-13, 3.150593898623947e-14, 1.998717160269713e-15], [0.011019788033659836, 0.011185415907790881, 0.005676766587891855, 0.0019206962088886628, 0.00048739108827036546, 0.00010168643214126945, 1.912271251130378e-05, 2.7728753826519994e-06, 3.518189769247383e-07, 3.9678536759272636e-08, 4.027490682301568e-09, 3.7163854867009347e-10, 3.143535763078706e-11, 2.4544486437034135e-12, 1.779527935193734e-13, 1.2041828762268602e-14, 7.63926121950775e-16], [0.0035098779459693153, 0.0035626315580056496, 0.0018080890295164586, 0.0006117548943676249, 0.00015523739899142108, 3.1514124715628304e-05, 5.4791025480848965e-06, 8.831797964501487e-07, 1.1205675320703214e-07, 1.2637885653908643e-08, 1.2827833602814232e-09, 1.1836942252109656e-10, 1.0012376656877861e-11, 7.817586996895983e-13, 5.667918325556426e-14, 3.835404916385546e-15, 2.433157007734563e-16], [0.0009582172795213831, 0.0009726193252302468, 0.0004936189171436407, 0.00016701267669094082, 4.238072104825136e-05, 8.603541010930337e-06, 1.4554754319085659e-06, 2.169013568978329e-07, 3.0592151312084424e-08, 3.4502169581416343e-09, 3.5020738630405634e-10, 3.231554708531563e-11, 2.7334375922429243e-12, 2.134247133348294e-13, 1.547374969178359e-14, 1.0470880530368236e-15, 6.642661438632785e-17], [0.0002288990736413813, 0.00023233943627285706, 0.00011791575384914534, 3.989601085050227e-05, 1.012391238972856e-05, 2.055215043107183e-06, 3.4768416849888947e-07, 5.041569658062434e-08, 6.574022936326066e-09, 8.241882947204573e-10, 8.365758791931595e-11, 7.719542268886958e-12, 6.529639426179546e-13, 5.0982924456258074e-14, 3.696371424210821e-15, 2.5012853606731263e-16, 1.5867998650325307e-17], [4.8603948217073445e-05, 4.933446758758946e-05, 2.5037983347368747e-05, 8.471435094069569e-06, 2.14969027928647e-06, 4.364000427831923e-07, 7.382652560705349e-08, 1.0705163052653606e-08, 1.3582577625233922e-09, 1.5743276249940083e-10, 1.7763676394628345e-11, 1.6391513811205789e-12, 1.38648991233321e-13, 1.0825607027616021e-14, 7.848797395086243e-16, 5.311176765037905e-17, 3.3693774834463696e-18], [9.288414191619468e-06, 9.428019444634086e-06, 4.784861485214441e-06, 1.618926051021887e-06, 4.108146442863842e-07, 8.339784110762546e-08, 1.4108552356774015e-08, 2.0458006410874105e-09, 2.595686387647794e-10, 2.927444069336233e-11, 3.0538242272783462e-12, 3.1324856331866483e-13, 2.6496391858407047e-14, 2.068817979541881e-15, 1.4999374286646093e-16, 1.0149877005516257e-17, 6.439018800364191e-19], [1.613685557353581e-06, 1.6379393186386496e-06, 8.312788074841135e-07, 2.8125765421987475e-07, 7.137124212574585e-08, 1.4488790974811152e-08, 2.451093017991652e-09, 3.5541900690927964e-10, 4.509512117736679e-11, 5.085878081223498e-12, 5.16231904107769e-13, 4.895618710754696e-14, 4.603244857714258e-15, 3.594178323133202e-16, 2.6058564095408166e-17, 1.7633483600994657e-18, 1.11865722472312e-19], [2.569849498095791e-07, 2.6084744433221617e-07, 1.3238399615437794e-07, 4.479124438083888e-08, 1.1366114663386846e-08, 2.3073895682437944e-09, 3.9034495496149243e-10, 5.6601693704034543e-11, 7.181552440382432e-12, 8.099434970368754e-13, 8.22116981605791e-14, 7.586122128690172e-15, 6.59468436145028e-16, 5.723852034047042e-17, 4.149915549315929e-18, 2.8081926354978987e-19, 1.7814999300176765e-20], [3.77775997852185e-08, 3.8345398686893115e-08, 1.9460865814880402e-08, 6.584454480136157e-09, 1.6708547764547985e-09, 3.3919355869786043e-10, 5.738194200726979e-11, 8.32062785583732e-12, 1.0557109049785063e-12, 1.1906425377194935e-13, 1.2085379447609093e-14, 1.1151839277428565e-15, 9.432876572721245e-17, 7.569308907341628e-18, 6.100507009483581e-19, 4.1281319229879366e-20, 2.618861198816162e-21], [5.156753233343924e-09, 5.2342594496929405e-09, 2.656465293854463e-09, 8.987973593688605e-10, 2.2807658029938514e-10, 4.630091616431971e-11, 7.83280347782504e-12, 1.1357901201502298e-12, 1.4410763663324316e-13, 1.6252620047460493e-14, 1.649689760518647e-15, 1.522258787709239e-16, 1.2876153340252e-17, 1.0053601894176197e-18, 7.49116008676958e-20, 5.6350212196031896e-21, 3.574822389843389e-22], [6.569844861347556e-10, 6.668589903850371e-10, 3.384409544231897e-10, 1.1450924536509493e-10, 2.9057581025686883e-11, 5.898863536283397e-12, 9.979206169104277e-13, 1.4470277220536224e-13, 1.8359707613969315e-14, 2.0706283095303814e-15, 2.1017499394542526e-16, 1.939399389795408e-17, 1.6404572029816155e-18, 1.2808564178599773e-19, 9.286483880611324e-21, 6.458259330017052e-22, 4.5544216380726715e-23], [7.847027155893003e-11, 7.964968301594651e-11, 4.04234105381963e-11, 1.3676992028642972e-11, 3.470639447433731e-12, 7.04560660639839e-13, 1.1919170612980733e-13, 1.7283308921172526e-14, 2.1928847219616452e-15, 2.473159856519505e-16, 2.5103315523969898e-17, 2.3164199458319297e-18, 1.959363195257653e-19, 1.5298557737458522e-20, 1.1091782642029223e-21, 7.505661732086162e-23, 4.893554559950523e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9110410845916983, "lambda_away": 1.0150300417417408, "rho": -0.0948261506055015, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5546 |
| Legacy p draw | 0.2387 |
| Legacy p away | 0.2067 |
| Legacy p over 1 5 | 0.7980 |
| Legacy p under 3 5 | 0.6657 |
| Legacy p btts yes | 0.5542 |
| Legacy p over 2 5 | 0.5595 |
| Legacy goal margin distribution | {"-1": 0.12983795562260214, "-10": 2.2589017420109585e-08, "-11": 2.0545863854254615e-09, "-12": 1.7167648086226e-10, "-13": 1.3264162141626675e-11, "-14": 9.527000498655668e-13, "-15": 6.356533198286788e-14, "-16": 3.5965200642315835e-15, "-2": 0.05573389646822235, "-3": 0.01642442989601554, "-4": 0.0038190123851169146, "-5": 0.000730094310226399, "-6": 0.00011822914293531628, "-7": 1.6584049829249263e-05, "-8": 2.050077895010769e-06, "-9": 2.2641356788667856e-07, "0": 0.23874331972470608, "1": 0.22239618635901895, "10": 1.1065556055528174e-05, "11": 1.8949224270017326e-06, "12": 2.981047936751392e-07, "13": 4.3363977181363267e-08, "14": 5.864035634267157e-09, "15": 7.366341691507021e-10, "16": 7.847027155893003e-11, "2": 0.17292838580603315, "3": 0.09594631788145874, "4": 0.04200298963557637, "5": 0.01511817011654691, "6": 0.004609310162389824, "7": 0.0012172873623606639, "8": 0.00028331137365632627, "9": 5.890975588446903e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5730 |
| Legacy raw p draw | 0.2400 |
| Legacy raw p away | 0.1869 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9110 |
| Legacy lambda away | 1.0150 |
| Legacy model home team | Buyuksehyr |
| Legacy model away team | Samsunspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 76.5% |
| Market reference home draw last update utc | 2026-11-01T07:36:15Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 48.2% |
| Market reference draw away last update utc | 2026-11-01T07:36:15Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.3% |
| Market reference home away last update utc | 2026-11-01T07:36:15Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.9% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.78 |
| Market reference over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.53 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.7% |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-11-01T07:36:37Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,539.1035 |
| Elo away rating | 1,443.8010 |
| Elo rating diff | 155.3026 |
| Elo home expectancy | 0.7097 |

</details>


---

## 2026-11-01 — Kasimpasa SK vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **56.4%**. Expected goals are 1.25 for Kasimpasa SK and 1.54 for Besiktas JK (2.79 combined). The most likely exact score is 1-2 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 57.6%; Under 3.5 goals: 65.6%; Double Chance 1X: 43.6%; Double Chance X2: 79.7%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 81.9%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kasimpasa SK win | 20.3% | 4.92 |
| Draw | 23.3% | 4.29 |
| Besiktas JK win | 56.4% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kasimpasa SK expected goals | 1.25 |
| Besiktas JK expected goals | 1.54 |
| Expected total goals | 2.79 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.1% |
| Under 4.5 | 81.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.87% |
| 2 | 1-1 | 10.92% |
| 3 | 0-1 | 9.73% |
| 4 | 0-2 | 9.03% |
| 5 | 1-3 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kasimpasa SK win | 20.3% | 16.3% | 5.72 | +16.3% |
| Draw | 23.3% | 21.6% | 4.37 | +1.8% |
| Besiktas JK win | 56.4% | 62.1% | 1.58 | -10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:00:00+00:00 |
| Fixture id | bf609ced8c6472e7d11428e42a2e468e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:59Z |
| Market best draw last update utc | 2026-11-01T07:36:59Z |
| Market best away last update utc | 2026-11-01T07:36:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Kasimpasa |
| Matched away-team name | Besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2413 |
| Dc lambda away | 1.5812 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2639 |
| Shot lambda away | 1.4396 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.76 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.17 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.53 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.2665873991143874, "-10": 2.8751657901436638e-06, "-11": 4.170471731475162e-07, "-12": 5.5584030634720135e-08, "-13": 6.848608959090621e-09, "-14": 7.786713062313671e-10, "-15": 7.367910523390051e-11, "-2": 0.17419655659934924, "-3": 0.08103695059364813, "-4": 0.029859835949710423, "-5": 0.009066428937619265, "-6": 0.0023351570873178964, "-7": 0.0005214631315846666, "-8": 0.00010268990016944726, "-9": 1.8075408430994953e-05, "0": 0.23291252242365879, "1": 0.11184255091074849, "10": 1.8556216336577626e-07, "11": 2.1831733013102366e-08, "12": 2.3600954141806235e-09, "13": 2.358622241933325e-10, "14": 2.1751373531889994e-11, "15": 1.6693728780624826e-12, "2": 0.06001421637256358, "3": 0.02264509563598755, "4": 0.006767916336485754, "5": 0.0016667878309466313, "6": 0.00034820632481094024, "7": 6.306968439763243e-05, "8": 1.0073984449295352e-05, "9": 1.4382625058409617e-06} |
| Raw goal margin distribution | {"-1": 0.2087716758881511, "-10": 1.5026977941951527e-06, "-11": 2.0722691587545468e-07, "-12": 2.6252238650981784e-08, "-13": 3.07424522619988e-09, "-14": 3.3260471447968797e-10, "-15": 3.0246937900365697e-11, "-2": 0.13240921418007848, "-3": 0.05922288888472821, "-4": 0.020891928320813456, "-5": 0.006058072584124604, "-6": 0.0014878033370693572, "-7": 0.00031647224944765366, "-8": 5.9321309717578505e-05, "-9": 9.933846975868807e-06, "0": 0.2731905259787487, "1": 0.16718871822423137, "10": 1.8519813120555024e-07, "11": 2.07151274529406e-08, "12": 2.1285521009282876e-09, "13": 2.0217755665655712e-10, "14": 1.7741867532729427e-11, "15": 1.308666066310697e-12, "2": 0.08711063876465322, "3": 0.031602327812564245, "4": 0.009042416510272914, "5": 0.0021267524805641735, "6": 0.0004236473548525305, "7": 7.309221108028145e-05, "8": 1.1112779364127239e-05, "9": 1.5094054775104896e-06} |
| Unadjusted home-win probability | 29.8% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 42.9% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 57.1% |
| P home draw | 43.6% |
| P draw away | 79.7% |
| P home away | 76.7% |
| Raw p home draw | 57.1% |
| Raw p draw away | 70.2% |
| Raw p home away | 72.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0534 |
| Totals anchor target over 2 5 | 0.5758 |
| Totals anchor reference over odds | 1.69 |
| Totals anchor reference under odds | 2.26 |
| Totals anchor reference last update utc | 2026-11-01T07:36:59Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5442 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.45, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.1, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.72 |
| Reference draw odds | 4.37 |
| Reference away odds | 1.58 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:59Z |
| Market reference home last update utc | 2026-11-01T07:36:59Z |
| Market reference draw last update utc | 2026-11-01T07:36:59Z |
| Market reference away last update utc | 2026-11-01T07:36:59Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:37Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:37Z |
| Home probability edge | +4.0% |
| Draw probability edge | +1.7% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.1346 |
| Raw ev home | 0.7022 |
| Raw edge prob draw | 0.0575 |
| Raw ev draw | 0.1938 |
| Raw edge prob away | -0.1921 |
| Raw ev away | -0.3218 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06622607232945803, 0.10395413919418481, 0.09121023828075986, 0.04719913675542358, 0.018318326038134356, 0.005687579763641884, 0.0014715938700060399, 0.00032636355129213486, 6.333202628802045e-05, 1.0924274241250074e-05, 1.6959159089554056e-06, 2.3934444328723903e-07, 3.096376931828535e-08, 3.6976192671363145e-09, 4.10020787645667e-10, 4.243520813767387e-11], [0.05099718296272305, 0.11611274415963603, 0.11093493741235856, 0.057406201108289076, 0.022279761470245813, 0.006917549137030421, 0.0017898338710947892, 0.00039694140502980423, 7.702791380538937e-05, 1.3286706646880408e-05, 2.062666744027979e-06, 2.9110395210607123e-07, 3.7659849114759686e-08, 4.497249099512833e-09, 4.986899636773878e-10, 5.161204758990617e-11], [0.03636631371449063, 0.05645611654967973, 0.050062347220934944, 0.03491029870696366, 0.013548939191760468, 0.00420675296451485, 0.0010884474824922347, 0.00024139104750394995, 4.6842804920113557e-05, 8.080013812434954e-06, 1.2543646988781388e-06, 1.7702836499545322e-07, 2.2901995890224567e-08, 2.7349015679936105e-09, 3.032671603073325e-10, 3.138671369043929e-11], [0.014743574156726445, 0.022888350672158657, 0.017766268576493643, 0.010502801829737922, 0.0054929897840896875, 0.0017054952222622386, 0.00044127667983659543, 9.78643817898498e-05, 1.8990936872811883e-05, 3.2757865910269727e-06, 5.085425787910027e-07, 7.177056348481368e-08, 9.284891435395229e-09, 1.108779525899385e-09, 1.2295009888531478e-10, 1.2724752485609866e-11], [0.004482987620524415, 0.006959519559285161, 0.005402079661599295, 0.0027954482031574985, 0.0012394290214901725, 0.0005185794086962932, 0.00013417627719741504, 2.975701871136943e-05, 5.774456993803958e-06, 9.96048215917436e-07, 1.5462940403697978e-07, 2.182283238787735e-08, 2.8231996475427146e-09, 3.3713974886002255e-10, 3.7384677920424925e-11, 3.8691369718651815e-12], [0.0010904915072635225, 0.001692910535663503, 0.0013140616238966818, 0.0006799957489469324, 0.00026391126385005175, 9.360911188250703e-05, 3.2638522152086876e-05, 7.238426454194435e-06, 1.4046428060546486e-06, 2.422897880221866e-07, 3.76137670118797e-08, 5.308427191380859e-09, 6.867463173129531e-10, 8.200960252703182e-11, 9.093862670367256e-12, 9.411716840218977e-13], [0.00022105268258484142, 0.0003431685737962613, 0.0002663724064876733, 0.00013784140770450173, 5.349724637911564e-05, 1.6610134314838886e-05, 4.9096676750935534e-06, 1.4672957787704225e-06, 2.847340472472341e-07, 4.911437388413718e-08, 7.62465736295547e-09, 1.076067134081299e-09, 1.392098101508682e-10, 1.6624102540521807e-11, 1.84340980645258e-12, 1.9078417772185122e-13], [3.8408071552386224e-05, 5.962580043261133e-05, 4.6282408013905006e-05, 2.3950049318963534e-05, 9.295187204960026e-06, 2.8860234573910826e-06, 7.467243722435061e-07, 1.8918752215369323e-07, 4.9472757046840844e-08, 8.53365977890172e-09, 1.324790009939938e-09, 1.8696748212998105e-10, 2.4187810283716044e-11, 2.888450447216386e-12, 3.202938544725732e-13, 3.314889583478196e-14], [5.8392526624559635e-06, 9.065024612139438e-06, 7.036403112597243e-06, 3.641171857872693e-06, 1.4131651093327887e-06, 4.3876767242780895e-07, 1.135259361511149e-07, 2.5177277808237915e-08, 5.58147504976189e-09, 1.2973886365651018e-09, 2.0141036193878462e-10, 2.8425024316336732e-11, 3.677319112612248e-12, 4.39136652338186e-13, 4.8694887998901864e-14, 5.039690107760699e-15], [7.891135674320268e-07, 1.2250427107800158e-06, 9.508958565488862e-07, 4.920660708643707e-07, 1.9097439779683053e-07, 5.9294835020502326e-08, 1.5341835959293426e-08, 3.4024442266777243e-09, 6.602565953040297e-10, 1.301069335859438e-10, 2.721849154587574e-11, 3.8413430004195764e-12, 4.969509920673536e-13, 5.93446987736604e-14, 6.580601834816774e-15, 6.810610996946105e-16], [9.597635733046948e-08, 1.4899647123991124e-07, 1.1565321428852514e-07, 5.984779757515321e-08, 2.3227362702135603e-08, 7.21176584543919e-09, 1.865958958133649e-09, 4.138240886661007e-10, 8.030405956257651e-11, 1.3851815909973574e-11, 2.4566139511751513e-12, 4.672053854515996e-13, 6.044192871452061e-14, 7.217830550937174e-15, 8.003691980651711e-16, 8.283441847399607e-17], [1.0611977732296609e-08, 1.6474340962373088e-08, 1.2787621543839573e-08, 6.6172911002207356e-09, 2.568218492876553e-09, 7.973953241299113e-10, 2.0631659154256428e-10, 4.575597716103814e-11, 8.879112685604506e-12, 1.5315767974228495e-12, 2.377664089325494e-13, 3.83343422657447e-14, 6.682983387325586e-15, 7.980658905223817e-16, 8.84957539932313e-17, 9.158891093220503e-18], [1.0755728630759048e-09, 1.6697504012151296e-09, 1.2960843928252435e-09, 6.706929579026551e-10, 2.6030078342332805e-10, 8.081969199459833e-11, 2.091113764686285e-11, 4.637579214678847e-12, 8.999390022996608e-13, 1.5523236879881877e-13, 2.409872161911456e-14, 3.4010501814408027e-15, 5.026457288269375e-16, 8.088765698970353e-17, 8.969452621717992e-18, 9.282958336554716e-19], [1.0062855501313589e-10, 1.562186773905476e-10, 1.212591950787045e-10, 6.274875978017977e-11, 2.4353247096406345e-11, 7.561336940730527e-12, 1.956406336867663e-12, 4.338831065312514e-13, 8.41965844530489e-14, 1.4523245704451126e-14, 2.254630641442819e-15, 3.181957978251809e-16, 4.116469614497195e-17, 5.615801706092641e-18, 8.391649581052773e-19, 8.684959575711438e-20], [8.742143944971912e-12, 1.3571556944875351e-11, 1.0534438638128958e-11, 5.4513223437938436e-12, 2.1156975931579455e-12, 6.568940192341122e-13, 1.699635437428242e-13, 3.769375970958383e-14, 7.314610260153827e-15, 1.2617124878711913e-15, 1.9587189349647842e-16, 2.764338081680484e-17, 3.576198615824291e-18, 4.2706108449041945e-19, 5.409936476310972e-20, 7.545091625058157e-21], [7.088452712220441e-13, 1.100431887652531e-12, 8.541711347490853e-13, 4.420133195733775e-13, 1.7154856333707832e-13, 5.326338963978694e-14, 1.3781270935436317e-14, 3.0563490481172078e-15, 5.930955754537104e-16, 1.0230430158767743e-16, 1.5882015480898454e-17, 2.2414272626856453e-18, 2.8997137243843595e-19, 3.4627687689597325e-20, 3.839787375359715e-21, 4.539898256980186e-22]] |
| Legacy trial inputs | {"lambda_home": 1.21625531851899, "lambda_away": 1.5524289042027388, "rho": -0.0948261506055015, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2252 |
| Legacy p draw | 0.2442 |
| Legacy p away | 0.5306 |
| Legacy p over 1 5 | 0.7788 |
| Legacy p under 3 5 | 0.6942 |
| Legacy p btts yes | 0.5576 |
| Legacy p over 2 5 | 0.5351 |
| Legacy goal margin distribution | {"-1": 0.255845101122062, "-10": 2.0110689623272054e-06, "-11": 2.798660132058495e-07, "-12": 3.577701033059112e-08, "-13": 4.2276959445041414e-09, "-14": 4.616328352355732e-10, "-15": 4.243520813767387e-11, "-2": 0.16401258197974325, "-3": 0.07415813999963143, "-4": 0.02642821160159101, "-5": 0.00773883038179711, "-6": 0.0019188139465258496, "-7": 0.00041200254801689143, "-8": 7.794777528307258e-05, "-9": 1.317360066610461e-05, "0": 0.2442421082424143, "1": 0.12829631026621846, "10": 1.1381170040643078e-07, "11": 1.2408610199497574e-08, "12": 1.2427679924241545e-09, "13": 1.1505428309276033e-10, "14": 9.842575832624443e-12, "15": 7.088452712220441e-13, "2": 0.06539324007727244, "3": 0.02316474646718685, "4": 0.006467694984568504, "5": 0.0014837820581348486, "6": 0.00028823099831137833, "7": 4.848649085152776e-05, "8": 7.186833913764982e-06, "9": 9.515933770960668e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2873 |
| Legacy raw p draw | 0.2728 |
| Legacy raw p away | 0.4398 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2163 |
| Legacy lambda away | 1.5524 |
| Legacy model home team | Kasimpasa |
| Legacy model away team | Besiktas |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 40.3% |
| Market reference home draw last update utc | 2026-11-01T07:36:15Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 81.6% |
| Market reference draw away last update utc | 2026-11-01T07:36:15Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.2% |
| Market reference home away last update utc | 2026-11-01T07:36:15Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.35 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 80.7% |
| Market over 1 5 odds | 1.22 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-11-01T07:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.5% |
| Market under 3 5 odds | 1.49 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.63 |
| Market reference under 3 5 last update utc | 2026-11-01T07:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.8% |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-11-01T07:37:02Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,457.3688 |
| Elo away rating | 1,573.4966 |
| Elo rating diff | -56.1278 |
| Elo home expectancy | 0.4199 |

</details>


---

## 2026-11-01 — Trabzonspor vs Gazişehir Gaziantep

The model's most likely 1X2 outcome is **Trabzonspor win** at **74.5%**. Expected goals are 2.26 for Trabzonspor and 0.98 for Gazişehir Gaziantep (3.24 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 97.4%; Over 2.5 goals: 72.9%; Under 3.5 goals: 48.3%; Double Chance 1X: 89.7%; Double Chance X2: 25.5%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 67.5%; BTTS Yes (both teams score): 61.9%; BTTS No (at least one team does not score): 38.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Trabzonspor win | 74.5% | 1.34 |
| Draw | 15.2% | 6.59 |
| Gazişehir Gaziantep win | 10.3% | 9.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Trabzonspor expected goals | 2.26 |
| Gazişehir Gaziantep expected goals | 0.98 |
| Expected total goals | 3.24 |
| Over 0.5 | 97.4% |
| Under 0.5 | 2.6% |
| Over 1.5 | 89.6% |
| Under 1.5 | 10.4% |
| Over 2.5 | 72.9% |
| Under 2.5 | 27.1% |
| Over 3.5 | 51.7% |
| Under 3.5 | 48.3% |
| Over 4.5 | 32.5% |
| Under 4.5 | 67.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.07% |
| 2 | 2-0 | 8.97% |
| 3 | 3-1 | 8.67% |
| 4 | 3-0 | 7.72% |
| 5 | 1-1 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Trabzonspor win | 74.5% | 78.4% | 1.26 | -6.1% |
| Draw | 15.2% | 12.9% | 6.99 | +6.1% |
| Gazişehir Gaziantep win | 10.3% | 8.7% | 10.23 | +5.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | cd2960ff2b4d605144a83562b0085400 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:59Z |
| Market best draw last update utc | 2026-11-01T07:36:59Z |
| Market best away last update utc | 2026-11-01T07:36:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Trabzonspor |
| Matched away-team name | Gaziantep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3917 |
| Dc lambda away | 0.8904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.9435 |
| Shot lambda away | 1.1919 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.9% |
| P btts no | 38.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.98 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.63 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.69 |
| Fair Over 3.5 odds | 1.93 |
| Fair Under 3.5 odds | 2.07 |
| Fair Over 4.5 odds | 3.08 |
| Fair Under 4.5 odds | 1.48 |
| Goal margin distribution | {"-1": 0.06421776246645308, "-10": 2.0968231166034347e-08, "-11": 2.094475175973359e-09, "-12": 1.9239480959534967e-10, "-13": 1.6355052108823338e-11, "-14": 1.293637417555208e-12, "-15": 9.565843617228365e-14, "-16": 6.636842891724983e-15, "-17": 4.296261296565249e-16, "-18": 2.3074492957514993e-17, "-2": 0.027839018625135395, "-3": 0.008585207280498513, "-4": 0.002126512357020729, "-5": 0.00043769740425341494, "-6": 7.683150745939473e-05, "-7": 1.1735380007874208e-05, "-8": 1.5847037151653496e-06, "-9": 1.9162436271258803e-07, "0": 0.1518406673669864, "1": 0.22493715864795896, "10": 0.0001271476499495892, "11": 2.9226309154876084e-05, "12": 6.177949057637326e-06, "13": 1.2085235516369854e-06, "14": 2.1997228681533537e-07, "15": 3.7430953693593353e-08, "16": 5.976148322130018e-09, "17": 8.902310391945616e-10, "18": 1.1002627927540152e-10, "2": 0.21467562932455297, "3": 0.15234626916265115, "4": 0.08683627063665264, "5": 0.041130069055277683, "6": 0.0166141082843992, "7": 0.0058396531741390255, "8": 0.001814638781497799, "9": 0.0005049461327653576} |
| Raw goal margin distribution | {"-1": 0.09172310987304441, "-10": 1.088505260718934e-08, "-11": 9.548408701915905e-10, "-12": 7.69696865933207e-11, "-13": 5.738480795548842e-12, "-14": 3.978947375172721e-13, "-15": 2.577508099559807e-14, "-16": 1.5565296728214485e-15, "-17": 7.946145167703775e-17, "-2": 0.03728847681885425, "-3": 0.010445348239010286, "-4": 0.0023213105347280327, "-5": 0.00042550213358765636, "-6": 6.620064373246733e-05, "-7": 8.933553540156673e-06, "-8": 1.0634180112914683e-06, "-9": 1.1316901122136921e-07, "0": 0.20451259360909402, "1": 0.22192912737018522, "10": 4.5326551693015185e-05, "11": 9.149668571687953e-06, "12": 1.6972518706863414e-06, "13": 2.911895097274641e-07, "14": 4.646213932078307e-08, "15": 6.926012339591757e-09, "16": 9.624824988976862e-10, "17": 1.1306915506422498e-10, "2": 0.19745997288922737, "3": 0.12728568614927474, "4": 0.06509417117481368, "5": 0.027457615314466763, "6": 0.009830497598517942, "7": 0.0030527395149657862, "8": 0.0008362222718332716, "9": 0.00020478467572613388} |
| Unadjusted home-win probability | 65.3% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 14.2% |
| Raw p over 1 5 | 84.2% |
| Raw p under 3 5 | 59.4% |
| Raw p btts yes | 56.8% |
| P home draw | 89.7% |
| P draw away | 25.5% |
| P home away | 84.8% |
| Raw p home draw | 85.8% |
| Raw p draw away | 34.7% |
| Raw p home away | 79.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1443 |
| Totals anchor target over 2 5 | 0.7293 |
| Totals anchor reference over odds | 1.34 |
| Totals anchor reference under odds | 3.36 |
| Totals anchor reference last update utc | 2026-11-01T07:36:59Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6529 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.13, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.26 |
| Reference draw odds | 6.99 |
| Reference away odds | 10.23 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:59Z |
| Market reference home last update utc | 2026-11-01T07:36:59Z |
| Market reference draw last update utc | 2026-11-01T07:36:59Z |
| Market reference away last update utc | 2026-11-01T07:36:59Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:39Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:39Z |
| Home probability edge | -3.9% |
| Draw probability edge | +2.3% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.1309 |
| Raw ev home | -0.1770 |
| Raw edge prob draw | 0.0752 |
| Raw ev draw | 0.4295 |
| Raw edge prob away | 0.0557 |
| Raw ev away | 0.4555 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.037068687357647685, 0.021767133356451668, 0.012403881544132776, 0.0036156283564926636, 0.0007904442068654791, 0.00013824474919723993, 2.0148597580335212e-05, 2.517063728196274e-06, 2.751386821451386e-07, 2.673354620467011e-08, 2.337781944707446e-09, 1.8584836441956712e-10, 1.3543313317132905e-11, 9.110222875873081e-13, 5.690473360544046e-14, 3.3174513592450826e-15, 1.8131427997601355e-16, 9.326753884435774e-18, 4.531118706486068e-19], [0.08468679025247679, 0.0723663695021427, 0.03043964023921469, 0.008872902084621975, 0.0019397828978411774, 0.0003392583535687627, 4.944549490318401e-05, 6.176978881398037e-06, 6.752017479843816e-07, 6.560523219229726e-08, 5.737013942082242e-09, 4.560796015223163e-10, 3.3235853112084346e-11, 2.2356865135640796e-12, 1.3964657858872375e-13, 8.141163354972548e-15, 4.449527700716182e-16, 2.2888241219637696e-17, 1.1119553408816021e-18], [0.11330832768895653, 0.09908530676336698, 0.03546181545130099, 0.010887235030933798, 0.0023801538793474125, 0.00041627704174852494, 6.067064857672645e-05, 7.5792813018245e-06, 8.284865598081803e-07, 8.049898165499197e-08, 7.039435189017354e-09, 5.596191378234552e-10, 4.0781081638665573e-11, 2.7432337578532066e-12, 1.7134925054523205e-13, 9.989376421095471e-15, 5.459662846759727e-16, 2.8084347063266276e-17, 1.364392283902441e-18], [0.0926877799955113, 0.0810531520620599, 0.03543948004533912, 0.008455665406639378, 0.0019469988095669102, 0.00034052038053801475, 4.962943008832954e-05, 6.199956986004223e-06, 6.777134704126688e-07, 6.584928092825253e-08, 5.758355395407474e-09, 4.5777619867664474e-10, 3.3359489103747704e-11, 2.2440031744369242e-12, 1.4016605805470846e-13, 8.1714481441516e-15, 4.466079758755927e-16, 2.2973384525304526e-17, 1.1160917685156884e-18], [0.05686491497835611, 0.04972694999232926, 0.021742488813012377, 0.006337754743412322, 0.0011341151197282633, 0.00020891278751772267, 3.0448170433403414e-05, 3.803737956564166e-06, 4.15784247681511e-07, 4.039921725984058e-08, 3.5328107976139026e-09, 2.8085044887387653e-10, 2.046639278336236e-11, 1.376719236685749e-12, 8.599333131636471e-14, 5.01326824301682e-15, 2.739986282771169e-16, 1.4094409833311243e-17, 6.847338832342441e-19], [0.02790977240496876, 0.024406399925286478, 0.010671394031270869, 0.0031106226486837286, 0.0006800404825848131, 9.735235578541738e-05, 1.4944214851414782e-05, 1.8669061704612402e-06, 2.0407036090318624e-07, 1.9828271254607474e-08, 1.7339328714155161e-09, 1.378437321305533e-10, 1.0045075504847814e-11, 6.757052318827251e-13, 4.2206240988812147e-14, 2.4605536774461554e-15, 1.3448080169290075e-16, 6.917653368158475e-18, 3.360730750465755e-19], [0.011415290019537838, 0.009982386435740755, 0.00436467399347316, 0.00127226618550806, 0.00027814126253319406, 4.864551950198418e-05, 5.803276965614302e-06, 7.635775407213914e-07, 8.346618955899845e-08, 8.109900133657613e-09, 7.09190541378056e-10, 5.6379040173241203e-11, 4.108505382708857e-12, 2.763681150007216e-13, 1.726264458666894e-14, 1.0063834784868306e-15, 5.500357835634366e-17, 2.829368090371934e-18, 1.3745621296186483e-19], [0.00400194222826496, 0.0034995986740306807, 0.0015301558819087527, 0.0004460277193714633, 9.751002927208902e-05, 1.7054017758434395e-05, 2.485552203160605e-06, 2.541596194870027e-07, 2.9261356308671985e-08, 2.843147371319266e-09, 2.486261470859973e-10, 1.976521501181057e-11, 1.440348966865946e-12, 9.68884038928827e-14, 6.051892350056728e-15, 3.5281526211698367e-16, 1.9283009240517236e-17, 9.919123930084136e-19, 4.8189036130309323e-20], [0.0012276165454043733, 0.0010735200533811475, 0.0004693832570625097, 0.00013682131744484913, 2.9911707478390862e-05, 5.231408444132079e-06, 7.624560363504153e-07, 9.524982698125835e-08, 8.52228220437453e-09, 8.72150209816421e-10, 7.626736078977292e-11, 6.063082270553724e-12, 4.418345198469621e-13, 2.972102066758006e-14, 1.8564493828679797e-15, 1.0822791248382653e-16, 5.9151631479466445e-18, 3.042742737884803e-19, 1.4782236895584724e-20], [0.0003347357739131124, 0.0002927180862990216, 0.00012798733318059174, 3.7307243661844865e-05, 8.1560635438843e-06, 1.4264548329505631e-06, 2.078998628341322e-07, 2.5971892175141086e-08, 2.838971499146222e-09, 2.2578767206380013e-10, 2.079591883462754e-11, 1.6532283991530514e-12, 1.204755837612014e-13, 8.104068727236768e-15, 5.06200428163942e-16, 2.951064335186274e-17, 1.612895102760309e-18, 8.296685548897324e-20, 4.03069144508851e-21], [8.214554852734702e-05, 7.183423355625545e-05, 3.1408622884152956e-05, 9.155352470456664e-06, 2.0015318524341e-06, 3.500579377351668e-07, 5.101948940689846e-08, 6.373610158482386e-09, 6.96695391486317e-10, 6.769363832692643e-11, 4.845399157534988e-12, 4.0570911230021785e-13, 2.956520839265026e-14, 1.988772108579536e-15, 1.2422368649219558e-16, 7.242034387883843e-18, 3.9581115392736127e-19, 2.036041076237016e-20, 9.891484134803751e-22], [1.832623511313213e-05, 1.6025835567770586e-05, 7.007096767551147e-06, 2.0425104576583026e-06, 4.465311142443573e-07, 7.809606467010369e-08, 1.1382176818887593e-08, 1.4219185382262107e-09, 1.5542903754989665e-10, 1.5102090787422144e-11, 1.3206401761993178e-12, 8.593568096336068e-14, 6.59584079582936e-15, 4.4368448323325353e-16, 2.7713643965967385e-17, 1.6156593664422817e-18, 8.830336393527301e-20, 4.542299385911618e-21, 2.206737518002965e-22], [3.747778479651775e-06, 3.2773388144676896e-06, 1.4329755297883132e-06, 4.177004545898349e-07, 9.131715762288469e-08, 1.5970915395840133e-08, 2.3276945357342182e-09, 2.9078726014834583e-10, 3.1785775880670407e-11, 3.088429811221312e-12, 2.700754847446362e-13, 2.1470388726051022e-14, 1.280679224030026e-15, 9.073501173328626e-17, 5.667536065493181e-18, 3.3040792975864675e-19, 1.8058343407388154e-20, 9.289159383563943e-22, 4.5128545656850953e-23], [7.074772286833258e-07, 6.186711926824806e-07, 2.705062644683988e-07, 7.88503273705866e-08, 1.7238161208578065e-08, 3.014868414750781e-09, 4.394045401305515e-10, 5.489261600255626e-11, 6.000277965653788e-12, 5.830103822008284e-13, 5.098280395168781e-14, 4.053017326699539e-15, 2.9535521448732763e-16, 1.6262338368760605e-17, 1.069874521892893e-18, 6.237190585030571e-20, 3.408917260674875e-21, 1.753537134908826e-22, 8.519024960830767e-24], [1.2401274922309363e-07, 1.0844605643700057e-07, 4.7416685906948136e-08, 1.3821569766373819e-08, 3.021654516012037e-09, 5.284723034194898e-10, 7.70226416249645e-11, 9.62205417578414e-12, 1.0517808014942477e-12, 1.0219512005621577e-13, 8.9367083841236e-15, 7.104480553646539e-16, 5.177242554381208e-17, 3.48259192181579e-18, 1.7805585345414939e-19, 1.093308901712029e-20, 5.975446052972195e-22, 3.073752089089049e-23, 1.4932886363833299e-24], [2.0288828987366556e-08, 1.7742074965586506e-08, 7.757501043566864e-09, 2.2612470659967753e-09, 4.943510414722401e-10, 8.645953142566936e-11, 1.2601117335709545e-11, 1.5741946929058707e-12, 1.7207425000572685e-13, 1.6719404473760704e-14, 1.4620702246449685e-15, 1.1623126807526968e-16, 8.470112102989855e-18, 5.697616767401439e-19, 3.5588741214390737e-20, 1.698255660452001e-21, 9.775995117557719e-23, 5.028743486115313e-24, 2.443061536992138e-25], [3.111851787346935e-09, 2.72123678144669e-09, 1.1898268501745897e-09, 3.468246357804419e-10, 7.582237362935569e-11, 1.3260954960371509e-11, 1.932729066232123e-12, 2.414461954310666e-13, 2.6392334558595302e-14, 2.5643820413413492e-15, 2.242488141933285e-16, 1.7827272314772263e-17, 1.299125420354734e-18, 8.738867547405635e-20, 5.458515522329515e-21, 3.1822237961028166e-22, 1.423614618911618e-23, 7.712965797642302e-25, 3.7471090200530674e-26], [4.492125570796386e-10, 3.928251782373684e-10, 1.717579108433774e-10, 5.006600318518864e-11, 1.0945367796880005e-11, 1.9142902342868775e-12, 2.789998448880109e-13, 3.4854058052427253e-14, 3.809875567523656e-15, 3.701823521300058e-16, 3.2371523494615273e-17, 2.5734627255822677e-18, 1.8753574781987125e-19, 1.2615025731341796e-20, 7.879660996756744e-22, 4.593711353668814e-23, 2.5106787600275027e-24, 1.0571191247323298e-25, 5.409153583080192e-27], [6.124368130604278e-11, 5.35560719436739e-11, 2.3416724638929987e-11, 6.825780568723996e-12, 1.4922437197380091e-12, 2.6098598355778144e-13, 3.8037622313677766e-14, 4.7518502988035095e-15, 5.194218224664003e-16, 5.0469047762954897e-17, 4.413392361923262e-18, 3.508546867949621e-19, 2.5567806135335655e-20, 1.719877602221297e-21, 1.074278622179013e-22, 6.262865757471838e-24, 3.4229499469160015e-25, 1.7607555079418717e-26, 7.001776652764423e-28]] |
| Legacy trial inputs | {"lambda_home": 2.4540415136109632, "lambda_away": 0.874475060962569, "rho": -0.0948261506055015, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7487 |
| Legacy p draw | 0.1546 |
| Legacy p away | 0.0967 |
| Legacy p over 1 5 | 0.8565 |
| Legacy p under 3 5 | 0.5674 |
| Legacy p btts yes | 0.5317 |
| Legacy p over 2 5 | 0.6584 |
| Legacy goal margin distribution | {"-1": 0.06526565817079176, "-10": 2.8369751409381317e-09, "-11": 2.2197276797416124e-10, "-12": 1.5958801583124222e-11, "-13": 1.0611192810559115e-12, "-14": 6.561552136349752e-14, "-15": 3.791604568148483e-15, "-16": 2.0556691347955368e-16, "-17": 1.0438709225317376e-17, "-18": 4.531118706486068e-19, "-2": 0.024029859352531574, "-3": 0.006025333899200019, "-4": 0.0011970095079217292, "-5": 0.00019598942987241602, "-6": 2.7223587164279573e-05, "-7": 3.2788139912853026e-06, "-8": 3.482622854446041e-07, "-9": 3.306495872513203e-08, "0": 0.15459007138283204, "1": 0.2262806015167197, "10": 9.968632003442648e-05, "11": 2.1888409657582716e-05, "12": 4.416205380008686e-06, "13": 8.240388171534542e-07, "14": 1.4299620928575968e-07, "15": 2.318864946022535e-08, "16": 3.5280936902232334e-09, "17": 5.027686290233125e-10, "18": 6.124368130604278e-11, "2": 0.21951057563300436, "3": 0.1544613460743779, "4": 0.08611340725258433, "5": 0.03956765384061277, "6": 0.015423661205865856, "7": 0.005213067918528062, "8": 0.0015538801756948468, "9": 0.0004140125841714447} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7132 |
| Legacy raw p draw | 0.1799 |
| Legacy raw p away | 0.1069 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.4540 |
| Legacy lambda away | 0.8745 |
| Legacy model home team | Trabzonspor |
| Legacy model away team | Gaziantep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 90.4% |
| Market reference home draw last update utc | 2026-11-01T07:36:15Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 24.8% |
| Market reference draw away last update utc | 2026-11-01T07:36:15Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.8% |
| Market reference home away last update utc | 2026-11-01T07:36:15Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 3.86 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.30 |
| Market reference over 1 5 last update utc | 2026-11-01T07:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 51.2% |
| Market under 3 5 odds | 1.96 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-11-01T07:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.1% |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-11-01T07:36:37Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,616.7819 |
| Elo away rating | 1,414.5620 |
| Elo rating diff | 262.2199 |
| Elo home expectancy | 0.8190 |

</details>


---

## 2026-11-02 — Genclerbirligi SK vs Alanyaspor

The model's most likely 1X2 outcome is **Genclerbirligi SK win** at **35.4%**. Expected goals are 1.18 for Genclerbirligi SK and 1.19 for Alanyaspor (2.37 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 47.1%; Under 3.5 goals: 74.4%; Double Chance 1X: 64.6%; Double Chance X2: 64.6%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 88.3%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genclerbirligi SK win | 35.4% | 2.82 |
| Draw | 29.2% | 3.42 |
| Alanyaspor win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genclerbirligi SK expected goals | 1.18 |
| Alanyaspor expected goals | 1.19 |
| Expected total goals | 2.37 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 25.6% |
| Under 3.5 | 74.4% |
| Over 4.5 | 11.7% |
| Under 4.5 | 88.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.95% |
| 2 | 0-0 | 8.98% |
| 3 | 1-0 | 8.67% |
| 4 | 0-1 | 8.62% |
| 5 | 2-1 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genclerbirligi SK win | 35.4% | 35.8% | 2.68 | -5.0% |
| Draw | 29.2% | 28.7% | 3.31 | -3.3% |
| Alanyaspor win | 35.4% | 35.5% | 2.70 | -4.5% |
| Over 2.5 | 47.1% | 47.1% | 2.04 | -3.8% |
| Under 2.5 | 52.9% | 52.9% | 1.83 | -3.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-02T17:00:00+00:00 |
| Fixture id | 10a70d197a090f08183739878151539d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:36:59Z |
| Market best draw last update utc | 2026-11-01T07:36:59Z |
| Market best away last update utc | 2026-11-01T07:36:59Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genclerbirligi |
| Matched away-team name | Alanyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1092 |
| Dc lambda away | 1.1527 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3499 |
| Shot lambda away | 1.2751 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.13 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.81 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.91 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.54 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19216642311904183, "-10": 3.0065406923564226e-07, "-11": 3.4702748706415e-08, "-12": 3.6777255323345978e-09, "-13": 3.5834847195314565e-10, "-14": 2.944749324951609e-11, "-2": 0.10560841629174274, "-3": 0.040152612694648655, "-4": 0.011969171603839684, "-5": 0.0029227740043302032, "-6": 0.0006031959909323919, "-7": 0.00010766934129497799, "-8": 1.691958894775818e-05, "-9": 2.3736508851713563e-06, "0": 0.2921389178594234, "1": 0.1934153852032141, "10": 2.848630016662142e-07, "11": 3.265850064352494e-08, "12": 3.4377563165392972e-09, "13": 3.327091446077576e-10, "14": 2.715632006651045e-11, "2": 0.10562342218646502, "3": 0.0398876932339822, "4": 0.01181007381250486, "5": 0.0028644890162889615, "6": 0.0005871834125793161, "7": 0.00010410480986390404, "8": 1.6249198872897107e-05, "9": 2.264239678378863e-06} |
| Raw goal margin distribution | {"-1": 0.19712425105703935, "-10": 1.656484605478283e-07, "-11": 1.7721345885312346e-08, "-12": 1.7325557724832634e-09, "-13": 1.4305684770142775e-10, "-2": 0.10299365752236056, "-3": 0.03679717932505153, "-4": 0.010252862309334664, "-5": 0.002333194195661499, "-6": 0.0004479055084219798, "-7": 7.427916528327326e-05, "-8": 1.0835534267025574e-05, "-9": 1.4102760042774247e-06, "0": 0.3038372822884063, "1": 0.19571089398196817, "10": 1.5481800739488658e-07, "11": 1.6451071069703538e-08, "12": 1.5975266326564602e-09, "13": 1.3101859600282792e-10, "2": 0.10161019738464681, "3": 0.03605825868536909, "4": 0.009979269534062305, "5": 0.0022556303113914888, "6": 0.00043009742768119964, "7": 7.084527056613382e-05, "8": 1.02649676593102e-05, "9": 1.3270117824003149e-06} |
| Unadjusted home-win probability | 34.6% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 35.0% |
| Raw p over 1 5 | 69.8% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 49.5% |
| P home draw | 64.6% |
| P draw away | 64.6% |
| P home away | 70.8% |
| Raw p home draw | 65.0% |
| Raw p draw away | 65.4% |
| Raw p home away | 69.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0806 |
| Totals anchor target over 2 5 | 0.4714 |
| Totals anchor reference over odds | 2.04 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-11-01T07:36:59Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4268 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:36:15Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.66, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.67, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:36:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.67, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.68 |
| Reference draw odds | 3.31 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-11-01T07:36:59Z |
| Market reference home last update utc | 2026-11-01T07:36:59Z |
| Market reference draw last update utc | 2026-11-01T07:36:59Z |
| Market reference away last update utc | 2026-11-01T07:36:59Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:36:59Z |
| Market best over 2 5 last update utc | 2026-11-01T07:36:59Z |
| Market best under 2 5 last update utc | 2026-11-01T07:36:59Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0117 |
| Raw ev home | -0.0724 |
| Raw edge prob draw | 0.0167 |
| Raw ev draw | 0.0057 |
| Raw edge prob away | -0.0050 |
| Raw ev away | -0.0549 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.11586488145228348, 0.11054001041629295, 0.06994814081751602, 0.026471120358662104, 0.007513282749760791, 0.0017059925507650444, 0.0003228072513041965, 5.235554002917912e-05, 7.430021291617197e-06, 9.372705053540145e-07, 1.064099777315479e-07, 1.0982648112158081e-08, 1.0390662161851523e-09, 9.074386521145012e-11], [0.10954710777621107, 0.13995739696522788, 0.0759192120324352, 0.02873080793509998, 0.008154648564953569, 0.0018516233408573067, 0.0003503634531374694, 5.6824831912509566e-05, 8.064279554125616e-06, 1.0172799076012098e-06, 1.1549358663933356e-07, 1.1920173730990137e-08, 1.1277653338649816e-09, 9.849014803129184e-11], [0.0666215921400018, 0.07563667154318705, 0.03938071717053502, 0.015591696033626508, 0.004425382048879797, 0.0010048428977225236, 0.0001901359848616509, 3.083782079303665e-05, 4.376340401639254e-06, 5.520596265953399e-07, 6.267630554565294e-08, 6.4688652648212096e-09, 6.12018093003305e-10, 5.344884327233719e-11], [0.024102898330590337, 0.027364446656252553, 0.015533670070136982, 0.0053918031661241185, 0.0016010505028762952, 0.00036354018905950935, 6.878893411127823e-05, 1.1156756172226585e-05, 1.583307819169195e-06, 1.9972859586256635e-07, 2.2675540643478952e-08, 2.3403583850805994e-09, 2.2142085468538677e-10, 1.9337154725656577e-11], [0.006540106097066156, 0.0074250980925502485, 0.004214922576617312, 0.0015950920428200914, 0.0004152474409414111, 9.864338198610519e-05, 1.866526262614966e-05, 3.0272860991515633e-06, 4.296164295120832e-07, 5.4194569866371723e-08, 6.152805342437665e-09, 6.350353361512372e-10, 6.008057047262288e-11, 5.246964152882469e-12], [0.001419679481669517, 0.001611787217963603, 0.0009149452638900641, 0.0003462511786440048, 9.827627136072707e-05, 2.046726789040018e-05, 4.0517217881533565e-06, 6.571416268058368e-07, 9.325806354120579e-08, 1.1764169833836073e-08, 1.3356070023518126e-09, 1.3784893142229654e-10, 1.3041860771225858e-11, 1.1389734720426465e-12], [0.00025681156145891405, 0.0002915627066033123, 0.00016550814807348403, 6.263477566076142e-05, 1.7777592075098723e-05, 4.0366429243759936e-06, 7.005679920421751e-07, 1.1887300581480361e-07, 1.6869828173107925e-08, 2.128068245899031e-09, 2.4160335075496584e-10, 2.4936050553024524e-11, 2.359194925497939e-12, 2.0603351643257977e-13], [3.981915573229475e-05, 4.520739157541412e-05, 2.5662375500785708e-05, 9.71164955395599e-06, 2.7564518644025944e-06, 6.258897081123378e-07, 1.1843060874135993e-07, 1.761761556746906e-08, 2.6157012222734625e-09, 3.2996131642601924e-10, 3.74610916833483e-11, 3.866385433266844e-12, 3.6579797890552176e-13, 3.1945916415502697e-14], [5.40228605732225e-06, 6.133310882774276e-06, 3.4816281464557635e-06, 1.3175846653219029e-06, 3.739692919371672e-07, 8.49147899139025e-08, 1.6067543738621712e-08, 2.6059666441175125e-09, 3.392033033514807e-10, 4.4766027465978425e-11, 5.082366252403722e-12, 5.245545701369798e-13, 4.9628006543474624e-14, 4.334119487618441e-15], [6.514942448827139e-07, 7.396529357767041e-07, 4.198705281744945e-07, 1.5889547822804825e-07, 4.509921149578893e-08, 1.0240386448871869e-08, 1.9376819672340637e-09, 3.142692284311233e-10, 4.459942648365354e-11, 5.160217081906961e-12, 6.1291318687933e-13, 6.325919804042374e-14, 5.984940505742408e-15, 5.226775984937441e-16], [7.071085683920885e-08, 8.027928606157174e-08, 4.557124647216886e-08, 1.7245947299816683e-08, 4.894907227022456e-09, 1.111454945077391e-09, 2.1030907526999075e-10, 3.410965882678269e-11, 4.8406623480828884e-12, 6.106321727980254e-13, 6.358590985447543e-14, 6.865927261114704e-15, 6.495840517653702e-16, 5.672955844269388e-17], [6.977003340200748e-09, 7.921115257790789e-09, 4.496491105692999e-09, 1.7016486193818453e-09, 4.829779414293766e-10, 1.0966667936044145e-10, 2.0751086696203483e-11, 3.3655822345460556e-12, 4.776256275349099e-13, 6.025075779994651e-14, 6.8403750669392925e-15, 6.475427385720265e-16, 6.409411936859838e-17, 5.597475924281518e-18], [6.310491717447117e-10, 7.16441282738364e-10, 4.066942281159044e-10, 1.5390904941584114e-10, 4.36839162959616e-11, 9.919024515818595e-12, 1.876873986427694e-12, 3.044068890309425e-13, 4.319981544559226e-14, 5.449501591546248e-15, 6.186915513632271e-16, 6.385558707407745e-17, 5.541136688982247e-18, 5.062750257730538e-19], [5.268601667183244e-11, 5.981536630874882e-11, 3.3954721505475346e-11, 1.2849798568073062e-11, 3.647150880329561e-12, 8.281349764929989e-13, 1.5669938028198795e-13, 2.5414796736304067e-14, 3.606733514115624e-15, 4.549764813280402e-16, 5.16542844034214e-17, 5.3312747655986234e-18, 5.043908756396848e-19, 4.0402205828107016e-20]] |
| Legacy trial inputs | {"lambda_home": 1.08536425908012, "lambda_away": 1.1353176817545962, "rho": -0.0948261506055015, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-11-01T07:36:59Z", "over": 2.04, "under": 1.83, "bookmaker": "pinnacle", "event_id": "10a70d197a090f08183739878151539d", "kickoff_utc": "2026-11-02T17:00:00Z", "home_team": "Genclerbirligi SK", "away_team": "Alanyaspor"}} |
| Legacy p home | 0.3439 |
| Legacy p draw | 0.3010 |
| Legacy p away | 0.3551 |
| Legacy p over 1 5 | 0.6640 |
| Legacy p under 3 5 | 0.8146 |
| Legacy p btts yes | 0.4590 |
| Legacy p over 2 5 | 0.3875 |
| Legacy goal margin distribution | {"-1": 0.2037547856230981, "-10": 1.18961506710267e-07, "-11": 1.2163862289295399e-08, "-12": 1.1375563642164443e-09, "-13": 9.074386521145012e-11, "-2": 0.10348721059974403, "-3": 0.0357025234656721, "-4": 0.009566640457771208, "-5": 0.0020888326879977713, "-6": 0.0003842144452596226, "-7": 6.099520303377399e-05, "-8": 8.512379082693085e-06, "-9": 1.0594596250770075e-06, "0": 0.3010312319930376, "1": 0.20241497542843262, "10": 7.905151612368361e-08, "11": 7.727399344444588e-09, "12": 6.908645380534606e-10, "13": 5.268601667183244e-11, "2": 0.09856563242001337, "3": 0.032508419801620475, "4": 0.008327497536053897, "5": 0.001738268380164478, "6": 0.0003056644831352071, "7": 4.6390076144208656e-05, "8": 6.189256400241777e-06, "9": 7.364275782502747e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3300 |
| Legacy raw p draw | 0.3149 |
| Legacy raw p away | 0.3551 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0854 |
| Legacy lambda away | 1.1353 |
| Legacy model home team | Genclerbirligi |
| Legacy model away team | Alanyaspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 63.3% |
| Market reference home draw last update utc | 2026-11-01T07:36:15Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.0% |
| Market reference draw away last update utc | 2026-11-01T07:36:15Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market reference home away last update utc | 2026-11-01T07:36:15Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.52 |
| Market reference dc draw away odds | 1.48 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 71.7% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.13 |
| Market reference over 1 5 last update utc | 2026-11-01T07:37:01Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.9% |
| Market under 3 5 odds | 1.30 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:36:59Z |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.59 |
| Market reference under 3 5 last update utc | 2026-11-01T07:37:01Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.3% |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 1.93 |
| Market reference btts yes last update utc | 2026-11-01T07:36:15Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,419.5227 |
| Elo away rating | 1,462.0223 |
| Elo rating diff | 17.5004 |
| Elo home expectancy | 0.5252 |

</details>


---
