# Ligue 1 — football model report

Fixtures in this report: **13**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,741 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | ddef9182f39b5da858ffcd246948f093a52d0699a7614848c1a03192c104ac4e |
| Training as of utc | 2026-10-19T11:19:59.671092+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T11:19:59.671092+00:00', 'observations': 76, 'observations_sha256': '2787aa3b89fdfbe359cc22efa66e26638042c51a7ceb9bc0ecb3fa5c36c064e0', 'eligible_training_matches': 17, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 47, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 17, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '6451d322e757cf80e7b777ac8793016e3ff63c5c9ce7ff33ce5b8fc64bce2561', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 5075.352 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.055 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 13.00 |
| Additional event odds calls used before this league | 4.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261019T111959671092Z_69ea015620fe174db7b11cbbf0dfd10292c90a42e60a999b2ab2b8eef2c4fa62.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Le Havre vs Auxerre

The model's most likely 1X2 outcome is **Le Havre win** at **40.0%**. Expected goals are 1.24 for Le Havre and 1.14 for Auxerre (2.38 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.4%; Over 2.5 goals: 42.9%; Under 3.5 goals: 78.3%; Double Chance 1X: 68.0%; Double Chance X2: 60.0%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 90.6%; BTTS Yes (both teams score): 48.7%; BTTS No (at least one team does not score): 51.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Le Havre win | 40.0% | 2.50 |
| Draw | 28.0% | 3.57 |
| Auxerre win | 32.0% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Le Havre expected goals | 1.24 |
| Auxerre expected goals | 1.14 |
| Expected total goals | 2.38 |
| Over 0.5 | 90.4% |
| Under 0.5 | 9.6% |
| Over 1.5 | 69.5% |
| Under 1.5 | 30.5% |
| Over 2.5 | 42.9% |
| Under 2.5 | 57.1% |
| Over 3.5 | 21.7% |
| Under 3.5 | 78.3% |
| Over 4.5 | 9.4% |
| Under 4.5 | 90.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.23% |
| 2 | 1-0 | 11.39% |
| 3 | 0-0 | 9.58% |
| 4 | 0-1 | 9.56% |
| 5 | 2-1 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Le Havre win | 40.0% | 42.2% | 2.34 | -6.3% |
| Draw | 28.0% | 26.8% | 3.60 | +0.8% |
| Auxerre win | 32.0% | 31.1% | 3.23 | +3.3% |
| Over 2.5 | 42.9% | 54.8% | 1.79 | -23.3% |
| Under 2.5 | 57.1% | 45.2% | 2.19 | +25.1% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Le Havre |
| Matched away-team name | Auxerre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2399 |
| Dc lambda away | 1.1379 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.7% |
| P btts no | 51.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.44 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.28 |
| Fair Over 2.5 odds | 2.33 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.60 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.60 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 32.9% |
| Raw p over 1 5 | 69.4% |
| Raw p under 3 5 | 78.3% |
| Raw p btts yes | 49.0% |
| P home draw | 68.0% |
| P draw away | 60.0% |
| P home away | 72.0% |
| Raw p home draw | 67.1% |
| Raw p draw away | 62.1% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0430 |
| Raw ev home | -0.1137 |
| Raw edge prob draw | 0.0245 |
| Raw ev draw | 0.0515 |
| Raw edge prob away | 0.0186 |
| Raw ev away | 0.0631 |

</details>


---

## 2026-10-18 — Lorient vs AS Monaco

