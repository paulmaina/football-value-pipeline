# Serie A — football model report

Fixtures in this report: **20**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,970 |
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
| Training sha256 | b853f76a1c7d175b2be57ae97c26e1d88d1296ed6336164803055513fb1f3834 |
| Training as of utc | 2026-10-23T14:33:55.052720+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 63, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-23T14:33:55.052720+00:00', 'observations': 197, 'observations_sha256': '0ac0924301e6c2ff0d91137e29e8d1d6e1e231a34d06293ffc91e3341806c9fa', 'eligible_training_matches': 91, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 99, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 7, 'retrospective_eligible_training_matches': 91, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': '61cdfe0f2d468f2f694a0c7982174b928d742c55131fd6b385eb7a1580d75240', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 2436.826 |
| Base scoring parameter | 0.132 |
| Home-advantage parameter | 0.126 |
| Dixon-Coles low-score adjustment | -0.034 |
| Xi per day | 0.0009 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1970, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 20.00 |
| Additional event odds calls used before this league | 23.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261023T143355052720Z_a1ba47dcdff894f5257ffddd6ff959463963f22ed9fdba3252d0815e666e0873.json |
| Over 1 5 in window quote fixtures | 7 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 8.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 8.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 730.0, 'selected_xi_per_day': 0.0009495166856985552, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — Torino vs Monza

The model's most likely 1X2 outcome is **Torino win** at **47.2%**. Expected goals are 1.51 for Torino and 1.00 for Monza (2.51 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.3%; Over 2.5 goals: 45.6%; Under 3.5 goals: 75.7%; Double Chance 1X: 74.5%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 49.8%; BTTS No (at least one team does not score): 50.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 47.2% | 2.12 |
| Draw | 27.3% | 3.66 |
| Monza win | 25.5% | 3.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 1.51 |
| Monza expected goals | 1.00 |
| Expected total goals | 2.51 |
| Over 0.5 | 91.3% |
| Under 0.5 | 8.7% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.6% |
| Under 2.5 | 54.4% |
| Over 3.5 | 24.3% |
| Under 3.5 | 75.7% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.97% |
| 2 | 1-0 | 11.48% |
| 3 | 2-0 | 8.99% |
| 4 | 2-1 | 8.96% |
| 5 | 0-0 | 8.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 47.2% | 45.5% | 2.13 | +0.4% |
| Draw | 27.3% | 27.9% | 3.45 | -5.8% |
| Monza win | 25.5% | 26.6% | 3.72 | -5.0% |
| Over 2.5 | 45.6% | 50.3% | 1.91 | -12.9% |
| Under 2.5 | 54.4% | 49.7% | 2.00 | +8.8% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Torino |
| Matched away-team name | Monza |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5140 |
| Dc lambda away | 0.9959 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.8% |
| P btts no | 50.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.44 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.16 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.16196008733835182, "-10": 2.5692804808870756e-08, "-11": 2.3000479712192018e-09, "-12": 1.8906642447460948e-10, "-13": 1.436320941652294e-11, "-14": 1.0101514122312518e-12, "-15": 6.094012889117917e-14, "-2": 0.06758570619847615, "-3": 0.020081696698266746, "-4": 0.0046643615881913555, "-5": 0.0008859992115759714, "-6": 0.0001420875505939506, "-7": 1.969489791122313e-05, "-8": 2.402216466003888e-06, "-9": 2.6148939839609233e-07, "0": 0.2730952471536758, "1": 0.22994389799954096, "10": 1.5678745216035218e-06, "11": 2.1337787583835006e-07, "12": 2.66648787201414e-08, "13": 3.0795651929272133e-09, "14": 3.2925857424844755e-10, "15": 3.019720133370169e-11, "2": 0.14456160984718136, "3": 0.06529970683323894, "4": 0.02305768736661302, "5": 0.0066583953724080385, "6": 0.0016233231428018748, "7": 0.00034207032061416833, "8": 6.342880194074375e-05, "9": 1.0496419102810827e-05} |
| Raw goal margin distribution | {"-1": 0.15525824889083661, "-10": 2.4629647645137734e-08, "-11": 2.204872979787865e-09, "-12": 1.812429375062981e-10, "-13": 1.3768866015754893e-11, "-14": 9.683517831772107e-13, "-15": 5.841845268371811e-14, "-2": 0.06478903887291985, "-3": 0.01925072476415916, "-4": 0.0044713523206701, "-5": 0.0008493369469514576, "-6": 0.0001362080291320089, "-7": 1.8879931543826838e-05, "-8": 2.302813786395017e-06, "-9": 2.506690800535399e-07, "0": 0.26678143675049015, "1": 0.23817483171053688, "10": 1.6239972166032555e-06, "11": 2.210158221665544e-07, "12": 2.7619358708810934e-08, "13": 3.1897994595556977e-09, "14": 3.4104451648041496e-10, "15": 3.1278122221786285e-11, "2": 0.14973625043629313, "3": 0.06763713593210953, "4": 0.023883046499403926, "5": 0.006896735295357427, "6": 0.0016814306433538333, "7": 0.0003543148644266768, "8": 6.56992612514022e-05, "9": 1.0872142618806193e-05} |
| Unadjusted home-win probability | 48.8% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 71.9% |
| Raw p under 3 5 | 75.5% |
| Raw p btts yes | 49.6% |
| P home draw | 74.5% |
| P draw away | 52.8% |
| P home away | 72.7% |
| Raw p home draw | 75.5% |
| Raw p draw away | 51.2% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.5, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.15, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.7, "price": 1.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.12, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.62, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.58, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.1, "price": 6.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:08Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.81, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.2, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.81, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.15 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.62 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:48Z |
| Market reference home last update utc | 2026-10-23T14:33:48Z |
| Market reference draw last update utc | 2026-10-23T14:33:48Z |
| Market reference away last update utc | 2026-10-23T14:33:48Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.90 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:48Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:42Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:42Z |
| Home probability edge | +1.7% |
| Draw probability edge | -0.6% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -4.7% |
| Under 2.5 probability edge | +4.7% |
| Raw edge prob home | 0.0338 |
| Raw ev home | 0.0404 |
| Raw edge prob draw | -0.0126 |
| Raw ev draw | -0.0796 |
| Raw edge prob away | -0.0211 |
| Raw ev away | -0.0894 |
| Market p home draw | 73.0% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:34Z |
| Market reference home draw last update utc | 2026-10-23T14:33:48Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.1% |
| Market draw away odds | 1.79 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:34Z |
| Market reference draw away last update utc | 2026-10-23T14:33:48Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:34Z |
| Market reference home away last update utc | 2026-10-23T14:33:48Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home draw odds | 1.32 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 76.8% |
| Market over 1 5 odds | 1.28 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.94 |
| Market reference over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market over 1 5 bookmakers | 2 |
| Market p under 3 5 | 70.6% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.18 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.7% |
| Market btts yes odds | 1.71 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:34Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,443.9623 |
| Elo away rating | 1,369.6129 |
| Elo rating diff | 134.3494 |
| Elo home expectancy | 0.6843 |

</details>


---

## 2026-10-24 — Cagliari vs Bologna

The model's most likely 1X2 outcome is **Bologna win** at **42.5%**. Expected goals are 1.04 for Cagliari and 1.43 for Bologna (2.47 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 90.5%; Over 2.5 goals: 44.0%; Under 3.5 goals: 76.6%; Double Chance 1X: 57.5%; Double Chance X2: 71.8%; Double Chance 12 (either team wins): 70.6%; Under 4.5 goals: 89.8%; BTTS Yes (both teams score): 50.1%; BTTS No (at least one team does not score): 49.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Cagliari win | 28.2% | 3.55 |
| Draw | 29.4% | 3.40 |
| Bologna win | 42.5% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Cagliari expected goals | 1.04 |
| Bologna expected goals | 1.43 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.5% |
| Under 0.5 | 9.5% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.0% |
| Under 2.5 | 56.0% |
| Over 3.5 | 23.4% |
| Under 3.5 | 76.6% |
| Over 4.5 | 10.2% |
| Under 4.5 | 89.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.94% |
| 2 | 0-1 | 10.91% |
| 3 | 0-0 | 9.54% |
| 4 | 1-0 | 8.74% |
| 5 | 1-2 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Cagliari win | 28.2% | 29.2% | 3.22 | -9.3% |
| Draw | 29.4% | 31.3% | 3.01 | -11.5% |
| Bologna win | 42.5% | 39.4% | 2.57 | +9.1% |
| Over 2.5 | 44.0% | 43.5% | 2.24 | -1.4% |
| Under 2.5 | 56.0% | 56.5% | 1.76 | -1.5% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Cagliari |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0400 |
| Dc lambda away | 1.4266 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.1% |
| P btts no | 49.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.48 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.43 |
| Fair Over 2.5 odds | 2.27 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.28 |
| Fair Under 3.5 odds | 1.30 |
| Fair Over 4.5 odds | 9.80 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21639110646662854, "-10": 8.715654537879348e-07, "-11": 1.1178764953811353e-07, "-12": 1.3163026038968431e-08, "-13": 1.4261655690255522e-09, "-14": 1.313995114501682e-10, "-2": 0.1286508375754351, "-3": 0.05484453265482942, "-4": 0.018266836069654308, "-5": 0.0049740349963064805, "-6": 0.0011432830938543567, "-7": 0.00022710150315791746, "-8": 3.969263990510478e-05, "-9": 6.190946576004338e-06, "0": 0.2939300333998726, "1": 0.17456080984928982, "10": 4.117784441563892e-08, "11": 3.850361439794306e-09, "12": 3.305274165680035e-10, "13": 2.6107529065313538e-11, "14": 1.7536125600674772e-12, "2": 0.07617695800676873, "3": 0.02367491465223092, "4": 0.0057486052528162804, "5": 0.0011411745212159441, "6": 0.00019122342196874892, "7": 2.7691812800630623e-05, "8": 3.52846193481735e-06, "9": 4.0121446550721294e-07} |
| Raw goal margin distribution | {"-1": 0.2318329191390931, "-10": 9.337609418047237e-07, "-11": 1.1976489024568798e-07, "-12": 1.4102348294931249e-08, "-13": 1.527937688575242e-09, "-14": 1.4077626761264832e-10, "-2": 0.13783144654977805, "-3": 0.058758274828403206, "-4": 0.01957036958964082, "-5": 0.00532898542792735, "-6": 0.0012248685326238437, "-7": 0.0002433076168317273, "-8": 4.252513297701733e-05, "-9": 6.632736623908354e-06, "0": 0.27443336371221405, "1": 0.16786477957081664, "10": 3.959829117429322e-08, "11": 3.702664274513119e-09, "12": 3.178486166064559e-10, "13": 2.510606255476979e-11, "14": 1.6863452117487987e-12, "2": 0.07325486330649954, "3": 0.02276676152502857, "4": 0.00552809278575634, "5": 0.001097399866677612, "6": 0.0001838882255717942, "7": 2.6629574276766503e-05, "8": 3.393112608858243e-06, "9": 3.8582415990816575e-07} |
| Unadjusted home-win probability | 27.1% |
| Unadjusted draw probability | 27.4% |
| Unadjusted away-win probability | 45.5% |
| Raw p over 1 5 | 71.0% |
| Raw p under 3 5 | 76.5% |
| Raw p btts yes | 49.6% |
| P home draw | 57.5% |
| P draw away | 71.8% |
| P home away | 70.6% |
| Raw p home draw | 54.5% |
| Raw p draw away | 72.9% |
| Raw p home away | 72.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.3, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.1, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.16, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.25 |
| Reference draw odds | 3.04 |
| Reference away odds | 2.44 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:48Z |
| Market reference home last update utc | 2026-10-23T14:33:48Z |
| Market reference draw last update utc | 2026-10-23T14:33:48Z |
| Market reference away last update utc | 2026-10-23T14:33:48Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.17 |
| Reference Under 2.5 odds | 1.70 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:48Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | -1.1% |
| Draw probability edge | -1.9% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | -0.0216 |
| Raw ev home | -0.1283 |
| Raw edge prob draw | -0.0390 |
| Raw ev draw | -0.1740 |
| Raw edge prob away | 0.0606 |
| Raw ev away | 0.1689 |
| Market p home draw | 60.8% |
| Market home draw odds | 1.55 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:34Z |
| Market reference home draw last update utc | 2026-10-23T14:33:48Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.6% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:34Z |
| Market reference draw away last update utc | 2026-10-23T14:33:48Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 68.6% |
| Market home away odds | 1.42 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:34Z |
| Market reference home away last update utc | 2026-10-23T14:33:48Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.36 |
| Market reference dc home draw odds | 1.58 |
| Market reference dc home away odds | 1.40 |
| Market p over 1 5 | 71.4% |
| Market over 1 5 odds | 1.37 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference over 1 5 odds | 1.37 |
| Market reference over 1 5 opposite odds | 3.21 |
| Market reference over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.2% |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 3.60 |
| Market reference under 3 5 last update utc | 2026-10-23T14:33:44Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 51.7% |
| Market btts yes odds | 1.84 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:34Z |
| Market reference btts yes odds | 1.91 |
| Market reference btts yes opposite odds | 2.04 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,429.1686 |
| Elo away rating | 1,493.4486 |
| Elo rating diff | -4.2800 |
| Elo home expectancy | 0.4938 |

</details>


---

## 2026-10-24 — Como vs Sassuolo

