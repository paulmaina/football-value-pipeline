# Serie A — football model report

Fixtures in this report: **16**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,204 |
| Training data through | 2026-10-17 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training sha256 | ce94e0219c5e66cfe91eade48c9a1c243922664d928d1cb05189c3e36c1ccc3b |
| Training as of utc | 2026-10-18T08:36:27.418900+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 64, 'bbs_added_results': 4, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 64, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T08:36:27.418900+00:00', 'observations': 74, 'observations_sha256': '542437d1e72a23c825115140c3e879ef5202b1f631d74eaa67990ed72a75b1a3', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 40, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 2, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '4151ac6e691b9a03f6453b55dbe5333bb486725586965dd1aab45b54d639eeaf', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
| Optimizer objective | 845.845 |
| Base scoring parameter | 0.129 |
| Home-advantage parameter | 0.119 |
| Dixon-Coles low-score adjustment | -0.005 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-17', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 12.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261018T083627418900Z_5bed762a3b6250ddf0403862ff483e6bbe276f31eacdcb9c6586e3fb9a1b67d2.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
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

## 2026-10-18 — AC Milan vs Atalanta BC

The model's most likely 1X2 outcome is **AC Milan win** at **48.3%**. Expected goals are 1.30 for AC Milan and 1.15 for Atalanta BC (2.45 combined). The most likely exact score is 1-0 at 13.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 45.0%; Under 3.5 goals: 76.7%; Double Chance 1X: 73.7%; Double Chance X2: 51.7%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 48.3% | 2.07 |
| Draw | 25.4% | 3.93 |
| Atalanta BC win | 26.3% | 3.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.30 |
| Atalanta BC expected goals | 1.15 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 70.5% |
| Under 1.5 | 29.5% |
| Over 2.5 | 45.0% |
| Under 2.5 | 55.0% |
| Over 3.5 | 23.3% |
| Under 3.5 | 76.7% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.51% |
| 2 | 1-1 | 12.04% |
| 3 | 2-1 | 10.14% |
| 4 | 2-0 | 8.83% |
| 5 | 0-0 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 48.3% | 56.7% | 1.80 | -13.0% |
| Draw | 25.4% | 23.5% | 4.07 | +3.4% |
| Atalanta BC win | 26.3% | 19.9% | 4.67 | +22.6% |
| Over 2.5 | 45.0% | 58.4% | 1.75 | -21.2% |
| Under 2.5 | 55.0% | 41.6% | 2.25 | +23.7% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Milan |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.3009 |
| Dc lambda away | 1.1478 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.37 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.39 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.57 |
| Fair Under 4.5 odds | 1.12 |
| Unadjusted home-win probability | 40.0% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 32.6% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 49.7% |
| P home draw | 73.7% |
| P draw away | 51.7% |
| P home away | 74.6% |
| Raw p home draw | 67.4% |
| Raw p draw away | 60.0% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.67 |
| Reference draw odds | 3.70 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -8.3% |
| Draw probability edge | +1.9% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -13.3% |
| Under 2.5 probability edge | +13.3% |
| Raw edge prob home | -0.1666 |
| Raw ev home | -0.2801 |
| Raw edge prob draw | 0.0389 |
| Raw ev draw | 0.1137 |
| Raw edge prob away | 0.1277 |
| Raw ev away | 0.5244 |
| Market p home draw | 80.4% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 44.2% |
| Market draw away odds | 2.13 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.4% |
| Market home away odds | 1.28 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.20 |
| Market reference dc home draw odds | 1.21 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 81.0% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:24Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.2% |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.64 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:24Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 58.7% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-18T08:36:24Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Fiorentina vs Como

The model's most likely 1X2 outcome is **Como win** at **50.9%**. Expected goals are 0.96 for Fiorentina and 1.69 for Como (2.64 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 48.9%; Under 3.5 goals: 72.9%; Double Chance 1X: 49.1%; Double Chance X2: 75.8%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 87.3%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 24.2% | 4.13 |
| Draw | 24.8% | 4.02 |
| Como win | 50.9% | 1.96 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fiorentina expected goals | 0.96 |
| Como expected goals | 1.69 |
| Expected total goals | 2.64 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 73.8% |
| Under 1.5 | 26.2% |
| Over 2.5 | 48.9% |
| Under 2.5 | 51.1% |
| Over 3.5 | 27.1% |
| Under 3.5 | 72.9% |
| Over 4.5 | 12.7% |
| Under 4.5 | 87.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.82% |
| 2 | 0-1 | 11.15% |
| 3 | 0-2 | 9.45% |
| 4 | 1-2 | 9.05% |
| 5 | 1-0 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 24.2% | 27.1% | 3.54 | -14.3% |
| Draw | 24.8% | 25.4% | 3.81 | -5.3% |
| Como win | 50.9% | 47.4% | 2.12 | +8.0% |
| Over 2.5 | 48.9% | 59.5% | 1.73 | -15.5% |
| Under 2.5 | 51.1% | 40.5% | 2.29 | +17.1% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 0.9575 |
| Dc lambda away | 1.6874 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.63 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.82 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.96 |
| Fair Over 3.5 odds | 3.69 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.87 |
| Fair Under 4.5 odds | 1.15 |
| Unadjusted home-win probability | 21.3% |
| Unadjusted draw probability | 24.2% |
| Unadjusted away-win probability | 54.5% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.6% |
| Raw p btts yes | 50.3% |
| P home draw | 49.1% |
| P draw away | 75.8% |
| P home away | 75.2% |
| Raw p home draw | 45.5% |
| Raw p draw away | 78.7% |
| Raw p home away | 75.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.30 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.98 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.32 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -2.9% |
| Draw probability edge | -0.6% |
| Away probability edge | +3.5% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.0586 |
| Raw ev home | -0.2466 |
| Raw edge prob draw | -0.0121 |
| Raw ev draw | -0.0764 |
| Raw edge prob away | 0.0706 |
| Raw ev away | 0.1549 |
| Market p home draw | 53.4% |
| Market home draw odds | 1.80 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 71.9% |
| Market draw away odds | 1.34 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.31 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.30 |
| Market reference dc home draw odds | 1.75 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.7% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:35:38Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:24Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.3% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:35:38Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.58 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:24Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.55 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-18T08:36:24Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Juventus vs Lazio

