# Premier League — football model report

Fixtures in this report: **15**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,205 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | f6d988748d86cafa4f93679cd23949b2c8c78f2143041abee2f3869ed56381b8 |
| Training as of utc | 2026-10-18T09:56:19.378962+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 65, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 65, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T09:56:19.378962+00:00', 'observations': 73, 'observations_sha256': '1d27299b21954ae6e9630aa457cf07c6550f57c023866140a025a2bd43095bd4', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 48, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 4, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'cd8481836ceaa1e52231bfc6e4b497ca09731370509b93f6bf72b8feb32e4166', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1310.878 |
| Base scoring parameter | 0.223 |
| Home-advantage parameter | 0.165 |
| Dixon-Coles low-score adjustment | -0.092 |
| Xi per day | 0.0019 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261018T095619378962Z_2c3b998bf857d0452b3ff14932391321ffef60cc80106c48b8ea4a7dab202e28.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **46.8%**. Expected goals are 1.54 for Bournemouth and 1.05 for Sunderland (2.59 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 48.1%; Under 3.5 goals: 73.8%; Double Chance 1X: 74.1%; Double Chance X2: 53.2%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 52.2%; BTTS No (at least one team does not score): 47.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 46.8% | 2.14 |
| Draw | 27.3% | 3.66 |
| Sunderland win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.54 |
| Sunderland expected goals | 1.05 |
| Expected total goals | 2.59 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.1% |
| Under 2.5 | 51.9% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.04% |
| 2 | 1-0 | 10.27% |
| 3 | 2-1 | 9.22% |
| 4 | 2-0 | 8.75% |
| 5 | 0-0 | 8.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 46.8% | 46.2% | 2.15 | +0.7% |
| Draw | 27.3% | 26.9% | 3.63 | -0.9% |
| Sunderland win | 25.9% | 26.9% | 3.63 | -6.1% |
| Over 2.5 | 48.1% | 50.3% | 1.96 | -5.7% |
| Under 2.5 | 51.9% | 49.7% | 1.98 | +2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5390 |
| Dc lambda away | 1.0544 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.2% |
| P btts no | 47.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.83 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.20 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 24.9% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 52.3% |
| P home draw | 74.1% |
| P draw away | 53.2% |
| P home away | 72.7% |
| Raw p home draw | 75.1% |
| Raw p draw away | 52.6% |
| Raw p home away | 72.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.10 |
| Reference draw odds | 3.54 |
| Reference away odds | 3.54 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | 0.0113 |
| Raw ev home | 0.0187 |
| Raw edge prob draw | 0.0087 |
| Raw ev draw | 0.0070 |
| Raw edge prob away | -0.0200 |
| Raw ev away | -0.0970 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.4% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 74.6% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.9% |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:03Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.9% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.09 |
| Market reference btts yes last update utc | 2026-10-18T08:35:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **59.9%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.8%; Double Chance 1X: 82.1%; Double Chance X2: 40.1%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 59.9% | 1.67 |
| Draw | 22.2% | 4.51 |
| Crystal Palace win | 17.9% | 5.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.2% |
| Under 3.5 | 65.8% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.85% |
| 2 | 1-1 | 10.47% |
| 3 | 2-0 | 10.08% |
| 4 | 1-0 | 9.80% |
| 5 | 3-1 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 59.9% | 65.3% | 1.54 | -7.7% |
| Draw | 22.2% | 19.7% | 4.83 | +7.0% |
| Crystal Palace win | 17.9% | 15.0% | 6.26 | +12.1% |
| Over 2.5 | 57.2% | 61.2% | 1.63 | -6.8% |
| Under 2.5 | 42.8% | 38.8% | 2.49 | +6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8530 |
| Dc lambda away | 1.0769 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.58 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.11 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.60 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.6% |
| P home draw | 82.1% |
| P draw away | 40.1% |
| P home away | 77.8% |
| Raw p home draw | 79.1% |
| Raw p draw away | 45.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.10 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.41 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -5.4% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.1079 |
| Raw ev home | -0.1601 |
| Raw edge prob draw | 0.0491 |
| Raw ev draw | 0.1886 |
| Raw edge prob away | 0.0588 |
| Raw ev away | 0.3054 |
| Market p home draw | 85.4% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.9% |
| Market draw away odds | 2.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.8% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.79 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.4% |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.24 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:03Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-18T08:35:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.7%**. Expected goals are 1.42 for Leeds United and 1.29 for Manchester United (2.71 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.2%; Double Chance 1X: 66.6%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 72.1%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.1%; BTTS No (at least one team does not score): 43.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.7% | 2.58 |
| Draw | 27.9% | 3.58 |
| Manchester United win | 33.4% | 3.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.29 |
| Expected total goals | 2.71 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 2-1 | 8.59% |
| 3 | 1-0 | 8.26% |
| 4 | 1-2 | 7.94% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.7% | 38.5% | 2.57 | -0.5% |
| Draw | 27.9% | 27.9% | 3.52 | -1.8% |
| Manchester United win | 33.4% | 33.7% | 2.92 | -2.6% |
| Over 2.5 | 50.9% | 51.4% | 1.92 | -2.2% |
| Under 2.5 | 49.1% | 48.6% | 2.02 | -0.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4199 |
| Dc lambda away | 1.2914 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.1% |
| P btts no | 43.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.89 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 56.1% |
| P home draw | 66.6% |
| P draw away | 61.3% |
| P home away | 72.1% |
| Raw p home draw | 66.9% |
| Raw p draw away | 61.0% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.53 |
| Reference draw odds | 3.46 |
| Reference away odds | 2.88 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.0% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0052 |
| Raw ev home | 0.0020 |
| Raw edge prob draw | 0.0006 |
| Raw ev draw | -0.0168 |
| Raw edge prob away | -0.0058 |
| Raw ev away | -0.0341 |
| Market p home draw | 66.4% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 61.8% |
| Market draw away odds | 1.57 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.46 |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:35:38Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.62 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:38Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.1% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:35:38Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 2.98 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:38Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-18T08:35:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.6%**. Expected goals are 0.77 for Nottingham Forest and 1.59 for Arsenal (2.36 combined). The most likely exact score is 0-1 at 14.7%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 42.6%; Under 3.5 goals: 78.5%; Double Chance 1X: 41.4%; Double Chance X2: 84.2%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 43.3%; BTTS No (at least one team does not score): 56.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 15.8% | 6.32 |
| Draw | 25.6% | 3.91 |
| Arsenal win | 58.6% | 1.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.59 |
| Expected total goals | 2.36 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 69.7% |
| Under 1.5 | 30.3% |
| Over 2.5 | 42.6% |
| Under 2.5 | 57.4% |
| Over 3.5 | 21.5% |
| Under 3.5 | 78.5% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.67% |
| 2 | 0-2 | 12.52% |
| 3 | 1-1 | 11.87% |
| 4 | 0-0 | 9.88% |
| 5 | 1-2 | 9.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 15.8% | 14.6% | 6.50 | +2.9% |
| Draw | 25.6% | 23.9% | 4.04 | +3.3% |
| Arsenal win | 58.6% | 61.5% | 1.63 | -4.5% |
| Over 2.5 | 42.6% | 50.0% | 1.97 | -16.0% |
| Under 2.5 | 57.4% | 50.0% | 1.97 | +13.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7711 |
| Dc lambda away | 1.5869 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.3% |
| P btts no | 56.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.12 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.30 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.76 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 55.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.7% |
| Raw p btts yes | 43.8% |
| P home draw | 41.4% |
| P draw away | 84.2% |
| P home away | 74.4% |
| Raw p home draw | 44.3% |
| Raw p draw away | 83.0% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 6.40 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.60 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +1.2% |
| Draw probability edge | +1.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0241 |
| Raw ev home | 0.1073 |
| Raw edge prob draw | 0.0331 |
| Raw ev draw | 0.0999 |
| Raw edge prob away | -0.0572 |
| Raw ev away | -0.0915 |
| Market p home draw | 38.5% |
| Market home draw odds | 2.43 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 85.4% |
| Market draw away odds | 1.15 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.53 |
| Market reference dc draw away odds | 1.14 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:34:52Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.50 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.9% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:34:52Z |
| Market reference under 3 5 odds | 1.31 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:03Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.0% |
| Market btts yes odds | 1.96 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 2.01 |
| Market reference btts yes opposite odds | 1.86 |
| Market reference btts yes last update utc | 2026-10-18T08:35:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **57.0%**. Expected goals are 1.59 for Tottenham Hotspur and 1.05 for Coventry City (2.64 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.6%; Under 3.5 goals: 72.1%; Double Chance 1X: 80.7%; Double Chance X2: 43.0%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 57.0% | 1.76 |
| Draw | 23.7% | 4.22 |
| Coventry City win | 19.3% | 5.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.59 |
| Coventry City expected goals | 1.05 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.00% |
| 2 | 1-1 | 11.33% |
| 3 | 2-1 | 11.09% |
| 4 | 2-0 | 10.53% |
| 5 | 0-0 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 57.0% | 65.3% | 1.54 | -12.3% |
| Draw | 23.7% | 20.2% | 4.72 | +12.0% |
| Coventry City win | 19.3% | 14.5% | 6.47 | +24.9% |
| Over 2.5 | 50.6% | 60.8% | 1.64 | -16.9% |
| Under 2.5 | 49.4% | 39.2% | 2.46 | +21.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T19:00:00+00:00 |
| Fixture id | 9baaf4e48b041cfef04e70e42532502e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5853 |
| Dc lambda away | 1.0528 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.95 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.11 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.59 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.46 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 72.8% |
| Raw p btts yes | 52.9% |
| P home draw | 80.7% |
| P draw away | 43.0% |
| P home away | 76.3% |
| Raw p home draw | 75.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.50 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -8.4% |
| Draw probability edge | +3.6% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.1673 |
| Raw ev home | -0.2514 |
| Raw edge prob draw | 0.0712 |
| Raw ev draw | 0.2876 |
| Raw edge prob away | 0.0962 |
| Raw ev away | 0.5600 |
| Market p home draw | 85.9% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.3% |
| Market draw away odds | 2.65 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.13 |
| Market reference dc draw away odds | 2.75 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-18T08:35:23Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.4% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-18T08:35:03Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.7% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.16 |
| Market reference btts yes last update utc | 2026-10-18T08:35:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **45.6%**. Expected goals are 1.22 for Ipswich Town and 1.78 for Nottingham Forest (3.00 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.4%; Under 3.5 goals: 64.9%; Double Chance 1X: 54.4%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 28.4% | 3.52 |
| Draw | 26.0% | 3.84 |
| Nottingham Forest win | 45.6% | 2.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.78 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.16% |
| 2 | 1-2 | 8.84% |
| 3 | 2-1 | 7.44% |
| 4 | 0-2 | 7.24% |
| 5 | 0-1 | 7.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 28.4% | 31.7% | 3.10 | -11.9% |
| Draw | 26.0% | 26.8% | 3.63 | -5.5% |
| Nottingham Forest win | 45.6% | 41.5% | 2.39 | +8.9% |
| Over 2.5 | 57.4% | 53.9% | 1.84 | +5.5% |
| Under 2.5 | 42.6% | 46.1% | 2.12 | -9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | d0202960708a442401d7fc7bd74a0183 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2201 |
| Dc lambda away | 1.7839 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.29 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.46 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 49.6% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 59.6% |
| P home draw | 54.4% |
| P draw away | 71.6% |
| P home away | 74.0% |
| Raw p home draw | 50.4% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.02 |
| Reference draw odds | 3.54 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -3.3% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | +3.5% |
| Under 2.5 probability edge | -3.5% |
| Raw edge prob home | -0.0653 |
| Raw ev home | -0.2206 |
| Raw edge prob draw | -0.0161 |
| Raw ev draw | -0.0839 |
| Raw edge prob away | 0.0814 |
| Raw ev away | 0.1859 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.3%**. Expected goals are 1.71 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.6%; Double Chance 1X: 89.2%; Double Chance X2: 32.7%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.4%; BTTS No (at least one team does not score): 63.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.3% | 1.49 |
| Draw | 22.0% | 4.55 |
| Everton win | 10.8% | 9.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.71 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.18% |
| 2 | 2-0 | 15.53% |
| 3 | 0-0 | 9.74% |
| 4 | 1-1 | 9.74% |
| 5 | 2-1 | 9.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.3% | 70.7% | 1.43 | -3.8% |
| Draw | 22.0% | 19.1% | 4.93 | +8.3% |
| Everton win | 10.8% | 10.2% | 8.90 | -4.2% |
| Over 2.5 | 41.4% | 54.2% | 1.83 | -24.2% |
| Under 2.5 | 58.6% | 45.8% | 2.14 | +25.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | f66e4f29c1b7bcfc5ab58c0b88c8850b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7102 |
| Dc lambda away | 0.5843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.4% |
| P btts no | 63.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.26 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.59 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 67.7% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 37.2% |
| P home draw | 89.2% |
| P draw away | 32.7% |
| P home away | 78.0% |
| Raw p home draw | 88.7% |
| Raw p draw away | 36.1% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.39 |
| Reference draw odds | 4.80 |
| Reference away odds | 8.70 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -3.4% |
| Draw probability edge | +2.8% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | -0.0679 |
| Raw ev home | -0.0866 |
| Raw edge prob draw | 0.0570 |
| Raw ev draw | 0.2236 |
| Raw edge prob away | 0.0109 |
| Raw ev away | 0.0063 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.9%**. Expected goals are 1.14 for Aston Villa and 1.83 for Manchester City (2.97 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.1%; Double Chance 1X: 45.1%; Double Chance X2: 78.6%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 81.8%; BTTS Yes (both teams score): 57.8%; BTTS No (at least one team does not score): 42.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.4% | 4.67 |
| Draw | 23.7% | 4.22 |
| Manchester City win | 54.9% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.14 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.8% |
| Under 1.5 | 19.2% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.9% |
| Under 3.5 | 65.1% |
| Over 4.5 | 18.2% |
| Under 4.5 | 81.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.15% |
| 2 | 1-2 | 10.21% |
| 3 | 0-2 | 8.97% |
| 4 | 0-1 | 8.76% |
| 5 | 1-3 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.4% | 20.3% | 4.72 | +1.1% |
| Draw | 23.7% | 22.6% | 4.26 | +1.0% |
| Manchester City win | 54.9% | 57.1% | 1.76 | -3.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T11:30:00+00:00 |
| Fixture id | aca5dd297dbee71f576f7641569fe578 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1388 |
| Dc lambda away | 1.8337 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.8% |
| P btts no | 42.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.16 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.21 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.87 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.48 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.5% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 52.6% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 58.1% |
| P home draw | 45.1% |
| P draw away | 78.6% |
| P home away | 76.3% |
| Raw p home draw | 47.4% |
| Raw p draw away | 77.5% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:25Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:25Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.1% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | 0.0223 |
| Raw ev home | 0.0635 |
| Raw edge prob draw | 0.0222 |
| Raw ev draw | 0.0575 |
| Raw edge prob away | -0.0445 |
| Raw ev away | -0.0735 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **54.7%**. Expected goals are 2.10 for Chelsea and 1.22 for Tottenham Hotspur (3.32 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.7%; Double Chance 1X: 77.7%; Double Chance X2: 45.3%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 54.7% | 1.83 |
| Draw | 23.0% | 4.35 |
| Tottenham Hotspur win | 22.3% | 4.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.10 |
| Tottenham Hotspur expected goals | 1.22 |
| Expected total goals | 3.32 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.33% |
| 2 | 2-1 | 9.36% |
| 3 | 2-0 | 7.68% |
| 4 | 3-1 | 6.57% |
| 5 | 1-0 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 54.7% | 52.6% | 1.90 | +4.0% |
| Draw | 23.0% | 23.5% | 4.11 | -5.5% |
| Tottenham Hotspur win | 22.3% | 23.8% | 4.06 | -9.6% |
| Over 2.5 | 64.3% | 60.0% | 1.66 | +6.7% |
| Under 2.5 | 35.7% | 40.0% | 2.42 | -13.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0382a9faef0bb8df1bcc436536cffb05 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1050 |
| Dc lambda away | 1.2189 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.95 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.73 |
| Fair Over 2.5 odds | 1.56 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.37 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.17 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.9% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.7% |
| P home draw | 77.7% |
| P draw away | 45.3% |
| P home away | 77.0% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.1% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.95 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +2.1% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | +4.3% |
| Under 2.5 probability edge | -4.3% |
| Raw edge prob home | 0.0423 |
| Raw ev home | 0.0803 |
| Raw edge prob draw | -0.0108 |
| Raw ev draw | -0.0771 |
| Raw edge prob away | -0.0316 |
| Raw ev away | -0.1601 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **40.4%**. Expected goals are 1.09 for Coventry City and 1.27 for Fulham (2.35 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 42.3%; Under 3.5 goals: 78.8%; Double Chance 1X: 59.6%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 90.9%; BTTS Yes (both teams score): 48.4%; BTTS No (at least one team does not score): 51.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 31.0% | 3.23 |
| Draw | 28.6% | 3.49 |
| Fulham win | 40.4% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.09 |
| Fulham expected goals | 1.27 |
| Expected total goals | 2.35 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.3% |
| Under 2.5 | 57.7% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.1% |
| Under 4.5 | 90.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 0-1 | 11.16% |
| 3 | 0-0 | 10.15% |
| 4 | 1-0 | 9.29% |
| 5 | 1-2 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 31.0% | 31.5% | 3.12 | -3.4% |
| Draw | 28.6% | 27.0% | 3.61 | +3.4% |
| Fulham win | 40.4% | 41.5% | 2.39 | -3.5% |
| Over 2.5 | 42.3% | 54.6% | 1.81 | -23.4% |
| Under 2.5 | 57.7% | 45.4% | 2.15 | +24.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:00:00+00:00 |
| Fixture id | 0fbb2626ed9534b9dcf21d16925f9bd7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0851 |
| Dc lambda away | 1.2661 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.4% |
| P btts no | 51.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.85 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.36 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.72 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.95 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 30.3% |
| Unadjusted away-win probability | 39.3% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 48.7% |
| P home draw | 59.6% |
| P draw away | 69.0% |
| P home away | 71.4% |
| Raw p home draw | 60.7% |
| Raw p draw away | 69.6% |
| Raw p home away | 69.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.52 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -0.5% |
| Draw probability edge | +1.6% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -12.3% |
| Under 2.5 probability edge | +12.3% |
| Raw edge prob home | -0.0103 |
| Raw ev home | -0.0500 |
| Raw edge prob draw | 0.0323 |
| Raw ev draw | 0.0923 |
| Raw edge prob away | -0.0221 |
| Raw ev away | -0.0609 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **37.8%**. Expected goals are 1.48 for Crystal Palace and 1.52 for Newcastle United (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.8%; Under 3.5 goals: 64.6%; Double Chance 1X: 62.2%; Double Chance X2: 64.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 35.8% | 2.79 |
| Draw | 26.3% | 3.80 |
| Newcastle United win | 37.8% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.48 |
| Newcastle United expected goals | 1.52 |
| Expected total goals | 3.01 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.22% |
| 2 | 1-2 | 8.53% |
| 3 | 2-1 | 8.26% |
| 4 | 0-1 | 6.53% |
| 5 | 2-2 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 35.8% | 35.7% | 2.76 | -1.1% |
| Draw | 26.3% | 26.4% | 3.69 | -2.8% |
| Newcastle United win | 37.8% | 37.9% | 2.61 | -1.3% |
| Over 2.5 | 57.8% | 58.9% | 1.69 | -2.3% |
| Under 2.5 | 42.2% | 41.1% | 2.36 | -0.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | fe235b26408c477368c40672a4488694 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4826 |
| Dc lambda away | 1.5229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.71 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.39 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 36.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 37.7% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 61.5% |
| P home draw | 62.2% |
| P draw away | 64.2% |
| P home away | 73.7% |
| Raw p home draw | 62.3% |
| Raw p draw away | 64.0% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.69 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.54 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +0.1% |
| Draw probability edge | -0.0% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | 0.0024 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | -0.0005 |
| Raw ev draw | -0.0287 |
| Raw edge prob away | -0.0019 |
| Raw ev away | -0.0154 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.9%**. Expected goals are 1.24 for Hull City and 1.05 for Brentford (2.29 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 57.1%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 29.9% | 3.35 |
| Draw | 27.2% | 3.68 |
| Brentford win | 42.9% | 2.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.24 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.56% |
| 2 | 1-1 | 12.73% |
| 3 | 0-0 | 10.06% |
| 4 | 1-2 | 9.93% |
| 5 | 1-0 | 8.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 29.9% | 20.3% | 4.72 | +41.0% |
| Draw | 27.2% | 23.6% | 4.09 | +11.1% |
| Brentford win | 42.9% | 56.1% | 1.79 | -23.1% |
| Over 2.5 | 41.1% | 57.3% | 1.73 | -28.9% |
| Under 2.5 | 58.9% | 42.7% | 2.28 | +34.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 69493b5ebb84f24ab1d6023a30ee89f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2403 |
| Dc lambda away | 1.0457 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.87 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 47.3% |
| P home draw | 57.1% |
| P draw away | 70.1% |
| P home away | 72.8% |
| Raw p home draw | 70.2% |
| Raw p draw away | 60.5% |
| Raw p home away | 69.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 3.98 |
| Reference away odds | 1.74 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | +9.6% |
| Draw probability edge | +3.5% |
| Away probability edge | -13.1% |
| Over 2.5 probability edge | -16.2% |
| Under 2.5 probability edge | +16.2% |
| Raw edge prob home | 0.1914 |
| Raw ev home | 0.8621 |
| Raw edge prob draw | 0.0710 |
| Raw ev draw | 0.2564 |
| Raw edge prob away | -0.2624 |
| Raw ev away | -0.4660 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **47.1%**. Expected goals are 1.79 for Liverpool and 1.35 for Brighton and Hove Albion (3.13 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.8%; Under 3.5 goals: 61.7%; Double Chance 1X: 71.8%; Double Chance X2: 52.9%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 62.5%; BTTS No (at least one team does not score): 37.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 47.1% | 2.12 |
| Draw | 24.6% | 4.06 |
| Brighton and Hove Albion win | 28.2% | 3.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.79 |
| Brighton and Hove Albion expected goals | 1.35 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 2-1 | 9.41% |
| 3 | 1-2 | 7.11% |
| 4 | 2-0 | 6.99% |
| 5 | 1-0 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 47.1% | 47.3% | 2.11 | -0.5% |
| Draw | 24.6% | 24.2% | 4.00 | -1.5% |
| Brighton and Hove Albion win | 28.2% | 28.5% | 3.43 | -3.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 290ba8cd3f3a2e9252effca673bf5549 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7884 |
| Dc lambda away | 1.3464 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.5% |
| P btts no | 37.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.13 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.80 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 46.9% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.7% |
| Raw p btts yes | 62.6% |
| P home draw | 71.8% |
| P draw away | 52.9% |
| P home away | 75.4% |
| Raw p home draw | 72.0% |
| Raw p draw away | 53.1% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.34 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:25Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:25Z |
| Home probability edge | -0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0038 |
| Raw ev home | -0.0094 |
| Raw edge prob draw | 0.0081 |
| Raw ev draw | 0.0010 |
| Raw edge prob away | -0.0043 |
| Raw ev away | -0.0387 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.0%**. Expected goals are 1.72 for Manchester United and 1.31 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.7%; Double Chance 1X: 74.1%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.0% | 2.00 |
| Draw | 24.1% | 4.15 |
| Bournemouth win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.72 |
| Bournemouth expected goals | 1.31 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.18% |
| 2 | 2-1 | 10.15% |
| 3 | 1-0 | 7.90% |
| 4 | 2-0 | 7.73% |
| 5 | 1-2 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.0% | 53.8% | 1.86 | -7.1% |
| Draw | 24.1% | 22.6% | 4.26 | +2.8% |
| Bournemouth win | 25.9% | 23.5% | 4.11 | +6.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 33fb7467b23c91d57dc976d9ab05ea97 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7215 |
| Dc lambda away | 1.3129 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.27 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.44 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.16 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 46.1% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 28.3% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 64.0% |
| Raw p btts yes | 61.0% |
| P home draw | 74.1% |
| P draw away | 50.0% |
| P home away | 75.9% |
| Raw p home draw | 71.7% |
| Raw p draw away | 53.9% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.81 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.64 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:25Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:25Z |
| Home probability edge | -3.9% |
| Draw probability edge | +1.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0775 |
| Raw ev home | -0.1429 |
| Raw edge prob draw | 0.0296 |
| Raw ev draw | 0.0907 |
| Raw edge prob away | 0.0479 |
| Raw ev away | 0.1638 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.3%**. Expected goals are 1.10 for Sunderland and 1.20 for Leeds United (2.30 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.2%; Over 2.5 goals: 40.7%; Under 3.5 goals: 79.9%; Double Chance 1X: 62.7%; Double Chance X2: 66.9%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 47.5%; BTTS No (at least one team does not score): 52.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 33.1% | 3.02 |
| Draw | 29.6% | 3.38 |
| Leeds United win | 37.3% | 2.68 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.10 |
| Leeds United expected goals | 1.20 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.2% |
| Under 0.5 | 10.8% |
| Over 1.5 | 68.1% |
| Under 1.5 | 31.9% |
| Over 2.5 | 40.7% |
| Under 2.5 | 59.3% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.90% |
| 2 | 0-1 | 10.91% |
| 3 | 0-0 | 10.84% |
| 4 | 1-0 | 10.12% |
| 5 | 1-2 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 33.1% | 34.0% | 2.90 | -4.0% |
| Draw | 29.6% | 28.4% | 3.44 | +1.8% |
| Leeds United win | 37.3% | 37.6% | 2.63 | -1.9% |
| Over 2.5 | 40.7% | 45.8% | 2.14 | -12.9% |
| Under 2.5 | 59.3% | 54.2% | 1.83 | +8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | e82f6b60fa41b82c8510f5b67ce61849 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0996 |
| Dc lambda away | 1.1971 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T09:56:19.378962+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.5% |
| P btts no | 52.5% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.22 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.85 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 37.0% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 47.8% |
| P home draw | 62.7% |
| P draw away | 66.9% |
| P home away | 70.4% |
| Raw p home draw | 63.0% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.82 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.56 |
| Market reference 1x2 last update utc | 2026-10-18T08:35:29Z |
| Market reference home last update utc | 2026-10-18T08:35:29Z |
| Market reference draw last update utc | 2026-10-18T08:35:29Z |
| Market reference away last update utc | 2026-10-18T08:35:29Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.07 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:29Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0179 |
| Raw ev home | -0.0662 |
| Raw edge prob draw | 0.0237 |
| Raw ev draw | 0.0589 |
| Raw edge prob away | -0.0058 |
| Raw ev away | -0.0264 |

</details>


---