The model's most likely 1X2 outcome is **Como win** at **64.9%**. Expected goals are 2.12 for Como and 0.96 for Sassuolo (3.08 combined). The most likely exact score is 2-0 at 10.5%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 59.7%; Under 3.5 goals: 62.8%; Double Chance 1X: 84.9%; Double Chance X2: 35.1%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 80.0%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Como win | 64.9% | 1.54 |
| Draw | 20.1% | 4.98 |
| Sassuolo win | 15.1% | 6.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Como expected goals | 2.12 |
| Sassuolo expected goals | 0.96 |
| Expected total goals | 3.08 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 59.7% |
| Under 2.5 | 40.3% |
| Over 3.5 | 37.2% |
| Under 3.5 | 62.8% |
| Over 4.5 | 20.0% |
| Under 4.5 | 80.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.52% |
| 2 | 2-1 | 10.12% |
| 3 | 1-0 | 9.62% |
| 4 | 1-1 | 9.45% |
| 5 | 3-0 | 7.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Como win | 64.9% | 66.2% | 1.50 | -2.7% |
| Draw | 20.1% | 19.6% | 4.79 | -3.8% |
| Sassuolo win | 15.1% | 14.3% | 6.16 | -7.3% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Como |
| Matched away-team name | Sassuolo |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1168 |
| Dc lambda away | 0.9623 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.86 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.48 |
| Fair Over 3.5 odds | 2.69 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.01 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.09916836258073185, "-10": 9.852469884525097e-09, "-11": 8.48955675395379e-10, "-12": 6.720942004463898e-11, "-13": 4.920371573906099e-12, "-14": 3.3497149251026325e-13, "-15": 2.1304086018526895e-14, "-16": 1.2642088402976574e-15, "-17": 6.390283226606317e-17, "-2": 0.037987811470054096, "-3": 0.010550346669412894, "-4": 0.0023165198565460697, "-5": 0.00041867041643385084, "-6": 6.414152200782006e-05, "-7": 8.515973718581564e-06, "-8": 9.96752145250616e-07, "-9": 1.042548290657932e-07, "0": 0.20090824843244556, "1": 0.23818967496429921, "10": 2.8085177107147676e-05, "11": 5.323575202264997e-06, "12": 9.271176559386565e-07, "13": 1.4931001233108278e-07, "14": 2.2360690237855237e-08, "15": 3.128431071103132e-09, "16": 4.0838410765087494e-10, "17": 4.541051673709676e-11, "2": 0.19746299161921263, "3": 0.12064087964213616, "4": 0.05827068436708363, "5": 0.023167154368810842, "6": 0.007807751918042693, "7": 0.002280380841666174, "8": 0.0005871466357518598, "9": 0.00013509581786532194} |
| Raw goal margin distribution | {"-1": 0.10438357211495508, "-10": 1.0370605845836272e-08, "-11": 8.936017864860058e-10, "-12": 7.074392640417544e-11, "-13": 5.1791312032512555e-12, "-14": 3.525874586911139e-13, "-15": 2.242445616108404e-14, "-16": 1.33069288647521e-15, "-17": 6.726344699665865e-17, "-2": 0.03998556953933369, "-3": 0.01110518358622585, "-4": 0.0024383443591160436, "-5": 0.0004406880628954984, "-6": 6.75146893003873e-05, "-7": 8.96382408309863e-06, "-8": 1.0491707912369971e-06, "-9": 1.0973753306920063e-07, "0": 0.20601671129126103, "1": 0.23340661420920897, "10": 2.7521201744063227e-05, "11": 5.216673072143105e-06, "12": 9.085003079107201e-07, "13": 1.4631173433926852e-07, "14": 2.1911667668134504e-08, "15": 3.065609389670294e-09, "16": 4.0018339114794415e-10, "17": 4.449863312792634e-11, "2": 0.1934977589283408, "3": 0.11821830336143738, "4": 0.05710055714133287, "5": 0.02270193728127258, "6": 0.007650965307580807, "7": 0.002234588763936239, "8": 0.000575356208516217, "9": 0.00013238297355456296} |
| Unadjusted home-win probability | 63.6% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 54.7% |
| P home draw | 84.9% |
| P draw away | 35.1% |
| P home away | 79.9% |
| Raw p home draw | 84.2% |
| Raw p draw away | 36.4% |
| Raw p home away | 79.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.7, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.71, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.17, "price": 4.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 4.91, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.2, "price": 4.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.42, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.48 |
| Reference draw odds | 4.70 |
| Reference away odds | 6.35 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:48Z |
| Market reference home last update utc | 2026-10-23T14:33:48Z |
| Market reference draw last update utc | 2026-10-23T14:33:48Z |
| Market reference away last update utc | 2026-10-23T14:33:48Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.43 |
| Reference Under 2.5 odds | 2.78 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | -1.3% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -7.8% |
| Under 2.5 probability edge | +7.8% |
| Raw edge prob home | -0.0260 |
| Raw ev home | -0.0467 |
| Raw edge prob draw | 0.0102 |
| Raw ev draw | -0.0132 |
| Raw edge prob away | 0.0158 |
| Raw ev away | -0.0241 |
| Market p home draw | 85.1% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:34Z |
| Market reference home draw last update utc | 2026-10-23T14:33:48Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.5% |
| Market draw away odds | 2.73 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:34Z |
| Market reference draw away last update utc | 2026-10-23T14:33:48Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.5% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:34Z |
| Market reference home away last update utc | 2026-10-23T14:33:48Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.71 |
| Market reference dc home draw odds | 1.13 |
| Market reference dc home away odds | 1.21 |
| Market p over 1 5 | 86.9% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:33:18Z |
| Market reference over 1 5 odds | 1.12 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-23T14:33:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.9% |
| Market under 3 5 odds | 1.76 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.76 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:34Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.52 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,552.1056 |
| Elo away rating | 1,423.0825 |
| Elo rating diff | 189.0231 |
| Elo home expectancy | 0.7480 |

</details>


