# Bundesliga — football model report

Fixtures in this report: **9**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,584 |
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
| Training sha256 | 6cb95c5c600d1855f907a27a1405e6c738d0a494a972ad102c43d4a319c26eeb |
| Training as of utc | 2026-10-19T16:27:04.716688+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T16:27:04.716688+00:00', 'observations': 81, 'observations_sha256': '001795b9724d2b3dd6eeda93c915544fb67a3643b7d4eadde09b38bb5e41fbd8', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 45, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'e22fb845209f937518918fd0f6c6723231aff91a4a8b75f28d3de6cd7c7500af', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 4823.299 |
| Base scoring parameter | 0.234 |
| Home-advantage parameter | 0.237 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261019T162704716688Z_b272ea748d0261b34673505ecb464b5efa08fdbc9c3c6f0e9697749e1e9b7558.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **64.1%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.45 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.8%; Double Chance 1X: 83.2%; Double Chance X2: 35.9%; Double Chance 12 (either team wins): 80.8%; Under 4.5 goals: 72.5%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 64.1% | 1.56 |
| Draw | 19.2% | 5.22 |
| Borussia Monchengladbach win | 16.8% | 5.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.45 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.5% |
| Under 4.5 | 72.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.84% |
| 2 | 2-0 | 8.42% |
| 3 | 1-1 | 8.39% |
| 4 | 3-1 | 7.83% |
| 5 | 1-0 | 6.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 64.1% | 71.7% | 1.43 | -8.4% |
| Draw | 19.2% | 16.0% | 5.80 | +11.1% |
| Borussia Monchengladbach win | 16.8% | 12.4% | 6.98 | +17.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1668 |
| Dc lambda away | 1.2878 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.21 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.90 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.17 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.63 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 83.2% |
| P draw away | 35.9% |
| P home away | 80.8% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.36 |
| Reference draw odds | 5.45 |
| Reference away odds | 6.90 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -7.6% |
| Draw probability edge | +3.2% |
| Away probability edge | +4.4% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.1522 |
| Raw ev home | -0.1925 |
| Raw edge prob draw | 0.0641 |
| Raw ev draw | 0.2972 |
| Raw edge prob away | 0.0881 |
| Raw ev away | 0.4776 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.5%**. Expected goals are 1.75 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.2%; Under 3.5 goals: 72.1%; Double Chance 1X: 77.0%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.6%; BTTS No (at least one team does not score): 48.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.5% | 1.94 |
| Draw | 25.5% | 3.92 |
| FC Schalke 04 win | 23.0% | 4.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.75 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.18% |
| 2 | 1-0 | 9.95% |
| 3 | 2-0 | 9.72% |
| 4 | 2-1 | 9.07% |
| 5 | 0-0 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.5% | 47.5% | 2.12 | +9.1% |
| Draw | 25.5% | 25.1% | 3.98 | +1.5% |
| FC Schalke 04 win | 23.0% | 27.4% | 3.43 | -21.0% |
| Over 2.5 | 50.2% | 60.3% | 1.64 | -17.6% |
| Under 2.5 | 49.8% | 39.7% | 2.46 | +22.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7519 |
| Dc lambda away | 0.9338 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.6% |
| P btts no | 48.4% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.63 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.48 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 55.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.7% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 77.0% |
| P draw away | 48.5% |
| P home away | 74.5% |
| Raw p home draw | 81.3% |
| Raw p draw away | 44.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.02 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market best over 2 5 last update utc | 2026-10-19T16:26:05Z |
| Market best under 2 5 last update utc | 2026-10-19T16:26:05Z |
| Home probability edge | +3.9% |
| Draw probability edge | +0.4% |
| Away probability edge | -4.4% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0788 |
| Raw ev home | 0.1748 |
| Raw edge prob draw | 0.0087 |
| Raw ev draw | 0.0318 |
| Raw edge prob away | -0.0875 |
| Raw ev away | -0.3600 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.3%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 46.8%; Under 3.5 goals: 75.5%; Double Chance 1X: 72.7%; Double Chance X2: 53.7%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.3% | 2.16 |
| Draw | 26.5% | 3.78 |
| Union Berlin win | 27.3% | 3.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 73.0% |
| Under 1.5 | 27.0% |
| Over 2.5 | 46.8% |
| Under 2.5 | 53.2% |
| Over 3.5 | 24.5% |
| Under 3.5 | 75.5% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.63% |
| 2 | 1-0 | 11.24% |
| 3 | 2-1 | 10.01% |
| 4 | 2-0 | 8.66% |
| 5 | 0-0 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.3% | 52.9% | 1.90 | -12.1% |
| Draw | 26.5% | 23.2% | 4.21 | +11.4% |
| Union Berlin win | 27.3% | 23.9% | 3.98 | +8.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.1558 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.65 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.08 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 8.88 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.0% |
| P home draw | 72.7% |
| P draw away | 53.7% |
| P home away | 73.5% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.82 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.52 |
| Reference Under 2.5 odds | 2.56 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -6.7% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -16.8% |
| Under 2.5 probability edge | +16.8% |
| Raw edge prob home | -0.1330 |
| Raw ev home | -0.2474 |
| Raw edge prob draw | 0.0647 |
| Raw ev draw | 0.2502 |
| Raw edge prob away | 0.0683 |
| Raw ev away | 0.2216 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.0%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.3%; Double Chance 1X: 84.0%; Double Chance X2: 35.0%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.0% | 1.54 |
| Draw | 19.0% | 5.26 |
| Eintracht Frankfurt win | 16.0% | 6.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.68% |
| 2 | 1-1 | 8.14% |
| 3 | 2-0 | 7.92% |
| 4 | 3-1 | 7.81% |
| 5 | 3-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.0% | 67.1% | 1.48 | -3.8% |
| Draw | 19.0% | 17.9% | 5.39 | +2.4% |
| Eintracht Frankfurt win | 16.0% | 15.0% | 6.42 | +2.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4215 |
| Dc lambda away | 1.2225 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.41 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.97 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.44 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.27 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.1% |
| P home draw | 84.0% |
| P draw away | 35.0% |
| P home away | 81.0% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.0% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.45 |
| Reference draw odds | 4.95 |
| Reference away odds | 5.85 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.31 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -2.1% |
| Draw probability edge | +1.1% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0413 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0215 |
| Raw ev draw | 0.0822 |
| Raw edge prob away | 0.0198 |
| Raw ev away | 0.0892 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.8%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.9%; Double Chance 1X: 77.1%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.8% | 1.89 |
| Draw | 24.4% | 4.11 |
| Werder Bremen win | 22.9% | 4.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 2-1 | 10.29% |
| 3 | 1-0 | 8.93% |
| 4 | 2-0 | 8.87% |
| 5 | 0-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.8% | 56.1% | 1.80 | -5.0% |
| Draw | 24.4% | 22.5% | 4.31 | +5.0% |
| Werder Bremen win | 22.9% | 21.4% | 4.41 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7304 |
| Dc lambda away | 1.1601 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.84 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.96 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.88 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.1% |
| P draw away | 47.2% |
| P home away | 75.6% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.72 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.49 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -3.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0661 |
| Raw ev home | -0.1092 |
| Raw edge prob draw | 0.0368 |
| Raw ev draw | 0.1290 |
| Raw edge prob away | 0.0293 |
| Raw ev away | 0.0723 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **64.9%**. Expected goals are 2.49 for RB Leipzig and 1.47 for Elversberg (3.97 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.4%; Under 3.5 goals: 43.4%; Double Chance 1X: 83.3%; Double Chance X2: 35.1%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 62.9%; BTTS Yes (both teams score): 70.8%; BTTS No (at least one team does not score): 29.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 64.9% | 1.54 |
| Draw | 18.4% | 5.42 |
| Elversberg win | 16.7% | 5.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.49 |
| Elversberg expected goals | 1.47 |
| Expected total goals | 3.97 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.6% |
| Under 1.5 | 8.4% |
| Over 2.5 | 76.4% |
| Under 2.5 | 23.6% |
| Over 3.5 | 56.6% |
| Under 3.5 | 43.4% |
| Over 4.5 | 37.1% |
| Under 4.5 | 62.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.52% |
| 2 | 3-1 | 7.91% |
| 3 | 1-1 | 7.10% |
| 4 | 2-0 | 6.47% |
| 5 | 2-2 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 64.9% | 70.6% | 1.43 | -7.2% |
| Draw | 18.4% | 16.8% | 5.80 | +7.0% |
| Elversberg win | 16.7% | 12.6% | 6.98 | +16.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4946 |
| Dc lambda away | 1.4710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.8% |
| P btts no | 29.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.80 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.89 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.23 |
| Fair Over 3.5 odds | 1.77 |
| Fair Under 3.5 odds | 2.30 |
| Fair Over 4.5 odds | 2.69 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 59.1% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 91.4% |
| Raw p under 3 5 | 44.0% |
| Raw p btts yes | 71.4% |
| P home draw | 83.3% |
| P draw away | 35.1% |
| P home away | 81.6% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.9% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 1.38 |
| Reference draw odds | 5.20 |
| Reference away odds | 6.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.72 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -5.7% |
| Draw probability edge | +1.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.1146 |
| Raw ev home | -0.1544 |
| Raw edge prob draw | 0.0325 |
| Raw ev draw | 0.1642 |
| Raw edge prob away | 0.0821 |
| Raw ev away | 0.4516 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.7%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.8%; Double Chance 1X: 68.6%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 40.2%; BTTS No (at least one team does not score): 59.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.7% | 2.58 |
| Draw | 29.9% | 3.35 |
| Hamburger SV win | 31.4% | 3.19 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.8% |
| Under 1.5 | 39.2% |
| Over 2.5 | 33.2% |
| Under 2.5 | 66.8% |
| Over 3.5 | 14.2% |
| Under 3.5 | 85.8% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.07% |
| 2 | 0-0 | 13.41% |
| 3 | 1-1 | 13.21% |
| 4 | 0-1 | 11.70% |
| 5 | 2-0 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.7% | 43.0% | 2.31 | -10.5% |
| Draw | 29.9% | 25.8% | 3.94 | +17.7% |
| Hamburger SV win | 31.4% | 31.3% | 3.04 | -4.6% |
| Over 2.5 | 33.2% | 60.3% | 1.64 | -45.5% |
| Under 2.5 | 66.8% | 39.7% | 2.47 | +64.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0203 |
| Dc lambda away | 0.9638 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.2% |
| P btts no | 59.8% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.46 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.04 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.60 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 60.5% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 41.1% |
| P home draw | 68.6% |
| P draw away | 61.3% |
| P home away | 70.1% |
| Raw p home draw | 68.5% |
| Raw p draw away | 65.5% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.22 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market best over 2 5 last update utc | 2026-10-19T16:26:05Z |
| Market best under 2 5 last update utc | 2026-10-19T16:26:05Z |
| Home probability edge | -4.2% |
| Draw probability edge | +4.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -27.1% |
| Under 2.5 probability edge | +27.1% |
| Raw edge prob home | -0.0849 |
| Raw ev home | -0.2032 |
| Raw edge prob draw | 0.0822 |
| Raw ev draw | 0.3389 |
| Raw edge prob away | 0.0028 |
| Raw ev away | -0.0416 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **68.0%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.2%; Under 3.5 goals: 49.1%; Double Chance 1X: 32.0%; Double Chance X2: 85.5%; Double Chance 12 (either team wins): 82.5%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 14.5% | 6.88 |
| Draw | 17.5% | 5.71 |
| Bayern Munich win | 68.0% | 1.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.0% |
| Under 0.5 | 3.0% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.2% |
| Under 2.5 | 27.8% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.02% |
| 2 | 1-3 | 8.17% |
| 3 | 0-2 | 8.10% |
| 4 | 1-1 | 7.43% |
| 5 | 0-3 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 14.5% | 12.1% | 7.03 | +2.2% |
| Draw | 17.5% | 15.1% | 5.95 | +4.2% |
| Bayern Munich win | 68.0% | 72.8% | 1.42 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2371 |
| Dc lambda away | 2.4469 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.87 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.43 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.60 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.0% |
| P draw away | 85.5% |
| P home away | 82.5% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 7.00 |
| Reference draw odds | 5.70 |
| Reference away odds | 1.34 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 4.05 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | +2.4% |
| Draw probability edge | +2.4% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0488 |
| Raw ev home | 0.1932 |
| Raw edge prob draw | 0.0479 |
| Raw ev draw | 0.1846 |
| Raw edge prob away | -0.0967 |
| Raw ev away | -0.1037 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **47.0%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.4%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.0%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 29.7% | 3.36 |
| Draw | 23.2% | 4.31 |
| Bayer Leverkusen win | 47.0% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.4% |
| Under 2.5 | 29.6% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.56% |
| 2 | 1-2 | 8.18% |
| 3 | 2-1 | 7.24% |
| 4 | 2-2 | 6.96% |
| 5 | 1-3 | 5.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 29.7% | 33.8% | 2.76 | -17.9% |
| Draw | 23.2% | 23.9% | 4.25 | -1.3% |
| Bayer Leverkusen win | 47.0% | 42.3% | 2.39 | +12.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-19T16:26:05Z |
| Market best draw last update utc | 2026-10-19T16:26:05Z |
| Market best away last update utc | 2026-10-19T16:26:05Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5001 |
| Dc lambda away | 2.1590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:27:04.716688+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.70 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.91 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.38 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.6% |
| P home draw | 53.0% |
| P draw away | 70.3% |
| P home away | 76.8% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betsson |
| Reference home odds | 2.78 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-19T16:27:04Z |
| Market reference home last update utc | 2026-10-19T16:27:04Z |
| Market reference draw last update utc | 2026-10-19T16:27:04Z |
| Market reference away last update utc | 2026-10-19T16:27:04Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.07 |
| Market reference over 2 5 last update utc | 2026-10-19T16:27:04Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:27:04Z |
| Home probability edge | -4.0% |
| Draw probability edge | -0.7% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | -0.0809 |
| Raw ev home | -0.2908 |
| Raw edge prob draw | -0.0140 |
| Raw ev draw | -0.0432 |
| Raw edge prob away | 0.0950 |
| Raw ev away | 0.2378 |

</details>


---
