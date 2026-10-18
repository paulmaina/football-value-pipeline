# Serie A — football model report

Fixtures in this report: **15**.

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
| Training as of utc | 2026-10-18T11:57:35.915018+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 64, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 64, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:57:35.915018+00:00', 'observations': 78, 'observations_sha256': '3c0ed3e5b79d831ea5dfbc093ace97a9135205fbd11f3cbbe901038e53ac324d', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 40, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '0b92d19a30ce70e2b0ea5653218420f57abfaaff0806535c02e4e649ff5b9044', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 845.504 |
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
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 11.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261018T115735915018Z_d8646df411172b6fb6f4045668b64bb00e5dbe0c00ba1013af9be905e331c012.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

The model's most likely 1X2 outcome is **AC Milan win** at **48.2%**. Expected goals are 1.30 for AC Milan and 1.15 for Atalanta BC (2.45 combined). The most likely exact score is 1-0 at 13.5%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.6%; Double Chance 1X: 73.2%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.1%; BTTS No (at least one team does not score): 50.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 48.2% | 2.08 |
| Draw | 25.0% | 4.01 |
| Atalanta BC win | 26.8% | 3.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.30 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.45 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.47% |
| 2 | 1-1 | 11.83% |
| 3 | 2-1 | 10.11% |
| 4 | 2-0 | 8.81% |
| 5 | 0-1 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 48.2% | 56.4% | 1.80 | -13.3% |
| Draw | 25.0% | 22.6% | 4.07 | +1.6% |
| Atalanta BC win | 26.8% | 21.0% | 4.67 | +25.4% |
| Over 2.5 | 45.2% | 58.4% | 1.75 | -21.0% |
| Under 2.5 | 54.8% | 41.6% | 2.25 | +23.4% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.1% |
| P btts no | 50.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.59 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.53 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 40.0% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 49.7% |
| P home draw | 73.2% |
| P draw away | 51.8% |
| P home away | 75.0% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.0% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.68 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -8.2% |
| Draw probability edge | +2.4% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | -0.1639 |
| Raw ev home | -0.2801 |
| Raw edge prob draw | 0.0480 |
| Raw ev draw | 0.1137 |
| Raw edge prob away | 0.1159 |
| Raw ev away | 0.5244 |
| Market p home draw | 79.2% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:30Z |
| Market reference home draw last update utc | 2026-10-18T11:57:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.4% |
| Market draw away odds | 2.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:30Z |
| Market reference draw away last update utc | 2026-10-18T11:57:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.5% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:30Z |
| Market reference home away last update utc | 2026-10-18T11:57:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.13 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 81.5% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:11Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.8% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:29Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:30Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-18T11:57:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.9%**. Expected goals are 0.96 for Fiorentina and 1.69 for Como (2.64 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.9%; Under 3.5 goals: 72.9%; Double Chance 1X: 49.1%; Double Chance X2: 75.6%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.4% | 4.09 |
| Draw | 24.6% | 4.06 |
| Como win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.69 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.72% |
| 2 | 0-1 | 11.15% |
| 3 | 0-2 | 9.45% |
| 4 | 1-2 | 9.05% |
| 5 | 1-0 | 7.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.4% | 27.6% | 3.54 | -13.5% |
| Draw | 24.6% | 25.0% | 3.81 | -6.1% |
| Como win | 50.9% | 47.4% | 2.12 | +8.0% |
| Over 2.5 | 48.9% | 59.5% | 1.73 | -15.4% |
| Under 2.5 | 51.1% | 40.5% | 2.29 | +17.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9576 |
| Dc lambda away | 1.6873 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.75 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.04 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.70 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.86 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 54.5% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 50.3% |
| P home draw | 49.1% |
| P draw away | 75.6% |
| P home away | 75.4% |
| Raw p home draw | 45.5% |
| Raw p draw away | 78.7% |
| Raw p home away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.25 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.98 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -3.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.0629 |
| Raw ev home | -0.2465 |
| Raw edge prob draw | -0.0079 |
| Raw ev draw | -0.0763 |
| Raw edge prob away | 0.0708 |
| Raw ev away | 0.1548 |
| Market p home draw | 53.7% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:30Z |
| Market reference home draw last update utc | 2026-10-18T11:57:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.3% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:30Z |
| Market reference draw away last update utc | 2026-10-18T11:57:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.0% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:30Z |
| Market reference home away last update utc | 2026-10-18T11:57:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home draw odds | 1.79 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:56:54Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:11Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.4% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:56:54Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.52 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:29Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.1% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:30Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-18T11:57:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **55.8%**. Expected goals are 1.37 for Juventus and 0.86 for Lazio (2.23 combined). The most likely exact score is 1-0 at 16.8%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.9%; Double Chance 1X: 81.0%; Double Chance X2: 44.2%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.3%; BTTS No (at least one team does not score): 57.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 55.8% | 1.79 |
| Draw | 25.2% | 3.97 |
| Lazio win | 19.0% | 5.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.86 |
| Expected total goals | 2.23 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
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
| 1 | 1-0 | 16.81% |
| 2 | 2-0 | 11.56% |
| 3 | 1-1 | 11.52% |
| 4 | 2-1 | 9.95% |
| 5 | 0-0 | 9.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 55.8% | 62.9% | 1.61 | -10.1% |
| Draw | 25.2% | 22.5% | 4.27 | +7.5% |
| Lazio win | 19.0% | 14.5% | 6.30 | +19.9% |
| Over 2.5 | 39.7% | 51.4% | 1.96 | -22.3% |
| Under 2.5 | 60.3% | 48.6% | 1.98 | +19.5% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda home | 1.3694 |
| Dc lambda away | 0.8603 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.3% |
| P btts no | 57.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.22 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.24 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.65 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.1% |
| P home draw | 81.0% |
| P draw away | 44.2% |
| P home away | 74.8% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.3% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.55 |
| Reference draw odds | 4.10 |
| Reference away odds | 6.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -7.1% |
| Draw probability edge | +2.6% |
| Away probability edge | +4.5% |
| Over 2.5 probability edge | -11.8% |
| Under 2.5 probability edge | +11.8% |
| Raw edge prob home | -0.1425 |
| Raw ev home | -0.2162 |
| Raw edge prob draw | 0.0529 |
| Raw ev draw | 0.1875 |
| Raw edge prob away | 0.0896 |
| Raw ev away | 0.4808 |
| Market p home draw | 84.6% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:30Z |
| Market reference home draw last update utc | 2026-10-18T11:57:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 38.9% |
| Market draw away odds | 2.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:30Z |
| Market reference draw away last update utc | 2026-10-18T11:57:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:30Z |
| Market reference home away last update utc | 2026-10-18T11:57:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.48 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 76.8% |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:29Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.5% |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:29Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 48.8% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:30Z |
| Market reference btts yes odds | 1.90 |
| Market reference btts yes opposite odds | 1.82 |
| Market reference btts yes last update utc | 2026-10-18T11:57:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.7%**. Expected goals are 1.14 for Monza and 1.60 for Cagliari (2.74 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.7%; Under 3.5 goals: 71.1%; Double Chance 1X: 60.3%; Double Chance X2: 66.4%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.6% | 2.98 |
| Draw | 26.7% | 3.74 |
| Cagliari win | 39.7% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.14 |
| Cagliari expected goals | 1.60 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.7% |
| Under 2.5 | 49.3% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.69% |
| 2 | 1-0 | 9.10% |
| 3 | 0-1 | 8.51% |
| 4 | 2-1 | 8.34% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.6% | 40.2% | 2.49 | -16.3% |
| Draw | 26.7% | 28.5% | 3.25 | -13.1% |
| Cagliari win | 39.7% | 31.2% | 3.25 | +28.9% |
| Over 2.5 | 50.7% | 45.5% | 2.15 | +8.9% |
| Under 2.5 | 49.3% | 54.5% | 1.82 | -10.2% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda away | 1.6008 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.27 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.22 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 27.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 48.1% |
| Raw p over 1 5 | 75.9% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.3% |
| P home draw | 60.3% |
| P draw away | 66.4% |
| P home away | 73.3% |
| Raw p home draw | 51.9% |
| Raw p draw away | 73.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -6.6% |
| Draw probability edge | -1.8% |
| Away probability edge | +8.4% |
| Over 2.5 probability edge | +5.1% |
| Under 2.5 probability edge | -5.1% |
| Raw edge prob home | -0.1326 |
| Raw ev home | -0.3283 |
| Raw edge prob draw | -0.0359 |
| Raw ev draw | -0.1893 |
| Raw edge prob away | 0.1685 |
| Raw ev away | 0.5626 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:30Z |
| Market reference home draw last update utc | 2026-10-18T11:57:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.5% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:30Z |
| Market reference draw away last update utc | 2026-10-18T11:57:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.7% |
| Market home away odds | 1.39 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:30Z |
| Market reference home away last update utc | 2026-10-18T11:57:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.59 |
| Market reference dc home draw odds | 1.38 |
| Market reference dc home away odds | 1.38 |
| Market p over 1 5 | 73.6% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:57:22Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:29Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.8% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:57:22Z |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.44 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.0% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:30Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.08 |
| Market reference btts yes last update utc | 2026-10-18T11:57:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.7%**. Expected goals are 1.01 for Parma and 1.10 for Torino (2.10 combined). The most likely exact score is 0-1 at 13.8%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.8%; Double Chance 1X: 61.3%; Double Chance X2: 68.7%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.3%; BTTS No (at least one team does not score): 57.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.3% | 3.19 |
| Draw | 30.0% | 3.33 |
| Torino win | 38.7% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.01 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.82% |
| 2 | 1-1 | 13.52% |
| 3 | 0-0 | 12.26% |
| 4 | 1-0 | 11.72% |
| 5 | 1-2 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.3% | 30.0% | 3.43 | +7.5% |
| Draw | 30.0% | 30.0% | 3.17 | -4.9% |
| Torino win | 38.7% | 40.1% | 2.45 | -5.2% |
| Over 2.5 | 35.1% | 38.8% | 2.49 | -12.5% |
| Under 2.5 | 64.9% | 61.2% | 1.63 | +5.7% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.3% |
| P btts no | 57.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.15 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.17 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.01 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.7% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 62.2% |
| Raw p under 3 5 | 83.8% |
| Raw p btts yes | 42.3% |
| P home draw | 61.3% |
| P draw away | 68.7% |
| P home away | 70.0% |
| Raw p home draw | 62.7% |
| Raw p draw away | 67.3% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.41 |
| Reference Under 2.5 odds | 1.58 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +1.4% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | 0.0275 |
| Raw ev home | 0.1218 |
| Raw edge prob draw | 0.0007 |
| Raw ev draw | -0.0482 |
| Raw edge prob away | -0.0282 |
| Raw ev away | -0.0869 |
| Market p home draw | 59.8% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:57:30Z |
| Market reference home draw last update utc | 2026-10-18T11:57:34Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.4% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:57:30Z |
| Market reference draw away last update utc | 2026-10-18T11:57:34Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.8% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:57:30Z |
| Market reference home away last update utc | 2026-10-18T11:57:34Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.35 |
| Market reference dc home draw odds | 1.61 |
| Market reference dc home away odds | 1.40 |
| Market p over 1 5 | 67.8% |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.89 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:29Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 81.1% |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:10Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.5% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:57:30Z |
| Market reference btts yes odds | 1.98 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-18T11:57:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.5%**. Expected goals are 1.94 for Torino and 1.17 for Monza (3.11 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.1%; Under 3.5 goals: 62.7%; Double Chance 1X: 74.8%; Double Chance X2: 49.5%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.5% | 1.98 |
| Draw | 24.3% | 4.11 |
| Monza win | 25.2% | 3.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.17 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.21% |
| 2 | 2-1 | 9.00% |
| 3 | 1-0 | 7.89% |
| 4 | 2-0 | 7.68% |
| 5 | 1-2 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.5% | 45.9% | 2.15 | +8.6% |
| Draw | 24.3% | 26.5% | 3.62 | -11.9% |
| Monza win | 25.2% | 27.5% | 3.64 | -8.4% |
| Over 2.5 | 59.1% | 46.5% | 2.11 | +24.7% |
| Under 2.5 | 40.9% | 53.5% | 1.85 | -24.4% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda home | 1.9351 |
| Dc lambda away | 1.1717 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.11 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.05 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.1% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 22.8% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.1% |
| P home draw | 74.8% |
| P draw away | 49.5% |
| P home away | 75.7% |
| Raw p home draw | 77.2% |
| Raw p draw away | 44.9% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.15 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +4.6% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.4% |
| Over 2.5 probability edge | +12.6% |
| Under 2.5 probability edge | -12.6% |
| Raw edge prob home | 0.0917 |
| Raw ev home | 0.1845 |
| Raw edge prob draw | -0.0439 |
| Raw ev draw | -0.1984 |
| Raw edge prob away | -0.0478 |
| Raw ev away | -0.1714 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.8%**. Expected goals are 1.10 for Cagliari and 1.17 for Bologna (2.28 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.4%; Double Chance 1X: 61.2%; Double Chance X2: 67.4%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 46.2%; BTTS No (at least one team does not score): 53.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 32.6% | 3.07 |
| Draw | 28.7% | 3.49 |
| Bologna win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.10 |
| Bologna expected goals | 1.17 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 66.4% |
| Under 1.5 | 33.6% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.36% |
| 2 | 0-1 | 12.44% |
| 3 | 1-0 | 10.80% |
| 4 | 0-0 | 10.34% |
| 5 | 1-2 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 32.6% | 31.1% | 3.35 | +9.1% |
| Draw | 28.7% | 28.7% | 3.13 | -10.3% |
| Bologna win | 38.8% | 40.2% | 2.52 | -2.3% |
| Over 2.5 | 39.7% | 43.5% | 2.24 | -11.0% |
| Under 2.5 | 60.3% | 56.5% | 1.76 | +6.0% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.2% |
| P btts no | 53.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.67 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.11 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.36 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 46.2% |
| P home draw | 61.2% |
| P draw away | 67.4% |
| P home away | 71.3% |
| Raw p home draw | 62.7% |
| Raw p draw away | 66.0% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.75 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.0% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -3.7% |
| Under 2.5 probability edge | +3.7% |
| Raw edge prob home | 0.0292 |
| Raw ev home | 0.1394 |
| Raw edge prob draw | -0.0001 |
| Raw ev draw | -0.1029 |
| Raw edge prob away | -0.0291 |
| Raw ev away | -0.0594 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **66.5%**. Expected goals are 2.06 for Como and 0.92 for Sassuolo (2.98 combined). The most likely exact score is 2-0 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 58.0%; Under 3.5 goals: 64.8%; Double Chance 1X: 85.2%; Double Chance X2: 33.5%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 66.5% | 1.50 |
| Draw | 18.7% | 5.36 |
| Sassuolo win | 14.8% | 6.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.06 |
| Sassuolo expected goals | 0.92 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 80.1% |
| Under 1.5 | 19.9% |
| Over 2.5 | 58.0% |
| Under 2.5 | 42.0% |
| Over 3.5 | 35.2% |
| Under 3.5 | 64.8% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.27% |
| 2 | 1-0 | 10.87% |
| 3 | 2-1 | 10.32% |
| 4 | 1-1 | 8.83% |
| 5 | 3-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 66.5% | 69.2% | 1.49 | -0.9% |
| Draw | 18.7% | 16.9% | 4.94 | -7.8% |
| Sassuolo win | 14.8% | 13.9% | 7.10 | +5.1% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0646 |
| Dc lambda away | 0.9157 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.31 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.03 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.84 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.40 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 52.4% |
| P home draw | 85.2% |
| P draw away | 33.5% |
| P home away | 81.3% |
| Raw p home draw | 84.3% |
| Raw p draw away | 36.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.36 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Home probability edge | -2.6% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -8.5% |
| Under 2.5 probability edge | +8.5% |
| Raw edge prob home | -0.0530 |
| Raw ev home | -0.0481 |
| Raw edge prob draw | 0.0344 |
| Raw ev draw | 0.0069 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.1170 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **59.5%**. Expected goals are 1.37 for Lazio and 0.66 for Parma (2.03 combined). The most likely exact score is 1-0 at 19.8%. Goal-market probabilities: at least one goal: 88.5%; Over 2.5 goals: 34.5%; Under 3.5 goals: 84.7%; Double Chance 1X: 84.0%; Double Chance X2: 40.5%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 94.2%; BTTS Yes (both teams score): 35.1%; BTTS No (at least one team does not score): 64.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 59.5% | 1.68 |
| Draw | 24.5% | 4.09 |
| Parma win | 16.0% | 6.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.37 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.03 |
| Over 0.5 | 88.5% |
| Under 0.5 | 11.5% |
| Over 1.5 | 61.0% |
| Under 1.5 | 39.0% |
| Over 2.5 | 34.5% |
| Under 2.5 | 65.5% |
| Over 3.5 | 15.3% |
| Under 3.5 | 84.7% |
| Over 4.5 | 5.8% |
| Under 4.5 | 94.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.75% |
| 2 | 2-0 | 13.60% |
| 3 | 0-0 | 11.50% |
| 4 | 1-1 | 10.39% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 59.5% | 64.9% | 1.58 | -6.0% |
| Draw | 24.5% | 20.9% | 4.33 | +6.0% |
| Parma win | 16.0% | 14.2% | 6.64 | +6.3% |
| Over 2.5 | 34.5% | 47.8% | 2.06 | -28.9% |
| Under 2.5 | 65.5% | 52.2% | 1.89 | +23.8% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 35.1% |
| P btts no | 64.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.70 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.90 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.55 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.10 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 54.1% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 36.0% |
| P home draw | 84.0% |
| P draw away | 40.5% |
| P home away | 75.5% |
| Raw p home draw | 82.2% |
| Raw p draw away | 45.9% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.44 |
| Reference draw odds | 3.75 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -5.4% |
| Draw probability edge | +3.6% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -13.2% |
| Under 2.5 probability edge | +13.2% |
| Raw edge prob home | -0.1080 |
| Raw ev home | -0.1448 |
| Raw edge prob draw | 0.0716 |
| Raw ev draw | 0.2148 |
| Raw edge prob away | 0.0364 |
| Raw ev away | 0.1833 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **40.8%**. Expected goals are 0.98 for Napoli and 1.19 for AS Roma (2.16 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 37.1%; Under 3.5 goals: 82.6%; Double Chance 1X: 59.2%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 93.1%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 31.1% | 3.21 |
| Draw | 28.1% | 3.56 |
| AS Roma win | 40.8% | 2.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 0.98 |
| AS Roma expected goals | 1.19 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 63.8% |
| Under 1.5 | 36.2% |
| Over 2.5 | 37.1% |
| Under 2.5 | 62.9% |
| Over 3.5 | 17.4% |
| Under 3.5 | 82.6% |
| Over 4.5 | 6.9% |
| Under 4.5 | 93.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.63% |
| 2 | 1-1 | 12.81% |
| 3 | 1-0 | 11.56% |
| 4 | 0-0 | 11.05% |
| 5 | 0-2 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 31.1% | 32.2% | 3.04 | -5.4% |
| Draw | 28.1% | 26.8% | 3.60 | +1.1% |
| AS Roma win | 40.8% | 41.0% | 2.45 | -0.0% |
| Over 2.5 | 37.1% | 51.0% | 1.93 | -28.3% |
| Under 2.5 | 62.9% | 49.0% | 2.01 | +26.4% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda away | 1.1856 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.05 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.76 |
| Fair Over 2.5 odds | 2.69 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.75 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.39 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 40.6% |
| Raw p over 1 5 | 63.7% |
| Raw p under 3 5 | 82.6% |
| Raw p btts yes | 43.4% |
| P home draw | 59.2% |
| P draw away | 68.9% |
| P home away | 71.9% |
| Raw p home draw | 59.4% |
| Raw p draw away | 69.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | -1.0% |
| Draw probability edge | +1.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -13.9% |
| Under 2.5 probability edge | +13.9% |
| Raw edge prob home | -0.0209 |
| Raw ev home | -0.0856 |
| Raw edge prob draw | 0.0254 |
| Raw ev draw | 0.0564 |
| Raw edge prob away | -0.0045 |
| Raw ev away | -0.0058 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **54.3%**. Expected goals are 1.77 for Atalanta BC and 1.27 for Frosinone (3.04 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 59.3%; Under 3.5 goals: 63.4%; Double Chance 1X: 76.2%; Double Chance X2: 45.7%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 54.3% | 1.84 |
| Draw | 21.8% | 4.58 |
| Frosinone win | 23.8% | 4.20 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.77 |
| Frosinone expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.51% |
| 2 | 1-1 | 10.07% |
| 3 | 1-0 | 9.27% |
| 4 | 2-0 | 8.28% |
| 5 | 3-1 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 54.3% | 59.4% | 1.72 | -6.6% |
| Draw | 21.8% | 20.3% | 4.37 | -4.5% |
| Frosinone win | 23.8% | 20.3% | 4.88 | +16.3% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7744 |
| Dc lambda away | 1.2690 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.22 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.74 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.11 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 63.8% |
| Raw p btts yes | 59.8% |
| P home draw | 76.2% |
| P draw away | 45.7% |
| P home away | 78.2% |
| Raw p home draw | 72.6% |
| Raw p draw away | 50.8% |
| Raw p home away | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Home probability edge | -5.1% |
| Draw probability edge | +1.5% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | -0.1016 |
| Raw ev home | -0.1531 |
| Raw edge prob draw | 0.0309 |
| Raw ev draw | 0.0223 |
| Raw edge prob away | 0.0706 |
| Raw ev away | 0.3355 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **49.7%**. Expected goals are 1.55 for Genoa and 0.90 for Venezia (2.45 combined). The most likely exact score is 1-0 at 12.6%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.2%; Under 3.5 goals: 77.0%; Double Chance 1X: 75.5%; Double Chance X2: 50.3%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 49.7% | 2.01 |
| Draw | 25.9% | 3.87 |
| Venezia win | 24.5% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.55 |
| Venezia expected goals | 0.90 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.59% |
| 2 | 1-1 | 12.18% |
| 3 | 2-0 | 9.79% |
| 4 | 2-1 | 8.85% |
| 5 | 0-0 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 49.7% | 47.0% | 2.14 | +6.3% |
| Draw | 25.9% | 26.0% | 3.44 | -11.0% |
| Venezia win | 24.5% | 27.0% | 3.87 | -5.3% |
| Over 2.5 | 44.2% | 50.1% | 1.97 | -12.9% |
| Under 2.5 | 55.8% | 49.9% | 1.98 | +10.5% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
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
| Dc lambda away | 0.9042 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.47 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.34 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.84 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.4% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 21.9% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 46.9% |
| P home draw | 75.5% |
| P draw away | 50.3% |
| P home away | 74.1% |
| Raw p home draw | 78.1% |
| Raw p draw away | 47.6% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.20 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +2.7% |
| Draw probability edge | -0.2% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0536 |
| Raw ev home | 0.1203 |
| Raw edge prob draw | -0.0031 |
| Raw ev draw | -0.1157 |
| Raw edge prob away | -0.0505 |
| Raw ev away | -0.1509 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **74.0%**. Expected goals are 2.81 for Inter Milan and 0.94 for Fiorentina (3.75 combined). The most likely exact score is 2-0 at 9.0%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 71.9%; Under 3.5 goals: 48.7%; Double Chance 1X: 88.8%; Double Chance X2: 26.0%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 74.0% | 1.35 |
| Draw | 14.7% | 6.79 |
| Fiorentina win | 11.2% | 8.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.81 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.75 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.6% |
| Under 1.5 | 11.4% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.02% |
| 2 | 2-1 | 8.50% |
| 3 | 3-0 | 8.45% |
| 4 | 3-1 | 7.96% |
| 5 | 1-1 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 74.0% | 72.1% | 1.41 | +4.4% |
| Draw | 14.7% | 15.3% | 5.56 | -18.1% |
| Fiorentina win | 11.2% | 12.6% | 7.90 | -11.3% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8099 |
| Dc lambda away | 0.9426 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.47 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.81 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 76.0% |
| Unadjusted draw probability | 14.2% |
| Unadjusted away-win probability | 9.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 57.4% |
| P home draw | 88.8% |
| P draw away | 26.0% |
| P home away | 85.3% |
| Raw p home draw | 90.2% |
| Raw p draw away | 24.0% |
| Raw p home away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.31 |
| Reference draw odds | 4.70 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +5.4% |
| Under 2.5 probability edge | -5.4% |
| Raw edge prob home | 0.0395 |
| Raw ev home | 0.0718 |
| Raw edge prob draw | -0.0113 |
| Raw ev draw | -0.2123 |
| Raw edge prob away | -0.0282 |
| Raw ev away | -0.2242 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **66.6%**. Expected goals are 0.61 for Lecce and 1.64 for Juventus (2.24 combined). The most likely exact score is 0-1 at 18.5%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.6%; Double Chance 1X: 33.4%; Double Chance X2: 87.7%; Double Chance 12 (either team wins): 78.9%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 35.8%; BTTS No (at least one team does not score): 64.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 12.3% | 8.10 |
| Draw | 21.1% | 4.75 |
| Juventus win | 66.6% | 1.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.61 |
| Juventus expected goals | 1.64 |
| Expected total goals | 2.24 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 66.4% |
| Under 1.5 | 33.6% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.4% |
| Under 3.5 | 80.6% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.46% |
| 2 | 0-2 | 15.17% |
| 3 | 0-0 | 9.30% |
| 4 | 1-1 | 9.22% |
| 5 | 1-2 | 9.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 12.3% | 11.3% | 7.70 | -5.0% |
| Draw | 21.1% | 18.0% | 4.53 | -4.6% |
| Juventus win | 66.6% | 70.7% | 1.50 | -0.1% |
| Over 2.5 | 40.2% | 51.3% | 1.92 | -22.9% |
| Under 2.5 | 59.8% | 48.7% | 2.02 | +20.8% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda away | 1.6390 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.8% |
| P btts no | 64.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.76 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.97 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.15 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.39 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 13.4% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 62.5% |
| Raw p over 1 5 | 65.7% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 36.6% |
| P home draw | 33.4% |
| P draw away | 87.7% |
| P home away | 78.9% |
| Raw p home draw | 37.5% |
| Raw p draw away | 86.6% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 6.00 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.33 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +1.0% |
| Draw probability edge | +3.1% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -11.1% |
| Under 2.5 probability edge | +11.1% |
| Raw edge prob home | 0.0204 |
| Raw ev home | 0.0290 |
| Raw edge prob draw | 0.0615 |
| Raw ev draw | 0.0932 |
| Raw edge prob away | -0.0819 |
| Raw ev away | -0.0625 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **51.7%**. Expected goals are 1.04 for Udinese and 1.56 for AC Milan (2.61 combined). The most likely exact score is 0-1 at 12.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.6%; Under 3.5 goals: 73.3%; Double Chance 1X: 48.3%; Double Chance X2: 76.6%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 23.4% | 4.28 |
| Draw | 25.0% | 4.01 |
| AC Milan win | 51.7% | 1.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.56 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 73.6% |
| Under 1.5 | 26.4% |
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
| Over 3.5 | 26.7% |
| Under 3.5 | 73.3% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.00% |
| 2 | 1-1 | 11.88% |
| 3 | 1-2 | 9.85% |
| 4 | 0-2 | 9.44% |
| 5 | 0-0 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 23.4% | 21.5% | 4.68 | +9.4% |
| Draw | 25.0% | 24.5% | 3.91 | -2.4% |
| AC Milan win | 51.7% | 54.0% | 1.83 | -5.5% |
| Over 2.5 | 48.6% | 50.0% | 1.97 | -4.2% |
| Under 2.5 | 51.4% | 50.0% | 1.97 | +1.2% |

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
| Market best home last update utc | 2026-10-18T11:57:30Z |
| Market best draw last update utc | 2026-10-18T11:57:30Z |
| Market best away last update utc | 2026-10-18T11:57:30Z |
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
| Dc lambda home | 1.0439 |
| Dc lambda away | 1.5648 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:35.915018+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.71 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.79 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.01 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 25.3% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 49.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.3% |
| P home draw | 48.3% |
| P draw away | 76.6% |
| P home away | 75.0% |
| Raw p home draw | 50.7% |
| Raw p draw away | 74.7% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.75 |
| Reference draw odds | 3.35 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:34Z |
| Market reference home last update utc | 2026-10-18T11:57:34Z |
| Market reference draw last update utc | 2026-10-18T11:57:34Z |
| Market reference away last update utc | 2026-10-18T11:57:34Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:34Z |
| Market best over 2 5 last update utc | 2026-10-18T11:57:30Z |
| Market best under 2 5 last update utc | 2026-10-18T11:57:30Z |
| Home probability edge | +1.9% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -1.4% |
| Under 2.5 probability edge | +1.4% |
| Raw edge prob home | 0.0374 |
| Raw ev home | 0.1817 |
| Raw edge prob draw | 0.0088 |
| Raw ev draw | -0.0065 |
| Raw edge prob away | -0.0462 |
| Raw ev away | -0.0971 |

</details>


---