The model's most likely 1X2 outcome is **AS Monaco win** at **49.7%**. Expected goals are 1.26 for Lorient and 1.84 for AS Monaco (3.10 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.6%; Double Chance 1X: 50.3%; Double Chance X2: 74.7%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lorient win | 25.3% | 3.95 |
| Draw | 25.0% | 4.01 |
| AS Monaco win | 49.7% | 2.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lorient expected goals | 1.26 |
| AS Monaco expected goals | 1.84 |
| Expected total goals | 3.10 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 82.0% |
| Under 1.5 | 18.0% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.48% |
| 2 | 1-2 | 9.46% |
| 3 | 0-1 | 7.62% |
| 4 | 0-2 | 7.53% |
| 5 | 2-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lorient win | 25.3% | 25.2% | 3.80 | -3.7% |
| Draw | 25.0% | 26.0% | 3.49 | -12.9% |
| AS Monaco win | 49.7% | 48.8% | 2.15 | +6.8% |
| Over 2.5 | 59.4% | 48.5% | 2.05 | +21.9% |
| Under 2.5 | 40.6% | 51.5% | 1.89 | -23.3% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.2555 |
| Dc lambda away | 1.8408 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.83 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.56 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 25.5% |
| Unadjusted draw probability | 24.0% |
| Unadjusted away-win probability | 50.5% |
| Raw p over 1 5 | 82.1% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 60.7% |
| P home draw | 50.3% |
| P draw away | 74.7% |
| P home away | 75.0% |
| Raw p home draw | 49.5% |
| Raw p draw away | 74.5% |
| Raw p home away | 76.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.96 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.82 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +0.1% |
| Draw probability edge | -1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | +10.9% |
| Under 2.5 probability edge | -10.9% |
| Raw edge prob home | 0.0030 |
| Raw ev home | -0.0311 |
| Raw edge prob draw | -0.0200 |
| Raw ev draw | -0.1639 |
| Raw edge prob away | 0.0170 |
| Raw ev away | 0.0867 |

</details>


---

## 2026-10-18 — Lyon vs Nice

The model's most likely 1X2 outcome is **Lyon win** at **48.7%**. Expected goals are 1.49 for Lyon and 1.14 for Nice (2.63 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.7%; Double Chance 1X: 74.1%; Double Chance X2: 51.3%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 87.1%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lyon win | 48.7% | 2.05 |
| Draw | 25.4% | 3.93 |
| Nice win | 25.9% | 3.87 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lyon expected goals | 1.49 |
| Nice expected goals | 1.14 |
| Expected total goals | 2.63 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.3% |
| Under 3.5 | 72.7% |
| Over 4.5 | 12.9% |
| Under 4.5 | 87.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.12% |
| 2 | 1-0 | 11.00% |
| 3 | 2-1 | 9.96% |
| 4 | 2-0 | 8.75% |
| 5 | 0-0 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lyon win | 48.7% | 52.8% | 1.92 | -6.5% |
| Draw | 25.4% | 23.8% | 3.94 | +0.2% |
| Nice win | 25.9% | 23.4% | 4.16 | +7.6% |
| Over 2.5 | 49.6% | 56.7% | 1.75 | -13.3% |
| Under 2.5 | 50.4% | 43.3% | 2.25 | +13.5% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.4906 |
| Dc lambda away | 1.1385 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.51 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.67 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.74 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 44.6% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 28.3% |
| Raw p over 1 5 | 74.5% |
| Raw p under 3 5 | 73.0% |
| Raw p btts yes | 53.3% |
| P home draw | 74.1% |
| P draw away | 51.3% |
| P home away | 74.6% |
| Raw p home draw | 71.7% |
| Raw p draw away | 55.4% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.82 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -4.1% |
| Draw probability edge | +1.7% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | -0.0819 |
| Raw ev home | -0.1433 |
| Raw edge prob draw | 0.0333 |
| Raw ev draw | 0.0674 |
| Raw edge prob away | 0.0486 |
| Raw ev away | 0.1769 |

</details>


---

## 2026-10-18 — Paris FC vs Rennes

The model's most likely 1X2 outcome is **Paris FC win** at **41.3%**. Expected goals are 1.49 for Paris FC and 1.56 for Rennes (3.05 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 58.9%; Under 3.5 goals: 63.6%; Double Chance 1X: 66.4%; Double Chance X2: 58.7%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris FC win | 41.3% | 2.42 |
| Draw | 25.1% | 3.99 |
| Rennes win | 33.6% | 2.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris FC expected goals | 1.49 |
| Rennes expected goals | 1.56 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.9% |
| Under 2.5 | 41.1% |
| Over 3.5 | 36.4% |
| Under 3.5 | 63.6% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 2-1 | 9.43% |
| 3 | 1-2 | 7.44% |
| 4 | 1-0 | 7.42% |
| 5 | 2-2 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris FC win | 41.3% | 46.6% | 2.17 | -10.4% |
| Draw | 25.1% | 24.9% | 3.62 | -9.3% |
| Rennes win | 33.6% | 28.5% | 3.60 | +21.1% |
| Over 2.5 | 58.9% | 58.6% | 1.72 | +1.2% |
| Under 2.5 | 41.1% | 41.4% | 2.30 | -5.4% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.4940 |
| Dc lambda away | 1.5567 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.88 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.17 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 36.0% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 38.7% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 61.8% |
| P home draw | 66.4% |
| P draw away | 58.7% |
| P home away | 74.9% |
| Raw p home draw | 61.3% |
| Raw p draw away | 64.0% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:33Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -5.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | -0.1060 |
| Raw ev home | -0.2188 |
| Raw edge prob draw | 0.0041 |
| Raw ev draw | -0.0853 |
| Raw edge prob away | 0.1019 |
| Raw ev away | 0.3944 |

