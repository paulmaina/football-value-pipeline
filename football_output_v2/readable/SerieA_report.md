# Serie A — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,204 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 2daa2277a33aa78a7fc64a35b9c1fcb559029205c5bb3c1feb07d274a16cb356 |
| Training as of utc | 2026-10-18T14:34:33.287337+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 64, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 64, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T14:34:33.287337+00:00', 'observations': 78, 'observations_sha256': '3c0ed3e5b79d831ea5dfbc093ace97a9135205fbd11f3cbbe901038e53ac324d', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 40, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '0b92d19a30ce70e2b0ea5653218420f57abfaaff0806535c02e4e649ff5b9044', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 845.238 |
| Base scoring parameter | 0.129 |
| Home-advantage parameter | 0.119 |
| Dixon-Coles low-score adjustment | -0.005 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 6.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261018T143433287337Z_6322a7a0c838a15549bb8ac4dd8fdfbf55b85d50749f12598e6fa9c56ae611fd.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **49.2%**. Expected goals are 1.30 for AC Milan and 1.15 for Atalanta BC (2.45 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 45.1%; Under 3.5 goals: 76.6%; Double Chance 1X: 74.6%; Double Chance X2: 50.8%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 49.2% | 2.03 |
| Draw | 25.3% | 3.95 |
| Atalanta BC win | 25.4% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.30 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.76% |
| 2 | 1-1 | 12.00% |
| 3 | 2-1 | 10.33% |
| 4 | 2-0 | 9.00% |
| 5 | 0-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 49.2% | 58.5% | 1.77 | -12.8% |
| Draw | 25.3% | 23.3% | 4.12 | +4.3% |
| Atalanta BC win | 25.4% | 18.2% | 4.83 | +22.9% |
| Over 2.5 | 45.1% | 59.8% | 1.68 | -24.3% |
| Under 2.5 | 54.9% | 40.2% | 2.38 | +30.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.3009 |
| Dc lambda away | 1.1478 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.42 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.55 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 40.0% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 49.7% |
| P home draw | 74.6% |
| P draw away | 50.8% |
| P home away | 74.7% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.0% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.65 |
| Reference draw odds | 3.90 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | -9.2% |
| Draw probability edge | +2.0% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -14.7% |
| Under 2.5 probability edge | +14.7% |
| Raw edge prob home | -0.1849 |
| Raw ev home | -0.2921 |
| Raw edge prob draw | 0.0408 |
| Raw ev draw | 0.1273 |
| Raw edge prob away | 0.1441 |
| Raw ev away | 0.5766 |
| Market p home draw | 79.9% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:33Z |
| Market reference home draw last update utc | 2026-10-18T14:34:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.0% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:33Z |
| Market reference draw away last update utc | 2026-10-18T14:34:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:33Z |
| Market reference home away last update utc | 2026-10-18T14:34:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.19 |
| Market reference dc draw away odds | 2.16 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.6% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:33Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.1% |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.59 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.1% |
| Market btts yes odds | 1.60 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:33Z |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.36 |
| Market reference btts yes last update utc | 2026-10-18T14:34:34Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **56.2%**. Expected goals are 1.37 for Juventus and 0.86 for Lazio (2.23 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.9%; Double Chance 1X: 81.1%; Double Chance X2: 43.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.2%; BTTS No (at least one team does not score): 57.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 56.2% | 1.78 |
| Draw | 25.0% | 4.01 |
| Lazio win | 18.9% | 5.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.86 |
| Expected total goals | 2.23 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.92% |
| 2 | 2-0 | 11.64% |
| 3 | 1-1 | 11.43% |
| 4 | 2-1 | 10.01% |
| 5 | 0-0 | 9.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 56.2% | 63.7% | 1.61 | -9.6% |
| Draw | 25.0% | 22.1% | 4.27 | +6.6% |
| Lazio win | 18.9% | 14.2% | 6.30 | +18.8% |
| Over 2.5 | 39.7% | 51.5% | 1.96 | -22.1% |
| Under 2.5 | 60.3% | 48.5% | 1.98 | +19.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3695 |
| Dc lambda away | 0.8603 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.2% |
| P btts no | 57.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.30 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.62 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.1% |
| P home draw | 81.1% |
| P draw away | 43.8% |
| P home away | 75.0% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.3% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 1.52 |
| Reference draw odds | 4.05 |
| Reference away odds | 6.10 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | -7.5% |
| Draw probability edge | +2.8% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.1497 |
| Raw ev home | -0.2161 |
| Raw edge prob draw | 0.0569 |
| Raw ev draw | 0.1874 |
| Raw edge prob away | 0.0928 |
| Raw ev away | 0.4807 |
| Market p home draw | 83.5% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:33Z |
| Market reference home draw last update utc | 2026-10-18T14:34:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.7% |
| Market draw away odds | 2.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:33Z |
| Market reference draw away last update utc | 2026-10-18T14:34:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:33Z |
| Market reference home away last update utc | 2026-10-18T14:34:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.14 |
| Market reference dc draw away odds | 2.40 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 76.2% |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.83 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:37Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.5% |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.24 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:37Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.6% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:33Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.97 |
| Market reference btts yes last update utc | 2026-10-18T14:34:34Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.5%**. Expected goals are 1.14 for Monza and 1.60 for Cagliari (2.74 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.1%; Double Chance 1X: 60.5%; Double Chance X2: 66.8%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.1%; BTTS No (at least one team does not score): 44.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.2% | 3.01 |
| Draw | 27.4% | 3.65 |
| Cagliari win | 39.5% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.14 |
| Cagliari expected goals | 1.60 |
| Expected total goals | 2.74 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.99% |
| 2 | 1-0 | 8.98% |
| 3 | 0-1 | 8.46% |
| 4 | 2-1 | 8.23% |
| 5 | 1-2 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.2% | 39.4% | 2.49 | -17.4% |
| Draw | 27.4% | 29.8% | 3.25 | -11.0% |
| Cagliari win | 39.5% | 30.8% | 3.25 | +28.2% |
| Over 2.5 | 50.4% | 45.2% | 2.15 | +8.5% |
| Under 2.5 | 49.6% | 54.8% | 1.82 | -9.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1360 |
| Dc lambda away | 1.6007 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.1% |
| P btts no | 44.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.94 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.26 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 27.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 48.1% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.3% |
| P home draw | 60.5% |
| P draw away | 66.8% |
| P home away | 72.6% |
| Raw p home draw | 51.9% |
| Raw p draw away | 73.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 2.42 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | -6.2% |
| Draw probability edge | -2.4% |
| Away probability edge | +8.6% |
| Over 2.5 probability edge | +5.3% |
| Under 2.5 probability edge | -5.3% |
| Raw edge prob home | -0.1238 |
| Raw ev home | -0.3282 |
| Raw edge prob draw | -0.0486 |
| Raw ev draw | -0.1893 |
| Raw edge prob away | 0.1724 |
| Raw ev away | 0.5625 |
| Market p home draw | 68.8% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:33Z |
| Market reference home draw last update utc | 2026-10-18T14:34:33Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.9% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:33Z |
| Market reference draw away last update utc | 2026-10-18T14:34:33Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.3% |
| Market home away odds | 1.39 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:33Z |
| Market reference home away last update utc | 2026-10-18T14:34:33Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.56 |
| Market reference dc home away odds | 1.35 |
| Market p over 1 5 | 73.6% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:33:11Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:37Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:33:11Z |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.2% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:33Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 2.10 |
| Market reference btts yes last update utc | 2026-10-18T14:34:34Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.9%**. Expected goals are 1.01 for Parma and 1.10 for Torino (2.10 combined). The most likely exact score is 0-1 at 13.9%. Goal-market probabilities: at least one goal: 87.5%; Over 2.5 goals: 34.9%; Under 3.5 goals: 83.8%; Double Chance 1X: 61.1%; Double Chance X2: 69.5%; Double Chance 12 (either team wins): 69.4%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.5% | 3.28 |
| Draw | 30.6% | 3.26 |
| Torino win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.01 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.5% |
| Under 0.5 | 12.5% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 34.9% |
| Under 2.5 | 65.1% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.89% |
| 2 | 1-1 | 13.82% |
| 3 | 0-0 | 12.53% |
| 4 | 1-0 | 11.40% |
| 5 | 1-2 | 7.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.5% | 28.3% | 3.43 | +4.6% |
| Draw | 30.6% | 31.3% | 3.17 | -2.9% |
| Torino win | 38.9% | 40.5% | 2.45 | -4.8% |
| Over 2.5 | 34.9% | 39.6% | 2.49 | -13.0% |
| Under 2.5 | 65.1% | 60.4% | 1.63 | +6.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0069 |
| Dc lambda away | 1.0959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.98 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.64 |
| Fair Over 2.5 odds | 2.86 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.18 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.11 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.7% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 62.2% |
| Raw p under 3 5 | 83.8% |
| Raw p btts yes | 42.3% |
| P home draw | 61.1% |
| P draw away | 69.5% |
| P home away | 69.4% |
| Raw p home draw | 62.7% |
| Raw p draw away | 67.3% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Nordic Bet |
| Reference home odds | 3.30 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.32 |
| Reference Under 2.5 odds | 1.58 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +2.2% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0445 |
| Raw ev home | 0.1218 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.0482 |
| Raw edge prob away | -0.0321 |
| Raw ev away | -0.0869 |
| Market p home draw | 59.8% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:33Z |
| Market reference home draw last update utc | 2026-10-18T14:34:39Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:33Z |
| Market reference draw away last update utc | 2026-10-18T14:34:39Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.8% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:33Z |
| Market reference home away last update utc | 2026-10-18T14:34:39Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.61 |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home away odds | 1.40 |
| Market p over 1 5 | 67.8% |
| Market over 1 5 odds | 1.44 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T14:34:26Z |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.89 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:37Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 81.1% |
| Market under 3 5 odds | 1.18 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T14:34:26Z |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:33Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.6% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:33Z |
| Market reference btts yes odds | 2.02 |
| Market reference btts yes opposite odds | 1.91 |
| Market reference btts yes last update utc | 2026-10-18T14:34:34Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.2%**. Expected goals are 1.93 for Torino and 1.17 for Monza (3.11 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 58.8%; Under 3.5 goals: 62.7%; Double Chance 1X: 75.4%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.2% | 1.99 |
| Draw | 25.2% | 3.97 |
| Monza win | 24.6% | 4.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.93 |
| Monza expected goals | 1.17 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.60% |
| 2 | 2-1 | 8.95% |
| 3 | 1-0 | 7.85% |
| 4 | 2-0 | 7.64% |
| 5 | 2-2 | 6.54% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.2% | 45.3% | 2.15 | +8.0% |
| Draw | 25.2% | 28.2% | 3.62 | -8.8% |
| Monza win | 24.6% | 26.4% | 3.64 | -10.5% |
| Over 2.5 | 58.8% | 44.2% | 2.11 | +24.2% |
| Under 2.5 | 41.2% | 55.8% | 1.85 | -23.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9350 |
| Dc lambda away | 1.1718 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.43 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 55.1% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 22.8% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.1% |
| P home draw | 75.4% |
| P draw away | 49.8% |
| P home away | 74.8% |
| Raw p home draw | 77.2% |
| Raw p draw away | 44.9% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.07 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +4.9% |
| Draw probability edge | -3.0% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +14.6% |
| Under 2.5 probability edge | -14.6% |
| Raw edge prob home | 0.0975 |
| Raw ev home | 0.1844 |
| Raw edge prob draw | -0.0609 |
| Raw ev draw | -0.1984 |
| Raw edge prob away | -0.0366 |
| Raw ev away | -0.1713 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.8%**. Expected goals are 1.10 for Cagliari and 1.17 for Bologna (2.28 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.4%; Double Chance 1X: 61.2%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.2% | 3.10 |
| Draw | 29.0% | 3.45 |
| Bologna win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.10 |
| Bologna expected goals | 1.17 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.4% |
| Under 1.5 | 33.6% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 0-1 | 12.43% |
| 3 | 1-0 | 10.69% |
| 4 | 0-0 | 10.47% |
| 5 | 1-2 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.2% | 30.4% | 3.35 | +7.9% |
| Draw | 29.0% | 29.4% | 3.13 | -9.2% |
| Bologna win | 38.8% | 40.2% | 2.52 | -2.3% |
| Over 2.5 | 39.6% | 42.7% | 2.24 | -11.2% |
| Under 2.5 | 60.4% | 57.3% | 1.76 | +6.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1042 |
| Dc lambda away | 1.1710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.55 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.11 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.40 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 46.2% |
| P home draw | 61.2% |
| P draw away | 67.8% |
| P home away | 71.0% |
| Raw p home draw | 62.7% |
| Raw p draw away | 66.0% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.66 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | 0.0358 |
| Raw ev home | 0.1394 |
| Raw edge prob draw | -0.0071 |
| Raw ev draw | -0.1029 |
| Raw edge prob away | -0.0287 |
| Raw ev away | -0.0594 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **66.1%**. Expected goals are 2.06 for Como and 0.92 for Sassuolo (2.98 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.9%; Double Chance 1X: 85.6%; Double Chance X2: 33.9%; Double Chance 12 (either team wins): 80.6%; Under 4.5 goals: 81.6%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 66.1% | 1.51 |
| Draw | 19.4% | 5.15 |
| Sassuolo win | 14.4% | 6.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.06 |
| Sassuolo expected goals | 0.92 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.4% |
| Under 4.5 | 81.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.20% |
| 2 | 1-0 | 10.80% |
| 3 | 2-1 | 10.26% |
| 4 | 1-1 | 9.19% |
| 5 | 3-0 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 66.1% | 68.4% | 1.49 | -1.5% |
| Draw | 19.4% | 18.5% | 4.94 | -4.0% |
| Sassuolo win | 14.4% | 13.2% | 7.10 | +2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0647 |
| Dc lambda away | 0.9157 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.47 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.02 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.43 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 52.4% |
| P home draw | 85.6% |
| P draw away | 33.9% |
| P home away | 80.6% |
| Raw p home draw | 84.3% |
| Raw p draw away | 36.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.25 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.72 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0448 |
| Raw ev home | -0.0481 |
| Raw edge prob draw | 0.0191 |
| Raw ev draw | 0.0068 |
| Raw edge prob away | 0.0257 |
| Raw ev away | 0.1169 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **58.2%**. Expected goals are 1.37 for Lazio and 0.66 for Parma (2.03 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 88.1%; Over 2.5 goals: 34.2%; Under 3.5 goals: 84.8%; Double Chance 1X: 83.6%; Double Chance X2: 41.8%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 94.2%; BTTS Yes (both teams score): 35.4%; BTTS No (at least one team does not score): 64.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 58.2% | 1.72 |
| Draw | 25.4% | 3.94 |
| Parma win | 16.4% | 6.08 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.37 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.03 |
| Over 0.5 | 88.1% |
| Under 0.5 | 11.9% |
| Over 1.5 | 60.9% |
| Under 1.5 | 39.1% |
| Over 2.5 | 34.2% |
| Under 2.5 | 65.8% |
| Over 3.5 | 15.2% |
| Under 3.5 | 84.8% |
| Over 4.5 | 5.8% |
| Under 4.5 | 94.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.30% |
| 2 | 2-0 | 13.29% |
| 3 | 0-0 | 11.93% |
| 4 | 1-1 | 10.78% |
| 5 | 2-1 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 58.2% | 62.2% | 1.58 | -8.1% |
| Draw | 25.4% | 22.7% | 4.33 | +9.9% |
| Parma win | 16.4% | 15.1% | 6.64 | +9.2% |
| Over 2.5 | 34.2% | 49.3% | 2.06 | -29.6% |
| Under 2.5 | 65.8% | 50.7% | 1.89 | +24.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3728 |
| Dc lambda away | 0.6578 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 35.4% |
| P btts no | 64.6% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.38 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 2.93 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.59 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.33 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 54.1% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 36.0% |
| P home draw | 83.6% |
| P draw away | 41.8% |
| P home away | 74.6% |
| Raw p home draw | 82.2% |
| Raw p draw away | 45.9% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 3.85 |
| Reference away odds | 5.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | -4.0% |
| Draw probability edge | +2.7% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -15.2% |
| Under 2.5 probability edge | +15.2% |
| Raw edge prob home | -0.0809 |
| Raw ev home | -0.1449 |
| Raw edge prob draw | 0.0533 |
| Raw ev draw | 0.2148 |
| Raw edge prob away | 0.0277 |
| Raw ev away | 0.1834 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **40.1%**. Expected goals are 0.98 for Napoli and 1.19 for AS Roma (2.16 combined). The most likely exact score is 0-1 at 13.4%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 37.0%; Under 3.5 goals: 82.6%; Double Chance 1X: 59.9%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 93.1%; BTTS Yes (both teams score): 43.2%; BTTS No (at least one team does not score): 56.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 31.5% | 3.18 |
| Draw | 28.4% | 3.52 |
| AS Roma win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 0.98 |
| AS Roma expected goals | 1.19 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 63.7% |
| Under 1.5 | 36.3% |
| Over 2.5 | 37.0% |
| Under 2.5 | 63.0% |
| Over 3.5 | 17.4% |
| Under 3.5 | 82.6% |
| Over 4.5 | 6.9% |
| Under 4.5 | 93.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.41% |
| 2 | 1-1 | 12.97% |
| 3 | 1-0 | 11.68% |
| 4 | 0-0 | 11.19% |
| 5 | 0-2 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 31.5% | 32.8% | 3.04 | -4.4% |
| Draw | 28.4% | 27.5% | 3.60 | +2.3% |
| AS Roma win | 40.1% | 39.7% | 2.45 | -1.7% |
| Over 2.5 | 37.0% | 51.5% | 1.93 | -28.6% |
| Under 2.5 | 63.0% | 48.5% | 2.01 | +26.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9781 |
| Dc lambda away | 1.1857 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 43.2% |
| P btts no | 56.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.94 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.76 |
| Fair Over 2.5 odds | 2.70 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.76 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.45 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 40.6% |
| Raw p over 1 5 | 63.7% |
| Raw p under 3 5 | 82.6% |
| Raw p btts yes | 43.4% |
| P home draw | 59.9% |
| P draw away | 68.5% |
| P home away | 71.6% |
| Raw p home draw | 59.4% |
| Raw p draw away | 69.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -14.4% |
| Under 2.5 probability edge | +14.4% |
| Raw edge prob home | -0.0275 |
| Raw ev home | -0.0856 |
| Raw edge prob draw | 0.0186 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | 0.0090 |
| Raw ev away | -0.0058 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **54.5%**. Expected goals are 1.77 for Atalanta BC and 1.27 for Frosinone (3.04 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 59.1%; Under 3.5 goals: 63.4%; Double Chance 1X: 76.9%; Double Chance X2: 45.5%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 80.5%; BTTS Yes (both teams score): 59.4%; BTTS No (at least one team does not score): 40.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 54.5% | 1.83 |
| Draw | 22.4% | 4.47 |
| Frosinone win | 23.1% | 4.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.77 |
| Frosinone expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.5% |
| Under 4.5 | 80.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.55% |
| 2 | 1-1 | 10.32% |
| 3 | 1-0 | 9.31% |
| 4 | 2-0 | 8.31% |
| 5 | 3-1 | 6.24% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 54.5% | 59.8% | 1.72 | -6.2% |
| Draw | 22.4% | 21.4% | 4.37 | -2.2% |
| Frosinone win | 23.1% | 18.8% | 4.88 | +12.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7745 |
| Dc lambda away | 1.2688 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.4% |
| P btts no | 40.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.69 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.27 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.13 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 63.8% |
| Raw p btts yes | 59.7% |
| P home draw | 76.9% |
| P draw away | 45.5% |
| P home away | 77.6% |
| Raw p home draw | 72.6% |
| Raw p draw away | 50.8% |
| Raw p home away | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Home probability edge | -5.3% |
| Draw probability edge | +1.0% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.1056 |
| Raw ev home | -0.1530 |
| Raw edge prob draw | 0.0203 |
| Raw ev draw | 0.0223 |
| Raw edge prob away | 0.0853 |
| Raw ev away | 0.3353 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **48.5%**. Expected goals are 1.55 for Genoa and 0.90 for Venezia (2.45 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.0%; Under 3.5 goals: 77.1%; Double Chance 1X: 74.9%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 89.9%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 48.5% | 2.06 |
| Draw | 26.3% | 3.80 |
| Venezia win | 25.1% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.55 |
| Venezia expected goals | 0.90 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 22.9% |
| Under 3.5 | 77.1% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 1-0 | 12.30% |
| 3 | 2-0 | 9.57% |
| 4 | 0-0 | 8.87% |
| 5 | 0-1 | 8.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 48.5% | 44.7% | 2.14 | +3.9% |
| Draw | 26.3% | 27.0% | 3.44 | -9.4% |
| Venezia win | 25.1% | 28.3% | 3.87 | -2.7% |
| Over 2.5 | 44.0% | 51.5% | 1.97 | -13.4% |
| Under 2.5 | 56.0% | 48.5% | 1.98 | +10.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5486 |
| Dc lambda away | 0.9041 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.27 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.36 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.91 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.4% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 21.9% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 46.9% |
| P home draw | 74.9% |
| P draw away | 51.5% |
| P home away | 73.7% |
| Raw p home draw | 78.1% |
| Raw p draw away | 47.6% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.6% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | 0.0763 |
| Raw ev home | 0.1204 |
| Raw edge prob draw | -0.0124 |
| Raw ev draw | -0.1157 |
| Raw edge prob away | -0.0638 |
| Raw ev away | -0.1509 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **73.0%**. Expected goals are 2.81 for Inter Milan and 0.94 for Fiorentina (3.75 combined). The most likely exact score is 2-0 at 8.9%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 71.5%; Under 3.5 goals: 48.9%; Double Chance 1X: 88.8%; Double Chance X2: 27.0%; Double Chance 12 (either team wins): 84.1%; Under 4.5 goals: 68.4%; BTTS Yes (both teams score): 58.1%; BTTS No (at least one team does not score): 41.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.0% | 1.37 |
| Draw | 15.9% | 6.31 |
| Fiorentina win | 11.2% | 8.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.81 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.75 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.5% |
| Under 2.5 | 28.5% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.6% |
| Under 4.5 | 68.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 8.89% |
| 2 | 2-1 | 8.38% |
| 3 | 3-0 | 8.33% |
| 4 | 3-1 | 7.85% |
| 5 | 1-1 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.0% | 69.9% | 1.41 | +2.9% |
| Draw | 15.9% | 17.5% | 5.56 | -11.9% |
| Fiorentina win | 11.2% | 12.5% | 7.90 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8098 |
| Dc lambda away | 0.9425 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 58.1% |
| P btts no | 41.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.61 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.74 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.51 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 76.0% |
| Unadjusted draw probability | 14.2% |
| Unadjusted away-win probability | 9.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 57.4% |
| P home draw | 88.8% |
| P draw away | 27.0% |
| P home away | 84.1% |
| Raw p home draw | 90.2% |
| Raw p draw away | 24.0% |
| Raw p home away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.78 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Home probability edge | +3.0% |
| Draw probability edge | -1.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.0607 |
| Raw ev home | 0.0718 |
| Raw edge prob draw | -0.0337 |
| Raw ev draw | -0.2123 |
| Raw edge prob away | -0.0270 |
| Raw ev away | -0.2242 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **65.7%**. Expected goals are 0.61 for Lecce and 1.64 for Juventus (2.24 combined). The most likely exact score is 0-1 at 18.2%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 39.8%; Under 3.5 goals: 80.7%; Double Chance 1X: 34.3%; Double Chance X2: 88.0%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 12.0% | 8.30 |
| Draw | 22.3% | 4.49 |
| Juventus win | 65.7% | 1.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.61 |
| Juventus expected goals | 1.64 |
| Expected total goals | 2.24 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.8% |
| Under 2.5 | 60.2% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.21% |
| 2 | 0-2 | 14.97% |
| 3 | 0-0 | 9.83% |
| 4 | 1-1 | 9.75% |
| 5 | 1-2 | 9.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 12.0% | 10.7% | 7.70 | -7.3% |
| Draw | 22.3% | 20.4% | 4.53 | +0.8% |
| Juventus win | 65.7% | 68.9% | 1.50 | -1.5% |
| Over 2.5 | 39.8% | 50.0% | 1.92 | -23.7% |
| Under 2.5 | 60.2% | 50.0% | 2.02 | +21.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6051 |
| Dc lambda away | 1.6392 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.18 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.51 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.54 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 13.4% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 62.5% |
| Raw p over 1 5 | 65.7% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 36.6% |
| P home draw | 34.3% |
| P draw away | 88.0% |
| P home away | 77.7% |
| Raw p home draw | 37.5% |
| Raw p draw away | 86.6% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 7.50 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.40 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -10.2% |
| Under 2.5 probability edge | +10.2% |
| Raw edge prob home | 0.0263 |
| Raw ev home | 0.0288 |
| Raw edge prob draw | 0.0374 |
| Raw ev draw | 0.0931 |
| Raw edge prob away | -0.0637 |
| Raw ev away | -0.0624 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.2%**. Expected goals are 1.04 for Udinese and 1.56 for AC Milan (2.61 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.3%; Double Chance 1X: 48.8%; Double Chance X2: 76.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 23.4% | 4.28 |
| Draw | 25.5% | 3.93 |
| AC Milan win | 51.2% | 1.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.56 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.11% |
| 2 | 0-1 | 11.89% |
| 3 | 1-2 | 9.76% |
| 4 | 0-2 | 9.35% |
| 5 | 0-0 | 7.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 23.4% | 21.5% | 4.68 | +9.3% |
| Draw | 25.5% | 25.5% | 3.91 | -0.4% |
| AC Milan win | 51.2% | 53.0% | 1.83 | -6.3% |
| Over 2.5 | 48.4% | 50.0% | 1.97 | -4.6% |
| Under 2.5 | 51.6% | 50.0% | 1.97 | +1.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:33Z |
| Market best draw last update utc | 2026-10-18T14:34:33Z |
| Market best away last update utc | 2026-10-18T14:34:33Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0438 |
| Dc lambda away | 1.5649 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:33.287337+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.45 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.05 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 25.2% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 49.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.3% |
| P home draw | 48.8% |
| P draw away | 76.6% |
| P home away | 74.5% |
| Raw p home draw | 50.7% |
| Raw p draw away | 74.8% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.79 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:34Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Home probability edge | +1.9% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0377 |
| Raw ev home | 0.1815 |
| Raw edge prob draw | -0.0011 |
| Raw ev draw | -0.0066 |
| Raw edge prob away | -0.0366 |
| Raw ev away | -0.0969 |

</details>


---
