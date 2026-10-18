# Ligue 1 — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 976 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | a52875f70dfdad85275fceacaaa30cb545749af558b7d57b0088795806680ba7 |
| Training as of utc | 2026-10-18T08:36:44.091007+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 58, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 58, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T08:36:44.091007+00:00', 'observations': 64, 'observations_sha256': 'fcbd29edf8ab8f3e65d0b3144d189df35592ca75cb7f8767a21c68014aa4fa0d', 'eligible_training_matches': 13, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 42, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 3, 'retrospective_eligible_training_matches': 13, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'b4d2f20e19530f0d01b3095a9843b23c28adf827a2424efbd983e284d824be11', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1680.478 |
| Base scoring parameter | 0.201 |
| Home-advantage parameter | 0.195 |
| Dixon-Coles low-score adjustment | -0.046 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 18.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261018T083644091007Z_8fd900f79a2a17bf0cb414fd84cc4cd3e0522c0cd120ef150f8870f6d648790e.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Angers vs Marseille

The model's most likely 1X2 outcome is **Marseille win** at **52.5%**. Expected goals are 0.94 for Angers and 1.71 for Marseille (2.65 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.4%; Under 3.5 goals: 72.7%; Double Chance 1X: 47.5%; Double Chance X2: 77.2%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 22.8% | 4.39 |
| Draw | 24.7% | 4.05 |
| Marseille win | 52.5% | 1.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 0.94 |
| Marseille expected goals | 1.71 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.4% |
| Under 2.5 | 50.6% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.77% |
| 2 | 0-1 | 11.01% |
| 3 | 0-2 | 9.86% |
| 4 | 1-2 | 9.27% |
| 5 | 0-0 | 7.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 22.8% | 25.5% | 3.78 | -13.9% |
| Draw | 24.7% | 24.5% | 3.85 | -4.9% |
| Marseille win | 52.5% | 50.0% | 2.04 | +7.1% |
| Over 2.5 | 49.4% | 59.7% | 1.68 | -17.0% |
| Under 2.5 | 50.6% | 40.3% | 2.38 | +20.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | c7a60aa94470fe959fbf6b0c68060fc1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Marseille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9401 |
| Dc lambda away | 1.7125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.32 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.93 |
| Fair Over 2.5 odds | 2.03 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.66 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.73 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 55.0% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 50.5% |
| P home draw | 47.5% |
| P draw away | 77.2% |
| P home away | 75.3% |
| Raw p home draw | 45.0% |
| Raw p draw away | 80.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.77 |
| Reference draw odds | 3.92 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.29 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | -2.7% |
| Draw probability edge | +0.2% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | -0.0545 |
| Raw ev home | -0.2422 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | -0.0408 |
| Raw edge prob away | 0.0503 |
| Raw ev away | 0.1228 |
| Market p home draw | 50.4% |
| Market home draw odds | 1.87 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.93 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.6% |
| Market over 1 5 odds | 1.16 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:34:47Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.90 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.8% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:34:47Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.8% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:23Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-18T08:36:44Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **38.6%**. Expected goals are 1.17 for Le Havre and 1.17 for Auxerre (2.34 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.7%; Under 3.5 goals: 79.0%; Double Chance 1X: 67.2%; Double Chance X2: 61.4%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 38.6% | 2.59 |
| Draw | 28.6% | 3.49 |
| Auxerre win | 32.8% | 3.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.17 |
| Auxerre expected goals | 1.17 |
| Expected total goals | 2.34 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 41.7% |
| Under 2.5 | 58.3% |
| Over 3.5 | 21.0% |
| Under 3.5 | 79.0% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.49% |
| 2 | 1-0 | 11.61% |
| 3 | 0-0 | 9.99% |
| 4 | 0-1 | 9.87% |
| 5 | 2-1 | 8.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 38.6% | 41.8% | 2.42 | -6.6% |
| Draw | 28.6% | 28.0% | 3.51 | +0.5% |
| Auxerre win | 32.8% | 30.2% | 3.14 | +3.0% |
| Over 2.5 | 41.7% | 51.9% | 1.95 | -18.6% |
| Under 2.5 | 58.3% | 48.1% | 1.99 | +15.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | d637845b9760bb02b55bbbaa32b5c21e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1714 |
| Dc lambda away | 1.1715 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.01 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.18 |
| Fair Over 2.5 odds | 2.40 |
| Fair Under 2.5 odds | 1.72 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 11.18 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 35.4% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.1% |
| Raw p btts yes | 48.2% |
| P home draw | 67.2% |
| P draw away | 61.4% |
| P home away | 71.4% |
| Raw p home draw | 64.6% |
| Raw p draw away | 64.6% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.34 |
| Reference draw odds | 3.46 |
| Reference away odds | 3.21 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | -3.2% |
| Draw probability edge | +0.7% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.0644 |
| Raw ev home | -0.1444 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | 0.0278 |
| Raw edge prob away | 0.0514 |
| Raw ev away | 0.1104 |
| Market p home draw | 69.8% |
| Market home draw odds | 1.41 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:45Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 58.4% |
| Market draw away odds | 1.63 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:45Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.8% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:45Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.66 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 77.4% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.01 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.1% |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.13 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:45Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.9% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:23Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.27 |
| Market reference btts yes last update utc | 2026-10-18T08:36:45Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **47.0%**. Expected goals are 1.36 for Lorient and 1.81 for AS Monaco (3.18 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.8%; Under 3.5 goals: 60.9%; Double Chance 1X: 53.0%; Double Chance X2: 73.1%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 78.8%; BTTS Yes (both teams score): 63.2%; BTTS No (at least one team does not score): 36.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 26.9% | 3.72 |
| Draw | 26.1% | 3.84 |
| AS Monaco win | 47.0% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.36 |
| AS Monaco expected goals | 1.81 |
| Expected total goals | 3.18 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.8% |
| Under 2.5 | 39.2% |
| Over 3.5 | 39.1% |
| Under 3.5 | 60.9% |
| Over 4.5 | 21.2% |
| Under 4.5 | 78.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.78% |
| 2 | 1-2 | 9.23% |
| 3 | 0-1 | 7.00% |
| 4 | 2-2 | 6.96% |
| 5 | 0-2 | 6.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 26.9% | 25.3% | 3.80 | +2.2% |
| Draw | 26.1% | 28.2% | 3.49 | -9.1% |
| AS Monaco win | 47.0% | 46.4% | 2.15 | +1.1% |
| Over 2.5 | 60.8% | 47.2% | 2.05 | +24.6% |
| Under 2.5 | 39.2% | 52.8% | 1.89 | -25.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 53f5fe7ed0ba0fbf6345c73270e4cd00 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lorient |
| Matched away-team name | Monaco |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3622 |
| Dc lambda away | 1.8143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.2% |
| P btts no | 36.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.69 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.55 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.72 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 28.5% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 47.7% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.8% |
| Raw p btts yes | 62.7% |
| P home draw | 53.0% |
| P draw away | 73.1% |
| P home away | 73.9% |
| Raw p home draw | 52.3% |
| Raw p draw away | 71.5% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.80 |
| Reference draw odds | 3.42 |
| Reference away odds | 2.11 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +1.6% |
| Draw probability edge | -2.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | +13.6% |
| Under 2.5 probability edge | -13.6% |
| Raw edge prob home | 0.0310 |
| Raw ev home | 0.0811 |
| Raw edge prob draw | -0.0438 |
| Raw ev draw | -0.1671 |
| Raw edge prob away | 0.0128 |
| Raw ev away | 0.0252 |
| Market p home draw | 54.3% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 74.2% |
| Market draw away odds | 1.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.5% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.79 |
| Market reference dc draw away odds | 1.31 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 73.8% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:35:12Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.53 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:45Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 74.3% |
| Market under 3 5 odds | 1.27 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:35:12Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.57 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:45Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.1% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:23Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-18T08:36:44Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **51.9%**. Expected goals are 1.77 for Lyon and 1.09 for Nice (2.86 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.3%; Under 3.5 goals: 68.0%; Double Chance 1X: 76.5%; Double Chance X2: 48.1%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 51.9% | 1.93 |
| Draw | 24.6% | 4.06 |
| Nice win | 23.5% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.77 |
| Nice expected goals | 1.09 |
| Expected total goals | 2.86 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 32.0% |
| Under 3.5 | 68.0% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.65% |
| 2 | 2-1 | 9.60% |
| 3 | 1-0 | 9.46% |
| 4 | 2-0 | 8.82% |
| 5 | 0-0 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 51.9% | 50.9% | 1.92 | -0.4% |
| Draw | 24.6% | 24.8% | 3.94 | -3.0% |
| Nice win | 23.5% | 24.3% | 4.16 | -2.2% |
| Over 2.5 | 54.3% | 57.8% | 1.75 | -4.9% |
| Under 2.5 | 45.7% | 42.2% | 2.25 | +2.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 471f891b1f6516a864ad94c8eb649f5e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lyon |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7717 |
| Dc lambda away | 1.0876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.88 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.61 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.12 |
| Fair Under 3.5 odds | 1.47 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 52.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 78.4% |
| Raw p under 3 5 | 67.9% |
| Raw p btts yes | 55.5% |
| P home draw | 76.5% |
| P draw away | 48.1% |
| P home away | 75.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 47.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.93 |
| Reference draw odds | 3.88 |
| Reference away odds | 3.96 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.16 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | 0.0201 |
| Raw ev home | 0.0154 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0384 |
| Raw edge prob away | -0.0159 |
| Raw ev away | -0.0552 |
| Market p home draw | 75.4% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:49Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.9% |
| Market draw away odds | 1.98 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:49Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:49Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 79.5% |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.0% |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.76 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:45Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 59.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:23Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.34 |
| Market reference btts yes last update utc | 2026-10-18T08:36:49Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **43.5%**. Expected goals are 1.57 for Paris FC and 1.37 for Rennes (2.94 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.1%; Double Chance 1X: 69.6%; Double Chance X2: 56.5%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 82.6%; BTTS Yes (both teams score): 59.6%; BTTS No (at least one team does not score): 40.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 43.5% | 2.30 |
| Draw | 26.1% | 3.84 |
| Rennes win | 30.4% | 3.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.57 |
| Rennes expected goals | 1.37 |
| Expected total goals | 2.94 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 79.7% |
| Under 1.5 | 20.3% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.9% |
| Under 3.5 | 66.1% |
| Over 4.5 | 17.4% |
| Under 4.5 | 82.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 2-1 | 9.32% |
| 3 | 1-0 | 8.14% |
| 4 | 1-2 | 7.22% |
| 5 | 2-0 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 43.5% | 45.3% | 2.26 | -1.6% |
| Draw | 26.1% | 26.6% | 3.54 | -7.7% |
| Rennes win | 30.4% | 28.0% | 3.44 | +4.6% |
| Over 2.5 | 56.1% | 57.8% | 1.73 | -3.0% |
| Under 2.5 | 43.9% | 42.2% | 2.29 | +0.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:15:00+00:00 |
| Fixture id | 27f7222d2abde93fc6e8d17b5b05b272 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paris FC |
| Matched away-team name | Rennes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5687 |
| Dc lambda away | 1.3672 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 59.6% |
| P btts no | 40.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.77 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.92 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.95 |
| Fair Under 3.5 odds | 1.51 |
| Fair Over 4.5 odds | 5.76 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 41.7% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 32.8% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 66.2% |
| Raw p btts yes | 59.5% |
| P home draw | 69.6% |
| P draw away | 56.5% |
| P home away | 73.9% |
| Raw p home draw | 67.2% |
| Raw p draw away | 58.3% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.16 |
| Reference draw odds | 3.63 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | -1.8% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0364 |
| Raw ev home | -0.0575 |
| Raw edge prob draw | -0.0109 |
| Raw ev draw | -0.0965 |
| Raw edge prob away | 0.0473 |
| Raw ev away | 0.1274 |
| Market p home draw | 70.9% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:44Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.5% |
| Market draw away odds | 1.71 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:44Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:44Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.33 |
| Market reference dc draw away odds | 1.67 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.9% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.70 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:45Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:45Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 61.3% |
| Market btts yes odds | 1.53 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:23Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.40 |
| Market reference btts yes last update utc | 2026-10-18T08:36:44Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **43.2%**. Expected goals are 1.56 for Brest and 1.27 for Nice (2.83 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 70.3%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 43.2% | 2.32 |
| Draw | 27.1% | 3.69 |
| Nice win | 29.7% | 3.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.56 |
| Nice expected goals | 1.27 |
| Expected total goals | 2.83 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 2-1 | 9.06% |
| 3 | 1-0 | 8.60% |
| 4 | 1-2 | 7.22% |
| 5 | 2-0 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 43.2% | 42.9% | 2.31 | -0.3% |
| Draw | 27.1% | 28.3% | 3.49 | -5.4% |
| Nice win | 29.7% | 28.8% | 3.37 | +0.2% |
| Over 2.5 | 53.4% | 56.7% | 1.76 | -6.1% |
| Under 2.5 | 46.6% | 43.3% | 2.23 | +4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 8aa36b30d655d6c81ed98bf9ec1b4039 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brest |
| Matched away-team name | Nice |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5564 |
| Dc lambda away | 1.2733 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.85 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 43.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.5% |
| Raw p btts yes | 57.4% |
| P home draw | 70.3% |
| P draw away | 56.8% |
| P home away | 72.9% |
| Raw p home draw | 69.3% |
| Raw p draw away | 56.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.24 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +0.2% |
| Draw probability edge | -1.2% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | 0.0046 |
| Raw ev home | 0.0026 |
| Raw edge prob draw | -0.0233 |
| Raw ev draw | -0.0950 |
| Raw edge prob away | 0.0187 |
| Raw ev away | 0.0334 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **48.3%**. Expected goals are 1.59 for RC Lens and 1.01 for Paris FC (2.59 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 48.2%; Under 3.5 goals: 73.8%; Double Chance 1X: 73.9%; Double Chance X2: 51.7%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 87.8%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 48.3% | 2.07 |
| Draw | 25.6% | 3.91 |
| Paris FC win | 26.1% | 3.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.59 |
| Paris FC expected goals | 1.01 |
| Expected total goals | 2.59 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 26.2% |
| Under 3.5 | 73.8% |
| Over 4.5 | 12.2% |
| Under 4.5 | 87.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.18% |
| 2 | 1-0 | 10.86% |
| 3 | 2-1 | 9.10% |
| 4 | 2-0 | 9.04% |
| 5 | 0-0 | 7.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 48.3% | 46.4% | 2.09 | +1.0% |
| Draw | 25.6% | 24.9% | 3.90 | -0.3% |
| Paris FC win | 26.1% | 28.7% | 3.58 | -6.6% |
| Over 2.5 | 48.2% | 59.4% | 1.68 | -19.1% |
| Under 2.5 | 51.8% | 40.6% | 2.38 | +23.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5879 |
| Dc lambda away | 1.0071 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.79 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.82 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.20 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 51.1% |
| P home draw | 73.9% |
| P draw away | 51.7% |
| P home away | 74.4% |
| Raw p home draw | 76.5% |
| Raw p draw away | 49.7% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.08 |
| Reference draw odds | 3.76 |
| Reference away odds | 3.28 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +2.0% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.0396 |
| Raw ev home | 0.0516 |
| Raw edge prob draw | 0.0132 |
| Raw ev draw | 0.0226 |
| Raw edge prob away | -0.0527 |
| Raw ev away | -0.1599 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **68.1%**. Expected goals are 2.45 for Toulouse and 0.66 for Troyes (3.11 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.9%; Under 3.5 goals: 64.1%; Double Chance 1X: 87.0%; Double Chance X2: 31.9%; Double Chance 12 (either team wins): 81.1%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 46.1%; BTTS No (at least one team does not score): 53.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 68.1% | 1.47 |
| Draw | 18.9% | 5.29 |
| Troyes win | 13.0% | 7.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 2.45 |
| Troyes expected goals | 0.66 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 35.9% |
| Under 3.5 | 64.1% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.92% |
| 2 | 3-0 | 9.72% |
| 3 | 1-0 | 9.44% |
| 4 | 1-1 | 9.01% |
| 5 | 2-1 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 68.1% | 59.9% | 1.71 | +16.5% |
| Draw | 18.9% | 21.9% | 4.26 | -19.5% |
| Troyes win | 13.0% | 18.2% | 5.13 | -33.4% |
| Over 2.5 | 57.9% | 59.8% | 1.67 | -3.3% |
| Under 2.5 | 42.1% | 40.2% | 2.40 | +1.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T15:15:00+00:00 |
| Fixture id | 0bbce95e5764e706e6c428bb52dc5536 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4462 |
| Dc lambda away | 0.6631 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 46.1% |
| P btts no | 53.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.53 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.24 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 76.3% |
| Unadjusted draw probability | 15.9% |
| Unadjusted away-win probability | 7.8% |
| Raw p over 1 5 | 82.0% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 44.6% |
| P home draw | 87.0% |
| P draw away | 31.9% |
| P home away | 81.1% |
| Raw p home draw | 92.2% |
| Raw p draw away | 23.7% |
| Raw p home away | 84.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.18 |
| Reference away odds | 4.98 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +8.2% |
| Draw probability edge | -3.0% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.1641 |
| Raw ev home | 0.3052 |
| Raw edge prob draw | -0.0600 |
| Raw ev draw | -0.3228 |
| Raw edge prob away | -0.1041 |
| Raw ev away | -0.6011 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **43.2%**. Expected goals are 1.46 for AS Monaco and 1.26 for Lille (2.72 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.0%; Double Chance 1X: 71.2%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 43.2% | 2.31 |
| Draw | 28.0% | 3.58 |
| Lille win | 28.8% | 3.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.46 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.72 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 29.0% |
| Under 3.5 | 71.0% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.29% |
| 2 | 1-0 | 9.50% |
| 3 | 2-1 | 9.25% |
| 4 | 0-0 | 7.52% |
| 5 | 2-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 43.2% | 45.0% | 2.18 | -5.8% |
| Draw | 28.0% | 29.2% | 3.60 | +0.7% |
| Lille win | 28.8% | 25.7% | 3.60 | +3.8% |
| Over 2.5 | 50.6% | 54.7% | 1.77 | -10.4% |
| Under 2.5 | 49.4% | 45.3% | 2.22 | +9.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4612 |
| Dc lambda away | 1.2553 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.31 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.45 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.23 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 71.0% |
| Raw p btts yes | 55.5% |
| P home draw | 71.2% |
| P draw away | 56.8% |
| P home away | 72.0% |
| Raw p home draw | 68.1% |
| Raw p draw away | 58.6% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.14 |
| Reference draw odds | 3.23 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | -1.8% |
| Draw probability edge | -1.3% |
| Away probability edge | +3.1% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0365 |
| Raw ev home | -0.0980 |
| Raw edge prob draw | -0.0255 |
| Raw ev draw | -0.0390 |
| Raw edge prob away | 0.0620 |
| Raw ev away | 0.1494 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **36.5%**. Expected goals are 1.09 for Angers and 1.24 for Lorient (2.33 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.2%; Under 3.5 goals: 79.4%; Double Chance 1X: 63.5%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.2% | 2.92 |
| Draw | 29.3% | 3.41 |
| Lorient win | 36.5% | 2.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.09 |
| Lorient expected goals | 1.24 |
| Expected total goals | 2.33 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.2% |
| Under 2.5 | 58.8% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.78% |
| 2 | 1-0 | 10.78% |
| 3 | 0-1 | 10.70% |
| 4 | 0-0 | 10.35% |
| 5 | 2-1 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.2% | 36.7% | 2.69 | -7.9% |
| Draw | 29.3% | 29.4% | 3.40 | -0.3% |
| Lorient win | 36.5% | 34.0% | 2.85 | +3.9% |
| Over 2.5 | 41.2% | 46.3% | 2.19 | -9.9% |
| Under 2.5 | 58.8% | 53.7% | 1.79 | +5.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0917 |
| Dc lambda away | 1.2386 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.66 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.84 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.48 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 39.0% |
| Raw p over 1 5 | 68.2% |
| Raw p under 3 5 | 79.3% |
| Raw p btts yes | 47.8% |
| P home draw | 63.5% |
| P draw away | 65.8% |
| P home away | 70.7% |
| Raw p home draw | 61.0% |
| Raw p draw away | 68.2% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.61 |
| Reference draw odds | 3.23 |
| Reference away odds | 2.81 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | -2.5% |
| Draw probability edge | -0.0% |
| Away probability edge | +2.5% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0492 |
| Raw ev home | -0.1457 |
| Raw edge prob draw | -0.0008 |
| Raw ev draw | -0.0047 |
| Raw edge prob away | 0.0501 |
| Raw ev away | 0.1106 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **46.2%**. Expected goals are 1.82 for Auxerre and 1.40 for Le Mans FC (3.22 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.0%; Under 3.5 goals: 59.9%; Double Chance 1X: 71.1%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 77.9%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 46.2% | 2.16 |
| Draw | 24.9% | 4.02 |
| Le Mans FC win | 28.9% | 3.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.82 |
| Le Mans FC expected goals | 1.40 |
| Expected total goals | 3.22 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 83.6% |
| Under 1.5 | 16.4% |
| Over 2.5 | 62.0% |
| Under 2.5 | 38.0% |
| Over 3.5 | 40.1% |
| Under 3.5 | 59.9% |
| Over 4.5 | 22.1% |
| Under 4.5 | 77.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.15% |
| 2 | 2-1 | 9.11% |
| 3 | 1-2 | 7.04% |
| 4 | 2-2 | 6.79% |
| 5 | 1-0 | 6.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 46.2% | 45.4% | 2.23 | +3.1% |
| Draw | 24.9% | 26.0% | 3.70 | -7.9% |
| Le Mans FC win | 28.9% | 28.6% | 3.37 | -2.7% |
| Over 2.5 | 62.0% | 52.9% | 1.78 | +10.4% |
| Under 2.5 | 38.0% | 47.1% | 2.20 | -16.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8205 |
| Dc lambda away | 1.3990 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.37 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 6.09 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.53 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 23.8% |
| Unadjusted away-win probability | 29.2% |
| Raw p over 1 5 | 83.6% |
| Raw p under 3 5 | 59.8% |
| Raw p btts yes | 63.6% |
| P home draw | 71.1% |
| P draw away | 53.8% |
| P home away | 75.1% |
| Raw p home draw | 70.8% |
| Raw p draw away | 53.0% |
| Raw p home away | 76.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.12 |
| Reference draw odds | 3.61 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:44Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +0.8% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | +9.2% |
| Under 2.5 probability edge | -9.2% |
| Raw edge prob home | 0.0159 |
| Raw ev home | 0.0490 |
| Raw edge prob draw | -0.0223 |
| Raw ev draw | -0.1207 |
| Raw edge prob away | 0.0064 |
| Raw ev away | -0.0160 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.1%**. Expected goals are 2.13 for Marseille and 0.86 for Le Havre (2.99 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 56.9%; Under 3.5 goals: 65.5%; Double Chance 1X: 84.0%; Double Chance X2: 36.9%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.1% | 1.58 |
| Draw | 20.8% | 4.81 |
| Le Havre win | 16.0% | 6.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.13 |
| Le Havre expected goals | 0.86 |
| Expected total goals | 2.99 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.9% |
| Under 2.5 | 43.1% |
| Over 3.5 | 34.5% |
| Under 3.5 | 65.5% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.90% |
| 2 | 1-1 | 9.89% |
| 3 | 1-0 | 9.85% |
| 4 | 2-1 | 9.38% |
| 5 | 3-0 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.1% | 60.3% | 1.64 | +3.6% |
| Draw | 20.8% | 21.3% | 4.57 | -4.9% |
| Le Havre win | 16.0% | 18.4% | 5.33 | -14.5% |
| Over 2.5 | 56.9% | 59.4% | 1.66 | -5.5% |
| Under 2.5 | 43.1% | 40.6% | 2.42 | +4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1258 |
| Dc lambda away | 0.8608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.84 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.99 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 66.0% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 13.6% |
| Raw p over 1 5 | 80.3% |
| Raw p under 3 5 | 65.0% |
| Raw p btts yes | 51.3% |
| P home draw | 84.0% |
| P draw away | 36.9% |
| P home away | 79.2% |
| Raw p home draw | 86.4% |
| Raw p draw away | 34.0% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.60 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:23Z |
| Home probability edge | +2.9% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0578 |
| Raw ev home | 0.0831 |
| Raw edge prob draw | -0.0097 |
| Raw ev draw | -0.0712 |
| Raw edge prob away | -0.0481 |
| Raw ev away | -0.2732 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **68.0%**. Expected goals are 2.31 for Paris Saint Germain and 1.06 for Lyon (3.37 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 66.2%; Under 3.5 goals: 56.0%; Double Chance 1X: 86.0%; Double Chance X2: 32.0%; Double Chance 12 (either team wins): 82.0%; Under 4.5 goals: 74.5%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 68.0% | 1.47 |
| Draw | 18.0% | 5.55 |
| Lyon win | 14.0% | 7.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.31 |
| Lyon expected goals | 1.06 |
| Expected total goals | 3.37 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 85.7% |
| Under 1.5 | 14.3% |
| Over 2.5 | 66.2% |
| Under 2.5 | 33.8% |
| Over 3.5 | 44.0% |
| Under 3.5 | 56.0% |
| Over 4.5 | 25.5% |
| Under 4.5 | 74.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.17% |
| 2 | 2-0 | 9.59% |
| 3 | 1-1 | 8.16% |
| 4 | 1-0 | 7.88% |
| 5 | 3-1 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 68.0% | 71.0% | 1.43 | -2.8% |
| Draw | 18.0% | 16.6% | 5.44 | -2.0% |
| Lyon win | 14.0% | 12.4% | 7.60 | +6.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3135 |
| Dc lambda away | 1.0601 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.23 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.97 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.27 |
| Fair Under 3.5 odds | 1.79 |
| Fair Over 4.5 odds | 3.92 |
| Fair Under 4.5 odds | 1.34 |
| Unadjusted home-win probability | 65.0% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 85.4% |
| Raw p under 3 5 | 56.4% |
| Raw p btts yes | 59.3% |
| P home draw | 86.0% |
| P draw away | 32.0% |
| P home away | 82.0% |
| Raw p home draw | 84.4% |
| Raw p draw away | 35.0% |
| Raw p home away | 80.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.36 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Home probability edge | -3.0% |
| Draw probability edge | +1.4% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0596 |
| Raw ev home | -0.0703 |
| Raw edge prob draw | 0.0278 |
| Raw ev draw | 0.0556 |
| Raw edge prob away | 0.0318 |
| Raw ev away | 0.1842 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **51.8%**. Expected goals are 1.87 for Rennes and 1.48 for Strasbourg (3.36 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.7%; Under 3.5 goals: 56.6%; Double Chance 1X: 73.8%; Double Chance X2: 48.2%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 74.9%; BTTS Yes (both teams score): 65.5%; BTTS No (at least one team does not score): 34.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 51.8% | 1.93 |
| Draw | 22.1% | 4.53 |
| Strasbourg win | 26.2% | 3.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.87 |
| Strasbourg expected goals | 1.48 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.7% |
| Under 2.5 | 34.3% |
| Over 3.5 | 43.4% |
| Under 3.5 | 56.6% |
| Over 4.5 | 25.1% |
| Under 4.5 | 74.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.12% |
| 2 | 1-1 | 9.61% |
| 3 | 2-0 | 6.81% |
| 4 | 1-0 | 6.78% |
| 5 | 2-2 | 6.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 51.8% | 57.1% | 1.74 | -9.9% |
| Draw | 22.1% | 20.9% | 4.52 | -0.2% |
| Strasbourg win | 26.2% | 22.0% | 4.58 | +19.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:36:23Z |
| Market best draw last update utc | 2026-10-18T08:36:23Z |
| Market best away last update utc | 2026-10-18T08:36:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8707 |
| Dc lambda away | 1.4845 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:44.091007+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.5% |
| P btts no | 34.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.78 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.85 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.30 |
| Fair Under 3.5 odds | 1.77 |
| Fair Over 4.5 odds | 3.99 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 46.4% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 85.2% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 65.9% |
| P home draw | 73.8% |
| P draw away | 48.2% |
| P home away | 77.9% |
| Raw p home draw | 69.7% |
| Raw p draw away | 53.6% |
| Raw p home away | 76.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.67 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:45Z |
| Market reference home last update utc | 2026-10-18T08:36:45Z |
| Market reference draw last update utc | 2026-10-18T08:36:45Z |
| Market reference away last update utc | 2026-10-18T08:36:45Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:45Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:45Z |
| Home probability edge | -5.4% |
| Draw probability edge | +1.2% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.1074 |
| Raw ev home | -0.1929 |
| Raw edge prob draw | 0.0242 |
| Raw ev draw | 0.0528 |
| Raw edge prob away | 0.0831 |
| Raw ev away | 0.3888 |

</details>


---
