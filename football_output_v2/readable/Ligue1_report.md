# Ligue 1 — football model report

Fixtures in this report: **9**.

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
| Training sha256 | 9a38da0cc1171ad797146062adbda94f5f554f9d1c190caea1d3324ba3f684f9 |
| Training as of utc | 2026-10-20T05:43:35.816142+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 63, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 63, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:43:35.816142+00:00', 'observations': 90, 'observations_sha256': 'e7b70d444df0e97c04a85cbca1ceb109ecbaa0f4f7bb0dc6ac55b222e199bd4d', 'eligible_training_matches': 17, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 47, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 17, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': 'babfa604a8c02df26e4fdf9fe1cee2e6bca631dbc5eb2239b7fcddec660c6911', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 5075.352 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.055 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 9.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261020T054335816142Z_a99c0a3e43ed35c4b9d33b933c9b1e4340d84560abfcf58d5d8820e969f5c4d0.json |
| Over 1 5 in window quote fixtures | 0 |
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

## 2026-10-23 — Brest vs Nice

The model's most likely 1X2 outcome is **Brest win** at **39.0%**. Expected goals are 1.22 for Brest and 1.24 for Nice (2.46 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 44.9%; Under 3.5 goals: 76.6%; Double Chance 1X: 66.7%; Double Chance X2: 61.0%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brest win | 39.0% | 2.57 |
| Draw | 27.7% | 3.61 |
| Nice win | 33.3% | 3.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brest expected goals | 1.22 |
| Nice expected goals | 1.24 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 71.1% |
| Under 1.5 | 28.9% |
| Over 2.5 | 44.9% |
| Under 2.5 | 55.1% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.17% |
| 2 | 1-0 | 10.77% |
| 3 | 0-1 | 9.13% |
| 4 | 0-0 | 8.95% |
| 5 | 2-1 | 8.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brest win | 39.0% | 42.8% | 2.31 | -10.0% |
| Draw | 27.7% | 26.7% | 3.49 | -3.3% |
| Nice win | 33.3% | 30.5% | 3.40 | +13.4% |
| Over 2.5 | 44.9% | 56.3% | 1.76 | -21.0% |
| Under 2.5 | 55.1% | 43.7% | 2.23 | +22.9% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.17 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.47 |
| Fair Over 2.5 odds | 2.23 |
| Fair Under 2.5 odds | 1.81 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.59 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 35.1% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 36.2% |
| Raw p over 1 5 | 71.1% |
| Raw p under 3 5 | 76.7% |
| Raw p btts yes | 50.8% |
| P home draw | 66.7% |
| P draw away | 61.0% |
| P home away | 72.3% |
| Raw p home draw | 63.8% |
| Raw p draw away | 64.9% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.30 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | -3.8% |
| Draw probability edge | +1.0% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -11.5% |
| Under 2.5 probability edge | +11.5% |
| Raw edge prob home | -0.0762 |
| Raw ev home | -0.1881 |
| Raw edge prob draw | 0.0200 |
| Raw ev draw | 0.0015 |
| Raw edge prob away | 0.0562 |
| Raw ev away | 0.2293 |

</details>


