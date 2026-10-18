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
| Training sha256 | d02f9e12c96d4487c683b5a45d892a02fc56ca12e5677b7f8cac0fe2b9f6adde |
| Training as of utc | 2026-10-18T14:35:00.015368+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 36, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 27, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T14:35:00.015368+00:00', 'observations': 54, 'observations_sha256': '0edc36b296a2e980e3a8e9c1bb30620bc3d5c291e8f29f1e98b505cc0aae317e', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 27, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '0f92b6373ad88e018690d9fe5ac866058277e3f45e0e3443c662a063cc8fbad1', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 967.004 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-18T14:34:55.859952+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '2217b36d746063d412e90f633195640580308995d5c6ce928aa37c3aa5a6809e', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.0011542822222222221, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 14.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261018T143500015368Z_f87c3aa39aa7d4e95b961b1ed1464f21653e42658263f5b484f925fc3940bacc.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

The model's most likely 1X2 outcome is **AS Roma win** at **82.4%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.07 combined). The most likely exact score is 3-1 at 7.4%. Goal-market probabilities: at least one goal: 99.5%; Over 2.5 goals: 88.1%; Under 3.5 goals: 25.1%; Double Chance 1X: 93.2%; Double Chance X2: 17.6%; Double Chance 12 (either team wins): 89.2%; Under 4.5 goals: 42.7%; BTTS Yes (both teams score): 71.3%; BTTS No (at least one team does not score): 28.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 82.4% | 1.21 |
| Draw | 10.8% | 9.25 |
| ŠK Slovan Bratislava win | 6.8% | 14.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.07 |
| Over 0.5 | 99.5% |
| Under 0.5 | 0.5% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.1% |
| Under 2.5 | 11.9% |
| Over 3.5 | 74.9% |
| Under 3.5 | 25.1% |
| Over 4.5 | 57.3% |
| Under 4.5 | 42.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.40% |
| 2 | 4-1 | 6.96% |
| 3 | 2-1 | 5.91% |
| 4 | 3-0 | 5.63% |
| 5 | 4-0 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 82.4% | 83.7% | 1.19 | -1.9% |
| Draw | 10.8% | 11.5% | 8.15 | -11.9% |
| ŠK Slovan Bratislava win | 6.8% | 4.8% | 18.00 | +21.9% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.7583 |
| Dc lambda away | 1.3152 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 71.3% |
| P btts no | 28.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 198.75 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.27 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.43 |
| Fair Over 3.5 odds | 1.34 |
| Fair Under 3.5 odds | 3.98 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.34 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.2% |
| P draw away | 17.6% |
| P home away | 89.2% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.18 |
| Reference draw odds | 7.50 |
| Reference away odds | 17.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | -1.3% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +13.6% |
| Under 2.5 probability edge | -13.6% |
| Raw edge prob home | -0.0262 |
| Raw ev home | -0.0349 |
| Raw edge prob draw | -0.0137 |
| Raw ev draw | -0.1743 |
| Raw edge prob away | 0.0399 |
| Raw ev away | 0.5780 |
| Market p home draw | 94.3% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 18.3% |
| Market draw away odds | 5.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 87.4% |
| Market home away odds | 1.11 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 5.25 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 90.5% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:34:43Z |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.6% |
| Market under 3 5 odds | 2.08 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:34:43Z |
| Market reference under 3 5 odds | 1.95 |
| Market reference under 3 5 opposite odds | 1.73 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.88 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **42.3%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 86.9%; Over 2.5 goals: 28.7%; Under 3.5 goals: 88.7%; Double Chance 1X: 68.8%; Double Chance X2: 57.7%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.9%; BTTS No (at least one team does not score): 66.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 42.3% | 2.36 |
| Draw | 26.5% | 3.78 |
| Slavia Praha win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 86.9% |
| Under 0.5 | 13.1% |
| Over 1.5 | 53.6% |
| Under 1.5 | 46.4% |
| Over 2.5 | 28.7% |
| Under 2.5 | 71.3% |
| Over 3.5 | 11.3% |
| Under 3.5 | 88.7% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.40% |
| 2 | 0-0 | 13.13% |
| 3 | 0-1 | 12.87% |
| 4 | 1-1 | 10.77% |
| 5 | 2-1 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 42.3% | 57.8% | 1.74 | -26.4% |
| Draw | 26.5% | 22.3% | 4.31 | +14.1% |
| Slavia Praha win | 31.2% | 19.9% | 4.83 | +50.7% |
| Over 2.5 | 28.7% | 58.9% | 1.69 | -51.5% |
| Under 2.5 | 71.3% | 41.1% | 2.36 | +68.3% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fenerbahçe SK |
| Matched away-team name | SK Slavia Praha |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7760 |
| Dc lambda away | 1.0670 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 33.9% |
| P btts no | 66.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.62 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.16 |
| Fair Over 2.5 odds | 3.48 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.89 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.97 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.9% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 68.8% |
| P draw away | 57.7% |
| P home away | 73.5% |
| Raw p home draw | 57.5% |
| Raw p draw away | 73.1% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.69 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:53Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:53Z |
| Home probability edge | -15.5% |
| Draw probability edge | +4.1% |
| Away probability edge | +11.3% |
| Over 2.5 probability edge | -30.2% |
| Under 2.5 probability edge | +30.2% |
| Raw edge prob home | -0.3095 |
| Raw ev home | -0.5328 |
| Raw edge prob draw | 0.0828 |
| Raw ev draw | 0.3193 |
| Raw edge prob away | 0.2268 |
| Raw ev away | 1.0546 |
| Market p home draw | 79.6% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.4% |
| Market draw away odds | 2.23 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.0% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.21 |
| Market reference dc draw away odds | 2.22 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.6% |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-18T14:34:53Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **77.8%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 69.1%; Under 3.5 goals: 50.4%; Double Chance 1X: 91.1%; Double Chance X2: 22.2%; Double Chance 12 (either team wins): 86.7%; Under 4.5 goals: 69.1%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 77.8% | 1.28 |
| Draw | 13.3% | 7.51 |
| Villarreal win | 8.9% | 11.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.4% |
| Under 1.5 | 13.6% |
| Over 2.5 | 69.1% |
| Under 2.5 | 30.9% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.9% |
| Under 4.5 | 69.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.48% |
| 2 | 2-0 | 10.26% |
| 3 | 4-0 | 9.63% |
| 4 | 5-0 | 6.46% |
| 5 | 1-1 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 77.8% | 65.8% | 1.53 | +19.1% |
| Draw | 13.3% | 19.5% | 4.88 | -35.0% |
| Villarreal win | 8.9% | 14.7% | 6.36 | -43.7% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3554 |
| Dc lambda away | 0.5056 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.88 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.38 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.24 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 89.9% |
| Unadjusted draw probability | 7.2% |
| Unadjusted away-win probability | 3.0% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 46.1% |
| Raw p btts yes | 38.1% |
| P home draw | 91.1% |
| P draw away | 22.2% |
| P home away | 86.7% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.49 |
| Reference draw odds | 4.75 |
| Reference away odds | 6.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +12.0% |
| Draw probability edge | -6.2% |
| Away probability edge | -5.9% |
| Over 2.5 probability edge | +5.3% |
| Under 2.5 probability edge | -5.3% |
| Raw edge prob home | 0.2408 |
| Raw ev home | 0.3751 |
| Raw edge prob draw | -0.1233 |
| Raw ev draw | -0.6511 |
| Raw edge prob away | -0.1175 |
| Raw ev away | -0.8108 |
| Market p home draw | 84.4% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.3% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 85.1% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.8% |
| Market reference under 3 5 odds | 1.59 |
| Market reference under 3 5 opposite odds | 2.17 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.29 |
| Market reference btts yes last update utc | 2026-10-18T14:35:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **83.4%**. Expected goals are 1.97 for Manchester City and 0.39 for AEK Athens (2.37 combined). The most likely exact score is 1-0 at 20.8%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 44.9%; Under 3.5 goals: 77.3%; Double Chance 1X: 95.3%; Double Chance X2: 16.6%; Double Chance 12 (either team wins): 88.1%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 26.0%; BTTS No (at least one team does not score): 74.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 83.4% | 1.20 |
| Draw | 11.9% | 8.37 |
| AEK Athens win | 4.7% | 21.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| AEK Athens expected goals | 0.39 |
| Expected total goals | 2.37 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 70.2% |
| Under 1.5 | 29.8% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 22.7% |
| Under 3.5 | 77.3% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.77% |
| 2 | 2-0 | 20.12% |
| 3 | 3-0 | 13.25% |
| 4 | 2-1 | 7.86% |
| 5 | 4-0 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 83.4% | 90.9% | 1.10 | -8.3% |
| Draw | 11.9% | 6.5% | 14.10 | +68.4% |
| AEK Athens win | 4.7% | 2.7% | 31.00 | +45.0% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9749 |
| Dc lambda away | 0.3904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 26.0% |
| P btts no | 74.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.16 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.36 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.40 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.08 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.5% |
| P home draw | 95.3% |
| P draw away | 16.6% |
| P home away | 88.1% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.09 |
| Reference draw odds | 11.75 |
| Reference away odds | 26.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.75 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | -7.5% |
| Draw probability edge | +5.5% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -32.8% |
| Under 2.5 probability edge | +32.8% |
| Raw edge prob home | -0.1497 |
| Raw ev home | -0.1652 |
| Raw edge prob draw | 0.1097 |
| Raw ev draw | 1.4577 |
| Raw edge prob away | 0.0401 |
| Raw ev away | 1.0705 |
| Market p home draw | 96.0% |
| Market reference home draw last update utc | 2026-10-18T14:34:52Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 10.8% |
| Market reference draw away last update utc | 2026-10-18T14:34:52Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 93.2% |
| Market reference home away last update utc | 2026-10-18T14:34:52Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.01 |
| Market reference dc draw away odds | 9.00 |
| Market reference dc home away odds | 1.04 |
| Market p over 1 5 | 91.4% |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 6.40 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.5% |
| Market reference under 3 5 odds | 1.99 |
| Market reference under 3 5 opposite odds | 1.70 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 38.2% |
| Market btts yes odds | 2.29 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 2.40 |
| Market reference btts yes opposite odds | 1.55 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.3%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.4%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 55.8%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.7%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.3% | 2.31 |
| Draw | 21.4% | 4.68 |
| Bodø/Glimt win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.17 |
| Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 55.8% |
| Under 2.5 | 44.2% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.35% |
| 2 | 2-1 | 10.81% |
| 3 | 1-1 | 9.96% |
| 4 | 0-1 | 6.69% |
| 5 | 1-2 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.3% | 61.1% | 1.64 | -28.9% |
| Draw | 21.4% | 20.5% | 4.67 | -0.3% |
| Bodø/Glimt win | 35.3% | 18.4% | 5.18 | +83.0% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.1660 |
| Dc lambda away | 1.7786 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.07 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.43 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.26 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 64.7% |
| P draw away | 56.7% |
| P home away | 78.6% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.55 |
| Reference away odds | 5.05 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | -17.8% |
| Draw probability edge | +0.9% |
| Away probability edge | +17.0% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.3565 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0175 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.3391 |
| Raw ev away | 1.7077 |
| Market p home draw | 81.0% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:04Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.7% |
| Market draw away odds | 2.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:04Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:04Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.39 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 85.9% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.6% |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 62.8% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.54 |
| Market reference btts yes last update utc | 2026-10-18T14:35:04Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.3%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.6%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.6%; Under 3.5 goals: 32.3%; Double Chance 1X: 72.7%; Double Chance X2: 44.7%; Double Chance 12 (either team wins): 82.6%; Under 4.5 goals: 50.9%; BTTS Yes (both teams score): 76.7%; BTTS No (at least one team does not score): 23.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.3% | 1.81 |
| Draw | 17.4% | 5.76 |
| Barcelona win | 27.3% | 3.66 |

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
| Over 4.5 | 49.1% |
| Under 4.5 | 50.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.55% |
| 2 | 1-2 | 5.86% |
| 3 | 3-1 | 5.75% |
| 4 | 2-1 | 5.35% |
| 5 | 1-1 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.3% | 39.7% | 2.50 | +38.3% |
| Draw | 17.4% | 20.9% | 4.62 | -19.8% |
| Barcelona win | 27.3% | 39.5% | 2.51 | -31.5% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.2229 |
| Dc lambda away | 1.5230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.7% |
| P btts no | 23.3% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 121.80 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.83 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.12 |
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
| P home draw | 72.7% |
| P draw away | 44.7% |
| P home away | 82.6% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.43 |
| Reference draw odds | 4.50 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.20 |
| Reference Under 2.5 odds | 4.40 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +15.7% |
| Draw probability edge | -3.5% |
| Away probability edge | -12.2% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | 0.3136 |
| Raw ev home | 0.7754 |
| Raw edge prob draw | -0.0700 |
| Raw ev draw | -0.3594 |
| Raw edge prob away | -0.2436 |
| Raw ev away | -0.6205 |
| Market p home draw | 60.5% |
| Market home draw odds | 1.59 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.5% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 94.6% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.80 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 35.7% |
| Market under 3 5 odds | 2.43 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 3 5 odds | 2.45 |
| Market reference under 3 5 opposite odds | 1.47 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 80.1% |
| Market btts yes odds | 1.18 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.23 |
| Market reference btts yes opposite odds | 4.50 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **59.0%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.4%; Under 3.5 goals: 58.5%; Double Chance 1X: 79.4%; Double Chance X2: 41.0%; Double Chance 12 (either team wins): 79.6%; Under 4.5 goals: 76.8%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 59.0% | 1.69 |
| Draw | 20.4% | 4.91 |
| PSV Eindhoven win | 20.6% | 4.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Porto expected goals | 2.11 |
| PSV Eindhoven expected goals | 1.17 |
| Expected total goals | 3.28 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 83.4% |
| Under 1.5 | 16.6% |
| Over 2.5 | 63.4% |
| Under 2.5 | 36.6% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.2% |
| Under 4.5 | 76.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.73% |
| 2 | 1-1 | 9.13% |
| 3 | 1-0 | 8.36% |
| 4 | 2-0 | 8.34% |
| 5 | 3-1 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 59.0% | 58.6% | 1.71 | +0.9% |
| Draw | 20.4% | 21.1% | 4.57 | -6.9% |
| PSV Eindhoven win | 20.6% | 20.4% | 4.72 | -2.7% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1111 |
| Dc lambda away | 1.1674 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.23 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.73 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.30 |
| Fair Under 4.5 odds | 1.30 |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.7% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 83.4% |
| Raw p under 3 5 | 58.5% |
| Raw p btts yes | 60.1% |
| P home draw | 79.4% |
| P draw away | 41.0% |
| P home away | 79.6% |
| Raw p home draw | 79.1% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.67 |
| Reference draw odds | 4.45 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +0.4% |
| Draw probability edge | -0.7% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0089 |
| Raw ev home | 0.0168 |
| Raw edge prob draw | -0.0139 |
| Raw ev draw | -0.1005 |
| Raw edge prob away | 0.0050 |
| Raw ev away | -0.0155 |
| Market p home draw | 79.1% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.5% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.4% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.27 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.3% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:34:57Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:57Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:34:57Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:57Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.2% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **75.3%**. Expected goals are 0.75 for Sabah FK and 2.48 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.6%; Double Chance 1X: 24.7%; Double Chance X2: 90.3%; Double Chance 12 (either team wins): 84.9%; Under 4.5 goals: 77.6%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.7% | 10.35 |
| Draw | 15.1% | 6.64 |
| Borussia Dortmund win | 75.3% | 1.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.48 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.4% |
| Under 3.5 | 59.6% |
| Over 4.5 | 22.4% |
| Under 4.5 | 77.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.10% |
| 2 | 0-1 | 10.14% |
| 3 | 0-3 | 9.98% |
| 4 | 1-2 | 9.12% |
| 5 | 1-3 | 7.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.7% | 9.6% | 9.40 | -9.1% |
| Draw | 15.1% | 15.2% | 6.11 | -8.0% |
| Borussia Dortmund win | 75.3% | 75.1% | 1.34 | +0.9% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7542 |
| Dc lambda away | 2.4756 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.52 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.84 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.48 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.46 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.1% |
| P home draw | 24.7% |
| P draw away | 90.3% |
| P home away | 84.9% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 9.10 |
| Reference draw odds | 5.90 |
| Reference away odds | 1.31 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +0.0% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0006 |
| Raw ev home | -0.0886 |
| Raw edge prob draw | -0.0039 |
| Raw ev draw | -0.0922 |
| Raw edge prob away | 0.0033 |
| Raw ev away | 0.0110 |
| Market p home draw | 26.7% |
| Market home draw odds | 3.56 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.8% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.5% |
| Market home away odds | 1.16 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.60 |
| Market reference dc draw away odds | 1.07 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 88.5% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:34:37Z |
| Market reference over 1 5 odds | 1.10 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:52Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.8% |
| Market under 3 5 odds | 1.84 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:34:37Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 1.93 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.2% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.73 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **49.8%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.4%; Under 3.5 goals: 53.7%; Double Chance 1X: 50.2%; Double Chance X2: 72.2%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 72.9%; BTTS Yes (both teams score): 66.6%; BTTS No (at least one team does not score): 33.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 27.8% | 3.60 |
| Draw | 22.4% | 4.47 |
| Atlético Madrid win | 49.8% | 2.01 |

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
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.1% |
| Under 4.5 | 72.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.36% |
| 2 | 1-2 | 8.62% |
| 3 | 2-2 | 7.30% |
| 4 | 2-1 | 6.65% |
| 5 | 0-1 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 27.8% | 29.4% | 3.33 | -7.4% |
| Draw | 22.4% | 24.6% | 3.94 | -11.8% |
| Atlético Madrid win | 49.8% | 46.0% | 2.17 | +8.1% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4143 |
| Dc lambda away | 2.0956 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.6% |
| P btts no | 33.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.33 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.13 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.69 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 65.9% |
| P home draw | 50.2% |
| P draw away | 72.2% |
| P home away | 77.6% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.24 |
| Reference draw odds | 3.84 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | -1.6% |
| Draw probability edge | -2.2% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0321 |
| Raw ev home | -0.1277 |
| Raw edge prob draw | -0.0449 |
| Raw ev draw | -0.2062 |
| Raw edge prob away | 0.0770 |
| Raw ev away | 0.1644 |
| Market p home draw | 54.5% |
| Market home draw odds | 1.77 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:33:53Z |
| Market reference home draw last update utc | 2026-10-18T14:35:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.5% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:33:53Z |
| Market reference draw away last update utc | 2026-10-18T14:35:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.9% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:33:53Z |
| Market reference home away last update utc | 2026-10-18T14:35:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 87.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:35:06Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-18T14:35:06Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:35:06Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-18T14:35:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.3% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:33:53Z |
| Market reference btts yes odds | 1.44 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-18T14:34:52Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **81.9%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 87.9%; Under 3.5 goals: 24.8%; Double Chance 1X: 93.4%; Double Chance X2: 18.1%; Double Chance 12 (either team wins): 88.5%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 68.5%; BTTS No (at least one team does not score): 31.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 81.9% | 1.22 |
| Draw | 11.5% | 8.70 |
| Viking FK win | 6.6% | 15.14 |

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
| Over 2.5 | 87.9% |
| Under 2.5 | 12.1% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.79% |
| 2 | 3-1 | 6.78% |
| 3 | 4-0 | 5.83% |
| 4 | 3-0 | 5.82% |
| 5 | 5-1 | 5.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 81.9% | 78.2% | 1.29 | +5.6% |
| Draw | 11.5% | 14.8% | 6.31 | -27.4% |
| Viking FK win | 6.6% | 7.1% | 12.60 | -16.8% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.0063 |
| Dc lambda away | 1.1642 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.5% |
| P btts no | 31.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 163.88 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.55 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.29 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.04 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.4% |
| P draw away | 18.1% |
| P home away | 88.5% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.26 |
| Reference draw odds | 6.00 |
| Reference away odds | 12.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +3.7% |
| Draw probability edge | -3.3% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | +13.7% |
| Under 2.5 probability edge | -13.7% |
| Raw edge prob home | 0.0748 |
| Raw ev home | 0.1047 |
| Raw edge prob draw | -0.0658 |
| Raw ev draw | -0.4819 |
| Raw edge prob away | -0.0091 |
| Raw ev away | -0.2246 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **37.2%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.6%; Double Chance 1X: 62.8%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.1% | 2.69 |
| Draw | 25.6% | 3.90 |
| Arsenal win | 37.2% | 2.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.02 |
| Arsenal expected goals | 1.31 |
| Expected total goals | 2.33 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 66.6% |
| Under 1.5 | 33.4% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.26% |
| 2 | 1-1 | 11.95% |
| 3 | 0-1 | 11.38% |
| 4 | 0-0 | 8.80% |
| 5 | 2-1 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.1% | 44.6% | 2.23 | -17.2% |
| Draw | 25.6% | 24.8% | 3.92 | +0.5% |
| Arsenal win | 37.2% | 30.6% | 3.21 | +19.6% |
| Over 2.5 | 41.2% | 59.2% | 1.68 | -30.8% |
| Under 2.5 | 58.8% | 40.8% | 2.38 | +40.0% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0182 |
| Dc lambda away | 1.3102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.36 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.52 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 29.6% |
| Unadjusted draw probability | 26.5% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 79.4% |
| Raw p btts yes | 46.0% |
| P home draw | 62.8% |
| P draw away | 62.9% |
| P home away | 74.4% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.17 |
| Reference draw odds | 3.82 |
| Reference away odds | 3.12 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:53Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:53Z |
| Home probability edge | -7.5% |
| Draw probability edge | +0.9% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -18.1% |
| Under 2.5 probability edge | +18.1% |
| Raw edge prob home | -0.1503 |
| Raw ev home | -0.3396 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.1332 |
| Raw ev away | 0.4094 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **59.8%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 7.0%. Goal-market probabilities: at least one goal: 98.5%; Over 2.5 goals: 78.3%; Under 3.5 goals: 39.3%; Double Chance 1X: 79.0%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 59.2%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 59.8% | 1.67 |
| Draw | 19.2% | 5.22 |
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
| Over 2.5 | 78.3% |
| Under 2.5 | 21.7% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 40.8% |
| Under 4.5 | 59.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.98% |
| 2 | 1-1 | 6.83% |
| 3 | 3-1 | 6.52% |
| 4 | 2-1 | 6.41% |
| 5 | 1-2 | 5.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 59.8% | 46.4% | 2.15 | +28.6% |
| Draw | 19.2% | 24.6% | 3.94 | -24.5% |
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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0510 |
| Dc lambda away | 1.2729 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 67.06 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.29 |
| Fair Over 2.5 odds | 1.28 |
| Fair Under 2.5 odds | 4.60 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.55 |
| Fair Over 4.5 odds | 2.45 |
| Fair Under 4.5 odds | 1.69 |
| Unadjusted home-win probability | 73.3% |
| Unadjusted draw probability | 13.7% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 92.7% |
| Raw p under 3 5 | 37.3% |
| Raw p btts yes | 68.3% |
| P home draw | 79.0% |
| P draw away | 40.2% |
| P home away | 80.8% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.84 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.44 |
| Market reference over 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:35:00Z |
| Home probability edge | +13.4% |
| Draw probability edge | -5.4% |
| Away probability edge | -8.0% |
| Over 2.5 probability edge | +16.6% |
| Under 2.5 probability edge | -16.6% |
| Raw edge prob home | 0.2688 |
| Raw ev home | 0.5751 |
| Raw edge prob draw | -0.1089 |
| Raw ev draw | -0.4594 |
| Raw edge prob away | -0.1599 |
| Raw ev away | -0.5613 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **50.7%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.94 combined). The most likely exact score is 2-2 at 7.7%. Goal-market probabilities: at least one goal: 99.3%; Over 2.5 goals: 86.0%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.4%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 46.6%; BTTS Yes (both teams score): 82.3%; BTTS No (at least one team does not score): 17.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 50.7% | 1.97 |
| Draw | 20.8% | 4.81 |
| Manchester United win | 28.6% | 3.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.99 |
| Manchester United expected goals | 1.94 |
| Expected total goals | 4.94 |
| Over 0.5 | 99.3% |
| Under 0.5 | 0.7% |
| Over 1.5 | 95.4% |
| Under 1.5 | 4.6% |
| Over 2.5 | 86.0% |
| Under 2.5 | 14.0% |
| Over 3.5 | 72.1% |
| Under 3.5 | 27.9% |
| Over 4.5 | 53.4% |
| Under 4.5 | 46.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.74% |
| 2 | 2-1 | 5.31% |
| 3 | 3-1 | 5.30% |
| 4 | 3-2 | 5.14% |
| 5 | 1-1 | 5.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 50.7% | 41.6% | 2.38 | +20.6% |
| Draw | 20.8% | 25.3% | 3.85 | -20.0% |
| Manchester United win | 28.6% | 33.1% | 2.97 | -15.2% |
| Over 2.5 | 86.0% | 58.5% | 1.70 | +46.3% |
| Under 2.5 | 14.0% | 41.5% | 2.34 | -67.3% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Como 1907 |
| Matched away-team name | Manchester United FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.9933 |
| Dc lambda away | 1.9420 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.3% |
| P btts no | 17.7% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 153.82 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.92 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.16 |
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
| P home draw | 71.4% |
| P draw away | 49.3% |
| P home away | 79.2% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.32 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.89 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.27 |
| Market reference over 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:53Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:53Z |
| Home probability edge | +9.0% |
| Draw probability edge | -4.5% |
| Away probability edge | -4.5% |
| Over 2.5 probability edge | +27.6% |
| Under 2.5 probability edge | -27.6% |
| Raw edge prob home | 0.1806 |
| Raw ev home | 0.4206 |
| Raw edge prob draw | -0.0896 |
| Raw ev draw | -0.3728 |
| Raw edge prob away | -0.0910 |
| Raw ev away | -0.2866 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **72.4%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.4%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 58.9%; Under 3.5 goals: 64.3%; Double Chance 1X: 88.3%; Double Chance X2: 27.6%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 72.4% | 1.38 |
| Draw | 15.9% | 6.30 |
| Shakhtar Donetsk win | 11.7% | 8.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.42% |
| 2 | 2-0 | 12.18% |
| 3 | 2-1 | 11.22% |
| 4 | 3-0 | 8.33% |
| 5 | 3-1 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 72.4% | 80.8% | 1.24 | -10.2% |
| Draw | 15.9% | 12.3% | 7.50 | +19.1% |
| Shakhtar Donetsk win | 11.7% | 6.9% | 12.90 | +50.8% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0512 |
| Dc lambda away | 0.9215 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.46 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.27 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 88.3% |
| P draw away | 27.6% |
| P home away | 84.1% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.22 |
| Reference draw odds | 7.10 |
| Reference away odds | 12.25 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | -8.4% |
| Draw probability edge | +3.6% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -15.3% |
| Under 2.5 probability edge | +15.3% |
| Raw edge prob home | -0.1684 |
| Raw ev home | -0.2064 |
| Raw edge prob draw | 0.0718 |
| Raw ev draw | 0.4605 |
| Raw edge prob away | 0.0967 |
| Raw ev away | 1.1319 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.6%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.5%; Double Chance 1X: 78.1%; Double Chance X2: 42.4%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.6% | 1.74 |
| Draw | 20.5% | 4.87 |
| Galatasaray win | 21.9% | 4.58 |

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
| 2 | 2-1 | 7.57% |
| 3 | 2-0 | 7.30% |
| 4 | 3-1 | 6.48% |
| 5 | 2-2 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.6% | 44.4% | 2.24 | +29.0% |
| Draw | 20.5% | 25.3% | 3.84 | -21.1% |
| Galatasaray win | 21.9% | 30.2% | 3.25 | -29.0% |
| Over 2.5 | 67.2% | 57.7% | 1.72 | +15.6% |
| Under 2.5 | 32.8% | 42.3% | 2.30 | -24.5% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lille OSC |
| Matched away-team name | Galatasaray SK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5692 |
| Dc lambda away | 1.0370 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.55 |
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
| P home draw | 78.1% |
| P draw away | 42.4% |
| P home away | 79.5% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.18 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:35:00Z |
| Market best over 2 5 last update utc | 2026-10-18T14:33:53Z |
| Market best under 2 5 last update utc | 2026-10-18T14:33:53Z |
| Home probability edge | +13.2% |
| Draw probability edge | -4.8% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +9.5% |
| Under 2.5 probability edge | -9.5% |
| Raw edge prob home | 0.2631 |
| Raw ev home | 0.5850 |
| Raw edge prob draw | -0.0961 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1670 |
| Raw ev away | -0.5611 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **78.0%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.5%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.8%; Under 3.5 goals: 7.7%; Double Chance 1X: 89.9%; Double Chance X2: 22.0%; Double Chance 12 (either team wins): 88.1%; Under 4.5 goals: 17.1%; BTTS Yes (both teams score): 82.8%; BTTS No (at least one team does not score): 17.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 78.0% | 1.28 |
| Draw | 11.9% | 8.41 |
| Feyenoord win | 10.1% | 9.90 |

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
| Over 2.5 | 96.8% |
| Under 2.5 | 3.2% |
| Over 3.5 | 92.3% |
| Under 3.5 | 7.7% |
| Over 4.5 | 82.9% |
| Under 4.5 | 17.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.51% |
| 2 | 6-1 | 4.32% |
| 3 | 4-1 | 3.92% |
| 4 | 5-2 | 3.71% |
| 5 | 3-3 | 3.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 78.0% | 64.5% | 1.56 | +21.7% |
| Draw | 11.9% | 19.1% | 4.98 | -40.8% |
| Feyenoord win | 10.1% | 16.4% | 5.75 | -41.9% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.7505 |
| Dc lambda away | 1.6460 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 82.8% |
| P btts no | 17.2% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1219.41 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 132.36 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 30.84 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 12.95 |
| Fair Over 4.5 odds | 1.21 |
| Fair Under 4.5 odds | 5.86 |
| Unadjusted home-win probability | 91.5% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 89.9% |
| P draw away | 22.0% |
| P home away | 88.1% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.5% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.52 |
| Reference draw odds | 4.85 |
| Reference away odds | 5.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +13.5% |
| Draw probability edge | -7.2% |
| Away probability edge | -6.3% |
| Over 2.5 probability edge | +25.9% |
| Under 2.5 probability edge | -25.9% |
| Raw edge prob home | 0.2707 |
| Raw ev home | 0.4281 |
| Raw edge prob draw | -0.1442 |
| Raw ev draw | -0.7667 |
| Raw edge prob away | -0.1266 |
| Raw ev away | -0.7832 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **77.2%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 9.9%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 71.0%; Under 3.5 goals: 49.9%; Double Chance 1X: 90.6%; Double Chance X2: 22.8%; Double Chance 12 (either team wins): 86.6%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 54.6%; BTTS No (at least one team does not score): 45.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.2% | 1.29 |
| Draw | 13.4% | 7.46 |
| RB Leipzig win | 9.4% | 10.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 87.8% |
| Under 1.5 | 12.2% |
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 50.1% |
| Under 3.5 | 49.9% |
| Over 4.5 | 30.8% |
| Under 4.5 | 69.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.87% |
| 2 | 3-0 | 9.22% |
| 3 | 2-1 | 8.66% |
| 4 | 3-1 | 8.08% |
| 5 | 1-0 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.2% | 76.9% | 1.31 | +1.2% |
| Draw | 13.4% | 13.7% | 6.80 | -8.9% |
| RB Leipzig win | 9.4% | 9.4% | 9.60 | -10.0% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8009 |
| Dc lambda away | 0.8772 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.6% |
| P btts no | 45.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 44.25 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.22 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.45 |
| Fair Over 3.5 odds | 2.00 |
| Fair Under 3.5 odds | 2.00 |
| Fair Over 4.5 odds | 3.25 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 77.5% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.6% |
| P draw away | 22.8% |
| P home away | 86.6% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.5% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.28 |
| Reference draw odds | 6.50 |
| Reference away odds | 9.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +0.3% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | 0.0064 |
| Raw ev home | 0.0158 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.1060 |
| Raw edge prob away | -0.0013 |
| Raw ev away | -0.1063 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.0%**. Expected goals are 6.10 for Sporting Lisbon and 1.31 for LASK (7.41 combined). The most likely exact score is 6-1 at 5.2%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 97.0%; Under 3.5 goals: 7.3%; Double Chance 1X: 95.4%; Double Chance X2: 12.0%; Double Chance 12 (either team wins): 92.6%; Under 4.5 goals: 16.1%; BTTS Yes (both teams score): 74.6%; BTTS No (at least one team does not score): 25.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.0% | 1.14 |
| Draw | 7.4% | 13.49 |
| LASK win | 4.6% | 21.77 |

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
| Over 3.5 | 92.7% |
| Under 3.5 | 7.3% |
| Over 4.5 | 83.9% |
| Under 4.5 | 16.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.24% |
| 2 | 5-1 | 5.15% |
| 3 | 7-1 | 4.56% |
| 4 | 4-1 | 4.23% |
| 5 | 6-0 | 3.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.0% | 80.8% | 1.24 | +9.1% |
| Draw | 7.4% | 11.9% | 7.75 | -42.6% |
| LASK win | 4.6% | 7.3% | 12.20 | -43.9% |

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
| Market best home last update utc | 2026-10-18T14:33:53Z |
| Market best draw last update utc | 2026-10-18T14:33:53Z |
| Market best away last update utc | 2026-10-18T14:33:53Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 6.0984 |
| Dc lambda away | 1.3145 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:35:00.015368+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 74.6% |
| P btts no | 25.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1095.94 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 141.63 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 33.00 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.64 |
| Fair Over 4.5 odds | 1.19 |
| Fair Under 4.5 odds | 6.20 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 73.0% |
| P home draw | 95.4% |
| P draw away | 12.0% |
| P home away | 92.6% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.22 |
| Reference draw odds | 7.30 |
| Reference away odds | 11.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:35:00Z |
| Market reference home last update utc | 2026-10-18T14:35:00Z |
| Market reference draw last update utc | 2026-10-18T14:35:00Z |
| Market reference away last update utc | 2026-10-18T14:35:00Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:52Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:52Z |
| Home probability edge | +7.2% |
| Draw probability edge | -4.5% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | +23.9% |
| Under 2.5 probability edge | -23.9% |
| Raw edge prob home | 0.1437 |
| Raw ev home | 0.1802 |
| Raw edge prob draw | -0.0895 |
| Raw ev draw | -0.7724 |
| Raw edge prob away | -0.0542 |
| Raw ev away | -0.7700 |

</details>


---
