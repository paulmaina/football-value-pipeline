# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,969 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 730 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | d5253304468b210b2f7561ac9ac9cd3f24e629d934a19d6f4233faf88560f9ad |
| Training as of utc | 2026-10-20T05:43:07.772166+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 69, 'bbs_added_results': 9, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 69, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-20T05:43:07.772166+00:00', 'observations': 100, 'observations_sha256': 'b8cde538f8f80687eff19983d55e1c13c1c3f05983d5dcb605cf2aedd97a4624', 'eligible_training_matches': 19, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 45, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 19, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'ce20a98c71564d556c697faf42f4e2ecedb7e188b0b5511fa24cafd55dace92c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 2441.049 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.128 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261020T054307772166Z_f0853e9a10ade28bdc8934b2b4c25d66aea64a98b1584324f587abea8bc72664.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **46.5%**. Expected goals are 1.49 for Torino and 1.00 for Monza (2.49 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.1%; Double Chance 1X: 73.5%; Double Chance X2: 53.5%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 46.5% | 2.15 |
| Draw | 27.0% | 3.70 |
| Monza win | 26.5% | 3.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.49 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.4% |
| Under 1.5 | 28.6% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.9% |
| Under 3.5 | 76.1% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.81% |
| 2 | 1-0 | 11.55% |
| 3 | 2-1 | 8.91% |
| 4 | 2-0 | 8.89% |
| 5 | 0-0 | 8.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 46.5% | 45.0% | 2.19 | +1.9% |
| Draw | 27.0% | 27.1% | 3.62 | -2.3% |
| Monza win | 26.5% | 27.9% | 3.64 | -3.6% |
| Over 2.5 | 45.3% | 48.8% | 2.11 | -4.5% |
| Under 2.5 | 54.7% | 51.2% | 1.87 | +2.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:45:00+00:00 |
| Fixture id | 124c70f8f3248a845bdb983a54e74720 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:52Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4875 |
| Dc lambda away | 1.0026 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.46 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.49 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.18 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.34 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 48.0% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 25.1% |
| Raw p over 1 5 | 71.5% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 49.4% |
| P home draw | 73.5% |
| P draw away | 53.5% |
| P home away | 73.0% |
| Raw p home draw | 74.9% |
| Raw p draw away | 52.0% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.14 |
| Reference draw odds | 3.48 |
| Reference away odds | 3.38 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.93 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:52Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -3.6% |
| Under 2.5 probability edge | +3.6% |
| Raw edge prob home | 0.0295 |
| Raw ev home | 0.0510 |
| Raw edge prob draw | -0.0012 |
| Raw ev draw | -0.0250 |
| Raw edge prob away | -0.0282 |
| Raw ev away | -0.0872 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **41.7%**. Expected goals are 1.04 for Cagliari and 1.42 for Bologna (2.47 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 43.8%; Under 3.5 goals: 76.7%; Double Chance 1X: 58.3%; Double Chance X2: 71.7%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 89.9%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.3% | 3.53 |
| Draw | 30.0% | 3.34 |
| Bologna win | 41.7% | 2.40 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.42 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.1% |
| Under 4.5 | 89.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.21% |
| 2 | 0-1 | 10.72% |
| 3 | 0-0 | 9.72% |
| 4 | 1-0 | 8.78% |
| 5 | 1-2 | 8.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.3% | 29.5% | 3.35 | -5.1% |
| Draw | 30.0% | 32.5% | 3.13 | -6.2% |
| Bologna win | 41.7% | 38.0% | 2.55 | +6.3% |
| Over 2.5 | 43.8% | 43.8% | 2.24 | -1.8% |
| Under 2.5 | 56.2% | 56.2% | 1.76 | -1.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | b7f0880e3da978f9481f7cb5697e2aa5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0423 |
| Dc lambda away | 1.4246 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.28 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.29 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.85 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 27.2% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 45.4% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 58.3% |
| P draw away | 71.7% |
| P home away | 70.0% |
| Raw p home draw | 54.6% |
| Raw p draw away | 72.8% |
| Raw p home away | 72.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 3.26 |
| Reference draw odds | 2.97 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.69 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -1.2% |
| Draw probability edge | -2.5% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0233 |
| Raw ev home | -0.0899 |
| Raw edge prob draw | -0.0503 |
| Raw ev draw | -0.1407 |
| Raw edge prob away | 0.0736 |
| Raw ev away | 0.1572 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.1%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 59.7%; Under 3.5 goals: 62.7%; Double Chance 1X: 85.4%; Double Chance X2: 34.9%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.1% | 1.54 |
| Draw | 20.3% | 4.92 |
| Sassuolo win | 14.6% | 6.85 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.54% |
| 2 | 2-1 | 10.12% |
| 3 | 1-0 | 9.61% |
| 4 | 1-1 | 9.55% |
| 5 | 3-0 | 7.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.1% | 66.4% | 1.49 | -3.0% |
| Draw | 20.3% | 20.1% | 4.94 | +0.4% |
| Sassuolo win | 14.6% | 13.5% | 7.10 | +3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:00:00+00:00 |
| Fixture id | 08ffd99b2249c81d8a7410598f32b9b0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1230 |
| Dc lambda away | 0.9606 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.65 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.48 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.99 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 63.7% |
| Unadjusted draw probability | 20.5% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 62.9% |
| Raw p btts yes | 54.7% |
| P home draw | 85.4% |
| P draw away | 34.9% |
| P home away | 79.7% |
| Raw p home draw | 84.3% |
| Raw p draw away | 36.3% |
| Raw p home away | 79.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.48 |
| Reference draw odds | 4.65 |
| Reference away odds | 6.83 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Home probability edge | -1.4% |
| Draw probability edge | +0.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -6.6% |
| Under 2.5 probability edge | +6.6% |
| Raw edge prob home | -0.0270 |
| Raw ev home | -0.0506 |
| Raw edge prob draw | 0.0042 |
| Raw ev draw | 0.0145 |
| Raw edge prob away | 0.0228 |
| Raw ev away | 0.1179 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **61.8%**. Expected goals are 1.57 for Lazio and 0.72 for Parma (2.29 combined). The most likely exact score is 1-0 at 16.8%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 41.1%; Under 3.5 goals: 79.8%; Double Chance 1X: 85.4%; Double Chance X2: 38.2%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 40.2%; BTTS No (at least one team does not score): 59.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 61.8% | 1.62 |
| Draw | 23.5% | 4.25 |
| Parma win | 14.6% | 6.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.57 |
| Parma expected goals | 0.72 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.78% |
| 2 | 2-0 | 13.47% |
| 3 | 1-1 | 10.70% |
| 4 | 2-1 | 9.69% |
| 5 | 0-0 | 9.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 61.8% | 66.4% | 1.50 | -7.2% |
| Draw | 23.5% | 21.0% | 4.58 | +7.8% |
| Parma win | 14.6% | 12.6% | 7.62 | +11.4% |
| Over 2.5 | 41.1% | 49.3% | 1.98 | -18.6% |
| Under 2.5 | 58.9% | 50.7% | 1.97 | +16.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | b27cb3ea731fa3f18d05e6a627bdf984 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5670 |
| Dc lambda away | 0.7191 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 40.2% |
| P btts no | 59.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.49 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.94 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.71 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 57.3% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 16.7% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 41.0% |
| P home draw | 85.4% |
| P draw away | 38.2% |
| P home away | 76.5% |
| Raw p home draw | 83.3% |
| Raw p draw away | 42.7% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.48 |
| Reference draw odds | 4.45 |
| Reference away odds | 7.28 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -4.6% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -8.2% |
| Under 2.5 probability edge | +8.2% |
| Raw edge prob home | -0.0910 |
| Raw ev home | -0.1406 |
| Raw edge prob draw | 0.0503 |
| Raw ev draw | 0.1932 |
| Raw edge prob away | 0.0408 |
| Raw ev away | 0.2690 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.1%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.6%; Double Chance X2: 63.9%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.1% | 2.77 |
| Draw | 28.4% | 3.52 |
| AS Roma win | 35.4% | 2.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.20 |
| AS Roma expected goals | 1.06 |
| Expected total goals | 2.26 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.5% |
| Under 1.5 | 33.5% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.3% |
| Under 3.5 | 80.7% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.25% |
| 2 | 0-1 | 11.81% |
| 3 | 1-0 | 11.21% |
| 4 | 0-0 | 10.47% |
| 5 | 1-2 | 7.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.1% | 33.3% | 2.90 | +4.7% |
| Draw | 28.4% | 27.5% | 3.54 | +0.7% |
| AS Roma win | 35.4% | 39.2% | 2.57 | -8.9% |
| Over 2.5 | 39.7% | 51.2% | 1.94 | -22.9% |
| Under 2.5 | 60.3% | 48.8% | 2.00 | +20.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:00:00+00:00 |
| Fixture id | 0b4894e9fb123ef3045269f97e339eba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2045 |
| Dc lambda away | 1.0599 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.55 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.17 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.46 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 38.9% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.7% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.6% |
| P draw away | 63.9% |
| P home away | 71.6% |
| Raw p home draw | 68.3% |
| Raw p draw away | 61.1% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.90 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +2.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | 0.0553 |
| Raw ev home | 0.1275 |
| Raw edge prob draw | 0.0196 |
| Raw ev draw | 0.0418 |
| Raw edge prob away | -0.0749 |
| Raw ev away | -0.1855 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.8%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.36 combined). The most likely exact score is 1-1 at 9.5%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.3%; Double Chance 1X: 79.8%; Double Chance X2: 41.2%; Double Chance 12 (either team wins): 79.0%; Under 4.5 goals: 75.7%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.8% | 1.70 |
| Draw | 21.0% | 4.77 |
| Frosinone win | 20.2% | 4.95 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.3% |
| Under 4.5 | 75.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.46% |
| 2 | 2-1 | 9.13% |
| 3 | 2-0 | 8.26% |
| 4 | 1-0 | 7.06% |
| 5 | 3-1 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.8% | 54.7% | 1.81 | +6.5% |
| Draw | 21.0% | 22.1% | 4.28 | -10.2% |
| Frosinone win | 20.2% | 23.2% | 4.37 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 63aa6e3f679ee4c68de5b4bd8d3361bb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:52Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2516 |
| Dc lambda away | 1.1053 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.10 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.57 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.11 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.1% |
| P home draw | 79.8% |
| P draw away | 41.2% |
| P home away | 79.0% |
| Raw p home draw | 82.8% |
| Raw p draw away | 37.1% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.79 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Home probability edge | +4.1% |
| Draw probability edge | -1.1% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | 0.0819 |
| Raw ev home | 0.1388 |
| Raw edge prob draw | -0.0220 |
| Raw ev draw | -0.1490 |
| Raw edge prob away | -0.0600 |
| Raw ev away | -0.2483 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.7%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 39.1%; Under 3.5 goals: 80.9%; Double Chance 1X: 76.4%; Double Chance X2: 52.3%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.7% | 2.10 |
| Draw | 28.7% | 3.49 |
| Venezia win | 23.6% | 4.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.1% |
| Under 2.5 | 60.9% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.78% |
| 2 | 1-1 | 13.22% |
| 3 | 0-0 | 11.08% |
| 4 | 2-0 | 9.93% |
| 5 | 0-1 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.7% | 46.2% | 2.14 | +2.1% |
| Draw | 28.7% | 29.2% | 3.44 | -1.3% |
| Venezia win | 23.6% | 24.6% | 3.91 | -7.8% |
| Over 2.5 | 39.1% | 50.7% | 2.02 | -21.1% |
| Under 2.5 | 60.9% | 49.3% | 1.98 | +20.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | 95cfaecfe96bb7ced1fb6af974a4110b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:52Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4003 |
| Dc lambda away | 0.8580 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.03 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.78 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 76.4% |
| P draw away | 52.3% |
| P home away | 71.3% |
| Raw p home draw | 77.4% |
| Raw p draw away | 50.8% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 2.11 |
| Reference draw odds | 3.29 |
| Reference away odds | 3.89 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:52Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | 0.0301 |
| Raw ev home | 0.0535 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.0309 |
| Raw edge prob away | -0.0197 |
| Raw ev away | -0.1164 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.5%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.35 combined). The most likely exact score is 2-0 at 10.3%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.3%; Under 3.5 goals: 56.9%; Double Chance 1X: 87.7%; Double Chance X2: 29.5%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.5% | 1.42 |
| Draw | 17.2% | 5.82 |
| Fiorentina win | 12.3% | 8.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.35 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.1% |
| Under 1.5 | 14.9% |
| Over 2.5 | 65.3% |
| Under 2.5 | 34.7% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.34% |
| 2 | 2-1 | 9.69% |
| 3 | 1-0 | 8.31% |
| 4 | 3-0 | 8.31% |
| 5 | 1-1 | 7.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.5% | 71.3% | 1.41 | -0.6% |
| Draw | 17.2% | 16.6% | 5.75 | -1.2% |
| Fiorentina win | 12.3% | 12.1% | 8.05 | -0.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T11:30:00+00:00 |
| Fixture id | c9b6c7048d8dc33dae618f67f462f67a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:52Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4100 |
| Dc lambda away | 0.9371 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.35 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.69 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.88 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.04 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 69.6% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 85.0% |
| Raw p under 3 5 | 57.0% |
| Raw p btts yes | 55.6% |
| P home draw | 87.7% |
| P draw away | 29.5% |
| P home away | 82.8% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.4% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 1.38 |
| Reference draw odds | 5.55 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | -0.0170 |
| Raw ev home | -0.0181 |
| Raw edge prob draw | 0.0121 |
| Raw ev draw | 0.0227 |
| Raw edge prob away | 0.0049 |
| Raw ev away | 0.0125 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.5%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.1%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 36.4%; Under 3.5 goals: 83.3%; Double Chance 1X: 37.5%; Double Chance X2: 86.8%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.5%; BTTS No (at least one team does not score): 64.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.2% | 7.60 |
| Draw | 24.3% | 4.11 |
| Juventus win | 62.5% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 63.4% |
| Under 1.5 | 36.6% |
| Over 2.5 | 36.4% |
| Under 2.5 | 63.6% |
| Over 3.5 | 16.7% |
| Under 3.5 | 83.3% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.13% |
| 2 | 0-2 | 14.48% |
| 3 | 0-0 | 11.26% |
| 4 | 1-1 | 10.46% |
| 5 | 1-2 | 9.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.2% | 11.1% | 8.19 | +7.7% |
| Draw | 24.3% | 21.6% | 4.53 | +10.2% |
| Juventus win | 62.5% | 67.4% | 1.50 | -6.2% |
| Over 2.5 | 36.4% | 51.2% | 1.92 | -30.1% |
| Under 2.5 | 63.6% | 48.8% | 2.02 | +28.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:00:00+00:00 |
| Fixture id | 63af660d4d0d52f8ac7685172ef939c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:52Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6248 |
| Dc lambda away | 1.4820 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.5% |
| P btts no | 64.5% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.88 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.75 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 5.98 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.22 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.5% |
| P draw away | 86.8% |
| P home away | 75.7% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 8.25 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +2.1% |
| Draw probability edge | +2.8% |
| Away probability edge | -4.8% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | 0.0419 |
| Raw ev home | 0.2489 |
| Raw edge prob draw | 0.0551 |
| Raw ev draw | 0.2264 |
| Raw edge prob away | -0.0970 |
| Raw ev away | -0.1348 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **55.3%**. Expected goals are 1.05 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.9%; Under 3.5 goals: 70.3%; Double Chance 1X: 44.7%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.4% | 4.91 |
| Draw | 24.4% | 4.11 |
| AC Milan win | 55.3% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.05 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 51.9% |
| Under 2.5 | 48.1% |
| Over 3.5 | 29.7% |
| Under 3.5 | 70.3% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.59% |
| 2 | 0-1 | 11.21% |
| 3 | 1-2 | 10.28% |
| 4 | 0-2 | 9.82% |
| 5 | 0-0 | 6.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.4% | 17.7% | 5.48 | +11.7% |
| Draw | 24.4% | 23.8% | 4.17 | +1.6% |
| AC Milan win | 55.3% | 58.5% | 1.70 | -6.0% |
| Over 2.5 | 51.9% | 50.9% | 1.93 | +0.1% |
| Under 2.5 | 48.1% | 49.1% | 2.01 | -3.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T19:45:00+00:00 |
| Fixture id | 3564688383b255192409c9deb8e526ed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:52Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0466 |
| Dc lambda away | 1.6909 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.90 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.24 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.37 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.92 |
| Fair Under 4.5 odds | 1.17 |
| Unadjusted home-win probability | 23.1% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 44.7% |
| P draw away | 79.6% |
| P home away | 75.6% |
| Raw p home draw | 47.9% |
| Raw p draw away | 76.9% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / BetOnline.ag |
| Reference home odds | 5.33 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.68 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:11Z |
| Market reference home last update utc | 2026-10-20T05:43:11Z |
| Market reference draw last update utc | 2026-10-20T05:43:11Z |
| Market reference away last update utc | 2026-10-20T05:43:11Z |
| O/U 2.5 market source | The Odds API / BetOnline.ag |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:43:11Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +2.7% |
| Draw probability edge | +0.5% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | +1.0% |
| Under 2.5 probability edge | -1.0% |
| Raw edge prob home | 0.0534 |
| Raw ev home | 0.2632 |
| Raw edge prob draw | 0.0105 |
| Raw ev draw | 0.0376 |
| Raw edge prob away | -0.0640 |
| Raw ev away | -0.1149 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **69.7%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.3%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 50.2%; Under 3.5 goals: 72.3%; Double Chance 1X: 88.8%; Double Chance X2: 30.3%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 42.9%; BTTS No (at least one team does not score): 57.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.7% | 1.43 |
| Draw | 19.1% | 5.24 |
| Cagliari win | 11.2% | 8.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 50.2% |
| Under 2.5 | 49.8% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.28% |
| 2 | 2-0 | 14.07% |
| 3 | 2-1 | 9.99% |
| 4 | 3-0 | 9.02% |
| 5 | 1-1 | 8.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.7% | 73.6% | 1.40 | -2.4% |
| Draw | 19.1% | 16.6% | 5.20 | -0.7% |
| Cagliari win | 11.2% | 9.8% | 9.84 | +10.3% |
| Over 2.5 | 50.2% | 55.8% | 1.78 | -10.7% |
| Under 2.5 | 49.8% | 44.2% | 2.21 | +10.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7eecf109ae6a5f87441a79b0e4111982 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9239 |
| Dc lambda away | 0.7100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 42.9% |
| P btts no | 57.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.03 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.97 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.59 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.5% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.8% |
| P draw away | 30.3% |
| P home away | 80.9% |
| Raw p home draw | 87.4% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.31 |
| Reference draw odds | 4.85 |
| Reference away odds | 7.75 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -3.9% |
| Draw probability edge | +2.5% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.0778 |
| Raw ev home | -0.0786 |
| Raw edge prob draw | 0.0491 |
| Raw ev draw | 0.1206 |
| Raw edge prob away | 0.0287 |
| Raw ev away | 0.2435 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **44.1%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.6%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.6%; Double Chance 1X: 55.9%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 30.1% | 3.32 |
| Draw | 25.8% | 3.88 |
| Lazio win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.6% |
| Under 0.5 | 6.4% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.17% |
| 2 | 1-2 | 8.64% |
| 3 | 0-1 | 8.50% |
| 4 | 2-1 | 7.63% |
| 5 | 0-2 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 30.1% | 33.9% | 2.96 | -10.8% |
| Draw | 25.8% | 26.5% | 3.54 | -8.8% |
| Lazio win | 44.1% | 39.5% | 2.53 | +11.6% |
| Over 2.5 | 53.6% | 53.7% | 1.82 | -2.5% |
| Under 2.5 | 46.4% | 46.3% | 2.15 | -0.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T17:30:00+00:00 |
| Fixture id | c7445242bf16a8f37afef7863af45a78 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1697 |
| Dc lambda away | 1.6697 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.56 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.15 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.40 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 26.4% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.4% |
| P home draw | 55.9% |
| P draw away | 69.9% |
| P home away | 74.2% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.6% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.68 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -3.8% |
| Draw probability edge | -0.8% |
| Away probability edge | +4.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0755 |
| Raw ev home | -0.2198 |
| Raw edge prob draw | -0.0157 |
| Raw ev draw | -0.1159 |
| Raw edge prob away | 0.0913 |
| Raw ev away | 0.2313 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.9%**. Expected goals are 0.92 for Torino and 1.49 for Como (2.41 combined). The most likely exact score is 0-1 at 13.7%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.5%; Double Chance 1X: 47.1%; Double Chance X2: 78.4%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.6% | 4.64 |
| Draw | 25.6% | 3.91 |
| Como win | 52.9% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.92 |
| Como expected goals | 1.49 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 70.0% |
| Under 1.5 | 30.0% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.5% |
| Under 3.5 | 77.5% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.71% |
| 2 | 1-1 | 12.03% |
| 3 | 0-2 | 10.53% |
| 4 | 1-2 | 9.68% |
| 5 | 0-0 | 8.90% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.6% | 20.2% | 4.89 | +5.4% |
| Draw | 25.6% | 24.1% | 3.86 | -1.3% |
| Como win | 52.9% | 55.7% | 1.83 | -3.2% |
| Over 2.5 | 43.8% | 54.3% | 1.82 | -20.2% |
| Under 2.5 | 56.2% | 45.7% | 2.15 | +20.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-27T19:45:00+00:00 |
| Fixture id | 7d989a0a7bae47eb957731e97c5bd9c1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:52Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9191 |
| Dc lambda away | 1.4892 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.24 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.33 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.44 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.12 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 22.9% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 50.1% |
| Raw p over 1 5 | 69.8% |
| Raw p under 3 5 | 77.7% |
| Raw p btts yes | 47.0% |
| P home draw | 47.1% |
| P draw away | 78.4% |
| P home away | 74.4% |
| Raw p home draw | 49.9% |
| Raw p draw away | 77.1% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 4.25 |
| Reference draw odds | 3.63 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | 0.0262 |
| Raw ev home | 0.1181 |
| Raw edge prob draw | 0.0296 |
| Raw ev draw | 0.0441 |
| Raw edge prob away | -0.0558 |
| Raw ev away | -0.0835 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **56.3%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.8%; Double Chance 1X: 80.0%; Double Chance X2: 43.7%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 56.3% | 1.78 |
| Draw | 23.7% | 4.21 |
| Bologna win | 20.0% | 5.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.18% |
| 2 | 1-1 | 11.30% |
| 3 | 2-1 | 10.65% |
| 4 | 2-0 | 10.22% |
| 5 | 0-0 | 6.85% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 56.3% | 62.1% | 1.65 | -7.2% |
| Draw | 23.7% | 21.9% | 4.28 | +1.6% |
| Bologna win | 20.0% | 16.0% | 5.71 | +14.3% |
| Over 2.5 | 50.6% | 53.7% | 1.88 | -5.0% |
| Under 2.5 | 49.4% | 46.3% | 2.07 | +2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 3d0b0fbec194258530882514714c74be |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6194 |
| Dc lambda away | 1.0423 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.60 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.04 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.40 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 50.4% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.0% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 80.0% |
| P draw away | 43.7% |
| P home away | 76.3% |
| Raw p home draw | 76.0% |
| Raw p draw away | 49.6% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.52 |
| Reference draw odds | 3.80 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -5.8% |
| Draw probability edge | +1.8% |
| Away probability edge | +4.0% |
| Over 2.5 probability edge | -3.1% |
| Under 2.5 probability edge | +3.1% |
| Raw edge prob home | -0.1169 |
| Raw ev home | -0.1682 |
| Raw edge prob draw | 0.0369 |
| Raw ev draw | 0.0946 |
| Raw edge prob away | 0.0800 |
| Raw ev away | 0.3713 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.9%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.22 combined). The most likely exact score is 0-1 at 16.4%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.0%; Under 3.5 goals: 81.3%; Double Chance 1X: 44.1%; Double Chance X2: 81.8%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.2% | 5.50 |
| Draw | 25.9% | 3.87 |
| Juventus win | 55.9% | 1.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 18.7% |
| Under 3.5 | 81.3% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.37% |
| 2 | 0-2 | 12.03% |
| 3 | 1-1 | 11.74% |
| 4 | 0-0 | 10.51% |
| 5 | 1-2 | 9.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.2% | 16.2% | 5.61 | +2.1% |
| Draw | 25.9% | 23.9% | 4.01 | +3.7% |
| Juventus win | 55.9% | 59.9% | 1.70 | -4.9% |
| Over 2.5 | 39.0% | 46.3% | 2.11 | -17.8% |
| Under 2.5 | 61.0% | 53.7% | 1.85 | +12.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | 34848497b90b1392f6a767fc183d3ac1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7841 |
| Dc lambda away | 1.4309 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.52 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.36 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.08 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.0% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.8% |
| P home draw | 44.1% |
| P draw away | 81.8% |
| P home away | 74.1% |
| Raw p home draw | 48.0% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 4.95 |
| Reference draw odds | 3.53 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +1.9% |
| Draw probability edge | +2.0% |
| Away probability edge | -4.0% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | 0.0389 |
| Raw ev home | 0.1297 |
| Raw edge prob draw | 0.0402 |
| Raw ev draw | 0.1180 |
| Raw edge prob away | -0.0791 |
| Raw ev away | -0.1163 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **57.7%**. Expected goals are 0.82 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.5%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.1%; Double Chance 1X: 42.3%; Double Chance X2: 81.1%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 86.7%; BTTS Yes (both teams score): 48.1%; BTTS No (at least one team does not score): 51.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 18.9% | 5.30 |
| Draw | 23.4% | 4.27 |
| Napoli win | 57.7% | 1.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.82 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.3% |
| Under 4.5 | 86.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.49% |
| 2 | 1-1 | 11.13% |
| 3 | 0-2 | 11.08% |
| 4 | 1-2 | 9.05% |
| 5 | 0-0 | 7.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 18.9% | 22.4% | 4.22 | -20.4% |
| Draw | 23.4% | 24.3% | 3.95 | -7.5% |
| Napoli win | 57.7% | 53.4% | 1.90 | +9.7% |
| Over 2.5 | 49.8% | 55.8% | 1.79 | -10.9% |
| Under 2.5 | 50.2% | 44.2% | 2.19 | +10.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T19:45:00+00:00 |
| Fixture id | abec89862e33762414fcb8b2232aba08 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8165 |
| Dc lambda away | 1.8762 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.1% |
| P btts no | 51.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.53 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.59 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.54 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 15.4% |
| Unadjusted draw probability | 22.6% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 42.3% |
| P draw away | 81.1% |
| P home away | 76.6% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.6% |
| Raw p home away | 77.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 3.80 |
| Reference draw odds | 3.53 |
| Reference away odds | 1.75 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -3.5% |
| Draw probability edge | -0.9% |
| Away probability edge | +4.3% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.0697 |
| Raw ev home | -0.3508 |
| Raw edge prob draw | -0.0173 |
| Raw ev draw | -0.1091 |
| Raw edge prob away | 0.0870 |
| Raw ev away | 0.1792 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.4%**. Expected goals are 1.07 for Parma and 1.14 for Udinese (2.21 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.2%; Under 3.5 goals: 81.7%; Double Chance 1X: 61.6%; Double Chance X2: 67.7%; Double Chance 12 (either team wins): 70.8%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 32.3% | 3.09 |
| Draw | 29.2% | 3.42 |
| Udinese win | 38.4% | 2.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.07 |
| Udinese expected goals | 1.14 |
| Expected total goals | 2.21 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.2% |
| Under 1.5 | 34.8% |
| Over 2.5 | 38.2% |
| Under 2.5 | 61.8% |
| Over 3.5 | 18.3% |
| Under 3.5 | 81.7% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.51% |
| 2 | 0-1 | 12.61% |
| 3 | 0-0 | 11.17% |
| 4 | 1-0 | 10.98% |
| 5 | 1-2 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 32.3% | 31.4% | 3.13 | +1.2% |
| Draw | 29.2% | 28.5% | 3.40 | -0.6% |
| Udinese win | 38.4% | 40.1% | 2.49 | -4.3% |
| Over 2.5 | 38.2% | 43.1% | 2.22 | -15.2% |
| Under 2.5 | 61.8% | 56.9% | 1.77 | +9.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 482c18a8081afdfa310324fa8f37e95a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0692 |
| Dc lambda away | 1.1388 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.95 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.88 |
| Fair Over 2.5 odds | 2.62 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.48 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.52 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 33.3% |
| Unadjusted draw probability | 29.9% |
| Unadjusted away-win probability | 36.8% |
| Raw p over 1 5 | 65.2% |
| Raw p under 3 5 | 81.8% |
| Raw p btts yes | 45.1% |
| P home draw | 61.6% |
| P draw away | 67.7% |
| P home away | 70.8% |
| Raw p home draw | 63.2% |
| Raw p draw away | 66.7% |
| Raw p home away | 70.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.83 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.27 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.67 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +1.0% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.7% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0192 |
| Raw ev home | 0.0417 |
| Raw edge prob draw | 0.0141 |
| Raw ev draw | 0.0181 |
| Raw edge prob away | -0.0332 |
| Raw ev away | -0.0843 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **77.0%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.0%; Under 3.5 goals: 57.2%; Double Chance 1X: 23.0%; Double Chance X2: 91.0%; Double Chance 12 (either team wins): 86.1%; Under 4.5 goals: 75.4%; BTTS Yes (both teams score): 46.9%; BTTS No (at least one team does not score): 53.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 9.0% | 11.09 |
| Draw | 13.9% | 7.17 |
| Inter Milan win | 77.0% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.6% |
| Under 4.5 | 75.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.05% |
| 2 | 0-3 | 10.74% |
| 3 | 0-1 | 8.81% |
| 4 | 1-2 | 8.31% |
| 5 | 1-3 | 7.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 9.0% | 11.1% | 8.55 | -22.9% |
| Draw | 13.9% | 14.0% | 6.28 | -12.5% |
| Inter Milan win | 77.0% | 75.0% | 1.35 | +4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-28T17:30:00+00:00 |
| Fixture id | 33320ad169692216a91dec030e7ef6a6 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 1.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6899 |
| Dc lambda away | 2.6725 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 46.9% |
| P btts no | 53.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.11 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.53 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.85 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.07 |
| Fair Under 4.5 odds | 1.33 |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.1% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.7% |
| Raw p btts yes | 46.6% |
| P home draw | 23.0% |
| P draw away | 91.0% |
| P home away | 86.1% |
| Raw p home draw | 20.9% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 6.60 |
| Reference draw odds | 5.40 |
| Reference away odds | 1.28 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Home probability edge | -2.0% |
| Draw probability edge | -0.0% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0407 |
| Raw ev home | -0.4029 |
| Raw edge prob draw | -0.0007 |
| Raw ev draw | -0.1267 |
| Raw edge prob away | 0.0414 |
| Raw ev away | 0.0680 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **37.9%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.8%; Under 3.5 goals: 68.5%; Double Chance 1X: 62.1%; Double Chance X2: 63.5%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 36.5% | 2.74 |
| Draw | 25.7% | 3.90 |
| Atalanta BC win | 37.9% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 1.25 |
| Atalanta BC expected goals | 1.59 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 53.8% |
| Under 2.5 | 46.2% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.10% |
| 2 | 2-1 | 8.91% |
| 3 | 1-0 | 8.47% |
| 4 | 1-2 | 7.80% |
| 5 | 0-1 | 7.50% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 36.5% | 43.1% | 2.40 | -12.5% |
| Draw | 25.7% | 25.9% | 3.69 | -5.3% |
| Atalanta BC win | 37.9% | 31.0% | 3.06 | +15.9% |
| Over 2.5 | 53.8% | 54.7% | 1.78 | -4.2% |
| Under 2.5 | 46.2% | 45.3% | 2.21 | +2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T19:45:00+00:00 |
| Fixture id | da159a6b84dbb548b4d7b94c722caac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2541 |
| Dc lambda away | 1.5889 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.96 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.35 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 29.8% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.8% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.3% |
| P home draw | 62.1% |
| P draw away | 63.5% |
| P home away | 74.3% |
| Raw p home draw | 55.2% |
| Raw p draw away | 70.2% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 2.12 |
| Reference draw odds | 3.35 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | -6.7% |
| Draw probability edge | -0.2% |
| Away probability edge | +6.9% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.1338 |
| Raw ev home | -0.2855 |
| Raw edge prob draw | -0.0042 |
| Raw ev draw | -0.0610 |
| Raw edge prob away | 0.1379 |
| Raw ev away | 0.3703 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.7%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-0 at 12.0%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 46.8%; Under 3.5 goals: 75.0%; Double Chance 1X: 75.9%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.3%; BTTS No (at least one team does not score): 50.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.7% | 1.97 |
| Draw | 25.2% | 3.98 |
| Lecce win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 72.4% |
| Under 1.5 | 27.6% |
| Over 2.5 | 46.8% |
| Under 2.5 | 53.2% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.00% |
| 2 | 1-1 | 11.95% |
| 3 | 2-0 | 9.70% |
| 4 | 2-1 | 9.41% |
| 5 | 0-0 | 8.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.7% | 50.7% | 2.01 | +2.0% |
| Draw | 25.2% | 24.1% | 3.85 | -3.2% |
| Lecce win | 24.1% | 25.1% | 3.93 | -5.3% |
| Over 2.5 | 46.8% | 60.5% | 1.69 | -20.9% |
| Under 2.5 | 53.2% | 39.5% | 2.37 | +26.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-29T17:30:00+00:00 |
| Fixture id | 667cf69986b200753742c90cb9c5126c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-20T05:42:54Z |
| Market best draw last update utc | 2026-10-20T05:42:54Z |
| Market best away last update utc | 2026-10-20T05:42:52Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 4.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5635 |
| Dc lambda away | 0.9704 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-20T05:43:07.772166+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.3% |
| P btts no | 50.7% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.49 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.00 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.75 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 75.9% |
| P draw away | 49.3% |
| P home away | 74.8% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Betclic (FR) |
| Reference home odds | 1.83 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.42 |
| Market reference 1x2 last update utc | 2026-10-20T05:43:03Z |
| Market reference home last update utc | 2026-10-20T05:43:03Z |
| Market reference draw last update utc | 2026-10-20T05:43:03Z |
| Market reference away last update utc | 2026-10-20T05:43:03Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market reference under 2 5 last update utc | 2026-10-20T05:42:55Z |
| Market best over 2 5 last update utc | 2026-10-20T05:42:54Z |
| Market best under 2 5 last update utc | 2026-10-20T05:42:54Z |
| Home probability edge | +0.0% |
| Draw probability edge | +1.0% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -13.7% |
| Under 2.5 probability edge | +13.7% |
| Raw edge prob home | 0.0000 |
| Raw ev home | 0.0199 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | 0.0086 |
| Raw edge prob away | -0.0209 |
| Raw ev away | -0.0937 |

</details>


---
