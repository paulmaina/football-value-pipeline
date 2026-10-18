# Premier League — football model report

Fixtures in this report: **15**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,205 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 365 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | ff75dd96de15007c8cc41acef6b16ce522ef237c4977a391c2e0a0df9ffc8e13 |
| Training as of utc | 2026-10-18T11:56:28.580790+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 65, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 65, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:56:28.580790+00:00', 'observations': 78, 'observations_sha256': '450aea933785c85418c78670ab356ec59d4c2865409b43720840f601937b8288', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 48, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 4, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'e32ff2d076e239f96dd776a89521890955df11fd7826b407263adc2a3514fbeb', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 1310.670 |
| Base scoring parameter | 0.223 |
| Home-advantage parameter | 0.165 |
| Dixon-Coles low-score adjustment | -0.092 |
| Xi per day | 0.0019 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261018T115628580790Z_3cbcb41cf5e6dda389149b92aebc8cba0d8fba7de38934a23187b296e07891ec.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-18 — Bournemouth vs Sunderland

The model's most likely 1X2 outcome is **Bournemouth win** at **47.5%**. Expected goals are 1.54 for Bournemouth and 1.05 for Sunderland (2.59 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 47.9%; Under 3.5 goals: 73.7%; Double Chance 1X: 75.5%; Double Chance X2: 52.5%; Double Chance 12 (either team wins): 72.0%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 47.5% | 2.11 |
| Draw | 28.0% | 3.57 |
| Sunderland win | 24.5% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.54 |
| Sunderland expected goals | 1.05 |
| Expected total goals | 2.59 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 74.2% |
| Under 1.5 | 25.8% |
| Over 2.5 | 47.9% |
| Under 2.5 | 52.1% |
| Over 3.5 | 26.3% |
| Under 3.5 | 73.7% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.39% |
| 2 | 1-0 | 10.41% |
| 3 | 2-1 | 9.36% |
| 4 | 2-0 | 8.87% |
| 5 | 0-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 47.5% | 47.6% | 2.14 | +1.6% |
| Draw | 28.0% | 28.3% | 3.43 | -3.8% |
| Sunderland win | 24.5% | 24.1% | 3.90 | -4.5% |
| Over 2.5 | 47.9% | 44.3% | 2.15 | +3.0% |
| Under 2.5 | 52.1% | 55.7% | 1.81 | -5.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | dfd5d6648be46426e418801584d46a68 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bournemouth |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5390 |
| Dc lambda away | 1.0544 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.52 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.88 |
| Fair Over 2.5 odds | 2.09 |
| Fair Under 2.5 odds | 1.92 |
| Fair Over 3.5 odds | 3.81 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.24 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 47.4% |
| Unadjusted draw probability | 27.7% |
| Unadjusted away-win probability | 24.9% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 73.7% |
| Raw p btts yes | 52.3% |
| P home draw | 75.5% |
| P draw away | 52.5% |
| P home away | 72.0% |
| Raw p home draw | 75.1% |
| Raw p draw away | 52.6% |
| Raw p home away | 72.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -0.1% |
| Draw probability edge | -0.3% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | +3.6% |
| Under 2.5 probability edge | -3.6% |
| Raw edge prob home | -0.0020 |
| Raw ev home | 0.0140 |
| Raw edge prob draw | -0.0059 |
| Raw ev draw | -0.0485 |
| Raw edge prob away | 0.0080 |
| Raw ev away | -0.0298 |
| Market p home draw | 75.2% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:10Z |
| Market reference home draw last update utc | 2026-10-18T11:56:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 53.5% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:10Z |
| Market reference draw away last update utc | 2026-10-18T11:56:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.3% |
| Market home away odds | 1.36 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:10Z |
| Market reference home away last update utc | 2026-10-18T11:56:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.26 |
| Market reference dc draw away odds | 1.77 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 71.7% |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 2.95 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:30Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 76.8% |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.45 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:30Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.6% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:10Z |
| Market reference btts yes odds | 1.95 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-18T11:56:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Brighton and Hove Albion vs Crystal Palace

