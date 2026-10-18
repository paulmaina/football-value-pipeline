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
| Training sha256 | 7de5ffc801935c85b53a157c1374aebb5e94c0dc9cb2ea4b6500ba7d027bef7f |
| Training as of utc | 2026-10-18T11:57:16.468991+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 52, 'bbs_added_results': 7, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 52, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-18T11:57:16.468991+00:00', 'observations': 69, 'observations_sha256': '14055384d46eb480440cb8456b658a9a03c2f0fad4ccd5f2d8433e095b178d60', 'eligible_training_matches': 14, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 43, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 5, 'retrospective_eligible_training_matches': 14, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'd0b2e9577288abe1ec04145aa17d927c0dad0636138aea7199a08fa770e09c34', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.'} |
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
| Additional event odds calls used before this league | 9.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261018T115716468991Z_0a326609a4f6271f6781adb52fe93ef4a3101efe87ea1a2f5ef3966ce27ecdb4.json |
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

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **65.1%**. Expected goals are 2.47 for Bayer Leverkusen and 0.98 for SC Freiburg (3.45 combined). The most likely exact score is 2-0 at 9.1%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 66.5%; Under 3.5 goals: 55.5%; Double Chance 1X: 84.0%; Double Chance X2: 34.9%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 73.9%; BTTS Yes (both teams score): 58.4%; BTTS No (at least one team does not score): 41.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 65.1% | 1.53 |
| Draw | 18.8% | 5.31 |
| SC Freiburg win | 16.0% | 6.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.47 |
| SC Freiburg expected goals | 0.98 |
| Expected total goals | 3.45 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 86.2% |
| Under 1.5 | 13.8% |
| Over 2.5 | 66.5% |
| Under 2.5 | 33.5% |
| Over 3.5 | 44.5% |
| Under 3.5 | 55.5% |
| Over 4.5 | 26.1% |
| Under 4.5 | 73.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.12% |
| 2 | 2-1 | 8.92% |
| 3 | 1-1 | 8.60% |
| 4 | 3-0 | 7.51% |
| 5 | 3-1 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 65.1% | 61.0% | 1.65 | +7.5% |
| Draw | 18.8% | 19.3% | 4.67 | -12.1% |
| SC Freiburg win | 16.0% | 19.8% | 5.17 | -17.2% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Leverkusen |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4712 |
| Dc lambda away | 0.9784 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.4% |
| P btts no | 41.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.04 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.25 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 2.99 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Unadjusted home-win probability | 69.3% |
| Unadjusted draw probability | 18.4% |
| Unadjusted away-win probability | 12.3% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 54.8% |
| Raw p btts yes | 57.9% |
| P home draw | 84.0% |
| P draw away | 34.9% |
| P home away | 81.2% |
| Raw p home draw | 87.7% |
| Raw p draw away | 30.7% |
| Raw p home away | 81.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 4.40 |
| Reference away odds | 4.30 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | +4.2% |
| Draw probability edge | -0.4% |
| Away probability edge | -3.7% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0831 |
| Raw ev home | 0.1435 |
| Raw edge prob draw | -0.0085 |
| Raw ev draw | -0.1403 |
| Raw edge prob away | -0.0747 |
| Raw ev away | -0.3647 |
| Market p home draw | 79.6% |
| Market home draw odds | 1.20 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:48Z |
| Market reference home draw last update utc | 2026-10-18T11:57:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 41.5% |
| Market draw away odds | 2.39 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:48Z |
| Market reference draw away last update utc | 2026-10-18T11:57:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.9% |
| Market home away odds | 1.23 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:48Z |
| Market reference home away last update utc | 2026-10-18T11:57:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.20 |
| Market reference dc draw away odds | 2.30 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 89.3% |
| Market over 1 5 odds | 1.09 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-18T11:57:07Z |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:07Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 55.4% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | 1xBet |
| Market best under 3 5 last update utc | 2026-10-18T11:57:07Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.20 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:07Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.1% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:48Z |
| Market reference btts yes odds | 1.55 |
| Market reference btts yes opposite odds | 2.74 |
| Market reference btts yes last update utc | 2026-10-18T11:57:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-18 — Borussia Monchengladbach vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **40.5%**. Expected goals are 1.94 for Borussia Monchengladbach and 1.79 for TSG Hoffenheim (3.73 combined). The most likely exact score is 1-1 at 9.0%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 72.0%; Under 3.5 goals: 48.8%; Double Chance 1X: 59.5%; Double Chance X2: 63.3%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 68.1%; BTTS Yes (both teams score): 72.1%; BTTS No (at least one team does not score): 27.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 36.7% | 2.72 |
| Draw | 22.8% | 4.39 |
| TSG Hoffenheim win | 40.5% | 2.47 |

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
| Over 2.5 | 72.0% |
| Under 2.5 | 28.0% |
| Over 3.5 | 51.2% |
| Under 3.5 | 48.8% |
| Over 4.5 | 31.9% |
| Under 4.5 | 68.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.03% |
| 2 | 1-2 | 8.52% |
| 3 | 2-2 | 7.16% |
| 4 | 2-1 | 7.14% |
| 5 | 1-3 | 5.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 36.7% | 31.8% | 3.21 | +17.9% |
| Draw | 22.8% | 22.6% | 4.21 | -4.0% |
| TSG Hoffenheim win | 40.5% | 45.6% | 2.15 | -13.0% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | M'gladbach |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9442 |
| Dc lambda away | 1.7870 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 72.1% |
| P btts no | 27.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.69 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.46 |
| Fair Over 2.5 odds | 1.39 |
| Fair Under 2.5 odds | 3.58 |
| Fair Over 3.5 odds | 1.95 |
| Fair Under 3.5 odds | 2.05 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Unadjusted home-win probability | 41.6% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 35.4% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.8% |
| Raw p btts yes | 72.1% |
| P home draw | 59.5% |
| P draw away | 63.3% |
| P home away | 77.2% |
| Raw p home draw | 64.6% |
| Raw p draw away | 58.4% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.10 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | +4.9% |
| Draw probability edge | +0.2% |
| Away probability edge | -5.1% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | 0.0980 |
| Raw ev home | 0.3359 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | -0.0307 |
| Raw edge prob away | -0.1025 |
| Raw ev away | -0.2398 |
| Market p home draw | 55.1% |
| Market home draw odds | 1.79 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-10-18T11:56:48Z |
| Market reference home draw last update utc | 2026-10-18T11:57:09Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.2% |
| Market draw away odds | 1.40 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-10-18T11:56:48Z |
| Market reference draw away last update utc | 2026-10-18T11:57:09Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.7% |
| Market home away odds | 1.27 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-10-18T11:56:48Z |
| Market reference home away last update utc | 2026-10-18T11:57:09Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.76 |
| Market reference dc draw away odds | 1.40 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 89.5% |
| Market reference over 1 5 odds | 1.09 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-18T11:57:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 50.3% |
| Market reference under 3 5 odds | 1.94 |
| Market reference under 3 5 opposite odds | 1.96 |
| Market reference under 3 5 last update utc | 2026-10-18T11:57:06Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 71.7% |
| Market btts yes odds | 1.32 |
| Best btts yes bookmaker | 1xBet |
| Market best btts yes last update utc | 2026-10-18T11:56:48Z |
| Market reference btts yes odds | 1.37 |
| Market reference btts yes opposite odds | 3.31 |
| Market reference btts yes last update utc | 2026-10-18T11:57:09Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **68.5%**. Expected goals are 2.52 for VfB Stuttgart and 1.19 for Borussia Monchengladbach (3.71 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 72.6%; Under 3.5 goals: 48.7%; Double Chance 1X: 85.2%; Double Chance X2: 31.5%; Double Chance 12 (either team wins): 83.3%; Under 4.5 goals: 67.8%; BTTS Yes (both teams score): 64.1%; BTTS No (at least one team does not score): 35.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 68.5% | 1.46 |
| Draw | 16.7% | 6.00 |
| Borussia Monchengladbach win | 14.8% | 6.75 |

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
| Over 4.5 | 32.2% |
| Under 4.5 | 67.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.67% |
| 2 | 3-1 | 8.12% |
| 3 | 2-0 | 8.11% |
| 4 | 1-1 | 7.07% |
| 5 | 3-0 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 68.5% | 71.6% | 1.43 | -2.0% |
| Draw | 16.7% | 14.4% | 5.80 | -3.4% |
| Borussia Monchengladbach win | 14.8% | 14.0% | 6.98 | +3.4% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5192 |
| Dc lambda away | 1.1932 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.1% |
| P btts no | 35.9% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.21 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.45 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.65 |
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
| P home draw | 85.2% |
| P draw away | 31.5% |
| P home away | 83.3% |
| Raw p home draw | 84.4% |
| Raw p draw away | 34.5% |
| Raw p home away | 81.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.32 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -3.0% |
| Draw probability edge | +2.3% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0607 |
| Raw ev home | -0.0634 |
| Raw edge prob draw | 0.0454 |
| Raw ev draw | 0.0977 |
| Raw edge prob away | 0.0153 |
| Raw ev away | 0.0871 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **41.8%**. Expected goals are 0.88 for 1. FC Köln and 0.73 for FC Schalke 04 (1.61 combined). The most likely exact score is 1-0 at 19.3%. Goal-market probabilities: at least one goal: 82.9%; Over 2.5 goals: 23.7%; Under 3.5 goals: 91.7%; Double Chance 1X: 72.0%; Double Chance X2: 58.2%; Double Chance 12 (either team wins): 69.8%; Under 4.5 goals: 97.3%; BTTS Yes (both teams score): 30.1%; BTTS No (at least one team does not score): 69.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 41.8% | 2.39 |
| Draw | 30.2% | 3.31 |
| FC Schalke 04 win | 28.0% | 3.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 0.88 |
| FC Schalke 04 expected goals | 0.73 |
| Expected total goals | 1.61 |
| Over 0.5 | 82.9% |
| Under 0.5 | 17.1% |
| Over 1.5 | 49.7% |
| Under 1.5 | 50.3% |
| Over 2.5 | 23.7% |
| Under 2.5 | 76.3% |
| Over 3.5 | 8.3% |
| Under 3.5 | 91.7% |
| Over 4.5 | 2.7% |
| Under 4.5 | 97.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 19.28% |
| 2 | 0-0 | 17.13% |
| 3 | 0-1 | 13.89% |
| 4 | 1-1 | 11.32% |
| 5 | 2-0 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 41.8% | 48.0% | 2.12 | -11.4% |
| Draw | 30.2% | 22.9% | 3.98 | +20.3% |
| FC Schalke 04 win | 28.0% | 29.0% | 3.43 | -4.1% |
| Over 2.5 | 23.7% | 61.8% | 1.64 | -61.1% |
| Under 2.5 | 76.3% | 38.2% | 2.46 | +87.6% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
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
| Dc lambda home | 0.8799 |
| Dc lambda away | 0.7275 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 30.1% |
| P btts no | 69.9% |
| Fair Over 0.5 odds | 1.21 |
| Fair Under 0.5 odds | 5.84 |
| Fair Over 1.5 odds | 2.01 |
| Fair Under 1.5 odds | 1.99 |
| Fair Over 2.5 odds | 4.21 |
| Fair Under 2.5 odds | 1.31 |
| Fair Over 3.5 odds | 12.11 |
| Fair Under 3.5 odds | 1.09 |
| Fair Over 4.5 odds | 37.72 |
| Fair Under 4.5 odds | 1.03 |
| Unadjusted home-win probability | 35.6% |
| Unadjusted draw probability | 37.5% |
| Unadjusted away-win probability | 26.9% |
| Raw p over 1 5 | 49.0% |
| Raw p under 3 5 | 92.0% |
| Raw p btts yes | 31.5% |
| P home draw | 72.0% |
| P draw away | 58.2% |
| P home away | 69.8% |
| Raw p home draw | 73.1% |
| Raw p draw away | 64.4% |
| Raw p home away | 62.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:07Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:07Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:48Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:48Z |
| Home probability edge | -6.2% |
| Draw probability edge | +7.3% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -38.0% |
| Under 2.5 probability edge | +38.0% |
| Raw edge prob home | -0.1243 |
| Raw ev home | -0.2454 |
| Raw edge prob draw | 0.1456 |
| Raw ev draw | 0.4929 |
| Raw edge prob away | -0.0213 |
| Raw ev away | -0.0774 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **49.9%**. Expected goals are 1.54 for Augsburg and 1.03 for Union Berlin (2.57 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.0%; Over 2.5 goals: 48.2%; Under 3.5 goals: 74.2%; Double Chance 1X: 75.2%; Double Chance X2: 50.1%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 87.9%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 49.9% | 2.01 |
| Draw | 25.4% | 3.94 |
| Union Berlin win | 24.8% | 4.04 |

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
| 1 | 1-1 | 12.11% |
| 2 | 1-0 | 11.09% |
| 3 | 2-1 | 9.71% |
| 4 | 2-0 | 9.45% |
| 5 | 0-0 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 49.9% | 51.8% | 1.96 | -2.3% |
| Draw | 25.4% | 22.9% | 4.16 | +5.6% |
| Union Berlin win | 24.8% | 25.4% | 3.77 | -6.7% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5383 |
| Dc lambda away | 1.0276 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.43 |
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
| P home away | 74.6% |
| Raw p home draw | 75.8% |
| Raw p draw away | 52.0% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.55 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -1.9% |
| Draw probability edge | +2.5% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -13.6% |
| Under 2.5 probability edge | +13.6% |
| Raw edge prob home | -0.0381 |
| Raw ev home | -0.0599 |
| Raw edge prob draw | 0.0500 |
| Raw ev draw | 0.1595 |
| Raw edge prob away | -0.0119 |
| Raw ev away | -0.0890 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **63.8%**. Expected goals are 2.26 for Borussia Dortmund and 1.23 for Eintracht Frankfurt (3.49 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.7%; Under 3.5 goals: 53.4%; Double Chance 1X: 82.7%; Double Chance X2: 36.2%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 72.1%; BTTS Yes (both teams score): 63.5%; BTTS No (at least one team does not score): 36.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 63.8% | 1.57 |
| Draw | 18.8% | 5.31 |
| Eintracht Frankfurt win | 17.3% | 5.76 |

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
| 1 | 2-1 | 10.24% |
| 2 | 2-0 | 8.32% |
| 3 | 1-1 | 8.25% |
| 4 | 3-1 | 7.71% |
| 5 | 1-0 | 6.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 63.8% | 67.9% | 1.48 | -5.6% |
| Draw | 18.8% | 16.4% | 5.39 | +1.5% |
| Eintracht Frankfurt win | 17.3% | 15.6% | 6.42 | +11.4% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2572 |
| Dc lambda away | 1.2319 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.5% |
| P btts no | 36.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 29.21 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.93 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.15 |
| Fair Under 3.5 odds | 1.87 |
| Fair Over 4.5 odds | 3.58 |
| Fair Under 4.5 odds | 1.39 |
| Unadjusted home-win probability | 59.7% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 19.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.9% |
| Raw p btts yes | 64.2% |
| P home draw | 82.7% |
| P draw away | 36.2% |
| P home away | 81.2% |
| Raw p home draw | 80.9% |
| Raw p draw away | 40.3% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 4.50 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -4.1% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -4.2% |
| Under 2.5 probability edge | +4.2% |
| Raw edge prob home | -0.0826 |
| Raw ev home | -0.1167 |
| Raw edge prob draw | 0.0478 |
| Raw ev draw | 0.1444 |
| Raw edge prob away | 0.0347 |
| Raw ev away | 0.2253 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.0%**. Expected goals are 1.60 for FSV Mainz 05 and 1.15 for Werder Bremen (2.75 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.2%; Under 3.5 goals: 69.9%; Double Chance 1X: 76.7%; Double Chance X2: 47.0%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 54.7%; BTTS No (at least one team does not score): 45.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.0% | 1.89 |
| Draw | 23.7% | 4.22 |
| Werder Bremen win | 23.3% | 4.29 |

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
| Over 2.5 | 53.2% |
| Under 2.5 | 46.8% |
| Over 3.5 | 30.1% |
| Under 3.5 | 69.9% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.30% |
| 2 | 2-1 | 10.67% |
| 3 | 1-0 | 10.34% |
| 4 | 2-0 | 9.30% |
| 5 | 0-0 | 6.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.0% | 59.2% | 1.73 | -8.3% |
| Draw | 23.7% | 20.4% | 4.41 | +4.6% |
| Werder Bremen win | 23.3% | 20.4% | 4.72 | +10.0% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6016 |
| Dc lambda away | 1.1476 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.7% |
| P btts no | 45.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.17 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.45 |
| Fair Over 2.5 odds | 1.88 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.32 |
| Fair Under 3.5 odds | 1.43 |
| Fair Over 4.5 odds | 6.67 |
| Fair Under 4.5 odds | 1.18 |
| Unadjusted home-win probability | 46.8% |
| Unadjusted draw probability | 27.0% |
| Unadjusted away-win probability | 26.2% |
| Raw p over 1 5 | 77.1% |
| Raw p under 3 5 | 70.3% |
| Raw p btts yes | 55.6% |
| P home draw | 76.7% |
| P draw away | 47.0% |
| P home away | 76.3% |
| Raw p home draw | 73.8% |
| Raw p draw away | 53.2% |
| Raw p home away | 73.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.85 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -6.2% |
| Draw probability edge | +3.3% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | -0.1242 |
| Raw ev home | -0.1908 |
| Raw edge prob draw | 0.0663 |
| Raw ev draw | 0.1922 |
| Raw edge prob away | 0.0579 |
| Raw ev away | 0.2363 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **63.1%**. Expected goals are 2.46 for RB Leipzig and 1.69 for Elversberg (4.15 combined). The most likely exact score is 2-1 at 9.4%. Goal-market probabilities: at least one goal: 98.1%; Over 2.5 goals: 79.3%; Under 3.5 goals: 39.9%; Double Chance 1X: 80.4%; Double Chance X2: 36.9%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 59.0%; BTTS Yes (both teams score): 74.3%; BTTS No (at least one team does not score): 25.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 63.1% | 1.58 |
| Draw | 17.3% | 5.78 |
| Elversberg win | 19.6% | 5.11 |

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
| 1 | 2-1 | 9.41% |
| 2 | 3-1 | 7.71% |
| 3 | 3-2 | 6.51% |
| 4 | 1-1 | 6.12% |
| 5 | 2-2 | 5.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 63.1% | 72.1% | 1.40 | -11.6% |
| Draw | 17.3% | 14.3% | 6.02 | +4.1% |
| Elversberg win | 19.6% | 13.6% | 7.50 | +46.8% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4575 |
| Dc lambda away | 1.6892 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 74.3% |
| P btts no | 25.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 53.29 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.79 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.84 |
| Fair Over 3.5 odds | 1.66 |
| Fair Under 3.5 odds | 2.51 |
| Fair Over 4.5 odds | 2.44 |
| Fair Under 4.5 odds | 1.70 |
| Unadjusted home-win probability | 54.1% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 25.5% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.5% |
| Raw p btts yes | 75.2% |
| P home draw | 80.4% |
| P draw away | 36.9% |
| P home away | 82.7% |
| Raw p home draw | 74.5% |
| Raw p draw away | 45.9% |
| Raw p home away | 79.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.31 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.20 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -9.0% |
| Draw probability edge | +3.0% |
| Away probability edge | +6.0% |
| Over 2.5 probability edge | +1.6% |
| Under 2.5 probability edge | -1.6% |
| Raw edge prob home | -0.1798 |
| Raw ev home | -0.2419 |
| Raw edge prob draw | 0.0605 |
| Raw ev draw | 0.2232 |
| Raw edge prob away | 0.1193 |
| Raw ev away | 0.9150 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **37.6%**. Expected goals are 1.01 for SC Paderborn and 0.98 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 87.0%; Over 2.5 goals: 33.3%; Under 3.5 goals: 85.8%; Double Chance 1X: 66.5%; Double Chance X2: 62.4%; Double Chance 12 (either team wins): 71.1%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 39.8%; BTTS No (at least one team does not score): 60.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 37.6% | 2.66 |
| Draw | 28.9% | 3.46 |
| Hamburger SV win | 33.5% | 2.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.01 |
| Hamburger SV expected goals | 0.98 |
| Expected total goals | 1.98 |
| Over 0.5 | 87.0% |
| Under 0.5 | 13.0% |
| Over 1.5 | 60.6% |
| Under 1.5 | 39.4% |
| Over 2.5 | 33.3% |
| Under 2.5 | 66.7% |
| Over 3.5 | 14.2% |
| Under 3.5 | 85.8% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.90% |
| 2 | 0-0 | 12.95% |
| 3 | 1-1 | 12.75% |
| 4 | 0-1 | 12.56% |
| 5 | 2-0 | 7.71% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 37.6% | 41.2% | 2.40 | -9.8% |
| Draw | 28.9% | 24.2% | 3.92 | +13.3% |
| Hamburger SV win | 33.5% | 34.6% | 2.91 | -2.5% |
| Over 2.5 | 33.3% | 61.8% | 1.64 | -45.3% |
| Under 2.5 | 66.7% | 38.2% | 2.47 | +64.6% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
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
| Dc lambda home | 1.0066 |
| Dc lambda away | 0.9764 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.72 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.54 |
| Fair Over 2.5 odds | 3.00 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.05 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 18.54 |
| Fair Under 4.5 odds | 1.06 |
| Unadjusted home-win probability | 34.0% |
| Unadjusted draw probability | 33.6% |
| Unadjusted away-win probability | 32.4% |
| Raw p over 1 5 | 60.2% |
| Raw p under 3 5 | 86.0% |
| Raw p btts yes | 40.8% |
| P home draw | 66.5% |
| P draw away | 62.4% |
| P home away | 71.1% |
| Raw p home draw | 67.6% |
| Raw p draw away | 66.0% |
| Raw p home away | 66.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.50 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-18T11:57:07Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:57:07Z |
| Market best over 2 5 last update utc | 2026-10-18T11:56:48Z |
| Market best under 2 5 last update utc | 2026-10-18T11:56:48Z |
| Home probability edge | -3.6% |
| Draw probability edge | +4.7% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -28.4% |
| Under 2.5 probability edge | +28.4% |
| Raw edge prob home | -0.0719 |
| Raw ev home | -0.1839 |
| Raw edge prob draw | 0.0935 |
| Raw ev draw | 0.3161 |
| Raw edge prob away | -0.0217 |
| Raw ev away | -0.0565 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **70.9%**. Expected goals are 1.18 for SC Freiburg and 2.79 for Bayern Munich (3.96 combined). The most likely exact score is 1-2 at 8.7%. Goal-market probabilities: at least one goal: 97.7%; Over 2.5 goals: 76.1%; Under 3.5 goals: 44.0%; Double Chance 1X: 29.1%; Double Chance X2: 86.2%; Double Chance 12 (either team wins): 84.7%; Under 4.5 goals: 63.3%; BTTS Yes (both teams score): 65.2%; BTTS No (at least one team does not score): 34.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 13.8% | 7.27 |
| Draw | 15.3% | 6.53 |
| Bayern Munich win | 70.9% | 1.41 |

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
| Over 2.5 | 76.1% |
| Under 2.5 | 23.9% |
| Over 3.5 | 56.0% |
| Under 3.5 | 44.0% |
| Over 4.5 | 36.7% |
| Under 4.5 | 63.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 8.75% |
| 2 | 1-3 | 8.13% |
| 3 | 0-2 | 7.44% |
| 4 | 0-3 | 6.91% |
| 5 | 1-1 | 6.25% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 13.8% | 14.6% | 6.52 | -10.3% |
| Draw | 15.3% | 13.9% | 5.80 | -11.1% |
| Bayern Munich win | 70.9% | 71.5% | 1.45 | +2.8% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
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
| Dc lambda away | 2.7862 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 65.2% |
| P btts no | 34.8% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 43.78 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.39 |
| Fair Over 2.5 odds | 1.31 |
| Fair Under 2.5 odds | 4.19 |
| Fair Over 3.5 odds | 1.79 |
| Fair Under 3.5 odds | 2.27 |
| Fair Over 4.5 odds | 2.72 |
| Fair Under 4.5 odds | 1.58 |
| Unadjusted home-win probability | 12.9% |
| Unadjusted draw probability | 16.7% |
| Unadjusted away-win probability | 70.4% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 44.1% |
| Raw p btts yes | 65.5% |
| P home draw | 29.1% |
| P draw away | 86.2% |
| P home away | 84.7% |
| Raw p home draw | 29.6% |
| Raw p draw away | 87.1% |
| Raw p home away | 83.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.90 |
| Reference draw odds | 5.10 |
| Reference away odds | 1.32 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.20 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.4% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0170 |
| Raw ev home | -0.1581 |
| Raw edge prob draw | 0.0280 |
| Raw ev draw | -0.0303 |
| Raw edge prob away | -0.0110 |
| Raw ev away | 0.0203 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **50.2%**. Expected goals are 1.40 for TSG Hoffenheim and 2.36 for Bayer Leverkusen (3.76 combined). The most likely exact score is 1-1 at 8.8%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.8%; Under 3.5 goals: 49.0%; Double Chance 1X: 49.8%; Double Chance X2: 71.8%; Double Chance 12 (either team wins): 78.4%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 69.6%; BTTS No (at least one team does not score): 30.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 28.2% | 3.55 |
| Draw | 21.6% | 4.63 |
| Bayer Leverkusen win | 50.2% | 1.99 |

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
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.80% |
| 2 | 1-2 | 7.83% |
| 3 | 2-1 | 7.18% |
| 4 | 2-2 | 6.62% |
| 5 | 1-3 | 6.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 28.2% | 35.3% | 2.76 | -22.3% |
| Draw | 21.6% | 22.5% | 4.25 | -8.1% |
| Bayer Leverkusen win | 50.2% | 42.2% | 2.39 | +20.0% |

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
| Market best home last update utc | 2026-10-18T11:56:48Z |
| Market best draw last update utc | 2026-10-18T11:56:48Z |
| Market best away last update utc | 2026-10-18T11:56:48Z |
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
| Dc lambda away | 2.3622 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-18T11:57:16.468991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 69.6% |
| P btts no | 30.4% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.24 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.34 |
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
| P home draw | 49.8% |
| P draw away | 71.8% |
| P home away | 78.4% |
| Raw p home draw | 41.7% |
| Raw p draw away | 79.0% |
| Raw p home away | 79.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-18T11:57:11Z |
| Market reference home last update utc | 2026-10-18T11:57:11Z |
| Market reference draw last update utc | 2026-10-18T11:57:11Z |
| Market reference away last update utc | 2026-10-18T11:57:11Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-18T11:56:31Z |
| Market reference under 2 5 last update utc | 2026-10-18T11:56:31Z |
| Home probability edge | -7.1% |
| Draw probability edge | -0.9% |
| Away probability edge | +8.0% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.1423 |
| Raw ev home | -0.4193 |
| Raw edge prob draw | -0.0184 |
| Raw ev draw | -0.1204 |
| Raw edge prob away | 0.1607 |
| Raw ev away | 0.3925 |

</details>


---
