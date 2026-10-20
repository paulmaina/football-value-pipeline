# UEFA Champions League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 539 |
| Training data through | 2026-10-14 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 056d196e8a59c0ce6b7d8ec047c46c9b920d1f0f1e5408934bf1a4db21202e6f |
| Training as of utc | 2026-10-20T05:43:57.422675+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 36, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 27, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:43:57.422675+00:00', 'observations': 90, 'observations_sha256': 'f5d8c20e76b17b358422497f114c5f42db583ab2b7e1e3bc4401b0f636ae680a', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 27, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '74a644453a99c64eb29870884c2ab52202e2baa36409c53c8629f08367eb967c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 965.511 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-20T05:04:10.781512+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '88cc817532193de59b6090581451b4d53ddbf3916512fa74597ef848a3d783a1', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'LIVE_REFRESH_FAILED_USING_CACHE', 'download_age_hours': 0.662955878611111, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': 'ValueError', 'last_refresh_error_reason': 'Unknown match status'} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261020T054357422675Z_feeb72c69d0bce2ce8234a75db02faeb2f98b64352a98a453dd22c01143cbb85.json |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 18.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 18.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-20 — AS Roma vs ŠK Slovan Bratislava

The model's most likely 1X2 outcome is **AS Roma win** at **83.9%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.07 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.4%; Under 3.5 goals: 24.9%; Double Chance 1X: 93.7%; Double Chance X2: 16.1%; Double Chance 12 (either team wins): 90.2%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 83.9% | 1.19 |
| Draw | 9.8% | 10.18 |
| ŠK Slovan Bratislava win | 6.3% | 15.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.07 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.3% |
| Under 1.5 | 3.7% |
| Over 2.5 | 88.4% |
| Under 2.5 | 11.6% |
| Over 3.5 | 75.1% |
| Under 3.5 | 24.9% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.54% |
| 2 | 4-1 | 7.08% |
| 3 | 2-1 | 6.01% |
| 4 | 3-0 | 5.73% |
| 5 | 4-0 | 5.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 83.9% | 86.7% | 1.15 | -3.5% |
| Draw | 9.8% | 9.5% | 9.70 | -4.7% |
| ŠK Slovan Bratislava win | 6.3% | 3.8% | 22.00 | +37.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | e3b50e57c4cf46191ab068d1e880e595 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.7592 |
| Dc lambda away | 1.3151 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 218.86 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.68 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.65 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.01 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.7% |
| P draw away | 16.1% |
| P home away | 90.2% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.14 |
| Reference draw odds | 8.70 |
| Reference away odds | 20.50 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.3% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | +10.2% |
| Under 2.5 probability edge | -10.2% |
| Raw edge prob home | -0.0561 |
| Raw ev home | -0.0672 |
| Raw edge prob draw | 0.0060 |
| Raw ev draw | -0.0177 |
| Raw edge prob away | 0.0501 |
| Raw ev away | 0.9273 |
| Market p home draw | 95.3% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:37Z |
| Market reference home draw last update utc | 2026-10-20T05:43:55Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 15.6% |
| Market draw away odds | 6.35 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:43:55Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 89.1% |
| Market home away odds | 1.09 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:43:37Z |
| Market reference home away last update utc | 2026-10-20T05:43:55Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 6.15 |
| Market reference dc home away odds | 1.08 |
| Market p over 1 5 | 92.5% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 9.60 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 42.5% |
| Market under 3 5 odds | 2.25 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 2.25 |
| Market reference under 3 5 opposite odds | 1.69 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.7% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:37Z |
| Market reference btts yes odds | 1.87 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **44.6%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 21.5%. Goal-market probabilities: at least one goal: 87.4%; Over 2.5 goals: 28.9%; Under 3.5 goals: 88.8%; Double Chance 1X: 70.1%; Double Chance X2: 55.4%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.8%; BTTS No (at least one team does not score): 66.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 44.6% | 2.24 |
| Draw | 25.5% | 3.92 |
| Slavia Praha win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 87.4% |
| Under 0.5 | 12.6% |
| Over 1.5 | 53.5% |
| Under 1.5 | 46.5% |
| Over 2.5 | 28.9% |
| Under 2.5 | 71.1% |
| Over 3.5 | 11.2% |
| Under 3.5 | 88.8% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.49% |
| 2 | 0-0 | 12.65% |
| 3 | 0-1 | 12.33% |
| 4 | 1-1 | 10.39% |
| 5 | 2-1 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 44.6% | 62.3% | 1.61 | -28.2% |
| Draw | 25.5% | 20.4% | 4.67 | +19.2% |
| Slavia Praha win | 29.9% | 17.2% | 5.51 | +64.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | 16e237246e9bef441e69998d1ef9536d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7763 |
| Dc lambda away | 1.0672 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 33.8% |
| P btts no | 66.2% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.91 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.46 |
| Fair Under 2.5 odds | 1.41 |
| Fair Over 3.5 odds | 8.90 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.80 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.8% |
| P home draw | 70.1% |
| P draw away | 55.4% |
| P home away | 74.5% |
| Raw p home draw | 57.5% |
| Raw p draw away | 73.1% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.57 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -17.7% |
| Draw probability edge | +5.1% |
| Away probability edge | +12.6% |
| Over 2.5 probability edge | -35.8% |
| Under 2.5 probability edge | +35.8% |
| Raw edge prob home | -0.3547 |
| Raw ev home | -0.5676 |
| Raw edge prob draw | 0.1017 |
| Raw ev draw | 0.4293 |
| Raw edge prob away | 0.2530 |
| Raw ev away | 1.3438 |
| Market p home draw | 82.2% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:43:55Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.9% |
| Market draw away odds | 2.52 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:37Z |
| Market reference draw away last update utc | 2026-10-20T05:43:55Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.8% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:43:55Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.17 |
| Market reference dc draw away odds | 2.47 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 84.3% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.0% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.3% |
| Market btts yes odds | 1.59 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:37Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **77.1%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.4%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 68.8%; Under 3.5 goals: 50.7%; Double Chance 1X: 90.6%; Double Chance X2: 22.9%; Double Chance 12 (either team wins): 86.5%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 41.3%; BTTS No (at least one team does not score): 58.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 77.1% | 1.30 |
| Draw | 13.5% | 7.40 |
| Villarreal win | 9.4% | 10.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 49.3% |
| Under 3.5 | 50.7% |
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.37% |
| 2 | 2-0 | 10.17% |
| 3 | 4-0 | 9.54% |
| 4 | 1-1 | 6.41% |
| 5 | 5-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 77.1% | 64.4% | 1.55 | +19.5% |
| Draw | 13.5% | 19.9% | 4.83 | -34.7% |
| Villarreal win | 9.4% | 15.8% | 6.33 | -40.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | b9567e9c3df909f8f6f21425b4b38d3f |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3551 |
| Dc lambda away | 0.5056 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.3% |
| P btts no | 58.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.45 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.26 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.97 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.2% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.1% |
| Raw p btts yes | 38.1% |
| P home draw | 90.6% |
| P draw away | 22.9% |
| P home away | 86.5% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.53 |
| Reference draw odds | 4.75 |
| Reference away odds | 5.95 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +12.8% |
| Draw probability edge | -6.4% |
| Away probability edge | -6.4% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | 0.2552 |
| Raw ev home | 0.3930 |
| Raw edge prob draw | -0.1274 |
| Raw ev draw | -0.6546 |
| Raw edge prob away | -0.1278 |
| Raw ev away | -0.8117 |
| Market p home draw | 84.0% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:43:55Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.9% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:37Z |
| Market reference draw away last update utc | 2026-10-20T05:43:55Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.2% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:43:55Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.62 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 85.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 6.10 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.4% |
| Market under 3 5 odds | 1.73 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:37Z |
| Market reference btts yes odds | 1.54 |
| Market reference btts yes opposite odds | 2.35 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **82.6%**. Expected goals are 1.97 for Manchester City and 0.39 for AEK Athens (2.36 combined). The most likely exact score is 1-0 at 20.6%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 44.6%; Under 3.5 goals: 77.4%; Double Chance 1X: 95.1%; Double Chance X2: 17.4%; Double Chance 12 (either team wins): 87.5%; Under 4.5 goals: 90.2%; BTTS Yes (both teams score): 26.1%; BTTS No (at least one team does not score): 73.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 82.6% | 1.21 |
| Draw | 12.5% | 8.03 |
| AEK Athens win | 4.9% | 20.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| AEK Athens expected goals | 0.39 |
| Expected total goals | 2.36 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.8% |
| Under 4.5 | 90.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.59% |
| 2 | 2-0 | 19.94% |
| 3 | 3-0 | 13.12% |
| 4 | 2-1 | 7.78% |
| 5 | 4-0 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 82.6% | 89.3% | 1.12 | -7.5% |
| Draw | 12.5% | 7.5% | 11.50 | +43.2% |
| AEK Athens win | 4.9% | 3.2% | 25.00 | +23.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 00625830dd764a06f12f78c0d0a72ff8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9745 |
| Dc lambda away | 0.3903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 26.1% |
| P btts no | 73.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.50 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.43 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.17 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.5% |
| P home draw | 95.1% |
| P draw away | 17.4% |
| P home away | 87.5% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.11 |
| Reference draw odds | 11.00 |
| Reference away odds | 24.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -6.7% |
| Draw probability edge | +5.0% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -33.0% |
| Under 2.5 probability edge | +33.0% |
| Raw edge prob home | -0.1344 |
| Raw ev home | -0.1501 |
| Raw edge prob draw | 0.0997 |
| Raw ev draw | 1.0050 |
| Raw edge prob away | 0.0347 |
| Raw ev away | 0.6696 |
| Market p home draw | 95.6% |
| Market home draw odds | 1.02 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:38Z |
| Market reference home draw last update utc | 2026-10-20T05:43:50Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 13.2% |
| Market draw away odds | 7.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:43:50Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 91.1% |
| Market home away odds | 1.06 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:43:50Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 7.30 |
| Market reference dc home away odds | 1.06 |
| Market p over 1 5 | 91.6% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.80 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 44.2% |
| Market under 3 5 odds | 2.13 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 2.17 |
| Market reference under 3 5 opposite odds | 1.74 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.1% |
| Market btts yes odds | 2.17 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:38Z |
| Market reference btts yes odds | 2.04 |
| Market reference btts yes opposite odds | 1.71 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **40.3%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 10.6%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 55.5%; Under 3.5 goals: 67.1%; Double Chance 1X: 62.9%; Double Chance X2: 59.7%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 40.3% | 2.48 |
| Draw | 22.6% | 4.42 |
| Bodø/Glimt win | 37.1% | 2.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.17 |
| Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 55.5% |
| Under 2.5 | 44.5% |
| Over 3.5 | 32.9% |
| Under 3.5 | 67.1% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 10.57% |
| 2 | 1-1 | 10.54% |
| 3 | 2-1 | 10.06% |
| 4 | 0-1 | 7.03% |
| 5 | 1-2 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 40.3% | 55.2% | 1.79 | -27.8% |
| Draw | 22.6% | 23.0% | 4.31 | -2.6% |
| Bodø/Glimt win | 37.1% | 21.9% | 4.62 | +71.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 49dba87d5ac664efdf2a64c72db31702 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:34Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.1660 |
| Dc lambda away | 1.7783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.84 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.04 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.91 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 62.9% |
| P draw away | 59.7% |
| P home away | 77.4% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.77 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -14.8% |
| Draw probability edge | -0.4% |
| Away probability edge | +15.2% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.2965 |
| Raw ev home | -0.5435 |
| Raw edge prob draw | -0.0075 |
| Raw ev draw | -0.0418 |
| Raw edge prob away | 0.3040 |
| Raw ev away | 1.4147 |
| Market p home draw | 78.1% |
| Market home draw odds | 1.24 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:01Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.7% |
| Market draw away odds | 2.18 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:44:01Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.2% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:44:01Z |
| Market reference home away last update utc | 2026-10-20T05:44:01Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.24 |
| Market reference dc draw away odds | 2.12 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 83.6% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.5% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.8% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:01Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-20T05:44:01Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.1%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.3%; Double Chance 1X: 72.8%; Double Chance X2: 44.9%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 51.0%; BTTS Yes (both teams score): 76.8%; BTTS No (at least one team does not score): 23.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.1% | 1.82 |
| Draw | 17.7% | 5.65 |
| Barcelona win | 27.2% | 3.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.22 |
| Barcelona expected goals | 1.52 |
| Expected total goals | 4.75 |
| Over 0.5 | 99.2% |
| Under 0.5 | 0.8% |
| Over 1.5 | 94.1% |
| Under 1.5 | 5.9% |
| Over 2.5 | 83.6% |
| Under 2.5 | 16.4% |
| Over 3.5 | 67.7% |
| Under 3.5 | 32.3% |
| Over 4.5 | 49.0% |
| Under 4.5 | 51.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.68% |
| 2 | 1-2 | 5.85% |
| 3 | 3-1 | 5.73% |
| 4 | 2-1 | 5.33% |
| 5 | 1-1 | 5.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.1% | 39.1% | 2.52 | +38.8% |
| Draw | 17.7% | 21.5% | 4.51 | -20.1% |
| Barcelona win | 27.2% | 39.3% | 2.52 | -31.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 46b790335fa98338b7e1ed0b614078fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.2230 |
| Dc lambda away | 1.5228 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.8% |
| P btts no | 23.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 119.44 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.83 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.09 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.10 |
| Fair Over 4.5 odds | 2.04 |
| Fair Under 4.5 odds | 1.96 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.3% |
| Raw p btts yes | 74.9% |
| P home draw | 72.8% |
| P draw away | 44.9% |
| P home away | 82.3% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.49 |
| Reference draw odds | 4.45 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.60 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +15.9% |
| Draw probability edge | -3.8% |
| Away probability edge | -12.1% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | 0.3188 |
| Raw ev home | 0.7897 |
| Raw edge prob draw | -0.0768 |
| Raw ev draw | -0.3747 |
| Raw edge prob away | -0.2419 |
| Raw ev away | -0.6191 |
| Market p home draw | 60.8% |
| Market home draw odds | 1.59 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:43:55Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.2% |
| Market draw away odds | 1.59 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:43:55Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.0% |
| Market home away odds | 1.25 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:43:38Z |
| Market reference home away last update utc | 2026-10-20T05:43:55Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.58 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 98.3% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-20T05:43:57Z |
| Market reference over 1 5 odds | 1.01 |
| Market reference over 1 5 opposite odds | 11.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 36.1% |
| Market under 3 5 odds | 2.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-20T05:43:57Z |
| Market reference under 3 5 odds | 2.44 |
| Market reference under 3 5 opposite odds | 1.48 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:57Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 82.3% |
| Market btts yes odds | 1.25 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:38Z |
| Market reference btts yes odds | 1.18 |
| Market reference btts yes opposite odds | 4.37 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **61.1%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.7%; Under 3.5 goals: 58.3%; Double Chance 1X: 80.9%; Double Chance X2: 38.9%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 61.1% | 1.64 |
| Draw | 19.8% | 5.04 |
| PSV Eindhoven win | 19.1% | 5.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 63.7% |
| Under 2.5 | 36.3% |
| Over 3.5 | 41.7% |
| Under 3.5 | 58.3% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.08% |
| 2 | 1-1 | 8.89% |
| 3 | 1-0 | 8.66% |
| 4 | 2-0 | 8.63% |
| 5 | 3-1 | 7.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 61.1% | 62.8% | 1.60 | -2.2% |
| Draw | 19.8% | 20.0% | 4.78 | -5.2% |
| PSV Eindhoven win | 19.1% | 17.3% | 5.60 | +6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 0686ce05e8489734fd66e5ee97fbbfa2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1110 |
| Dc lambda away | 1.1672 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.03 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.09 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.27 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 80.9% |
| P draw away | 38.9% |
| P home away | 80.2% |
| Raw p home draw | 79.1% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.65 |
| Reference away odds | 5.35 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -1.6% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | -0.0330 |
| Raw ev home | -0.0486 |
| Raw edge prob draw | -0.0030 |
| Raw ev draw | -0.0591 |
| Raw edge prob away | 0.0360 |
| Raw ev away | 0.1678 |
| Market p home draw | 83.0% |
| Market home draw odds | 1.19 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:02Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.7% |
| Market draw away odds | 2.51 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:44:02Z |
| Market reference draw away last update utc | 2026-10-20T05:44:02Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:44:02Z |
| Market reference home away last update utc | 2026-10-20T05:44:02Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.17 |
| Market reference dc draw away odds | 2.51 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 83.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.2% |
| Market under 3 5 odds | 1.59 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:02Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-20T05:44:09Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **75.7%**. Expected goals are 0.75 for Sabah FK and 2.48 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.5%; Double Chance 1X: 24.3%; Double Chance X2: 90.8%; Double Chance 12 (either team wins): 85.0%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.2% | 10.83 |
| Draw | 15.0% | 6.65 |
| Borussia Dortmund win | 75.7% | 1.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.48 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.17% |
| 2 | 0-1 | 10.20% |
| 3 | 0-3 | 10.04% |
| 4 | 1-2 | 9.18% |
| 5 | 1-3 | 7.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.2% | 8.8% | 10.40 | -3.9% |
| Draw | 15.0% | 15.2% | 6.15 | -7.5% |
| Borussia Dortmund win | 75.7% | 76.0% | 1.32 | -0.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T16:45:00+00:00 |
| Fixture id | 464c74a35c648d4910cc16976ce2f7cd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7544 |
| Dc lambda away | 2.4751 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.54 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.45 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.1% |
| P home draw | 24.3% |
| P draw away | 90.8% |
| P home away | 85.0% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 10.25 |
| Reference draw odds | 6.05 |
| Reference away odds | 1.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.0093 |
| Raw ev home | 0.0092 |
| Raw edge prob draw | -0.0036 |
| Raw ev draw | -0.0858 |
| Raw edge prob away | -0.0057 |
| Raw ev away | -0.0043 |
| Market p home draw | 25.6% |
| Market home draw odds | 3.77 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:37Z |
| Market reference home draw last update utc | 2026-10-20T05:43:55Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 90.7% |
| Market draw away odds | 1.08 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:37Z |
| Market reference draw away last update utc | 2026-10-20T05:43:55Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.6% |
| Market home away odds | 1.16 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:43:55Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.75 |
| Market reference dc draw away odds | 1.06 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 85.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 6.00 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 56.2% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:43:34Z |
| Market reference under 3 5 odds | 1.73 |
| Market reference under 3 5 opposite odds | 2.19 |
| Market reference under 3 5 last update utc | 2026-10-20T05:43:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 51.2% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:37Z |
| Market reference btts yes odds | 1.82 |
| Market reference btts yes opposite odds | 1.90 |
| Market reference btts yes last update utc | 2026-10-20T05:43:50Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.3%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.4%; Under 3.5 goals: 53.6%; Double Chance 1X: 49.7%; Double Chance X2: 72.5%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 72.8%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 27.5% | 3.63 |
| Draw | 22.2% | 4.50 |
| Atlético Madrid win | 50.3% | 1.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.41 |
| Atlético Madrid expected goals | 2.10 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.28% |
| 2 | 1-2 | 8.70% |
| 3 | 2-2 | 7.24% |
| 4 | 2-1 | 6.59% |
| 5 | 0-1 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 27.5% | 28.9% | 3.38 | -7.0% |
| Draw | 22.2% | 24.3% | 4.00 | -11.2% |
| Atlético Madrid win | 50.3% | 46.9% | 2.13 | +7.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-20T19:00:00+00:00 |
| Fixture id | 56989e10c299aba1a0fce210bb214775 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4143 |
| Dc lambda away | 2.0955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.63 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.14 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.68 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 65.9% |
| P home draw | 49.7% |
| P draw away | 72.5% |
| P home away | 77.8% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.07 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.78 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -1.3% |
| Draw probability edge | -2.1% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.0266 |
| Raw ev home | -0.1145 |
| Raw edge prob draw | -0.0410 |
| Raw ev draw | -0.1941 |
| Raw edge prob away | 0.0676 |
| Raw ev away | 0.1428 |
| Market p home draw | 54.4% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:01Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.2% |
| Market draw away odds | 1.37 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:44:01Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-20T05:44:01Z |
| Market reference home away last update utc | 2026-10-20T05:44:01Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 90.1% |
| Market over 1 5 odds | 1.08 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-20T05:43:56Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 5.45 |
| Market reference over 1 5 last update utc | 2026-10-20T05:43:56Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.0% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-20T05:43:56Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.13 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 67.1% |
| Market btts yes odds | 1.41 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:01Z |
| Market reference btts yes odds | 1.48 |
| Market reference btts yes opposite odds | 2.98 |
| Market reference btts yes last update utc | 2026-10-20T05:44:09Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **82.5%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.1%; Under 3.5 goals: 24.7%; Double Chance 1X: 93.4%; Double Chance X2: 17.5%; Double Chance 12 (either team wins): 89.1%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 82.5% | 1.21 |
| Draw | 10.9% | 9.20 |
| Viking FK win | 6.6% | 15.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 4.01 |
| Viking FK expected goals | 1.16 |
| Expected total goals | 5.17 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 75.3% |
| Under 3.5 | 24.7% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.84% |
| 2 | 3-1 | 6.83% |
| 3 | 4-0 | 5.88% |
| 4 | 3-0 | 5.87% |
| 5 | 5-1 | 5.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 82.5% | 79.5% | 1.26 | +4.0% |
| Draw | 10.9% | 13.5% | 6.88 | -25.2% |
| Viking FK win | 6.6% | 7.0% | 12.70 | -16.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d3b3e714b6af9e5430e3030ed639e6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.0057 |
| Dc lambda away | 1.1640 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.3% |
| P btts no | 31.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 173.32 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.66 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.41 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.05 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.4% |
| P draw away | 17.5% |
| P home away | 89.1% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.24 |
| Reference draw odds | 6.50 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +3.1% |
| Draw probability edge | -2.7% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +11.2% |
| Under 2.5 probability edge | -11.2% |
| Raw edge prob home | 0.0617 |
| Raw ev home | 0.0790 |
| Raw edge prob draw | -0.0531 |
| Raw ev draw | -0.4350 |
| Raw edge prob away | -0.0087 |
| Raw ev away | -0.2183 |
| Market p home draw | 90.3% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:02Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 25.0% |
| Market draw away odds | 4.53 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:02Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.7% |
| Market home away odds | 1.14 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.05 |
| Market reference dc draw away odds | 3.80 |
| Market reference dc home away odds | 1.12 |
| Market p over 1 5 | 91.3% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 8.00 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.3% |
| Market under 3 5 odds | 2.19 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 2.19 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.9% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:02Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.25 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **38.1%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.6%; Double Chance 1X: 63.6%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 38.1% | 2.62 |
| Draw | 25.5% | 3.92 |
| Arsenal win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.02 |
| Arsenal expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.61% |
| 2 | 1-1 | 11.90% |
| 3 | 0-1 | 11.11% |
| 4 | 0-0 | 8.76% |
| 5 | 2-1 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 38.1% | 46.6% | 2.14 | -18.4% |
| Draw | 25.5% | 24.5% | 4.01 | +2.3% |
| Arsenal win | 36.4% | 28.8% | 3.40 | +23.6% |
| Over 2.5 | 41.2% | 60.5% | 1.65 | -32.0% |
| Under 2.5 | 58.8% | 39.5% | 2.45 | +44.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 2ebbccdeea2dab59717d5c3d802c3fed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:34Z |
| Market best away last update utc | 2026-10-20T05:43:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0183 |
| Dc lambda away | 1.3101 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.41 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.91 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.53 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 63.6% |
| P draw away | 61.9% |
| P home away | 74.5% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.08 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -8.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +7.5% |
| Over 2.5 probability edge | -19.3% |
| Under 2.5 probability edge | +19.3% |
| Raw edge prob home | -0.1701 |
| Raw ev home | -0.3662 |
| Raw edge prob draw | 0.0193 |
| Raw ev draw | 0.0619 |
| Raw edge prob away | 0.1508 |
| Raw ev away | 0.4927 |
| Market p home draw | 70.1% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.1% |
| Market draw away odds | 1.84 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:44:01Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.35 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 81.7% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.7% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:01Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.45 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **60.3%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 6.8%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.4%; Under 3.5 goals: 39.2%; Double Chance 1X: 79.0%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 70.5%; BTTS No (at least one team does not score): 29.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 60.3% | 1.66 |
| Draw | 18.7% | 5.36 |
| RC Lens win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 3.05 |
| RC Lens expected goals | 1.27 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.5% |
| Under 0.5 | 1.5% |
| Over 1.5 | 91.9% |
| Under 1.5 | 8.1% |
| Over 2.5 | 78.4% |
| Under 2.5 | 21.6% |
| Over 3.5 | 60.8% |
| Under 3.5 | 39.2% |
| Over 4.5 | 41.0% |
| Under 4.5 | 59.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.80% |
| 2 | 1-1 | 6.65% |
| 3 | 3-1 | 6.57% |
| 4 | 2-1 | 6.46% |
| 5 | 1-2 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 60.3% | 47.4% | 2.10 | +26.7% |
| Draw | 18.7% | 23.6% | 4.11 | -23.3% |
| RC Lens win | 21.0% | 29.0% | 3.37 | -29.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d306a78e402e5f505e8644fdf3f75dcd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0508 |
| Dc lambda away | 1.2727 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.5% |
| P btts no | 29.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 68.82 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.29 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.63 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.55 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.69 |
| Unadjusted home-win probability | 73.3% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 92.7% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 68.3% |
| P home draw | 79.0% |
| P draw away | 39.7% |
| P home away | 81.3% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.05 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +13.0% |
| Draw probability edge | -4.9% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | +12.1% |
| Under 2.5 probability edge | -12.1% |
| Raw edge prob home | 0.2591 |
| Raw ev home | 0.5385 |
| Raw edge prob draw | -0.0989 |
| Raw ev draw | -0.4361 |
| Raw edge prob away | -0.1602 |
| Raw ev away | -0.5614 |
| Market p home draw | 70.8% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.8% |
| Market draw away odds | 1.83 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:44:01Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 86.0% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.7% |
| Market under 3 5 odds | 1.74 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.74 |
| Market reference under 3 5 opposite odds | 2.16 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.0% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:01Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.75 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **51.5%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.1%; Under 3.5 goals: 27.8%; Double Chance 1X: 72.2%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 46.5%; BTTS Yes (both teams score): 82.2%; BTTS No (at least one team does not score): 17.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 51.5% | 1.94 |
| Draw | 20.6% | 4.85 |
| Manchester United win | 27.8% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.99 |
| Manchester United expected goals | 1.94 |
| Expected total goals | 4.93 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 95.5% |
| Under 1.5 | 4.5% |
| Over 2.5 | 86.1% |
| Under 2.5 | 13.9% |
| Over 3.5 | 72.2% |
| Under 3.5 | 27.8% |
| Over 4.5 | 53.5% |
| Under 4.5 | 46.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.68% |
| 2 | 2-1 | 5.40% |
| 3 | 3-1 | 5.39% |
| 4 | 3-2 | 5.23% |
| 5 | 1-1 | 5.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 51.5% | 43.4% | 2.29 | +18.0% |
| Draw | 20.6% | 24.9% | 3.90 | -19.6% |
| Manchester United win | 27.8% | 31.7% | 3.10 | -13.7% |
| Over 2.5 | 86.1% | 59.2% | 1.68 | +44.6% |
| Under 2.5 | 13.9% | 40.8% | 2.38 | -66.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | 8af9379136075f45b290208b35a706c8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9925 |
| Dc lambda away | 1.9419 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.2% |
| P btts no | 17.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 154.87 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.99 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.18 |
| Fair Over 3.5 odds | 1.39 |
| Fair Under 3.5 odds | 3.59 |
| Fair Over 4.5 odds | 1.87 |
| Fair Under 4.5 odds | 2.15 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 95.5% |
| Raw p under 3 5 | 27.4% |
| Raw p btts yes | 81.2% |
| P home draw | 72.2% |
| P draw away | 48.5% |
| P home away | 79.4% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.23 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.02 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +8.1% |
| Draw probability edge | -4.3% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | +26.8% |
| Under 2.5 probability edge | -26.8% |
| Raw edge prob home | 0.1627 |
| Raw ev home | 0.3667 |
| Raw edge prob draw | -0.0864 |
| Raw ev draw | -0.3645 |
| Raw edge prob away | -0.0764 |
| Raw ev away | -0.2552 |
| Market p home draw | 67.8% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:44:01Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.6% |
| Market draw away odds | 1.70 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.40 |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 83.0% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-20T05:43:06Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 61.6% |
| Market under 3 5 odds | 1.58 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.58 |
| Market reference under 3 5 opposite odds | 2.47 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-20T05:43:50Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **73.5%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.6%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 59.2%; Under 3.5 goals: 64.2%; Double Chance 1X: 88.7%; Double Chance X2: 26.5%; Double Chance 12 (either team wins): 84.8%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 50.4%; BTTS No (at least one team does not score): 49.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.5% | 1.36 |
| Draw | 15.2% | 6.58 |
| Shakhtar Donetsk win | 11.3% | 8.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.60% |
| 2 | 2-0 | 12.35% |
| 3 | 2-1 | 11.38% |
| 4 | 3-0 | 8.45% |
| 5 | 3-1 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.5% | 82.9% | 1.21 | -11.1% |
| Draw | 15.2% | 10.9% | 8.35 | +26.9% |
| Shakhtar Donetsk win | 11.3% | 6.2% | 14.20 | +61.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | a889456204e8ef1b64294efbee8dc3e5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0511 |
| Dc lambda away | 0.9214 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.4% |
| P btts no | 49.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.65 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.05 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.79 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.7% |
| P draw away | 26.5% |
| P home away | 84.8% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.19 |
| Reference draw odds | 7.80 |
| Reference away odds | 13.25 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.75 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -9.5% |
| Draw probability edge | +4.3% |
| Away probability edge | +5.2% |
| Over 2.5 probability edge | -17.2% |
| Under 2.5 probability edge | +17.2% |
| Raw edge prob home | -0.1890 |
| Raw ev home | -0.2256 |
| Raw edge prob draw | 0.0855 |
| Raw ev draw | 0.6260 |
| Raw edge prob away | 0.1035 |
| Raw ev away | 1.3464 |
| Market p home draw | 92.0% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:44:12Z |
| Market reference home draw last update utc | 2026-10-20T05:44:12Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 19.4% |
| Market draw away odds | 5.03 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:44:12Z |
| Market reference draw away last update utc | 2026-10-20T05:44:12Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.6% |
| Market home away odds | 1.10 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:12Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 5.03 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 92.2% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 8.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 43.6% |
| Market under 3 5 odds | 2.18 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 2.18 |
| Market reference under 3 5 opposite odds | 1.71 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.5% |
| Market btts yes odds | 1.74 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:12Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.14 |
| Market reference btts yes last update utc | 2026-10-20T05:44:12Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.7%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.2%; Double Chance X2: 42.3%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.7% | 1.73 |
| Draw | 20.5% | 4.87 |
| Galatasaray win | 21.8% | 4.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 2.57 |
| Galatasaray expected goals | 1.04 |
| Expected total goals | 3.61 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 46.5% |
| Under 3.5 | 53.5% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.97% |
| 2 | 2-1 | 7.58% |
| 3 | 2-0 | 7.31% |
| 4 | 3-1 | 6.49% |
| 5 | 2-2 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.7% | 44.7% | 2.23 | +28.7% |
| Draw | 20.5% | 25.3% | 3.84 | -21.1% |
| Galatasaray win | 21.8% | 30.0% | 3.27 | -28.9% |
| Over 2.5 | 67.2% | 59.7% | 1.67 | +12.2% |
| Under 2.5 | 32.8% | 40.3% | 2.41 | -20.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T16:45:00+00:00 |
| Fixture id | 015d619d774655965e17ba67a025634e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5689 |
| Dc lambda away | 1.0368 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.53 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.05 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 70.8% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 59.2% |
| P home draw | 78.2% |
| P draw away | 42.3% |
| P home away | 79.5% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.18 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.34 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +13.1% |
| Draw probability edge | -4.8% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +7.5% |
| Under 2.5 probability edge | -7.5% |
| Raw edge prob home | 0.2610 |
| Raw ev home | 0.5779 |
| Raw edge prob draw | -0.0960 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1650 |
| Raw ev away | -0.5584 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-20T05:43:50Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.9% |
| Market draw away odds | 1.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:44:01Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.1% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.36 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 81.7% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.52 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:01Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **76.9%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.4%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.7%; Under 3.5 goals: 7.9%; Double Chance 1X: 89.0%; Double Chance X2: 23.1%; Double Chance 12 (either team wins): 87.9%; Under 4.5 goals: 17.3%; BTTS Yes (both teams score): 82.9%; BTTS No (at least one team does not score): 17.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 76.9% | 1.30 |
| Draw | 12.1% | 8.26 |
| Feyenoord win | 11.0% | 9.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 5.75 |
| Feyenoord expected goals | 1.65 |
| Expected total goals | 7.40 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.2% |
| Under 1.5 | 0.8% |
| Over 2.5 | 96.7% |
| Under 2.5 | 3.3% |
| Over 3.5 | 92.1% |
| Under 3.5 | 7.9% |
| Over 4.5 | 82.7% |
| Under 4.5 | 17.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.45% |
| 2 | 6-1 | 4.26% |
| 3 | 4-1 | 3.87% |
| 4 | 3-3 | 3.73% |
| 5 | 5-2 | 3.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 76.9% | 62.3% | 1.61 | +23.9% |
| Draw | 12.1% | 19.5% | 4.88 | -40.9% |
| Feyenoord win | 11.0% | 18.1% | 5.24 | -42.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | f5905225efa837b0dc89b7dcdbb6c625 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.7507 |
| Dc lambda away | 1.6458 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 82.9% |
| P btts no | 17.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1197.01 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 127.86 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.29 |
| Fair Over 3.5 odds | 1.09 |
| Fair Under 3.5 odds | 12.72 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.79 |
| Unadjusted home-win probability | 91.5% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 89.0% |
| P draw away | 23.1% |
| P home away | 87.9% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.5% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.57 |
| Reference draw odds | 4.75 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +14.6% |
| Draw probability edge | -7.4% |
| Away probability edge | -7.2% |
| Over 2.5 probability edge | +25.2% |
| Under 2.5 probability edge | -25.2% |
| Raw edge prob home | 0.2922 |
| Raw ev home | 0.4739 |
| Raw edge prob draw | -0.1485 |
| Raw ev draw | -0.7714 |
| Raw edge prob away | -0.1436 |
| Raw ev away | -0.8025 |
| Market p home draw | 80.7% |
| Market home draw odds | 1.21 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:38Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.0% |
| Market draw away odds | 2.52 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:38Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.3% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.38 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.3% |
| Market under 3 5 odds | 1.93 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 1.93 |
| Market reference under 3 5 opposite odds | 1.95 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.7% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:38Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.70 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **77.9%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 10.0%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 71.2%; Under 3.5 goals: 49.8%; Double Chance 1X: 90.9%; Double Chance X2: 22.1%; Double Chance 12 (either team wins): 86.9%; Under 4.5 goals: 69.1%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.9% | 1.28 |
| Draw | 13.1% | 7.66 |
| RB Leipzig win | 9.1% | 11.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 50.2% |
| Under 3.5 | 49.8% |
| Over 4.5 | 30.9% |
| Under 4.5 | 69.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.95% |
| 2 | 3-0 | 9.29% |
| 3 | 2-1 | 8.73% |
| 4 | 3-1 | 8.15% |
| 5 | 1-0 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.9% | 78.2% | 1.29 | +0.4% |
| Draw | 13.1% | 13.0% | 7.18 | -6.3% |
| RB Leipzig win | 9.1% | 8.9% | 10.20 | -7.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 30f27b8e9719e9ae71c25b4c8aa265f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:34Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8012 |
| Dc lambda away | 0.8770 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.44 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.27 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.23 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 77.6% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.9% |
| P draw away | 22.1% |
| P home away | 86.9% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.4% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.26 |
| Reference draw odds | 6.80 |
| Reference away odds | 9.70 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.55 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -10.4% |
| Under 2.5 probability edge | +10.4% |
| Raw edge prob home | -0.0061 |
| Raw ev home | 0.0004 |
| Raw edge prob draw | 0.0018 |
| Raw ev draw | -0.0563 |
| Raw edge prob away | 0.0043 |
| Raw ev away | -0.0509 |
| Market p home draw | 89.1% |
| Market home draw odds | 1.08 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:43:49Z |
| Market reference home draw last update utc | 2026-10-20T05:44:10Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 25.1% |
| Market draw away odds | 4.27 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-20T05:43:49Z |
| Market reference draw away last update utc | 2026-10-20T05:44:10Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 85.9% |
| Market home away odds | 1.13 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:10Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.07 |
| Market reference dc draw away odds | 3.80 |
| Market reference dc home away odds | 1.11 |
| Market p over 1 5 | 93.4% |
| Market over 1 5 odds | 1.02 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-20T05:43:56Z |
| Market reference over 1 5 odds | 1.06 |
| Market reference over 1 5 opposite odds | 10.00 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 37.8% |
| Market under 3 5 odds | 2.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 2.45 |
| Market reference under 3 5 opposite odds | 1.55 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:43:49Z |
| Market reference btts yes odds | 1.50 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-20T05:44:10Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.7%**. Expected goals are 6.10 for Sporting Lisbon and 1.31 for LASK (7.41 combined). The most likely exact score is 6-1 at 5.3%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 97.0%; Under 3.5 goals: 7.2%; Double Chance 1X: 95.7%; Double Chance X2: 11.3%; Double Chance 12 (either team wins): 93.0%; Under 4.5 goals: 15.9%; BTTS Yes (both teams score): 74.5%; BTTS No (at least one team does not score): 25.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.7% | 1.13 |
| Draw | 7.0% | 14.19 |
| LASK win | 4.3% | 23.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 6.10 |
| LASK expected goals | 1.31 |
| Expected total goals | 7.41 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.3% |
| Under 1.5 | 0.7% |
| Over 2.5 | 97.0% |
| Under 2.5 | 3.0% |
| Over 3.5 | 92.8% |
| Under 3.5 | 7.2% |
| Over 4.5 | 84.1% |
| Under 4.5 | 15.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.28% |
| 2 | 5-1 | 5.19% |
| 3 | 7-1 | 4.60% |
| 4 | 4-1 | 4.26% |
| 5 | 6-0 | 4.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.7% | 82.2% | 1.22 | +8.2% |
| Draw | 7.0% | 11.2% | 8.25 | -41.9% |
| LASK win | 4.3% | 6.6% | 13.40 | -42.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 8fdcaee14b3e8966e09d468a0b17ce18 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:43:50Z |
| Market best draw last update utc | 2026-10-20T05:43:50Z |
| Market best away last update utc | 2026-10-20T05:43:50Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 6.0990 |
| Dc lambda away | 1.3147 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:57.422675+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 74.5% |
| P btts no | 25.5% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1153.56 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 145.88 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 33.89 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.85 |
| Fair Over 4.5 odds | 1.19 |
| Fair Under 4.5 odds | 6.29 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 73.0% |
| P home draw | 95.7% |
| P draw away | 11.3% |
| P home away | 93.0% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.20 |
| Reference draw odds | 7.70 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:55Z |
| Market reference home last update utc | 2026-10-20T05:43:55Z |
| Market reference draw last update utc | 2026-10-20T05:43:55Z |
| Market reference away last update utc | 2026-10-20T05:43:55Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.55 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:50Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:50Z |
| Home probability edge | +6.5% |
| Draw probability edge | -4.1% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | +22.0% |
| Under 2.5 probability edge | -22.0% |
| Raw edge prob home | 0.1297 |
| Raw ev home | 0.1612 |
| Raw edge prob draw | -0.0822 |
| Raw ev draw | -0.7578 |
| Raw edge prob away | -0.0474 |
| Raw ev away | -0.7474 |
| Market p home draw | 91.5% |
| Market home draw odds | 1.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-20T05:44:12Z |
| Market reference home draw last update utc | 2026-10-20T05:44:12Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 20.3% |
| Market draw away odds | 4.84 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-20T05:43:50Z |
| Market reference draw away last update utc | 2026-10-20T05:44:12Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.2% |
| Market home away odds | 1.10 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-20T05:43:50Z |
| Market reference home away last update utc | 2026-10-20T05:44:12Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.06 |
| Market reference dc draw away odds | 4.78 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 91.2% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-20T05:44:10Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.1% |
| Market under 3 5 odds | 2.09 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market reference under 3 5 odds | 2.09 |
| Market reference under 3 5 opposite odds | 1.80 |
| Market reference under 3 5 last update utc | 2026-10-20T05:44:08Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.1% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-20T05:44:12Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-20T05:44:12Z |
| Market btts yes bookmakers | 2 |

</details>


---
