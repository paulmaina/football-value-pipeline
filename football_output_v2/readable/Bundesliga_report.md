# Bundesliga — football model report

Fixtures in this report: **10**.

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
| Training sha256 | 0c519f91f218e2f4361feb69cc2eafeded772cf8cb1af3a3eaec2282cd116bc2 |
| Training as of utc | 2026-10-19T11:19:26.390802+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-19T11:19:26.390802+00:00', 'observations': 77, 'observations_sha256': '0755276705974e99d0d76f3e984ca35eeab8644a13efb091ff5c61f9b4cf00e1', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 45, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'cbf8eebcb4457b0f0a618ac7b5ad4a9b5649a27a804117960523ba2082c73fe9', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
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
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 2.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261019T111926390802Z_75352050cf6db47852f77a5633a6d319803c7ebef108650f3a87821b8c040e8d.json |
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

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **38.7%**. Expected goals are 1.95 for Borussia Monchengladbach and 1.65 for TSG Hoffenheim (3.60 combined). The most likely exact score is 1-1 at 9.4%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 70.0%; Under 3.5 goals: 51.6%; Double Chance 1X: 61.3%; Double Chance X2: 61.6%; Double Chance 12 (either team wins): 77.1%; Under 4.5 goals: 70.5%; BTTS Yes (both teams score): 70.3%; BTTS No (at least one team does not score): 29.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 38.4% | 2.61 |
| Draw | 22.9% | 4.37 |
| TSG Hoffenheim win | 38.7% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.95 |
| TSG Hoffenheim expected goals | 1.65 |
| Expected total goals | 3.60 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 70.0% |
| Under 2.5 | 30.0% |
| Over 3.5 | 48.4% |
| Under 3.5 | 51.6% |
| Over 4.5 | 29.5% |
| Under 4.5 | 70.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.44% |
| 2 | 1-2 | 8.73% |
| 3 | 2-1 | 7.44% |
| 4 | 2-2 | 6.85% |
| 5 | 3-1 | 4.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 38.4% | 32.6% | 3.19 | +22.4% |
| Draw | 22.9% | 22.1% | 4.16 | -4.8% |
| TSG Hoffenheim win | 38.7% | 45.2% | 2.17 | -15.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | fd9b8c185737a15615aa0c9daaa3dfbf |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9491 |
| Dc lambda away | 1.6548 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 70.3% |
| P btts no | 29.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.96 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.63 |
| Fair Over 2.5 odds | 1.43 |
| Fair Under 2.5 odds | 3.33 |
| Fair Over 3.5 odds | 2.06 |
| Fair Under 3.5 odds | 1.94 |
| Fair Over 4.5 odds | 3.39 |
| Fair Under 4.5 odds | 1.42 |
| Unadjusted home-win probability | 44.1% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 32.2% |
| Raw p over 1 5 | 88.4% |
| Raw p under 3 5 | 51.4% |
| Raw p btts yes | 70.3% |
| P home draw | 61.3% |
| P draw away | 61.6% |
| P home away | 77.1% |
| Raw p home draw | 67.8% |
| Raw p draw away | 55.9% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 4.10 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | +5.7% |
| Draw probability edge | +0.8% |
| Away probability edge | -6.5% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | 0.1148 |
| Raw ev home | 0.4072 |
| Raw edge prob draw | 0.0152 |
| Raw ev draw | -0.0162 |
| Raw edge prob away | -0.1300 |
| Raw ev away | -0.3004 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **63.9%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.45 combined). The most likely exact score is 2-1 at 10.8%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.7%; Under 3.5 goals: 53.8%; Double Chance 1X: 82.3%; Double Chance X2: 36.1%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 63.9% | 1.57 |
| Draw | 18.4% | 5.42 |
| Borussia Monchengladbach win | 17.7% | 5.66 |

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
| 1 | 2-1 | 10.81% |
| 2 | 2-0 | 8.39% |
| 3 | 1-1 | 8.07% |
| 4 | 3-1 | 7.81% |
| 5 | 1-0 | 6.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 63.9% | 71.3% | 1.43 | -8.6% |
| Draw | 18.4% | 14.5% | 5.80 | +6.9% |
| Borussia Monchengladbach win | 17.7% | 14.2% | 6.98 | +23.3% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1670 |
| Dc lambda away | 1.2877 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.32 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.61 |
| Fair Under 4.5 odds | 1.38 |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 82.3% |
| P draw away | 36.1% |
| P home away | 81.6% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -7.4% |
| Draw probability edge | +3.9% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.1485 |
| Raw ev home | -0.1925 |
| Raw edge prob draw | 0.0786 |
| Raw ev draw | 0.2972 |
| Raw edge prob away | 0.0699 |
| Raw ev away | 0.4773 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.6%**. Expected goals are 1.75 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.6%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.0%; Double Chance X2: 48.4%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.6% | 1.94 |
| Draw | 24.5% | 4.09 |
| FC Schalke 04 win | 24.0% | 4.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.75 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.69% |
| 2 | 1-0 | 9.96% |
| 3 | 2-0 | 9.74% |
| 4 | 2-1 | 9.09% |
| 5 | 0-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.6% | 47.7% | 2.12 | +9.3% |
| Draw | 24.5% | 23.0% | 3.98 | -2.6% |
| FC Schalke 04 win | 24.0% | 29.3% | 3.43 | -17.8% |
| Over 2.5 | 50.6% | 60.5% | 1.64 | -17.0% |
| Under 2.5 | 49.4% | 39.5% | 2.46 | +21.6% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
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
| Dc lambda home | 1.7517 |
| Dc lambda away | 0.9334 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.15 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.42 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 55.4% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.7% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.0% |
| P draw away | 48.4% |
| P home away | 75.5% |
| Raw p home draw | 81.3% |
| Raw p draw away | 44.6% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.92 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:08Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:08Z |
| Home probability edge | +3.9% |
| Draw probability edge | +1.5% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -9.9% |
| Under 2.5 probability edge | +9.9% |
| Raw edge prob home | 0.0772 |
| Raw ev home | 0.1749 |
| Raw edge prob draw | 0.0292 |
| Raw ev draw | 0.0319 |
| Raw edge prob away | -0.1064 |
| Raw ev away | -0.3603 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **45.7%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 46.9%; Under 3.5 goals: 75.5%; Double Chance 1X: 71.9%; Double Chance X2: 54.3%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 45.7% | 2.19 |
| Draw | 26.2% | 3.81 |
| Union Berlin win | 28.1% | 3.56 |

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
| 1 | 1-1 | 12.52% |
| 2 | 1-0 | 11.10% |
| 3 | 2-1 | 9.88% |
| 4 | 2-0 | 8.55% |
| 5 | 0-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 45.7% | 51.8% | 1.96 | -10.4% |
| Draw | 26.2% | 22.8% | 4.16 | +9.2% |
| Union Berlin win | 28.1% | 25.4% | 3.77 | +5.8% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
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
| Dc lambda away | 1.1557 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.75 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.70 |
| Fair Over 2.5 odds | 2.13 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.08 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 8.86 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.0% |
| P home draw | 71.9% |
| P draw away | 54.3% |
| P home away | 73.8% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.80 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -6.1% |
| Draw probability edge | +3.5% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | -14.9% |
| Under 2.5 probability edge | +14.9% |
| Raw edge prob home | -0.1219 |
| Raw ev home | -0.2236 |
| Raw edge prob draw | 0.0692 |
| Raw ev draw | 0.2355 |
| Raw edge prob away | 0.0527 |
| Raw ev away | 0.1570 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.2%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.2%; Under 3.5 goals: 50.3%; Double Chance 1X: 83.5%; Double Chance X2: 34.8%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.2% | 1.53 |
| Draw | 18.3% | 5.48 |
| Eintracht Frankfurt win | 16.5% | 6.06 |

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
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.71% |
| 2 | 2-0 | 7.95% |
| 3 | 3-1 | 7.84% |
| 4 | 1-1 | 7.82% |
| 5 | 3-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.2% | 67.5% | 1.48 | -3.4% |
| Draw | 18.3% | 16.4% | 5.39 | -1.6% |
| Eintracht Frankfurt win | 16.5% | 16.0% | 6.42 | +5.9% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4214 |
| Dc lambda away | 1.2224 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.65 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.01 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.48 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Unadjusted home-win probability | 63.0% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.1% |
| P home draw | 83.5% |
| P draw away | 34.8% |
| P home away | 81.7% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.0% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.40 |
| Reference draw odds | 4.70 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.8% |
| Away probability edge | +0.5% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0458 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0365 |
| Raw ev draw | 0.0823 |
| Raw edge prob away | 0.0093 |
| Raw ev away | 0.0892 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **54.1%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.3%; Under 3.5 goals: 66.8%; Double Chance 1X: 77.5%; Double Chance X2: 45.9%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 54.1% | 1.85 |
| Draw | 23.4% | 4.27 |
| Werder Bremen win | 22.5% | 4.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.0% |
| Under 1.5 | 20.0% |
| Over 2.5 | 56.3% |
| Under 2.5 | 43.7% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.09% |
| 2 | 2-1 | 10.54% |
| 3 | 1-0 | 9.15% |
| 4 | 2-0 | 9.08% |
| 5 | 3-1 | 6.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 54.1% | 58.6% | 1.73 | -6.5% |
| Draw | 23.4% | 20.7% | 4.41 | +3.4% |
| Werder Bremen win | 22.5% | 20.7% | 4.72 | +6.2% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7305 |
| Dc lambda away | 1.1602 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.45 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.99 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.29 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.82 |
| Fair Under 4.5 odds | 1.21 |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.5% |
| P draw away | 45.9% |
| P home away | 76.6% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.60 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -4.6% |
| Draw probability edge | +2.8% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | -7.5% |
| Under 2.5 probability edge | +7.5% |
| Raw edge prob home | -0.0913 |
| Raw ev home | -0.1438 |
| Raw edge prob draw | 0.0550 |
| Raw ev draw | 0.1552 |
| Raw edge prob away | 0.0362 |
| Raw ev away | 0.1477 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **65.5%**. Expected goals are 2.49 for RB Leipzig and 1.47 for Elversberg (3.97 combined). The most likely exact score is 2-1 at 9.6%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 76.8%; Under 3.5 goals: 43.3%; Double Chance 1X: 82.6%; Double Chance X2: 34.5%; Double Chance 12 (either team wins): 82.9%; Under 4.5 goals: 62.6%; BTTS Yes (both teams score): 70.6%; BTTS No (at least one team does not score): 29.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 65.5% | 1.53 |
| Draw | 17.1% | 5.83 |
| Elversberg win | 17.4% | 5.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.49 |
| Elversberg expected goals | 1.47 |
| Expected total goals | 3.97 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.8% |
| Under 2.5 | 23.2% |
| Over 3.5 | 56.7% |
| Under 3.5 | 43.3% |
| Over 4.5 | 37.4% |
| Under 4.5 | 62.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.61% |
| 2 | 3-1 | 7.99% |
| 3 | 1-1 | 6.60% |
| 4 | 2-0 | 6.53% |
| 5 | 3-2 | 5.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 65.5% | 71.9% | 1.40 | -8.3% |
| Draw | 17.1% | 14.2% | 6.02 | +3.2% |
| Elversberg win | 17.4% | 13.9% | 7.50 | +30.2% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4945 |
| Dc lambda away | 1.4720 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 70.6% |
| P btts no | 29.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.93 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 11.99 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.31 |
| Fair Over 3.5 odds | 1.76 |
| Fair Under 3.5 odds | 2.31 |
| Fair Over 4.5 odds | 2.67 |
| Fair Under 4.5 odds | 1.60 |
| Unadjusted home-win probability | 59.1% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 91.4% |
| Raw p under 3 5 | 44.0% |
| Raw p btts yes | 71.5% |
| P home draw | 82.6% |
| P draw away | 34.5% |
| P home away | 82.9% |
| Raw p home draw | 79.2% |
| Raw p draw away | 40.9% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.40 |
| Reference away odds | 5.50 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -6.4% |
| Draw probability edge | +2.9% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.1278 |
| Raw ev home | -0.1725 |
| Raw edge prob draw | 0.0587 |
| Raw ev draw | 0.2086 |
| Raw edge prob away | 0.0691 |
| Raw ev away | 0.5610 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.1%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 33.5%; Under 3.5 goals: 85.8%; Double Chance 1X: 67.0%; Double Chance X2: 61.9%; Double Chance 12 (either team wins): 71.0%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.1% | 2.63 |
| Draw | 29.0% | 3.45 |
| Hamburger SV win | 33.0% | 3.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
| Over 1.5 | 60.9% |
| Under 1.5 | 39.1% |
| Over 2.5 | 33.5% |
| Under 2.5 | 66.5% |
| Over 3.5 | 14.2% |
| Under 3.5 | 85.8% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.85% |
| 2 | 0-0 | 13.00% |
| 3 | 1-1 | 12.80% |
| 4 | 0-1 | 12.29% |
| 5 | 2-0 | 7.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.1% | 41.7% | 2.40 | -8.6% |
| Draw | 29.0% | 23.9% | 3.92 | +13.5% |
| Hamburger SV win | 33.0% | 34.3% | 2.91 | -4.1% |
| Over 2.5 | 33.5% | 60.5% | 1.64 | -45.1% |
| Under 2.5 | 66.5% | 39.5% | 2.47 | +64.3% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0192 |
| Dc lambda away | 0.9641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.69 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.56 |
| Fair Over 2.5 odds | 2.99 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.03 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.45 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.4% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 41.0% |
| P home draw | 67.0% |
| P draw away | 61.9% |
| P home away | 71.0% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.6% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market best over 2 5 last update utc | 2026-10-18T14:34:08Z |
| Market best under 2 5 last update utc | 2026-10-18T14:34:08Z |
| Home probability edge | -3.6% |
| Draw probability edge | +5.0% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -27.0% |
| Under 2.5 probability edge | +27.0% |
| Raw edge prob home | -0.0728 |
| Raw ev home | -0.1732 |
| Raw edge prob draw | 0.1007 |
| Raw ev draw | 0.3325 |
| Raw edge prob away | -0.0279 |
| Raw ev away | -0.0817 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **66.7%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.8%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.3%; Under 3.5 goals: 49.2%; Double Chance 1X: 33.3%; Double Chance X2: 83.9%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 16.1% | 6.22 |
| Draw | 17.2% | 5.81 |
| Bayern Munich win | 66.7% | 1.50 |

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
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.84% |
| 2 | 1-3 | 8.02% |
| 3 | 0-2 | 7.95% |
| 4 | 1-1 | 7.30% |
| 5 | 0-3 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 16.1% | 15.2% | 6.52 | +4.8% |
| Draw | 17.2% | 14.5% | 5.80 | -0.3% |
| Bayern Munich win | 66.7% | 70.3% | 1.45 | -3.2% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
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
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.49 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.39 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.61 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 33.3% |
| P draw away | 83.9% |
| P home away | 82.8% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 5.00 |
| Reference draw odds | 5.20 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.20 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | +0.9% |
| Draw probability edge | +2.7% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0180 |
| Raw ev home | 0.1065 |
| Raw edge prob draw | 0.0543 |
| Raw ev draw | 0.1548 |
| Raw edge prob away | -0.0723 |
| Raw ev away | -0.0848 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.7%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.7%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.3%; Double Chance X2: 69.2%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 69.9%; BTTS No (at least one team does not score): 30.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.8% | 3.25 |
| Draw | 22.5% | 4.45 |
| Bayer Leverkusen win | 46.7% | 2.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.7% |
| Under 2.5 | 29.3% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.25% |
| 2 | 1-2 | 8.13% |
| 3 | 2-1 | 7.50% |
| 4 | 2-2 | 6.74% |
| 5 | 1-3 | 5.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.8% | 35.9% | 2.76 | -15.0% |
| Draw | 22.5% | 22.4% | 4.25 | -4.5% |
| Bayer Leverkusen win | 46.7% | 41.7% | 2.39 | +11.7% |

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
| Market best home last update utc | 2026-10-18T14:34:08Z |
| Market best draw last update utc | 2026-10-18T14:34:08Z |
| Market best away last update utc | 2026-10-18T14:34:08Z |
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
| Bbs statistics cutoff utc | 2026-10-19T11:19:26.390802+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.9% |
| P btts no | 30.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.62 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.93 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.41 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.6% |
| P home draw | 53.3% |
| P draw away | 69.2% |
| P home away | 77.5% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-18T14:34:10Z |
| Market reference home last update utc | 2026-10-18T14:34:10Z |
| Market reference draw last update utc | 2026-10-18T14:34:10Z |
| Market reference away last update utc | 2026-10-18T14:34:10Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-18T14:34:09Z |
| Market reference under 2 5 last update utc | 2026-10-18T14:34:09Z |
| Home probability edge | -5.1% |
| Draw probability edge | +0.1% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | -0.1021 |
| Raw ev home | -0.2908 |
| Raw edge prob draw | 0.0010 |
| Raw ev draw | -0.0431 |
| Raw edge prob away | 0.1010 |
| Raw ev away | 0.2378 |

</details>


---
