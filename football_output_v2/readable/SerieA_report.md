# Serie A — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,968 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | f92312438a998cae15e949932daf07bc0514d3e7702d7311116ff3f5086dcbd7 |
| Training as of utc | 2026-10-19T11:19:43.784125+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 68, 'bbs_added_results': 8, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 68, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T11:19:43.784125+00:00', 'observations': 87, 'observations_sha256': '5b474ebec0290e8d778e27013e9ccc47cd8a79147adae9b01e55b48ff813d9ce', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 44, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '17c3401e954c5514854d0870edada48bc827821c1d0c63856be54225797f449b', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2438.029 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.125 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261019T111943784125Z_1549c69c1a764670de4f78ce01440b2be7a00b8acc3877cc88ca75c5050bb150.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
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

The model's most likely 1X2 outcome is **AC Milan win** at **49.9%**. Expected goals are 1.50 for AC Milan and 1.31 for Atalanta BC (2.81 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.8%; Double Chance 1X: 74.5%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.6%; BTTS No (at least one team does not score): 43.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 49.9% | 2.00 |
| Draw | 24.6% | 4.07 |
| Atalanta BC win | 25.5% | 3.93 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.50 |
| Atalanta BC expected goals | 1.31 |
| Expected total goals | 2.81 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.62% |
| 2 | 2-1 | 10.71% |
| 3 | 1-0 | 10.45% |
| 4 | 2-0 | 8.19% |
| 5 | 0-0 | 6.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 49.9% | 58.5% | 1.77 | -11.6% |
| Draw | 24.6% | 23.3% | 4.12 | +1.3% |
| Atalanta BC win | 25.5% | 18.2% | 4.83 | +23.0% |
| Over 2.5 | 53.8% | 59.8% | 1.68 | -9.7% |
| Under 2.5 | 46.2% | 40.2% | 2.38 | +10.0% |

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
| Dc lambda home | 1.4992 |
| Dc lambda away | 1.3074 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.6% |
| P btts no | 43.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.36 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.46 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 41.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 77.4% |
| Raw p under 3 5 | 69.0% |
| Raw p btts yes | 57.1% |
| P home draw | 74.5% |
| P draw away | 50.1% |
| P home away | 75.4% |
| Raw p home draw | 67.3% |
| Raw p draw away | 58.6% |
| Raw p home away | 74.1% |
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
| Home probability edge | -8.6% |
| Draw probability edge | +1.3% |
| Away probability edge | +7.2% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.1711 |
| Raw ev home | -0.2676 |
| Raw edge prob draw | 0.0264 |
| Raw ev draw | 0.0677 |
| Raw edge prob away | 0.1447 |
| Raw ev away | 0.5796 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **54.1%**. Expected goals are 1.33 for Juventus and 0.96 for Lazio (2.29 combined). The most likely exact score is 1-0 at 15.8%. Goal-market probabilities: at least one goal: 90.6%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.7%; Double Chance 1X: 79.6%; Double Chance X2: 45.9%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 44.8%; BTTS No (at least one team does not score): 55.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 54.1% | 1.85 |
| Draw | 25.4% | 3.93 |
| Lazio win | 20.4% | 4.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.33 |
| Lazio expected goals | 0.96 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.6% |
| Under 0.5 | 9.4% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 15.82% |
| 2 | 1-1 | 11.84% |
| 3 | 2-0 | 10.84% |
| 4 | 2-1 | 10.41% |
| 5 | 0-0 | 9.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 54.1% | 63.7% | 1.61 | -12.8% |
| Draw | 25.4% | 22.1% | 4.27 | +8.6% |
| Lazio win | 20.4% | 14.2% | 6.30 | +28.7% |
| Over 2.5 | 41.4% | 51.5% | 1.96 | -18.9% |
| Under 2.5 | 58.6% | 48.5% | 1.98 | +16.1% |

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
| Dc lambda home | 1.3258 |
| Dc lambda away | 0.9605 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.8% |
| P btts no | 55.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.66 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.60 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 44.6% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 26.6% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 45.8% |
| P home draw | 79.6% |
| P draw away | 45.9% |
| P home away | 74.6% |
| Raw p home draw | 73.4% |
| Raw p draw away | 55.4% |
| Raw p home away | 71.3% |
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
| Home probability edge | -9.5% |
| Draw probability edge | +3.3% |
| Away probability edge | +6.2% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.1903 |
| Raw ev home | -0.2815 |
| Raw edge prob draw | 0.0661 |
| Raw ev draw | 0.2270 |
| Raw edge prob away | 0.1242 |
| Raw ev away | 0.6783 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Monza win** at **36.7%**. Expected goals are 1.21 for Monza and 1.30 for Cagliari (2.51 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.4%; Under 3.5 goals: 75.7%; Double Chance 1X: 65.5%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 36.7% | 2.72 |
| Draw | 28.8% | 3.47 |
| Cagliari win | 34.5% | 2.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.21 |
| Cagliari expected goals | 1.30 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.70% |
| 2 | 1-0 | 10.18% |
| 3 | 0-1 | 9.17% |
| 4 | 0-0 | 8.90% |
| 5 | 2-1 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 36.7% | 39.4% | 2.49 | -8.6% |
| Draw | 28.8% | 29.8% | 3.25 | -6.4% |
| Cagliari win | 34.5% | 30.8% | 3.25 | +12.1% |
| Over 2.5 | 45.4% | 45.2% | 2.15 | -2.4% |
| Under 2.5 | 54.6% | 54.8% | 1.82 | -0.7% |

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
| Dc lambda home | 1.2097 |
| Dc lambda away | 1.2963 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.23 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.12 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.22 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 75.6% |
| Raw p btts yes | 51.4% |
| P home draw | 65.5% |
| P draw away | 63.3% |
| P home away | 71.2% |
| Raw p home draw | 61.8% |
| Raw p draw away | 66.0% |
| Raw p home away | 72.2% |
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
| Home probability edge | -2.7% |
| Draw probability edge | -1.0% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.0532 |
| Raw ev home | -0.1525 |
| Raw edge prob draw | -0.0200 |
| Raw ev draw | -0.0965 |
| Raw edge prob away | 0.0733 |
| Raw ev away | 0.2402 |
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
| Market reference dc draw away odds | 1.56 |
| Market reference dc home draw odds | 1.38 |
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

The model's most likely 1X2 outcome is **Torino win** at **38.6%**. Expected goals are 0.97 for Parma and 1.06 for Torino (2.03 combined). The most likely exact score is 0-1 at 14.2%. Goal-market probabilities: at least one goal: 86.4%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.1%; Double Chance 1X: 61.4%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 68.7%; Under 4.5 goals: 94.4%; BTTS Yes (both teams score): 41.0%; BTTS No (at least one team does not score): 59.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.0% | 3.33 |
| Draw | 31.3% | 3.19 |
| Torino win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 0.97 |
| Torino expected goals | 1.06 |
| Expected total goals | 2.03 |
| Over 0.5 | 86.4% |
| Under 0.5 | 13.6% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.9% |
| Under 3.5 | 85.1% |
| Over 4.5 | 5.6% |
| Under 4.5 | 94.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.18% |
| 2 | 1-1 | 13.92% |
| 3 | 0-0 | 13.55% |
| 4 | 1-0 | 11.56% |
| 5 | 0-2 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.0% | 28.3% | 3.43 | +3.0% |
| Draw | 31.3% | 31.3% | 3.17 | -0.6% |
| Torino win | 38.6% | 40.5% | 2.45 | -5.3% |
| Over 2.5 | 33.2% | 39.6% | 2.49 | -17.4% |
| Under 2.5 | 66.8% | 60.4% | 1.63 | +8.9% |

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
| Dc lambda home | 0.9668 |
| Dc lambda away | 1.0632 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 41.0% |
| P btts no | 59.0% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.38 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 6.73 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.01 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 31.4% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 60.7% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 41.0% |
| P home draw | 61.4% |
| P draw away | 70.0% |
| P home away | 68.7% |
| Raw p home draw | 63.2% |
| Raw p draw away | 68.2% |
| Raw p home away | 68.6% |
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
| Home probability edge | +1.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0351 |
| Raw ev home | 0.0898 |
| Raw edge prob draw | 0.0018 |
| Raw ev draw | -0.0034 |
| Raw edge prob away | -0.0369 |
| Raw ev away | -0.0987 |
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
| Market reference dc draw away odds | 1.35 |
| Market reference dc home draw odds | 1.61 |
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

The model's most likely 1X2 outcome is **Torino win** at **47.5%**. Expected goals are 1.51 for Torino and 0.96 for Monza (2.46 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.3%; Under 3.5 goals: 76.7%; Double Chance 1X: 75.0%; Double Chance X2: 52.5%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 89.7%; BTTS Yes (both teams score): 48.5%; BTTS No (at least one team does not score): 51.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 47.5% | 2.11 |
| Draw | 27.5% | 3.63 |
| Monza win | 25.0% | 4.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 0.96 |
| Expected total goals | 2.46 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.3% |
| Under 4.5 | 89.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.02% |
| 2 | 1-0 | 11.89% |
| 3 | 2-0 | 9.26% |
| 4 | 0-0 | 9.18% |
| 5 | 2-1 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 47.5% | 45.3% | 2.15 | +2.1% |
| Draw | 27.5% | 28.2% | 3.62 | -0.4% |
| Monza win | 25.0% | 26.4% | 3.64 | -9.0% |
| Over 2.5 | 44.3% | 44.2% | 2.11 | -6.5% |
| Under 2.5 | 55.7% | 55.8% | 1.85 | +3.0% |

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
| Dc lambda home | 1.5063 |
| Dc lambda away | 0.9556 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.5% |
| P btts no | 51.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.90 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.30 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.74 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 49.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 23.6% |
| Raw p over 1 5 | 70.9% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.3% |
| P home draw | 75.0% |
| P draw away | 52.5% |
| P home away | 72.5% |
| Raw p home draw | 76.4% |
| Raw p draw away | 50.4% |
| Raw p home away | 73.2% |
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
| Home probability edge | +2.1% |
| Draw probability edge | -0.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | 0.0429 |
| Raw ev home | 0.0670 |
| Raw edge prob draw | -0.0141 |
| Raw ev draw | -0.0290 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.1427 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.2%**. Expected goals are 1.06 for Cagliari and 1.40 for Bologna (2.45 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 44.0%; Under 3.5 goals: 76.9%; Double Chance 1X: 57.8%; Double Chance X2: 70.8%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 89.9%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 29.2% | 3.42 |
| Draw | 28.5% | 3.50 |
| Bologna win | 42.2% | 2.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.06 |
| Bologna expected goals | 1.40 |
| Expected total goals | 2.45 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 70.6% |
| Under 1.5 | 29.4% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.52% |
| 2 | 0-1 | 11.06% |
| 3 | 0-0 | 9.32% |
| 4 | 1-0 | 9.04% |
| 5 | 1-2 | 8.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 29.2% | 30.4% | 3.35 | -2.1% |
| Draw | 28.5% | 29.4% | 3.13 | -10.7% |
| Bologna win | 42.2% | 40.2% | 2.52 | +6.4% |
| Over 2.5 | 44.0% | 42.7% | 2.24 | -1.3% |
| Under 2.5 | 56.0% | 57.3% | 1.76 | -1.5% |

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
| Dc lambda home | 1.0562 |
| Dc lambda away | 1.3954 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.73 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.40 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.87 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 28.0% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 44.3% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 49.5% |
| P home draw | 57.8% |
| P draw away | 70.8% |
| P home away | 71.5% |
| Raw p home draw | 55.7% |
| Raw p draw away | 72.0% |
| Raw p home away | 72.3% |
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
| Home probability edge | -1.2% |
| Draw probability edge | -0.8% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | -0.0239 |
| Raw ev home | -0.0606 |
| Raw edge prob draw | -0.0168 |
| Raw ev draw | -0.1333 |
| Raw edge prob away | 0.0407 |
| Raw ev away | 0.1155 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **66.0%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.7%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 60.1%; Under 3.5 goals: 62.5%; Double Chance 1X: 85.5%; Double Chance X2: 34.0%; Double Chance 12 (either team wins): 80.5%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 66.0% | 1.51 |
| Draw | 19.5% | 5.12 |
| Sassuolo win | 14.5% | 6.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 81.9% |
| Under 1.5 | 18.1% |
| Over 2.5 | 60.1% |
| Under 2.5 | 39.9% |
| Over 3.5 | 37.5% |
| Under 3.5 | 62.5% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.68% |
| 2 | 2-1 | 10.28% |
| 3 | 1-0 | 9.74% |
| 4 | 1-1 | 9.17% |
| 5 | 3-0 | 7.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 66.0% | 68.4% | 1.49 | -1.6% |
| Draw | 19.5% | 18.5% | 4.94 | -3.6% |
| Sassuolo win | 14.5% | 13.2% | 7.10 | +2.8% |

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
| Dc lambda home | 2.1219 |
| Dc lambda away | 0.9624 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.53 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.51 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.95 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 63.7% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 62.8% |
| Raw p btts yes | 54.7% |
| P home draw | 85.5% |
| P draw away | 34.0% |
| P home away | 80.5% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.3% |
| Raw p home away | 79.4% |
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
| Home probability edge | -2.4% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0472 |
| Raw ev home | -0.0516 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | 0.0155 |
| Raw edge prob away | 0.0263 |
| Raw ev away | 0.1211 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **59.7%**. Expected goals are 1.57 for Lazio and 0.72 for Parma (2.29 combined). The most likely exact score is 1-0 at 16.2%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 40.7%; Under 3.5 goals: 80.0%; Double Chance 1X: 84.1%; Double Chance X2: 40.3%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 40.6%; BTTS No (at least one team does not score): 59.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 59.7% | 1.68 |
| Draw | 24.4% | 4.10 |
| Parma win | 15.9% | 6.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.57 |
| Parma expected goals | 0.72 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.7% |
| Under 2.5 | 59.3% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.20% |
| 2 | 2-0 | 12.99% |
| 3 | 1-1 | 11.10% |
| 4 | 0-0 | 9.87% |
| 5 | 2-1 | 9.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 59.7% | 62.2% | 1.58 | -5.7% |
| Draw | 24.4% | 22.7% | 4.33 | +5.7% |
| Parma win | 15.9% | 15.1% | 6.64 | +5.5% |
| Over 2.5 | 40.7% | 49.3% | 2.06 | -16.1% |
| Under 2.5 | 59.3% | 50.7% | 1.89 | +12.0% |

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
| Dc lambda home | 1.5652 |
| Dc lambda away | 0.7215 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 40.6% |
| P btts no | 59.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.13 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.45 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.88 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 57.2% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 41.0% |
| P home draw | 84.1% |
| P draw away | 40.3% |
| P home away | 75.6% |
| Raw p home draw | 83.3% |
| Raw p draw away | 42.8% |
| Raw p home away | 73.9% |
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
| Home probability edge | -2.5% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.0503 |
| Raw ev home | -0.0965 |
| Raw edge prob draw | 0.0336 |
| Raw ev draw | 0.1295 |
| Raw edge prob away | 0.0168 |
| Raw ev away | 0.1110 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **35.8%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.27 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.3%; Double Chance X2: 64.2%; Double Chance 12 (either team wins): 71.5%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 35.8% | 2.79 |
| Draw | 28.5% | 3.51 |
| AS Roma win | 35.7% | 2.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.26% |
| 2 | 0-1 | 11.89% |
| 3 | 1-0 | 11.11% |
| 4 | 0-0 | 10.47% |
| 5 | 1-2 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 35.8% | 32.8% | 3.04 | +8.8% |
| Draw | 28.5% | 27.5% | 3.60 | +2.5% |
| AS Roma win | 35.7% | 39.7% | 2.45 | -12.4% |
| Over 2.5 | 39.7% | 51.5% | 1.93 | -23.3% |
| Under 2.5 | 60.3% | 48.5% | 2.01 | +21.1% |

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
| Dc lambda home | 1.2030 |
| Dc lambda away | 1.0624 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.55 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.45 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.6% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 46.2% |
| P home draw | 64.3% |
| P draw away | 64.2% |
| P home away | 71.5% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
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
| Home probability edge | +3.0% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.9% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | 0.0594 |
| Raw ev home | 0.1788 |
| Raw edge prob draw | 0.0195 |
| Raw ev draw | 0.0595 |
| Raw edge prob away | -0.0789 |
| Raw ev away | -0.2211 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **61.3%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.36 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 64.9%; Under 3.5 goals: 56.9%; Double Chance 1X: 82.0%; Double Chance X2: 38.7%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 61.3% | 1.63 |
| Draw | 20.6% | 4.85 |
| Frosinone win | 18.0% | 5.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 64.9% |
| Under 2.5 | 35.1% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.52% |
| 2 | 1-1 | 9.29% |
| 3 | 2-0 | 8.60% |
| 4 | 1-0 | 7.35% |
| 5 | 3-1 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 61.3% | 59.8% | 1.72 | +5.5% |
| Draw | 20.6% | 21.4% | 4.37 | -9.8% |
| Frosinone win | 18.0% | 18.8% | 4.88 | -12.0% |

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
| Dc lambda home | 2.2513 |
| Dc lambda away | 1.1076 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.58 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.67 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 60.2% |
| P home draw | 82.0% |
| P draw away | 38.7% |
| P home away | 79.4% |
| Raw p home draw | 82.8% |
| Raw p draw away | 37.1% |
| Raw p home away | 80.1% |
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
| Home probability edge | +1.5% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.0811 |
| Raw edge prob draw | -0.0147 |
| Raw ev draw | -0.1305 |
| Raw edge prob away | -0.0159 |
| Raw ev away | -0.1584 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **46.9%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 89.4%; Over 2.5 goals: 39.4%; Under 3.5 goals: 80.9%; Double Chance 1X: 74.5%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 43.8%; BTTS No (at least one team does not score): 56.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 46.9% | 2.13 |
| Draw | 27.6% | 3.63 |
| Venezia win | 25.5% | 3.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.4% |
| Under 0.5 | 10.6% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.4% |
| Under 2.5 | 60.6% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.55% |
| 2 | 1-1 | 12.71% |
| 3 | 0-0 | 10.63% |
| 4 | 2-0 | 9.76% |
| 5 | 0-1 | 9.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 46.9% | 44.7% | 2.14 | +0.4% |
| Draw | 27.6% | 27.0% | 3.44 | -5.2% |
| Venezia win | 25.5% | 28.3% | 3.87 | -1.3% |
| Over 2.5 | 39.4% | 51.5% | 1.97 | -22.4% |
| Under 2.5 | 60.6% | 48.5% | 1.98 | +20.0% |

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
| Dc lambda home | 1.3992 |
| Dc lambda away | 0.8599 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.8% |
| P btts no | 56.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.41 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.54 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.67 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.9% |
| P home draw | 74.5% |
| P draw away | 53.1% |
| P home away | 72.4% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.8% |
| Raw p home away | 71.8% |
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
| Home probability edge | +2.2% |
| Draw probability edge | +0.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -12.1% |
| Under 2.5 probability edge | +12.1% |
| Raw edge prob home | 0.0443 |
| Raw ev home | 0.0518 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | -0.0304 |
| Raw edge prob away | -0.0566 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **69.7%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.35 combined). The most likely exact score is 2-0 at 10.2%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.1%; Under 3.5 goals: 56.9%; Double Chance 1X: 87.4%; Double Chance X2: 30.3%; Double Chance 12 (either team wins): 82.3%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 55.7%; BTTS No (at least one team does not score): 44.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.7% | 1.43 |
| Draw | 17.7% | 5.66 |
| Fiorentina win | 12.6% | 7.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.1% |
| Under 2.5 | 34.9% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.22% |
| 2 | 2-1 | 9.61% |
| 3 | 1-0 | 8.22% |
| 4 | 3-0 | 8.21% |
| 5 | 1-1 | 8.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.7% | 69.9% | 1.41 | -1.7% |
| Draw | 17.7% | 17.5% | 5.56 | -1.7% |
| Fiorentina win | 12.6% | 12.5% | 7.90 | -0.6% |

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
| Dc lambda home | 2.4081 |
| Dc lambda away | 0.9397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.7% |
| P btts no | 44.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.63 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.67 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.06 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.0% |
| Raw p btts yes | 55.7% |
| P home draw | 87.4% |
| P draw away | 30.3% |
| P home away | 82.3% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
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
| Home probability edge | -0.2% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0040 |
| Raw ev home | -0.0194 |
| Raw edge prob draw | 0.0029 |
| Raw ev draw | -0.0092 |
| Raw edge prob away | 0.0011 |
| Raw ev away | -0.0017 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **63.3%**. Expected goals are 0.62 for Lecce and 1.49 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.3%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 36.7%; Under 3.5 goals: 83.1%; Double Chance 1X: 36.7%; Double Chance X2: 87.0%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 93.3%; BTTS Yes (both teams score): 35.4%; BTTS No (at least one team does not score): 64.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.0% | 7.72 |
| Draw | 23.7% | 4.22 |
| Juventus win | 63.3% | 1.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.49 |
| Expected total goals | 2.11 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 63.6% |
| Under 1.5 | 36.4% |
| Over 2.5 | 36.7% |
| Under 2.5 | 63.3% |
| Over 3.5 | 16.9% |
| Under 3.5 | 83.1% |
| Over 4.5 | 6.7% |
| Under 4.5 | 93.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.32% |
| 2 | 0-2 | 14.67% |
| 3 | 0-0 | 10.96% |
| 4 | 1-1 | 10.20% |
| 5 | 1-2 | 9.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.0% | 10.7% | 7.70 | -0.3% |
| Draw | 23.7% | 20.4% | 4.53 | +7.4% |
| Juventus win | 63.3% | 68.9% | 1.50 | -5.0% |
| Over 2.5 | 36.7% | 50.0% | 1.92 | -29.5% |
| Under 2.5 | 63.3% | 50.0% | 2.02 | +27.8% |

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
| Dc lambda home | 0.6242 |
| Dc lambda away | 1.4866 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.4% |
| P btts no | 64.6% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.12 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.75 |
| Fair Over 2.5 odds | 2.72 |
| Fair Under 2.5 odds | 1.58 |
| Fair Over 3.5 odds | 5.93 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.01 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 57.8% |
| Raw p over 1 5 | 62.7% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 36.7% |
| P draw away | 87.0% |
| P home away | 76.3% |
| Raw p home draw | 42.2% |
| Raw p draw away | 84.8% |
| Raw p home away | 73.0% |
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
| Home probability edge | +2.2% |
| Draw probability edge | +3.3% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | 0.0445 |
| Raw ev home | 0.1686 |
| Raw edge prob draw | 0.0662 |
| Raw ev draw | 0.2235 |
| Raw edge prob away | -0.1107 |
| Raw ev away | -0.1328 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.6%**. Expected goals are 1.05 for Udinese and 1.70 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 51.6%; Under 3.5 goals: 70.5%; Double Chance 1X: 47.4%; Double Chance X2: 77.8%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 85.7%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 22.2% | 4.50 |
| Draw | 25.2% | 3.97 |
| AC Milan win | 52.6% | 1.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.05 |
| AC Milan expected goals | 1.70 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.3% |
| Under 1.5 | 23.7% |
| Over 2.5 | 51.6% |
| Under 2.5 | 48.4% |
| Over 3.5 | 29.5% |
| Under 3.5 | 70.5% |
| Over 4.5 | 14.3% |
| Under 4.5 | 85.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.98% |
| 2 | 0-1 | 10.63% |
| 3 | 1-2 | 9.77% |
| 4 | 0-2 | 9.34% |
| 5 | 0-0 | 6.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 22.2% | 21.5% | 4.68 | +4.0% |
| Draw | 25.2% | 25.5% | 3.91 | -1.5% |
| AC Milan win | 52.6% | 53.0% | 1.83 | -3.7% |
| Over 2.5 | 51.6% | 50.0% | 1.97 | +1.6% |
| Under 2.5 | 48.4% | 50.0% | 1.97 | -4.6% |

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
| Dc lambda home | 1.0458 |
| Dc lambda away | 1.6957 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:43.784125+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.44 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.22 |
| Fair Over 2.5 odds | 1.94 |
| Fair Under 2.5 odds | 2.06 |
| Fair Over 3.5 odds | 3.39 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.99 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 52.2% |
| Raw p over 1 5 | 76.3% |
| Raw p under 3 5 | 70.5% |
| Raw p btts yes | 53.3% |
| P home draw | 47.4% |
| P draw away | 77.8% |
| P home away | 74.8% |
| Raw p home draw | 47.8% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.2% |
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
| Home probability edge | +0.7% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | 0.0148 |
| Raw ev home | 0.0745 |
| Raw edge prob draw | -0.0068 |
| Raw ev draw | -0.0287 |
| Raw edge prob away | -0.0081 |
| Raw ev away | -0.0448 |

</details>


---
