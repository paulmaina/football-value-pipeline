# Bundesliga — football model report

Fixtures in this report: **2**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,602 |
| Training data through | 2026-10-31 |
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
| Training sha256 | 42e1c02dabf9ac4d449e156a41a109c7298d50521993b971575ec7e2ca7daddf |
| Training as of utc | 2026-11-01T07:11:06.583192+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 64, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-01T07:11:06.583192+00:00', 'observations': 363, 'observations_sha256': 'a7d1b621253d8d4a3fc289448d3bcba403d71404007d411b27fd14028a609736', 'eligible_training_matches': 75, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 111, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 21, 'retrospective_eligible_training_matches': 75, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '878a9c1d69aa8c24cb7e65f8d509fa0b0aab63a7bace976f1a6ec9057fe87afc', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-11-01', 'selected_weight': 0.2, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1592, 'tune_start_date': '2025-11-02', 'audit_start_date': '2026-05-03', 'training_shot_matches': 1302, 'tuning_matches': 206, 'audit_matches': 78, 'audit_matchdays': 26, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.7307409848365726, 'audit_candidate_poisson_score': 0.7195456173296279, 'audit_gain': 0.01119536750694472, 'audit_gain_lower95': 0.0018640767408074723, 'audit_baseline_briers': [0.597547620009099, 0.16610067079309407, 0.2894101452518172, 0.25563709869937135], 'audit_candidate_briers': [0.593722815607305, 0.1632385342160329, 0.28689523973175785, 0.2537938886319943], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1591.565 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.225 |
| Dixon-Coles low-score adjustment | -0.075 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1602, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-31'} |
| Training data health | {'training_end': '2026-10-31', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 2.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 7.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261101T071106583192Z_fb23af67526d59741ebb088f51b6bc8bd375f527e6ed082360e37a76d1eca1e8.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2} |
| Shot features applied fixtures | 2 |
| Goal rate features used | {'shot_features': 2} |
| Legacy comparison status | {'AVAILABLE': 2} |
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

