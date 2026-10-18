# Bundesliga — football model report

Fixtures in this report: **10**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 970 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 7de5ffc801935c85b53a157c1374aebb5e94c0dc9cb2ea4b6500ba7d027bef7f |
| Training as of utc | 2026-10-18T14:34:20.292027+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 52, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 52, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T14:34:20.292027+00:00', 'observations': 69, 'observations_sha256': '14055384d46eb480440cb8456b658a9a03c2f0fad4ccd5f2d8433e095b178d60', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 43, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 5, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'd0b2e9577288abe1ec04145aa17d927c0dad0636138aea7199a08fa770e09c34', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2940.808 |
| Base scoring parameter | 0.250 |
| Home-advantage parameter | 0.197 |
| Dixon-Coles low-score adjustment | -0.095 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 10.00 |
| Additional event odds calls used before this league | 5.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261018T143420292027Z_d1be48d82fafb5c893c33b942f9c58a6359a2274b328679936e29e38d63ab987.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.3%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 8.9%. Goal-market probabilities: at least one goal: 96.9%; Over 2.5 goals: 72.1%; Under 3.5 goals: 48.8%; Double Chance 1X: 59.7%; Double Chance X2: 62.9%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 37.1% | 2.69 |
| Draw | 22.6% | 4.43 |
| TSG Hoffenheim win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.94 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.73 |
| Over 0.5 | 96.9% |
| Under 0.5 | 3.1% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.2% |
| Under 3.5 | 48.8% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.94% |
| 2 | 1-2 | 8.48% |
| 3 | 2-1 | 7.22% |
| 4 | 2-2 | 7.09% |
| 5 | 1-3 | 5.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 37.1% | 32.6% | 3.19 | +18.4% |
| Draw | 22.6% | 22.1% | 4.16 | -6.1% |
| TSG Hoffenheim win | 40.3% | 45.2% | 2.17 | -12.5% |

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
| Dc lambda home | 1.9440 |
| Dc lambda away | 1.7870 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 32.00 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.47 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.13 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.8% |
| Raw p btts yes | 72.1% |
| P home draw | 59.7% |
| P draw away | 62.9% |
| P home away | 77.4% |
| Raw p home draw | 64.6% |
| Raw p draw away | 58.4% |
| Raw p home away | 77.0% |
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
| Home probability edge | +4.5% |
| Draw probability edge | +0.5% |
| Away probability edge | -4.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0897 |
| Raw ev home | 0.3274 |
| Raw edge prob draw | 0.0090 |
| Raw ev draw | -0.0421 |
| Raw edge prob away | -0.0988 |
| Raw ev away | -0.2326 |
| Market p home draw | 55.3% |
| Market home draw odds | 1.77 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T14:34:08Z |
| Market reference home draw last update utc | 2026-10-18T14:34:10Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.6% |
| Market draw away odds | 1.41 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T14:34:08Z |
| Market reference draw away last update utc | 2026-10-18T14:34:10Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.1% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T14:34:08Z |
| Market reference home away last update utc | 2026-10-18T14:34:10Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.75 |
| Market reference dc draw away odds | 1.41 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 91.2% |
| Market reference over 1 5 odds | 1.08 |
| Market reference over 1 5 opposite odds | 7.50 |
| Market reference over 1 5 last update utc | 2026-10-18T14:34:09Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 46.8% |
| Market reference under 3 5 odds | 2.08 |
| Market reference under 3 5 opposite odds | 1.84 |
| Market reference under 3 5 last update utc | 2026-10-18T14:34:08Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 74.0% |
| Market btts yes odds | 1.30 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T14:34:08Z |
| Market reference btts yes odds | 1.33 |
| Market reference btts yes opposite odds | 3.58 |
| Market reference btts yes last update utc | 2026-10-18T14:34:10Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.4%**. Expected goals are 2.52 for VfB Stuttgart and 1.19 for Borussia Monchengladbach (3.71 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.7%; Double Chance 1X: 85.1%; Double Chance X2: 31.6%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 67.9%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.4% | 1.46 |
| Draw | 16.7% | 5.98 |
| Borussia Monchengladbach win | 14.9% | 6.72 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.52 |
| Borussia Monchengladbach expected goals | 1.19 |
| Expected total goals | 3.71 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.6% |
| Under 2.5 | 27.4% |
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 32.1% |
| Under 4.5 | 67.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.66% |
| 2 | 3-1 | 8.11% |
| 3 | 2-0 | 8.09% |
| 4 | 1-1 | 7.10% |
| 5 | 3-0 | 6.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.4% | 71.3% | 1.43 | -2.2% |
| Draw | 16.7% | 14.5% | 5.80 | -3.1% |
| Borussia Monchengladbach win | 14.9% | 14.2% | 6.98 | +3.8% |

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
| Dc lambda home | 2.5190 |
| Dc lambda away | 1.1932 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.07 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.44 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.64 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.11 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 65.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 89.2% |
| Raw p under 3 5 | 49.2% |
| Raw p btts yes | 64.8% |
| P home draw | 85.1% |
| P draw away | 31.6% |
| P home away | 83.3% |
| Raw p home draw | 84.4% |
| Raw p draw away | 34.5% |
| Raw p home away | 81.1% |
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
| Home probability edge | -2.9% |
| Draw probability edge | +2.2% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -5.0% |
| Under 2.5 probability edge | +5.0% |
| Raw edge prob home | -0.0583 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0442 |
| Raw ev draw | 0.0977 |
| Raw edge prob away | 0.0140 |
| Raw ev away | 0.0872 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.6%**. Expected goals are 0.88 for 1. FC Köln and 0.73 for FC Schalke 04 (1.61 combined). The most likely exact score is 1-0 at 19.2%. Goal-market probabilities: at least one goal: 82.8%; Over 2.5 goals: 23.7%; Under 3.5 goals: 91.8%; Double Chance 1X: 71.9%; Double Chance X2: 58.4%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 30.0%; BTTS No (at least one team does not score): 70.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.6% | 2.40 |
| Draw | 30.3% | 3.30 |
| FC Schalke 04 win | 28.1% | 3.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.88 |
| FC Schalke 04 expected goals | 0.73 |
| Expected total goals | 1.61 |
| Over 0.5 | 82.8% |
| Under 0.5 | 17.2% |
| Over 1.5 | 49.6% |
| Under 1.5 | 50.4% |
| Over 2.5 | 23.7% |
| Under 2.5 | 76.3% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.23% |
| 2 | 0-0 | 17.18% |
| 3 | 0-1 | 13.97% |
| 4 | 1-1 | 11.32% |
| 5 | 2-0 | 9.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.6% | 47.7% | 2.12 | -11.7% |
| Draw | 30.3% | 23.0% | 3.98 | +20.5% |
| FC Schalke 04 win | 28.1% | 29.3% | 3.43 | -3.7% |
| Over 2.5 | 23.7% | 60.5% | 1.64 | -61.2% |
| Under 2.5 | 76.3% | 39.5% | 2.46 | +87.7% |

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
| Dc lambda home | 0.8789 |
| Dc lambda away | 0.7263 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 30.0% |
| P btts no | 70.0% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.82 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.22 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 12.16 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.93 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 37.5% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 48.9% |
| Raw p under 3 5 | 92.0% |
| Raw p btts yes | 31.4% |
| P home draw | 71.9% |
| P draw away | 58.4% |
| P home away | 69.7% |
| Raw p home draw | 73.1% |
| Raw p draw away | 64.4% |
| Raw p home away | 62.5% |
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
| Home probability edge | -6.1% |
| Draw probability edge | +7.3% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -36.8% |
| Under 2.5 probability edge | +36.8% |
| Raw edge prob home | -0.1211 |
| Raw ev home | -0.2455 |
| Raw edge prob draw | 0.1453 |
| Raw ev draw | 0.4940 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.0782 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **49.9%**. Expected goals are 1.54 for Augsburg and 1.03 for Union Berlin (2.57 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 48.2%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.2%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 49.9% | 2.00 |
| Draw | 25.3% | 3.95 |
| Union Berlin win | 24.8% | 4.03 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.54 |
| Union Berlin expected goals | 1.03 |
| Expected total goals | 2.57 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 25.8% |
| Under 3.5 | 74.2% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.09% |
| 2 | 1-0 | 11.10% |
| 3 | 2-1 | 9.72% |
| 4 | 2-0 | 9.46% |
| 5 | 0-0 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 49.9% | 51.8% | 1.96 | -2.2% |
| Draw | 25.3% | 22.8% | 4.16 | +5.4% |
| Union Berlin win | 24.8% | 25.4% | 3.77 | -6.5% |

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
| Dc lambda home | 1.5382 |
| Dc lambda away | 1.0276 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.45 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.28 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 48.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.6% |
| P home draw | 75.2% |
| P draw away | 50.1% |
| P home away | 74.7% |
| Raw p home draw | 75.8% |
| Raw p draw away | 52.0% |
| Raw p home away | 72.1% |
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
| Home probability edge | -1.9% |
| Draw probability edge | +2.5% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -13.5% |
| Under 2.5 probability edge | +13.5% |
| Raw edge prob home | -0.0384 |
| Raw ev home | -0.0599 |
| Raw edge prob draw | 0.0509 |
| Raw ev draw | 0.1595 |
| Raw edge prob away | -0.0126 |
| Raw ev away | -0.0890 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **63.6%**. Expected goals are 2.26 for Borussia Dortmund and 1.23 for Eintracht Frankfurt (3.49 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.7%; Under 3.5 goals: 53.4%; Double Chance 1X: 82.4%; Double Chance X2: 36.4%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 72.1%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 63.6% | 1.57 |
| Draw | 18.8% | 5.31 |
| Eintracht Frankfurt win | 17.6% | 5.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.26 |
| Eintracht Frankfurt expected goals | 1.23 |
| Expected total goals | 3.49 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.7% |
| Under 2.5 | 31.3% |
| Over 3.5 | 46.6% |
| Under 3.5 | 53.4% |
| Over 4.5 | 27.9% |
| Under 4.5 | 72.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.21% |
| 2 | 2-0 | 8.29% |
| 3 | 1-1 | 8.24% |
| 4 | 3-1 | 7.68% |
| 5 | 1-0 | 6.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 63.6% | 67.5% | 1.48 | -5.9% |
| Draw | 18.8% | 16.4% | 5.39 | +1.5% |
| Eintracht Frankfurt win | 17.6% | 16.0% | 6.42 | +12.7% |

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
| Dc lambda home | 2.2571 |
| Dc lambda away | 1.2318 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.21 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.59 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.9% |
| Raw p btts yes | 64.2% |
| P home draw | 82.4% |
| P draw away | 36.4% |
| P home away | 81.2% |
| Raw p home draw | 80.9% |
| Raw p draw away | 40.3% |
| Raw p home away | 78.8% |
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
| Home probability edge | -3.9% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0785 |
| Raw ev home | -0.1167 |
| Raw edge prob draw | 0.0480 |
| Raw ev draw | 0.1445 |
| Raw edge prob away | 0.0305 |
| Raw ev away | 0.2253 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.7%**. Expected goals are 1.60 for FSV Mainz 05 and 1.15 for Werder Bremen (2.75 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.1%; Under 3.5 goals: 69.9%; Double Chance 1X: 76.6%; Double Chance X2: 47.3%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.7% | 1.90 |
| Draw | 23.9% | 4.19 |
| Werder Bremen win | 23.4% | 4.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.60 |
| Werder Bremen expected goals | 1.15 |
| Expected total goals | 2.75 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.5% |
| Under 1.5 | 22.5% |
| Over 2.5 | 53.1% |
| Under 2.5 | 46.9% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 2-1 | 10.61% |
| 3 | 1-0 | 10.29% |
| 4 | 2-0 | 9.24% |
| 5 | 0-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.7% | 58.6% | 1.73 | -8.8% |
| Draw | 23.9% | 20.7% | 4.41 | +5.2% |
| Werder Bremen win | 23.4% | 20.7% | 4.72 | +10.6% |

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
| Dc lambda home | 1.6014 |
| Dc lambda away | 1.1476 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.07 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.45 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.68 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 55.6% |
| P home draw | 76.6% |
| P draw away | 47.3% |
| P home away | 76.1% |
| Raw p home draw | 73.8% |
| Raw p draw away | 53.2% |
| Raw p home away | 73.0% |
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
| Home probability edge | -5.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +2.8% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.1185 |
| Raw ev home | -0.1909 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.1922 |
| Raw edge prob away | 0.0550 |
| Raw ev away | 0.2364 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **63.0%**. Expected goals are 2.46 for RB Leipzig and 1.69 for Elversberg (4.15 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 79.3%; Under 3.5 goals: 39.9%; Double Chance 1X: 80.3%; Double Chance X2: 37.0%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 74.3%; BTTS No (at least one team does not score): 25.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 63.0% | 1.59 |
| Draw | 17.3% | 5.79 |
| Elversberg win | 19.7% | 5.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.46 |
| Elversberg expected goals | 1.69 |
| Expected total goals | 4.15 |
| Over 0.5 | 98.1% |
| Under 0.5 | 1.9% |
| Over 1.5 | 92.7% |
| Under 1.5 | 7.3% |
| Over 2.5 | 79.3% |
| Under 2.5 | 20.7% |
| Over 3.5 | 60.1% |
| Under 3.5 | 39.9% |
| Over 4.5 | 41.0% |
| Under 4.5 | 59.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.39% |
| 2 | 3-1 | 7.69% |
| 3 | 3-2 | 6.49% |
| 4 | 1-1 | 6.11% |
| 5 | 2-2 | 5.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 63.0% | 71.9% | 1.40 | -11.8% |
| Draw | 17.3% | 14.2% | 6.02 | +3.9% |
| Elversberg win | 19.7% | 13.9% | 7.50 | +47.8% |

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
| Dc lambda home | 2.4581 |
| Dc lambda away | 1.6883 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 74.3% |
| P btts no | 25.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 53.37 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.78 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.84 |
| Fair Over 3.5 odds | 1.66 |
| Fair Under 3.5 odds | 2.51 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.70 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 25.5% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.5% |
| Raw p btts yes | 75.2% |
| P home draw | 80.3% |
| P draw away | 37.0% |
| P home away | 82.7% |
| Raw p home draw | 74.5% |
| Raw p draw away | 45.8% |
| Raw p home away | 79.7% |
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
| Home probability edge | -8.9% |
| Draw probability edge | +3.1% |
| Away probability edge | +5.8% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.1771 |
| Raw ev home | -0.2415 |
| Raw edge prob draw | 0.0611 |
| Raw ev draw | 0.2229 |
| Raw edge prob away | 0.1160 |
| Raw ev away | 0.9130 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **37.9%**. Expected goals are 1.01 for SC Paderborn and 0.98 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.0%. Goal-market probabilities: at least one goal: 87.1%; Over 2.5 goals: 33.4%; Under 3.5 goals: 85.8%; Double Chance 1X: 66.6%; Double Chance X2: 62.1%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 39.8%; BTTS No (at least one team does not score): 60.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 37.9% | 2.64 |
| Draw | 28.8% | 3.48 |
| Hamburger SV win | 33.4% | 2.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.01 |
| Hamburger SV expected goals | 0.98 |
| Expected total goals | 1.98 |
| Over 0.5 | 87.1% |
| Under 0.5 | 12.9% |
| Over 1.5 | 60.6% |
| Under 1.5 | 39.4% |
| Over 2.5 | 33.4% |
| Under 2.5 | 66.6% |
| Over 3.5 | 14.2% |
| Under 3.5 | 85.8% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.01% |
| 2 | 0-0 | 12.90% |
| 3 | 1-1 | 12.68% |
| 4 | 0-1 | 12.53% |
| 5 | 2-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 37.9% | 41.7% | 2.40 | -9.2% |
| Draw | 28.8% | 23.9% | 3.92 | +12.7% |
| Hamburger SV win | 33.4% | 34.3% | 2.91 | -2.8% |
| Over 2.5 | 33.4% | 60.5% | 1.64 | -45.3% |
| Under 2.5 | 66.6% | 39.5% | 2.47 | +64.6% |

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
| Dc lambda home | 1.0054 |
| Dc lambda away | 0.9763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.75 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.00 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.05 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.55 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 33.6% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 40.8% |
| P home draw | 66.6% |
| P draw away | 62.1% |
| P home away | 71.2% |
| Raw p home draw | 67.6% |
| Raw p draw away | 66.0% |
| Raw p home away | 66.4% |
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
| Home probability edge | -3.9% |
| Draw probability edge | +4.8% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -27.1% |
| Under 2.5 probability edge | +27.1% |
| Raw edge prob home | -0.0776 |
| Raw ev home | -0.1847 |
| Raw edge prob draw | 0.0966 |
| Raw ev draw | 0.3166 |
| Raw edge prob away | -0.0190 |
| Raw ev away | -0.0559 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **70.4%**. Expected goals are 1.18 for SC Freiburg and 2.79 for Bayern Munich (3.96 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 76.0%; Under 3.5 goals: 44.1%; Double Chance 1X: 29.6%; Double Chance X2: 86.0%; Double Chance 12 (either team wins): 84.4%; Under 4.5 goals: 63.4%; BTTS Yes (both teams score): 65.3%; BTTS No (at least one team does not score): 34.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 14.0% | 7.12 |
| Draw | 15.6% | 6.41 |
| Bayern Munich win | 70.4% | 1.42 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.18 |
| Bayern Munich expected goals | 2.79 |
| Expected total goals | 3.96 |
| Over 0.5 | 97.7% |
| Under 0.5 | 2.3% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.0% |
| Under 2.5 | 24.0% |
| Over 3.5 | 55.9% |
| Under 3.5 | 44.1% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.68% |
| 2 | 1-3 | 8.06% |
| 3 | 0-2 | 7.38% |
| 4 | 0-3 | 6.85% |
| 5 | 1-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 14.0% | 15.2% | 6.52 | -8.5% |
| Draw | 15.6% | 14.5% | 5.80 | -9.5% |
| Bayern Munich win | 70.4% | 70.3% | 1.45 | +2.0% |

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
| Dc lambda home | 1.1764 |
| Dc lambda away | 2.7858 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 65.3% |
| P btts no | 34.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.97 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.33 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.17 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.27 |
| Fair Over 4.5 odds | 2.73 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 12.9% |
| Unadjusted draw probability | 16.7% |
| Unadjusted away-win probability | 70.4% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 44.1% |
| Raw p btts yes | 65.5% |
| P home draw | 29.6% |
| P draw away | 86.0% |
| P home away | 84.4% |
| Raw p home draw | 29.6% |
| Raw p draw away | 87.1% |
| Raw p home away | 83.3% |
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
| Home probability edge | -1.1% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0225 |
| Raw ev home | -0.1579 |
| Raw edge prob draw | 0.0224 |
| Raw ev draw | -0.0302 |
| Raw edge prob away | 0.0001 |
| Raw ev away | 0.0203 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **50.0%**. Expected goals are 1.40 for TSG Hoffenheim and 2.36 for Bayer Leverkusen (3.76 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.8%; Under 3.5 goals: 49.0%; Double Chance 1X: 50.0%; Double Chance X2: 71.5%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 68.3%; BTTS Yes (both teams score): 69.6%; BTTS No (at least one team does not score): 30.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 28.5% | 3.51 |
| Draw | 21.6% | 4.64 |
| Bayer Leverkusen win | 50.0% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.40 |
| Bayer Leverkusen expected goals | 2.36 |
| Expected total goals | 3.76 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.3% |
| Under 1.5 | 10.7% |
| Over 2.5 | 71.8% |
| Under 2.5 | 28.2% |
| Over 3.5 | 51.0% |
| Under 3.5 | 49.0% |
| Over 4.5 | 31.7% |
| Under 4.5 | 68.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.77% |
| 2 | 1-2 | 7.80% |
| 3 | 2-1 | 7.26% |
| 4 | 2-2 | 6.60% |
| 5 | 1-3 | 6.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 28.5% | 35.9% | 2.76 | -21.4% |
| Draw | 21.6% | 22.4% | 4.25 | -8.4% |
| Bayer Leverkusen win | 50.0% | 41.7% | 2.39 | +19.4% |

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
| Dc lambda home | 1.3950 |
| Dc lambda away | 2.3620 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T14:34:20.292027+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 69.6% |
| P btts no | 30.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.32 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.33 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.55 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.15 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 58.3% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 48.2% |
| Raw p btts yes | 68.9% |
| P home draw | 50.0% |
| P draw away | 71.5% |
| P home away | 78.4% |
| Raw p home draw | 41.7% |
| Raw p draw away | 79.0% |
| Raw p home away | 79.3% |
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
| Home probability edge | -7.4% |
| Draw probability edge | -0.9% |
| Away probability edge | +8.3% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.1486 |
| Raw ev home | -0.4192 |
| Raw edge prob draw | -0.0171 |
| Raw ev draw | -0.1203 |
| Raw edge prob away | 0.1658 |
| Raw ev away | 0.3924 |

</details>


---
