# UEFA Champions League — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | UEFA Champions League |
| Training matches | 557 |
| Training data through | 2026-10-21 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 4 |
| Training seasons loaded | ['2023', '2024', '2025', '2026'] |
| Training sha256 | 2258b17aabe5286e4528376b610054a501a38c0c7c8395d5ded6eafb5e1cccd3 |
| Training as of utc | 2026-10-22T10:57:57.424777+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 45, 'bbs_added_results': 0, 'bbs_result_conflicts': 9, 'bbs_rows_with_statistics': 34, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 139, 'added_results': 0, 'conflicts': 1, 'unmapped': 78, 'ambiguous': 0, 'excluded_phase': 460, 'statistics_observations': 4, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:57:57.424777+00:00', 'observations': 130, 'observations_sha256': 'c90a4f949241897f87170f11e1812ed3007aee986089a9986e619c46115e4c7a', 'eligible_training_matches': 0, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 38, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 0, 'retrospective_eligible_training_matches': 0, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.957146+00:00', 'retrospective_inputs_sha256': '625afa63f72cc4b92ac2f52b597e7dba5814aec27f873d04c607e49f0dfa4b28', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 493.181 |
| Base scoring parameter | 0.212 |
| Home-advantage parameter | 0.314 |
| Dixon-Coles low-score adjustment | 0.050 |
| Xi per day | 0.0029 |
| Training data health | {'completed_matches': 54, 'latest_completed_utc': '2026-10-21T19:00:00+00:00', 'latest_completed_date': '2026-10-21', 'next_fixture_utc': '2026-11-03T17:45:00+00:00', 'overdue_unfinished_match_ids': [], 'source_schedule_matches': 144, 'provider': 'football-data.org', 'season_start': 2026, 'checked_at_utc': '2026-10-22T10:57:47.604309+00:00', 'download_status': 'VERIFIED_LIVE', 'added_matches': 0, 'corrected_scores': 0, 'sha256': 'f06b49a6ae473f3aeb59e8f44956d9bac8f40f44017b95dba0ffc21209fe9571', 'coverage_status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'note': 'Provider schedule comparison is not independent proof of complete coverage.', 'status': 'CURRENT_WITHIN_PROVIDER_SCHEDULE', 'download_age_hours': 0.002727907777777778, 'training_end': '2026-10-21', 'cache_hash_verified': True, 'last_refresh_error': None, 'last_refresh_error_reason': None} |
| Training source | football-data.org |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 5.00 |
| Bbs statistics model artifact | bbs/feature_models/UCL/20261022T105757424777Z_b34d85617fdfed8c2e09846d750dcef254ebc954eca1f959943e861b815f20d3.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'UNRELIABLE_AUDIT', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'UNRELIABLE_AUDIT', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Aston Villa vs Viking FK

The model's most likely 1X2 outcome is **Aston Villa win** at **77.6%**. Expected goals are 3.41 for Aston Villa and 1.20 for Viking FK (4.61 combined). The most likely exact score is 3-1 at 7.7%. Goal-market probabilities: at least one goal: 99.1%; Over 2.5 goals: 83.4%; Under 3.5 goals: 32.6%; Double Chance 1X: 90.4%; Double Chance X2: 22.4%; Double Chance 12 (either team wins): 87.2%; Under 4.5 goals: 51.7%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 77.6% | 1.29 |
| Draw | 12.8% | 7.82 |
| Viking FK win | 9.6% | 10.37 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 3.41 |
| Viking FK expected goals | 1.20 |
| Expected total goals | 4.61 |
| Over 0.5 | 99.1% |
| Under 0.5 | 0.9% |
| Over 1.5 | 94.2% |
| Under 1.5 | 5.8% |
| Over 2.5 | 83.4% |
| Under 2.5 | 16.6% |
| Over 3.5 | 67.4% |
| Under 3.5 | 32.6% |
| Over 4.5 | 48.3% |
| Under 4.5 | 51.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.72% |
| 2 | 2-1 | 6.79% |
| 3 | 4-1 | 6.59% |
| 4 | 3-0 | 6.45% |
| 5 | 2-0 | 5.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 77.6% | 75.9% | 1.27 | -1.5% |
| Draw | 12.8% | 14.3% | 6.60 | -15.6% |
| Viking FK win | 9.6% | 9.8% | 9.62 | -7.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d3b3e714b6af9e5430e3030ed639e6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa FC |
| Matched away-team name | Viking FK |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.4129 |
| Dc lambda away | 1.1972 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 111.20 |
| Fair Over 1.5 odds | 1.06 |
| Fair Under 1.5 odds | 17.12 |
| Fair Over 2.5 odds | 1.20 |
| Fair Under 2.5 odds | 6.02 |
| Fair Over 3.5 odds | 1.48 |
| Fair Under 3.5 odds | 3.06 |
| Fair Over 4.5 odds | 2.07 |
| Fair Under 4.5 odds | 1.94 |
| Goal margin distribution | {"-1": 0.06291452555861066, "-10": 2.433390882839066e-08, "-11": 2.5708050126843165e-09, "-12": 2.5007000574193517e-10, "-13": 2.2532972162591638e-11, "-14": 1.8906958822132953e-12, "-15": 1.4841179607866713e-13, "-16": 1.094258757236369e-14, "-17": 7.605706933405915e-16, "-18": 4.9992353417094795e-17, "-19": 3.1137253489391538e-18, "-2": 0.023826257085533004, "-20": 1.8187890840790735e-19, "-21": 8.679917910303581e-21, "-3": 0.007381233406544129, "-4": 0.0018696206594016654, "-5": 0.000397975721640658, "-6": 7.278617057442164e-05, "-7": 1.1642731861423132e-05, "-8": 1.6524812809160864e-06, "-9": 2.1058724094079976e-07, "0": 0.12791414232001236, "1": 0.16880061296707327, "10": 0.0008296087476137321, "11": 0.0002498582013082093, "12": 6.928657605560702e-05, "13": 1.77979097978287e-05, "14": 4.257309506714026e-06, "15": 9.526754903275396e-07, "16": 2.0024405310163557e-07, "17": 3.967730886537092e-08, "18": 7.4347989367416204e-09, "19": 1.3201065125237457e-09, "2": 0.18621431747930697, "20": 2.198234579645799e-10, "21": 2.9906827049096815e-11, "3": 0.16445580567877385, "4": 0.11875086847121276, "5": 0.07206143396898639, "6": 0.03757147256426036, "7": 0.017132757453049645, "8": 0.00693221373850503, "9": 0.0025184334309937837} |
| Raw goal margin distribution | {"-1": 0.061826366068103336, "-10": 2.391303346459115e-08, "-11": 2.5263407836695055e-09, "-12": 2.4574483524079533e-10, "-13": 2.21432455090032e-11, "-14": 1.8579947110667865e-12, "-15": 1.458448895817598e-13, "-16": 1.07533263419586e-14, "-17": 7.474159852535171e-16, "-18": 4.912769373253705e-17, "-19": 3.059870857322191e-18, "-2": 0.023414161984430523, "-20": 1.787331601319738e-19, "-21": 8.529791449568812e-21, "-3": 0.00725356878360267, "-4": 0.0018372840019110002, "-5": 0.0003910923977238091, "-6": 7.152727270330191e-05, "-7": 1.1441361048277016e-05, "-8": 1.6239002311068593e-06, "-9": 2.069449579739513e-07, "0": 0.11262757705050142, "1": 0.1724906736824532, "10": 0.0008477443846525745, "11": 0.00025532021899201204, "12": 7.080121316451283e-05, "13": 1.8186980468879248e-05, "14": 4.350376292952553e-06, "15": 9.735014241886249e-07, "16": 2.0462148219297975e-07, "17": 4.0544673480715406e-08, "18": 7.597327134957169e-09, "19": 1.3489646611782844e-09, "2": 0.1902850499576642, "20": 2.2462890204618576e-10, "21": 3.056060434099006e-11, "3": 0.16805088686529637, "4": 0.12134681825457254, "5": 0.07363673077572708, "6": 0.03839280260857362, "7": 0.017507287581301982, "8": 0.007083755188132726, "9": 0.0025734875691551333} |
| Unadjusted home-win probability | 79.3% |
| Unadjusted draw probability | 11.3% |
| Unadjusted away-win probability | 9.5% |
| Raw p over 1 5 | 94.2% |
| Raw p under 3 5 | 32.4% |
| Raw p btts yes | 67.3% |
| P home draw | 90.4% |
| P draw away | 22.4% |
| P home away | 87.2% |
| Raw p home draw | 90.5% |
| Raw p draw away | 20.7% |
| Raw p home away | 88.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.29 |
| Reference draw odds | 6.00 |
| Reference away odds | 8.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +1.7% |
| Draw probability edge | -1.5% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +5.6% |
| Under 2.5 probability edge | -5.6% |
| Raw edge prob home | 0.0339 |
| Raw ev home | 0.0066 |
| Raw edge prob draw | -0.0306 |
| Raw ev draw | -0.2567 |
| Raw edge prob away | -0.0033 |
| Raw ev away | -0.0880 |

</details>


---

## 2026-10-21 — Bayern Munich vs Arsenal

The model's most likely 1X2 outcome is **Bayern Munich win** at **39.1%**. Expected goals are 1.19 for Bayern Munich and 1.26 for Arsenal (2.44 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 44.2%; Under 3.5 goals: 77.0%; Double Chance 1X: 64.7%; Double Chance X2: 60.9%; Double Chance 12 (either team wins): 74.3%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 48.9%; BTTS No (at least one team does not score): 51.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayern Munich win | 39.1% | 2.56 |
| Draw | 25.7% | 3.90 |
| Arsenal win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayern Munich expected goals | 1.19 |
| Arsenal expected goals | 1.26 |
| Expected total goals | 2.44 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 69.4% |
| Under 1.5 | 30.6% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 23.0% |
| Under 3.5 | 77.0% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.14% |
| 2 | 1-1 | 12.12% |
| 3 | 0-1 | 10.55% |
| 4 | 2-1 | 8.51% |
| 5 | 0-0 | 7.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayern Munich win | 39.1% | 42.9% | 2.29 | -10.6% |
| Draw | 25.7% | 25.3% | 3.78 | -3.0% |
| Arsenal win | 35.3% | 31.9% | 3.06 | +8.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 2ebbccdeea2dab59717d5c3d802c3fed |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Bayern München |
| Matched away-team name | Arsenal FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1855 |
| Dc lambda away | 1.2572 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 48.9% |
| P btts no | 51.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.62 |
| Fair Over 1.5 odds | 1.44 |
| Fair Under 1.5 odds | 3.27 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.35 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.85 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.20070918139145336, "-10": 2.4654040973539087e-07, "-11": 2.7865985593159602e-08, "-12": 2.891552344008176e-09, "-13": 2.760743520102142e-10, "-14": 2.2406581718475035e-11, "-2": 0.10016082441870747, "-3": 0.03761336173381461, "-4": 0.011037277857690701, "-5": 0.002648102084039772, "-6": 0.0005363272485245221, "-7": 9.387745262259448e-05, "-8": 1.4458618585663567e-05, "-9": 1.987269599022446e-06, "0": 0.25659726783711945, "1": 0.2304564265995928, "10": 1.6650363834514587e-07, "11": 1.7745422502576487e-08, "12": 1.7362782119266687e-09, "13": 1.5631139525795367e-10, "14": 1.1962350035569024e-11, "2": 0.1082487612410743, "3": 0.03833041457475858, "4": 0.010605707929258437, "5": 0.002399323078534231, "6": 0.0004582053880289596, "7": 7.5625445707247e-05, "8": 1.098271650377405e-05, "9": 1.4233643431460676e-06} |
| Raw goal margin distribution | {"-1": 0.22014322648935278, "-10": 2.704121499718652e-07, "-11": 3.056416221348405e-08, "-12": 3.1715323542240135e-09, "-13": 3.0280577191908103e-10, "-14": 2.4576141260234762e-11, "-2": 0.10985908518237188, "-3": 0.0412553464360136, "-4": 0.012105983106535587, "-5": 0.002904509563599457, "-6": 0.0005882581460689117, "-7": 0.00010296731405940217, "-8": 1.5858601604373028e-05, "-9": 2.1796907266526907e-06, "0": 0.2605836278949279, "1": 0.20794788572486322, "10": 1.5024132791717738e-07, "11": 1.6012237736882934e-08, "12": 1.5666969610164677e-09, "13": 1.410445550953115e-10, "14": 1.0793994486946177e-11, "2": 0.09767616969748108, "3": 0.03458670598771062, "4": 0.009569854800953535, "5": 0.0021649826334369836, "6": 0.000413452742777758, "7": 6.823915381255951e-05, "8": 9.91004117426253e-06, "9": 1.2843452020005696e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 26.1% |
| Unadjusted away-win probability | 38.7% |
| Raw p over 1 5 | 69.4% |
| Raw p under 3 5 | 77.0% |
| Raw p btts yes | 49.0% |
| P home draw | 64.7% |
| P draw away | 60.9% |
| P home away | 74.3% |
| Raw p home draw | 61.3% |
| Raw p draw away | 64.8% |
| Raw p home away | 73.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 2.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | -3.8% |
| Draw probability edge | +0.4% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | -19.6% |
| Under 2.5 probability edge | +19.6% |
| Raw edge prob home | -0.0763 |
| Raw ev home | -0.1929 |
| Raw edge prob draw | 0.0080 |
| Raw ev draw | -0.0150 |
| Raw edge prob away | 0.0683 |
| Raw ev away | 0.1842 |

</details>


---

## 2026-10-21 — Club Brugge vs RC Lens

The model's most likely 1X2 outcome is **Club Brugge win** at **69.4%**. Expected goals are 3.70 for Club Brugge and 0.87 for RC Lens (4.57 combined). The most likely exact score is 3-0 at 7.0%. Goal-market probabilities: at least one goal: 98.3%; Over 2.5 goals: 78.7%; Under 3.5 goals: 38.0%; Double Chance 1X: 85.0%; Double Chance X2: 30.6%; Double Chance 12 (either team wins): 84.5%; Under 4.5 goals: 57.1%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Club Brugge win | 69.4% | 1.44 |
| Draw | 15.5% | 6.44 |
| RC Lens win | 15.0% | 6.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Club Brugge expected goals | 3.70 |
| RC Lens expected goals | 0.87 |
| Expected total goals | 4.57 |
| Over 0.5 | 98.3% |
| Under 0.5 | 1.7% |
| Over 1.5 | 91.8% |
| Under 1.5 | 8.2% |
| Over 2.5 | 78.7% |
| Under 2.5 | 21.3% |
| Over 3.5 | 62.0% |
| Under 3.5 | 38.0% |
| Over 4.5 | 42.9% |
| Under 4.5 | 57.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 6.96% |
| 2 | 4-0 | 6.44% |
| 3 | 1-1 | 6.23% |
| 4 | 3-1 | 6.06% |
| 5 | 2-0 | 5.64% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Club Brugge win | 69.4% | 51.6% | 1.86 | +29.1% |
| Draw | 15.5% | 23.2% | 4.17 | -35.2% |
| RC Lens win | 15.0% | 25.2% | 3.96 | -40.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | d306a78e402e5f505e8644fdf3f75dcd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Club Brugge KV |
| Matched away-team name | Racing Club de Lens |
| Home-name matching confidence | 90/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.6996 |
| Dc lambda away | 0.8703 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 22 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 58.56 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.20 |
| Fair Over 2.5 odds | 1.27 |
| Fair Under 2.5 odds | 4.70 |
| Fair Over 3.5 odds | 1.61 |
| Fair Under 3.5 odds | 2.63 |
| Fair Over 4.5 odds | 2.33 |
| Fair Under 4.5 odds | 1.75 |
| Goal margin distribution | {"-1": 0.10966737808208778, "-10": 2.9387839545681972e-09, "-11": 2.2707320856817213e-10, "-12": 1.614039536036512e-11, "-13": 1.0619860441516103e-12, "-14": 6.503090282131818e-14, "-15": 3.723563676962864e-15, "-16": 2.0018511585854175e-16, "-17": 1.0142151987049206e-17, "-18": 4.858171129336294e-19, "-19": 2.2066118452736727e-20, "-2": 0.0316935398668745, "-20": 9.524876035819065e-22, "-21": 3.8855710822251945e-23, "-22": 1.3408107588299396e-24, "-3": 0.0074501954345586475, "-4": 0.001413987501680408, "-5": 0.00022372455216279128, "-6": 3.0251995027435523e-05, "-7": 3.564582435848796e-06, "-8": 3.7170324485356277e-07, "-9": 3.4734188624220896e-08, "0": 0.15527649678234695, "1": 0.11561878870746045, "10": 0.001457288431619493, "11": 0.00047868001390459687, "12": 0.0001446422296855845, "13": 4.045770933127019e-05, "14": 1.0531829133774797e-05, "15": 2.5635650812789718e-06, "16": 5.85893779267456e-07, "17": 1.2618820382372494e-07, "18": 2.5695850324896844e-08, "19": 4.96155341520378e-09, "2": 0.1473452968680765, "20": 9.104426604341729e-10, "21": 1.578881973505331e-10, "22": 2.3161348170614587e-11, "3": 0.1472430266471263, "4": 0.11879938223915926, "5": 0.07990681122107111, "6": 0.045933095467649294, "7": 0.023008160449232984, "8": 0.010199317885983803, "9": 0.004051664486868994} |
| Raw goal margin distribution | {"-1": 0.03544929547032992, "-10": 9.4994357073964e-10, "-11": 7.339999738029425e-11, "-12": 5.2172820591119645e-12, "-13": 3.4328036033029014e-13, "-14": 2.102083344319279e-14, "-15": 1.2036187177598268e-15, "-16": 6.470858923535025e-17, "-17": 3.278387327038906e-18, "-18": 1.5703734950274837e-19, "-19": 7.132735063008918e-21, "-2": 0.010244738945072133, "-20": 3.07885672856406e-22, "-21": 1.2559866003331394e-23, "-22": 4.33408709050947e-25, "-3": 0.0024082291734346586, "-4": 0.0004570626344408739, "-5": 7.231756509806988e-05, "-6": 9.778768573201372e-06, "-7": 1.1522290238594777e-06, "-8": 1.201507538935728e-07, "-9": 1.12276096775153e-08, "0": 0.0790337063907256, "1": 0.14527674985302402, "10": 0.001831104868947913, "11": 0.0006014686489720419, "12": 0.00018174514069148356, "13": 5.0835721285895455e-05, "14": 1.3233401972697412e-05, "15": 3.2211581457338103e-06, "16": 7.361843603676228e-07, "17": 1.585573791789672e-07, "18": 3.228722305122981e-08, "19": 6.234266613938902e-09, "2": 0.185141585329045, "20": 1.1439849190089504e-09, "21": 1.9838889861815538e-10, "22": 2.910258291111169e-11, "3": 0.18501308125568042, "4": 0.1492732135424844, "5": 0.10040411212652069, "6": 0.05771562645508131, "7": 0.028910100231362992, "8": 0.012815596580436526, "9": 0.005090977467655019} |
| Unadjusted home-win probability | 87.2% |
| Unadjusted draw probability | 7.9% |
| Unadjusted away-win probability | 4.9% |
| Raw p over 1 5 | 94.1% |
| Raw p under 3 5 | 33.1% |
| Raw p btts yes | 56.5% |
| P home draw | 85.0% |
| P draw away | 30.6% |
| P home away | 84.5% |
| Raw p home draw | 95.1% |
| Raw p draw away | 12.8% |
| Raw p home away | 92.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.85 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +17.8% |
| Draw probability edge | -7.6% |
| Away probability edge | -10.2% |
| Over 2.5 probability edge | +9.7% |
| Under 2.5 probability edge | -9.7% |
| Raw edge prob home | 0.3562 |
| Raw ev home | 0.6225 |
| Raw edge prob draw | -0.1525 |
| Raw ev draw | -0.6704 |
| Raw edge prob away | -0.2037 |
| Raw ev away | -0.8074 |

</details>


---

## 2026-10-21 — Inter Milan vs Shakhtar Donetsk

The model's most likely 1X2 outcome is **Inter Milan win** at **68.1%**. Expected goals are 1.62 for Inter Milan and 0.85 for Shakhtar Donetsk (2.47 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 47.3%; Under 3.5 goals: 75.4%; Double Chance 1X: 86.3%; Double Chance X2: 31.9%; Double Chance 12 (either team wins): 81.7%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 43.5%; BTTS No (at least one team does not score): 56.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 68.1% | 1.47 |
| Draw | 18.3% | 5.47 |
| Shakhtar Donetsk win | 13.7% | 7.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 1.62 |
| Shakhtar Donetsk expected goals | 0.85 |
| Expected total goals | 2.47 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 71.3% |
| Under 1.5 | 28.7% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.28% |
| 2 | 2-0 | 13.47% |
| 3 | 2-1 | 11.39% |
| 4 | 1-1 | 8.56% |
| 5 | 3-0 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 68.1% | 79.7% | 1.25 | -14.9% |
| Draw | 18.3% | 13.0% | 6.82 | +24.7% |
| Shakhtar Donetsk win | 13.7% | 7.3% | 10.34 | +41.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | a889456204e8ef1b64294efbee8dc3e5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | FC Internazionale Milano |
| Matched away-team name | FK Shakhtar Donetsk |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6247 |
| Dc lambda away | 0.8461 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 43.5% |
| P btts no | 56.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.38 |
| Fair Over 1.5 odds | 1.40 |
| Fair Under 1.5 odds | 3.49 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 4.06 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.81 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.09475586704072822, "-10": 3.37746992364708e-09, "-11": 2.5713157594895954e-10, "-12": 1.7972483709903765e-11, "-13": 1.160872787729637e-12, "-14": 6.9454713897486e-14, "-15": 3.588783646436936e-15, "-2": 0.03182786532714022, "-3": 0.008105273241982196, "-4": 0.0016085893195796769, "-5": 0.0002606301141332928, "-6": 3.561458521248445e-05, "-7": 4.203462938544165e-06, "-8": 4.363569186657017e-07, "-9": 4.041226431899529e-08, "0": 0.18282209652570053, "1": 0.3160121750879383, "10": 4.0798253024189365e-06, "11": 5.964280706080799e-07, "12": 8.005037098628353e-08, "13": 9.928701818264686e-09, "14": 1.1406755969764932e-09, "15": 1.1317754988556385e-10, "2": 0.20798733689670515, "3": 0.10170671547731074, "4": 0.03875964019205773, "5": 0.012059012268279457, "6": 0.00316422691432106, "7": 0.000717132721439432, "8": 0.0001429508590239565, "9": 2.5422056219311702e-05} |
| Raw goal margin distribution | {"-1": 0.13911401722676595, "-10": 4.95856798966517e-09, "-11": 3.7750281437173727e-10, "-12": 2.6385958848887636e-11, "-13": 1.7043132212688309e-12, "-14": 1.0196861225977668e-13, "-15": 5.268804197622664e-15, "-2": 0.04672747285936233, "-3": 0.011899602173743043, "-4": 0.0023616197002198757, "-5": 0.0003826391264170341, "-6": 5.22868733673677e-05, "-7": 6.171233865585989e-06, "-8": 6.406290797190137e-07, "-9": 5.933049435586828e-08, "0": 0.2356628999851891, "1": 0.26178477704101005, "10": 3.3797310399917516e-06, "11": 4.940815632868807e-07, "12": 6.63138010896664e-08, "13": 8.224945735327458e-09, "14": 9.449367156424155e-10, "15": 9.37563866157858e-11, "2": 0.17229690154091667, "3": 0.08425393682187116, "4": 0.03210852165124346, "5": 0.009989696875153203, "6": 0.002621248491588002, "7": 0.000594073407262213, "8": 0.00011842062334146969, "9": 2.105965479793488e-05} |
| Unadjusted home-win probability | 56.4% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 20.1% |
| Raw p over 1 5 | 70.1% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 45.3% |
| P home draw | 86.3% |
| P draw away | 31.9% |
| P home away | 81.7% |
| Raw p home draw | 79.9% |
| Raw p draw away | 43.6% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.00 |
| Reference away odds | 10.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | -11.7% |
| Draw probability edge | +5.3% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -24.7% |
| Under 2.5 probability edge | +24.7% |
| Raw edge prob home | -0.2336 |
| Raw ev home | -0.2953 |
| Raw edge prob draw | 0.1057 |
| Raw ev draw | 0.6072 |
| Raw edge prob away | 0.1279 |
| Raw ev away | 1.0736 |