## 2026-11-01 — Eintracht Frankfurt vs Hamburger SV

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **61.0%**. Expected goals are 2.01 for Eintracht Frankfurt and 1.16 for Hamburger SV (3.16 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.0%; Double Chance 1X: 81.8%; Double Chance X2: 39.0%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 72.0%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eintracht Frankfurt win | 61.0% | 1.64 |
| Draw | 20.8% | 4.81 |
| Hamburger SV win | 18.2% | 5.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eintracht Frankfurt expected goals | 2.01 |
| Hamburger SV expected goals | 1.16 |
| Expected total goals | 3.16 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 47.0% |
| Under 3.5 | 53.0% |
| Over 4.5 | 28.0% |
| Under 4.5 | 72.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.95% |
| 2 | 1-1 | 8.98% |
| 3 | 2-0 | 7.74% |
| 4 | 3-1 | 7.41% |
| 5 | 1-0 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eintracht Frankfurt win | 61.0% | 62.9% | 1.56 | -4.9% |
| Draw | 20.8% | 19.9% | 4.71 | -2.0% |
| Hamburger SV win | 18.2% | 17.2% | 5.43 | -1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 1eb5e1a69ae9dd9edd92fde344308a4e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:12:13Z |
| Market best draw last update utc | 2026-11-01T07:12:13Z |
| Market best away last update utc | 2026-11-01T07:12:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ein Frankfurt |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0304 |
| Dc lambda away | 1.1068 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:11:06.583192+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.9213 |
| Shot lambda away | 1.3486 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.27 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.57 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.10601339931829172, "-10": 1.148495237766935e-07, "-11": 1.3135171065043989e-08, "-12": 1.3814460469026054e-09, "-13": 1.3445026523151946e-10, "-14": 1.217503816722549e-11, "-15": 1.0300468513669994e-12, "-16": 8.094103219978504e-14, "-17": 5.233979653847531e-15, "-2": 0.05143758258940574, "-3": 0.018186679043362308, "-4": 0.005162237278484942, "-5": 0.0012172600014032696, "-6": 0.0002447400778690184, "-7": 4.281174959117021e-05, "-8": 6.620248286422009e-06, "-9": 9.1666018803446e-07, "0": 0.20804406051477137, "1": 0.22285766855519026, "10": 3.429614009561771e-05, "11": 6.8202067151915415e-06, "12": 1.2472154779606322e-06, "13": 2.1106439933012297e-07, "14": 3.323298971811807e-08, "15": 4.888794923674163e-09, "16": 6.679736613448138e-10, "17": 7.510492018645141e-11, "2": 0.18383598382257543, "3": 0.11301839493523094, "4": 0.05578012131441303, "5": 0.022870233691296416, "6": 0.007995361482875232, "7": 0.002431877784047671, "8": 0.000653881131339314, "9": 0.00015742679594393932} |
| Raw goal margin distribution | {"-1": 0.12475489057183052, "-10": 6.07483758892384e-08, "-11": 6.2709319830900785e-09, "-12": 5.949319866302827e-10, "-13": 5.220719844697744e-11, "-14": 4.261066777412009e-12, "-15": 3.2491821011705853e-13, "-16": 2.3084370883875244e-14, "-17": 1.380236109013813e-15, "-2": 0.057417120174688197, "-3": 0.018824208926394324, "-4": 0.004906093440285902, "-5": 0.0010559325224054471, "-6": 0.00019304550722349764, "-7": 3.062711050194912e-05, "-8": 4.287700524184884e-06, "-9": 5.367823516424292e-07, "0": 0.22899382375829083, "1": 0.22237745847240387, "10": 1.5345896388040353e-05, "11": 2.754453463484935e-06, "12": 4.5437709181584155e-07, "13": 6.933064742228287e-08, "14": 9.83918137521853e-09, "15": 1.3045491233227568e-09, "16": 1.6115737595931843e-10, "17": 1.675449291315172e-11, "2": 0.173593286011576, "3": 0.09895870682437612, "4": 0.04484549803311104, "5": 0.01678282095000146, "6": 0.005334997898941558, "7": 0.0014717238860206614, "8": 0.00035825356136231655, "9": 7.798481741983755e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 22.9% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 83.1% |
| Raw p under 3 5 | 61.1% |
| Raw p btts yes | 60.0% |
| P home draw | 81.8% |
| P draw away | 39.0% |
| P home away | 79.2% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.6% |
| Raw p home away | 77.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1123 |
| Totals anchor target over 2 5 | 0.6851 |
| Totals anchor reference over odds | 1.42 |
| Totals anchor reference under odds | 2.92 |
| Totals anchor reference last update utc | 2026-11-01T07:12:38Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6218 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.83, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.09, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:11:54Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.33, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.13, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:38Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.33, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.56 |
| Reference draw odds | 4.71 |
| Reference away odds | 5.43 |
| Market reference 1x2 last update utc | 2026-11-01T07:12:13Z |
| Market reference home last update utc | 2026-11-01T07:12:13Z |
| Market reference draw last update utc | 2026-11-01T07:12:13Z |
| Market reference away last update utc | 2026-11-01T07:12:13Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.95 |
| Market reference over 2 5 last update utc | 2026-11-01T07:11:29Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:11:29Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0655 |
| Raw ev home | -0.1204 |
| Raw edge prob draw | 0.0299 |
| Raw ev draw | 0.0786 |
| Raw edge prob away | 0.0355 |
| Raw ev away | 0.1250 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.05638162731112762, 0.03916633931642023, 0.025808511552561704, 0.008854747816357698, 0.002278508741145583, 0.00046904573150112196, 8.046340949037045e-05, 1.1831365865988615e-05, 1.5222268947934507e-06, 1.7408901768992017e-07, 1.7918673993680997e-08, 1.6766703189206746e-09, 1.43813919828137e-10, 1.1386547567395978e-11, 8.371408263309198e-13, 5.744361420332909e-14, 3.6953558644406e-15], [0.09089274707211878, 0.10336016327611172, 0.050676077695345975, 0.01738666282247875, 0.004473945960062837, 0.0009209906539481135, 0.0001579932257101328, 2.323137522463559e-05, 2.9889553387607636e-06, 3.418309718634349e-07, 3.5184055990676553e-08, 3.292211376780113e-09, 2.8238456758888685e-10, 2.2357956135205205e-11, 1.6437605659936246e-12, 1.12792907508083e-13, 7.255983767872757e-15], [0.1008081908117901, 0.10376008383634211, 0.04698362711411001, 0.017069715048469377, 0.004392388778701569, 0.0009042015817361136, 0.00015511310997379693, 2.280788207130285e-05, 2.934468589296177e-06, 3.355996112667652e-07, 3.454267309041989e-08, 3.2321964631596728e-09, 2.7723687702712e-10, 2.195038485480453e-11, 1.6137958592689682e-12, 1.1073676474372731e-13, 7.123711811663766e-15], [0.06598034785928947, 0.06791240245758083, 0.034950516003615505, 0.01055063405660342, 0.0028748788884927993, 0.0005918123757349587, 0.00010152366460692763, 1.4928072618700441e-05, 1.920650065681722e-06, 2.196545629329332e-07, 2.260865479423983e-08, 2.115517055424609e-09, 1.8145535038739187e-10, 1.4366828892597242e-11, 1.056251593357572e-12, 7.247873610036951e-14, 4.662567392568782e-15], [0.0323887841000988, 0.033337201337714985, 0.017156695194185372, 0.005886360745648984, 0.0013327021726819396, 0.00029051200679214707, 4.983647647655842e-05, 7.3279716880063745e-06, 9.428189199891826e-07, 1.0782520017336798e-07, 1.1098256718590499e-08, 1.0384762643923758e-09, 8.907376754118715e-11, 7.052465382537083e-12, 5.184984002449025e-13, 3.557874748416316e-14, 2.288785881398006e-15], [0.012719342889431202, 0.013091794167941859, 0.006737575833346413, 0.0023116224574348553, 0.0005948280046738016, 0.00010773768152579473, 1.957119571847358e-05, 2.8777549751709487e-06, 3.702527729637443e-07, 4.2343846218124645e-08, 4.358377030839374e-09, 4.078182017738032e-10, 3.498000382812737e-11, 2.76956137467535e-12, 2.0361860204305528e-13, 1.3972067843886073e-14, 8.98825109828728e-16], [0.004162492460325444, 0.004284379703409941, 0.002204918041047442, 0.0007564943514642407, 0.00019466155651031827, 4.0072337893522e-05, 6.048388139153319e-06, 9.417651124702703e-07, 1.2116776702016358e-07, 1.3857314969516157e-08, 1.4263088657825915e-09, 1.334613120208798e-10, 1.1447446889549699e-11, 9.063580124153923e-13, 6.663558826537201e-14, 4.572455319500563e-15, 2.9414670044959994e-16], [0.0011676036793196547, 0.001201793769714788, 0.0006184925118456538, 0.0002122011262658537, 5.460371442589185e-05, 1.1240527066266094e-05, 1.928279209206272e-06, 2.4946987040421183e-07, 3.398827311668654e-08, 3.887058558811989e-09, 4.000880471033432e-10, 3.7436684978457394e-11, 3.211076352558616e-12, 2.542387668359454e-13, 1.8691675426168787e-14, 1.2826006786703393e-15, 8.250988391648327e-17], [0.00028657975223633916, 0.00029497145894977184, 0.00015180444695758237, 5.208320876907054e-05, 1.3402080884563456e-05, 2.7589048567690456e-06, 4.732819772705861e-07, 6.9591535659907e-08, 7.87793976463172e-09, 9.540499901144239e-10, 9.819867429537899e-11, 9.188559522121063e-12, 7.881351196704176e-13, 6.240103906761573e-14, 4.587734526183374e-15, 3.148049215857922e-16, 2.025144533940905e-17], [6.252346358536573e-05, 6.435429275254179e-05, 3.3119366380153686e-05, 1.1363058909327438e-05, 2.9239487773130806e-06, 6.019137290810142e-07, 1.0325652193000649e-07, 1.518287252231821e-08, 1.9534326936953414e-09, 1.9656317809683266e-10, 2.1424127798725147e-11, 2.0046795427805292e-12, 1.7194842646951227e-13, 1.361411287220148e-14, 1.0009117892969516e-15, 6.868138414409363e-17, 4.418283201617652e-18], [1.2276740144356105e-05, 1.2636231008189007e-05, 6.503124290926824e-06, 2.231183518557906e-06, 5.741294112004763e-07, 1.1818824514030234e-07, 2.0274844278483073e-08, 2.9812196879798763e-09, 3.8356457231842265e-10, 4.386624611873585e-11, 3.972616972417276e-12, 3.9362710266076185e-13, 3.376278326479691e-14, 2.6731872555293182e-15, 1.9653316115227663e-16, 1.3485873263251094e-17, 8.675481433682056e-19], [2.1914441821183905e-06, 2.255614650240053e-06, 1.160832087783172e-06, 3.982746301940735e-07, 1.0248425422091803e-07, 2.1097045238557672e-08, 3.6191357815669086e-09, 5.321589008173113e-10, 6.846771541876781e-11, 7.83028953272017e-12, 8.05957821319072e-13, 6.635380800242306e-14, 6.026783501789593e-15, 4.771739557862901e-16, 3.5081906722485395e-17, 2.407278980904715e-18, 1.5486059891606346e-19], [3.585825920642278e-07, 3.6908270563353494e-07, 1.8994514320060891e-07, 6.51690562843171e-08, 1.6769338605185034e-08, 3.452076593265286e-09, 5.921935407600297e-10, 8.70763305778841e-11, 1.1203265439252378e-11, 1.281258058118544e-12, 1.3187762071295942e-13, 1.2339936116772565e-14, 9.3127487900653e-16, 7.807922981911721e-17, 5.740397656372825e-18, 3.938993034082725e-19, 2.5339598161364812e-20], [5.416090155623246e-08, 5.574685589406779e-08, 2.8689625290370994e-08, 9.843240915875975e-09, 2.5328683473733004e-09, 5.214072982631755e-10, 8.94458815713948e-11, 1.3152151478290392e-11, 1.6921595470395996e-12, 1.935233139858012e-13, 1.9919011661406593e-14, 1.863844146430303e-15, 1.598684783896098e-16, 1.1136935690406744e-17, 8.670390566666106e-19, 5.949519543643306e-20, 3.827334376695975e-21], [7.596226123540172e-09, 7.818660895223184e-09, 4.023804531374474e-09, 1.3805435588594333e-09, 3.5524225326694275e-10, 7.312891082433364e-11, 1.2545048599869977e-11, 1.8446280207580927e-12, 2.3733036539420315e-13, 2.7142215343050314e-14, 2.79370011188572e-15, 2.6140963662913913e-16, 2.2422025427566522e-17, 1.7752764085246597e-18, 1.1483761621549577e-19, 8.344376567109693e-21, 5.367949302984924e-22], [9.943669021592737e-10, 1.0234842258478768e-09, 5.267270854876262e-10, 1.8071695070594138e-10, 4.650218847520356e-11, 9.572775656234037e-12, 1.642181382019818e-12, 2.414668837928935e-13, 3.106719789370606e-14, 3.552990675826624e-15, 3.6570303208972503e-16, 3.421924075745609e-17, 2.935104827310618e-18, 2.32388566916227e-19, 1.7085245179597392e-20, 1.0315164997199587e-21, 7.026793347838815e-23], [1.2203002846773544e-10, 1.256033451488405e-10, 6.464064833333198e-11, 2.2177824494520457e-11, 5.706810404809858e-12, 1.1747837576942726e-12, 2.0153068285147426e-13, 2.963313706366947e-14, 3.812607836352214e-15, 4.3602774023875715e-16, 4.487956238259646e-17, 4.199430727942512e-18, 3.6019996729047615e-19, 2.851903394489803e-20, 2.096724007121625e-21, 1.4387472354423416e-22, 8.143493278217124e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9635412756035504, "lambda_away": 1.0292822736007952, "rho": -0.11152998455064249, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.6045 |
| Legacy p draw | 0.2187 |
| Legacy p away | 0.1768 |
| Legacy p over 1 5 | 0.8136 |
| Legacy p under 3 5 | 0.6457 |
| Legacy p btts yes | 0.5585 |
| Legacy p over 2 5 | 0.5836 |
| Legacy goal margin distribution | {"-1": 0.11009807088049844, "-10": 2.1503021840995615e-08, "-11": 1.9820980005303173e-09, "-12": 1.6786043934459295e-10, "-13": 1.3145707465525899e-11, "-14": 9.570574456506667e-13, "-15": 6.469959797120184e-14, "-16": 3.6953558644406e-15, "-2": 0.04823221491599189, "-3": 0.01434213151399078, "-4": 0.0033705272049999, "-5": 0.0006518798096612475, "-6": 0.00010686042564849847, "-7": 1.5179603852447517e-05, "-8": 1.9008079680700862e-06, "-9": 2.1269398623309358e-07, "0": 0.2187227975487129, "1": 0.236126607869155, "10": 1.4732508195272248e-05, "11": 2.5906447335733894e-06, "12": 4.185396762507808e-07, "13": 6.252846736143779e-08, "14": 8.68435099772138e-09, "15": 1.1199702473081143e-09, "16": 1.2203002846773544e-10, "2": 0.18839530186094616, "3": 0.10686908830860853, "4": 0.047911722248370404, "5": 0.017677344158410102, "6": 0.005528049567950201, "7": 0.0014980317158209651, "8": 0.00035785274744623335, "9": 7.638830340669494e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5796 |
| Legacy raw p draw | 0.2384 |
| Legacy raw p away | 0.1820 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9635 |
| Legacy lambda away | 1.0293 |
| Legacy model home team | Ein Frankfurt |
| Legacy model away team | Hamburg |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 82.3% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:12:35Z |
| Market reference home draw last update utc | 2026-11-01T07:12:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.1% |
| Market draw away odds | 2.55 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:12:35Z |
| Market reference draw away last update utc | 2026-11-01T07:12:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.6% |
| Market home away odds | 1.22 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:12:35Z |
| Market reference home away last update utc | 2026-11-01T07:12:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.55 |
| Market reference dc home draw odds | 1.18 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.66, "price": 1.44, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.44, "price": 2.66, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.81, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.81, "price": 2.01, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.24, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:35Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.8% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 5.70 |
| Market reference over 1 5 last update utc | 2026-11-01T07:12:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.3% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:12:38Z |
| Market reference under 3 5 odds | 1.81 |
| Market reference under 3 5 opposite odds | 2.05 |
| Market reference under 3 5 last update utc | 2026-11-01T07:12:38Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.4% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:12:35Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-11-01T07:12:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.303560003176896, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,474.7389 |
| Elo away rating | 1,410.7728 |
| Elo rating diff | 123.9661 |
| Elo home expectancy | 0.6712 |

</details>


---

## 2026-11-01 — Union Berlin vs 1. FC Köln

The model's most likely 1X2 outcome is **Union Berlin win** at **37.6%**. Expected goals are 1.44 for Union Berlin and 1.19 for 1. FC Köln (2.63 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.2%; Under 3.5 goals: 64.9%; Double Chance 1X: 64.7%; Double Chance X2: 62.4%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Union Berlin win | 37.6% | 2.66 |
| Draw | 27.1% | 3.69 |
| 1. FC Köln win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Union Berlin expected goals | 1.44 |
| 1. FC Köln expected goals | 1.19 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.57% |
| 2 | 1-2 | 8.61% |
| 3 | 2-1 | 7.89% |
| 4 | 0-1 | 6.74% |
| 5 | 2-2 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Union Berlin win | 37.6% | 35.8% | 2.71 | +1.9% |
| Draw | 27.1% | 26.8% | 3.59 | -2.8% |
| 1. FC Köln win | 35.3% | 37.5% | 2.59 | -8.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T14:30:00+00:00 |
| Fixture id | 60eaeb599578cd5c951f917c4fef06ff |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-01T07:12:13Z |
| Market best draw last update utc | 2026-11-01T07:12:13Z |
| Market best away last update utc | 2026-11-01T07:12:13Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Union Berlin |
| Matched away-team name | FC Koln |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4286 |
| Dc lambda away | 1.1543 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-01T07:11:06.583192+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.2000 |
| Shot lambda home | 1.4865 |
| Shot lambda away | 1.3222 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.38 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.21 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.48 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.19236282067062996, "-10": 4.086404448565437e-07, "-11": 4.9632064752092926e-08, "-12": 5.539543709372954e-09, "-13": 5.715941010974738e-10, "-14": 5.439070267694108e-11, "-15": 4.286210272965983e-12, "-2": 0.1039670298236738, "-3": 0.04027625408393024, "-4": 0.012383885457365202, "-5": 0.0031414981792095664, "-6": 0.0006765200041033448, "-7": 0.00012637875088227082, "-8": 2.0826615098234818e-05, "-9": 3.0685362908301694e-06, "0": 0.2708467480755113, "1": 0.1778551067052601, "10": 2.120181974637693e-06, "11": 3.1220779615455335e-07, "12": 4.224788825536066e-08, "13": 5.285284403562959e-09, "14": 6.097543462338748e-10, "15": 5.825769792001514e-11, "2": 0.11553951376800306, "3": 0.05426672114741061, "4": 0.020229774776981856, "5": 0.00622186444540119, "6": 0.0016244785711802896, "7": 0.0003679230645145632, "8": 7.35108183629176e-05, "9": 1.313147291105964e-05} |
| Raw goal margin distribution | {"-1": 0.17403783441574736, "-10": 1.299401275204212e-07, "-11": 1.3854466852909264e-08, "-12": 1.3563629309994382e-09, "-13": 1.2204245518034665e-10, "-14": 9.227594203803766e-12, "-2": 0.08698231930479833, "-3": 0.030429017159376223, "-4": 0.00835875134800119, "-5": 0.0018825817614270101, "-6": 0.0003585355245815064, "-7": 5.907921189156378e-05, "-8": 8.57249891149166e-06, "-9": 1.1106713930625872e-06, "0": 0.2784061343760659, "1": 0.212981331946274, "10": 8.917423707002804e-07, "11": 1.1527510941220885e-07, "12": 1.3682682474275885e-08, "13": 1.492642777503203e-09, "14": 1.3683054187955138e-10, "2": 0.12785867699728987, "3": 0.05422964472460444, "4": 0.018060919285418156, "5": 0.004931759658571926, "6": 0.001138753858093643, "7": 0.000227500299586661, "8": 4.002251072465107e-05, "9": 6.286835379808705e-06} |
| Unadjusted home-win probability | 41.9% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 30.2% |
| Raw p over 1 5 | 74.7% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 54.0% |
| P home draw | 64.7% |
| P draw away | 62.4% |
| P home away | 72.9% |
| Raw p home draw | 69.8% |
| Raw p draw away | 58.1% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1435 |
| Totals anchor target over 2 5 | 0.5721 |
| Totals anchor reference over odds | 1.70 |
| Totals anchor reference under odds | 2.24 |
| Totals anchor reference last update utc | 2026-11-01T07:12:13Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.4905 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.34, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.32, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-01T07:12:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 10.4, "price": 1.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.9, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.08, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.78, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-01T07:12:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.02, "price": 10.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.71 |
| Reference draw odds | 3.59 |
| Reference away odds | 2.59 |
| Market reference 1x2 last update utc | 2026-11-01T07:12:13Z |
| Market reference home last update utc | 2026-11-01T07:12:13Z |
| Market reference draw last update utc | 2026-11-01T07:12:13Z |
| Market reference away last update utc | 2026-11-01T07:12:13Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.34 |
| Market reference over 2 5 last update utc | 2026-11-01T07:11:51Z |
| Market reference under 2 5 last update utc | 2026-11-01T07:11:51Z |
| Home probability edge | +1.9% |
| Draw probability edge | +0.3% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | 0.0618 |
| Raw ev home | 0.1368 |
| Raw edge prob draw | 0.0108 |
| Raw ev draw | -0.0005 |
| Raw edge prob away | -0.0726 |
| Raw ev away | -0.2175 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 1,000,000,000 |
| Legacy trial matrix | [[0.09272451006700089, 0.08905206489502436, 0.05617581475831221, 0.019858579521536784, 0.0052651196379156304, 0.0011167560004581643, 0.00019739088731214464, 2.9905365472767744e-05, 3.964415653671299e-06, 4.671504030312126e-07, 4.9542370504242214e-08, 4.7764380870863416e-09, 4.2212683514334956e-10, 3.443655229130485e-11, 2.608625190141143e-12], [0.09463311909239928, 0.13363542937156642, 0.08029174640511957, 0.028383745527664116, 0.007525403104146057, 0.0015961724804697164, 0.00028212958076238897, 4.274355487361387e-05, 5.666314902214438e-06, 6.676951968494857e-07, 7.081060534589752e-08, 6.826933570221943e-09, 6.033432882806638e-10, 4.92199523146384e-11, 3.728491934366246e-12], [0.07670153268747089, 0.0813437326819997, 0.04555982199540717, 0.02028435642401998, 0.005378006177872022, 0.0011406997528392914, 0.0002016230369725484, 3.0546549997814655e-05, 4.049414513501401e-06, 4.77166318388134e-07, 5.060458127476054e-08, 4.878847074165041e-09, 4.3117742489612856e-10, 3.517488750560811e-11, 2.6645552908813974e-12], [0.036543009584714216, 0.038754698881529756, 0.020550123025804275, 0.0076732807488235875, 0.0025622503803855836, 0.0005434650461436802, 9.605952207771939e-05, 1.4553331990097678e-05, 1.9292677498677227e-06, 2.2733696101497463e-07, 2.4109605554936913e-08, 2.324435368456348e-09, 2.054264135097972e-10, 1.675841676457985e-11, 1.2694774944123812e-12], [0.013057674690964647, 0.013847963167023438, 0.007343041100875785, 0.0025958211066280587, 0.0007269468934517296, 0.000194192811678616, 3.4324320971775416e-05, 5.2002469680492456e-06, 6.893726312044009e-07, 8.123282991469205e-08, 8.614927720554422e-09, 8.305752926866627e-10, 7.340367722927094e-11, 5.98817549332406e-12, 4.536140930349537e-13], [0.0037326508193540665, 0.003958561710649905, 0.0020990726932951127, 0.0007420382273159537, 0.00019673713512531168, 4.407621121217136e-05, 9.811908156030532e-06, 1.4865361992486986e-06, 1.9706321206530833e-07, 2.3221116800324007e-08, 2.462652637307197e-09, 2.374272311231152e-10, 2.0983084847643602e-11, 1.7117724779174094e-12, 1.2966956645114481e-13], [0.0008891758084146349, 0.0009429913162451821, 0.0005000319476185974, 0.0001767651121361533, 4.686586279734051e-05, 9.94046424295473e-06, 1.8558519774810102e-06, 3.541161739134539e-07, 4.6943539424691635e-08, 5.5316332286318255e-09, 5.866423771192698e-10, 5.655888010710781e-11, 4.9984990119341176e-12, 4.0777097846444914e-13, 3.0889318919985224e-14], [0.00018155621602833485, 0.0001925445266333859, 0.00010209894088861365, 3.609275531515467e-05, 9.569298478283037e-06, 2.0296920546383617e-06, 3.587558208517411e-07, 5.7410170041597534e-08, 9.585158867648396e-09, 1.1294756199425019e-09, 1.1978347717482616e-10, 1.1548465621613444e-11, 1.0206176976926312e-12, 8.326065009368117e-14, 6.307130497403064e-15], [3.2437147815161845e-05, 3.440033840776223e-05, 1.8241173504401368e-05, 6.448394138328077e-06, 1.7096674298335616e-06, 3.626282957191015e-07, 6.40959359314996e-08, 9.710744074621058e-09, 1.3597229832452475e-09, 2.0179406929244815e-10, 2.1400723367838393e-11, 2.0632688574437342e-12, 1.8234532447877913e-13, 1.4875491863378063e-14, 1.1268428518131787e-15], [5.151357310942311e-06, 5.4631324481890605e-06, 2.8968885620745914e-06, 1.0240722297040885e-06, 2.7151301539022586e-07, 5.758915466155709e-08, 1.0179102985376737e-08, 1.5421674176946842e-09, 2.0443798477761318e-10, 2.544526620680181e-11, 3.398658026549373e-12, 3.2766860926854706e-13, 2.895833893049146e-14, 2.3623832218829476e-15, 1.7895439500564297e-16], [7.362803310140461e-07, 7.808421595570551e-07, 4.1405049982931973e-07, 1.4637001371797533e-07, 3.8807188237845004e-08, 8.231182443307163e-09, 1.4548929268756716e-09, 2.2042104017273333e-10, 2.9220195381160826e-11, 3.443187405518159e-12, 3.8569905786226167e-13, 4.683347272042098e-14, 4.138997566344115e-15, 3.376539804170234e-16, 2.557784157415998e-17], [9.566917700534555e-08, 1.0145935403844852e-07, 5.3799984718819416e-08, 1.9018705458794468e-08, 5.042443216557051e-09, 1.0695253111644279e-09, 1.8904268263338759e-10, 2.8640585140913293e-11, 3.796749588843391e-12, 4.4739332491391665e-13, 4.744708710554004e-14, 4.831753689404426e-15, 5.378039778054529e-16, 4.387334152276769e-17, 3.3234774173619952e-18], [1.1394947173067188e-08, 1.208460254045086e-08, 6.4079989289394115e-09, 2.2652765581016588e-09, 6.005944220953013e-10, 1.2738882890459004e-10, 2.2516461931537204e-11, 3.4113176772515213e-12, 4.5222256894524783e-13, 5.3288043887866936e-14, 5.65131913963613e-15, 5.448503110792136e-16, 5.0860880464620335e-17, 5.225658091842255e-18, 3.958521520427176e-19], [1.252825221968052e-09, 1.3286498506917444e-09, 7.045318033149447e-10, 2.490573728529914e-10, 6.603276248202077e-11, 1.400585149055014e-11, 2.4755877310241357e-12, 3.750596436557062e-13, 4.971991811044899e-14, 5.858790251336477e-15, 6.213381289086902e-16, 5.99039382587538e-17, 5.294124912485911e-18, 4.56182634211025e-19, 4.352223426025395e-20], [1.2790395582788442e-10, 1.356450754931686e-10, 7.192735512538427e-11, 2.5426869332943788e-11, 6.741444367176815e-12, 1.4298912401884232e-12, 2.5273873661288577e-13, 3.82907457910237e-14, 5.076026646218868e-15, 5.9813806137668105e-16, 6.343391177045129e-17, 6.115737884752888e-18, 5.404900117593323e-19, 4.409246464171742e-20, 3.5279649074742346e-21]] |
| Legacy trial inputs | {"lambda_home": 1.4292938473711938, "lambda_away": 1.060522910454006, "rho": -0.11152998455064249, "max_goals": 14, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.3993 |
| Legacy p draw | 0.2804 |
| Legacy p away | 0.3203 |
| Legacy p over 1 5 | 0.7236 |
| Legacy p under 3 5 | 0.7610 |
| Legacy p btts yes | 0.5098 |
| Legacy p over 2 5 | 0.4571 |
| Legacy goal margin distribution | {"-1": 0.192394786730957, "-10": 5.68176935302179e-08, "-11": 5.416225740367026e-09, "-12": 4.740113427488693e-10, "-13": 3.8165044225671096e-11, "-14": 2.608625190141143e-12, "-2": 0.09051689046191068, "-3": 0.02862614486428924, "-4": 0.007078181679471573, "-5": 0.00143144515204534, "-6": 0.00024442005109811307, "-7": 3.6073808271380895e-05, "-8": 4.685115013503028e-06, "-9": 5.430513997098448e-07, "0": 0.2803659799351683, "1": 0.1993298421806937, "10": 8.444034827986541e-07, "11": 1.0848373821844429e-07, "12": 1.2795524378884317e-08, "13": 1.3884702974612205e-09, "14": 1.2790395582788442e-10, "2": 0.123590272119821, "3": 0.052676752887317616, "4": 0.017554129845124455, "5": 0.0047844694073283425, "6": 0.0011010254803922729, "7": 0.0002190049853578136, "8": 3.833396432165134e-05, "9": 5.988332194430009e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4410 |
| Legacy raw p draw | 0.2931 |
| Legacy raw p away | 0.2659 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.4293 |
| Legacy lambda away | 1.0605 |
| Legacy model home team | Union Berlin |
| Legacy model away team | FC Koln |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 62.8% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-11-01T07:12:27Z |
| Market reference home draw last update utc | 2026-11-01T07:12:27Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.0% |
| Market draw away odds | 1.51 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-11-01T07:12:27Z |
| Market reference draw away last update utc | 2026-11-01T07:12:27Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.2% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-01T07:12:27Z |
| Market reference home away last update utc | 2026-11-01T07:12:27Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home draw odds | 1.54 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.58, "price": 1.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.48, "price": 2.58, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.97, "price": 1.85, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.97, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.28, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-11-01T07:12:27Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.28, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 82.0% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-11-01T07:12:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.1% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-01T07:12:13Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-11-01T07:12:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.7% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-11-01T07:12:27Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.58 |
| Market reference btts yes last update utc | 2026-11-01T07:12:36Z |
| Market btts yes bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.01169351969556193, "mu": 10.176335074241845, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,423.6013 |
| Elo away rating | 1,399.6261 |
| Elo rating diff | 83.9752 |
| Elo home expectancy | 0.6186 |

</details>


---