The model's most likely 1X2 outcome is **Brighton and Hove Albion win** at **61.9%**. Expected goals are 1.85 for Brighton and Hove Albion and 1.08 for Crystal Palace (2.93 combined). The most likely exact score is 2-1 at 11.2%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 57.5%; Under 3.5 goals: 65.6%; Double Chance 1X: 83.3%; Double Chance X2: 38.1%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 55.5%; BTTS No (at least one team does not score): 44.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brighton and Hove Albion win | 61.9% | 1.62 |
| Draw | 21.4% | 4.66 |
| Crystal Palace win | 16.7% | 6.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brighton and Hove Albion expected goals | 1.85 |
| Crystal Palace expected goals | 1.08 |
| Expected total goals | 2.93 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 80.6% |
| Under 1.5 | 19.4% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.20% |
| 2 | 2-0 | 10.40% |
| 3 | 1-1 | 10.14% |
| 4 | 1-0 | 10.12% |
| 5 | 3-1 | 6.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brighton and Hove Albion win | 61.9% | 69.2% | 1.51 | -6.5% |
| Draw | 21.4% | 18.3% | 4.93 | +5.7% |
| Crystal Palace win | 16.7% | 12.5% | 6.63 | +10.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 9fc08b390a49c4434f7cf631a0bb88fb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Brighton |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8529 |
| Dc lambda away | 1.0769 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 55.5% |
| P btts no | 44.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.16 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.14 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.90 |
| Fair Under 3.5 odds | 1.53 |
| Fair Over 4.5 odds | 5.55 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 54.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 20.9% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 66.3% |
| Raw p btts yes | 56.6% |
| P home draw | 83.3% |
| P draw away | 38.1% |
| P home away | 78.6% |
| Raw p home draw | 79.1% |
| Raw p draw away | 45.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.41 |
| Reference draw odds | 4.90 |
| Reference away odds | 7.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -7.4% |
| Draw probability edge | +3.2% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | -0.1471 |
| Raw ev home | -0.1765 |
| Raw edge prob draw | 0.0634 |
| Raw ev draw | 0.2132 |
| Raw edge prob away | 0.0838 |
| Raw ev away | 0.3827 |
| Market p home draw | 84.8% |
| Market home draw odds | 1.14 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:10Z |
| Market reference home draw last update utc | 2026-10-18T11:56:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.7% |
| Market draw away odds | 2.75 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:10Z |
| Market reference draw away last update utc | 2026-10-18T11:56:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.5% |
| Market home away odds | 1.22 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:10Z |
| Market reference home away last update utc | 2026-10-18T11:56:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.74 |
| Market reference dc home away odds | 1.18 |
| Market p over 1 5 | 84.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:30Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.6% |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.26 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:30Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.4% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:10Z |
| Market reference btts yes odds | 1.79 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-18T11:56:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Leeds United vs Manchester United

