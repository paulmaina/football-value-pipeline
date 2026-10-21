# Bundesliga — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,586 |
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
| Training sha256 | be69da8cd9026762d164248fce7cac589a120bf247c11e41710c7af06f04ec4b |
| Training as of utc | 2026-10-21T09:19:30.333113+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 13, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T09:19:30.333113+00:00', 'observations': 105, 'observations_sha256': 'e09cf5008b98dfa7810e64aebaef1439f8208c0ebae44a30cff33d7dd736a068', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 54, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '1f6ec49777565a6c752cd0bc63faf9c0d96890fc48c41da8a6e94ff6ebb04bf7', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4828.985 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.236 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261021T091930333113Z_f0ed8a7a55c69b96bc773bb8c2b20f655718c99ae18df20dd7ca11b39083670e.json |
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

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **63.9%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.5%; Under 3.5 goals: 53.8%; Double Chance 1X: 82.9%; Double Chance X2: 36.1%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 72.4%; BTTS Yes (both teams score): 64.0%; BTTS No (at least one team does not score): 36.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 63.9% | 1.56 |
| Draw | 19.0% | 5.26 |
| Borussia Monchengladbach win | 17.1% | 5.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.5% |
| Under 2.5 | 31.5% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.6% |
| Under 4.5 | 72.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.81% |
| 2 | 2-0 | 8.40% |
| 3 | 1-1 | 8.33% |
| 4 | 3-1 | 7.81% |
| 5 | 1-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 63.9% | 71.4% | 1.43 | -8.6% |
| Draw | 19.0% | 15.7% | 5.87 | +11.6% |
| Borussia Monchengladbach win | 17.1% | 13.0% | 7.02 | +19.8% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:19:30Z |
| Market best away last update utc | 2026-10-21T09:19:30Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1677 |
| Dc lambda away | 1.2877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.0% |
| P btts no | 36.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.43 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.91 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.18 |
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
| P home draw | 82.9% |
| P draw away | 36.1% |
| P home away | 81.0% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.38 |
| Reference draw odds | 5.87 |
| Reference away odds | 7.02 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -7.4% |
| Draw probability edge | +3.4% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | -0.1487 |
| Raw ev home | -0.1922 |
| Raw edge prob draw | 0.0670 |
| Raw ev draw | 0.3126 |
| Raw edge prob away | 0.0817 |
| Raw ev away | 0.4850 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.2%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.4%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.3%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.2% | 1.95 |
| Draw | 25.1% | 3.98 |
| FC Schalke 04 win | 23.7% | 4.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.00% |
| 2 | 1-0 | 9.86% |
| 3 | 2-0 | 9.66% |
| 4 | 2-1 | 9.00% |
| 5 | 0-0 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.2% | 46.7% | 2.12 | +8.5% |
| Draw | 25.1% | 24.4% | 3.98 | -0.0% |
| FC Schalke 04 win | 23.7% | 28.9% | 3.43 | -18.6% |
| Over 2.5 | 50.4% | 60.5% | 1.64 | -17.4% |
| Under 2.5 | 49.6% | 39.5% | 2.46 | +22.1% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
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
| Dc lambda home | 1.7565 |
| Dc lambda away | 0.9312 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.81 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.13 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.45 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.3% |
| P draw away | 48.8% |
| P home away | 74.9% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.09 |
| Reference draw odds | 3.93 |
| Reference away odds | 3.33 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market best over 2 5 last update utc | 2026-10-21T09:18:49Z |
| Market best under 2 5 last update utc | 2026-10-21T09:18:49Z |
| Home probability edge | +4.4% |
| Draw probability edge | +0.8% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0885 |
| Raw ev home | 0.1785 |
| Raw edge prob draw | 0.0151 |
| Raw ev draw | 0.0298 |
| Raw edge prob away | -0.1036 |
| Raw ev away | -0.3642 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.3%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 46.9%; Under 3.5 goals: 75.5%; Double Chance 1X: 72.5%; Double Chance X2: 53.7%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.3% | 2.16 |
| Draw | 26.3% | 3.81 |
| Union Berlin win | 27.5% | 3.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
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
| 1 | 1-1 | 12.53% |
| 2 | 1-0 | 11.23% |
| 3 | 2-1 | 10.01% |
| 4 | 2-0 | 8.66% |
| 5 | 0-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.3% | 53.0% | 1.90 | -12.1% |
| Draw | 26.3% | 22.8% | 4.21 | +10.5% |
| Union Berlin win | 27.5% | 24.2% | 3.98 | +9.3% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.1565 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.75 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.85 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 72.5% |
| P draw away | 53.7% |
| P home away | 73.7% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.85 |
| Reference draw odds | 4.18 |
| Reference away odds | 3.94 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -6.7% |
| Draw probability edge | +3.4% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1336 |
| Raw ev home | -0.2477 |
| Raw edge prob draw | 0.0689 |
| Raw ev draw | 0.2503 |
| Raw edge prob away | 0.0647 |
| Raw ev away | 0.2222 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.7%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 71.0%; Under 3.5 goals: 50.4%; Double Chance 1X: 83.6%; Double Chance X2: 35.3%; Double Chance 12 (either team wins): 81.0%; Under 4.5 goals: 69.5%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.7% | 1.55 |
| Draw | 19.0% | 5.27 |
| Eintracht Frankfurt win | 16.4% | 6.12 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.7% |
| Under 0.5 | 3.3% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 71.0% |
| Under 2.5 | 29.0% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.5% |
| Under 4.5 | 69.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.63% |
| 2 | 1-1 | 8.13% |
| 3 | 2-0 | 7.88% |
| 4 | 3-1 | 7.77% |
| 5 | 3-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.7% | 66.4% | 1.48 | -4.3% |
| Draw | 19.0% | 17.9% | 5.39 | +2.3% |
| Eintracht Frankfurt win | 16.4% | 15.7% | 6.42 | +5.0% |

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
| Market best home last update utc | 2026-10-21T09:19:30Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4204 |
| Dc lambda away | 1.2230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 30.45 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.96 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.44 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.28 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.6% |
| P draw away | 35.3% |
| P home away | 81.0% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.48 |
| Reference draw odds | 5.21 |
| Reference away odds | 5.89 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -1.8% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0350 |
| Raw ev home | -0.0688 |
| Raw edge prob draw | 0.0223 |
| Raw ev draw | 0.0830 |
| Raw edge prob away | 0.0127 |
| Raw ev away | 0.0905 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.6%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.9%; Double Chance 1X: 76.9%; Double Chance X2: 47.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 1.90 |
| Draw | 24.3% | 4.11 |
| Werder Bremen win | 23.1% | 4.33 |

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
| 1 | 1-1 | 11.51% |
| 2 | 2-1 | 10.25% |
| 3 | 1-0 | 8.89% |
| 4 | 2-0 | 8.83% |
| 5 | 0-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 55.7% | 1.80 | -5.4% |
| Draw | 24.3% | 22.5% | 4.31 | +4.9% |
| Werder Bremen win | 23.1% | 21.8% | 4.41 | +1.8% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7300 |
| Dc lambda away | 1.1607 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
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
| P home draw | 76.9% |
| P draw away | 47.4% |
| P home away | 75.7% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.76 |
| Reference draw odds | 4.22 |
| Reference away odds | 4.34 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -3.1% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0620 |
| Raw ev home | -0.1097 |
| Raw edge prob draw | 0.0371 |
| Raw ev draw | 0.1293 |
| Raw edge prob away | 0.0249 |
| Raw ev away | 0.0732 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **67.5%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 76.5%; Under 3.5 goals: 42.9%; Double Chance 1X: 85.3%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 62.5%; BTTS Yes (both teams score): 68.8%; BTTS No (at least one team does not score): 31.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 67.5% | 1.48 |
| Draw | 17.9% | 5.60 |
| Elversberg win | 14.7% | 6.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.69 |
| Elversberg expected goals | 1.32 |
| Expected total goals | 4.01 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.5% |
| Under 2.5 | 23.5% |
| Over 3.5 | 57.1% |
| Under 3.5 | 42.9% |
| Over 4.5 | 37.5% |
| Under 4.5 | 62.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.90% |
| 2 | 3-1 | 7.97% |
| 3 | 1-1 | 7.01% |
| 4 | 2-0 | 6.73% |
| 5 | 3-0 | 6.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 67.5% | 69.3% | 1.43 | -3.5% |
| Draw | 17.9% | 17.5% | 5.80 | +3.6% |
| Elversberg win | 14.7% | 13.3% | 6.98 | +2.3% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6870 |
| Dc lambda away | 1.3218 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.8% |
| P btts no | 31.2% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.38 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.07 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.26 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.67 |
| Fair Under 4.5 odds | 1.60 |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.1% |
| P home draw | 85.3% |
| P draw away | 32.5% |
| P home away | 82.1% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.42 |
| Reference draw odds | 5.30 |
| Reference away odds | 6.90 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.0362 |
| Raw ev home | -0.0609 |
| Raw edge prob draw | 0.0080 |
| Raw ev draw | 0.0592 |
| Raw edge prob away | 0.0282 |
| Raw ev away | 0.1215 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.7%**. Expected goals are 1.01 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.1%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 33.1%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.4%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 70.3%; Under 4.5 goals: 94.7%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.7% | 2.58 |
| Draw | 29.7% | 3.37 |
| Hamburger SV win | 31.6% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.01 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.6% |
| Under 1.5 | 39.4% |
| Over 2.5 | 33.1% |
| Under 2.5 | 66.9% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.3% |
| Under 4.5 | 94.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.15% |
| 2 | 0-0 | 13.38% |
| 3 | 1-1 | 13.09% |
| 4 | 0-1 | 11.84% |
| 5 | 2-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.7% | 43.1% | 2.31 | -10.6% |
| Draw | 29.7% | 25.3% | 3.94 | +16.9% |
| Hamburger SV win | 31.6% | 31.6% | 3.05 | -3.5% |
| Over 2.5 | 33.1% | 60.5% | 1.64 | -45.7% |
| Under 2.5 | 66.9% | 39.5% | 2.47 | +65.2% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:19:30Z |
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
| Dc lambda home | 1.0136 |
| Dc lambda away | 0.9630 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.48 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.02 |
| Fair Under 2.5 odds | 1.49 |
| Fair Over 3.5 odds | 7.10 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.79 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 34.1% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.4% |
| P draw away | 61.3% |
| P home away | 70.3% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.7% |
| Raw p home away | 65.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.26 |
| Reference draw odds | 3.79 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market best over 2 5 last update utc | 2026-10-21T09:18:49Z |
| Market best under 2 5 last update utc | 2026-10-21T09:18:49Z |
| Home probability edge | -4.4% |
| Draw probability edge | +4.4% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -27.4% |
| Under 2.5 probability edge | +27.4% |
| Raw edge prob home | -0.0880 |
| Raw ev home | -0.2077 |
| Raw edge prob draw | 0.0879 |
| Raw ev draw | 0.3421 |
| Raw edge prob away | 0.0001 |
| Raw ev away | -0.0351 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **66.9%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.2%; Under 3.5 goals: 49.2%; Double Chance 1X: 33.1%; Double Chance X2: 84.6%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.4% | 6.47 |
| Draw | 17.6% | 5.68 |
| Bayern Munich win | 66.9% | 1.49 |

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
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.87% |
| 2 | 1-3 | 8.05% |
| 3 | 0-2 | 7.97% |
| 4 | 1-1 | 7.47% |
| 5 | 0-3 | 6.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.4% | 13.9% | 7.03 | +8.6% |
| Draw | 17.6% | 15.3% | 5.99 | +5.5% |
| Bayern Munich win | 66.9% | 70.8% | 1.42 | -4.9% |

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
| Market best home last update utc | 2026-10-21T09:18:49Z |
| Market best draw last update utc | 2026-10-21T09:19:30Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2379 |
| Dc lambda away | 2.4470 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.71 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.40 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.59 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.16 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 33.1% |
| P draw away | 84.6% |
| P home away | 82.4% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.56 |
| Reference draw odds | 5.99 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.3% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -5.8% |
| Under 2.5 probability edge | +5.8% |
| Raw edge prob home | 0.0308 |
| Raw ev home | 0.1940 |
| Raw edge prob draw | 0.0462 |
| Raw ev draw | 0.1928 |
| Raw edge prob away | -0.0769 |
| Raw ev away | -0.1040 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.8%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.5%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.2%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 69.8%; BTTS Yes (both teams score): 70.0%; BTTS No (at least one team does not score): 30.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 3.31 |
| Draw | 23.0% | 4.34 |
| Bayer Leverkusen win | 46.8% | 2.14 |

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
| Over 2.5 | 70.5% |
| Under 2.5 | 29.5% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.2% |
| Under 4.5 | 69.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.48% |
| 2 | 1-2 | 8.13% |
| 3 | 2-1 | 7.35% |
| 4 | 2-2 | 6.91% |
| 5 | 1-3 | 5.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.2% | 34.7% | 2.79 | -15.7% |
| Draw | 23.0% | 23.5% | 4.25 | -2.1% |
| Bayer Leverkusen win | 46.8% | 41.8% | 2.39 | +11.8% |

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
| Market best home last update utc | 2026-10-21T09:19:30Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5010 |
| Dc lambda away | 2.1589 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.0% |
| P btts no | 30.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.93 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.92 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.39 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.31 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.2% |
| P draw away | 69.8% |
| P home away | 77.0% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.79 |
| Reference draw odds | 4.06 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | -4.5% |
| Draw probability edge | -0.5% |
| Away probability edge | +5.0% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0897 |
| Raw ev home | -0.2826 |
| Raw edge prob draw | -0.0103 |
| Raw ev draw | -0.0430 |
| Raw edge prob away | 0.1000 |
| Raw ev away | 0.2373 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **38.9%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 67.1%; Under 3.5 goals: 54.6%; Double Chance 1X: 61.1%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 73.3%; BTTS Yes (both teams score): 68.6%; BTTS No (at least one team does not score): 31.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 36.5% | 2.74 |
| Draw | 24.6% | 4.07 |
| FSV Mainz 05 win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.1% |
| Under 2.5 | 32.9% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.7% |
| Under 4.5 | 73.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.50% |
| 2 | 1-2 | 9.15% |
| 3 | 2-1 | 7.16% |
| 4 | 2-2 | 7.04% |
| 5 | 0-1 | 4.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 36.5% | 27.9% | 3.38 | +23.4% |
| Draw | 24.6% | 25.1% | 4.07 | +0.0% |
| FSV Mainz 05 win | 38.9% | 47.1% | 2.13 | -17.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | b275fe870ec88a9f0054c9220beb2673 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T09:19:30Z |
| Market best draw last update utc | 2026-10-21T09:18:49Z |
| Market best away last update utc | 2026-10-21T09:18:49Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9121 |
| Dc lambda away | 1.5590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T09:19:30.333113+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.6% |
| P btts no | 31.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.70 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.68 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.04 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.75 |
| Fair Under 4.5 odds | 1.36 |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 61.1% |
| P draw away | 63.5% |
| P home away | 75.4% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.38 |
| Reference draw odds | 3.74 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-21T09:19:30Z |
| Market reference home last update utc | 2026-10-21T09:19:30Z |
| Market reference draw last update utc | 2026-10-21T09:19:30Z |
| Market reference away last update utc | 2026-10-21T09:19:30Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T09:19:30Z |
| Market reference under 2 5 last update utc | 2026-10-21T09:19:30Z |
| Home probability edge | +8.7% |
| Draw probability edge | -0.5% |
| Away probability edge | -8.2% |
| Over 2.5 probability edge | +3.3% |
| Under 2.5 probability edge | -3.3% |
| Raw edge prob home | 0.1732 |
| Raw ev home | 0.5272 |
| Raw edge prob draw | -0.0095 |
| Raw ev draw | -0.0189 |
| Raw edge prob away | -0.1638 |
| Raw ev away | -0.3459 |

</details>


---
