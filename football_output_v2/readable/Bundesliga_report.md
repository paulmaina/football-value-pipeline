# Bundesliga — football model report

Fixtures in this report: **11**.

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
| Training sha256 | e1a609f9677ca1d796419fdb654360dd875a4511ee6b12aa590f932ef9603c0f |
| Training as of utc | 2026-10-18T08:36:11.911617+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 52, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 52, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T08:36:11.911617+00:00', 'observations': 62, 'observations_sha256': 'e6fc5188c8da74f77a29db3c516fbc8337c942eb35299db631759f1a2784ad36', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 43, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 5, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '5da75b806449591c4436ba24040da3144bd83dabc668958df1906363afd8eee4', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
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
| Live odds matched | 11.00 |
| Additional event odds calls used before this league | 10.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261018T083611911617Z_34bfbb90b7afa2480377f915b8b190be1d8cb0d3ae442fd9e316fafad2d52b43.json |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 2.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 2.00 |
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

## 2026-10-18 — Bayer Leverkusen vs SC Freiburg

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **65.6%**. Expected goals are 2.47 for Bayer Leverkusen and 0.98 for SC Freiburg (3.45 combined). The most likely exact score is 2-0 at 9.2%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 66.4%; Under 3.5 goals: 55.4%; Double Chance 1X: 84.8%; Double Chance X2: 34.4%; Double Chance 12 (either team wins): 80.9%; Under 4.5 goals: 73.9%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 65.6% | 1.52 |
| Draw | 19.1% | 5.23 |
| SC Freiburg win | 15.2% | 6.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.47 |
| SC Freiburg expected goals | 0.98 |
| Expected total goals | 3.45 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 66.4% |
| Under 2.5 | 33.6% |
| Over 3.5 | 44.6% |
| Under 3.5 | 55.4% |
| Over 4.5 | 26.1% |
| Under 4.5 | 73.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.19% |
| 2 | 2-1 | 8.99% |
| 3 | 1-1 | 8.74% |
| 4 | 3-0 | 7.57% |
| 5 | 3-1 | 7.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 65.6% | 62.0% | 1.65 | +8.3% |
| Draw | 19.1% | 19.8% | 4.67 | -10.7% |
| SC Freiburg win | 15.2% | 18.2% | 5.17 | -21.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-18T13:30:00+00:00 |
| Fixture id | 096d800bcc95c547ef592cbef624d080 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4709 |
| Dc lambda away | 0.9784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.65 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.27 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.98 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 69.3% |
| Unadjusted draw probability | 18.4% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 54.8% |
| Raw p btts yes | 57.9% |
| P home draw | 84.8% |
| P draw away | 34.4% |
| P home away | 80.9% |
| Raw p home draw | 87.7% |
| Raw p draw away | 30.7% |
| Raw p home away | 81.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.57 |
| Reference draw odds | 4.60 |
| Reference away odds | 5.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | +3.7% |
| Draw probability edge | -0.7% |
| Away probability edge | -2.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | 0.0730 |
| Raw ev home | 0.1434 |
| Raw edge prob draw | -0.0143 |
| Raw ev draw | -0.1402 |
| Raw edge prob away | -0.0587 |
| Raw ev away | -0.3645 |
| Market p home draw | 81.1% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:35:50Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.9% |
| Market draw away odds | 2.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:35:50Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:35:50Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.44 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T08:34:20Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 6.20 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.7% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T08:34:20Z |
| Market reference under 3 5 odds | 1.75 |
| Market reference under 3 5 opposite odds | 2.18 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.57 |
| Market reference btts yes last update utc | 2026-10-18T08:35:50Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **41.1%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.1%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.9%; Under 3.5 goals: 48.9%; Double Chance 1X: 58.9%; Double Chance X2: 64.1%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 72.2%; BTTS No (at least one team does not score): 27.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 35.9% | 2.79 |
| Draw | 23.0% | 4.34 |
| TSG Hoffenheim win | 41.1% | 2.44 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.94 |
| TSG Hoffenheim expected goals | 1.79 |
| Expected total goals | 3.73 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 71.9% |
| Under 2.5 | 28.1% |
| Over 3.5 | 51.1% |
| Under 3.5 | 48.9% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.12% |
| 2 | 1-2 | 8.64% |
| 3 | 2-2 | 7.23% |
| 4 | 2-1 | 6.98% |
| 5 | 1-3 | 5.15% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 35.9% | 30.2% | 3.21 | +15.2% |
| Draw | 23.0% | 23.0% | 4.21 | -3.0% |
| TSG Hoffenheim win | 41.1% | 46.8% | 2.15 | -11.7% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
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
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 72.2% |
| P btts no | 27.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.36 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.45 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.56 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.8% |
| Raw p btts yes | 72.1% |
| P home draw | 58.9% |
| P draw away | 64.1% |
| P home away | 77.0% |
| Raw p home draw | 64.6% |
| Raw p draw away | 58.4% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 3.10 |
| Reference draw odds | 4.00 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.37 |
| Reference Under 2.5 odds | 3.15 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | +5.7% |
| Draw probability edge | -0.0% |
| Away probability edge | -5.7% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.1143 |
| Raw ev home | 0.3357 |
| Raw edge prob draw | -0.0002 |
| Raw ev draw | -0.0306 |
| Raw edge prob away | -0.1141 |
| Raw ev away | -0.2397 |
| Market p home draw | 54.5% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T08:35:23Z |
| Market reference home draw last update utc | 2026-10-18T08:36:02Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.2% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T08:35:23Z |
| Market reference draw away last update utc | 2026-10-18T08:36:02Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.3% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T08:35:23Z |
| Market reference home away last update utc | 2026-10-18T08:36:02Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.78 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 88.7% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market reference over 1 5 last update utc | 2026-10-18T08:36:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 51.0% |
| Market reference under 3 5 odds | 1.87 |
| Market reference under 3 5 opposite odds | 1.94 |
| Market reference under 3 5 last update utc | 2026-10-18T08:36:05Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 71.7% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T08:35:23Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 3.31 |
| Market reference btts yes last update utc | 2026-10-18T08:36:02Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.4%**. Expected goals are 2.52 for VfB Stuttgart and 1.19 for Borussia Monchengladbach (3.71 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.4%; Under 3.5 goals: 48.7%; Double Chance 1X: 85.5%; Double Chance X2: 31.6%; Double Chance 12 (either team wins): 82.9%; Under 4.5 goals: 67.9%; BTTS Yes (both teams score): 64.2%; BTTS No (at least one team does not score): 35.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.4% | 1.46 |
| Draw | 17.1% | 5.86 |
| Borussia Monchengladbach win | 14.5% | 6.89 |

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
| Over 2.5 | 72.4% |
| Under 2.5 | 27.6% |
| Over 3.5 | 51.3% |
| Under 3.5 | 48.7% |
| Over 4.5 | 32.1% |
| Under 4.5 | 67.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.66% |
| 2 | 3-1 | 8.11% |
| 3 | 2-0 | 8.10% |
| 4 | 1-1 | 7.25% |
| 5 | 3-0 | 6.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.4% | 71.4% | 1.43 | -2.1% |
| Draw | 17.1% | 15.2% | 5.80 | -1.0% |
| Borussia Monchengladbach win | 14.5% | 13.4% | 6.98 | +1.3% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5189 |
| Dc lambda away | 1.1932 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.2% |
| P btts no | 35.8% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 35.34 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.44 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.63 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.12 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 65.5% |
| Unadjusted draw probability | 18.9% |
| Unadjusted away-win probability | 15.6% |
| Raw p over 1 5 | 89.2% |
| Raw p under 3 5 | 49.2% |
| Raw p btts yes | 64.8% |
| P home draw | 85.5% |
| P draw away | 31.6% |
| P home away | 82.9% |
| Raw p home draw | 84.4% |
| Raw p draw away | 34.5% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.37 |
| Reference draw odds | 5.80 |
| Reference away odds | 6.50 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.76 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -2.9% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0586 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0373 |
| Raw ev draw | 0.0978 |
| Raw edge prob away | 0.0213 |
| Raw ev away | 0.0873 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.9%**. Expected goals are 0.88 for 1. FC Köln and 0.73 for FC Schalke 04 (1.61 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 82.2%; Over 2.5 goals: 23.4%; Under 3.5 goals: 91.8%; Double Chance 1X: 73.2%; Double Chance X2: 58.1%; Double Chance 12 (either team wins): 68.7%; Under 4.5 goals: 97.4%; BTTS Yes (both teams score): 30.2%; BTTS No (at least one team does not score): 69.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.9% | 2.39 |
| Draw | 31.3% | 3.19 |
| FC Schalke 04 win | 26.8% | 3.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.88 |
| FC Schalke 04 expected goals | 0.73 |
| Expected total goals | 1.61 |
| Over 0.5 | 82.2% |
| Under 0.5 | 17.8% |
| Over 1.5 | 49.6% |
| Under 1.5 | 50.4% |
| Over 2.5 | 23.4% |
| Under 2.5 | 76.6% |
| Over 3.5 | 8.2% |
| Under 3.5 | 91.8% |
| Over 4.5 | 2.6% |
| Under 4.5 | 97.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.33% |
| 2 | 0-0 | 17.78% |
| 3 | 0-1 | 13.32% |
| 4 | 1-1 | 11.73% |
| 5 | 2-0 | 9.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.9% | 48.1% | 2.12 | -11.2% |
| Draw | 31.3% | 25.2% | 3.98 | +24.8% |
| FC Schalke 04 win | 26.8% | 26.7% | 3.43 | -8.1% |
| Over 2.5 | 23.4% | 61.8% | 1.64 | -61.6% |
| Under 2.5 | 76.6% | 38.2% | 2.46 | +88.3% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
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
| Dc lambda home | 0.8792 |
| Dc lambda away | 0.7267 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 30.2% |
| P btts no | 69.8% |
| Fair Over 0.5 odds | 1.22 |
| Fair Under 0.5 odds | 5.62 |
| Fair Over 1.5 odds | 2.02 |
| Fair Under 1.5 odds | 1.98 |
| Fair Over 2.5 odds | 4.27 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 12.18 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 38.33 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 37.5% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 48.9% |
| Raw p under 3 5 | 92.0% |
| Raw p btts yes | 31.4% |
| P home draw | 73.2% |
| P draw away | 58.1% |
| P home away | 68.7% |
| Raw p home draw | 73.1% |
| Raw p draw away | 64.4% |
| Raw p home away | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.00 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.50 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:07Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:07Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -6.3% |
| Draw probability edge | +6.2% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -38.3% |
| Under 2.5 probability edge | +38.3% |
| Raw edge prob home | -0.1256 |
| Raw ev home | -0.2455 |
| Raw edge prob draw | 0.1236 |
| Raw ev draw | 0.4936 |
| Raw edge prob away | 0.0020 |
| Raw ev away | -0.0779 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **50.1%**. Expected goals are 1.54 for Augsburg and 1.03 for Union Berlin (2.57 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.2%; Under 3.5 goals: 74.1%; Double Chance 1X: 75.7%; Double Chance X2: 49.9%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 50.1% | 1.99 |
| Draw | 25.5% | 3.92 |
| Union Berlin win | 24.3% | 4.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.54 |
| Union Berlin expected goals | 1.03 |
| Expected total goals | 2.57 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 74.0% |
| Under 1.5 | 26.0% |
| Over 2.5 | 48.2% |
| Under 2.5 | 51.8% |
| Over 3.5 | 25.9% |
| Under 3.5 | 74.1% |
| Over 4.5 | 12.1% |
| Under 4.5 | 87.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 1-0 | 11.15% |
| 3 | 2-1 | 9.77% |
| 4 | 2-0 | 9.50% |
| 5 | 0-0 | 8.10% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 50.1% | 52.3% | 1.96 | -1.7% |
| Draw | 25.5% | 23.2% | 4.16 | +6.2% |
| Union Berlin win | 24.3% | 24.5% | 3.77 | -8.3% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5381 |
| Dc lambda away | 1.0276 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.35 |
| Fair Over 1.5 odds | 1.35 |
| Fair Under 1.5 odds | 3.84 |
| Fair Over 2.5 odds | 2.08 |
| Fair Under 2.5 odds | 1.93 |
| Fair Over 3.5 odds | 3.87 |
| Fair Under 3.5 odds | 1.35 |
| Fair Over 4.5 odds | 8.29 |
| Fair Under 4.5 odds | 1.14 |
| Unadjusted home-win probability | 48.0% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 24.2% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 74.3% |
| Raw p btts yes | 51.6% |
| P home draw | 75.7% |
| P draw away | 49.9% |
| P home away | 74.5% |
| Raw p home draw | 75.8% |
| Raw p draw away | 52.0% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.85 |
| Reference draw odds | 4.00 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -2.2% |
| Draw probability edge | +2.3% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -14.2% |
| Under 2.5 probability edge | +14.2% |
| Raw edge prob home | -0.0434 |
| Raw ev home | -0.0600 |
| Raw edge prob draw | 0.0467 |
| Raw ev draw | 0.1596 |
| Raw edge prob away | -0.0033 |
| Raw ev away | -0.0889 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **64.3%**. Expected goals are 2.26 for Borussia Dortmund and 1.23 for Eintracht Frankfurt (3.49 combined). The most likely exact score is 2-1 at 10.3%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.8%; Under 3.5 goals: 53.4%; Double Chance 1X: 83.0%; Double Chance X2: 35.7%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 72.1%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 64.3% | 1.56 |
| Draw | 18.8% | 5.33 |
| Eintracht Frankfurt win | 17.0% | 5.89 |

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
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 46.6% |
| Under 3.5 | 53.4% |
| Over 4.5 | 27.9% |
| Under 4.5 | 72.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.32% |
| 2 | 2-0 | 8.38% |
| 3 | 1-1 | 8.21% |
| 4 | 3-1 | 7.76% |
| 5 | 1-0 | 6.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 64.3% | 68.9% | 1.48 | -4.9% |
| Draw | 18.8% | 16.3% | 5.39 | +1.1% |
| Eintracht Frankfurt win | 17.0% | 14.9% | 6.42 | +8.9% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2570 |
| Dc lambda away | 1.2319 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.32 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.14 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.58 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.9% |
| Raw p btts yes | 64.2% |
| P home draw | 83.0% |
| P draw away | 35.7% |
| P home away | 81.2% |
| Raw p home draw | 80.9% |
| Raw p draw away | 40.3% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.42 |
| Reference draw odds | 5.50 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -4.6% |
| Draw probability edge | +2.5% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | -0.0917 |
| Raw ev home | -0.1168 |
| Raw edge prob draw | 0.0494 |
| Raw ev draw | 0.1445 |
| Raw edge prob away | 0.0423 |
| Raw ev away | 0.2254 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **52.8%**. Expected goals are 1.60 for FSV Mainz 05 and 1.15 for Werder Bremen (2.75 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 53.0%; Under 3.5 goals: 69.9%; Double Chance 1X: 77.0%; Double Chance X2: 47.2%; Double Chance 12 (either team wins): 75.8%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 54.8%; BTTS No (at least one team does not score): 45.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 52.8% | 1.89 |
| Draw | 24.2% | 4.14 |
| Werder Bremen win | 23.0% | 4.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.60 |
| Werder Bremen expected goals | 1.15 |
| Expected total goals | 2.75 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 77.5% |
| Under 1.5 | 22.5% |
| Over 2.5 | 53.0% |
| Under 2.5 | 47.0% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 2-1 | 10.63% |
| 3 | 1-0 | 10.31% |
| 4 | 2-0 | 9.26% |
| 5 | 0-0 | 6.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 52.8% | 58.8% | 1.73 | -8.7% |
| Draw | 24.2% | 21.3% | 4.41 | +6.6% |
| Werder Bremen win | 23.0% | 19.9% | 4.72 | +8.7% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
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
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.8% |
| P btts no | 45.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.88 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.44 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.70 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 55.6% |
| P home draw | 77.0% |
| P draw away | 47.2% |
| P home away | 75.8% |
| Raw p home draw | 73.8% |
| Raw p draw away | 53.2% |
| Raw p home away | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.65 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -6.0% |
| Draw probability edge | +2.9% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -10.3% |
| Under 2.5 probability edge | +10.3% |
| Raw edge prob home | -0.1205 |
| Raw ev home | -0.1909 |
| Raw edge prob draw | 0.0571 |
| Raw ev draw | 0.1922 |
| Raw edge prob away | 0.0634 |
| Raw ev away | 0.2363 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **63.3%**. Expected goals are 2.46 for RB Leipzig and 1.69 for Elversberg (4.15 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 79.2%; Under 3.5 goals: 39.9%; Double Chance 1X: 81.2%; Double Chance X2: 36.7%; Double Chance 12 (either team wins): 82.1%; Under 4.5 goals: 59.1%; BTTS Yes (both teams score): 74.4%; BTTS No (at least one team does not score): 25.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 63.3% | 1.58 |
| Draw | 17.9% | 5.59 |
| Elversberg win | 18.8% | 5.32 |

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
| Over 2.5 | 79.2% |
| Under 2.5 | 20.8% |
| Over 3.5 | 60.1% |
| Under 3.5 | 39.9% |
| Over 4.5 | 40.9% |
| Under 4.5 | 59.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.43% |
| 2 | 3-1 | 7.73% |
| 3 | 3-2 | 6.53% |
| 4 | 1-1 | 6.33% |
| 5 | 2-2 | 6.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 63.3% | 72.5% | 1.40 | -11.3% |
| Draw | 17.9% | 15.5% | 6.02 | +7.7% |
| Elversberg win | 18.8% | 12.0% | 7.50 | +40.9% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4580 |
| Dc lambda away | 1.6888 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 74.4% |
| P btts no | 25.6% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 51.50 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.76 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.80 |
| Fair Over 3.5 odds | 1.66 |
| Fair Under 3.5 odds | 2.51 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.69 |
| Unadjusted home-win probability | 54.2% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 25.5% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.5% |
| Raw p btts yes | 75.2% |
| P home draw | 81.2% |
| P draw away | 36.7% |
| P home away | 82.1% |
| Raw p home draw | 74.5% |
| Raw p draw away | 45.8% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 1.35 |
| Reference draw odds | 5.70 |
| Reference away odds | 7.20 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.28 |
| Reference Under 2.5 odds | 3.72 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -9.2% |
| Draw probability edge | +2.4% |
| Away probability edge | +6.7% |
| Over 2.5 probability edge | +2.9% |
| Under 2.5 probability edge | -2.9% |
| Raw edge prob home | -0.1832 |
| Raw ev home | -0.2417 |
| Raw edge prob draw | 0.0484 |
| Raw ev draw | 0.2230 |
| Raw edge prob away | 0.1348 |
| Raw ev away | 0.9139 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **37.4%**. Expected goals are 1.01 for SC Paderborn and 0.98 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 13.8%. Goal-market probabilities: at least one goal: 86.6%; Over 2.5 goals: 33.0%; Under 3.5 goals: 85.9%; Double Chance 1X: 67.2%; Double Chance X2: 62.6%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 94.7%; BTTS Yes (both teams score): 40.0%; BTTS No (at least one team does not score): 60.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 37.4% | 2.68 |
| Draw | 29.8% | 3.36 |
| Hamburger SV win | 32.8% | 3.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.01 |
| Hamburger SV expected goals | 0.98 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.6% |
| Under 0.5 | 13.4% |
| Over 1.5 | 60.5% |
| Under 1.5 | 39.5% |
| Over 2.5 | 33.0% |
| Under 2.5 | 67.0% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.3% |
| Under 4.5 | 94.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.82% |
| 2 | 0-0 | 13.36% |
| 3 | 1-1 | 13.14% |
| 4 | 0-1 | 12.32% |
| 5 | 2-0 | 7.66% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 37.4% | 40.7% | 2.40 | -10.3% |
| Draw | 29.8% | 26.0% | 3.92 | +16.8% |
| Hamburger SV win | 32.8% | 33.3% | 2.91 | -4.4% |
| Over 2.5 | 33.0% | 61.8% | 1.64 | -45.8% |
| Under 2.5 | 67.0% | 38.2% | 2.47 | +65.4% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
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
| Dc lambda home | 1.0059 |
| Dc lambda away | 0.9764 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 40.0% |
| P btts no | 60.0% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.48 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.53 |
| Fair Over 2.5 odds | 3.03 |
| Fair Under 2.5 odds | 1.49 |
| Fair Over 3.5 odds | 7.07 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.75 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 33.6% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 40.8% |
| P home draw | 67.2% |
| P draw away | 62.6% |
| P home away | 70.2% |
| Raw p home draw | 67.6% |
| Raw p draw away | 66.0% |
| Raw p home away | 66.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.35 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T08:36:07Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:36:07Z |
| Market best over 2 5 last update utc | 2026-10-18T08:35:23Z |
| Market best under 2 5 last update utc | 2026-10-18T08:35:23Z |
| Home probability edge | -3.4% |
| Draw probability edge | +3.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -28.7% |
| Under 2.5 probability edge | +28.7% |
| Raw edge prob home | -0.0675 |
| Raw ev home | -0.1844 |
| Raw edge prob draw | 0.0757 |
| Raw ev draw | 0.3164 |
| Raw edge prob away | -0.0082 |
| Raw ev away | -0.0562 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **70.9%**. Expected goals are 1.18 for SC Freiburg and 2.79 for Bayern Munich (3.96 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 75.9%; Under 3.5 goals: 44.0%; Double Chance 1X: 29.1%; Double Chance X2: 86.8%; Double Chance 12 (either team wins): 84.0%; Under 4.5 goals: 63.4%; BTTS Yes (both teams score): 65.3%; BTTS No (at least one team does not score): 34.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 13.2% | 7.59 |
| Draw | 16.0% | 6.27 |
| Bayern Munich win | 70.9% | 1.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.18 |
| Bayern Munich expected goals | 2.79 |
| Expected total goals | 3.96 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 75.9% |
| Under 2.5 | 24.1% |
| Over 3.5 | 56.0% |
| Under 3.5 | 44.0% |
| Over 4.5 | 36.6% |
| Under 4.5 | 63.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.74% |
| 2 | 1-3 | 8.12% |
| 3 | 0-2 | 7.43% |
| 4 | 0-3 | 6.90% |
| 5 | 1-1 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 13.2% | 13.4% | 6.52 | -14.1% |
| Draw | 16.0% | 15.2% | 5.80 | -7.4% |
| Bayern Munich win | 70.9% | 71.4% | 1.45 | +2.7% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
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
| Dc lambda away | 2.7859 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 65.3% |
| P btts no | 34.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 42.02 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.36 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.15 |
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
| P home draw | 29.1% |
| P draw away | 86.8% |
| P home away | 84.0% |
| Raw p home draw | 29.6% |
| Raw p draw away | 87.1% |
| Raw p home away | 83.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 6.50 |
| Reference draw odds | 5.80 |
| Reference away odds | 1.37 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.34 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:47Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:47Z |
| Home probability edge | -0.3% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0053 |
| Raw ev home | -0.1579 |
| Raw edge prob draw | 0.0153 |
| Raw ev draw | -0.0302 |
| Raw edge prob away | -0.0100 |
| Raw ev away | 0.0203 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **49.9%**. Expected goals are 1.40 for TSG Hoffenheim and 2.36 for Bayer Leverkusen (3.76 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 71.5%; Under 3.5 goals: 49.1%; Double Chance 1X: 50.1%; Double Chance X2: 72.6%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 68.5%; BTTS Yes (both teams score): 69.7%; BTTS No (at least one team does not score): 30.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 27.4% | 3.64 |
| Draw | 22.6% | 4.42 |
| Bayer Leverkusen win | 49.9% | 2.00 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.40 |
| Bayer Leverkusen expected goals | 2.36 |
| Expected total goals | 3.76 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 89.3% |
| Under 1.5 | 10.7% |
| Over 2.5 | 71.5% |
| Under 2.5 | 28.5% |
| Over 3.5 | 50.9% |
| Under 3.5 | 49.1% |
| Over 4.5 | 31.5% |
| Under 4.5 | 68.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.21% |
| 2 | 1-2 | 7.79% |
| 3 | 2-1 | 7.00% |
| 4 | 2-2 | 6.93% |
| 5 | 1-3 | 6.13% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 27.4% | 33.8% | 2.76 | -24.3% |
| Draw | 22.6% | 24.5% | 4.25 | -3.9% |
| Bayer Leverkusen win | 49.9% | 41.6% | 2.39 | +19.4% |

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
| Market best home last update utc | 2026-10-18T08:35:23Z |
| Market best draw last update utc | 2026-10-18T08:35:23Z |
| Market best away last update utc | 2026-10-18T08:35:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3951 |
| Dc lambda away | 2.3619 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T08:36:11.911617+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 69.7% |
| P btts no | 30.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.85 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.30 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.51 |
| Fair Over 3.5 odds | 1.96 |
| Fair Under 3.5 odds | 2.04 |
| Fair Over 4.5 odds | 3.17 |
| Fair Under 4.5 odds | 1.46 |
| Unadjusted home-win probability | 21.0% |
| Unadjusted draw probability | 20.7% |
| Unadjusted away-win probability | 58.3% |
| Raw p over 1 5 | 89.6% |
| Raw p under 3 5 | 48.2% |
| Raw p btts yes | 68.9% |
| P home draw | 50.1% |
| P draw away | 72.6% |
| P home away | 77.4% |
| Raw p home draw | 41.7% |
| Raw p draw away | 79.0% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Tipico |
| Reference home odds | 2.80 |
| Reference draw odds | 3.80 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-18T08:36:07Z |
| Market reference home last update utc | 2026-10-18T08:36:07Z |
| Market reference draw last update utc | 2026-10-18T08:36:07Z |
| Market reference away last update utc | 2026-10-18T08:36:07Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 3.05 |
| Market reference over 2 5 last update utc | 2026-10-18T08:35:46Z |
| Market reference under 2 5 last update utc | 2026-10-18T08:35:46Z |
| Home probability edge | -6.4% |
| Draw probability edge | -1.9% |
| Away probability edge | +8.3% |
| Over 2.5 probability edge | +1.4% |
| Under 2.5 probability edge | -1.4% |
| Raw edge prob home | -0.1280 |
| Raw ev home | -0.4192 |
| Raw edge prob draw | -0.0384 |
| Raw ev draw | -0.1203 |
| Raw edge prob away | 0.1664 |
| Raw ev away | 0.3924 |

</details>


---
