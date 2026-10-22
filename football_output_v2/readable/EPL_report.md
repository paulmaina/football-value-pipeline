# Premier League — football model report

Fixtures in this report: **18**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,970 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 240 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 72fb270aab150bee81f0f51bae563271f0b752386c4017510e5d78a6fc35c109 |
| Training as of utc | 2026-10-22T15:04:47.131720+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 60, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T15:04:47.131720+00:00', 'observations': 188, 'observations_sha256': '87ab8167f617b44c77e101e6429da3c336de22c386ba6dafcbcdfebdc6b75f90', 'eligible_training_matches': 103, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 101, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 103, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'ffcf4f614ddc2a074e5b01e3bac4c35e06fa935602f4431e95fa6e5fe48ce1d0', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 927.614 |
| Base scoring parameter | 0.212 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.089 |
| Xi per day | 0.0029 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 18.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261022T150447131720Z_5c7f4edbdb6912f8cf0e42cf89666163665e2fc2e509e6b85fa69a7027c2cd19.json |
| Over 1 5 in window quote fixtures | 3 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 240.0, 'selected_xi_per_day': 0.0028881132523331052, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Ipswich Town vs Nottingham Forest

The model's most likely 1X2 outcome is **Nottingham Forest win** at **43.4%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.6%; Under 3.5 goals: 64.6%; Double Chance 1X: 56.6%; Double Chance X2: 69.9%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 61.0%; BTTS No (at least one team does not score): 39.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 30.1% | 3.32 |
| Draw | 26.5% | 3.77 |
| Nottingham Forest win | 43.4% | 2.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.69 |
| Expected total goals | 3.01 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.6% |
| Under 2.5 | 42.4% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.32% |
| 2 | 1-2 | 8.92% |
| 3 | 2-1 | 7.52% |
| 4 | 0-1 | 7.05% |
| 5 | 0-2 | 6.75% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 30.1% | 31.1% | 3.29 | -1.0% |
| Draw | 26.5% | 27.3% | 3.48 | -7.7% |
| Nottingham Forest win | 43.4% | 41.6% | 2.26 | -1.9% |
| Over 2.5 | 57.6% | 53.6% | 1.83 | +5.5% |
| Under 2.5 | 42.4% | 46.4% | 2.14 | -9.4% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3211 |
| Dc lambda away | 1.6908 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.0% |
| P btts no | 39.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.47 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.31 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.36 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.40 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.19986324127413374, "-10": 3.0411282760476004e-06, "-11": 4.597740616868861e-07, "-12": 6.387683165180569e-08, "-13": 8.204345492640238e-09, "-14": 9.717989288579714e-10, "-15": 9.534242607026163e-11, "-2": 0.13417853457490284, "-3": 0.06471405876907088, "-4": 0.024770871007062958, "-5": 0.007822394917861108, "-6": 0.0020969684228879203, "-7": 0.0004876259246494349, "-8": 0.00010002950704410598, "-9": 1.834568627335587e-05, "0": 0.2651424629708108, "1": 0.16615432052716025, "10": 2.781534862518643e-07, "11": 3.285870601835246e-08, "12": 3.567020279868236e-09, "13": 3.5798297613204594e-10, "14": 3.313226081696884e-11, "15": 2.539902677719774e-12, "2": 0.08832487643203255, "3": 0.033285482351130484, "4": 0.009955285409649971, "5": 0.0024564526499397236, "6": 0.0005145371917789882, "7": 9.349058769360992e-05, "8": 1.4985300398155557e-05, "9": 2.1474719951317584e-06} |
| Raw goal margin distribution | {"-1": 0.20808078533271648, "-10": 3.1661668045779455e-06, "-11": 4.786780561624048e-07, "-12": 6.650318092481388e-08, "-13": 8.541674008518417e-09, "-14": 1.0117552533079513e-09, "-15": 9.926250953278247e-11, "-2": 0.13969539706825632, "-3": 0.06737483133412274, "-4": 0.02578934605316116, "-5": 0.008144019216913625, "-6": 0.0021831870306453257, "-7": 0.0005076750717280501, "-8": 0.00010414230375476173, "-9": 1.909998448384801e-05, "0": 0.25763396108012826, "1": 0.16044387420076858, "10": 2.6859381576781966e-07, "11": 3.1729407204592067e-08, "12": 3.4444277539037445e-09, "13": 3.456796994885123e-10, "14": 3.19935603819333e-11, "15": 2.4526104672652977e-12, "2": 0.08528929803388999, "3": 0.032141515948023204, "4": 0.009613138886975441, "5": 0.002372028477481864, "6": 0.0004968534083705037, "7": 9.02774724321268e-05, "8": 1.4470280666276028e-05, "9": 2.0736669714241465e-06} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 56.6% |
| P draw away | 69.9% |
| P home away | 73.5% |
| Raw p home draw | 54.8% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.48, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.7, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.05 |
| Reference draw odds | 3.46 |
| Reference away odds | 2.31 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -1.0% |
| Draw probability edge | -0.8% |
| Away probability edge | +1.8% |
| Over 2.5 probability edge | +4.0% |
| Under 2.5 probability edge | -4.0% |
| Raw edge prob home | -0.0207 |
| Raw ev home | -0.0444 |
| Raw edge prob draw | -0.0150 |
| Raw ev draw | -0.1034 |
| Raw edge prob away | 0.0357 |
| Raw ev away | 0.0213 |
| Market p home draw | 57.1% |
| Market home draw odds | 1.69 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:04:32Z |
| Market reference home draw last update utc | 2026-10-22T15:04:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.9% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:04:32Z |
| Market reference draw away last update utc | 2026-10-22T15:04:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:04:32Z |
| Market reference home away last update utc | 2026-10-22T15:04:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.69 |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 78.5% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference over 1 5 odds | 1.24 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-10-22T15:04:40Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.3% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.80 |
| Market reference under 3 5 last update utc | 2026-10-22T15:04:40Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 59.8% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:04:32Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.46 |
| Market reference btts yes last update utc | 2026-10-22T15:04:39Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.2%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.2%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.4%; Under 3.5 goals: 79.7%; Double Chance 1X: 88.9%; Double Chance X2: 32.8%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.2% | 1.49 |
| Draw | 21.7% | 4.61 |
| Everton win | 11.1% | 8.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.19% |
| 2 | 2-0 | 15.55% |
| 3 | 0-0 | 9.69% |
| 4 | 1-1 | 9.59% |
| 5 | 2-1 | 8.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.2% | 70.1% | 1.46 | -1.9% |
| Draw | 21.7% | 18.8% | 4.35 | -5.6% |
| Everton win | 11.1% | 11.1% | 8.19 | -8.9% |
| Over 2.5 | 41.4% | 52.0% | 1.92 | -20.6% |
| Under 2.5 | 58.6% | 48.0% | 2.02 | +18.5% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7157 |
| Dc lambda away | 0.5763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.14 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.93 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.66 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.08339810525626351, "-10": 1.232516552836455e-10, "-11": 6.409463586120857e-12, "-12": 3.0588174938427e-13, "-13": 1.3486840894518234e-14, "-14": 5.525567280357658e-16, "-15": 2.110654318663169e-17, "-16": 7.159753618954117e-19, "-2": 0.02307820391161536, "-3": 0.004110084071464772, "-4": 0.0005650871926693439, "-5": 6.309842508565186e-05, "-6": 5.923455962315224e-06, "-7": 4.793131909417846e-07, "-8": 3.406525933242616e-08, "-9": 2.1577846228613942e-09, "0": 0.21708031012490214, "1": 0.27760754135884025, "10": 7.037878969664158e-06, "11": 1.0896116994807745e-06, "12": 1.5481202033834e-07, "13": 2.032181001713363e-08, "14": 2.4787347994980425e-09, "15": 2.818845955519987e-10, "16": 2.8467763546035303e-11, "2": 0.21352204548257092, "3": 0.11321199933393418, "4": 0.04634023789016348, "5": 0.015405023099861925, "6": 0.00430546475309109, "7": 0.0010372066561019184, "8": 0.00021946165666323212, "9": 4.138625100745421e-05} |
| Raw goal margin distribution | {"-1": 0.08327473326361566, "-10": 1.2306932737268436e-10, "-11": 6.399981976292987e-12, "-12": 3.0542925420083393e-13, "-13": 1.3466889620678516e-14, "-14": 5.517393230793909e-16, "-15": 2.1075319979787347e-17, "-16": 7.149162094504924e-19, "-2": 0.023044063999268907, "-3": 0.0041040039661639546, "-4": 0.0005642512512200128, "-5": 6.300508269601557e-05, "-6": 5.914693310415796e-06, "-7": 4.786041361822407e-07, "-8": 3.4014866114127096e-08, "-9": 2.154592581653632e-09, "0": 0.2464142365544608, "1": 0.26555206985501273, "10": 6.7322498467992945e-06, "11": 1.0422938826483129e-06, "12": 1.480891053537417e-07, "13": 1.943930876962222e-08, "14": 2.3710924905224804e-09, "15": 2.6964338736143143e-10, "16": 2.723151358493171e-11, "2": 0.20424957067099234, "3": 0.10829561981059335, "4": 0.044327852294905705, "5": 0.014736039771501501, "6": 0.0041184943005321975, "7": 0.0009921645969956992, "8": 0.0002099312464476591, "9": 3.958899878862599e-05} |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 88.9% |
| P draw away | 32.8% |
| P home away | 78.3% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.55, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 5.38, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:04:21Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:51Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.4, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:51Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.4, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.39 |
| Reference draw odds | 4.71 |
| Reference away odds | 7.64 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.96 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -2.9% |
| Draw probability edge | +2.9% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.0583 |
| Raw ev home | -0.0619 |
| Raw edge prob draw | 0.0587 |
| Raw ev draw | 0.0719 |
| Raw edge prob away | -0.0003 |
| Raw ev away | -0.0904 |
| Market p home draw | 87.7% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:04:51Z |
| Market reference home draw last update utc | 2026-10-22T15:04:51Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.2% |
| Market draw away odds | 2.93 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:04:51Z |
| Market reference draw away last update utc | 2026-10-22T15:04:51Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:04:51Z |
| Market reference home away last update utc | 2026-10-22T15:04:51Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.93 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 76.5% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T15:04:21Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.64 |
| Market reference over 1 5 last update utc | 2026-10-22T15:04:21Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.9% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.18 |
| Market reference under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 45.0% |
| Market btts yes odds | 2.13 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:04:51Z |
| Market reference btts yes odds | 2.13 |
| Market reference btts yes opposite odds | 1.76 |
| Market reference btts yes last update utc | 2026-10-22T15:04:51Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.0%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 56.8%; Under 3.5 goals: 65.7%; Double Chance 1X: 45.0%; Double Chance X2: 79.2%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 82.2%; BTTS Yes (both teams score): 57.3%; BTTS No (at least one team does not score): 42.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.8% | 4.80 |
| Draw | 24.1% | 4.15 |
| Manchester City win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 56.8% |
| Under 2.5 | 43.2% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.8% |
| Under 4.5 | 82.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.37% |
| 2 | 1-2 | 10.21% |
| 3 | 0-2 | 9.10% |
| 4 | 0-1 | 8.98% |
| 5 | 1-3 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.8% | 19.4% | 4.65 | -3.1% |
| Draw | 24.1% | 23.4% | 4.36 | +5.2% |
| Manchester City win | 55.0% | 57.2% | 1.69 | -7.0% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1220 |
| Dc lambda away | 1.8242 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.3% |
| P btts no | 42.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.58 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.76 |
| Fair Under 2.5 odds | 2.32 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.63 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.23341027337196443, "-10": 7.40092482814298e-06, "-11": 1.2088416662799992e-06, "-12": 1.8141055482780486e-07, "-13": 2.5175462076749083e-08, "-14": 3.247985492251905e-09, "-15": 3.890474134873052e-10, "-16": 3.932569824871112e-11, "-2": 0.1714102422494568, "-3": 0.09019374355535469, "-4": 0.03752739077300224, "-5": 0.012853970347480518, "-6": 0.0037324014734318634, "-7": 0.0009392653970136174, "-8": 0.00020838218844904737, "-9": 4.131420930338895e-05, "0": 0.24123398207979488, "1": 0.1253713909676379, "10": 5.146056891890231e-08, "11": 5.169895769525852e-09, "12": 4.771980875403419e-10, "13": 4.073215331136973e-11, "14": 3.232196654264046e-12, "15": 2.381277477575249e-13, "16": 1.48049754278065e-14, "2": 0.05818823013623445, "3": 0.018832092058419223, "4": 0.004819414738427313, "5": 0.0010153294937961048, "6": 0.00018133508359155905, "7": 2.8067619736966373e-05, "8": 3.830025205773125e-06, "9": 4.6705094931405747e-07} |
| Raw goal margin distribution | {"-1": 0.22411771189775975, "-10": 7.106278204676289e-06, "-11": 1.160715097838063e-06, "-12": 1.741882132039617e-07, "-13": 2.4173173164568757e-08, "-14": 3.1186762531252396e-09, "-15": 3.735586050729051e-10, "-16": 3.7760058214050744e-11, "-2": 0.16458603442689443, "-3": 0.08660293799881805, "-4": 0.036033345199571576, "-5": 0.012342226335891037, "-6": 0.003583806599533552, "-7": 0.0009018712355816868, "-8": 0.00020008604848777755, "-9": 3.966940239680481e-05, "0": 0.24854171529956406, "1": 0.13415406309927566, "10": 5.506554850024021e-08, "11": 5.532063718274279e-09, "12": 5.106273596602725e-10, "13": 4.358557262009947e-11, "14": 3.4586225019816104e-12, "15": 2.5480936800483895e-13, "16": 1.5842111923587594e-14, "2": 0.06226450418298843, "3": 0.02015134112174507, "4": 0.005157030355413773, "5": 0.001086456614431583, "6": 0.0001940381937098705, "7": 3.0033847436624667e-05, "8": 4.098330880445719e-06, "9": 4.997693815252337e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 45.0% |
| P draw away | 79.2% |
| P home away | 75.9% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.35, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.64, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T14:59:12Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 8.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.12, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:51Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.62, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:51Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.31, "price": 3.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.84 |
| Reference draw odds | 4.04 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:20Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:20Z |
| Home probability edge | +1.5% |
| Draw probability edge | +0.7% |
| Away probability edge | -2.2% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | 0.0292 |
| Raw ev home | 0.0371 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0836 |
| Raw edge prob away | -0.0438 |
| Raw ev away | -0.1070 |
| Market p home draw | 42.6% |
| Market home draw odds | 2.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:04:51Z |
| Market reference home draw last update utc | 2026-10-22T15:04:51Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 79.3% |
| Market draw away odds | 1.22 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:04:51Z |
| Market reference draw away last update utc | 2026-10-22T15:04:51Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.0% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:04:51Z |
| Market reference home away last update utc | 2026-10-22T15:04:51Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.27 |
| Market reference dc draw away odds | 1.22 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 84.9% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T14:59:12Z |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:04:19Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.0% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.33 |
| Market reference under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:04:51Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.47 |
| Market reference btts yes last update utc | 2026-10-22T15:04:51Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.1%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.6%; Double Chance 1X: 79.4%; Double Chance X2: 42.9%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.1% | 1.75 |
| Draw | 22.3% | 4.48 |
| Tottenham Hotspur win | 20.6% | 4.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.2% |
| Under 1.5 | 14.8% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 42.4% |
| Under 3.5 | 57.6% |
| Over 4.5 | 24.1% |
| Under 4.5 | 75.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.04% |
| 2 | 2-1 | 9.60% |
| 3 | 2-0 | 8.04% |
| 4 | 3-1 | 6.82% |
| 5 | 1-0 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.1% | 56.2% | 1.74 | -0.6% |
| Draw | 22.3% | 22.5% | 4.28 | -4.6% |
| Tottenham Hotspur win | 20.6% | 21.3% | 4.37 | -10.1% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1330 |
| Dc lambda away | 1.1934 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.50 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12241223167605693, "-10": 7.565345845552e-08, "-11": 8.054656164538308e-09, "-12": 7.883288981236957e-10, "-13": 7.138034729049429e-11, "-14": 6.012282171521491e-12, "-15": 4.73126845443212e-13, "-16": 3.4647578133975835e-14, "-17": 2.1154521173490003e-15, "-2": 0.05756563929317754, "-3": 0.01924677120399983, "-4": 0.005136892209930904, "-5": 0.0011350241213307338, "-6": 0.00021336418919973703, "-7": 3.4843571906924973e-05, "-8": 5.024804150353996e-06, "-9": 6.483436058224756e-07, "0": 0.22300518441238518, "1": 0.21392190549105777, "10": 2.388535898967026e-05, "11": 4.5452889128472345e-06, "12": 7.951213872273587e-07, "13": 1.2868150920866191e-07, "14": 1.9372619339296995e-08, "15": 2.7248216521624253e-09, "16": 3.5665217305346594e-10, "17": 3.892124215581766e-11, "2": 0.17449151445246225, "3": 0.1042750398392369, "4": 0.049743281807313106, "5": 0.019644933979767517, "6": 0.006600525496792272, "7": 0.001926598214327045, "8": 0.0004965913198799283, "9": 0.00011452405525995933} |
| Raw goal margin distribution | {"-1": 0.11801149584191023, "-10": 7.293370667055639e-08, "-11": 7.76509021569737e-09, "-12": 7.599883705181942e-10, "-13": 6.881421441411316e-11, "-14": 5.7961398364382316e-12, "-15": 4.56117873101717e-13, "-16": 3.340199314158648e-14, "-17": 2.03940133540692e-15, "-2": 0.05549614698685765, "-3": 0.018554847246978864, "-4": 0.0049522202591391305, "-5": 0.0010942198548373387, "-6": 0.00020569371852635092, "-7": 3.359094091261182e-05, "-8": 4.844161780051085e-06, "-9": 6.250355678926279e-07, "0": 0.22123822800855192, "1": 0.21735357100194713, "10": 2.4268520136593988e-05, "11": 4.618202956705624e-06, "12": 8.078764654660981e-07, "13": 1.3074577605420482e-07, "14": 1.96833885870262e-08, "15": 2.768532353343709e-09, "16": 3.6237347101424204e-10, "17": 3.954560404171474e-11, "2": 0.1772906504769607, "3": 0.10594778605492487, "4": 0.05054124732741617, "5": 0.019960071610237457, "6": 0.006706408976322306, "7": 0.0019575040751844018, "8": 0.0005045574760411085, "9": 0.00011636121284183784} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.4% |
| P draw away | 42.9% |
| P home away | 77.7% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.74 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.42 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.49 |
| Reference Under 2.5 odds | 2.66 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:20Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:20Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -0.6% |
| Under 2.5 probability edge | +0.6% |
| Raw edge prob home | 0.0183 |
| Raw ev home | 0.0099 |
| Raw edge prob draw | -0.0035 |
| Raw ev draw | -0.0531 |
| Raw edge prob away | -0.0148 |
| Raw ev away | -0.1332 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **41.8%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 45.1%; Under 3.5 goals: 76.4%; Double Chance 1X: 58.2%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 71.6%; Under 4.5 goals: 89.5%; BTTS Yes (both teams score): 50.7%; BTTS No (at least one team does not score): 49.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 29.8% | 3.35 |
| Draw | 28.4% | 3.52 |
| Fulham win | 41.8% | 2.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.7% |
| Under 0.5 | 9.3% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.1% |
| Under 2.5 | 54.9% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.5% |
| Under 4.5 | 89.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.51% |
| 2 | 0-1 | 10.46% |
| 3 | 0-0 | 9.35% |
| 4 | 1-2 | 8.72% |
| 5 | 1-0 | 8.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 29.8% | 30.6% | 3.20 | -4.5% |
| Draw | 28.4% | 27.6% | 3.54 | +0.5% |
| Fulham win | 41.8% | 41.8% | 2.28 | -4.8% |
| Over 2.5 | 45.1% | 54.9% | 1.81 | -18.4% |
| Under 2.5 | 54.9% | 45.1% | 2.15 | +18.1% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1010 |
| Dc lambda away | 1.3665 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.7% |
| P btts no | 49.3% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.70 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.22 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.50 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.2166262625521455, "-10": 6.081559480082364e-07, "-11": 7.470421738244928e-08, "-12": 8.424620387629518e-09, "-13": 8.741068059014487e-10, "-14": 7.703863849520354e-11, "-2": 0.12722979977007765, "-3": 0.05188279652817899, "-4": 0.016537586616930847, "-5": 0.004310742724482207, "-6": 0.0009486423909959361, "-7": 0.0001804349614507073, "-8": 3.019913825453468e-05, "-9": 4.510745948256177e-06, "0": 0.2837852980143757, "1": 0.17686938656021994, "10": 7.196416157559147e-08, "11": 7.122395410503487e-09, "12": 6.471589322214929e-10, "13": 5.410093360047157e-11, "14": 3.841744743180468e-12, "2": 0.08477210434609729, "3": 0.02785269003838762, "4": 0.007153120644661899, "5": 0.001502294823644235, "6": 0.0002663699587357761, "7": 4.082094513909379e-05, "8": 5.504736865767385e-06, "9": 6.62475818065878e-07} |
| Raw goal margin distribution | {"-1": 0.2164728174226935, "-10": 6.077251665920327e-07, "-11": 7.465130136861139e-08, "-12": 8.418652888810426e-09, "-13": 8.734876407531135e-10, "-14": 7.698406891662413e-11, "-2": 0.12713967776517449, "-3": 0.05184604584829462, "-4": 0.016525872376518064, "-5": 0.004307689251336339, "-6": 0.000947970429282822, "-7": 0.0001803071520812833, "-8": 3.017774698542348e-05, "-9": 4.507550804750488e-06, "0": 0.29195603252849994, "1": 0.17220276069878868, "10": 7.006541683498861e-08, "11": 6.934473943344e-09, "12": 6.300839105442236e-10, "13": 5.267350276703236e-11, "14": 3.740381891642339e-12, "2": 0.08253542731474028, "3": 0.027117808292194, "4": 0.006964388504863631, "5": 0.0014626573939462157, "6": 0.00025934189716831247, "7": 3.974390132739208e-05, "8": 5.359496652535698e-06, "9": 6.449966666689999e-07} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.7% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 50.9% |
| P home draw | 58.2% |
| P draw away | 70.2% |
| P home away | 71.6% |
| Raw p home draw | 58.3% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.15 |
| Reference draw odds | 3.49 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.8% |
| Away probability edge | -0.0% |
| Over 2.5 probability edge | -9.8% |
| Under 2.5 probability edge | +9.8% |
| Raw edge prob home | -0.0157 |
| Raw ev home | -0.0701 |
| Raw edge prob draw | 0.0163 |
| Raw ev draw | 0.0335 |
| Raw edge prob away | -0.0006 |
| Raw ev away | -0.0482 |
| Market p home draw | 57.5% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T15:04:39Z |
| Market reference home draw last update utc | 2026-10-22T15:04:39Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.0% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T15:04:39Z |
| Market reference draw away last update utc | 2026-10-22T15:04:39Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T15:04:39Z |
| Market reference home away last update utc | 2026-10-22T15:04:39Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-22T15:04:19Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market reference under 3 5 last update utc | 2026-10-22T15:04:39Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.2% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T15:04:39Z |
| Market reference btts yes odds | 1.61 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-22T15:04:39Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **39.6%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.3%; Under 3.5 goals: 63.0%; Double Chance 1X: 60.4%; Double Chance X2: 65.6%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.4% | 2.91 |
| Draw | 26.0% | 3.84 |
| Newcastle United win | 39.6% | 2.52 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.3% |
| Under 2.5 | 40.7% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.94% |
| 2 | 1-2 | 8.78% |
| 3 | 2-1 | 7.96% |
| 4 | 2-2 | 6.48% |
| 5 | 0-1 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.4% | 33.5% | 3.04 | +4.5% |
| Draw | 26.0% | 26.1% | 3.72 | -3.2% |
| Newcastle United win | 39.6% | 40.3% | 2.30 | -8.9% |
| Over 2.5 | 59.3% | 59.0% | 1.69 | +0.2% |
| Under 2.5 | 40.7% | 41.0% | 2.36 | -4.0% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4955 |
| Dc lambda away | 1.5800 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.80 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.60 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.07 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.19438885462372169, "-10": 1.5542449389897595e-06, "-11": 2.1937448167119819e-07, "-12": 2.8457721627813918e-08, "-13": 3.412956401217361e-09, "-14": 3.7717460864263013e-10, "-15": 3.432208437082438e-11, "-2": 0.12094496795236102, "-3": 0.05409956561789945, "-4": 0.019252678797452856, "-5": 0.005660789278874461, "-6": 0.0014142218401892945, "-7": 0.0003066683241314776, "-8": 5.8688619969874156e-05, "-9": 1.0044741422224951e-05, "0": 0.2601588487842121, "1": 0.17578274597413285, "10": 8.595616680515879e-07, "11": 1.1483571241073343e-07, "12": 1.4100167484430276e-08, "13": 1.600619738170705e-09, "14": 1.6742995452830234e-10, "15": 1.4421075436952148e-11, "2": 0.10381954383664108, "3": 0.043956021161641066, "4": 0.014806385219262051, "5": 0.004120672988828641, "6": 0.0009744105674470996, "7": 0.0001999984585434547, "8": 3.622804588846894e-05, "9": 5.868985766814972e-06} |
| Raw goal margin distribution | {"-1": 0.19086278970063758, "-10": 1.5260521263315379e-06, "-11": 2.1539519661219677e-07, "-12": 2.794152035579674e-08, "-13": 3.351047986387495e-09, "-14": 3.703329501535818e-10, "-15": 3.369950805068833e-11, "-2": 0.11875111887626119, "-3": 0.05311824093728124, "-4": 0.018903449951413756, "-5": 0.005558106897459914, "-6": 0.0013885689392871125, "-7": 0.0003011055956363994, "-8": 5.7624053358477836e-05, "-9": 9.862537506990629e-06, "0": 0.258831981717736, "1": 0.18013636914025602, "10": 8.808504900574267e-07, "11": 1.1767985627183345e-07, "12": 1.4449387286784862e-08, "13": 1.640262395552332e-09, "14": 1.715767035433885e-10, "15": 1.4778243188285174e-11, "2": 0.10639084950511699, "3": 0.045044682912596334, "4": 0.01517309596405045, "5": 0.004222729975620863, "6": 0.0009985438599169833, "7": 0.0002049518339016474, "8": 3.7125308352821515e-05, "9": 6.014343334501468e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 60.4% |
| P draw away | 65.6% |
| P home away | 74.0% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.9, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.84 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.26 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +0.9% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0170 |
| Raw ev home | 0.0707 |
| Raw edge prob draw | -0.0027 |
| Raw ev draw | -0.0371 |
| Raw edge prob away | -0.0144 |
| Raw ev away | -0.1054 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **43.0%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 13.8%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.9%; Under 3.5 goals: 81.0%; Double Chance 1X: 57.0%; Double Chance X2: 70.8%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.9%; BTTS No (at least one team does not score): 54.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 29.2% | 3.43 |
| Draw | 27.8% | 3.59 |
| Brentford win | 43.0% | 2.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 39.9% |
| Under 2.5 | 60.1% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.82% |
| 2 | 1-1 | 12.97% |
| 3 | 0-0 | 10.55% |
| 4 | 1-2 | 9.71% |
| 5 | 1-0 | 8.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 29.2% | 20.4% | 4.92 | +43.5% |
| Draw | 27.8% | 24.6% | 4.21 | +17.1% |
| Brentford win | 43.0% | 55.0% | 1.68 | -27.7% |
| Over 2.5 | 39.9% | 56.7% | 1.73 | -30.9% |
| Under 2.5 | 60.1% | 43.3% | 2.28 | +37.0% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1914 |
| Dc lambda away | 1.0535 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.9% |
| P btts no | 54.1% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.48 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.01 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.57 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2578927637093715, "-10": 7.634764790187819e-08, "-11": 7.242852082821339e-09, "-12": 6.283700116055553e-10, "-13": 4.6439227589478266e-11, "-2": 0.12139519110583023, "-3": 0.038802840023886155, "-4": 0.009638606841925376, "-5": 0.0019515604783061603, "-6": 0.0003329327675797399, "-7": 4.902703250926755e-05, "-8": 6.347225636822922e-06, "-9": 7.328854539323199e-07, "0": 0.2781723317945996, "1": 0.16315272124525368, "10": 1.4508457548445398e-07, "11": 1.5565554677674244e-08, "12": 1.527213801276096e-09, "13": 1.2764352267655662e-10, "2": 0.08621678652893566, "3": 0.031166157854901996, "4": 0.008755146602695963, "5": 0.002004751630712391, "6": 0.00038678044254333323, "7": 6.441291837632088e-05, "8": 9.430847244581654e-06, "9": 1.231493940666746e-06} |
| Raw goal margin distribution | {"-1": 0.1860627879561116, "-10": 5.5082802705250254e-08, "-11": 5.2255256483355795e-09, "-12": 4.533522947510886e-10, "-13": 3.350467082342844e-11, "-2": 0.08758341016140325, "-3": 0.027995219763496195, "-4": 0.006953999155410651, "-5": 0.0014079991165157763, "-6": 0.0002402021601801908, "-7": 3.537170342696883e-05, "-8": 4.579354925618115e-06, "-9": 5.287574139334899e-07, "0": 0.31065320527144347, "1": 0.21197427041174102, "10": 1.8849944274042553e-07, "11": 2.0223365391461692e-08, "12": 1.9842147211360706e-09, "13": 1.658393582750906e-10, "2": 0.11201615444858923, "3": 0.04049226713723718, "4": 0.011375022122153536, "5": 0.0026046501770461256, "6": 0.0005025199793904049, "7": 8.368773302522438e-05, "8": 1.225291830118911e-05, "9": 1.600004140886541e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.5% |
| P home draw | 57.0% |
| P draw away | 70.8% |
| P home away | 72.2% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.05, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 4.62 |
| Reference draw odds | 3.87 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.19 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +8.7% |
| Draw probability edge | +3.2% |
| Away probability edge | -12.0% |
| Over 2.5 probability edge | -16.8% |
| Under 2.5 probability edge | +16.8% |
| Raw edge prob home | 0.1746 |
| Raw ev home | 0.8650 |
| Raw edge prob draw | 0.0650 |
| Raw ev draw | 0.3078 |
| Raw edge prob away | -0.2396 |
| Raw ev away | -0.4787 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.6%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.1%; Double Chance 1X: 68.5%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.6% | 2.29 |
| Draw | 24.8% | 4.03 |
| Brighton and Hove Albion win | 31.5% | 3.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.47 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.4% |
| Under 2.5 | 39.6% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.34% |
| 2 | 2-1 | 9.43% |
| 3 | 1-2 | 7.43% |
| 4 | 1-0 | 6.78% |
| 5 | 2-0 | 6.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.6% | 46.5% | 2.11 | -7.9% |
| Draw | 24.8% | 24.0% | 4.00 | -0.7% |
| Brighton and Hove Albion win | 31.5% | 29.4% | 3.22 | +1.5% |
| Over 2.5 | 60.4% | 61.3% | 1.64 | -0.9% |
| Under 2.5 | 39.6% | 38.7% | 2.47 | -2.3% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6382 |
| Dc lambda away | 1.4736 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 19.07 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.79 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.87 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16345452746134576, "-10": 6.903837305593456e-07, "-11": 9.084886139713752e-08, "-12": 1.0988000936480529e-08, "-13": 1.2286818939893826e-09, "-14": 1.265605332584217e-10, "-15": 1.0709653571891632e-11, "-2": 0.09476986553224503, "-3": 0.039420166127464885, "-4": 0.01305784537001367, "-5": 0.0035756918719621503, "-6": 0.0008322628984100822, "-7": 0.0001681810687720271, "-8": 2.999859447943239e-05, "-9": 4.7860576100612625e-06, "0": 0.24834069230905287, "1": 0.20869855664809098, "10": 2.273383412019109e-06, "11": 3.325717666792176e-07, "12": 4.471655388017447e-08, "13": 5.558695032904675e-09, "14": 6.365249564193538e-10, "15": 5.9879244603948e-11, "2": 0.1337772919244095, "3": 0.06186062967145184, "4": 0.022779865623469564, "5": 0.006934632874397182, "6": 0.0017943521182363978, "7": 0.0004030955423453025, "8": 7.993105497033311e-05, "9": 1.4176737896179858e-05} |
| Raw goal margin distribution | {"-1": 0.17431408837633974, "-10": 7.362513139978217e-07, "-11": 9.688466083152986e-08, "-12": 1.1718019660078987e-08, "-13": 1.310312828783056e-09, "-14": 1.3496893797929411e-10, "-15": 1.1421179506038322e-11, "-2": 0.10106616789619505, "-3": 0.042039155653109075, "-4": 0.013925380025777603, "-5": 0.0038132530108299888, "-6": 0.0008875566231110455, "-7": 0.0001793546507427713, "-8": 3.199163541364963e-05, "-9": 5.1040327984293055e-06, "0": 0.2563370391079886, "1": 0.19485445738520427, "10": 2.1225776464015608e-06, "11": 3.10510490243539e-07, "12": 4.175026402865807e-08, "13": 5.189956853572609e-09, "14": 5.943008278891638e-10, "15": 5.590713181410468e-11, "2": 0.1249031236586242, "3": 0.057757080938815784, "4": 0.021268754449766978, "5": 0.006474621327567399, "6": 0.0016753230782832226, "7": 0.00037635604404553545, "8": 7.462879760464156e-05, "9": 1.3236318519012903e-05} |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 68.5% |
| P draw away | 56.4% |
| P home away | 75.2% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.87, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.05, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 2.05 |
| Reference draw odds | 3.81 |
| Reference away odds | 3.15 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.20 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -2.9% |
| Draw probability edge | +0.8% |
| Away probability edge | +2.1% |
| Over 2.5 probability edge | -0.9% |
| Under 2.5 probability edge | +0.9% |
| Raw edge prob home | -0.0579 |
| Raw ev home | -0.1404 |
| Raw edge prob draw | 0.0160 |
| Raw ev draw | 0.0253 |
| Raw edge prob away | 0.0419 |
| Raw ev away | 0.0828 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **48.9%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.5%; Under 3.5 goals: 63.9%; Double Chance 1X: 74.1%; Double Chance X2: 51.1%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 80.9%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 48.9% | 2.04 |
| Draw | 25.1% | 3.98 |
| Bournemouth win | 25.9% | 3.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.6% |
| Under 1.5 | 18.4% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.1% |
| Under 3.5 | 63.9% |
| Over 4.5 | 19.1% |
| Under 4.5 | 80.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.67% |
| 2 | 2-1 | 9.68% |
| 3 | 1-0 | 7.66% |
| 4 | 2-0 | 7.62% |
| 5 | 1-2 | 6.65% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 48.9% | 49.8% | 2.03 | -0.6% |
| Draw | 25.1% | 25.0% | 3.77 | -5.2% |
| Bournemouth win | 25.9% | 25.1% | 3.62 | -6.2% |
| Over 2.5 | 58.5% | 60.5% | 1.68 | -1.6% |
| Under 2.5 | 41.5% | 39.5% | 2.38 | -1.3% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7644 |
| Dc lambda away | 1.2710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.43 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.44 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.77 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.23 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.14661787736774343, "-10": 1.7330164589058824e-07, "-11": 1.9694774152646884e-08, "-12": 2.0568407947330862e-09, "-13": 1.9867492024124913e-10, "-14": 1.7841392212849675e-11, "-15": 1.4859629733738491e-12, "-16": 1.035327001572707e-13, "-2": 0.07510566150407631, "-3": 0.02721628992782133, "-4": 0.007828632019683332, "-5": 0.0018579853540675504, "-6": 0.00037435184670316074, "-7": 6.543028839532103e-05, "-8": 1.0088741128445175e-05, "-9": 1.3908135049851645e-06, "0": 0.25146022130870377, "1": 0.2171988034661564, "10": 4.827546792528231e-06, "11": 7.615716471771888e-07, "12": 1.1040694606380197e-07, "13": 1.4803851659945462e-08, "14": 1.845424896776299e-09, "15": 2.1335930126114578e-10, "16": 2.0635599510254793e-11, "2": 0.15174305378365402, "3": 0.07633101274308036, "4": 0.030478524547237987, "5": 0.010041215855529837, "6": 0.002808406401822728, "7": 0.0006813884481912174, "8": 0.0001458441010726484, "9": 2.790980140341035e-05} |
| Raw goal margin distribution | {"-1": 0.15091097420425276, "-10": 1.783760662893276e-07, "-11": 2.0271453982749892e-08, "-12": 2.11706685220713e-09, "-13": 2.0449229181212623e-10, "-14": 1.8363803434748578e-11, "-15": 1.5294732400254436e-12, "-16": 1.065642261587393e-13, "-2": 0.07730481950305872, "-3": 0.02801320617219983, "-4": 0.008057861060242963, "-5": 0.001912388754178313, "-6": 0.00038531318891923846, "-7": 6.734614319532816e-05, "-8": 1.0384148096548084e-05, "-9": 1.4315377138307897e-06, "0": 0.25284144719460955, "1": 0.2132195852032039, "10": 4.739103108421659e-06, "11": 7.476191770961714e-07, "12": 1.0838422158685817e-07, "13": 1.4532635815533707e-08, "14": 1.8116155555876226e-09, "15": 2.0945042508595341e-10, "16": 2.025754238872477e-11, "2": 0.1489630258955805, "3": 0.07493258073015145, "4": 0.02992013886752537, "5": 0.009857254485223305, "6": 0.0027569546356730717, "7": 0.0006689049845904159, "8": 0.0001431721456968785, "9": 2.7398476342279732e-05} |
| Unadjusted home-win probability | 48.0% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.1% |
| P draw away | 51.1% |
| P home away | 74.9% |
| Raw p home draw | 73.3% |
| Raw p draw away | 52.0% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 1.94 |
| Reference draw odds | 3.74 |
| Reference away odds | 3.72 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -0.9% |
| Draw probability edge | +0.1% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0179 |
| Raw ev home | -0.0246 |
| Raw edge prob draw | 0.0028 |
| Raw ev draw | -0.0468 |
| Raw edge prob away | 0.0152 |
| Raw ev away | -0.0347 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **39.4%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.3%; Under 3.5 goals: 80.3%; Double Chance 1X: 60.6%; Double Chance X2: 69.0%; Double Chance 12 (either team wins): 70.4%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.0% | 3.23 |
| Draw | 29.6% | 3.38 |
| Leeds United win | 39.4% | 2.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.88% |
| 2 | 0-1 | 11.59% |
| 3 | 0-0 | 10.98% |
| 4 | 1-0 | 9.72% |
| 5 | 1-2 | 8.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.0% | 30.8% | 3.22 | -0.3% |
| Draw | 29.6% | 28.5% | 3.24 | -4.0% |
| Leeds United win | 39.4% | 40.7% | 2.42 | -4.6% |
| Over 2.5 | 40.3% | 44.9% | 2.21 | -11.0% |
| Under 2.5 | 59.7% | 55.1% | 1.78 | +6.3% |

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
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0683 |
| Dc lambda away | 1.2111 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.10 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.10 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.07 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.14 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2186883940763218, "-10": 2.2246016829713134e-07, "-11": 2.4256968283169847e-08, "-12": 2.4278484841860235e-09, "-13": 2.237837515181912e-10, "-14": 1.7721203714335936e-11, "-2": 0.1169312810716922, "-3": 0.04285481820722726, "-4": 0.012216818921222552, "-5": 0.0028402488560699225, "-6": 0.0005565406151744346, "-7": 9.415208189318756e-05, "-8": 1.4005304274667434e-05, "-9": 1.8582410761832105e-06, "0": 0.2962723507611839, "1": 0.1845779386538917, "10": 6.115151563857345e-08, "11": 5.8816157170499064e-09, "12": 5.192623890278192e-10, "13": 4.221813056734114e-11, "14": 2.9489596359143535e-12, "2": 0.08770904445775925, "3": 0.028354271305389377, "4": 0.007129878542476517, "5": 0.0014621285253501482, "6": 0.00025271509385687413, "7": 3.771111793042438e-05, "8": 4.948085434287327e-06, "9": 5.79097724458357e-07} |
| Raw goal margin distribution | {"-1": 0.2116024186250445, "-10": 2.1525197922930937e-07, "-11": 2.3470990213766835e-08, "-12": 2.349180958956684e-09, "-13": 2.1653267550041579e-10, "-14": 1.7146998507803376e-11, "-2": 0.1131424554659253, "-3": 0.04146622970408345, "-4": 0.011820967649214628, "-5": 0.0027482186696732636, "-6": 0.0005385074993640525, "-7": 9.110135145182295e-05, "-8": 1.3551502221306854e-05, "-9": 1.7980300590233612e-06, "0": 0.3079088260496885, "1": 0.1852555956305292, "10": 6.137602649564909e-08, "11": 5.903209402371279e-09, "12": 5.211688020216817e-10, "13": 4.237312964755732e-11, "14": 2.9597864069015784e-12, "2": 0.0880310582711352, "3": 0.028458370798035676, "4": 0.007156055083249068, "5": 0.0014674965644731887, "6": 0.00025364290867430376, "7": 3.784957002469265e-05, "8": 4.966251769007484e-06, "9": 5.812238161028737e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 60.6% |
| P draw away | 69.0% |
| P home away | 70.4% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.25, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / GTbets |
| Reference home odds | 3.11 |
| Reference draw odds | 3.36 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:45Z |
| Market reference home last update utc | 2026-10-22T15:04:45Z |
| Market reference draw last update utc | 2026-10-22T15:04:45Z |
| Market reference away last update utc | 2026-10-22T15:04:45Z |
| O/U 2.5 market source | The Odds API / GTbets |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.75 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:45Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +0.1% |
| Draw probability edge | +1.2% |
| Away probability edge | -1.3% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0023 |
| Raw ev home | 0.0003 |
| Raw edge prob draw | 0.0233 |
| Raw ev draw | -0.0024 |
| Raw edge prob away | -0.0255 |
| Raw ev away | -0.0770 |

</details>


---

## 2026-10-31 — Aston Villa vs Fulham

The model's most likely 1X2 outcome is **Aston Villa win** at **47.6%**. Expected goals are 1.55 for Aston Villa and 1.05 for Fulham (2.60 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.5%; Double Chance 1X: 73.8%; Double Chance X2: 52.4%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 52.0%; BTTS No (at least one team does not score): 48.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 47.6% | 2.10 |
| Draw | 26.2% | 3.81 |
| Fulham win | 26.2% | 3.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.55 |
| Fulham expected goals | 1.05 |
| Expected total goals | 2.60 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 74.4% |
| Under 1.5 | 25.6% |
| Over 2.5 | 48.7% |
| Under 2.5 | 51.3% |
| Over 3.5 | 26.5% |
| Under 3.5 | 73.5% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.52% |
| 2 | 1-0 | 10.37% |
| 3 | 2-1 | 9.32% |
| 4 | 2-0 | 8.88% |
| 5 | 0-0 | 8.08% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 47.6% | 47.3% | 2.06 | -2.0% |
| Draw | 26.2% | 24.9% | 3.67 | -3.8% |
| Fulham win | 26.2% | 27.8% | 3.41 | -10.7% |
| Over 2.5 | 48.7% | 54.8% | 1.83 | -10.9% |
| Under 2.5 | 51.3% | 45.2% | 2.14 | +9.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T20:00:00+00:00 |
| Fixture id | 640c52a86289f35698261b41987dd71e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5522 |
| Dc lambda away | 1.0500 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.0% |
| P btts no | 48.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.38 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.05 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.78 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.05 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1600163767810197, "-10": 4.104278233162297e-08, "-11": 3.870241982056286e-09, "-12": 3.351577807968561e-10, "-13": 2.6825657484971886e-11, "-14": 1.9865917167998812e-12, "-15": 1.2542705546685085e-13, "-2": 0.07253537451729111, "-3": 0.02254439068545208, "-4": 0.005492327922741965, "-5": 0.001095960824304233, "-6": 0.00018481127949690056, "-7": 2.695304811515728e-05, "-8": 3.4604660743228806e-06, "-9": 3.9662356458263794e-07, "0": 0.26214016150329805, "1": 0.22596500133876055, "10": 1.9110036759648606e-06, "11": 2.664118961729038e-07, "12": 3.4107945950169296e-08, "13": 4.035965089828937e-09, "14": 4.418719283353563e-10, "15": 4.1244855332075743e-11, "2": 0.14799548230260529, "3": 0.0680029680869849, "4": 0.024492695971939777, "5": 0.0072254671144676135, "6": 0.0018013169602508023, "7": 0.000388383093735607, "8": 7.371872106233446e-05, "9": 1.2491439115463485e-05} |
| Raw goal margin distribution | {"-1": 0.15020743105115164, "-10": 3.8526874693965284e-08, "-11": 3.6329975554098863e-09, "-12": 3.146127306656541e-10, "-13": 2.518125443241302e-11, "-14": 1.8648143666967587e-12, "-15": 1.1773842256013813e-13, "-2": 0.06808898242637762, "-3": 0.021162427731440416, "-4": 0.005155650217568447, "-5": 0.0010287788241620023, "-6": 0.00017348241524362874, "-7": 2.5300836063275227e-05, "-8": 3.248340761864807e-06, "-9": 3.723106842485085e-07, "0": 0.2755460813760933, "1": 0.22722237547896154, "10": 1.9216373873349902e-06, "11": 2.6789433560779453e-07, "12": 3.429773839129526e-08, "13": 4.058423072722921e-09, "14": 4.4433070882205956e-10, "15": 4.147436084931793e-11, "2": 0.14881899785240887, "3": 0.06838136816231914, "4": 0.024628984699647444, "5": 0.007265672966908381, "6": 0.001811340323827931, "7": 0.0003905442375218622, "8": 7.412892623996508e-05, "9": 1.2560947280111213e-05} |
| Unadjusted home-win probability | 47.9% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.4% |
| Raw p under 3 5 | 73.6% |
| Raw p btts yes | 52.3% |
| P home draw | 73.8% |
| P draw away | 52.4% |
| P home away | 73.8% |
| Raw p home draw | 75.4% |
| Raw p draw away | 52.1% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.90 |
| Reference draw odds | 3.30 |
| Reference away odds | 3.00 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.0053 |
| Raw ev home | -0.0141 |
| Raw edge prob draw | 0.0268 |
| Raw ev draw | 0.0113 |
| Raw edge prob away | -0.0321 |
| Raw ev away | -0.1617 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **42.9%**. Expected goals are 1.44 for Bournemouth and 1.22 for Leeds United (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.4%; Double Chance 1X: 70.0%; Double Chance X2: 57.1%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 42.9% | 2.33 |
| Draw | 27.1% | 3.70 |
| Leeds United win | 30.0% | 3.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.44 |
| Leeds United expected goals | 1.22 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.91% |
| 2 | 1-0 | 9.45% |
| 3 | 2-1 | 9.25% |
| 4 | 0-0 | 7.85% |
| 5 | 2-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 42.9% | 44.8% | 2.15 | -7.7% |
| Draw | 27.1% | 26.0% | 3.37 | -8.8% |
| Leeds United win | 30.0% | 29.2% | 3.48 | +4.4% |
| Over 2.5 | 49.8% | 52.2% | 1.88 | -6.3% |
| Under 2.5 | 50.2% | 47.8% | 1.95 | -2.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | a6c06eabdf4e6710354b6098d39449e7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Bournemouth |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4356 |
| Dc lambda away | 1.2156 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.74 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.17007554123662016, "-10": 1.560317035995166e-07, "-11": 1.702063726776144e-08, "-12": 1.7048582103435086e-09, "-13": 1.5691622588086941e-10, "-14": 1.2114942724491395e-11, "-2": 0.08744734051830358, "-3": 0.031238255130507608, "-4": 0.008768897954662893, "-5": 0.002019048001408428, "-6": 0.0003932135539198796, "-7": 6.626889557486032e-05, "-8": 9.835879997504897e-06, "-9": 1.3036452800676422e-06, "0": 0.2706080317514671, "1": 0.21810159110850136, "10": 8.856861707748237e-07, "11": 1.1410079480125728e-07, "12": 1.3497301790167076e-08, "13": 1.4671428010724149e-09, "14": 1.3377400768479668e-10, "2": 0.13117373973189106, "3": 0.055339203206356304, "4": 0.018345814172852803, "5": 0.004988666343296148, "6": 0.0011473928339770685, "7": 0.00022837009179246047, "8": 4.0030273287716555e-05, "9": 6.265858888350259e-06} |
| Raw goal margin distribution | {"-1": 0.17486674283231105, "-10": 1.6042727595418153e-07, "-11": 1.7500125992853998e-08, "-12": 1.7528858063072353e-09, "-13": 1.613367161310473e-10, "-14": 1.2456233026972518e-11, "-2": 0.08991082135972163, "-3": 0.03211826866296292, "-4": 0.009015926760612006, "-5": 0.002075926644485423, "-6": 0.00040429078109369826, "-7": 6.813575800501544e-05, "-8": 1.0112966776687947e-05, "-9": 1.3403702982604994e-06, "0": 0.2810496222393458, "1": 0.2085045700493591, "10": 8.467137415068111e-07, "11": 1.0908007154560811e-07, "12": 1.2903386409433372e-08, "13": 1.4025848109766142e-09, "14": 1.278876133563932e-10, "2": 0.1254017637631915, "3": 0.05290413844654285, "4": 0.017538551997143187, "5": 0.0047691524199436576, "6": 0.001096904650306236, "7": 0.00021832123075907084, "8": 3.826884012350676e-05, "9": 5.9901452660906394e-06} |
| Unadjusted home-win probability | 41.0% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 54.7% |
| P home draw | 70.0% |
| P draw away | 57.1% |
| P home away | 72.9% |
| Raw p home draw | 69.2% |
| Raw p draw away | 59.0% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:04:39Z |
| Market best under 2 5 last update utc | 2026-10-22T15:04:39Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.0% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | -0.0378 |
| Raw ev home | -0.1175 |
| Raw edge prob draw | 0.0209 |
| Raw ev draw | -0.0529 |
| Raw edge prob away | 0.0169 |
| Raw ev away | 0.0735 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **48.2%**. Expected goals are 1.60 for Brentford and 1.08 for Nottingham Forest (2.68 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.6%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.0%; Double Chance X2: 51.8%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.5%; BTTS No (at least one team does not score): 46.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 48.2% | 2.08 |
| Draw | 25.8% | 3.87 |
| Nottingham Forest win | 26.0% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.60 |
| Nottingham Forest expected goals | 1.08 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.9% |
| Under 1.5 | 24.1% |
| Over 2.5 | 50.6% |
| Under 2.5 | 49.4% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.32% |
| 2 | 1-0 | 9.88% |
| 3 | 2-1 | 9.45% |
| 4 | 2-0 | 8.74% |
| 5 | 0-0 | 7.55% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 48.2% | 48.0% | 2.01 | -3.2% |
| Draw | 25.8% | 24.6% | 3.81 | -1.7% |
| Nottingham Forest win | 26.0% | 27.4% | 3.42 | -11.0% |
| Over 2.5 | 50.6% | 55.8% | 1.78 | -10.0% |
| Under 2.5 | 49.4% | 44.2% | 2.21 | +9.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | b9254b648ca25ce7831988b53ed17c3c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Brentford |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5979 |
| Dc lambda away | 1.0816 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.5% |
| P btts no | 46.5% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.24 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.39 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15733261830461673, "-10": 5.109887974015952e-08, "-11": 4.960261492757487e-09, "-12": 4.42235813295453e-10, "-13": 3.6443141579780924e-11, "-14": 2.777335949302393e-12, "-15": 1.7957736944404785e-13, "-2": 0.07265491671958041, "-3": 0.023117508400487916, "-4": 0.005777994020245765, "-5": 0.0011843112046665218, "-6": 0.00020529509086529758, "-7": 3.079311851616523e-05, "-8": 4.067480045130225e-06, "-9": 4.797572506023725e-07, "0": 0.25808009561223577, "1": 0.22477771919706135, "10": 2.391550487388445e-06, "11": 3.4295477222866653e-07, "12": 4.517002096972095e-08, "13": 5.4989059834033886e-09, "14": 6.190888834005015e-10, "15": 5.913441427117671e-11, "2": 0.14990646144157524, "3": 0.07046289321900237, "4": 0.026017205017758675, "5": 0.00787795495429628, "6": 0.002017392135074473, "7": 0.00044702265782153215, "8": 8.722990464824451e-05, "9": 1.519937106463566e-05} |
| Raw goal margin distribution | {"-1": 0.14910773176157804, "-10": 4.842758059781976e-08, "-11": 4.7009536108868345e-09, "-12": 4.1911702566693234e-10, "-13": 3.453800132345304e-11, "-14": 2.63214499448915e-12, "-15": 1.7018959273702732e-13, "-2": 0.06885673136391891, "-3": 0.0219089930538252, "-4": 0.005475937486928141, "-5": 0.0011223988981467633, "-6": 0.0001945628673225566, "-7": 2.918334484792665e-05, "-8": 3.854844151519802e-06, "-9": 4.546769525883599e-07, "0": 0.27051769243997714, "1": 0.22532403411224458, "10": 2.3973630728454956e-06, "11": 3.437883126167933e-07, "12": 4.5279805232427435e-08, "13": 5.512270895044341e-09, "14": 6.205935587394718e-10, "15": 5.927813853634128e-11, "2": 0.1502708042067764, "3": 0.07063415098276123, "4": 0.02608043898598006, "5": 0.007897102066866188, "6": 0.0020222953408597327, "7": 0.00044810913181132577, "8": 8.744191408641117e-05, "9": 1.5236312640267253e-05} |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.9% |
| Raw p btts yes | 53.8% |
| P home draw | 74.0% |
| P draw away | 51.8% |
| P home away | 74.2% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +0.1% |
| Draw probability edge | +1.2% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -5.2% |
| Under 2.5 probability edge | +5.2% |
| Raw edge prob home | 0.0023 |
| Raw ev home | -0.0296 |
| Raw edge prob draw | 0.0249 |
| Raw ev draw | 0.0307 |
| Raw edge prob away | -0.0272 |
| Raw ev away | -0.1563 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **49.4%**. Expected goals are 1.83 for Chelsea and 1.49 for Manchester United (3.33 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.0%; Under 3.5 goals: 57.2%; Double Chance 1X: 72.6%; Double Chance X2: 50.6%; Double Chance 12 (either team wins): 76.8%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 49.4% | 2.03 |
| Draw | 23.2% | 4.30 |
| Manchester United win | 27.4% | 3.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.83 |
| Manchester United expected goals | 1.49 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 85.5% |
| Under 1.5 | 14.5% |
| Over 2.5 | 65.0% |
| Under 2.5 | 35.0% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.22% |
| 2 | 2-1 | 9.91% |
| 3 | 2-0 | 6.63% |
| 4 | 1-2 | 6.54% |
| 5 | 2-2 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 49.4% | 53.9% | 1.82 | -10.1% |
| Draw | 23.2% | 22.1% | 4.01 | -6.8% |
| Manchester United win | 27.4% | 24.0% | 3.94 | +7.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T12:30:00+00:00 |
| Fixture id | 6601f69175a02f03fb7065aacb538e01 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8317 |
| Dc lambda away | 1.4947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.45 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.88 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1430980830406784, "-10": 6.276186910880705e-07, "-11": 8.358015859006073e-08, "-12": 1.023389092512045e-08, "-13": 1.159434182461755e-09, "-14": 1.2212939604052049e-10, "-15": 1.1895612612519927e-11, "-16": 9.489235862885647e-13, "-2": 0.0817619691129144, "-3": 0.03387415971176273, "-4": 0.011241153843410475, "-5": 0.0030946441515820196, "-6": 0.0007257670306108278, "-7": 0.00014799808580615723, "-8": 2.666751611554469e-05, "-9": 4.301268125563732e-06, "0": 0.23231566129638795, "1": 0.21895357346338537, "10": 5.924892094177142e-06, "11": 9.668905964068782e-07, "12": 1.4507898170264415e-07, "13": 2.014185123715635e-08, "14": 2.5999384246488696e-09, "15": 3.103267655963162e-10, "16": 3.033564497024476e-11, "2": 0.151781683433933, "3": 0.07705948870341366, "4": 0.03133704584293259, "5": 0.0105717637183117, "6": 0.0030382502017173947, "7": 0.0007592275645975576, "8": 0.00016764399603714765, "9": 3.313534700449751e-05} |
| Raw goal margin distribution | {"-1": 0.16076089162453794, "-10": 7.050865967985182e-07, "-11": 9.389658150234537e-08, "-12": 1.149707525741591e-08, "-13": 1.3025448628793546e-09, "-14": 1.3720400849436363e-10, "-15": 1.3363905716788536e-11, "-16": 1.066050631663169e-12, "-2": 0.0918539702019179, "-3": 0.038055297475557026, "-4": 0.012628666131338435, "-5": 0.0034766206681298723, "-6": 0.0008153495314086274, "-7": 0.00016626570899736854, "-8": 2.995912717382811e-05, "-9": 4.832180028472257e-06, "0": 0.24353567664352363, "1": 0.19898014503821052, "10": 5.384410355066724e-06, "11": 8.786887012889762e-07, "12": 1.3184455665445202e-07, "13": 1.830446709369483e-08, "14": 2.3627663008366495e-09, "15": 2.820180728309499e-10, "16": 2.7568360454351613e-11, "2": 0.13793582313411393, "3": 0.07002995199500463, "4": 0.028478411328319825, "5": 0.00960738408926276, "6": 0.002761094309799863, "7": 0.0006899691497654059, "8": 0.00015235114055736163, "9": 3.0112667487242056e-05} |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 66.0% |
| P home draw | 72.6% |
| P draw away | 50.6% |
| P home away | 76.8% |
| Raw p home draw | 69.2% |
| Raw p draw away | 55.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.45, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.05, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.70 |
| Reference draw odds | 3.65 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.51 |
| Reference Under 2.5 odds | 2.60 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:20Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:20Z |
| Home probability edge | -4.5% |
| Draw probability edge | +1.1% |
| Away probability edge | +3.4% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0901 |
| Raw ev home | -0.1834 |
| Raw edge prob draw | 0.0224 |
| Raw ev draw | -0.0234 |
| Raw edge prob away | 0.0676 |
| Raw ev away | 0.2127 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **37.7%**. Expected goals are 1.15 for Coventry City and 1.24 for Sunderland (2.39 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.9%; Double Chance 1X: 62.3%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 71.8%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 34.1% | 2.93 |
| Draw | 28.2% | 3.54 |
| Sunderland win | 37.7% | 2.65 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.15 |
| Sunderland expected goals | 1.24 |
| Expected total goals | 2.39 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 43.5% |
| Under 2.5 | 56.5% |
| Over 3.5 | 22.1% |
| Under 3.5 | 77.9% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.39% |
| 2 | 0-1 | 10.30% |
| 3 | 1-0 | 9.72% |
| 4 | 0-0 | 9.69% |
| 5 | 1-2 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 34.1% | 35.4% | 2.74 | -6.6% |
| Draw | 28.2% | 26.5% | 3.43 | -3.2% |
| Sunderland win | 37.7% | 38.1% | 2.54 | -4.3% |
| Over 2.5 | 43.5% | 50.7% | 1.92 | -16.5% |
| Under 2.5 | 56.5% | 49.3% | 1.92 | +8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | d20fbb0cd5ad9369b8ed6f2c4a198619 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Coventry |
| Matched away-team name | Sunderland |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1510 |
| Dc lambda away | 1.2427 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.53 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.33 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.2071724140170019, "-10": 2.5452073388301723e-07, "-11": 2.844920635665766e-08, "-12": 2.919221444319359e-09, "-13": 2.7569234272968536e-10, "-14": 2.220379210323924e-11, "-2": 0.11202925289644573, "-3": 0.041749576007702405, "-4": 0.012140941227988781, "-5": 0.002884496010751876, "-6": 0.00057823480652587, "-7": 0.00010014756028613398, "-8": 1.52587233240702e-05, "-9": 2.074409167187287e-06, "0": 0.282360268251293, "1": 0.19639488654553952, "10": 1.2158066206385996e-07, "11": 1.2586912392276885e-08, "12": 1.196255125039251e-09, "13": 1.0463794247657208e-10, "14": 7.805475351922173e-12, "2": 0.0988123078280508, "3": 0.03410667548264105, "4": 0.00918644318153687, "5": 0.002021495113795456, "6": 0.00037533122848027546, "7": 6.020860440340236e-05, "8": 8.496579042460656e-06, "9": 1.0698626925496527e-06} |
| Raw goal margin distribution | {"-1": 0.20474942437259278, "-10": 2.5154398089487403e-07, "-11": 2.811647802156096e-08, "-12": 2.8850796240249716e-09, "-13": 2.7246797671239256e-10, "-14": 2.1944107151514214e-11, "-2": 0.1107190122404832, "-3": 0.04126129289913742, "-4": 0.01199894657581283, "-5": 0.0028507603225495955, "-6": 0.0005714720482942932, "-7": 9.89762822342876e-05, "-8": 1.508026458101529e-05, "-9": 2.0501478679491095e-06, "0": 0.2999854903372552, "1": 0.18878034246949074, "10": 1.1686678520909884e-07, "11": 1.2098897653817119e-08, "12": 1.149874399267664e-09, "13": 1.0058096197657236e-10, "14": 7.50284458007699e-12, "2": 0.09498119650714416, "3": 0.0327843050873719, "4": 0.008830270076736046, "5": 0.0019431185128856176, "6": 0.000360779036044665, "7": 5.787422044844748e-05, "8": 8.167153074440623e-06, "9": 1.0283824036733401e-06} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.2% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 78.0% |
| Raw p btts yes | 49.8% |
| P home draw | 62.3% |
| P draw away | 65.9% |
| P home away | 71.8% |
| Raw p home draw | 62.8% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.45 |
| Reference draw odds | 3.15 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.90 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:04:39Z |
| Market best under 2 5 last update utc | 2026-10-22T15:04:39Z |
| Home probability edge | -1.3% |
| Draw probability edge | +1.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -7.3% |
| Under 2.5 probability edge | +7.3% |
| Raw edge prob home | -0.0264 |
| Raw ev home | -0.1020 |
| Raw edge prob draw | 0.0353 |
| Raw ev draw | 0.0290 |
| Raw edge prob away | -0.0088 |
| Raw ev away | -0.0544 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **48.5%**. Expected goals are 1.86 for Hull City and 0.87 for Ipswich Town (2.73 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 50.4%; Under 3.5 goals: 72.0%; Double Chance 1X: 73.3%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.0%; BTTS No (at least one team does not score): 49.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 48.5% | 2.06 |
| Draw | 24.8% | 4.03 |
| Ipswich Town win | 26.7% | 3.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.86 |
| Ipswich Town expected goals | 0.87 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.85% |
| 2 | 2-0 | 9.14% |
| 3 | 1-0 | 9.06% |
| 4 | 2-1 | 7.96% |
| 5 | 0-1 | 7.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 48.5% | 37.2% | 2.63 | +27.6% |
| Draw | 24.8% | 25.6% | 3.41 | -15.4% |
| Ipswich Town win | 26.7% | 37.2% | 2.66 | -29.0% |
| Over 2.5 | 50.4% | 54.3% | 1.81 | -8.8% |
| Under 2.5 | 49.6% | 45.7% | 2.17 | +7.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 1ec76c009147b63859f68c6b5a1dd77b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8625 |
| Dc lambda away | 0.8711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.0% |
| P btts no | 49.0% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.03 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.39 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17737676990605014, "-10": 8.615950990123675e-09, "-11": 6.740774627633063e-10, "-12": 4.843119031894345e-11, "-13": 3.21666283694951e-12, "-14": 1.9858229491573943e-13, "-15": 1.1405095608136532e-14, "-16": 5.637495938653071e-16, "-2": 0.0677480722593982, "-3": 0.017477296949491104, "-4": 0.0035335367846398794, "-5": 0.0005850930980788872, "-6": 8.186723901259801e-05, "-7": 9.906604522597457e-06, "-8": 1.0552988364335484e-06, "-9": 1.0035411080291548e-07, "0": 0.24813911021928528, "1": 0.19489171084679452, "10": 8.44762103887415e-06, "11": 1.4131175709357004e-06, "12": 2.1708555123848814e-07, "13": 3.08282309165784e-08, "14": 4.069310915113324e-09, "15": 4.997083017317805e-10, "16": 5.2813039460007346e-11, "2": 0.15206520638074417, "3": 0.08387730442510172, "4": 0.03625910690094237, "5": 0.012837183443144797, "6": 0.003840539201171664, "7": 0.0009936745588462069, "8": 0.00022632477125944143, "9": 4.6018142458014846e-05} |
| Raw goal margin distribution | {"-1": 0.10736025175714733, "-10": 5.21494820272612e-09, "-11": 4.0799663983293253e-10, "-12": 2.931378662659216e-11, "-13": 1.9469388927066027e-12, "-14": 1.2019524985125273e-13, "-15": 6.9031245548806706e-15, "-16": 3.41218854968587e-16, "-2": 0.041005651967181915, "-3": 0.010578425808101194, "-4": 0.002138732140589841, "-5": 0.0003541373672797729, "-6": 4.955151340116541e-05, "-7": 5.996137804109827e-06, "-8": 6.387372417399398e-07, "-9": 6.074100123918297e-08, "0": 0.24054614813451794, "1": 0.24026018441231087, "10": 1.0414126798038742e-05, "11": 1.7420745434175164e-06, "12": 2.676204870242442e-07, "13": 3.800467661215696e-08, "14": 5.016598123379025e-09, "15": 6.160344542350501e-10, "16": 6.510728724635605e-11, "2": 0.18746417879441907, "3": 0.10340294382773609, "4": 0.044699795967691816, "5": 0.01582552715035269, "6": 0.004734571073890235, "7": 0.0012249901841227433, "8": 0.00027901048763748297, "9": 5.6730618994699485e-05} |
| Unadjusted home-win probability | 59.8% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 50.1% |
| P home draw | 73.3% |
| P draw away | 51.5% |
| P home away | 75.2% |
| Raw p home draw | 83.9% |
| Raw p draw away | 40.2% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.35 |
| Reference draw odds | 3.25 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | +11.3% |
| Draw probability edge | -0.8% |
| Away probability edge | -10.5% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.2258 |
| Raw ev home | 0.5726 |
| Raw edge prob draw | -0.0152 |
| Raw ev draw | -0.1797 |
| Raw edge prob away | -0.2106 |
| Raw ev away | -0.5704 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **57.5%**. Expected goals are 1.97 for Manchester City and 1.14 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 2-1 at 10.2%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.7%; Under 3.5 goals: 62.1%; Double Chance 1X: 79.3%; Double Chance X2: 42.5%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 59.0%; BTTS No (at least one team does not score): 41.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 57.5% | 1.74 |
| Draw | 21.8% | 4.59 |
| Brighton and Hove Albion win | 20.7% | 4.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| Brighton and Hove Albion expected goals | 1.14 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.7% |
| Under 2.5 | 39.3% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.17% |
| 2 | 1-1 | 10.12% |
| 3 | 2-0 | 8.93% |
| 4 | 1-0 | 8.15% |
| 5 | 3-1 | 6.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 57.5% | 59.2% | 1.67 | -4.1% |
| Draw | 21.8% | 20.1% | 4.36 | -4.9% |
| Brighton and Hove Albion win | 20.7% | 20.7% | 4.40 | -8.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:00:00+00:00 |
| Fixture id | 7df53f9af95d5a4e13b504882078dab8 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9683 |
| Dc lambda away | 1.1396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.0% |
| P btts no | 41.0% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.11 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.55 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.84 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.12480430245489861, "-10": 5.56446652572594e-08, "-11": 5.6698929008301405e-09, "-12": 5.309184102162665e-10, "-13": 4.598049138443864e-11, "-14": 3.702224969268838e-12, "-15": 2.7646759738989374e-13, "-16": 1.7270525949994112e-14, "-2": 0.057743354336974285, "-3": 0.01876070220442394, "-4": 0.004838396058859168, "-5": 0.0010295699955658049, "-6": 0.00018599159809677105, "-7": 2.914694691519589e-05, "-8": 4.029516090927568e-06, "-9": 4.98066196601426e-07, "0": 0.21806855876099096, "1": 0.22924173246711205, "10": 1.3569858882328272e-05, "11": 2.3881326513387492e-06, "12": 3.8622747955001216e-07, "13": 5.7772450173397525e-08, "14": 8.034184075148884e-09, "15": 1.0362272394208703e-09, "16": 1.118016269477531e-10, "2": 0.17782771803272107, "3": 0.09978800276389999, "4": 0.044449046602660115, "5": 0.016336112131582443, "6": 0.005097038899141894, "7": 0.0013795882466764585, "8": 0.00032941328041577954, "9": 7.032456764836688e-05} |
| Raw goal margin distribution | {"-1": 0.12494445922555975, "-10": 5.570715490251658e-08, "-11": 5.676260260475149e-09, "-12": 5.315146381378748e-10, "-13": 4.6032128043264424e-11, "-14": 3.70638261356272e-12, "-15": 2.7677807391097846e-13, "-16": 1.728992096360468e-14, "-2": 0.057808200835947635, "-3": 0.018781770704344107, "-4": 0.004843829637297175, "-5": 0.0010307262153668026, "-6": 0.00018620046895495936, "-7": 2.917967929600257e-05, "-8": 4.034041287187012e-06, "-9": 4.986255310820329e-07, "0": 0.2352233038238791, "1": 0.2223039948302351, "10": 1.3159182694873863e-05, "11": 2.3158585605842462e-06, "12": 3.745387486525755e-07, "13": 5.602403334881224e-08, "14": 7.791038725304023e-09, "15": 1.0048670126335483e-09, "16": 1.0841807916702438e-10, "2": 0.17244596646856147, "3": 0.09676803351557299, "4": 0.04310384727869839, "5": 0.015841718467934043, "6": 0.004942782873301241, "7": 0.0013378365935225829, "8": 0.0003194439659762478, "9": 6.819627541064718e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.4% |
| P home draw | 79.3% |
| P draw away | 42.5% |
| P home away | 78.2% |
| Raw p home draw | 79.2% |
| Raw p draw away | 44.3% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.56 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.47 |
| Reference Under 2.5 odds | 2.73 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:20Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:20Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | -0.0348 |
| Raw ev home | -0.0696 |
| Raw edge prob draw | 0.0343 |
| Raw ev draw | 0.0256 |
| Raw edge prob away | 0.0005 |
| Raw ev away | -0.0864 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **52.2%**. Expected goals are 1.57 for Tottenham Hotspur and 1.25 for Crystal Palace (2.82 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.9%; Under 3.5 goals: 68.3%; Double Chance 1X: 75.9%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 76.3%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 56.7%; BTTS No (at least one team does not score): 43.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 52.2% | 1.91 |
| Draw | 23.7% | 4.22 |
| Crystal Palace win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Tottenham Hotspur expected goals | 1.57 |
| Crystal Palace expected goals | 1.25 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.7% |
| Under 1.5 | 21.3% |
| Over 2.5 | 54.9% |
| Under 2.5 | 45.1% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.22% |
| 2 | 2-1 | 10.98% |
| 3 | 1-0 | 9.92% |
| 4 | 2-0 | 8.76% |
| 5 | 0-0 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 52.2% | 60.8% | 1.62 | -15.4% |
| Draw | 23.7% | 20.5% | 4.33 | +2.6% |
| Crystal Palace win | 24.1% | 18.7% | 4.87 | +17.3% |
| Over 2.5 | 54.9% | 60.9% | 1.68 | -7.8% |
| Under 2.5 | 45.1% | 39.1% | 2.38 | +7.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T17:30:00+00:00 |
| Fixture id | 01b17432a283eb27af86ae45602eb6dd |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-22T15:04:39Z |
| Market best draw last update utc | 2026-10-22T15:04:39Z |
| Market best away last update utc | 2026-10-22T15:04:39Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5687 |
| Dc lambda away | 1.2530 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T15:04:47.131720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.7% |
| P btts no | 43.3% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.24 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.22 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.20 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.13554067113956092, "-10": 1.5277479252056284e-07, "-11": 1.7150645802268274e-08, "-12": 1.7687880612291777e-09, "-13": 1.686286664770452e-10, "-14": 1.4849007139753914e-11, "-15": 1.0967052288200917e-12, "-2": 0.07025166930633488, "-3": 0.025516686622018565, "-4": 0.007316639588497962, "-5": 0.0017254403767039243, "-6": 0.00034473835420407935, "-7": 5.966987905598122e-05, "-8": 9.102755539284452e-06, "-9": 1.2407109307573668e-06, "0": 0.23690629292234405, "1": 0.2514352111841802, "10": 2.1141693372193198e-06, "11": 2.9712987995516507e-07, "12": 3.836360671940967e-08, "13": 4.578812080864651e-09, "14": 5.047735766816423e-10, "15": 4.667312642315784e-11, "2": 0.16110998463398654, "3": 0.07326016125597606, "4": 0.026298624571249107, "5": 0.007764242867973087, "6": 0.0019420774317830708, "7": 0.0004208330866813615, "8": 8.037211222234547e-05, "9": 1.3714528874233156e-05} |
| Raw goal margin distribution | {"-1": 0.16575079799000378, "-10": 1.8682616487096273e-07, "-11": 2.0973285758949978e-08, "-12": 2.1630262721810923e-09, "-13": 2.0621364641009542e-10, "-14": 1.8158643911680483e-11, "-15": 1.3411455418393815e-12, "-2": 0.08590978744428093, "-3": 0.031204000497426873, "-4": 0.008947416596086352, "-5": 0.0021100169928210863, "-6": 0.0004215757294594714, "-7": 7.296946360338008e-05, "-8": 1.1131632902944562e-05, "-9": 1.5172481080324984e-06, "0": 0.26903585603356245, "1": 0.21013667187080745, "10": 1.7669144516483334e-06, "11": 2.4832593570760537e-07, "12": 3.206233764558954e-08, "13": 3.826736626358729e-09, "14": 4.2186390264371187e-10, "15": 3.900700862928667e-11, "2": 0.13464747366407423, "3": 0.06122709064711174, "4": 0.021979043492576004, "5": 0.0064889565315391735, "6": 0.0016230888510335123, "7": 0.00035171074024139827, "8": 6.717089501541283e-05, "9": 1.1461900822619441e-05} |
| Unadjusted home-win probability | 43.7% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 29.4% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.6% |
| P home draw | 75.9% |
| P draw away | 47.8% |
| P home away | 76.3% |
| Raw p home draw | 70.6% |
| Raw p draw away | 56.3% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T15:02:25Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T15:04:39Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.52 |
| Reference draw odds | 3.80 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-22T15:04:41Z |
| Market reference home last update utc | 2026-10-22T15:04:41Z |
| Market reference draw last update utc | 2026-10-22T15:04:41Z |
| Market reference away last update utc | 2026-10-22T15:04:41Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market reference under 2 5 last update utc | 2026-10-22T15:04:40Z |
| Market best over 2 5 last update utc | 2026-10-22T15:02:25Z |
| Market best under 2 5 last update utc | 2026-10-22T15:02:25Z |
| Home probability edge | -8.6% |
| Draw probability edge | +3.2% |
| Away probability edge | +5.4% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.1716 |
| Raw ev home | -0.2928 |
| Raw edge prob draw | 0.0643 |
| Raw ev draw | 0.1649 |
| Raw edge prob away | 0.1073 |
| Raw ev away | 0.4339 |

</details>


---
