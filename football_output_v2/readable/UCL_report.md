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
| Training as of utc | 2026-10-18T11:58:10.240643+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 36, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 27, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:58:10.240643+00:00', 'observations': 54, 'observations_sha256': '0edc36b296a2e980e3a8e9c1bb30620bc3d5c291e8f29f1e98b505cc0aae317e', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 27, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '0f92b6373ad88e018690d9fe5ac866058277e3f45e0e3443c662a063cc8fbad1', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 967.104 |
| Base scoring parameter | 0.203 |
| Home-advantage parameter | 0.306 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0009 |
| Training data health | {'completed_matches': 36, 'latest_completed_utc': '2026-10-14T19:00:00+00:00', 'latest_completed_date': '2026-10-14', 'next_fixture_utc': '2026-10-20T16:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-18T11:58:04.345872+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': '2217b36d746063d412e90f633195640580308995d5c6ce928aa37c3aa5a6809e', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.001637436388888889, 'training_end': '2026-10-14', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 21.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261018T115810240643Z_68fa8a060599f160bef05ec9ee8905cea136f2bd65390dddd31caaceeda5bb06.json |
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

The model's most likely 1X2 outcome is **AS Roma win** at **83.8%**. Expected goals are 3.76 for AS Roma and 1.32 for ŠK Slovan Bratislava (5.08 combined). The most likely exact score is 3-1 at 7.5%. Goal-market probabilities: at least one goal: 99.6%; Over 2.5 goals: 88.5%; Under 3.5 goals: 25.0%; Double Chance 1X: 93.1%; Double Chance X2: 16.2%; Double Chance 12 (either team wins): 90.7%; Under 4.5 goals: 42.2%; BTTS Yes (both teams score): 70.9%; BTTS No (at least one team does not score): 29.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 83.8% | 1.19 |
| Draw | 9.3% | 10.74 |
| ŠK Slovan Bratislava win | 6.9% | 14.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 3.76 |
| ŠK Slovan Bratislava expected goals | 1.32 |
| Expected total goals | 5.08 |
| Over 0.5 | 99.6% |
| Under 0.5 | 0.4% |
| Over 1.5 | 96.2% |
| Under 1.5 | 3.8% |
| Over 2.5 | 88.5% |
| Under 2.5 | 11.5% |
| Over 3.5 | 75.0% |
| Under 3.5 | 25.0% |
| Over 4.5 | 57.8% |
| Under 4.5 | 42.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.52% |
| 2 | 4-1 | 7.07% |
| 3 | 2-1 | 6.00% |
| 4 | 3-0 | 5.72% |
| 5 | 4-0 | 5.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 83.8% | 86.5% | 1.19 | -0.3% |
| Draw | 9.3% | 8.5% | 8.15 | -24.1% |
| ŠK Slovan Bratislava win | 6.9% | 5.0% | 18.00 | +23.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | AS Roma |
| Matched away-team name | ŠK Slovan Bratislava |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.7597 |
| Dc lambda away | 1.3156 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 70.9% |
| P btts no | 29.1% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 231.29 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.41 |
| Fair Over 2.5 odds | 1.13 |
| Fair Under 2.5 odds | 8.72 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.00 |
| Fair Over 4.5 odds | 1.73 |
| Fair Under 4.5 odds | 2.37 |
| Unadjusted home-win probability | 81.1% |
| Unadjusted draw probability | 10.1% |
| Unadjusted away-win probability | 8.8% |
| Raw p over 1 5 | 96.0% |
| Raw p under 3 5 | 25.5% |
| Raw p btts yes | 71.3% |
| P home draw | 93.1% |
| P draw away | 16.2% |
| P home away | 90.7% |
| Raw p home draw | 91.2% |
| Raw p draw away | 18.9% |
| Raw p home away | 89.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.13 |
| Reference draw odds | 8.00 |
| Reference away odds | 12.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.55 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +13.5% |
| Under 2.5 probability edge | -13.5% |
| Raw edge prob home | -0.0540 |
| Raw ev home | -0.0348 |
| Raw edge prob draw | 0.0164 |
| Raw ev draw | -0.1746 |
| Raw edge prob away | 0.0376 |
| Raw ev away | 0.5775 |
| Market p home draw | 93.7% |
| Market home draw odds | 1.03 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 17.7% |
| Market draw away odds | 5.30 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 88.6% |
| Market home away odds | 1.11 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.04 |
| Market reference dc draw away odds | 5.51 |
| Market reference dc home away odds | 1.10 |
| Market p over 1 5 | 94.4% |
| Market over 1 5 odds | 1.04 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:57:17Z |
| Market reference over 1 5 odds | 1.04 |
| Market reference over 1 5 opposite odds | 7.10 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:17Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 46.8% |
| Market under 3 5 odds | 2.08 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:57:17Z |
| Market reference under 3 5 odds | 2.04 |
| Market reference under 3 5 opposite odds | 1.81 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:52Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 49.0% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 1.88 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Fenerbahce vs Slavia Praha

The model's most likely 1X2 outcome is **Fenerbahce win** at **42.9%**. Expected goals are 0.78 for Fenerbahce and 1.07 for Slavia Praha (1.84 combined). The most likely exact score is 1-0 at 20.7%. Goal-market probabilities: at least one goal: 87.1%; Over 2.5 goals: 28.8%; Under 3.5 goals: 88.7%; Double Chance 1X: 68.9%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 96.0%; BTTS Yes (both teams score): 33.8%; BTTS No (at least one team does not score): 66.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 42.9% | 2.33 |
| Draw | 26.0% | 3.85 |
| Slavia Praha win | 31.1% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 0.78 |
| Slavia Praha expected goals | 1.07 |
| Expected total goals | 1.84 |
| Over 0.5 | 87.1% |
| Under 0.5 | 12.9% |
| Over 1.5 | 53.6% |
| Under 1.5 | 46.4% |
| Over 2.5 | 28.8% |
| Under 2.5 | 71.2% |
| Over 3.5 | 11.3% |
| Under 3.5 | 88.7% |
| Over 4.5 | 4.0% |
| Under 4.5 | 96.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.68% |
| 2 | 0-0 | 12.88% |
| 3 | 0-1 | 12.85% |
| 4 | 1-1 | 10.56% |
| 5 | 2-1 | 8.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 42.9% | 59.0% | 1.74 | -25.4% |
| Draw | 26.0% | 21.3% | 4.31 | +11.9% |
| Slavia Praha win | 31.1% | 19.7% | 4.83 | +50.4% |
| Over 2.5 | 28.8% | 60.0% | 1.69 | -51.3% |
| Under 2.5 | 71.2% | 40.0% | 2.36 | +68.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 0.7756 |
| Dc lambda away | 1.0673 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 33.8% |
| P btts no | 66.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.77 |
| Fair Over 1.5 odds | 1.87 |
| Fair Under 1.5 odds | 2.15 |
| Fair Over 2.5 odds | 3.47 |
| Fair Under 2.5 odds | 1.40 |
| Fair Over 3.5 odds | 8.88 |
| Fair Under 3.5 odds | 1.13 |
| Fair Over 4.5 odds | 24.86 |
| Fair Under 4.5 odds | 1.04 |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 42.6% |
| Raw p over 1 5 | 54.3% |
| Raw p under 3 5 | 88.4% |
| Raw p btts yes | 34.7% |
| P home draw | 68.9% |
| P draw away | 57.1% |
| P home away | 74.0% |
| Raw p home draw | 57.4% |
| Raw p draw away | 73.2% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.62 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -16.1% |
| Draw probability edge | +4.6% |
| Away probability edge | +11.4% |
| Over 2.5 probability edge | -31.2% |
| Under 2.5 probability edge | +31.2% |
| Raw edge prob home | -0.3212 |
| Raw ev home | -0.5331 |
| Raw edge prob draw | 0.0929 |
| Raw ev draw | 0.3192 |
| Raw edge prob away | 0.2283 |
| Raw ev away | 1.0556 |
| Market p home draw | 79.4% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 43.1% |
| Market draw away odds | 2.23 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.25 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.2% |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.7% |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.56 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.8% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.31 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Liverpool vs Villarreal

The model's most likely 1X2 outcome is **Liverpool win** at **77.7%**. Expected goals are 3.36 for Liverpool and 0.51 for Villarreal (3.86 combined). The most likely exact score is 3-0 at 11.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 69.1%; Under 3.5 goals: 50.5%; Double Chance 1X: 90.5%; Double Chance X2: 22.3%; Double Chance 12 (either team wins): 87.1%; Under 4.5 goals: 69.2%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 77.7% | 1.29 |
| Draw | 12.9% | 7.76 |
| Villarreal win | 9.5% | 10.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 3.36 |
| Villarreal expected goals | 0.51 |
| Expected total goals | 3.86 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.3% |
| Under 1.5 | 13.7% |
| Over 2.5 | 69.1% |
| Under 2.5 | 30.9% |
| Over 3.5 | 49.5% |
| Under 3.5 | 50.5% |
| Over 4.5 | 30.8% |
| Under 4.5 | 69.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 11.45% |
| 2 | 2-0 | 10.24% |
| 3 | 4-0 | 9.60% |
| 4 | 5-0 | 6.45% |
| 5 | 1-0 | 6.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 77.7% | 65.4% | 1.53 | +18.8% |
| Draw | 12.9% | 18.6% | 4.88 | -37.1% |
| Villarreal win | 9.5% | 15.9% | 6.36 | -39.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool FC |
| Matched away-team name | Villarreal CF |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.3552 |
| Dc lambda away | 0.5055 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.79 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.31 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.24 |
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
| P home draw | 90.5% |
| P draw away | 22.3% |
| P home away | 87.1% |
| Raw p home draw | 97.0% |
| Raw p draw away | 10.1% |
| Raw p home away | 92.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.47 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +12.2% |
| Draw probability edge | -5.7% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | +3.8% |
| Under 2.5 probability edge | -3.8% |
| Raw edge prob home | 0.2445 |
| Raw ev home | 0.3751 |
| Raw edge prob draw | -0.1148 |
| Raw ev draw | -0.6510 |
| Raw edge prob away | -0.1297 |
| Raw ev away | -0.8109 |
| Market p home draw | 84.4% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.69 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.3% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 85.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.0% |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.4% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.29 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Manchester City vs AEK Athens

The model's most likely 1X2 outcome is **Manchester City win** at **84.3%**. Expected goals are 1.97 for Manchester City and 0.39 for AEK Athens (2.36 combined). The most likely exact score is 1-0 at 21.0%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 45.3%; Under 3.5 goals: 77.1%; Double Chance 1X: 95.3%; Double Chance X2: 15.7%; Double Chance 12 (either team wins): 89.0%; Under 4.5 goals: 90.0%; BTTS Yes (both teams score): 25.7%; BTTS No (at least one team does not score): 74.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 84.3% | 1.19 |
| Draw | 11.0% | 9.08 |
| AEK Athens win | 4.7% | 21.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| AEK Athens expected goals | 0.39 |
| Expected total goals | 2.36 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 22.9% |
| Under 3.5 | 77.1% |
| Over 4.5 | 10.0% |
| Under 4.5 | 90.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 21.03% |
| 2 | 2-0 | 20.36% |
| 3 | 3-0 | 13.39% |
| 4 | 2-1 | 7.95% |
| 5 | 4-0 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 84.3% | 92.8% | 1.08 | -8.9% |
| Draw | 11.0% | 4.6% | 15.50 | +70.8% |
| AEK Athens win | 4.7% | 2.6% | 35.00 | +62.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Manchester City FC |
| Matched away-team name | PAE AEK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9738 |
| Dc lambda away | 0.3904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 25.7% |
| P btts no | 74.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.52 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.38 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.37 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.99 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 75.9% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 6.7% |
| Raw p over 1 5 | 68.0% |
| Raw p under 3 5 | 78.6% |
| Raw p btts yes | 27.5% |
| P home draw | 95.3% |
| P draw away | 15.7% |
| P home away | 89.0% |
| Raw p home draw | 93.3% |
| Raw p draw away | 24.1% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.06 |
| Reference draw odds | 11.00 |
| Reference away odds | 17.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.29 |
| Reference Under 2.5 odds | 3.60 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -8.5% |
| Draw probability edge | +6.4% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -30.3% |
| Under 2.5 probability edge | +30.3% |
| Raw edge prob home | -0.1692 |
| Raw ev home | -0.1806 |
| Raw edge prob draw | 0.1285 |
| Raw ev draw | 1.7039 |
| Raw edge prob away | 0.0406 |
| Raw ev away | 1.3397 |
| Market p home draw | 95.6% |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 11.6% |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 92.8% |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.02 |
| Market reference dc draw away odds | 8.42 |
| Market reference dc home away odds | 1.05 |
| Market p over 1 5 | 90.2% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 7.00 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 45.8% |
| Market reference under 3 5 odds | 2.07 |
| Market reference under 3 5 opposite odds | 1.77 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 36.8% |
| Market btts yes odds | 2.41 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 2.52 |
| Market reference btts yes opposite odds | 1.53 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Napoli vs Bodø/Glimt

The model's most likely 1X2 outcome is **Napoli win** at **43.8%**. Expected goals are 1.17 for Napoli and 1.78 for Bodø/Glimt (2.94 combined). The most likely exact score is 1-0 at 11.5%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 55.9%; Under 3.5 goals: 67.3%; Double Chance 1X: 64.6%; Double Chance X2: 56.2%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 43.8% | 2.28 |
| Draw | 20.8% | 4.80 |
| Bodø/Glimt win | 35.4% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.17 |
| Bodø/Glimt expected goals | 1.78 |
| Expected total goals | 2.94 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 32.7% |
| Under 3.5 | 67.3% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 11.47% |
| 2 | 2-1 | 10.92% |
| 3 | 1-1 | 9.72% |
| 4 | 0-1 | 6.71% |
| 5 | 1-2 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 43.8% | 62.0% | 1.64 | -28.2% |
| Draw | 20.8% | 19.4% | 4.67 | -2.7% |
| Bodø/Glimt win | 35.4% | 18.5% | 5.18 | +83.3% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | SSC Napoli |
| Matched away-team name | FK Bodø/Glimt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.1659 |
| Dc lambda away | 1.7783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.61 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.06 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 52.3% |
| Raw p over 1 5 | 78.7% |
| Raw p under 3 5 | 66.0% |
| Raw p btts yes | 56.7% |
| P home draw | 64.6% |
| P draw away | 56.2% |
| P home away | 79.2% |
| Raw p home draw | 47.7% |
| Raw p draw away | 74.5% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.65 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -18.3% |
| Draw probability edge | +1.4% |
| Away probability edge | +16.9% |
| Over 2.5 probability edge | -9.4% |
| Under 2.5 probability edge | +9.4% |
| Raw edge prob home | -0.3655 |
| Raw ev home | -0.5818 |
| Raw edge prob draw | 0.0279 |
| Raw ev draw | 0.0382 |
| Raw edge prob away | 0.3376 |
| Raw ev away | 1.7074 |
| Market p home draw | 80.9% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:57:55Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.1% |
| Market draw away odds | 2.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:57:55Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:57:55Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.40 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 85.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.30 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:14Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 57.7% |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.25 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:52Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.9% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.58 |
| Market reference btts yes last update utc | 2026-10-18T11:57:51Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Paris Saint Germain vs Barcelona

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **55.7%**. Expected goals are 3.22 for Paris Saint Germain and 1.52 for Barcelona (4.75 combined). The most likely exact score is 2-2 at 6.3%. Goal-market probabilities: at least one goal: 99.2%; Over 2.5 goals: 83.8%; Under 3.5 goals: 32.3%; Double Chance 1X: 72.3%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 83.4%; Under 4.5 goals: 50.8%; BTTS Yes (both teams score): 76.5%; BTTS No (at least one team does not score): 23.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 55.7% | 1.80 |
| Draw | 16.6% | 6.02 |
| Barcelona win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 3.22 |
| Barcelona expected goals | 1.52 |
| Expected total goals | 4.75 |
| Over 0.5 | 99.2% |
| Under 0.5 | 0.8% |
| Over 1.5 | 94.0% |
| Under 1.5 | 6.0% |
| Over 2.5 | 83.8% |
| Under 2.5 | 16.2% |
| Over 3.5 | 67.7% |
| Under 3.5 | 32.3% |
| Over 4.5 | 49.2% |
| Under 4.5 | 50.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.27% |
| 2 | 1-2 | 5.95% |
| 3 | 3-1 | 5.79% |
| 4 | 2-1 | 5.39% |
| 5 | 2-3 | 4.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 55.7% | 40.3% | 2.50 | +39.2% |
| Draw | 16.6% | 19.4% | 4.62 | -23.2% |
| Barcelona win | 27.7% | 40.3% | 2.51 | -30.4% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris Saint-Germain FC |
| Matched away-team name | FC Barcelona |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.2230 |
| Dc lambda away | 1.5229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 76.5% |
| P btts no | 23.5% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 127.23 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 16.77 |
| Fair Over 2.5 odds | 1.19 |
| Fair Under 2.5 odds | 6.17 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.10 |
| Fair Over 4.5 odds | 2.03 |
| Fair Under 4.5 odds | 1.97 |
| Unadjusted home-win probability | 71.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 94.8% |
| Raw p under 3 5 | 30.3% |
| Raw p btts yes | 74.9% |
| P home draw | 72.3% |
| P draw away | 44.3% |
| P home away | 83.4% |
| Raw p home draw | 84.9% |
| Raw p draw away | 29.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 4.50 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.19 |
| Reference Under 2.5 odds | 4.70 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +15.4% |
| Draw probability edge | -2.8% |
| Away probability edge | -12.6% |
| Over 2.5 probability edge | +1.5% |
| Under 2.5 probability edge | -1.5% |
| Raw edge prob home | 0.3071 |
| Raw ev home | 0.7755 |
| Raw edge prob draw | -0.0552 |
| Raw ev draw | -0.3594 |
| Raw edge prob away | -0.2519 |
| Raw ev away | -0.6206 |
| Market p home draw | 60.7% |
| Market home draw odds | 1.59 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.3% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 98.3% |
| Market over 1 5 odds | 1.01 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:58:10Z |
| Market reference over 1 5 odds | 1.01 |
| Market reference over 1 5 opposite odds | 11.00 |
| Market reference over 1 5 last update utc | 2026-10-18T11:58:10Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 36.2% |
| Market under 3 5 odds | 2.43 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:58:10Z |
| Market reference under 3 5 odds | 2.43 |
| Market reference under 3 5 opposite odds | 1.48 |
| Market reference under 3 5 last update utc | 2026-10-18T11:58:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 80.1% |
| Market btts yes odds | 1.18 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.23 |
| Market reference btts yes opposite odds | 4.50 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Porto vs PSV Eindhoven

The model's most likely 1X2 outcome is **Porto win** at **59.2%**. Expected goals are 2.11 for Porto and 1.17 for PSV Eindhoven (3.28 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 63.5%; Under 3.5 goals: 58.5%; Double Chance 1X: 79.4%; Double Chance X2: 40.8%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 76.7%; BTTS Yes (both teams score): 60.2%; BTTS No (at least one team does not score): 39.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Porto win | 59.2% | 1.69 |
| Draw | 20.2% | 4.94 |
| PSV Eindhoven win | 20.6% | 4.87 |

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
| Over 2.5 | 63.5% |
| Under 2.5 | 36.5% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.3% |
| Under 4.5 | 76.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.76% |
| 2 | 1-1 | 9.07% |
| 3 | 1-0 | 8.39% |
| 4 | 2-0 | 8.36% |
| 5 | 3-1 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Porto win | 59.2% | 59.0% | 1.71 | +1.3% |
| Draw | 20.2% | 20.8% | 4.57 | -7.5% |
| PSV Eindhoven win | 20.6% | 20.3% | 4.72 | -3.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | FC Porto |
| Matched away-team name | PSV |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1110 |
| Dc lambda away | 1.1673 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.2% |
| P btts no | 39.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.44 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.03 |
| Fair Over 2.5 odds | 1.58 |
| Fair Under 2.5 odds | 2.74 |
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
| P draw away | 40.8% |
| P home away | 79.8% |
| Raw p home draw | 79.1% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.62 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +0.2% |
| Draw probability edge | -0.5% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0049 |
| Raw ev home | 0.0167 |
| Raw edge prob draw | -0.0110 |
| Raw ev draw | -0.1005 |
| Raw edge prob away | 0.0061 |
| Raw ev away | -0.0155 |
| Market p home draw | 79.5% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.1% |
| Market draw away odds | 2.27 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.22 |
| Market reference dc draw away odds | 2.36 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 86.3% |
| Market over 1 5 odds | 1.12 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:58:03Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 4.65 |
| Market reference over 1 5 last update utc | 2026-10-18T11:58:03Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 60.2% |
| Market under 3 5 odds | 1.64 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:58:03Z |
| Market reference under 3 5 odds | 1.64 |
| Market reference under 3 5 opposite odds | 2.46 |
| Market reference under 3 5 last update utc | 2026-10-18T11:58:03Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.2% |
| Market btts yes odds | 1.56 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — Sabah FK vs Borussia Dortmund

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **76.3%**. Expected goals are 0.75 for Sabah FK and 2.47 for Borussia Dortmund (3.23 combined). The most likely exact score is 0-2 at 12.3%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 63.0%; Under 3.5 goals: 59.5%; Double Chance 1X: 23.7%; Double Chance X2: 90.1%; Double Chance 12 (either team wins): 86.2%; Under 4.5 goals: 77.3%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sabah FK win | 9.9% | 10.12 |
| Draw | 13.8% | 7.23 |
| Borussia Dortmund win | 76.3% | 1.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sabah FK expected goals | 0.75 |
| Borussia Dortmund expected goals | 2.47 |
| Expected total goals | 3.23 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 63.0% |
| Under 2.5 | 37.0% |
| Over 3.5 | 40.5% |
| Under 3.5 | 59.5% |
| Over 4.5 | 22.7% |
| Under 4.5 | 77.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.26% |
| 2 | 0-1 | 10.28% |
| 3 | 0-3 | 10.11% |
| 4 | 1-2 | 9.25% |
| 5 | 1-3 | 7.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sabah FK win | 9.9% | 10.0% | 9.40 | -7.1% |
| Draw | 13.8% | 12.8% | 6.11 | -15.5% |
| Borussia Dortmund win | 76.3% | 77.2% | 1.34 | +2.2% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sabah FK |
| Matched away-team name | Borussia Dortmund |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7547 |
| Dc lambda away | 2.4744 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.95 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.70 |
| Fair Over 3.5 odds | 2.47 |
| Fair Under 3.5 odds | 1.68 |
| Fair Over 4.5 odds | 4.41 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 9.7% |
| Unadjusted draw probability | 14.9% |
| Unadjusted away-win probability | 75.4% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 59.6% |
| Raw p btts yes | 48.2% |
| P home draw | 23.7% |
| P draw away | 90.1% |
| P home away | 86.2% |
| Raw p home draw | 24.6% |
| Raw p draw away | 90.3% |
| Raw p home away | 85.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 7.75 |
| Reference draw odds | 6.25 |
| Reference away odds | 1.26 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -0.2% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
| Raw edge prob home | -0.0034 |
| Raw ev home | -0.0869 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | -0.0913 |
| Raw edge prob away | -0.0174 |
| Raw ev away | 0.0106 |
| Market p home draw | 26.0% |
| Market home draw odds | 3.56 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 89.3% |
| Market draw away odds | 1.07 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 84.7% |
| Market home away odds | 1.16 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 3.75 |
| Market reference dc draw away odds | 1.09 |
| Market reference dc home away odds | 1.15 |
| Market p over 1 5 | 91.2% |
| Market over 1 5 odds | 1.07 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:57:47Z |
| Market reference over 1 5 odds | 1.07 |
| Market reference over 1 5 opposite odds | 5.95 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 52.2% |
| Market under 3 5 odds | 1.84 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:57:47Z |
| Market reference under 3 5 odds | 1.85 |
| Market reference under 3 5 opposite odds | 2.01 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:51Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.6% |
| Market btts yes odds | 1.69 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-20 — VfB Stuttgart vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **50.3%**. Expected goals are 1.41 for VfB Stuttgart and 2.10 for Atlético Madrid (3.51 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 67.5%; Under 3.5 goals: 53.7%; Double Chance 1X: 49.7%; Double Chance X2: 72.1%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 72.8%; BTTS Yes (both teams score): 66.4%; BTTS No (at least one team does not score): 33.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 27.9% | 3.58 |
| Draw | 21.7% | 4.60 |
| Atlético Madrid win | 50.3% | 1.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 1.41 |
| Atlético Madrid expected goals | 2.10 |
| Expected total goals | 3.51 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 86.0% |
| Under 1.5 | 14.0% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 46.3% |
| Under 3.5 | 53.7% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.09% |
| 2 | 1-2 | 8.71% |
| 3 | 2-2 | 7.09% |
| 4 | 2-1 | 6.68% |
| 5 | 0-1 | 6.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 27.9% | 29.7% | 3.33 | -7.0% |
| Draw | 21.7% | 23.3% | 3.94 | -14.3% |
| Atlético Madrid win | 50.3% | 47.0% | 2.17 | +9.2% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | VfB Stuttgart |
| Matched away-team name | Club Atlético de Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4141 |
| Dc lambda away | 2.0957 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 66.4% |
| P btts no | 33.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.37 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.13 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.67 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 26.2% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 53.7% |
| Raw p over 1 5 | 86.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 65.9% |
| P home draw | 49.7% |
| P draw away | 72.1% |
| P home away | 78.3% |
| Raw p home draw | 46.3% |
| Raw p draw away | 73.8% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -1.7% |
| Draw probability edge | -1.6% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | +4.1% |
| Under 2.5 probability edge | -4.1% |
| Raw edge prob home | -0.0347 |
| Raw ev home | -0.1278 |
| Raw edge prob draw | -0.0320 |
| Raw ev draw | -0.2063 |
| Raw edge prob away | 0.0668 |
| Raw ev away | 0.1645 |
| Market p home draw | 54.2% |
| Market home draw odds | 1.77 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:29Z |
| Market reference home draw last update utc | 2026-10-18T11:58:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.0% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:29Z |
| Market reference draw away last update utc | 2026-10-18T11:58:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:29Z |
| Market reference home away last update utc | 2026-10-18T11:58:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 87.3% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:58:03Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-18T11:58:03Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.8% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:58:03Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.38 |
| Market reference under 3 5 last update utc | 2026-10-18T11:58:03Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 66.3% |
| Market btts yes odds | 1.45 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:29Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.78 |
| Market reference btts yes last update utc | 2026-10-18T11:58:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **81.9%**. Expected goals are 4.01 for Aston Villa and 1.16 for Viking FK (5.17 combined). The most likely exact score is 4-1 at 6.8%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 88.0%; Under 3.5 goals: 24.8%; Double Chance 1X: 93.1%; Double Chance X2: 18.1%; Double Chance 12 (either team wins): 88.8%; Under 4.5 goals: 42.4%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 81.9% | 1.22 |
| Draw | 11.2% | 8.92 |
| Viking FK win | 6.9% | 14.54 |

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
| Over 2.5 | 88.0% |
| Under 2.5 | 12.0% |
| Over 3.5 | 75.2% |
| Under 3.5 | 24.8% |
| Over 4.5 | 57.6% |
| Under 4.5 | 42.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 4-1 | 6.79% |
| 2 | 3-1 | 6.78% |
| 3 | 4-0 | 5.84% |
| 4 | 3-0 | 5.83% |
| 5 | 5-1 | 5.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 81.9% | 78.2% | 1.29 | +5.7% |
| Draw | 11.2% | 14.2% | 6.31 | -29.2% |
| Viking FK win | 6.9% | 7.6% | 12.60 | -13.3% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 4.0061 |
| Dc lambda away | 1.1639 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 23 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 167.95 |
| Fair Over 1.5 odds | 1.04 |
| Fair Under 1.5 odds | 26.40 |
| Fair Over 2.5 odds | 1.14 |
| Fair Under 2.5 odds | 8.32 |
| Fair Over 3.5 odds | 1.33 |
| Fair Under 3.5 odds | 4.03 |
| Fair Over 4.5 odds | 1.74 |
| Fair Under 4.5 odds | 2.36 |
| Unadjusted home-win probability | 85.6% |
| Unadjusted draw probability | 8.2% |
| Unadjusted away-win probability | 6.2% |
| Raw p over 1 5 | 96.4% |
| Raw p under 3 5 | 24.2% |
| Raw p btts yes | 67.4% |
| P home draw | 93.1% |
| P draw away | 18.1% |
| P home away | 88.8% |
| Raw p home draw | 93.8% |
| Raw p draw away | 14.4% |
| Raw p home away | 91.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.24 |
| Reference draw odds | 5.50 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.31 |
| Reference Under 2.5 odds | 3.50 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +3.7% |
| Draw probability edge | -3.0% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +13.5% |
| Under 2.5 probability edge | -13.5% |
| Raw edge prob home | 0.0746 |
| Raw ev home | 0.1047 |
| Raw edge prob draw | -0.0601 |
| Raw ev draw | -0.4820 |
| Raw edge prob away | -0.0145 |
| Raw ev away | -0.2248 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **37.2%**. Expected goals are 1.02 for Bayern Munich and 1.31 for Arsenal (2.33 combined). The most likely exact score is 1-0 at 13.3%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.6%; Double Chance 1X: 62.8%; Double Chance X2: 62.8%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 37.2% | 2.69 |
| Draw | 25.6% | 3.91 |
| Arsenal win | 37.2% | 2.69 |

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
| 1 | 1-0 | 13.29% |
| 2 | 1-1 | 11.93% |
| 3 | 0-1 | 11.37% |
| 4 | 0-0 | 8.78% |
| 5 | 2-1 | 8.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 37.2% | 44.8% | 2.23 | -17.0% |
| Draw | 25.6% | 24.7% | 3.92 | +0.3% |
| Arsenal win | 37.2% | 30.5% | 3.21 | +19.4% |
| Over 2.5 | 41.2% | 60.2% | 1.68 | -30.8% |
| Under 2.5 | 58.8% | 39.8% | 2.38 | +40.0% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda away | 1.3101 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.38 |
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
| P draw away | 62.8% |
| P home away | 74.4% |
| Raw p home draw | 56.1% |
| Raw p draw away | 70.4% |
| Raw p home away | 73.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | -7.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | -19.0% |
| Under 2.5 probability edge | +19.0% |
| Raw edge prob home | -0.1523 |
| Raw ev home | -0.3396 |
| Raw edge prob draw | 0.0181 |
| Raw ev draw | 0.0381 |
| Raw edge prob away | 0.1341 |
| Raw ev away | 0.4093 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **60.1%**. Expected goals are 3.05 for Club Brugge and 1.27 for RC Lens (4.32 combined). The most likely exact score is 2-2 at 6.7%. Goal-market probabilities: at least one goal: 98.6%; Over 2.5 goals: 78.4%; Under 3.5 goals: 39.3%; Double Chance 1X: 78.7%; Double Chance X2: 39.9%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 70.4%; BTTS No (at least one team does not score): 29.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 60.1% | 1.66 |
| Draw | 18.5% | 5.40 |
| RC Lens win | 21.3% | 4.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 3.05 |
| RC Lens expected goals | 1.27 |
| Expected total goals | 4.32 |
| Over 0.5 | 98.6% |
| Under 0.5 | 1.4% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 78.4% |
| Under 2.5 | 21.6% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 41.0% |
| Under 4.5 | 59.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 6.75% |
| 2 | 1-1 | 6.60% |
| 3 | 3-1 | 6.55% |
| 4 | 2-1 | 6.44% |
| 5 | 1-2 | 5.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 60.1% | 47.0% | 2.15 | +29.3% |
| Draw | 18.5% | 23.3% | 3.94 | -27.0% |
| RC Lens win | 21.3% | 29.7% | 3.37 | -28.1% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0509 |
| Dc lambda away | 1.2727 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 70.4% |
| P btts no | 29.6% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 69.32 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.26 |
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
| P home draw | 78.7% |
| P draw away | 39.9% |
| P home away | 81.5% |
| Raw p home draw | 87.0% |
| Raw p draw away | 26.7% |
| Raw p home away | 86.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +13.1% |
| Draw probability edge | -4.8% |
| Away probability edge | -8.3% |
| Over 2.5 probability edge | +15.1% |
| Under 2.5 probability edge | -15.1% |
| Raw edge prob home | 0.2628 |
| Raw ev home | 0.5752 |
| Raw edge prob draw | -0.0963 |
| Raw ev draw | -0.4595 |
| Raw edge prob away | -0.1665 |
| Raw ev away | -0.5614 |

</details>


---

## 2026-10-21 — Como vs Manchester United

The model's most likely 1X2 outcome is **Como win** at **51.2%**. Expected goals are 2.99 for Como and 1.94 for Manchester United (4.93 combined). The most likely exact score is 2-2 at 7.6%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.1%; Under 3.5 goals: 27.9%; Double Chance 1X: 71.5%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 46.5%; BTTS Yes (both teams score): 82.2%; BTTS No (at least one team does not score): 17.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 51.2% | 1.95 |
| Draw | 20.3% | 4.92 |
| Manchester United win | 28.5% | 3.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.99 |
| Manchester United expected goals | 1.94 |
| Expected total goals | 4.93 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 95.4% |
| Under 1.5 | 4.6% |
| Over 2.5 | 86.1% |
| Under 2.5 | 13.9% |
| Over 3.5 | 72.1% |
| Under 3.5 | 27.9% |
| Over 4.5 | 53.5% |
| Under 4.5 | 46.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-2 | 7.58% |
| 2 | 2-1 | 5.37% |
| 3 | 3-1 | 5.35% |
| 4 | 3-2 | 5.20% |
| 5 | 1-1 | 4.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 51.2% | 42.7% | 2.38 | +21.8% |
| Draw | 20.3% | 24.4% | 3.85 | -21.7% |
| Manchester United win | 28.5% | 32.9% | 2.97 | -15.4% |
| Over 2.5 | 86.1% | 59.5% | 1.70 | +46.4% |
| Under 2.5 | 13.9% | 40.5% | 2.34 | -67.5% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 2.9926 |
| Dc lambda away | 1.9422 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 82.2% |
| P btts no | 17.8% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 157.08 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 21.91 |
| Fair Over 2.5 odds | 1.16 |
| Fair Under 2.5 odds | 7.20 |
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
| P home draw | 71.5% |
| P draw away | 48.8% |
| P home away | 79.7% |
| Raw p home draw | 76.0% |
| Raw p draw away | 40.3% |
| Raw p home away | 83.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +8.5% |
| Draw probability edge | -4.0% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | +26.6% |
| Under 2.5 probability edge | -26.6% |
| Raw edge prob home | 0.1697 |
| Raw ev home | 0.4203 |
| Raw edge prob draw | -0.0808 |
| Raw ev draw | -0.3727 |
| Raw edge prob away | -0.0889 |
| Raw ev away | -0.2863 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **72.9%**. Expected goals are 2.05 for Inter Milan and 0.92 for Shakhtar Donetsk (2.97 combined). The most likely exact score is 1-0 at 12.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 59.2%; Under 3.5 goals: 64.2%; Double Chance 1X: 87.8%; Double Chance X2: 27.1%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 72.9% | 1.37 |
| Draw | 14.8% | 6.74 |
| Shakhtar Donetsk win | 12.2% | 8.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.05 |
| Shakhtar Donetsk expected goals | 0.92 |
| Expected total goals | 2.97 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.51% |
| 2 | 2-0 | 12.27% |
| 3 | 2-1 | 11.30% |
| 4 | 3-0 | 8.39% |
| 5 | 3-1 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 72.9% | 81.8% | 1.24 | -9.6% |
| Draw | 14.8% | 10.2% | 7.50 | +11.3% |
| Shakhtar Donetsk win | 12.2% | 8.0% | 12.90 | +57.9% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.32 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 64.0% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 16.5% |
| Raw p over 1 5 | 79.2% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 52.0% |
| P home draw | 87.8% |
| P draw away | 27.1% |
| P home away | 85.2% |
| Raw p home draw | 83.5% |
| Raw p draw away | 36.0% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.19 |
| Reference draw odds | 7.25 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -8.9% |
| Draw probability edge | +4.6% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -14.6% |
| Under 2.5 probability edge | +14.6% |
| Raw edge prob home | -0.1784 |
| Raw ev home | -0.2064 |
| Raw edge prob draw | 0.0927 |
| Raw ev draw | 0.4605 |
| Raw edge prob away | 0.0857 |
| Raw ev away | 1.1317 |

</details>


---

## 2026-10-21 — Lille vs Galatasaray

The model's most likely 1X2 outcome is **Lille win** at **57.2%**. Expected goals are 2.57 for Lille and 1.04 for Galatasaray (3.61 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 67.2%; Under 3.5 goals: 53.6%; Double Chance 1X: 77.5%; Double Chance X2: 42.8%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lille win | 57.2% | 1.75 |
| Draw | 20.3% | 4.92 |
| Galatasaray win | 22.5% | 4.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lille expected goals | 2.57 |
| Galatasaray expected goals | 1.04 |
| Expected total goals | 3.61 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 67.2% |
| Under 2.5 | 32.8% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.88% |
| 2 | 2-1 | 7.51% |
| 3 | 2-0 | 7.24% |
| 4 | 3-1 | 6.43% |
| 5 | 1-2 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lille win | 57.2% | 43.6% | 2.24 | +28.1% |
| Draw | 20.3% | 24.9% | 3.84 | -22.0% |
| Galatasaray win | 22.5% | 31.5% | 3.25 | -26.9% |
| Over 2.5 | 67.2% | 58.3% | 1.72 | +15.5% |
| Under 2.5 | 32.8% | 41.7% | 2.30 | -24.5% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
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
| Dc lambda home | 2.5691 |
| Dc lambda away | 1.0367 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.88 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.01 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.05 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.66 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 70.8% |
| Unadjusted draw probability | 15.7% |
| Unadjusted away-win probability | 13.5% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 59.2% |
| P home draw | 77.5% |
| P draw away | 42.8% |
| P home away | 79.7% |
| Raw p home draw | 86.5% |
| Raw p draw away | 29.2% |
| Raw p home away | 84.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:29Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:29Z |
| Home probability edge | +13.6% |
| Draw probability edge | -4.6% |
| Away probability edge | -9.0% |
| Over 2.5 probability edge | +8.9% |
| Under 2.5 probability edge | -8.9% |
| Raw edge prob home | 0.2718 |
| Raw ev home | 0.5851 |
| Raw edge prob draw | -0.0918 |
| Raw ev draw | -0.3957 |
| Raw edge prob away | -0.1800 |
| Raw ev away | -0.5612 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **78.1%**. Expected goals are 5.75 for Real Betis and 1.65 for Feyenoord (7.40 combined). The most likely exact score is 5-1 at 4.5%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 96.8%; Under 3.5 goals: 7.8%; Double Chance 1X: 89.4%; Double Chance X2: 21.9%; Double Chance 12 (either team wins): 88.7%; Under 4.5 goals: 17.0%; BTTS Yes (both teams score): 82.7%; BTTS No (at least one team does not score): 17.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 78.1% | 1.28 |
| Draw | 11.3% | 8.85 |
| Feyenoord win | 10.6% | 9.40 |

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
| Over 3.5 | 92.2% |
| Under 3.5 | 7.8% |
| Over 4.5 | 83.0% |
| Under 4.5 | 17.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 5-1 | 4.51% |
| 2 | 6-1 | 4.32% |
| 3 | 4-1 | 3.92% |
| 4 | 5-2 | 3.71% |
| 5 | 6-2 | 3.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 78.1% | 64.6% | 1.56 | +21.8% |
| Draw | 11.3% | 17.9% | 4.98 | -43.7% |
| Feyenoord win | 10.6% | 17.5% | 5.75 | -38.8% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 5.7503 |
| Dc lambda away | 1.6459 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 27 |
| Score grid omitted mass | 0 |
| P btts yes | 82.7% |
| P btts no | 17.3% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1283.30 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 129.79 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 31.25 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 12.89 |
| Fair Over 4.5 odds | 1.20 |
| Fair Under 4.5 odds | 5.89 |
| Unadjusted home-win probability | 91.5% |
| Unadjusted draw probability | 4.7% |
| Unadjusted away-win probability | 3.8% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 80.4% |
| P home draw | 89.4% |
| P draw away | 21.9% |
| P home away | 88.7% |
| Raw p home draw | 96.2% |
| Raw p draw away | 8.5% |
| Raw p home away | 95.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.49 |
| Reference draw odds | 4.80 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +13.5% |
| Draw probability edge | -6.6% |
| Away probability edge | -6.9% |
| Over 2.5 probability edge | +25.9% |
| Under 2.5 probability edge | -25.9% |
| Raw edge prob home | 0.2696 |
| Raw ev home | 0.4281 |
| Raw edge prob draw | -0.1322 |
| Raw ev draw | -0.7667 |
| Raw edge prob away | -0.1374 |
| Raw ev away | -0.7832 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **77.9%**. Expected goals are 2.80 for Real Madrid and 0.88 for RB Leipzig (3.68 combined). The most likely exact score is 2-0 at 10.0%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 71.3%; Under 3.5 goals: 49.8%; Double Chance 1X: 90.5%; Double Chance X2: 22.1%; Double Chance 12 (either team wins): 87.5%; Under 4.5 goals: 69.0%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 77.9% | 1.28 |
| Draw | 12.5% | 7.98 |
| RB Leipzig win | 9.5% | 10.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 2.80 |
| RB Leipzig expected goals | 0.88 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 87.9% |
| Under 1.5 | 12.1% |
| Over 2.5 | 71.3% |
| Under 2.5 | 28.7% |
| Over 3.5 | 50.2% |
| Under 3.5 | 49.8% |
| Over 4.5 | 31.0% |
| Under 4.5 | 69.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.96% |
| 2 | 3-0 | 9.30% |
| 3 | 2-1 | 8.74% |
| 4 | 3-1 | 8.16% |
| 5 | 1-0 | 7.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 77.9% | 78.3% | 1.31 | +2.1% |
| Draw | 12.5% | 11.9% | 6.80 | -14.8% |
| RB Leipzig win | 9.5% | 9.8% | 9.60 | -8.5% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8010 |
| Dc lambda away | 0.8770 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 47.31 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 8.24 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.48 |
| Fair Over 3.5 odds | 1.99 |
| Fair Under 3.5 odds | 2.01 |
| Fair Over 4.5 odds | 3.23 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 77.5% |
| Unadjusted draw probability | 13.1% |
| Unadjusted away-win probability | 9.3% |
| Raw p over 1 5 | 87.9% |
| Raw p under 3 5 | 49.9% |
| Raw p btts yes | 54.5% |
| P home draw | 90.5% |
| P draw away | 22.1% |
| P home away | 87.5% |
| Raw p home draw | 90.7% |
| Raw p draw away | 22.5% |
| Raw p home away | 86.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.24 |
| Reference draw odds | 6.50 |
| Reference away odds | 7.75 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.00 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -6.9% |
| Under 2.5 probability edge | +6.9% |
| Raw edge prob home | -0.0077 |
| Raw ev home | 0.0159 |
| Raw edge prob draw | 0.0122 |
| Raw ev draw | -0.1062 |
| Raw edge prob away | -0.0046 |
| Raw ev away | -0.1067 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **88.2%**. Expected goals are 6.10 for Sporting Lisbon and 1.32 for LASK (7.41 combined). The most likely exact score is 6-1 at 5.2%. Goal-market probabilities: at least one goal: 99.9%; Over 2.5 goals: 97.0%; Under 3.5 goals: 7.3%; Double Chance 1X: 95.0%; Double Chance X2: 11.8%; Double Chance 12 (either team wins): 93.1%; Under 4.5 goals: 16.0%; BTTS Yes (both teams score): 74.6%; BTTS No (at least one team does not score): 25.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 88.2% | 1.13 |
| Draw | 6.9% | 14.59 |
| LASK win | 5.0% | 20.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 6.10 |
| LASK expected goals | 1.32 |
| Expected total goals | 7.41 |
| Over 0.5 | 99.9% |
| Under 0.5 | 0.1% |
| Over 1.5 | 99.3% |
| Under 1.5 | 0.7% |
| Over 2.5 | 97.0% |
| Under 2.5 | 3.0% |
| Over 3.5 | 92.7% |
| Under 3.5 | 7.3% |
| Over 4.5 | 84.0% |
| Under 4.5 | 16.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 6-1 | 5.25% |
| 2 | 5-1 | 5.16% |
| 3 | 7-1 | 4.57% |
| 4 | 4-1 | 4.23% |
| 5 | 6-0 | 3.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 88.2% | 81.2% | 1.24 | +9.3% |
| Draw | 6.9% | 10.8% | 7.75 | -46.9% |
| LASK win | 5.0% | 8.1% | 12.20 | -39.2% |

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
| Market best home last update utc | 2026-10-18T11:57:29Z |
| Market best draw last update utc | 2026-10-18T11:57:29Z |
| Market best away last update utc | 2026-10-18T11:57:29Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 6.0998 |
| Dc lambda away | 1.3152 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:58:10.240643+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 28 |
| Score grid omitted mass | 0 |
| P btts yes | 74.6% |
| P btts no | 25.4% |
| Fair Over 0.5 odds | 1.00 |
| Fair Under 0.5 odds | 1188.07 |
| Fair Over 1.5 odds | 1.01 |
| Fair Under 1.5 odds | 138.93 |
| Fair Over 2.5 odds | 1.03 |
| Fair Under 2.5 odds | 33.71 |
| Fair Over 3.5 odds | 1.08 |
| Fair Under 3.5 odds | 13.62 |
| Fair Over 4.5 odds | 1.19 |
| Fair Under 4.5 odds | 6.26 |
| Unadjusted home-win probability | 95.2% |
| Unadjusted draw probability | 2.9% |
| Unadjusted away-win probability | 1.9% |
| Raw p over 1 5 | 99.5% |
| Raw p under 3 5 | 6.3% |
| Raw p btts yes | 73.0% |
| P home draw | 95.0% |
| P draw away | 11.8% |
| P home away | 93.1% |
| Raw p home draw | 98.1% |
| Raw p draw away | 4.8% |
| Raw p home away | 97.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.20 |
| Reference draw odds | 7.00 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:58:10Z |
| Market reference home last update utc | 2026-10-18T11:58:10Z |
| Market reference draw last update utc | 2026-10-18T11:58:10Z |
| Market reference away last update utc | 2026-10-18T11:58:10Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:58:08Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:58:08Z |
| Home probability edge | +7.0% |
| Draw probability edge | -3.9% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | +23.2% |
| Under 2.5 probability edge | -23.2% |
| Raw edge prob home | 0.1402 |
| Raw ev home | 0.1802 |
| Raw edge prob draw | -0.0783 |
| Raw ev draw | -0.7725 |
| Raw edge prob away | -0.0619 |
| Raw ev away | -0.7700 |

</details>


---