---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **65.1%**. Expected goals are 1.60 for Lazio and 0.71 for Parma (2.31 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 42.2%; Under 3.5 goals: 79.1%; Double Chance 1X: 87.1%; Double Chance X2: 34.9%; Double Chance 12 (either team wins): 78.0%; Under 4.5 goals: 91.0%; BTTS Yes (both teams score): 39.8%; BTTS No (at least one team does not score): 60.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 65.1% | 1.54 |
| Draw | 22.0% | 4.54 |
| Parma win | 12.9% | 7.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.60 |
| Parma expected goals | 0.71 |
| Expected total goals | 2.31 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 68.5% |
| Under 1.5 | 31.5% |
| Over 2.5 | 42.2% |
| Under 2.5 | 57.8% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 9.0% |
| Under 4.5 | 91.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.28% |
| 2 | 2-0 | 14.18% |
| 3 | 1-1 | 10.03% |
| 4 | 2-1 | 10.02% |
| 5 | 0-0 | 8.89% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 65.1% | 71.6% | 1.37 | -10.8% |
| Draw | 22.0% | 18.5% | 5.00 | +10.2% |
| Parma win | 12.9% | 9.8% | 9.12 | +17.5% |
| Over 2.5 | 42.2% | 52.2% | 1.85 | -21.9% |
| Under 2.5 | 57.8% | 47.8% | 2.05 | +18.4% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6029 |
| Dc lambda away | 0.7067 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 39.8% |
| P btts no | 60.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.24 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.17 |
| Fair Over 2.5 odds | 2.37 |
| Fair Under 2.5 odds | 1.73 |
| Fair Over 3.5 odds | 4.77 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.15 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.09257752806055843, "-10": 7.627555224191836e-10, "-11": 4.859216159492904e-11, "-12": 2.841316255687131e-12, "-13": 1.5350597804731148e-13, "-14": 7.688769702127639e-15, "-15": 3.3682575793945934e-16, "-2": 0.028804598196175066, "-3": 0.006228271282330942, "-4": 0.001043435194900074, "-5": 0.00014225386146070917, "-6": 1.6324334058878035e-05, "-7": 1.615957536499269e-06, "-8": 1.4057278650452196e-07, "-9": 1.0902831998344176e-08, "0": 0.22045360174400103, "1": 0.2937978776054874, "10": 3.773153015157987e-06, "11": 5.451580031267386e-07, "12": 7.229576629477007e-08, "13": 8.858408395515088e-09, "14": 1.006292821133773e-09, "15": 9.997926354769358e-11, "2": 0.20355601951620217, "3": 0.09982211448316838, "4": 0.03792816588737045, "5": 0.011727286648410676, "6": 0.00305215135444761, "7": 0.0006852320269295296, "8": 0.00013519047022782503, "9": 2.378051530043761e-05} |
| Raw goal margin distribution | {"-1": 0.11440073033203232, "-10": 9.425590708413123e-10, "-11": 6.004674018986204e-11, "-12": 3.511096716065445e-12, "-13": 1.8969177906173856e-13, "-14": 9.501235210156233e-15, "-15": 4.162253357824431e-16, "-2": 0.035594675507079974, "-3": 0.007696455050502083, "-4": 0.001289403064128378, "-5": 0.0001757872129941888, "-6": 2.0172451972341548e-05, "-7": 1.9968854886699922e-06, "-8": 1.737098600257135e-07, "-9": 1.3472944994622505e-08, "0": 0.25552179545162823, "1": 0.26425546322362614, "10": 3.3937491514934364e-06, "11": 4.903404402388801e-07, "12": 6.502617162192414e-08, "13": 7.96766414059751e-09, "14": 9.051065234187656e-10, "15": 8.992599543904706e-11, "2": 0.18308774272849546, "3": 0.08978464826806094, "4": 0.03411435483291051, "5": 0.010548066551363432, "6": 0.002745246754577327, "7": 0.0006163295261617813, "8": 0.00012159659091018052, "9": 2.1389300486547474e-05} |
| Unadjusted home-win probability | 58.5% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 15.9% |
| Raw p over 1 5 | 67.5% |
| Raw p under 3 5 | 79.7% |
| Raw p btts yes | 40.9% |
| P home draw | 87.1% |
| P draw away | 34.9% |
| P home away | 78.0% |
| Raw p home draw | 84.1% |
| Raw p draw away | 41.5% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.18, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.8, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:00Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 7.17, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:00Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.12, "price": 7.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.39, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 4.90 |
| Reference away odds | 8.90 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.83 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | -6.5% |
| Draw probability edge | +3.5% |
| Away probability edge | +3.0% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.1309 |
| Raw ev home | -0.1981 |
| Raw edge prob draw | 0.0701 |
| Raw ev draw | 0.2776 |
| Raw edge prob away | 0.0607 |
| Raw ev away | 0.4517 |
| Market p home draw | 89.1% |
| Market home draw odds | 1.09 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:34:00Z |
| Market reference home draw last update utc | 2026-10-23T14:34:00Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 29.9% |
| Market draw away odds | 3.25 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:34:00Z |
| Market reference draw away last update utc | 2026-10-23T14:34:00Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.20 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:34:00Z |
| Market reference home away last update utc | 2026-10-23T14:34:00Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.25 |
| Market reference dc home draw odds | 1.09 |
| Market reference dc home away odds | 1.20 |
| Market p over 1 5 | 77.3% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.97 |
| Market reference over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.09 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 43.5% |
| Market btts yes odds | 2.19 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:34:00Z |
| Market reference btts yes odds | 2.26 |
| Market reference btts yes opposite odds | 1.75 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,525.7636 |
| Elo away rating | 1,403.2770 |
| Elo rating diff | 182.4866 |
| Elo home expectancy | 0.7409 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **36.3%**. Expected goals are 1.20 for Napoli and 1.06 for AS Roma (2.26 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 39.7%; Under 3.5 goals: 80.7%; Double Chance 1X: 64.9%; Double Chance X2: 63.7%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 46.0%; BTTS No (at least one team does not score): 54.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 36.3% | 2.75 |
| Draw | 28.6% | 3.50 |
| AS Roma win | 35.1% | 2.85 |

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
| 1 | 1-1 | 13.30% |
| 2 | 0-1 | 11.70% |
| 3 | 1-0 | 11.29% |
| 4 | 0-0 | 10.52% |
| 5 | 1-2 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 36.3% | 33.9% | 2.80 | +1.7% |
| Draw | 28.6% | 27.7% | 3.44 | -1.8% |
| AS Roma win | 35.1% | 38.4% | 2.60 | -8.7% |
| Over 2.5 | 39.7% | 50.8% | 1.92 | -23.8% |
| Under 2.5 | 60.3% | 49.2% | 1.97 | +18.9% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Napoli |
| Matched away-team name | Roma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2023 |
| Dc lambda away | 1.0610 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.0% |
| P btts no | 54.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.50 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 2.98 |
| Fair Over 2.5 odds | 2.52 |
| Fair Under 2.5 odds | 1.66 |
| Fair Over 3.5 odds | 5.18 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.49 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2131911079833449, "-10": 6.427791614821728e-08, "-11": 6.140370340534711e-09, "-12": 5.3638767728062e-10, "-13": 3.986680159933672e-11, "-2": 0.09697656216078536, "-3": 0.031175604159687613, "-4": 0.007792291373259395, "-5": 0.0015880020929185854, "-6": 0.0002727192529271699, "-7": 4.043262207771281e-05, "-8": 5.270469990495891e-06, "-9": 6.127643461608439e-07, "0": 0.28560890818400547, "1": 0.20534424261354353, "10": 1.902096211467904e-07, "11": 2.0590086800201394e-08, "12": 2.038146157820972e-09, "13": 1.7165673499004076e-10, "2": 0.1055587194618729, "3": 0.038453433841717184, "4": 0.010891265701916114, "5": 0.00251511102218326, "6": 0.0004894572985680416, "7": 8.222877817713407e-05, "8": 1.2146025705895907e-05, "9": 1.6001889212040643e-06} |
| Raw goal margin distribution | {"-1": 0.19293292958007635, "-10": 5.816999961718331e-08, "-11": 5.556890480622313e-09, "-12": 4.85418209733622e-10, "-13": 3.607851611779511e-11, "-2": 0.08776150382288163, "-3": 0.0282131872142962, "-4": 0.007051840093170962, "-5": 0.0014371044780629896, "-6": 0.0002468044981699671, "-7": 3.6590570319033326e-05, "-8": 4.769651160167939e-06, "-9": 5.545372955060935e-07, "0": 0.29441529619975865, "1": 0.21921906179126222, "10": 2.030618154215571e-07, "11": 2.1981329756761816e-08, "12": 2.1758608024470147e-09, "13": 1.8325533706580843e-10, "2": 0.11269117239322389, "3": 0.04105167781742146, "4": 0.011627173075345481, "5": 0.0026850535060850625, "6": 0.0005225292339016613, "7": 8.778486007108647e-05, "8": 1.2966715432826253e-05, "9": 1.708311416625958e-06} |
| Unadjusted home-win probability | 38.8% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 31.8% |
| Raw p over 1 5 | 66.5% |
| Raw p under 3 5 | 80.7% |
| Raw p btts yes | 46.2% |
| P home draw | 64.9% |
| P draw away | 63.7% |
| P home away | 71.4% |
| Raw p home draw | 68.2% |
| Raw p draw away | 61.2% |
| Raw p home away | 70.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.87, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.36, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.23, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.87, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.86 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.53 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | +2.5% |
| Draw probability edge | +0.9% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | 0.0491 |
| Raw ev home | 0.0861 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | 0.0128 |
| Raw edge prob away | -0.0667 |
| Raw ev away | -0.1740 |
| Market p home draw | 61.9% |
| Market home draw odds | 1.54 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:35Z |
| Market reference home draw last update utc | 2026-10-23T14:33:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 66.1% |
| Market draw away odds | 1.47 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:35Z |
| Market reference draw away last update utc | 2026-10-23T14:33:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.0% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:35Z |
| Market reference home away last update utc | 2026-10-23T14:33:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.46 |
| Market reference dc home draw odds | 1.56 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 77.2% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 3.92 |
| Market reference over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 71.9% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.26 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.6% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:35Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,562.3912 |
| Elo away rating | 1,591.2548 |
| Elo rating diff | 31.1364 |
| Elo home expectancy | 0.5447 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **58.4%**. Expected goals are 2.25 for Atalanta BC and 1.11 for Frosinone (3.35 combined). The most likely exact score is 1-1 at 9.7%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 64.3%; Under 3.5 goals: 57.4%; Double Chance 1X: 79.9%; Double Chance X2: 41.6%; Double Chance 12 (either team wins): 78.5%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 58.4% | 1.71 |
| Draw | 21.5% | 4.65 |
| Frosinone win | 20.1% | 4.99 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.25 |
| Frosinone expected goals | 1.11 |
| Expected total goals | 3.35 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.3% |
| Under 2.5 | 35.7% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.70% |
| 2 | 2-1 | 9.08% |
| 3 | 2-0 | 8.20% |
| 4 | 1-0 | 7.03% |
| 5 | 3-1 | 6.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 58.4% | 54.0% | 1.85 | +8.1% |
| Draw | 21.5% | 23.1% | 4.18 | -10.0% |
| Frosinone win | 20.1% | 22.8% | 3.93 | -21.2% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2476 |
| Dc lambda away | 1.1073 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.46 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.55 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.80 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12590587858421698, "-10": 3.8705954611841175e-08, "-11": 3.825190615103654e-09, "-12": 3.474916557316315e-10, "-13": 2.9202875505227764e-11, "-14": 2.28286466983005e-12, "-15": 1.6672875321323415e-13, "-16": 1.1335358245924691e-14, "-17": 6.440313834980295e-16, "-2": 0.05303494748904995, "-3": 0.016505675931732314, "-4": 0.00409643457950831, "-5": 0.0008411472707183488, "-6": 0.00014688521306554443, "-7": 2.22768276460795e-05, "-8": 2.9829296738797363e-06, "-9": 3.5732515651579435e-07, "0": 0.2152390289486115, "1": 0.207684319794618, "10": 3.6850860349516166e-05, "11": 7.3924861666727194e-06, "12": 1.363168084653754e-06, "13": 2.3254030428849803e-07, "14": 3.689949109400933e-08, "15": 5.470390162334724e-09, "16": 7.549368772644685e-10, "17": 8.706628443934825e-11, "2": 0.1751827219255266, "3": 0.11067003086093354, "4": 0.055753268253302374, "5": 0.023238277717921065, "6": 0.00823716120301118, "7": 0.002535831677579733, "8": 0.0006892514409058752, "9": 0.00016759684973142994} |
| Raw goal margin distribution | {"-1": 0.10849249523746075, "-10": 3.335273653308955e-08, "-11": 3.2961485139386956e-09, "-12": 2.9943190285038307e-10, "-13": 2.5163978579060927e-11, "-14": 1.9671336009433276e-12, "-15": 1.4366937165555124e-13, "-16": 9.767624151784907e-15, "-17": 5.549587723197394e-16, "-2": 0.04569996137254242, "-3": 0.014222862248776827, "-4": 0.003529878144733323, "-5": 0.0007248125924586757, "-6": 0.0001265702877273329, "-7": 1.9195836163292406e-05, "-8": 2.5703762769155235e-06, "-9": 3.0790538358845474e-07, "0": 0.19923209099460015, "1": 0.2232355989814358, "10": 3.9610231004635846e-05, "11": 7.946031164081786e-06, "12": 1.465241305607431e-06, "13": 2.499527849117545e-07, "14": 3.96625031905504e-08, "15": 5.880009746323623e-09, "16": 8.114661046918169e-10, "17": 9.358575638799693e-11, "2": 0.1883003006626438, "3": 0.11895693739886619, "4": 0.05992804004658013, "5": 0.024978346226557514, "6": 0.00885395496819061, "7": 0.002725713255677768, "8": 0.0007408621816591666, "9": 0.00018014640283963796} |
| Unadjusted home-win probability | 62.8% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 17.3% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.8% |
| Raw p btts yes | 60.2% |
| P home draw | 79.9% |
| P draw away | 41.6% |
| P home away | 78.5% |
| Raw p home draw | 82.7% |
| Raw p draw away | 37.2% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.03, "price": 1.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.80 |
| Reference draw odds | 4.05 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.92 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | +4.4% |
| Draw probability edge | -1.6% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | 0.0875 |
| Raw ev home | 0.1617 |
| Raw edge prob draw | -0.0320 |
| Raw ev draw | -0.1672 |
| Raw edge prob away | -0.0555 |
| Raw ev away | -0.3208 |
| Market p home draw | 75.7% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:34:00Z |
| Market reference home draw last update utc | 2026-10-23T14:34:00Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.5% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:34:00Z |
| Market reference draw away last update utc | 2026-10-23T14:34:00Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:34:00Z |
| Market reference home away last update utc | 2026-10-23T14:34:00Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.04 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 87.8% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:33:44Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.7% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.83 |
| Market reference under 3 5 opposite odds | 2.03 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.5% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:34:00Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.96 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,513.0173 |
| Elo away rating | 1,441.1854 |
| Elo rating diff | 131.8319 |
| Elo home expectancy | 0.6811 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **47.2%**. Expected goals are 1.40 for Genoa and 0.86 for Venezia (2.26 combined). The most likely exact score is 1-0 at 13.6%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 39.0%; Under 3.5 goals: 80.9%; Double Chance 1X: 75.9%; Double Chance X2: 52.8%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 92.2%; BTTS Yes (both teams score): 44.0%; BTTS No (at least one team does not score): 56.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 47.2% | 2.12 |
| Draw | 28.7% | 3.48 |
| Venezia win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.40 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.26 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 66.1% |
| Under 1.5 | 33.9% |
| Over 2.5 | 39.0% |
| Under 2.5 | 61.0% |
| Over 3.5 | 19.1% |
| Under 3.5 | 80.9% |
| Over 4.5 | 7.8% |
| Under 4.5 | 92.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.64% |
| 2 | 1-1 | 13.23% |
| 3 | 0-0 | 11.09% |
| 4 | 2-0 | 9.82% |
| 5 | 0-1 | 9.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 47.2% | 45.2% | 2.16 | +1.9% |
| Draw | 28.7% | 29.2% | 3.22 | -7.5% |
| Venezia win | 24.1% | 25.5% | 3.85 | -7.2% |
| Over 2.5 | 39.0% | 48.0% | 2.02 | -21.2% |
| Under 2.5 | 61.0% | 52.0% | 1.87 | +14.1% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Venezia |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3977 |
| Dc lambda away | 0.8591 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.0% |
| P btts no | 56.0% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.02 |
| Fair Over 1.5 odds | 1.51 |
| Fair Under 1.5 odds | 2.95 |
| Fair Over 2.5 odds | 2.56 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.25 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.83 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.16127416553549803, "-10": 7.486585899257622e-09, "-11": 5.794431513624823e-10, "-12": 4.116265129337412e-11, "-13": 2.6938965572071993e-12, "-14": 1.5224410547955137e-13, "-2": 0.060197961075205406, "-3": 0.015748213035842333, "-4": 0.003197401088604646, "-5": 0.0005287652173409277, "-6": 7.364496417812425e-05, "-7": 8.851214668665907e-06, "-8": 9.350751508618304e-07, "-9": 8.809132045540842e-08, "0": 0.2872105180312323, "1": 0.23945011889670426, "10": 8.786868968769205e-07, "11": 1.1065084450883627e-07, "12": 1.2789124030091144e-08, "13": 1.3617956262521877e-09, "14": 1.252175110480231e-10, "2": 0.14387443661989374, "3": 0.06123880337492861, "4": 0.020229544018483776, "5": 0.005443088741010777, "6": 0.0012334431899154647, "7": 0.00024119734922258443, "8": 4.145813231156158e-05, "9": 6.354624571020204e-06} |
| Raw goal margin distribution | {"-1": 0.1516506012043474, "-10": 7.039845773317657e-09, "-11": 5.44866575350659e-10, "-12": 3.8706390419556015e-11, "-13": 2.5331461559655177e-12, "-14": 1.4315938358217804e-13, "-2": 0.0566058237413196, "-3": 0.014808484464016392, "-4": 0.0030066055264852745, "-5": 0.0004972126988810804, "-6": 6.925041624739899e-05, "-7": 8.32304431050658e-06, "-8": 8.792772749968421e-07, "-9": 8.283472844884781e-08, "0": 0.2820092385704023, "1": 0.24939035688887748, "10": 9.151636249562605e-07, "11": 1.152442676965995e-07, "12": 1.3320036009405584e-08, "13": 1.4183275364638788e-09, "14": 1.304156369305242e-10, "2": 0.1498470631843789, "3": 0.06378099580610168, "4": 0.021069328450178372, "5": 0.005669046438369472, "6": 0.0012846468348085126, "7": 0.00025121011958745564, "8": 4.3179174271309786e-05, "9": 6.618422646702519e-06} |
| Unadjusted home-win probability | 49.1% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 66.3% |
| Raw p under 3 5 | 80.8% |
| Raw p btts yes | 43.8% |
| P home draw | 75.9% |
| P draw away | 52.8% |
| P home away | 71.3% |
| Raw p home draw | 77.3% |
| Raw p draw away | 50.9% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 5.03, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.81, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.28, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 5.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.14 |
| Reference draw odds | 3.25 |
| Reference away odds | 3.70 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.98 |
| Reference Under 2.5 odds | 1.84 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:42Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:42Z |
| Home probability edge | +2.0% |
| Draw probability edge | -0.5% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -9.0% |
| Under 2.5 probability edge | +9.0% |
| Raw edge prob home | 0.0392 |
| Raw ev home | 0.0613 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.0919 |
| Raw edge prob away | -0.0288 |
| Raw ev away | -0.1274 |
| Market p home draw | 73.9% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:34Z |
| Market reference home draw last update utc | 2026-10-23T14:33:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.5% |
| Market draw away odds | 1.75 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:34Z |
| Market reference draw away last update utc | 2026-10-23T14:33:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.6% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:34Z |
| Market reference home away last update utc | 2026-10-23T14:33:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.73 |
| Market reference dc home draw odds | 1.30 |
| Market reference dc home away odds | 1.36 |
| Market p over 1 5 | 74.8% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference over 1 5 odds | 1.31 |
| Market reference over 1 5 opposite odds | 3.61 |
| Market reference over 1 5 last update utc | 2026-10-23T14:34:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.6% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.33 |
| Market reference under 3 5 opposite odds | 3.44 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.6% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:34Z |
| Market reference btts yes odds | 1.84 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,364.9563 |
| Elo rating diff | 91.2019 |
| Elo home expectancy | 0.6283 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **70.6%**. Expected goals are 2.41 for Inter Milan and 0.94 for Fiorentina (3.34 combined). The most likely exact score is 2-0 at 10.4%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 65.2%; Under 3.5 goals: 56.9%; Double Chance 1X: 87.9%; Double Chance X2: 29.4%; Double Chance 12 (either team wins): 82.7%; Under 4.5 goals: 75.3%; BTTS Yes (both teams score): 55.4%; BTTS No (at least one team does not score): 44.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 70.6% | 1.42 |
| Draw | 17.3% | 5.78 |
| Fiorentina win | 12.1% | 8.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.41 |
| Fiorentina expected goals | 0.94 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 85.0% |
| Under 1.5 | 15.0% |
| Over 2.5 | 65.2% |
| Under 2.5 | 34.8% |
| Over 3.5 | 43.1% |
| Under 3.5 | 56.9% |
| Over 4.5 | 24.7% |
| Under 4.5 | 75.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.37% |
| 2 | 2-1 | 9.73% |
| 3 | 1-0 | 8.35% |
| 4 | 3-0 | 8.32% |
| 5 | 1-1 | 8.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 70.6% | 71.7% | 1.35 | -4.7% |
| Draw | 17.3% | 16.8% | 5.77 | -0.1% |
| Fiorentina win | 12.1% | 11.5% | 8.07 | -2.5% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4051 |
| Dc lambda away | 0.9382 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 55.4% |
| P btts no | 44.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.11 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.69 |
| Fair Over 2.5 odds | 1.53 |
| Fair Under 2.5 odds | 2.87 |
| Fair Over 3.5 odds | 2.32 |
| Fair Under 3.5 odds | 1.76 |
| Fair Over 4.5 odds | 4.05 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.08117102673378755, "-10": 6.030845384609856e-09, "-11": 5.058745335818746e-10, "-12": 3.8995595448497345e-11, "-13": 2.780306805620474e-12, "-14": 1.8436626649919888e-13, "-15": 1.1425380394623992e-14, "-16": 6.643243201764559e-16, "-17": 3.6160320580132e-17, "-18": 1.6748740315512184e-18, "-2": 0.029727272726447537, "-3": 0.007945373843300678, "-4": 0.0016861297873580993, "-5": 0.00029528152040023055, "-6": 4.390425185425813e-05, "-7": 5.663270029679892e-06, "-8": 6.444772994950634e-07, "-9": 6.557472666138988e-08, "0": 0.17313923863351766, "1": 0.22517674495141196, "10": 7.844932352896534e-05, "11": 1.6868380809533512e-05, "12": 3.3332332646872805e-06, "13": 6.092035775445029e-07, "14": 1.0355492409036536e-07, "15": 1.6450516308840327e-08, "16": 2.451932938093398e-09, "17": 3.421214305429616e-10, "18": 4.062091740222832e-11, "2": 0.20740036013649407, "3": 0.14209812461913493, "4": 0.07730090561692439, "5": 0.0347015937142219, "6": 0.013226328489086775, "7": 0.004373403664751123, "8": 0.0012757908729262174, "9": 0.00033275755633811277} |
| Raw goal margin distribution | {"-1": 0.08487225535810665, "-10": 6.305839289018231e-09, "-11": 5.289413516245735e-10, "-12": 4.07737128372265e-11, "-13": 2.907082966369322e-12, "-14": 1.9277298168297564e-13, "-15": 1.1946353784538183e-14, "-16": 6.946161162594658e-16, "-17": 3.7809155379705004e-17, "-18": 1.7512447756103882e-18, "-2": 0.031082774032337383, "-3": 0.008307666231152167, "-4": 0.0017630137702816411, "-5": 0.00030874573860116745, "-6": 4.590619368290147e-05, "-7": 5.921503268614328e-06, "-8": 6.738641130490938e-07, "-9": 6.856479670383289e-08, "0": 0.17835636394632673, "1": 0.22175475670855244, "10": 7.725713708522611e-05, "11": 1.6612033730625534e-05, "12": 3.2825784555286832e-06, "13": 5.999455723259131e-07, "14": 1.0198121037137584e-07, "15": 1.6200519474531497e-08, "16": 2.4146711609580812e-09, "17": 3.3692224572837997e-10, "18": 4.000360542449906e-11, "2": 0.20424851781767445, "3": 0.1399386737758252, "4": 0.07612617156416693, "5": 0.03417423710053526, "6": 0.013025329311327015, "7": 0.004306941491113758, "8": 0.0012564028079266852, "9": 0.0003277006733737668} |
| Unadjusted home-win probability | 69.5% |
| Unadjusted draw probability | 17.8% |
| Unadjusted away-win probability | 12.6% |
| Raw p over 1 5 | 84.9% |
| Raw p under 3 5 | 57.1% |
| Raw p btts yes | 55.6% |
| P home draw | 87.9% |
| P draw away | 29.4% |
| P home away | 82.7% |
| Raw p home draw | 87.4% |
| Raw p draw away | 30.5% |
| Raw p home away | 82.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.51, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:18Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.7, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.32, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.07, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:34:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.37 |
| Reference draw odds | 5.40 |
| Reference away odds | 7.70 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.88 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | -1.1% |
| Draw probability edge | +0.5% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.8% |
| Under 2.5 probability edge | +3.8% |
| Raw edge prob home | -0.0215 |
| Raw ev home | -0.0614 |
| Raw edge prob draw | 0.0104 |
| Raw ev draw | 0.0291 |
| Raw edge prob away | 0.0110 |
| Raw ev away | 0.0199 |
| Market p home draw | 87.6% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:33:34Z |
| Market reference home draw last update utc | 2026-10-23T14:33:49Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 30.0% |
| Market draw away odds | 3.41 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:33:34Z |
| Market reference draw away last update utc | 2026-10-23T14:33:49Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.3% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:33:34Z |
| Market reference home away last update utc | 2026-10-23T14:33:49Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.18 |
| Market reference dc home draw odds | 1.09 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 87.6% |
| Market over 1 5 odds | 1.11 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:33:18Z |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 5.20 |
| Market reference over 1 5 last update utc | 2026-10-23T14:33:44Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 53.7% |
| Market under 3 5 odds | 1.80 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market reference under 3 5 odds | 1.80 |
| Market reference under 3 5 opposite odds | 2.07 |
| Market reference under 3 5 last update utc | 2026-10-23T14:34:05Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 56.8% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:33:34Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-23T14:34:06Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,671.4331 |
| Elo away rating | 1,448.7633 |
| Elo rating diff | 282.6699 |
| Elo home expectancy | 0.8358 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **62.4%**. Expected goals are 0.62 for Lecce and 1.48 for Juventus (2.11 combined). The most likely exact score is 0-1 at 19.1%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 36.5%; Under 3.5 goals: 83.3%; Double Chance 1X: 37.6%; Double Chance X2: 86.4%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 93.4%; BTTS Yes (both teams score): 35.4%; BTTS No (at least one team does not score): 64.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.6% | 7.37 |
| Draw | 24.0% | 4.17 |
| Juventus win | 62.4% | 1.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.62 |
| Juventus expected goals | 1.48 |
| Expected total goals | 2.11 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 63.4% |
| Under 1.5 | 36.6% |
| Over 2.5 | 36.5% |
| Under 2.5 | 63.5% |
| Over 3.5 | 16.7% |
| Under 3.5 | 83.3% |
| Over 4.5 | 6.6% |
| Under 4.5 | 93.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.09% |
| 2 | 0-2 | 14.46% |
| 3 | 0-0 | 11.13% |
| 4 | 1-1 | 10.32% |
| 5 | 1-2 | 9.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.6% | 11.9% | 7.83 | +6.3% |
| Draw | 24.0% | 21.0% | 4.26 | +2.3% |
| Juventus win | 62.4% | 67.1% | 1.48 | -7.6% |
| Over 2.5 | 36.5% | 51.3% | 1.92 | -30.0% |
| Under 2.5 | 63.5% | 48.7% | 2.02 | +28.3% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6239 |
| Dc lambda away | 1.4832 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 35.4% |
| P btts no | 64.6% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.99 |
| Fair Over 1.5 odds | 1.58 |
| Fair Under 1.5 odds | 2.73 |
| Fair Over 2.5 odds | 2.74 |
| Fair Under 2.5 odds | 1.57 |
| Fair Over 3.5 odds | 5.98 |
| Fair Under 3.5 odds | 1.20 |
| Fair Over 4.5 odds | 15.19 |
| Fair Under 4.5 odds | 1.07 |
| Goal margin distribution | {"-1": 0.29610625891154463, "-10": 2.0294141834412596e-06, "-11": 2.717438023197681e-07, "-12": 3.339029773912587e-08, "-13": 3.790232884962939e-09, "-14": 3.9912337581371887e-10, "-15": 3.7172037462146085e-11, "-2": 0.19466707433503103, "-3": 0.08962865111164166, "-4": 0.0318057309387898, "-5": 0.009158319429238528, "-6": 0.0022158900703448986, "-7": 0.0004619756059703483, "-8": 8.457392567711863e-05, "-9": 1.3797040538818017e-05, "0": 0.2400812995598045, "1": 0.10089179245958932, "10": 2.905691297896479e-10, "11": 1.636594907974473e-11, "12": 8.458719151155621e-13, "13": 4.038805840179307e-14, "14": 1.7889450910229504e-15, "15": 7.008240208853083e-17, "2": 0.028441280999485865, "3": 0.005508156587589957, "4": 0.00082218124271166, "5": 9.958197541068908e-05, "6": 1.0134817385256508e-05, "7": 8.88770285805061e-07, "8": 6.843995867902977e-08, "9": 4.6963662192128815e-09} |
| Raw goal margin distribution | {"-1": 0.27390988618879086, "-10": 1.8772875995923134e-06, "-11": 2.5137365971096313e-07, "-12": 3.088733310519437e-08, "-13": 3.506113859144551e-09, "-14": 3.6920475388222005e-10, "-15": 3.4385590456916e-11, "-2": 0.18007466769468666, "-3": 0.08291001249176046, "-4": 0.029421546756962385, "-5": 0.0084718041481612, "-6": 0.002049785098113571, "-7": 0.0004273455283197402, "-8": 7.823419350172892e-05, "-9": 1.2762802845240485e-05, "0": 0.2705429512379711, "1": 0.1130224817232606, "10": 3.2550560714983953e-10, "11": 1.8333703224572407e-11, "12": 9.475750280148924e-13, "13": 4.524410243165206e-14, "14": 2.0040382763052087e-15, "15": 7.850873511188503e-17, "2": 0.03186090844047629, "3": 0.0061704278620988385, "4": 0.0009210359159275118, "5": 0.00011155517928109775, "6": 1.1353373597287754e-05, "7": 9.956312692512997e-07, "8": 7.666881309537238e-08, "9": 5.261032163635394e-09} |
| Unadjusted home-win probability | 15.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 57.7% |
| Raw p over 1 5 | 62.6% |
| Raw p under 3 5 | 83.7% |
| Raw p btts yes | 36.3% |
| P home draw | 37.6% |
| P draw away | 86.4% |
| P home away | 76.0% |
| Raw p home draw | 42.3% |
| Raw p draw away | 84.8% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 7.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.46 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.86 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | +1.6% |
| Draw probability edge | +3.0% |
| Away probability edge | -4.7% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | 0.0326 |
| Raw ev home | 0.1909 |
| Raw edge prob draw | 0.0609 |
| Raw ev draw | 0.1525 |
| Raw edge prob away | -0.0936 |
| Raw ev away | -0.1455 |
| Elo home rating | 1,374.5856 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -122.9499 |
| Elo home expectancy | 0.3301 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **54.8%**. Expected goals are 1.04 for Udinese and 1.69 for AC Milan (2.74 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 93.3%; Over 2.5 goals: 51.8%; Under 3.5 goals: 70.4%; Double Chance 1X: 45.2%; Double Chance X2: 79.1%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 85.6%; BTTS Yes (both teams score): 53.1%; BTTS No (at least one team does not score): 46.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 20.9% | 4.79 |
| Draw | 24.4% | 4.10 |
| AC Milan win | 54.8% | 1.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.04 |
| AC Milan expected goals | 1.69 |
| Expected total goals | 2.74 |
| Over 0.5 | 93.3% |
| Under 0.5 | 6.7% |
| Over 1.5 | 76.4% |
| Under 1.5 | 23.6% |
| Over 2.5 | 51.8% |
| Under 2.5 | 48.2% |
| Over 3.5 | 29.6% |
| Under 3.5 | 70.4% |
| Over 4.5 | 14.4% |
| Under 4.5 | 85.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.61% |
| 2 | 0-1 | 11.10% |
| 3 | 1-2 | 10.17% |
| 4 | 0-2 | 9.74% |
| 5 | 0-0 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 20.9% | 18.7% | 5.19 | +8.2% |
| Draw | 24.4% | 23.9% | 4.02 | -2.0% |
| AC Milan win | 54.8% | 57.4% | 1.68 | -8.0% |
| Over 2.5 | 51.8% | 50.7% | 1.90 | -1.5% |
| Under 2.5 | 48.2% | 49.3% | 1.99 | -4.1% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Udinese |
| Matched away-team name | Milan |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0448 |
| Dc lambda away | 1.6924 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.1% |
| P btts no | 46.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.86 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.23 |
| Fair Over 2.5 odds | 1.93 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.38 |
| Fair Under 3.5 odds | 1.42 |
| Fair Over 4.5 odds | 6.94 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.24756914513331735, "-10": 4.236742444234491e-06, "-11": 6.433131691778101e-07, "-12": 8.971966443475917e-08, "-13": 1.1565758484540204e-08, "-14": 1.3785566893658403e-09, "-15": 1.3913518909684344e-10, "-2": 0.16905602415056317, "-3": 0.08395377930273197, "-4": 0.032777898474840854, "-5": 0.010499964494658428, "-6": 0.002845448771051289, "-7": 0.0006673646800533515, "-8": 0.00013785817308910322, "-9": 2.5431349871717956e-05, "0": 0.24389726454108873, "1": 0.13073310927242354, "10": 2.9438329827785372e-08, "11": 2.7595214804543566e-09, "12": 2.375905766720613e-10, "13": 1.8908014388867118e-11, "14": 1.3913188492018882e-12, "15": 8.669005039340585e-14, "2": 0.05567623803601212, "3": 0.017069064406687165, "4": 0.004114156476152321, "5": 0.000813612784519184, "6": 0.0001361165517685057, "7": 1.970850217311991e-05, "8": 2.513351060171582e-06, "9": 2.8623338200640016e-07} |
| Raw goal margin distribution | {"-1": 0.23577440926785515, "-10": 4.034894762315856e-06, "-11": 6.126643219430723e-07, "-12": 8.544522327458944e-08, "-13": 1.1014740439317244e-08, "-14": 1.3128792317897757e-09, "-15": 1.3250648419864347e-10, "-2": 0.16100182519031986, "-3": 0.07995403752857108, "-4": 0.031216287658890854, "-5": 0.009999723207544331, "-6": 0.0027098853644919583, "-7": 0.0006355699662051087, "-8": 0.00013129030802819052, "-9": 2.4219744708733943e-05, "0": 0.2486884961180322, "1": 0.14408108643750037, "10": 3.2444011835244256e-08, "11": 3.0412712981756538e-09, "12": 2.618488048263967e-10, "13": 2.0838540983883087e-11, "14": 1.533373852191136e-12, "15": 9.554118855978481e-14, "2": 0.06136083590167945, "3": 0.01881183242618646, "4": 0.0045342158398656105, "5": 0.0008966834383835105, "6": 0.00015001418363014046, "7": 2.172075934675207e-05, "8": 2.769966639390186e-06, "9": 3.1545808773066035e-07} |
| Unadjusted home-win probability | 23.0% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 76.2% |
| Raw p under 3 5 | 70.6% |
| Raw p btts yes | 53.3% |
| P home draw | 45.2% |
| P draw away | 79.1% |
| P home away | 75.6% |
| Raw p home draw | 47.9% |
| Raw p draw away | 77.0% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.95 |
| Reference draw odds | 3.92 |
| Reference away odds | 1.70 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:42Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:42Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.5% |
| Away probability edge | -2.6% |
| Over 2.5 probability edge | +1.1% |
| Under 2.5 probability edge | -1.1% |
| Raw edge prob home | 0.0426 |
| Raw ev home | 0.1930 |
| Raw edge prob draw | 0.0096 |
| Raw ev draw | -0.0003 |
| Raw edge prob away | -0.0522 |
| Raw ev away | -0.1240 |
| Elo home rating | 1,386.6713 |
| Elo away rating | 1,580.4486 |
| Elo rating diff | -133.7773 |
| Elo home expectancy | 0.3165 |

