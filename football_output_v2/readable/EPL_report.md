# Premier League — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,980 |
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
| Training sha256 | 3c3633d0a676185ff520329701a83aa20503ffa5df55c08bc64e611de1a0876e |
| Training as of utc | 2026-10-28T15:54:19.274058+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 80, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 80, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 151, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-28T15:54:19.274058+00:00', 'observations': 411, 'observations_sha256': '12ab74e11af389796b3f3ba7ba8bcc5fe9a3345dfc5b9b70062daadd81763223', 'eligible_training_matches': 209, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 193, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 18, 'retrospective_eligible_training_matches': 209, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'aa0ef3f42a5f7eee4dbdec991826b824706923fff334859ad0c3ff2c5a666e85', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 148, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-21T00:00:00+00:00', 'audit_origin_utc': '2025-10-19T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 31, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-28', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1979, 'tune_start_date': '2025-10-29', 'audit_start_date': '2026-04-29', 'training_shot_matches': 1609, 'tuning_matches': 249, 'audit_matches': 114, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9291957452119189, 'audit_candidate_poisson_score': 0.9172299545156815, 'audit_gain': 0.011965790696237488, 'audit_gain_lower95': 0.0018417655996871333, 'audit_baseline_briers': [0.6363700722068394, 0.1562167946714981, 0.21728883176887465, 0.2522537364336064], 'audit_candidate_briers': [0.634782310416445, 0.15465038640283008, 0.2152834171800079, 0.24898943506191437], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1871.943 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.175 |
| Dixon-Coles low-score adjustment | -0.076 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1980, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-25'} |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261028T155419274058Z_d772deaf7d9a6c6bb17144bf0aca6de9d75ce1e665bcb5581652ac6013e69d80.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3, 'ANCHORED_MAIN': 3} |
| Shot features applied fixtures | 6 |
| Goal rate features used | {'shot_features': 6} |
| Legacy comparison status | {'AVAILABLE': 6} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **45.4%**. Expected goals are 1.64 for Bournemouth and 1.19 for Leeds United (2.83 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 50.7%; Under 3.5 goals: 71.2%; Double Chance 1X: 72.9%; Double Chance X2: 54.6%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 45.4% | 2.20 |
| Draw | 27.5% | 3.64 |
| Leeds United win | 27.1% | 3.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.64 |
| Leeds United expected goals | 1.19 |
| Expected total goals | 2.83 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.2% |
| Under 1.5 | 23.8% |
| Over 2.5 | 50.7% |
| Under 2.5 | 49.3% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.11% |
| 2 | 1-0 | 9.33% |
| 3 | 2-1 | 9.15% |
| 4 | 2-0 | 8.02% |
| 5 | 0-0 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 45.4% | 44.7% | 2.18 | -1.0% |
| Draw | 27.5% | 28.1% | 3.42 | -5.9% |
| Leeds United win | 27.1% | 27.2% | 3.53 | -4.3% |
| Over 2.5 | 50.7% | 50.7% | 1.92 | -2.7% |
| Under 2.5 | 49.3% | 49.3% | 1.97 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | a6c06eabdf4e6710354b6098d39449e7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bournemouth |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6064 |
| Dc lambda away | 1.1733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7240 |
| Shot lambda away | 1.2381 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.95 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.20 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.48 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.25 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1603085424968895, "-10": 8.149081589465108e-08, "-11": 8.340525125274844e-09, "-12": 7.840864712035343e-10, "-13": 6.813352044441165e-11, "-14": 5.47355767171091e-12, "-15": 3.719125773611391e-13, "-2": 0.07656632739489401, "-3": 0.02559617736281451, "-4": 0.006730719229310555, "-5": 0.0014525766580715475, "-6": 0.00026524714732625214, "-7": 4.192404989174138e-05, "-8": 5.836709642831338e-06, "-9": 7.257149097320981e-07, "0": 0.2750664267259316, "1": 0.21667112853200135, "10": 1.92288556249167e-06, "11": 2.708847417174936e-07, "12": 3.5051086439043794e-08, "13": 4.1922263957084776e-09, "14": 4.6355361516302685e-10, "15": 4.335283621445037e-11, "2": 0.14025281473278167, "3": 0.06453499132183582, "4": 0.023357588063677433, "5": 0.0069382821526167635, "6": 0.0017438534828636454, "7": 0.0003793751461316199, "8": 7.269760627872514e-05, "9": 1.2441262200752895e-05} |
| Raw goal margin distribution | {"-1": 0.15639193322893075, "-10": 1.1256327272710652e-07, "-11": 1.2028848364683303e-08, "-12": 1.1809035415074351e-09, "-13": 1.0716765209461632e-10, "-14": 8.983418118399922e-12, "-15": 6.318343232828363e-13, "-2": 0.07669097845687264, "-3": 0.026526990417809534, "-4": 0.007242425580691951, "-5": 0.001626079495319087, "-6": 0.0003092974265286654, "-7": 5.096481789662724e-05, "-8": 7.401257729823143e-06, "-9": 9.603122211011162e-07, "0": 0.26142806488152215, "1": 0.21854051644202674, "10": 2.7470114212006028e-06, "11": 4.040491329269451e-07, "12": 5.459727023543843e-08, "13": 6.8197208100311295e-09, "14": 7.868480423503658e-10, "15": 7.617261143511946e-11, "2": 0.14529043680202666, "3": 0.06917148614635336, "4": 0.02599378621291786, "5": 0.008032923854348848, "6": 0.0021030740211124043, "7": 0.00047697443721538295, "8": 9.534030358997496e-05, "9": 1.7026674512948794e-05} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 57.0% |
| P home draw | 72.9% |
| P draw away | 54.6% |
| P home away | 72.5% |
| Raw p home draw | 73.1% |
| Raw p draw away | 53.0% |
| Raw p home away | 73.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9566 |
| Totals anchor target over 2 5 | 0.5067 |
| Totals anchor reference over odds | 1.92 |
| Totals anchor reference under odds | 1.97 |
| Totals anchor reference last update utc | 2026-10-28T15:54:44Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5335 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.18 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.53 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Home probability edge | +0.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0225 |
| Raw ev home | 0.0240 |
| Raw edge prob draw | -0.0195 |
| Raw ev draw | -0.1059 |
| Raw edge prob away | -0.0030 |
| Raw ev away | -0.0510 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08668039209081844, 0.07105614174406205, 0.04785258347461164, 0.018285876938927647, 0.005240677793337043, 0.0012015701002606293, 0.00022957760471300367, 3.75978610279485e-05, 5.387717417770632e-06, 6.862683302866385e-07, 7.867298266997048e-08, 8.199069888071742e-09, 7.832763254385817e-10, 6.907220269555431e-11, 5.655967795918558e-12, 4.3226226705848195e-13], [0.0976549761362297, 0.13549319479909364, 0.06926003919654534, 0.02646629422223921, 0.007585160988759638, 0.001739107613397743, 0.00033228203675790514, 5.4417737547724145e-05, 7.797980640537039e-06, 9.932791085400446e-07, 1.1386833202688459e-07, 1.1867027035736697e-08, 1.1336848517360528e-09, 9.997252224895979e-11, 8.186236202848957e-12, 6.256402347752445e-13], [0.08011775176484845, 0.0918460348231467, 0.0509622656634758, 0.019153162087812085, 0.005489239130342094, 0.0012585596505447158, 0.00024046629480695147, 3.9381098802558225e-05, 5.643252731631959e-06, 7.188175119854532e-07, 8.24043820289399e-08, 8.587945498048762e-09, 8.20426522106453e-10, 7.234824440789141e-11, 5.924226019921265e-12, 4.527641355712712e-13], [0.03865314558907438, 0.04431150497355697, 0.02539909033401625, 0.009395398808489065, 0.0026483064564905706, 0.0006071973855160447, 0.00011601397315440453, 1.8999576397759958e-05, 2.722610964820106e-06, 3.4679652549786564e-07, 3.975633995685604e-08, 4.143290348703439e-09, 3.958182188785819e-10, 3.490471415648382e-11, 2.858167706985861e-12, 2.1843795743437457e-13], [0.013986279236049079, 0.016033703660716388, 0.009190423297750895, 0.0035119305424437235, 0.0009743258793932542, 0.0002197086952640356, 4.197857118980882e-05, 6.874819030015241e-06, 9.85151314977749e-07, 1.2548507941034856e-07, 1.4385459800639201e-08, 1.4992108634328917e-09, 1.432231206951561e-10, 1.2629944378577251e-11, 1.0342012543647068e-12, 7.903973200289612e-14], [0.004048643470280055, 0.004641316574250114, 0.002660374975043025, 0.0010166073777573466, 0.00029135664244867027, 6.466558798701882e-05, 1.2151642711468992e-05, 1.9900711765776873e-06, 2.851742319245425e-07, 3.632448192960554e-08, 4.1641952735162554e-09, 4.3398034390489706e-10, 4.145915740771223e-11, 3.656021803606699e-12, 2.993728413949435e-13, 2.2879830258315885e-14], [0.0009766425170935156, 0.0011196113303081074, 0.0006417545360838829, 0.00024523324802420656, 7.028311747917422e-05, 1.6114345480931906e-05, 2.980435526235406e-06, 4.800590956836326e-07, 6.879175252686049e-08, 8.762449379469295e-09, 1.0045167433116843e-09, 1.0468781915515763e-10, 1.0001072246661298e-11, 8.819315316436672e-13, 7.221684189177833e-14, 5.519235066803331e-15], [0.00020193654912457028, 0.00023149765082523018, 0.00013269307257632936, 5.070591846031245e-05, 1.4532165001067863e-05, 3.3319001178697594e-06, 6.366084242921782e-07, 1.00923581217368e-07, 1.4223801309456506e-08, 1.8117773480051474e-09, 2.0769999373556876e-10, 2.1645890451793006e-11, 2.0678825483110896e-12, 1.8235352951280128e-13, 1.4931993626183742e-14, 1.1411906236833048e-15], [3.653442586595987e-05, 4.1882629959180425e-05, 2.4006873663943786e-05, 9.173731189250526e-06, 2.6291639983205556e-06, 6.028084483805043e-07, 1.1517540229233431e-07, 1.8862243878877652e-08, 2.6165056701020965e-09, 3.277873445558727e-10, 3.7577150131507245e-11, 3.916181510687699e-12, 3.7412198033640356e-13, 3.299145961572221e-14, 2.7015011226633782e-15, 2.0646457721809863e-16], [5.875395697385595e-06, 6.7354835343570675e-06, 3.860738984931879e-06, 1.4753017046454818e-06, 4.228170684857114e-07, 9.69424886258425e-08, 1.8522285407077847e-08, 3.0333895744137724e-09, 4.346802024935479e-10, 5.3597639428213536e-11, 6.043084596776915e-12, 6.297927352818686e-13, 6.016557319473104e-14, 5.305622718360245e-15, 4.344501848971851e-16, 3.320323393339527e-17], [8.503827938820441e-07, 9.748686898895627e-07, 5.587889179815751e-07, 2.135296497516959e-07, 6.119696076978926e-08, 1.4031093150067356e-08, 2.6808462995199275e-09, 4.39041459347237e-10, 6.291398640710425e-11, 8.013760384104427e-12, 8.893130475247111e-13, 9.115384450343035e-14, 8.70813998989321e-15, 7.679159843703591e-16, 6.288069452068303e-17, 4.805711869034428e-18], [1.118920221604534e-07, 1.2827167933948763e-07, 7.352456146059187e-08, 2.8095893371573427e-08, 8.052199244703278e-09, 1.8461890303727049e-09, 3.527415132487514e-10, 5.7768380371831663e-11, 8.278122760610118e-12, 1.0544379083605417e-12, 1.208795038762172e-13, 1.2194901453920502e-14, 1.1458032779301694e-15, 1.0104116988102305e-16, 8.273742266884228e-18, 6.323279619664331e-19], [1.3495693924107122e-08, 1.5471302511760102e-08, 8.868058313875497e-09, 3.388745418537251e-09, 9.71204330069296e-10, 2.2267541151615886e-10, 4.254540587625604e-11, 6.9676493903350365e-12, 9.98453767178982e-13, 1.271794985776841e-13, 1.4579705992550426e-14, 1.519454637711197e-15, 1.405156848627932e-16, 1.2186934118435744e-17, 9.97925420283291e-19, 7.626731977473852e-20], [1.5025509633289527e-09, 1.7225064990155198e-09, 9.873304505349858e-10, 3.772879498996634e-10, 1.0812960118546975e-10, 2.4791696963845554e-11, 4.7368176059771734e-12, 7.757473133623209e-13, 1.1116343317733151e-13, 1.4159603735695656e-14, 1.6232400799360081e-15, 1.6916936931634298e-16, 1.616114556696752e-17, 1.379580671895919e-18, 1.1110460936719203e-19, 8.491266580472061e-21], [1.5533828965455134e-10, 1.7807796208330057e-10, 1.0207322563633073e-10, 3.900517604729986e-11, 1.1178767122790987e-11, 2.5630410535064042e-12, 4.897066144684041e-13, 8.01991172364877e-14, 1.1492413903643563e-14, 1.4638629105904195e-15, 1.67815497690226e-16, 1.748924404754897e-17, 1.6707883942046089e-18, 1.4733629866989974e-19, 1.1678848675000717e-20, 8.778529712490082e-22], [1.4988721958145514e-11, 1.718289203824491e-11, 9.8491312208753e-12, 3.763642177351379e-12, 1.0786486230213435e-12, 2.473099826433828e-13, 4.72522022847997e-14, 7.738480140470692e-15, 1.1089126641777212e-15, 1.4124936099448385e-16, 1.6192658234749075e-17, 1.6875518384412848e-18, 1.6121577459955993e-19, 1.4216603131246767e-20, 1.1641245876014603e-21, 8.612446051766986e-23]] |
| Legacy trial inputs | {"lambda_home": 1.4473625908471903, "lambda_away": 1.146388070058701, "rho": -0.10285334743314112, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T15:54:44Z", "over": 1.92, "under": 1.97, "bookmaker": "pinnacle", "event_id": "a6c06eabdf4e6710354b6098d39449e7", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Bournemouth", "away_team": "Leeds United"}} |
| Legacy p home | 0.4372 |
| Legacy p draw | 0.2836 |
| Legacy p away | 0.2792 |
| Legacy p over 1 5 | 0.7446 |
| Legacy p under 3 5 | 0.7369 |
| Legacy p btts yes | 0.5337 |
| Legacy p over 2 5 | 0.4811 |
| Legacy goal margin distribution | {"-1": 0.16235000443970526, "-10": 9.139639802305474e-08, "-11": 9.408040191654674e-09, "-12": 8.893915116648971e-10, "-13": 7.771120303397454e-11, "-14": 6.2816080306938024e-12, "-15": 4.3226226705848195e-13, "-2": 0.08045935349682098, "-3": 0.02725278051877484, "-4": 0.007240273780278529, "-5": 0.0015760856028497292, "-6": 0.00029000022114416266, "-7": 4.615595708751868e-05, "-8": 6.467691151188852e-06, "-9": 8.091333608669054e-07, "0": 0.28357332685936965, "1": 0.2187201587372505, "10": 9.879112455624122e-07, "11": 1.2839073894741882e-07, "12": 1.5324037290936326e-08, "13": 1.6904780566331286e-09, "14": 1.7252118169279625e-10, "15": 1.4988721958145514e-11, "2": 0.13471002070428573, "3": 0.05760761141604126, "4": 0.019322785110957797, "5": 0.005310558812337185, "6": 0.0012336854297699217, "7": 0.00024790172741121614, "8": 4.3857790705142214e-05, "9": 6.927288434048728e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4272 |
| Legacy raw p draw | 0.2862 |
| Legacy raw p away | 0.2866 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4474 |
| Legacy lambda away | 1.1464 |
| Legacy model home team | Bournemouth |
| Legacy model away team | Leeds |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.998094794574687, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,502.9673 |
| Elo away rating | 1,455.9965 |
| Elo rating diff | 106.9708 |
| Elo home expectancy | 0.6493 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **46.6%**. Expected goals are 1.58 for Brentford and 1.20 for Nottingham Forest (2.78 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.9%; Under 3.5 goals: 69.6%; Double Chance 1X: 72.3%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 46.6% | 2.15 |
| Draw | 25.8% | 3.88 |
| Nottingham Forest win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.58 |
| Nottingham Forest expected goals | 1.20 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 77.5% |
| Under 1.5 | 22.5% |
| Over 2.5 | 52.9% |
| Under 2.5 | 47.1% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 2-1 | 9.57% |
| 3 | 1-0 | 9.19% |
| 4 | 2-0 | 7.97% |
| 5 | 1-2 | 6.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 46.6% | 47.1% | 2.07 | -3.6% |
| Draw | 25.8% | 25.4% | 3.77 | -2.9% |
| Nottingham Forest win | 27.7% | 27.5% | 3.49 | -3.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | b9254b648ca25ce7831988b53ed17c3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6215 |
| Dc lambda away | 1.1275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.4728 |
| Shot lambda away | 1.3686 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.55 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.44 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.12 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.66 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.15991785598580358, "-10": 1.2377989253216157e-07, "-11": 1.3312944137598334e-08, "-12": 1.3153175519154335e-09, "-13": 1.2012508001749475e-10, "-14": 1.0137268553879883e-11, "-15": 7.200513026454685e-13, "-2": 0.07934809439260108, "-3": 0.027722144557930584, "-4": 0.007634482192260887, "-5": 0.0017276323665334702, "-6": 0.0003310440421243446, "-7": 5.493360821177092e-05, "-8": 8.032173634091399e-06, "-9": 1.0491297194896818e-06, "0": 0.2576391710212873, "1": 0.22297864221396038, "10": 1.9929704282922595e-06, "11": 2.817137898293092e-07, "12": 3.658034987637392e-08, "13": 4.390704126437778e-09, "14": 4.869727700364513e-10, "15": 4.546010234720782e-11, "2": 0.14352293603775315, "3": 0.06590143565252767, "4": 0.023852333963252783, "5": 0.007093913193843234, "6": 0.0017865022080055938, "7": 0.00038961812315684767, "8": 7.487164161192308e-05, "9": 1.2852768940161097e-05} |
| Raw goal margin distribution | {"-1": 0.16254600767331803, "-10": 1.258141389984701e-07, "-11": 1.3531734193188627e-08, "-12": 1.3369339875684404e-09, "-13": 1.2209926188614619e-10, "-14": 1.0303868332825339e-11, "-15": 7.318849033055014e-13, "-2": 0.08065213156151786, "-3": 0.028177740967426663, "-4": 0.007759950215410661, "-5": 0.0017560249427815695, "-6": 0.000336484547517488, "-7": 5.5836408303937236e-05, "-8": 8.164177471691123e-06, "-9": 1.0663715216993305e-06, "0": 0.266758542323342, "1": 0.21643340525826116, "10": 1.9344694724636862e-06, "11": 2.73444461925018e-07, "12": 3.550658309994201e-08, "13": 4.261820935543085e-09, "14": 4.726783419279362e-10, "15": 4.4125682427261866e-11, "2": 0.13931001404837562, "3": 0.06396698799519258, "4": 0.023152180907400212, "5": 0.0068856809508990365, "6": 0.0017340618479909505, "7": 0.00037818140925018865, "8": 7.26738856710559e-05, "9": 1.247549326292613e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 28.1% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 72.3% |
| P draw away | 53.4% |
| P home away | 74.2% |
| Raw p home draw | 71.9% |
| Raw p draw away | 54.8% |
| Raw p home away | 73.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5285 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.07 |
| Reference draw odds | 3.77 |
| Reference away odds | 3.49 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:45Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:45Z |
| Home probability edge | -0.6% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | -0.0195 |
| Raw ev home | -0.0645 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | 0.0057 |
| Raw edge prob away | 0.0065 |
| Raw ev away | -0.0183 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.07828513974127167, 0.06602144423032265, 0.0424237811210285, 0.015184826296668792, 0.004076350755998115, 0.0008754336815599514, 0.0001566728381755668, 2.403351984837082e-05, 3.2258866479326903e-06, 3.8488262249150423e-07, 4.132853517087552e-08, 4.0344007604977445e-09, 3.610102231607826e-10, 2.98193283895281e-11, 2.2871335869709605e-12, 1.6372763255756227e-13], [0.09702921849313358, 0.12598899957505402, 0.067834502531628, 0.02428013511867606, 0.0065179769075438335, 0.0013997952732840058, 0.0002505157191797281, 3.84289617737571e-05, 5.158107321024899e-06, 6.15417120772346e-07, 6.608323326200648e-08, 6.450899975672686e-09, 5.772457864394619e-10, 4.768031640933215e-11, 3.657066036922636e-12, 2.6179614856909195e-13], [0.08720477557163277, 0.09364012360314056, 0.049036317786691645, 0.019411646530013163, 0.005211036231948625, 0.0011191177860650204, 0.00020028400036326013, 3.072344609374795e-05, 4.123838503789521e-06, 4.920178392154929e-07, 5.2832669973725635e-08, 5.157409113094622e-09, 4.615003628494345e-10, 3.8119781626141554e-11, 2.923775872690826e-12, 2.0930255429398643e-13], [0.04647937558424277, 0.049909359277349914, 0.026796230717007118, 0.009354882176316703, 0.0027774363114882617, 0.0005964799010209575, 0.0001067496041974423, 1.6375325558409785e-05, 2.197969519558573e-06, 2.622411650410064e-07, 2.8159346718460475e-08, 2.748853530529568e-09, 2.4597561952926846e-10, 2.0317507106423897e-11, 1.5583467306709066e-12, 1.1155641383172262e-13], [0.0185798226691714, 0.0199509359419944, 0.01071161582241611, 0.003834029436367561, 0.0010038788855194574, 0.00023843889138759074, 4.267244753316163e-05, 6.545927977749116e-06, 8.786237636007921e-07, 1.0482916953537184e-07, 1.1256512419372535e-08, 1.0988359998123492e-09, 9.832712540447175e-11, 8.121788952022037e-12, 6.229387884196155e-13, 4.459393786057623e-14], [0.005941728882173488, 0.006380203644765349, 0.0034255180062832485, 0.0012261023069379178, 0.0003291458834082196, 6.894524063377251e-05, 1.3646422707872199e-05, 2.093353096989164e-06, 2.8097922599729623e-07, 3.3523813193119025e-08, 3.5997730519627784e-09, 3.5140193279079283e-10, 3.144449391792281e-11, 2.5973050900651577e-12, 1.9921252516152548e-13, 1.4260905137468257e-14], [0.0015834445219541408, 0.0017002961108787515, 0.0009128854293870666, 0.00032675085312307143, 8.771592516955302e-05, 1.883779878108569e-05, 3.288249566129682e-06, 5.578693608670184e-07, 7.487972356382287e-08, 8.93394825114276e-09, 9.593236299471682e-10, 9.364706409797298e-11, 8.379818841842162e-12, 6.921703427172962e-13, 5.308925868665352e-14, 3.800468275451084e-15], [0.0003616979796131675, 0.00038838977906848447, 0.00020852566089281886, 7.463799443105252e-05, 2.0036491631909526e-05, 4.3030201974297e-06, 7.70094184469564e-07, 1.1522100845016758e-07, 1.7104384998347054e-08, 2.0407352373918623e-09, 2.1913329702188958e-10, 2.1391310785640908e-11, 1.9141583444162153e-12, 1.5810886395946022e-13, 1.2126902673183463e-14, 8.681211610231629e-16], [7.229318634917826e-05, 7.762812140765399e-05, 4.1678376190081734e-05, 1.4918022063335225e-05, 4.00472743828579e-06, 8.600519177070304e-07, 1.5392002588407577e-07, 2.3611240086180963e-08, 3.0911115546760422e-09, 4.0788520014374336e-10, 4.3798542347004514e-11, 4.275517431790562e-12, 3.8258606266673837e-13, 3.160148579735672e-14, 2.423824528211117e-15, 1.735128433247897e-16], [1.284387671997385e-05, 1.3791701150746191e-05, 7.404735531901036e-06, 2.6503913572417262e-06, 7.114947910305247e-07, 1.5280002669202802e-07, 2.734600502517101e-08, 4.194860846330093e-09, 5.630530059469913e-10, 6.552282900385674e-11, 7.781412147230309e-12, 7.596043497485346e-13, 6.797166471453548e-14, 5.61443765652844e-15, 4.3062569245222145e-16, 3.082693793895928e-17], [2.0537018739357946e-06, 2.2052564903556296e-06, 1.1839976020803074e-06, 4.23790559167065e-07, 1.1376613288125051e-07, 2.4432319617865056e-08, 4.372553784910956e-09, 6.707471403560424e-10, 9.003068455494117e-11, 1.0741619206743481e-11, 1.1250080258284445e-12, 1.214587239149024e-13, 1.0868489182996554e-14, 8.977337129355151e-16, 6.885590782561069e-17, 4.929145739501618e-18], [2.985286281451686e-07, 3.205587934301495e-07, 1.7210734642746572e-07, 6.160271646758649e-08, 1.6537184880361292e-08, 3.5515120040025683e-09, 6.355997915115312e-10, 9.750062858882322e-11, 1.3086970943669333e-11, 1.5614149680359967e-12, 1.6766408679371228e-13, 1.5963687990837448e-14, 1.579856943691916e-15, 1.3049567571787024e-16, 1.0008979377068226e-17, 7.165066820146572e-19], [3.977828088901612e-08, 4.2713751795716844e-08, 2.2932924094388015e-08, 8.20842602064439e-09, 2.203543390031983e-09, 4.73231136838335e-10, 8.469226953822036e-11, 1.2991743589080017e-11, 1.7438099971119843e-12, 2.0805509866426257e-13, 2.2340869553848864e-14, 2.1808665791219557e-15, 1.9034160163619705e-16, 1.738826080352727e-17, 1.333674413563385e-18, 9.547293414746249e-20], [4.892647516897747e-09, 5.253704458565648e-09, 2.8207029468836166e-09, 1.0096196791308335e-09, 2.710313481293104e-10, 5.8206465810595415e-11, 1.0416976626333477e-11, 1.5979579959383399e-12, 2.144850773243772e-13, 2.5590353306060078e-14, 2.747881444473321e-15, 2.682421465823743e-16, 2.4003108007267702e-17, 1.9337930510693127e-18, 1.6403923603628484e-19, 1.1742976411947152e-20], [5.588009864839895e-10, 6.0003816420507e-10, 3.221592366613569e-10, 1.1531108070292437e-10, 3.095513915107764e-11, 6.647899813418562e-12, 1.189747839972479e-12, 1.8250660841729813e-13, 2.449685418395973e-14, 2.9227355174294796e-15, 3.1384211852775353e-16, 3.0636577764722384e-17, 2.7414524318006907e-18, 2.2644308965102934e-19, 1.6940136461447613e-20, 1.34119345008835e-21], [5.956719860209918e-11, 6.396300894337538e-11, 3.4341605859454845e-11, 1.2291957622466693e-11, 3.299763182541712e-12, 7.08654383315244e-13, 1.2682501925413064e-13, 1.945488224384197e-14, 2.611321407079159e-15, 3.1155844610005737e-16, 3.3455015750194774e-17, 3.2658051011729217e-18, 2.9223398922535424e-19, 2.413843357397559e-20, 1.851410650257799e-21, 1.2926988632134015e-22]] |
| Legacy trial inputs | {"lambda_home": 1.5989735176623374, "lambda_away": 1.0737958212646461, "rho": -0.10285334743314112, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4774 |
| Legacy p draw | 0.2637 |
| Legacy p away | 0.2589 |
| Legacy p over 1 5 | 0.7587 |
| Legacy p under 3 5 | 0.7201 |
| Legacy p btts yes | 0.5357 |
| Legacy p over 2 5 | 0.5030 |
| Legacy goal margin distribution | {"-1": 0.15629769030708307, "-10": 4.8261890216197626e-08, "-11": 4.65136926923188e-09, "-12": 4.117258718566373e-10, "-13": 3.368569698074473e-11, "-14": 2.5489297355400525e-12, "-15": 1.6372763255756227e-13, "-2": 0.07255627513833224, "-3": 0.02293550665910478, "-4": 0.005693718483883796, "-5": 0.0011589793408888329, "-6": 0.0001994994960728889, "-7": 2.9712935340294162e-05, "-8": 3.896986270597166e-06, "-9": 4.5637756528808e-07, "0": 0.2637415700338374, "1": 0.22164838021122715, "10": 2.3982348749329977e-06, "11": 3.441816937316545e-07, "12": 4.5366436541865595e-08, "13": 5.527027286962272e-09, "14": 6.227639954273649e-10, "15": 5.956719860209918e-11, "2": 0.14914403013020516, "3": 0.07020350495924307, "4": 0.02595171173704398, "5": 0.007866205251928018, "6": 0.00201628047252987, "7": 0.00044717164813000133, "8": 8.733275077753091e-05, "9": 1.5229726788850554e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4833 |
| Legacy raw p draw | 0.2738 |
| Legacy raw p away | 0.2430 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.5990 |
| Legacy lambda away | 1.0738 |
| Legacy model home team | Brentford |
| Legacy model away team | Nott'm Forest |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.85815621132972, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,503.9116 |
| Elo away rating | 1,478.7386 |
| Elo rating diff | 85.1730 |
| Elo home expectancy | 0.6202 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **51.2%**. Expected goals are 1.74 for Chelsea and 1.38 for Manchester United (3.11 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.6%; Under 3.5 goals: 61.9%; Double Chance 1X: 75.3%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 79.3%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 51.2% | 1.95 |
| Draw | 24.1% | 4.14 |
| Manchester United win | 24.7% | 4.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.74 |
| Manchester United expected goals | 1.38 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 20.7% |
| Under 4.5 | 79.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 2-1 | 10.45% |
| 3 | 1-0 | 7.83% |
| 4 | 2-0 | 7.58% |
| 5 | 2-2 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 51.2% | 53.8% | 1.82 | -6.8% |
| Draw | 24.1% | 23.8% | 4.00 | -3.5% |
| Manchester United win | 24.7% | 22.5% | 4.22 | +4.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T12:30:00+00:00 |
| Fixture id | 6601f69175a02f03fb7065aacb538e01 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7690 |
| Dc lambda away | 1.3442 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6583 |
| Shot lambda away | 1.4548 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.73 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.84 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.13430060296139376, "-10": 3.093575629633366e-07, "-11": 3.8056859812775546e-08, "-12": 4.303040850675505e-09, "-13": 4.5005309942018673e-10, "-14": 4.3763040264212683e-11, "-15": 3.9434465408220375e-12, "-16": 2.953386693235682e-13, "-2": 0.07256645623482982, "-3": 0.0282509759080365, "-4": 0.00875485734031945, "-5": 0.002242272937606218, "-6": 0.0004880548820249787, "-7": 9.221834408734671e-05, "-8": 1.5379417031999147e-05, "-9": 2.293989881928938e-06, "0": 0.2413664932569617, "1": 0.23370757070970552, "10": 4.272909726336235e-06, "11": 6.624478519197596e-07, "12": 9.439521515463143e-08, "13": 1.2442109940398123e-08, "14": 1.5247320481614893e-09, "15": 1.7314811470071752e-10, "16": 1.634247725429117e-11, "2": 0.15752618931359053, "3": 0.07728693292461394, "4": 0.03018404626210053, "5": 0.009742549599104472, "6": 0.002672443777818539, "7": 0.0006363748409820119, "8": 0.00013374923953720884, "9": 2.5141935729067373e-05} |
| Raw goal margin distribution | {"-1": 0.16212003028756364, "-10": 3.7343881093162386e-07, "-11": 4.5940071224179895e-08, "-12": 5.194385562369158e-09, "-13": 5.432784403059344e-10, "-14": 5.28282469077933e-11, "-15": 4.76030381501142e-12, "-16": 3.5651600186478205e-13, "-2": 0.087598088342415, "-3": 0.03410296729033074, "-4": 0.010568364593149986, "-5": 0.00270674403943072, "-6": 0.0005891520254650515, "-7": 0.0001113207268384885, "-8": 1.856515533105614e-05, "-9": 2.7691737857989462e-06, "0": 0.25005969137810036, "1": 0.20640783303712765, "10": 3.7737846262235e-06, "11": 5.850663082913094e-07, "12": 8.336876614640094e-08, "13": 1.098872810755989e-08, "14": 1.3466257728304074e-09, "15": 1.529224194206e-10, "16": 1.4433487568559554e-11, "2": 0.1391253149569633, "3": 0.06825892844896574, "4": 0.026658201796086918, "5": 0.008604507525799115, "6": 0.002360271545410282, "7": 0.0005620389255151711, "8": 0.00011812578693708751, "9": 2.220506788221054e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 62.4% |
| P home draw | 75.3% |
| P draw away | 48.8% |
| P home away | 75.9% |
| Raw p home draw | 70.2% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6058 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.22 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:45Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:45Z |
| Home probability edge | -2.6% |
| Draw probability edge | +0.4% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +0.4% |
| Under 2.5 probability edge | -0.4% |
| Raw edge prob home | -0.0854 |
| Raw ev home | -0.1771 |
| Raw edge prob draw | 0.0124 |
| Raw ev draw | 0.0002 |
| Raw edge prob away | 0.0730 |
| Raw ev away | 0.2568 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.04536527586817435, 0.03778974763864308, 0.0346064201742704, 0.017133452929492334, 0.006362010455188283, 0.0018898783426079353, 0.00046783431314884136, 9.926668201332267e-05, 1.8429900599123478e-05, 3.0415149637954166e-06, 4.517513213222777e-07, 6.099808774893597e-08, 7.54995648186453e-09, 8.626022171408261e-10, 9.15149419209689e-11, 9.061711334788192e-12, 8.412008730969915e-13], [0.06151782211190289, 0.10664022027397387, 0.06360676073836925, 0.031491365926331526, 0.011693404715089005, 0.003473605156428842, 0.0008598816367542711, 0.0001824526218059281, 3.387424275429522e-05, 5.590318605914099e-06, 8.303210232057492e-07, 1.1211476810968418e-07, 1.3876855020216831e-08, 1.585466874694447e-09, 1.6820488757403086e-10, 1.665546744937749e-11, 1.5461311051112124e-12], [0.06672896654966937, 0.09911145980904965, 0.06599322512494389, 0.028940638293611567, 0.010746266042313438, 0.0031922511917139265, 0.0007902332176647826, 0.00016767438242465532, 3.113050762280009e-05, 5.137515759026768e-06, 7.630669452824951e-07, 1.0303373181159702e-07, 1.2752861934679717e-08, 1.4570477334763203e-09, 1.5458068163462167e-10, 1.530641319881314e-11, 1.4208980700361148e-12], [0.040882716639181624, 0.06072244089158745, 0.04509503197126751, 0.02001764210805332, 0.0065838956041697734, 0.001955790830580111, 0.00048415077270244514, 0.00010272876411497374, 1.9072672450718867e-05, 3.1475925953278853e-06, 4.6750686116934516e-07, 6.312549226722327e-08, 7.813273122191035e-09, 8.926868299861207e-10, 9.470666986061838e-11, 9.377752809996241e-12, 8.705390803139052e-13], [0.018785655685475692, 0.027902031976949515, 0.020721219463333284, 0.010258964565790604, 0.003415458512282069, 0.0008986881537338063, 0.00022246784126690077, 4.720398619031152e-05, 8.763915099459856e-06, 1.4463224461290623e-06, 2.148199446244189e-07, 2.900623686958472e-08, 3.590208056511399e-09, 4.101906331490238e-10, 4.351782458151268e-11, 4.309088286546361e-12, 4.000137165017677e-13], [0.006905624450504903, 0.010256812829150558, 0.007617139490153971, 0.003771204887842225, 0.0014003274777036015, 0.0003729624269999937, 8.17793847510759e-05, 1.7352229097286185e-05, 3.2216233176130727e-06, 5.316694724169272e-07, 7.896801085316665e-08, 1.0662719571646875e-08, 1.3197638108854222e-09, 1.507864571281403e-10, 1.599719267159918e-11, 1.5840248500863183e-12, 1.4704541313123695e-13], [0.0021154282931719923, 0.0031420115895483057, 0.0023333896168262172, 0.0011552486782721962, 0.00042896806614263293, 0.00012742787261725398, 2.8282556161264623e-05, 5.315579589521066e-06, 9.868930992218999e-07, 1.6286849257844614e-07, 2.419059501593484e-08, 3.266354668674655e-09, 4.042886672829979e-10, 4.619103455773816e-11, 4.9004857173126864e-12, 4.852408365061209e-13, 4.504502518903118e-14], [0.0005554524301947252, 0.0008250045528594542, 0.0006126829906930268, 0.0003033360610221186, 0.00011263504207820707, 3.3459002958528976e-05, 8.282686411521994e-06, 1.5757185756837482e-06, 2.591305846076437e-07, 4.27647206463331e-08, 6.351775114678849e-09, 8.576535751409249e-10, 1.0615492071622306e-10, 1.212847652700757e-11, 1.286730781469493e-12, 1.2741070105614428e-13, 1.1827566450816933e-14], [0.00012761551776745744, 0.00018954527417723192, 0.0001407642722117438, 6.969163582794663e-05, 2.5877966198708785e-05, 7.68722532195722e-06, 1.9029520035429692e-06, 4.0377485385988953e-07, 6.721322862639841e-08, 9.8252193541565e-09, 1.4593240139718636e-09, 1.970464059691848e-10, 2.4389154560031395e-11, 2.78652451152643e-12, 2.9562714280859015e-13, 2.927268241259554e-14, 2.717390247119573e-15], [2.6061990373980308e-05, 3.87094547548839e-05, 2.8747265000074464e-05, 1.4232616643099588e-05, 5.284869095605545e-06, 1.5699061983083965e-06, 3.8862606731616683e-07, 8.246000595105687e-08, 1.530956492408142e-08, 2.265300470907245e-09, 2.9802714489594446e-10, 4.0241356423081224e-11, 4.98081990727263e-12, 5.690716635934148e-13, 6.037378435594527e-14, 5.9781473335227254e-15, 5.549528748676822e-16], [4.790205914785568e-06, 7.114815732189608e-06, 5.283760636131104e-06, 2.615961538176213e-06, 9.71361390184215e-07, 2.885494871605576e-07, 7.142965136524394e-08, 1.5156187327671076e-08, 2.8139051315645272e-09, 4.6438311038754384e-10, 6.184176725288953e-11, 7.396379969094359e-12, 9.154770083914807e-13, 1.0459563562741493e-13, 1.1096729557868727e-14, 1.098786251762652e-15, 1.0200059571322884e-16], [8.004018801738289e-07, 1.188824027701494e-06, 8.82870595289872e-07, 4.371044942255663e-07, 1.6230606718427753e-07, 4.8214117755070036e-08, 1.1935275491275336e-08, 2.5324675074803598e-09, 4.7017915262957e-10, 7.759439182517887e-11, 1.1524970105845227e-11, 1.3952518218444045e-12, 1.5296827147048742e-13, 1.7477023932468516e-14, 1.8541673071889687e-15, 1.8359765685758623e-16, 1.704341526023388e-17], [1.2259519724562936e-07, 1.8208867292360175e-07, 1.3522668730915747e-07, 6.695000725747485e-08, 2.485994200350641e-08, 7.38481433217413e-09, 1.8280909743940767e-09, 3.8789058507743074e-10, 7.201595521600545e-11, 1.1884904329430753e-11, 1.765245707655293e-12, 2.3835373023109324e-13, 2.6451248942042957e-14, 2.6769042519018563e-15, 2.8399734231241703e-16, 2.8121112048615995e-17, 2.610489689396736e-18], [1.7333118536092683e-08, 2.574460193200692e-08, 1.9119021405680138e-08, 9.465724904875492e-09, 3.514822205341556e-09, 1.0441017679522e-09, 2.58464591320386e-10, 5.484189952980515e-11, 1.0181973815401372e-11, 1.6803468664388364e-12, 2.4957921503902e-13, 3.369963548684356e-14, 4.171127174143337e-15, 4.2728294163164506e-16, 4.01529563052431e-17, 3.97590264102114e-18, 3.690840117733448e-19], [2.275596588360251e-09, 3.379906979991959e-09, 2.510060713711586e-09, 1.2427175903192674e-09, 4.614471078884756e-10, 1.3707599218833542e-10, 3.393279408987317e-11, 7.199976115628228e-12, 1.3367510773582854e-12, 2.206060951217629e-13, 3.276626817533156e-14, 4.424291877030707e-15, 5.47610791868328e-16, 6.256596105295789e-17, 5.951350934855413e-18, 5.219805349349303e-19, 4.845558035392454e-20], [2.7883713870428994e-10, 4.141523133793769e-10, 3.0756688200597064e-10, 1.5227471287070566e-10, 5.6542794924696344e-11, 1.6796420614424005e-11, 4.157908858124982e-12, 8.822392989557319e-13, 1.6379697854928112e-13, 2.703166838055595e-14, 4.014970188811204e-15, 5.421245989267469e-16, 6.71007449691175e-17, 7.666435100811014e-18, 8.133451886051172e-19, 7.220863223327139e-20, 5.937438757490859e-21], [3.203149711314576e-11, 4.7575867017064805e-11, 3.533183470054708e-11, 1.7492601768862096e-11, 6.495369952567007e-12, 1.9294936855333145e-12, 4.776409850016314e-13, 1.0134749513253951e-13, 1.8816225377737225e-14, 3.105270738750304e-15, 4.612208639418725e-16, 6.227672040453424e-17, 7.708217523518683e-18, 8.806839538694825e-19, 9.343326424112019e-20, 9.251661552177874e-21, 7.700257174712132e-22]] |
| Legacy trial inputs | {"lambda_home": 1.8380046366558418, "lambda_away": 1.4852839019359982, "rho": -0.10285334743314112, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.4941 |
| Legacy p draw | 0.2418 |
| Legacy p away | 0.2640 |
| Legacy p over 1 5 | 0.8553 |
| Legacy p under 3 5 | 0.5734 |
| Legacy p btts yes | 0.6586 |
| Legacy p over 2 5 | 0.6474 |
| Legacy goal margin distribution | {"-1": 0.13790709465425124, "-10": 5.775567850910843e-07, "-11": 7.643115330618942e-08, "-12": 9.299781804720097e-09, "-13": 1.0469840569939838e-09, "-14": 1.095913074403825e-10, "-15": 1.0607842439899404e-11, "-16": 8.412008730969915e-13, "-2": 0.07904069420217813, "-3": 0.03255385464090703, "-4": 0.010737898251186859, "-5": 0.0029380357000521663, "-6": 0.0006847909345559446, "-7": 0.0001387763208960874, "-8": 2.4850157667714745e-05, "-9": 3.9831096768291775e-06, "0": 0.24183471213095745, "1": 0.2175197360553125, "10": 6.124201075870583e-06, "11": 1.00291076438204e-06, "12": 1.5100862997417117e-07, "13": 2.1038084999859472e-08, "14": 2.725080736440175e-09, "15": 3.2641300572135475e-10, "16": 3.203149711314576e-11, "2": 0.15240824716684204, "3": 0.07767786331653026, "4": 0.031706716100720095, "5": 0.010735596418729681, "6": 0.0030964511946913473, "7": 0.0007765308876231939, "8": 0.00017207177653031906, "9": 3.413028286617115e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4507 |
| Legacy raw p draw | 0.2460 |
| Legacy raw p away | 0.3032 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.8380 |
| Legacy lambda away | 1.4853 |
| Legacy model home team | Chelsea |
| Legacy model away team | Man United |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.966170897129066, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.8075 |
| Elo away rating | 1,504.9896 |
| Elo rating diff | 42.8180 |
| Elo home expectancy | 0.5613 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **40.0%**. Expected goals are 1.03 for Coventry City and 1.17 for Sunderland (2.20 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 47.7%; Under 3.5 goals: 73.7%; Double Chance 1X: 60.0%; Double Chance X2: 69.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.7% | 3.25 |
| Draw | 29.3% | 3.42 |
| Sunderland win | 40.0% | 2.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.03 |
| Sunderland expected goals | 1.17 |
| Expected total goals | 2.20 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 74.1% |
| Under 1.5 | 25.9% |
| Over 2.5 | 47.7% |
| Under 2.5 | 52.3% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.97% |
| 2 | 0-1 | 9.41% |
| 3 | 0-0 | 8.71% |
| 4 | 1-2 | 8.71% |
| 5 | 1-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.7% | 30.6% | 3.16 | -2.9% |
| Draw | 29.3% | 28.5% | 3.38 | -1.0% |
| Sunderland win | 40.0% | 40.9% | 2.38 | -4.8% |
| Over 2.5 | 47.7% | 47.7% | 2.03 | -3.1% |
| Under 2.5 | 52.3% | 52.3% | 1.86 | -2.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | d20fbb0cd5ad9369b8ed6f2c4a198619 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Coventry |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8796 |
| Dc lambda away | 1.1504 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3943 |
| Shot lambda away | 1.2078 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.47 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.86 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.80 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.26 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.20925344349281813, "-10": 5.934603680299275e-07, "-11": 7.33890786203184e-08, "-12": 8.333005539964777e-09, "-13": 8.697461468719682e-10, "-14": 7.64036037007509e-11, "-2": 0.12077756817233894, "-3": 0.04908882903629288, "-4": 0.015656221918770283, "-5": 0.0040924655977557095, "-6": 0.0009043712919362227, "-7": 0.00017288821394303525, "-8": 2.910099361027317e-05, "-9": 4.373431492038237e-06, "0": 0.292763384996305, "1": 0.17394396739922377, "10": 1.66169567754045e-07, "11": 1.8196848164649075e-08, "12": 1.8296641303460004e-09, "13": 1.6910918025976577e-10, "14": 1.3155079640329748e-11, "2": 0.08943475260962129, "3": 0.03218901365206426, "4": 0.009091110416347633, "5": 0.0021043596638866627, "6": 0.0004118003075369441, "7": 6.971243523472628e-05, "8": 1.0391007332624667e-05, "9": 1.3828565433891874e-06} |
| Raw goal margin distribution | {"-1": 0.21438770520284417, "-10": 1.601895682597723e-07, "-11": 1.6849048327349812e-08, "-12": 1.6210642187851543e-09, "-13": 1.3322880959758934e-10, "-2": 0.1107274983750149, "-3": 0.03935464616352868, "-4": 0.010857322211951749, "-5": 0.002439989692602969, "-6": 0.0004618395082420536, "-7": 7.543779813241858e-05, "-8": 1.0831313697338185e-05, "-9": 1.3868311726889702e-06, "0": 0.3105723939488633, "1": 0.18868886678885957, "10": 4.749893862318902e-08, "11": 4.424151778650136e-09, "12": 3.769292402925696e-10, "13": 2.7432331749682178e-11, "2": 0.08682912470268879, "3": 0.027328192887241094, "4": 0.006676403810136889, "5": 0.0013286568439655891, "6": 0.00022270034340325667, "7": 3.221245136735202e-05, "8": 4.095631491258648e-06, "9": 4.643744342352438e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 37.8% |
| Raw p over 1 5 | 65.6% |
| Raw p under 3 5 | 81.9% |
| Raw p btts yes | 45.4% |
| P home draw | 60.0% |
| P draw away | 69.3% |
| P home away | 70.7% |
| Raw p home draw | 62.2% |
| Raw p draw away | 68.9% |
| Raw p home away | 68.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1797 |
| Totals anchor target over 2 5 | 0.4772 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-10-28T15:54:44Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3838 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.22, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.16 |
| Reference draw odds | 3.38 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0055 |
| Raw ev home | -0.0169 |
| Raw edge prob draw | 0.0254 |
| Raw ev draw | 0.0497 |
| Raw edge prob away | -0.0309 |
| Raw ev away | -0.0996 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.1278214638057091, 0.13114718945229878, 0.08515738525971293, 0.03334820419827105, 0.009794535610662772, 0.0023013635698803793, 0.00045061471784726596, 7.562732184323171e-05, 1.110606275121392e-05, 1.4497362631819844e-06, 1.7031793821799006e-07, 1.8190267878704173e-08, 1.7808577781898538e-09, 1.609375086106703e-10], [0.10520426804690285, 0.13807164504473193, 0.07894934591763496, 0.030917094283151817, 0.009080506378518836, 0.0021335923831692083, 0.00041776455590319516, 7.011403150550114e-05, 1.0296422174711381e-05, 1.344049366736977e-06, 1.5790162860615529e-07, 1.6864183261503542e-08, 1.6510318668384107e-09, 1.4920503958259975e-10], [0.05547007960746179, 0.06516736755135391, 0.03408979183287492, 0.014331607081901825, 0.00420926521521635, 0.0009890259229562498, 0.00019365459810408283, 3.250133215179009e-05, 4.7729025116619494e-06, 6.230335634500525e-07, 7.319523879089161e-08, 7.81738561999221e-09, 7.653351824890433e-10, 6.916393831689141e-11], [0.017142089280345184, 0.0201388719943374, 0.011829776364230334, 0.004125527124377429, 0.0013008021736133175, 0.00030564172238200995, 5.984567597056409e-05, 1.0043986621594699e-05, 1.4749847406075632e-06, 1.9253797803952904e-07, 2.261974973046307e-08, 2.415830717841022e-09, 2.365138849710906e-10, 2.1373944548097456e-11], [0.003973104423701738, 0.004667683156965435, 0.0027418441262008967, 0.0010737245809217535, 0.0002808387757923404, 7.084005102319297e-05, 1.3870719960063176e-05, 2.3279430543868568e-06, 3.418643026506547e-07, 4.4625452578674046e-08, 5.242688113879624e-09, 5.599286968464226e-10, 5.4817959892611273e-11, 4.953941858964091e-12], [0.0007366924067879053, 0.000865481087915744, 0.000508392313154026, 0.00019908984546889992, 5.847369080424386e-05, 1.2235301330198673e-05, 2.5719067463470938e-06, 4.3164684053373e-07, 6.338842604089735e-08, 8.27444450441932e-09, 9.720984179554665e-10, 1.0382189223334963e-10, 1.0164337631696312e-11, 9.18559132097349e-13], [0.00011383115995755546, 0.00013373114104478593, 7.855501996030302e-05, 3.076267358897856e-05, 9.035152242532656e-06, 2.122935792550623e-06, 3.7017729354383763e-07, 6.669657525615631e-08, 9.794560114417516e-09, 1.2785385152118752e-09, 1.5020528172843386e-10, 1.6042199312789947e-11, 1.5705582576329318e-12, 1.4193257665318902e-13], [1.5076111461629818e-05, 1.7711719612045564e-05, 1.0404042594608348e-05, 4.0742929796912205e-06, 1.1966403780125563e-06, 2.8116744700054583e-07, 5.5053530635566884e-08, 8.228322458880653e-09, 1.297218442275841e-09, 1.69333152455867e-10, 1.9893600050353104e-11, 2.1246729368257627e-12, 2.0800904917323207e-13, 1.879794026923441e-14], [1.7471314074037902e-06, 2.0525651917665755e-06, 1.205697478906938e-06, 4.721592332280203e-07, 1.386755459532312e-07, 3.258376529282362e-08, 6.3800107014774885e-09, 1.0707664520790086e-09, 1.4003253017790913e-10, 1.9623579311104173e-11, 2.3054176498204343e-12, 2.4622282926447936e-13, 2.410562854749983e-14, 2.178444483013223e-15], [1.7997379717829106e-07, 2.1143684439120252e-07, 1.2420013320556338e-07, 4.863760660287745e-08, 1.4285110138374054e-08, 3.3564870628877446e-09, 6.572114422058812e-10, 1.103007498206158e-10, 1.619794300733048e-11, 1.882961863306237e-12, 2.374834352824051e-13, 2.536366603389026e-14, 2.483145506215657e-15, 2.2440379921541695e-16], [1.668535679695324e-08, 1.9602293467166126e-08, 1.15145847298593e-08, 4.5091887410416255e-09, 1.3243714545091339e-09, 3.111796556315312e-10, 6.093002190414456e-11, 1.0225973972784778e-11, 1.5017100416361239e-12, 1.960265805185061e-13, 2.0508747168036644e-14, 2.351463513519015e-15, 2.302122275550731e-16, 2.080445884459413e-17], [1.406271033018692e-09, 1.6521155537195857e-09, 9.704693258820378e-10, 3.800423081212599e-10, 1.1162034088315732e-10, 2.622676524719332e-11, 5.13528873776549e-12, 8.618629590801554e-13, 1.2656674695334012e-13, 1.6521462815540043e-14, 1.940974751443285e-15, 1.8460836155994977e-16, 1.940268889644134e-17, 1.7534361528381904e-18], [1.0864606545979661e-10, 1.2763958752052345e-10, 7.497678003092532e-11, 2.936141079220095e-11, 8.62359429832267e-12, 2.0262344789458592e-12, 3.967435176137984e-13, 6.658604015229826e-14, 9.778327755929345e-15, 1.2764196149981426e-15, 1.4995634906057022e-16, 1.601561284773772e-17, 1.3963249004574185e-18, 1.3546744160113823e-19], [7.74812947219457e-12, 9.102658671541896e-12, 5.3469934380903e-12, 2.0939185541739336e-12, 6.149944303671796e-13, 1.445015704660439e-13, 2.829389291472435e-14, 4.748605096349883e-15, 6.973446222268394e-16, 9.10282797264665e-17, 1.0694185774530815e-17, 1.1421586358940287e-18, 1.118192488544865e-19, 8.999064927476625e-21]] |
| Legacy trial inputs | {"lambda_home": 0.9270992254735781, "lambda_away": 1.1748201555237654, "rho": -0.10285334743314112, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T15:54:44Z", "over": 2.03, "under": 1.86, "bookmaker": "pinnacle", "event_id": "d20fbb0cd5ad9369b8ed6f2c4a198619", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Coventry City", "away_team": "Sunderland"}} |
| Legacy p home | 0.2902 |
| Legacy p draw | 0.3044 |
| Legacy p away | 0.4054 |
| Legacy p over 1 5 | 0.6358 |
| Legacy p under 3 5 | 0.8375 |
| Legacy p btts yes | 0.4272 |
| Legacy p over 2 5 | 0.3571 |
| Legacy goal margin distribution | {"-1": 0.22580242459687555, "-10": 1.8796883060653073e-07, "-11": 1.9910463683859474e-08, "-12": 1.9300628177724535e-09, "-13": 1.609375086106703e-10, "-2": 0.120603698813488, "-3": 0.043479974805877966, "-4": 0.012132176869659098, "-5": 0.0027531500564793553, "-6": 0.000525699537941831, "-7": 8.656996756609067e-05, "-8": 1.2525778923978653e-05, "-9": 1.6156967452349619e-06, "0": 0.30440188043236804, "1": 0.18333578931069863, "10": 1.8414543049257927e-08, "11": 1.5392576139773057e-09, "12": 1.177487241313385e-10, "13": 7.74812947219457e-12, "2": 0.07855920838498835, "3": 0.022350157315762197, "4": 0.004921356918392246, "5": 0.0008813143511528938, "6": 0.0001327985656548227, "7": 1.7257499650212254e-05, "8": 1.9704716469288422e-06, "9": 2.0057653637656178e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2748 |
| Legacy raw p draw | 0.3237 |
| Legacy raw p away | 0.4015 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9271 |
| Legacy lambda away | 1.1748 |
| Legacy model home team | Coventry |
| Legacy model away team | Sunderland |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.38433409336513, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,364.9791 |
| Elo away rating | 1,407.0794 |
| Elo rating diff | 17.8997 |
| Elo home expectancy | 0.5257 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **42.2%**. Expected goals are 1.75 for Hull City and 0.91 for Ipswich Town (2.66 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 51.3%; Under 3.5 goals: 70.6%; Double Chance 1X: 69.5%; Double Chance X2: 57.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 42.2% | 2.37 |
| Draw | 27.3% | 3.66 |
| Ipswich Town win | 30.5% | 3.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.75 |
| Ipswich Town expected goals | 0.91 |
| Expected total goals | 2.66 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.3% |
| Under 2.5 | 48.7% |
| Over 3.5 | 29.4% |
| Under 3.5 | 70.6% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.01% |
| 2 | 1-2 | 8.50% |
| 3 | 0-1 | 8.21% |
| 4 | 0-0 | 7.71% |
| 5 | 1-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 42.2% | 36.1% | 2.69 | +13.5% |
| Draw | 27.3% | 28.3% | 3.41 | -6.9% |
| Ipswich Town win | 30.5% | 35.7% | 2.72 | -17.0% |
| Over 2.5 | 51.3% | 51.3% | 1.89 | -2.9% |
| Under 2.5 | 48.7% | 48.7% | 1.99 | -3.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 1ec76c009147b63859f68c6b5a1dd77b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8158 |
| Dc lambda away | 0.7783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.6092 |
| Shot lambda away | 1.2179 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.97 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.95 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.40 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.97 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.19648850130331003, "-10": 2.1647273831587212e-08, "-11": 1.8666162937770867e-09, "-12": 1.478395860119119e-10, "-13": 1.082555582599599e-11, "-14": 7.368724535356173e-13, "-15": 4.66287853478225e-14, "-16": 2.520669341983053e-15, "-2": 0.0799956975088461, "-3": 0.02254494708065524, "-4": 0.004996592759167088, "-5": 0.0009087163694646829, "-6": 0.0001398229876304105, "-7": 1.862106118598179e-05, "-8": 2.184264296590374e-06, "-9": 2.288160642625647e-07, "0": 0.27303973088399625, "1": 0.17330162732065119, "10": 6.770806820006427e-06, "11": 1.1250167512832583e-06, "12": 1.7169648281793867e-07, "13": 2.422632781194233e-08, "14": 3.177579548229957e-09, "15": 3.87458271704665e-10, "16": 4.036021194017905e-11, "2": 0.1316345963077531, "3": 0.07148573075820265, "4": 0.03052887632883437, "5": 0.010698722946770026, "6": 0.0031721147678793558, "7": 0.0008140319780484648, "8": 0.00018399624082043734, "9": 3.714129130259647e-05} |
| Raw goal margin distribution | {"-1": 0.1209997103423058, "-10": 8.65188141762052e-09, "-11": 7.074038355134671e-10, "-12": 5.3115413349533745e-11, "-13": 3.686625622947961e-12, "-14": 2.3784122018093297e-13, "-15": 1.4276323497738357e-14, "-16": 7.384377837205572e-16, "-2": 0.04762417786355949, "-3": 0.012858747824689808, "-4": 0.0027194279734982976, "-5": 0.0004708623946575228, "-6": 6.887988516151425e-05, "-7": 8.712898952021452e-06, "-8": 9.70128254955482e-07, "-9": 9.642201934256825e-08, "0": 0.25082896717222103, "1": 0.24097091972530765, "10": 6.106295301629962e-06, "11": 9.62058274701628e-07, "12": 1.3919423840959047e-07, "13": 1.8616432297140575e-08, "14": 2.314308586954574e-09, "15": 2.676808159057428e-10, "16": 2.667973438828405e-11, "2": 0.17683203320502835, "3": 0.09200233563144064, "4": 0.037492505036435926, "5": 0.012509145075453894, "6": 0.0035260848697190616, "7": 0.0008594680733355291, "8": 0.00018440086303216302, "9": 3.531642567067461e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 25.1% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.2% |
| Raw p btts yes | 50.3% |
| P home draw | 69.5% |
| P draw away | 57.8% |
| P home away | 72.7% |
| Raw p home draw | 81.5% |
| Raw p draw away | 43.6% |
| Raw p home away | 74.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0560 |
| Totals anchor target over 2 5 | 0.5135 |
| Totals anchor reference over odds | 1.89 |
| Totals anchor reference under odds | 1.99 |
| Totals anchor reference last update utc | 2026-10-28T15:54:44Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4812 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.69 |
| Reference draw odds | 3.41 |
| Reference away odds | 2.72 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best over 2 5 last update utc | 2026-10-28T15:54:44Z |
| Market best under 2 5 last update utc | 2026-10-28T15:54:44Z |
| Home probability edge | +6.1% |
| Draw probability edge | -1.0% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.2036 |
| Raw ev home | 0.5183 |
| Raw edge prob draw | -0.0317 |
| Raw ev draw | -0.1447 |
| Raw edge prob away | -0.1719 |
| Raw ev away | -0.4975 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.08617041830037415, 0.07755668893039636, 0.04139935488701942, 0.0120244179183696, 0.0026193637558518295, 0.0004564755837362315, 6.629153042789526e-05, 8.251858049017146e-06, 8.987802170036539e-07, 8.70167258685428e-08, 7.582186828179047e-09, 6.00611356072792e-10, 4.361180247643413e-11, 2.9231589231346023e-12, 1.8193494955333112e-13, 1.0568579502540381e-14, 5.755570516536559e-16], [0.09249013088392848, 0.12755992833401356, 0.07398800389051617, 0.02148977157140368, 0.004681268495307104, 0.0008158029843115146, 0.0001184747449469377, 1.4747536697150304e-05, 1.606279961942976e-06, 1.5551435208765508e-07, 1.3550715224256496e-08, 1.0733992225500902e-09, 7.794204088698404e-11, 5.2242044439512075e-12, 3.251500848771284e-13, 1.888792961835169e-14, 1.028622728377751e-15], [0.09078434038365134, 0.07910477244360278, 0.045029382319765415, 0.01920302027616681, 0.00418312933364007, 0.0007289924509917969, 0.00010586771115134431, 1.3178234365028818e-05, 1.4353538647864108e-06, 1.389658911194802e-07, 1.2108768040802533e-08, 9.591775774145508e-10, 6.964813872243563e-11, 4.668290843888342e-12, 2.905504905878818e-13, 1.6878043316135994e-14, 9.19165801457319e-16], [0.05408258291169338, 0.04712476178504253, 0.02053103840216968, 0.007791354420006282, 0.002491998488515389, 0.0004342796842071049, 6.306813754241765e-05, 7.850615531979402e-06, 8.550774734043226e-07, 8.278558060350324e-08, 7.213506743097924e-09, 5.714069258898463e-10, 4.1491200147328194e-11, 2.7810217660176587e-12, 1.7308845259927746e-13, 1.0054687550458401e-14, 5.475708746335795e-16], [0.024163796548277692, 0.02105508085697612, 0.00917315350276363, 0.002664336960022786, 0.0007583199084927642, 0.00019403374190476872, 2.8178492265099872e-05, 3.5076112545002586e-06, 3.8204384827726097e-07, 3.698813590505456e-08, 3.222954599347736e-09, 2.5530142903906495e-10, 1.853803692292099e-11, 1.2425450215665101e-12, 7.73349556971851e-14, 4.4923783452148385e-15, 2.4465161421769817e-16], [0.008636999672592375, 0.0075258342001340225, 0.0032788110776266317, 0.0009523287205889328, 0.0002074524813842819, 4.723587115605082e-05, 1.0071994604885938e-05, 1.2537449235749092e-06, 1.3655604929026876e-07, 1.3220874338330285e-08, 1.1519985182680484e-09, 9.125380420321145e-11, 6.6261532418499945e-12, 4.4412975101034614e-13, 2.7642261666209152e-14, 1.6057356806187477e-15, 8.744718188947283e-17], [0.002572642203089486, 0.002241667177336798, 0.0009766363406295906, 0.0002836634422455573, 6.179240812506023e-05, 1.0768540836047938e-05, 2.043284820681395e-06, 3.734441616957832e-07, 4.067498770506132e-08, 3.938008634232412e-09, 3.4313767724196226e-10, 2.7181127334138576e-11, 1.9736855528911906e-12, 1.3228979789389032e-13, 8.233605609248308e-15, 4.7828916702118e-16, 2.6047275581588174e-17], [0.0006568241111504878, 0.0005723225132050165, 0.0002493460985678244, 7.242242551065897e-05, 1.577628769902408e-05, 2.7493280078088226e-06, 3.9927033948706905e-07, 6.49370131366823e-08, 1.038477585936758e-08, 1.0054173167867756e-09, 8.760685787787926e-11, 6.939643522862942e-12, 5.039038298491377e-13, 3.377505383826193e-14, 2.102130906258043e-15, 1.2211253341966044e-16, 6.6501585845178476e-18], [0.00014673267561720056, 0.00012785525417365807, 5.570322339945958e-05, 1.6178967990764964e-05, 3.5243786975630006e-06, 6.141922135417281e-07, 8.91958809260319e-08, 1.1102953019906922e-08, 1.580053582633796e-09, 2.2460742609704446e-10, 1.9571127856924597e-11, 1.5502970196323293e-12, 1.1257071102034808e-13, 7.545252883793275e-15, 4.696101850350354e-16, 2.7279599592768832e-17, 1.4856268913085477e-18], [2.9137485097047796e-05, 2.538889546853951e-05, 1.106128430380109e-05, 3.212743424282427e-06, 6.998545575799257e-07, 1.2196340313102737e-07, 1.7712098823717262e-08, 2.2047722280669466e-09, 2.401405416591798e-10, 3.037709757666598e-11, 3.886342587735858e-12, 3.078506959375543e-13, 2.2353762724783093e-14, 1.4983008558266339e-15, 9.325298342938552e-17, 5.417054676092587e-18, 2.9500880579732257e-19], [5.207386362912084e-06, 4.537446783479213e-06, 1.9768480652348183e-06, 5.741743406962348e-07, 1.2507644592610453e-07, 2.1797027441575946e-08, 3.165466805593374e-09, 3.940319761819928e-10, 4.291738211631157e-11, 4.155109340368806e-12, 4.730485943848414e-13, 5.501838990217589e-14, 3.995014627552809e-15, 2.677729878946086e-16, 1.6665965253818354e-17, 9.681239322295448e-19, 5.272331593242434e-20], [8.460477080336079e-07, 7.372021555435844e-07, 3.211798891348802e-07, 9.328650710797253e-08, 2.032125773467537e-08, 3.541378308364696e-09, 5.14295608023805e-10, 6.401865102905492e-11, 6.972817118567428e-12, 6.75083523489923e-13, 5.882328194534392e-14, 6.088073209049598e-15, 6.490728234176267e-16, 4.350526480905358e-17, 2.7077310425024086e-18, 1.572917730454791e-19, 8.565994050730379e-21], [1.2600313314942521e-07, 1.0979260446068326e-07, 4.783379465637929e-08, 1.3893297109084231e-08, 3.0264748900003808e-09, 5.274226952975062e-10, 7.65948035325378e-11, 9.534392130686044e-12, 1.0384719389636856e-12, 1.0054118495869138e-13, 8.760638149439823e-15, 6.939605786872646e-16, 6.583803405547374e-17, 6.47930326196029e-18, 4.032663782923576e-19, 2.3425695778341836e-20, 1.2757461295415378e-21], [1.7322306909443423e-08, 1.5093761109889978e-08, 6.575960858834221e-09, 1.9099839066877834e-09, 4.160652643148165e-10, 7.250754461886918e-11, 1.0529886529771528e-11, 1.310742539130895e-12, 1.4276414557280253e-13, 1.3821920291682157e-14, 1.204370549795867e-15, 9.540237473952525e-17, 6.927390700915527e-18, 6.06665963309912e-19, 5.5439129142574e-20, 3.2204523942946216e-21, 1.753834642210553e-22], [2.2112886170505128e-09, 1.926802377146649e-09, 8.394579006900327e-10, 2.438200462379447e-10, 5.3113040182188296e-11, 9.25599049273162e-12, 1.3441984571595063e-12, 1.673235598362437e-13, 1.822463553373354e-14, 1.7644448378936095e-15, 1.537445850253694e-16, 1.2178642625601528e-17, 8.843198704928308e-19, 5.9273118136614e-20, 4.820066594521063e-21, 4.111086218761367e-22, 2.238867259876799e-23], [2.634643804601665e-10, 2.2956921618003416e-10, 1.0001736273697795e-10, 2.904998331313792e-11, 6.3281627364504786e-12, 1.1028066539615446e-12, 1.6015476722501083e-13, 1.9935795666259934e-14, 2.1713774823351157e-15, 2.102250979303801e-16, 1.8317926267283386e-17, 1.4510265686076142e-18, 1.0536245020732462e-19, 7.062106333561675e-21, 4.395395506444179e-22, 3.336030407813227e-23, 2.6675024282572753e-24], [2.94286041106453e-11, 2.564256149978804e-11, 1.117180002487032e-11, 3.244842649507385e-12, 7.068469581864224e-13, 1.2318196628073782e-13, 1.7889064293493666e-14, 2.2268005916715688e-15, 2.4253983855730753e-16, 2.3481850450938508e-17, 2.0460868346086587e-18, 1.6207764543730305e-19, 1.1768838845931693e-20, 7.888274350964462e-22, 4.9095955226635154e-23, 2.851978178682801e-24, 2.0293152329572477e-25]] |
| Legacy trial inputs | {"lambda_home": 1.7871777010156928, "lambda_away": 0.8713482094963613, "rho": -0.10285334743314112, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-28T15:54:44Z", "over": 1.89, "under": 1.99, "bookmaker": "pinnacle", "event_id": "1ec76c009147b63859f68c6b5a1dd77b", "kickoff_utc": "2026-10-31T15:00:00Z", "home_team": "Hull City", "away_team": "Ipswich Town"}} |
| Legacy p home | 0.4699 |
| Legacy p draw | 0.2674 |
| Legacy p away | 0.2627 |
| Legacy p over 1 5 | 0.7438 |
| Legacy p under 3 5 | 0.7352 |
| Legacy p btts yes | 0.5061 |
| Legacy p over 2 5 | 0.4840 |
| Legacy goal margin distribution | {"-1": 0.17344420137959138, "-10": 8.728094177956246e-09, "-11": 6.833993560817907e-10, "-12": 4.9136856750137894e-11, "-13": 3.2657346222025e-12, "-14": 2.0174204497314012e-13, "-15": 1.1597202230918133e-14, "-16": 5.755570516536559e-16, "-2": 0.06753600941374698, "-3": 0.017501395196703125, "-4": 0.0035492806817606897, "-5": 0.0005890218083486963, "-6": 8.256052278677471e-05, "-7": 1.0004579470824483e-05, "-8": 1.0669937345818793e-06, "-9": 1.0156938054258374e-07, "0": 0.26735874898655193, "1": 0.19500891032959175, "10": 5.994386530754636e-06, "11": 9.62666544744066e-07, "12": 1.4196610899027655e-07, "13": 1.9352371491976558e-08, "14": 2.4520296332554173e-09, "15": 2.8910694195995453e-10, "16": 2.94286041106453e-11, "2": 0.14809921757243377, "3": 0.07871654688165962, "4": 0.03274233908719056, "5": 0.011144914092047332, "6": 0.003204009378866462, "7": 0.0007963356833484782, "8": 0.00017419480600489428, "9": 3.401043055040735e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5791 |
| Legacy raw p draw | 0.2522 |
| Legacy raw p away | 0.1688 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.7872 |
| Legacy lambda away | 0.8713 |
| Legacy model home team | Hull |
| Legacy model away team | Ipswich |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 9.82919620852559, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,403.0690 |
| Elo away rating | 1,376.0928 |
| Elo rating diff | 86.9763 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **58.7%**. Expected goals are 2.03 for Manchester City and 1.07 for Brighton and Hove Albion (3.09 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.7%; Double Chance 1X: 80.2%; Double Chance X2: 41.3%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 58.7% | 1.70 |
| Draw | 21.4% | 4.67 |
| Brighton and Hove Albion win | 19.8% | 5.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 2.03 |
| Brighton and Hove Albion expected goals | 1.07 |
| Expected total goals | 3.09 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 60.1% |
| Under 2.5 | 39.9% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.00% |
| 2 | 2-1 | 9.93% |
| 3 | 2-0 | 9.31% |
| 4 | 1-0 | 8.45% |
| 5 | 3-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 58.7% | 58.7% | 1.67 | -1.9% |
| Draw | 21.4% | 20.9% | 4.52 | -3.2% |
| Brighton and Hove Albion win | 19.8% | 20.4% | 4.63 | -8.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 7df53f9af95d5a4e13b504882078dab8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-28T15:54:44Z |
| Market best draw last update utc | 2026-10-28T15:54:44Z |
| Market best away last update utc | 2026-10-28T15:54:44Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1445 |
| Dc lambda away | 1.0540 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-28T15:54:19.274058+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.7466 |
| Shot lambda away | 1.0954 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.97 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.51 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.95 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.12363682638758403, "-10": 3.0861858848907196e-08, "-11": 2.944498288098261e-09, "-12": 2.581447812537475e-10, "-13": 2.093069764516947e-11, "-14": 1.5782734360435848e-12, "-15": 1.1118266512445877e-13, "-16": 7.303573113880787e-15, "-17": 4.0652063734708117e-16, "-2": 0.05357771889821846, "-3": 0.016369995731212113, "-4": 0.0039638383167961, "-5": 0.0007911711896482791, "-6": 0.000133981826302189, "-7": 1.967473320121559e-05, "-8": 2.548062636937098e-06, "-9": 2.949834834115686e-07, "0": 0.21405051497013106, "1": 0.2266946902264874, "10": 1.7636114678729232e-05, "11": 3.1953008430719664e-06, "12": 5.319654316465958e-07, "13": 8.190744531642673e-08, "14": 1.1728474762529526e-08, "15": 1.5689748611171998e-09, "16": 1.9571941117548314e-10, "17": 2.0687153234700217e-11, "2": 0.18105400603021657, "3": 0.10504904283733443, "4": 0.04830355328161804, "5": 0.018308519468976873, "6": 0.005887735203769985, "7": 0.0016418400391453318, "8": 0.00040378641612862635, "9": 8.876850772435429e-05} |
| Raw goal margin distribution | {"-1": 0.11594361341614094, "-10": 2.8941501785753877e-08, "-11": 2.761278991014586e-09, "-12": 2.4208190712734477e-10, "-13": 1.9628299975074132e-11, "-14": 1.4800665018685592e-12, "-15": 1.0426440341775907e-13, "-16": 6.849113507796679e-15, "-17": 3.812251818442542e-16, "-2": 0.05024388371293181, "-3": 0.015351384471270591, "-4": 0.0037171913164931107, "-5": 0.0007419411290209265, "-6": 0.00012564490312030167, "-7": 1.8450487019104967e-05, "-8": 2.3895112643138485e-06, "-9": 2.766283474278189e-07, "0": 0.22597650732071028, "1": 0.2268588048574363, "10": 1.764888226692895e-05, "11": 3.197614067162516e-06, "12": 5.323505456975913e-07, "13": 8.196674185375031e-08, "14": 1.1736965540612255e-08, "15": 1.5701107136157437e-09, "16": 1.9586110138844098e-10, "17": 2.0702129608937763e-11, "2": 0.1811850792871675, "3": 0.1051250926331173, "4": 0.04833852242806083, "5": 0.018321773841687893, "6": 0.005891997603957332, "7": 0.0016430286420712863, "8": 0.00040407873554113195, "9": 8.883277129784386e-05} |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 62.7% |
| Raw p btts yes | 57.7% |
| P home draw | 80.2% |
| P draw away | 41.3% |
| P home away | 78.6% |
| Raw p home draw | 81.4% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6011 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-28T15:54:18Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.57, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-28T15:54:44Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.67 |
| Reference draw odds | 4.52 |
| Reference away odds | 4.63 |
| Market reference 1x2 last update utc | 2026-10-28T15:54:44Z |
| Market reference home last update utc | 2026-10-28T15:54:44Z |
| Market reference draw last update utc | 2026-10-28T15:54:44Z |
| Market reference away last update utc | 2026-10-28T15:54:44Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.85 |
| Market reference over 2 5 last update utc | 2026-10-28T15:54:20Z |
| Market reference under 2 5 last update utc | 2026-10-28T15:54:20Z |
| Home probability edge | +0.0% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | 0.0006 |
| Raw ev home | -0.0182 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | -0.0176 |
| Raw ev away | -0.1381 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 240 |
| Legacy trial matrix | [[0.05017909473140396, 0.03931931968872641, 0.028635494232184464, 0.011064322190165522, 0.0032063151556381486, 0.0007433230305901713, 0.00014360439242177035, 2.37799572316138e-05, 3.445581028900325e-06, 4.4377347831521407e-07, 5.1440209521629656e-08, 5.42065077819567e-09, 5.236143839881719e-10, 4.668846561980352e-11, 3.8656537482076405e-12, 2.987260369874723e-13, 2.164185485822168e-14, 1.4756621707226654e-15], [0.0775391237192481, 0.10297398242436447, 0.0568470357305628, 0.021964835451377396, 0.0063651603404542454, 0.0014756410536060165, 0.0002850827005420045, 4.7207848673952536e-05, 6.8401497202831435e-06, 8.809768245490013e-07, 1.0211883912159189e-07, 1.0761048018673751e-08, 1.0394765794598104e-09, 9.268570159026918e-11, 7.674075920064187e-12, 5.930293907478618e-13, 4.2963298849517714e-14, 2.929476944421919e-15], [0.08738321857003892, 0.10129066498030655, 0.05371483890782209, 0.021802239130152615, 0.006318041769607003, 0.0014647175114153302, 0.00028297235473697595, 4.685838907775785e-05, 6.7895150053722685e-06, 8.74455328356915e-07, 1.0136289685169998e-07, 1.0681388563712987e-08, 1.031781777092926e-09, 9.199958881960551e-11, 7.617268004695814e-12, 5.886394467609275e-13, 4.2645259847765283e-14, 2.90779127437307e-15], [0.057824238548435845, 0.06702723555388872, 0.03884746620773281, 0.013733976306247859, 0.004180847998313486, 0.000969249887703165, 0.00018725175394871267, 3.100767758807083e-05, 4.4928367451258075e-06, 5.786547386822642e-07, 6.707503366696585e-08, 7.068212529178292e-09, 6.827626240469782e-10, 6.087903669969512e-11, 5.040587076085569e-12, 3.895213331063277e-13, 2.8219716768852296e-14, 1.9241774227352514e-15], [0.02869809516995334, 0.033265530739209556, 0.0192799474809724, 0.007449480320098377, 0.001975244389099794, 0.0004810374718116273, 9.293280448577915e-05, 1.5389070479091626e-05, 2.229789094182055e-06, 2.8718560206094233e-07, 3.328925288121205e-08, 3.5079447812167033e-09, 3.38854211577288e-10, 3.021418756080088e-11, 2.501636878465275e-12, 1.9331893629431753e-13, 1.400540911270777e-14, 9.54966778425922e-16], [0.011394262157988794, 0.013207712073658328, 0.007654890496720461, 0.002957733996117248, 0.0008571177858980123, 0.0001818131761835791, 3.689794500705207e-05, 6.1100606980397476e-06, 8.853131661064185e-07, 1.1402387574866855e-07, 1.3217130688494077e-08, 1.3927907840650162e-09, 1.3453832727172253e-10, 1.1996209919843577e-11, 9.932473304768278e-13, 7.675515142019687e-14, 5.5606932137836746e-15, 3.7915902644811833e-16], [0.0037699717628211964, 0.004369980335607217, 0.0025327415342897746, 0.0009786130503834673, 0.00028359096933554224, 6.574515870775167e-05, 1.1621638939260227e-05, 2.021610173729695e-06, 2.9291985660826247e-07, 3.7726601854471365e-08, 4.3730966332211664e-09, 4.608268490435999e-10, 4.4514132446564476e-11, 3.969135695809596e-12, 3.286315811831487e-13, 2.5395655242347288e-14, 1.8398432568077932e-15, 1.2545075789097767e-16], [0.0010691612193225793, 0.0012393232092903351, 0.000718283636428029, 0.0002775339413709558, 8.042619033750069e-05, 1.8645278657454528e-05, 3.6021269393637483e-06, 5.457777471005806e-07, 8.307185590714424e-08, 1.0699236540021044e-08, 1.24020698900178e-09, 1.3069015547515266e-10, 1.2624175224071278e-11, 1.1256439642436207e-12, 9.319967473250993e-14, 7.202189149577368e-15, 5.217781945239312e-16, 3.557774267552805e-17], [0.00026531166855263947, 0.0003075372568611897, 0.00017824162215266507, 6.886986895369491e-05, 1.9957707376717466e-05, 4.626813900313817e-06, 8.938654819771068e-07, 1.4801833407575523e-07, 1.962367650520713e-08, 2.655008662277248e-09, 3.0775656622785845e-10, 3.243067797996436e-11, 3.1326809579956377e-12, 2.7932782535725073e-13, 2.3127439309398525e-14, 1.787218602744295e-15, 1.2947892319854213e-16, 8.828593950088711e-18], [5.852170650582833e-05, 6.783570878665386e-05, 3.9316038965212114e-05, 1.5191123255113595e-05, 4.402215326604583e-06, 1.0205696817195575e-06, 1.9716635034307318e-07, 3.2649470532218006e-08, 4.730723237798529e-09, 5.574935956947795e-10, 6.788408343395145e-11, 7.153468329840719e-12, 6.909980122636184e-13, 6.16133512093344e-14, 5.10138593933513e-15, 3.9421968548212085e-16, 2.856009908441844e-17, 1.9473865843322824e-18], [1.1617699047817481e-05, 1.3466709985640012e-05, 7.804999814976509e-06, 3.0157339680214983e-06, 8.739255203210462e-07, 2.0260296781270134e-07, 3.9141362366359566e-08, 6.4815560816928235e-09, 9.391407417312137e-10, 1.2095659631565932e-10, 1.2828751962873006e-11, 1.420102850143411e-12, 1.371765696599996e-13, 1.2231450762739453e-14, 1.0127245104183818e-15, 7.826028901259766e-17, 5.669736167136137e-18, 3.8659418218223854e-19], [2.096672394575778e-06, 2.430367575923195e-06, 1.408585950141699e-06, 5.442563225394443e-07, 1.577193130783187e-07, 3.656421533417306e-08, 7.063930096816418e-09, 1.1697410695909765e-09, 1.69488851424428e-10, 2.182931020962641e-11, 2.5303546646341683e-12, 2.4397400960691825e-13, 2.4756565444235192e-14, 2.207437553193154e-15, 1.8276868040435141e-16, 1.4123811168534365e-17, 1.0232300954977342e-18, 6.976952547564675e-20], [3.468586036479531e-07, 4.020627666567546e-07, 2.3302646472012618e-07, 9.003790413370597e-08, 2.6091964030331384e-08, 6.0489243370137615e-09, 1.1686064718490468e-09, 1.9351366244800582e-10, 2.8039032941465926e-11, 3.611286187340206e-12, 4.1860392113698485e-13, 4.4111516884721067e-14, 3.898751880546198e-15, 3.6518280553579284e-16, 3.0235953618523746e-17, 2.3365431017163777e-18, 1.6927592648860926e-19, 1.1542175232654581e-20], [5.296783956074368e-08, 6.13979180382063e-08, 3.558484139326835e-08, 1.3749444904587716e-08, 3.984433282173953e-09, 9.237148810159362e-10, 1.7845473475229548e-10, 2.9550948189139347e-11, 4.281764911299004e-12, 5.514697498266731e-13, 6.392387301652815e-14, 6.7361504790649e-15, 6.506866846569389e-16, 5.308641750126159e-17, 4.6172507280734546e-18, 3.5680717974661623e-19, 2.5849669062397525e-20, 1.762574373175261e-21], [7.510820172200484e-09, 8.706202200367733e-09, 5.045917424187315e-09, 1.9496662314781907e-09, 5.649911742429945e-10, 1.30982430456502e-10, 2.5304815765897337e-11, 4.1903135866454225e-12, 6.071526899171352e-13, 7.819820773710211e-14, 9.06438168744107e-15, 9.551836608913834e-16, 9.226713261164723e-17, 8.227067438380483e-18, 6.232637560181227e-19, 5.0595126881728194e-20, 3.665473567520301e-21, 2.4993239797644682e-22], [9.940294359462648e-10, 1.1522338525021825e-09, 6.678086195647584e-10, 2.580311577067026e-10, 7.477450469738e-11, 1.7335043108534717e-11, 3.3489993324030896e-12, 5.545725973293795e-13, 8.035442628827694e-14, 1.0349245295024432e-14, 1.199637590754475e-15, 1.264150457462991e-16, 1.2211215777179808e-17, 1.0888221283121595e-18, 9.01509459684624e-20, 6.374320267354991e-21, 4.85111950394449e-22, 3.307763398526928e-23], [1.2333388242815262e-10, 1.4296304450879827e-10, 8.285813959976053e-11, 3.201513286888105e-11, 9.277622611035581e-12, 2.1508398960033954e-12, 4.155260146007313e-13, 6.880841657549702e-14, 9.969949587041949e-15, 1.284079280028137e-15, 1.4884464807992152e-16, 1.568490612592525e-17, 1.5151026684977478e-18, 1.3509525523314803e-19, 1.1185449614252803e-20, 8.643777360396199e-22, 5.72978650795501e-23, 4.104096793730364e-24], [1.4402458144578872e-11, 1.669467646864196e-11, 9.675856009952569e-12, 3.738604526666058e-12, 1.0834052144144443e-12, 2.511668405146084e-13, 4.8523535588502944e-14, 8.035183197128735e-15, 1.1642525055074106e-15, 1.4994985741813263e-16, 1.73815075939449e-17, 1.8316232290172534e-18, 1.769278833859007e-19, 1.5775906188310195e-20, 1.3061939405938878e-21, 1.0093871950936643e-22, 7.312724191122544e-24, 4.562313486984394e-25]] |
| Legacy trial inputs | {"lambda_home": 1.985194851872693, "lambda_away": 1.1591546596457831, "rho": -0.10285334743314112, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5712 |
| Legacy p draw | 0.2228 |
| Legacy p away | 0.2061 |
| Legacy p over 1 5 | 0.8330 |
| Legacy p under 3 5 | 0.6131 |
| Legacy p btts yes | 0.5987 |
| Legacy p over 2 5 | 0.6140 |
| Legacy goal margin distribution | {"-1": 0.1226694853709416, "-10": 6.329649862154692e-08, "-11": 6.557366538631437e-09, "-12": 6.243212594843824e-10, "-13": 5.498035567017591e-11, "-14": 4.503252576226003e-12, "-15": 3.445971271113631e-13, "-16": 2.45713318026436e-14, "-17": 1.4756621707226654e-15, "-2": 0.05798696814019845, "-3": 0.019097765179571947, "-4": 0.004998284561521251, "-5": 0.0010800578334233416, "-6": 0.0001982151385467465, "-7": 3.1565283861180845e-05, "-8": 4.4353401492168984e-06, "-9": 5.572877019857192e-07, "0": 0.22277113754605488, "1": 0.22605335317152, "10": 1.4295425283143938e-05, "11": 2.536346642725408e-06, "12": 4.135699990575049e-07, "13": 6.237494891875947e-08, "14": 8.749650768829092e-09, "15": 1.1466683364650157e-09, "16": 1.4002855889679457e-10, "17": 1.4402458144578872e-11, "2": 0.17695129932535827, "3": 0.0998085296600586, "4": 0.04473710133603396, "5": 0.016556008079077096, "6": 0.005203639406030037, "7": 0.0014191942000811222, "8": 0.00034152367502522885, "9": 7.349115918042838e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5551 |
| Legacy raw p draw | 0.2366 |
| Legacy raw p away | 0.2083 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9852 |
| Legacy lambda away | 1.1592 |
| Legacy model home team | Man City |
| Legacy model away team | Brighton |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.00920497334261621, "mu": 10.249093243279138, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,654.7730 |
| Elo away rating | 1,529.0307 |
| Elo rating diff | 185.7423 |
| Elo home expectancy | 0.7444 |

</details>


---