</details>


---

## 2026-10-21 — Real Betis vs Feyenoord

The model's most likely 1X2 outcome is **Real Betis win** at **58.9%**. Expected goals are 2.22 for Real Betis and 1.26 for Feyenoord (3.49 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 97.2%; Over 2.5 goals: 67.4%; Under 3.5 goals: 54.0%; Double Chance 1X: 79.0%; Double Chance X2: 41.1%; Double Chance 12 (either team wins): 79.8%; Under 4.5 goals: 73.0%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Betis win | 58.9% | 1.70 |
| Draw | 20.2% | 4.96 |
| Feyenoord win | 21.0% | 4.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Betis expected goals | 2.22 |
| Feyenoord expected goals | 1.26 |
| Expected total goals | 3.49 |
| Over 0.5 | 97.2% |
| Under 0.5 | 2.8% |
| Over 1.5 | 85.9% |
| Under 1.5 | 14.1% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 46.0% |
| Under 3.5 | 54.0% |
| Over 4.5 | 27.0% |
| Under 4.5 | 73.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.45% |
| 2 | 1-1 | 8.62% |
| 3 | 2-0 | 7.47% |
| 4 | 1-0 | 7.15% |
| 5 | 3-1 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Betis win | 58.9% | 58.2% | 1.68 | -1.1% |
| Draw | 20.2% | 21.2% | 4.48 | -9.7% |
| Feyenoord win | 21.0% | 20.5% | 4.57 | -4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | f5905225efa837b0dc89b7dcdbb6c625 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Real Betis Balompié |
| Matched away-team name | Feyenoord Rotterdam |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2229 |
| Dc lambda away | 1.2646 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 36.04 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.07 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.17 |
| Fair Under 3.5 odds | 1.85 |
| Fair Over 4.5 odds | 3.70 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.12709552074607194, "-10": 1.112843285827853e-07, "-11": 1.2531878002153707e-08, "-12": 1.2976653577648297e-09, "-13": 1.24341795832657e-10, "-14": 1.1085005606682915e-11, "-15": 9.232808906586653e-13, "-16": 7.14520599043408e-14, "-17": 4.5611380421627254e-15, "-2": 0.05597998620906568, "-3": 0.01954366099055863, "-4": 0.005472066749112601, "-5": 0.0012720038489714715, "-6": 0.0002520157610149842, "-7": 4.3429531051595196e-05, "-8": 6.614740942925621e-06, "-9": 9.019921326103558e-07, "0": 0.20161285671505078, "1": 0.22223653839324725, "10": 3.161769957391962e-05, "11": 6.258405013153627e-06, "12": 1.1390989873749322e-06, "13": 1.9185235669757193e-07, "14": 3.0063335820920947e-08, "15": 4.401354465254453e-09, "16": 5.987127417773205e-10, "17": 6.717817658262697e-11, "2": 0.17454968163782952, "3": 0.10711331064504968, "4": 0.05271572168267397, "5": 0.02153914419265983, "6": 0.007500996599786961, "7": 0.0022721011122089946, "8": 0.0006082842936245966, "9": 0.00014579672213569628} |
| Raw goal margin distribution | {"-1": 0.12966916712167695, "-10": 1.135378030344219e-07, "-11": 1.2785644792756861e-08, "-12": 1.323942694095448e-09, "-13": 1.268596801003512e-10, "-14": 1.1309473662958473e-11, "-15": 9.419770532296228e-13, "-16": 7.289894279936998e-14, "-17": 4.653499726681093e-15, "-2": 0.05711356422792621, "-3": 0.019939414294680952, "-4": 0.005582874468167152, "-5": 0.0012977615474052474, "-6": 0.00025711900498553617, "-7": 4.430896609799999e-05, "-8": 6.748687473483053e-06, "-9": 9.202572041824286e-07, "0": 0.19093024577477433, "1": 0.22466641871501367, "10": 3.1963399820016164e-05, "11": 6.3268328931820536e-06, "12": 1.1515536189759185e-06, "13": 1.9395002375805787e-07, "14": 3.03920410313515e-08, "15": 4.449477805734659e-09, "16": 6.052589214476556e-10, "17": 6.791268644545352e-11, "2": 0.176458165452637, "3": 0.10828446156207443, "4": 0.05329210257706039, "5": 0.021774647962651165, "6": 0.007583010674354696, "7": 0.002296943713797087, "8": 0.0006149351263175652, "9": 0.00014739082807640658} |
| Unadjusted home-win probability | 59.5% |
| Unadjusted draw probability | 19.1% |
| Unadjusted away-win probability | 21.4% |
| Raw p over 1 5 | 85.8% |
| Raw p under 3 5 | 53.9% |
| Raw p btts yes | 63.6% |
| P home draw | 79.0% |
| P draw away | 41.1% |
| P home away | 79.8% |
| Raw p home draw | 78.6% |
| Raw p draw away | 40.5% |
| Raw p home away | 80.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.65 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.33 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.35 |
| Reference Under 2.5 odds | 3.20 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +0.6% |
| Draw probability edge | -1.1% |
| Away probability edge | +0.4% |
| Over 2.5 probability edge | -4.6% |
| Under 2.5 probability edge | +4.6% |
| Raw edge prob home | 0.0129 |
| Raw ev home | -0.0001 |
| Raw edge prob draw | -0.0214 |
| Raw ev draw | -0.1446 |
| Raw edge prob away | 0.0085 |
| Raw ev away | -0.0224 |

