# Serie A — football model report

Fixtures in this report: **19**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,201 |
| Training data through | 2026-10-16 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | 3daecc23c998096314c157429cb1b35725f94cf9b05908a170fc588ec71f3d6f |
| Training as of utc | 2026-10-17T14:10:47.594048+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 61, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 61, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-17T14:10:47.594048+00:00', 'observations': 61, 'observations_sha256': 'e708526b1f42fe70bd6071f8663704762680ef07011a6eee5f9111037af1f25e', 'eligible_training_matches': 12, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 37, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 12, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'e07b1a4849986b1c379a7ded35775c86c7cada267fdac1729cf8823142c36961', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 839.968 |
| Base scoring parameter | 0.133 |
| Home-advantage parameter | 0.114 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-16', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 16.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261017T141047594048Z_6eb5c6871bcd64b09efb311c04d1228719086573eb4b4cc00b95cf1fb0965999.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-17 — AS Roma vs Genoa

The model's most likely 1X2 outcome is **AS Roma win** at **65.7%**. Expected goals are 1.97 for AS Roma and 0.64 for Genoa (2.60 combined). The most likely exact score is 1-0 at 13.7%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 47.5%; Under 3.5 goals: 74.0%; Double Chance 1X: 87.1%; Double Chance X2: 34.3%; Double Chance 12 (either team wins): 78.6%; Under 4.5 goals: 88.0%; BTTS Yes (both teams score): 41.1%; BTTS No (at least one team does not score): 58.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 65.7% | 1.52 |
| Draw | 21.4% | 4.67 |
| Genoa win | 12.9% | 7.74 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.97 |
| Genoa expected goals | 0.64 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.0% |
| Under 0.5 | 8.0% |
| Over 1.5 | 72.9% |
| Under 1.5 | 27.1% |
| Over 2.5 | 47.5% |
| Under 2.5 | 52.5% |
| Over 3.5 | 26.0% |
| Under 3.5 | 74.0% |
| Over 4.5 | 12.0% |
| Under 4.5 | 88.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.75% |
| 2 | 2-0 | 13.69% |
| 3 | 1-1 | 9.92% |
| 4 | 3-0 | 8.97% |
| 5 | 2-1 | 8.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 65.7% | 62.7% | 1.61 | +5.8% |
| Draw | 21.4% | 22.4% | 4.28 | -8.4% |
| Genoa win | 12.9% | 14.9% | 6.28 | -18.9% |
| Over 2.5 | 47.5% | 52.1% | 1.90 | -9.7% |
| Under 2.5 | 52.5% | 47.9% | 2.05 | +7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T18:45:00+00:00 |
| Fixture id | 18d478f469da3bcc654dd4555b85c7e3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Genoa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9661 |
| Dc lambda away | 0.6364 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 41.1% |
| P btts no | 58.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.55 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.69 |
| Fair Over 2.5 odds | 2.10 |
| Fair Under 2.5 odds | 1.91 |
| Fair Over 3.5 odds | 3.85 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.33 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 68.7% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 10.9% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.5% |
| Raw p btts yes | 40.7% |
| P home draw | 87.1% |
| P draw away | 34.3% |
| P home away | 78.6% |
| Raw p home draw | 89.1% |
| Raw p draw away | 31.3% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.15 |
| Reference away odds | 6.10 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +3.0% |
| Draw probability edge | -1.0% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0606 |
| Raw ev home | 0.1063 |
| Raw edge prob draw | -0.0202 |
| Raw ev draw | -0.1276 |
| Raw edge prob away | -0.0404 |
| Raw ev away | -0.3154 |
| Market p home draw | 84.2% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.0% |
| Market draw away odds | 2.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.48 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 76.2% |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.40 |
| Market reference over 1 5 last update utc | 2026-10-17T09:09:47Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 70.9% |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.19 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:30Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.0% |
| Market btts yes odds | 1.86 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.86 |
| Market reference btts yes opposite odds | 1.86 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Bologna vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **61.5%**. Expected goals are 1.07 for Bologna and 2.12 for Inter Milan (3.19 combined). The most likely exact score is 1-2 at 10.0%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 61.7%; Under 3.5 goals: 60.3%; Double Chance 1X: 38.5%; Double Chance X2: 83.0%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 78.2%; BTTS Yes (both teams score): 58.3%; BTTS No (at least one team does not score): 41.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bologna win | 17.0% | 5.88 |
| Draw | 21.5% | 4.65 |
| Inter Milan win | 61.5% | 1.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bologna expected goals | 1.07 |
| Inter Milan expected goals | 2.12 |
| Expected total goals | 3.19 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.7% |
| Under 2.5 | 38.3% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 21.8% |
| Under 4.5 | 78.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.96% |
| 2 | 1-1 | 9.91% |
| 3 | 0-2 | 9.26% |
| 4 | 0-1 | 8.55% |
| 5 | 1-3 | 7.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bologna win | 17.0% | 15.8% | 6.05 | +2.8% |
| Draw | 21.5% | 22.4% | 4.32 | -7.0% |
| Inter Milan win | 61.5% | 61.9% | 1.62 | -0.4% |
| Over 2.5 | 61.7% | 59.2% | 1.68 | +3.6% |
| Under 2.5 | 38.3% | 40.8% | 2.38 | -8.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T16:00:00+00:00 |
| Fixture id | bfefc309177723410230fee52f650315 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Bologna |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0750 |
| Dc lambda away | 2.1199 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 58.3% |
| P btts no | 41.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.44 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.61 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.59 |
| Fair Under 4.5 odds | 1.28 |
| Unadjusted home-win probability | 18.2% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 61.1% |
| Raw p over 1 5 | 83.0% |
| Raw p under 3 5 | 60.4% |
| Raw p btts yes | 58.1% |
| P home draw | 38.5% |
| P draw away | 83.0% |
| P home away | 78.5% |
| Raw p home draw | 38.9% |
| Raw p draw away | 81.8% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.95 |
| Reference draw odds | 4.25 |
| Reference away odds | 1.59 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | +2.4% |
| Under 2.5 probability edge | -2.4% |
| Raw edge prob home | 0.0243 |
| Raw ev home | 0.1016 |
| Raw edge prob draw | -0.0167 |
| Raw ev draw | -0.1066 |
| Raw edge prob away | -0.0076 |
| Raw ev away | -0.0100 |
| Market p home draw | 39.0% |
| Market home draw odds | 2.46 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:09:23Z |
| Market reference home draw last update utc | 2026-10-17T09:10:15Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 84.1% |
| Market draw away odds | 1.16 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:09:23Z |
| Market reference draw away last update utc | 2026-10-17T09:10:15Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.8% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:09:23Z |
| Market reference home away last update utc | 2026-10-17T09:10:15Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.50 |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 83.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:22Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.4% |
| Market under 3 5 odds | 1.50 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.45 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:22Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.2% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:09:23Z |
| Market reference btts yes odds | 1.70 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-17T09:10:15Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-17 — Venezia vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **65.2%**. Expected goals are 0.66 for Venezia and 2.25 for Napoli (2.91 combined). The most likely exact score is 0-2 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.3%; Double Chance 1X: 34.8%; Double Chance X2: 85.5%; Double Chance 12 (either team wins): 79.7%; Under 4.5 goals: 84.0%; BTTS Yes (both teams score): 44.8%; BTTS No (at least one team does not score): 55.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 14.5% | 6.89 |
| Draw | 20.3% | 4.93 |
| Napoli win | 65.2% | 1.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.66 |
| Napoli expected goals | 2.25 |
| Expected total goals | 2.91 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 77.4% |
| Under 1.5 | 22.6% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 16.0% |
| Under 4.5 | 84.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.23% |
| 2 | 0-1 | 10.72% |
| 3 | 1-1 | 9.61% |
| 4 | 0-3 | 9.18% |
| 5 | 1-2 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 14.5% | 19.8% | 4.83 | -29.9% |
| Draw | 20.3% | 23.1% | 4.17 | -15.5% |
| Napoli win | 65.2% | 57.0% | 1.76 | +14.8% |
| Over 2.5 | 53.6% | 56.1% | 1.77 | -5.1% |
| Under 2.5 | 46.4% | 43.9% | 2.22 | +2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-17T13:00:00+00:00 |
| Fixture id | 907639dade64cca45d1ab639195d201e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Venezia |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6618 |
| Dc lambda away | 2.2515 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 44.8% |
| P btts no | 55.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.35 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.42 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.26 |
| Fair Under 4.5 odds | 1.19 |
| Unadjusted home-win probability | 9.2% |
| Unadjusted draw probability | 17.4% |
| Unadjusted away-win probability | 73.4% |
| Raw p over 1 5 | 78.9% |
| Raw p under 3 5 | 66.7% |
| Raw p btts yes | 43.5% |
| P home draw | 34.8% |
| P draw away | 85.5% |
| P home away | 79.7% |
| Raw p home draw | 26.6% |
| Raw p draw away | 90.8% |
| Raw p home away | 82.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.70 |
| Reference draw odds | 4.05 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.15 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -5.3% |
| Draw probability edge | -2.9% |
| Away probability edge | +8.2% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.1060 |
| Raw ev home | -0.5553 |
| Raw edge prob draw | -0.0574 |
| Raw ev draw | -0.2742 |
| Raw edge prob away | 0.1634 |
| Raw ev away | 0.2916 |

