# Premier League — football model report

Fixtures in this report: **1**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,990 |
| Training data through | 2026-11-02 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 480 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 70.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | 3c9f5f99eb55e2475c2e23eaea8dbf3e2923865194db3d46f20429a57242ed26 |
| Training as of utc | 2026-11-04T09:28:30.390798+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 90, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 90, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 226, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-11-04T09:28:30.390798+00:00', 'observations': 625, 'observations_sha256': '054a32550f4580794084213895724217cfacef1961ad8831e61e7aee0b6caeb6', 'eligible_training_matches': 291, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 262, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 28, 'retrospective_eligible_training_matches': 291, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '9d600f2cca3142254a349d46ce12c988d0df0096fbc8edcb2fb67ee6492ca223', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 230, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-10-04T00:00:00+00:00', 'audit_origin_utc': '2025-11-02T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 12, 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1989, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1619, 'tuning_matches': 249, 'audit_matches': 112, 'audit_matchdays': 37, 'selected_shrinkage': 15.0, 'selected_component': 'shots_on_target_and_total_shots', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.9372149208477853, 'audit_candidate_poisson_score': 0.9280257670321073, 'audit_gain': 0.009189153815678086, 'audit_gain_lower95': 0.0003474802310925464, 'audit_baseline_briers': [0.6265738347139245, 0.167832988720583, 0.21447736421684555, 0.2603646763863064], 'audit_candidate_briers': [0.6266934513464083, 0.16714356098353306, 0.2120711078558599, 0.25712093059759306], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1881.080 |
| Base scoring parameter | 0.214 |
| Home-advantage parameter | 0.178 |
| Dixon-Coles low-score adjustment | -0.061 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1990, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 1.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261104T092830390798Z_416cff278d39690b14d089603b8e43f7b6e488f250fd741a3c2f8107c1f4a280.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Totals anchor fixtures | {'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 1} |
| Legacy comparison status | {'None': 1} |
| Bbs statistics applied fixtures | 0 |
| Goal market validation | SKIPPED: not required by 48h-ah-price-edge-cagey-v28 |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-11-06 — Everton vs Coventry City

The model's most likely 1X2 outcome is **Everton win** at **54.6%**. Expected goals are 1.44 for Everton and 0.90 for Coventry City (2.33 combined). The most likely exact score is 1-0 at 14.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 42.7%; Under 3.5 goals: 78.8%; Double Chance 1X: 79.5%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 90.8%; BTTS Yes (both teams score): 44.9%; BTTS No (at least one team does not score): 55.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Everton win | 54.6% | 1.83 |
| Draw | 24.9% | 4.02 |
| Coventry City win | 20.5% | 4.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Everton expected goals | 1.44 |
| Coventry City expected goals | 0.90 |
| Expected total goals | 2.33 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 69.0% |
| Under 1.5 | 31.0% |
| Over 2.5 | 42.7% |
| Under 2.5 | 57.3% |
| Over 3.5 | 21.2% |
| Under 3.5 | 78.8% |
| Over 4.5 | 9.2% |
| Under 4.5 | 90.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.69% |
| 2 | 1-1 | 11.62% |
| 3 | 2-0 | 11.18% |
| 4 | 2-1 | 10.01% |
| 5 | 0-0 | 9.17% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Everton win | 54.6% | 57.0% | 1.75 | -4.4% |
| Draw | 24.9% | 23.4% | 4.16 | +3.4% |
| Coventry City win | 20.5% | 19.6% | 4.93 | +1.1% |
| Over 2.5 | 42.7% | 55.8% | 1.81 | -22.8% |
| Under 2.5 | 57.3% | 44.2% | 2.15 | +23.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T20:00:00+00:00 |
| Fixture id | 586bec023ee8ac2f0645d963bd2c9d25 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T09:28:05Z |
| Market best draw last update utc | 2026-11-04T09:28:05Z |
| Market best away last update utc | 2026-11-04T09:28:05Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Everton |
| Matched away-team name | Coventry |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4393 |
| Dc lambda away | 0.8953 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T09:28:30.390798+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.9% |
| P btts no | 55.1% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.91 |
| Fair Over 1.5 odds | 1.45 |
| Fair Under 1.5 odds | 3.22 |
| Fair Over 2.5 odds | 2.34 |
| Fair Under 2.5 odds | 1.74 |
| Fair Over 3.5 odds | 4.72 |
| Fair Under 3.5 odds | 1.27 |
| Fair Over 4.5 odds | 10.89 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.13423720569679917, "-10": 8.978038724262404e-09, "-11": 7.237002217117452e-10, "-12": 5.354695799421094e-11, "-13": 3.64873437444757e-12, "-14": 2.1366377987451065e-13, "-2": 0.052865144321632494, "-3": 0.01432737275497688, "-4": 0.0030199476899886706, "-5": 0.0005190893441009559, "-6": 7.519843512287609e-05, "-7": 9.404944482595352e-06, "-8": 1.0342490011685705e-06, "-9": 1.0144603531071977e-07, "0": 0.24866701563285903, "1": 0.2709611537162326, "10": 1.2755399085933462e-06, "11": 1.6530065321116382e-07, "12": 1.9663189054407473e-08, "13": 2.154094176154619e-09, "14": 2.0279471498511658e-10, "2": 0.1682889891422222, "3": 0.07332568466794487, "4": 0.02484804782791698, "5": 0.0068665447514902524, "6": 0.0015992200692900235, "7": 0.00032155772816907895, "8": 5.685008426289517e-05, "9": 8.964877683974102e-06} |
| Raw goal margin distribution | {"-1": 0.14832538627714706, "-10": 9.920282941491222e-09, "-11": 7.996524836542474e-10, "-12": 5.916670558829196e-11, "-13": 4.031668662226518e-12, "-14": 2.360877710379648e-13, "-2": 0.058413335642684916, "-3": 0.01583102901455353, "-4": 0.003336890881549602, "-5": 0.0005735677160178034, "-6": 8.309050295810452e-05, "-7": 1.039199241413695e-05, "-8": 1.1427933247625668e-06, "-9": 1.120927860174193e-07, "0": 0.28333377009267824, "1": 0.24309157773051365, "10": 1.1443448796461771e-06, "11": 1.4829873595485443e-07, "12": 1.764074143061535e-08, "13": 1.9325358808072095e-09, "14": 1.819363644752171e-10, "2": 0.1509797080658255, "3": 0.06578380749281924, "4": 0.02229231410911924, "5": 0.006160289673644631, "6": 0.0014347330768643815, "7": 0.00028848406644268787, "8": 5.1002796851288734e-05, "9": 8.04279960602995e-06} |
| Unadjusted home-win probability | 49.0% |
| Unadjusted draw probability | 28.3% |
| Unadjusted away-win probability | 22.7% |
| Raw p over 1 5 | 68.5% |
| Raw p under 3 5 | 79.2% |
| Raw p btts yes | 45.9% |
| P home draw | 79.5% |
| P draw away | 45.4% |
| P home away | 75.1% |
| Raw p home draw | 77.3% |
| Raw p draw away | 51.0% |
| Raw p home away | 71.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.4267 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:28:52Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:28:05Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:28:05Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:28:52Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:28:05Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.93, "draw": 4.16, "home": 1.75}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T09:28:05Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.81, "under": 2.15}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T09:28:52Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.83, "draw": 4.07, "home": 1.72}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.72 |
| Reference draw odds | 4.07 |
| Reference away odds | 4.83 |
| Market reference 1x2 last update utc | 2026-11-04T09:28:52Z |
| Market reference home last update utc | 2026-11-04T09:28:52Z |
| Market reference draw last update utc | 2026-11-04T09:28:52Z |
| Market reference away last update utc | 2026-11-04T09:28:52Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.24 |
| Market reference over 2 5 last update utc | 2026-11-04T09:28:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T09:28:50Z |
| Market best over 2 5 last update utc | 2026-11-04T09:28:05Z |
| Market best under 2 5 last update utc | 2026-11-04T09:28:05Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.5% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -13.1% |
| Under 2.5 probability edge | +13.1% |
| Raw edge prob home | -0.0803 |
| Raw ev home | -0.1423 |
| Raw edge prob draw | 0.0495 |
| Raw ev draw | 0.1787 |
| Raw edge prob away | 0.0307 |
| Raw ev away | 0.1170 |
| Count model | {"corners": {"alpha": 0.00930322941348174, "mu": 9.757177087800525, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,448.4574 |
| Elo away rating | 1,377.6232 |
| Elo rating diff | 130.8342 |
| Elo home expectancy | 0.6799 |

</details>


---