</details>


---

## 2026-10-27 — AS Roma vs Cagliari

The model's most likely 1X2 outcome is **AS Roma win** at **69.0%**. Expected goals are 1.92 for AS Roma and 0.71 for Cagliari (2.63 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.4%; Double Chance 1X: 88.8%; Double Chance X2: 31.0%; Double Chance 12 (either team wins): 80.1%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Roma win | 69.0% | 1.45 |
| Draw | 19.9% | 5.04 |
| Cagliari win | 11.2% | 8.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Roma expected goals | 1.92 |
| Cagliari expected goals | 0.71 |
| Expected total goals | 2.63 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 74.7% |
| Under 1.5 | 25.3% |
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.15% |
| 2 | 2-0 | 13.93% |
| 3 | 2-1 | 9.89% |
| 4 | 1-1 | 9.34% |
| 5 | 3-0 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Roma win | 69.0% | 72.2% | 1.34 | -7.6% |
| Draw | 19.9% | 18.1% | 4.80 | -4.7% |
| Cagliari win | 11.2% | 9.7% | 9.84 | +10.1% |
| Over 2.5 | 49.8% | 55.7% | 1.78 | -11.3% |
| Under 2.5 | 50.2% | 44.3% | 2.21 | +10.9% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Roma |
| Matched away-team name | Cagliari |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9214 |
| Dc lambda away | 0.7103 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.44 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.95 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.63 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.66 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.08091088257699884, "-10": 6.479911917713711e-10, "-11": 4.14185660261264e-11, "-12": 2.4305598023806823e-12, "-13": 1.3182136204670633e-13, "-14": 6.644569506638651e-15, "-15": 3.118972885119746e-16, "-16": 1.2758210900756483e-17, "-2": 0.02469667355516934, "-3": 0.005283398291460724, "-4": 0.0008806546331677994, "-5": 0.00011982400520134882, "-6": 1.374902059538863e-05, "-7": 1.3625531696559467e-06, "-8": 1.1876136715057638e-07, "-9": 9.234697628682646e-09, "0": 0.19853472122914992, "1": 0.26571802126840266, "10": 1.6134077863158756e-05, "11": 2.789584437517635e-06, "12": 4.4281280429686333e-07, "13": 6.49634469741818e-08, "14": 8.857670511903839e-09, "15": 1.1246921875151437e-09, "16": 1.2444609196610257e-10, "2": 0.21451529067995698, "3": 0.12413737312905425, "4": 0.05597115005118775, "5": 0.0206002193614702, "6": 0.006393949208201051, "7": 0.0017140373628001138, "8": 0.000404121002074531, "9": 8.500183853475743e-05} |
| Raw goal margin distribution | {"-1": 0.09158493454807971, "-10": 7.334764990313428e-10, "-11": 4.688265085933519e-11, "-12": 2.7512079132790143e-12, "-13": 1.4921170589873604e-13, "-14": 7.521144795158397e-15, "-15": 3.5304389031857053e-16, "-16": 1.444131954912758e-17, "-2": 0.027954746741923026, "-3": 0.005980403022478247, "-4": 0.0009968337307578001, "-5": 0.0001356316149834457, "-6": 1.5562840389616893e-05, "-7": 1.5423060395177697e-06, "-8": 1.3442878993409988e-07, "-9": 1.0452971849483169e-08, "0": 0.21581271821769424, "1": 0.2533711314798354, "10": 1.5384389602401448e-05, "11": 2.659963226876669e-06, "12": 4.2223700418544694e-07, "13": 6.194484659379793e-08, "14": 8.446088786765787e-09, "15": 1.072432087055923e-09, "16": 1.1866356289717155e-10, "2": 0.2045475939488703, "3": 0.11836918903167805, "4": 0.053370386965106646, "5": 0.01964300676120226, "6": 0.0060968470929191835, "7": 0.0016343926691095695, "8": 0.0003853430605181338, "9": 8.10521315212684e-05} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 74.2% |
| Raw p under 3 5 | 72.9% |
| Raw p btts yes | 43.7% |
| P home draw | 88.8% |
| P draw away | 31.0% |
| P home away | 80.1% |
| Raw p home draw | 87.3% |
| Raw p draw away | 34.2% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.36 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.00 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | -3.2% |
| Draw probability edge | +1.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0641 |
| Raw ev home | -0.1189 |
| Raw edge prob draw | 0.0346 |
| Raw ev draw | 0.0359 |
| Raw edge prob away | 0.0295 |
| Raw ev away | 0.2464 |
| Elo home rating | 1,629.0662 |
| Elo away rating | 1,426.7784 |
| Elo rating diff | 262.2878 |
| Elo home expectancy | 0.8190 |