</details>


---

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **46.6%**. Expected goals are 1.29 for AC Milan and 1.14 for Atalanta BC (2.44 combined). The most likely exact score is 1-0 at 13.0%. Goal-market probabilities: at least one goal: 91.5%; Over 2.5 goals: 44.5%; Under 3.5 goals: 77.0%; Double Chance 1X: 72.9%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 46.6% | 2.15 |
| Draw | 26.3% | 3.81 |
| Atalanta BC win | 27.1% | 3.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.29 |
| Atalanta BC expected goals | 1.14 |
| Expected total goals | 2.44 |
| Over 0.5 | 91.5% |
| Under 0.5 | 8.5% |
| Over 1.5 | 70.4% |
| Under 1.5 | 29.6% |
| Over 2.5 | 44.5% |
| Under 2.5 | 55.5% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.00% |
| 2 | 1-1 | 12.45% |
| 3 | 2-1 | 9.83% |
| 4 | 2-0 | 8.59% |
| 5 | 0-0 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 46.6% | 53.6% | 1.86 | -13.3% |
| Draw | 26.3% | 24.7% | 3.94 | +3.5% |
| Atalanta BC win | 27.1% | 21.7% | 4.47 | +21.2% |
| Over 2.5 | 44.5% | 54.6% | 1.81 | -19.4% |
| Under 2.5 | 55.5% | 45.4% | 2.15 | +19.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T16:00:00+00:00 |
| Fixture id | f9403dd597edbfaa73abdc974e55344c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2911 |
| Dc lambda away | 1.1441 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.76 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.25 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.34 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.78 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 32.5% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 77.1% |
| Raw p btts yes | 49.7% |
| P home draw | 72.9% |
| P draw away | 53.4% |
| P home away | 73.7% |
| Raw p home draw | 67.5% |
| Raw p draw away | 60.4% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.83 |
| Reference draw odds | 3.88 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.09 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -7.0% |
| Draw probability edge | +1.6% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.1400 |
| Raw ev home | -0.2631 |
| Raw edge prob draw | 0.0315 |
| Raw ev draw | 0.0972 |
| Raw edge prob away | 0.1084 |
| Raw ev away | 0.4543 |
| Market p home draw | 77.6% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.3% |
| Market draw away odds | 2.05 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.25 |
| Market reference dc draw away odds | 2.05 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 78.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.30 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:31Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.2% |
| Market reference under 3 5 odds | 1.46 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:31Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.8%**. Expected goals are 0.95 for Fiorentina and 1.69 for Como (2.64 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.8%; Under 3.5 goals: 73.0%; Double Chance 1X: 49.2%; Double Chance X2: 75.8%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.2% | 4.13 |
| Draw | 25.0% | 4.00 |
| Como win | 50.8% | 1.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.95 |
| Como expected goals | 1.69 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.9% |
| Under 1.5 | 26.1% |
| Over 2.5 | 48.8% |
| Under 2.5 | 51.2% |
| Over 3.5 | 27.0% |
| Under 3.5 | 73.0% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.91% |
| 2 | 0-1 | 10.99% |
| 3 | 0-2 | 9.47% |
| 4 | 1-2 | 9.02% |
| 5 | 1-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.2% | 27.5% | 3.54 | -14.3% |
| Draw | 25.0% | 25.5% | 3.81 | -4.7% |
| Como win | 50.8% | 47.0% | 2.12 | +7.6% |
| Over 2.5 | 48.8% | 57.6% | 1.73 | -15.5% |
| Under 2.5 | 51.2% | 42.4% | 2.29 | +17.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:00:00+00:00 |
| Fixture id | 3ea32a0aa44a5f0ef7fd088155430087 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9518 |
| Dc lambda away | 1.6904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.35 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.71 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.89 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 54.5% |
| Raw p over 1 5 | 74.3% |
| Raw p under 3 5 | 72.7% |
| Raw p btts yes | 50.3% |
| P home draw | 49.2% |
| P draw away | 75.8% |
| P home away | 75.0% |
| Raw p home draw | 45.5% |
| Raw p draw away | 79.1% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.44 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.06 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -3.3% |
| Draw probability edge | -0.5% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -8.8% |
| Under 2.5 probability edge | +8.8% |
| Raw edge prob home | -0.0658 |
| Raw ev home | -0.2591 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.0646 |
| Raw edge prob away | 0.0752 |
| Raw ev away | 0.1558 |
| Market p home draw | 53.9% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 72.0% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.2% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.79 |
| Market reference dc draw away odds | 1.34 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 80.2% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:31Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.0% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.73 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.47 |
| Market reference btts yes last update utc | 2026-10-17T09:10:31Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **53.8%**. Expected goals are 1.36 for Juventus and 0.86 for Lazio (2.22 combined). The most likely exact score is 1-0 at 16.1%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 39.3%; Under 3.5 goals: 81.1%; Double Chance 1X: 79.9%; Double Chance X2: 46.2%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 42.5%; BTTS No (at least one team does not score): 57.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 53.8% | 1.86 |
| Draw | 26.1% | 3.83 |
| Lazio win | 20.1% | 4.97 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.36 |
| Lazio expected goals | 0.86 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 65.8% |
| Under 1.5 | 34.2% |
| Over 2.5 | 39.3% |
| Under 2.5 | 60.7% |
| Over 3.5 | 18.9% |
| Under 3.5 | 81.1% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.14% |
| 2 | 1-1 | 11.96% |
| 3 | 2-0 | 11.20% |
| 4 | 0-0 | 10.23% |
| 5 | 2-1 | 9.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 53.8% | 59.2% | 1.69 | -9.1% |
| Draw | 26.1% | 24.0% | 4.04 | +5.5% |
| Lazio win | 20.1% | 16.8% | 5.69 | +14.4% |
| Over 2.5 | 39.3% | 48.3% | 2.03 | -20.3% |
| Under 2.5 | 60.7% | 51.7% | 1.91 | +16.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T18:45:00+00:00 |
| Fixture id | 4c4026e2782f09d6f0ff2bde2a390513 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Juventus |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3641 |
| Dc lambda away | 0.8595 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.5% |
| P btts no | 57.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.77 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.93 |
| Fair Over 2.5 odds | 2.55 |
| Fair Under 2.5 odds | 1.65 |
| Fair Over 3.5 odds | 5.30 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.88 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 48.4% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 23.4% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.5% |
| Raw p btts yes | 43.2% |
| P home draw | 79.9% |
| P draw away | 46.2% |
| P home away | 73.9% |
| Raw p home draw | 76.6% |
| Raw p draw away | 51.6% |
| Raw p home away | 71.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.66 |
| Reference draw odds | 3.98 |
| Reference away odds | 5.60 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.85 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -5.4% |
| Draw probability edge | +2.1% |
| Away probability edge | +3.3% |
| Over 2.5 probability edge | -9.1% |
| Under 2.5 probability edge | +9.1% |
| Raw edge prob home | -0.1083 |
| Raw ev home | -0.1826 |
| Raw edge prob draw | 0.0429 |
| Raw ev draw | 0.1415 |
| Raw edge prob away | 0.0654 |
| Raw ev away | 0.3301 |
| Market p home draw | 82.2% |
| Market home draw odds | 1.18 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 42.0% |
| Market draw away odds | 2.31 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 2.31 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 73.5% |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:31Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 73.9% |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.55 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:31Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 48.2% |
| Market btts yes odds | 1.92 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.80 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **51.5%**. Expected goals are 1.46 for Udinese and 0.83 for Lecce (2.29 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.1%; Double Chance 1X: 78.4%; Double Chance X2: 48.5%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 51.5% | 1.94 |
| Draw | 26.9% | 3.72 |
| Lecce win | 21.6% | 4.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.46 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.9% |
| Under 3.5 | 80.1% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.49% |
| 2 | 1-1 | 12.39% |
| 3 | 2-0 | 10.75% |
| 4 | 0-0 | 10.26% |
| 5 | 2-1 | 8.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 51.5% | 51.4% | 1.95 | +0.5% |
| Draw | 26.9% | 26.6% | 3.65 | -1.9% |
| Lecce win | 21.6% | 22.0% | 4.38 | -5.4% |
| Over 2.5 | 40.2% | 47.2% | 2.08 | -16.4% |
| Under 2.5 | 59.8% | 52.8% | 1.87 | +11.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T10:30:00+00:00 |
| Fixture id | 367da93aa21a1e13eeafb94fd2263c75 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4592 |
| Dc lambda away | 0.8313 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.75 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.03 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.08 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 51.7% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 66.9% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 43.6% |
| P home draw | 78.4% |
| P draw away | 48.5% |
| P home away | 73.1% |
| Raw p home draw | 78.8% |
| Raw p draw away | 48.3% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.89 |
| Reference draw odds | 3.55 |
| Reference away odds | 4.25 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.01 |
| Reference Under 2.5 odds | 1.81 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +0.1% |
| Draw probability edge | +0.3% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0029 |
| Raw ev home | 0.0078 |
| Raw edge prob draw | 0.0057 |
| Raw ev draw | -0.0089 |
| Raw edge prob away | -0.0086 |
| Raw ev away | -0.0731 |
| Market p home draw | 77.5% |
| Market home draw odds | 1.25 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.7% |
| Market draw away odds | 1.95 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.8% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.25 |
| Market reference dc draw away odds | 1.95 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 72.5% |
| Market reference over 1 5 odds | 1.35 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:29Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 76.5% |
| Market reference under 3 5 odds | 1.28 |
| Market reference under 3 5 opposite odds | 3.81 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:29Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.9% |
| Market btts yes odds | 1.83 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.83 |
| Market reference btts yes opposite odds | 1.89 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.2%**. Expected goals are 1.13 for Monza and 1.61 for Cagliari (2.74 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.6%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.1%; Double Chance 1X: 60.8%; Double Chance X2: 66.9%; Double Chance 12 (either team wins): 72.3%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 55.2%; BTTS No (at least one team does not score): 44.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 33.1% | 3.02 |
| Draw | 27.7% | 3.61 |
| Cagliari win | 39.2% | 2.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.13 |
| Cagliari expected goals | 1.61 |
| Expected total goals | 2.74 |
| Over 0.5 | 92.6% |
| Under 0.5 | 7.4% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.15% |
| 2 | 1-0 | 8.84% |
| 3 | 2-1 | 8.30% |
| 4 | 0-1 | 8.26% |
| 5 | 1-2 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 33.1% | 39.8% | 2.49 | -17.5% |
| Draw | 27.7% | 30.1% | 3.25 | -10.1% |
| Cagliari win | 39.2% | 30.1% | 3.25 | +27.4% |
| Over 2.5 | 50.4% | 45.5% | 2.15 | +8.4% |
| Under 2.5 | 49.6% | 54.5% | 1.82 | -9.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T16:30:00+00:00 |
| Fixture id | ce94aca384a20f6af459366da6e1dd21 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1290 |
| Dc lambda away | 1.6088 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.2% |
| P btts no | 44.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.60 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.09 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.26 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 26.5% |
| Unadjusted draw probability | 25.2% |
| Unadjusted away-win probability | 48.3% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.4% |
| P home draw | 60.8% |
| P draw away | 66.9% |
| P home away | 72.3% |
| Raw p home draw | 51.7% |
| Raw p draw away | 73.5% |
| Raw p home away | 74.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.42 |
| Reference draw odds | 3.16 |
| Reference away odds | 3.16 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.08 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -6.6% |
| Draw probability edge | -2.4% |
| Away probability edge | +9.1% |
| Over 2.5 probability edge | +4.9% |
| Under 2.5 probability edge | -4.9% |
| Raw edge prob home | -0.1328 |
| Raw ev home | -0.3402 |
| Raw edge prob draw | -0.0487 |
| Raw ev draw | -0.1797 |
| Raw edge prob away | 0.1815 |
| Raw ev away | 0.5686 |
| Market p home draw | 69.7% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.6% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.7% |
| Market home away odds | 1.39 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.60 |
| Market reference dc home away odds | 1.39 |
| Market p over 1 5 | 71.9% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference over 1 5 odds | 1.37 |
| Market reference over 1 5 opposite odds | 3.35 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.7% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-17T09:10:22Z |
| Market reference under 3 5 odds | 1.30 |
| Market reference under 3 5 opposite odds | 3.80 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.5% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.78 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **38.9%**. Expected goals are 1.00 for Parma and 1.10 for Torino (2.10 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 87.4%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.8%; Double Chance 1X: 61.1%; Double Chance X2: 69.5%; Double Chance 12 (either team wins): 69.3%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.6%; BTTS No (at least one team does not score): 57.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.5% | 3.28 |
| Draw | 30.7% | 3.26 |
| Torino win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.00 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.4% |
| Under 0.5 | 12.6% |
| Over 1.5 | 62.4% |
| Under 1.5 | 37.6% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.85% |
| 2 | 0-1 | 13.72% |
| 3 | 0-0 | 12.58% |
| 4 | 1-0 | 11.29% |
| 5 | 1-2 | 7.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.5% | 28.6% | 3.42 | +4.2% |
| Draw | 30.7% | 30.9% | 3.17 | -2.8% |
| Torino win | 38.9% | 40.5% | 2.45 | -4.8% |
| Over 2.5 | 35.1% | 38.9% | 2.48 | -13.1% |
| Under 2.5 | 64.9% | 61.1% | 1.63 | +5.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-19T18:45:00+00:00 |
| Fixture id | 07014d9adc65ca39710bd9f0c7c0d3f0 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Torino |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0038 |
| Dc lambda away | 1.0994 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.6% |
| P btts no | 57.4% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 7.95 |
| Fair Over 1.5 odds | 1.60 |
| Fair Under 1.5 odds | 2.66 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.17 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.04 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.3% |
| Unadjusted draw probability | 30.4% |
| Unadjusted away-win probability | 37.2% |
| Raw p over 1 5 | 62.4% |
| Raw p under 3 5 | 83.8% |
| Raw p btts yes | 42.5% |
| P home draw | 61.1% |
| P draw away | 69.5% |
| P home away | 69.3% |
| Raw p home draw | 62.8% |
| Raw p draw away | 67.7% |
| Raw p home away | 69.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.32 |
| Reference draw odds | 3.08 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.40 |
| Reference Under 2.5 odds | 1.58 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +1.9% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.0374 |
| Raw ev home | 0.1060 |
| Raw edge prob draw | -0.0051 |
| Raw ev draw | -0.0357 |
| Raw edge prob away | -0.0323 |
| Raw ev away | -0.0876 |
| Market p home draw | 59.9% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-17T09:10:30Z |
| Market reference home draw last update utc | 2026-10-17T09:10:30Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.3% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-17T09:10:30Z |
| Market reference draw away last update utc | 2026-10-17T09:10:30Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.8% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-17T09:10:30Z |
| Market reference home away last update utc | 2026-10-17T09:10:30Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.62 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.41 |
| Market p over 1 5 | 66.2% |
| Market reference over 1 5 odds | 1.48 |
| Market reference over 1 5 opposite odds | 2.80 |
| Market reference over 1 5 last update utc | 2026-10-17T09:10:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 80.9% |
| Market reference under 3 5 odds | 1.22 |
| Market reference under 3 5 opposite odds | 4.75 |
| Market reference under 3 5 last update utc | 2026-10-17T09:10:32Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.5% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-17T09:10:30Z |
| Market reference btts yes odds | 1.98 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-17T09:10:30Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **50.7%**. Expected goals are 1.94 for Torino and 1.17 for Monza (3.11 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 59.1%; Under 3.5 goals: 62.7%; Double Chance 1X: 75.3%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 60.0%; BTTS No (at least one team does not score): 40.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 50.7% | 1.97 |
| Draw | 24.7% | 4.05 |
| Monza win | 24.7% | 4.06 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.94 |
| Monza expected goals | 1.17 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 59.1% |
| Under 2.5 | 40.9% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 2-1 | 9.04% |
| 3 | 1-0 | 7.79% |
| 4 | 2-0 | 7.73% |
| 5 | 1-2 | 6.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 50.7% | 46.3% | 2.15 | +9.0% |
| Draw | 24.7% | 26.9% | 3.62 | -10.7% |
| Monza win | 24.7% | 26.7% | 3.64 | -10.3% |
| Over 2.5 | 59.1% | 46.5% | 2.11 | +24.8% |
| Under 2.5 | 40.9% | 53.5% | 1.85 | -24.4% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9373 |
| Dc lambda away | 1.1708 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.0% |
| P btts no | 40.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.47 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.43 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.0% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 81.8% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.2% |
| P home draw | 75.3% |
| P draw away | 49.3% |
| P home away | 75.3% |
| Raw p home draw | 77.4% |
| Raw p draw away | 45.0% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.09 |
| Reference draw odds | 3.52 |
| Reference away odds | 3.54 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +4.3% |
| Draw probability edge | -2.2% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | +12.6% |
| Under 2.5 probability edge | -12.6% |
| Raw edge prob home | 0.0866 |
| Raw ev home | 0.1827 |
| Raw edge prob draw | -0.0448 |
| Raw ev draw | -0.1881 |
| Raw edge prob away | -0.0419 |
| Raw ev away | -0.1788 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **38.6%**. Expected goals are 1.07 for Cagliari and 1.17 for Bologna (2.25 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.7%; Under 3.5 goals: 81.0%; Double Chance 1X: 61.4%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 92.3%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 31.1% | 3.22 |
| Draw | 30.3% | 3.30 |
| Bologna win | 38.6% | 2.59 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.07 |
| Bologna expected goals | 1.17 |
| Expected total goals | 2.25 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 38.7% |
| Under 2.5 | 61.3% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 7.7% |
| Under 4.5 | 92.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.07% |
| 2 | 0-1 | 12.38% |
| 3 | 0-0 | 11.21% |
| 4 | 1-0 | 10.46% |
| 5 | 1-2 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 31.1% | 29.2% | 3.35 | +4.1% |
| Draw | 30.3% | 31.3% | 3.13 | -5.2% |
| Bologna win | 38.6% | 39.4% | 2.52 | -2.6% |
| Over 2.5 | 38.7% | 43.5% | 2.24 | -13.3% |
| Under 2.5 | 61.3% | 56.5% | 1.76 | +7.9% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0747 |
| Dc lambda away | 1.1741 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.92 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.58 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.26 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.97 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 32.9% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 37.9% |
| Raw p over 1 5 | 66.0% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 45.8% |
| P home draw | 61.4% |
| P draw away | 68.9% |
| P home away | 69.7% |
| Raw p home draw | 62.1% |
| Raw p draw away | 67.1% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +1.8% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.0367 |
| Raw ev home | 0.1023 |
| Raw edge prob draw | -0.0211 |
| Raw ev draw | -0.0849 |
| Raw edge prob away | -0.0156 |
| Raw ev away | -0.0459 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **65.8%**. Expected goals are 2.06 for Como and 0.92 for Sassuolo (2.98 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.9%; Double Chance 1X: 85.7%; Double Chance X2: 34.2%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 81.6%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 65.8% | 1.52 |
| Draw | 19.9% | 5.03 |
| Sassuolo win | 14.3% | 6.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.06 |
| Sassuolo expected goals | 0.92 |
| Expected total goals | 2.98 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.1% |
| Under 3.5 | 64.9% |
| Over 4.5 | 18.4% |
| Under 4.5 | 81.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.16% |
| 2 | 1-0 | 10.63% |
| 3 | 2-1 | 10.26% |
| 4 | 1-1 | 9.41% |
| 5 | 3-0 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 65.8% | 68.0% | 1.49 | -2.0% |
| Draw | 19.9% | 19.0% | 4.94 | -1.8% |
| Sassuolo win | 14.3% | 13.0% | 7.10 | +1.8% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0610 |
| Dc lambda away | 0.9191 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.78 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.06 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.85 |
| Fair Under 3.5 odds | 1.54 |
| Fair Over 4.5 odds | 5.44 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 80.0% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 52.6% |
| P home draw | 85.7% |
| P draw away | 34.2% |
| P home away | 80.1% |
| Raw p home draw | 84.3% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.44 |
| Reference draw odds | 4.80 |
| Reference away odds | 6.90 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.48 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:47Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:47Z |
| Home probability edge | -2.2% |
| Draw probability edge | +0.8% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0442 |
| Raw ev home | -0.0526 |
| Raw edge prob draw | 0.0169 |
| Raw ev draw | 0.0235 |
| Raw edge prob away | 0.0273 |
| Raw ev away | 0.1145 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **58.8%**. Expected goals are 1.36 for Lazio and 0.66 for Parma (2.02 combined). The most likely exact score is 1-0 at 19.5%. Goal-market probabilities: at least one goal: 88.1%; Over 2.5 goals: 34.2%; Under 3.5 goals: 84.9%; Double Chance 1X: 84.1%; Double Chance X2: 41.2%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 35.3%; BTTS No (at least one team does not score): 64.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 58.8% | 1.70 |
| Draw | 25.3% | 3.95 |
| Parma win | 15.9% | 6.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.36 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.02 |
| Over 0.5 | 88.1% |
| Under 0.5 | 11.9% |
| Over 1.5 | 61.0% |
| Under 1.5 | 39.0% |
| Over 2.5 | 34.2% |
| Under 2.5 | 65.8% |
| Over 3.5 | 15.1% |
| Under 3.5 | 84.9% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.50% |
| 2 | 2-0 | 13.48% |
| 3 | 0-0 | 11.94% |
| 4 | 1-1 | 10.75% |
| 5 | 2-1 | 8.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 58.8% | 63.9% | 1.58 | -7.1% |
| Draw | 25.3% | 22.1% | 4.33 | +9.6% |
| Parma win | 15.9% | 14.0% | 6.64 | +5.7% |
| Over 2.5 | 34.2% | 47.8% | 2.06 | -29.6% |
| Under 2.5 | 65.8% | 52.2% | 1.89 | +24.4% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3638 |
| Dc lambda away | 0.6589 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 35.3% |
| P btts no | 64.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.38 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.56 |
| Fair Over 2.5 odds | 2.93 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.62 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.39 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 53.7% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 85.3% |
| Raw p btts yes | 36.2% |
| P home draw | 84.1% |
| P draw away | 41.2% |
| P home away | 74.7% |
| Raw p home draw | 82.2% |
| Raw p draw away | 46.3% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.53 |
| Reference draw odds | 4.20 |
| Reference away odds | 6.45 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.99 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -5.1% |
| Draw probability edge | +3.2% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.1024 |
| Raw ev home | -0.1521 |
| Raw edge prob draw | 0.0648 |
| Raw ev draw | 0.2359 |
| Raw edge prob away | 0.0375 |
| Raw ev away | 0.1815 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **39.6%**. Expected goals are 1.04 for Napoli and 1.18 for AS Roma (2.22 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 89.3%; Over 2.5 goals: 38.6%; Under 3.5 goals: 81.5%; Double Chance 1X: 60.4%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 44.8%; BTTS No (at least one team does not score): 55.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 32.2% | 3.11 |
| Draw | 28.3% | 3.54 |
| AS Roma win | 39.6% | 2.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.04 |
| AS Roma expected goals | 1.18 |
| Expected total goals | 2.22 |
| Over 0.5 | 89.3% |
| Under 0.5 | 10.7% |
| Over 1.5 | 65.3% |
| Under 1.5 | 34.7% |
| Over 2.5 | 38.6% |
| Under 2.5 | 61.4% |
| Over 3.5 | 18.5% |
| Under 3.5 | 81.5% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 0-1 | 12.83% |
| 3 | 1-0 | 11.15% |
| 4 | 0-0 | 10.70% |
| 5 | 1-2 | 8.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 32.2% | 32.4% | 3.04 | -2.3% |
| Draw | 28.3% | 27.1% | 3.60 | +1.8% |
| AS Roma win | 39.6% | 40.5% | 2.45 | -3.0% |
| Over 2.5 | 38.6% | 51.0% | 1.93 | -25.5% |
| Under 2.5 | 61.4% | 49.0% | 2.01 | +23.4% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0421 |
| Dc lambda away | 1.1767 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 44.8% |
| P btts no | 55.2% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.35 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.88 |
| Fair Over 2.5 odds | 2.59 |
| Fair Under 2.5 odds | 1.63 |
| Fair Over 3.5 odds | 5.41 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.25 |
| Fair Under 4.5 odds | 1.08 |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 38.7% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.0% |
| P home draw | 60.4% |
| P draw away | 67.8% |
| P home away | 71.7% |
| Raw p home draw | 61.3% |
| Raw p draw away | 68.1% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.95 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.87 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | -0.2% |
| Draw probability edge | +1.2% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -12.4% |
| Under 2.5 probability edge | +12.4% |
| Raw edge prob home | -0.0047 |
| Raw ev home | -0.0298 |
| Raw edge prob draw | 0.0233 |
| Raw ev draw | 0.0594 |
| Raw edge prob away | -0.0185 |
| Raw ev away | -0.0529 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **54.4%**. Expected goals are 1.75 for Atalanta BC and 1.25 for Frosinone (3.01 combined). The most likely exact score is 2-1 at 10.6%. Goal-market probabilities: at least one goal: 95.1%; Over 2.5 goals: 58.5%; Under 3.5 goals: 64.2%; Double Chance 1X: 76.9%; Double Chance X2: 45.6%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 58.8%; BTTS No (at least one team does not score): 41.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 54.4% | 1.84 |
| Draw | 22.5% | 4.44 |
| Frosinone win | 23.1% | 4.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.75 |
| Frosinone expected goals | 1.25 |
| Expected total goals | 3.01 |
| Over 0.5 | 95.1% |
| Under 0.5 | 4.9% |
| Over 1.5 | 80.7% |
| Under 1.5 | 19.3% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 35.8% |
| Under 3.5 | 64.2% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.60% |
| 2 | 1-1 | 10.45% |
| 3 | 1-0 | 9.40% |
| 4 | 2-0 | 8.45% |
| 5 | 3-1 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 54.4% | 59.9% | 1.68 | -8.6% |
| Draw | 22.5% | 21.2% | 4.53 | +2.1% |
| Frosinone win | 23.1% | 18.9% | 5.04 | +16.3% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7523 |
| Dc lambda away | 1.2548 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 58.8% |
| P btts no | 41.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.56 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.17 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.80 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 48.9% |
| Unadjusted draw probability | 23.9% |
| Unadjusted away-win probability | 27.2% |
| Raw p over 1 5 | 80.4% |
| Raw p under 3 5 | 64.6% |
| Raw p btts yes | 59.3% |
| P home draw | 76.9% |
| P draw away | 45.6% |
| P home away | 77.5% |
| Raw p home draw | 72.8% |
| Raw p draw away | 51.1% |
| Raw p home away | 76.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.63 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.90 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:47Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:47Z |
| Home probability edge | -5.5% |
| Draw probability edge | +1.4% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -8.6% |
| Under 2.5 probability edge | +8.6% |
| Raw edge prob home | -0.1105 |
| Raw ev home | -0.1789 |
| Raw edge prob draw | 0.0273 |
| Raw ev draw | 0.0826 |
| Raw edge prob away | 0.0832 |
| Raw ev away | 0.3722 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **50.8%**. Expected goals are 1.73 for Genoa and 0.88 for Venezia (2.61 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 47.2%; Under 3.5 goals: 74.1%; Double Chance 1X: 77.0%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 88.1%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 50.8% | 1.97 |
| Draw | 26.3% | 3.81 |
| Venezia win | 23.0% | 4.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.73 |
| Venezia expected goals | 0.88 |
| Expected total goals | 2.61 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 72.9% |
| Under 1.5 | 27.1% |
| Over 2.5 | 47.2% |
| Under 2.5 | 52.8% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 11.9% |
| Under 4.5 | 88.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.46% |
| 2 | 1-0 | 11.11% |
| 3 | 2-0 | 9.76% |
| 4 | 2-1 | 8.59% |
| 5 | 0-0 | 8.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 50.8% | 44.4% | 2.25 | +14.2% |
| Draw | 26.3% | 28.4% | 3.44 | -9.7% |
| Venezia win | 23.0% | 27.2% | 3.58 | -17.7% |
| Over 2.5 | 47.2% | 50.1% | 1.97 | -7.0% |
| Under 2.5 | 52.8% | 49.9% | 1.98 | +4.6% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7266 |
| Dc lambda away | 0.8806 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.08 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.69 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 3.86 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.42 |
| Fair Under 4.5 odds | 1.13 |
| Unadjusted home-win probability | 57.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 18.8% |
| Raw p over 1 5 | 73.6% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 48.4% |
| P home draw | 77.0% |
| P draw away | 49.2% |
| P home away | 73.7% |
| Raw p home draw | 81.2% |
| Raw p draw away | 42.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.18 |
| Reference draw odds | 3.34 |
| Reference away odds | 3.48 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +6.4% |
| Draw probability edge | -2.2% |
| Away probability edge | -4.2% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | 0.1281 |
| Raw ev home | 0.2862 |
| Raw edge prob draw | -0.0433 |
| Raw ev draw | -0.1714 |
| Raw edge prob away | -0.0848 |
| Raw ev away | -0.3287 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **73.5%**. Expected goals are 2.77 for Inter Milan and 0.94 for Fiorentina (3.71 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 71.1%; Under 3.5 goals: 49.6%; Double Chance 1X: 89.2%; Double Chance X2: 26.5%; Double Chance 12 (either team wins): 84.3%; Under 4.5 goals: 69.0%; BTTS Yes (both teams score): 57.7%; BTTS No (at least one team does not score): 42.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 73.5% | 1.36 |
| Draw | 15.7% | 6.36 |
| Fiorentina win | 10.8% | 9.29 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.77 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.71 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 88.4% |
| Under 1.5 | 11.6% |
| Over 2.5 | 71.1% |
| Under 2.5 | 28.9% |
| Over 3.5 | 50.4% |
| Under 3.5 | 49.6% |
| Over 4.5 | 31.0% |
| Under 4.5 | 69.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.17% |
| 2 | 2-1 | 8.62% |
| 3 | 3-0 | 8.45% |
| 4 | 3-1 | 7.95% |
| 5 | 1-1 | 6.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 73.5% | 71.7% | 1.41 | +3.6% |
| Draw | 15.7% | 16.8% | 5.56 | -12.5% |
| Fiorentina win | 10.8% | 11.5% | 7.90 | -15.0% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.7667 |
| Dc lambda away | 0.9404 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 57.7% |
| P btts no | 42.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.12 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.60 |
| Fair Over 2.5 odds | 1.41 |
| Fair Under 2.5 odds | 3.45 |
| Fair Over 3.5 odds | 1.98 |
| Fair Under 3.5 odds | 2.02 |
| Fair Over 4.5 odds | 3.22 |
| Fair Under 4.5 odds | 1.45 |
| Unadjusted home-win probability | 75.3% |
| Unadjusted draw probability | 14.7% |
| Unadjusted away-win probability | 10.0% |
| Raw p over 1 5 | 88.6% |
| Raw p under 3 5 | 49.3% |
| Raw p btts yes | 57.2% |
| P home draw | 89.2% |
| P draw away | 26.5% |
| P home away | 84.3% |
| Raw p home draw | 90.0% |
| Raw p draw away | 24.7% |
| Raw p home away | 85.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.70 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-17T09:09:47Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:09:47Z |
| Home probability edge | +1.8% |
| Draw probability edge | -1.1% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | 0.0367 |
| Raw ev home | 0.0623 |
| Raw edge prob draw | -0.0212 |
| Raw ev draw | -0.1845 |
| Raw edge prob away | -0.0155 |
| Raw ev away | -0.2109 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **64.8%**. Expected goals are 0.60 for Lecce and 1.64 for Juventus (2.24 combined). The most likely exact score is 0-1 at 17.8%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 39.6%; Under 3.5 goals: 80.8%; Double Chance 1X: 35.2%; Double Chance X2: 87.5%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 36.2%; BTTS No (at least one team does not score): 63.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 12.5% | 8.00 |
| Draw | 22.7% | 4.41 |
| Juventus win | 64.8% | 1.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.60 |
| Juventus expected goals | 1.64 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 66.2% |
| Under 1.5 | 33.8% |
| Over 2.5 | 39.6% |
| Under 2.5 | 60.4% |
| Over 3.5 | 19.2% |
| Under 3.5 | 80.8% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 17.84% |
| 2 | 0-2 | 14.84% |
| 3 | 0-0 | 10.06% |
| 4 | 1-1 | 9.93% |
| 5 | 1-2 | 8.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 12.5% | 11.9% | 7.70 | -3.8% |
| Draw | 22.7% | 21.0% | 4.53 | +2.7% |
| Juventus win | 64.8% | 67.1% | 1.50 | -2.7% |
| Over 2.5 | 39.6% | 51.3% | 1.92 | -23.9% |
| Under 2.5 | 60.4% | 48.7% | 2.02 | +22.0% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6006 |
| Dc lambda away | 1.6435 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 36.2% |
| P btts no | 63.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.95 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.96 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.21 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.62 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 13.1% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 62.6% |
| Raw p over 1 5 | 65.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 36.6% |
| P home draw | 35.2% |
| P draw away | 87.5% |
| P home away | 77.3% |
| Raw p home draw | 37.4% |
| Raw p draw away | 86.9% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 7.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +0.6% |
| Draw probability edge | +1.7% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | 0.0111 |
| Raw ev home | 0.0052 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | 0.1039 |
| Raw edge prob away | -0.0452 |
| Raw ev away | -0.0613 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.0%**. Expected goals are 1.04 for Udinese and 1.56 for AC Milan (2.60 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 48.4%; Under 3.5 goals: 73.5%; Double Chance 1X: 48.0%; Double Chance X2: 77.3%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 22.7% | 4.40 |
| Draw | 25.3% | 3.95 |
| AC Milan win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.56 |
| Expected total goals | 2.60 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.4% |
| Under 2.5 | 51.6% |
| Over 3.5 | 26.5% |
| Under 3.5 | 73.5% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.04% |
| 2 | 0-1 | 12.01% |
| 3 | 1-2 | 9.93% |
| 4 | 0-2 | 9.57% |
| 5 | 0-0 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 22.7% | 20.5% | 4.68 | +6.4% |
| Draw | 25.3% | 24.8% | 3.91 | -1.1% |
| AC Milan win | 52.0% | 54.7% | 1.83 | -4.9% |
| Over 2.5 | 48.4% | 50.0% | 1.97 | -4.7% |
| Under 2.5 | 51.6% | 50.0% | 1.97 | +1.7% |

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
| Market best home last update utc | 2026-10-17T09:09:23Z |
| Market best draw last update utc | 2026-10-17T09:09:23Z |
| Market best away last update utc | 2026-10-17T09:09:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 9.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0373 |
| Dc lambda away | 1.5607 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-17T14:10:47.594048+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.29 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.77 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.09 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 25.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 49.2% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.6% |
| Raw p btts yes | 51.2% |
| P home draw | 48.0% |
| P draw away | 77.3% |
| P home away | 74.7% |
| Raw p home draw | 50.8% |
| Raw p draw away | 75.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.55 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-17T09:10:14Z |
| Market reference home last update utc | 2026-10-17T09:10:14Z |
| Market reference draw last update utc | 2026-10-17T09:10:14Z |
| Market reference away last update utc | 2026-10-17T09:10:14Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market reference under 2 5 last update utc | 2026-10-17T09:10:14Z |
| Market best over 2 5 last update utc | 2026-10-17T09:09:23Z |
| Market best under 2 5 last update utc | 2026-10-17T09:09:23Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | 0.0445 |
| Raw ev home | 0.1684 |
| Raw edge prob draw | 0.0105 |
| Raw ev draw | 0.0095 |
| Raw edge prob away | -0.0551 |
| Raw ev away | -0.0993 |

</details>


---
