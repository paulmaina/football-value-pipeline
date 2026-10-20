# Premier League — football model report

Fixtures in this report: **10**.

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
| Training sha256 | c48bdc48c5fd2ee80d97cea695a952f70d52927306e6012953c78682ccb233b4 |
| Training as of utc | 2026-10-20T05:41:32.620650+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 69, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 69, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:41:32.620650+00:00', 'observations': 101, 'observations_sha256': 'ca7836a42829a073c775bfd8f6034bd32e04db206769d09a875a847d1b6924a9', 'eligible_training_matches': 18, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 52, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 18, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'd86404451dcc40fd688b80ebb547ef56889b0e431c2ec946b9fe3e3b33315eab', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 931.087 |
| Base scoring parameter | 0.210 |
| Home-advantage parameter | 0.183 |
| Dixon-Coles low-score adjustment | -0.090 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261020T054132620650Z_c2da396e8ef0b3e60e8138a02378269d5843b03ab61240119f548952e6dde72c.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
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

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **43.4%**. Expected goals are 1.32 for Ipswich Town and 1.70 for Nottingham Forest (3.02 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.4%; Double Chance 1X: 56.6%; Double Chance X2: 70.1%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.9% | 3.35 |
| Draw | 26.8% | 3.74 |
| Nottingham Forest win | 43.4% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.70 |
| Expected total goals | 3.02 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 81.3% |
| Under 1.5 | 18.7% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.6% |
| Under 3.5 | 64.4% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 1-2 | 8.89% |
| 3 | 2-1 | 7.48% |
| 4 | 0-1 | 6.97% |
| 5 | 0-2 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.9% | 30.9% | 3.14 | -6.2% |
| Draw | 26.8% | 27.8% | 3.63 | -2.9% |
| Nottingham Forest win | 43.4% | 41.3% | 2.39 | +3.7% |
| Over 2.5 | 57.7% | 55.8% | 1.84 | +6.2% |
| Under 2.5 | 42.3% | 44.2% | 2.12 | -10.4% |

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
| Market best home last update utc | 2026-10-20T05:41:33Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3205 |
| Dc lambda away | 1.7009 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.39 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.35 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.81 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.37 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 28.8% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 81.4% |
| Raw p under 3 5 | 64.2% |
| Raw p btts yes | 60.9% |
| P home draw | 56.6% |
| P draw away | 70.1% |
| P home away | 73.2% |
| Raw p home draw | 54.6% |
| Raw p draw away | 71.2% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.20 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | -1.0% |
| Draw probability edge | -1.0% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | -0.0204 |
| Raw ev home | -0.0941 |
| Raw edge prob draw | -0.0210 |
| Raw ev draw | -0.0666 |
| Raw edge prob away | 0.0414 |
| Raw ev away | 0.0859 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.3%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.30 combined). The most likely exact score is 1-0 at 17.1%. Goal-market probabilities: at least one goal: 90.1%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.6%; Double Chance 1X: 89.5%; Double Chance X2: 32.7%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.3% | 1.49 |
| Draw | 22.2% | 4.51 |
| Everton win | 10.5% | 9.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.1% |
| Under 0.5 | 9.9% |
| Over 1.5 | 68.3% |
| Under 1.5 | 31.7% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.4% |
| Under 3.5 | 79.6% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.13% |
| 2 | 2-0 | 15.56% |
| 3 | 0-0 | 9.87% |
| 4 | 1-1 | 9.81% |
| 5 | 2-1 | 8.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.3% | 70.2% | 1.43 | -3.8% |
| Draw | 22.2% | 19.7% | 4.93 | +9.3% |
| Everton win | 10.5% | 10.0% | 9.07 | -4.4% |
| Over 2.5 | 41.4% | 53.0% | 1.83 | -24.3% |
| Under 2.5 | 58.6% | 47.0% | 2.14 | +25.5% |

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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:41:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.13 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.59 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 64.4% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 36.9% |
| P home draw | 89.5% |
| P draw away | 32.7% |
| P home away | 77.8% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.6% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.42 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.80 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | -2.9% |
| Draw probability edge | +2.4% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -11.6% |
| Under 2.5 probability edge | +11.6% |
| Raw edge prob home | -0.0587 |
| Raw ev home | -0.0797 |
| Raw edge prob draw | 0.0484 |
| Raw ev draw | 0.2121 |
| Raw edge prob away | 0.0103 |
| Raw ev away | 0.0029 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **54.8%**. Expected goals are 1.12 for Aston Villa and 1.83 for Manchester City (2.96 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.5%; Double Chance 1X: 45.2%; Double Chance X2: 78.2%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.8% | 4.59 |
| Draw | 23.4% | 4.28 |
| Manchester City win | 54.8% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.96 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.5% |
| Under 3.5 | 65.5% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.01% |
| 2 | 1-2 | 10.14% |
| 3 | 0-2 | 9.05% |
| 4 | 0-1 | 8.86% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.8% | 21.5% | 4.72 | +2.9% |
| Draw | 23.4% | 22.0% | 4.26 | -0.4% |
| Manchester City win | 54.8% | 56.6% | 1.76 | -3.5% |

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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1206 |
| Dc lambda away | 1.8345 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.17 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.1% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 53.1% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 65.7% |
| Raw p btts yes | 57.6% |
| P home draw | 45.2% |
| P draw away | 78.2% |
| P home away | 76.6% |
| Raw p home draw | 46.9% |
| Raw p draw away | 77.9% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.60 |
| Reference draw odds | 4.50 |
| Reference away odds | 1.76 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.52 |
| Market reference over 2 5 last update utc | 2026-10-20T05:40:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:40:55Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | 0.0064 |
| Raw ev home | 0.0439 |
| Raw edge prob draw | 0.0282 |
| Raw ev draw | 0.0557 |
| Raw edge prob away | -0.0346 |
| Raw ev away | -0.0654 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **58.0%**. Expected goals are 2.13 for Chelsea and 1.16 for Tottenham Hotspur (3.29 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 63.8%; Under 3.5 goals: 58.4%; Double Chance 1X: 79.9%; Double Chance X2: 42.0%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 76.5%; BTTS Yes (both teams score): 61.2%; BTTS No (at least one team does not score): 38.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 58.0% | 1.72 |
| Draw | 21.8% | 4.58 |
| Tottenham Hotspur win | 20.1% | 4.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.16 |
| Expected total goals | 3.29 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 63.8% |
| Under 2.5 | 36.2% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.5% |
| Under 4.5 | 76.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.92% |
| 2 | 2-1 | 9.68% |
| 3 | 2-0 | 8.37% |
| 4 | 1-0 | 7.04% |
| 5 | 3-1 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 58.0% | 57.3% | 1.75 | +1.6% |
| Draw | 21.8% | 21.6% | 4.41 | -3.7% |
| Tottenham Hotspur win | 20.1% | 21.1% | 4.60 | -7.5% |

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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:41:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1298 |
| Dc lambda away | 1.1570 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.2% |
| P btts no | 38.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.15 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.57 |
| Fair Over 2.5 odds | 1.57 |
| Fair Under 2.5 odds | 2.77 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.26 |
| Fair Under 4.5 odds | 1.31 |
| Unadjusted home-win probability | 58.8% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 84.8% |
| Raw p under 3 5 | 58.3% |
| Raw p btts yes | 61.2% |
| P home draw | 79.9% |
| P draw away | 42.0% |
| P home away | 78.2% |
| Raw p home draw | 80.9% |
| Raw p draw away | 41.2% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.74 |
| Reference draw odds | 4.60 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.54 |
| Reference Under 2.5 odds | 2.51 |
| Market reference over 2 5 last update utc | 2026-10-20T05:40:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:40:55Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.3% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0147 |
| Raw ev home | 0.0287 |
| Raw edge prob draw | 0.0053 |
| Raw ev draw | -0.0253 |
| Raw edge prob away | -0.0200 |
| Raw ev away | -0.1208 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **38.6%**. Expected goals are 1.11 for Coventry City and 1.21 for Fulham (2.32 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.5%; Double Chance 1X: 61.4%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 91.3%; BTTS Yes (both teams score): 47.9%; BTTS No (at least one team does not score): 52.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 32.2% | 3.11 |
| Draw | 29.2% | 3.42 |
| Fulham win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.11 |
| Fulham expected goals | 1.21 |
| Expected total goals | 2.32 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 68.7% |
| Under 1.5 | 31.3% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.5% |
| Under 3.5 | 79.5% |
| Over 4.5 | 8.7% |
| Under 4.5 | 91.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.77% |
| 2 | 0-1 | 11.11% |
| 3 | 0-0 | 10.55% |
| 4 | 1-0 | 9.68% |
| 5 | 1-2 | 8.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 32.2% | 32.0% | 3.12 | +0.3% |
| Draw | 29.2% | 27.9% | 3.61 | +5.6% |
| Fulham win | 38.6% | 40.1% | 2.39 | -7.8% |
| Over 2.5 | 41.4% | 55.4% | 1.81 | -25.1% |
| Under 2.5 | 58.6% | 44.6% | 2.15 | +26.0% |

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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1110 |
| Dc lambda away | 1.2084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.9% |
| P btts no | 52.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.19 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.87 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.46 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 32.3% |
| Unadjusted draw probability | 30.6% |
| Unadjusted away-win probability | 37.1% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 79.5% |
| Raw p btts yes | 48.2% |
| P home draw | 61.4% |
| P draw away | 67.8% |
| P home away | 70.8% |
| Raw p home draw | 62.9% |
| Raw p draw away | 67.7% |
| Raw p home away | 69.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.10 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | +0.2% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | -14.0% |
| Under 2.5 probability edge | +14.0% |
| Raw edge prob home | 0.0031 |
| Raw ev home | 0.0084 |
| Raw edge prob draw | 0.0265 |
| Raw ev draw | 0.1037 |
| Raw edge prob away | -0.0296 |
| Raw ev away | -0.1131 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.0%**. Expected goals are 1.49 for Crystal Palace and 1.59 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 62.9%; Double Chance 1X: 60.0%; Double Chance X2: 66.0%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 62.7%; BTTS No (at least one team does not score): 37.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.0% | 2.94 |
| Draw | 26.1% | 3.84 |
| Newcastle United win | 40.0% | 2.50 |

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
| 1 | 1-1 | 11.95% |
| 2 | 1-2 | 8.84% |
| 3 | 2-1 | 7.88% |
| 4 | 2-2 | 6.50% |
| 5 | 0-1 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.0% | 32.9% | 3.02 | +2.6% |
| Draw | 26.1% | 26.2% | 3.67 | -4.4% |
| Newcastle United win | 40.0% | 40.9% | 2.42 | -3.2% |
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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda home | 1.4945 |
| Dc lambda away | 1.5881 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.7% |
| P btts no | 37.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.83 |
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
| P home draw | 60.0% |
| P draw away | 66.0% |
| P home away | 73.9% |
| Raw p home draw | 60.9% |
| Raw p draw away | 65.0% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | +1.1% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0215 |
| Raw ev home | 0.0580 |
| Raw edge prob draw | -0.0037 |
| Raw ev draw | -0.0507 |
| Raw edge prob away | -0.0178 |
| Raw ev away | -0.0538 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.7%**. Expected goals are 1.21 for Hull City and 1.05 for Brentford (2.27 combined). The most likely exact score is 0-1 at 13.6%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.5%; Under 3.5 goals: 80.7%; Double Chance 1X: 57.3%; Double Chance X2: 70.3%; Double Chance 12 (either team wins): 72.4%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 46.3%; BTTS No (at least one team does not score): 53.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 29.7% | 3.36 |
| Draw | 27.6% | 3.63 |
| Brentford win | 42.7% | 2.34 |

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
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.59% |
| 2 | 1-1 | 12.88% |
| 3 | 0-0 | 10.33% |
| 4 | 1-2 | 9.74% |
| 5 | 1-0 | 8.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 29.7% | 21.0% | 4.54 | +35.0% |
| Draw | 27.6% | 24.2% | 4.02 | +10.8% |
| Brentford win | 42.7% | 54.8% | 1.84 | -21.4% |
| Over 2.5 | 40.5% | 56.2% | 1.78 | -27.9% |
| Under 2.5 | 59.5% | 43.8% | 2.21 | +31.5% |

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
| Market best home last update utc | 2026-10-20T05:41:33Z |
| Market best draw last update utc | 2026-10-20T05:41:33Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2118 |
| Dc lambda away | 1.0533 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.3% |
| P btts no | 53.7% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.68 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.5% |
| Unadjusted draw probability | 30.9% |
| Unadjusted away-win probability | 30.6% |
| Raw p over 1 5 | 67.3% |
| Raw p under 3 5 | 80.6% |
| Raw p btts yes | 46.9% |
| P home draw | 57.3% |
| P draw away | 70.3% |
| P home away | 72.4% |
| Raw p home draw | 69.4% |
| Raw p draw away | 61.5% |
| Raw p home away | 69.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 4.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.80 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | +8.7% |
| Draw probability edge | +3.3% |
| Away probability edge | -12.1% |
| Over 2.5 probability edge | -15.7% |
| Under 2.5 probability edge | +15.7% |
| Raw edge prob home | 0.1750 |
| Raw ev home | 0.7471 |
| Raw edge prob draw | 0.0670 |
| Raw ev draw | 0.2425 |
| Raw edge prob away | -0.2420 |
| Raw ev away | -0.4368 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **42.4%**. Expected goals are 1.64 for Liverpool and 1.48 for Brighton and Hove Albion (3.12 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.5%; Under 3.5 goals: 62.0%; Double Chance 1X: 67.5%; Double Chance X2: 57.6%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 63.0%; BTTS No (at least one team does not score): 37.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 42.4% | 2.36 |
| Draw | 25.1% | 3.98 |
| Brighton and Hove Albion win | 32.5% | 3.07 |

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
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 38.0% |
| Under 3.5 | 62.0% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.45% |
| 2 | 2-1 | 9.17% |
| 3 | 1-2 | 7.65% |
| 4 | 1-0 | 6.56% |
| 5 | 2-2 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 42.4% | 44.2% | 2.19 | -7.2% |
| Draw | 25.1% | 24.6% | 3.98 | -0.1% |
| Brighton and Hove Albion win | 32.5% | 31.3% | 3.25 | +5.8% |
| Over 2.5 | 60.5% | 60.9% | 1.64 | -0.8% |
| Under 2.5 | 39.5% | 39.1% | 2.47 | -2.3% |

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
| Market best home last update utc | 2026-10-20T05:40:34Z |
| Market best draw last update utc | 2026-10-20T05:40:34Z |
| Market best away last update utc | 2026-10-20T05:40:34Z |
| Odds bookmakers 1x2 | 2.00 |
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
| Dc lambda home | 1.6362 |
| Dc lambda away | 1.4807 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.0% |
| P btts no | 37.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.92 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.81 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 40.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.8% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.1% |
| Raw p btts yes | 63.2% |
| P home draw | 67.5% |
| P draw away | 57.6% |
| P home away | 74.9% |
| Raw p home draw | 66.2% |
| Raw p draw away | 59.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 2.24 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.15 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:34Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:34Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0364 |
| Raw ev home | -0.1122 |
| Raw edge prob draw | 0.0109 |
| Raw ev draw | 0.0206 |
| Raw edge prob away | 0.0255 |
| Raw ev away | 0.0992 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **49.6%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.7%; Under 3.5 goals: 63.8%; Double Chance 1X: 74.4%; Double Chance X2: 50.4%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.6% | 2.02 |
| Draw | 24.9% | 4.02 |
| Bournemouth win | 25.6% | 3.91 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.54% |
| 2 | 2-1 | 9.82% |
| 3 | 1-0 | 7.75% |
| 4 | 2-0 | 7.72% |
| 5 | 1-2 | 6.56% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.6% | 51.2% | 1.91 | -5.3% |
| Draw | 24.9% | 24.4% | 4.05 | +0.7% |
| Bournemouth win | 25.6% | 24.4% | 4.07 | +4.0% |

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
| Market best home last update utc | 2026-10-20T05:40:35Z |
| Market best draw last update utc | 2026-10-20T05:40:35Z |
| Market best away last update utc | 2026-10-20T05:40:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7619 |
| Dc lambda away | 1.2729 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.61 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.45 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.22 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 47.9% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.4% |
| P draw away | 50.4% |
| P home away | 75.1% |
| Raw p home draw | 73.3% |
| Raw p draw away | 52.1% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 1.93 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | -2.7% |
| Under 2.5 probability edge | +2.7% |
| Raw edge prob home | -0.0328 |
| Raw ev home | -0.0844 |
| Raw edge prob draw | 0.0093 |
| Raw ev draw | 0.0258 |
| Raw edge prob away | 0.0234 |
| Raw ev away | 0.0882 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.3%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 40.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.7%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 69.8%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.5% | 3.18 |
| Draw | 30.2% | 3.31 |
| Leeds United win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.14% |
| 2 | 0-1 | 11.25% |
| 3 | 0-0 | 11.20% |
| 4 | 1-0 | 9.88% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.5% | 32.0% | 2.99 | -5.9% |
| Draw | 30.2% | 29.6% | 3.44 | +3.9% |
| Leeds United win | 38.3% | 38.5% | 2.63 | +0.8% |
| Over 2.5 | 40.1% | 45.4% | 2.14 | -14.3% |
| Under 2.5 | 59.9% | 54.6% | 1.83 | +9.7% |

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
| Market best home last update utc | 2026-10-20T05:41:33Z |
| Market best draw last update utc | 2026-10-20T05:40:35Z |
| Market best away last update utc | 2026-10-20T05:40:35Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0667 |
| Dc lambda away | 1.2125 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:41:32.620650+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.93 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.2% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 61.7% |
| P draw away | 68.5% |
| P home away | 69.8% |
| Raw p home draw | 61.8% |
| Raw p draw away | 69.0% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.10 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.58 |
| Market reference 1x2 last update utc | 2026-10-20T05:41:33Z |
| Market reference home last update utc | 2026-10-20T05:41:33Z |
| Market reference draw last update utc | 2026-10-20T05:41:33Z |
| Market reference away last update utc | 2026-10-20T05:41:33Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:41:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:40:35Z |
| Market best under 2 5 last update utc | 2026-10-20T05:40:35Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0099 |
| Raw ev home | -0.0737 |
| Raw edge prob draw | 0.0126 |
| Raw ev draw | 0.0602 |
| Raw edge prob away | -0.0027 |
| Raw ev away | 0.0047 |

</details>


---