</details>


---

## 2026-10-27 — Sassuolo vs Lazio

The model's most likely 1X2 outcome is **Lazio win** at **43.9%**. Expected goals are 1.17 for Sassuolo and 1.67 for Lazio (2.84 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.4%; Under 3.5 goals: 68.6%; Double Chance 1X: 56.1%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sassuolo win | 29.8% | 3.36 |
| Draw | 26.3% | 3.80 |
| Lazio win | 43.9% | 2.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sassuolo expected goals | 1.17 |
| Lazio expected goals | 1.67 |
| Expected total goals | 2.84 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.4% |
| Under 2.5 | 46.6% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.42% |
| 2 | 1-2 | 8.60% |
| 3 | 0-1 | 8.47% |
| 4 | 2-1 | 7.55% |
| 5 | 0-2 | 7.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sassuolo win | 29.8% | 33.2% | 2.98 | -11.3% |
| Draw | 26.3% | 27.6% | 3.37 | -11.4% |
| Lazio win | 43.9% | 39.2% | 2.40 | +5.5% |
| Over 2.5 | 53.4% | 54.5% | 1.82 | -2.9% |
| Under 2.5 | 46.6% | 45.5% | 2.15 | +0.3% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sassuolo |
| Matched away-team name | Lazio |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1681 |
| Dc lambda away | 1.6708 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.24 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.48 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.14 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.20365241709737178, "-10": 2.9392455170405606e-06, "-11": 4.4002883153098727e-07, "-12": 6.051827335483566e-08, "-13": 7.693955957782275e-09, "-14": 9.035589929596025e-10, "-15": 8.905892489386448e-11, "-2": 0.13485004413946985, "-3": 0.0653672173282598, "-4": 0.025007214630883467, "-5": 0.007866829894437457, "-6": 0.0020964795622585193, "-7": 0.0004839802632311524, "-8": 9.846824343030703e-05, "-9": 1.7899045278104436e-05, "0": 0.2629161063667829, "1": 0.17737778117636108, "10": 1.028952015451035e-07, "11": 1.0769399387487568e-08, "12": 1.035494916152692e-09, "13": 9.203695263310557e-11, "14": 7.556490482937137e-12, "15": 5.207055029189766e-13, "2": 0.08271830222395023, "3": 0.02803248567754197, "4": 0.007497526773850852, "5": 0.0016489350727780334, "6": 0.0003072171962830537, "7": 4.958309500061787e-05, "8": 7.052665133705041e-06, "9": 8.962682913983355e-07} |
| Raw goal margin distribution | {"-1": 0.2258375110717106, "-10": 3.2594353725727997e-06, "-11": 4.879638431457326e-07, "-12": 6.711089622019461e-08, "-13": 8.532105282944527e-09, "-14": 1.001989158709039e-09, "-15": 9.876065417449112e-11, "-2": 0.14954007799380653, "-3": 0.07248806509396594, "-4": 0.027731402315615678, "-5": 0.008723811426872629, "-6": 0.002324861806706656, "-7": 0.0005367031710882913, "-8": 0.00010919498689412237, "-9": 1.9848896928310148e-05, "0": 0.2496885932292959, "1": 0.15673189820247885, "10": 9.09187168039732e-08, "11": 9.51589538051164e-09, "12": 9.149685079568292e-10, "13": 8.132431353741999e-11, "14": 6.676952937877539e-12, "15": 4.600979972560609e-13, "2": 0.07309030723952827, "3": 0.024769645118102767, "4": 0.006624852308425173, "5": 0.0014570073109223547, "6": 0.0002714586574178182, "7": 4.3811871738738044e-05, "8": 6.231770329187894e-06, "9": 7.919471631561615e-07} |
| Unadjusted home-win probability | 26.3% |
| Unadjusted draw probability | 25.0% |
| Unadjusted away-win probability | 48.7% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.3% |
| Raw p btts yes | 56.3% |
| P home draw | 56.1% |
| P draw away | 70.2% |
| P home away | 73.7% |
| Raw p home draw | 51.3% |
| Raw p draw away | 73.7% |
| Raw p home away | 75.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.88 |
| Reference draw odds | 3.44 |
| Reference away odds | 2.46 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | -3.5% |
| Draw probability edge | -1.3% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -1.1% |
| Under 2.5 probability edge | +1.1% |
| Raw edge prob home | -0.0693 |
| Raw ev home | -0.2163 |
| Raw edge prob draw | -0.0265 |
| Raw ev draw | -0.1585 |
| Raw edge prob away | 0.0957 |
| Raw ev away | 0.1696 |
| Elo home rating | 1,447.3948 |
| Elo away rating | 1,573.0190 |
| Elo rating diff | -65.6242 |
| Elo home expectancy | 0.4067 |

</details>


---

## 2026-10-27 — Torino vs Como