The model's most likely 1X2 outcome is **Juventus win** at **56.2%**. Expected goals are 1.37 for Juventus and 0.86 for Lazio (2.23 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.9%; Double Chance 1X: 81.2%; Double Chance X2: 43.8%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 92.1%; BTTS Yes (both teams score): 42.2%; BTTS No (at least one team does not score): 57.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Juventus win | 56.2% | 1.78 |
| Draw | 24.9% | 4.01 |
| Lazio win | 18.8% | 5.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Juventus expected goals | 1.37 |
| Lazio expected goals | 0.86 |
| Expected total goals | 2.23 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 66.0% |
| Under 1.5 | 34.0% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.9% |
| Under 4.5 | 92.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.94% |
| 2 | 2-0 | 11.65% |
| 3 | 1-1 | 11.42% |
| 4 | 2-1 | 10.02% |
| 5 | 0-0 | 9.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Juventus win | 56.2% | 63.7% | 1.61 | -9.5% |
| Draw | 24.9% | 22.1% | 4.27 | +6.5% |
| Lazio win | 18.8% | 14.2% | 6.30 | +18.8% |
| Over 2.5 | 39.7% | 50.6% | 1.96 | -22.1% |
| Under 2.5 | 60.3% | 49.4% | 1.98 | +19.3% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.3695 |
| Dc lambda away | 0.8603 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 42.2% |
| P btts no | 57.8% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.31 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.94 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.23 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.61 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 48.7% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 43.1% |
| P home draw | 81.2% |
| P draw away | 43.8% |
| P home away | 75.1% |
| Raw p home draw | 76.5% |
| Raw p draw away | 51.3% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.50 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -7.5% |
| Draw probability edge | +2.9% |
| Away probability edge | +4.7% |
| Over 2.5 probability edge | -10.8% |
| Under 2.5 probability edge | +10.8% |
| Raw edge prob home | -0.1506 |
| Raw ev home | -0.2161 |
| Raw edge prob draw | 0.0575 |
| Raw ev draw | 0.1874 |
| Raw edge prob away | 0.0931 |
| Raw ev away | 0.4807 |
| Market p home draw | 83.6% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 40.1% |
| Market draw away odds | 2.48 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.38 |
| Market reference dc home draw odds | 1.14 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 75.6% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.77 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 72.0% |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.30 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:25Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 49.1% |
| Market btts yes odds | 1.90 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-18T08:36:24Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Udinese vs Lecce

The model's most likely 1X2 outcome is **Udinese win** at **53.0%**. Expected goals are 1.47 for Udinese and 0.83 for Lecce (2.30 combined). The most likely exact score is 1-0 at 14.9%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 40.5%; Under 3.5 goals: 79.9%; Double Chance 1X: 79.3%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 43.4%; BTTS No (at least one team does not score): 56.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 53.0% | 1.89 |
| Draw | 26.3% | 3.80 |
| Lecce win | 20.7% | 4.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.47 |
| Lecce expected goals | 0.83 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
| Over 1.5 | 67.1% |
| Under 1.5 | 32.9% |
| Over 2.5 | 40.5% |
| Under 2.5 | 59.5% |
| Over 3.5 | 20.1% |
| Under 3.5 | 79.9% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.93% |
| 2 | 1-1 | 12.15% |
| 3 | 2-0 | 10.99% |
| 4 | 0-0 | 9.96% |
| 5 | 2-1 | 9.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 53.0% | 54.0% | 1.86 | -1.4% |
| Draw | 26.3% | 26.0% | 3.68 | -3.1% |
| Lecce win | 20.7% | 20.0% | 4.83 | -0.2% |
| Over 2.5 | 40.5% | 46.1% | 2.08 | -15.7% |
| Under 2.5 | 59.5% | 53.9% | 1.87 | +11.2% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Udinese |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4661 |
| Dc lambda away | 0.8331 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.4% |
| P btts no | 56.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.04 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.04 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 4.97 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.88 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 21.3% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 43.5% |
| P home draw | 79.3% |
| P draw away | 47.0% |
| P home away | 73.7% |
| Raw p home draw | 78.7% |
| Raw p draw away | 48.0% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.75 |
| Reference draw odds | 3.40 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -1.0% |
| Draw probability edge | +0.4% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | -0.0197 |
| Raw ev home | -0.0327 |
| Raw edge prob draw | 0.0073 |
| Raw ev draw | -0.0175 |
| Raw edge prob away | 0.0124 |
| Raw ev away | 0.0285 |
| Market p home draw | 79.7% |
| Market home draw odds | 1.22 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.7% |
| Market draw away odds | 2.05 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.04 |
| Market reference dc home draw odds | 1.22 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 73.3% |
| Market reference over 1 5 odds | 1.34 |
| Market reference over 1 5 opposite odds | 3.47 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:24Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 75.3% |
| Market reference under 3 5 odds | 1.27 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.4% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 1.92 |
| Market reference btts yes opposite odds | 1.95 |
| Market reference btts yes last update utc | 2026-10-18T08:36:29Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Monza vs Cagliari

