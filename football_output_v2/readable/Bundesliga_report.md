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
| Training as of utc | 2026-11-04T09:29:36.036580+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 68, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T09:29:36.036580+00:00', 'observations': 397, 'observations_sha256': '6a2b183c5aeb285c4dd83b4e2ecc9360e1931c9770747bd94631a91f58b81fac', 'eligible_training_matches': 80, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 114, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 80, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'd309fbcc186badb6d0155f5242cca2fc20f0c490a6c4512d9f9824984fd0c5b5', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694601589980784, 'audit_candidate_poisson_score': 0.6673686986674418, 'audit_gain': 0.002091460330636674, 'audit_gain_lower95': -0.006071819396616229, 'audit_baseline_briers': [0.5838791063980268, 0.13631367949783407, 0.2743769881803856, 0.2354603100616698], 'audit_candidate_briers': [0.5818323738130945, 0.1359856171064298, 0.2735024403933491, 0.236260431039501], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1589.138 |
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
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261104T092936036580Z_44c8452386312fd34e76b45cedf0af7e657fb0c1db4a870d420f534ce3f741fc.json |
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
| Hamburger SV win | 38.8% | 39.3% | 2.49 | -3.5% |
| Draw | 26.3% | 26.0% | 3.85 | +1.3% |
| Borussia Monchengladbach win | 34.9% | 34.7% | 2.83 | -1.2% |
| Over 2.5 | 54.2% | 58.5% | 1.69 | -8.5% |
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
| Market best home last update utc | 2026-11-04T09:29:37Z |
| Market best draw last update utc | 2026-11-04T09:29:37Z |
| Market best away last update utc | 2026-11-04T09:29:37Z |
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
| Dc lambda home | 1.4417 |
| Dc lambda away | 1.3956 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:29:36.036580+00:00 |
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
| Goal margin distribution | {"-1": 0.18443454655749528, "-10": 5.337935851056034e-07, "-11": 6.671747936254993e-08, "-12": 7.658146555917549e-09, "-13": 8.064815155482443e-10, "-14": 7.02917821121665e-11, "-2": 0.10463266529769696, "-3": 0.042208786693799655, "-4": 0.01345446180587557, "-5": 0.003529138865330154, "-6": 0.0007845517937139748, "-7": 0.00015112950817068894, "-8": 2.5662426502515054e-05, "-9": 3.89381768831434e-06, "0": 0.26304248300402877, "1": 0.2001516555626547, "10": 7.747448984337726e-07, "11": 1.0003016895599987e-07, "12": 1.1860992826222734e-08, "13": 1.2903210590445707e-09, "14": 1.1617533118018321e-10, "2": 0.11711288580025465, "3": 0.04880297086875847, "4": 0.0160699941882897, "5": 0.004354358021669267, "6": 0.0009999608667285438, "7": 0.00019898331013869512, "8": 3.490367035156779e-05, "9": 5.470852311506948e-06} |
| Raw goal margin distribution | {"-1": 0.18745293779245414, "-10": 5.425294640861595e-07, "-11": 6.780935427798877e-08, "-12": 7.7834771020211e-09, "-13": 8.196801097548253e-10, "-14": 7.14421528153626e-11, "-2": 0.10634504687544272, "-3": 0.042899560923317974, "-4": 0.013674652818589574, "-5": 0.0035868955167650002, "-6": 0.0007973914937686459, "-7": 0.00015360284080451761, "-8": 2.6082408792540202e-05, "-9": 3.957542545724781e-06, "0": 0.26934618160631857, "1": 0.19394731258929168, "10": 7.507291936761283e-07, "11": 9.692941281115652e-08, "12": 1.1493323284386506e-08, "13": 1.2503234163892522e-09, "14": 1.1257410391249142e-10, "2": 0.11348259601792698, "3": 0.047290166148069884, "4": 0.015571853139974017, "5": 0.004219380718986934, "6": 0.0009689638701776804, "7": 0.00019281518378168352, "8": 3.382171906177424e-05, "9": 5.301265684797385e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:37Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:29:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:37Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:29:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:29:39Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.8, "draw": 3.7, "home": 2.48}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:37Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.83, "draw": 3.85, "home": 2.49}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:29:37Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.48 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-11-04T09:29:39Z |
| Market reference home last update utc | 2026-11-04T09:29:39Z |
| Market reference draw last update utc | 2026-11-04T09:29:39Z |
| Market reference away last update utc | 2026-11-04T09:29:39Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-04T09:29:37Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:29:37Z |
| Market best over 2 5 last update utc | 2026-11-04T09:29:37Z |
| Market best under 2 5 last update utc | 2026-11-04T09:29:37Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | -0.0172 |
| Raw ev home | -0.0645 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | 0.0370 |
| Raw edge prob away | 0.0082 |
| Raw ev away | 0.0045 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 9.857657217579082, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---