The model's most likely 1X2 outcome is **Como win** at **52.0%**. Expected goals are 0.94 for Torino and 1.48 for Como (2.41 combined). The most likely exact score is 0-1 at 13.5%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 43.8%; Under 3.5 goals: 77.4%; Double Chance 1X: 48.0%; Double Chance X2: 78.1%; Double Chance 12 (either team wins): 73.9%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torino win | 21.9% | 4.57 |
| Draw | 26.1% | 3.83 |
| Como win | 52.0% | 1.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torino expected goals | 0.94 |
| Como expected goals | 1.48 |
| Expected total goals | 2.41 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 70.1% |
| Under 1.5 | 29.9% |
| Over 2.5 | 43.8% |
| Under 2.5 | 56.2% |
| Over 3.5 | 22.6% |
| Under 3.5 | 77.4% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.50% |
| 2 | 1-1 | 12.30% |
| 3 | 0-2 | 10.30% |
| 4 | 1-2 | 9.64% |
| 5 | 0-0 | 9.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torino win | 21.9% | 20.2% | 4.89 | +6.9% |
| Draw | 26.1% | 25.1% | 3.55 | -7.3% |
| Como win | 52.0% | 54.7% | 1.76 | -8.4% |
| Over 2.5 | 43.8% | 54.5% | 1.82 | -20.2% |
| Under 2.5 | 56.2% | 45.5% | 2.15 | +20.7% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Torino |
| Matched away-team name | Como |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9359 |
| Dc lambda away | 1.4781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.11 |
| Fair Over 1.5 odds | 1.43 |
| Fair Under 1.5 odds | 3.34 |
| Fair Over 2.5 odds | 2.28 |
| Fair Under 2.5 odds | 1.78 |
| Fair Over 3.5 odds | 4.42 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.08 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.2563035981695189, "-10": 1.4653493448236566e-06, "-11": 1.9487597500152256e-07, "-12": 2.3794048739351465e-08, "-13": 2.684754957099195e-09, "-14": 2.8058620683759787e-10, "-15": 2.531409355026616e-11, "-2": 0.15947966855218135, "-3": 0.07090810609146439, "-4": 0.024574908186237893, "-5": 0.006954071355008722, "-6": 0.0016597412566910304, "-7": 0.00034216636529046766, "-8": 6.204446354426531e-05, "-9": 1.0037257271006962e-05, "0": 0.2611060139369082, "1": 0.14197340058792657, "10": 1.3411521389815943e-08, "11": 1.1293373337749207e-09, "12": 8.730964920531683e-11, "13": 6.237737025652746e-12, "14": 4.1277866184376635e-13, "15": 2.3579892113642768e-14, "2": 0.056495531544948976, "3": 0.015904981661513433, "4": 0.0034902593807117186, "5": 0.0006253648309014261, "6": 9.450683366900797e-05, "7": 1.2336405947839651e-05, "8": 1.416390096984205e-06, "9": 1.4508530127317928e-07} |
| Raw goal margin distribution | {"-1": 0.24321435150272733, "-10": 1.390514971976762e-06, "-11": 1.8492379436713533e-07, "-12": 2.2578903203450543e-08, "-13": 2.547646386933432e-09, "-14": 2.662568642188195e-10, "-15": 2.402132038207004e-11, "-2": 0.15133515269315295, "-3": 0.06728687838364134, "-4": 0.023319884700962138, "-5": 0.006598931762922401, "-6": 0.0015749794239776598, "-7": 0.00032469216676827504, "-8": 5.887589590245439e-05, "-9": 9.524661516532367e-06, "0": 0.27151256401436796, "1": 0.15247187090054135, "10": 1.4403259691321095e-08, "11": 1.212848149339423e-09, "12": 9.376591324062918e-11, "13": 6.698997351252654e-12, "14": 4.433022987299857e-13, "15": 2.532354829363561e-14, "2": 0.06067319199587767, "3": 0.017081103224458383, "4": 0.0037483526879086107, "5": 0.0006716085222167296, "6": 0.00010149530604132977, "7": 1.3248642965981291e-05, "8": 1.5211275289446444e-06, "9": 1.5581388650045155e-07} |
| Unadjusted home-win probability | 23.5% |
| Unadjusted draw probability | 27.2% |
| Unadjusted away-win probability | 49.4% |
| Raw p over 1 5 | 69.9% |
| Raw p under 3 5 | 77.6% |
| Raw p btts yes | 47.3% |
| P home draw | 48.0% |
| P draw away | 78.1% |
| P home away | 73.9% |
| Raw p home draw | 50.6% |
| Raw p draw away | 76.5% |
| Raw p home away | 72.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.4, "price": 3.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.35, "price": 1.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 4.60 |
| Reference draw odds | 3.75 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.0% |
| Away probability edge | -2.7% |
| Over 2.5 probability edge | -10.6% |
| Under 2.5 probability edge | +10.6% |
| Raw edge prob home | 0.0323 |
| Raw ev home | 0.1480 |
| Raw edge prob draw | 0.0208 |
| Raw ev draw | -0.0361 |
| Raw edge prob away | -0.0531 |
| Raw ev away | -0.1310 |
| Elo home rating | 1,443.9623 |
| Elo away rating | 1,579.5470 |
| Elo rating diff | -75.5848 |
| Elo home expectancy | 0.3929 |

</details>


---

## 2026-10-28 — AC Milan vs Bologna

The model's most likely 1X2 outcome is **AC Milan win** at **55.7%**. Expected goals are 1.62 for AC Milan and 1.04 for Bologna (2.66 combined). The most likely exact score is 1-0 at 12.1%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 50.4%; Under 3.5 goals: 71.9%; Double Chance 1X: 79.7%; Double Chance X2: 44.3%; Double Chance 12 (either team wins): 76.0%; Under 4.5 goals: 86.6%; BTTS Yes (both teams score): 51.8%; BTTS No (at least one team does not score): 48.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AC Milan win | 55.7% | 1.80 |
| Draw | 24.0% | 4.16 |
| Bologna win | 20.3% | 4.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AC Milan expected goals | 1.62 |
| Bologna expected goals | 1.04 |
| Expected total goals | 2.66 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 75.2% |
| Under 1.5 | 24.8% |
| Over 2.5 | 50.4% |
| Under 2.5 | 49.6% |
| Over 3.5 | 28.1% |
| Under 3.5 | 71.9% |
| Over 4.5 | 13.4% |
| Under 4.5 | 86.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.08% |
| 2 | 1-1 | 11.44% |
| 3 | 2-1 | 10.55% |
| 4 | 2-0 | 10.12% |
| 5 | 0-0 | 6.94% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AC Milan win | 55.7% | 61.0% | 1.62 | -9.8% |
| Draw | 24.0% | 22.4% | 4.03 | -3.2% |
| Bologna win | 20.3% | 16.5% | 5.26 | +6.8% |
| Over 2.5 | 50.4% | 52.5% | 1.84 | -7.3% |
| Under 2.5 | 49.6% | 47.5% | 2.00 | -0.8% |

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
| Market best home last update utc | 2026-10-23T14:33:41Z |
| Market best draw last update utc | 2026-10-23T14:33:41Z |
| Market best away last update utc | 2026-10-23T14:33:41Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Milan |
| Matched away-team name | Bologna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6166 |
| Dc lambda away | 1.0433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 51.8% |
| P btts no | 48.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.42 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.03 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.56 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.44 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.12690635663839572, "-10": 2.8910559651351536e-08, "-11": 2.707676309551916e-09, "-12": 2.3290217552751604e-10, "-13": 1.8516269360458724e-11, "-14": 1.3616735185688252e-12, "-15": 8.51326167426428e-14, "-2": 0.054410367701340126, "-3": 0.0167424735199004, "-4": 0.004043203129665754, "-5": 0.0008003125499695048, "-6": 0.00013393022807810552, "-7": 1.9389582431233004e-05, "-8": 2.4716772544791647e-06, "-9": 2.813157648596923e-07, "0": 0.24015884584431682, "1": 0.260486670961541, "10": 3.028517483667665e-06, "11": 4.3952446208143845e-07, "12": 5.858312988302037e-08, "13": 7.217141745065253e-09, "14": 8.22427182641483e-10, "15": 7.967703542100531e-11, "2": 0.1714563171000464, "3": 0.08175308880841042, "4": 0.030593053754569235, "5": 0.00938360279335332, "6": 0.0024333317150737658, "7": 0.0005458884229887479, "8": 0.00010783007524701943, "9": 1.9017566230432328e-05} |
| Raw goal margin distribution | {"-1": 0.150508316170775, "-10": 3.428732624543081e-08, "-11": 3.2112481429701604e-09, "-12": 2.762171667337203e-10, "-13": 2.195991278157921e-11, "-14": 1.6149166510081858e-12, "-15": 1.0096552400173827e-13, "-2": 0.06452957158241959, "-3": 0.019856227574116682, "-4": 0.004795155349990461, "-5": 0.0009491541440234363, "-6": 0.00015883848253433195, "-7": 2.2995644034558844e-05, "-8": 2.9313581410997005e-06, "-9": 3.33634683107086e-07, "0": 0.2560047709117436, "1": 0.2354052995022317, "10": 2.7369118836632925e-06, "11": 3.9720415349050377e-07, "12": 5.2942360486178794e-08, "13": 6.5222278275343415e-09, "14": 7.43238479473213e-10, "15": 7.200520593816073e-11, "2": 0.1549473741957612, "3": 0.07388136323880387, "4": 0.027647353145549364, "5": 0.0084800877443186, "6": 0.002199034518966967, "7": 0.0004933266920495904, "8": 9.744748575876465e-05, "9": 1.7186429761465308e-05} |
| Unadjusted home-win probability | 50.3% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 24.1% |
| Raw p over 1 5 | 74.8% |
| Raw p under 3 5 | 72.3% |
| Raw p btts yes | 52.3% |
| P home draw | 79.7% |
| P draw away | 44.3% |
| P home away | 76.0% |
| Raw p home draw | 75.9% |
| Raw p draw away | 49.7% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.76, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:41Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.60 |
| Reference draw odds | 4.15 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | -5.4% |
| Draw probability edge | +1.6% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | -2.1% |
| Under 2.5 probability edge | +2.1% |
| Raw edge prob home | -0.1072 |
| Raw ev home | -0.1849 |
| Raw edge prob draw | 0.0317 |
| Raw ev draw | 0.0317 |
| Raw edge prob away | 0.0755 |
| Raw ev away | 0.2667 |
| Elo home rating | 1,550.8302 |
| Elo away rating | 1,493.4486 |
| Elo rating diff | 117.3816 |
| Elo home expectancy | 0.6628 |

</details>


---

## 2026-10-28 — Genoa vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **55.6%**. Expected goals are 0.78 for Genoa and 1.43 for Juventus (2.21 combined). The most likely exact score is 0-1 at 16.3%. Goal-market probabilities: at least one goal: 89.5%; Over 2.5 goals: 38.9%; Under 3.5 goals: 81.4%; Double Chance 1X: 44.4%; Double Chance X2: 81.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 92.4%; BTTS Yes (both teams score): 41.2%; BTTS No (at least one team does not score): 58.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 18.5% | 5.41 |
| Draw | 25.9% | 3.86 |
| Juventus win | 55.6% | 1.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 0.78 |
| Juventus expected goals | 1.43 |
| Expected total goals | 2.21 |
| Over 0.5 | 89.5% |
| Under 0.5 | 10.5% |
| Over 1.5 | 65.7% |
| Under 1.5 | 34.3% |
| Over 2.5 | 38.9% |
| Under 2.5 | 61.1% |
| Over 3.5 | 18.6% |
| Under 3.5 | 81.4% |
| Over 4.5 | 7.6% |
| Under 4.5 | 92.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 16.26% |
| 2 | 0-2 | 11.96% |
| 3 | 1-1 | 11.77% |
| 4 | 0-0 | 10.54% |
| 5 | 1-2 | 9.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 18.5% | 16.9% | 5.59 | +3.3% |
| Draw | 25.9% | 24.0% | 3.81 | -1.2% |
| Juventus win | 55.6% | 59.1% | 1.63 | -9.4% |
| Over 2.5 | 38.9% | 46.5% | 2.12 | -17.5% |
| Under 2.5 | 61.1% | 53.5% | 1.75 | +6.9% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Genoa |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7826 |
| Dc lambda away | 1.4324 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 41.2% |
| P btts no | 58.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.49 |
| Fair Over 1.5 odds | 1.52 |
| Fair Under 1.5 odds | 2.92 |
| Fair Over 2.5 odds | 2.57 |
| Fair Under 2.5 odds | 1.64 |
| Fair Over 3.5 odds | 5.37 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.11 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.2753800162218163, "-10": 1.2924535241240453e-06, "-11": 1.6688821902104965e-07, "-12": 1.9777460032587978e-08, "-13": 2.1598836411869213e-09, "-14": 2.045976778908996e-10, "-2": 0.17101857037916643, "-3": 0.07500583275294635, "-4": 0.025480741144386348, "-5": 0.007043035266609031, "-6": 0.0016384693462973498, "-7": 0.0003287854088778583, "-8": 5.7975559518535744e-05, "-9": 9.114458001797301e-06, "0": 0.25923098088612007, "1": 0.12796133733445988, "10": 2.641788585285266e-09, "11": 1.8638611406499102e-10, "12": 1.2068773561720613e-11, "13": 7.201578983749722e-13, "14": 3.727372725148161e-14, "2": 0.044003619347209325, "3": 0.01054495945630014, "4": 0.0019573418534557497, "5": 0.00029561008024942936, "6": 3.7575299127339616e-05, "7": 4.119850068599969e-06, "8": 3.9693424959372484e-07, "9": 3.409645460176388e-08} |
| Raw goal margin distribution | {"-1": 0.2578581845483317, "-10": 1.2102175165654498e-06, "-11": 1.5626948450975874e-07, "-12": 1.8519063252841468e-08, "-13": 2.022454941332731e-09, "-14": 1.915795725033884e-10, "-2": 0.1601370305915806, "-3": 0.07023337470004229, "-4": 0.023859456988138995, "-5": 0.006594902246264753, "-6": 0.0015342171043159943, "-7": 0.00030786550818900346, "-8": 5.428670072261782e-05, "-9": 8.534524856706997e-06, "0": 0.2786279251435359, "1": 0.13902459592154148, "10": 2.8701918738115476e-09, "11": 2.0250065162685336e-10, "12": 1.3112213443825473e-11, "13": 7.824211821075188e-13, "14": 4.049633254521702e-14, "2": 0.04780807645704123, "3": 0.011456653688991809, "4": 0.00212656936794709, "5": 0.0003211678840898138, "6": 4.082397766878177e-05, "7": 4.476043334459603e-06, "8": 4.3125232047982833e-07, "9": 3.704435982079146e-08} |
| Unadjusted home-win probability | 20.1% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 52.1% |
| Raw p over 1 5 | 65.3% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 41.7% |
| P home draw | 44.4% |
| P draw away | 81.5% |
| P home away | 74.1% |
| Raw p home draw | 47.9% |
| Raw p draw away | 79.9% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.45 |
| Reference draw odds | 3.90 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.04 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:42Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:42Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.9% |
| Away probability edge | -3.5% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | 0.0320 |
| Raw ev home | 0.1224 |
| Raw edge prob draw | 0.0388 |
| Raw ev draw | 0.0616 |
| Raw edge prob away | -0.0707 |
| Raw ev away | -0.1514 |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -101.3773 |
| Elo home expectancy | 0.3581 |