The model's most likely 1X2 outcome is **Cagliari win** at **39.0%**. Expected goals are 1.14 for Monza and 1.60 for Cagliari (2.74 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.1%; Double Chance 1X: 61.0%; Double Chance X2: 65.7%; Double Chance 12 (either team wins): 73.3%; Under 4.5 goals: 86.2%; BTTS Yes (both teams score): 54.9%; BTTS No (at least one team does not score): 45.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 34.3% | 2.92 |
| Draw | 26.7% | 3.75 |
| Cagliari win | 39.0% | 2.56 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 1.14 |
| Cagliari expected goals | 1.60 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.8% |
| Under 4.5 | 86.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.66% |
| 2 | 1-0 | 9.28% |
| 3 | 2-1 | 8.50% |
| 4 | 0-1 | 8.37% |
| 5 | 1-2 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 34.3% | 41.6% | 2.49 | -14.6% |
| Draw | 26.7% | 28.4% | 3.25 | -13.3% |
| Cagliari win | 39.0% | 30.0% | 3.25 | +26.9% |
| Over 2.5 | 50.6% | 45.4% | 2.15 | +8.9% |
| Under 2.5 | 49.4% | 54.6% | 1.82 | -10.2% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.1360 |
| Dc lambda away | 1.6007 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.9% |
| P btts no | 45.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 14.31 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.06 |
| Fair Over 2.5 odds | 1.97 |
| Fair Under 2.5 odds | 2.03 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.23 |
| Fair Under 4.5 odds | 1.16 |
| Unadjusted home-win probability | 27.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 48.1% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 54.3% |
| P home draw | 61.0% |
| P draw away | 65.7% |
| P home away | 73.3% |
| Raw p home draw | 51.9% |
| Raw p draw away | 73.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.20 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.09 |
| Reference Under 2.5 odds | 1.76 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -7.3% |
| Draw probability edge | -1.7% |
| Away probability edge | +9.0% |
| Over 2.5 probability edge | +5.2% |
| Under 2.5 probability edge | -5.2% |
| Raw edge prob home | -0.1461 |
| Raw ev home | -0.3282 |
| Raw edge prob draw | -0.0345 |
| Raw ev draw | -0.1893 |
| Raw edge prob away | 0.1807 |
| Raw ev away | 0.5625 |
| Market p home draw | 69.2% |
| Market home draw odds | 1.39 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.0% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.39 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.57 |
| Market reference dc home draw odds | 1.36 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 73.6% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:36:10Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:24Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.8% |
| Market under 3 5 odds | 1.25 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:36:10Z |
| Market reference under 3 5 odds | 1.25 |
| Market reference under 3 5 opposite odds | 3.44 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:10Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 52.9% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 2.00 |
| Market reference btts yes last update utc | 2026-10-18T08:36:24Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-19 — Parma vs Torino

