# Premier League — football model report

Fixtures in this report: **11**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,969 |
| Training data through | 2026-10-18 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 86419600d85effc83fdd569a2b0b03458ba1cd4e7b70ce49b60d3c87d9d4e7dc |
| Training as of utc | 2026-10-19T16:25:33.358592+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 69, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 69, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T16:25:33.358592+00:00', 'observations': 96, 'observations_sha256': '67e7a0ebe5508caf5663e4c386e06942fadad59ec55e2b7968c1a901f88cc193', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 52, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '4ef09f78e0e59a69a0e1c8d1f31010b0f7f3615b2b84e65dc1084865f94c4b8f', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 932.574 |
| Base scoring parameter | 0.210 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.090 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261019T162533358592Z_313d7ffe0f051368b2be842f51b24733378e3d7098e1e3e6c9252d36d9f11e2a.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **54.6%**. Expected goals are 1.49 for Tottenham Hotspur and 1.07 for Coventry City (2.56 combined). The most likely exact score is 1-0 at 12.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 48.8%; Under 3.5 goals: 73.9%; Double Chance 1X: 78.9%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 87.7%; BTTS Yes (both teams score): 50.9%; BTTS No (at least one team does not score): 49.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 54.6% | 1.83 |
| Draw | 24.3% | 4.12 |
| Coventry City win | 21.1% | 4.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.49 |
| Coventry City expected goals | 1.07 |
| Expected total goals | 2.56 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 26.1% |
| Under 3.5 | 73.9% |
| Over 4.5 | 12.3% |
| Under 4.5 | 87.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.40% |
| 2 | 1-1 | 11.59% |
| 3 | 2-1 | 10.95% |
| 4 | 2-0 | 10.25% |
| 5 | 0-0 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 54.6% | 63.4% | 1.57 | -14.2% |
| Draw | 24.3% | 20.4% | 4.57 | +10.9% |
| Coventry City win | 21.1% | 16.2% | 6.19 | +30.6% |
| Over 2.5 | 48.8% | 58.9% | 1.65 | -19.5% |
| Under 2.5 | 51.2% | 41.1% | 2.45 | +25.5% |

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
| Market best home last update utc | 2026-10-19T16:24:37Z |
| Market best draw last update utc | 2026-10-19T16:24:37Z |
| Market best away last update utc | 2026-10-19T16:24:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4932 |
| Dc lambda away | 1.0682 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.9% |
| P btts no | 49.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.12 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.87 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.83 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.13 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 45.9% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 26.0% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 74.4% |
| Raw p btts yes | 52.0% |
| P home draw | 78.9% |
| P draw away | 45.4% |
| P home away | 75.7% |
| Raw p home draw | 74.0% |
| Raw p draw away | 54.1% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.60 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.59 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:37Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:37Z |
| Home probability edge | -8.7% |
| Draw probability edge | +3.9% |
| Away probability edge | +4.9% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | -0.1750 |
| Raw ev home | -0.2797 |
| Raw edge prob draw | 0.0771 |
| Raw ev draw | 0.2856 |
| Raw edge prob away | 0.0978 |
| Raw ev away | 0.6088 |
| Market p home draw | 83.9% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-19T16:24:37Z |
| Market reference home draw last update utc | 2026-10-19T16:25:35Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 37.0% |
| Market draw away odds | 2.56 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-19T16:24:37Z |
| Market reference draw away last update utc | 2026-10-19T16:25:35Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.24 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-19T16:24:37Z |
| Market reference home away last update utc | 2026-10-19T16:25:35Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.63 |
| Market reference dc home draw odds | 1.16 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 81.9% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.10 |
| Market reference over 1 5 last update utc | 2026-10-19T16:25:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.2% |
| Market reference under 3 5 odds | 1.47 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-19T16:25:25Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 54.3% |
| Market btts yes odds | 1.66 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-19T16:24:37Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-19T16:25:35Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **43.6%**. Expected goals are 1.32 for Ipswich Town and 1.70 for Nottingham Forest (3.02 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.9%; Under 3.5 goals: 64.3%; Double Chance 1X: 56.4%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.3%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 30.0% | 3.33 |
| Draw | 26.3% | 3.80 |
| Nottingham Forest win | 43.6% | 2.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.70 |
| Expected total goals | 3.02 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 57.9% |
| Under 2.5 | 42.1% |
| Over 3.5 | 35.7% |
| Under 3.5 | 64.3% |
| Over 4.5 | 18.7% |
| Under 4.5 | 81.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 1-2 | 8.94% |
| 3 | 2-1 | 7.52% |
| 4 | 0-1 | 7.01% |
| 5 | 0-2 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 30.0% | 31.2% | 3.10 | -7.0% |
| Draw | 26.3% | 27.0% | 3.63 | -4.4% |
| Nottingham Forest win | 43.6% | 41.9% | 2.39 | +4.3% |
| Over 2.5 | 57.9% | 55.6% | 1.84 | +6.5% |
| Under 2.5 | 42.1% | 44.4% | 2.12 | -10.7% |

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
| Market best home last update utc | 2026-10-19T16:24:37Z |
| Market best draw last update utc | 2026-10-19T16:24:37Z |
| Market best away last update utc | 2026-10-19T16:24:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3206 |
| Dc lambda away | 1.7009 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.65 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.35 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.38 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.35 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 28.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 60.9% |
| P home draw | 56.4% |
| P draw away | 70.0% |
| P home away | 73.7% |
| Raw p home draw | 54.6% |
| Raw p draw away | 71.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 3.05 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.03 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:37Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:37Z |
| Home probability edge | -1.2% |
| Draw probability edge | -0.6% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +2.3% |
| Under 2.5 probability edge | -2.3% |
| Raw edge prob home | -0.0231 |
| Raw ev home | -0.1056 |
| Raw edge prob draw | -0.0127 |
| Raw ev draw | -0.0666 |
| Raw edge prob away | 0.0358 |
| Raw ev away | 0.0859 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.1%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.30 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.5%; Under 3.5 goals: 79.6%; Double Chance 1X: 88.8%; Double Chance X2: 32.9%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.1% | 1.49 |
| Draw | 21.7% | 4.60 |
| Everton win | 11.2% | 8.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.5% |
| Under 2.5 | 58.5% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.09% |
| 2 | 2-0 | 15.52% |
| 3 | 0-0 | 9.67% |
| 4 | 1-1 | 9.61% |
| 5 | 2-1 | 8.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.1% | 69.9% | 1.43 | -4.0% |
| Draw | 21.7% | 18.8% | 4.93 | +7.1% |
| Everton win | 11.2% | 11.2% | 8.90 | -0.8% |
| Over 2.5 | 41.5% | 52.5% | 1.83 | -24.1% |
| Under 2.5 | 58.5% | 47.5% | 2.14 | +25.2% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7214 |
| Dc lambda away | 0.5769 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.34 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.57 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 64.4% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 36.9% |
| P home draw | 88.8% |
| P draw away | 32.9% |
| P home away | 78.3% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.6% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.80 |
| Reference away odds | 7.80 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | -2.8% |
| Draw probability edge | +2.9% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0555 |
| Raw ev home | -0.0797 |
| Raw edge prob draw | 0.0574 |
| Raw ev draw | 0.2121 |
| Raw edge prob away | -0.0019 |
| Raw ev away | -0.0159 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.8%**. Expected goals are 1.12 for Aston Villa and 1.83 for Manchester City (2.96 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.6%; Double Chance 1X: 45.2%; Double Chance X2: 78.5%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.5% | 4.64 |
| Draw | 23.7% | 4.22 |
| Manchester City win | 54.8% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.16% |
| 2 | 1-2 | 10.13% |
| 3 | 0-2 | 9.04% |
| 4 | 0-1 | 8.85% |
| 5 | 1-3 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.5% | 21.0% | 4.72 | +1.7% |
| Draw | 23.7% | 22.6% | 4.26 | +0.9% |
| Manchester City win | 54.8% | 56.4% | 1.76 | -3.6% |

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
| Market best home last update utc | 2026-10-19T16:24:37Z |
| Market best draw last update utc | 2026-10-19T16:24:37Z |
| Market best away last update utc | 2026-10-19T16:24:37Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1207 |
| Dc lambda away | 1.8346 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.95 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.58 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 53.1% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 57.6% |
| P home draw | 45.2% |
| P draw away | 78.5% |
| P home away | 76.3% |
| Raw p home draw | 46.9% |
| Raw p draw away | 77.9% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 4.40 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:22Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:22Z |
| Home probability edge | +0.6% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | 0.0115 |
| Raw ev home | 0.0439 |
| Raw edge prob draw | 0.0219 |
| Raw ev draw | 0.0557 |
| Raw edge prob away | -0.0335 |
| Raw ev away | -0.0654 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.3%**. Expected goals are 2.13 for Chelsea and 1.16 for Tottenham Hotspur (3.29 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 63.6%; Under 3.5 goals: 58.5%; Double Chance 1X: 79.7%; Double Chance X2: 42.7%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 76.6%; BTTS Yes (both teams score): 61.4%; BTTS No (at least one team does not score): 38.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.3% | 1.75 |
| Draw | 22.4% | 4.47 |
| Tottenham Hotspur win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.16 |
| Expected total goals | 3.29 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 63.6% |
| Under 2.5 | 36.4% |
| Over 3.5 | 41.5% |
| Under 3.5 | 58.5% |
| Over 4.5 | 23.4% |
| Under 4.5 | 76.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.17% |
| 2 | 2-1 | 9.56% |
| 3 | 2-0 | 8.26% |
| 4 | 1-0 | 6.95% |
| 5 | 3-1 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.3% | 55.8% | 1.81 | +3.7% |
| Draw | 22.4% | 22.6% | 4.30 | -3.8% |
| Tottenham Hotspur win | 20.3% | 21.5% | 4.36 | -11.4% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1298 |
| Dc lambda away | 1.1569 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.4% |
| P btts no | 38.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.62 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.54 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.75 |
| Fair Over 3.5 odds | 2.41 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.28 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 84.8% |
| Raw p under 3 5 | 58.3% |
| Raw p btts yes | 61.2% |
| P home draw | 79.7% |
| P draw away | 42.7% |
| P home away | 77.6% |
| Raw p home draw | 80.9% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.74 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:22Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:22Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0296 |
| Raw ev home | 0.0640 |
| Raw edge prob draw | -0.0054 |
| Raw ev draw | -0.0495 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.1667 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.7%**. Expected goals are 1.11 for Coventry City and 1.21 for Fulham (2.32 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 41.5%; Under 3.5 goals: 79.4%; Double Chance 1X: 61.3%; Double Chance X2: 67.4%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 91.2%; BTTS Yes (both teams score): 47.8%; BTTS No (at least one team does not score): 52.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.6% | 3.07 |
| Draw | 28.8% | 3.48 |
| Fulham win | 38.7% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.11 |
| Fulham expected goals | 1.21 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.5% |
| Under 2.5 | 58.5% |
| Over 3.5 | 20.6% |
| Under 3.5 | 79.4% |
| Over 4.5 | 8.8% |
| Under 4.5 | 91.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.55% |
| 2 | 0-1 | 11.13% |
| 3 | 0-0 | 10.38% |
| 4 | 1-0 | 9.81% |
| 5 | 1-2 | 8.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.6% | 32.8% | 3.12 | +1.6% |
| Draw | 28.8% | 27.0% | 3.61 | +3.9% |
| Fulham win | 38.7% | 40.2% | 2.39 | -7.6% |
| Over 2.5 | 41.5% | 55.7% | 1.81 | -24.8% |
| Under 2.5 | 58.5% | 44.3% | 2.15 | +25.7% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1111 |
| Dc lambda away | 1.2084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.8% |
| P btts no | 52.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.64 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.86 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.40 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 32.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 48.2% |
| P home draw | 61.3% |
| P draw away | 67.4% |
| P home away | 71.2% |
| Raw p home draw | 62.9% |
| Raw p draw away | 67.7% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.39 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | -0.3% |
| Draw probability edge | +1.8% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -14.1% |
| Under 2.5 probability edge | +14.1% |
| Raw edge prob home | -0.0051 |
| Raw ev home | 0.0084 |
| Raw edge prob draw | 0.0360 |
| Raw ev draw | 0.1036 |
| Raw edge prob away | -0.0309 |
| Raw ev away | -0.1132 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **39.4%**. Expected goals are 1.49 for Crystal Palace and 1.59 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 60.6%; Double Chance X2: 65.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 62.7%; BTTS No (at least one team does not score): 37.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.6% | 2.89 |
| Draw | 26.0% | 3.84 |
| Newcastle United win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.49 |
| Newcastle United expected goals | 1.59 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.3% |
| Under 1.5 | 17.7% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.1% |
| Under 3.5 | 62.9% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 1-2 | 8.71% |
| 3 | 2-1 | 8.02% |
| 4 | 2-2 | 6.50% |
| 5 | 0-1 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.6% | 34.1% | 3.02 | +4.4% |
| Draw | 26.0% | 26.2% | 3.67 | -4.4% |
| Newcastle United win | 39.4% | 39.7% | 2.42 | -4.6% |
| Over 2.5 | 59.4% | 59.2% | 1.69 | +0.5% |
| Under 2.5 | 40.6% | 40.8% | 2.36 | -4.3% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4944 |
| Dc lambda away | 1.5882 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.7% |
| P btts no | 37.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.84 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.64 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 35.0% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 39.1% |
| Raw p over 1 5 | 82.3% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 62.7% |
| P home draw | 60.6% |
| P draw away | 65.4% |
| P home away | 74.0% |
| Raw p home draw | 60.9% |
| Raw p draw away | 65.0% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.58 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | +0.5% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0094 |
| Raw ev home | 0.0579 |
| Raw edge prob draw | -0.0034 |
| Raw ev draw | -0.0507 |
| Raw edge prob away | -0.0060 |
| Raw ev away | -0.0537 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.6%**. Expected goals are 1.21 for Hull City and 1.05 for Brentford (2.27 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.5%; Under 3.5 goals: 80.6%; Double Chance 1X: 57.4%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 30.0% | 3.33 |
| Draw | 27.4% | 3.65 |
| Brentford win | 42.6% | 2.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.21 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.27 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 19.4% |
| Under 3.5 | 80.6% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.54% |
| 2 | 1-1 | 12.81% |
| 3 | 0-0 | 10.27% |
| 4 | 1-2 | 9.71% |
| 5 | 1-0 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 30.0% | 21.6% | 4.52 | +35.7% |
| Draw | 27.4% | 23.9% | 3.98 | +9.1% |
| Brentford win | 42.6% | 54.5% | 1.84 | -21.7% |
| Over 2.5 | 40.5% | 56.3% | 1.78 | -27.8% |
| Under 2.5 | 59.5% | 43.7% | 2.21 | +31.4% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2120 |
| Dc lambda away | 1.0532 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.74 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.19 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.5% |
| Unadjusted draw probability | 30.9% |
| Unadjusted away-win probability | 30.6% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 46.9% |
| P home draw | 57.4% |
| P draw away | 70.0% |
| P home away | 72.6% |
| Raw p home draw | 69.4% |
| Raw p draw away | 61.5% |
| Raw p home away | 69.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 4.30 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.06 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | +8.5% |
| Draw probability edge | +3.5% |
| Away probability edge | -12.0% |
| Over 2.5 probability edge | -15.8% |
| Under 2.5 probability edge | +15.8% |
| Raw edge prob home | 0.1692 |
| Raw ev home | 0.7397 |
| Raw edge prob draw | 0.0701 |
| Raw ev draw | 0.2301 |
| Raw edge prob away | -0.2393 |
| Raw ev away | -0.4369 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **42.9%**. Expected goals are 1.64 for Liverpool and 1.48 for Brighton and Hove Albion (3.12 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.1%; Double Chance 1X: 68.3%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 42.9% | 2.33 |
| Draw | 25.4% | 3.94 |
| Brighton and Hove Albion win | 31.7% | 3.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.48 |
| Expected total goals | 3.12 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
| Over 1.5 | 82.8% |
| Under 1.5 | 17.2% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.59% |
| 2 | 2-1 | 9.28% |
| 3 | 1-2 | 7.46% |
| 4 | 1-0 | 6.64% |
| 5 | 2-2 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 42.9% | 45.2% | 2.19 | -6.1% |
| Draw | 25.4% | 25.1% | 3.98 | +1.1% |
| Brighton and Hove Albion win | 31.7% | 29.7% | 3.25 | +3.2% |
| Over 2.5 | 60.4% | 61.3% | 1.64 | -1.0% |
| Under 2.5 | 39.6% | 38.7% | 2.47 | -2.1% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6363 |
| Dc lambda away | 1.4807 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.70 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.80 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.8% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 63.2% |
| P home draw | 68.3% |
| P draw away | 57.1% |
| P home away | 74.6% |
| Raw p home draw | 66.2% |
| Raw p draw away | 59.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.14 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.2% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0464 |
| Raw ev home | -0.1122 |
| Raw edge prob draw | 0.0050 |
| Raw ev draw | 0.0206 |
| Raw edge prob away | 0.0414 |
| Raw ev away | 0.0991 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.0%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.8%; Double Chance 1X: 74.5%; Double Chance X2: 50.0%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 60.4%; BTTS No (at least one team does not score): 39.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.0% | 2.00 |
| Draw | 24.5% | 4.09 |
| Bournemouth win | 25.5% | 3.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 2-1 | 9.91% |
| 3 | 1-0 | 7.82% |
| 4 | 2-0 | 7.79% |
| 5 | 1-2 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.0% | 52.1% | 1.91 | -4.5% |
| Draw | 24.5% | 23.6% | 4.05 | -0.9% |
| Bournemouth win | 25.5% | 24.3% | 4.07 | +3.8% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7619 |
| Dc lambda away | 1.2730 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.4% |
| P btts no | 39.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.89 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 47.9% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.5% |
| P draw away | 50.0% |
| P home away | 75.5% |
| Raw p home draw | 73.3% |
| Raw p draw away | 52.1% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 1.86 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:24Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:24Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -2.6% |
| Under 2.5 probability edge | +2.6% |
| Raw edge prob home | -0.0417 |
| Raw ev home | -0.0845 |
| Raw edge prob draw | 0.0170 |
| Raw ev draw | 0.0258 |
| Raw edge prob away | 0.0247 |
| Raw ev away | 0.0883 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.4%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.6%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 70.3%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.9% | 3.13 |
| Draw | 29.7% | 3.36 |
| Leeds United win | 38.4% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.93% |
| 2 | 0-1 | 11.26% |
| 3 | 0-0 | 11.04% |
| 4 | 1-0 | 10.01% |
| 5 | 1-2 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.9% | 32.8% | 2.90 | -7.5% |
| Draw | 29.7% | 28.7% | 3.44 | +2.3% |
| Leeds United win | 38.4% | 38.5% | 2.63 | +0.9% |
| Over 2.5 | 40.2% | 45.1% | 2.14 | -14.0% |
| Under 2.5 | 59.8% | 54.9% | 1.83 | +9.4% |

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
| Market best home last update utc | 2026-10-19T16:24:38Z |
| Market best draw last update utc | 2026-10-19T16:24:38Z |
| Market best away last update utc | 2026-10-19T16:24:38Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0668 |
| Dc lambda away | 1.2125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T16:25:33.358592+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.06 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.16 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 61.6% |
| P draw away | 68.1% |
| P home away | 70.3% |
| Raw p home draw | 61.8% |
| Raw p draw away | 69.0% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Codere (IT) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.49 |
| Market reference 1x2 last update utc | 2026-10-19T16:25:25Z |
| Market reference home last update utc | 2026-10-19T16:25:25Z |
| Market reference draw last update utc | 2026-10-19T16:25:25Z |
| Market reference away last update utc | 2026-10-19T16:25:25Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market reference under 2 5 last update utc | 2026-10-19T16:25:25Z |
| Market best over 2 5 last update utc | 2026-10-19T16:24:38Z |
| Market best under 2 5 last update utc | 2026-10-19T16:24:38Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0184 |
| Raw ev home | -0.1016 |
| Raw edge prob draw | 0.0214 |
| Raw ev draw | 0.0602 |
| Raw edge prob away | -0.0030 |
| Raw ev away | 0.0047 |

</details>


---