</details>


---

## 2026-10-28 — Monza vs Napoli

The model's most likely 1X2 outcome is **Napoli win** at **56.6%**. Expected goals are 0.81 for Monza and 1.88 for Napoli (2.69 combined). The most likely exact score is 0-1 at 11.3%. Goal-market probabilities: at least one goal: 92.5%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.3%; Double Chance 1X: 43.4%; Double Chance X2: 80.3%; Double Chance 12 (either team wins): 76.4%; Under 4.5 goals: 86.8%; BTTS Yes (both teams score): 48.2%; BTTS No (at least one team does not score): 51.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Monza win | 19.7% | 5.07 |
| Draw | 23.6% | 4.23 |
| Napoli win | 56.6% | 1.77 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Monza expected goals | 0.81 |
| Napoli expected goals | 1.88 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.5% |
| Under 0.5 | 7.5% |
| Over 1.5 | 74.6% |
| Under 1.5 | 25.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.7% |
| Under 3.5 | 72.3% |
| Over 4.5 | 13.2% |
| Under 4.5 | 86.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 11.26% |
| 2 | 1-1 | 11.24% |
| 3 | 0-2 | 10.88% |
| 4 | 1-2 | 8.86% |
| 5 | 0-0 | 7.47% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Monza win | 19.7% | 24.1% | 3.79 | -25.3% |
| Draw | 23.6% | 24.8% | 3.85 | -9.0% |
| Napoli win | 56.6% | 51.1% | 1.89 | +7.0% |
| Over 2.5 | 49.6% | 55.0% | 1.80 | -10.7% |
| Under 2.5 | 50.4% | 45.0% | 2.17 | +9.3% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Monza |
| Matched away-team name | Napoli |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.8150 |
| Dc lambda away | 1.8783 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 48.2% |
| P btts no | 51.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.39 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.94 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.61 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.58 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.22700858070117172, "-10": 1.066697811465121e-05, "-11": 1.800791630943309e-06, "-12": 2.7915829754173505e-07, "-13": 4.0000776107921265e-08, "-14": 5.327494786418979e-09, "-15": 6.603368727080179e-10, "-16": 7.075181876629248e-11, "-2": 0.17603996586123843, "-3": 0.09850875570098243, "-4": 0.04311328781422146, "-5": 0.015435647704780476, "-6": 0.004666581292868895, "-7": 0.0012195492646202624, "-8": 0.0002804761954025249, "-9": 5.757070956591783e-05, "0": 0.23648106155914872, "1": 0.13649598281355338, "10": 3.5604307720798706e-09, "11": 2.607958730999408e-10, "12": 1.754138584112401e-11, "13": 1.0905808998418099e-12, "14": 6.302148206433603e-14, "15": 3.389278343915857e-15, "16": 1.5756342249529877e-16, "2": 0.046780358275513134, "3": 0.011358035207015086, "4": 0.0021568285803664, "5": 0.0003350467839271926, "6": 4.394966212104888e-05, "7": 4.98347360993927e-06, "8": 4.972845094502457e-07, "9": 4.4288055718850836e-08} |
| Raw goal margin distribution | {"-1": 0.24910218012783586, "-10": 1.1705141257340208e-05, "-11": 1.976053591623659e-06, "-12": 3.06327365704121e-07, "-13": 4.389384975894528e-08, "-14": 5.845992965629767e-09, "-15": 7.246041277483547e-10, "-16": 7.763773619594292e-11, "-2": 0.1931730472487728, "-3": 0.10809611571069765, "-4": 0.047309286520489637, "-5": 0.01693792139076704, "-6": 0.0051207560974430456, "-7": 0.0013382418393695474, "-8": 0.0003077735279121509, "-9": 6.317377616335436e-05, "0": 0.22525634626683824, "1": 0.10610969727940167, "10": 2.767819415797108e-09, "11": 2.0273835592767476e-10, "12": 1.3636380376155896e-11, "13": 8.477993766232759e-13, "14": 4.8991847570197734e-14, "15": 2.6347683767352115e-15, "16": 1.2248717301900336e-16, "2": 0.0363662691964863, "3": 0.008829546867700832, "4": 0.0016766825149634775, "5": 0.0002604597738639192, "6": 3.416573328437489e-05, "7": 3.874069150246348e-06, "8": 3.8658067198635426e-07, "9": 3.442879481544646e-08} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 62.1% |
| Raw p over 1 5 | 75.4% |
| Raw p under 3 5 | 71.6% |
| Raw p btts yes | 47.6% |
| P home draw | 43.4% |
| P draw away | 80.3% |
| P home away | 76.4% |
| Raw p home draw | 37.9% |
| Raw p draw away | 84.7% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.90 |
| Reference draw odds | 3.80 |
| Reference away odds | 1.90 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | -4.4% |
| Draw probability edge | -1.1% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0878 |
| Raw ev home | -0.4191 |
| Raw edge prob draw | -0.0224 |
| Raw ev draw | -0.1328 |
| Raw edge prob away | 0.1102 |
| Raw ev away | 0.1746 |
| Elo home rating | 1,364.4494 |
| Elo away rating | 1,577.6538 |
| Elo rating diff | -153.2044 |
| Elo home expectancy | 0.2928 |

</details>


---

## 2026-10-28 — Parma vs Udinese

The model's most likely 1X2 outcome is **Udinese win** at **38.9%**. Expected goals are 1.05 for Parma and 1.17 for Udinese (2.22 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 38.3%; Under 3.5 goals: 81.6%; Double Chance 1X: 61.1%; Double Chance X2: 68.3%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 92.5%; BTTS Yes (both teams score): 45.1%; BTTS No (at least one team does not score): 54.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Parma win | 31.7% | 3.15 |
| Draw | 29.3% | 3.41 |
| Udinese win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Parma expected goals | 1.05 |
| Udinese expected goals | 1.17 |
| Expected total goals | 2.22 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 65.4% |
| Under 1.5 | 34.6% |
| Over 2.5 | 38.3% |
| Under 2.5 | 61.7% |
| Over 3.5 | 18.4% |
| Under 3.5 | 81.6% |
| Over 4.5 | 7.5% |
| Under 4.5 | 92.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.56% |
| 2 | 0-1 | 12.56% |
| 3 | 0-0 | 11.16% |
| 4 | 1-0 | 10.86% |
| 5 | 1-2 | 7.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Parma win | 31.7% | 31.4% | 2.96 | -6.1% |
| Draw | 29.3% | 28.8% | 3.21 | -5.9% |
| Udinese win | 38.9% | 39.8% | 2.50 | -2.6% |
| Over 2.5 | 38.3% | 43.9% | 2.22 | -14.9% |
| Under 2.5 | 61.7% | 56.1% | 1.77 | +9.2% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Parma |
| Matched away-team name | Udinese |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0479 |
| Dc lambda away | 1.1680 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.1% |
| P btts no | 54.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.96 |
| Fair Over 1.5 odds | 1.53 |
| Fair Under 1.5 odds | 2.89 |
| Fair Over 2.5 odds | 2.61 |
| Fair Under 2.5 odds | 1.62 |
| Fair Over 3.5 odds | 5.43 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 13.40 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.22337417074444166, "-10": 1.621888051249277e-07, "-11": 1.7062152035655322e-08, "-12": 1.6417197703787706e-09, "-13": 1.348084745414133e-10, "-2": 0.11224524507139401, "-3": 0.039860744078706524, "-4": 0.010992180756424245, "-5": 0.002469776346731946, "-6": 0.0004674421656549951, "-7": 7.635386985272078e-05, "-8": 1.0963632570767299e-05, "-9": 1.4039342943252985e-06, "0": 0.2932323205892513, "1": 0.193445162412344, "10": 5.302485890420073e-08, "11": 5.004622107182808e-09, "12": 4.32031433334196e-10, "13": 3.1828219711126036e-11, "2": 0.08741700396191955, "3": 0.027851731641970415, "4": 0.006890797654026973, "5": 0.0013890634951092364, "6": 0.0002358691770036485, "7": 3.456632388150451e-05, "8": 4.45302823864385e-06, "9": 5.115953575538135e-07} |
| Raw goal margin distribution | {"-1": 0.21846415360001464, "-10": 1.5862371158191186e-07, "-11": 1.6687106618646325e-08, "-12": 1.6056329113115833e-09, "-13": 1.3184523166061635e-10, "-2": 0.10977796751712614, "-3": 0.03898455979937021, "-4": 0.010750560179663688, "-5": 0.0024154878667123473, "-6": 0.0004571672576844584, "-7": 7.467552535670867e-05, "-8": 1.0722639515445547e-05, "-9": 1.373074229207596e-06, "0": 0.2983587866141486, "1": 0.19553964030107931, "10": 5.3598971966234454e-08, "11": 5.058808369657686e-09, "12": 4.367091428880193e-10, "13": 3.217283159798556e-11, "2": 0.08836348915500725, "3": 0.028153289123996006, "4": 0.00696540599854243, "5": 0.0014041032238896038, "6": 0.00023842299003111152, "7": 3.494058188910643e-05, "8": 4.501242259958445e-06, "9": 5.171345250936669e-07} |
| Unadjusted home-win probability | 32.1% |
| Unadjusted draw probability | 29.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 65.4% |
| Raw p under 3 5 | 81.6% |
| Raw p btts yes | 45.2% |
| P home draw | 61.1% |
| P draw away | 68.3% |
| P home away | 70.7% |
| Raw p home draw | 61.9% |
| Raw p draw away | 67.9% |
| Raw p home away | 70.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.77, "price": 2.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.04 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.42 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.15 |
| Reference Under 2.5 odds | 1.71 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.5% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -5.5% |
| Under 2.5 probability edge | +5.5% |
| Raw edge prob home | 0.0069 |
| Raw ev home | -0.0507 |
| Raw edge prob draw | 0.0103 |
| Raw ev draw | -0.0423 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.0477 |
| Elo home rating | 1,371.5475 |
| Elo away rating | 1,454.9036 |
| Elo rating diff | -23.3561 |
| Elo home expectancy | 0.4664 |

</details>


---

## 2026-10-28 — Venezia vs Inter Milan

