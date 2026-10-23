# Premier League — football model report

Fixtures in this report: **19**.

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
| Training sha256 | fe022050bf7291d98204217104785785177adeb107b106a40458f2a4e99448f2 |
| Training as of utc | 2026-10-23T14:29:21.316153+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 80, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-23T14:29:21.316153+00:00', 'observations': 213, 'observations_sha256': 'f306d8741b34e2c16b88c23b5e83c943e663bd665f7143ef456fe9000b8ffd9f', 'eligible_training_matches': 127, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 119, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 127, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'e5ec6566177f405633f071ef4b1e25cf1c1ad76b7f644c2551e2da5e2ac7c794', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 64, 'tuning_matches': 22, 'audit_matches': 41, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-04T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 35, 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 925.005 |
| Base scoring parameter | 0.212 |
| Home-advantage parameter | 0.185 |
| Dixon-Coles low-score adjustment | -0.089 |
| Xi per day | 0.0029 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1970, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-19'} |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 19.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261023T142921316153Z_d76577e8ddc3046cedc0c49ae78074ec2fb5ff1d8de12e1194840100d27ec77e.json |
| Over 1 5 in window quote fixtures | 6 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 9.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 9.00 |
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

The model's most likely 1X2 outcome is **Nottingham Forest win** at **43.3%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 57.5%; Under 3.5 goals: 64.6%; Double Chance 1X: 56.7%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 81.5%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.8% | 3.36 |
| Draw | 26.9% | 3.72 |
| Nottingham Forest win | 43.3% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.69 |
| Expected total goals | 3.01 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 81.1% |
| Under 1.5 | 18.9% |
| Over 2.5 | 57.5% |
| Under 2.5 | 42.5% |
| Over 3.5 | 35.4% |
| Under 3.5 | 64.6% |
| Over 4.5 | 18.5% |
| Under 4.5 | 81.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.49% |
| 2 | 1-2 | 8.91% |
| 3 | 2-1 | 7.44% |
| 4 | 0-1 | 7.04% |
| 5 | 0-2 | 6.74% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.8% | 30.5% | 3.24 | -3.5% |
| Draw | 26.9% | 28.0% | 3.48 | -6.4% |
| Nottingham Forest win | 43.3% | 41.5% | 2.32 | +0.5% |
| Over 2.5 | 57.5% | 52.7% | 1.83 | +5.2% |
| Under 2.5 | 42.5% | 47.3% | 2.14 | -9.1% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.3212 |
| Dc lambda away | 1.6905 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.23 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.30 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.42 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.19950204705309357, "-10": 3.030989201844697e-06, "-11": 4.5815907931896054e-07, "-12": 6.364103643511307e-08, "-13": 8.172592153160342e-09, "-14": 9.678656960901703e-10, "-15": 9.494095416100872e-11, "-2": 0.13391755689246648, "-3": 0.06457760464815815, "-4": 0.02471444799533654, "-5": 0.00780322722197304, "-6": 0.002091463828347168, "-7": 0.00048626004632839487, "-8": 9.973161013037766e-05, "-9": 1.8287791198493555e-05, "0": 0.2689168457029827, "1": 0.16452594966117584, "10": 2.755736230446864e-07, "11": 3.255559930999757e-08, "12": 3.534294878192535e-09, "13": 3.5471659279165986e-10, "14": 3.283166559932198e-11, "15": 2.5170251243884565e-12, "2": 0.08746648058354756, "3": 0.03296417465390557, "4": 0.009859782385356224, "5": 0.0024330263285089995, "6": 0.0005096582439411805, "7": 9.26090486983904e-05, "8": 1.4844781406468332e-05, "9": 2.1274451460936753e-06} |
| Raw goal margin distribution | {"-1": 0.20806686210539382, "-10": 3.1611124879100782e-06, "-11": 4.778282899203673e-07, "-12": 6.63732074321274e-08, "-13": 8.523449406625368e-09, "-14": 1.009417102729482e-09, "-15": 9.901686077594963e-11, "-2": 0.13966676660726515, "-3": 0.06734998342071706, "-4": 0.025775463054211682, "-5": 0.008138227283147788, "-6": 0.002181252385121236, "-7": 0.0005071356585120498, "-8": 0.00010401318422073008, "-9": 1.9072903690539805e-05, "0": 0.25765885964663043, "1": 0.16047157453522168, "10": 2.6878272565164673e-07, "11": 3.175333916608222e-08, "12": 3.447200062624286e-09, "13": 3.4597539340311686e-10, "14": 3.20226024173518e-11, "15": 2.4549986533257556e-12, "2": 0.08531106422544114, "3": 0.03215184608178888, "4": 0.009616810036417747, "5": 0.002373069820448032, "6": 0.0004970988530899011, "7": 9.032690521735122e-05, "8": 1.4478964873522859e-05, "9": 2.075019004807651e-06} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 56.7% |
| P draw away | 70.2% |
| P home away | 73.1% |
| Raw p home draw | 54.8% |
| Raw p draw away | 70.9% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.2, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.81, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.12, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.16, "price": 5.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:01Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.04, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.32, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.66, "price": 2.32, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.20 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.37 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -0.7% |
| Draw probability edge | -1.1% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +4.8% |
| Under 2.5 probability edge | -4.8% |
| Raw edge prob home | -0.0147 |
| Raw ev home | -0.0587 |
| Raw edge prob draw | -0.0225 |
| Raw ev draw | -0.1033 |
| Raw edge prob away | 0.0372 |
| Raw ev away | 0.0482 |
| Market p home draw | 57.6% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:32Z |
| Market reference home draw last update utc | 2026-10-23T14:29:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.1% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:32Z |
| Market reference draw away last update utc | 2026-10-23T14:29:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.2% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:32Z |
| Market reference home away last update utc | 2026-10-23T14:29:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 77.0% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:29:01Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.6% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.10 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 60.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:32Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.39 |
| Market reference btts yes last update utc | 2026-10-23T14:29:32Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,345.2452 |
| Elo away rating | 1,480.4097 |
| Elo rating diff | -75.1645 |
| Elo home expectancy | 0.3935 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.3%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.0%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 88.9%; Double Chance X2: 33.7%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.3% | 1.51 |
| Draw | 22.7% | 4.41 |
| Everton win | 11.1% | 9.04 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 68.0% |
| Under 1.5 | 32.0% |
| Over 2.5 | 41.0% |
| Under 2.5 | 59.0% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.97% |
| 2 | 2-0 | 15.34% |
| 3 | 0-0 | 10.11% |
| 4 | 1-1 | 10.01% |
| 5 | 2-1 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.3% | 68.3% | 1.45 | -3.9% |
| Draw | 22.7% | 20.7% | 4.36 | -1.2% |
| Everton win | 11.1% | 11.0% | 8.33 | -7.9% |
| Over 2.5 | 41.0% | 51.5% | 1.92 | -21.3% |
| Under 2.5 | 59.0% | 48.5% | 2.02 | +19.2% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.7158 |
| Dc lambda away | 0.5764 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.89 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.13 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.78 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.08290305042301245, "-10": 1.226275004611841e-10, "-11": 6.377644462289594e-12, "-12": 3.0439377211763754e-13, "-13": 1.3422581982746632e-14, "-14": 5.499793397407722e-16, "-15": 2.1010196773115092e-17, "-16": 7.127730761696029e-19, "-2": 0.0229434817791039, "-3": 0.004086462128983404, "-4": 0.0005618926353065762, "-5": 6.274778415998758e-05, "-6": 5.891116016978265e-06, "-7": 4.767433861222355e-07, "-8": 3.388598508675578e-08, "-9": 2.1466428676114495e-09, "0": 0.2265965651578261, "1": 0.2739357206606294, "10": 6.947508570730046e-06, "11": 1.0756712875339942e-06, "12": 1.5283861394853675e-07, "13": 2.0063719596367344e-08, "14": 2.4473710368694536e-09, "15": 2.7833102379659306e-10, "16": 2.8109999651743295e-11, "2": 0.21070560506667813, "3": 0.11172292535311164, "4": 0.04573263410257321, "5": 0.015203701245817505, "6": 0.004249389741520662, "7": 0.0010237448327114393, "8": 0.0002166233250373865, "9": 4.085290616982378e-05} |
| Raw goal margin distribution | {"-1": 0.08327539535952805, "-10": 1.2317826100185553e-10, "-11": 6.406288566581458e-12, "-12": 3.057609049212747e-13, "-13": 1.3482867224492742e-14, "-14": 5.524494783098087e-16, "-15": 2.1104560494881047e-17, "-16": 7.159743750897538e-19, "-2": 0.023046528521327467, "-3": 0.004104815777904955, "-4": 0.0005644162804143771, "-5": 6.302960514956916e-05, "-6": 5.917574961590743e-06, "-7": 4.788845978742056e-07, "-8": 3.40381782195961e-08, "-9": 2.1562841485798103e-09, "0": 0.24640872397938024, "1": 0.2655426032384654, "10": 6.734643833393115e-06, "11": 1.0427137915121158e-06, "12": 1.4815579116654526e-07, "13": 1.944898722743213e-08, "14": 2.372386027837002e-09, "15": 2.6980323866757736e-10, "16": 2.724873728243602e-11, "2": 0.204249795358591, "3": 0.10829984628560291, "4": 0.044331431779918544, "5": 0.014737874994681259, "6": 0.0041191926756283075, "7": 0.000992378311505081, "8": 0.0002099862022881748, "9": 3.960121384692018e-05} |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 88.9% |
| P draw away | 33.7% |
| P home away | 77.3% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.61, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.91, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.35, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:34Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.49, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:34Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.49, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.45 |
| Reference draw odds | 4.65 |
| Reference away odds | 8.60 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.99 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -2.0% |
| Draw probability edge | +2.0% |
| Away probability edge | +0.0% |
| Over 2.5 probability edge | -10.5% |
| Under 2.5 probability edge | +10.5% |
| Raw edge prob home | -0.0406 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0396 |
| Raw ev draw | 0.0743 |
| Raw edge prob away | 0.0010 |
| Raw ev away | -0.0749 |
| Market p home draw | 87.6% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:34Z |
| Market reference home draw last update utc | 2026-10-23T14:29:34Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.3% |
| Market draw away odds | 2.92 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:34Z |
| Market reference draw away last update utc | 2026-10-23T14:29:34Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 79.1% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:34Z |
| Market reference home away last update utc | 2026-10-23T14:29:34Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.11 |
| Market reference dc draw away odds | 2.92 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 75.6% |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.75 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.2% |
| Market under 3 5 odds | 1.38 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.38 |
| Market reference under 3 5 opposite odds | 3.25 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.4% |
| Market btts yes odds | 2.11 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:34Z |
| Market reference btts yes odds | 2.11 |
| Market reference btts yes opposite odds | 1.77 |
| Market reference btts yes last update utc | 2026-10-23T14:29:34Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,645.3362 |
| Elo away rating | 1,482.5802 |
| Elo rating diff | 222.7561 |
| Elo home expectancy | 0.7828 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.2%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 10.9%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.6%; Double Chance 1X: 43.8%; Double Chance X2: 79.3%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 57.0%; BTTS No (at least one team does not score): 43.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 20.7% | 4.83 |
| Draw | 23.1% | 4.34 |
| Manchester City win | 56.2% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.87% |
| 2 | 1-2 | 10.43% |
| 3 | 0-2 | 9.30% |
| 4 | 0-1 | 9.17% |
| 5 | 1-3 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 20.7% | 19.1% | 4.99 | +3.4% |
| Draw | 23.1% | 21.3% | 4.43 | +2.2% |
| Manchester City win | 56.2% | 59.6% | 1.64 | -7.8% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda away | 1.8243 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.0% |
| P btts no | 43.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.34 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.12 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.34 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.57 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.23842935157657438, "-10": 7.5625416255186575e-06, "-11": 1.2352851990895613e-06, "-12": 1.8538578181099822e-07, "-13": 2.5728080929164712e-08, "-14": 3.3194039074919853e-09, "-15": 3.97616614529632e-10, "-16": 4.019328246680669e-11, "-2": 0.17510284104689272, "-3": 0.09213990855018328, "-4": 0.03833849723014917, "-5": 0.013132263953566804, "-6": 0.003813347707514513, "-7": 0.0009596706729892734, "-8": 0.00021291703534339414, "-9": 4.22148477214808e-05, "0": 0.2306612651922399, "1": 0.1246011938402106, "10": 5.1137892511316464e-08, "11": 5.137404341161303e-09, "12": 4.741921891098862e-10, "13": 4.047499735365347e-11, "14": 3.21174457645736e-12, "15": 2.366175124997433e-13, "16": 1.4710834142244447e-14, "2": 0.057830445660505915, "3": 0.01871598058888063, "4": 0.00478962329661307, "5": 0.0010090375723421073, "6": 0.0001802086378660827, "7": 2.7892849470879275e-05, "8": 3.806120493325008e-06, "9": 4.6412911444756864e-07} |
| Raw goal margin distribution | {"-1": 0.2241171876104151, "-10": 7.108586040647781e-06, "-11": 1.161134914330424e-06, "-12": 1.7425765648276446e-07, "-13": 2.4183705161844132e-08, "-14": 3.1201505325203328e-09, "-15": 3.737489399116033e-10, "-16": 3.778060615326003e-11, "-2": 0.16459196830646755, "-3": 0.08660903967738169, "-4": 0.03603715783990293, "-5": 0.012343975457592896, "-6": 0.003584444439988756, "-7": 0.0009020646612523932, "-8": 0.00020013629546857003, "-9": 3.968082320477931e-05, "0": 0.24853847297431148, "1": 0.13414584593161089, "10": 5.505513742418524e-08, "11": 5.53093778637144e-09, "12": 5.105160743795372e-10, "13": 4.357544732716166e-11, "14": 3.457769382833128e-12, "15": 2.547427949784878e-13, "16": 1.5837707726153113e-14, "2": 0.06226035092151018, "3": 0.020149654840022655, "4": 0.005156516153784752, "5": 0.001086331475220015, "6": 0.00019401290971361151, "7": 3.0029486655742485e-05, "8": 4.097675452046539e-06, "9": 4.996821519936836e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 43.8% |
| P draw away | 79.3% |
| P home away | 76.9% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.5, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:29:00Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:33Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:33Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 5.05 |
| Reference draw odds | 4.55 |
| Reference away odds | 1.66 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:08Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:08Z |
| Home probability edge | +1.6% |
| Draw probability edge | +1.8% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -6.2% |
| Under 2.5 probability edge | +6.2% |
| Raw edge prob home | 0.0317 |
| Raw ev home | 0.1129 |
| Raw edge prob draw | 0.0358 |
| Raw ev draw | 0.1010 |
| Raw edge prob away | -0.0675 |
| Raw ev away | -0.1334 |
| Market p home draw | 41.1% |
| Market home draw odds | 2.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:33Z |
| Market reference home draw last update utc | 2026-10-23T14:29:33Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.8% |
| Market draw away odds | 1.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:33Z |
| Market reference draw away last update utc | 2026-10-23T14:29:33Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.2% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:33Z |
| Market reference home away last update utc | 2026-10-23T14:29:33Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.36 |
| Market reference dc draw away odds | 1.20 |
| Market reference dc home away odds | 1.24 |
| Market p over 1 5 | 83.7% |
| Market over 1 5 odds | 1.15 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:29:00Z |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 5.40 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 59.1% |
| Market under 3 5 odds | 1.66 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.34 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:33Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.47 |
| Market reference btts yes last update utc | 2026-10-23T14:29:33Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,517.7051 |
| Elo away rating | 1,655.9177 |
| Elo rating diff | -78.2126 |
| Elo home expectancy | 0.3893 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **56.8%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 10.1%. Goal-market probabilities: at least one goal: 95.5%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.6%; Double Chance 1X: 79.1%; Double Chance X2: 43.2%; Double Chance 12 (either team wins): 77.7%; Under 4.5 goals: 75.9%; BTTS Yes (both teams score): 62.4%; BTTS No (at least one team does not score): 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 56.8% | 1.76 |
| Draw | 22.3% | 4.48 |
| Tottenham Hotspur win | 20.9% | 4.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 2.13 |
| Tottenham Hotspur expected goals | 1.19 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.5% |
| Under 0.5 | 4.5% |
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
| 1 | 1-1 | 10.06% |
| 2 | 2-1 | 9.54% |
| 3 | 2-0 | 8.00% |
| 4 | 3-1 | 6.79% |
| 5 | 1-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 56.8% | 55.6% | 1.77 | +0.5% |
| Draw | 22.3% | 22.6% | 4.21 | -5.9% |
| Tottenham Hotspur win | 20.9% | 21.9% | 4.30 | -10.3% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1328 |
| Dc lambda away | 1.1934 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.4% |
| P btts no | 37.6% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.46 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.76 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.15 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12407286803538543, "-10": 7.66883002718766e-08, "-11": 8.164895357894932e-09, "-12": 7.991242060455088e-10, "-13": 7.235835122908366e-11, "-14": 6.094702127019983e-12, "-15": 4.796161964940216e-13, "-16": 3.5123082158445155e-14, "-17": 2.1445150335375376e-15, "-2": 0.058348356895950027, "-3": 0.019508761096097636, "-4": 0.005206880277990835, "-5": 0.0011505006123470535, "-6": 0.00021627556883185162, "-7": 3.531933091028987e-05, "-8": 5.093456351378092e-06, "-9": 6.572069958458186e-07, "0": 0.2234297626598816, "1": 0.21272888225556943, "10": 2.3739354122300193e-05, "11": 4.5172137574838756e-06, "12": 7.901590837549052e-07, "13": 1.278701415124084e-07, "14": 1.9249222848172624e-08, "15": 2.707290058670399e-09, "16": 3.5433479363152337e-10, "17": 3.8666112246940036e-11, "2": 0.17351081902766116, "3": 0.10368307089695182, "4": 0.049457935694274514, "5": 0.01953104496561792, "6": 0.006561850338870701, "7": 0.0019151886435953766, "8": 0.0004936190492036352, "9": 0.00011383130960495292} |
| Raw goal margin distribution | {"-1": 0.11802002411949902, "-10": 7.294709303559417e-08, "-11": 7.766574290820147e-09, "-12": 7.601392598184208e-10, "-13": 6.8828378778736e-11, "-14": 5.79737458657696e-12, "-15": 4.562183173051446e-13, "-16": 3.3409617018836294e-14, "-17": 2.0398957482835478e-15, "-2": 0.05550185626586147, "-3": 0.018557034197406792, "-4": 0.004952864761863673, "-5": 0.0010943739124332388, "-6": 0.00020572465402116634, "-7": 3.359629185591291e-05, "-8": 4.844974174932559e-06, "-9": 6.251454224392232e-07, "0": 0.2212533026767154, "1": 0.2173541172131504, "10": 2.4255504488873098e-05, "11": 4.615428794203146e-06, "12": 8.073390330757627e-07, "13": 1.3065034438041142e-07, "14": 1.9667747016022442e-08, "15": 2.766153023054474e-09, "16": 3.620388799634528e-10, "17": 3.9506806054673393e-11, "2": 0.17728335944237122, "3": 0.10593738897044122, "4": 0.05053326956844083, "5": 0.019955696620697523, "6": 0.00670452066765707, "7": 0.0019568294277277224, "8": 0.0005043515085570465, "9": 0.00011630627467255255} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.1% |
| P draw away | 43.2% |
| P home away | 77.7% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.93, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.29, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:40Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.16, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.31, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.36, "price": 3.31, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 1.77 |
| Reference draw odds | 4.25 |
| Reference away odds | 4.38 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:08Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:08Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0247 |
| Raw ev home | 0.0273 |
| Raw edge prob draw | -0.0044 |
| Raw ev draw | -0.0685 |
| Raw edge prob away | -0.0203 |
| Raw ev away | -0.1470 |
| Market p home draw | 78.7% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:32Z |
| Market reference home draw last update utc | 2026-10-23T14:29:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 45.0% |
| Market draw away odds | 2.15 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:32Z |
| Market reference draw away last update utc | 2026-10-23T14:29:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.2% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:32Z |
| Market reference home away last update utc | 2026-10-23T14:29:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.23 |
| Market reference dc draw away odds | 2.15 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.4% |
| Market over 1 5 odds | 1.13 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:28:40Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.60 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.2% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.29 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 63.1% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:32Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.66 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,507.4574 |
| Elo away rating | 1,444.7579 |
| Elo rating diff | 122.6995 |
| Elo home expectancy | 0.6696 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **42.1%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.7%; Over 2.5 goals: 45.2%; Under 3.5 goals: 76.4%; Double Chance 1X: 57.9%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 71.9%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 29.8% | 3.36 |
| Draw | 28.1% | 3.55 |
| Fulham win | 42.1% | 2.38 |

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
| Over 2.5 | 45.2% |
| Under 2.5 | 54.8% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.39% |
| 2 | 0-1 | 10.53% |
| 3 | 0-0 | 9.27% |
| 4 | 1-2 | 8.78% |
| 5 | 1-0 | 8.40% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 29.8% | 30.5% | 3.20 | -4.7% |
| Draw | 28.1% | 27.1% | 3.54 | -0.4% |
| Fulham win | 42.1% | 42.4% | 2.28 | -4.1% |
| Over 2.5 | 45.2% | 54.9% | 1.81 | -18.3% |
| Under 2.5 | 54.8% | 45.1% | 2.15 | +17.9% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda away | 1.3667 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.79 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.82 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.47 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21812835933728267, "-10": 6.132608997401215e-07, "-11": 7.534395928206999e-08, "-12": 8.498196100024465e-09, "-13": 8.818880122853552e-10, "-14": 7.773630976309547e-11, "-2": 0.12813048825651505, "-3": 0.052258064623542974, "-4": 0.016659846950448844, "-5": 0.004343315644584165, "-6": 0.0009559675244708053, "-7": 0.000181858339347013, "-8": 3.0442436463281852e-05, "-9": 4.547847013736213e-06, "0": 0.2813603527667096, "1": 0.17656377744296925, "10": 7.183944702745269e-08, "11": 7.1100893906889945e-09, "12": 6.460442842085794e-10, "13": 5.400797535270917e-11, "14": 3.835105323452036e-12, "2": 0.08462503191587452, "3": 0.02780408474687859, "4": 0.007140608242254712, "5": 0.0014996658756409246, "6": 0.00026590418559359547, "7": 4.074967723673323e-05, "8": 5.4951465369718055e-06, "9": 6.613245335206905e-07} |
| Raw goal margin distribution | {"-1": 0.21648044041760972, "-10": 6.086278284492181e-07, "-11": 7.477474977459827e-08, "-12": 8.433993819409193e-09, "-13": 8.752255134480049e-10, "-14": 7.714902649560396e-11, "-2": 0.12716248640464053, "-3": 0.0518632647283791, "-4": 0.016533984925575458, "-5": 0.004310502707987718, "-6": 0.0009487453687870849, "-7": 0.00018048443363837078, "-8": 3.0212449554834007e-05, "-9": 4.513488880935492e-06, "0": 0.29193817451093335, "1": 0.1721787745004203, "10": 7.005529746309358e-08, "11": 6.933508648299587e-09, "12": 6.299996224535e-10, "13": 5.266667458155163e-11, "14": 3.739859580684924e-12, "2": 0.08252334934350052, "3": 0.027113563762361674, "4": 0.006963269557008298, "5": 0.0014624213208813857, "6": 0.00025930039260077374, "7": 3.973764941778428e-05, "8": 5.358673280206882e-06, "9": 6.449003831798611e-07} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.8% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.9% |
| P home draw | 57.9% |
| P draw away | 70.2% |
| P home away | 71.9% |
| Raw p home draw | 58.2% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.20 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.32 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 1.77 |
| Reference Under 2.5 odds | 2.13 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -0.7% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0148 |
| Raw ev home | -0.0703 |
| Raw edge prob draw | 0.0212 |
| Raw ev draw | 0.0335 |
| Raw edge prob away | -0.0064 |
| Raw ev away | -0.0481 |
| Market p home draw | 57.3% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:28:50Z |
| Market reference home draw last update utc | 2026-10-23T14:29:14Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.8% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:28:50Z |
| Market reference draw away last update utc | 2026-10-23T14:29:14Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:28:50Z |
| Market reference home away last update utc | 2026-10-23T14:29:14Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 78.8% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.5% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.7% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:28:50Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.44 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,374.3497 |
| Elo away rating | 1,443.1425 |
| Elo rating diff | -8.7928 |
| Elo home expectancy | 0.4873 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.1%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 59.2%; Under 3.5 goals: 63.0%; Double Chance 1X: 59.9%; Double Chance X2: 66.4%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 80.3%; BTTS Yes (both teams score): 62.7%; BTTS No (at least one team does not score): 37.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 33.6% | 2.98 |
| Draw | 26.3% | 3.80 |
| Newcastle United win | 40.1% | 2.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 59.2% |
| Under 2.5 | 40.8% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.7% |
| Under 4.5 | 80.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.07% |
| 2 | 1-2 | 8.89% |
| 3 | 2-1 | 7.78% |
| 4 | 2-2 | 6.55% |
| 5 | 0-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 33.6% | 32.0% | 3.01 | +1.1% |
| Draw | 26.3% | 26.7% | 3.68 | -3.2% |
| Newcastle United win | 40.1% | 41.3% | 2.33 | -6.6% |
| Over 2.5 | 59.2% | 59.2% | 1.69 | +0.1% |
| Under 2.5 | 40.8% | 40.8% | 2.36 | -3.7% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
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
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.7% |
| P btts no | 37.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.61 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.60 |
| Fair Over 2.5 odds | 1.69 |
| Fair Under 2.5 odds | 2.45 |
| Fair Over 3.5 odds | 2.71 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.08 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.19679072454088753, "-10": 1.573254401710579e-06, "-11": 2.2205428362247904e-07, "-12": 2.8804923608877495e-08, "-13": 3.4545453184957746e-09, "-14": 3.817650453838156e-10, "-15": 3.47392927391754e-11, "-2": 0.12243870511382077, "-3": 0.05476691866301672, "-4": 0.019489885172161627, "-5": 0.0057304493560967, "-6": 0.001431603652452342, "-7": 0.00031043289915778097, "-8": 5.940818415871064e-05, "-9": 1.016774625368073e-05, "0": 0.2629867796566833, "1": 0.17183204775703706, "10": 8.40355608561995e-07, "11": 1.1227138213537162e-07, "12": 1.3785496351380742e-08, "13": 1.5649207186625252e-09, "14": 1.6369800018735392e-10, "15": 1.4099832414743698e-11, "2": 0.10148847942661725, "3": 0.04296967717787993, "4": 0.014474342020263833, "5": 0.004028320301557615, "6": 0.0009525853108791114, "7": 0.0001955215311548677, "8": 3.5417580781448775e-05, "9": 5.737769275573443e-06} |
| Raw goal margin distribution | {"-1": 0.19085853928175622, "-10": 1.5258292164409761e-06, "-11": 2.1536053750662214e-07, "-12": 2.7936609598541686e-08, "-13": 3.3504092985528024e-09, "-14": 3.7025687608385993e-10, "-15": 3.3692089316449207e-11, "-2": 0.11874783460497, "-3": 0.05311598969602016, "-4": 0.018902369628478383, "-5": 0.005557707031590586, "-6": 0.0013884484778179202, "-7": 0.00030107501162202695, "-8": 5.7617345920982425e-05, "-9": 9.861243218106304e-06, "0": 0.25883562022144757, "1": 0.18013771577059806, "10": 8.809750086631852e-07, "11": 1.1769812784207784e-07, "12": 1.4451831633950495e-08, "13": 1.6405626732712045e-09, "14": 1.7161050115435892e-10, "15": 1.4781361434576444e-11, "2": 0.1063940231148963, "3": 0.04504665803184723, "4": 0.015173973323645793, "5": 0.004223033054584533, "6": 0.0009986294420527312, "7": 0.00020497225323187873, "8": 3.7129523760968695e-05, "9": 6.0151098960420235e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 59.9% |
| P draw away | 66.4% |
| P home away | 73.7% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:35Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.22, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:35Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.7, "price": 2.22, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.06 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +1.6% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0325 |
| Raw ev home | 0.0602 |
| Raw edge prob draw | -0.0083 |
| Raw ev draw | -0.0475 |
| Raw edge prob away | -0.0242 |
| Raw ev away | -0.0938 |
| Market p home draw | 58.2% |
| Market home draw odds | 1.66 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:35Z |
| Market reference home draw last update utc | 2026-10-23T14:29:35Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.0% |
| Market draw away odds | 1.42 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:35Z |
| Market reference draw away last update utc | 2026-10-23T14:29:35Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:35Z |
| Market reference home away last update utc | 2026-10-23T14:29:35Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.66 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 82.2% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.95 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 62.5% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.56 |
| Market reference under 3 5 opposite odds | 2.53 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.7% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:35Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.76 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,423.3950 |
| Elo away rating | 1,440.4285 |
| Elo rating diff | 42.9664 |
| Elo home expectancy | 0.5615 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **44.4%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 89.7%; Over 2.5 goals: 40.1%; Under 3.5 goals: 81.0%; Double Chance 1X: 55.6%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 72.8%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.4% | 3.52 |
| Draw | 27.2% | 3.68 |
| Brentford win | 44.4% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.7% |
| Under 0.5 | 10.3% |
| Over 1.5 | 66.8% |
| Under 1.5 | 33.2% |
| Over 2.5 | 40.1% |
| Under 2.5 | 59.9% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.28% |
| 2 | 1-1 | 12.66% |
| 3 | 0-0 | 10.30% |
| 4 | 1-2 | 10.03% |
| 5 | 1-0 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.4% | 18.9% | 4.89 | +39.0% |
| Draw | 27.2% | 23.3% | 4.17 | +13.3% |
| Brentford win | 44.4% | 57.8% | 1.69 | -24.9% |
| Over 2.5 | 40.1% | 57.2% | 1.71 | -31.4% |
| Under 2.5 | 59.9% | 42.8% | 2.32 | +38.9% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1911 |
| Dc lambda away | 1.0534 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.71 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.51 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2663768685010662, "-10": 7.876832853001894e-08, "-11": 7.471421557901994e-09, "-12": 6.481084789585004e-10, "-13": 4.789259335335005e-11, "-2": 0.12537862067095518, "-3": 0.04007154501881107, "-4": 0.009952501052630947, "-5": 0.002014848976405549, "-6": 0.00034368280008229295, "-7": 5.060302770201059e-05, "-8": 6.550337760117175e-06, "-9": 7.562304621479582e-07, "0": 0.27163048782202953, "1": 0.15893076487138635, "10": 1.4104000303004035e-07, "11": 1.5127934425805306e-08, "12": 1.4839176781928908e-09, "13": 1.2399842625394783e-10, "2": 0.0839708326862878, "3": 0.0303477692394436, "4": 0.00852331680206928, "5": 0.0019512126870387136, "6": 0.00037636187500316684, "7": 6.266283527654425e-05, "8": 9.172399174494086e-06, "9": 1.1974548102548753e-06} |
| Raw goal margin distribution | {"-1": 0.1860789341081614, "-10": 5.502402178096306e-08, "-11": 5.219200028855272e-09, "-12": 4.527395176228553e-10, "-13": 3.345561787333393e-11, "-2": 0.08758388153477914, "-3": 0.027992184258062637, "-4": 0.0069523708946841525, "-5": 0.001407483134808922, "-6": 0.0002400813909649419, "-7": 3.534900575422225e-05, "-8": 4.575772195648312e-06, "-9": 5.282686861229886e-07, "0": 0.310694564755611, "1": 0.21197035572250247, "10": 1.881089519551099e-07, "11": 2.017654444801559e-08, "12": 1.979142039390559e-09, "13": 1.6538012979016337e-10, "2": 0.11199422144121152, "3": 0.04047565898443262, "4": 0.011367783298169233, "5": 0.002602386313918255, "6": 0.0005019642395188165, "7": 8.357515610585884e-05, "8": 1.223348240612629e-05, "9": 1.5970785914027014e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.1% |
| Raw p btts yes | 46.5% |
| P home draw | 55.6% |
| P draw away | 71.6% |
| P home away | 72.8% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.5, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.35, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.11, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:59Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:33Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.78, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:33Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.29, "price": 3.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 5.10 |
| Reference draw odds | 4.17 |
| Reference away odds | 1.71 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.18 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +9.5% |
| Draw probability edge | +3.9% |
| Away probability edge | -13.4% |
| Over 2.5 probability edge | -17.1% |
| Under 2.5 probability edge | +17.1% |
| Raw edge prob home | 0.1897 |
| Raw ev home | 0.8534 |
| Raw edge prob draw | 0.0781 |
| Raw ev draw | 0.2956 |
| Raw edge prob away | -0.2678 |
| Raw ev away | -0.4756 |
| Market p home draw | 42.6% |
| Market home draw odds | 2.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:33Z |
| Market reference home draw last update utc | 2026-10-23T14:29:33Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.3% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:33Z |
| Market reference draw away last update utc | 2026-10-23T14:29:33Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:33Z |
| Market reference home away last update utc | 2026-10-23T14:29:33Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.28 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 80.7% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:28:59Z |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 65.1% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.70 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 57.2% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:33Z |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 2.32 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,401.6375 |
| Elo away rating | 1,497.6340 |
| Elo rating diff | -35.9965 |
| Elo home expectancy | 0.4484 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.3%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 94.7%; Over 2.5 goals: 60.4%; Under 3.5 goals: 62.1%; Double Chance 1X: 68.3%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.3% | 2.31 |
| Draw | 25.0% | 3.99 |
| Brighton and Hove Albion win | 31.7% | 3.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.64 |
| Brighton and Hove Albion expected goals | 1.47 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.7% |
| Under 0.5 | 5.3% |
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
| 1 | 1-1 | 11.44% |
| 2 | 2-1 | 9.35% |
| 3 | 1-2 | 7.46% |
| 4 | 1-0 | 6.73% |
| 5 | 2-0 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.3% | 45.8% | 2.11 | -8.7% |
| Draw | 25.0% | 24.5% | 4.03 | +1.0% |
| Brighton and Hove Albion win | 31.7% | 29.7% | 3.21 | +1.7% |
| Over 2.5 | 60.4% | 62.9% | 1.64 | -1.0% |
| Under 2.5 | 39.6% | 37.1% | 2.47 | -2.1% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.6380 |
| Dc lambda away | 1.4736 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.91 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16415412608944122, "-10": 6.935827380392578e-07, "-11": 9.12729984187978e-08, "-12": 1.1039681728758053e-08, "-13": 1.2345035589111788e-09, "-14": 1.271647143592771e-10, "-15": 1.0761233295827951e-11, "-2": 0.09518062808461064, "-3": 0.03959269421618304, "-4": 0.013115512043889267, "-5": 0.0035916187810202025, "-6": 0.000836000715164879, "-7": 0.00016894248919136913, "-8": 3.0135482088293417e-05, "-9": 4.808066445117378e-06, "0": 0.2504992656827617, "1": 0.20702823170055387, "10": 2.253393536007838e-06, "11": 3.296166658986522e-07, "12": 4.431507343068847e-08, "13": 5.508271554343602e-09, "14": 6.306925374692963e-10, "15": 5.932547100556265e-11, "2": 0.13269749571150166, "3": 0.06135603581511321, "4": 0.022592045970574553, "5": 0.006876835287579194, "6": 0.001779234181653772, "7": 0.00039966252623542656, "8": 7.924297281716275e-05, "9": 1.4053391762798846e-05} |
| Raw goal margin distribution | {"-1": 0.1743275296704706, "-10": 7.365673238002284e-07, "-11": 9.692961559367863e-08, "-12": 1.1723862750023265e-08, "-13": 1.3110115531127841e-09, "-14": 1.3504571005071872e-10, "-15": 1.1428157557533188e-11, "-2": 0.10107941945628172, "-3": 0.042046439770541226, "-4": 0.01392834203709722, "-5": 0.003814208296367595, "-6": 0.0008878116130814351, "-7": 0.00017941265016430152, "-8": 3.200311970847756e-05, "-9": 5.106044945907134e-06, "0": 0.25634770471561036, "1": 0.19484341673988181, "10": 2.120768226675417e-06, "11": 3.102168089374145e-07, "12": 4.170687374079038e-08, "13": 5.184077751925926e-09, "14": 5.935726152103092e-10, "15": 5.583382215786802e-11, "2": 0.1248874766734803, "3": 0.05774487642401688, "4": 0.021262372730006026, "5": 0.006472093553536994, "6": 0.0016745159067736992, "7": 0.0003761400631931053, "8": 7.457906320068455e-05, "9": 1.3226267960441228e-05} |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 68.3% |
| P draw away | 56.7% |
| P home away | 75.0% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.67, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.4, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:25Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.44, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.59, "price": 2.44, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.15 |
| Reference draw odds | 3.98 |
| Reference away odds | 3.29 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -2.5% |
| Draw probability edge | +0.6% |
| Away probability edge | +2.0% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0509 |
| Raw ev home | -0.1405 |
| Raw edge prob draw | 0.0117 |
| Raw ev draw | 0.0331 |
| Raw edge prob away | 0.0393 |
| Raw ev away | 0.0795 |
| Market p home draw | 69.9% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:32Z |
| Market reference home draw last update utc | 2026-10-23T14:29:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.2% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:32Z |
| Market reference draw away last update utc | 2026-10-23T14:29:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.9% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:32Z |
| Market reference home away last update utc | 2026-10-23T14:29:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.27 |
| Market p over 1 5 | 84.3% |
| Market over 1 5 odds | 1.17 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:28:25Z |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 58.7% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.66 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:32Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.82 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,540.2938 |
| Elo rating diff | 77.7935 |
| Elo home expectancy | 0.6101 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **46.8%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.4%; Under 3.5 goals: 64.0%; Double Chance 1X: 72.3%; Double Chance X2: 53.2%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 46.8% | 2.14 |
| Draw | 25.5% | 3.92 |
| Bournemouth win | 27.7% | 3.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 58.4% |
| Under 2.5 | 41.6% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.85% |
| 2 | 2-1 | 9.26% |
| 3 | 1-0 | 7.32% |
| 4 | 2-0 | 7.29% |
| 5 | 1-2 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 46.8% | 45.6% | 2.18 | +2.0% |
| Draw | 25.5% | 25.7% | 3.70 | -5.6% |
| Bournemouth win | 27.7% | 28.7% | 3.28 | -9.2% |
| Over 2.5 | 58.4% | 59.6% | 1.70 | -0.8% |
| Under 2.5 | 41.6% | 40.4% | 2.33 | -3.0% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7643 |
| Dc lambda away | 1.2710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.18 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.40 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.26 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.15661901115988858, "-10": 1.85062893187444e-07, "-11": 2.103051757212634e-08, "-12": 2.1962504705867866e-09, "-13": 2.121321159216217e-10, "-14": 1.9049092511273862e-11, "-15": 1.5864852328924127e-12, "-16": 1.105326604925242e-13, "-2": 0.08022745812795899, "-3": 0.029071306210433218, "-4": 0.008361913330907978, "-5": 0.0019844747250043295, "-6": 0.0003998216935482058, "-7": 6.987921555009713e-05, "-8": 1.0774293052074199e-05, "-9": 1.4852623896369974e-06, "0": 0.25514560771135203, "1": 0.2077235369151386, "10": 4.6164352676863556e-06, "11": 7.282556660647598e-07, "12": 1.055752910258896e-07, "13": 1.4155765252757167e-08, "14": 1.764605902551229e-09, "15": 2.0401212482745398e-10, "16": 1.9731362576853804e-11, "2": 0.1451237083850933, "3": 0.07300059317588525, "4": 0.02914835255789657, "5": 0.009602856351637037, "6": 0.002685763227080475, "7": 0.0006516222398875844, "8": 0.00013947076070217713, "9": 2.6689723715023875e-05} |
| Raw goal margin distribution | {"-1": 0.1509078168075082, "-10": 1.7831447776469364e-07, "-11": 2.0263628723218038e-08, "-12": 2.116163045751605e-09, "-13": 2.0439660710032512e-10, "-14": 1.835445736600855e-11, "-15": 1.528633217130545e-12, "-16": 1.0650202907885738e-13, "-2": 0.07730192180658309, "-3": 0.028011205788295777, "-4": 0.00805699177740754, "-5": 0.0019121098137591937, "-6": 0.00038524198587899745, "-7": 6.733103331958195e-05, "-8": 1.0381402807306412e-05, "-9": 1.4311015179224e-06, "0": 0.2528479484881452, "1": 0.2132213306110399, "10": 4.73861790085898e-06, "11": 7.475303205856432e-07, "12": 1.0836953946814584e-07, "13": 1.45304241774175e-08, "14": 1.8113095132776326e-09, "15": 2.094116890290881e-10, "16": 2.025359016067781e-11, "2": 0.14896468000022295, "3": 0.07493269103499013, "4": 0.029919818475137236, "5": 0.009857013987775515, "6": 0.0027568469971616613, "7": 0.0006688686467982594, "8": 0.0001431621164355635, "9": 2.7396117400423865e-05} |
| Unadjusted home-win probability | 48.0% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 72.3% |
| P draw away | 53.2% |
| P home away | 74.5% |
| Raw p home draw | 73.3% |
| Raw p draw away | 52.0% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.42, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:38Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.14, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.25, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.42, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:32Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.6, "price": 2.42, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 2.16 |
| Reference draw odds | 3.78 |
| Reference away odds | 3.40 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.2% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0248 |
| Raw ev home | 0.0475 |
| Raw edge prob draw | -0.0046 |
| Raw ev draw | -0.0645 |
| Raw edge prob away | -0.0202 |
| Raw ev away | -0.1254 |
| Market p home draw | 70.6% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T14:29:32Z |
| Market reference home draw last update utc | 2026-10-23T14:29:32Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.6% |
| Market draw away odds | 1.74 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T14:29:32Z |
| Market reference draw away last update utc | 2026-10-23T14:29:32Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T14:29:32Z |
| Market reference home away last update utc | 2026-10-23T14:29:32Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.37 |
| Market reference dc draw away odds | 1.74 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.4% |
| Market over 1 5 odds | 1.20 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-23T14:28:38Z |
| Market reference over 1 5 odds | 1.21 |
| Market reference over 1 5 opposite odds | 4.75 |
| Market reference over 1 5 last update utc | 2026-10-23T14:29:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 63.8% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T14:29:29Z |
| Market reference under 3 5 odds | 1.53 |
| Market reference under 3 5 opposite odds | 2.62 |
| Market reference under 3 5 last update utc | 2026-10-23T14:29:32Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 62.2% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T14:29:32Z |
| Market reference btts yes odds | 1.60 |
| Market reference btts yes opposite odds | 2.62 |
| Market reference btts yes last update utc | 2026-10-23T14:29:39Z |
| Market btts yes bookmakers | 2 |
| Elo home rating | 1,529.3488 |
| Elo away rating | 1,499.8325 |
| Elo rating diff | 89.5163 |
| Elo home expectancy | 0.6260 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **37.9%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.1%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 62.1%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 69.8%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.9% | 3.14 |
| Draw | 30.2% | 3.31 |
| Leeds United win | 37.9% | 2.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 67.6% |
| Under 1.5 | 32.4% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.15% |
| 2 | 0-0 | 11.20% |
| 3 | 0-1 | 11.16% |
| 4 | 1-0 | 10.00% |
| 5 | 1-2 | 7.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.9% | 32.6% | 3.00 | -4.4% |
| Draw | 30.2% | 29.6% | 3.26 | -1.5% |
| Leeds United win | 37.9% | 37.8% | 2.55 | -3.2% |
| Over 2.5 | 40.0% | 45.1% | 2.17 | -13.1% |
| Under 2.5 | 60.0% | 54.9% | 1.81 | +8.5% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.0684 |
| Dc lambda away | 1.2110 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.93 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.24 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.21052626662440668, "-10": 2.1402651313070893e-07, "-11": 2.3335794444974963e-08, "-12": 2.3354922643725267e-09, "-13": 2.1525639003582373e-10, "-14": 1.7044710448880825e-11, "-2": 0.1125602031155476, "-3": 0.041249877782536436, "-4": 0.01175846831155127, "-5": 0.0027334997566674326, "-6": 0.0005355867153829616, "-7": 9.060106732162735e-05, "-8": 1.3476170689980268e-05, "-9": 1.7879141452410294e-06, "0": 0.30201064204415234, "1": 0.18992619712289166, "10": 6.299216468654421e-08, "11": 6.059396308831085e-09, "12": 5.350236886611047e-10, "13": 4.350492671293669e-11, "14": 3.0392038265660274e-12, "2": 0.0902612491475858, "3": 0.029182799290607346, "4": 0.0073391006855940055, "5": 0.0015052164051267895, "6": 0.0002601941394412003, "7": 3.883191770817739e-05, "8": 5.095770244940928e-06, "9": 5.9645516874365e-07} |
| Raw goal margin distribution | {"-1": 0.211580905710542, "-10": 2.150986868306283e-07, "-11": 2.3452695966681983e-08, "-12": 2.3471919988848404e-09, "-13": 2.163347248493945e-10, "-14": 1.7130096553614824e-11, "-2": 0.11312407759853922, "-3": 0.04145652056448148, "-4": 0.01181737279161109, "-5": 0.0027471933243706317, "-6": 0.0005382697567588175, "-7": 9.10549367051254e-05, "-8": 1.3543680063366163e-05, "-9": 1.7968707669987771e-06, "0": 0.3079119239672015, "1": 0.18527388372370543, "10": 6.144914799767041e-08, "11": 5.9109691246637855e-09, "12": 5.219180828344923e-10, "13": 4.243925722371794e-11, "14": 2.9647573894795087e-12, "2": 0.08805026601204247, "3": 0.028467955681762767, "4": 0.007159326662974718, "5": 0.0014683455649987412, "6": 0.0002538205864524635, "7": 3.7880715326375604e-05, "8": 4.9709474424584795e-06, "9": 5.818447757826175e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 62.1% |
| P draw away | 68.1% |
| P home away | 69.8% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Coolbet |
| Reference home odds | 3.00 |
| Reference draw odds | 3.30 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:32Z |
| Market reference home last update utc | 2026-10-23T14:29:32Z |
| Market reference draw last update utc | 2026-10-23T14:29:32Z |
| Market reference away last update utc | 2026-10-23T14:29:32Z |
| O/U 2.5 market source | The Odds API / Coolbet |
| Reference Over 2.5 odds | 2.13 |
| Reference Under 2.5 odds | 1.77 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:32Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.6% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | -0.0156 |
| Raw ev home | -0.0678 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | 0.0038 |
| Raw edge prob away | 0.0038 |
| Raw ev away | -0.0275 |
| Elo home rating | 1,421.3554 |
| Elo away rating | 1,454.8163 |
| Elo rating diff | 26.5391 |
| Elo home expectancy | 0.5381 |

</details>


---

## 2026-10-31 — Aston Villa vs Fulham

The model's most likely 1X2 outcome is **Aston Villa win** at **47.5%**. Expected goals are 1.55 for Aston Villa and 1.05 for Fulham (2.60 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.7%; Under 3.5 goals: 73.5%; Double Chance 1X: 73.8%; Double Chance X2: 52.5%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 52.1%; BTTS No (at least one team does not score): 47.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 47.5% | 2.10 |
| Draw | 26.3% | 3.81 |
| Fulham win | 26.2% | 3.81 |

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
| 1 | 1-1 | 12.53% |
| 2 | 1-0 | 10.35% |
| 3 | 2-1 | 9.31% |
| 4 | 2-0 | 8.86% |
| 5 | 0-0 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 47.5% | 47.2% | 2.06 | -2.1% |
| Draw | 26.3% | 24.9% | 3.67 | -3.7% |
| Fulham win | 26.2% | 27.9% | 3.41 | -10.6% |
| Over 2.5 | 48.7% | 53.8% | 1.83 | -11.0% |
| Under 2.5 | 51.3% | 46.2% | 2.14 | +9.9% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.1% |
| P btts no | 47.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.36 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.91 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.95 |
| Fair Over 3.5 odds | 3.78 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.05 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.16025789006603122, "-10": 4.111320720825254e-08, "-11": 3.876963207179679e-09, "-12": 3.357467708575062e-10, "-13": 2.6873354562932648e-11, "-14": 1.9901654295645454e-12, "-15": 1.256555574167488e-13, "-2": 0.07264736619701796, "-3": 0.022579717370751828, "-4": 0.00550105591405082, "-5": 0.0010977261564563993, "-6": 0.00018511290807562747, "-7": 2.6997607260737995e-05, "-8": 3.4662595771314883e-06, "-9": 3.972958734403108e-07, "0": 0.26252359130074704, "1": 0.22559990819026599, "10": 1.907185470450986e-06, "11": 2.6586771053651563e-07, "12": 3.403675154161187e-08, "13": 4.027360312697681e-09, "14": 4.4091017945221397e-10, "15": 4.1153330928301094e-11, "2": 0.14775177116463883, "3": 0.06788810205894096, "4": 0.024450264903225313, "5": 0.007212633521842026, "6": 0.0017980381438787304, "7": 0.00038765895103407434, "8": 7.357799808045759e-05, "9": 1.2467037988673347e-05} |
| Raw goal margin distribution | {"-1": 0.1502138622876805, "-10": 3.853647170345689e-08, "-11": 3.633977815742714e-09, "-12": 3.147041258333211e-10, "-13": 2.5189089784353876e-11, "-14": 1.8654334937464496e-12, "-15": 1.1778020158448394e-13, "-2": 0.0680942539364845, "-3": 0.021164552673365034, "-4": 0.005156281885213791, "-5": 0.0010289270976148817, "-6": 0.00017351111305588263, "-7": 2.530555504936713e-05, "-8": 3.249014688500182e-06, "-9": 3.723956904451744e-07, "0": 0.2755563477475074, "1": 0.22721729039466043, "10": 1.9208585604142378e-06, "11": 2.677737826940548e-07, "12": 3.4280769532046365e-08, "13": 4.056233466737033e-09, "14": 4.4407117487859916e-10, "15": 4.144836945747838e-11, "2": 0.14881104059106032, "3": 0.06837480885346515, "4": 0.024625554971667428, "5": 0.007264342696719912, "6": 0.0018109287293406678, "7": 0.00039043817507634617, "8": 7.410549716361294e-05, "9": 1.2556417304233098e-05} |
| Unadjusted home-win probability | 47.9% |
| Unadjusted draw probability | 27.6% |
| Unadjusted away-win probability | 24.6% |
| Raw p over 1 5 | 74.4% |
| Raw p under 3 5 | 73.6% |
| Raw p btts yes | 52.3% |
| P home draw | 73.8% |
| P draw away | 52.5% |
| P home away | 73.7% |
| Raw p home draw | 75.4% |
| Raw p draw away | 52.1% |
| Raw p home away | 72.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.76 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -5.1% |
| Under 2.5 probability edge | +5.1% |
| Raw edge prob home | 0.0068 |
| Raw ev home | -0.0141 |
| Raw edge prob draw | 0.0261 |
| Raw ev draw | 0.0113 |
| Raw edge prob away | -0.0329 |
| Raw ev away | -0.1616 |
| Elo home rating | 1,517.7051 |
| Elo away rating | 1,443.1425 |
| Elo rating diff | 134.5626 |
| Elo home expectancy | 0.6845 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **42.8%**. Expected goals are 1.44 for Bournemouth and 1.22 for Leeds United (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 49.9%; Under 3.5 goals: 72.4%; Double Chance 1X: 69.8%; Double Chance X2: 57.2%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 42.8% | 2.34 |
| Draw | 27.0% | 3.70 |
| Leeds United win | 30.2% | 3.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bournemouth expected goals | 1.44 |
| Leeds United expected goals | 1.22 |
| Expected total goals | 2.65 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.4% |
| Under 1.5 | 24.6% |
| Over 2.5 | 49.9% |
| Under 2.5 | 50.1% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.88% |
| 2 | 1-0 | 9.41% |
| 3 | 2-1 | 9.21% |
| 4 | 0-0 | 7.83% |
| 5 | 2-0 | 7.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 42.8% | 44.5% | 2.20 | -5.9% |
| Draw | 27.0% | 25.9% | 3.35 | -9.6% |
| Leeds United win | 30.2% | 29.6% | 3.36 | +1.6% |
| Over 2.5 | 49.9% | 53.2% | 1.89 | -5.8% |
| Under 2.5 | 50.1% | 46.8% | 1.94 | -2.7% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda away | 1.2155 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.4% |
| P btts no | 45.6% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.76 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.17136958159964066, "-10": 1.571182766193874e-07, "-11": 1.7137824640799385e-08, "-12": 1.716461654123811e-09, "-13": 1.5797201546373925e-10, "-14": 1.2195645963106054e-11, "-2": 0.08810875078840628, "-3": 0.03147243110448979, "-4": 0.008834005679173135, "-5": 0.0020338893171595535, "-6": 0.0003960741222509716, "-7": 6.674589820405543e-05, "-8": 9.905915384383887e-06, "-9": 1.3128259277605025e-06, "0": 0.2699648480305279, "1": 0.21727638848848627, "10": 8.820793021546789e-07, "11": 1.1363171479557456e-07, "12": 1.3441288809729143e-08, "13": 1.4609989617955262e-09, "14": 1.3321020536389586e-10, "2": 0.13067618261214115, "3": 0.0551277957694495, "4": 0.01827515006299849, "5": 0.004969280752692004, "6": 0.0011428931465438292, "7": 0.0002274661007493525, "8": 3.9870314030918724e-05, "9": 6.240582498599098e-06} |
| Raw goal margin distribution | {"-1": 0.17486299138651507, "-10": 1.603211701557754e-07, "-11": 1.7487183282905274e-08, "-12": 1.7514521342623425e-09, "-13": 1.6119231267005776e-10, "-14": 1.2444257114321346e-11, "-2": 0.08990486868424491, "-3": 0.03211400411768657, "-4": 0.009014088991560658, "-5": 0.0020753506359050457, "-6": 0.00040414818768360917, "-7": 6.810652925562973e-05, "-8": 1.0107849831727071e-05, "-9": 1.3395881973633747e-06, "0": 0.28106213833599897, "1": 0.20850918376949706, "10": 8.464869864218397e-07, "11": 1.0904662152744254e-07, "12": 1.289892646883356e-08, "13": 1.40204696484179e-09, "14": 1.278351107702845e-10, "2": 0.12540333703132756, "3": 0.05290336321798982, "4": 0.017537739141419924, "5": 0.00476876793135849, "6": 0.001096776869218968, "7": 0.0002182877363362977, "8": 3.8261528061347184e-05, "9": 5.988772052413141e-06} |
| Unadjusted home-win probability | 41.0% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 54.7% |
| P home draw | 69.8% |
| P draw away | 57.2% |
| P home away | 73.0% |
| Raw p home draw | 69.2% |
| Raw p draw away | 59.0% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.00 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:29Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:29Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0345 |
| Raw ev home | -0.0969 |
| Raw edge prob draw | 0.0222 |
| Raw ev draw | -0.0584 |
| Raw edge prob away | 0.0123 |
| Raw ev away | 0.0364 |
| Elo home rating | 1,491.5511 |
| Elo away rating | 1,454.8163 |
| Elo rating diff | 96.7348 |
| Elo home expectancy | 0.6357 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **48.0%**. Expected goals are 1.60 for Brentford and 1.08 for Nottingham Forest (2.68 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.0%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 48.0% | 2.08 |
| Draw | 26.0% | 3.85 |
| Nottingham Forest win | 26.0% | 3.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Brentford expected goals | 1.60 |
| Nottingham Forest expected goals | 1.08 |
| Expected total goals | 2.68 |
| Over 0.5 | 92.4% |
| Under 0.5 | 7.6% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.41% |
| 2 | 1-0 | 9.84% |
| 3 | 2-1 | 9.41% |
| 4 | 2-0 | 8.70% |
| 5 | 0-0 | 7.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 48.0% | 47.7% | 2.01 | -3.6% |
| Draw | 26.0% | 24.9% | 3.81 | -1.0% |
| Nottingham Forest win | 26.0% | 27.4% | 3.42 | -11.0% |
| Over 2.5 | 50.5% | 55.8% | 1.78 | -10.1% |
| Under 2.5 | 49.5% | 44.2% | 2.21 | +9.4% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.5978 |
| Dc lambda away | 1.0816 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.14 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.40 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15734660774226872, "-10": 5.1086651931167265e-08, "-11": 4.958873212914266e-09, "-12": 4.420940472093863e-10, "-13": 3.642997463718481e-11, "-14": 2.77622070054866e-12, "-15": 1.794988863974437e-13, "-2": 0.07266009528525655, "-3": 0.023118342740014463, "-4": 0.0057779872036368765, "-5": 0.0011842642509139272, "-6": 0.00020527890260199947, "-7": 3.0789468060211384e-05, "-8": 4.066835033069586e-06, "-9": 4.79661851605001e-07, "0": 0.2599101822325363, "1": 0.22391461469710203, "10": 2.382139164837935e-06, "11": 3.4160033961269017e-07, "12": 4.499099081513876e-08, "13": 5.477033033949516e-09, "14": 6.166178330332033e-10, "15": 5.889785142998784e-11, "2": 0.1493312988712101, "3": 0.07019192914430483, "4": 0.02591687639011703, "5": 0.007847481531803455, "6": 0.00200956288563044, "7": 0.0004452819293506359, "8": 8.688904863573902e-05, "9": 1.5139769623145472e-05} |
| Raw goal margin distribution | {"-1": 0.14910398376118503, "-10": 4.8410470548147875e-08, "-11": 4.699101948376605e-09, "-12": 4.1893488891732277e-10, "-13": 3.452158533738763e-11, "-14": 2.630787992138411e-12, "-15": 1.7009581221092646e-13, "-2": 0.06885378606474203, "-3": 0.021907285132824847, "-4": 0.005475306538508702, "-5": 0.0011222264030404455, "-6": 0.00019452533867280876, "-7": 2.9176557483749485e-05, "-8": 3.853793312935409e-06, "-9": 4.5453469864262873e-07, "0": 0.27052420721471643, "1": 0.22532564654966045, "10": 2.3971505755194587e-06, "11": 3.437529858822976e-07, "12": 4.527450835687763e-08, "13": 5.5115473870160715e-09, "14": 6.20503543684303e-10, "15": 5.926900515984771e-11, "2": 0.1502723326647222, "3": 0.07063425421517666, "4": 0.026080195511357707, "5": 0.007896933625043184, "6": 0.0020222264504682224, "7": 0.00044808794085878314, "8": 8.743659313357976e-05, "9": 1.5235175174085296e-05} |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.9% |
| Raw p btts yes | 53.8% |
| P home draw | 74.0% |
| P draw away | 52.0% |
| P home away | 74.0% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.98 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -5.3% |
| Under 2.5 probability edge | +5.3% |
| Raw edge prob home | 0.0060 |
| Raw ev home | -0.0296 |
| Raw edge prob draw | 0.0212 |
| Raw ev draw | 0.0307 |
| Raw edge prob away | -0.0273 |
| Raw ev away | -0.1563 |
| Elo home rating | 1,503.9940 |
| Elo away rating | 1,480.4097 |
| Elo rating diff | 83.5844 |
| Elo home expectancy | 0.6180 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **49.1%**. Expected goals are 1.83 for Chelsea and 1.49 for Manchester United (3.33 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 65.0%; Under 3.5 goals: 57.3%; Double Chance 1X: 72.4%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 75.5%; BTTS Yes (both teams score): 65.7%; BTTS No (at least one team does not score): 34.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 49.1% | 2.04 |
| Draw | 23.3% | 4.28 |
| Manchester United win | 27.6% | 3.63 |

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
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.5% |
| Under 4.5 | 75.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.27% |
| 2 | 2-1 | 9.85% |
| 3 | 2-0 | 6.59% |
| 4 | 1-2 | 6.58% |
| 5 | 2-2 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 49.1% | 53.3% | 1.82 | -10.7% |
| Draw | 23.3% | 22.3% | 4.01 | -6.4% |
| Manchester United win | 27.6% | 24.4% | 3.94 | +8.6% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8315 |
| Dc lambda away | 1.4947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.33 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.87 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.09 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1439791317320288, "-10": 6.315579788183868e-07, "-11": 8.410535572805964e-08, "-12": 1.0298269394444682e-08, "-13": 1.166735714616964e-09, "-14": 1.2289933341017121e-10, "-15": 1.1970703506395364e-11, "-16": 9.549301490125244e-13, "-2": 0.08226809235354482, "-3": 0.0340844498378474, "-4": 0.011311095578298977, "-5": 0.00311393480586343, "-6": 0.0007302984924515516, "-7": 0.00014892348785388673, "-8": 2.6834486625128635e-05, "-9": 4.3282330881618215e-06, "0": 0.2334790879431486, "1": 0.21770009259825138, "10": 5.886851575983151e-06, "11": 9.606019452499648e-07, "12": 1.4412323704416963e-07, "13": 2.0007471244416614e-08, "14": 2.582374272682909e-09, "15": 3.082047182484965e-10, "16": 3.0125978623193836e-11, "2": 0.15090432562604536, "3": 0.07660841906379347, "4": 0.031151203766181176, "5": 0.010508231382777676, "6": 0.003019746350630348, "7": 0.0007545416366633984, "8": 0.00016659549437896592, "9": 3.292536142823285e-05} |
| Raw goal margin distribution | {"-1": 0.16077148439376157, "-10": 7.0521687770929e-07, "-11": 9.391460222882794e-08, "-12": 1.1499361312396394e-08, "-13": 1.3028126401213602e-09, "-14": 1.3723313945337284e-10, "-15": 1.3366852187598414e-11, "-16": 1.066304093532376e-12, "-2": 0.09186305797800703, "-3": 0.038059734971692606, "-4": 0.01263031388206591, "-5": 0.0034771144611139213, "-6": 0.0008154735430721009, "-7": 0.00016629250305472945, "-8": 2.996420519951472e-05, "-9": 4.833036913162426e-06, "0": 0.2435485102045679, "1": 0.1989746377539384, "10": 5.380494541194592e-06, "11": 8.779758510923831e-07, "12": 1.317264891370974e-07, "13": 1.828653031662565e-08, "14": 2.360251570496113e-09, "15": 2.8169451577000303e-10, "16": 2.7534695148682878e-11, "2": 0.13792430296460945, "3": 0.07001895245056342, "4": 0.028471735638686678, "5": 0.00960436675918782, "6": 0.002760003126568616, "7": 0.0006896398023239491, "8": 0.00015226579717935902, "9": 3.0093289281185864e-05} |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 66.0% |
| P home draw | 72.4% |
| P draw away | 50.9% |
| P home away | 76.7% |
| Raw p home draw | 69.2% |
| Raw p draw away | 55.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.45, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.05, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:08Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:08Z |
| Home probability edge | -4.2% |
| Draw probability edge | +1.0% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +3.2% |
| Under 2.5 probability edge | -3.2% |
| Raw edge prob home | -0.0844 |
| Raw ev home | -0.1835 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | -0.0234 |
| Raw edge prob away | 0.0643 |
| Raw ev away | 0.2128 |
| Elo home rating | 1,507.4574 |
| Elo away rating | 1,515.5196 |
| Elo rating diff | 51.9378 |
| Elo home expectancy | 0.5742 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **37.6%**. Expected goals are 1.15 for Coventry City and 1.24 for Sunderland (2.39 combined). The most likely exact score is 1-1 at 13.4%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 43.5%; Under 3.5 goals: 77.9%; Double Chance 1X: 62.4%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 49.4%; BTTS No (at least one team does not score): 50.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 34.1% | 2.93 |
| Draw | 28.3% | 3.54 |
| Sunderland win | 37.6% | 2.66 |

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
| 1 | 1-1 | 13.41% |
| 2 | 0-1 | 10.27% |
| 3 | 1-0 | 9.73% |
| 4 | 0-0 | 9.70% |
| 5 | 1-2 | 8.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 34.1% | 35.5% | 2.74 | -6.4% |
| Draw | 28.3% | 26.6% | 3.43 | -3.0% |
| Sunderland win | 37.6% | 37.9% | 2.54 | -4.6% |
| Over 2.5 | 43.5% | 50.9% | 1.92 | -16.5% |
| Under 2.5 | 56.5% | 49.1% | 1.92 | +8.5% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.1511 |
| Dc lambda away | 1.2431 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.4% |
| P btts no | 50.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.31 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.53 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.33 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.2065755171844454, "-10": 2.5446182476018715e-07, "-11": 2.845139967524964e-08, "-12": 2.920348622114532e-09, "-13": 2.7588340414884764e-10, "-14": 2.2225422847358835e-11, "-2": 0.11173529231859726, "-3": 0.041651705052889974, "-4": 0.012116011413677122, "-5": 0.002879430289622228, "-6": 0.0005773934096669356, "-7": 0.00010003224471524157, "-8": 1.5245814471525455e-05, "-9": 2.0732905970312515e-06, "0": 0.28284809080504836, "1": 0.19670241596053462, "10": 1.2178086648980918e-07, "11": 1.2607899901440187e-08, "12": 1.198275025812947e-09, "13": 1.0481660235116546e-10, "14": 7.81874820074772e-12, "2": 0.09896582464005593, "3": 0.03415940958550974, "4": 0.009200680253296716, "5": 0.0020246479879156803, "6": 0.0003759217666583032, "7": 6.0304310733598924e-05, "8": 8.510237238187042e-06, "9": 1.0716029675195348e-06} |
| Raw goal margin distribution | {"-1": 0.20476883331895457, "-10": 2.522363331847886e-07, "-11": 2.820256726062226e-08, "-12": 2.894807615081875e-09, "-13": 2.734705620956078e-10, "-14": 2.203104205427491e-11, "-2": 0.110758069303066, "-3": 0.04128742440378454, "-4": 0.012010046279795123, "-5": 0.002854247149253173, "-6": 0.0005723435984816411, "-7": 9.915737510329966e-05, "-8": 1.5112476468080553e-05, "-9": 2.055157854481777e-06, "0": 0.29995626236520023, "1": 0.18874054685455716, "10": 1.1685157615105245e-07, "11": 1.2097573435817758e-08, "12": 1.1497727801140505e-09, "13": 1.0057396982437076e-10, "14": 7.502270899526163e-12, "2": 0.09496001241908489, "3": 0.03277674864294223, "4": 0.008828266871869838, "5": 0.0019426968731479826, "6": 0.00036070568562744437, "7": 5.7863389882461864e-05, "8": 8.16577072708504e-06, "9": 1.0282279915727253e-06} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.2% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 78.0% |
| Raw p btts yes | 49.8% |
| P home draw | 62.4% |
| P draw away | 65.9% |
| P home away | 71.7% |
| Raw p home draw | 62.8% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:29:29Z |
| Market best under 2 5 last update utc | 2026-10-23T14:29:29Z |
| Home probability edge | -1.4% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -7.4% |
| Under 2.5 probability edge | +7.4% |
| Raw edge prob home | -0.0276 |
| Raw ev home | -0.1022 |
| Raw edge prob draw | 0.0342 |
| Raw ev draw | 0.0288 |
| Raw edge prob away | -0.0066 |
| Raw ev away | -0.0542 |
| Elo home rating | 1,374.3497 |
| Elo away rating | 1,407.0466 |
| Elo rating diff | 27.3031 |
| Elo home expectancy | 0.5392 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **48.5%**. Expected goals are 1.86 for Hull City and 0.87 for Ipswich Town (2.73 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 50.3%; Under 3.5 goals: 72.0%; Double Chance 1X: 73.7%; Double Chance X2: 51.5%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 48.5% | 2.06 |
| Draw | 25.2% | 3.97 |
| Ipswich Town win | 26.3% | 3.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.86 |
| Ipswich Town expected goals | 0.87 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.3% |
| Under 2.5 | 49.7% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.03% |
| 2 | 2-0 | 9.15% |
| 3 | 1-0 | 9.06% |
| 4 | 2-1 | 7.97% |
| 5 | 0-0 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 48.5% | 37.2% | 2.63 | +27.6% |
| Draw | 25.2% | 26.3% | 3.41 | -14.1% |
| Ipswich Town win | 26.3% | 36.5% | 2.66 | -30.0% |
| Over 2.5 | 50.3% | 54.2% | 1.81 | -9.0% |
| Under 2.5 | 49.7% | 45.8% | 2.17 | +7.9% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda home | 1.8617 |
| Dc lambda away | 0.8710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.83 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.41 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17486177767211603, "-10": 8.489483889829657e-09, "-11": 6.641312556318955e-10, "-12": 4.771280339009998e-11, "-13": 3.168697097146458e-12, "-14": 1.9560545322777758e-13, "-15": 1.1233265483365245e-14, "-16": 5.552336779933723e-16, "-2": 0.06678786780214487, "-3": 0.017228989156653704, "-4": 0.00348315434113297, "-5": 0.0005767153018430321, "-6": 8.068958214511933e-05, "-7": 9.763404468912091e-06, "-8": 1.039967774235348e-06, "-9": 9.888871235776722e-08, "0": 0.2518785832366365, "1": 0.19497355028534577, "10": 8.423857348784108e-06, "11": 1.4086036488749828e-06, "12": 2.163092034218945e-07, "13": 3.070619217127343e-08, "14": 4.051644849327068e-09, "15": 4.973494119251117e-10, "16": 5.254562480622571e-11, "2": 0.1520848316517908, "3": 0.08385969804067575, "4": 0.03623859818067471, "5": 0.012825234641164165, "6": 0.0038355397270146336, "7": 0.0009920086845685214, "8": 0.0002258599610975675, "9": 4.590619140338457e-05} |
| Raw goal margin distribution | {"-1": 0.10740272303589293, "-10": 5.214368165962246e-09, "-11": 4.079193649847395e-10, "-12": 2.930591851457591e-11, "-13": 1.9462612198053184e-12, "-14": 1.2014379927399874e-13, "-15": 6.899639918798118e-15, "-16": 3.4103284166275335e-16, "-2": 0.04102210879476525, "-3": 0.010582303206651872, "-4": 0.0021394055692002013, "-5": 0.0003542271767964866, "-6": 4.9560749972840605e-05, "-7": 5.996829267218297e-06, "-8": 6.387637842267251e-07, "-9": 6.073892834746697e-08, "0": 0.240629184971147, "1": 0.2402802796632546, "10": 1.038134042616004e-05, "11": 1.7359261201892389e-06, "12": 2.6657377790927507e-07, "13": 3.784150430409307e-08, "14": 4.993140639167319e-09, "15": 6.129203454151951e-10, "16": 6.475584716512857e-11, "2": 0.18742534989156354, "3": 0.10334648811697879, "4": 0.04465949608402488, "5": 0.015805482137529723, "6": 0.004726818365454297, "7": 0.0012225254338737697, "8": 0.00027834388068448813, "9": 5.65735839170857e-05} |
| Unadjusted home-win probability | 59.8% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 16.2% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 50.1% |
| P home draw | 73.7% |
| P draw away | 51.5% |
| P home away | 74.8% |
| Raw p home draw | 83.8% |
| Raw p draw away | 40.2% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | +11.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | 0.2254 |
| Raw ev home | 0.5723 |
| Raw edge prob draw | -0.0225 |
| Raw ev draw | -0.1795 |
| Raw edge prob away | -0.2029 |
| Raw ev away | -0.5703 |
| Elo home rating | 1,401.6375 |
| Elo away rating | 1,374.6638 |
| Elo rating diff | 86.9737 |
| Elo home expectancy | 0.6226 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **56.9%**. Expected goals are 1.97 for Manchester City and 1.14 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 60.6%; Under 3.5 goals: 62.2%; Double Chance 1X: 79.0%; Double Chance X2: 43.1%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 59.1%; BTTS No (at least one team does not score): 40.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 56.9% | 1.76 |
| Draw | 22.1% | 4.52 |
| Brighton and Hove Albion win | 21.0% | 4.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| Brighton and Hove Albion expected goals | 1.14 |
| Expected total goals | 3.11 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.26% |
| 2 | 2-1 | 10.08% |
| 3 | 2-0 | 8.84% |
| 4 | 1-0 | 8.07% |
| 5 | 3-1 | 6.61% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 56.9% | 58.1% | 1.67 | -5.0% |
| Draw | 22.1% | 20.7% | 4.37 | -3.4% |
| Brighton and Hove Albion win | 21.0% | 21.2% | 4.41 | -7.4% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda away | 1.1397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.1% |
| P btts no | 40.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.84 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.76 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.12636502384469703, "-10": 5.6363982593836484e-08, "-11": 5.7434612433303785e-09, "-12": 5.378329070525187e-10, "-13": 4.658155419052727e-11, "-14": 3.750800472282384e-12, "-15": 2.8010828277664575e-13, "-16": 1.7498708111121942e-14, "-2": 0.05846827748486935, "-3": 0.018997039462189953, "-4": 0.004899565849295048, "-5": 0.0010426340046027652, "-6": 0.00018836033704119703, "-7": 2.9519536175415607e-05, "-8": 4.081218254603173e-06, "-9": 5.044807066832444e-07, "0": 0.2210156797012712, "1": 0.22703087360986576, "10": 1.343805582406645e-05, "11": 2.364922450508813e-06, "12": 3.8247144852049827e-07, "13": 5.721027890607005e-08, "14": 7.95595820349399e-09, "15": 1.0261312702384172e-09, "16": 1.1071115939891858e-10, "2": 0.17611143020180503, "3": 0.09882381376705411, "4": 0.04401915733308476, "5": 0.016177985845911052, "6": 0.005047664318024562, "7": 0.0013662147713875712, "8": 0.00032621784034535045, "9": 6.964194470921845e-05} |
| Raw goal margin distribution | {"-1": 0.12494838932671731, "-10": 5.57321055056687e-08, "-11": 5.679073288479989e-09, "-12": 5.318034486006896e-10, "-13": 4.6059344519213906e-11, "-14": 3.708751547212577e-12, "-15": 2.7696808582910186e-13, "-16": 1.730253615486343e-14, "-2": 0.0578128098754644, "-3": 0.018784070232075803, "-4": 0.004844638513438599, "-5": 0.0010309453958754404, "-6": 0.00018624869453797715, "-7": 2.9188602878934447e-05, "-8": 4.035465130210259e-06, "-9": 4.988251481987968e-07, "0": 0.2352279167363763, "1": 0.22229942290182314, "10": 1.3157999205631574e-05, "11": 2.3156361405677515e-06, "12": 3.7450052907181525e-07, "13": 5.601798461440206e-08, "14": 7.790151573424082e-09, "15": 1.0047461191886208e-09, "16": 1.0840387675846863e-10, "2": 0.1724411692462197, "3": 0.09676427007511071, "4": 0.04310177341159677, "5": 0.01584082754947215, "6": 0.004942468163282544, "7": 0.001337742089480316, "8": 0.00031941927763387323, "9": 6.819056753146011e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.4% |
| P home draw | 79.0% |
| P draw away | 43.1% |
| P home away | 77.9% |
| Raw p home draw | 79.2% |
| Raw p draw away | 44.3% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:08Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:08Z |
| Home probability edge | -1.2% |
| Draw probability edge | +1.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.7% |
| Under 2.5 probability edge | +5.7% |
| Raw edge prob home | -0.0237 |
| Raw ev home | -0.0696 |
| Raw edge prob draw | 0.0284 |
| Raw ev draw | 0.0279 |
| Raw edge prob away | -0.0047 |
| Raw ev away | -0.0843 |
| Elo home rating | 1,660.4429 |
| Elo away rating | 1,540.2938 |
| Elo rating diff | 180.1491 |
| Elo home expectancy | 0.7383 |

</details>


---

## 2026-10-31 — Tottenham Hotspur vs Crystal Palace

The model's most likely 1X2 outcome is **Tottenham Hotspur win** at **52.2%**. Expected goals are 1.57 for Tottenham Hotspur and 1.25 for Crystal Palace (2.82 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.8%; Under 3.5 goals: 68.3%; Double Chance 1X: 76.1%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 76.1%; Under 4.5 goals: 83.9%; BTTS Yes (both teams score): 56.8%; BTTS No (at least one team does not score): 43.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Tottenham Hotspur win | 52.2% | 1.92 |
| Draw | 23.9% | 4.19 |
| Crystal Palace win | 23.9% | 4.18 |

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
| Over 2.5 | 54.8% |
| Under 2.5 | 45.2% |
| Over 3.5 | 31.7% |
| Under 3.5 | 68.3% |
| Over 4.5 | 16.1% |
| Under 4.5 | 83.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.31% |
| 2 | 2-1 | 10.96% |
| 3 | 1-0 | 9.91% |
| 4 | 2-0 | 8.75% |
| 5 | 0-0 | 6.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Tottenham Hotspur win | 52.2% | 60.7% | 1.62 | -15.5% |
| Draw | 23.9% | 20.9% | 4.33 | +3.4% |
| Crystal Palace win | 23.9% | 18.5% | 4.87 | +16.6% |
| Over 2.5 | 54.8% | 58.3% | 1.68 | -7.9% |
| Under 2.5 | 45.2% | 41.7% | 2.38 | +7.6% |

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
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
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
| Dc lambda away | 1.2531 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.11 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.13481436396058613, "-10": 1.5197856007381099e-07, "-11": 1.706155045930167e-08, "-12": 1.7596295234546057e-09, "-13": 1.6775840341478332e-10, "-14": 1.4772621543024632e-11, "-15": 1.091078433462173e-12, "-2": 0.06987667330714865, "-3": 0.025380822604626638, "-4": 0.007277789782250772, "-5": 0.0017163054236613187, "-6": 0.0003429187333708667, "-7": 5.935590015902235e-05, "-8": 9.055008192213918e-06, "-9": 1.2342236879617013e-06, "0": 0.2388405101962824, "1": 0.2511205487105321, "10": 2.1118085026666534e-06, "11": 2.9680278749131983e-07, "12": 3.832198463221805e-08, "13": 4.573917304428993e-09, "14": 5.042418271904292e-10, "15": 4.662453777011725e-11, "2": 0.16091119307437765, "3": 0.0731706645748512, "4": 0.02626685547959852, "5": 0.007754975398473882, "6": 0.0019397882854861395, "7": 0.000420343454269439, "8": 8.027984264691414e-05, "9": 1.3698998377616314e-05} |
| Raw goal margin distribution | {"-1": 0.1657484659826816, "-10": 1.868511073631257e-07, "-11": 2.0976442960797046e-08, "-12": 2.1633888677893805e-09, "-13": 2.0625174651147232e-10, "-14": 1.816230323954867e-11, "-15": 1.341434037889416e-12, "-2": 0.08591036643557463, "-3": 0.031204630489710488, "-4": 0.008947729727858702, "-5": 0.0021101237492229543, "-6": 0.00042160384356048573, "-7": 7.297552804725916e-05, "-8": 1.1132743375615792e-05, "-9": 1.5174249757165887e-06, "0": 0.2690366022247212, "1": 0.2101338956007095, "10": 1.7671295706651732e-06, "11": 2.483601054591229e-07, "12": 3.2067259964460114e-08, "13": 3.827385159320697e-09, "14": 4.21941971759879e-10, "15": 3.90147114703491e-11, "2": 0.13464806452558833, "3": 0.06122811084062216, "4": 0.02197970932865116, "5": 0.006489246695010252, "6": 0.001623185641967053, "7": 0.0003517370760355916, "8": 6.717696405264556e-05, "9": 1.1463115661771354e-05} |
| Unadjusted home-win probability | 43.7% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 29.4% |
| Raw p over 1 5 | 78.3% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.6% |
| P home draw | 76.1% |
| P draw away | 47.8% |
| P home away | 76.1% |
| Raw p home draw | 70.6% |
| Raw p draw away | 56.3% |
| Raw p home away | 73.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -8.5% |
| Draw probability edge | +3.0% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -3.5% |
| Under 2.5 probability edge | +3.5% |
| Raw edge prob home | -0.1703 |
| Raw ev home | -0.2928 |
| Raw edge prob draw | 0.0604 |
| Raw ev draw | 0.1649 |
| Raw edge prob away | 0.1099 |
| Raw ev away | 0.4339 |
| Elo home rating | 1,386.8335 |
| Elo away rating | 1,458.5707 |
| Elo rating diff | -11.7372 |
| Elo home expectancy | 0.4831 |

