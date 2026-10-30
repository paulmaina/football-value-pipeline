# Primeira Liga — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Primeira Liga |
| Training matches | 1,611 |
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
| Training sha256 | 84c0a9d8af08458f9d90e4a3ffe4465c5e09f0dc593fdcb0fb4ebd37c58b23a7 |
| Training as of utc | 2026-10-30T12:03:05.225313+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1611, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1305, 'tuning_matches': 198, 'audit_matches': 102, 'audit_matchdays': 41, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8837344359927919, 'audit_candidate_poisson_score': 0.8736484991075407, 'audit_gain': 0.010085936885251168, 'audit_gain_lower95': 0.00023297797298160757, 'audit_baseline_briers': [0.5954697810381541, 0.18598455548023424, 0.2430638350018896, 0.24914758134392181], 'audit_candidate_briers': [0.5923556867513526, 0.18512769164413956, 0.24107872019596324, 0.24810667643793355], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1460.735 |
| Base scoring parameter | 0.094 |
| Home-advantage parameter | 0.170 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1611, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 34.00 |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 7 |
| Goal rate features used | {'shot_features': 7} |
| Legacy comparison status | {'AVAILABLE': 7} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Casa Pia vs Sporting Lisbon

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **76.3%**. Expected goals are 0.73 for Casa Pia and 2.38 for Sporting Lisbon (3.11 combined). The most likely exact score is 0-2 at 12.5%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 62.1%; Under 3.5 goals: 60.2%; Double Chance 1X: 23.7%; Double Chance X2: 91.3%; Double Chance 12 (either team wins): 85.0%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 47.7%; BTTS No (at least one team does not score): 52.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Casa Pia win | 8.7% | 11.54 |
| Draw | 15.0% | 6.66 |
| Sporting Lisbon win | 76.3% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Casa Pia expected goals | 0.73 |
| Sporting Lisbon expected goals | 2.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.47% |
| 2 | 0-1 | 10.60% |
| 3 | 0-3 | 10.14% |
| 4 | 1-2 | 9.35% |
| 5 | 1-3 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Casa Pia win | 8.7% | 8.1% | 10.93 | -5.3% |
| Draw | 15.0% | 14.8% | 6.16 | -7.5% |
| Sporting Lisbon win | 76.3% | 77.1% | 1.28 | -2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:15:00+00:00 |
| Fixture id | 75daf3f21fd7945dcc4215b1fe8a5da3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Casa Pia |
| Matched away-team name | Sp Lisbon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6959 |
| Dc lambda away | 2.5773 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 0.8099 |
| Shot lambda away | 1.9040 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 47.7% |
| P btts no | 52.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.95 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.76 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.56 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.2328979527124475, "-10": 0.00010200255091167846, "-11": 2.2323559767726657e-05, "-12": 4.4876982499962015e-06, "-13": 8.341213811565744e-07, "-14": 1.4415119378729904e-07, "-15": 2.3275826482360534e-08, "-16": 3.525975012582808e-09, "-17": 5.009509776934989e-10, "-18": 6.164807894707588e-11, "-2": 0.22051115247477945, "-3": 0.1572929564346255, "-4": 0.08832675960871768, "-5": 0.040725966438243486, "-6": 0.015893222911322006, "-7": 0.0053695448699709455, "-8": 0.0015981351378683516, "-9": 0.00042483905178853894, "0": 0.15015293526277934, "1": 0.06399366155545509, "10": 6.616921845187086e-10, "11": 4.4510535107164313e-11, "12": 2.7502831454502175e-12, "13": 1.5712214785768915e-13, "14": 8.346046321425281e-15, "15": 4.142114044864781e-16, "16": 1.9286373155461856e-17, "17": 8.422110930695981e-19, "18": 3.185661819340479e-20, "2": 0.017957272819521055, "3": 0.003937073213354088, "4": 0.0006795335558947706, "5": 9.63040169024341e-05, "6": 1.1551526310817157e-05, "7": 1.199552517823741e-06, "8": 1.0973614132531497e-07, "9": 8.966335997457558e-09} |
| Raw goal margin distribution | {"-1": 0.23348033647711364, "-10": 8.257139265166622e-05, "-11": 1.7601632616657402e-05, "-12": 3.4461833462189657e-06, "-13": 6.237822136985932e-07, "-14": 1.0497401241098122e-07, "-15": 1.650459922289543e-08, "-16": 2.434474180176495e-09, "-17": 3.369053863788257e-10, "-18": 4.055193031493566e-11, "-2": 0.21727935914774943, "-3": 0.1517682483265945, "-4": 0.083283470135762, "-5": 0.037481862703076886, "-6": 0.014266820329519434, "-7": 0.0046990338375080395, "-8": 0.0013629990770655297, "-9": 0.0003530314065216523, "0": 0.15567221308476922, "1": 0.07445465348397355, "10": 6.214032889168432e-10, "11": 4.0714704204224523e-11, "12": 2.450141153894187e-12, "13": 1.3631388851529662e-13, "14": 7.050879794783878e-15, "15": 3.4073825111319457e-16, "16": 1.5448114284932207e-17, "17": 6.571017883097652e-19, "18": 2.4310316912350943e-20, "2": 0.02052708398899401, "3": 0.004407010680612975, "4": 0.0007433209746155735, "5": 0.00010282367800336642, "6": 1.202966559346515e-05, "7": 1.217837461173887e-06, "8": 1.085752185430211e-07, "9": 8.643763728545103e-09} |
| Unadjusted home-win probability | 10.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 74.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 62.4% |
| Raw p btts yes | 46.6% |
| P home draw | 23.7% |
| P draw away | 91.3% |
| P home away | 85.0% |
| Raw p home draw | 25.6% |
| Raw p draw away | 90.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0274 |
| Totals anchor target over 2 5 | 0.6206 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.50 |
| Totals anchor reference last update utc | 2026-10-30T12:02:58Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6046 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 4.02, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.56, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.93 |
| Reference draw odds | 6.16 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-30T12:03:03Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:03:03Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0194 |
| Raw ev home | 0.0957 |
| Raw edge prob draw | 0.0079 |
| Raw ev draw | -0.0411 |
| Raw edge prob away | -0.0273 |
| Raw ev away | -0.0476 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03758295843872972, 0.10519701659479785, 0.1269532207882958, 0.10574134176894627, 0.06605522465087352, 0.033011063644049696, 0.013747718022699057, 0.004907439159608077, 0.001532806330643726, 0.0004255661969235249, 0.0001063382411130205, 2.415567266034297e-05, 5.029910274382749e-06, 9.66805770760555e-07, 1.725573833901604e-07, 2.874515374799565e-08, 4.489179815300428e-09, 6.598427183943833e-10, 9.159890281665568e-11], [0.03092964498429763, 0.0690063540692167, 0.0895432593493782, 0.07458199430605478, 0.04659039034667728, 0.023283522977390156, 0.009696606929110329, 0.003461338709498836, 0.0010811263703666006, 0.00030016240710424656, 7.500300223669279e-05, 1.7037595803817415e-05, 3.547720628169204e-06, 6.819121195519057e-07, 1.217090077558688e-07, 2.027467078906771e-08, 3.1663300070012817e-09, 4.654034556674606e-10, 6.460698090289381e-11], [0.009696293912714857, 0.024228588817599983, 0.03200493938870634, 0.02630226636816686, 0.01643067966333118, 0.008211223486832028, 0.0034196288352156224, 0.0012206840749536562, 0.0003812726387329016, 0.00010585599994776619, 2.6450740042513925e-05, 6.0085197141046055e-06, 1.2511477311672162e-06, 2.4048477618517353e-07, 4.292219283200722e-08, 7.1501144020448695e-09, 1.1166455929284035e-09, 1.6413030750288095e-10, 2.278445403293577e-11], [0.002279678964064714, 0.005696341793438013, 0.007116859509422457, 0.00626737993840691, 0.0038629888007689853, 0.001930526613639332, 0.0008039830465872787, 0.00028699293075177624, 8.964035351208534e-05, 2.488762185565719e-05, 6.21878794121455e-06, 1.4126527228563817e-06, 2.941551885034194e-07, 5.653996159586845e-08, 1.0091362841461092e-08, 1.681051084025363e-09, 2.625326224049775e-10, 3.858839395216194e-11, 5.356813751125261e-12], [0.00040197854659585716, 0.0010044428321418896, 0.0012549244376162665, 0.0010452463752256226, 0.0006903630900091939, 0.000340412090714599, 0.00014176730217250417, 5.060581029408909e-05, 1.5806391860053152e-05, 4.388464437083067e-06, 1.0965663927257716e-06, 2.490947617317087e-07, 5.186873985861733e-08, 9.969759753526239e-09, 1.7794222046726818e-09, 2.964217691007842e-10, 4.6292694564407104e-11, 6.804338137463324e-12, 9.445734421405604e-13], [5.6705090311560456e-05, 0.0001416916947228756, 0.00017702587407172836, 0.0001474476451714475, 9.210860353298984e-05, 4.8668625241769046e-05, 1.9998399767837212e-05, 7.138706946719412e-06, 2.2297281422467473e-06, 6.190585899203591e-07, 1.5468710173394561e-07, 3.513854428239964e-08, 7.316862063752842e-09, 1.4063838281813733e-09, 2.510141341443428e-10, 4.181472700350751e-11, 6.530277419703579e-12, 9.598537331475329e-13, 1.3324622121272686e-13], [6.665918066341915e-06, 1.665644517122414e-05, 2.0810124200509885e-05, 1.7333080970114353e-05, 1.0827747579319312e-05, 5.4111611360311696e-06, 2.382638205977529e-06, 8.391845484241491e-07, 2.6211377188131267e-07, 7.277289950516108e-08, 1.8184109052872122e-08, 4.130681317498063e-09, 8.601274198087008e-10, 1.6532623997204133e-10, 2.950775040664779e-11, 4.915494228831348e-12, 7.676611392567033e-13, 1.1283477912968685e-13, 1.5663644804611627e-14], [6.716625074404549e-07, 1.678314917376157e-06, 2.096842484644008e-06, 1.7464932077156865e-06, 1.091011323073303e-06, 5.452323326838522e-07, 2.2706630866004096e-07, 8.569856403455403e-08, 2.6410764654521276e-08, 7.332647606659255e-09, 1.83224338500237e-09, 4.16210301947309e-10, 8.66670327713818e-11, 1.6658386103785617e-11, 2.9732213072238455e-12, 4.952885928371089e-13, 7.735006649139729e-14, 1.1369310261913448e-14, 1.5782796668689901e-15], [5.921753080145084e-08, 1.4796964876451416e-07, 1.8486938461606075e-07, 1.5398062892709125e-07, 9.618967251131338e-08, 4.8070738052198455e-08, 2.0019438301370094e-08, 7.146216943880359e-09, 2.359962458701845e-09, 6.464873067848353e-10, 1.6154084511967694e-10, 3.669543275441938e-11, 7.641051310377986e-12, 1.4686966761961758e-12, 2.6213585303578507e-13, 4.366741805152629e-14, 6.819615348791318e-15, 1.0023821088238987e-15, 1.3914998046009541e-16], [4.640843896549624e-09, 1.1596296435354965e-08, 1.4488107552659236e-08, 1.2067373500241523e-08, 7.538329419407318e-09, 3.767276147331616e-09, 1.5689118880145697e-09, 5.600449197826759e-10, 1.7492634560879628e-10, 5.134895373986727e-11, 1.26598633034992e-11, 2.8758000008575507e-12, 5.98824805037656e-13, 1.1510091544446413e-13, 2.0543436329806364e-14, 3.4221904864959627e-15, 5.34449340253122e-16, 7.855611047585184e-17, 1.0905104093050293e-17], [3.273302449897612e-10, 8.179155855642442e-10, 1.021882205125631e-09, 8.511418208127553e-10, 5.316970944665206e-10, 2.657153422391473e-10, 1.1065925166174494e-10, 3.95013589950804e-11, 1.2337989563894105e-11, 3.42550209469938e-12, 9.049886292766771e-13, 2.028373157567576e-13, 4.2236600607198625e-14, 8.118353405291998e-15, 1.4489795814434958e-15, 2.4137559360253206e-16, 3.769603920738125e-17, 5.540757556318803e-18, 7.691640731701631e-19], [2.0988559148735396e-11, 5.24451067661794e-11, 6.552353604229375e-11, 5.457558757104662e-11, 3.4092651342898024e-11, 1.7037784508691698e-11, 7.0955198439728e-12, 2.5328444969990757e-12, 7.911173125672256e-13, 2.1964469959372022e-13, 5.488366132799596e-14, 1.3181634814344283e-14, 2.7082293911258666e-15, 5.205523878266683e-16, 9.290920749284243e-17, 1.5477109130402322e-17, 2.41708659889317e-18, 3.552758093076226e-19, 4.931913836840581e-20], [1.2336459993920368e-12, 3.0825696843360342e-12, 3.8512814306010125e-12, 3.2077931026317266e-12, 2.003866136774224e-12, 1.0014310438702767e-12, 4.170538628732531e-13, 1.4887317698477226e-13, 4.649955724841364e-14, 1.291007176916119e-14, 3.225900775249221e-15, 7.327919132952959e-16, 1.6133117881325389e-16, 3.0596543867806855e-17, 5.4609309442347126e-18, 9.096991187232209e-19, 1.4206926696482284e-19, 2.0882070928605134e-20, 2.8988344226245757e-21], [6.693239688116924e-14, 1.672471500150936e-13, 2.0895418729611303e-13, 1.7404124129923385e-13, 1.0872127306326634e-13, 5.433339881171882e-14, 2.2627572808094094e-14, 8.077226831535126e-15, 2.5228686528252704e-15, 7.004457095825875e-16, 1.7502368677453692e-16, 3.975817957190606e-17, 8.278803854127292e-18, 1.6824537171422375e-18, 2.9628693926807826e-19, 4.9356413822797946e-20, 7.708075546625639e-21, 1.132972554349409e-21, 1.5727845440549616e-22], [3.3720772645857386e-15, 8.425969163093352e-15, 1.0527184101477293e-14, 8.768257827780559e-15, 5.477415275062446e-15, 2.7373353917975853e-15, 1.1399849306815933e-15, 4.0693347659247465e-16, 1.2710299379883097e-16, 3.5288696691281675e-17, 8.817753770034742e-18, 2.0030308141177628e-18, 4.1708899658905746e-19, 8.016923301330952e-20, 1.512859435099719e-20, 2.486593169654839e-21, 3.8833550740207043e-22, 5.707954846894365e-23, 7.923742836395698e-24], [1.5856065574077903e-16, 3.962030199553557e-16, 4.950056250977406e-16, 4.1229799965686807e-16, 2.575571345590614e-16, 1.2871404201326583e-16, 5.360397878240371e-17, 1.9134685782267948e-17, 5.976593198209138e-18, 1.6593329418549008e-18, 4.1462538080639093e-19, 9.418582506724274e-20, 1.9612215145832093e-20, 3.7696900632516504e-21, 6.728216495800134e-22, 1.1850251935198906e-22, 1.826017848041952e-23, 2.683974869044156e-24, 3.7258750659574535e-25], [6.989798009575681e-18, 1.746573932438388e-17, 2.1821235014904795e-17, 1.8175251129542615e-17, 1.1353840194985675e-17, 5.6740756429489386e-18, 2.363013589014952e-18, 8.435105667916018e-19, 2.6346497525326486e-19, 7.31480457116818e-20, 1.827784861219338e-20, 4.1519750880794516e-21, 8.645613992276852e-22, 1.661785010772821e-22, 2.9659863634281774e-23, 4.940833730564267e-24, 8.158290050797169e-25, 1.1831713302237014e-25, 1.6424701322207786e-26], [2.900045952474579e-19, 7.246482168049142e-19, 9.053564093880422e-19, 7.54085645983335e-19, 4.710673793062901e-19, 2.354156740985363e-19, 9.804071569846758e-20, 3.499699707691584e-20, 1.0931081757374394e-20, 3.0348901871982116e-21, 7.583423843595774e-22, 1.7226418463687548e-22, 3.587038971743064e-23, 6.894695508757914e-24, 1.2305787286801497e-24, 2.049936899827897e-25, 3.201421510569798e-26, 4.975226103385371e-27, 6.814558664616418e-28], [1.1363746829786215e-20, 2.839513239230047e-20, 3.5476131053134334e-20, 2.954862960574253e-20, 1.845864005582332e-20, 9.224695622276273e-21, 3.841697305719499e-21, 1.3713472858783124e-21, 4.283313013040475e-22, 1.189213009335075e-22, 2.971542867727786e-23, 6.750122632997005e-24, 1.4055709258221541e-24, 2.701666646458968e-25, 4.8219874291678086e-26, 8.032618906194813e-27, 1.2544678304322778e-27, 1.8438812821654438e-28, 2.706321175641125e-29]] |
| Legacy trial inputs | {"lambda_home": 0.7053248337724208, "lambda_away": 2.4987473601464125, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0844 |
| Legacy p draw | 0.1456 |
| Legacy p away | 0.7700 |
| Legacy p over 1 5 | 0.8263 |
| Legacy p under 3 5 | 0.6012 |
| Legacy p btts yes | 0.4613 |
| Legacy p over 2 5 | 0.6206 |
| Legacy goal margin distribution | {"-1": 0.22526680785826017, "-10": 0.0001246853466257023, "-11": 2.7954272493998384e-05, "-12": 5.756472906062629e-06, "-13": 1.0959343631252323e-06, "-14": 1.9398823273955084e-07, "-15": 3.208097087625094e-08, "-16": 4.977367725000825e-09, "-17": 7.244496992972771e-10, "-18": 9.159890281665568e-11, "-2": 0.2200455969913192, "-3": 0.16139984882992456, "-4": 0.093061813452758, "-5": 0.04402254237200241, "-6": 0.017616349574774863, "-7": 0.0061008968978311226, "-8": 0.0018608854356469676, "-9": 0.000506882099830571, "0": 0.1456031342993104, "1": 0.06341809384214779, "10": 3.838062829555969e-10, "11": 2.4289114608817587e-11, "12": 1.4118442246058309e-12, "13": 7.587202721256481e-14, "14": 3.7908740638420375e-15, "15": 1.769613001041567e-16, "16": 7.74992235743373e-18, "17": 3.1839972763975835e-19, "18": 1.1363746829786215e-20, "2": 0.016806401360896707, "3": 0.0034796214425270237, "4": 0.000566326928914922, "5": 7.562016988806896e-05, "6": 8.54171890197322e-06, "7": 8.350065227013847e-07, "8": 7.189234438842421e-08, "9": 5.527602324325788e-09} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.0879 |
| Legacy raw p draw | 0.1434 |
| Legacy raw p away | 0.7687 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.7053 |
| Legacy lambda away | 2.4987 |
| Legacy model home team | Casa Pia |
| Legacy model away team | Sp Lisbon |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 27.3% |
| Market reference home draw last update utc | 2026-10-30T12:02:19Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.9% |
| Market reference draw away last update utc | 2026-10-30T12:02:19Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.7% |
| Market reference home away last update utc | 2026-10-30T12:02:19Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.42 |
| Market reference dc draw away odds | 1.04 |
| Market reference dc home away odds | 1.13 |
| Market p over 1 5 | 83.6% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.0% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 3 5 odds | 1.57 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.5% |
| Market reference btts yes odds | 2.04 |
| Market reference btts yes opposite odds | 1.92 |
| Market reference btts yes last update utc | 2026-10-30T12:02:59Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,356.0841 |
| Elo away rating | 1,692.9144 |
| Elo rating diff | -276.8303 |
| Elo home expectancy | 0.1689 |

</details>


---

## 2026-10-31 — FC Porto vs Estoril

The model's most likely 1X2 outcome is **FC Porto win** at **78.8%**. Expected goals are 2.34 for FC Porto and 0.69 for Estoril (3.04 combined). The most likely exact score is 2-0 at 14.9%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.6%; Double Chance 1X: 93.3%; Double Chance X2: 21.2%; Double Chance 12 (either team wins): 85.5%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 41.5%; BTTS No (at least one team does not score): 58.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Porto win | 78.8% | 1.27 |
| Draw | 14.5% | 6.88 |
| Estoril win | 6.7% | 14.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Porto expected goals | 2.34 |
| Estoril expected goals | 0.69 |
| Expected total goals | 3.04 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.4% |
| Under 3.5 | 66.6% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.90% |
| 2 | 1-0 | 13.87% |
| 3 | 3-0 | 11.02% |
| 4 | 2-1 | 9.75% |
| 5 | 3-1 | 7.21% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:30:00+00:00 |
| Fixture id | 60352ce6c1b34bca7b294edae8aa388b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Odds bookmakers 1x2 | 0.00 |
| Odds bookmakers ou25 | 10.00 |
| Matched home-team name | Porto |
| Matched away-team name | Estoril |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5377 |
| Dc lambda away | 0.6307 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.8905 |
| Shot lambda away | 0.8335 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 41.5% |
| P btts no | 58.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.73 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.71 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.05092399911096768, "-10": 1.734979716181481e-10, "-11": 1.0213425576043582e-11, "-12": 5.520466350335307e-13, "-13": 2.7579254367697212e-14, "-14": 1.2807270771761794e-15, "-15": 5.555155400070805e-17, "-16": 2.2536308481700863e-18, "-17": 7.994930706931677e-20, "-2": 0.012944892350858429, "-3": 0.002537448987169369, "-4": 0.0003883222192569199, "-5": 4.8565310570242924e-05, "-6": 5.125678135845186e-06, "-7": 4.6744125051500073e-07, "-8": 3.750402382998248e-08, "-9": 2.6850415737231393e-09, "0": 0.14527026062827517, "1": 0.2629161764257879, "10": 5.490269352992096e-05, "11": 1.0952531917796823e-05, "12": 2.006146826114945e-06, "13": 3.3963568734061076e-07, "14": 5.344797281447719e-08, "15": 7.85623937960163e-09, "16": 1.0800531388939199e-09, "17": 1.298437045724824e-10, "2": 0.2355303620338108, "3": 0.15645506434990697, "4": 0.0811387654921832, "5": 0.034387941104161567, "6": 0.01229915244414571, "7": 0.0038009725864171498, "8": 0.001033449875658733, "9": 0.00025073006601578264} |
| Raw goal margin distribution | {"-1": 0.07242040879156957, "-10": 3.837001508712093e-10, "-11": 2.383313450111448e-11, "-12": 1.35949737048153e-12, "-13": 7.168724933108716e-14, "-14": 3.5141894002515458e-15, "-15": 1.609366459531042e-16, "-16": 6.914303392328483e-18, "-17": 2.7882005511979595e-19, "-18": 9.827379051296806e-21, "-2": 0.019108200781520906, "-3": 0.00391399327928916, "-4": 0.0006282936958636726, "-5": 8.259930731898765e-05, "-6": 9.176021207999664e-06, "-7": 8.815730543716423e-07, "-8": 7.455824266436807e-08, "-9": 5.6291173927061436e-09, "0": 0.1560509882339361, "1": 0.23611197910435575, "10": 7.663558228733269e-05, "11": 1.613108221607545e-05, "12": 3.118204269539067e-06, "13": 5.57201087980987e-07, "14": 9.256334760377595e-08, "15": 1.436523329598319e-08, "16": 2.091462194295784e-09, "17": 2.8580475137344934e-10, "18": 3.413712893232071e-11, "2": 0.21943580610019503, "3": 0.15231813835192037, "4": 0.08285869686571448, "5": 0.03691438616739818, "6": 0.013896886279345535, "7": 0.004524444356610821, "8": 0.0012967207380884084, "9": 0.0003317683464365146} |
| Unadjusted home-win probability | 74.8% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 9.6% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 44.7% |
| P home draw | 93.3% |
| P draw away | 21.2% |
| P home away | 85.5% |
| Raw p home draw | 90.4% |
| Raw p draw away | 25.2% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9466 |
| Totals anchor target over 2 5 | 0.5618 |
| Totals anchor reference over odds | 1.64 |
| Totals anchor reference under odds | 2.03 |
| Totals anchor reference last update utc | 2026-10-30T12:02:58Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5943 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 3.73, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.24 |
| Reference draw odds | 7.00 |
| Reference away odds | 18.00 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:35Z |
| Market reference home last update utc | 2026-10-30T12:02:35Z |
| Market reference draw last update utc | 2026-10-30T12:02:35Z |
| Market reference away last update utc | 2026-10-30T12:02:35Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:37Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:37Z |
| Home probability edge | -1.7% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | -0.0573 |
| Raw edge prob draw | 0.0154 |
| Raw edge prob away | 0.0419 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.03887363585852925, 0.02555390425037749, 0.0071814460033302425, 0.0015173343841103492, 0.00024044290301729148, 3.0481238791819646e-05, 3.220119713192759e-06, 2.915846330856222e-07, 2.310283625960458e-08, 1.627097003904859e-09, 1.0313453150644992e-10, 5.942949908237514e-12, 3.139145735633396e-13, 1.5305896802145415e-14, 6.929811157043719e-16, 2.9283352514515785e-17, 1.1600894243224368e-18, 4.3254689720384395e-20, 1.5231804281089619e-21], [0.10955145055091177, 0.06506802259089262, 0.018346053564252417, 0.0038762524807485228, 0.0006142465425283415, 7.786878009250087e-05, 8.226266508742674e-06, 7.448955676365219e-07, 5.901957228506753e-08, 4.156657137577933e-09, 2.634722364359466e-10, 1.5182134252020307e-11, 8.019406646686236e-13, 3.9101150722412065e-14, 1.7703215566659153e-15, 7.480860449595548e-17, 2.9636180106447387e-18, 1.1050042765026674e-19, 3.891187054689174e-21], [0.13563397610089553, 0.08597241927157306, 0.027727162307349153, 0.004951226786875594, 0.0007845912902259555, 9.946359061235986e-05, 1.0507600136046638e-05, 9.514723063639677e-07, 7.538706229769064e-08, 5.3093941289034125e-09, 3.365391705309587e-10, 1.9392490598555824e-11, 1.0243373258352274e-12, 4.994480256793846e-14, 2.2612725967362597e-15, 9.555475767090176e-17, 3.785497707708054e-18, 1.411447474230469e-19, 4.970303062972874e-21], [0.11549893942091156, 0.07320970401936827, 0.023202207697645392, 0.004988664846798203, 0.000668117712869911, 8.46980937739202e-05, 8.947733499087477e-06, 8.102250293957236e-07, 6.419575678415854e-08, 4.521207801206014e-09, 2.8657950159187575e-10, 1.6513650644563005e-11, 8.722731438265367e-13, 4.2530432949134975e-14, 1.925583796720122e-15, 8.136953206622464e-17, 3.2235357466430965e-18, 1.2019162971428016e-19, 4.232455236340189e-21], [0.07376473095556839, 0.046756222588722286, 0.014818357787293715, 0.0031309020183795076, 0.0005048771988013593, 5.409341532491636e-05, 5.714573289863589e-06, 5.174595680834636e-07, 4.099936113192738e-08, 2.8875215540706154e-09, 1.8302730690251003e-10, 1.0546633614108249e-11, 5.570873126345151e-13, 2.716255196494705e-14, 1.2297963202919652e-15, 5.196759096611091e-17, 2.058748316382666e-18, 7.676177178281487e-20, 2.703106395222833e-21], [0.03768855755890853, 0.023889121039886003, 0.007571132208579696, 0.0015996693731869618, 0.0002534900362008482, 3.270146140628959e-05, 2.9197425594808183e-06, 2.643852212769355e-07, 2.0947772219624384e-08, 1.4753191787377386e-09, 9.351400190427378e-11, 5.3885834445388494e-12, 2.846321944861462e-13, 1.3878141896760648e-14, 6.283388931625841e-16, 2.6551761498375468e-17, 1.0518747023971474e-18, 3.921983333611044e-20, 1.3810960827007394e-21], [0.016046821568954848, 0.01017137528192834, 0.0032235939896651192, 0.0006810982076119662, 0.0001079295585686702, 1.3682361201531213e-05, 1.4709099072973389e-06, 1.1256844904898224e-07, 8.919024363031543e-09, 6.281530828410697e-10, 3.98158645475166e-11, 2.294320680986105e-12, 1.211890911601e-13, 5.908957019059877e-15, 2.675305916830257e-16, 1.130505932576252e-17, 4.478612808644018e-19, 1.6698799536835806e-20, 5.880353041912251e-22], [0.0058562787634278465, 0.0037120378513868847, 0.0011764488651205866, 0.00024856641870833225, 3.9388833425721986e-05, 4.993370244304099e-06, 5.275130078790963e-07, 4.860840891143102e-08, 3.254993067834003e-09, 2.2924412435300013e-10, 1.4530778010783854e-11, 8.373110788834774e-13, 4.4227892599807845e-14, 2.156470635385903e-15, 9.763514325302199e-17, 4.125775223726566e-18, 1.6344672973506594e-19, 6.09421776655797e-21, 2.1460316295554084e-22], [0.0018700900179298558, 0.0011853679123691758, 0.0003756763241883581, 7.937490635212524e-05, 1.2578066581692034e-05, 1.5945367744474027e-06, 1.68451135988176e-07, 1.525339647427832e-08, 1.2298519785882812e-09, 7.320470318094653e-11, 4.640124558349388e-12, 2.673791931321136e-13, 1.4123327082975436e-14, 6.886274325564245e-16, 3.117790565860203e-17, 1.3174869868382473e-18, 5.219357036923464e-20, 1.946071263462194e-21, 6.852939367668061e-23], [0.0005308242568264721, 0.00033646617816068976, 0.0001066355649635182, 2.253053343479111e-05, 3.5702788537054232e-06, 4.526085857703725e-07, 4.781478336079353e-08, 4.329670106737089e-09, 3.4304846066657795e-10, 2.458607702015172e-11, 1.3170973838974116e-12, 7.589547033801641e-14, 4.008900390279942e-15, 1.9546660407381337e-16, 8.849835271006752e-18, 3.7396812129991943e-19, 1.481512276774709e-20, 5.523915010798265e-22, 1.9452039271062074e-23], [0.00013560681573636976, 8.595520350961058e-05, 2.7241613816601966e-05, 5.755754106264626e-06, 9.12079921773733e-07, 1.1562547924656361e-07, 1.2214985342693572e-08, 1.1060775177715735e-09, 8.76367437923345e-11, 6.17212023901198e-12, 3.9811693354114067e-13, 1.9388607300809486e-14, 1.0241322048473538e-15, 4.9934801246124336e-17, 2.26081978255367e-18, 9.553562306963794e-20, 3.784739671258718e-21, 1.41116483540345e-22, 4.969307772214064e-24], [3.1493403012853095e-05, 1.9962284716150497e-05, 6.326607685521043e-06, 1.336719564773762e-06, 2.118219530513449e-07, 2.6852926209443278e-08, 2.8368150531711646e-09, 2.5687606365123005e-10, 2.0352806575384508e-11, 1.4334166691804296e-12, 9.085798589430866e-14, 5.3277850208564646e-15, 2.378450381756819e-16, 1.1596886273535121e-17, 5.250540554673429e-19, 2.218724673297663e-20, 8.789700659103083e-22, 3.277297135663654e-23, 1.154074826662767e-24], [6.7045417956966186e-06, 4.249714524734112e-06, 1.3468536771094584e-06, 2.84570460279998e-07, 4.509417851412339e-08, 5.716643769315533e-09, 6.039215604260084e-10, 5.4685621123916567e-11, 4.332851622566919e-12, 3.051560342731532e-13, 1.9342500512015015e-14, 1.1145783081952016e-15, 5.99108681548168e-17, 2.4688284301675666e-18, 1.1177727787765988e-19, 4.7233804169071535e-21, 1.8712145974370512e-22, 6.976945493634413e-24, 2.456877368115476e-25], [1.317517850332433e-06, 8.351166889209385e-07, 2.646718918982011e-07, 5.592129522361462e-08, 8.861513127797832e-09, 1.123384779985897e-09, 1.1867737726276793e-10, 1.0746339449106282e-11, 8.514540634585784e-13, 5.996659198240723e-14, 3.801018842331811e-15, 2.1902717014652058e-16, 1.1569308470870284e-17, 5.740375745787899e-19, 2.1965491953515945e-20, 9.281973627459837e-22, 3.6771470878268656e-23, 1.3710482399498067e-24, 4.828040285538375e-26], [2.4041370978618785e-07, 1.5238768965231247e-07, 4.8295931164287644e-08, 1.0204223067919423e-08, 1.6170021869801139e-09, 2.04989330812941e-10, 2.1655621992702405e-11, 1.9609353550158133e-12, 1.5536884760760653e-13, 1.0942387488782473e-14, 6.935898747949562e-16, 3.996692303304223e-17, 2.1111064024224737e-18, 1.029336623879524e-19, 4.742481680424734e-21, 1.6937256017837854e-22, 6.709864102341203e-24, 2.5018165300681727e-25, 8.809953320560893e-27], [4.094479761014421e-08, 2.595310856706338e-08, 8.225267721520024e-09, 1.7378786287034344e-09, 2.7539123014217163e-10, 3.491168066013918e-11, 3.688163459569597e-12, 3.3396640029016983e-13, 2.6460828818258464e-14, 1.8635952229946945e-15, 1.1812511471654975e-16, 6.8067564705169765e-18, 3.595419930816021e-19, 1.753060579404511e-20, 7.937057801427278e-22, 3.4130649770025173e-23, 1.1427552443089348e-24, 4.260837352930349e-26, 1.5004209035582531e-27], [6.537466912868575e-09, 4.143813095835822e-09, 1.3132905452584474e-09, 2.774790619777129e-10, 4.3970447046551687e-11, 5.574186966593967e-12, 5.888720422008753e-13, 5.3322874195033004e-14, 4.22487844569504e-15, 2.975516505249332e-16, 1.8860492031029702e-17, 1.0868033988995483e-18, 5.740641108885231e-20, 2.7990309399580015e-21, 1.2672733971336263e-22, 5.355126247965924e-24, 2.158867575086263e-25, 6.803082404050154e-27, 2.395652826467569e-28], [9.824067555262401e-10, 6.22704486805722e-10, 1.973525098981369e-10, 4.1697695550458457e-11, 6.607584374463296e-12, 8.376514949190566e-13, 8.849174766145437e-14, 8.013004506402976e-15, 6.34886444802944e-16, 4.471406975969101e-17, 2.834228460469898e-18, 1.633175380063693e-19, 8.626651089153852e-21, 4.206196285183374e-22, 1.9043736098948424e-23, 8.047325168624334e-25, 3.1880286990969315e-26, 1.2096217112322463e-27, 3.600026664738524e-29], [1.3942787002328232e-10, 8.837720196941773e-11, 2.800921303122187e-11, 5.917936580521032e-12, 9.377800082787928e-13, 1.1888351042111988e-13, 1.2559172482955101e-14, 1.137243961862076e-15, 9.010612376958994e-17, 6.346034849207278e-18, 4.022472719978455e-19, 2.3178806877683682e-20, 1.224335622723253e-21, 5.969635139864384e-23, 2.7027781991783633e-24, 1.1421149145549343e-25, 4.524602956848336e-27, 1.6870276799628214e-28, 6.0454129999736556e-30]] |
| Legacy trial inputs | {"lambda_home": 2.5546461751219502, "lambda_away": 0.6338560716351768, "rho": 0.05, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7987 |
| Legacy p draw | 0.1372 |
| Legacy p away | 0.0641 |
| Legacy p over 1 5 | 0.8260 |
| Legacy p under 3 5 | 0.6032 |
| Legacy p btts yes | 0.4300 |
| Legacy p over 2 5 | 0.6181 |
| Legacy goal margin distribution | {"-1": 0.04957643137024335, "-10": 1.1938479031936042e-10, "-11": 6.796813995649867e-12, "-12": 3.5536046497073914e-13, "-13": 1.717507479509674e-14, "-14": 7.716981126441449e-16, "-15": 3.2392347727819915e-17, "-16": 1.2755601550356763e-18, "-17": 4.714587677507357e-20, "-18": 1.5231804281089619e-21, "-2": 0.011932975979575326, "-3": 0.0022405313010457405, "-4": 0.0003296720236230421, "-5": 3.972615673851256e-05, "-6": 4.045112090195641e-06, "-7": 3.5621101627491827e-07, "-8": 2.7613117455521688e-08, "-9": 1.9108618064445177e-09, "0": 0.13719658503693463, "1": 0.22212469505162905, "10": 0.0001569735279356961, "11": 3.601827470759943e-05, "12": 7.589737115068262e-06, "13": 1.4784150132361283e-06, "14": 2.6772274437406846e-07, "15": 4.529188115245868e-08, "16": 7.188180612705519e-09, "17": 1.070783957495658e-09, "18": 1.3942787002328232e-10, "2": 0.22537480307945326, "3": 0.17054842473754836, "4": 0.10113905555525023, "5": 0.04911944540900571, "6": 0.020158005825638012, "7": 0.007154255654128698, "8": 0.0022351807690290737, "9": 0.00062339970872647} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7923 |
| Legacy raw p draw | 0.1337 |
| Legacy raw p away | 0.0740 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5546 |
| Legacy lambda away | 0.6339 |
| Legacy model home team | Porto |
| Legacy model away team | Estoril |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 91.4% |
| Market reference home draw last update utc | 2026-10-30T12:02:14Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 23.8% |
| Market reference draw away last update utc | 2026-10-30T12:02:14Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.9% |
| Market reference home away last update utc | 2026-10-30T12:02:14Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 4.00 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.5% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 38.8% |
| Market reference btts yes odds | 2.48 |
| Market reference btts yes opposite odds | 1.60 |
| Market reference btts yes last update utc | 2026-10-30T12:02:59Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,693.7612 |
| Elo away rating | 1,387.3773 |
| Elo rating diff | 366.3839 |
| Elo home expectancy | 0.8918 |

</details>


---

## 2026-10-31 — Moreirense FC vs CF Estrela

The model's most likely 1X2 outcome is **Moreirense FC win** at **36.9%**. Expected goals are 1.42 for Moreirense FC and 1.07 for CF Estrela (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.0%; Double Chance 1X: 65.0%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Moreirense FC win | 36.9% | 2.71 |
| Draw | 28.1% | 3.56 |
| CF Estrela win | 35.0% | 2.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Moreirense FC expected goals | 1.42 |
| CF Estrela expected goals | 1.07 |
| Expected total goals | 2.49 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.2% |
| Under 1.5 | 26.8% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.34% |
| 2 | 0-1 | 10.40% |
| 3 | 1-0 | 8.96% |
| 4 | 1-2 | 8.31% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Moreirense FC win | 36.9% | 33.0% | 2.89 | +6.5% |
| Draw | 28.1% | 29.3% | 3.24 | -8.9% |
| CF Estrela win | 35.0% | 37.6% | 2.55 | -10.7% |
| Over 2.5 | 47.9% | 47.9% | 2.00 | -4.1% |
| Under 2.5 | 52.1% | 52.1% | 1.85 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:30:00+00:00 |
| Fixture id | 853df01a49c2a57a62c1ac2d356b395b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Moreirense |
| Matched away-team name | Estrela |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4765 |
| Dc lambda away | 1.0418 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2894 |
| Shot lambda away | 1.1237 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.39 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.73 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.2145728258255073, "-10": 9.780805692827692e-08, "-11": 9.96976620572893e-09, "-12": 9.333545488392167e-10, "-13": 8.076414414150143e-11, "-14": 6.463433390586273e-12, "-15": 4.3907395609946507e-13, "-2": 0.09393772732354164, "-3": 0.03140379806833269, "-4": 0.008244954801087157, "-5": 0.0017749739529536429, "-6": 0.00032313613932427127, "-7": 5.0900141460645515e-05, "-8": 7.0604693630211e-06, "-9": 8.745031374971582e-07, "0": 0.28117341635471604, "1": 0.18650423635401858, "10": 1.1317601432956575e-06, "11": 1.536637517154698e-07, "12": 1.9161954323862152e-08, "13": 2.2086069850686506e-09, "14": 2.3543434494821653e-10, "15": 2.1303497596440635e-11, "2": 0.10968980427580266, "3": 0.0488444341431467, "4": 0.017081573725267807, "5": 0.0048982199053151316, "6": 0.0011877868705464554, "7": 0.00024921757839921327, "8": 4.604685245618352e-05, "9": 7.59686558496508e-06} |
| Raw goal margin distribution | {"-1": 0.18144207906868895, "-10": 4.996615074849299e-08, "-11": 4.789244087009395e-09, "-12": 4.214406953077513e-10, "-13": 3.4118786962986296e-11, "-14": 2.3450246059482496e-12, "-2": 0.07617633394763033, "-3": 0.024224874311348125, "-4": 0.0060230536334778565, "-5": 0.001224783659680804, "-6": 0.0002102843861316402, "-7": 3.120649662879328e-05, "-8": 4.075249942125986e-06, "-9": 4.749573054827024e-07, "0": 0.25311564883249627, "1": 0.23959075572336744, "10": 8.785021595967273e-07, "11": 1.1216067265643227e-07, "12": 1.3146701348366274e-08, "13": 1.4176878049636435e-09, "14": 1.297899662223092e-10, "2": 0.13515541672700718, "3": 0.05725080719470308, "4": 0.018960225850544743, "5": 0.005135619667865604, "6": 0.0011744842324684218, "7": 0.00023216239395769395, "8": 4.038385757368917e-05, "9": 6.2692388710785235e-06} |
| Unadjusted home-win probability | 45.8% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 28.9% |
| Raw p over 1 5 | 70.4% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.1% |
| P home draw | 65.0% |
| P draw away | 63.1% |
| P home away | 71.9% |
| Raw p home draw | 71.1% |
| Raw p draw away | 54.2% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0650 |
| Totals anchor target over 2 5 | 0.4793 |
| Totals anchor reference over odds | 2.00 |
| Totals anchor reference under odds | 1.85 |
| Totals anchor reference last update utc | 2026-10-30T12:02:58Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4415 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 5.28, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.89 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Home probability edge | +3.8% |
| Draw probability edge | -1.2% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.1272 |
| Raw ev home | 0.3223 |
| Raw edge prob draw | -0.0401 |
| Raw ev draw | -0.1799 |
| Raw edge prob away | -0.0871 |
| Raw ev away | -0.2622 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.08568417358675283, 0.11081726277415282, 0.05146918071920019, 0.017104140482151933, 0.004263011634514725, 0.0008500055628037719, 0.0001412361179413801, 2.0115136603530126e-05, 2.5067340115740595e-06, 2.7767769686786984e-07, 2.7683197612372426e-08, 2.508989374404527e-09, 2.084456471250612e-10, 1.5985445067847175e-11, 1.1383398803889182e-12, 7.565818984697701e-14], [0.11015381343735763, 0.12827484102388334, 0.07541386083376977, 0.025061391146664794, 0.006246265466940013, 0.0012454482532165303, 0.00020694250023606454, 2.9473173873641996e-05, 3.6729259579141244e-06, 4.0685992851686213e-07, 4.0562075848127926e-08, 3.6762305688725624e-09, 3.054194918985826e-10, 2.3422252168525125e-11, 1.6679225144369858e-12, 1.1085616907685494e-13], [0.07686827823413199, 0.07663416113289356, 0.04931023391987828, 0.018360271504479247, 0.004576087943040372, 0.0009124301177062976, 0.00015160852276373143, 2.159239569950236e-05, 2.6908289890414688e-06, 2.9807039474170347e-07, 2.9716256412047547e-08, 2.6932499861065776e-09, 2.2375393134408437e-10, 1.715941890630957e-11, 1.221939757225815e-12, 8.121454033761331e-14], [0.03754307306675157, 0.03742872842888681, 0.018657366024786282, 0.00800338534330317, 0.0022349974261445175, 0.0004456380624659518, 7.404679769623971e-05, 1.0545896279392363e-05, 1.3142220909126612e-06, 1.4557993057602176e-07, 1.451365389438951e-08, 1.3154045249647534e-09, 1.0928318399219487e-10, 8.380795467024333e-12, 5.968050103706801e-13, 3.9665821741064925e-14], [0.013752249637382849, 0.013710364520471497, 0.006834303486363135, 0.0022711627676017983, 0.000730689588591926, 0.0001632398571117197, 2.7123779797059205e-05, 3.8630241596442534e-06, 4.814073222258467e-07, 5.3326789309832695e-08, 5.3164372333436255e-09, 4.818404548102571e-10, 4.003107643203762e-11, 3.0699349309376523e-12, 2.186132039022399e-13, 1.4529825027513445e-14], [0.004030024281765824, 0.004017750068989864, 0.0020027566198428737, 0.0006655522799991556, 0.0001658813031835691, 4.269451504130892e-05, 7.948480726984552e-06, 1.132038871814508e-06, 1.4107387875771848e-07, 1.5627134574626183e-08, 1.5579539135632015e-09, 1.4120080597896767e-10, 1.1730895984305062e-11, 8.996282529288269e-13, 6.406344731016049e-14, 4.257888652014863e-15], [0.0009841478145918418, 0.0009811504034511814, 0.0004890810607508492, 0.00016253049015644796, 4.0508868085088736e-05, 8.07709810980359e-06, 1.7324023268489285e-06, 2.764483546091943e-07, 3.445079725786889e-08, 3.816207859971558e-09, 3.804584866164153e-10, 3.448179338560186e-11, 2.8647310385681917e-12, 2.1969276539372186e-13, 1.5644546349454882e-14, 1.0397931919704808e-15], [0.00020599952185644622, 0.0002053721107575969, 0.00010237330527986079, 3.4020502573800735e-05, 8.479221650189811e-06, 1.6906793105029759e-06, 2.8092167033779073e-07, 5.164542463919745e-08, 7.211160414594482e-09, 7.987997156555079e-10, 7.963668177398034e-11, 7.217648451653268e-12, 5.996388097829751e-13, 4.598557651138667e-14, 3.274679900585162e-15, 2.176470822773117e-16], [3.772942141303084e-05, 3.761450921549576e-05, 1.8749973502561586e-05, 6.2309556193266584e-06, 1.5529945118874814e-06, 3.096529137806011e-07, 5.145163439560365e-08, 7.327846937650992e-09, 1.1787753701577921e-09, 1.4630252936984073e-10, 1.4585693692433753e-11, 1.3219336510562596e-12, 1.098256206908868e-13, 8.422394282683563e-15, 5.997673045477183e-16, 3.98627065371527e-17], [6.1424489504033916e-06, 6.12374094268149e-06, 3.0525449568946633e-06, 1.0144159483644893e-06, 2.528315874526207e-07, 5.041230806110613e-08, 8.376461282829591e-09, 1.1929927373692863e-09, 1.4866990611436395e-10, 2.125813733130443e-11, 2.3745892610230212e-12, 2.15214272133763e-13, 1.7879899645297723e-14, 1.371187921362755e-15, 9.764369323281018e-17, 6.48975337439988e-18], [9.000061470794946e-07, 8.972650055437206e-07, 4.4726610634041726e-07, 1.486346238438917e-07, 3.7045482139217707e-08, 7.386530602013552e-09, 1.2273389174565178e-09, 1.748001173022428e-10, 2.1783466247590323e-11, 2.413013390930789e-12, 3.1053058583692917e-13, 3.153370413390338e-14, 2.619805181917811e-15, 2.009096970918397e-16, 1.430698485940242e-17, 9.508940126569877e-19], [1.1988275380082465e-07, 1.1951762785481553e-07, 5.957680698499236e-08, 1.9798451459889386e-08, 4.934537868591261e-09, 9.839017572012568e-10, 1.6348418257927103e-10, 2.328375144425442e-11, 2.901604538549649e-12, 3.214185716417087e-13, 3.204396296645272e-14, 3.748851061237947e-15, 3.489636828027541e-16, 2.676160360772721e-17, 1.9057211432361153e-18, 1.2666112690446659e-19], [1.463792050759524e-08, 1.4593337909986402e-08, 7.274445548619556e-09, 2.4174299426324185e-09, 6.025167988897205e-10, 1.2013634365726593e-10, 1.996174089244265e-11, 2.8429919396567754e-12, 3.542916327258673e-13, 3.9245841058781006e-14, 3.912631031403904e-15, 3.5461039657392856e-16, 3.802899678808255e-17, 3.2676445430718017e-18, 2.3269230744132185e-19, 1.5465573222570247e-20], [1.6498328703033702e-09, 1.6448079875039037e-09, 8.198992044749283e-10, 2.724673480048685e-10, 6.79093740946631e-11, 1.354050861124541e-11, 2.249878065381107e-12, 3.2043223281746354e-13, 3.9932036865570585e-14, 4.423379575526584e-15, 4.4099073236732677e-16, 3.996796458318068e-17, 3.320519539382229e-18, 3.2870577821037184e-19, 2.622663630972942e-20, 1.7431172035290542e-21], [1.726695814319793e-10, 1.7214368306654722e-10, 8.580969321278377e-11, 2.8516114438446817e-11, 7.107315784099409e-12, 1.4171338178332816e-12, 2.354696107799772e-13, 3.3536063266658125e-14, 4.179240343318281e-15, 4.629457404861243e-16, 4.6153575034086155e-17, 4.1830004962848054e-18, 3.475216970894819e-19, 2.6651019463965725e-20, 2.4497989343950975e-21, 1.8243261080432922e-22], [1.6866636956173602e-11, 1.6815266374673223e-11, 8.382026126071369e-12, 2.785499018676051e-12, 6.942538116391433e-13, 1.3842786566970496e-13, 2.300104283742603e-14, 3.275855534987892e-15, 4.082347859927615e-16, 4.522126984052719e-17, 4.5083539780057336e-18, 4.0860208366302914e-19, 3.394646729661927e-20, 2.603313600940798e-21, 1.8538462210667073e-22, 1.590475917630845e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4652236499586866, "lambda_away": 0.9969543079848188, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T12:02:58Z", "over": 2.0, "under": 1.85, "bookmaker": "pinnacle", "event_id": "853df01a49c2a57a62c1ac2d356b395b", "kickoff_utc": "2026-10-31T15:30:00Z", "home_team": "Moreirense FC", "away_team": "CF Estrela"}} |
| Legacy p home | 0.4081 |
| Legacy p draw | 0.2720 |
| Legacy p away | 0.3199 |
| Legacy p over 1 5 | 0.6933 |
| Legacy p under 3 5 | 0.7700 |
| Legacy p btts yes | 0.4861 |
| Legacy p over 2 5 | 0.4367 |
| Legacy goal margin distribution | {"-1": 0.20699786468460912, "-10": 3.1591785779148647e-08, "-11": 2.832179620044817e-09, "-12": 2.331295048725532e-10, "-13": 1.7734582122621773e-11, "-14": 1.2491960494657731e-12, "-15": 7.565818984697701e-14, "-2": 0.08158058895444072, "-3": 0.024340890859717447, "-4": 0.005671111729018525, "-5": 0.0010799096006634278, "-6": 0.00017355116128400178, "-7": 2.4101140404438447e-05, "-8": 2.9446665475948126e-06, "-9": 3.2104544092426796e-07, "0": 0.27204780322555017, "1": 0.20789075016456526, "10": 1.0270779335745844e-06, "11": 1.3532520128353606e-07, "12": 1.63713236873306e-08, "13": 1.8303585794959887e-09, "14": 1.8948484780665254e-10, "15": 1.6866636956173602e-11, "2": 0.12183911464351266, "3": 0.053427522125989065, "4": 0.01829470592749874, "5": 0.005120039330601823, "6": 0.001209322364470659, "7": 0.00024682026761071513, "8": 4.432084320956561e-05, "9": 7.101777542383692e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4858 |
| Legacy raw p draw | 0.2509 |
| Legacy raw p away | 0.2633 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4652 |
| Legacy lambda away | 0.9970 |
| Legacy model home team | Moreirense |
| Legacy model away team | Estrela |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 61.9% |
| Market reference home draw last update utc | 2026-10-30T12:02:19Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.8% |
| Market reference draw away last update utc | 2026-10-30T12:02:19Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market reference home away last update utc | 2026-10-30T12:02:19Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.51 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 72.9% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market reference over 1 5 last update utc | 2026-10-30T12:02:59Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.51 |
| Market reference under 3 5 last update utc | 2026-10-30T12:02:59Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.3% |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.16 |
| Market reference btts yes last update utc | 2026-10-30T12:02:59Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,438.8922 |
| Elo away rating | 1,379.1640 |
| Elo rating diff | 119.7282 |
| Elo home expectancy | 0.6658 |

</details>


---

## 2026-11-01 — Académico de Viseu vs Rio Ave FC

The model's most likely 1X2 outcome is **Académico de Viseu win** at **53.6%**. Expected goals are 2.00 for Académico de Viseu and 0.93 for Rio Ave FC (2.93 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 51.5%; Under 3.5 goals: 69.9%; Double Chance 1X: 77.8%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Académico de Viseu win | 53.6% | 1.87 |
| Draw | 24.2% | 4.13 |
| Rio Ave FC win | 22.2% | 4.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Académico de Viseu expected goals | 2.00 |
| Rio Ave FC expected goals | 0.93 |
| Expected total goals | 2.93 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 51.5% |
| Under 2.5 | 48.5% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.49% |
| 2 | 1-0 | 10.42% |
| 3 | 2-0 | 9.57% |
| 4 | 2-1 | 8.54% |
| 5 | 0-1 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Académico de Viseu win | 53.6% | 49.7% | 1.95 | +4.5% |
| Draw | 24.2% | 26.0% | 3.61 | -12.6% |
| Rio Ave FC win | 22.2% | 24.3% | 3.86 | -14.4% |
| Over 2.5 | 51.5% | 51.5% | 1.86 | -4.1% |
| Under 2.5 | 48.5% | 48.5% | 1.97 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | ce5c2cbdf5db2a13f40f528d3e5044b9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Academico Viseu |
| Matched away-team name | Rio Ave |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1613 |
| Dc lambda away | 0.7702 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6276 |
| Shot lambda away | 1.3047 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.11 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.15267422166529748, "-10": 7.904022966081287e-09, "-11": 6.332585754206085e-10, "-12": 4.6597877794594125e-11, "-13": 3.1699340942243596e-12, "-14": 2.0044976553031345e-13, "-15": 1.1787233803032451e-14, "-16": 5.939839260245561e-16, "-2": 0.05207719298993461, "-3": 0.013687423557633627, "-4": 0.0028249939602182695, "-5": 0.00047806472830922136, "-6": 6.841175121692716e-05, "-7": 8.470415966956414e-06, "-8": 9.235343829705467e-07, "-9": 8.991035552933391e-08, "0": 0.24222644626334736, "1": 0.21782815425458474, "10": 1.1355851758089397e-05, "11": 1.9565930038141763e-06, "12": 3.096231683395757e-07, "13": 4.529658291397763e-08, "14": 6.159829001656416e-09, "15": 7.789738831943417e-10, "16": 8.441771400883402e-11, "2": 0.16354449238155683, "3": 0.09243957885553668, "4": 0.041030014532373905, "5": 0.014932026271543632, "6": 0.004595265897249193, "7": 0.0012235805712245426, "8": 0.0002868988440985645, "9": 6.0066640173251964e-05} |
| Raw goal margin distribution | {"-1": 0.11752982903125388, "-10": 8.460697424854364e-09, "-11": 7.058936597552521e-10, "-12": 5.409974100359401e-11, "-13": 3.833613575496651e-12, "-14": 2.5258756872973756e-13, "-15": 1.5546811936156673e-14, "-16": 8.935447335979406e-16, "-17": 4.408219460884811e-17, "-2": 0.04118711619844327, "-3": 0.011180651232078544, "-4": 0.002390922598105287, "-5": 0.0004199781544159009, "-6": 6.245298092308847e-05, "-7": 8.04142743440752e-06, "-8": 9.122442249497621e-07, "-9": 9.243961844858005e-08, "0": 0.19961622657981387, "1": 0.24704245960119844, "10": 1.7901322654384476e-05, "11": 3.211930454555925e-06, "12": 5.293829305199446e-07, "13": 8.067351460111764e-08, "14": 1.1430954911618536e-08, "15": 1.5130726454749341e-09, "16": 1.8701766480274418e-10, "17": 1.9841633962244374e-11, "2": 0.1904834184025754, "3": 0.11120153630871588, "4": 0.05113957322864243, "5": 0.01931817869270291, "6": 0.006177895334848334, "7": 0.001710678577291731, "8": 0.0004173441092582985, "9": 9.094717322033962e-05} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 20.0% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 51.9% |
| P home draw | 77.8% |
| P draw away | 46.4% |
| P home away | 75.8% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9592 |
| Totals anchor target over 2 5 | 0.5153 |
| Totals anchor reference over odds | 1.86 |
| Totals anchor reference under odds | 1.97 |
| Totals anchor reference last update utc | 2026-10-30T12:02:58Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5407 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.86 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Home probability edge | +3.9% |
| Draw probability edge | -1.8% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1309 |
| Raw ev home | 0.2238 |
| Raw edge prob draw | -0.0609 |
| Raw ev draw | -0.2794 |
| Raw edge prob away | -0.0701 |
| Raw ev away | -0.3331 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06208702006917117, 0.06856206788808362, 0.02410470135564856, 0.006245142063709791, 0.0012135122155364703, 0.00018864094776175, 2.4436924158965352e-05, 2.7133781448064415e-06, 2.636223075873742e-07, 2.276677258591238e-08, 1.7695518442655705e-09, 1.2503523871456377e-10, 8.098656950994888e-12, 4.842074559326122e-13, 2.688222789278203e-14, 1.3929509410006017e-15, 6.766711490719588e-17, 3.0937880691827895e-18], [0.10542762778641447, 0.10524823321795714, 0.05080598416527683, 0.013163016795658905, 0.002557745126034028, 0.0003976024785994873, 5.150621712961106e-05, 5.719043975093263e-06, 5.556422619506669e-07, 4.798600366078675e-08, 3.729721503408109e-09, 2.6353939277265174e-10, 1.7069708964298625e-11, 1.0205742015159421e-12, 5.666023505111788e-14, 2.9359518878627442e-15, 1.426233960654047e-16, 6.520841944253745e-18], [0.10694966824658629, 0.08312683845511089, 0.0453739044879665, 0.013871983166694697, 0.002695506500055587, 0.0004190175379846943, 5.428036658266082e-05, 6.027074414904991e-06, 5.855694195441451e-07, 5.057055273521458e-08, 3.930606084830011e-09, 2.7773375032909136e-10, 1.7989091641303722e-11, 1.0755428154175923e-12, 5.971198237088686e-14, 3.0940836587011887e-15, 1.5030516029187272e-16, 6.8720576056088374e-18], [0.07514001897039858, 0.05840272644946386, 0.022696816579688528, 0.008259211319368732, 0.0018937918449828794, 0.0002943906817972258, 3.813595536675738e-05, 4.234463680876544e-06, 4.1140564542552255e-07, 3.5529537904750384e-08, 2.7615402704974562e-09, 1.95128415174995e-10, 1.2638661805582037e-11, 7.556480434106755e-13, 4.195206550583906e-14, 2.1738216548252677e-15, 1.0560044533883447e-16, 4.828126606812563e-18], [0.03959354813883728, 0.030774162594065246, 0.01195963898013228, 0.0030985509158405326, 0.0008456556024464402, 0.0001551233522572766, 2.0094988067930864e-05, 2.23126695851637e-06, 2.167820749840628e-07, 1.8721587892286316e-08, 1.455139074164367e-09, 1.028190624030822e-10, 6.659693083214855e-12, 3.981738039563883e-13, 2.210581189477018e-14, 1.1454523636662664e-15, 5.564406787883486e-17, 2.5440859058412385e-18], [0.016690430220306453, 0.012972669475428692, 0.005041516338924828, 0.0013061761391921006, 0.00025380698859719903, 5.5415142801113765e-05, 8.470925488910733e-06, 9.405776250061157e-07, 9.138322442957986e-08, 7.891976622904277e-09, 6.134054238589116e-10, 4.3342778483463626e-11, 2.807354933290888e-12, 1.678478540792692e-13, 9.318576592305298e-15, 4.828587900083647e-16, 2.3456433579760558e-17, 1.072444635095926e-18], [0.005863128254341129, 0.004557127882963471, 0.0017710182722258114, 0.00045884246995179026, 8.915905140557555e-05, 1.3859809356143138e-05, 2.5217433889162827e-06, 3.304125283640038e-07, 3.210172284678403e-08, 2.7723474176269714e-09, 2.1548124431314063e-10, 1.522574707743983e-11, 9.861868035801621e-13, 5.896273988703815e-14, 3.2734931926508425e-15, 1.6962193168098166e-16, 8.239936098246663e-18, 3.7673567177419555e-19], [0.001765405469212921, 0.0013721648477550642, 0.0005332589034784493, 0.0001381588412909594, 2.684605728429987e-05, 4.173230087789224e-06, 5.406085389372491e-07, 8.43101274664532e-08, 9.665924848720284e-09, 8.347621067325555e-10, 6.488204772623945e-11, 4.584518024735846e-12, 2.9694379880176685e-13, 1.7753857490544268e-14, 9.856585998196768e-16, 5.107367140849223e-17, 2.4810694262127036e-18, 1.1343623856519382e-19], [0.0004651227627277083, 0.0003615175754441407, 0.00014049512067368041, 3.6400035616271045e-05, 7.07299968770737e-06, 1.0995005633444166e-06, 1.424314932573467e-07, 1.5815022317153742e-08, 2.158115614131939e-09, 2.19930698117159e-10, 1.7094156450820314e-11, 1.2078605887580003e-12, 7.823433340507048e-14, 4.677522183477514e-15, 2.5968666068472456e-16, 1.3456130935606599e-17, 6.536752526057353e-19, 2.988649213735889e-20], [0.00010892766596945404, 8.466424104708808e-05, 3.290272332691645e-05, 8.524568648571112e-06, 1.6564344064056788e-06, 2.574933752862154e-07, 3.335620477931634e-08, 3.703739327139491e-09, 3.598423279082878e-10, 4.3648027575635096e-11, 4.003301306916704e-12, 2.8287034153803133e-13, 1.8321793770130508e-14, 1.0954346138179173e-15, 6.08163351668695e-17, 3.1513076831569035e-18, 1.5308500308771125e-19, 6.999153972695925e-21], [2.295891241609509e-05, 1.784485950080255e-05, 6.934975943811365e-06, 1.796741197432959e-06, 3.491301509236319e-07, 5.427241829067307e-08, 7.030557179811522e-09, 7.806448992277875e-10, 7.584472150873865e-11, 6.550050874806964e-12, 7.150551814749989e-13, 5.962117464541793e-14, 3.861722866550203e-15, 2.308870490556291e-16, 1.281838640475038e-17, 6.642077239959933e-19, 3.2266046892935417e-20, 1.4752263496672365e-21], [4.399180073380413e-06, 3.4192713010730515e-06, 1.3288176473028416e-06, 3.442753702578521e-07, 6.689717592558179e-08, 1.0399192119881065e-08, 1.347132063124481e-09, 1.4958014660404545e-10, 1.4532682623869632e-11, 1.2550617714747846e-12, 9.75499212283899e-14, 9.68119845174549e-15, 7.399485644422597e-16, 4.4240497415508e-17, 2.456143785153186e-18, 1.272695034953013e-19, 6.182529379686604e-21, 2.826695900731012e-22], [7.726870021837483e-07, 6.005724810552888e-07, 2.333980667343568e-07, 6.046970101995104e-08, 1.1750048294971614e-08, 1.826549595654371e-09, 2.366148732350952e-10, 2.6272767456157497e-11, 2.5525699750901395e-12, 2.2044333298024931e-13, 1.7134001095641762e-14, 1.2106759822108069e-15, 1.1013911071246541e-16, 7.770551955796407e-18, 4.314054770719879e-19, 2.235404995586656e-20, 1.0859205607903503e-21, 4.964905153206409e-23], [1.2527758356044153e-07, 9.737224641655565e-08, 3.784138431929466e-08, 9.804096614789882e-09, 1.9050633088849056e-09, 2.961428352621174e-10, 3.83629328170112e-11, 4.259666347500062e-12, 4.1385424815543103e-13, 3.5741002488363425e-14, 2.777976396545504e-15, 1.9628977981690703e-16, 1.2713884550198314e-17, 1.067652191745788e-18, 6.994479724594341e-20, 3.624315348059129e-21, 1.760628862785806e-22, 8.049718947550905e-24], [1.886072772019166e-08, 1.4659537444542262e-08, 5.697077050157236e-09, 1.4760214201033963e-09, 2.868101326465189e-10, 4.458474711455143e-11, 5.77559695714092e-12, 6.412991444738467e-13, 6.230637651578205e-14, 5.380861421664377e-15, 4.1822850456790274e-16, 2.9551720157476585e-17, 1.9140943491422877e-18, 1.1444104384484644e-19, 8.923775984856293e-21, 5.456461005162606e-22, 2.650653105971893e-23, 1.2118972363525553e-24], [2.6502100696996935e-09, 2.0598809509917896e-09, 8.005232454534529e-10, 2.0740275182821585e-10, 4.030104844883392e-11, 6.2648137182692875e-12, 8.115564490099235e-13, 9.011197635576259e-14, 8.754963694844543e-15, 7.560902916851304e-16, 5.876726554165199e-17, 4.152451989137564e-18, 2.689584513232463e-19, 1.6080652416176977e-20, 8.92765606187706e-22, 6.497422027692817e-23, 3.7245580642187934e-24, 1.7028941337106233e-25], [3.4911895621833605e-10, 2.713533903468174e-10, 1.0545497622114653e-10, 2.7321695386691435e-11, 5.308960270668583e-12, 8.252799471372937e-13, 1.0690840836730692e-13, 1.1870681304769194e-14, 1.1533137775828847e-15, 9.960170948631291e-17, 7.741562316240152e-18, 5.470131295511723e-19, 3.543058524515829e-20, 2.118345504393062e-21, 1.1760629851323447e-22, 6.09398167573729e-24, 4.157919205835641e-25, 2.2432660312801052e-26], [4.3285019992144797e-11, 3.36433662993444e-11, 1.3074686071038795e-11, 3.387441758655547e-12, 6.582239301542769e-13, 1.023211669681252e-13, 1.3254887799943009e-14, 1.4717696316552163e-15, 1.4299197746418246e-16, 1.2348977073793226e-17, 9.598266540970207e-19, 6.782064917088171e-20, 4.3928109985266974e-21, 2.6264007116983923e-22, 1.4581250578567526e-23, 7.555536987257948e-25, 3.670347421820158e-26, 2.3569650265487084e-27]] |
| Legacy trial inputs | {"lambda_home": 2.107720955164261, "lambda_away": 0.7772519524179469, "rho": 0.05, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T12:02:58Z", "over": 1.86, "under": 1.97, "bookmaker": "pinnacle", "event_id": "ce5c2cbdf5db2a13f40f528d3e5044b9", "kickoff_utc": "2026-11-01T18:00:00Z", "home_team": "Acad\u00e9mico de Viseu", "away_team": "Rio Ave FC"}} |
| Legacy p home | 0.5913 |
| Legacy p draw | 0.2219 |
| Legacy p away | 0.1868 |
| Legacy p over 1 5 | 0.7639 |
| Legacy p under 3 5 | 0.6877 |
| Legacy p btts yes | 0.4855 |
| Legacy p over 2 5 | 0.5276 |
| Legacy goal margin distribution | {"-1": 0.1352977616452318, "-10": 2.0518585737469934e-09, "-11": 1.4322361184531874e-10, "-12": 9.181173673049056e-12, "-13": 5.440699191736759e-13, "-14": 2.997331306754346e-14, "-15": 1.5424463946716153e-15, "-16": 7.418795685144962e-17, "-17": 3.0937880691827895e-18, "-2": 0.04027868385271909, "-3": 0.009262366171734098, "-4": 0.001669854418596207, "-5": 0.0002466049954724376, "-6": 3.07785665775637e-05, "-7": 3.3224581861421657e-06, "-8": 3.1574087661433076e-07, "-9": 2.6787274165968603e-08, "0": 0.22187204809571595, "1": 0.21461805732506017, "10": 2.662167906384383e-05, "11": 5.039111099758383e-06, "12": 8.759691396837271e-07, "13": 1.4076562416975408e-07, "14": 2.1029451089163255e-08, "15": 2.9346381461175496e-09, "16": 3.8276232251768045e-10, "17": 4.3285019992144797e-11, "2": 0.17871168830921758, "3": 0.1114425200827937, "4": 0.05448273240357179, "5": 0.02181892912301346, "6": 0.007384672561699099, "7": 0.0021616912719200202, "8": 0.0005570783071468704, "9": 0.0001281637632902055} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6860 |
| Legacy raw p draw | 0.1833 |
| Legacy raw p away | 0.1307 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1077 |
| Legacy lambda away | 0.7773 |
| Legacy model home team | Academico Viseu |
| Legacy model away team | Rio Ave |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,418.3104 |
| Elo away rating | 1,393.4483 |
| Elo rating diff | 84.8621 |
| Elo home expectancy | 0.6198 |

</details>


---

## 2026-11-01 — Arouca vs Nacional

The model's most likely 1X2 outcome is **Arouca win** at **52.7%**. Expected goals are 1.58 for Arouca and 1.14 for Nacional (2.71 combined). The most likely exact score is 1-0 at 11.7%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 51.9%; Under 3.5 goals: 69.9%; Double Chance 1X: 77.0%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.4%; BTTS Yes (both teams score): 54.2%; BTTS No (at least one team does not score): 45.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arouca win | 52.7% | 1.90 |
| Draw | 24.4% | 4.10 |
| Nacional win | 23.0% | 4.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arouca expected goals | 1.58 |
| Nacional expected goals | 1.14 |
| Expected total goals | 2.71 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.6% |
| Under 4.5 | 85.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.74% |
| 2 | 1-1 | 11.52% |
| 3 | 2-1 | 10.26% |
| 4 | 2-0 | 8.89% |
| 5 | 0-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arouca win | 52.7% | 54.6% | 1.78 | -6.3% |
| Draw | 24.4% | 24.6% | 3.81 | -7.2% |
| Nacional win | 23.0% | 20.8% | 4.47 | +2.7% |
| Over 2.5 | 51.9% | 51.9% | 1.85 | -3.9% |
| Under 2.5 | 48.1% | 48.1% | 1.99 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T15:30:00+00:00 |
| Fixture id | fd5c6a92f2448c1cfe7a2d9b8075172b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Arouca |
| Matched away-team name | Nacional |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5600 |
| Dc lambda away | 1.0677 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6115 |
| Shot lambda away | 1.2948 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.2% |
| P btts no | 45.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.79 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.33 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.86 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.14035402066007824, "-10": 7.103870245250644e-08, "-11": 7.35140288169929e-09, "-12": 6.988068837012107e-10, "-13": 6.140191073150384e-11, "-14": 4.9864742271576504e-12, "-15": 3.415826599811449e-13, "-2": 0.06160085170928234, "-3": 0.02075805747596771, "-4": 0.005508644786712491, "-5": 0.0012005706837646978, "-6": 0.0002214866119882392, "-7": 3.537762530691825e-05, "-8": 4.9783529517709005e-06, "-9": 6.257426760343754e-07, "0": 0.24366277210768533, "1": 0.2568981069538742, "10": 2.494463729693236e-06, "11": 3.5804569164987263e-07, "12": 4.720754950626628e-08, "13": 5.753368928151787e-09, "14": 6.480670950361882e-10, "15": 6.15755448518261e-11, "2": 0.15789938981717055, "3": 0.07380172276962067, "4": 0.02716505653265407, "5": 0.008211824014541333, "6": 0.0021012872917206874, "7": 0.00046553537404258244, "8": 9.086481512791458e-05, "9": 1.5841339209328743e-05} |
| Raw goal margin distribution | {"-1": 0.17238618356598454, "-10": 7.69258852927636e-08, "-11": 7.838117221097393e-09, "-12": 7.335601869160983e-10, "-13": 6.345788033443907e-11, "-14": 5.0751928093445026e-12, "-15": 3.4334537047889553e-13, "-2": 0.07488910838272035, "-3": 0.024926796053050027, "-4": 0.006525921209884979, "-5": 0.0014021550191444373, "-6": 0.00025490397898769176, "-7": 4.011002839181187e-05, "-8": 5.559275111265108e-06, "-9": 6.881354600159351e-07, "0": 0.23851834720414217, "1": 0.23680378701539603, "10": 2.0273701644056085e-06, "11": 2.865222526574693e-07, "12": 3.7193616609899223e-08, "13": 4.462767624157308e-09, "14": 4.950594022862929e-10, "15": 4.645388258508038e-11, "2": 0.1440757103742706, "3": 0.06651577028216189, "4": 0.02415383222157863, "5": 0.0071982397070620855, "6": 0.0018150681813069835, "7": 0.00039614607104945825, "8": 7.61564348208719e-05, "9": 1.3075202722557019e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 53.2% |
| P home draw | 77.0% |
| P draw away | 47.3% |
| P home away | 75.6% |
| Raw p home draw | 72.0% |
| Raw p draw away | 51.9% |
| Raw p home away | 76.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0161 |
| Totals anchor target over 2 5 | 0.5194 |
| Totals anchor reference over odds | 1.85 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-30T12:02:58Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5096 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 3.81 |
| Reference away odds | 4.47 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best over 2 5 last update utc | 2026-10-30T12:02:58Z |
| Market best under 2 5 last update utc | 2026-10-30T12:02:58Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0651 |
| Raw ev home | -0.1437 |
| Raw edge prob draw | -0.0073 |
| Raw ev draw | -0.0912 |
| Raw edge prob away | 0.0725 |
| Raw ev away | 0.2535 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.06955738267287825, 0.07615796222016477, 0.03748501369612043, 0.013238262123307325, 0.0035064329734431614, 0.0007430021906336297, 0.0001311998688000686, 1.9857744459071642e-05, 2.629871251261388e-06, 3.095897225931631e-07, 3.2800547426192854e-08, 3.159242503994869e-09, 2.789306729218729e-10, 2.2732514625535168e-11, 1.7203388634247934e-12, 1.2151147655729458e-13], [0.12856113663145435, 0.11618584485129499, 0.05718143738278696, 0.02019427984733972, 0.005348880999038583, 0.0011334111702188756, 0.00020013857119645224, 3.0291955621382355e-05, 4.011731714916206e-06, 4.72263008367195e-07, 5.003552790394463e-08, 4.819260008378184e-09, 4.2549422382821325e-10, 3.4677267885001755e-11, 2.6242873963863807e-12, 1.853594330891238e-13], [0.09312351580205652, 0.09866291009192027, 0.04941531576733921, 0.015402661420137671, 0.004079719783404517, 0.0008644798743334799, 0.00015265048679887264, 2.3104400836133438e-05, 3.0598439647464136e-06, 3.602063195184352e-07, 3.8163296790394584e-08, 3.6757651555689204e-09, 3.245346462163441e-10, 2.6449183642389595e-11, 2.001606917465734e-12, 1.4137808381795515e-13], [0.04735169216217003, 0.05016837805422822, 0.026576306375411116, 0.008873828204519565, 0.002074466729781905, 0.0004395730180209367, 7.76201241657372e-05, 1.1748186981142888e-05, 1.5558775700750157e-06, 1.8315866416556122e-07, 1.9405374313330945e-08, 1.8690628098374136e-09, 1.6502023716823325e-10, 1.3448951008650352e-11, 1.0177823911521004e-12, 7.188830281768039e-14], [0.018058135461081346, 0.019132312392623817, 0.01013519303468077, 0.003579359558225506, 0.0008963610674455567, 0.00016763644005102964, 2.9601364865491637e-05, 4.480311943256817e-06, 5.933525633054193e-07, 6.98497522970219e-08, 7.400472127225861e-09, 7.127895089729897e-10, 6.29324457169972e-11, 5.128918694011986e-12, 3.881435161046128e-13, 2.741546608097851e-14], [0.005509349152109703, 0.005837069352224702, 0.003092141892081199, 0.0010920253416918716, 0.000289245947109807, 5.7947529816575756e-05, 9.031068283570215e-06, 1.3668965358559133e-06, 1.810256905312349e-07, 2.1310432321323747e-08, 2.257807010431066e-09, 2.174646593695381e-10, 1.920003408980777e-11, 1.5647797038068332e-12, 1.1841854636413144e-13, 8.364173318638219e-15], [0.0014007042303854356, 0.0014840242484147994, 0.0007861502528899657, 0.0002776379702147161, 7.353827295251468e-05, 1.558253025594813e-05, 2.601503281339126e-06, 3.475215869263628e-07, 4.6024211487567094e-08, 5.417992557685391e-09, 5.740278467727279e-10, 5.5288503220311884e-11, 4.881442114235931e-12, 3.978316658155879e-13, 3.010688817658546e-14, 2.1265185101959313e-15], [0.0003052430571355014, 0.00032340025011896916, 0.000171318756204476, 6.050318187581623e-05, 1.602554398390995e-05, 3.39576269568573e-06, 5.996262538205896e-07, 8.580651214271007e-08, 1.0029648452514532e-08, 1.1806950932033675e-09, 1.2509280048479716e-10, 1.2048533431479734e-11, 1.0637694110264422e-12, 8.669592856547846e-14, 6.560927273939061e-15, 4.634133295426844e-16], [5.820404955571152e-05, 6.166628116261499e-05, 3.266723072925366e-05, 1.1536806862129486e-05, 3.0557666567422323e-06, 6.475074063073304e-07, 1.1433733012569842e-07, 1.7305516419597564e-08, 2.166866854004638e-09, 2.2513611401974648e-10, 2.3852819542584308e-11, 2.2974263313323747e-12, 2.0284060871447737e-13, 1.653126583732099e-14, 1.2510441343609337e-15, 8.836411432449455e-17], [9.86524980082018e-06, 1.0452078035816183e-05, 5.536906691288672e-06, 1.9554220448146702e-06, 5.179347765643753e-07, 1.0974876077975835e-07, 1.9379516233989794e-08, 2.9331849538770165e-09, 3.8845795406082364e-10, 4.323536787896449e-11, 4.042914969623251e-12, 3.894004769527532e-13, 3.438031013294639e-14, 2.801953957736829e-15, 2.1204474588160955e-16, 1.4977206360958937e-17], [1.504892510708973e-06, 1.5944101036486494e-06, 8.446262974022184e-07, 2.98289455404583e-07, 7.900825443088652e-08, 1.6741602239338924e-08, 2.9562443354723306e-09, 4.474420981460381e-10, 5.925723905570663e-11, 6.975790998169126e-12, 6.987649453687023e-13, 5.940101601725085e-14, 5.244537369000159e-15, 4.274234927126685e-16, 3.2346322339034104e-17, 2.2846948773741164e-18], [2.086941089833122e-07, 2.2110814796877795e-07, 1.1713031416256289e-07, 4.1365912629500414e-08, 1.0956634539308545e-08, 2.3216766230339298e-09, 4.099633516268276e-10, 6.204996657882191e-11, 8.217621270316346e-12, 9.673823721342518e-13, 1.0249265095324321e-13, 9.333352976527722e-15, 7.272971627306053e-16, 5.927384470016537e-17, 4.48569374317073e-18, 3.168348292913636e-19], [2.6529333432925358e-08, 2.810741429538559e-08, 1.4889683157134092e-08, 5.2584622261332105e-09, 1.3928146434610952e-09, 2.95133070866032e-10, 5.2114812936370005e-11, 7.887832871233905e-12, 1.0446294615970906e-12, 1.2297428821786247e-13, 1.3028933709769681e-14, 1.254904700912595e-15, 1.0475316407442395e-16, 7.53493041831796e-18, 5.702243612448069e-19, 4.0276253461982935e-20], [3.1130090276766935e-09, 3.298184429224685e-09, 1.7471874370532528e-09, 6.170392642181249e-10, 1.6343586505620606e-10, 3.463154912258921e-11, 6.1152642058188565e-12, 9.255752693160854e-13, 1.225790671578965e-13, 1.44300673954818e-14, 1.5288430959662371e-15, 1.4725321586732608e-16, 1.300104013536334e-17, 1.0017800906358597e-18, 6.691135262950781e-20, 4.726102182142991e-21], [3.3919523190023164e-10, 3.5937204883582735e-10, 1.9037453557490898e-10, 6.723294871850015e-11, 1.7808064691006813e-11, 3.773473263734107e-12, 6.663226614450216e-13, 1.0085120708792072e-13, 1.3356284784618023e-14, 1.5723083399470177e-15, 1.6658361214659268e-16, 1.6044794043353456e-17, 1.4166007179715715e-18, 1.1545125605046757e-19, 8.260536910338139e-21, 5.1495877827652485e-22], [3.449497812766411e-11, 3.654689039948512e-11, 1.9360429696878098e-11, 6.837357596421571e-12, 1.8110183877613872e-12, 3.837491375353983e-13, 6.776270262924429e-14, 1.0256217822276449e-14, 1.3582878182903402e-15, 1.5989830249845322e-16, 1.6940975335154977e-17, 1.6316998811797707e-18, 1.4406337762564893e-19, 1.1740992141786965e-20, 8.885284100507076e-22, 5.933592391845629e-23]] |
| Legacy trial inputs | {"lambda_home": 1.5254479522493822, "lambda_away": 1.0594843766599007, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T12:02:58Z", "over": 1.85, "under": 1.99, "bookmaker": "pinnacle", "event_id": "fd5c6a92f2448c1cfe7a2d9b8075172b", "kickoff_utc": "2026-11-01T15:30:00Z", "home_team": "Arouca", "away_team": "Nacional"}} |
| Legacy p home | 0.5163 |
| Legacy p draw | 0.2450 |
| Legacy p away | 0.2387 |
| Legacy p over 1 5 | 0.7257 |
| Legacy p under 3 5 | 0.7375 |
| Legacy p btts yes | 0.5048 |
| Legacy p over 2 5 | 0.4789 |
| Legacy goal margin distribution | {"-1": 0.1509935530416804, "-10": 3.795818753948546e-08, "-11": 3.6122311093227047e-09, "-12": 3.1568143602715806e-10, "-13": 2.5498180105739505e-11, "-14": 1.9056982965139173e-12, "-15": 1.2151147655729458e-13, "-2": 0.062229601835441066, "-3": 0.019533910003896506, "-4": 0.004804858066719733, "-5": 0.0009678732041646162, "-6": 0.00016474244995655357, "-7": 2.4249820261843635e-05, "-8": 3.142231147024537e-06, "-9": 3.6347128535360376e-07, "0": 0.24498936961389808, "1": 0.25768515846168477, "10": 1.7415255729129319e-06, "11": 2.386177546828573e-07, "12": 3.002472975532137e-08, "13": 3.491741506209399e-09, "14": 3.7574212229971676e-10, "15": 3.449497812766411e-11, "2": 0.15459616359905845, "3": 0.06987047730378045, "4": 0.024745026782842877, "5": 0.0071767640579452644, "6": 0.0017588085162634313, "7": 0.00037275579242989357, "8": 6.954354792433089e-05, "9": 1.1582215957958547e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4864 |
| Legacy raw p draw | 0.2441 |
| Legacy raw p away | 0.2695 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5254 |
| Legacy lambda away | 1.0595 |
| Legacy model home team | Arouca |
| Legacy model away team | Nacional |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,468.8191 |
| Elo away rating | 1,372.3854 |
| Elo rating diff | 156.4337 |
| Elo home expectancy | 0.7111 |

</details>


---

## 2026-11-01 — Braga vs Famalicão

The model's most likely 1X2 outcome is **Braga win** at **53.6%**. Expected goals are 1.54 for Braga and 0.97 for Famalicão (2.51 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.3%; Double Chance 1X: 79.9%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Braga win | 53.6% | 1.87 |
| Draw | 26.3% | 3.80 |
| Famalicão win | 20.1% | 4.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Braga expected goals | 1.54 |
| Famalicão expected goals | 0.97 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 71.2% |
| Under 1.5 | 28.8% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.7% |
| Under 3.5 | 75.3% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.70% |
| 2 | 1-1 | 12.44% |
| 3 | 2-0 | 10.08% |
| 4 | 2-1 | 9.79% |
| 5 | 0-0 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Braga win | 53.6% | 54.6% | 1.78 | -4.6% |
| Draw | 26.3% | 27.2% | 3.46 | -8.9% |
| Famalicão win | 20.1% | 18.2% | 5.06 | +1.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T20:30:00+00:00 |
| Fixture id | 12fa9f636dbb126cfd4118fa8cdc8fad |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sp Braga |
| Matched away-team name | Famalicao |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5361 |
| Dc lambda away | 0.9608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5565 |
| Shot lambda away | 0.9962 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.36 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.48 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.04 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 9.10 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.1318890460176389, "-10": 1.573007579455994e-08, "-11": 1.3737297864903027e-09, "-12": 1.1015886318915204e-10, "-13": 8.163843674878168e-12, "-14": 5.601261350578342e-13, "-15": 3.298128634486062e-14, "-2": 0.050372691389703204, "-3": 0.014609133583291857, "-4": 0.0033113608271822313, "-5": 0.000613740871369103, "-6": 9.603127990915578e-05, "-7": 1.2986561561317521e-05, "-8": 1.545331798584533e-06, "-9": 1.6410522057541407e-07, "0": 0.2633825423518432, "1": 0.2626820384329579, "10": 2.035687969320393e-06, "11": 2.8224025862459283e-07, "12": 3.593141689908828e-08, "13": 4.227531276956935e-09, "14": 4.604847348413121e-10, "15": 4.304614283881317e-11, "2": 0.16153905511599886, "3": 0.07437793118742629, "4": 0.026764762409360942, "5": 0.007875518984946452, "6": 0.0019563389690567816, "7": 0.00042001308332280526, "8": 7.934647411781228e-05, "9": 1.3377209865312258e-05} |
| Raw goal margin distribution | {"-1": 0.16033811428081676, "-10": 1.9123124827642998e-08, "-11": 1.6700495617186145e-09, "-12": 1.3392063198868615e-10, "-13": 9.924821959348124e-12, "-14": 6.809478949644081e-13, "-15": 4.0095500109867804e-14, "-2": 0.06123831047799349, "-3": 0.017760390273111024, "-4": 0.0040256364479484994, "-5": 0.0007461275742280096, "-6": 0.0001167456646137849, "-7": 1.578782207170495e-05, "-8": 1.8786669098363877e-06, "-9": 1.9950346450440124e-07, "0": 0.24389758227865013, "1": 0.25098660431354297, "10": 1.9450527105303316e-06, "11": 2.696740307611182e-07, "12": 3.43316367174381e-08, "13": 4.039308230446525e-09, "14": 4.399824998523472e-10, "15": 4.1129592584103794e-11, "2": 0.1543468261075283, "3": 0.07106639074358688, "4": 0.025573110641513234, "5": 0.007524876002296728, "6": 0.0018692365784086019, "7": 0.0004013127741025846, "8": 7.58137184479206e-05, "9": 1.2781614225752471e-05} |
| Unadjusted home-win probability | 51.2% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 24.4% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 48.2% |
| P home draw | 79.9% |
| P draw away | 46.4% |
| P home away | 73.7% |
| Raw p home draw | 75.6% |
| Raw p draw away | 48.8% |
| Raw p home away | 75.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4557 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.04, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.82, "price": 2.04, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.78 |
| Reference draw odds | 3.46 |
| Reference away odds | 5.06 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.20 |
| Reference Under 2.5 odds | 1.68 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:37Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:37Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +2.8% |
| Under 2.5 probability edge | -2.8% |
| Raw edge prob home | -0.0341 |
| Raw ev home | -0.0889 |
| Raw edge prob draw | -0.0278 |
| Raw ev draw | -0.1561 |
| Raw edge prob away | 0.0619 |
| Raw ev away | 0.2359 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.07665548283667847, 0.07105459119233894, 0.030843785083590133, 0.009650382648268197, 0.00226455390459383, 0.0004251192578550398, 6.650551315816975e-05, 8.917800019722611e-06, 1.0463232180059629e-06, 1.0912430062393186e-07, 1.0242821246402801e-08, 8.74027362174007e-10, 6.836627271245001e-11, 4.936244593569014e-12, 3.309533303591813e-13, 2.0709690902262396e-14], [0.13181872696441604, 0.120112306096077, 0.050069673609476575, 0.015665765667081437, 0.0036761206371653614, 0.0006901092854919858, 0.0001079604636083373, 1.4476541549359096e-05, 1.6985289540046885e-06, 1.7714486403971195e-07, 1.662748963065675e-08, 1.4188357437715125e-09, 1.1098109234427334e-10, 8.013159052519748e-12, 5.372468128066951e-13, 3.361868399806426e-14], [0.10219644226069505, 0.09592546152502496, 0.04816251097692556, 0.012715361808992543, 0.0029837803621232204, 0.0005601379108596564, 8.762778564543209e-05, 1.175010959916317e-05, 1.3786373837189478e-06, 1.4378237787654638e-07, 1.3495959988303667e-08, 1.1516200492833555e-09, 9.007952583383373e-11, 6.504004895202471e-12, 4.360647127462043e-13, 2.7287126570252995e-14], [0.05529955218072003, 0.051906259628207635, 0.024360593190574167, 0.008154020967897488, 0.0016145544226494146, 0.0003030964184738186, 4.7416301366140764e-05, 6.358105864884965e-06, 7.459949510255955e-07, 7.780213216982103e-08, 7.3028035721469e-09, 6.231535227542974e-10, 4.8742963346566965e-11, 3.5193843359871715e-12, 2.359591273751589e-13, 1.4765346486175757e-14], [0.02244236983994529, 0.021065260560836775, 0.009886326748481816, 0.0030932272368678283, 0.0007765278810303496, 0.0001230064557905014, 1.9243088410980663e-05, 2.5803276459627867e-06, 3.027491892689373e-07, 3.157465396438033e-08, 2.9637169230411e-09, 2.528961134985924e-10, 1.978149130292487e-11, 1.4282814554992293e-12, 9.575994370367294e-14, 5.992261303939159e-15], [0.007286279098780625, 0.006839178252093495, 0.0032097562095676816, 0.0010042663553139245, 0.00023566063430515685, 4.732844734279596e-05, 6.2475805311502635e-06, 8.377451904085677e-07, 9.82924310433882e-08, 1.0251223149455773e-08, 9.622187329174428e-10, 8.210682201074264e-11, 6.422381756077662e-12, 4.637147231152382e-13, 3.1090017733625515e-14, 1.9454847507062677e-15], [0.001971340500281171, 0.001850375053468704, 0.0008684161457675532, 0.0002717094572497801, 6.375920362499599e-05, 1.1969361944311169e-05, 2.003203031690361e-06, 2.2665629471214604e-07, 2.6593525661040477e-08, 2.7735214501080577e-09, 2.603332555085394e-10, 2.2214425413136066e-11, 1.73760860548721e-12, 1.2546041701953494e-13, 8.411565118746642e-15, 5.26360962811391e-16], [0.0004571626025179116, 0.0004291101790671469, 0.00020138955457519575, 6.301062783792143e-05, 1.4786042015326736e-05, 2.775748104480015e-06, 4.3423709623902164e-07, 6.229226193430296e-08, 6.1671565108078e-09, 6.431919214817555e-10, 6.03724362144791e-11, 5.1516237473236256e-12, 4.029591397978946e-13, 2.909482697152139e-14, 1.9506792461204066e-15, 1.220654410480421e-16], [9.276578017458079e-05, 8.707348396998052e-05, 4.086523929622478e-05, 1.2785888474869123e-05, 3.0003301138180362e-06, 5.632447559402318e-07, 8.811381944081724e-08, 1.1815282424456062e-08, 1.4830621099354484e-09, 1.3051417607131378e-10, 1.2250556182046496e-11, 1.0453488396782185e-12, 8.176700975965128e-14, 5.903816953076055e-15, 3.9582477031163705e-16, 2.4769077367242154e-17], [1.6732174453664624e-05, 1.570545433167504e-05, 7.370867918195396e-06, 2.3061921767271647e-06, 5.411698881689882e-07, 1.0159252149626308e-07, 1.589309976036238e-08, 2.1311238516321758e-09, 2.500442218347031e-10, 2.7898415168459873e-11, 2.2096342294180243e-12, 1.8854969060266288e-13, 1.4748324967226157e-14, 1.064872143752417e-15, 7.139495940714187e-17, 4.4676013373148426e-18], [2.716185809884701e-06, 2.5495151459017294e-06, 1.1965358657584321e-06, 3.743713336625835e-07, 8.784978754865658e-08, 1.6491829322166783e-08, 2.579976210726371e-09, 3.459519490990223e-10, 4.0590454580297194e-11, 4.233304672836917e-12, 4.2509377496398853e-13, 3.060785646786855e-14, 2.3941413655757285e-15, 1.72864000086273e-16, 1.158976534556158e-17, 7.252395909593662e-19], [4.008426114636214e-07, 3.7624609676194634e-07, 1.76579437016076e-07, 5.5248055010197834e-08, 1.296448060709905e-08, 2.4337907624921548e-09, 3.807414051196578e-10, 5.105404873743464e-11, 5.990158609639632e-12, 6.247322602179164e-13, 5.863974230933086e-14, 5.3530905194653656e-15, 3.5331672586537537e-16, 2.5510499675856373e-17, 1.7103659810234731e-18, 1.0702763062785497e-19], [5.4225020995212174e-08, 5.089766385312245e-08, 2.388724004306227e-08, 7.473823533715058e-09, 1.7538036451390795e-09, 3.292373400926906e-10, 5.1505778317766845e-11, 6.906468487892353e-12, 8.103341987178897e-13, 8.451227229312998e-14, 7.932642805281886e-15, 6.768981611003e-16, 5.664313832143001e-17, 3.450998823380352e-18, 2.3137418173145387e-19, 1.4478439546814386e-20], [6.771166118204141e-09, 6.355673647566431e-09, 2.982838318334147e-09, 9.332684387415263e-10, 2.19000299160736e-10, 4.1112399426827687e-11, 6.4316098848129505e-12, 8.624218960798634e-13, 1.0118774267077087e-13, 1.0553184198383458e-14, 9.905619436400623e-16, 8.452536872824325e-17, 6.611560072011813e-18, 5.106999498608683e-19, 2.8892068480813654e-20, 1.8079461751155917e-21], [7.851317223579039e-10, 7.36954449285028e-10, 3.458667156448334e-10, 1.08214544428537e-10, 2.5393570187961677e-11, 4.767073855339458e-12, 7.4575942433629e-13, 9.999973074769841e-14, 1.1732943085094684e-14, 1.2236651030848655e-15, 1.1485785333510376e-16, 9.800903887755092e-18, 7.666250474723447e-19, 5.535256780483821e-20, 3.97022350496893e-21, 2.0963536702823715e-22], [8.496857950987204e-11, 7.975473533431417e-11, 3.7430411600016646e-11, 1.1711201904805015e-11, 2.74814470758547e-12, 5.159025961788861e-13, 8.070762795273846e-14, 1.082217777099103e-14, 1.269763377305264e-15, 1.3242756934170315e-16, 1.2430154540346267e-17, 1.0606740977862476e-18, 8.296574886158985e-20, 5.9903694178554695e-21, 4.0162772961127576e-22, 2.6886709226822554e-23]] |
| Legacy trial inputs | {"lambda_home": 1.6233310365048297, "lambda_away": 0.9386379741119233, "rho": 0.05, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5431 |
| Legacy p draw | 0.2539 |
| Legacy p away | 0.2030 |
| Legacy p over 1 5 | 0.7205 |
| Legacy p under 3 5 | 0.7436 |
| Legacy p btts yes | 0.4874 |
| Legacy p over 2 5 | 0.4673 |
| Legacy goal margin distribution | {"-1": 0.13558366802598512, "-10": 1.1755353605772588e-08, "-11": 9.91754410802162e-10, "-12": 7.683026182420214e-11, "-13": 5.5007785329459615e-12, "-14": 3.6457201435724553e-13, "-15": 2.0709690902262396e-14, "-2": 0.04981653561402911, "-3": 0.013936738952690523, "-4": 0.003048962347576274, "-5": 0.0005456083855096237, "-6": 8.24415418142664e-05, "-7": 1.0767673601107112e-05, "-8": 1.2376074492963894e-06, "-9": 1.2695361316505275e-07, "0": 0.2539102442126363, "1": 0.2554460852198479, "10": 3.117278324601235e-06, "11": 4.548340763242141e-07, "12": 6.093827256032825e-08, "13": 7.545550979089186e-09, "14": 8.648864576922181e-10, "15": 8.496857950987204e-11, "2": 0.1650599202305944, "3": 0.07986164394027291, "4": 0.030216079420130836, "5": 0.009351387644767182, "6": 0.002443712446779646, "7": 0.0005519946259905766, "8": 0.00010972481409965063, "9": 1.9465966708196786e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5402 |
| Legacy raw p draw | 0.2361 |
| Legacy raw p away | 0.2237 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.6233 |
| Legacy lambda away | 0.9386 |
| Legacy model home team | Sp Braga |
| Legacy model away team | Famalicao |
| Legacy home name match score | 90/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,518.8201 |
| Elo away rating | 1,511.6518 |
| Elo rating diff | 67.1683 |
| Elo home expectancy | 0.5955 |

</details>


---

## 2026-11-01 — CS Maritimo vs Santa Clara

The model's most likely 1X2 outcome is **Santa Clara win** at **42.8%**. Expected goals are 1.03 for CS Maritimo and 1.32 for Santa Clara (2.35 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 40.9%; Under 3.5 goals: 78.9%; Double Chance 1X: 57.2%; Double Chance X2: 72.2%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.4%; BTTS No (at least one team does not score): 52.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| CS Maritimo win | 27.8% | 3.59 |
| Draw | 29.4% | 3.40 |
| Santa Clara win | 42.8% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| CS Maritimo expected goals | 1.03 |
| Santa Clara expected goals | 1.32 |
| Expected total goals | 2.35 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 67.5% |
| Under 1.5 | 32.5% |
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 21.1% |
| Under 3.5 | 78.9% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.76% |
| 2 | 0-1 | 12.85% |
| 3 | 0-0 | 9.89% |
| 4 | 1-0 | 9.77% |
| 5 | 1-2 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| CS Maritimo win | 27.8% | 27.0% | 3.50 | -2.6% |
| Draw | 29.4% | 30.8% | 3.09 | -9.1% |
| Santa Clara win | 42.8% | 42.3% | 2.28 | -2.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T18:00:00+00:00 |
| Fixture id | 6bf5102547eb3f3eb74023133e27d2d3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T12:02:58Z |
| Market best draw last update utc | 2026-10-30T12:02:58Z |
| Market best away last update utc | 2026-10-30T12:02:58Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Maritimo |
| Matched away-team name | Santa Clara |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9841 |
| Dc lambda away | 1.3334 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.1414 |
| Shot lambda away | 1.2988 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.4% |
| P btts no | 52.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.11 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.08 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.73 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.40 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.23319114332470486, "-10": 4.7328195463916196e-07, "-11": 5.6346269686415274e-08, "-12": 6.157961552616608e-09, "-13": 6.195822342073351e-10, "-14": 5.3352079697224587e-11, "-2": 0.12450717426420846, "-3": 0.04961360951160458, "-4": 0.01540353718585769, "-5": 0.003903765196254443, "-6": 0.0008343249004308559, "-7": 0.00015400667870573177, "-8": 2.5002492107047446e-05, "-9": 3.6211986179482344e-06, "0": 0.2941761702010731, "1": 0.17610400036069915, "10": 3.7675460152163076e-08, "11": 3.496251402915249e-09, "12": 2.978333468502134e-10, "13": 2.3357920172838958e-11, "14": 1.5677811243692197e-12, "2": 0.07273477143928943, "3": 0.02259162083985283, "4": 0.005467211720144773, "5": 0.0010800105146031558, "6": 0.00017991955398508188, "7": 2.5886991448488306e-05, "8": 3.275851368591199e-06, "9": 3.6982145302495146e-07} |
| Raw goal margin distribution | {"-1": 0.23968684392125592, "-10": 4.864655508566464e-07, "-11": 5.791583400346925e-08, "-12": 6.329495831151243e-09, "-13": 6.368411259086764e-10, "-14": 5.483823878103652e-11, "-2": 0.1279754077254457, "-3": 0.05099563092248137, "-4": 0.015832613368857697, "-5": 0.004012507276046025, "-6": 0.0008575655976382097, "-7": 0.00015829664126811217, "-8": 2.5698953819012498e-05, "-9": 3.7220696102486715e-06, "0": 0.2630660838274792, "1": 0.18825711299499037, "10": 4.0275481218352176e-08, "11": 3.737531197868221e-09, "12": 3.183871230455573e-10, "13": 2.4969873530978832e-11, "14": 1.6759752627837322e-12, "2": 0.07775427053028443, "3": 0.02415069111705026, "4": 0.005844509451566805, "5": 0.0011545431169478334, "6": 0.00019233598177896243, "7": 2.767347853675448e-05, "8": 3.5019211374445053e-06, "9": 3.95343200196985e-07} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 78.8% |
| Raw p btts yes | 46.6% |
| P home draw | 57.2% |
| P draw away | 72.2% |
| P home away | 70.6% |
| Raw p home draw | 56.0% |
| Raw p draw away | 70.3% |
| Raw p home away | 73.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4091 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T12:02:58Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.50 |
| Reference draw odds | 3.09 |
| Reference away odds | 2.28 |
| Market reference 1x2 last update utc | 2026-10-30T12:02:58Z |
| Market reference home last update utc | 2026-10-30T12:02:58Z |
| Market reference draw last update utc | 2026-10-30T12:02:58Z |
| Market reference away last update utc | 2026-10-30T12:02:58Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 2.48 |
| Reference Under 2.5 odds | 1.55 |
| Market reference over 2 5 last update utc | 2026-10-30T12:02:59Z |
| Market reference under 2 5 last update utc | 2026-10-30T12:02:59Z |
| Home probability edge | +0.8% |
| Draw probability edge | -1.3% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | +3.3% |
| Under 2.5 probability edge | -3.3% |
| Raw edge prob home | 0.0274 |
| Raw ev home | 0.0408 |
| Raw edge prob draw | -0.0444 |
| Raw ev draw | -0.1871 |
| Raw edge prob away | 0.0170 |
| Raw ev away | 0.0022 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 730 |
| Legacy trial matrix | [[0.10350775814706702, 0.1358832152532887, 0.08038441502620139, 0.03332583493110554, 0.01036218843067983, 0.0025775786093855707, 0.0005343072984379672, 9.493437693519143e-05, 1.4759238656515268e-05, 2.0396323135336483e-06, 2.536777176725694e-07, 2.8682702900804945e-08, 2.972824464601134e-09, 2.844175243733227e-10, 2.526729519208097e-11], [0.1053010440241702, 0.13381376951236706, 0.08234885405236765, 0.03414025363026381, 0.010615420196353321, 0.002640569625885944, 0.0005473647313828343, 9.725438877971972e-05, 1.5119925792248102e-05, 2.089476967057957e-06, 2.59877108543329e-07, 2.9383652468403428e-08, 3.0454745223803773e-09, 2.913681364344098e-10, 2.58847788267483e-11], [0.05077937544282487, 0.06315646198435182, 0.044867652800655196, 0.017487287570563437, 0.005437420227348296, 0.0013525500102620589, 0.00028037063131806234, 4.981554860455777e-05, 7.744713710628006e-06, 1.070269863567175e-06, 1.3311400024501234e-07, 1.5050865941223425e-08, 1.5599500032559791e-09, 1.492443039793642e-10, 1.3258676281259995e-11], [0.0173401082612368, 0.021566627762848747, 0.013411664623254877, 0.0063519487200335845, 0.001856766740075784, 0.0004618679021188121, 9.574078172348734e-05, 1.701098129630485e-05, 2.644659825440023e-06, 3.6547506032030735e-07, 4.5455682650798864e-08, 5.139559960520406e-09, 5.326907174947836e-10, 5.096384833029256e-11, 4.527564195361262e-12], [0.004440966709751526, 0.005523418567721384, 0.0034348549165274314, 0.0014240248924269464, 0.0005058283225929688, 0.00011828876421709959, 2.4520125133824745e-05, 4.356674162523789e-06, 6.773225441534073e-07, 9.360164029397758e-08, 1.1641632819126895e-08, 1.3162902067034153e-09, 1.364271610850517e-10, 1.305232645759226e-11, 1.159552268356379e-12], [0.0009098990626816116, 0.001131680038612379, 0.0007037592202915884, 0.0002917650591726812, 9.072014330281262e-05, 2.5779784135120196e-05, 5.023869876599743e-06, 8.92628563998262e-07, 1.387749984040731e-07, 1.9177816528536137e-08, 2.385226344288385e-09, 2.696915567204137e-10, 2.795223520208446e-11, 2.674259994676267e-12, 2.375778948738929e-13], [0.00015535587151383962, 0.00019322268357469633, 0.00012015962153217143, 4.9815871786340854e-05, 1.5489527909977157e-05, 3.8529965052583515e-06, 9.124160537623866e-07, 1.5240711215747436e-07, 2.369439831914686e-08, 3.2744141880337176e-09, 4.0725277415123165e-10, 4.604704912074937e-11, 4.772555592904468e-12, 4.566022860855551e-13, 4.0563972889234744e-14], [2.2736066767067343e-05, 2.8277810113374882e-05, 1.7585155625209956e-05, 7.290467852661845e-06, 2.266865985301503e-06, 5.638794655342468e-07, 1.1688679940825043e-07, 2.3725369245345053e-08, 3.46763477260414e-09, 4.79204930439563e-10, 5.960074874512193e-11, 6.7389070849666806e-12, 6.984553692915962e-13, 6.682296562902652e-14, 5.936468232325498e-15], [2.911461511718156e-06, 3.6211081109252424e-06, 2.251862835595322e-06, 9.335790914455228e-07, 2.902829735699128e-07, 7.220744810307945e-08, 1.496791072930762e-08, 2.6594607321714496e-09, 4.723339347191803e-10, 6.136447106239409e-11, 7.632159415205182e-12, 8.629491112044277e-13, 8.944053279659123e-14, 8.556998645411292e-15, 7.601929986847323e-16], [3.3140133089703454e-07, 4.121778846990444e-07, 2.5632155455610305e-07, 1.0626599464133359e-07, 3.304188064675692e-08, 8.219117548257525e-09, 1.7037441561483152e-09, 3.027169765297379e-10, 4.706274214061785e-11, 7.429853864747648e-12, 8.687416191618129e-13, 9.822643466126124e-14, 1.0180698417489353e-14, 9.740127864166466e-16, 8.653007106182067e-17], [3.39500135964227e-08, 4.222507119026939e-08, 2.6258555566693326e-08, 1.0886292922075108e-08, 3.384936005454079e-09, 8.419976822622843e-10, 1.7453803552778252e-10, 3.1011479167069745e-11, 4.8212864179937094e-12, 6.662709235750404e-13, 9.466652035556889e-14, 1.0062689800464486e-14, 1.0429494919627538e-15, 9.978157677407993e-17, 8.864469798888553e-18], [3.161789637294103e-09, 3.932451813140573e-09, 2.4454785163865307e-09, 1.0138484348999512e-09, 3.1524156992019925e-10, 7.84158609787143e-11, 1.6254855111562053e-11, 2.8881217731805195e-12, 4.4900993607983584e-13, 6.205029920847828e-14, 7.71745876924063e-15, 9.968439698147906e-16, 9.713065022914894e-17, 9.292731342835005e-18, 8.25554566292887e-19], [2.699214697494045e-10, 3.3571277500612535e-10, 2.087701052586648e-10, 8.655207684390073e-11, 2.691212181712104e-11, 6.6943493638475456e-12, 1.3876743507931012e-12, 2.4655848847025256e-13, 3.8331905592074e-14, 5.297224003516093e-15, 6.588382064236916e-16, 7.449318256221973e-17, 8.820248808020178e-18, 7.933189711479418e-19, 7.047745974738946e-20], [2.1270602029346788e-11, 2.6455149492007703e-11, 1.6451695482781042e-11, 6.8205570422732765e-12, 2.120753986219526e-12, 5.275343280251465e-13, 1.0935280135165073e-13, 1.942953070786471e-14, 3.020666379863981e-15, 4.1743675945341324e-16, 5.191837945894962e-17, 5.870280869660044e-18, 6.084264319077002e-19, 6.649825880254698e-20, 5.5538301555552195e-21], [1.5564581602307321e-12, 1.9358329985276782e-12, 1.2038387840869209e-12, 4.990884438117354e-13, 1.551843639939797e-13, 3.860187448026784e-14, 8.001797963830076e-15, 1.4217393366669239e-15, 2.210346857971984e-16, 3.054557881037517e-17, 3.799083131890055e-18, 4.295527954414614e-19, 4.452108518302666e-20, 4.259443159510332e-21, 4.322851778410833e-22]] |
| Legacy trial inputs | {"lambda_home": 1.0244380583664872, "lambda_away": 1.2437423941037429, "rho": 0.05, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2901 |
| Legacy p draw | 0.2891 |
| Legacy p away | 0.4208 |
| Legacy p over 1 5 | 0.6553 |
| Legacy p under 3 5 | 0.8058 |
| Legacy p btts yes | 0.4544 |
| Legacy p over 2 5 | 0.3903 |
| Legacy goal margin distribution | {"-1": 0.2376995921873796, "-10": 2.846734435448275e-07, "-11": 3.1881949291360045e-08, "-12": 3.277451277316804e-09, "-13": 3.10302303200071e-10, "-14": 2.526729519208097e-11, "-2": 0.12044939372096482, "-3": 0.045394044703493494, "-4": 0.013300836583622926, "-5": 0.0031774995828191895, "-6": 0.0006396837921531499, "-7": 0.00011117137297863815, "-8": 1.698710832576381e-05, "-9": 2.315106268640048e-06, "0": 0.2890736739081334, "1": 0.18338788825800886, "10": 3.809821125622821e-08, "11": 3.514453196226821e-09, "12": 2.9758045802549915e-10, "13": 2.3206435027874465e-11, "14": 1.5564581602307321e-12, "2": 0.07608869186426093, "3": 0.02361944272967951, "4": 0.005700395517304766, "5": 0.001121674381355757, "6": 0.0001859952752166425, "7": 2.6624704772164586e-05, "8": 3.3509392480767366e-06, "9": 3.761605920363951e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3103 |
| Legacy raw p draw | 0.2706 |
| Legacy raw p away | 0.4191 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.0244 |
| Legacy lambda away | 1.2437 |
| Legacy model home team | Maritimo |
| Legacy model away team | Santa Clara |
| Legacy home name match score | 95/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,412.3721 |
| Elo away rating | 1,471.5616 |
| Elo rating diff | 0.8105 |
| Elo home expectancy | 0.5012 |

</details>


---