</details>


---

## 2026-10-21 — Real Madrid vs RB Leipzig

The model's most likely 1X2 outcome is **Real Madrid win** at **81.1%**. Expected goals are 3.10 for Real Madrid and 0.82 for RB Leipzig (3.93 combined). The most likely exact score is 3-0 at 9.7%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 74.7%; Under 3.5 goals: 45.1%; Double Chance 1X: 92.6%; Double Chance X2: 18.9%; Double Chance 12 (either team wins): 88.5%; Under 4.5 goals: 64.6%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Madrid win | 81.1% | 1.23 |
| Draw | 11.5% | 8.72 |
| RB Leipzig win | 7.4% | 13.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Madrid expected goals | 3.10 |
| RB Leipzig expected goals | 0.82 |
| Expected total goals | 3.93 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 74.7% |
| Under 2.5 | 25.3% |
| Over 3.5 | 54.9% |
| Under 3.5 | 45.1% |
| Over 4.5 | 35.4% |
| Under 4.5 | 64.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-0 | 9.68% |
| 2 | 2-0 | 9.36% |
| 3 | 3-1 | 7.96% |
| 4 | 2-1 | 7.70% |
| 5 | 4-0 | 7.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Madrid win | 81.1% | 79.9% | 1.22 | -1.0% |
| Draw | 11.5% | 12.1% | 7.28 | -16.5% |
| RB Leipzig win | 7.4% | 7.9% | 11.27 | -16.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 30f27b8e9719e9ae71c25b4c8aa265f7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Real Madrid CF |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.1044 |
| Dc lambda away | 0.8223 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 20 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 54.70 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.88 |
| Fair Over 2.5 odds | 1.34 |
| Fair Under 2.5 odds | 3.96 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.22 |
| Fair Over 4.5 odds | 2.83 |
| Fair Under 4.5 odds | 1.55 |
| Goal margin distribution | {"-1": 0.05411518691665277, "-10": 1.0387317195836953e-09, "-11": 7.62012063724937e-11, "-12": 5.1388497102573864e-12, "-13": 3.2061493565324275e-13, "-14": 1.8608081250024362e-14, "-15": 1.0094770400441911e-15, "-16": 5.1403361743331885e-17, "-17": 2.466013035370246e-18, "-18": 1.1179499536418714e-19, "-19": 4.773727902672782e-21, "-2": 0.015571855668535856, "-20": 1.7405908605347688e-22, "-3": 0.0035860656699715763, "-4": 0.0006593279025350678, "-5": 0.00010036477497882623, "-6": 1.2998555688407473e-05, "-7": 1.4625424080171067e-06, "-8": 1.453207410433299e-07, "-9": 1.291944741165495e-08, "0": 0.11463521156126515, "1": 0.18040822980737156, "10": 0.0005598868844632175, "11": 0.00015505750396621867, "12": 3.947579634461355e-05, "13": 9.297855115575353e-06, "14": 2.0372046545482966e-06, "15": 4.1721849596103767e-07, "16": 8.020338006649854e-08, "17": 1.4525482195240617e-08, "18": 2.4859454477056838e-09, "19": 4.0073837645082134e-10, "2": 0.20345339369797558, "20": 5.5161239134022715e-11, "3": 0.1768792339006972, "4": 0.12277052330041006, "5": 0.07055178536007821, "6": 0.03449497493178719, "7": 0.014652213687298585, "8": 0.005496122719559229, "9": 0.0018446195084387887} |
| Raw goal margin distribution | {"-1": 0.0503431372253602, "-10": 9.663278735390326e-10, "-11": 7.088967086183959e-11, "-12": 4.780650883502336e-12, "-13": 2.982667643179528e-13, "-14": 1.7311021937583892e-14, "-15": 9.391123647242976e-16, "-16": 4.782033734957029e-17, "-17": 2.294121848463354e-18, "-18": 1.0400242729265807e-19, "-19": 4.4409795581216454e-21, "-2": 0.014486433687866732, "-20": 1.6192645639397105e-22, "-3": 0.0033361022368930777, "-4": 0.0006133700531230639, "-5": 9.336893998229165e-05, "-6": 1.2092503233165593e-05, "-7": 1.3605972249179508e-06, "-8": 1.35191291481691e-07, "-9": 1.2018909126610108e-08, "0": 0.10781913464545752, "1": 0.18307159795411482, "10": 0.0005681524990388432, "11": 0.00015734661914360322, "12": 4.0058577843350204e-05, "13": 9.435119425381497e-06, "14": 2.067279923238169e-06, "15": 4.233778959704565e-07, "16": 8.13874232110842e-08, "17": 1.4739922005642823e-08, "18": 2.522645480331857e-09, "19": 4.0665448032344586e-10, "2": 0.2064569777844697, "20": 5.597558495073689e-11, "3": 0.1794905034525046, "4": 0.12458298552270694, "5": 0.07159334193443477, "6": 0.035004224523971124, "7": 0.01486852443573669, "8": 0.005577262023445174, "9": 0.0018718516410686737} |
| Unadjusted home-win probability | 82.3% |
| Unadjusted draw probability | 10.8% |
| Unadjusted away-win probability | 6.9% |
| Raw p over 1 5 | 90.0% |
| Raw p under 3 5 | 44.8% |
| Raw p btts yes | 53.3% |
| P home draw | 92.6% |
| P draw away | 18.9% |
| P home away | 88.5% |
| Raw p home draw | 93.1% |
| Raw p draw away | 17.7% |
| Raw p home away | 89.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.22 |
| Reference draw odds | 6.50 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.17 |
| Reference Under 2.5 odds | 5.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.7% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | 0.0240 |
| Raw ev home | 0.0044 |
| Raw edge prob draw | -0.0136 |
| Raw ev draw | -0.2151 |
| Raw edge prob away | -0.0103 |
| Raw ev away | -0.2237 |