</details>


---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **45.2%**. Expected goals are 1.03 for Liverpool and 1.46 for Arsenal (2.49 combined). The most likely exact score is 1-1 at 12.8%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 45.9%; Under 3.5 goals: 76.0%; Double Chance 1X: 54.8%; Double Chance X2: 72.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.1%; BTTS Yes (both teams score): 50.2%; BTTS No (at least one team does not score): 49.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 28.0% | 3.57 |
| Draw | 26.9% | 3.72 |
| Arsenal win | 45.2% | 2.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.03 |
| Arsenal expected goals | 1.46 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 72.2% |
| Under 1.5 | 27.8% |
| Over 2.5 | 45.9% |
| Under 2.5 | 54.1% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.9% |
| Under 4.5 | 89.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.79% |
| 2 | 0-1 | 10.83% |
| 3 | 1-2 | 8.97% |
| 4 | 0-0 | 8.85% |
| 5 | 0-2 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 28.0% | 30.2% | 3.11 | -13.0% |
| Draw | 26.9% | 25.2% | 3.65 | -1.9% |
| Arsenal win | 45.2% | 44.6% | 2.20 | -0.7% |
| Over 2.5 | 45.9% | 55.2% | 1.81 | -16.9% |
| Under 2.5 | 54.1% | 44.8% | 2.15 | +16.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:30:00+00:00 |
| Fixture id | 6a3819cdbe2ba2fe5a3d8f9b4b459965 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-23T14:29:29Z |
| Market best draw last update utc | 2026-10-23T14:29:29Z |
| Market best away last update utc | 2026-10-23T14:29:29Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Liverpool |
| Matched away-team name | Arsenal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0335 |
| Dc lambda away | 1.4555 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T14:29:21.316153+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.2% |
| P btts no | 49.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.29 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.60 |
| Fair Over 2.5 odds | 2.18 |
| Fair Under 2.5 odds | 1.85 |
| Fair Over 3.5 odds | 4.16 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.19 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.22357623295950113, "-10": 1.104563773304995e-06, "-11": 1.4452721825041352e-07, "-12": 1.736436914188398e-08, "-13": 1.9280889082013777e-09, "-14": 1.9819810701837837e-10, "-15": 1.7479497260838418e-11, "-2": 0.13942607712205013, "-3": 0.060563208168842635, "-4": 0.020562994629855495, "-5": 0.005709448587684688, "-6": 0.0013383566738034668, "-7": 0.0002711545826207273, "-8": 4.834120531238729e-05, "-9": 7.691265123322118e-06, "0": 0.26872320072640893, "1": 0.17135021631584157, "10": 3.962783031825942e-08, "11": 3.6816327231216286e-09, "12": 3.1407339259842213e-10, "13": 2.47617030236533e-11, "14": 1.8073167557766257e-12, "15": 1.1317357335539395e-13, "2": 0.07742887703060454, "3": 0.023880814953058903, "4": 0.00575715538520326, "5": 0.0011350031688220918, "6": 0.00018891049879580534, "7": 2.7175809704284222e-05, "8": 3.44004669115223e-06, "9": 3.886207297634901e-07} |
| Raw goal margin distribution | {"-1": 0.22636957805540375, "-10": 1.1183641122696116e-06, "-11": 1.4633293074042297e-07, "-12": 1.7581318299421266e-08, "-13": 1.952178309945454e-09, "-14": 2.00674379665647e-10, "-15": 1.7697884820670195e-11, "-2": 0.14116805632804363, "-3": 0.06131988046039702, "-4": 0.0208199071802015, "-5": 0.0057807820205885594, "-6": 0.0013550780041606816, "-7": 0.0002745423681360702, "-8": 4.894517679451633e-05, "-9": 7.787359227016093e-06, "0": 0.2856959461083565, "1": 0.15750007622088263, "10": 3.6424735432429327e-08, "11": 3.3840484533741653e-09, "12": 2.8868701970018717e-10, "13": 2.276022871424702e-11, "14": 1.6612323749005995e-12, "15": 1.040258180754702e-13, "2": 0.07117034513419589, "3": 0.021950542323160408, "4": 0.005291807804395214, "5": 0.0010432615110967673, "6": 0.00017364097109992123, "7": 2.4979204531026077e-05, "8": 3.1619896823543173e-06, "9": 3.5720873818999646e-07} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 45.7% |
| Raw p over 1 5 | 72.2% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 50.5% |
| P home draw | 54.8% |
| P draw away | 72.0% |
| P home away | 73.1% |
| Raw p home draw | 54.3% |
| Raw p draw away | 74.3% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T14:28:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T14:29:29Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.00 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.10 |
| Market reference 1x2 last update utc | 2026-10-23T14:29:31Z |
| Market reference home last update utc | 2026-10-23T14:29:31Z |
| Market reference draw last update utc | 2026-10-23T14:29:31Z |
| Market reference away last update utc | 2026-10-23T14:29:31Z |
| O/U 2.5 market source | The Odds API / Unibet (NL) |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market reference under 2 5 last update utc | 2026-10-23T14:29:31Z |
| Market best over 2 5 last update utc | 2026-10-23T14:28:00Z |
| Market best under 2 5 last update utc | 2026-10-23T14:28:00Z |
| Home probability edge | -2.3% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0452 |
| Raw ev home | -0.2002 |
| Raw edge prob draw | 0.0339 |
| Raw ev draw | 0.0428 |
| Raw edge prob away | 0.0113 |
| Raw ev away | 0.0057 |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,646.9660 |
| Elo rating diff | -28.8787 |
| Elo home expectancy | 0.4585 |

</details>


---