---

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **46.9%**. Expected goals are 1.68 for RC Lens and 1.02 for Paris FC (2.70 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 72.2%; Double Chance X2: 53.1%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 86.4%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 46.9% | 2.13 |
| Draw | 25.2% | 3.96 |
| Paris FC win | 27.8% | 3.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.68 |
| Paris FC expected goals | 1.02 |
| Expected total goals | 2.70 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.6% |
| Under 4.5 | 86.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 1-0 | 9.58% |
| 3 | 2-1 | 8.72% |
| 4 | 2-0 | 8.51% |
| 5 | 0-1 | 7.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RC Lens win | 46.9% | 41.8% | 2.42 | +13.6% |
| Draw | 25.2% | 25.0% | 3.79 | -4.3% |
| Paris FC win | 27.8% | 33.2% | 2.98 | -17.1% |
| Over 2.5 | 50.5% | 59.6% | 1.71 | -13.6% |
| Under 2.5 | 49.5% | 40.4% | 2.32 | +14.8% |

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
| Market best home last update utc | 2026-10-20T05:43:31Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6771 |
| Dc lambda away | 1.0249 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.77 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.54 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.36 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 22.5% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.4% |
| Raw p btts yes | 52.8% |
| P home draw | 72.2% |
| P draw away | 53.1% |
| P home away | 74.8% |
| Raw p home draw | 77.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | +5.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -5.4% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | 0.1016 |
| Raw ev home | 0.2585 |
| Raw edge prob draw | 0.0055 |
| Raw ev draw | -0.0330 |
| Raw edge prob away | -0.1071 |
| Raw ev away | -0.3300 |

</details>


---

## 2026-10-24 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **59.0%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 1-1 at 10.8%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.9%; Double Chance 1X: 81.7%; Double Chance X2: 41.0%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 84.5%; BTTS Yes (both teams score): 51.5%; BTTS No (at least one team does not score): 48.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 59.0% | 1.70 |
| Draw | 22.7% | 4.40 |
| Troyes win | 18.3% | 5.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.6% |
| Under 1.5 | 22.4% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.5% |
| Under 4.5 | 84.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.84% |
| 2 | 2-0 | 10.65% |
| 3 | 1-0 | 10.61% |
| 4 | 2-1 | 9.70% |
| 5 | 3-0 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 59.0% | 57.8% | 1.71 | +0.9% |
| Draw | 22.7% | 22.5% | 4.26 | -3.2% |
| Troyes win | 18.3% | 19.7% | 5.13 | -6.3% |
| Over 2.5 | 53.5% | 59.6% | 1.67 | -10.7% |
| Under 2.5 | 46.5% | 40.4% | 2.40 | +11.7% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9080 |
| Dc lambda away | 0.9102 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.5% |
| P btts no | 48.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.43 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.47 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.22 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.46 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 81.7% |
| P draw away | 41.0% |
| P home away | 77.3% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.33 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | +1.2% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -6.1% |
| Under 2.5 probability edge | +6.1% |
| Raw edge prob home | 0.0241 |
| Raw ev home | 0.0294 |
| Raw edge prob draw | 0.0044 |
| Raw ev draw | -0.0221 |
| Raw edge prob away | -0.0285 |
| Raw ev away | -0.1357 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **44.3%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.5%; Under 3.5 goals: 68.7%; Double Chance 1X: 70.7%; Double Chance X2: 55.7%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 44.3% | 2.26 |
| Draw | 26.4% | 3.79 |
| Lille win | 29.3% | 3.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.9% |
| Under 1.5 | 22.1% |
| Over 2.5 | 53.5% |
| Under 2.5 | 46.5% |
| Over 3.5 | 31.3% |
| Under 3.5 | 68.7% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.48% |
| 2 | 2-1 | 9.29% |
| 3 | 1-0 | 8.78% |
| 4 | 2-0 | 7.35% |
| 5 | 1-2 | 7.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 44.3% | 45.1% | 2.19 | -2.9% |
| Draw | 26.4% | 26.7% | 3.60 | -5.0% |
| Lille win | 29.3% | 28.2% | 3.72 | +8.9% |
| Over 2.5 | 53.5% | 56.3% | 1.77 | -5.3% |
| Under 2.5 | 46.5% | 43.7% | 2.22 | +3.2% |

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
| Market best home last update utc | 2026-10-20T05:43:31Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:31Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.02 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.53 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 43.6% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 70.7% |
| P draw away | 55.7% |
| P home away | 73.6% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.4% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.18 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | -0.8% |
| Draw probability edge | -0.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | -0.0157 |
| Raw ev home | -0.0462 |
| Raw edge prob draw | -0.0050 |
| Raw ev draw | -0.0585 |
| Raw edge prob away | 0.0207 |
| Raw ev away | 0.1270 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **36.4%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.0%; Double Chance 1X: 63.6%; Double Chance X2: 65.2%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 34.8% | 2.87 |
| Draw | 28.8% | 3.47 |
| Lorient win | 36.4% | 2.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.7% |
| Under 1.5 | 28.3% |
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.72% |
| 2 | 1-0 | 9.61% |
| 3 | 0-1 | 9.55% |
| 4 | 0-0 | 9.12% |
| 5 | 2-1 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 34.8% | 36.4% | 2.86 | -0.5% |
| Draw | 28.8% | 29.2% | 3.43 | -1.2% |
| Lorient win | 36.4% | 34.4% | 2.70 | -1.7% |
| Over 2.5 | 45.2% | 45.5% | 2.10 | -5.1% |
| Under 2.5 | 54.8% | 54.5% | 1.86 | +1.9% |

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
| Market best home last update utc | 2026-10-20T05:43:31Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.96 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.17 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.35 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.4% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 63.6% |
| P draw away | 65.2% |
| P home away | 71.2% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | -1.6% |
| Draw probability edge | -0.4% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | -0.0318 |
| Raw ev home | -0.0506 |
| Raw edge prob draw | -0.0076 |
| Raw ev draw | -0.0246 |
| Raw edge prob away | 0.0394 |
| Raw ev away | 0.0360 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **43.0%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 62.5%; Under 3.5 goals: 59.3%; Double Chance 1X: 68.5%; Double Chance X2: 57.0%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 77.5%; BTTS Yes (both teams score): 65.0%; BTTS No (at least one team does not score): 35.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 43.0% | 2.32 |
| Draw | 25.5% | 3.93 |
| Le Mans FC win | 31.5% | 3.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.5% |
| Under 2.5 | 37.5% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.5% |
| Under 4.5 | 77.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 2-1 | 8.97% |
| 3 | 1-2 | 7.30% |
| 4 | 2-2 | 7.03% |
| 5 | 1-0 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 43.0% | 43.7% | 2.23 | -4.0% |
| Draw | 25.5% | 26.7% | 3.70 | -5.8% |
| Le Mans FC win | 31.5% | 29.6% | 3.37 | +6.1% |
| Over 2.5 | 62.5% | 54.2% | 1.78 | +11.3% |
| Under 2.5 | 37.5% | 45.8% | 2.20 | -17.5% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:32Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7277 |
| Dc lambda away | 1.5162 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.0% |
| P btts no | 35.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.32 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.24 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.44 |
| Fair Under 4.5 odds | 1.29 |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 68.5% |
| P draw away | 57.0% |
| P home away | 74.5% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.6% |
| Raw p home away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.25 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | -0.7% |
| Draw probability edge | -1.2% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +8.3% |
| Under 2.5 probability edge | -8.3% |
| Raw edge prob home | -0.0136 |
| Raw ev home | -0.0553 |
| Raw edge prob draw | -0.0245 |
| Raw ev draw | -0.1031 |
| Raw edge prob away | 0.0381 |
| Raw ev away | 0.1255 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **63.6%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 55.4%; Under 3.5 goals: 67.0%; Double Chance 1X: 84.4%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 79.1%; Under 4.5 goals: 83.1%; BTTS Yes (both teams score): 49.7%; BTTS No (at least one team does not score): 50.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 63.6% | 1.57 |
| Draw | 20.9% | 4.79 |
| Le Havre win | 15.6% | 6.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 78.9% |
| Under 1.5 | 21.1% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 33.0% |
| Under 3.5 | 67.0% |
| Over 4.5 | 16.9% |
| Under 4.5 | 83.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.40% |
| 2 | 1-0 | 10.31% |
| 3 | 1-1 | 9.95% |
| 4 | 2-1 | 9.23% |
| 5 | 3-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 63.6% | 60.2% | 1.61 | +2.3% |
| Draw | 20.9% | 21.4% | 4.82 | +0.6% |
| Le Havre win | 15.6% | 18.4% | 5.44 | -15.3% |
| Over 2.5 | 55.4% | 61.3% | 1.65 | -8.6% |
| Under 2.5 | 44.6% | 38.7% | 2.45 | +9.2% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:31Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1125 |
| Dc lambda away | 0.8098 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.7% |
| P btts no | 50.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.58 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.75 |
| Fair Over 2.5 odds | 1.80 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.03 |
| Fair Under 3.5 odds | 1.49 |
| Fair Over 4.5 odds | 5.93 |
| Fair Under 4.5 odds | 1.20 |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 84.4% |
| P draw away | 36.4% |
| P home away | 79.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:33Z |
| Market best over 2 5 last update utc | 2026-10-20T05:43:32Z |
| Market best under 2 5 last update utc | 2026-10-20T05:43:32Z |
| Home probability edge | +3.4% |
| Draw probability edge | -0.5% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | 0.0673 |
| Raw ev home | 0.0776 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.0181 |
| Raw edge prob away | -0.0573 |
| Raw ev away | -0.3094 |

</details>


---

## 2026-10-25 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **69.4%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 10.0%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 69.1%; Under 3.5 goals: 52.8%; Double Chance 1X: 86.3%; Double Chance X2: 30.6%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 71.6%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 69.4% | 1.44 |
| Draw | 17.0% | 5.90 |
| Lyon win | 13.7% | 7.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 87.3% |
| Under 1.5 | 12.7% |
| Over 2.5 | 69.1% |
| Under 2.5 | 30.9% |
| Over 3.5 | 47.2% |
| Under 3.5 | 52.8% |
| Over 4.5 | 28.4% |
| Under 4.5 | 71.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.99% |
| 2 | 2-0 | 9.12% |
| 3 | 3-1 | 8.07% |
| 4 | 1-1 | 7.51% |
| 5 | 3-0 | 7.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 69.4% | 72.6% | 1.43 | -0.8% |
| Draw | 17.0% | 15.2% | 5.89 | -0.1% |
| Lyon win | 13.7% | 12.2% | 7.60 | +3.8% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:31Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4235 |
| Dc lambda away | 1.0955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.54 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.88 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.23 |
| Fair Over 3.5 odds | 2.12 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.53 |
| Fair Under 4.5 odds | 1.40 |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.7% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.0% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 61.1% |
| P home draw | 86.3% |
| P draw away | 30.6% |
| P home away | 83.0% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.36 |
| Reference draw odds | 6.10 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.34 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:53Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:53Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.8% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0639 |
| Raw ev home | -0.0535 |
| Raw edge prob draw | 0.0356 |
| Raw ev draw | 0.1039 |
| Raw edge prob away | 0.0283 |
| Raw ev away | 0.1452 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **53.3%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.15 combined). The most likely exact score is 1-1 at 10.4%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.4%; Under 3.5 goals: 61.2%; Double Chance 1X: 76.0%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 53.3% | 1.88 |
| Draw | 22.7% | 4.41 |
| Strasbourg win | 24.0% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 38.8% |
| Under 3.5 | 61.2% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.37% |
| 2 | 2-1 | 9.89% |
| 3 | 2-0 | 7.90% |
| 4 | 1-0 | 7.73% |
| 5 | 3-1 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 53.3% | 54.5% | 1.79 | -4.6% |
| Draw | 22.7% | 21.9% | 4.46 | +1.2% |
| Strasbourg win | 24.0% | 23.6% | 4.36 | +4.8% |

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
| Market best home last update utc | 2026-10-20T05:43:32Z |
| Market best draw last update utc | 2026-10-20T05:43:31Z |
| Market best away last update utc | 2026-10-20T05:43:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9036 |
| Dc lambda away | 1.2513 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:35.816142+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.42 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.85 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.70 |
| Fair Under 4.5 odds | 1.27 |
| Unadjusted home-win probability | 52.1% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.8% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.0% |
| P draw away | 46.7% |
| P home away | 77.3% |
| Raw p home draw | 75.5% |
| Raw p draw away | 47.9% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.81 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:33Z |
| Market reference home last update utc | 2026-10-20T05:43:33Z |
| Market reference draw last update utc | 2026-10-20T05:43:33Z |
| Market reference away last update utc | 2026-10-20T05:43:33Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.41 |
| Reference Under 2.5 odds | 2.85 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:53Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:53Z |
| Home probability edge | -1.2% |
| Draw probability edge | +0.8% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -7.1% |
| Under 2.5 probability edge | +7.1% |
| Raw edge prob home | -0.0240 |
| Raw ev home | -0.0678 |
| Raw edge prob draw | 0.0151 |
| Raw ev draw | 0.0460 |
| Raw edge prob away | 0.0089 |
| Raw ev away | 0.0670 |

</details>


---
