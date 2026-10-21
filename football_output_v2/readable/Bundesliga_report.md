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
| Training as of utc | 2026-10-21T10:37:36.874560+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 13, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T10:37:36.874560+00:00', 'observations': 105, 'observations_sha256': 'e09cf5008b98dfa7810e64aebaef1439f8208c0ebae44a30cff33d7dd736a068', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 54, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '1f6ec49777565a6c752cd0bc63faf9c0d96890fc48c41da8a6e94ff6ebb04bf7', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
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
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261021T103736874560Z_6943151cc6e9ef1c71f3700989729bbd0f81bb8ed82f1167c90c325155334b29.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **63.2%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 68.2%; Under 3.5 goals: 53.9%; Double Chance 1X: 82.9%; Double Chance X2: 36.8%; Double Chance 12 (either team wins): 80.3%; Under 4.5 goals: 72.6%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 63.2% | 1.58 |
| Draw | 19.7% | 5.07 |
| Borussia Monchengladbach win | 17.1% | 5.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 68.2% |
| Under 2.5 | 31.8% |
| Over 3.5 | 46.1% |
| Under 3.5 | 53.9% |
| Over 4.5 | 27.4% |
| Under 4.5 | 72.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.68% |
| 2 | 1-1 | 8.65% |
| 3 | 2-0 | 8.30% |
| 4 | 3-1 | 7.72% |
| 5 | 1-0 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 63.2% | 69.8% | 1.43 | -9.7% |
| Draw | 19.7% | 17.1% | 5.87 | +15.9% |
| Borussia Monchengladbach win | 17.1% | 13.1% | 7.02 | +20.1% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:37:14Z |
| Market best away last update utc | 2026-10-21T10:37:14Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1676 |
| Dc lambda away | 1.2877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.38 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.87 |
| Fair Over 2.5 odds | 1.47 |
| Fair Under 2.5 odds | 3.15 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.65 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 82.9% |
| P draw away | 36.8% |
| P home away | 80.3% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.43 |
| Reference draw odds | 5.80 |
| Reference away odds | 7.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -6.7% |
| Draw probability edge | +2.6% |
| Away probability edge | +4.1% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.1335 |
| Raw ev home | -0.1923 |
| Raw edge prob draw | 0.0524 |
| Raw ev draw | 0.3126 |
| Raw edge prob away | 0.0810 |
| Raw ev away | 0.4850 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.4%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.4%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.6%; Double Chance X2: 48.6%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.4% | 1.94 |
| Draw | 25.2% | 3.97 |
| FC Schalke 04 win | 23.4% | 4.28 |

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
| 1 | 1-1 | 12.05% |
| 2 | 1-0 | 9.91% |
| 3 | 2-0 | 9.71% |
| 4 | 2-1 | 9.04% |
| 5 | 0-0 | 7.83% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.4% | 47.3% | 2.12 | +9.0% |
| Draw | 25.2% | 24.5% | 3.98 | +0.3% |
| FC Schalke 04 win | 23.4% | 28.2% | 3.43 | -19.9% |
| Over 2.5 | 50.4% | 60.8% | 1.64 | -17.4% |
| Under 2.5 | 49.6% | 39.2% | 2.46 | +22.1% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
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
| Dc lambda away | 0.9311 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.77 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.45 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.6% |
| P draw away | 48.6% |
| P home away | 74.8% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.08 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.39 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:17Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:17Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | +4.2% |
| Draw probability edge | +0.7% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -10.4% |
| Under 2.5 probability edge | +10.4% |
| Raw edge prob home | 0.0831 |
| Raw ev home | 0.1785 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | 0.0298 |
| Raw edge prob away | -0.0964 |
| Raw ev away | -0.3642 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **45.6%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 46.8%; Under 3.5 goals: 75.5%; Double Chance 1X: 72.2%; Double Chance X2: 54.4%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.3%; BTTS No (at least one team does not score): 48.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 45.6% | 2.19 |
| Draw | 26.5% | 3.77 |
| Union Berlin win | 27.8% | 3.59 |

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
| 1 | 1-1 | 12.67% |
| 2 | 1-0 | 11.07% |
| 3 | 2-1 | 9.87% |
| 4 | 0-0 | 8.61% |
| 5 | 2-0 | 8.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 45.6% | 51.6% | 1.88 | -14.2% |
| Draw | 26.5% | 23.4% | 4.26 | +13.1% |
| Union Berlin win | 27.8% | 25.0% | 4.01 | +11.6% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
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
| Dc lambda away | 1.1565 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.3% |
| P btts no | 48.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.62 |
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
| Raw p btts yes | 52.1% |
| P home draw | 72.2% |
| P draw away | 54.4% |
| P home away | 73.5% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.90 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -6.0% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -17.0% |
| Under 2.5 probability edge | +17.0% |
| Raw edge prob home | -0.1205 |
| Raw ev home | -0.2557 |
| Raw edge prob draw | 0.0630 |
| Raw ev draw | 0.2652 |
| Raw edge prob away | 0.0575 |
| Raw ev away | 0.2314 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.2%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 96.7%; Over 2.5 goals: 70.8%; Under 3.5 goals: 50.4%; Double Chance 1X: 83.5%; Double Chance X2: 35.8%; Double Chance 12 (either team wins): 80.7%; Under 4.5 goals: 69.6%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.2% | 1.56 |
| Draw | 19.3% | 5.19 |
| Eintracht Frankfurt win | 16.5% | 6.07 |

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
| Over 2.5 | 70.8% |
| Under 2.5 | 29.2% |
| Over 3.5 | 49.6% |
| Under 3.5 | 50.4% |
| Over 4.5 | 30.4% |
| Under 4.5 | 69.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.57% |
| 2 | 1-1 | 8.26% |
| 3 | 2-0 | 7.82% |
| 4 | 3-1 | 7.72% |
| 5 | 3-0 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.2% | 65.6% | 1.48 | -4.9% |
| Draw | 19.3% | 18.5% | 5.39 | +3.9% |
| Eintracht Frankfurt win | 16.5% | 16.0% | 6.42 | +5.7% |

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
| Market best home last update utc | 2026-10-21T10:37:14Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4207 |
| Dc lambda away | 1.2229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.97 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.94 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.43 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.29 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.5% |
| P draw away | 35.8% |
| P home away | 80.7% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.51 |
| Reference draw odds | 5.20 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.0264 |
| Raw ev home | -0.0686 |
| Raw edge prob draw | 0.0161 |
| Raw ev draw | 0.0828 |
| Raw edge prob away | 0.0102 |
| Raw ev away | 0.0902 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.6%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.9%; Double Chance 1X: 77.2%; Double Chance X2: 47.4%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 83.0%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 1.90 |
| Draw | 24.5% | 4.08 |
| Werder Bremen win | 22.8% | 4.38 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.1% |
| Under 3.5 | 66.9% |
| Over 4.5 | 17.0% |
| Under 4.5 | 83.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.60% |
| 2 | 2-1 | 10.26% |
| 3 | 1-0 | 8.90% |
| 4 | 2-0 | 8.84% |
| 5 | 0-0 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.6% | 55.8% | 1.80 | -5.3% |
| Draw | 24.5% | 22.9% | 4.31 | +5.7% |
| Werder Bremen win | 22.8% | 21.3% | 4.41 | +0.7% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7299 |
| Dc lambda away | 1.1607 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.72 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.96 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.89 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.2% |
| P draw away | 47.4% |
| P home away | 75.5% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.78 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -7.9% |
| Under 2.5 probability edge | +7.9% |
| Raw edge prob home | -0.0633 |
| Raw ev home | -0.1097 |
| Raw edge prob draw | 0.0335 |
| Raw ev draw | 0.1293 |
| Raw edge prob away | 0.0299 |
| Raw ev away | 0.0732 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **67.7%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.6%; Under 3.5 goals: 42.9%; Double Chance 1X: 85.2%; Double Chance X2: 32.3%; Double Chance 12 (either team wins): 82.5%; Under 4.5 goals: 62.4%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 67.7% | 1.48 |
| Draw | 17.5% | 5.72 |
| Elversberg win | 14.8% | 6.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.69 |
| Elversberg expected goals | 1.32 |
| Expected total goals | 4.01 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.6% |
| Under 2.5 | 23.4% |
| Over 3.5 | 57.1% |
| Under 3.5 | 42.9% |
| Over 4.5 | 37.6% |
| Under 4.5 | 62.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.93% |
| 2 | 3-1 | 8.00% |
| 3 | 1-1 | 6.86% |
| 4 | 2-0 | 6.76% |
| 5 | 3-0 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 67.7% | 69.7% | 1.43 | -3.2% |
| Draw | 17.5% | 16.7% | 5.80 | +1.5% |
| Elversberg win | 14.8% | 13.5% | 6.98 | +3.3% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6862 |
| Dc lambda away | 1.3216 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.20 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.09 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.28 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.66 |
| Fair Under 4.5 odds | 1.60 |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.0% |
| P home draw | 85.2% |
| P draw away | 32.3% |
| P home away | 82.5% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.42 |
| Reference draw odds | 5.70 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0408 |
| Raw ev home | -0.0610 |
| Raw edge prob draw | 0.0155 |
| Raw ev draw | 0.0595 |
| Raw edge prob away | 0.0253 |
| Raw ev away | 0.1217 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.4%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 33.1%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.2%; Double Chance X2: 61.6%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 94.7%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.4% | 2.61 |
| Draw | 29.9% | 3.35 |
| Hamburger SV win | 31.8% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.1% |
| Under 2.5 | 66.9% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.3% |
| Under 4.5 | 94.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.01% |
| 2 | 0-0 | 13.45% |
| 3 | 1-1 | 13.17% |
| 4 | 0-1 | 11.88% |
| 5 | 2-0 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.4% | 42.4% | 2.31 | -11.4% |
| Draw | 29.9% | 25.7% | 3.94 | +17.6% |
| Hamburger SV win | 31.8% | 31.9% | 3.05 | -3.1% |
| Over 2.5 | 33.1% | 61.8% | 1.64 | -45.7% |
| Under 2.5 | 66.9% | 38.2% | 2.47 | +65.3% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:37:14Z |
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
| Dc lambda home | 1.0150 |
| Dc lambda away | 0.9632 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.44 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.02 |
| Fair Under 2.5 odds | 1.49 |
| Fair Over 3.5 odds | 7.09 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.78 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.3% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.2% |
| P draw away | 61.6% |
| P home away | 70.1% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.7% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.34 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.10 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:13Z |
| Market best over 2 5 last update utc | 2026-10-21T10:36:31Z |
| Market best under 2 5 last update utc | 2026-10-21T10:36:31Z |
| Home probability edge | -4.0% |
| Draw probability edge | +4.2% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -28.7% |
| Under 2.5 probability edge | +28.7% |
| Raw edge prob home | -0.0807 |
| Raw ev home | -0.2067 |
| Raw edge prob draw | 0.0839 |
| Raw ev draw | 0.3414 |
| Raw edge prob away | -0.0032 |
| Raw ev away | -0.0358 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.1%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.0%; Over 2.5 goals: 72.1%; Under 3.5 goals: 49.2%; Double Chance 1X: 32.9%; Double Chance X2: 84.9%; Double Chance 12 (either team wins): 82.2%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.1% | 6.60 |
| Draw | 17.8% | 5.63 |
| Bayern Munich win | 67.1% | 1.49 |

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
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.89% |
| 2 | 1-3 | 8.07% |
| 3 | 0-2 | 7.99% |
| 4 | 1-1 | 7.54% |
| 5 | 0-3 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.1% | 13.3% | 7.03 | +6.5% |
| Draw | 17.8% | 15.6% | 5.99 | +6.4% |
| Bayern Munich win | 67.1% | 71.1% | 1.42 | -4.7% |

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
| Market best home last update utc | 2026-10-21T10:36:31Z |
| Market best draw last update utc | 2026-10-21T10:37:14Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2378 |
| Dc lambda away | 2.4467 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 33.41 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.39 |
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
| P home draw | 32.9% |
| P draw away | 84.9% |
| P home away | 82.2% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 7.00 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.39 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | +1.8% |
| Draw probability edge | +2.2% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0368 |
| Raw ev home | 0.1941 |
| Raw edge prob draw | 0.0430 |
| Raw ev draw | 0.1930 |
| Raw edge prob away | -0.0798 |
| Raw ev away | -0.1040 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.5%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.6%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.4%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.5%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 69.9%; BTTS Yes (both teams score): 70.1%; BTTS No (at least one team does not score): 29.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.1% | 3.32 |
| Draw | 23.4% | 4.28 |
| Bayer Leverkusen win | 46.5% | 2.15 |

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
| Over 4.5 | 30.1% |
| Under 4.5 | 69.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.62% |
| 2 | 1-2 | 8.08% |
| 3 | 2-1 | 7.34% |
| 4 | 2-2 | 7.02% |
| 5 | 1-3 | 5.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.1% | 34.6% | 2.79 | -15.9% |
| Draw | 23.4% | 24.3% | 4.25 | -0.6% |
| Bayer Leverkusen win | 46.5% | 41.2% | 2.39 | +11.1% |

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
| Market best home last update utc | 2026-10-21T10:37:14Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 2.1590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 70.1% |
| P btts no | 29.9% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.51 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.90 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.37 |
| Fair Over 3.5 odds | 2.03 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.32 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.5% |
| P draw away | 69.9% |
| P home away | 76.6% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.88 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:31Z |
| Market reference home last update utc | 2026-10-21T10:37:31Z |
| Market reference draw last update utc | 2026-10-21T10:37:31Z |
| Market reference away last update utc | 2026-10-21T10:37:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:12Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:12Z |
| Home probability edge | -4.4% |
| Draw probability edge | -0.9% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.0886 |
| Raw ev home | -0.2827 |
| Raw edge prob draw | -0.0173 |
| Raw ev draw | -0.0430 |
| Raw edge prob away | 0.1060 |
| Raw ev away | 0.2374 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **38.8%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 67.3%; Under 3.5 goals: 54.6%; Double Chance 1X: 61.2%; Double Chance X2: 62.8%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 73.2%; BTTS Yes (both teams score): 68.5%; BTTS No (at least one team does not score): 31.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 37.2% | 2.69 |
| Draw | 24.0% | 4.17 |
| FSV Mainz 05 win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.3% |
| Under 2.5 | 32.7% |
| Over 3.5 | 45.4% |
| Under 3.5 | 54.6% |
| Over 4.5 | 26.8% |
| Under 4.5 | 73.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.24% |
| 2 | 1-2 | 9.12% |
| 3 | 2-1 | 7.30% |
| 4 | 2-2 | 6.87% |
| 5 | 0-1 | 4.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 37.2% | 29.3% | 3.38 | +25.9% |
| Draw | 24.0% | 23.8% | 4.07 | -2.4% |
| FSV Mainz 05 win | 38.8% | 46.9% | 2.13 | -17.4% |

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
| Market best home last update utc | 2026-10-21T10:37:14Z |
| Market best draw last update utc | 2026-10-21T10:36:31Z |
| Market best away last update utc | 2026-10-21T10:36:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9116 |
| Dc lambda away | 1.5585 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T10:37:36.874560+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.5% |
| P btts no | 31.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.28 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.70 |
| Fair Over 2.5 odds | 1.49 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.74 |
| Fair Under 4.5 odds | 1.37 |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 61.2% |
| P draw away | 62.8% |
| P home away | 76.0% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.96 |
| Reference away odds | 2.07 |
| Market reference 1x2 last update utc | 2026-10-21T10:37:17Z |
| Market reference home last update utc | 2026-10-21T10:37:17Z |
| Market reference draw last update utc | 2026-10-21T10:37:17Z |
| Market reference away last update utc | 2026-10-21T10:37:17Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-21T10:37:13Z |
| Market reference under 2 5 last update utc | 2026-10-21T10:37:13Z |
| Home probability edge | +7.9% |
| Draw probability edge | +0.1% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | +6.0% |
| Under 2.5 probability edge | -6.0% |
| Raw edge prob home | 0.1589 |
| Raw ev home | 0.5272 |
| Raw edge prob draw | 0.0027 |
| Raw ev draw | -0.0187 |
| Raw edge prob away | -0.1616 |
| Raw ev away | -0.3460 |

</details>


---