The model's most likely 1X2 outcome is **Leeds United win** at **38.7%**. Expected goals are 1.42 for Leeds United and 1.29 for Manchester United (2.71 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 51.1%; Under 3.5 goals: 71.1%; Double Chance 1X: 65.9%; Double Chance X2: 61.3%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 86.0%; BTTS Yes (both teams score): 56.0%; BTTS No (at least one team does not score): 44.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Leeds United win | 38.7% | 2.59 |
| Draw | 27.3% | 3.67 |
| Manchester United win | 34.1% | 2.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Leeds United expected goals | 1.42 |
| Manchester United expected goals | 1.29 |
| Expected total goals | 2.71 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.1% |
| Under 2.5 | 48.9% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 14.0% |
| Under 4.5 | 86.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.00% |
| 2 | 2-1 | 8.58% |
| 3 | 1-0 | 8.24% |
| 4 | 1-2 | 8.10% |
| 5 | 0-1 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Leeds United win | 38.7% | 38.3% | 2.57 | -0.6% |
| Draw | 27.3% | 26.6% | 3.52 | -4.0% |
| Manchester United win | 34.1% | 35.0% | 2.92 | -0.6% |
| Over 2.5 | 51.1% | 52.4% | 1.92 | -1.8% |
| Under 2.5 | 48.9% | 47.6% | 2.02 | -1.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 676b3b0b609e9cf565da450786618d26 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Leeds |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4201 |
| Dc lambda away | 1.2914 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.0% |
| P btts no | 44.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.19 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.25 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.05 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.16 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 39.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 33.1% |
| Raw p over 1 5 | 76.5% |
| Raw p under 3 5 | 71.2% |
| Raw p btts yes | 56.1% |
| P home draw | 65.9% |
| P draw away | 61.3% |
| P home away | 72.7% |
| Raw p home draw | 66.9% |
| Raw p draw away | 61.0% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.48 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.6% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0067 |
| Raw ev home | 0.0021 |
| Raw edge prob draw | 0.0129 |
| Raw ev draw | -0.0169 |
| Raw edge prob away | -0.0196 |
| Raw ev away | -0.0341 |
| Market p home draw | 64.6% |
| Market home draw odds | 1.46 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:10Z |
| Market reference home draw last update utc | 2026-10-18T11:56:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.4% |
| Market draw away odds | 1.57 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:10Z |
| Market reference draw away last update utc | 2026-10-18T11:56:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.35 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:10Z |
| Market reference home away last update utc | 2026-10-18T11:56:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.47 |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 76.2% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:56:15Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:30Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.7% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:56:15Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 2.95 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:30Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:10Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-18T11:56:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Nottingham Forest vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **58.8%**. Expected goals are 0.77 for Nottingham Forest and 1.59 for Arsenal (2.36 combined). The most likely exact score is 0-1 at 14.7%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.4%; Double Chance 1X: 41.2%; Double Chance X2: 84.1%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 90.7%; BTTS Yes (both teams score): 43.3%; BTTS No (at least one team does not score): 56.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Nottingham Forest win | 15.9% | 6.29 |
| Draw | 25.3% | 3.95 |
| Arsenal win | 58.8% | 1.70 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Nottingham Forest expected goals | 0.77 |
| Arsenal expected goals | 1.59 |
| Expected total goals | 2.36 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 69.7% |
| Under 1.5 | 30.3% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.6% |
| Under 3.5 | 78.4% |
| Over 4.5 | 9.3% |
| Under 4.5 | 90.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.71% |
| 2 | 0-2 | 12.56% |
| 3 | 1-1 | 11.75% |
| 4 | 0-0 | 9.79% |
| 5 | 1-2 | 9.69% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Nottingham Forest win | 15.9% | 14.8% | 5.89 | -6.3% |
| Draw | 25.3% | 23.4% | 4.00 | +1.3% |
| Arsenal win | 58.8% | 61.8% | 1.68 | -1.3% |
| Over 2.5 | 42.7% | 50.4% | 1.90 | -18.8% |
| Under 2.5 | 57.3% | 49.6% | 2.05 | +17.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T15:30:00+00:00 |
| Fixture id | f696a248965373d9071dc0662e5c58a8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 18.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Nott'm Forest |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7711 |
| Dc lambda away | 1.5869 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.3% |
| P btts no | 56.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.22 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.30 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.75 |
| Fair Over 3.5 odds | 4.64 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.74 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 55.7% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.7% |
| Raw p btts yes | 43.8% |
| P home draw | 41.2% |
| P draw away | 84.1% |
| P home away | 74.7% |
| Raw p home draw | 44.3% |
| Raw p draw away | 83.0% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 6.00 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.57 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | +1.1% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0225 |
| Raw ev home | 0.0034 |
| Raw edge prob draw | 0.0381 |
| Raw ev draw | 0.0890 |
| Raw edge prob away | -0.0606 |
| Raw ev away | -0.0636 |
| Market p home draw | 41.6% |
| Market home draw odds | 2.33 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:10Z |
| Market reference home draw last update utc | 2026-10-18T11:56:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 82.5% |
| Market draw away odds | 1.17 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:10Z |
| Market reference draw away last update utc | 2026-10-18T11:56:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:10Z |
| Market reference home away last update utc | 2026-10-18T11:56:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.28 |
| Market reference dc draw away odds | 1.15 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 77.6% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:55:46Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:30Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.1% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:55:46Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 2.85 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:30Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 50.8% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:10Z |
| Market reference btts yes odds | 1.96 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-18T11:56:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Tottenham Hotspur vs Coventry City

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **57.9%**. Expected goals are 1.59 for Tottenham Hotspur and 1.05 for Coventry City (2.64 combined). The most likely exact score is 1-0 at 12.2%. Goal-market probabilities: at least one goal: 92.9%; Over 2.5 goals: 50.8%; Under 3.5 goals: 72.1%; Double Chance 1X: 81.2%; Double Chance X2: 42.1%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 57.9% | 1.73 |
| Draw | 23.4% | 4.28 |
| Coventry City win | 18.8% | 5.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.59 |
| Coventry City expected goals | 1.05 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.9% |
| Under 0.5 | 7.1% |
| Over 1.5 | 75.7% |
| Under 1.5 | 24.3% |
| Over 2.5 | 50.8% |
| Under 2.5 | 49.2% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.19% |
| 2 | 2-1 | 11.26% |
| 3 | 1-1 | 11.16% |
| 4 | 2-0 | 10.70% |
| 5 | 0-0 | 7.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 57.9% | 67.1% | 1.54 | -10.9% |
| Draw | 23.4% | 19.5% | 4.67 | +9.1% |
| Coventry City win | 18.8% | 13.4% | 6.50 | +22.0% |
| Over 2.5 | 50.8% | 61.3% | 1.64 | -16.7% |
| Under 2.5 | 49.2% | 38.7% | 2.46 | +21.0% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5855 |
| Dc lambda away | 1.0527 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.16 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.12 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 75.1% |
| Raw p under 3 5 | 72.8% |
| Raw p btts yes | 52.9% |
| P home draw | 81.2% |
| P draw away | 42.1% |
| P home away | 76.6% |
| Raw p home draw | 75.9% |
| Raw p draw away | 51.4% |
| Raw p home away | 72.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.45 |
| Reference draw odds | 4.60 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -9.3% |
| Draw probability edge | +3.9% |
| Away probability edge | +5.3% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.1851 |
| Raw ev home | -0.2513 |
| Raw edge prob draw | 0.0783 |
| Raw ev draw | 0.2739 |
| Raw edge prob away | 0.1068 |
| Raw ev away | 0.5669 |
| Market p home draw | 84.1% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:10Z |
| Market reference home draw last update utc | 2026-10-18T11:56:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.0% |
| Market draw away odds | 2.64 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:10Z |
| Market reference draw away last update utc | 2026-10-18T11:56:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:10Z |
| Market reference home away last update utc | 2026-10-18T11:56:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.13 |
| Market reference dc draw away odds | 2.64 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.16 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-18T11:56:30Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.4% |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-18T11:56:30Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 55.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:10Z |
| Market reference btts yes odds | 1.77 |
| Market reference btts yes opposite odds | 2.22 |
| Market reference btts yes last update utc | 2026-10-18T11:56:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **46.7%**. Expected goals are 1.22 for Ipswich Town and 1.78 for Nottingham Forest (3.00 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.4%; Under 3.5 goals: 64.8%; Double Chance 1X: 53.3%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 81.6%; BTTS Yes (both teams score): 59.9%; BTTS No (at least one team does not score): 40.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 27.4% | 3.65 |
| Draw | 25.9% | 3.86 |
| Nottingham Forest win | 46.7% | 2.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.22 |
| Nottingham Forest expected goals | 1.78 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 35.2% |
| Under 3.5 | 64.8% |
| Over 4.5 | 18.4% |
| Under 4.5 | 81.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.09% |
| 2 | 1-2 | 9.06% |
| 3 | 0-2 | 7.43% |
| 4 | 0-1 | 7.40% |
| 5 | 2-1 | 7.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 27.4% | 29.6% | 3.10 | -15.1% |
| Draw | 25.9% | 26.6% | 3.63 | -6.0% |
| Nottingham Forest win | 46.7% | 43.8% | 2.39 | +11.7% |
| Over 2.5 | 57.4% | 53.2% | 1.84 | +5.7% |
| Under 2.5 | 42.6% | 46.8% | 2.12 | -9.8% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2200 |
| Dc lambda away | 1.7839 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.9% |
| P btts no | 40.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.38 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.26 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.84 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.45 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 25.1% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 49.6% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 59.6% |
| P home draw | 53.3% |
| P draw away | 72.6% |
| P home away | 74.1% |
| Raw p home draw | 50.4% |
| Raw p draw away | 74.9% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -2.2% |
| Draw probability edge | -0.7% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | +4.3% |
| Under 2.5 probability edge | -4.3% |
| Raw edge prob home | -0.0447 |
| Raw ev home | -0.2207 |
| Raw edge prob draw | -0.0133 |
| Raw ev draw | -0.0838 |
| Raw edge prob away | 0.0580 |
| Raw ev away | 0.1860 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.2%**. Expected goals are 1.71 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.5%; Under 3.5 goals: 79.6%; Double Chance 1X: 89.1%; Double Chance X2: 32.8%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.4%; BTTS No (at least one team does not score): 63.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.2% | 1.49 |
| Draw | 21.8% | 4.59 |
| Everton win | 10.9% | 9.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.71 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
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
| 1 | 1-0 | 17.18% |
| 2 | 2-0 | 15.52% |
| 3 | 0-0 | 9.67% |
| 4 | 1-1 | 9.66% |
| 5 | 2-1 | 9.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.2% | 70.6% | 1.43 | -3.8% |
| Draw | 21.8% | 18.8% | 4.93 | +7.5% |
| Everton win | 10.9% | 10.6% | 8.90 | -2.6% |
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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7101 |
| Dc lambda away | 0.5843 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.4% |
| P btts no | 63.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.34 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.90 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.58 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 11.3% |
| Raw p over 1 5 | 67.7% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 37.2% |
| P home draw | 89.1% |
| P draw away | 32.8% |
| P home away | 78.2% |
| Raw p home draw | 88.7% |
| Raw p draw away | 36.1% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.38 |
| Reference draw odds | 4.70 |
| Reference away odds | 8.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -3.4% |
| Draw probability edge | +3.0% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -11.0% |
| Under 2.5 probability edge | +11.0% |
| Raw edge prob home | -0.0675 |
| Raw ev home | -0.0866 |
| Raw edge prob draw | 0.0602 |
| Raw ev draw | 0.2236 |
| Raw edge prob away | 0.0072 |
| Raw ev away | 0.0063 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.4%**. Expected goals are 1.14 for Aston Villa and 1.83 for Manchester City (2.97 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.7%; Under 3.5 goals: 65.1%; Double Chance 1X: 44.6%; Double Chance X2: 78.8%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 81.7%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.2% | 4.71 |
| Draw | 23.4% | 4.28 |
| Manchester City win | 55.4% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.14 |
| Manchester City expected goals | 1.83 |
| Expected total goals | 2.97 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 34.9% |
| Under 3.5 | 65.1% |
| Over 4.5 | 18.3% |
| Under 4.5 | 81.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.99% |
| 2 | 1-2 | 10.31% |
| 3 | 0-2 | 9.05% |
| 4 | 0-1 | 8.84% |
| 5 | 1-3 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.2% | 19.9% | 4.72 | +0.2% |
| Draw | 23.4% | 21.9% | 4.26 | -0.4% |
| Manchester City win | 55.4% | 58.1% | 1.76 | -2.5% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1389 |
| Dc lambda away | 1.8337 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.41 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.22 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.86 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.46 |
| Fair Under 4.5 odds | 1.22 |
| Unadjusted home-win probability | 22.5% |
| Unadjusted draw probability | 24.8% |
| Unadjusted away-win probability | 52.6% |
| Raw p over 1 5 | 80.7% |
| Raw p under 3 5 | 65.3% |
| Raw p btts yes | 58.1% |
| P home draw | 44.6% |
| P draw away | 78.8% |
| P home away | 76.6% |
| Raw p home draw | 47.4% |
| Raw p draw away | 77.5% |
| Raw p home away | 75.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.60 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.67 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:30Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0261 |
| Raw ev home | 0.0635 |
| Raw edge prob draw | 0.0289 |
| Raw ev draw | 0.0575 |
| Raw edge prob away | -0.0550 |
| Raw ev away | -0.0735 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **55.1%**. Expected goals are 2.10 for Chelsea and 1.22 for Tottenham Hotspur (3.32 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.4%; Under 3.5 goals: 57.7%; Double Chance 1X: 77.8%; Double Chance X2: 44.9%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 76.0%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 55.1% | 1.82 |
| Draw | 22.7% | 4.40 |
| Tottenham Hotspur win | 22.2% | 4.51 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.10 |
| Tottenham Hotspur expected goals | 1.22 |
| Expected total goals | 3.32 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.4% |
| Under 2.5 | 35.6% |
| Over 3.5 | 42.3% |
| Under 3.5 | 57.7% |
| Over 4.5 | 24.0% |
| Under 4.5 | 76.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.22% |
| 2 | 2-1 | 9.42% |
| 3 | 2-0 | 7.73% |
| 4 | 3-1 | 6.61% |
| 5 | 1-0 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 55.1% | 53.3% | 1.90 | +4.7% |
| Draw | 22.7% | 23.0% | 4.11 | -6.5% |
| Tottenham Hotspur win | 22.2% | 23.6% | 4.06 | -10.0% |
| Over 2.5 | 64.4% | 61.0% | 1.66 | +6.8% |
| Under 2.5 | 35.6% | 39.0% | 2.42 | -13.8% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1049 |
| Dc lambda away | 1.2190 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.19 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.75 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.73 |
| Fair Over 4.5 odds | 4.16 |
| Fair Under 4.5 odds | 1.32 |
| Unadjusted home-win probability | 56.9% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 20.7% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.7% |
| P home draw | 77.8% |
| P draw away | 44.9% |
| P home away | 77.3% |
| Raw p home draw | 79.3% |
| Raw p draw away | 43.1% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.83 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:30Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | +1.8% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.5% |
| Over 2.5 probability edge | +3.4% |
| Under 2.5 probability edge | -3.4% |
| Raw edge prob home | 0.0353 |
| Raw ev home | 0.0802 |
| Raw edge prob draw | -0.0058 |
| Raw ev draw | -0.0770 |
| Raw edge prob away | -0.0294 |
| Raw ev away | -0.1599 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **40.3%**. Expected goals are 1.09 for Coventry City and 1.27 for Fulham (2.35 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 42.5%; Under 3.5 goals: 78.8%; Double Chance 1X: 59.7%; Double Chance X2: 68.5%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 48.3%; BTTS No (at least one team does not score): 51.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 31.5% | 3.17 |
| Draw | 28.2% | 3.55 |
| Fulham win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.09 |
| Fulham expected goals | 1.27 |
| Expected total goals | 2.35 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 42.5% |
| Under 2.5 | 57.5% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.2% |
| Under 4.5 | 90.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.32% |
| 2 | 0-1 | 11.13% |
| 3 | 0-0 | 10.00% |
| 4 | 1-0 | 9.46% |
| 5 | 1-2 | 8.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 31.5% | 32.6% | 3.12 | -1.7% |
| Draw | 28.2% | 26.1% | 3.61 | +1.8% |
| Fulham win | 40.3% | 41.3% | 2.39 | -3.7% |
| Over 2.5 | 42.5% | 54.9% | 1.81 | -23.1% |
| Under 2.5 | 57.5% | 45.1% | 2.15 | +23.7% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0850 |
| Dc lambda away | 1.2662 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.3% |
| P btts no | 51.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.00 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.35 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.71 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.90 |
| Fair Under 4.5 odds | 1.10 |
| Unadjusted home-win probability | 30.4% |
| Unadjusted draw probability | 30.3% |
| Unadjusted away-win probability | 39.3% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 48.7% |
| P home draw | 59.7% |
| P draw away | 68.5% |
| P home away | 71.8% |
| Raw p home draw | 60.7% |
| Raw p draw away | 69.6% |
| Raw p home away | 69.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -1.1% |
| Draw probability edge | +2.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.0215 |
| Raw ev home | -0.0501 |
| Raw edge prob draw | 0.0411 |
| Raw ev draw | 0.0923 |
| Raw edge prob away | -0.0196 |
| Raw ev away | -0.0608 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **37.4%**. Expected goals are 1.48 for Crystal Palace and 1.52 for Newcastle United (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.8%; Under 3.5 goals: 64.6%; Double Chance 1X: 62.6%; Double Chance X2: 63.8%; Double Chance 12 (either team wins): 73.6%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 36.2% | 2.76 |
| Draw | 26.4% | 3.79 |
| Newcastle United win | 37.4% | 2.67 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.48 |
| Newcastle United expected goals | 1.52 |
| Expected total goals | 3.01 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.24% |
| 2 | 1-2 | 8.44% |
| 3 | 2-1 | 8.34% |
| 4 | 0-1 | 6.46% |
| 5 | 1-0 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 36.2% | 36.4% | 2.76 | -0.2% |
| Draw | 26.4% | 26.5% | 3.69 | -2.6% |
| Newcastle United win | 37.4% | 37.1% | 2.61 | -2.3% |
| Over 2.5 | 57.8% | 57.8% | 1.69 | -2.4% |
| Under 2.5 | 42.2% | 42.2% | 2.36 | -0.3% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4826 |
| Dc lambda away | 1.5229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.68 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.39 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 36.0% |
| Unadjusted draw probability | 26.3% |
| Unadjusted away-win probability | 37.7% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 61.5% |
| P home draw | 62.6% |
| P draw away | 63.8% |
| P home away | 73.6% |
| Raw p home draw | 62.3% |
| Raw p draw away | 64.0% |
| Raw p home away | 73.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -0.2% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.3% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0044 |
| Raw ev home | -0.0077 |
| Raw edge prob draw | -0.0016 |
| Raw ev draw | -0.0287 |
| Raw edge prob away | 0.0061 |
| Raw ev away | -0.0154 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **42.7%**. Expected goals are 1.24 for Hull City and 1.05 for Brentford (2.29 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.1%; Under 3.5 goals: 80.3%; Double Chance 1X: 57.3%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 46.7%; BTTS No (at least one team does not score): 53.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 30.2% | 3.31 |
| Draw | 27.2% | 3.68 |
| Brentford win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.24 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 41.1% |
| Under 2.5 | 58.9% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.47% |
| 2 | 1-1 | 12.73% |
| 3 | 0-0 | 10.06% |
| 4 | 1-2 | 9.86% |
| 5 | 1-0 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 30.2% | 20.9% | 4.72 | +42.4% |
| Draw | 27.2% | 23.6% | 4.09 | +11.1% |
| Brentford win | 42.7% | 55.5% | 1.79 | -23.6% |
| Over 2.5 | 41.1% | 56.7% | 1.73 | -28.9% |
| Under 2.5 | 58.9% | 43.3% | 2.28 | +34.3% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2404 |
| Dc lambda away | 1.0458 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.7% |
| P btts no | 53.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.43 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.86 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 39.5% |
| Unadjusted draw probability | 30.7% |
| Unadjusted away-win probability | 29.8% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 47.3% |
| P home draw | 57.3% |
| P draw away | 69.8% |
| P home away | 72.8% |
| Raw p home draw | 70.2% |
| Raw p draw away | 60.5% |
| Raw p home away | 69.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.00 |
| Reference away odds | 1.76 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | +9.3% |
| Draw probability edge | +3.6% |
| Away probability edge | -12.8% |
| Over 2.5 probability edge | -15.6% |
| Under 2.5 probability edge | +15.6% |
| Raw edge prob home | 0.1857 |
| Raw ev home | 0.8621 |
| Raw edge prob draw | 0.0711 |
| Raw ev draw | 0.2564 |
| Raw edge prob away | -0.2568 |
| Raw ev away | -0.4661 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **47.3%**. Expected goals are 1.79 for Liverpool and 1.35 for Brighton and Hove Albion (3.13 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.9%; Under 3.5 goals: 61.7%; Double Chance 1X: 71.7%; Double Chance X2: 52.7%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 62.4%; BTTS No (at least one team does not score): 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 47.3% | 2.11 |
| Draw | 24.4% | 4.10 |
| Brighton and Hove Albion win | 28.3% | 3.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.79 |
| Brighton and Hove Albion expected goals | 1.35 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 60.9% |
| Under 2.5 | 39.1% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.14% |
| 2 | 2-1 | 9.45% |
| 3 | 1-2 | 7.12% |
| 4 | 2-0 | 7.02% |
| 5 | 1-0 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 47.3% | 47.7% | 2.11 | -0.1% |
| Draw | 24.4% | 23.7% | 4.00 | -2.5% |
| Brighton and Hove Albion win | 28.3% | 28.5% | 3.43 | -3.0% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7884 |
| Dc lambda away | 1.3464 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 62.4% |
| P btts no | 37.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.32 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.79 |
| Fair Under 4.5 odds | 1.26 |
| Unadjusted home-win probability | 46.9% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 28.0% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 61.7% |
| Raw p btts yes | 62.6% |
| P home draw | 71.7% |
| P draw away | 52.7% |
| P home away | 75.6% |
| Raw p home draw | 72.0% |
| Raw p draw away | 53.1% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.04 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.35 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / MyBookie.ag |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:30Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:30Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0078 |
| Raw ev home | -0.0094 |
| Raw edge prob draw | 0.0129 |
| Raw ev draw | 0.0010 |
| Raw edge prob away | -0.0050 |
| Raw ev away | -0.0387 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **49.9%**. Expected goals are 1.72 for Manchester United and 1.31 for Bournemouth (3.03 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.7%; Double Chance 1X: 73.8%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 80.6%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 49.9% | 2.00 |
| Draw | 23.8% | 4.20 |
| Bournemouth win | 26.2% | 3.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.72 |
| Bournemouth expected goals | 1.31 |
| Expected total goals | 3.03 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 81.8% |
| Under 1.5 | 18.2% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.4% |
| Under 4.5 | 80.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 2-1 | 10.14% |
| 3 | 1-0 | 7.89% |
| 4 | 2-0 | 7.73% |
| 5 | 1-2 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 49.9% | 53.8% | 1.86 | -7.1% |
| Draw | 23.8% | 22.0% | 4.26 | +1.5% |
| Bournemouth win | 26.2% | 24.1% | 4.11 | +7.8% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7216 |
| Dc lambda away | 1.3131 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.51 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.49 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.75 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.15 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 46.1% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 28.3% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 61.0% |
| P home draw | 73.8% |
| P draw away | 50.1% |
| P home away | 76.2% |
| Raw p home draw | 71.7% |
| Raw p draw away | 53.9% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 1.80 |
| Reference draw odds | 4.20 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -3.9% |
| Draw probability edge | +1.8% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -6.3% |
| Under 2.5 probability edge | +6.3% |
| Raw edge prob home | -0.0774 |
| Raw ev home | -0.1429 |
| Raw edge prob draw | 0.0357 |
| Raw ev draw | 0.0907 |
| Raw edge prob away | 0.0417 |
| Raw ev away | 0.1639 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **36.4%**. Expected goals are 1.10 for Sunderland and 1.20 for Leeds United (2.30 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 89.1%; Over 2.5 goals: 40.6%; Under 3.5 goals: 80.0%; Double Chance 1X: 63.6%; Double Chance X2: 66.3%; Double Chance 12 (either team wins): 70.1%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 47.6%; BTTS No (at least one team does not score): 52.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 33.7% | 2.97 |
| Draw | 29.9% | 3.35 |
| Leeds United win | 36.4% | 2.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.10 |
| Leeds United expected goals | 1.20 |
| Expected total goals | 2.30 |
| Over 0.5 | 89.1% |
| Under 0.5 | 10.9% |
| Over 1.5 | 68.1% |
| Under 1.5 | 31.9% |
| Over 2.5 | 40.6% |
| Under 2.5 | 59.4% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.03% |
| 2 | 0-0 | 10.94% |
| 3 | 0-1 | 10.66% |
| 4 | 1-0 | 10.30% |
| 5 | 1-2 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 33.7% | 35.2% | 2.90 | -2.3% |
| Draw | 29.9% | 28.9% | 3.44 | +2.7% |
| Leeds United win | 36.4% | 35.9% | 2.63 | -4.1% |
| Over 2.5 | 40.6% | 44.8% | 2.14 | -13.1% |
| Under 2.5 | 59.4% | 55.2% | 1.83 | +8.7% |

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
| Market best home last update utc | 2026-10-18T11:56:10Z |
| Market best draw last update utc | 2026-10-18T11:56:10Z |
| Market best away last update utc | 2026-10-18T11:56:10Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0996 |
| Dc lambda away | 1.1972 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:56:28.580790+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 47.6% |
| P btts no | 52.4% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.14 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.46 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.99 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.88 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 32.2% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 37.0% |
| Raw p over 1 5 | 68.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 47.8% |
| P home draw | 63.6% |
| P draw away | 66.3% |
| P home away | 70.1% |
| Raw p home draw | 63.0% |
| Raw p draw away | 67.8% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / LeoVegas (SE) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.65 |
| Market reference 1x2 last update utc | 2026-10-18T11:56:31Z |
| Market reference home last update utc | 2026-10-18T11:56:31Z |
| Market reference draw last update utc | 2026-10-18T11:56:31Z |
| Market reference away last update utc | 2026-10-18T11:56:31Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:10Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:10Z |
| Home probability edge | -1.5% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0298 |
| Raw ev home | -0.0663 |
| Raw edge prob draw | 0.0184 |
| Raw ev draw | 0.0589 |
| Raw edge prob away | 0.0114 |
| Raw ev away | -0.0263 |

</details>


---