</details>


---

## 2026-10-21 — Sporting Lisbon vs LASK

The model's most likely 1X2 outcome is **Sporting Lisbon win** at **73.9%**. Expected goals are 3.46 for Sporting Lisbon and 1.48 for LASK (4.95 combined). The most likely exact score is 3-1 at 7.2%. Goal-market probabilities: at least one goal: 99.4%; Over 2.5 goals: 86.7%; Under 3.5 goals: 27.3%; Double Chance 1X: 88.4%; Double Chance X2: 26.1%; Double Chance 12 (either team wins): 85.5%; Under 4.5 goals: 45.5%; BTTS Yes (both teams score): 75.1%; BTTS No (at least one team does not score): 24.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sporting Lisbon win | 73.9% | 1.35 |
| Draw | 14.5% | 6.88 |
| LASK win | 11.6% | 8.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sporting Lisbon expected goals | 3.46 |
| LASK expected goals | 1.48 |
| Expected total goals | 4.95 |
| Over 0.5 | 99.4% |
| Under 0.5 | 0.6% |
| Over 1.5 | 95.6% |
| Under 1.5 | 4.4% |
| Over 2.5 | 86.7% |
| Under 2.5 | 13.3% |
| Over 3.5 | 72.7% |
| Under 3.5 | 27.3% |
| Over 4.5 | 54.5% |
| Under 4.5 | 45.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 3-1 | 7.20% |
| 2 | 2-1 | 6.24% |
| 3 | 4-1 | 6.23% |
| 4 | 2-2 | 5.48% |
| 5 | 3-2 | 5.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sporting Lisbon win | 73.9% | 72.8% | 1.34 | -1.0% |
| Draw | 14.5% | 16.6% | 5.89 | -14.4% |
| LASK win | 11.6% | 10.6% | 8.45 | -1.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T19:00:00+00:00 |
| Fixture id | 8fdcaee14b3e8966e09d468a0b17ce18 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:28:54Z |
| Market best draw last update utc | 2026-10-21T17:28:54Z |
| Market best away last update utc | 2026-10-21T17:28:54Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sporting Clube de Portugal |
| Matched away-team name | LASK Linz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 3.4623 |
| Dc lambda away | 1.4828 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:57:57.424777+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 21 |
| Score grid omitted mass | 0 |
| P btts yes | 75.1% |
| P btts no | 24.9% |
| Fair Over 0.5 odds | 1.01 |
| Fair Under 0.5 odds | 161.63 |
| Fair Over 1.5 odds | 1.05 |
| Fair Under 1.5 odds | 22.90 |
| Fair Over 2.5 odds | 1.15 |
| Fair Under 2.5 odds | 7.49 |
| Fair Over 3.5 odds | 1.38 |
| Fair Under 3.5 odds | 3.67 |
| Fair Over 4.5 odds | 1.84 |
| Fair Under 4.5 odds | 2.20 |
| Goal margin distribution | {"-1": 0.06950680055302849, "-10": 1.464492668740445e-07, "-11": 1.9023941645438576e-08, "-12": 2.2777183213847974e-09, "-13": 2.5282858008022734e-10, "-14": 2.615132088127697e-11, "-15": 2.531907568851493e-12, "-16": 2.3036132804323175e-13, "-17": 1.9765510679867857e-14, "-18": 1.6042307391184948e-15, "-19": 1.2331424943603173e-16, "-2": 0.03077818892106651, "-20": 8.832837779303456e-18, "-21": 5.011534285159337e-19, "-3": 0.011268702617674034, "-4": 0.0034170239650289816, "-5": 0.0008782440612562445, "-6": 0.0001950787151934548, "-7": 3.805453060943512e-05, "-8": 6.606551899562527e-06, "-9": 1.0320998745210074e-06, "0": 0.1453316138055502, "1": 0.17160930810714714, "10": 0.0007565462642591027, "11": 0.0002294757884289502, "12": 6.415410596194086e-05, "13": 1.662794900609441e-05, "14": 4.016004810463254e-06, "15": 9.078968685850319e-07, "16": 1.92879610835117e-07, "17": 3.8643180504314214e-08, "18": 7.3235176746475595e-09, "19": 1.3144807807355823e-09, "2": 0.17992302290959464, "20": 2.1985143643694668e-10, "21": 2.912646879703447e-11, "3": 0.15381747305275473, "4": 0.10891002444550094, "5": 0.0653616683457827, "6": 0.033900481777327504, "7": 0.015441533551908535, "8": 0.006259605845568695, "9": 0.002283399691440285} |
| Raw goal margin distribution | {"-1": 0.07561672445527573, "-10": 1.5932273923963916e-07, "-11": 2.0696221693572047e-08, "-12": 2.477938810656175e-09, "-13": 2.7505321669581827e-10, "-14": 2.8450125879587158e-11, "-15": 2.7544723028073337e-12, "-16": 2.506110039478355e-13, "-17": 2.1502977592201312e-14, "-18": 1.745248994306084e-15, "-19": 1.3415406185902002e-16, "-2": 0.033483714001497106, "-20": 9.609279310823313e-18, "-21": 5.452068058433302e-19, "-3": 0.01225926634558602, "-4": 0.0037173939465612784, "-5": 0.0009554452032910063, "-6": 0.0002122269092593121, "-7": 4.1399675031411466e-05, "-8": 7.187294057760099e-06, "-9": 1.1228255537735176e-06, "0": 0.12429498013620677, "1": 0.17412610191494107, "10": 0.0007676416469874574, "11": 0.00023284124249275902, "12": 6.509497949852524e-05, "13": 1.6871811763636225e-05, "14": 4.0749028746214865e-06, "15": 9.212119343129565e-07, "16": 1.9570835139443698e-07, "17": 3.920991501585946e-08, "18": 7.430923176937181e-09, "19": 1.3337587390579475e-09, "2": 0.18256174428743333, "20": 2.2307574134186267e-10, "21": 2.955363278434867e-11, "3": 0.15607333474219168, "4": 0.11050728090061106, "5": 0.06632025179311554, "6": 0.03439766065159427, "7": 0.015667996536084312, "8": 0.006351408192452593, "9": 0.0023168876546954447} |
| Unadjusted home-win probability | 74.9% |
| Unadjusted draw probability | 12.4% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 95.6% |
| Raw p under 3 5 | 27.3% |
| Raw p btts yes | 74.7% |
| P home draw | 88.4% |
| P draw away | 26.1% |
| P home away | 85.5% |
| Raw p home draw | 87.4% |
| Raw p draw away | 25.1% |
| Raw p home away | 87.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / William Hill |
| Reference home odds | 1.33 |
| Reference draw odds | 5.00 |
| Reference away odds | 7.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:28:55Z |
| Market reference home last update utc | 2026-10-21T17:28:55Z |
| Market reference draw last update utc | 2026-10-21T17:28:55Z |
| Market reference away last update utc | 2026-10-21T17:28:55Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:28:55Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:28:55Z |
| Home probability edge | +1.1% |
| Draw probability edge | -2.1% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +12.1% |
| Under 2.5 probability edge | -12.1% |
| Raw edge prob home | 0.0217 |
| Raw ev home | 0.0042 |
| Raw edge prob draw | -0.0421 |
| Raw ev draw | -0.2679 |
| Raw edge prob away | 0.0204 |
| Raw ev away | 0.0672 |

</details>


---
