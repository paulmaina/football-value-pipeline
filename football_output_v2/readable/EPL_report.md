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
| Training as of utc | 2026-10-23T16:19:46.649991+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 80, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-23T16:19:46.649991+00:00', 'observations': 213, 'observations_sha256': 'f306d8741b34e2c16b88c23b5e83c943e663bd665f7143ef456fe9000b8ffd9f', 'eligible_training_matches': 127, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 119, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 127, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'e5ec6566177f405633f071ef4b1e25cf1c1ad76b7f644c2551e2da5e2ac7c794', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 64, 'tuning_matches': 22, 'audit_matches': 41, 'tuning_origin_utc': '2025-09-13T00:00:00+00:00', 'audit_origin_utc': '2025-10-04T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 35, 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 924.800 |
| Base scoring parameter | 0.213 |
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
| Bbs statistics model artifact | bbs/feature_models/EPL/20261023T161946649991Z_0e5fbb5351b5055f8fbad99b97fcb78dd19d57847231cab0eeae42374cea183b.json |
| Over 1 5 in window quote fixtures | 0 |
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

The model's most likely 1X2 outcome is **Nottingham Forest win** at **44.2%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.7%; Under 3.5 goals: 64.5%; Double Chance 1X: 55.8%; Double Chance X2: 70.5%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.5% | 3.39 |
| Draw | 26.3% | 3.81 |
| Nottingham Forest win | 44.2% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Ipswich Town expected goals | 1.32 |
| Nottingham Forest expected goals | 1.69 |
| Expected total goals | 3.01 |
| Over 0.5 | 94.0% |
| Under 0.5 | 6.0% |
| Over 1.5 | 81.2% |
| Under 1.5 | 18.8% |
| Over 2.5 | 57.7% |
| Under 2.5 | 42.3% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.21% |
| 2 | 1-2 | 9.09% |
| 3 | 2-1 | 7.38% |
| 4 | 0-1 | 7.18% |
| 5 | 0-2 | 6.88% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.5% | 30.0% | 3.26 | -3.7% |
| Draw | 26.3% | 26.8% | 3.52 | -7.5% |
| Nottingham Forest win | 44.2% | 43.2% | 2.29 | +1.2% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3214 |
| Dc lambda away | 1.6905 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.62 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.38 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.20354129280251, "-10": 3.0917928723170374e-06, "-11": 4.673444266223245e-07, "-12": 6.491617639526504e-08, "-13": 8.336245079028819e-09, "-14": 9.872333725243753e-10, "-15": 9.683800036659727e-11, "-2": 0.13662341394144453, "-3": 0.06588050475858055, "-4": 0.025212506878971787, "-5": 0.007960331065338158, "-6": 0.0021335362660700654, "-7": 0.0004960343391400033, "-8": 0.00010173489720401904, "-9": 1.8654889735856454e-05, "0": 0.2627125596934575, "1": 0.1631024217677737, "10": 2.735476737555941e-07, "11": 3.2321268165229316e-08, "12": 3.509400606728442e-09, "13": 3.5227285540834553e-10, "14": 3.261048244725588e-11, "15": 2.500413871076671e-12, "2": 0.08671979527877247, "3": 0.03268727517216692, "4": 0.009778371237076795, "5": 0.002413294439188125, "6": 0.0005056009739967771, "7": 9.188577982546467e-05, "8": 1.4731100891633149e-05, "9": 2.1114783375390896e-06} |
| Raw goal margin distribution | {"-1": 0.20805096675293733, "-10": 3.1602948336853067e-06, "-11": 4.776989397414928e-07, "-12": 6.635446336701538e-08, "-13": 8.520943460176226e-09, "-14": 1.0091065785051656e-09, "-15": 9.898354931959738e-11, "-2": 0.13965045107178248, "-3": 0.06734015745145717, "-4": 0.0257711167999935, "-5": 0.008136700671465028, "-6": 0.002180807032551458, "-7": 0.0005070245078027696, "-8": 0.00010398894211772369, "-9": 1.9068208670464535e-05, "0": 0.2576543725872822, "1": 0.16048775034168233, "10": 2.6916247040612527e-07, "11": 3.180313057161966e-08, "12": 3.453141911182e-09, "13": 3.466256200133049e-10, "14": 3.208770850115656e-11, "15": 2.4603300965302996e-12, "2": 0.08532960273390186, "3": 0.032163270172957656, "4": 0.009621615576491318, "5": 0.0023746072637035416, "6": 0.0004974957576217832, "7": 9.041277212656099e-05, "8": 1.4494948735467972e-05, "9": 2.077629532499059e-06} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 55.8% |
| P draw away | 70.5% |
| P home away | 73.7% |
| Raw p home draw | 54.8% |
| Raw p draw away | 70.9% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.25, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.11, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.48, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 7.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.11, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.11, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 3.10 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | +3.1% |
| Under 2.5 probability edge | -3.1% |
| Raw edge prob home | -0.0095 |
| Raw ev home | -0.0527 |
| Raw edge prob draw | -0.0101 |
| Raw ev draw | -0.0931 |
| Raw edge prob away | 0.0196 |
| Raw ev away | 0.0345 |
| Market p home draw | 57.5% |
| Market home draw odds | 1.69 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:23Z |
| Market reference home draw last update utc | 2026-10-23T16:19:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 70.0% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:23Z |
| Market reference draw away last update utc | 2026-10-23T16:19:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:23Z |
| Market reference home away last update utc | 2026-10-23T16:19:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.9% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.44 |
| Market reference under 3 5 opposite odds | 2.91 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:23Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-23T16:19:48Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,345.2452 |
| Elo away rating | 1,480.4097 |
| Elo rating diff | -75.1645 |
| Elo home expectancy | 0.3935 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **66.1%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 16.9%. Goal-market probabilities: at least one goal: 90.0%; Over 2.5 goals: 41.0%; Under 3.5 goals: 79.8%; Double Chance 1X: 88.5%; Double Chance X2: 33.9%; Double Chance 12 (either team wins): 77.6%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 36.3%; BTTS No (at least one team does not score): 63.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 66.1% | 1.51 |
| Draw | 22.4% | 4.46 |
| Everton win | 11.5% | 8.73 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.0% |
| Under 0.5 | 10.0% |
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
| 1 | 1-0 | 16.92% |
| 2 | 2-0 | 15.31% |
| 3 | 0-0 | 10.01% |
| 4 | 1-1 | 9.91% |
| 5 | 2-1 | 8.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 66.1% | 68.0% | 1.45 | -4.1% |
| Draw | 22.4% | 20.2% | 4.34 | -2.7% |
| Everton win | 11.5% | 11.8% | 8.28 | -5.2% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Arsenal |
| Matched away-team name | Everton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7158 |
| Dc lambda away | 0.5763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.3% |
| P btts no | 63.7% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.99 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.12 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.96 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.78 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.08586480508551836, "-10": 1.269585543275742e-10, "-11": 6.602596723111779e-12, "-12": 3.1511608884837567e-13, "-13": 1.3894765012739126e-14, "-14": 5.693008445522139e-16, "-15": 2.1747330135137764e-17, "-16": 7.377491745904149e-19, "-2": 0.02376219555228129, "-3": 0.004232106790504992, "-4": 0.0005818938375924048, "-5": 6.497851073689798e-05, "-6": 6.100278658868211e-06, "-7": 4.936480018154901e-07, "-8": 3.508595818934939e-08, "-9": 2.2225599300166095e-09, "0": 0.22430152740074452, "1": 0.27325404371073775, "10": 6.929674637034534e-06, "11": 1.0728990671163135e-06, "12": 1.5244314263219654e-07, "13": 2.001159672041034e-08, "14": 2.4409876606197822e-09, "15": 2.776022126463438e-10, "16": 2.8036185732785833e-11, "2": 0.21018014165336532, "3": 0.11144355380562437, "4": 0.04561790252757093, "5": 0.015165423004853905, "6": 0.004238651095331286, "7": 0.0010211477827613321, "8": 0.0002160716442804953, "9": 4.074845395704854e-05} |
| Raw goal margin distribution | {"-1": 0.08327342692309228, "-10": 1.2312697717684302e-10, "-11": 6.403332019179395e-12, "-12": 3.0560596475902964e-13, "-13": 1.3475424508906473e-14, "-14": 5.521194886409765e-16, "-15": 2.1091001196323568e-17, "-16": 7.154840905611975e-19, "-2": 0.02304505848332561, "-3": 0.00410438287490247, "-4": 0.0005643324283271603, "-5": 6.301747567040176e-05, "-6": 5.916173787430369e-06, "-7": 4.787498296184432e-07, "-8": 3.4027072819853474e-08, "-9": 2.155483631857056e-09, "0": 0.24640932232706486, "1": 0.2655456380381652, "10": 6.73419082074472e-06, "11": 1.0426329413428484e-06, "12": 1.4814277229017612e-07, "13": 1.9447076233971944e-08, "14": 2.3721282107310207e-09, "15": 2.697711465745568e-10, "16": 2.7245294259762737e-11, "2": 0.20425102977570922, "3": 0.10829976822550576, "4": 0.044331036672489096, "5": 0.014737611466806449, "6": 0.00411908015795883, "7": 0.0009923415435039735, "8": 0.0002099763350735912, "9": 3.9598953626273626e-05} |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 88.5% |
| P draw away | 33.9% |
| P home away | 77.6% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:27Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 6.49, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:27Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.14, "price": 6.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.08, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.83, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.55, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.08, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.43 |
| Reference draw odds | 4.40 |
| Reference away odds | 7.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -1.9% |
| Draw probability edge | +2.2% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -11.2% |
| Under 2.5 probability edge | +11.2% |
| Raw edge prob home | -0.0373 |
| Raw ev home | -0.0683 |
| Raw edge prob draw | 0.0442 |
| Raw ev draw | 0.0694 |
| Raw edge prob away | -0.0069 |
| Raw ev away | -0.0805 |
| Market p home draw | 87.5% |
| Market home draw odds | 1.11 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:27Z |
| Market reference home draw last update utc | 2026-10-23T16:19:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 34.3% |
| Market draw away odds | 2.92 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:27Z |
| Market reference draw away last update utc | 2026-10-23T16:19:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:27Z |
| Market reference home away last update utc | 2026-10-23T16:19:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.10 |
| Market reference dc draw away odds | 2.81 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 77.5% |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 71.3% |
| Market under 3 5 odds | 1.37 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.37 |
| Market reference under 3 5 opposite odds | 3.19 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 46.5% |
| Market btts yes odds | 2.11 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:27Z |
| Market reference btts yes odds | 2.12 |
| Market reference btts yes opposite odds | 1.85 |
| Market reference btts yes last update utc | 2026-10-23T16:19:48Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,645.3362 |
| Elo away rating | 1,482.5802 |
| Elo rating diff | 222.7561 |
| Elo home expectancy | 0.7828 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **56.2%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 10.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 57.4%; Under 3.5 goals: 65.6%; Double Chance 1X: 43.8%; Double Chance X2: 78.9%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 56.9%; BTTS No (at least one team does not score): 43.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.1% | 4.73 |
| Draw | 22.6% | 4.42 |
| Manchester City win | 56.2% | 1.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.4% |
| Under 2.5 | 42.6% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.67% |
| 2 | 1-2 | 10.44% |
| 3 | 0-2 | 9.30% |
| 4 | 0-1 | 9.18% |
| 5 | 1-3 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.1% | 19.9% | 4.98 | +5.2% |
| Draw | 22.6% | 20.4% | 4.43 | +0.3% |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1220 |
| Dc lambda away | 1.8244 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 56.9% |
| P btts no | 43.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.67 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.74 |
| Fair Under 2.5 odds | 2.35 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.23849282204022, "-10": 7.567605446581582e-06, "-11": 1.2361685256373067e-06, "-12": 1.855267826941447e-07, "-13": 2.5748820208970403e-08, "-14": 3.32223076138212e-09, "-15": 3.979733057693745e-10, "-16": 4.0231143765014255e-11, "-2": 0.17515668456148256, "-3": 0.09217237100383105, "-4": 0.03835373236144168, "-5": 0.01313807626700493, "-6": 0.0038152082530309435, "-7": 0.0009601824373825687, "-8": 0.0002130402465781215, "-9": 4.2241195063848243e-05, "0": 0.226420027559617, "1": 0.12705074338671812, "10": 5.212451416491723e-08, "11": 5.236314462213492e-09, "12": 4.833026212172969e-10, "13": 4.1250989554755207e-11, "14": 3.273190866285572e-12, "15": 2.4113484769596083e-13, "16": 1.499107970982525e-14, "2": 0.058964994464746276, "3": 0.019082391616985266, "4": 0.004883196240743597, "5": 0.0010287096693743347, "6": 0.00018371465070055637, "7": 2.8434382396493653e-05, "8": 3.879861268079392e-06, "9": 4.731024928001933e-07} |
| Raw goal margin distribution | {"-1": 0.22412046904137245, "-10": 7.111556933658499e-06, "-11": 1.1616729904487126e-06, "-12": 1.743463354638669e-07, "-13": 2.4197112571896235e-08, "-14": 3.1220223323076327e-09, "-15": 3.739901402145172e-10, "-16": 3.780668421611992e-11, "-2": 0.16460117316667486, "-3": 0.08661776419648491, "-4": 0.03604241172878548, "-5": 0.012346333068111792, "-6": 0.003585291397221213, "-7": 0.000902318721337359, "-8": 0.00020020174854455843, "-9": 3.969560328730237e-05, "0": 0.24853001329408894, "1": 0.13413585222582664, "10": 5.503128862526013e-08, "11": 5.5283226543077e-09, "12": 5.10254464097336e-10, "13": 4.3551391291302014e-11, "14": 3.455723552995011e-12, "15": 2.545819680770474e-13, "16": 1.5827071916785973e-14, "2": 0.062253234992458405, "3": 0.020146539829839927, "4": 0.005155512450205547, "5": 0.001086076669181456, "6": 0.00019395967769414356, "7": 3.0020053512472733e-05, "8": 4.0962255224884524e-06, "9": 4.994855155530798e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 43.8% |
| P draw away | 78.9% |
| P home away | 77.4% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.5, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 7.9, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.62, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.8, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.41, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +1.2% |
| Draw probability edge | +2.2% |
| Away probability edge | -3.4% |
| Over 2.5 probability edge | -7.0% |
| Under 2.5 probability edge | +7.0% |
| Raw edge prob home | 0.0236 |
| Raw ev home | 0.1106 |
| Raw edge prob draw | 0.0442 |
| Raw ev draw | 0.1010 |
| Raw edge prob away | -0.0678 |
| Raw ev away | -0.1333 |
| Market p home draw | 42.6% |
| Market home draw odds | 2.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:24Z |
| Market reference home draw last update utc | 2026-10-23T16:19:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.0% |
| Market draw away odds | 1.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:24Z |
| Market reference draw away last update utc | 2026-10-23T16:19:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.4% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:24Z |
| Market reference home away last update utc | 2026-10-23T16:19:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.27 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 84.8% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.96 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.3% |
| Market under 3 5 odds | 1.67 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.30 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.5% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:24Z |
| Market reference btts yes odds | 1.57 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-23T16:19:25Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,517.7051 |
| Elo away rating | 1,655.9177 |
| Elo rating diff | -78.2126 |
| Elo home expectancy | 0.3893 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.1%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 9.9%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.0%; Double Chance X2: 42.9%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.1% | 1.75 |
| Draw | 21.9% | 4.57 |
| Tottenham Hotspur win | 21.0% | 4.75 |

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
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.86% |
| 2 | 2-1 | 9.59% |
| 3 | 2-0 | 8.04% |
| 4 | 3-1 | 6.82% |
| 5 | 1-0 | 6.73% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.1% | 56.1% | 1.74 | -0.7% |
| Draw | 21.9% | 21.7% | 4.25 | -6.9% |
| Tottenham Hotspur win | 21.0% | 22.2% | 4.40 | -7.5% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1330 |
| Dc lambda away | 1.1933 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.92 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.36 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.12513114099587416, "-10": 7.727887338748888e-08, "-11": 8.227014747438899e-09, "-12": 8.051298250722549e-10, "-13": 7.289542332844302e-11, "-14": 6.139373451728283e-12, "-15": 4.830870265824285e-13, "-16": 3.537399860893373e-14, "-17": 2.1596375982628965e-15, "-2": 0.05884094362932822, "-3": 0.019671658249774918, "-4": 0.005249875997015107, "-5": 0.0011598943003982025, "-6": 0.00021802138174651574, "-7": 3.560115834008359e-05, "-8": 5.1336264747627925e-06, "-9": 6.623291307760706e-07, "0": 0.2189492206663652, "1": 0.21372357294540908, "10": 2.3868974619624195e-05, "11": 4.542272904614019e-06, "12": 7.94611470091058e-07, "13": 1.286018287515184e-07, "14": 1.9361049754504798e-08, "15": 2.7232542548567994e-09, "16": 3.5645518622318354e-10, "17": 3.890089831084266e-11, "2": 0.17433672061050653, "3": 0.10418571620434201, "4": 0.049702040989052856, "5": 0.019629152959900555, "6": 0.0065953857225505745, "7": 0.001925143945614926, "8": 0.0004962280529424397, "9": 0.00011444290417659725} |
| Raw goal margin distribution | {"-1": 0.11799915835239409, "-10": 7.287428169815524e-08, "-11": 7.758107280285512e-09, "-12": 7.592405932434427e-10, "-13": 6.874067104352037e-11, "-14": 5.7894533235244476e-12, "-15": 4.555529670233467e-13, "-16": 3.3357819885543664e-14, "-17": 2.036546753374606e-15, "-2": 0.05548724138262534, "-3": 0.01855045113786588, "-4": 0.004950653723541482, "-5": 0.0010937848894803863, "-6": 0.00020559502090501298, "-7": 3.3572032405895604e-05, "-8": 4.841029966613592e-06, "-9": 6.245789765988468e-07, "0": 0.22123470510144544, "1": 0.2173564947480216, "10": 2.4274704867844344e-05, "11": 4.619483490424333e-06, "12": 8.081184562157806e-07, "13": 1.3078783182590351e-07, "14": 1.9690153272686076e-08, "15": 2.7695447487886674e-09, "16": 3.625142923846517e-10, "17": 3.956214460982144e-11, "2": 0.17730013575734035, "3": 0.10595668865582838, "4": 0.05054688756285401, "5": 0.019962813757219602, "6": 0.0067074955860433275, "7": 0.0019578679793600404, "8": 0.0005046630500172033, "9": 0.00011638823063735062} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.0% |
| P draw away | 42.9% |
| P home away | 78.1% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.55, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 8.45, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.29, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.64, "price": 1.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.93, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.48, "price": 2.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 8.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.89, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.59, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.55, "price": 2.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.88, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.72 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +1.0% |
| Draw probability edge | +0.2% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | +0.3% |
| Under 2.5 probability edge | -0.3% |
| Raw edge prob home | 0.0194 |
| Raw ev home | 0.0100 |
| Raw edge prob draw | 0.0046 |
| Raw ev draw | -0.0598 |
| Raw edge prob away | -0.0240 |
| Raw ev away | -0.1274 |
| Market p home draw | 75.3% |
| Market home draw odds | 1.23 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:23Z |
| Market reference home draw last update utc | 2026-10-23T16:19:48Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 49.9% |
| Market draw away odds | 2.17 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:23Z |
| Market reference draw away last update utc | 2026-10-23T16:19:48Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.7% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:23Z |
| Market reference home away last update utc | 2026-10-23T16:19:48Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.18 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.9% |
| Market under 3 5 odds | 1.65 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.65 |
| Market reference under 3 5 opposite odds | 2.32 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 62.4% |
| Market btts yes odds | 1.54 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:23Z |
| Market reference btts yes odds | 1.52 |
| Market reference btts yes opposite odds | 2.38 |
| Market reference btts yes last update utc | 2026-10-23T16:19:48Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,507.4574 |
| Elo away rating | 1,444.7579 |
| Elo rating diff | 122.6995 |
| Elo home expectancy | 0.6696 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **42.3%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.4%; Under 3.5 goals: 76.4%; Double Chance 1X: 57.7%; Double Chance X2: 69.8%; Double Chance 12 (either team wins): 72.5%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 50.5%; BTTS No (at least one team does not score): 49.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 30.2% | 3.31 |
| Draw | 27.5% | 3.64 |
| Fulham win | 42.3% | 2.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.4% |
| Under 2.5 | 54.6% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.07% |
| 2 | 0-1 | 10.60% |
| 3 | 0-0 | 9.04% |
| 4 | 1-2 | 8.84% |
| 5 | 1-0 | 8.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 30.2% | 31.4% | 3.20 | -3.4% |
| Draw | 27.5% | 25.7% | 3.54 | -2.8% |
| Fulham win | 42.3% | 42.9% | 2.28 | -3.4% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Coventry |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1008 |
| Dc lambda away | 1.3668 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.5% |
| P btts no | 49.5% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.06 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.55 |
| Fair Over 2.5 odds | 2.20 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.23 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.41 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21956765953426416, "-10": 6.175915526993187e-07, "-11": 7.587957696645109e-08, "-12": 8.559010212729139e-09, "-13": 8.882412398864253e-10, "-14": 7.830078371784936e-11, "-2": 0.12898349864218642, "-3": 0.052608962602913464, "-4": 0.016772602791640487, "-5": 0.004372933988677339, "-6": 0.0009625341586049389, "-7": 0.00018311643641995287, "-8": 3.0654507579706044e-05, "-9": 4.579746305639424e-06, "0": 0.2745073435881694, "1": 0.17898361173289368, "10": 7.272305104770836e-08, "11": 7.196392245482357e-09, "12": 6.537815379438116e-10, "13": 5.46461063283401e-11, "14": 3.87983789626369e-12, "2": 0.08577316611214308, "3": 0.02817709449259431, "4": 0.007235292858307654, "5": 0.0015193147558148193, "6": 0.0002693457746660706, "7": 4.127057561761979e-05, "8": 5.564507399895916e-06, "9": 6.695653687856382e-07} |
| Raw goal margin distribution | {"-1": 0.21650117896716198, "-10": 6.089662729164215e-07, "-11": 7.481984326659243e-08, "-12": 8.43947512934466e-09, "-13": 8.75836068256013e-10, "-14": 7.720723545956323e-11, "-2": 0.1271821159025695, "-3": 0.051874226158487025, "-4": 0.016538356725396556, "-5": 0.00431186161979595, "-6": 0.0009490914125338878, "-7": 0.0001805590334080983, "-8": 3.022638691755277e-05, "-9": 4.5157855972259445e-06, "0": 0.2919395117394417, "1": 0.17215761442955554, "10": 6.994957170210776e-08, "11": 6.921939441754528e-09, "12": 6.288479087038528e-10, "13": 5.2562037452850835e-11, "14": 3.731870365824043e-12, "2": 0.0825019872879387, "3": 0.027102489006873162, "4": 0.0069593564803258874, "5": 0.0014613718060346424, "6": 0.00025907358542072293, "7": 3.9696616777782e-05, "8": 5.352290693917387e-06, "9": 6.440297828317685e-07} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.8% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.9% |
| P home draw | 57.7% |
| P draw away | 69.8% |
| P home away | 72.5% |
| Raw p home draw | 58.2% |
| Raw p draw away | 71.0% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.01, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.95, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.5, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.01, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.08 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -1.2% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -9.3% |
| Under 2.5 probability edge | +9.3% |
| Raw edge prob home | -0.0230 |
| Raw ev home | -0.0704 |
| Raw edge prob draw | 0.0349 |
| Raw ev draw | 0.0335 |
| Raw edge prob away | -0.0118 |
| Raw ev away | -0.0479 |
| Market p home draw | 57.3% |
| Market home draw odds | 1.68 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:23Z |
| Market reference home draw last update utc | 2026-10-23T16:19:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.8% |
| Market draw away odds | 1.38 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:23Z |
| Market reference draw away last update utc | 2026-10-23T16:19:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.33 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:23Z |
| Market reference home away last update utc | 2026-10-23T16:19:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.38 |
| Market reference dc home away odds | 1.32 |
| Market p over 1 5 | 79.6% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 67.4% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.87 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.5% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:23Z |
| Market reference btts yes odds | 1.66 |
| Market reference btts yes opposite odds | 2.42 |
| Market reference btts yes last update utc | 2026-10-23T16:19:48Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,374.3497 |
| Elo away rating | 1,443.1425 |
| Elo rating diff | -8.7928 |
| Elo home expectancy | 0.4873 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.5%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.5%; Over 2.5 goals: 59.6%; Under 3.5 goals: 63.0%; Double Chance 1X: 59.5%; Double Chance X2: 65.8%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 80.1%; BTTS Yes (both teams score): 62.4%; BTTS No (at least one team does not score): 37.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.2% | 2.92 |
| Draw | 25.3% | 3.95 |
| Newcastle United win | 40.5% | 2.47 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.58 |
| Expected total goals | 3.08 |
| Over 0.5 | 94.5% |
| Under 0.5 | 5.5% |
| Over 1.5 | 82.2% |
| Under 1.5 | 17.8% |
| Over 2.5 | 59.6% |
| Under 2.5 | 40.4% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.9% |
| Under 4.5 | 80.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.61% |
| 2 | 1-2 | 8.97% |
| 3 | 2-1 | 7.93% |
| 4 | 0-1 | 6.58% |
| 5 | 2-2 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.2% | 33.3% | 2.99 | +2.4% |
| Draw | 25.3% | 24.7% | 3.69 | -6.7% |
| Newcastle United win | 40.5% | 42.0% | 2.33 | -5.7% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4954 |
| Dc lambda away | 1.5799 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.4% |
| P btts no | 37.6% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.30 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.62 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.47 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1985594946406097, "-10": 1.5871928859496154e-06, "-11": 2.2401712671159311e-07, "-12": 2.905895551305012e-08, "-13": 3.4849403337870667e-09, "-14": 3.851168046655502e-10, "-15": 3.5044019737352995e-11, "-2": 0.12353914819461381, "-3": 0.055258723294617375, "-4": 0.0196646629341435, "-5": 0.005781751360181577, "-6": 0.0014443960308301313, "-7": 0.0003132012475028943, "-8": 5.9936851181214444e-05, "-9": 1.0258030668078405e-05, "0": 0.25291563280724766, "1": 0.17514794446121576, "10": 8.560077262341647e-07, "11": 1.1435341644009437e-07, "12": 1.4040024541659676e-08, "13": 1.5936874731446876e-09, "14": 1.6669409935525406e-10, "15": 1.4356931188603913e-11, "2": 0.1034410730130046, "3": 0.043793454691967215, "4": 0.014750774082660723, "5": 0.004104948012678891, "6": 0.0009706317241129338, "7": 0.00019921022400625393, "8": 3.608294772457813e-05, "9": 5.84510105799268e-06} |
| Raw goal margin distribution | {"-1": 0.19086689890154204, "-10": 1.5257018288050865e-06, "-11": 2.1533825090392206e-07, "-12": 2.7933152902774298e-08, "-13": 3.349926708721602e-09, "-14": 3.701966020533521e-10, "-15": 3.368634365442732e-11, "-2": 0.11875299215241579, "-3": 0.05311788877984443, "-4": 0.018902814186637393, "-5": 0.0055577546384021235, "-6": 0.0013884372121778115, "-7": 0.00030106719878176776, "-8": 5.761477654638384e-05, "-9": 9.860613847737916e-06, "0": 0.25884252662132057, "1": 0.18013432624312345, "10": 8.803778742504404e-07, "11": 1.1760900584589556e-07, "12": 1.443973761170128e-08, "13": 1.6390590257860197e-09, "14": 1.7143980403784945e-10, "15": 1.476566644577851e-11, "2": 0.10638599299799045, "3": 0.045040234294859906, "4": 0.01517072186669597, "5": 0.004221814003022459, "6": 0.0009982651648646759, "7": 0.00020488164786915006, "8": 3.711021272460333e-05, "9": 6.011508408753443e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 59.5% |
| P draw away | 65.8% |
| P home away | 74.7% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.97, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.97, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +1.0% |
| Draw probability edge | +0.6% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.0195 |
| Raw ev home | 0.0531 |
| Raw edge prob draw | 0.0119 |
| Raw ev draw | -0.0449 |
| Raw edge prob away | -0.0314 |
| Raw ev away | -0.0937 |
| Market p home draw | 61.0% |
| Market home draw odds | 1.65 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:25Z |
| Market reference home draw last update utc | 2026-10-23T16:19:56Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.0% |
| Market draw away odds | 1.43 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:25Z |
| Market reference draw away last update utc | 2026-10-23T16:19:56Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:25Z |
| Market reference home away last update utc | 2026-10-23T16:19:56Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.45 |
| Market reference dc draw away odds | 1.32 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 83.5% |
| Market reference over 1 5 odds | 1.17 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.5% |
| Market under 3 5 odds | 1.61 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.61 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 64.6% |
| Market btts yes odds | 1.47 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:25Z |
| Market reference btts yes odds | 1.47 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-23T16:19:56Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,423.3950 |
| Elo away rating | 1,440.4285 |
| Elo rating diff | 42.9664 |
| Elo home expectancy | 0.5615 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **44.5%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 40.3%; Under 3.5 goals: 81.0%; Double Chance 1X: 55.5%; Double Chance X2: 71.1%; Double Chance 12 (either team wins): 73.5%; Under 4.5 goals: 91.9%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.9% | 3.46 |
| Draw | 26.5% | 3.77 |
| Brentford win | 44.5% | 2.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.3% |
| Under 2.5 | 59.7% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.1% |
| Under 4.5 | 91.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.32% |
| 2 | 1-1 | 12.37% |
| 3 | 0-0 | 10.06% |
| 4 | 1-2 | 10.06% |
| 5 | 1-0 | 8.72% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.9% | 19.9% | 4.88 | +41.1% |
| Draw | 26.5% | 22.0% | 4.17 | +10.7% |
| Brentford win | 44.5% | 58.1% | 1.69 | -24.7% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1913 |
| Dc lambda away | 1.0536 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.94 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.26 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.42 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.26712247344178386, "-10": 7.915482801912016e-08, "-11": 7.509943781260684e-09, "-12": 6.516101991423619e-10, "-13": 4.8161849366541675e-11, "-2": 0.12575336811760823, "-3": 0.04020012314455561, "-4": 0.00998673902629537, "-5": 0.002022259687715798, "-6": 0.00034503001032797184, "-7": 5.081375881898785e-05, "-8": 6.579229139298526e-06, "-9": 7.597531680127102e-07, "0": 0.26540237132233546, "1": 0.16168265279907282, "10": 1.436292032238362e-07, "11": 1.5407618072307797e-08, "12": 1.5115418254589815e-09, "13": 1.2631907231971153e-10, "2": 0.0854313268755477, "3": 0.03087865578304064, "4": 0.008673376137609243, "5": 0.001985797142176126, "6": 0.00038307896457708435, "7": 6.378906443986475e-05, "8": 9.33841993899605e-06, "9": 1.2192826228920834e-06} |
| Raw goal margin distribution | {"-1": 0.18608604138503662, "-10": 5.514177977167314e-08, "-11": 5.231666550824828e-09, "-12": 4.539324637204055e-10, "-13": 3.355108156542055e-11, "-2": 0.0876038102010947, "-3": 0.02800468894576805, "-4": 0.006957081176300859, "-5": 0.0014087706477515323, "-6": 0.00024035891834074143, "-7": 3.53984863373175e-05, "-8": 4.583301023393551e-06, "-9": 5.292683076927177e-07, "0": 0.31066234814312355, "1": 0.21195136806040785, "10": 1.8828492475658464e-07, "11": 2.019799695540763e-08, "12": 1.9814949361617265e-09, "13": 1.6559290515573473e-10, "2": 0.11199276046633536, "3": 0.04047913133399194, "4": 0.011370013456875425, "5": 0.002603200860996089, "6": 0.0005021819546601547, "7": 8.362170734620936e-05, "8": 1.2241825868929296e-05, "9": 1.5983694941931418e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.5% |
| P home draw | 55.5% |
| P draw away | 71.1% |
| P home away | 73.5% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.5, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.35, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.11, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.73, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.29, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:00Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.78, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:00Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.29, "price": 3.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 4.50 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.66 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +9.0% |
| Draw probability edge | +4.5% |
| Away probability edge | -13.5% |
| Over 2.5 probability edge | -18.8% |
| Under 2.5 probability edge | +18.8% |
| Raw edge prob home | 0.1798 |
| Raw ev home | 0.8495 |
| Raw edge prob draw | 0.0905 |
| Raw ev draw | 0.2955 |
| Raw edge prob away | -0.2703 |
| Raw ev away | -0.4755 |
| Market p home draw | 42.6% |
| Market home draw odds | 2.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:00Z |
| Market reference home draw last update utc | 2026-10-23T16:20:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.3% |
| Market draw away odds | 1.21 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:00Z |
| Market reference draw away last update utc | 2026-10-23T16:20:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:00Z |
| Market reference home away last update utc | 2026-10-23T16:20:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.28 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.39 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:43Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.6% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.51 |
| Market reference under 3 5 opposite odds | 2.66 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.7% |
| Market btts yes odds | 1.68 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:00Z |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.25 |
| Market reference btts yes last update utc | 2026-10-23T16:20:00Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,401.6375 |
| Elo away rating | 1,497.6340 |
| Elo rating diff | -35.9965 |
| Elo home expectancy | 0.4484 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.6%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.6%; Under 3.5 goals: 62.1%; Double Chance 1X: 68.0%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 75.5%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.6% | 2.30 |
| Draw | 24.5% | 4.09 |
| Brighton and Hove Albion win | 32.0% | 3.13 |

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
| Over 2.5 | 60.6% |
| Under 2.5 | 39.4% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.17% |
| 2 | 2-1 | 9.41% |
| 3 | 1-2 | 7.53% |
| 4 | 1-0 | 6.77% |
| 5 | 2-0 | 6.39% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.6% | 46.4% | 2.11 | -8.1% |
| Draw | 24.5% | 23.3% | 4.03 | -1.4% |
| Brighton and Hove Albion win | 32.0% | 30.3% | 3.21 | +2.6% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6381 |
| Dc lambda away | 1.4736 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.36 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.79 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.54 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.85 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16573537845621067, "-10": 7.002233398559366e-07, "-11": 9.214657108831208e-08, "-12": 1.1145306687255107e-08, "-13": 1.2463110265726713e-09, "-14": 1.2838047739360597e-10, "-15": 1.0864013505698417e-11, "-2": 0.09609607037671158, "-3": 0.03997311552650428, "-4": 0.013241435203807243, "-5": 0.003626080979574323, "-6": 0.0008440180706941884, "-7": 0.00017056191674556868, "-8": 3.042422902342805e-05, "-9": 4.854117509981919e-06, "0": 0.2446846397728732, "1": 0.20834453930256785, "10": 2.2687193924397376e-06, "11": 3.318758235907904e-07, "12": 4.462114362987682e-08, "13": 5.546606384012138e-09, "14": 6.351146527025876e-10, "15": 5.974419026043438e-11, "2": 0.13354632410964334, "3": 0.061751362577164154, "4": 0.022738711014859234, "5": 0.0069218234477621925, "6": 0.0017909645946296237, "7": 0.0004023180888445217, "8": 7.97736217566308e-05, "9": 1.4148234519791681e-05} |
| Raw goal margin distribution | {"-1": 0.17432069738430092, "-10": 7.364958650678311e-07, "-11": 9.691988930372331e-08, "-12": 1.1722648793405027e-08, "-13": 1.310871639680084e-09, "-14": 1.350307614357413e-10, "-15": 1.1426784240916816e-11, "-2": 0.10107397804859868, "-3": 0.04204377749705702, "-4": 0.013927359629534874, "-5": 0.003813916926001132, "-6": 0.0008877393593259672, "-7": 0.00017939725694804685, "-8": 3.200024563340251e-05, "-9": 5.1055674256595996e-06, "0": 0.25634203006505346, "1": 0.19484713090304429, "10": 2.1217425036468546e-06, "11": 3.1037555512237696e-07, "12": 4.173040408449522e-08, "13": 5.187274616320863e-09, "14": 5.939693369830374e-10, "15": 5.5873718117783996e-11, "2": 0.1248946489431286, "3": 0.05775085763126483, "4": 0.021265604639843644, "5": 0.00647339951375082, "6": 0.0016749386088095808, "7": 0.00037625428333357326, "8": 7.460556140831194e-05, "9": 1.3231654224070382e-05} |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 68.0% |
| P draw away | 56.4% |
| P home away | 75.5% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.67, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.4, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 3.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.99, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.99, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.05 |
| Reference draw odds | 3.90 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -2.8% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.7% |
| Over 2.5 probability edge | -2.0% |
| Under 2.5 probability edge | +2.0% |
| Raw edge prob home | -0.0564 |
| Raw ev home | -0.1404 |
| Raw edge prob draw | 0.0233 |
| Raw ev draw | 0.0331 |
| Raw edge prob away | 0.0331 |
| Raw ev away | 0.0795 |
| Market p home draw | 69.8% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:19:25Z |
| Market reference home draw last update utc | 2026-10-23T16:19:31Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 55.0% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:19:25Z |
| Market reference draw away last update utc | 2026-10-23T16:19:31Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.2% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:19:25Z |
| Market reference home away last update utc | 2026-10-23T16:19:31Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.75 |
| Market reference dc home away odds | 1.28 |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:25Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.7% |
| Market under 3 5 odds | 1.63 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.63 |
| Market reference under 3 5 opposite odds | 2.36 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.0% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:19:25Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.82 |
| Market reference btts yes last update utc | 2026-10-23T16:19:48Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,540.2938 |
| Elo rating diff | 77.7935 |
| Elo home expectancy | 0.6101 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **46.2%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.7%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.5%; Under 3.5 goals: 64.0%; Double Chance 1X: 71.3%; Double Chance X2: 53.8%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 81.0%; BTTS Yes (both teams score): 60.6%; BTTS No (at least one team does not score): 39.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 46.2% | 2.16 |
| Draw | 25.1% | 3.98 |
| Bournemouth win | 28.7% | 3.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.5% |
| Under 1.5 | 18.5% |
| Over 2.5 | 58.5% |
| Under 2.5 | 41.5% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 19.0% |
| Under 4.5 | 81.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.66% |
| 2 | 2-1 | 9.15% |
| 3 | 1-2 | 7.36% |
| 4 | 1-0 | 7.23% |
| 5 | 2-0 | 7.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 46.2% | 44.4% | 2.20 | +1.7% |
| Draw | 25.1% | 25.0% | 3.70 | -7.0% |
| Bournemouth win | 28.7% | 30.6% | 3.23 | -7.5% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7644 |
| Dc lambda away | 1.2709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.6% |
| P btts no | 39.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.45 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.41 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.25 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.16215103411660683, "-10": 1.9154547684936977e-07, "-11": 2.17665111644724e-08, "-12": 2.273039787717433e-09, "-13": 2.19542143365446e-10, "-14": 1.97138783505719e-11, "-15": 1.6417995455546002e-12, "-16": 1.1438290395976208e-13, "-2": 0.08305864768691784, "-3": 0.030096276903867025, "-4": 0.008656458665729934, "-5": 0.002054312543412728, "-6": 0.00041387923266117263, "-7": 7.233385775903607e-05, "-8": 1.1152409567261888e-05, "-9": 1.5373382240894717e-06, "0": 0.25123271273348935, "1": 0.2051192276281937, "10": 4.5597676675419195e-06, "11": 7.19337541787911e-07, "12": 1.042855243441209e-07, "13": 1.3983245419133596e-08, "14": 1.743151930614858e-09, "15": 2.015377421756953e-10, "16": 1.9492631144129015e-11, "2": 0.14330817296545598, "3": 0.07208949216111152, "4": 0.02878541801479024, "5": 0.00948357073119677, "6": 0.002652479852190784, "7": 0.0006435661232262842, "8": 0.00013775055155515806, "9": 2.6361319842905772e-05} |
| Raw goal margin distribution | {"-1": 0.15090093101062285, "-10": 1.782559756397097e-07, "-11": 2.0256341980588135e-08, "-12": 2.1153353850588864e-09, "-13": 2.0431022232081148e-10, "-14": 1.834612164602156e-11, "-15": 1.527890841441345e-12, "-16": 1.064469726835927e-13, "-2": 0.07729600574379301, "-3": 0.028008185266836436, "-4": 0.008055870127687572, "-5": 0.001911783523778542, "-6": 0.0003851641272273376, "-7": 6.731530599785805e-05, "-8": 1.0378650965009415e-05, "-9": 1.4306770879209568e-06, "0": 0.2528437593848963, "1": 0.2132252554160691, "10": 4.7399633705325155e-06, "11": 7.477647651643766e-07, "12": 1.0840674383183708e-07, "13": 1.4535843911448701e-08, "14": 1.812038880665515e-09, "15": 2.0950223461880793e-10, "16": 2.0262952929854174e-11, "2": 0.148971513480726, "3": 0.0749383690481239, "4": 0.02992297786723104, "5": 0.00985834831184712, "6": 0.002757302182292435, "7": 0.0006689989650838189, "8": 0.0001431942625695408, "9": 2.7403082692944382e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 71.3% |
| P draw away | 53.8% |
| P home away | 74.9% |
| Raw p home draw | 73.3% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.08, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.14, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.42, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.5, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:41Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.07, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.57, "price": 1.56, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:00Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 2.39, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:20:00Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.61, "price": 2.39, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +1.8% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -0.7% |
| Under 2.5 probability edge | +0.7% |
| Raw edge prob home | 0.0365 |
| Raw ev home | 0.0571 |
| Raw edge prob draw | 0.0032 |
| Raw ev draw | -0.0645 |
| Raw edge prob away | -0.0398 |
| Raw ev away | -0.1388 |
| Market p home draw | 70.0% |
| Market home draw odds | 1.38 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-23T16:20:00Z |
| Market reference home draw last update utc | 2026-10-23T16:20:00Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-23T16:20:00Z |
| Market reference draw away last update utc | 2026-10-23T16:20:00Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-23T16:20:00Z |
| Market reference home away last update utc | 2026-10-23T16:20:00Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.38 |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.37 |
| Market reference over 1 5 last update utc | 2026-10-23T16:19:41Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.0% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.61 |
| Market reference under 3 5 last update utc | 2026-10-23T16:19:50Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 61.6% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-23T16:20:00Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.47 |
| Market reference btts yes last update utc | 2026-10-23T16:20:00Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,529.3488 |
| Elo away rating | 1,499.8325 |
| Elo rating diff | 89.5163 |
| Elo home expectancy | 0.6260 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.3%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.0%. Goal-market probabilities: at least one goal: 88.9%; Over 2.5 goals: 40.2%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.7%; Double Chance X2: 68.1%; Double Chance 12 (either team wins): 70.2%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.1%; BTTS No (at least one team does not score): 52.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 31.9% | 3.14 |
| Draw | 29.8% | 3.35 |
| Leeds United win | 38.3% | 2.61 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.9% |
| Under 0.5 | 11.1% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.98% |
| 2 | 0-1 | 11.25% |
| 3 | 0-0 | 11.06% |
| 4 | 1-0 | 10.01% |
| 5 | 1-2 | 8.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 31.9% | 32.7% | 3.01 | -4.0% |
| Draw | 29.8% | 28.9% | 3.22 | -3.9% |
| Leeds United win | 38.3% | 38.4% | 2.56 | -2.0% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.1% |
| P btts no | 52.9% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.04 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.17 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2123635206523775, "-10": 2.158374778983967e-07, "-11": 2.353255552186803e-08, "-12": 2.355115183304581e-09, "-13": 2.1705860142460588e-10, "-14": 1.718691562871213e-11, "-2": 0.11353924305717479, "-3": 0.04160745638777467, "-4": 0.01186005126758232, "-5": 0.002757034060719287, "-6": 0.0005401820467416787, "-7": 9.137574020002824e-05, "-8": 1.3590997494285166e-05, "-9": 1.8030954527518935e-06, "0": 0.2984016598002329, "1": 0.1901053131956683, "10": 6.30656003529352e-08, "11": 6.066611546950294e-09, "12": 5.356741217779621e-10, "13": 4.355890290625683e-11, "14": 3.0430514560897603e-12, "2": 0.0903483702303221, "3": 0.02921170549184159, "4": 0.007346554957682223, "5": 0.0015067830129854012, "6": 0.0002604714625562892, "7": 3.887427737881271e-05, "8": 5.101456315574562e-06, "9": 5.971356174262862e-07} |
| Raw goal margin distribution | {"-1": 0.21157607053988764, "-10": 2.15037146251377e-07, "-11": 2.344529612140253e-08, "-12": 2.346382347691747e-09, "-13": 2.1625374181602702e-10, "-14": 1.7123186045572768e-11, "-2": 0.1131182362409253, "-3": 0.04145317472907774, "-4": 0.011816073852458933, "-5": 0.0027468108982166947, "-6": 0.0005381790359978135, "-7": 9.103691629713608e-05, "-8": 1.3540601680197853e-05, "-9": 1.796409522358869e-06, "0": 0.30791287666693506, "1": 0.18528036354403812, "10": 6.146496993741624e-08, "11": 5.912638494971963e-09, "12": 5.220784961543917e-10, "13": 4.245336035265857e-11, "14": 2.9658175807385705e-12, "2": 0.08805529209305056, "3": 0.02847030060490234, "4": 0.007160096424841181, "5": 0.0014685402513740862, "6": 0.00025386059160589623, "7": 3.7887632513694055e-05, "8": 4.971979293292161e-06, "9": 5.819800742126596e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.4% |
| Raw p btts yes | 47.3% |
| P home draw | 61.7% |
| P draw away | 68.1% |
| P home away | 70.2% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.20 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 2.10 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -0.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | -4.4% |
| Under 2.5 probability edge | +4.4% |
| Raw edge prob home | -0.0162 |
| Raw ev home | -0.0647 |
| Raw edge prob draw | 0.0190 |
| Raw ev draw | -0.0085 |
| Raw edge prob away | -0.0028 |
| Raw ev away | -0.0237 |
| Elo home rating | 1,421.3554 |
| Elo away rating | 1,454.8163 |
| Elo rating diff | 26.5391 |
| Elo home expectancy | 0.5381 |

</details>


---

## 2026-10-31 — Aston Villa vs Fulham

The model's most likely 1X2 outcome is **Aston Villa win** at **47.5%**. Expected goals are 1.55 for Aston Villa and 1.05 for Fulham (2.60 combined). The most likely exact score is 1-1 at 12.5%. Goal-market probabilities: at least one goal: 91.9%; Over 2.5 goals: 48.6%; Under 3.5 goals: 73.5%; Double Chance 1X: 73.8%; Double Chance X2: 52.5%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 52.1%; BTTS No (at least one team does not score): 47.9%.

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
| Over 2.5 | 48.6% |
| Under 2.5 | 51.4% |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Fulham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5521 |
| Dc lambda away | 1.0499 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
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
| Fair Over 4.5 odds | 8.06 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.16025889724751888, "-10": 4.110154965224112e-08, "-11": 3.875729933229e-09, "-12": 3.3562833488399623e-10, "-13": 2.686294241849581e-11, "-14": 1.989326114850984e-12, "-15": 1.2559881375760818e-13, "-2": 0.07264589847563531, "-3": 0.022578594662849078, "-4": 0.0055006092310855605, "-5": 0.0010976012432606214, "-6": 0.00018508568277350406, "-7": 2.69927259073234e-05, "-8": 3.4655148489828756e-06, "-9": 3.9719690029210626e-07, "0": 0.2625251296013079, "1": 0.22560255869134047, "10": 1.9069250621868355e-06, "11": 2.658264161096029e-07, "12": 3.4030822524147725e-08, "13": 4.026582555946693e-09, "14": 4.4081687273141397e-10, "15": 4.114404267938212e-11, "2": 0.14775185404879704, "3": 0.06788720767443936, "4": 0.024449559036968695, "5": 0.007212304041371996, "6": 0.0017979245409732684, "7": 0.0003876274985195217, "8": 7.357068448843458e-05, "9": 1.2465568283792569e-05} |
| Raw goal margin distribution | {"-1": 0.15021338585862923, "-10": 3.852518046323503e-08, "-11": 3.6327874828988972e-09, "-12": 3.145901378264943e-10, "-13": 2.5179092107287804e-11, "-14": 1.864629149589291e-12, "-15": 1.17725901016393e-13, "-2": 0.06809223429207363, "-3": 0.02116330020041146, "-4": 0.005155814441992771, "-5": 0.0010288002844433119, "-6": 0.00017348395353316114, "-7": 2.5300740375310188e-05, "-8": 3.248285918285472e-06, "-9": 3.7229939972242864e-07, "0": 0.27555942434862907, "1": 0.22722026605699933, "10": 1.920598873054733e-06, "11": 2.677325529629334e-07, "12": 3.427484419028522e-08, "13": 4.05545559842003e-09, "14": 4.439777974392759e-10, "15": 4.1439070454250945e-11, "2": 0.14881132457949928, "3": 0.06837400018479917, "4": 0.024624877224717307, "5": 0.007264020641745583, "6": 0.0018108167519025366, "7": 0.0003904070231096877, "8": 7.40982309794136e-05, "9": 1.255495397935733e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.3% |
| Away probability edge | -1.6% |
| Over 2.5 probability edge | -6.8% |
| Under 2.5 probability edge | +6.8% |
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

The model's most likely 1X2 outcome is **Bournemouth win** at **42.8%**. Expected goals are 1.44 for Bournemouth and 1.22 for Leeds United (2.65 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 49.8%; Under 3.5 goals: 72.4%; Double Chance 1X: 69.8%; Double Chance X2: 57.2%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.4%; BTTS No (at least one team does not score): 45.6%.

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
| Over 2.5 | 49.8% |
| Under 2.5 | 50.2% |
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
| Over 2.5 | 49.8% | 50.7% | 1.89 | -5.8% |
| Under 2.5 | 50.2% | 49.3% | 1.94 | -2.7% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.4355 |
| Dc lambda away | 1.2155 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
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
| Goal margin distribution | {"-1": 0.1713727549971262, "-10": 1.5708004193768002e-07, "-11": 1.7133088615189925e-08, "-12": 1.7159305013779022e-09, "-13": 1.57918034398354e-10, "-14": 1.2191179088180882e-11, "-2": 0.08810864730952347, "-3": 0.031471618377077674, "-4": 0.008833531348281087, "-5": 0.002033719664096968, "-6": 0.00039602885933064916, "-7": 6.673616000854063e-05, "-8": 9.904151721538536e-06, "-9": 1.3125495028398803e-06, "0": 0.26996843298270495, "1": 0.2172801736218329, "10": 8.817224283371171e-07, "11": 1.1357995617897886e-07, "12": 1.3434480765245794e-08, "13": 1.4601856552225652e-09, "14": 1.331303933448026e-10, "2": 0.13067369275962928, "3": 0.055124398411011, "4": 0.018273186942946062, "5": 0.004968510210757594, "6": 0.0011426601713705685, "7": 0.0002274084640297334, "8": 3.9858215591550014e-05, "9": 6.238374105945828e-06} |
| Raw goal margin distribution | {"-1": 0.17486709366743547, "-10": 1.6028294816910428e-07, "-11": 1.748243711046794e-08, "-12": 1.750918806879722e-09, "-13": 1.6113802753172372e-10, "-14": 1.2439760658368107e-11, "-2": 0.08990520740734925, "-3": 0.03211333352668872, "-4": 0.009013649536765629, "-5": 0.002075187779999882, "-6": 0.00040410399914934887, "-7": 6.809692907962024e-05, "-8": 1.0106100160529101e-05, "-9": 1.3393127563368872e-06, "0": 0.281069308240353, "1": 0.20851009925175185, "10": 8.46133487379515e-07, "11": 1.089955311666265e-07, "12": 1.2892225144446761e-08, "13": 1.4012482170892747e-09, "14": 1.277568545120136e-10, "2": 0.12539931367288545, "3": 0.052899413656939696, "4": 0.01753562674223051, "5": 0.0047679663538077646, "6": 0.0010965390066291832, "7": 0.0002182295817199383, "8": 3.8249419403799294e-05, "9": 5.986574763439987e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.9, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.95, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.94 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market best over 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market best under 2 5 last update utc | 2026-10-23T16:19:50Z |
| Home probability edge | -1.7% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0345 |
| Raw ev home | -0.0970 |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
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
| Goal margin distribution | {"-1": 0.15734751351877255, "-10": 5.107910237010843e-08, "-11": 4.9580487396882005e-09, "-12": 4.4201234494368033e-10, "-13": 3.6422565432759845e-11, "-14": 2.775605301600858e-12, "-15": 1.7945632863899208e-13, "-2": 0.07265948430523118, "-3": 0.023117796152453643, "-4": 0.0057777553263108, "-5": 0.0011841963472360184, "-6": 0.00020526350855339367, "-7": 3.078660658779356e-05, "-8": 4.066383268705984e-06, "-9": 4.795997936730655e-07, "0": 0.25991120196873796, "1": 0.22391642424751554, "10": 2.381881083274565e-06, "11": 3.415584153672741e-07, "12": 4.498481893827888e-08, "13": 5.476202380507437e-09, "14": 6.165155648832111e-10, "15": 5.888741567934395e-11, "2": 0.14933104105827819, "3": 0.07019102607979409, "4": 0.0259162217603844, "5": 0.007847180415181239, "6": 0.0020094585309687746, "7": 0.0004452526385669425, "8": 8.688211192149353e-05, "9": 1.5138345979432132e-05} |
| Raw goal margin distribution | {"-1": 0.1491044792978171, "-10": 4.840319870060268e-08, "-11": 4.698309233696332e-09, "-12": 4.1885644750383407e-10, "-13": 3.451448028693764e-11, "-14": 2.6301984313344806e-12, "-15": 1.7005507008042103e-13, "-2": 0.06885303956256585, "-3": 0.021906713876437812, "-4": 0.005475073486540859, "-5": 0.001122159326146185, "-6": 0.0001945102777747126, "-7": 2.9173774926364112e-05, "-8": 3.853355838593687e-06, "-9": 4.544747858276852e-07, "0": 0.2705262466871199, "1": 0.2253272590853126, "10": 2.39688865059825e-06, "11": 3.4371047952765133e-07, "12": 4.5268255715832815e-08, "13": 5.510706401921724e-09, "14": 6.20400057232999e-10, "15": 5.925844883525222e-11, "2": 0.15027193423213764, "3": 0.07063328012715518, "4": 0.026079512633961438, "5": 0.007896623306855763, "6": 0.002022119567827175, "7": 0.00044805805106056516, "8": 8.742953183806349e-05, "9": 1.5233728468529037e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.98 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +0.3% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.7% |
| P btts no | 34.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 23.34 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.87 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.86 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.08 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.14397486273860796, "-10": 6.314045227478539e-07, "-11": 8.408321931395264e-08, "-12": 1.0295352300722961e-08, "-13": 1.1663819556413898e-09, "-14": 1.2285961914842073e-10, "-15": 1.1966585042143215e-11, "-16": 9.545757742363299e-13, "-2": 0.08226300272066288, "-3": 0.034081409687080906, "-4": 0.011309806606025524, "-5": 0.0031135077168915814, "-6": 0.0007301821238370994, "-7": 0.00014889655468856418, "-8": 2.682906924252091e-05, "-9": 4.3272697905661525e-06, "0": 0.2334748706199912, "1": 0.21769597476390926, "10": 5.890358104739989e-06, "11": 9.612435242950738e-07, "12": 1.4422993040299112e-07, "13": 2.0023733634005136e-08, "14": 2.584660569582577e-09, "15": 3.084996459412756e-10, "16": 3.0156777550470464e-11, "2": 0.15090995261932663, "3": 0.07661626216160576, "4": 0.031156500725905156, "5": 0.010510745689401468, "6": 0.003020681000511434, "7": 0.0007548286955218632, "8": 0.00016667077128451832, "9": 3.294260184794137e-05} |
| Raw goal margin distribution | {"-1": 0.1607601359564599, "-10": 7.050166604760335e-07, "-11": 9.38860403229481e-08, "-12": 1.1495633363365262e-08, "-13": 1.30236430304156e-09, "-14": 1.3718317699470633e-10, "-15": 1.3361706354269125e-11, "-16": 1.0658647511655138e-12, "-2": 0.09185361423521689, "-3": 0.038054782277029534, "-4": 0.01262835756910485, "-5": 0.0034764952322108196, "-6": 0.0008153102233835389, "-7": 0.00016625562212648152, "-8": 2.9956929542926124e-05, "-9": 4.83176345244851e-06, "0": 0.24354007555825302, "1": 0.1989797757092208, "10": 5.383940313086875e-06, "11": 8.786015500452154e-07, "12": 1.3182990284164658e-07, "13": 1.8302212669189253e-08, "14": 2.3624468986060027e-09, "15": 2.819766898416066e-10, "16": 2.7564078020335943e-11, "2": 0.1379356166646998, "3": 0.07002925376607647, "4": 0.028477850971053285, "5": 0.009607094582625656, "6": 0.0027609808983501513, "7": 0.0006899330348055856, "8": 0.00015234141432078705, "9": 3.0110393791572503e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.45, "price": 3.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.05, "price": 1.45, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.58 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -4.2% |
| Draw probability edge | +1.0% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | -0.0844 |
| Raw ev home | -0.1834 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | -0.0234 |
| Raw edge prob away | 0.0643 |
| Raw ev away | 0.2127 |
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
| Over 2.5 | 43.5% | 50.0% | 1.92 | -16.5% |
| Under 2.5 | 56.5% | 50.0% | 1.92 | +8.5% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.1509 |
| Dc lambda away | 1.2433 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
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
| Goal margin distribution | {"-1": 0.2065807329618037, "-10": 2.5473569064589566e-07, "-11": 2.848534738175508e-08, "-12": 2.9241745649647797e-09, "-13": 2.7627713711874374e-10, "-14": 2.225978194183444e-11, "-2": 0.1117505570162795, "-3": 0.041662337065104686, "-4": 0.012120533096000754, "-5": 0.002880843361182991, "-6": 0.0005777445000281432, "-7": 0.0001001047907775596, "-8": 1.5258655947442913e-05, "-9": 2.0752795000478138e-06, "0": 0.28284695484960964, "1": 0.19669695979993093, "10": 1.2162788929019458e-07, "11": 1.2590322581972034e-08, "12": 1.1964391000172093e-09, "13": 1.0464156208667534e-10, "14": 7.804626741286917e-12, "2": 0.09895035353071006, "3": 0.034149413300070985, "4": 0.009196727217774522, "5": 0.002023499928882631, "6": 0.0003756568676610229, "7": 6.025350846339074e-05, "8": 8.501894734263171e-06, "9": 1.070404691099294e-06} |
| Raw goal margin distribution | {"-1": 0.2047947961725452, "-10": 2.5253344344239784e-07, "-11": 2.823908516206739e-08, "-12": 2.898894419721273e-09, "-13": 2.738886592769955e-10, "-14": 2.206734113227383e-11, "-2": 0.11078444837616541, "-3": 0.04130215681293753, "-4": 0.012015748367767774, "-5": 0.002855937823918879, "-6": 0.0005727497691904769, "-7": 9.923936239966861e-05, "-8": 1.5126741443023886e-05, "-9": 2.0573382431164883e-06, "0": 0.2999539904543225, "1": 0.188713524809235, "10": 1.1669131910531988e-07, "11": 1.2079313047573019e-08, "12": 1.1478786454731759e-09, "13": 1.003944242097424e-10, "14": 7.48785656711093e-12, "2": 0.09493420749814142, "3": 0.03276337448519134, "4": 0.008823455185787107, "5": 0.0019413711549943935, "6": 0.00036040990001683207, "7": 5.780797006631484e-05, "8": 8.156824205579008e-06, "9": 1.0269596562913379e-06} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.40 |
| Reference away odds | 2.45 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market best over 2 5 last update utc | 2026-10-23T16:19:50Z |
| Market best under 2 5 last update utc | 2026-10-23T16:19:50Z |
| Home probability edge | -1.4% |
| Draw probability edge | +1.7% |
| Away probability edge | -0.3% |
| Over 2.5 probability edge | -6.5% |
| Under 2.5 probability edge | +6.5% |
| Raw edge prob home | -0.0277 |
| Raw ev home | -0.1024 |
| Raw edge prob draw | 0.0342 |
| Raw ev draw | 0.0288 |
| Raw edge prob away | -0.0065 |
| Raw ev away | -0.0540 |
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
| 1 | 1-1 | 12.02% |
| 2 | 2-0 | 9.14% |
| 3 | 1-0 | 9.06% |
| 4 | 2-1 | 7.97% |
| 5 | 0-0 | 7.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 48.5% | 37.2% | 2.63 | +27.6% |
| Draw | 25.2% | 26.3% | 3.41 | -14.1% |
| Ipswich Town win | 26.3% | 36.5% | 2.66 | -30.0% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Ipswich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8620 |
| Dc lambda away | 0.8714 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.84 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.41 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.17485487771385624, "-10": 8.51895648399605e-09, "-11": 6.667149267366532e-10, "-12": 4.7918451750578064e-11, "-13": 3.1836879616705105e-12, "-14": 1.9661327015765744e-13, "-15": 1.1295834013911602e-14, "-16": 5.585339556818345e-16, "-2": 0.06680550122330971, "-3": 0.01723983242651085, "-4": 0.0034866898715092834, "-5": 0.0005775298370015032, "-6": 8.083619226475733e-05, "-7": 9.785141612461017e-06, "-8": 1.0427124576555819e-06, "-9": 9.919076686863989e-08, "0": 0.25186910904137666, "1": 0.19495385346314337, "10": 8.431260507246191e-06, "11": 1.4100303251545143e-06, "12": 2.165574945535651e-07, "13": 3.0745609163190453e-08, "14": 4.057397896120876e-09, "15": 4.981214472492384e-10, "16": 5.2631856129463384e-11, "2": 0.15207611381226976, "3": 0.08386176247145173, "4": 0.036243191326368315, "5": 0.012828317608491586, "6": 0.0038369248393771947, "7": 0.0009924913381627151, "8": 0.00022599890678924914, "9": 4.594044421073203e-05} |
| Raw goal margin distribution | {"-1": 0.10742252506492848, "-10": 5.233641911475151e-09, "-11": 4.0959795840373386e-10, "-12": 2.943881893116399e-11, "-13": 1.955906545662008e-12, "-14": 1.2078984708777623e-13, "-15": 6.939623465777263e-15, "-16": 3.431367122170417e-16, "-2": 0.04104212432312037, "-3": 0.01059133353993517, "-4": 0.002142056515739723, "-5": 0.0003548068787223871, "-6": 4.966191394400056e-05, "-7": 6.01152586574467e-06, "-8": 6.405929681945824e-07, "-9": 6.093809208795993e-08, "0": 0.24061023658062733, "1": 0.2402508770930296, "10": 1.0390242079768222e-05, "11": 1.7376472243478153e-06, "12": 2.668740683158596e-07, "13": 3.788927193281904e-08, "14": 5.0001238033632476e-09, "15": 6.138586771925674e-10, "16": 6.486073177583163e-11, "2": 0.18741060553186004, "3": 0.10334682608437186, "4": 0.04466420309284444, "5": 0.0158089440260832, "6": 0.00472842440210948, "7": 0.0012230941336376618, "8": 0.00027850916826554475, "9": 5.661458760423214e-05} |
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
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 2.50 |
| Reference draw odds | 3.45 |
| Reference away odds | 2.55 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.02 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | +11.3% |
| Draw probability edge | -1.1% |
| Away probability edge | -10.1% |
| Over 2.5 probability edge | -3.2% |
| Under 2.5 probability edge | +3.2% |
| Raw edge prob home | 0.2254 |
| Raw ev home | 0.5722 |
| Raw edge prob draw | -0.0225 |
| Raw ev draw | -0.1795 |
| Raw edge prob away | -0.2029 |
| Raw ev away | -0.5701 |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9684 |
| Dc lambda away | 1.1397 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
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
| Goal margin distribution | {"-1": 0.126362907187339, "-10": 5.637167308003821e-08, "-11": 5.7443652750532235e-09, "-12": 5.379289193769839e-10, "-13": 4.659085899461012e-11, "-14": 3.751629477499776e-12, "-15": 2.8017592260303394e-13, "-16": 1.750317948006699e-14, "-2": 0.05846762247756784, "-3": 0.01899708248449064, "-4": 0.004899656601924268, "-5": 0.0010426719917268914, "-6": 0.00018837077052804793, "-7": 2.9521751523974776e-05, "-8": 4.0816067452848735e-06, "-9": 5.045390676779327e-07, "0": 0.22101170094757513, "1": 0.22702609648903047, "10": 1.344234664072099e-05, "11": 2.3657762294926982e-06, "12": 3.8262554241875314e-07, "13": 5.723573086166576e-08, "14": 7.959832054596924e-09, "15": 1.0266732002326505e-09, "16": 1.1077348288042304e-10, "2": 0.17611242673684155, "3": 0.09882775401945594, "4": 0.04402254135042133, "5": 0.01617985497102236, "6": 0.005048447925159769, "7": 0.0013664820682060693, "8": 0.0003262950047302534, "9": 6.966129061378145e-05} |
| Raw goal margin distribution | {"-1": 0.12494472234293408, "-10": 5.5739007575616604e-08, "-11": 5.679895630003599e-09, "-12": 5.318916837846077e-10, "-13": 4.606796464543214e-11, "-14": 3.709524526092438e-12, "-15": 2.7703147732200137e-13, "-16": 1.730673936627055e-14, "-2": 0.05781143390188761, "-3": 0.018783876132507357, "-4": 0.004844667215479275, "-5": 0.001030969968963516, "-6": 0.00018625666459428928, "-7": 2.9190425650555936e-05, "-8": 4.035798422606747e-06, "-9": 4.988765700738675e-07, "0": 0.23521995922898437, "1": 0.22229741955106203, "10": 1.316235894091386e-05, "11": 2.316499993545363e-06, "12": 3.74655918634112e-07, "13": 5.6043580334748685e-08, "14": 7.794038452677274e-09, "15": 1.0052888485662553e-09, "16": 1.084662062195639e-10, "2": 0.1724442194968849, "3": 0.09676929233381623, "4": 0.04310560545955313, "5": 0.01584284830859735, "6": 0.004943294906870566, "7": 0.0013380199119077264, "8": 0.00031949867740179225, "9": 6.82103308188998e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.64 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.10 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.46 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -1.2% |
| Draw probability edge | +1.4% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Tottenham |
| Matched away-team name | Crystal Palace |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5686 |
| Dc lambda away | 1.2529 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.8% |
| P btts no | 43.2% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.10 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.69 |
| Fair Over 2.5 odds | 1.82 |
| Fair Under 2.5 odds | 2.21 |
| Fair Over 3.5 odds | 3.15 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.21 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.1348162767124382, "-10": 1.518756966257276e-07, "-11": 1.7048566766201784e-08, "-12": 1.758141857479285e-09, "-13": 1.6760238776002038e-10, "-14": 1.4757656617750392e-11, "-15": 1.0898970315354714e-12, "-2": 0.06987368186782185, "-3": 0.025377978391159028, "-4": 0.0072764289249906515, "-5": 0.001715850232105556, "-6": 0.0003428002522891316, "-7": 5.933054541931026e-05, "-8": 9.05039225395098e-06, "-9": 1.2334917359179786e-06, "0": 0.2388454003188593, "1": 0.2511277888614299, "10": 2.110991979953173e-06, "11": 2.9667219227986565e-07, "12": 3.8303066595969e-08, "13": 4.571413423788232e-09, "14": 5.039394578364796e-10, "15": 4.6594762132011286e-11, "2": 0.16091132181161147, "3": 0.07316791224967059, "4": 0.02626470923556808, "5": 0.007753974158030516, "6": 0.0019394418830332072, "7": 0.00042024702126540985, "8": 8.025726785140635e-05, "9": 1.3694427424929133e-05} |
| Raw goal margin distribution | {"-1": 0.16574826334409215, "-10": 1.867217636753356e-07, "-11": 2.0960157059010685e-08, "-12": 2.161526535933938e-09, "-13": 2.060567565057485e-10, "-14": 1.8143624902488505e-11, "-15": 1.3399609053601671e-12, "-2": 0.0859053647339049, "-3": 0.0312006528298554, "-4": 0.008945918750125579, "-5": 0.002109531601563763, "-6": 0.0004214516813280164, "-7": 7.29432313835824e-05, "-8": 1.1126896805456724e-05, "-9": 1.5165017018959982e-06, "0": 0.26904638246987506, "1": 0.21014051295181876, "10": 1.7664510149026664e-06, "11": 2.482514856156832e-07, "12": 3.205151488251259e-08, "13": 3.825300123674333e-09, "14": 4.216900751865934e-10, "15": 3.8989899364309973e-11, "2": 0.13464853036995234, "3": 0.061225970576452356, "4": 0.0219779718378285, "5": 0.006488426129068424, "6": 0.0016229000939666021, "7": 0.00035165731763726204, "8": 6.715825242148799e-05, "9": 1.1459321235229696e-05} |
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
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.79, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.08, "price": 1.79, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (DE) |
| Reference home odds | 1.58 |
| Reference draw odds | 4.20 |
| Reference away odds | 4.70 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -8.5% |
| Draw probability edge | +3.0% |
| Away probability edge | +5.5% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.1703 |
| Raw ev home | -0.2928 |
| Raw edge prob draw | 0.0604 |
| Raw ev draw | 0.1650 |
| Raw edge prob away | 0.1099 |
| Raw ev away | 0.4338 |
| Elo home rating | 1,386.8335 |
| Elo away rating | 1,458.5707 |
| Elo rating diff | -11.7372 |
| Elo home expectancy | 0.4831 |

</details>


---

## 2026-11-01 — Liverpool vs Arsenal

The model's most likely 1X2 outcome is **Arsenal win** at **44.3%**. Expected goals are 1.03 for Liverpool and 1.46 for Arsenal (2.49 combined). The most likely exact score is 1-1 at 13.0%. Goal-market probabilities: at least one goal: 91.0%; Over 2.5 goals: 45.7%; Under 3.5 goals: 76.0%; Double Chance 1X: 55.7%; Double Chance X2: 71.6%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 89.2%; BTTS Yes (both teams score): 50.3%; BTTS No (at least one team does not score): 49.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 28.4% | 3.52 |
| Draw | 27.3% | 3.66 |
| Arsenal win | 44.3% | 2.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.03 |
| Arsenal expected goals | 1.46 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.0% |
| Under 0.5 | 9.0% |
| Over 1.5 | 72.1% |
| Under 1.5 | 27.9% |
| Over 2.5 | 45.7% |
| Under 2.5 | 54.3% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.8% |
| Under 4.5 | 89.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.00% |
| 2 | 0-1 | 10.62% |
| 3 | 0-0 | 9.00% |
| 4 | 1-2 | 8.80% |
| 5 | 0-2 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 28.4% | 31.1% | 3.11 | -11.6% |
| Draw | 27.3% | 26.1% | 3.65 | -0.3% |
| Arsenal win | 44.3% | 42.8% | 2.20 | -2.6% |

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
| Market best home last update utc | 2026-10-23T16:19:50Z |
| Market best draw last update utc | 2026-10-23T16:19:50Z |
| Market best away last update utc | 2026-10-23T16:19:50Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
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
| Bbs statistics cutoff utc | 2026-10-23T16:19:46.649991+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 50.3% |
| P btts no | 49.7% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.11 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.59 |
| Fair Over 2.5 odds | 2.19 |
| Fair Under 2.5 odds | 1.84 |
| Fair Over 3.5 odds | 4.17 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.24 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21925867491870307, "-10": 1.0827243126648227e-06, "-11": 1.416621349918817e-07, "-12": 1.701924088070424e-08, "-13": 1.8896669309487025e-09, "-14": 1.942382589542085e-10, "-15": 1.7129382150644836e-11, "-2": 0.1367267522309245, "-3": 0.059387615307911125, "-4": 0.020162793992186828, "-5": 0.005598036786725049, "-6": 0.0013121715458802917, "-7": 0.0002658354032313526, "-8": 4.739040697968554e-05, "-9": 7.539591539656032e-06, "0": 0.2731015135956166, "1": 0.17401604488154998, "10": 4.025899250175307e-08, "11": 3.7404222929407e-09, "12": 3.191015250132127e-10, "13": 2.5159140378799834e-11, "14": 1.836399444150395e-12, "15": 1.14999490205288e-13, "2": 0.07863642942348055, "3": 0.024254259238949395, "4": 0.005847425294317603, "5": 0.0011528466924855566, "6": 0.00019188819890181234, "7": 2.7605289744302076e-05, "8": 3.494554116034405e-06, "9": 3.9479440661855497e-07} |
| Raw goal margin distribution | {"-1": 0.2263636167253647, "-10": 1.1178093246352432e-06, "-11": 1.4625260889535643e-07, "-12": 1.7570738859499358e-08, "-13": 1.9509004195818955e-09, "-14": 2.005324296501165e-10, "-15": 1.768444918919884e-11, "-2": 0.14115729810727237, "-3": 0.061312034266274185, "-4": 0.02081615686609506, "-5": 0.005779437707878931, "-6": 0.0013546916535900249, "-7": 0.00027444963512347504, "-8": 4.8926063819304413e-05, "-9": 7.783907342235413e-06, "0": 0.2857020748765868, "1": 0.15751159389341776, "10": 3.6440651675600804e-08, "11": 3.38566410698849e-09, "12": 2.888365256943067e-10, "13": 2.2772936281539227e-11, "14": 1.6622272024973672e-12, "15": 1.0409243016352398e-13, "2": 0.07117820282038206, "3": 0.021953878069298206, "4": 0.005292829629058566, "5": 0.001043505615656063, "6": 0.00017368867381703255, "7": 2.498708202725995e-05, "8": 3.163115154916052e-06, "9": 3.573503597844832e-07} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 28.6% |
| Unadjusted away-win probability | 45.7% |
| Raw p over 1 5 | 72.2% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 50.5% |
| P home draw | 55.7% |
| P draw away | 71.6% |
| P home away | 72.7% |
| Raw p home draw | 54.3% |
| Raw p draw away | 74.3% |
| Raw p home away | 71.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-23T16:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-23T16:19:50Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Betfair |
| Reference home odds | 3.15 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-23T16:19:50Z |
| Market reference home last update utc | 2026-10-23T16:19:50Z |
| Market reference draw last update utc | 2026-10-23T16:19:50Z |
| Market reference away last update utc | 2026-10-23T16:19:50Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.10 |
| Market reference over 2 5 last update utc | 2026-10-23T16:19:48Z |
| Market reference under 2 5 last update utc | 2026-10-23T16:19:48Z |
| Home probability edge | -2.7% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -9.7% |
| Under 2.5 probability edge | +9.7% |
| Raw edge prob home | -0.0539 |
| Raw ev home | -0.2002 |
| Raw edge prob draw | 0.0252 |
| Raw ev draw | 0.0428 |
| Raw edge prob away | 0.0287 |
| Raw ev away | 0.0057 |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,646.9660 |
| Elo rating diff | -28.8787 |
| Elo home expectancy | 0.4585 |

</details>


---
