# Ligue 1 — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,752 |
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
| Training sha256 | cb7a052e677118123498cf1ddc1199c7a85d2fa2e96e9cb3987850956e105e05 |
| Training as of utc | 2026-10-29T12:04:07.426807+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 118, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-29T12:04:07.426807+00:00', 'observations': 350, 'observations_sha256': '92b269fb1624102b58094cce481daaae31d2b99b17eeb4694b8c859ec9748df1', 'eligible_training_matches': 154, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 154, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 15, 'retrospective_eligible_training_matches': 154, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '1a85c01f470efd86f2d1d95a2700e7cd9c4de28619c6ff2bc9ae53f2909662ad', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 93, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-08-24T00:00:00+00:00', 'audit_origin_utc': '2025-09-27T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 28, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-10-29', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1750, 'tune_start_date': '2025-10-30', 'audit_start_date': '2026-04-30', 'training_shot_matches': 1462, 'tuning_matches': 187, 'audit_matches': 97, 'audit_matchdays': 32, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.879426841742805, 'audit_candidate_poisson_score': 0.8748055462464946, 'audit_gain': 0.004621295496310407, 'audit_gain_lower95': -0.0027905175658523153, 'audit_baseline_briers': [0.6035167061900473, 0.16831729334132228, 0.2150016623692741, 0.24570302359102236], 'audit_candidate_briers': [0.602201104775819, 0.1674077313623154, 0.21307301750233523, 0.2437098695771331], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1583.794 |
| Base scoring parameter | 0.208 |
| Home-advantage parameter | 0.192 |
| Dixon-Coles low-score adjustment | -0.056 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1752, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261029T120407426807Z_3770778614c605c6e7b52651fcd2ce661c1de0b58aa22a5209ec4de18e879a91.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 3.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 3.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 3, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 2} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'AVAILABLE': 5} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Le Havre vs Paris Saint Germain

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **77.1%**. Expected goals are 0.80 for Le Havre and 2.26 for Paris Saint Germain (3.06 combined). The most likely exact score is 0-2 at 9.3%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 73.2%; Under 3.5 goals: 47.6%; Double Chance 1X: 22.9%; Double Chance X2: 91.1%; Double Chance 12 (either team wins): 86.0%; Under 4.5 goals: 66.9%; BTTS Yes (both teams score): 58.5%; BTTS No (at least one team does not score): 41.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 8.9% | 11.21 |
| Draw | 14.0% | 7.15 |
| Paris Saint Germain win | 77.1% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 0.80 |
| Paris Saint Germain expected goals | 2.26 |
| Expected total goals | 3.06 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 89.6% |
| Under 1.5 | 10.4% |
| Over 2.5 | 73.2% |
| Under 2.5 | 26.8% |
| Over 3.5 | 52.4% |
| Under 3.5 | 47.6% |
| Over 4.5 | 33.1% |
| Under 4.5 | 66.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 9.28% |
| 2 | 1-2 | 9.11% |
| 3 | 0-3 | 8.61% |
| 4 | 1-3 | 8.45% |
| 5 | 0-1 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 8.9% | 7.9% | 10.64 | -5.1% |
| Draw | 14.0% | 11.9% | 7.28 | +1.8% |
| Paris Saint Germain win | 77.1% | 80.1% | 1.23 | -5.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | 9a9f6c78276f74f15f42b013b033aa5d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:03:55Z |
| Market best draw last update utc | 2026-10-29T12:03:55Z |
| Market best away last update utc | 2026-10-29T12:03:55Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Le Havre |
| Matched away-team name | Paris SG |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7974 |
| Dc lambda away | 2.2620 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:04:07.426807+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.5% |
| P btts no | 41.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.79 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.60 |
| Fair Over 2.5 odds | 1.37 |
| Fair Under 2.5 odds | 3.73 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.02 |
| Fair Under 4.5 odds | 1.49 |
| Goal margin distribution | {"-1": 0.20644243803659393, "-10": 0.00023629486541516803, "-11": 5.8618215783505945e-05, "-12": 1.3370246123505324e-05, "-13": 2.8217981722913543e-06, "-14": 5.540715325167492e-07, "-15": 1.0170123158702374e-07, "-16": 1.752330885707301e-08, "-17": 2.8436274165331294e-09, "-18": 4.327133732588188e-10, "-19": 5.5437750973844826e-11, "-2": 0.21215385192053876, "-3": 0.1637743880089529, "-4": 0.10125759646307465, "-5": 0.05193297291860954, "-6": 0.022689780373770875, "-7": 0.008619448942097138, "-8": 0.0028932709722822992, "-9": 0.0008693225735657899, "0": 0.1398760979594998, "1": 0.05931922465206596, "10": 5.899265652178678e-09, "11": 5.158716455252879e-10, "12": 4.147762285466857e-11, "13": 3.0857859551490345e-12, "14": 2.1358516335821201e-13, "15": 1.3819643822851903e-14, "16": 8.393674957714396e-16, "17": 4.8014688777404026e-17, "18": 2.5755331063057084e-18, "19": 1.1631556009859767e-19, "2": 0.022216285082790804, "3": 0.006045495432894473, "4": 0.0013175858445843638, "5": 0.00023820994256964077, "6": 3.668701571307538e-05, "7": 4.912776294840289e-06, "8": 5.813022327210045e-07, "9": 6.156859343326182e-08} |
| Raw goal margin distribution | {"-1": 0.23058690896039521, "-10": 5.3356247665135086e-05, "-11": 1.0825591734869827e-05, "-12": 2.0174976402074533e-06, "-13": 3.4762392993507466e-07, "-14": 5.5690271502524704e-08, "-15": 8.334266166940475e-09, "-16": 1.1649590059259287e-09, "-17": 1.4013816199673249e-10, "-2": 0.21057439308471074, "-3": 0.1394572252279508, "-4": 0.07266651567827462, "-5": 0.031080038996815332, "-6": 0.011248686330952981, "-7": 0.003524103109736235, "-8": 0.0009725356652944652, "-9": 0.00023970016824941448, "0": 0.18779196839647924, "1": 0.07820144355244663, "10": 1.5806627462999424e-09, "11": 1.13050106642006e-10, "12": 7.426732149382398e-12, "13": 4.510864528542226e-13, "14": 2.5473865322345115e-14, "15": 1.3438421947610424e-15, "16": 6.621508546771003e-17, "17": 2.807812555957271e-18, "2": 0.026165940244315674, "3": 0.006108536893748989, "4": 0.0011220078920707733, "5": 0.0001691642252446087, "6": 2.158212330599906e-05, "7": 2.3834517429494233e-06, "8": 2.3186152467109278e-07, "9": 2.0144518123122914e-08} |
| Unadjusted home-win probability | 11.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 70.0% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.4% |
| Raw p btts yes | 49.7% |
| P home draw | 22.9% |
| P draw away | 91.1% |
| P home away | 86.0% |
| Raw p home draw | 30.0% |
| Raw p draw away | 88.8% |
| Raw p home away | 81.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2309 |
| Totals anchor target over 2 5 | 0.7319 |
| Totals anchor reference over odds | 1.33 |
| Totals anchor reference under odds | 3.33 |
| Totals anchor reference last update utc | 2026-10-29T12:03:55Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6133 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.34, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.7, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 2.75, "market_key": "alternate_spreads", "opposite_price": 3.02, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -2.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:04:08Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 9.02, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:04:08Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.08, "price": 9.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 10.64 |
| Reference draw odds | 7.28 |
| Reference away odds | 1.23 |
| Market reference 1x2 last update utc | 2026-10-29T12:03:55Z |
| Market reference home last update utc | 2026-10-29T12:03:55Z |
| Market reference draw last update utc | 2026-10-29T12:03:55Z |
| Market reference away last update utc | 2026-10-29T12:03:55Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-29T12:03:25Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:03:25Z |
| Home probability edge | +1.0% |
| Draw probability edge | +2.1% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | 0.0323 |
| Raw ev home | 0.1895 |
| Raw edge prob draw | 0.0685 |
| Raw ev draw | 0.3671 |
| Raw edge prob away | -0.1008 |
| Raw ev away | -0.1385 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.038962781970894395, 0.099803599161412, 0.1226962581309, 0.09540154595159897, 0.05563406196286599, 0.025954706034288424, 0.01009044252086617, 0.0033624630582785786, 0.0009804216287387262, 0.00025410646988726585, 5.927356815809052e-05, 1.2569376507094244e-05, 2.4433058690860496e-06, 4.3840937718437386e-07, 7.304611924288683e-08, 1.1359291322644236e-08, 1.6560620454170987e-09, 2.27233852400546e-10, 2.9447326731596675e-11], [0.025734107426963505, 0.07176123226038139, 0.10217635116783147, 0.07944644775315846, 0.046329737667681184, 0.021614001915103365, 0.008402901719715859, 0.0028001196732910716, 0.0008164544392516967, 0.00021160932123553115, 4.936056736653006e-05, 1.046725505336429e-05, 2.0346837164652553e-06, 3.650891327971119e-07, 6.08297762695084e-08, 9.459546337280669e-09, 1.3790997352806848e-09, 1.8923092076147137e-10, 2.4522511467884346e-11], [0.012513128009407936, 0.029188463649335954, 0.03282719853983173, 0.03307985210112598, 0.019290741288932333, 0.008999621844472562, 0.0034987938916053924, 0.0011659117213864275, 0.00033995468471628606, 8.810972985778004e-05, 2.0552715877061544e-05, 4.3583477784415944e-06, 8.472000739713896e-07, 1.5201553824257263e-07, 2.5328256445045685e-08, 3.938758781931218e-09, 5.742285094675409e-10, 7.879182831683627e-11, 1.0210664862275483e-11], [0.00347347121304292, 0.008102313679097032, 0.00944983892596776, 0.0070852590329063365, 0.005354842889402785, 0.002498170511925159, 0.0009712167775894719, 0.00032364096316606685, 9.436671711608045e-05, 2.445804198757397e-05, 5.705149575321993e-06, 1.2098170444244281e-06, 2.3517101930188678e-07, 4.2197410241772514e-08, 7.030773566153076e-09, 1.0933449441156487e-09, 1.5939788962795248e-10, 2.1871521435390484e-11, 2.8343392985732623e-12], [0.0007231406642747622, 0.001686817634780934, 0.0019673584086586735, 0.0015297046257651702, 0.0008602014491166039, 0.0005200931784555026, 0.00020219725531727515, 6.737869028872863e-05, 1.964617131257848e-05, 5.091910554301093e-06, 1.1877529424149128e-06, 2.5187135504992024e-07, 4.8960165979656263e-08, 8.785062953257583e-09, 1.4637341020423624e-09, 2.2762307233190056e-10, 3.3184986637207086e-11, 4.553423814223084e-12, 5.900800315989279e-13], [0.00012044030613851138, 0.00028094234271364816, 0.00032766688519814005, 0.0002547749041514993, 0.0001485737223937532, 6.683817471746294e-05, 3.367629637478996e-05, 1.1222035333506053e-05, 3.2721032079002845e-06, 8.480663531831538e-07, 1.9782227036677293e-07, 4.194960207383377e-08, 8.154398819621091e-09, 1.4631671593210462e-09, 2.437874013518035e-10, 3.791100939308554e-11, 5.527015900559309e-12, 7.583804718179175e-13, 9.827883171702545e-14], [1.671628133060193e-05, 3.8992853713596265e-05, 4.5477896987366895e-05, 3.5360994257816845e-05, 2.062100489027723e-05, 9.620223675488717e-06, 3.6065046838010165e-06, 1.5575408744071545e-06, 4.541452900586446e-07, 1.1770574321293763e-07, 2.745636266572051e-08, 5.8223145760402695e-09, 1.1317741470529873e-09, 2.0307748006535056e-10, 3.383600487669335e-11, 5.2617858494405755e-12, 7.671115731489912e-13, 1.0525796329314796e-13, 1.3640421985770507e-14], [1.988660752838975e-06, 4.638804306282164e-06, 5.410300716515507e-06, 4.206738333193185e-06, 2.4531881402547717e-06, 1.1444747117263209e-06, 4.4493882072881374e-07, 1.429732668320893e-07, 5.402762112964379e-08, 1.4002922497050537e-08, 3.266359890047721e-09, 6.926545598904834e-10, 1.346420763571247e-10, 2.415921378710488e-11, 4.0253172102317864e-12, 6.259709801288186e-13, 9.125981122232234e-14, 1.252206614527655e-14, 1.6227396104900866e-15], [2.070092667567124e-07, 4.828754611365862e-07, 5.631842347470903e-07, 4.378996349922879e-07, 2.553641577154025e-07, 1.1913387970162702e-07, 4.631582279641139e-08, 1.5433935909615765e-08, 4.339495943010358e-09, 1.4576315816698869e-09, 3.4001111795314067e-10, 7.210174603884912e-11, 1.401554159576986e-11, 2.5148488118688136e-12, 4.190146373451001e-13, 6.516033135488734e-14, 9.499672872067096e-15, 1.3034821184619836e-15, 1.689187743183797e-16], [1.915430280827083e-08, 4.467984910145901e-08, 5.21107172553195e-08, 4.051829340630993e-08, 2.362851905083252e-08, 1.1023305585691036e-08, 4.285543872290976e-09, 1.4280823586688028e-09, 4.1639798201259813e-10, 1.0406835454910838e-10, 3.146079406728767e-11, 6.671482384681102e-12, 1.2968401461118957e-12, 2.3269574552992054e-13, 3.8770888716968943e-14, 6.029202158015498e-15, 8.789925862832845e-16, 1.2060953402404923e-16, 1.562983823858839e-17], [1.5950908364498638e-09, 3.7207523859822366e-09, 4.3395642434397625e-09, 3.3741953005506677e-09, 1.9676849945480446e-09, 9.179751360895241e-10, 3.5688230620137674e-10, 1.1892477146308392e-10, 3.467589564981254e-11, 8.987326651584116e-12, 2.0215435788487235e-12, 5.555733624899392e-13, 1.0799546473235115e-13, 1.937793586594934e-14, 3.2286786907613637e-15, 5.020869310472417e-16, 7.319885425860649e-17, 1.0043861394275227e-17, 1.301588055650911e-18], [1.2075685846456336e-10, 2.8168074130232504e-10, 3.285280895408157e-10, 2.5544452706358386e-10, 1.4896421756037833e-10, 6.949559927851495e-11, 2.7017888356994014e-11, 9.003237600850926e-12, 2.625149695196055e-12, 6.803884190417723e-13, 1.5870925816229672e-13, 3.245354609581212e-14, 8.175830963034424e-15, 1.4670127902608519e-15, 2.444281458951736e-16, 3.801065060615716e-17, 5.541542513746725e-18, 7.603737173524335e-19, 9.853713721108419e-20], [8.380108301833143e-12, 1.954766916486844e-11, 2.2798713096318922e-11, 1.772696664290554e-11, 1.033760145905199e-11, 4.822754217522598e-12, 1.8749480021036514e-12, 6.247935489677195e-13, 1.821763089400253e-13, 4.7216602943975066e-14, 1.1013873570534602e-14, 2.335569259814973e-15, 4.377882344007175e-16, 1.0180561351857306e-16, 1.6962467893439932e-17, 2.637807680266969e-18, 3.845638832848395e-19, 5.276730599240251e-20, 6.838136500742097e-21], [5.368158746812754e-13, 1.2521913491766694e-12, 1.4604478452540624e-12, 1.1355601575907422e-12, 6.622096480702402e-13, 3.0893765693766487e-13, 1.2010606730595715e-13, 4.0023241156794643e-14, 1.166991297814771e-14, 3.024617474609954e-15, 7.055305207812384e-16, 1.4961270307354054e-16, 2.908255594882461e-17, 5.0320135413633656e-18, 1.0865876324030491e-18, 1.68973596297526e-19, 2.463452618282039e-20, 3.3801863294164946e-21, 4.3803971197279595e-22], [3.1931284248167707e-14, 7.448378445849175e-14, 8.687145346459728e-14, 6.75462404953146e-14, 3.9390050670473394e-14, 1.837646128571835e-14, 7.144239125478775e-15, 2.3806924314027765e-15, 6.941585113850463e-16, 1.799125638396743e-16, 4.196689529384612e-17, 8.899374952006376e-18, 1.7299103928633327e-18, 3.1040278154109385e-19, 4.987123807044268e-20, 1.0051014115435657e-20, 1.4653293521351318e-21, 2.0106277699118407e-22, 2.6055806496582237e-23], [1.7727365459397877e-15, 4.135133612643441e-15, 4.822862718540239e-15, 3.749980368351558e-15, 2.1868266189129283e-15, 1.0202102819622706e-15, 3.9662838776664223e-16, 1.3216945629213544e-16, 3.8537759779519185e-17, 9.988247716989875e-18, 2.329885902139954e-18, 4.940686723036555e-19, 9.603983826005557e-20, 1.7232703530577122e-20, 2.871248158641621e-21, 4.305583854096827e-22, 8.135103098827852e-23, 1.116244902742571e-23, 1.446546278923222e-24], [9.226633854063294e-17, 2.1522297754212897e-16, 2.51017493458357e-16, 1.9517675030703873e-16, 1.1381865264323448e-16, 5.3099298637329887e-17, 2.0643478685154518e-17, 6.879077337753357e-18, 2.005790425293956e-18, 5.198623830451534e-19, 1.2126451722352801e-19, 2.5714992724383355e-20, 4.998624443426406e-21, 8.969175152192045e-22, 1.4944101832060665e-22, 2.3239346323270842e-23, 3.2670554574875402e-24, 5.809765152446976e-25, 7.528898131620973e-26], [4.519739832383935e-18, 1.054286839412237e-17, 1.229629116917082e-17, 9.560888040761362e-18, 5.5754970464483e-18, 2.6011112927939487e-18, 1.0112371897273466e-18, 3.3697706384870924e-19, 9.825523613493137e-20, 2.5465871488684484e-20, 5.9402386332759704e-21, 1.2596693305942174e-21, 2.4486158615834595e-22, 4.3936216436222894e-23, 7.320486905397362e-24, 1.1383978265225723e-24, 1.6596611351371668e-25, 2.1959532185900934e-26, 3.688090512496332e-27], [2.0910287428298984e-19, 4.877590671486704e-19, 5.688800510311652e-19, 4.423283737919449e-19, 2.5794680694125957e-19, 1.2033875130513395e-19, 4.6784242189956026e-20, 1.559002845989966e-20, 4.5457156940671375e-21, 1.178162266387909e-21, 2.748213433094241e-22, 5.82777963868885e-23, 1.1328364765676346e-23, 2.0326809689592166e-24, 3.386776473508193e-25, 5.266724776895465e-26, 7.67831615453638e-27, 1.053567627235371e-27, 1.316565570786993e-28]] |
| Legacy trial inputs | {"lambda_home": 0.8327584942225654, "lambda_away": 2.3326272717254026, "rho": -0.06159898497874209, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.0957 |
| Legacy p draw | 0.1516 |
| Legacy p away | 0.7527 |
| Legacy p over 1 5 | 0.8355 |
| Legacy p under 3 5 | 0.6017 |
| Legacy p btts yes | 0.5042 |
| Legacy p over 2 5 | 0.6285 |
| Legacy goal margin distribution | {"-1": 0.2409700278527543, "-10": 7.063172312058196e-05, "-11": 1.4763339792337162e-05, "-12": 2.8348505602798537e-06, "-13": 5.033419618280873e-07, "-14": 8.310235569110203e-08, "-15": 1.282001722554033e-08, "-16": 1.8555036310408456e-09, "-17": 2.5175636386843037e-10, "-18": 2.9447326731596675e-11, "-2": 0.22414550547057135, "-3": 0.15177289408036013, "-4": 0.0810910211336753, "-5": 0.03562318188484223, "-6": 0.013256205779764066, "-7": 0.004272992609886094, "-8": 0.00121384394070048, "-9": 0.0003080695902562588, "0": 0.1515672653514173, "1": 0.06606076937240464, "10": 1.9007462822520522e-09, "11": 1.4183476266792595e-10, "12": 9.723037551390938e-12, "13": 6.163233944444124e-13, "14": 3.6327254189117207e-14, "15": 2.0006981430248795e-15, "16": 1.0337808698578647e-16, "17": 5.007498899532606e-18, "18": 2.0910287428298984e-19, "2": 0.02285938826018975, "3": 0.005525893456441492, "4": 0.001054034395843059, "5": 0.00016530593435233647, "6": 2.196082726130683e-05, "7": 2.5271750360290323e-06, "8": 2.562947784462308e-07, "9": 2.3221991240153046e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1119 |
| Legacy raw p draw | 0.1838 |
| Legacy raw p away | 0.7043 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.8328 |
| Legacy lambda away | 2.3326 |
| Legacy model home team | Le Havre |
| Legacy model away team | Paris SG |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 21.8% |
| Market home draw odds | 4.47 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T12:04:08Z |
| Market reference home draw last update utc | 2026-10-29T12:04:08Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 91.1% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T12:04:08Z |
| Market reference draw away last update utc | 2026-10-29T12:04:08Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.1% |
| Market home away odds | 1.12 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T12:04:08Z |
| Market reference home away last update utc | 2026-10-29T12:04:08Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 4.47 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.12 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.59, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.28, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.0, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.0, "price": 1.81, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.45, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:04:08Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.45, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 89.6% |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 7.10 |
| Market reference over 1 5 last update utc | 2026-10-29T12:03:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 48.9% |
| Market under 3 5 odds | 1.97 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market reference under 3 5 odds | 1.97 |
| Market reference under 3 5 opposite odds | 1.89 |
| Market reference under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.8% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T12:04:08Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-29T12:04:08Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.29534949385133, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,379.4397 |
| Elo away rating | 1,704.9432 |
| Elo rating diff | -265.5035 |
| Elo home expectancy | 0.1782 |

</details>


---

## 2026-10-30 — Lille vs RC Lens

The model's most likely 1X2 outcome is **Lille win** at **38.3%**. Expected goals are 1.28 for Lille and 1.09 for RC Lens (2.37 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.9%; Under 3.5 goals: 65.9%; Double Chance 1X: 65.9%; Double Chance X2: 61.7%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 38.3% | 2.61 |
| Draw | 27.6% | 3.62 |
| RC Lens win | 34.1% | 2.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 1.28 |
| RC Lens expected goals | 1.09 |
| Expected total goals | 2.37 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 34.1% |
| Under 3.5 | 65.9% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.88% |
| 2 | 1-2 | 8.19% |
| 3 | 2-1 | 8.13% |
| 4 | 1-0 | 6.93% |
| 5 | 0-1 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 38.3% | 37.5% | 2.59 | -0.8% |
| Draw | 27.6% | 27.0% | 3.57 | -1.4% |
| RC Lens win | 34.1% | 35.5% | 2.73 | -6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:05:00+00:00 |
| Fixture id | 7932d9a82dcdb164a3e4ef5e03694ee3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:03:55Z |
| Market best draw last update utc | 2026-10-29T12:03:55Z |
| Market best away last update utc | 2026-10-29T12:03:55Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lille |
| Matched away-team name | Lens |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2816 |
| Dc lambda away | 1.0893 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:04:07.426807+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.85 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.97 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 2.94 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.76 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.18627088802682767, "-10": 3.9600645610384356e-07, "-11": 4.8085498377080754e-08, "-12": 5.365189610913608e-09, "-13": 5.534122459401836e-10, "-14": 5.266454882201171e-11, "-15": 4.163838391142051e-12, "-2": 0.09998945655986763, "-3": 0.038865464400324366, "-4": 0.011974104855225615, "-5": 0.0030412256247871975, "-6": 0.0006553900712924617, "-7": 0.00012247715283381205, "-8": 2.0186455600788896e-05, "-9": 2.97412829567409e-06, "0": 0.276167980007471, "1": 0.18581328485494303, "10": 1.6968703524496697e-06, "11": 2.4241450293494034e-07, "12": 3.182201190532715e-08, "13": 3.861796687211829e-09, "14": 4.323715306940544e-10, "15": 4.021894453387393e-11, "2": 0.11671211782659319, "3": 0.05337325445154763, "4": 0.019346435600127204, "5": 0.005781022078285979, "6": 0.0014657298296284998, "7": 0.00032226061554458784, "8": 6.248996809531952e-05, "9": 1.0831984069230207e-05} |
| Raw goal margin distribution | {"-1": 0.1840055262464897, "-10": 6.870957361519673e-08, "-11": 6.733768531494753e-09, "-12": 6.058107889735585e-10, "-13": 5.0170048224330014e-11, "-14": 3.549748291583482e-12, "-2": 0.08614314432431085, "-3": 0.028203904741223137, "-4": 0.007200002779412925, "-5": 0.0015009971123414786, "-6": 0.00026395225938273423, "-7": 4.00954881128175e-05, "-8": 5.357402292391326e-06, "-9": 6.386655577753546e-07, "0": 0.2916604149656316, "1": 0.21777995293222227, "10": 3.491387644700768e-07, "11": 4.025659910172148e-08, "12": 4.261024037168406e-09, "13": 4.151638979436488e-10, "14": 3.45597588127666e-11, "2": 0.11923860415721663, "3": 0.04593074442655713, "4": 0.0137951043822643, "5": 0.0033835318218479464, "6": 0.0007000255220963556, "7": 0.00012510713447872002, "8": 1.9667036009143827e-05, "9": 2.7583935680348263e-06} |
| Unadjusted home-win probability | 40.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.5% |
| Raw p btts yes | 48.7% |
| P home draw | 65.9% |
| P draw away | 61.7% |
| P home away | 72.4% |
| Raw p home draw | 69.3% |
| Raw p draw away | 59.9% |
| Raw p home away | 70.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.2460 |
| Totals anchor target over 2 5 | 0.5589 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.18 |
| Totals anchor reference last update utc | 2026-10-29T12:03:55Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4275 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.58, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.26, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.58, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.59 |
| Reference draw odds | 3.57 |
| Reference away odds | 2.73 |
| Market reference 1x2 last update utc | 2026-10-29T12:03:55Z |
| Market reference home last update utc | 2026-10-29T12:03:55Z |
| Market reference draw last update utc | 2026-10-29T12:03:55Z |
| Market reference away last update utc | 2026-10-29T12:03:55Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-29T12:03:25Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:03:25Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0258 |
| Raw ev home | 0.0385 |
| Raw edge prob draw | 0.0221 |
| Raw ev draw | 0.0412 |
| Raw edge prob away | -0.0480 |
| Raw ev away | -0.1609 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09743406677420602, 0.10193359535041849, 0.06195735341292819, 0.023179165281627622, 0.006503752261320395, 0.0014598901371192078, 0.00027308328162257474, 4.378478908727738e-05, 6.142702240954474e-06, 7.660253527937084e-07, 8.59744354022915e-08, 8.772085101106643e-09, 8.204418007815813e-10, 7.08321812320281e-11, 5.678436441456198e-12], [0.10749265037226521, 0.13316849026716507, 0.07719360201385327, 0.028879271970160218, 0.008103123132310975, 0.0018188991624231436, 0.00034023858342876497, 5.455212976154232e-05, 7.653285461010366e-06, 9.544025520583384e-07, 1.071168470605686e-07, 1.0929273263392532e-08, 1.022200826154838e-09, 8.825088398074441e-11, 7.074849692195954e-12], [0.07193672373397622, 0.08073778740042284, 0.04385262827725208, 0.017990560475176835, 0.005047901723432405, 0.0011330969635811256, 0.00021195419391071773, 3.3983661033380137e-05, 4.767671950399749e-06, 5.945522743166778e-07, 6.672924847082757e-08, 6.808473281388808e-09, 6.36787720954875e-10, 5.497655435649087e-11, 4.4073310217706075e-12], [0.0298756833865575, 0.03353080941837464, 0.018816560038208942, 0.006813460705165436, 0.0020964189891858544, 0.0004705808712585394, 8.802564338551937e-05, 1.4113585449122007e-05, 1.9800381541957796e-06, 2.4692055159377966e-07, 2.7712992703277476e-08, 2.8275932172392963e-09, 2.6446114513149547e-10, 2.2832039692442146e-11, 1.8303867531290146e-12], [0.009305641244323173, 0.010444135420833995, 0.005860959058316514, 0.0021926717530388216, 0.0005954734605443161, 0.00014657595301546626, 2.7418119513709277e-05, 4.3960822974755275e-06, 6.167398574490281e-07, 7.691051077398864e-08, 8.632009000981776e-09, 8.807352696859056e-10, 8.237403335061094e-11, 7.1116957394726024e-12, 5.701266224639422e-13], [0.0023188077835103, 0.002602501200080053, 0.0014604514752328604, 0.0005463765681630247, 0.00015330568627246202, 3.330711672616433e-05, 6.83212980904347e-06, 1.0954290607922004e-06, 1.53681099916275e-07, 1.9164793304843217e-08, 2.1509500670916235e-09, 2.1946427386780913e-10, 2.0526210357513773e-11, 1.7721138180247484e-12, 1.4206587327469889e-13], [0.0004815062709181973, 0.0005404159227090645, 0.00030326642367561765, 0.00011345646919254081, 3.183431150807174e-05, 7.145812989989124e-06, 1.2937464636173205e-06, 2.2746860083374077e-07, 3.1912267095839585e-08, 3.979617552932068e-09, 4.4665019373389274e-10, 4.557230869299838e-11, 4.262319229568444e-12, 3.679838933729865e-13, 2.9500336057041525e-14], [8.570227606332402e-05, 9.618747957053422e-05, 5.39777451143524e-05, 2.0193875409695472e-05, 5.666121332019206e-06, 1.271868041089286e-06, 2.379123535534764e-07, 3.692051353211711e-08, 5.6799964811233264e-09, 7.083236558839685e-10, 7.949831709174648e-11, 8.111318203608393e-12, 7.586411254538951e-13, 6.549666976625167e-14, 5.250702010381348e-15], [1.3347219953905353e-05, 1.4980179122560204e-05, 8.406460945386919e-06, 3.144981781065104e-06, 8.824382639277395e-07, 1.9807994929117418e-07, 3.705232414461481e-08, 5.940781831190954e-09, 8.066820559108642e-10, 1.1031389209140924e-10, 1.2381019185591262e-11, 1.263251726239843e-12, 1.1815030396660284e-13, 1.0200411211629113e-14, 8.177411133537483e-16], [1.847722538807087e-06, 2.0737812589971606e-06, 1.1637485119774397e-06, 4.353755869072461e-07, 1.2216035061953123e-07, 2.742119992440658e-08, 5.129338894063774e-09, 8.224121971119055e-10, 1.1537872744156974e-10, 1.3926180343959716e-11, 1.7139665249860737e-12, 1.7487826639714267e-13, 1.6356138608633925e-14, 1.4120940365048002e-15, 1.1320399987945208e-16], [2.3021054069578523e-07, 2.58375537934793e-07, 1.4499318406821303e-07, 5.4244101677933985e-08, 1.522014251439791e-08, 3.4164486975411305e-09, 6.390720767939e-10, 1.0246557726907037e-10, 1.4375209844148885e-11, 1.7926597709604579e-12, 1.9473618263435605e-13, 2.1788347231624603e-14, 2.0378360028122973e-15, 1.759349279069459e-16, 1.4104257253905348e-17], [2.607479893090515e-08, 2.926490759264147e-08, 1.642265427770481e-08, 6.14395865699645e-09, 1.7239095766995542e-09, 3.8696409198681286e-10, 7.238450443838428e-11, 1.160576451692879e-11, 1.628208270320148e-12, 2.0304562483559733e-13, 2.2788714358449044e-14, 2.2504839473204934e-15, 2.308155129078455e-16, 1.9927271167652908e-17, 1.5975188227863608e-18], [2.707248804201325e-09, 3.038465849542435e-09, 1.7051027420361682e-09, 6.379042373938114e-10, 1.7898708068423327e-10, 4.017703369740939e-11, 7.515412241635982e-12, 1.2049831024030426e-12, 1.69050772145759e-13, 2.1081467454115465e-14, 2.3660669391806157e-15, 2.414129322081489e-16, 2.1853855380299898e-17, 2.0689739998601454e-18, 1.6586440164458638e-19], [2.5946170443449906e-10, 2.912054211511147e-10, 1.6341640376683397e-10, 6.11365015447909e-11, 1.7154054313004634e-11, 3.8505517579598615e-12, 7.202742750192243e-13, 1.1548512610997314e-13, 1.6201762249867067e-14, 2.0204398905400547e-15, 2.2676296315773267e-16, 2.3136924380962236e-17, 2.163966683504836e-18, 1.808239689941853e-19, 1.5896381702681648e-20], [2.3090518197097058e-11, 2.5915516476076405e-11, 1.4543068901464129e-11, 5.440777877042055e-12, 1.5266068036195261e-12, 3.426757549050243e-13, 6.41000423953929e-14, 1.0277475867771338e-14, 1.4418585851463822e-15, 1.7980689736212476e-16, 2.0180528523981538e-17, 2.059045956735155e-18, 1.9257991152214278e-19, 1.6626231356800206e-20, 1.2900738247265356e-21]] |
| Legacy trial inputs | {"lambda_home": 1.2459150974280615, "lambda_away": 1.122344516258388, "rho": -0.06159898497874209, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3791 |
| Legacy p draw | 0.2819 |
| Legacy p away | 0.3390 |
| Legacy p over 1 5 | 0.6931 |
| Legacy p under 3 5 | 0.7849 |
| Legacy p btts yes | 0.4857 |
| Legacy p over 2 5 | 0.4261 |
| Legacy goal margin distribution | {"-1": 0.19936781817210614, "-10": 9.756389855295381e-08, "-11": 9.8510928683711e-09, "-12": 9.131000157840963e-10, "-13": 7.790703092422406e-11, "-14": 5.678436441456198e-12, "-2": 0.09638365415950255, "-3": 0.032507964844698284, "-4": 0.008549355562635221, "-5": 0.0018361715275376533, "-6": 0.00033265885968801907, "-7": 5.206124145002233e-05, "-8": 7.166745810348384e-06, "-9": 8.802223880424102e-07, "0": 0.28189875808884146, "1": 0.20940036503352807, "10": 2.6124321413881127e-07, "11": 2.928212196209146e-08, "12": 3.0129972942539036e-09, "13": 2.8537722091057544e-10, "14": 2.3090518197097058e-11, "2": 0.11190801284769654, "3": 0.041899596186552195, "4": 0.012232513253801326, "5": 0.0029164720835199685, "6": 0.0005865512017599713, "7": 0.00010190221261670174, "8": 1.5572321257360204e-05, "9": 2.123176131987047e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3830 |
| Legacy raw p draw | 0.2943 |
| Legacy raw p away | 0.3227 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2459 |
| Legacy lambda away | 1.1223 |
| Legacy model home team | Lille |
| Legacy model away team | Lens |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 64.5% |
| Market home draw odds | 1.50 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T12:03:41Z |
| Market reference home draw last update utc | 2026-10-29T12:03:41Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 62.8% |
| Market draw away odds | 1.54 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T12:03:41Z |
| Market reference draw away last update utc | 2026-10-29T12:03:41Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.7% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T12:03:41Z |
| Market reference home away last update utc | 2026-10-29T12:03:41Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.50 |
| Market reference dc draw away odds | 1.54 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.59, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.28, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.79, "price": 2.03, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.03, "price": 1.79, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.49, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.5% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-29T12:03:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.3% |
| Market under 3 5 odds | 1.47 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.78 |
| Market reference under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T12:03:41Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-29T12:03:41Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 8.924113546099875, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,569.6537 |
| Elo away rating | 1,580.6843 |
| Elo rating diff | 48.9694 |
| Elo home expectancy | 0.5700 |

</details>


---

## 2026-10-30 — Nice vs Rennes

The model's most likely 1X2 outcome is **Rennes win** at **40.1%**. Expected goals are 1.44 for Nice and 1.50 for Rennes (2.95 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.1%; Under 3.5 goals: 59.9%; Double Chance 1X: 59.9%; Double Chance X2: 65.3%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nice win | 34.7% | 2.89 |
| Draw | 25.2% | 3.97 |
| Rennes win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nice expected goals | 1.44 |
| Rennes expected goals | 1.50 |
| Expected total goals | 2.95 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.7% |
| Under 1.5 | 16.3% |
| Over 2.5 | 62.1% |
| Under 2.5 | 37.9% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.26% |
| 2 | 1-2 | 8.72% |
| 3 | 2-1 | 7.78% |
| 4 | 2-2 | 6.89% |
| 5 | 0-1 | 6.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nice win | 34.7% | 34.2% | 2.83 | -1.9% |
| Draw | 25.2% | 24.9% | 3.84 | -3.2% |
| Rennes win | 40.1% | 40.9% | 2.38 | -4.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T18:00:00+00:00 |
| Fixture id | a547720e6b4661d6319c4f11dbdf8e1f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:03:55Z |
| Market best draw last update utc | 2026-10-29T12:03:55Z |
| Market best away last update utc | 2026-10-29T12:03:55Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Nice |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4444 |
| Dc lambda away | 1.5037 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:04:07.426807+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.18 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.12 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.64 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.52 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.195538930354314, "-10": 2.02267998723489e-06, "-11": 2.960083045462671e-07, "-12": 3.982238552088668e-08, "-13": 4.953190263848808e-09, "-14": 5.668686556731722e-10, "-15": 5.288990806987075e-11, "-2": 0.12143496435124365, "-3": 0.055696385908426384, "-4": 0.02040685033624742, "-5": 0.006192681906576931, "-6": 0.0015992492248336303, "-7": 0.00035885653749214233, "-8": 7.111789139049732e-05, "-9": 1.2611553440669668e-05, "0": 0.2520691928867802, "1": 0.17430667419664733, "10": 1.2571567131030532e-06, "11": 1.767272413723218e-07, "12": 2.2838324379579395e-08, "13": 2.728722279695974e-09, "14": 2.999812647294671e-10, "15": 2.688573178446419e-11, "2": 0.10411351229146332, "3": 0.045869892763345646, "4": 0.016144107871575813, "5": 0.0047060247364868, "6": 0.0011674248770024394, "7": 0.00025163498356490783, "8": 4.7903405567934066e-05, "9": 8.160062106285394e-06} |
| Raw goal margin distribution | {"-1": 0.19534012917064297, "-10": 1.038909441787836e-06, "-11": 1.39751622893659e-07, "-12": 1.727416948576193e-08, "-13": 1.9739259891278325e-09, "-14": 2.0809361387565654e-10, "-15": 1.8222239089681804e-11, "-2": 0.11570787796934487, "-3": 0.04981244629139623, "-4": 0.016998889671518896, "-5": 0.004782468960846894, "-6": 0.0011416779430965507, "-7": 0.00023634615351815806, "-8": 4.315288411089331e-05, "-9": 7.043208058654259e-06, "0": 0.2581234971429772, "1": 0.18738902467889815, "10": 6.949464004220992e-07, "11": 8.979824275341335e-08, "12": 1.0662167876081489e-08, "13": 1.1703521750734136e-09, "14": 1.1851731817218275e-10, "15": 9.969242618597871e-12, "2": 0.10676715054268049, "3": 0.04415195673013738, "4": 0.014473381236433668, "5": 0.003911460675224371, "6": 0.0008969490631925555, "7": 0.0001783651774478359, "8": 3.128302344850656e-05, "9": 4.904635899926187e-06} |
| Unadjusted home-win probability | 35.8% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 79.9% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 60.1% |
| P home draw | 59.9% |
| P draw away | 65.3% |
| P home away | 74.8% |
| Raw p home draw | 61.6% |
| Raw p draw away | 64.2% |
| Raw p home away | 74.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0912 |
| Totals anchor target over 2 5 | 0.6213 |
| Totals anchor reference over odds | 1.57 |
| Totals anchor reference under odds | 2.51 |
| Totals anchor reference last update utc | 2026-10-29T12:03:55Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5673 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.75, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.75, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.83 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-29T12:03:55Z |
| Market reference home last update utc | 2026-10-29T12:03:55Z |
| Market reference draw last update utc | 2026-10-29T12:03:55Z |
| Market reference away last update utc | 2026-10-29T12:03:55Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-29T12:03:25Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:03:25Z |
| Home probability edge | +0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +2.2% |
| Under 2.5 probability edge | -2.2% |
| Raw edge prob home | 0.0160 |
| Raw ev home | 0.0126 |
| Raw edge prob draw | 0.0086 |
| Raw ev draw | -0.0088 |
| Raw edge prob away | -0.0246 |
| Raw ev away | -0.0859 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.07485897327819425, 0.09166451788671727, 0.06506268739461249, 0.028242402041888447, 0.00919459338028027, 0.0023947126679467385, 0.0005197482662586375, 9.669096561699587e-05, 1.5739350198972858e-05, 2.277378294676657e-06, 2.9656921336323856e-07, 3.5109469563983866e-08, 3.810078382135766e-09, 3.816642183161411e-10, 3.550130342530044e-11], [0.08427153446661029, 0.12537733069095852, 0.08730835692711937, 0.03789879909197514, 0.01233832896843594, 0.003213492044724561, 0.0006974560836618342, 0.00012975070160436592, 2.112081225047336e-05, 3.056039720642841e-06, 3.9796958549942596e-07, 4.711379475646997e-08, 5.112787322943507e-09, 5.121595361862494e-10, 4.763960105175053e-11], [0.061473674517142, 0.08005345153553006, 0.05159566793771613, 0.025428413816990177, 0.00827847167553075, 0.002156110680777865, 0.00046796210802061463, 8.705696783250445e-05, 1.4171128556147665e-05, 2.0504671525098524e-06, 2.670199465185232e-07, 3.1611267329310614e-08, 3.4304536006682546e-09, 3.4363634042481675e-10, 3.196406004001167e-11], [0.027497406636012123, 0.0358082110233208, 0.023315434681963728, 0.01001810167747895, 0.003702991626493726, 0.0009644364454749731, 0.00020932121718053608, 3.894091029683082e-05, 6.338799290270765e-06, 9.171816965427525e-07, 1.1943902991025235e-07, 1.413983918907196e-08, 1.5344548433857376e-09, 1.5370983208328278e-10, 1.4297644700139348e-11], [0.00922477033029027, 0.012012860958171015, 0.007821811450768587, 0.003395290796222864, 0.0010941582974479723, 0.00032354704665190227, 7.02226278756917e-05, 1.3063812114930289e-05, 2.1265266356418507e-06, 3.0769412598612693e-07, 4.006914666460847e-08, 4.743602578710074e-09, 5.147755822869781e-10, 5.156624103666402e-11, 4.7965428292478924e-12], [0.0024757647518702883, 0.003224038828555063, 0.0020992354706113234, 0.0009112358329438939, 0.0002966618400599709, 7.648122845887622e-05, 1.8846507897055785e-05, 3.5060954800142694e-06, 5.70722034254672e-07, 8.257964634334894e-08, 1.0753848323358425e-08, 1.2730988025456745e-09, 1.3815663654679853e-10, 1.3839464547514954e-11, 1.2873070268747225e-12], [0.0005537094589839391, 0.0007210623683667206, 0.0004694979746496487, 0.00020379961370925028, 6.634898038543227e-05, 1.7280453551661157e-05, 3.7125051082022756e-06, 7.841448707588871e-07, 1.2764306001959124e-07, 1.8469093747828122e-08, 2.4051184720292466e-09, 2.8473094976335583e-10, 3.08989924909378e-11, 3.0952223636930577e-12, 2.87908645948107e-13], [0.000106146998960915, 0.00013822882239762727, 9.000352119455756e-05, 3.906871561184247e-05, 1.271920686519197e-05, 3.31269089850517e-06, 7.189861957948786e-07, 1.3239929892723798e-07, 2.4469381079618802e-08, 3.540555146840317e-09, 4.610651015784273e-10, 5.458338364696047e-11, 5.92338684234764e-12, 5.93359133914051e-13, 5.5192553145780016e-14], [1.7804982477540463e-05, 2.318635274452785e-05, 1.5097093026399256e-05, 6.5533439823862005e-06, 2.1335059641803295e-06, 5.556671783354947e-07, 1.2060196466256213e-07, 2.2436092961832278e-08, 3.6151008484769954e-09, 5.938888802072463e-10, 7.733856006265508e-11, 9.155757571223024e-12, 9.93582484367058e-13, 9.952941755911884e-14, 9.257939002243298e-15], [2.6547452882749983e-06, 3.457114365513281e-06, 2.2509955642494505e-06, 9.771118326923693e-07, 3.181084234740981e-07, 8.285067538797107e-08, 1.798190466340026e-08, 3.3452496879936195e-09, 5.445395648534236e-10, 7.799200833445898e-11, 1.153127660683147e-11, 1.3651349729466325e-12, 1.4814439846898302e-13, 1.483996137840205e-14, 1.3803703528686545e-15], [3.5624327623223043e-07, 4.6391409123856576e-07, 3.0206364359478826e-07, 1.311197432239499e-07, 4.2687329543814044e-08, 1.1117825943084018e-08, 2.413012147899048e-09, 4.4890284349654193e-10, 7.307238079609013e-11, 1.0573082869470881e-11, 1.3629025665909078e-12, 1.8318900777773184e-13, 1.987966457615826e-14, 1.9913912208266375e-15, 1.8523346066066383e-16], [4.345880783269088e-08, 5.659377927141971e-08, 3.684932942192793e-08, 1.5995551646922193e-08, 5.207510078943974e-09, 1.356285138313243e-09, 2.943680294617888e-10, 5.476252806059194e-11, 8.914241381567394e-12, 1.2898308747977966e-12, 1.6796688051543555e-13, 1.9683129266931862e-14, 2.4251588176794623e-15, 2.4293367527081665e-16, 2.2596988934573983e-17], [4.859822193313753e-09, 6.328652768515572e-09, 4.120711033373196e-09, 1.788717656206254e-09, 5.823347283475169e-10, 1.5166786537292345e-10, 3.291798265815107e-11, 6.123871373909091e-12, 9.968434539087697e-13, 1.442365546495365e-13, 1.8783054905996718e-14, 2.2236397603854382e-15, 2.3886161160506906e-16, 2.7166287467653485e-17, 2.5269296099673583e-18], [5.016500330410083e-10, 6.53268523856453e-10, 4.253560611514033e-10, 1.846384982091404e-10, 6.011088967789288e-11, 1.5655755838200112e-11, 3.397924127928832e-12, 6.321301798421677e-13, 1.0289811678255418e-13, 1.4888666607023302e-14, 1.9388610816190005e-15, 2.2953287484537363e-16, 2.4908899373830315e-17, 2.4698715019767463e-18, 2.6083965048689763e-19], [4.808356139848003e-11, 6.261631637125474e-11, 4.077072248676037e-11, 1.7697749387841848e-11, 5.761677392948452e-12, 1.5006168593716994e-12, 3.2569377588237205e-13, 6.059018900092127e-14, 9.862867716979603e-15, 1.4270907361462916e-15, 1.858414028122461e-16, 2.2000911698723905e-17, 2.387538151148137e-18, 2.3916512752871966e-19, 2.2020794973426512e-20]] |
| Legacy trial inputs | {"lambda_home": 1.3419113231149589, "lambda_away": 1.3022395710737458, "rho": -0.06159898497874209, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3564 |
| Legacy p draw | 0.2630 |
| Legacy p away | 0.3806 |
| Legacy p over 1 5 | 0.7492 |
| Legacy p under 3 5 | 0.7258 |
| Legacy p btts yes | 0.5423 |
| Legacy p over 2 5 | 0.4973 |
| Legacy goal margin distribution | {"-1": 0.2084474830317271, "-10": 3.472719680952893e-07, "-11": 4.0580190872052326e-08, "-12": 4.354201978362027e-09, "-13": 4.293038193678916e-10, "-14": 3.550130342530044e-11, "-2": 0.11227825459328804, "-3": 0.04295981638189674, "-4": 0.012917200010314727, "-5": 0.0031858832574609038, "-6": 0.0006646286518627706, "-7": 0.0001199865689595195, "-8": 1.9077078608278775e-05, "-9": 2.7085464558968428e-06, "0": 0.2630245617091375, "1": 0.19135039575151017, "10": 4.171481667126254e-07, "11": 5.02305144117457e-08, "12": 5.553861439656966e-09, "13": 5.64266349412263e-10, "14": 4.808356139848003e-11, "2": 0.10608471851705478, "3": 0.041826595992415186, "4": 0.012959594674532985, "5": 0.003293713512259596, "6": 0.0007080565634153158, "7": 0.0001317208296493749, "8": 2.1580754354473415e-05, "9": 3.1573590380982354e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3709 |
| Legacy raw p draw | 0.2766 |
| Legacy raw p away | 0.3525 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.3419 |
| Legacy lambda away | 1.3022 |
| Legacy model home team | Nice |
| Legacy model away team | Rennes |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 59.6% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-29T12:03:41Z |
| Market reference home draw last update utc | 2026-10-29T12:03:41Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 65.6% |
| Market draw away odds | 1.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-29T12:03:41Z |
| Market reference draw away last update utc | 2026-10-29T12:03:41Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.29 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-29T12:03:41Z |
| Market reference home away last update utc | 2026-10-29T12:03:41Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.62 |
| Market reference dc draw away odds | 1.47 |
| Market reference dc home away odds | 1.29 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.74, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.74, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.14, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-29T12:03:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.14, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.1% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-29T12:03:54Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.6% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.42 |
| Market reference under 3 5 last update utc | 2026-10-29T12:03:55Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.5% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-29T12:03:41Z |
| Market reference btts yes odds | 1.49 |
| Market reference btts yes opposite odds | 2.73 |
| Market reference btts yes last update utc | 2026-10-29T12:03:41Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 10.005751152964043, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,480.4127 |
| Elo away rating | 1,532.6617 |
| Elo rating diff | 7.7510 |
| Elo home expectancy | 0.5112 |

</details>


---

## 2026-10-31 — Lyon vs Angers

The model's most likely 1X2 outcome is **Lyon win** at **69.5%**. Expected goals are 2.06 for Lyon and 0.74 for Angers (2.80 combined). The most likely exact score is 2-0 at 13.3%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.9%; Double Chance 1X: 88.0%; Double Chance X2: 30.5%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 69.5% | 1.44 |
| Draw | 18.5% | 5.42 |
| Angers win | 12.0% | 8.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 2.06 |
| Angers expected goals | 0.74 |
| Expected total goals | 2.80 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 13.26% |
| 2 | 1-0 | 12.35% |
| 3 | 2-1 | 9.84% |
| 4 | 3-0 | 9.09% |
| 5 | 1-1 | 8.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 69.5% | 70.4% | 1.40 | -2.7% |
| Draw | 18.5% | 17.5% | 5.29 | -2.3% |
| Angers win | 12.0% | 12.1% | 7.55 | -9.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 961df571fad52d969150e9ced52b16f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:03:55Z |
| Market best draw last update utc | 2026-10-29T12:03:55Z |
| Market best away last update utc | 2026-10-29T12:03:55Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lyon |
| Matched away-team name | Angers |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0579 |
| Dc lambda away | 0.7419 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:04:07.426807+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.91 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.42 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.08552080406908727, "-10": 9.863041015149187e-10, "-11": 6.577136982006388e-11, "-12": 4.027412067757067e-12, "-13": 2.2795336833917106e-13, "-14": 1.1993774913371672e-14, "-15": 5.894455937194489e-16, "-16": 2.7087099540188504e-17, "-17": 1.0847442593654288e-18, "-2": 0.02744661224907993, "-3": 0.006068154002378636, "-4": 0.0010491992192194568, "-5": 0.0001483933793883072, "-6": 1.772220304811795e-05, "-7": 1.8295255935632896e-06, "-8": 1.6620698325444543e-07, "-9": 1.3476110306260639e-08, "0": 0.18466295783681802, "1": 0.2502960659537061, "10": 2.6978219595708633e-05, "11": 4.9899210931801135e-06, "12": 8.47495113718682e-07, "13": 1.3304896319643063e-07, "14": 1.9416713374054278e-08, "15": 2.6467803142541946e-09, "16": 3.3735800425008614e-10, "17": 3.747228878632092e-11, "2": 0.21431690785814073, "3": 0.13142519399224226, "4": 0.06302811752590871, "5": 0.024725509380213347, "6": 0.008190355924746243, "7": 0.002345189284331283, "8": 0.0005909395043153874, "9": 0.0001328962292558647} |
| Raw goal margin distribution | {"-1": 0.08432307596509896, "-10": 9.72490805974467e-10, "-11": 6.485023467723172e-11, "-12": 3.971007726469564e-12, "-13": 2.2476085677861482e-13, "-14": 1.1825800799435014e-14, "-15": 5.811903444727332e-16, "-16": 2.6707741783582235e-17, "-17": 1.0695522987749694e-18, "-2": 0.02706221947812987, "-3": 0.005983168849735466, "-4": 0.001034505070757913, "-5": 0.0001463151140717698, "-6": 1.7474001679031536e-05, "-7": 1.8039028898921866e-06, "-8": 1.638792364904867e-07, "-9": 1.3287375924937283e-08, "0": 0.2061992058997982, "1": 0.24314743385133175, "10": 2.6207702624409296e-05, "11": 4.847405428864319e-06, "12": 8.232900557867874e-07, "13": 1.2924899100801612e-07, "14": 1.8862158351307578e-08, "15": 2.571186402498867e-09, "16": 3.277228218112971e-10, "17": 3.6402053800618493e-11, "2": 0.20819586587628358, "3": 0.12767159779705678, "4": 0.061227990054543366, "5": 0.024019331400829347, "6": 0.007956433585334237, "7": 0.002278209025012242, "8": 0.0005740618554597657, "9": 0.00012910061925647023} |
| Unadjusted home-win probability | 67.5% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 11.9% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 46.2% |
| P home draw | 88.0% |
| P draw away | 30.5% |
| P home away | 81.5% |
| Raw p home draw | 88.1% |
| Raw p draw away | 32.5% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5395 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.17, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.29 |
| Reference away odds | 7.55 |
| Market reference 1x2 last update utc | 2026-10-29T12:03:55Z |
| Market reference home last update utc | 2026-10-29T12:03:55Z |
| Market reference draw last update utc | 2026-10-29T12:03:55Z |
| Market reference away last update utc | 2026-10-29T12:03:55Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.46 |
| Market reference over 2 5 last update utc | 2026-10-29T12:03:25Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:03:25Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0284 |
| Raw ev home | -0.0547 |
| Raw edge prob draw | 0.0308 |
| Raw ev draw | 0.0908 |
| Raw edge prob away | -0.0024 |
| Raw ev away | -0.1048 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05376935928448006, 0.03641209940194284, 0.017298443372941705, 0.004760830836142912, 0.000982697247451007, 0.00016227316842539407, 2.2330191435798848e-05, 2.6338521170263158e-06, 2.71830623128348e-07, 2.4937496492154197e-08, 2.0589691173327356e-09, 1.5454470439592867e-10, 1.0633343971886118e-11, 6.753415826267842e-13, 3.9828361127836826e-14, 2.1922907827306513e-15, 1.1312931460651374e-16, 5.494437217868598e-18], [0.10820599688315118, 0.09046317364827076, 0.03679580082202747, 0.010126840861767721, 0.0020903113306785836, 0.0003451739012239641, 4.7498914132044825e-05, 5.602509763645557e-06, 5.782153486482969e-07, 5.3044955210283286e-08, 4.379666765773119e-09, 3.2873455943132435e-10, 2.261835926079003e-11, 1.4365300868653885e-12, 8.471955606248547e-14, 4.663257453066761e-15, 2.406392088380073e-16, 1.1687306952373892e-17], [0.12125006543419967, 0.10011034599328554, 0.0374144658651657, 0.010770484120231185, 0.002223167649292265, 0.0003671125154031501, 5.051785718474418e-05, 5.958594912910629e-06, 6.149656458216852e-07, 5.6416394367137524e-08, 4.658030277808628e-09, 3.4962831947852174e-10, 2.4055940304516524e-11, 1.5278332798958597e-12, 9.010417421378895e-14, 4.959645464206298e-15, 2.5593379148276e-16, 1.2430130546836454e-17], [0.08597099675749428, 0.07098211617420552, 0.029303259276967704, 0.007301048878136543, 0.0015763120463831285, 0.0002602970048580091, 3.581911911282317e-05, 4.224874783387725e-06, 4.360344825677451e-07, 4.000141063708378e-08, 3.302724039576837e-09, 2.479000321573276e-10, 1.7056594225430717e-11, 1.08329302323717e-12, 6.38873524845573e-14, 3.516580899108818e-15, 1.8146697965815257e-16, 8.813444422570105e-18], [0.04571757708135875, 0.03774680403841331, 0.015582860095349886, 0.004288672642839458, 0.0008014076597694955, 0.00013842050031373496, 1.904785800781255e-05, 2.2467000017861223e-06, 2.3187401354845327e-07, 2.1271913123474913e-08, 1.7563195327806669e-09, 1.318280496455449e-10, 9.070339889697877e-12, 5.760725612062445e-13, 3.397395717041136e-14, 1.870044135597702e-15, 9.650034247764784e-17, 4.686805317352516e-18], [0.019449320659484216, 0.01605836841062958, 0.006629311134467782, 0.0018245010947474996, 0.00037660069544338175, 5.629913162185699e-05, 8.103401840630963e-06, 9.55798437932078e-07, 9.864459864265891e-08, 9.049566617296726e-09, 7.471791804009456e-10, 5.608271857687881e-11, 3.858733560864413e-12, 2.4507466671060953e-13, 1.445331159835986e-14, 7.955602716194233e-16, 4.105349024200819e-17, 1.993875994861791e-18], [0.006895161158735173, 0.0056930028599039674, 0.002350219292685829, 0.0006468210022769188, 0.00013351224616205818, 2.2046927743519986e-05, 2.746549377780353e-06, 3.3884907242738563e-07, 3.497142224081774e-08, 3.208246773007114e-09, 2.6488950197877024e-10, 1.98824107832785e-11, 1.3679958409141553e-12, 8.688371961562259e-14, 5.123979109240023e-15, 2.8204153658334123e-16, 1.4554258027987856e-17, 7.068676873503746e-19], [0.00209525852506523, 0.0017299541665277934, 0.0007141699657787343, 0.00019655192794080457, 4.057086782043756e-05, 6.699482759382097e-06, 9.21906769858973e-07, 9.844180019420662e-08, 1.0626897457052377e-08, 9.749019996639573e-10, 8.049296810389724e-11, 6.0417428590102576e-12, 4.1569803546911555e-13, 2.6401682284595642e-14, 1.557042781703552e-15, 8.57050212959989e-17, 4.422657064441191e-18, 2.1479853971762699e-19], [0.0005571073195489813, 0.00045997671271944197, 0.00018989032168476288, 5.2261101156420385e-05, 1.0787369268675969e-05, 1.7813223703875767e-06, 2.4512536438156366e-07, 2.8912603000715456e-08, 2.7013931160419426e-09, 2.592162415083458e-10, 2.140223803719294e-11, 1.6064362126781546e-12, 1.105297582668308e-13, 7.0199310840159886e-15, 4.14001384631498e-16, 2.2788068448315153e-17, 1.1759382400692019e-18, 5.711268431727158e-20], [0.000131670228770622, 0.00010871377357231558, 4.487986644620178e-05, 1.23517155557054e-05, 2.5495543310930455e-06, 4.2100887170723547e-07, 5.7934461948430506e-08, 6.833385449935143e-09, 7.052497036277219e-10, 5.857212570121251e-11, 5.058338814937682e-12, 3.7967518323037797e-13, 2.6123294464587643e-14, 1.6591344241082432e-15, 9.784767694295375e-17, 5.385874643074839e-18, 2.779285994938739e-19, 1.3498369068005576e-20], [2.8007788952924043e-05, 2.3124683954135746e-05, 9.546469535268952e-06, 2.6273535462097727e-06, 5.42319856933367e-07, 8.955348324507374e-08, 1.2323333820430672e-08, 1.453540555847105e-09, 1.5001481384776478e-10, 1.3762223884295201e-11, 1.0286774071927928e-12, 8.076132700508984e-14, 5.556728540313018e-15, 3.529171873461712e-16, 2.0813338830953673e-17, 1.1456381730218561e-18, 5.911864535579024e-20, 2.871260083583374e-21], [5.4159840310949334e-06, 4.471717465103254e-06, 1.846040993926906e-06, 5.080624134318597e-07, 1.0487067329140802e-07, 1.7317333974469646e-08, 2.383014928221837e-09, 2.8107725505389785e-10, 2.9008995947263078e-11, 2.6612591559789825e-12, 2.1972736586062854e-13, 1.493076455343064e-14, 1.0745279854132433e-15, 6.824508190127057e-17, 4.024762930472046e-18, 2.215368753644997e-19, 1.1432021275406562e-20, 5.552276471357925e-22], [9.600356583489582e-07, 7.926552581974716e-07, 3.2722865702125947e-07, 9.005898665155544e-08, 1.8589343191704595e-08, 3.0696652773674562e-09, 4.2241249094088126e-10, 4.98236675096018e-11, 5.14212567141611e-12, 4.717339769059396e-13, 3.894880507959041e-14, 2.9234686022865694e-15, 1.8209908799947483e-16, 1.209710216204595e-17, 7.134282352884e-19, 3.926955817595552e-20, 2.026436564137251e-21, 9.841948142594334e-23], [1.5708519193612796e-07, 1.296976860081085e-07, 5.354256995369e-08, 1.4735841404122702e-08, 3.0416688357778213e-09, 5.022719261326255e-10, 6.911696106140604e-11, 8.152364243602697e-12, 8.413768707750283e-13, 7.718715618595012e-14, 6.372972158276225e-15, 4.783505930386027e-16, 3.291258936899021e-17, 1.892384063055458e-18, 1.1673421742028255e-19, 6.425455168952381e-21, 3.315743262821413e-22, 1.6103821764950456e-23], [2.3867033705855698e-08, 1.9705861547953346e-08, 8.135090940350766e-09, 2.238917743560098e-09, 4.621416680388184e-10, 7.631362856523576e-11, 1.0501415308259232e-11, 1.2386447747639585e-12, 1.2783617530467257e-13, 1.1727575563572431e-14, 9.68289495867346e-16, 7.26790958877305e-17, 5.000636088830563e-18, 3.175988192708127e-19, 1.695670350341167e-20, 9.762636006785869e-22, 5.037836809334664e-23, 2.44676440929865e-24], [3.3845304247701917e-09, 2.7944439504852963e-09, 1.1536189681223047e-09, 3.1749589475703545e-10, 6.553527159295344e-11, 1.082186420343817e-11, 1.4891821100177444e-12, 1.756494324907535e-13, 1.8128160794391774e-14, 1.663061140855721e-15, 1.373109578315286e-16, 1.0306459290601434e-17, 7.091289682009546e-19, 4.503797497170444e-20, 2.6561206621728594e-21, 1.3235706374816035e-22, 7.14404318792118e-24, 3.469701634302546e-25], [4.499556141447984e-10, 3.715067043662943e-10, 1.5336760677097636e-10, 4.220941826030541e-11, 8.71257151714207e-12, 1.4387102323597102e-12, 1.979789710213576e-13, 2.3351673157415535e-14, 2.4100441419757823e-15, 2.2109527854071355e-16, 1.8254773515321866e-17, 1.370189845486708e-18, 9.427498658588448e-20, 5.9875631608799374e-21, 3.5311734680944015e-22, 1.9436800378200335e-23, 9.080199167513959e-25, 4.6127868088756164e-26], [5.630046588545098e-11, 4.648458620778533e-11, 1.9190043287611755e-11, 5.281431852618941e-12, 1.0901560510756426e-12, 1.800178813414045e-13, 2.477201740267137e-14, 2.92186614998917e-15, 3.015555395516718e-16, 2.7664433547683126e-17, 2.2841191913993454e-18, 1.7144430300983175e-19, 1.1796109436745199e-20, 7.491907754430693e-22, 4.4183627257083466e-23, 2.4320196975318463e-24, 1.2550010411877099e-25, 5.5180514767309505e-27]] |
| Legacy trial inputs | {"lambda_home": 2.1271162976192186, "lambda_away": 0.8256518925147608, "rho": -0.06159898497874209, "max_goals": 17, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6857 |
| Legacy p draw | 0.1898 |
| Legacy p away | 0.1245 |
| Legacy p over 1 5 | 0.8016 |
| Legacy p under 3 5 | 0.6550 |
| Legacy p btts yes | 0.4963 |
| Legacy p over 2 5 | 0.5726 |
| Legacy goal margin distribution | {"-1": 0.08570157003306529, "-10": 2.4128776943783124e-09, "-11": 1.7875669609359266e-10, "-12": 1.2163593308082876e-11, "-13": 7.652069379384514e-13, "-14": 4.4756365816808917e-14, "-15": 2.445360122115495e-15, "-16": 1.2481662155888763e-16, "-17": 5.494437217868598e-18, "-2": 0.029928788513417227, "-3": 0.007256422436310555, "-4": 0.0013828550752667237, "-5": 0.0002161887513504489, "-6": 2.85894820529715e-05, "-7": 3.271922359328365e-06, "-8": 3.297908292740272e-07, "-9": 2.968443898402538e-08, "0": 0.18980860221963142, "1": 0.24230787395803827, "10": 3.2821944080885757e-05, "11": 6.264487775743498e-06, "12": 1.0981948237815729e-06, "13": 1.7798797202651499e-07, "14": 2.682012669496459e-08, "15": 3.7752271724240975e-09, "16": 4.964402003525837e-10, "17": 5.630046588545098e-11, "2": 0.20978000663888935, "3": 0.1310363445403328, "4": 0.06433393770038671, "5": 0.02591139612782951, "6": 0.008827917430388717, "7": 0.00260285046848961, "8": 0.000675894727364618, "9": 0.0001567341322006359} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6678 |
| Legacy raw p draw | 0.2042 |
| Legacy raw p away | 0.1281 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.1271 |
| Legacy lambda away | 0.8257 |
| Legacy model home team | Lyon |
| Legacy model away team | Angers |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.904724219664642, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.6014 |
| Elo away rating | 1,418.6457 |
| Elo rating diff | 222.9557 |
| Elo home expectancy | 0.7830 |

</details>


---

## 2026-10-31 — Troyes vs Le Mans FC

The model's most likely 1X2 outcome is **Le Mans FC win** at **36.9%**. Expected goals are 1.25 for Troyes and 1.78 for Le Mans FC (3.03 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.3%; Under 3.5 goals: 64.8%; Double Chance 1X: 63.1%; Double Chance X2: 63.4%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Troyes win | 36.6% | 2.73 |
| Draw | 26.5% | 3.77 |
| Le Mans FC win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Troyes expected goals | 1.25 |
| Le Mans FC expected goals | 1.78 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.3% |
| Under 2.5 | 42.7% |
| Over 3.5 | 35.2% |
| Under 3.5 | 64.8% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.30% |
| 2 | 2-1 | 9.37% |
| 3 | 1-0 | 7.57% |
| 4 | 1-2 | 7.16% |
| 5 | 2-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Troyes win | 36.6% | 41.1% | 2.37 | -13.3% |
| Draw | 26.5% | 27.4% | 3.51 | -7.0% |
| Le Mans FC win | 36.9% | 31.5% | 3.06 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T19:45:00+00:00 |
| Fixture id | 75cf0c0e471877a0bfa95d689d0f0325 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-29T12:03:55Z |
| Market best draw last update utc | 2026-10-29T12:03:55Z |
| Market best away last update utc | 2026-10-29T12:03:55Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Troyes |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2480 |
| Dc lambda away | 1.7833 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-29T12:04:07.426807+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.99 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.14 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.84 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.16342365345120416, "-10": 3.950825129713584e-06, "-11": 6.300253681675274e-07, "-12": 9.23255064278944e-08, "-13": 1.2513302490486e-08, "-14": 1.5767538017628624e-09, "-15": 1.842851968231737e-10, "-16": 1.803154413341824e-11, "-2": 0.11364906014439533, "-3": 0.05783951449505412, "-4": 0.02335835323386796, "-5": 0.007781713273350481, "-6": 0.002200576018062726, "-7": 0.0005397879976475329, "-8": 0.00011680048116832477, "-9": 2.2595499271617972e-05, "0": 0.2650539638500311, "1": 0.21134261992635062, "10": 2.0821789638133186e-07, "11": 2.3237335017498347e-08, "12": 2.3831315518589895e-09, "13": 2.260457243171802e-10, "14": 1.993362463602679e-11, "15": 1.6304627283164012e-12, "16": 1.1164811095327717e-13, "2": 0.10409067176319231, "3": 0.037073930985255424, "4": 0.010478141416948982, "5": 0.002442954025820123, "6": 0.00048347551044028577, "7": 8.299642082705105e-05, "8": 1.2568365671616888e-05, "9": 1.7015869785482551e-06} |
| Raw goal margin distribution | {"-1": 0.21865726520815731, "-10": 5.286117400604904e-06, "-11": 8.429601291248022e-07, "-12": 1.2352950333783392e-07, "-13": 1.6742524374594637e-08, "-14": 2.10966201598825e-09, "-15": 2.4656955284464824e-10, "-16": 2.4125810703838322e-11, "-2": 0.15205995068560113, "-3": 0.07738800224676362, "-4": 0.03125296448845272, "-5": 0.01041176174349134, "-6": 0.0029443224639199685, "-7": 0.0007222245058487714, "-8": 0.00015627648291982667, "-9": 3.0232282612749847e-05, "0": 0.24449742960010792, "1": 0.15121197712987947, "10": 1.4897629165673058e-07, "11": 1.6625909967661967e-08, "12": 1.7050892708852315e-09, "13": 1.6173179317862127e-10, "14": 1.4262162518988762e-11, "15": 1.1665677886988322e-12, "16": 7.988228595796e-14, "2": 0.07447506936165868, "3": 0.026525754276211684, "4": 0.0074969283566915, "5": 0.0017478912129053313, "6": 0.00034591833797191496, "7": 5.9382498865280365e-05, "8": 8.992447539255373e-06, "9": 1.2174559555209657e-06} |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.0% |
| Raw p btts yes | 59.9% |
| P home draw | 63.1% |
| P draw away | 63.4% |
| P home away | 73.5% |
| Raw p home draw | 50.6% |
| Raw p draw away | 73.8% |
| Raw p home away | 75.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5728 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-29T12:03:55Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-29T12:03:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.51 |
| Reference away odds | 3.06 |
| Market reference 1x2 last update utc | 2026-10-29T12:03:55Z |
| Market reference home last update utc | 2026-10-29T12:03:55Z |
| Market reference draw last update utc | 2026-10-29T12:03:55Z |
| Market reference away last update utc | 2026-10-29T12:03:55Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-29T12:03:25Z |
| Market reference under 2 5 last update utc | 2026-10-29T12:03:25Z |
| Home probability edge | -4.5% |
| Draw probability edge | -0.9% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | +5.1% |
| Under 2.5 probability edge | -5.1% |
| Raw edge prob home | -0.1488 |
| Raw ev home | -0.3794 |
| Raw edge prob draw | -0.0294 |
| Raw ev draw | -0.1418 |
| Raw edge prob away | 0.1781 |
| Raw ev away | 0.5105 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05118221713355881, 0.0566603351596387, 0.05314826336311896, 0.030242828254060047, 0.012906752774154496, 0.004406579061289514, 0.0012537325333473997, 0.0003057464583837929, 6.524181397292371e-05, 1.2374797407056669e-05, 2.112480346366901e-06, 3.278344369090369e-07, 4.6636709949805e-08, 6.124055700748228e-09, 7.467335702175671e-10, 8.498240087860403e-11, 9.066999530268635e-12], [0.06233517091338584, 0.11753524543069223, 0.0777013185251167, 0.044214194078442536, 0.018869322250055536, 0.006442298987420254, 0.0018329229358513318, 0.0004469930238076414, 9.538176128223847e-05, 1.8091617941306736e-05, 3.0883889309731687e-06, 4.792850489155941e-07, 6.818160416672966e-08, 8.953203219798865e-09, 1.0917042123550543e-09, 1.242419635535964e-10, 1.325570722330263e-11], [0.05092070907511182, 0.08692586521287181, 0.0690782810767067, 0.032319975856486605, 0.013793218496035124, 0.004709233133692012, 0.0013398417921723284, 0.0003267458344225418, 6.972277310589187e-05, 1.3224727200283972e-05, 2.2575703971309245e-06, 3.503508665530484e-07, 4.983982737796072e-08, 6.544670052986535e-09, 7.98020964108071e-10, 9.081918931487559e-11, 9.689742091820293e-12], [0.024814898204906417, 0.04236108522073037, 0.03615693939705904, 0.01915547396951033, 0.006721770358544293, 0.0022949236756181816, 0.00065293744504603, 0.00015923118054213343, 3.3977600638560905e-05, 6.444730743608231e-06, 1.1001688824202813e-06, 1.7073448597682472e-07, 2.428815830333147e-08, 3.189376662253475e-09, 3.888949967391941e-10, 4.425839660984362e-11, 4.722046648754163e-12], [0.009069676916883877, 0.015482689214684923, 0.013215116013243872, 0.007519765626497402, 0.002987905166696145, 0.0008387790316483797, 0.00023864420577523159, 5.8197916053736323e-05, 1.2418582484522298e-05, 2.355505357232468e-06, 4.021042615273861e-07, 6.240229613651482e-08, 8.877157056956688e-09, 1.1656955291144047e-09, 1.421384825314217e-10, 1.6176143653542105e-11, 1.7258760095250611e-12], [0.002651924297973286, 0.00452705428238107, 0.0038640281872463966, 0.00219873864997876, 0.0009383572175146778, 0.00029827763445597284, 6.977827034695645e-05, 1.701675474095491e-05, 3.631126107235712e-06, 6.887369801698756e-07, 1.1757310334594064e-07, 1.8246092654710053e-08, 2.5956325359775644e-09, 3.408430450198909e-10, 4.15605207281889e-11, 4.729816596055041e-12, 5.046367766891961e-13], [0.0006461735578372885, 0.0011030717484674503, 0.0009415173891821717, 0.0005357493716155254, 0.00022864213063214126, 7.80622084425273e-05, 2.067816893186689e-05, 4.146338929135654e-06, 8.847679692295646e-07, 1.678191286344787e-07, 2.8648114334590613e-08, 4.4458820398204194e-09, 6.324573864693861e-10, 8.305054681723669e-11, 1.012672554983118e-11, 1.1524772483613051e-12, 1.2296087850547076e-13], [0.00013495545765461223, 0.00023038013678328747, 0.00019663898128566108, 0.00011189300576850661, 4.775265562066866e-05, 1.630354714784504e-05, 4.638584077108335e-06, 1.0531976674006365e-06, 1.8478667961152422e-07, 3.5049573034010284e-08, 5.983252230107313e-09, 9.285369821856271e-10, 1.320907904738322e-10, 1.7345377906980636e-11, 2.1149997002264464e-12, 2.4069863677134955e-13, 2.5680781008525165e-14], [2.4662652028440018e-05, 4.210118839574365e-05, 3.59351067008104e-05, 2.0448067189304953e-05, 8.726635806167656e-06, 2.979417928881561e-06, 8.476855029543572e-07, 2.0672418833990885e-07, 4.106991501473059e-08, 6.405190560691993e-09, 1.0934190459134894e-09, 1.6968698328443852e-10, 2.413914381999332e-11, 3.1698089655363765e-12, 3.8650901974216773e-13, 4.398685926140308e-14, 4.693075603157585e-15], [4.0062364321885985e-06, 6.838977194949003e-06, 5.837350074653646e-06, 3.3216132493442746e-06, 1.4175671885081435e-06, 4.839809052017919e-07, 1.3769924422798054e-07, 3.358057251048786e-08, 7.165602101867742e-09, 1.2654141162305787e-09, 1.7761655203731133e-10, 2.7564196004483582e-11, 3.921197010847763e-12, 5.149082972166126e-13, 6.278507739049985e-14, 7.145288264513213e-15, 7.623499061943602e-16], [5.857008929485091e-07, 9.998399040437743e-07, 8.53404737600553e-07, 4.856108417714461e-07, 2.0724447550145012e-07, 7.075669475449784e-08, 2.0131255772791173e-08, 4.909388559069694e-09, 1.047591578933571e-09, 1.987028374168396e-10, 3.158104994458446e-11, 4.029810643106283e-12, 5.732683603563319e-13, 7.527819552617181e-14, 9.179007907770397e-15, 1.0446217510466887e-15, 1.114534871705817e-16], [7.784352807456979e-08, 1.328853457072484e-07, 1.1342314217065702e-07, 6.454089732465936e-08, 2.754416348211868e-08, 9.40403339127185e-09, 2.675577231983805e-09, 6.524902569347982e-10, 1.39231859584287e-10, 2.640892320496129e-11, 4.5082217836859685e-12, 6.51380995783973e-13, 7.619116214593832e-14, 1.0004970792079148e-14, 1.2199509482872505e-15, 1.3883714978740526e-16, 1.4812906659397237e-17], [9.483760439352182e-09, 1.6189564062163117e-08, 1.3818462950377268e-08, 7.863086680520788e-09, 3.3557349522561437e-09, 1.1457034650466519e-09, 3.2596844121468944e-10, 7.94935871849637e-11, 1.696276664847448e-11, 3.2174274128117486e-12, 5.49241490737546e-13, 8.523642605844634e-14, 1.1289286149794171e-14, 1.2189163125276129e-15, 1.4862793128073095e-16, 1.6914678730965066e-17, 1.804672291235747e-18], [1.0665384893045605e-09, 1.8206694810332342e-09, 1.554016752516487e-09, 8.842784086695365e-10, 3.773841093280773e-10, 1.288451823109657e-10, 3.665823183507419e-11, 8.939805146685348e-12, 1.907623419147178e-12, 3.618301194185081e-13, 6.176739633404543e-14, 9.585641651689059e-15, 1.36362364371328e-15, 1.6671461208324598e-16, 1.6714615506192693e-17, 1.9022154783601586e-18, 2.0295245451348085e-19], [1.1137502315329922e-10, 1.9012638328392923e-10, 1.6228073672708712e-10, 9.234221664494324e-11, 3.9408951796487305e-11, 1.3454868536841938e-11, 3.8280957136883146e-12, 9.335537490515643e-13, 1.9920669024690232e-13, 3.778470100415629e-14, 6.4501612138808174e-15, 1.0009962805863956e-15, 1.4239862547293765e-16, 1.8698941564378124e-17, 2.1228117579729918e-18, 1.9864195720031656e-19, 2.1193641436416168e-20], [1.0855150732647771e-11, 1.8530640805878735e-11, 1.5816668839233163e-11, 9.000120963278843e-12, 3.840987861144589e-12, 1.3113768412361737e-12, 3.731048022669572e-13, 9.098868288480321e-14, 1.9415651627794458e-14, 3.682680489534821e-15, 6.286640419385673e-16, 9.756195959330066e-17, 1.387886170405528e-17, 1.8224896702639586e-18, 2.2222433705078285e-19, 2.354630991866645e-20, 2.065635237169171e-21], [9.91870984279559e-13, 1.6932058695581723e-12, 1.4452212848975718e-12, 8.223707858458294e-13, 3.509637502297538e-13, 1.19824834340285e-13, 3.409181839833281e-14, 8.313936551780802e-15, 1.7740722321404538e-15, 3.364986826904301e-16, 5.744311041056142e-17, 8.914558560574313e-18, 1.2681574450807647e-18, 1.6652690207675414e-19, 2.0305371832240656e-20, 2.3108633625964097e-21, 2.2954972679935457e-22]] |
| Legacy trial inputs | {"lambda_home": 1.4619728587225256, "lambda_away": 1.7070827722498858, "rho": -0.06159898497874209, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3674 |
| Legacy p draw | 0.2603 |
| Legacy p away | 0.3723 |
| Legacy p over 1 5 | 0.8298 |
| Legacy p under 3 5 | 0.6115 |
| Legacy p btts yes | 0.6392 |
| Legacy p over 2 5 | 0.6082 |
| Legacy goal margin distribution | {"-1": 0.17431629491430473, "-10": 2.6449415905827152e-06, "-11": 4.029662869059225e-07, "-12": 5.643391840633131e-08, "-13": 7.311301149066912e-09, "-14": 8.806652758629837e-10, "-15": 9.823810810190666e-11, "-16": 9.066999530268635e-12, "-2": 0.11370718151283991, "-3": 0.05453632410108016, "-4": 0.020861261655068596, "-5": 0.00660270309186901, "-6": 0.0017773140615552534, "-7": 0.00041551819888770386, "-8": 8.577096516955744e-05, "-9": 1.583903379709409e-05, "0": 0.26025917414579247, "1": 0.19395901325293652, "10": 7.333297344352605e-07, "11": 9.568341191858982e-08, "12": 1.1476061741826012e-08, "13": 1.2733039122135686e-09, "14": 1.3135088524407554e-10, "15": 1.2548356602205943e-11, "16": 9.91870984279559e-13, "2": 0.10894147697747975, "3": 0.044748239803147676, "4": 0.014659373012004167, "5": 0.00397357417581583, "6": 0.0009160273981908166, "7": 0.00018340833444526586, "8": 3.2423063359307267e-05, "9": 5.127753785480155e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3242 |
| Legacy raw p draw | 0.2467 |
| Legacy raw p away | 0.4291 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4620 |
| Legacy lambda away | 1.7071 |
| Legacy model home team | Troyes |
| Legacy model away team | Le Mans |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Count model | {"corners": {"alpha": 0.015442826785551094, "mu": 9.88845497893048, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,390.3655 |
| Elo away rating | 1,409.0026 |
| Elo rating diff | 41.3628 |
| Elo home expectancy | 0.5592 |

</details>


---