</details>


---

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **39.6%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.6%; Double Chance 1X: 66.5%; Double Chance X2: 60.4%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.6% | 2.52 |
| Draw | 26.9% | 3.72 |
| Nice win | 33.5% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.2% |
| Under 1.5 | 28.8% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.78% |
| 2 | 1-0 | 10.95% |
| 3 | 0-1 | 9.17% |
| 4 | 2-1 | 8.88% |
| 5 | 0-0 | 8.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.6% | 44.1% | 2.31 | -8.5% |
| Draw | 26.9% | 25.1% | 3.49 | -6.2% |
| Nice win | 33.5% | 30.9% | 3.37 | +12.9% |
| Over 2.5 | 45.2% | 56.0% | 1.76 | -20.5% |
| Under 2.5 | 54.8% | 44.0% | 2.23 | +22.3% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.2185 |
| Dc lambda away | 1.2395 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.51 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.27 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.52 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.2% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 50.8% |
| P home draw | 66.5% |
| P draw away | 60.4% |
| P home away | 73.1% |
| Raw p home draw | 63.8% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -4.5% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -10.9% |
| Under 2.5 probability edge | +10.9% |
| Raw edge prob home | -0.0892 |
| Raw ev home | -0.1881 |
| Raw edge prob draw | 0.0363 |
| Raw ev draw | 0.0015 |
| Raw edge prob away | 0.0530 |
| Raw ev away | 0.2185 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **49.4%**. Expected goals are 1.68 for RC Lens and 1.03 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.8%; Under 3.5 goals: 71.6%; Double Chance 1X: 74.0%; Double Chance X2: 50.6%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 86.3%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 49.4% | 2.03 |
| Draw | 24.7% | 4.05 |
| Paris FC win | 26.0% | 3.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.03 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 28.4% |
| Under 3.5 | 71.6% |
| Over 4.5 | 13.7% |
| Under 4.5 | 86.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.76% |
| 2 | 1-0 | 10.08% |
| 3 | 2-1 | 9.18% |
| 4 | 2-0 | 8.96% |
| 5 | 0-1 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 49.4% | 46.8% | 2.09 | +3.2% |
| Draw | 24.7% | 23.8% | 3.90 | -3.8% |
| Paris FC win | 26.0% | 29.4% | 3.58 | -7.1% |
| Over 2.5 | 50.8% | 58.8% | 1.68 | -14.6% |
| Under 2.5 | 49.2% | 41.2% | 2.38 | +17.0% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.6768 |
| Dc lambda away | 1.0251 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.7% |
| P btts no | 47.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.09 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.52 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.28 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 74.0% |
| P draw away | 50.6% |
| P home away | 75.3% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | 0.0524 |
| Raw ev home | 0.0867 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | -0.0048 |
| Raw edge prob away | -0.0694 |
| Raw ev away | -0.1949 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.8%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.8%; Double Chance 1X: 81.8%; Double Chance X2: 40.2%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.8% | 1.67 |
| Draw | 22.0% | 4.55 |
| Troyes win | 18.2% | 5.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.81% |
| 2 | 1-0 | 10.76% |
| 3 | 1-1 | 10.49% |
| 4 | 2-1 | 9.84% |
| 5 | 3-0 | 6.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.8% | 59.5% | 1.71 | +2.3% |
| Draw | 22.0% | 21.0% | 4.26 | -6.3% |
| Troyes win | 18.2% | 19.5% | 5.13 | -6.9% |
| Over 2.5 | 53.8% | 59.2% | 1.67 | -10.2% |
| Under 2.5 | 46.2% | 40.8% | 2.40 | +11.0% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.9078 |
| Dc lambda away | 0.9102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.95 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.41 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 81.8% |
| P draw away | 40.2% |
| P home away | 78.0% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | 0.0069 |
| Raw ev home | 0.0293 |
| Raw edge prob draw | 0.0192 |
| Raw ev draw | -0.0220 |
| Raw edge prob away | -0.0261 |
| Raw ev away | -0.1356 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **45.2%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.6%; Double Chance 1X: 70.8%; Double Chance X2: 54.8%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 45.2% | 2.21 |
| Draw | 25.6% | 3.91 |
| Lille win | 29.2% | 3.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.10% |
| 2 | 2-1 | 9.48% |
| 3 | 1-0 | 8.96% |
| 4 | 2-0 | 7.50% |
| 5 | 1-2 | 7.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 45.2% | 46.9% | 2.18 | -1.4% |
| Draw | 25.6% | 25.1% | 3.60 | -7.8% |
| Lille win | 29.2% | 28.1% | 3.60 | +5.0% |
| Over 2.5 | 53.8% | 55.8% | 1.77 | -4.8% |
| Under 2.5 | 46.2% | 44.2% | 2.22 | +2.6% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.5580 |
| Dc lambda away | 1.2637 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.49 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.38 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 70.8% |
| P draw away | 54.8% |
| P home away | 74.4% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.4% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -1.7% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0334 |
| Raw ev home | -0.0506 |
| Raw edge prob draw | 0.0110 |
| Raw ev draw | -0.0585 |
| Raw edge prob away | 0.0224 |
| Raw ev away | 0.0907 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **36.7%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.5%; Under 3.5 goals: 76.0%; Double Chance 1X: 63.3%; Double Chance X2: 64.7%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 35.3% | 2.83 |
| Draw | 28.0% | 3.58 |
| Lorient win | 36.7% | 2.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.5% |
| Under 2.5 | 54.5% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.31% |
| 2 | 1-0 | 9.76% |
| 3 | 0-1 | 9.64% |
| 4 | 0-0 | 8.85% |
| 5 | 2-1 | 8.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 35.3% | 37.4% | 2.69 | -5.0% |
| Draw | 28.0% | 27.5% | 3.40 | -5.0% |
| Lorient win | 36.7% | 35.1% | 2.85 | +4.7% |
| Over 2.5 | 45.5% | 44.9% | 2.19 | -0.4% |
| Under 2.5 | 54.5% | 55.1% | 1.79 | -2.4% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.1904 |
| Dc lambda away | 1.2988 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.30 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.28 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.4% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 63.3% |
| P draw away | 64.7% |
| P home away | 72.0% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.19 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0425 |
| Raw ev home | -0.1071 |
| Raw edge prob draw | 0.0097 |
| Raw ev draw | -0.0331 |
| Raw edge prob away | 0.0328 |
| Raw ev away | 0.0935 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.0%**. Expected goals are 1.73 for Auxerre and 1.51 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 68.8%; Double Chance X2: 56.0%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.0% | 2.27 |
| Draw | 24.8% | 4.03 |
| Le Mans FC win | 31.2% | 3.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.51 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.05% |
| 2 | 2-1 | 9.17% |
| 3 | 1-2 | 7.24% |
| 4 | 2-2 | 6.85% |
| 5 | 1-0 | 6.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.0% | 45.6% | 2.23 | -1.9% |
| Draw | 24.8% | 25.4% | 3.70 | -8.1% |
| Le Mans FC win | 31.2% | 29.0% | 3.37 | +5.1% |
| Over 2.5 | 62.7% | 55.4% | 1.78 | +11.6% |
| Under 2.5 | 37.3% | 44.6% | 2.20 | -17.9% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 1.7265 |
| Dc lambda away | 1.5148 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.83 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.24 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.42 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 68.8% |
| P draw away | 56.0% |
| P home away | 75.2% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.6% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:33Z |
| Market reference home last update utc | 2026-10-18T14:34:33Z |
| Market reference draw last update utc | 2026-10-18T14:34:33Z |
| Market reference away last update utc | 2026-10-18T14:34:33Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | -1.6% |
| Draw probability edge | -0.6% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | +7.3% |
| Under 2.5 probability edge | -7.3% |
| Raw edge prob home | -0.0323 |
| Raw ev home | -0.0553 |
| Raw edge prob draw | -0.0115 |
| Raw ev draw | -0.1027 |
| Raw edge prob away | 0.0438 |
| Raw ev away | 0.1251 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.7%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 55.6%; Under 3.5 goals: 67.0%; Double Chance 1X: 84.1%; Double Chance X2: 36.3%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 49.6%; BTTS No (at least one team does not score): 50.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.7% | 1.57 |
| Draw | 20.5% | 4.89 |
| Le Havre win | 15.9% | 6.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 55.6% |
| Under 2.5 | 44.4% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.42% |
| 2 | 1-0 | 10.33% |
| 3 | 1-1 | 9.76% |
| 4 | 2-1 | 9.25% |
| 5 | 3-0 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.7% | 60.4% | 1.64 | +4.4% |
| Draw | 20.5% | 20.6% | 4.57 | -6.5% |
| Le Havre win | 15.9% | 19.0% | 5.33 | -15.4% |
| Over 2.5 | 55.6% | 59.5% | 1.66 | -7.8% |
| Under 2.5 | 44.4% | 40.5% | 2.42 | +7.5% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
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
| Dc lambda home | 2.1126 |
| Dc lambda away | 0.8099 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.6% |
| P btts no | 50.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.91 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.75 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.25 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.91 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.1% |
| P draw away | 36.3% |
| P home away | 79.5% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:32Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:32Z |
| Home probability edge | +3.3% |
| Draw probability edge | -0.1% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0654 |
| Raw ev home | 0.0977 |
| Raw edge prob draw | -0.0018 |
| Raw ev draw | -0.0691 |
| Raw edge prob away | -0.0636 |
| Raw ev away | -0.3234 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **68.5%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 69.0%; Under 3.5 goals: 52.9%; Double Chance 1X: 85.5%; Double Chance X2: 31.5%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 71.7%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 68.5% | 1.46 |
| Draw | 17.0% | 5.87 |
| Lyon win | 14.5% | 6.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 69.0% |
| Under 2.5 | 31.0% |
| Over 3.5 | 47.1% |
| Under 3.5 | 52.9% |
| Over 4.5 | 28.3% |
| Under 4.5 | 71.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.86% |
| 2 | 2-0 | 9.00% |
| 3 | 3-1 | 7.97% |
| 4 | 1-1 | 7.55% |
| 5 | 3-0 | 7.27% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 68.5% | 70.8% | 1.43 | -2.1% |
| Draw | 17.0% | 15.3% | 5.44 | -7.3% |
| Lyon win | 14.5% | 13.9% | 7.60 | +10.0% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4236 |
| Dc lambda away | 1.0955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.38 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.83 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.22 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.54 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 61.1% |
| P home draw | 85.5% |
| P draw away | 31.5% |
| P home away | 83.0% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.36 |
| Reference draw odds | 5.30 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:33Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | -0.0459 |
| Raw ev home | -0.0535 |
| Raw edge prob draw | 0.0339 |
| Raw ev draw | 0.0195 |
| Raw edge prob away | 0.0120 |
| Raw ev away | 0.1452 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **54.3%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.15 combined). The most likely exact score is 2-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.6%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.4%; Double Chance X2: 45.7%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 78.6%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 54.3% | 1.84 |
| Draw | 22.1% | 4.53 |
| Strasbourg win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.6% |
| Under 2.5 | 38.4% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.4% |
| Under 4.5 | 78.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.08% |
| 2 | 1-1 | 10.08% |
| 3 | 2-0 | 8.06% |
| 4 | 1-0 | 7.88% |
| 5 | 3-1 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 54.3% | 56.6% | 1.74 | -5.5% |
| Draw | 22.1% | 20.7% | 4.52 | -0.3% |
| Strasbourg win | 23.6% | 22.8% | 4.58 | +8.1% |

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
| Market best home last update utc | 2026-10-18T14:34:32Z |
| Market best draw last update utc | 2026-10-18T14:34:32Z |
| Market best away last update utc | 2026-10-18T14:34:32Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9037 |
| Dc lambda away | 1.2513 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:59.671092+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.03 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.87 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.60 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.67 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.4% |
| P draw away | 45.7% |
| P home away | 77.9% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.68 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:34Z |
| Market reference home last update utc | 2026-10-18T14:34:34Z |
| Market reference draw last update utc | 2026-10-18T14:34:34Z |
| Market reference away last update utc | 2026-10-18T14:34:34Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-18T14:33:33Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:33:33Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0449 |
| Raw ev home | -0.0939 |
| Raw edge prob draw | 0.0277 |
| Raw ev draw | 0.0600 |
| Raw edge prob away | 0.0172 |
| Raw ev away | 0.1208 |

</details>


---