The model's most likely 1X2 outcome is **Torino win** at **39.4%**. Expected goals are 1.01 for Parma and 1.10 for Torino (2.10 combined). The most likely exact score is 0-1 at 14.1%. Goal-market probabilities: at least one goal: 87.7%; Over 2.5 goals: 35.1%; Under 3.5 goals: 83.8%; Double Chance 1X: 60.6%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 70.0%; Under 4.5 goals: 93.8%; BTTS Yes (both teams score): 42.3%; BTTS No (at least one team does not score): 57.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 30.6% | 3.27 |
| Draw | 30.0% | 3.33 |
| Torino win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.01 |
| Torino expected goals | 1.10 |
| Expected total goals | 2.10 |
| Over 0.5 | 87.7% |
| Under 0.5 | 12.3% |
| Over 1.5 | 62.2% |
| Under 1.5 | 37.8% |
| Over 2.5 | 35.1% |
| Under 2.5 | 64.9% |
| Over 3.5 | 16.2% |
| Under 3.5 | 83.8% |
| Over 4.5 | 6.2% |
| Under 4.5 | 93.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.09% |
| 2 | 1-1 | 13.54% |
| 3 | 0-0 | 12.27% |
| 4 | 1-0 | 11.42% |
| 5 | 1-2 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 30.6% | 28.4% | 3.42 | +4.5% |
| Draw | 30.0% | 30.0% | 3.17 | -4.8% |
| Torino win | 39.4% | 41.6% | 2.45 | -3.4% |
| Over 2.5 | 35.1% | 39.7% | 2.48 | -12.9% |
| Under 2.5 | 64.9% | 60.3% | 1.63 | +5.7% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.0069 |
| Dc lambda away | 1.0959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 42.3% |
| P btts no | 57.7% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.15 |
| Fair Over 1.5 odds | 1.61 |
| Fair Under 1.5 odds | 2.65 |
| Fair Over 2.5 odds | 2.85 |
| Fair Under 2.5 odds | 1.54 |
| Fair Over 3.5 odds | 6.17 |
| Fair Under 3.5 odds | 1.19 |
| Fair Over 4.5 odds | 16.00 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 32.7% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 62.2% |
| Raw p under 3 5 | 83.8% |
| Raw p btts yes | 42.3% |
| P home draw | 60.6% |
| P draw away | 69.4% |
| P home away | 70.0% |
| Raw p home draw | 62.7% |
| Raw p draw away | 67.3% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 3.10 |
| Reference draw odds | 2.95 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 2.36 |
| Reference Under 2.5 odds | 1.60 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +2.2% |
| Draw probability edge | +0.0% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0431 |
| Raw ev home | 0.1186 |
| Raw edge prob draw | 0.0001 |
| Raw ev draw | -0.0482 |
| Raw edge prob away | -0.0432 |
| Raw ev away | -0.0869 |
| Market p home draw | 60.0% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:36:06Z |
| Market reference home draw last update utc | 2026-10-18T08:36:24Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.8% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:36:06Z |
| Market reference draw away last update utc | 2026-10-18T08:36:24Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.2% |
| Market home away odds | 1.41 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:36:06Z |
| Market reference home away last update utc | 2026-10-18T08:36:24Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.33 |
| Market reference dc home draw odds | 1.57 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 67.8% |
| Market reference over 1 5 odds | 1.44 |
| Market reference over 1 5 opposite odds | 2.90 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:24Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 81.1% |
| Market reference under 3 5 odds | 1.19 |
| Market reference under 3 5 opposite odds | 4.00 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 46.3% |
| Market btts yes odds | 1.98 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:36:06Z |
| Market reference btts yes odds | 2.00 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-18T08:36:24Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **51.1%**. Expected goals are 1.93 for Torino and 1.17 for Monza (3.11 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 59.2%; Under 3.5 goals: 62.7%; Double Chance 1X: 75.4%; Double Chance X2: 48.9%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 59.8%; BTTS No (at least one team does not score): 40.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 51.1% | 1.96 |
| Draw | 24.3% | 4.12 |
| Monza win | 24.6% | 4.07 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.93 |
| Monza expected goals | 1.17 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 37.3% |
| Under 3.5 | 62.7% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.17% |
| 2 | 2-1 | 9.11% |
| 3 | 1-0 | 7.99% |
| 4 | 2-0 | 7.78% |
| 5 | 1-2 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 51.1% | 47.2% | 2.15 | +10.0% |
| Draw | 24.3% | 26.4% | 3.62 | -12.1% |
| Monza win | 24.6% | 26.4% | 3.64 | -10.5% |
| Over 2.5 | 59.2% | 44.2% | 2.11 | +24.9% |
| Under 2.5 | 40.8% | 55.8% | 1.85 | -24.5% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.9350 |
| Dc lambda away | 1.1718 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.8% |
| P btts no | 40.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.17 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.39 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.68 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Unadjusted home-win probability | 55.1% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 22.8% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.1% |
| P home draw | 75.4% |
| P draw away | 48.9% |
| P home away | 75.7% |
| Raw p home draw | 77.2% |
| Raw p draw away | 44.9% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.96 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +3.9% |
| Draw probability edge | -2.1% |
| Away probability edge | -1.8% |
| Over 2.5 probability edge | +15.0% |
| Under 2.5 probability edge | -15.0% |
| Raw edge prob home | 0.0789 |
| Raw ev home | 0.1844 |
| Raw edge prob draw | -0.0425 |
| Raw ev draw | -0.1984 |
| Raw edge prob away | -0.0363 |
| Raw ev away | -0.1713 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **39.6%**. Expected goals are 1.10 for Cagliari and 1.17 for Bologna (2.28 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 89.6%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.4%; Double Chance 1X: 60.4%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 46.2%; BTTS No (at least one team does not score): 53.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 31.7% | 3.16 |
| Draw | 28.7% | 3.48 |
| Bologna win | 39.6% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.10 |
| Bologna expected goals | 1.17 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.6% |
| Under 0.5 | 10.4% |
| Over 1.5 | 66.4% |
| Under 1.5 | 33.6% |
| Over 2.5 | 39.7% |
| Under 2.5 | 60.3% |
| Over 3.5 | 19.6% |
| Under 3.5 | 80.4% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.37% |
| 2 | 0-1 | 12.71% |
| 3 | 1-0 | 10.50% |
| 4 | 0-0 | 10.36% |
| 5 | 1-2 | 8.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 31.7% | 29.3% | 3.35 | +6.0% |
| Draw | 28.7% | 28.7% | 3.13 | -10.2% |
| Bologna win | 39.6% | 42.0% | 2.52 | -0.1% |
| Over 2.5 | 39.7% | 42.7% | 2.24 | -11.0% |
| Under 2.5 | 60.3% | 57.3% | 1.76 | +6.1% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1042 |
| Dc lambda away | 1.1710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.2% |
| P btts no | 53.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.65 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.11 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.36 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 28.7% |
| Unadjusted away-win probability | 37.3% |
| Raw p over 1 5 | 66.4% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 46.2% |
| P home draw | 60.4% |
| P draw away | 68.3% |
| P home away | 71.3% |
| Raw p home draw | 62.7% |
| Raw p draw away | 66.0% |
| Raw p home away | 71.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.00 |
| Reference away odds | 2.15 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.66 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +2.4% |
| Draw probability edge | -0.0% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -3.0% |
| Under 2.5 probability edge | +3.0% |
| Raw edge prob home | 0.0471 |
| Raw ev home | 0.1394 |
| Raw edge prob draw | -0.0008 |
| Raw ev draw | -0.1029 |
| Raw edge prob away | -0.0463 |
| Raw ev away | -0.0594 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **67.5%**. Expected goals are 2.06 for Como and 0.92 for Sassuolo (2.98 combined). The most likely exact score is 2-0 at 11.4%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.7%; Double Chance 1X: 85.9%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 51.7%; BTTS No (at least one team does not score): 48.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 67.5% | 1.48 |
| Draw | 18.4% | 5.42 |
| Sassuolo win | 14.1% | 7.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.06 |
| Sassuolo expected goals | 0.92 |
| Expected total goals | 2.98 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 80.2% |
| Under 1.5 | 19.8% |
| Over 2.5 | 58.2% |
| Under 2.5 | 41.8% |
| Over 3.5 | 35.3% |
| Under 3.5 | 64.7% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.43% |
| 2 | 1-0 | 11.03% |
| 3 | 2-1 | 10.47% |
| 4 | 1-1 | 8.72% |
| 5 | 3-0 | 7.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 67.5% | 71.1% | 1.49 | +0.6% |
| Draw | 18.4% | 16.5% | 4.94 | -8.9% |
| Sassuolo win | 14.1% | 12.4% | 7.10 | -0.1% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0647 |
| Dc lambda away | 0.9157 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 51.7% |
| P btts no | 48.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.58 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 5.06 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.39 |
| Fair Over 3.5 odds | 2.83 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.37 |
| Fair Under 4.5 odds | 1.23 |
| Unadjusted home-win probability | 63.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 15.7% |
| Raw p over 1 5 | 79.8% |
| Raw p under 3 5 | 65.2% |
| Raw p btts yes | 52.4% |
| P home draw | 85.9% |
| P draw away | 32.5% |
| P home away | 81.6% |
| Raw p home draw | 84.3% |
| Raw p draw away | 36.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.34 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -8.3% |
| Under 2.5 probability edge | +8.3% |
| Raw edge prob home | -0.0722 |
| Raw ev home | -0.0481 |
| Raw edge prob draw | 0.0390 |
| Raw ev draw | 0.0068 |
| Raw edge prob away | 0.0333 |
| Raw ev away | 0.1169 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **60.3%**. Expected goals are 1.37 for Lazio and 0.66 for Parma (2.03 combined). The most likely exact score is 1-0 at 20.0%. Goal-market probabilities: at least one goal: 88.6%; Over 2.5 goals: 34.6%; Under 3.5 goals: 84.7%; Double Chance 1X: 84.6%; Double Chance X2: 39.7%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 94.1%; BTTS Yes (both teams score): 35.1%; BTTS No (at least one team does not score): 64.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 60.3% | 1.66 |
| Draw | 24.3% | 4.12 |
| Parma win | 15.4% | 6.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.37 |
| Parma expected goals | 0.66 |
| Expected total goals | 2.03 |
| Over 0.5 | 88.6% |
| Under 0.5 | 11.4% |
| Over 1.5 | 61.2% |
| Under 1.5 | 38.8% |
| Over 2.5 | 34.6% |
| Under 2.5 | 65.4% |
| Over 3.5 | 15.3% |
| Under 3.5 | 84.7% |
| Over 4.5 | 5.9% |
| Under 4.5 | 94.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.02% |
| 2 | 2-0 | 13.78% |
| 3 | 0-0 | 11.42% |
| 4 | 1-1 | 10.32% |
| 5 | 2-1 | 9.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 60.3% | 66.5% | 1.58 | -4.7% |
| Draw | 24.3% | 20.5% | 4.33 | +5.2% |
| Parma win | 15.4% | 12.9% | 6.64 | +2.2% |
| Over 2.5 | 34.6% | 49.7% | 2.06 | -28.7% |
| Under 2.5 | 65.4% | 50.3% | 1.89 | +23.6% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3728 |
| Dc lambda away | 0.6578 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 35.1% |
| P btts no | 64.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.76 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.89 |
| Fair Under 2.5 odds | 1.53 |
| Fair Over 3.5 odds | 6.52 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.02 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 54.1% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 17.8% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 36.0% |
| P home draw | 84.6% |
| P draw away | 39.7% |
| P home away | 75.7% |
| Raw p home draw | 82.2% |
| Raw p draw away | 45.9% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.42 |
| Reference draw odds | 3.90 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | -6.2% |
| Draw probability edge | +3.8% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -15.1% |
| Under 2.5 probability edge | +15.1% |
| Raw edge prob home | -0.1239 |
| Raw ev home | -0.1449 |
| Raw edge prob draw | 0.0751 |
| Raw ev draw | 0.2148 |
| Raw edge prob away | 0.0487 |
| Raw ev away | 0.1834 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **AS Roma win** at **41.9%**. Expected goals are 0.98 for Napoli and 1.19 for AS Roma (2.16 combined). The most likely exact score is 0-1 at 14.0%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 37.2%; Under 3.5 goals: 82.6%; Double Chance 1X: 58.1%; Double Chance X2: 70.0%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 93.0%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 30.0% | 3.33 |
| Draw | 28.1% | 3.56 |
| AS Roma win | 41.9% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 0.98 |
| AS Roma expected goals | 1.19 |
| Expected total goals | 2.16 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 63.8% |
| Under 1.5 | 36.2% |
| Over 2.5 | 37.2% |
| Under 2.5 | 62.8% |
| Over 3.5 | 17.4% |
| Under 3.5 | 82.6% |
| Over 4.5 | 7.0% |
| Under 4.5 | 93.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.99% |
| 2 | 1-1 | 12.81% |
| 3 | 1-0 | 11.15% |
| 4 | 0-0 | 11.06% |
| 5 | 0-2 | 8.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 30.0% | 30.0% | 3.04 | -8.7% |
| Draw | 28.1% | 26.8% | 3.60 | +1.1% |
| AS Roma win | 41.9% | 43.2% | 2.45 | +2.6% |
| Over 2.5 | 37.2% | 51.5% | 1.93 | -28.3% |
| Under 2.5 | 62.8% | 48.5% | 2.01 | +26.3% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9781 |
| Dc lambda away | 1.1857 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.04 |
| Fair Over 1.5 odds | 1.57 |
| Fair Under 1.5 odds | 2.76 |
| Fair Over 2.5 odds | 2.69 |
| Fair Under 2.5 odds | 1.59 |
| Fair Over 3.5 odds | 5.74 |
| Fair Under 3.5 odds | 1.21 |
| Fair Over 4.5 odds | 14.37 |
| Fair Under 4.5 odds | 1.07 |
| Unadjusted home-win probability | 30.1% |
| Unadjusted draw probability | 29.3% |
| Unadjusted away-win probability | 40.6% |
| Raw p over 1 5 | 63.7% |
| Raw p under 3 5 | 82.6% |
| Raw p btts yes | 43.4% |
| P home draw | 58.1% |
| P draw away | 70.0% |
| P home away | 71.9% |
| Raw p home draw | 59.4% |
| Raw p draw away | 69.9% |
| Raw p home away | 70.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 2.90 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +0.0% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -14.3% |
| Under 2.5 probability edge | +14.3% |
| Raw edge prob home | 0.0010 |
| Raw ev home | -0.0856 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0563 |
| Raw edge prob away | -0.0262 |
| Raw ev away | -0.0058 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **55.2%**. Expected goals are 1.77 for Atalanta BC and 1.27 for Frosinone (3.04 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.4%; Double Chance 1X: 76.9%; Double Chance X2: 44.8%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 80.4%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 55.2% | 1.81 |
| Draw | 21.7% | 4.61 |
| Frosinone win | 23.1% | 4.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 1.77 |
| Frosinone expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
| Over 1.5 | 81.0% |
| Under 1.5 | 19.0% |
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.6% |
| Under 4.5 | 80.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.67% |
| 2 | 1-1 | 10.00% |
| 3 | 1-0 | 9.42% |
| 4 | 2-0 | 8.41% |
| 5 | 3-1 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 55.2% | 61.1% | 1.72 | -5.1% |
| Draw | 21.7% | 20.0% | 4.37 | -5.2% |
| Frosinone win | 23.1% | 18.9% | 4.88 | +12.9% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7745 |
| Dc lambda away | 1.2688 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.38 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.27 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.10 |
| Fair Under 4.5 odds | 1.24 |
| Unadjusted home-win probability | 49.2% |
| Unadjusted draw probability | 23.4% |
| Unadjusted away-win probability | 27.4% |
| Raw p over 1 5 | 80.8% |
| Raw p under 3 5 | 63.8% |
| Raw p btts yes | 59.7% |
| P home draw | 76.9% |
| P draw away | 44.8% |
| P home away | 78.3% |
| Raw p home draw | 72.6% |
| Raw p draw away | 50.8% |
| Raw p home away | 76.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.54 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Home probability edge | -5.9% |
| Draw probability edge | +1.7% |
| Away probability edge | +4.2% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | -0.1185 |
| Raw ev home | -0.1530 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | 0.0223 |
| Raw edge prob away | 0.0844 |
| Raw ev away | 0.3353 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **50.7%**. Expected goals are 1.55 for Genoa and 0.90 for Venezia (2.45 combined). The most likely exact score is 1-0 at 12.8%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 44.3%; Under 3.5 goals: 76.9%; Double Chance 1X: 76.5%; Double Chance X2: 49.3%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 50.7% | 1.97 |
| Draw | 25.8% | 3.87 |
| Venezia win | 23.5% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.55 |
| Venezia expected goals | 0.90 |
| Expected total goals | 2.45 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 70.2% |
| Under 1.5 | 29.8% |
| Over 2.5 | 44.3% |
| Under 2.5 | 55.7% |
| Over 3.5 | 23.1% |
| Under 3.5 | 76.9% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.84% |
| 2 | 1-1 | 12.16% |
| 3 | 2-0 | 9.99% |
| 4 | 2-1 | 9.03% |
| 5 | 0-0 | 8.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 50.7% | 49.0% | 2.14 | +8.4% |
| Draw | 25.8% | 25.9% | 3.44 | -11.2% |
| Venezia win | 23.5% | 25.1% | 3.87 | -9.0% |
| Over 2.5 | 44.3% | 51.5% | 1.97 | -12.8% |
| Under 2.5 | 55.7% | 48.5% | 1.98 | +10.4% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.5486 |
| Dc lambda away | 0.9041 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.49 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.35 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.33 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.81 |
| Fair Under 4.5 odds | 1.11 |
| Unadjusted home-win probability | 52.4% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 21.9% |
| Raw p over 1 5 | 70.3% |
| Raw p under 3 5 | 76.8% |
| Raw p btts yes | 46.9% |
| P home draw | 76.5% |
| P draw away | 49.3% |
| P home away | 74.2% |
| Raw p home draw | 78.1% |
| Raw p draw away | 47.6% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.1% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -7.2% |
| Under 2.5 probability edge | +7.2% |
| Raw edge prob home | 0.0336 |
| Raw ev home | 0.1204 |
| Raw edge prob draw | -0.0023 |
| Raw ev draw | -0.1157 |
| Raw edge prob away | -0.0314 |
| Raw ev away | -0.1509 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **74.7%**. Expected goals are 2.81 for Inter Milan and 0.94 for Fiorentina (3.75 combined). The most likely exact score is 2-0 at 9.1%. Goal-market probabilities: at least one goal: 97.5%; Over 2.5 goals: 72.1%; Under 3.5 goals: 48.6%; Double Chance 1X: 89.3%; Double Chance X2: 25.3%; Double Chance 12 (either team wins): 85.4%; Under 4.5 goals: 67.9%; BTTS Yes (both teams score): 57.6%; BTTS No (at least one team does not score): 42.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 74.7% | 1.34 |
| Draw | 14.6% | 6.84 |
| Fiorentina win | 10.7% | 9.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.81 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.75 |
| Over 0.5 | 97.5% |
| Under 0.5 | 2.5% |
| Over 1.5 | 88.7% |
| Under 1.5 | 11.3% |
| Over 2.5 | 72.1% |
| Under 2.5 | 27.9% |
| Over 3.5 | 51.4% |
| Under 3.5 | 48.6% |
| Over 4.5 | 32.1% |
| Under 4.5 | 67.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.11% |
| 2 | 2-1 | 8.58% |
| 3 | 3-0 | 8.53% |
| 4 | 3-1 | 8.04% |
| 5 | 1-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 74.7% | 73.5% | 1.41 | +5.4% |
| Draw | 14.6% | 15.1% | 5.56 | -18.7% |
| Fiorentina win | 10.7% | 11.5% | 7.90 | -15.9% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8098 |
| Dc lambda away | 0.9425 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 57.6% |
| P btts no | 42.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 40.78 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.87 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.06 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 76.0% |
| Unadjusted draw probability | 14.2% |
| Unadjusted away-win probability | 9.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 48.3% |
| Raw p btts yes | 57.4% |
| P home draw | 89.3% |
| P draw away | 25.3% |
| P home away | 85.4% |
| Raw p home draw | 90.2% |
| Raw p draw away | 24.0% |
| Raw p home away | 85.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 1.30 |
| Reference draw odds | 5.00 |
| Reference away odds | 6.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Home probability edge | +1.3% |
| Draw probability edge | -0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | +5.5% |
| Under 2.5 probability edge | -5.5% |
| Raw edge prob home | 0.0256 |
| Raw ev home | 0.0718 |
| Raw edge prob draw | -0.0090 |
| Raw ev draw | -0.2123 |
| Raw edge prob away | -0.0166 |
| Raw ev away | -0.2242 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **67.6%**. Expected goals are 0.61 for Lecce and 1.64 for Juventus (2.24 combined). The most likely exact score is 0-1 at 18.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.5%; Double Chance 1X: 32.4%; Double Chance X2: 88.4%; Double Chance 12 (either team wins): 79.2%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 35.7%; BTTS No (at least one team does not score): 64.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 11.6% | 8.64 |
| Draw | 20.8% | 4.81 |
| Juventus win | 67.6% | 1.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.61 |
| Juventus expected goals | 1.64 |
| Expected total goals | 2.24 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 66.6% |
| Under 1.5 | 33.4% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 19.5% |
| Under 3.5 | 80.5% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 18.75% |
| 2 | 0-2 | 15.41% |
| 3 | 1-2 | 9.32% |
| 4 | 0-0 | 9.18% |
| 5 | 1-1 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 11.6% | 9.8% | 7.70 | -10.9% |
| Draw | 20.8% | 17.5% | 4.53 | -5.8% |
| Juventus win | 67.6% | 72.8% | 1.50 | +1.4% |
| Over 2.5 | 40.4% | 50.0% | 1.92 | -22.5% |
| Under 2.5 | 59.6% | 50.0% | 2.02 | +20.5% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 0.6051 |
| Dc lambda away | 1.6392 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.7% |
| P btts no | 64.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.89 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.99 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.12 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.29 |
| Fair Under 4.5 odds | 1.09 |
| Unadjusted home-win probability | 13.4% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 62.5% |
| Raw p over 1 5 | 65.7% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 36.6% |
| P home draw | 32.4% |
| P draw away | 88.4% |
| P home away | 79.2% |
| Raw p home draw | 37.5% |
| Raw p draw away | 86.6% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 7.20 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.31 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +1.8% |
| Draw probability edge | +3.3% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0358 |
| Raw ev home | 0.0288 |
| Raw edge prob draw | 0.0667 |
| Raw ev draw | 0.0931 |
| Raw edge prob away | -0.1025 |
| Raw ev away | -0.0624 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.6%**. Expected goals are 1.04 for Udinese and 1.56 for AC Milan (2.61 combined). The most likely exact score is 0-1 at 12.2%. Goal-market probabilities: at least one goal: 92.8%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.2%; Double Chance 1X: 47.4%; Double Chance X2: 77.3%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 22.7% | 4.41 |
| Draw | 24.7% | 4.04 |
| AC Milan win | 52.6% | 1.90 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.56 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.8% |
| Under 0.5 | 7.2% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 12.22% |
| 2 | 1-1 | 11.77% |
| 3 | 1-2 | 10.03% |
| 4 | 0-2 | 9.61% |
| 5 | 0-0 | 7.23% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 22.7% | 20.1% | 4.68 | +6.1% |
| Draw | 24.7% | 24.1% | 3.91 | -3.3% |
| AC Milan win | 52.6% | 55.8% | 1.83 | -3.8% |
| Over 2.5 | 48.7% | 50.0% | 1.97 | -4.0% |
| Under 2.5 | 51.3% | 50.0% | 1.97 | +1.0% |

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
| Market best home last update utc | 2026-10-18T08:36:06Z |
| Market best draw last update utc | 2026-10-18T08:36:06Z |
| Market best away last update utc | 2026-10-18T08:36:06Z |
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
| Dc lambda home | 1.0438 |
| Dc lambda away | 1.5649 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:27.418900+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.84 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.73 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 7.98 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 25.2% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 49.3% |
| Raw p over 1 5 | 73.5% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 51.3% |
| P home draw | 47.4% |
| P draw away | 77.3% |
| P home away | 75.3% |
| Raw p home draw | 50.7% |
| Raw p draw away | 74.8% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Unibet (FR) |
| Reference home odds | 4.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 1.67 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:26Z |
| Market reference home last update utc | 2026-10-18T08:36:26Z |
| Market reference draw last update utc | 2026-10-18T08:36:26Z |
| Market reference away last update utc | 2026-10-18T08:36:26Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.88 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:26Z |
| Market best over 2 5 last update utc | 2026-10-18T08:36:06Z |
| Market best under 2 5 last update utc | 2026-10-18T08:36:06Z |
| Home probability edge | +2.6% |
| Draw probability edge | +0.7% |
| Away probability edge | -3.2% |
| Over 2.5 probability edge | -1.3% |
| Under 2.5 probability edge | +1.3% |
| Raw edge prob home | 0.0514 |
| Raw ev home | 0.1815 |
| Raw edge prob draw | 0.0134 |
| Raw ev draw | -0.0066 |
| Raw edge prob away | -0.0647 |
| Raw ev away | -0.0969 |

</details>


---
