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
| Training sha256 | 5e16013120ca372a3037818b428b60c70af68d8797a577f6688a132e0f2a0019 |
| Training as of utc | 2026-10-20T05:42:39.181052+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:42:39.181052+00:00', 'observations': 88, 'observations_sha256': '1158af74fef245f5b1f516df4ca2a4ac866c48e45ed3fcf2f8df329913bd4056', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 45, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'ce4bdb8aafa21d81f4e4ec2f2327663cf03f9758992482fd858acc0bb6d334c4', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 4823.299 |
| Base scoring parameter | 0.234 |
| Home-advantage parameter | 0.237 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261020T054239181052Z_95090a2e5f0297eb71e55a191b53420a691affdf32aea25b75925fd8a89743fd.json |
| Over 1 5 in window quote fixtures | 0 |
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

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **64.5%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.45 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.7%; Under 3.5 goals: 53.8%; Double Chance 1X: 83.0%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 81.5%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 64.5% | 1.55 |
| Draw | 18.5% | 5.40 |
| Borussia Monchengladbach win | 17.0% | 5.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.45 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.91% |
| 2 | 2-0 | 8.47% |
| 3 | 1-1 | 8.11% |
| 4 | 3-1 | 7.88% |
| 5 | 1-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 64.5% | 72.5% | 1.43 | -7.8% |
| Draw | 18.5% | 14.7% | 5.87 | +8.7% |
| Borussia Monchengladbach win | 17.0% | 12.8% | 7.02 | +19.3% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.19 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.93 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.61 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 83.0% |
| P draw away | 35.5% |
| P home away | 81.5% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.35 |
| Reference draw odds | 6.00 |
| Reference away odds | 6.80 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:14Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:14Z |
| Home probability edge | -8.0% |
| Draw probability edge | +3.8% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -8.0% |
| Under 2.5 probability edge | +8.0% |
| Raw edge prob home | -0.1604 |
| Raw ev home | -0.1925 |
| Raw edge prob draw | 0.0770 |
| Raw ev draw | 0.3128 |
| Raw edge prob away | 0.0834 |
| Raw ev away | 0.4861 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.2%**. Expected goals are 1.75 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.3%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.4%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.2% | 1.95 |
| Draw | 25.2% | 3.96 |
| FC Schalke 04 win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.75 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.06% |
| 2 | 1-0 | 9.90% |
| 3 | 2-0 | 9.67% |
| 4 | 2-1 | 9.02% |
| 5 | 0-0 | 7.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.2% | 47.0% | 2.12 | +8.6% |
| Draw | 25.2% | 24.5% | 3.98 | +0.4% |
| FC Schalke 04 win | 23.6% | 28.5% | 3.43 | -19.2% |
| Over 2.5 | 50.3% | 60.9% | 1.64 | -17.5% |
| Under 2.5 | 49.7% | 39.1% | 2.46 | +22.3% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda away | 0.9332 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.75 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.59 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.47 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 55.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.6% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.4% |
| P draw away | 48.8% |
| P home away | 74.8% |
| Raw p home draw | 81.4% |
| Raw p draw away | 44.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.05 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:30Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:30Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:11Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:11Z |
| Home probability edge | +4.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0845 |
| Raw ev home | 0.1751 |
| Raw edge prob draw | 0.0138 |
| Raw ev draw | 0.0318 |
| Raw edge prob away | -0.0983 |
| Raw ev away | -0.3605 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.7%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.6%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 46.9%; Under 3.5 goals: 75.5%; Double Chance 1X: 73.1%; Double Chance X2: 53.3%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.7% | 2.14 |
| Draw | 26.4% | 3.79 |
| Union Berlin win | 26.9% | 3.72 |

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
| Over 2.5 | 46.9% |
| Under 2.5 | 53.1% |
| Over 3.5 | 24.5% |
| Under 3.5 | 75.5% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.60% |
| 2 | 1-0 | 11.34% |
| 3 | 2-1 | 10.10% |
| 4 | 2-0 | 8.73% |
| 5 | 0-0 | 8.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.7% | 53.7% | 1.90 | -11.3% |
| Draw | 26.4% | 23.1% | 4.21 | +11.2% |
| Union Berlin win | 26.9% | 23.1% | 3.98 | +7.1% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3431 |
| Dc lambda away | 1.1558 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.67 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.08 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.87 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.0% |
| P home draw | 73.1% |
| P draw away | 53.3% |
| P home away | 73.6% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.80 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:14Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:14Z |
| Home probability edge | -7.1% |
| Draw probability edge | +3.3% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -17.1% |
| Under 2.5 probability edge | +17.1% |
| Raw edge prob home | -0.1414 |
| Raw ev home | -0.2474 |
| Raw edge prob draw | 0.0657 |
| Raw ev draw | 0.2503 |
| Raw edge prob away | 0.0757 |
| Raw ev away | 0.2216 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.1%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.1%; Under 3.5 goals: 50.3%; Double Chance 1X: 83.8%; Double Chance X2: 34.9%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 69.4%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.1% | 1.54 |
| Draw | 18.7% | 5.35 |
| Eintracht Frankfurt win | 16.2% | 6.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.6% |
| Under 4.5 | 69.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.70% |
| 2 | 1-1 | 8.00% |
| 3 | 2-0 | 7.93% |
| 4 | 3-1 | 7.83% |
| 5 | 3-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.1% | 67.3% | 1.48 | -3.6% |
| Draw | 18.7% | 17.3% | 5.39 | +0.7% |
| Eintracht Frankfurt win | 16.2% | 15.4% | 6.42 | +3.9% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4213 |
| Dc lambda away | 1.2224 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.93 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.99 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.46 |
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
| P home draw | 83.8% |
| P draw away | 34.9% |
| P home away | 81.3% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.0% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.45 |
| Reference draw odds | 5.20 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:15Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:15Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -1.8% |
| Under 2.5 probability edge | +1.8% |
| Raw edge prob home | -0.0438 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0280 |
| Raw ev draw | 0.0823 |
| Raw edge prob away | 0.0158 |
| Raw ev away | 0.0893 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.9%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.9%; Double Chance 1X: 76.9%; Double Chance X2: 47.1%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.9% | 1.89 |
| Draw | 24.0% | 4.16 |
| Werder Bremen win | 23.1% | 4.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 2-1 | 10.31% |
| 3 | 1-0 | 8.95% |
| 4 | 2-0 | 8.89% |
| 5 | 0-0 | 6.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.9% | 56.3% | 1.80 | -4.8% |
| Draw | 24.0% | 21.9% | 4.31 | +3.5% |
| Werder Bremen win | 23.1% | 21.9% | 4.41 | +1.8% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7304 |
| Dc lambda away | 1.1602 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.05 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.97 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 76.9% |
| P draw away | 47.1% |
| P home away | 76.0% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.72 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:15Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:15Z |
| Home probability edge | -3.4% |
| Draw probability edge | +2.2% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0680 |
| Raw ev home | -0.1092 |
| Raw edge prob draw | 0.0434 |
| Raw ev draw | 0.1290 |
| Raw edge prob away | 0.0246 |
| Raw ev away | 0.0724 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **65.3%**. Expected goals are 2.49 for RB Leipzig and 1.47 for Elversberg (3.97 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.6%; Under 3.5 goals: 43.4%; Double Chance 1X: 83.1%; Double Chance X2: 34.7%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 62.7%; BTTS Yes (both teams score): 70.7%; BTTS No (at least one team does not score): 29.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 65.3% | 1.53 |
| Draw | 17.8% | 5.62 |
| Elversberg win | 16.9% | 5.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.49 |
| Elversberg expected goals | 1.47 |
| Expected total goals | 3.97 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.6% |
| Under 1.5 | 8.4% |
| Over 2.5 | 76.6% |
| Under 2.5 | 23.4% |
| Over 3.5 | 56.6% |
| Under 3.5 | 43.4% |
| Over 4.5 | 37.3% |
| Under 4.5 | 62.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.58% |
| 2 | 3-1 | 7.96% |
| 3 | 1-1 | 6.85% |
| 4 | 2-0 | 6.51% |
| 5 | 3-2 | 5.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 65.3% | 71.4% | 1.43 | -6.7% |
| Draw | 17.8% | 15.5% | 5.80 | +3.3% |
| Elversberg win | 16.9% | 13.1% | 6.98 | +18.2% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4941 |
| Dc lambda away | 1.4712 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.7% |
| P btts no | 29.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.26 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.94 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.27 |
| Fair Over 3.5 odds | 1.77 |
| Fair Under 3.5 odds | 2.30 |
| Fair Over 4.5 odds | 2.68 |
| Fair Under 4.5 odds | 1.59 |
| Unadjusted home-win probability | 59.1% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 91.4% |
| Raw p under 3 5 | 44.0% |
| Raw p btts yes | 71.4% |
| P home draw | 83.1% |
| P draw away | 34.7% |
| P home away | 82.2% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.9% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.37 |
| Reference draw odds | 5.70 |
| Reference away odds | 6.70 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.27 |
| Reference Under 2.5 odds | 3.65 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:15Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:15Z |
| Home probability edge | -6.1% |
| Draw probability edge | +2.3% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | +0.1% |
| Under 2.5 probability edge | -0.1% |
| Raw edge prob home | -0.1228 |
| Raw ev home | -0.1546 |
| Raw edge prob draw | 0.0454 |
| Raw ev draw | 0.1644 |
| Raw edge prob away | 0.0774 |
| Raw ev away | 0.4521 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.5%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 86.5%; Over 2.5 goals: 33.2%; Under 3.5 goals: 85.8%; Double Chance 1X: 68.5%; Double Chance X2: 61.5%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 40.2%; BTTS No (at least one team does not score): 59.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.5% | 2.60 |
| Draw | 30.0% | 3.34 |
| Hamburger SV win | 31.5% | 3.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.5% |
| Under 0.5 | 13.5% |
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
| 1 | 1-0 | 14.01% |
| 2 | 0-0 | 13.46% |
| 3 | 1-1 | 13.25% |
| 4 | 0-1 | 11.75% |
| 5 | 2-0 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.5% | 42.6% | 2.31 | -11.0% |
| Draw | 30.0% | 26.0% | 3.94 | +18.1% |
| Hamburger SV win | 31.5% | 31.5% | 3.06 | -3.6% |
| Over 2.5 | 33.2% | 61.8% | 1.64 | -45.6% |
| Under 2.5 | 66.8% | 38.2% | 2.47 | +65.1% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0191 |
| Dc lambda away | 0.9637 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.2% |
| P btts no | 59.8% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.43 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.02 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.05 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.67 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.5% |
| Raw p over 1 5 | 60.4% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 41.0% |
| P home draw | 68.5% |
| P draw away | 61.5% |
| P home away | 70.0% |
| Raw p home draw | 68.5% |
| Raw p draw away | 65.5% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.25 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:30Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:30Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:11Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:11Z |
| Home probability edge | -4.1% |
| Draw probability edge | +4.0% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -28.6% |
| Under 2.5 probability edge | +28.6% |
| Raw edge prob home | -0.0813 |
| Raw ev home | -0.2041 |
| Raw edge prob draw | 0.0803 |
| Raw ev draw | 0.3395 |
| Raw edge prob away | 0.0009 |
| Raw ev away | -0.0346 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.8%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.3%; Under 3.5 goals: 49.1%; Double Chance 1X: 32.2%; Double Chance X2: 85.1%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 14.9% | 6.71 |
| Draw | 17.3% | 5.78 |
| Bayern Munich win | 67.8% | 1.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.3% |
| Under 2.5 | 27.7% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.00% |
| 2 | 1-3 | 8.15% |
| 3 | 0-2 | 8.08% |
| 4 | 1-1 | 7.34% |
| 5 | 0-3 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 14.9% | 12.8% | 7.03 | +4.7% |
| Draw | 17.3% | 14.7% | 5.99 | +3.6% |
| Bayern Munich win | 67.8% | 72.5% | 1.42 | -3.7% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.32 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.43 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.2% |
| P draw away | 85.1% |
| P home away | 82.7% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 6.80 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.23 |
| Reference Under 2.5 odds | 4.10 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:15Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:15Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.6% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0414 |
| Raw ev home | 0.1931 |
| Raw edge prob draw | 0.0524 |
| Raw ev draw | 0.1926 |
| Raw edge prob away | -0.0939 |
| Raw ev away | -0.1037 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.7%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.4%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.3%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.1% | 3.32 |
| Draw | 23.2% | 4.31 |
| Bayer Leverkusen win | 46.7% | 2.14 |

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
| 1 | 1-1 | 9.55% |
| 2 | 1-2 | 8.12% |
| 3 | 2-1 | 7.33% |
| 4 | 2-2 | 6.96% |
| 5 | 1-3 | 5.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.1% | 34.5% | 2.80 | -15.7% |
| Draw | 23.2% | 23.9% | 4.25 | -1.4% |
| Bayer Leverkusen win | 46.7% | 41.6% | 2.39 | +11.6% |

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
| Market best home last update utc | 2026-10-20T05:42:11Z |
| Market best draw last update utc | 2026-10-20T05:42:11Z |
| Market best away last update utc | 2026-10-20T05:42:11Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:42:39.181052+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.72 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.91 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.38 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.6% |
| P home draw | 53.3% |
| P draw away | 69.9% |
| P home away | 76.8% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.75 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:42:30Z |
| Market reference home last update utc | 2026-10-20T05:42:30Z |
| Market reference draw last update utc | 2026-10-20T05:42:30Z |
| Market reference away last update utc | 2026-10-20T05:42:30Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:15Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:15Z |
| Home probability edge | -4.4% |
| Draw probability edge | -0.7% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0880 |
| Raw ev home | -0.2805 |
| Raw edge prob draw | -0.0137 |
| Raw ev draw | -0.0431 |
| Raw edge prob away | 0.1016 |
| Raw ev away | 0.2378 |

</details>


---