The model's most likely 1X2 outcome is **Inter Milan win** at **76.8%**. Expected goals are 0.69 for Venezia and 2.67 for Inter Milan (3.36 combined). The most likely exact score is 0-2 at 12.0%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 64.8%; Under 3.5 goals: 57.2%; Double Chance 1X: 23.2%; Double Chance X2: 91.2%; Double Chance 12 (either team wins): 85.6%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 47.0%; BTTS No (at least one team does not score): 53.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Venezia win | 8.8% | 11.34 |
| Draw | 14.4% | 6.95 |
| Inter Milan win | 76.8% | 1.30 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Venezia expected goals | 0.69 |
| Inter Milan expected goals | 2.67 |
| Expected total goals | 3.36 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 42.8% |
| Under 3.5 | 57.2% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-2 | 12.01% |
| 2 | 0-3 | 10.71% |
| 3 | 0-1 | 8.77% |
| 4 | 1-2 | 8.27% |
| 5 | 1-3 | 7.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Venezia win | 8.8% | 10.7% | 7.76 | -31.6% |
| Draw | 14.4% | 14.9% | 5.92 | -14.9% |
| Inter Milan win | 76.8% | 74.4% | 1.32 | +1.4% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Venezia |
| Matched away-team name | Inter |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6888 |
| Dc lambda away | 2.6746 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 47.0% |
| P btts no | 53.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.26 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.52 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.20017680274314095, "-10": 0.00020474181763234612, "-11": 4.910468216883925e-05, "-12": 1.0818141112956363e-05, "-13": 2.2035973147202314e-06, "-14": 4.173484823277177e-07, "-15": 7.38529935472136e-08, "-16": 1.2262859409570207e-08, "-17": 1.9175638749414506e-09, "-18": 2.822661114340154e-10, "-19": 3.62219474162607e-11, "-2": 0.21313526699008795, "-3": 0.16650070605935902, "-4": 0.10242101651910208, "-5": 0.051739295061134886, "-6": 0.022123417725677566, "-7": 0.008190199669961, "-8": 0.0026711915061638876, "-9": 0.0007781498228079716, "0": 0.14382114690583983, "1": 0.06532047663697445, "10": 3.433330843216655e-10, "11": 2.1207168508311434e-11, "12": 1.2032700506042423e-12, "13": 6.312383586427922e-14, "14": 3.079006943431939e-15, "15": 1.403235669439886e-16, "16": 6.0007418445779e-18, "17": 2.4166497738430187e-19, "18": 9.161641620498948e-21, "19": 3.0278686893393632e-22, "2": 0.01846541018581979, "3": 0.0037150991072053526, "4": 0.0005885645338510352, "5": 7.657309412828897e-05, "6": 8.432543512822012e-06, "7": 8.039916590169941e-07, "8": 6.753248969315111e-08, "9": 5.0666585919855665e-09} |
| Raw goal margin distribution | {"-1": 0.20632825320324727, "-10": 0.00021103355139479203, "-11": 5.061367329858807e-05, "-12": 1.1150583524938442e-05, "-13": 2.2713140507744004e-06, "-14": 4.301736372830287e-07, "-15": 7.61225024259181e-08, "-16": 1.2639698139750216e-08, "-17": 1.976490778654304e-09, "-18": 2.909401734494888e-10, "-19": 3.7335050992930446e-11, "-2": 0.21968493217718457, "-3": 0.17161728715597643, "-4": 0.10556842321436948, "-5": 0.053329248072912123, "-6": 0.022803272265678236, "-7": 0.008441885214128633, "-8": 0.00275327745215988, "-9": 0.0008020624341592775, "0": 0.138814830786665, "1": 0.051545650020746105, "10": 2.709307695861233e-10, "11": 1.6734986364775586e-11, "12": 9.495236425415734e-13, "13": 4.981223835077433e-14, "14": 2.4297038614649823e-15, "15": 1.1073203754400219e-16, "16": 4.735301316071133e-18, "17": 1.907025023064762e-19, "18": 7.229628393716106e-21, "19": 2.3893496772360836e-22, "2": 0.01457141190529858, "3": 0.0029316564763704894, "4": 0.00046444764396186804, "5": 6.0425307869052495e-05, "6": 6.654282991722661e-06, "7": 6.344453502017274e-07, "8": 5.329119225658557e-08, "9": 3.998198176178999e-09} |
| Unadjusted home-win probability | 7.0% |
| Unadjusted draw probability | 13.9% |
| Unadjusted away-win probability | 79.2% |
| Raw p over 1 5 | 85.1% |
| Raw p under 3 5 | 56.6% |
| Raw p btts yes | 46.6% |
| P home draw | 23.2% |
| P draw away | 91.2% |
| P home away | 85.6% |
| Raw p home draw | 20.8% |
| Raw p draw away | 93.0% |
| Raw p home away | 86.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 8.20 |
| Reference draw odds | 6.00 |
| Reference away odds | 1.32 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:41Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:41Z |
| Home probability edge | -1.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.4% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.0372 |
| Raw ev home | -0.4601 |
| Raw edge prob draw | -0.0100 |
| Raw ev draw | -0.1782 |
| Raw edge prob away | 0.0472 |
| Raw ev away | 0.0449 |
| Elo home rating | 1,364.0519 |
| Elo away rating | 1,684.1272 |
| Elo rating diff | -260.0753 |
| Elo home expectancy | 0.1829 |

</details>


---

## 2026-10-29 — Fiorentina vs Atalanta BC

The model's most likely 1X2 outcome is **Atalanta BC win** at **38.5%**. Expected goals are 1.25 for Fiorentina and 1.59 for Atalanta BC (2.84 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 53.7%; Under 3.5 goals: 68.5%; Double Chance 1X: 61.5%; Double Chance X2: 64.5%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fiorentina win | 35.5% | 2.81 |
| Draw | 25.9% | 3.85 |
| Atalanta BC win | 38.5% | 2.60 |

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
| Over 2.5 | 53.7% |
| Under 2.5 | 46.3% |
| Over 3.5 | 31.5% |
| Under 3.5 | 68.5% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 2-1 | 8.70% |
| 3 | 1-0 | 8.27% |
| 4 | 1-2 | 7.92% |
| 5 | 0-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fiorentina win | 35.5% | 41.4% | 2.25 | -20.0% |
| Draw | 25.9% | 26.5% | 3.54 | -8.1% |
| Atalanta BC win | 38.5% | 32.1% | 3.09 | +19.0% |
| Over 2.5 | 53.7% | 55.7% | 1.78 | -4.3% |
| Under 2.5 | 46.3% | 44.3% | 2.21 | +2.2% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Fiorentina |
| Matched away-team name | Atalanta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.2523 |
| Dc lambda away | 1.5903 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.77 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.50 |
| Fair Over 2.5 odds | 1.86 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.36 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.18651272955244852, "-10": 1.7066828404603155e-06, "-11": 2.431149540236868e-07, "-12": 3.1816249951594534e-08, "-13": 3.849028939606324e-09, "-14": 4.3003263901317894e-10, "-15": 4.024802800768625e-11, "-2": 0.11719493156199039, "-3": 0.05393918445653856, "-4": 0.019608665204967644, "-5": 0.005864428621549612, "-6": 0.0014862370031066875, "-7": 0.0003263484760461928, "-8": 6.31634175428191e-05, "-9": 1.092338596914308e-05, "0": 0.25949557413474894, "1": 0.20383175640648127, "10": 2.1821075793200418e-07, "11": 2.447725213253563e-08, "12": 2.5224794133917853e-09, "13": 2.403020465642789e-10, "14": 2.1141478940724782e-11, "15": 1.5581390232930388e-12, "2": 0.10134701132021527, "3": 0.036731117760858294, "4": 0.010514907407054385, "5": 0.0024763428822220965, "6": 0.000494197786492214, "7": 8.545194799306947e-05, "8": 1.3023678027134868e-05, "9": 1.7735889026952082e-06} |
| Raw goal margin distribution | {"-1": 0.21730562615663798, "-10": 1.988452928585376e-06, "-11": 2.8325277014029946e-07, "-12": 3.7069052253310877e-08, "-13": 4.484496290538537e-09, "-14": 5.010302091057653e-10, "-15": 4.689290081576283e-11, "-2": 0.13654359167105082, "-3": 0.0628444411318875, "-4": 0.0228460185033276, "-5": 0.006832634623463524, "-6": 0.0017316119031245182, "-7": 0.0003802279882057065, "-8": 7.359157754149811e-05, "-9": 1.2726816198932783e-05, "0": 0.2544314964064196, "1": 0.17028936578882156, "10": 1.8230217033717088e-07, "11": 2.04492951215625e-08, "12": 2.107382220978533e-09, "13": 2.007581342015349e-10, "14": 1.766245409510329e-11, "15": 1.3017329132868554e-12, "2": 0.08466942829014064, "3": 0.030686674434269805, "4": 0.00878458266387454, "5": 0.0020688378804346835, "6": 0.00041287299447184005, "7": 7.139004385626964e-05, "8": 1.0880511999591877e-05, "9": 1.4817285330543103e-06} |
| Unadjusted home-win probability | 29.7% |
| Unadjusted draw probability | 25.4% |
| Unadjusted away-win probability | 44.9% |
| Raw p over 1 5 | 78.0% |
| Raw p under 3 5 | 68.2% |
| Raw p btts yes | 57.2% |
| P home draw | 61.5% |
| P draw away | 64.5% |
| P home away | 74.1% |
| Raw p home draw | 55.1% |
| Raw p draw away | 70.3% |
| Raw p home away | 74.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.24, "price": 1.76, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.33 |
| Reference draw odds | 3.58 |
| Reference away odds | 2.97 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market best over 2 5 last update utc | 2026-10-23T14:33:17Z |
| Market best under 2 5 last update utc | 2026-10-23T14:33:17Z |
| Home probability edge | -5.9% |
| Draw probability edge | -0.5% |
| Away probability edge | +6.4% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.1170 |
| Raw ev home | -0.3318 |
| Raw edge prob draw | -0.0101 |
| Raw ev draw | -0.0993 |
| Raw edge prob away | 0.1271 |
| Raw ev away | 0.3861 |
| Elo home rating | 1,435.7664 |
| Elo away rating | 1,541.0294 |
| Elo rating diff | -45.2630 |
| Elo home expectancy | 0.4352 |

</details>


---

## 2026-10-29 — Frosinone vs Lecce

The model's most likely 1X2 outcome is **Frosinone win** at **50.8%**. Expected goals are 1.56 for Frosinone and 0.97 for Lecce (2.53 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 46.7%; Under 3.5 goals: 75.0%; Double Chance 1X: 76.3%; Double Chance X2: 49.2%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 88.6%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Frosinone win | 50.8% | 1.97 |
| Draw | 25.6% | 3.91 |
| Lecce win | 23.7% | 4.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Frosinone expected goals | 1.56 |
| Lecce expected goals | 0.97 |
| Expected total goals | 2.53 |
| Over 0.5 | 91.9% |
| Under 0.5 | 8.1% |
| Over 1.5 | 72.4% |
| Under 1.5 | 27.6% |
| Over 2.5 | 46.7% |
| Under 2.5 | 53.3% |
| Over 3.5 | 25.0% |
| Under 3.5 | 75.0% |
| Over 4.5 | 11.4% |
| Under 4.5 | 88.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 1-0 | 12.02% |
| 3 | 2-0 | 9.70% |
| 4 | 2-1 | 9.42% |
| 5 | 0-0 | 8.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Frosinone win | 50.8% | 50.8% | 1.88 | -4.5% |
| Draw | 25.6% | 24.9% | 3.68 | -5.9% |
| Lecce win | 23.7% | 24.2% | 4.05 | -4.1% |

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
| Market best home last update utc | 2026-10-23T14:33:42Z |
| Market best draw last update utc | 2026-10-23T14:33:42Z |
| Market best away last update utc | 2026-10-23T14:33:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Frosinone |
| Matched away-team name | Lecce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5623 |
| Dc lambda away | 0.9711 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:33:55.052720+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.29 |
| Fair Over 1.5 odds | 1.38 |
| Fair Under 1.5 odds | 3.62 |
| Fair Over 2.5 odds | 2.14 |
| Fair Under 2.5 odds | 1.88 |
| Fair Over 3.5 odds | 4.00 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.78 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1520044756374865, "-10": 1.917038627188575e-08, "-11": 1.673264453873966e-09, "-12": 1.3410806628787033e-10, "-13": 9.933612083265257e-12, "-14": 6.81144866032121e-13, "-15": 4.004495278017188e-14, "-2": 0.0618325690366487, "-3": 0.017903411784260925, "-4": 0.004053150697057313, "-5": 0.0007505007421387364, "-6": 0.00011733378281549226, "-7": 1.5855903053465587e-05, "-8": 1.885532408004698e-06, "-9": 2.001109606754674e-07, "0": 0.2556063547224868, "1": 0.24146403079156026, "10": 2.177439536753743e-06, "11": 3.057817800620167e-07, "12": 3.943062840732756e-08, "13": 4.699133390626344e-09, "14": 5.184201138398024e-10, "15": 4.903677724933647e-11, "2": 0.15641496499311208, "3": 0.07286661419833511, "4": 0.026541002287450044, "5": 0.007906922334565072, "6": 0.0019888919873901215, "7": 0.00043242509169476296, "8": 8.273431670854178e-05, "9": 1.4127142918365517e-05} |
| Raw goal margin distribution | {"-1": 0.14832273737422103, "-10": 1.8706055571340402e-08, "-11": 1.6327358987866669e-09, "-12": 1.3085980141281403e-10, "-13": 9.693007590890855e-12, "-14": 6.646466865832596e-13, "-15": 3.90750140051253e-14, "-2": 0.06033490698174212, "-3": 0.017469768788338138, "-4": 0.003954978324529771, "-5": 0.0007323226767406415, "-6": 0.00011449181203829132, "-7": 1.54718532764722e-05, "-8": 1.8398624579320825e-06, "-9": 1.95264023256501e-07, "0": 0.26209378684471607, "1": 0.24110507353384333, "10": 2.1742025837285017e-06, "11": 3.0532720888273574e-07, "12": 3.9372011352867113e-08, "13": 4.692147720628142e-09, "14": 5.176494373054996e-10, "15": 4.896387982013762e-11, "2": 0.15618244055990455, "3": 0.0727582916464171, "4": 0.026501546781936742, "5": 0.007895168007641546, "6": 0.0019859353266761083, "7": 0.00043178225423125385, "8": 8.261132495963648e-05, "9": 1.4106141693194513e-05} |
| Unadjusted home-win probability | 50.7% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 23.1% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.0% |
| Raw p btts yes | 49.5% |
| P home draw | 76.3% |
| P draw away | 49.2% |
| P home away | 74.4% |
| Raw p home draw | 76.9% |
| Raw p draw away | 49.3% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:33:42Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:33:17Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.91 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.88 |
| Market reference 1x2 last update utc | 2026-10-23T14:33:49Z |
| Market reference home last update utc | 2026-10-23T14:33:49Z |
| Market reference draw last update utc | 2026-10-23T14:33:49Z |
| Market reference away last update utc | 2026-10-23T14:33:49Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-23T14:33:49Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:33:49Z |
| Home probability edge | -0.1% |
| Draw probability edge | +0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -14.8% |
| Under 2.5 probability edge | +14.8% |
| Raw edge prob home | -0.0015 |
| Raw ev home | -0.0469 |
| Raw edge prob draw | 0.0130 |
| Raw ev draw | -0.0355 |
| Raw edge prob away | -0.0115 |
| Raw ev away | -0.0647 |
| Elo home rating | 1,459.6529 |
| Elo away rating | 1,423.2697 |
| Elo rating diff | 96.3832 |
| Elo home expectancy | 0.6353 |

</details>


---
