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
| Training sha256 | a3462040aa40164fa3fdf4be795c175eef9ab017b46bab8c20d7e0fc71ba5c17 |
| Training as of utc | 2026-11-04T10:18:30.346210+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 68, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T10:18:30.346210+00:00', 'observations': 397, 'observations_sha256': '6a2b183c5aeb285c4dd83b4e2ecc9360e1931c9770747bd94631a91f58b81fac', 'eligible_training_matches': 80, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 114, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 80, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'd309fbcc186badb6d0155f5242cca2fc20f0c490a6c4512d9f9824984fd0c5b5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694601589980784, 'audit_candidate_poisson_score': 0.6673686986674418, 'audit_gain': 0.002091460330636674, 'audit_gain_lower95': -0.006071819396616229, 'audit_baseline_briers': [0.5838791063980268, 0.13631367949783407, 0.2743769881803856, 0.2354603100616698], 'audit_candidate_briers': [0.5818323738130945, 0.1359856171064298, 0.2735024403933491, 0.236260431039501], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1589.060 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261104T101830346210Z_c85d4b9bf34444e255b134023066126df4a550e2c411c5d8ae13eead3f8c920f.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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

## 2026-11-06 — Hamburger SV vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **38.8%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Monchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 54.2%; Under 3.5 goals: 68.3%; Double Chance 1X: 65.1%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.1%; BTTS Yes (both teams score): 58.2%; BTTS No (at least one team does not score): 41.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 38.8% | 2.58 |
| Draw | 26.3% | 3.80 |
| Borussia Monchengladbach win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Monchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 54.2% |
| Under 2.5 | 45.8% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 15.9% |
| Under 4.5 | 84.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 2-1 | 8.77% |
| 3 | 1-2 | 8.09% |
| 4 | 1-0 | 7.76% |
| 5 | 0-1 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 38.8% | 39.3% | 2.49 | -3.4% |
| Draw | 26.3% | 26.0% | 3.85 | +1.3% |
| Borussia Monchengladbach win | 34.9% | 34.7% | 2.83 | -1.2% |
| Over 2.5 | 54.2% | 58.5% | 1.69 | -8.4% |
| Under 2.5 | 45.8% | 41.5% | 2.36 | +8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | 295076c39e49863cb54db085ac3cd340 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T10:17:48Z |
| Market best draw last update utc | 2026-11-04T10:17:48Z |
| Market best away last update utc | 2026-11-04T10:17:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4420 |
| Dc lambda away | 1.3955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T10:18:30.346210+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 58.2% |
| P btts no | 41.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.09 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.18 |
| Fair Over 3.5 odds | 3.16 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.29 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.18443133773549858, "-10": 5.333299576495873e-07, "-11": 6.66535598959446e-08, "-12": 7.65012534992562e-09, "-13": 8.055632576209067e-10, "-14": 7.020430433705749e-11, "-2": 0.10462113788483546, "-3": 0.042199684837184274, "-4": 0.013450222565007797, "-5": 0.0035276883926027083, "-6": 0.0007841558259702013, "-7": 0.00015103929258729283, "-8": 2.5644766762060478e-05, "-9": 3.890785847863918e-06, "0": 0.2630403492170407, "1": 0.20013629791786505, "10": 7.76266335342851e-07, "11": 1.0024999664960278e-07, "12": 1.1889834579751377e-08, "13": 1.2937583166890707e-09, "14": 1.1651007700445998e-10, "2": 0.11712895289495659, "3": 0.048820280804348054, "4": 0.016079286751787936, "5": 0.0043578649722126285, "6": 0.0010009956054844384, "7": 0.00019923516061801913, "8": 3.49559443170089e-05, "9": 5.480319227871709e-06} |
| Raw goal margin distribution | {"-1": 0.1874129214131844, "-10": 5.419519625435138e-07, "-11": 6.77311054404573e-08, "-12": 7.773800041849729e-09, "-13": 8.185862844543971e-10, "-14": 7.13392524997979e-11, "-2": 0.10631248102038059, "-3": 0.042881900197431155, "-4": 0.013667663725243712, "-5": 0.0035847182784154467, "-6": 0.0007968327725248485, "-7": 0.00015348104839190202, "-8": 2.6059349332108727e-05, "-9": 3.9536856983979915e-06, "0": 0.2693390689830252, "1": 0.19397168682737786, "10": 7.523557298714223e-07, "11": 9.716208982012264e-08, "12": 1.1523603132098271e-08, "13": 1.2539078900026304e-09, "14": 1.1292132613653912e-10, "2": 0.11352113937214561, "3": 0.047316515382391997, "4": 0.015584011529509792, "5": 0.00422363373571013, "6": 0.0009701628746140459, "7": 0.0001930983064164645, "8": 3.387922907716009e-05, "9": 5.311514083362576e-06} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 65.1% |
| P draw away | 61.2% |
| P home away | 73.7% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5417 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:32Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:32Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T10:18:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.8, "draw": 3.7, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:48Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.83, "draw": 3.85, "home": 2.49}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T10:17:48Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.48 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-11-04T10:18:32Z |
| Market reference home last update utc | 2026-11-04T10:18:32Z |
| Market reference draw last update utc | 2026-11-04T10:18:32Z |
| Market reference away last update utc | 2026-11-04T10:18:32Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-04T10:17:48Z |
| Market reference under 2 5 last update utc | 2026-11-04T10:17:48Z |
| Market best over 2 5 last update utc | 2026-11-04T10:17:48Z |
| Market best under 2 5 last update utc | 2026-11-04T10:17:48Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0171 |
| Raw ev home | -0.0642 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0370 |
| Raw edge prob away | 0.0081 |
| Raw ev away | 0.0042 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 9.857657217579082, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---
