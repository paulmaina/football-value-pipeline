# Bundesliga — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,604 |
| Training data through | 2026-11-01 |
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
| Training sha256 | 0fa0d9672f664bc52cb0c3e8f12ec99ffd75193f03671d76b5ed2bc935e5edba |
| Training as of utc | 2026-11-04T19:39:12.830329+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 72, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 72, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 70, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-11-04T19:39:12.830329+00:00', 'observations': 406, 'observations_sha256': 'cf7c875429061248016b8133b446dc0d3d07fca94f90ee10e42140b8f4f34a33', 'eligible_training_matches': 83, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 115, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 22, 'retrospective_eligible_training_matches': 83, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': '3e3b40acf02e0408ddc71402f81e1521b46bfb7aa649d9fdd25d92f2de0010a7', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1601, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1304, 'tuning_matches': 207, 'audit_matches': 82, 'audit_matchdays': 28, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.6694601589980784, 'audit_candidate_poisson_score': 0.6673686986674418, 'audit_gain': 0.002091460330636674, 'audit_gain_lower95': -0.006071819396616229, 'audit_baseline_briers': [0.5838791063980268, 0.13631367949783407, 0.2743769881803856, 0.2354603100616698], 'audit_candidate_briers': [0.5818323738130945, 0.1359856171064298, 0.2735024403933491, 0.236260431039501], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive', 'market_brier_worse']} |
| Optimizer objective | 1588.167 |
| Base scoring parameter | 0.218 |
| Home-advantage parameter | 0.226 |
| Dixon-Coles low-score adjustment | -0.079 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1604, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-01'} |
| Training data health | {'training_end': '2026-11-01', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261104T193912830329Z_6e0c5a3476086dce1e3b3c79d7071ae5c791ff6565bb23b8ad70657a8952f6ba.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 5} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 6} |
| Legacy comparison status | {'None': 6} |
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

## 2026-11-06 — Hamburger SV vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **Hamburger SV win** at **38.8%**. Expected goals are 1.44 for Hamburger SV and 1.40 for Borussia Monchengladbach (2.84 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 94.2%; Over 2.5 goals: 58.2%; Under 3.5 goals: 64.0%; Double Chance 1X: 65.1%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 73.7%; Under 4.5 goals: 81.1%; BTTS Yes (both teams score): 61.8%; BTTS No (at least one team does not score): 38.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hamburger SV win | 38.8% | 2.58 |
| Draw | 26.3% | 3.81 |
| Borussia Monchengladbach win | 34.9% | 2.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hamburger SV expected goals | 1.44 |
| Borussia Monchengladbach expected goals | 1.40 |
| Expected total goals | 2.84 |
| Over 0.5 | 94.2% |
| Under 0.5 | 5.8% |
| Over 1.5 | 81.4% |
| Under 1.5 | 18.6% |
| Over 2.5 | 58.2% |
| Under 2.5 | 41.8% |
| Over 3.5 | 36.0% |
| Under 3.5 | 64.0% |
| Over 4.5 | 18.9% |
| Under 4.5 | 81.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.13% |
| 2 | 2-1 | 8.68% |
| 3 | 1-2 | 8.02% |
| 4 | 1-0 | 6.67% |
| 5 | 2-2 | 6.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hamburger SV win | 38.8% | 39.3% | 2.49 | -3.4% |
| Draw | 26.3% | 26.0% | 3.85 | +1.1% |
| Borussia Monchengladbach win | 34.9% | 34.7% | 2.83 | -1.1% |
| Over 2.5 | 58.2% | 58.5% | 1.69 | -1.6% |
| Under 2.5 | 41.8% | 41.5% | 2.36 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T19:30:00+00:00 |
| Fixture id | 295076c39e49863cb54db085ac3cd340 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:43Z |
| Market best draw last update utc | 2026-11-04T19:38:43Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Hamburg |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4421 |
| Dc lambda away | 1.3955 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 61.8% |
| P btts no | 38.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.30 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.38 |
| Fair Over 2.5 odds | 1.72 |
| Fair Under 2.5 odds | 2.39 |
| Fair Over 3.5 odds | 2.78 |
| Fair Under 3.5 odds | 1.56 |
| Fair Over 4.5 odds | 5.28 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.17897217960654122, "-10": 8.612860551008944e-07, "-11": 1.1475637847984755e-07, "-12": 1.4051534662736375e-08, "-13": 1.5906697444596394e-09, "-14": 1.6599680010747933e-10, "-15": 1.4307025935123275e-11, "-2": 0.10533648150072855, "-3": 0.04462880500879836, "-4": 0.015024473669716992, "-5": 0.004175878592917727, "-6": 0.0009857020162870472, "-7": 0.00020189089872893769, "-8": 3.6485926740490724e-05, "-9": 5.896093886214889e-06, "0": 0.2626945802678556, "1": 0.19393645825314157, "10": 1.2518518635793828e-06, "11": 1.723558835330302e-07, "12": 2.1808047896541322e-08, "13": 2.551037297420916e-09, "14": 2.7509345533734143e-10, "15": 2.4500427419331095e-11, "2": 0.11776989750956861, "3": 0.05156018915768774, "4": 0.01793668846312189, "5": 0.005151510819314275, "6": 0.0012565395185516965, "7": 0.000265944493590774, "8": 4.966419466137121e-05, "9": 8.293276793201693e-06} |
| Raw goal margin distribution | {"-1": 0.18741141957197338, "-10": 5.422310533008762e-07, "-11": 6.77704289675384e-08, "-12": 7.778824503406508e-09, "-13": 8.191678643178489e-10, "-14": 7.139359458443709e-11, "-2": 0.10631534251024667, "-3": 0.042885271732237704, "-4": 0.013669516864402539, "-5": 0.0035854195154205, "-6": 0.0007970380192655695, "-7": 0.0001535302878815997, "-8": 2.6069380833840826e-05, "-9": 3.9554637557460814e-06, "0": 0.26932687619853746, "1": 0.19396892157350776, "10": 7.527000236816932e-07, "11": 9.721237038583741e-08, "12": 1.153025802982319e-08, "13": 1.2547052460513434e-09, "14": 1.1299827408790656e-10, "2": 0.11352289335703636, "3": 0.04731942181001736, "4": 0.01558576711642235, "5": 0.0042243388759416935, "6": 0.0009703793910287745, "7": 0.00019315250504616045, "8": 3.389071658259272e-05, "9": 5.313628638065965e-06} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 78.5% |
| Raw p under 3 5 | 68.4% |
| Raw p btts yes | 58.4% |
| P home draw | 65.1% |
| P draw away | 61.2% |
| P home away | 73.7% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0682 |
| Totals anchor target over 2 5 | 0.5824 |
| Totals anchor reference over odds | 1.67 |
| Totals anchor reference under odds | 2.29 |
| Totals anchor reference last update utc | 2026-11-04T19:39:27Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5419 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.62, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.08, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.62, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.83, "draw": 3.85, "home": 2.49}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.69, "under": 2.36}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.6, "home_away": 1.3, "home_draw": 1.49}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:38:57Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.58, "home_away": 1.31, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.8, "draw": 3.71, "home": 2.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.29}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.48 |
| Reference draw odds | 3.71 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.69 |
| Reference Under 2.5 odds | 2.36 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:43Z |
| Market best over 2 5 last update utc | 2026-11-04T19:38:43Z |
| Market best under 2 5 last update utc | 2026-11-04T19:38:43Z |
| Home probability edge | -0.5% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.2% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0173 |
| Raw ev home | -0.0642 |
| Raw edge prob draw | 0.0095 |
| Raw ev draw | 0.0369 |
| Raw edge prob away | 0.0078 |
| Raw ev away | 0.0042 |
| Market p home draw | 64.9% |
| Market home draw odds | 1.49 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:38:43Z |
| Market reference home draw last update utc | 2026-11-04T19:39:28Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 60.3% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:38:43Z |
| Market reference draw away last update utc | 2026-11-04T19:39:28Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.8% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-11-04T19:38:57Z |
| Market reference home away last update utc | 2026-11-04T19:39:28Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.55 |
| Market reference dc home draw odds | 1.44 |
| Market reference dc home away odds | 1.25 |
| Market p over 1 5 | 82.7% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-11-04T19:39:28Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 63.3% |
| Market under 3 5 odds | 1.52 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:39:27Z |
| Market reference under 3 5 odds | 1.49 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-11-04T19:39:28Z |
| Market under 3 5 bookmakers | 1 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 9.857657217579082, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,426.8279 |
| Elo away rating | 1,410.3288 |
| Elo rating diff | 76.4991 |
| Elo home expectancy | 0.6083 |

</details>


---

## 2026-11-07 — Borussia Dortmund vs Elversberg

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **73.9%**. Expected goals are 2.88 for Borussia Dortmund and 1.29 for Elversberg (4.18 combined). The most likely exact score is 2-1 at 8.8%. Goal-market probabilities: at least one goal: 98.2%; Over 2.5 goals: 79.4%; Under 3.5 goals: 39.3%; Double Chance 1X: 88.6%; Double Chance X2: 26.1%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 58.7%; BTTS Yes (both teams score): 68.3%; BTTS No (at least one team does not score): 31.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 73.9% | 1.35 |
| Draw | 14.7% | 6.82 |
| Elversberg win | 11.4% | 8.78 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.88 |
| Elversberg expected goals | 1.29 |
| Expected total goals | 4.18 |
| Over 0.5 | 98.2% |
| Under 0.5 | 1.8% |
| Over 1.5 | 92.8% |
| Under 1.5 | 7.2% |
| Over 2.5 | 79.4% |
| Under 2.5 | 20.6% |
| Over 3.5 | 60.7% |
| Under 3.5 | 39.3% |
| Over 4.5 | 41.3% |
| Under 4.5 | 58.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.76% |
| 2 | 3-1 | 8.42% |
| 3 | 2-0 | 6.76% |
| 4 | 3-0 | 6.50% |
| 5 | 4-1 | 6.07% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 73.9% | 75.8% | 1.32 | -2.4% |
| Draw | 14.7% | 14.0% | 6.58 | -3.5% |
| Elversberg win | 11.4% | 10.2% | 9.50 | +8.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | 3ef62ef56758041178c5280225fe5db7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:43Z |
| Market best draw last update utc | 2026-11-04T19:38:43Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Dortmund |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.8831 |
| Dc lambda away | 1.2950 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.3% |
| P btts no | 31.7% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 56.12 |
| Fair Over 1.5 odds | 1.08 |
| Fair Under 1.5 odds | 13.81 |
| Fair Over 2.5 odds | 1.26 |
| Fair Under 2.5 odds | 4.86 |
| Fair Over 3.5 odds | 1.65 |
| Fair Under 3.5 odds | 2.54 |
| Fair Over 4.5 odds | 2.42 |
| Fair Under 4.5 odds | 1.70 |
| Goal margin distribution | {"-1": 0.06823383081600166, "-10": 6.348401377952119e-08, "-11": 7.2727323466710496e-09, "-12": 7.668506393646366e-10, "-13": 7.487969414769291e-11, "-14": 6.807107964643222e-12, "-15": 5.787894670048463e-13, "-16": 4.6215901528356275e-14, "-17": 3.4749882264670454e-15, "-18": 2.4363096649455487e-16, "-19": 1.3878071401399506e-17, "-2": 0.031209214088913636, "-3": 0.010636988095132093, "-4": 0.002949756050749624, "-5": 0.0006852729407271778, "-6": 0.00013649406741441636, "-7": 2.3743312650001042e-05, "-8": 3.660900758605158e-06, "-9": 5.064207451495265e-07, "0": 0.14664735566347536, "1": 0.20481273922864668, "10": 0.00024878491535184325, "11": 6.34538852702295e-05, "12": 1.4896091986886139e-05, "13": 3.2383707686094826e-06, "14": 6.554296667178776e-07, "15": 1.2407521103732197e-07, "16": 2.2057524991981502e-08, "17": 3.6924926167900136e-09, "18": 5.763678311231099e-10, "19": 7.309662247895156e-11, "2": 0.2025978912733996, "3": 0.15373463066513038, "4": 0.09491614336198392, "5": 0.04909288034873178, "6": 0.02177056264338422, "7": 0.008431369767803645, "8": 0.002894314552453613, "9": 0.000891395028248874} |
| Raw goal margin distribution | {"-1": 0.0841552909398604, "-10": 7.829716704683138e-08, "-11": 8.969728054874286e-09, "-12": 9.457850730552096e-10, "-13": 9.235187840295015e-11, "-14": 8.395456394179908e-12, "-15": 7.138423184837058e-13, "-16": 5.699976965465452e-14, "-17": 4.2858306753948694e-15, "-18": 3.0047902370594264e-16, "-19": 1.7116335438036722e-17, "-2": 0.03849147058354797, "-3": 0.013118988296048401, "-4": 0.003638042532330362, "-5": 0.0008451722995828807, "-6": 0.00016834314910150634, "-7": 2.9283499988810835e-05, "-8": 4.51512343302471e-06, "-9": 6.245873144798558e-07, "0": 0.16315603945639842, "1": 0.1928805535396487, "10": 0.0002342909545866106, "11": 5.975712527090397e-05, "12": 1.4028260540964732e-05, "13": 3.049706521031923e-06, "14": 6.172449887588324e-07, "15": 1.1684671312711063e-07, "16": 2.0772475609627332e-08, "17": 3.4773716837624744e-09, "18": 5.427892167652972e-10, "19": 6.883808623778673e-11, "2": 0.19079474041482491, "3": 0.14477820458131144, "4": 0.0893864236202134, "5": 0.04623277815716411, "6": 0.02050223140093732, "7": 0.007940166583563602, "8": 0.0027256946765010174, "9": 0.0008394632439303158} |
| Unadjusted home-win probability | 69.6% |
| Unadjusted draw probability | 16.3% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 39.9% |
| Raw p btts yes | 69.0% |
| P home draw | 88.6% |
| P draw away | 26.1% |
| P home away | 85.3% |
| Raw p home draw | 86.0% |
| Raw p draw away | 30.4% |
| Raw p home away | 83.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7940 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.89, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 8.64, "draw": 6.45, "home": 1.3}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 9.5, "draw": 6.58, "home": 1.32}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.30 |
| Reference draw odds | 6.45 |
| Reference away odds | 8.64 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.37 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:50Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +6.1% |
| Under 2.5 probability edge | -6.1% |
| Raw edge prob home | -0.0615 |
| Raw ev home | -0.0808 |
| Raw edge prob draw | 0.0236 |
| Raw ev draw | 0.0736 |
| Raw edge prob away | 0.0380 |
| Raw ev away | 0.3343 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 10.850684578094096, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,639.4058 |
| Elo away rating | 1,432.5460 |
| Elo rating diff | 266.8598 |
| Elo home expectancy | 0.8229 |

</details>


---

## 2026-11-07 — FSV Mainz 05 vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **71.8%**. Expected goals are 1.19 for FSV Mainz 05 and 2.70 for Bayern Munich (3.88 combined). The most likely exact score is 1-2 at 9.3%. Goal-market probabilities: at least one goal: 97.8%; Over 2.5 goals: 75.4%; Under 3.5 goals: 45.2%; Double Chance 1X: 28.2%; Double Chance X2: 86.5%; Double Chance 12 (either team wins): 85.3%; Under 4.5 goals: 64.4%; BTTS Yes (both teams score): 64.6%; BTTS No (at least one team does not score): 35.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 13.5% | 7.38 |
| Draw | 14.7% | 6.82 |
| Bayern Munich win | 71.8% | 1.39 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.19 |
| Bayern Munich expected goals | 2.70 |
| Expected total goals | 3.88 |
| Over 0.5 | 97.8% |
| Under 0.5 | 2.2% |
| Over 1.5 | 90.7% |
| Under 1.5 | 9.3% |
| Over 2.5 | 75.4% |
| Under 2.5 | 24.6% |
| Over 3.5 | 54.8% |
| Under 3.5 | 45.2% |
| Over 4.5 | 35.6% |
| Under 4.5 | 64.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.25% |
| 2 | 1-3 | 8.32% |
| 3 | 0-2 | 7.81% |
| 4 | 0-3 | 7.02% |
| 5 | 1-1 | 6.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 13.5% | 13.4% | 7.95 | +7.7% |
| Draw | 14.7% | 13.6% | 6.74 | -1.2% |
| Bayern Munich win | 71.8% | 73.0% | 1.36 | -2.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | fe97f5adf397dd6b0a8a9e0a5272f307 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:43Z |
| Market best draw last update utc | 2026-11-04T19:39:27Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | Mainz |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1852 |
| Dc lambda away | 2.6993 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 64.6% |
| P btts no | 35.4% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 45.66 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 10.75 |
| Fair Over 2.5 odds | 1.33 |
| Fair Under 2.5 odds | 4.07 |
| Fair Over 3.5 odds | 1.82 |
| Fair Under 3.5 odds | 2.21 |
| Fair Over 4.5 odds | 2.81 |
| Fair Under 4.5 odds | 1.55 |
| Goal margin distribution | {"-1": 0.2097837940826707, "-10": 0.00016161392919157146, "-11": 3.873803548123721e-05, "-12": 8.541561416874595e-06, "-13": 1.7433556675942405e-06, "-14": 3.311502726584848e-07, "-15": 5.881619001324604e-08, "-16": 9.808119544351078e-09, "-17": 1.540359391298946e-09, "-18": 2.2628290505330914e-10, "-19": 2.7514468242713427e-11, "-2": 0.20272117395822223, "-3": 0.1479630007990887, "-4": 0.08716637709713239, "-5": 0.04280042885548902, "-6": 0.017958192508071513, "-7": 0.006565268431816166, "-8": 0.0021239671943693015, "-9": 0.0006157381194091531, "0": 0.14662437903119682, "1": 0.08335185810193589, "10": 4.0285076269401824e-08, "11": 4.23996129555878e-09, "12": 4.1050690432544644e-10, "13": 3.6789856539866307e-11, "14": 3.0684998877541937e-12, "15": 2.393077599648813e-13, "16": 1.752284188151018e-14, "17": 1.2083694884197752e-15, "18": 7.794501303628135e-17, "19": 4.161564313080615e-18, "2": 0.03656733635045595, "3": 0.011719423349255034, "4": 0.003031523969762264, "5": 0.0006536105141481779, "6": 0.0001204182829626729, "7": 1.9330415698178492e-05, "8": 2.745967601869642e-06, "9": 3.4954455689203004e-07} |
| Raw goal margin distribution | {"-1": 0.20128688857199006, "-10": 0.00015506805518087708, "-11": 3.716902282898364e-05, "-12": 8.195601231578975e-06, "-13": 1.6727442629152862e-06, "-14": 3.1773764186439e-07, "-15": 5.64339487575471e-08, "-16": 9.410859759007653e-09, "-17": 1.4779699762462324e-09, "-18": 2.171177334950018e-10, "-19": 2.6400045473036424e-11, "-2": 0.1945103268445578, "-3": 0.14197003245582776, "-4": 0.08363586382206586, "-5": 0.04106687645506678, "-6": 0.017230829054898544, "-7": 0.006299354347454562, "-8": 0.0020379398220584104, "-9": 0.0005907987829707911, "0": 0.17223749161678242, "1": 0.08548352444820985, "10": 4.1315339340868606e-08, "11": 4.348395384600844e-09, "12": 4.2100533558769247e-10, "13": 3.7730731774757554e-11, "14": 3.1469746583618458e-12, "15": 2.4542789105656587e-13, "16": 1.7970976490389736e-14, "17": 1.2392727055883542e-15, "18": 7.99384030450095e-17, "19": 4.2679934533068554e-18, "2": 0.03750252078480675, "3": 0.012019139527397006, "4": 0.0031090531067415744, "5": 0.0006703261527470988, "6": 0.0001234978975881045, "7": 1.9824777762103926e-05, "8": 2.8161938314721726e-06, "9": 3.5848391811825177e-07} |
| Unadjusted home-win probability | 13.9% |
| Unadjusted draw probability | 17.2% |
| Unadjusted away-win probability | 68.9% |
| Raw p over 1 5 | 90.5% |
| Raw p under 3 5 | 45.6% |
| Raw p btts yes | 65.3% |
| P home draw | 28.2% |
| P draw away | 86.5% |
| P home away | 85.3% |
| Raw p home draw | 31.1% |
| Raw p draw away | 86.1% |
| Raw p home away | 82.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7544 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.08, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.87, "price": 2.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.35, "draw": 6.74, "home": 6.82}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.36, "draw": 6.41, "home": 7.95}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 6.82 |
| Reference draw odds | 6.74 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.22 |
| Reference Under 2.5 odds | 4.37 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:50Z |
| Home probability edge | +0.1% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.2% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | 0.0049 |
| Raw ev home | 0.1045 |
| Raw edge prob draw | 0.0366 |
| Raw ev draw | 0.1609 |
| Raw edge prob away | -0.0415 |
| Raw ev away | -0.0632 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 10.005141171105354, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,435.5993 |
| Elo away rating | 1,723.5717 |
| Elo rating diff | -227.9724 |
| Elo home expectancy | 0.2121 |

</details>


---

## 2026-11-07 — RB Leipzig vs Augsburg

The model's most likely 1X2 outcome is **RB Leipzig win** at **66.6%**. Expected goals are 2.32 for RB Leipzig and 1.02 for Augsburg (3.34 combined). The most likely exact score is 2-1 at 9.9%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 65.6%; Under 3.5 goals: 57.0%; Double Chance 1X: 84.2%; Double Chance X2: 33.4%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 75.2%; BTTS Yes (both teams score): 57.9%; BTTS No (at least one team does not score): 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 66.6% | 1.50 |
| Draw | 17.6% | 5.67 |
| Augsburg win | 15.8% | 6.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.32 |
| Augsburg expected goals | 1.02 |
| Expected total goals | 3.34 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 65.6% |
| Under 2.5 | 34.4% |
| Over 3.5 | 43.0% |
| Under 3.5 | 57.0% |
| Over 4.5 | 24.8% |
| Under 4.5 | 75.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.87% |
| 2 | 2-0 | 9.65% |
| 3 | 1-1 | 8.08% |
| 4 | 1-0 | 7.66% |
| 5 | 3-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 66.6% | 67.0% | 1.50 | -0.1% |
| Draw | 17.6% | 16.7% | 5.59 | -1.5% |
| Augsburg win | 15.8% | 16.3% | 6.00 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | cdb5f9dd39e79db69659c76cd96d0bbe |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:38:43Z |
| Market best draw last update utc | 2026-11-04T19:39:27Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | 1xBet |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Augsburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3173 |
| Dc lambda away | 1.0224 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.66 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.84 |
| Fair Over 2.5 odds | 1.52 |
| Fair Under 2.5 odds | 2.91 |
| Fair Over 3.5 odds | 2.33 |
| Fair Under 3.5 odds | 1.75 |
| Fair Over 4.5 odds | 4.02 |
| Fair Under 4.5 odds | 1.33 |
| Goal margin distribution | {"-1": 0.10098285344427808, "-10": 1.6333685127171324e-08, "-11": 1.4917483455454666e-09, "-12": 1.2521821618626359e-10, "-13": 9.722670562300431e-12, "-14": 7.021805974749037e-13, "-15": 4.739573264985449e-14, "-16": 3.0016156048682362e-15, "-17": 1.7786052745612035e-16, "-18": 8.927347376688481e-18, "-2": 0.04139726818449646, "-3": 0.01197795744202683, "-4": 0.0027576346360646425, "-5": 0.0005245777081708864, "-6": 8.479244998763646e-05, "-7": 1.1896752752544573e-05, "-8": 1.4731345696625691e-06, "-9": 1.6314092047189973e-07, "0": 0.17627086117477037, "1": 0.22295361771160513, "10": 5.476605341854646e-05, "11": 1.1336791351650663e-05, "12": 2.1568970872383807e-06, "13": 3.795900362788346e-07, "14": 6.213629886174999e-08, "15": 9.506116217901199e-09, "16": 1.3645400135714178e-09, "17": 1.8326439570347907e-10, "18": 2.0849146443365308e-11, "2": 0.19927846541527292, "3": 0.1306889219178093, "4": 0.0681961813976935, "5": 0.029403598632419193, "6": 0.01077246671345984, "7": 0.00342573476594698, "8": 0.0009614684612607184, "9": 0.00024133641240536356} |
| Raw goal margin distribution | {"-1": 0.09329791255525244, "-10": 1.5090668115659248e-08, "-11": 1.3782241435071028e-09, "-12": 1.1568892921526648e-10, "-13": 8.982761300417891e-12, "-14": 6.487436405959525e-13, "-15": 4.378884899205435e-14, "-16": 2.7731883253032183e-15, "-17": 1.6432508462229877e-16, "-18": 8.247963357068699e-18, "-2": 0.038246876329699614, "-3": 0.01106641759368977, "-4": 0.0025477746603472756, "-5": 0.0004846565874905495, "-6": 7.833962216820656e-05, "-7": 1.0991392698274505e-05, "-8": 1.3610269028329336e-06, "-9": 1.507256609734188e-07, "0": 0.19760894927613173, "1": 0.21982889148450233, "10": 5.399849949756366e-05, "11": 1.1177904630586028e-05, "12": 2.1266678720014538e-06, "13": 3.7427002867329916e-07, "14": 6.126544991701766e-08, "15": 9.372886665634476e-09, "16": 1.3454157938700215e-09, "17": 1.806959194902357e-10, "18": 2.0556942731342294e-11, "2": 0.1964855497686411, "3": 0.12885729834470988, "4": 0.06724040234916835, "5": 0.02899150307298866, "6": 0.010621489081360225, "7": 0.003377722612656429, "8": 0.0009479933459059197, "9": 0.0002379540487319766} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 19.8% |
| Unadjusted away-win probability | 14.6% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.2% |
| Raw p btts yes | 58.4% |
| P home draw | 84.2% |
| P draw away | 33.4% |
| P home away | 82.4% |
| Raw p home draw | 85.4% |
| Raw p draw away | 34.3% |
| Raw p home away | 80.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6564 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.73, "draw": 5.59, "home": 1.47}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.0, "draw": 5.49, "home": 1.5}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.47 |
| Reference draw odds | 5.59 |
| Reference away odds | 5.73 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.26 |
| Reference Under 2.5 odds | 3.92 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:50Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.9% |
| Away probability edge | -0.5% |
| Over 2.5 probability edge | -12.0% |
| Under 2.5 probability edge | +12.0% |
| Raw edge prob home | -0.0133 |
| Raw ev home | -0.0150 |
| Raw edge prob draw | 0.0305 |
| Raw ev draw | 0.1046 |
| Raw edge prob away | -0.0171 |
| Raw ev away | -0.1256 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 10.789920045497722, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,597.4693 |
| Elo away rating | 1,452.7722 |
| Elo rating diff | 204.6971 |
| Elo home expectancy | 0.7646 |

</details>


---

## 2026-11-07 — SC Paderborn vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Eintracht Frankfurt win** at **42.7%**. Expected goals are 0.92 for SC Paderborn and 1.09 for Eintracht Frankfurt (2.01 combined). The most likely exact score is 0-1 at 15.2%. Goal-market probabilities: at least one goal: 88.0%; Over 2.5 goals: 34.3%; Under 3.5 goals: 85.3%; Double Chance 1X: 57.3%; Double Chance X2: 69.7%; Double Chance 12 (either team wins): 73.0%; Under 4.5 goals: 94.3%; BTTS Yes (both teams score): 39.6%; BTTS No (at least one team does not score): 60.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 30.3% | 3.30 |
| Draw | 27.0% | 3.70 |
| Eintracht Frankfurt win | 42.7% | 2.34 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 0.92 |
| Eintracht Frankfurt expected goals | 1.09 |
| Expected total goals | 2.01 |
| Over 0.5 | 88.0% |
| Under 0.5 | 12.0% |
| Over 1.5 | 61.1% |
| Under 1.5 | 38.9% |
| Over 2.5 | 34.3% |
| Under 2.5 | 65.7% |
| Over 3.5 | 14.7% |
| Under 3.5 | 85.3% |
| Over 4.5 | 5.7% |
| Under 4.5 | 94.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 15.22% |
| 2 | 0-0 | 11.96% |
| 3 | 1-1 | 11.95% |
| 4 | 1-0 | 11.73% |
| 5 | 0-2 | 8.92% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 30.3% | 30.8% | 3.14 | -4.7% |
| Draw | 27.0% | 24.5% | 4.16 | +12.3% |
| Eintracht Frankfurt win | 42.7% | 44.6% | 2.25 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T14:30:00+00:00 |
| Fixture id | 4ca4c7a2a1c15e9121f9a7eaa7f42ddb |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:27Z |
| Market best draw last update utc | 2026-11-04T19:38:43Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9188 |
| Dc lambda away | 1.0876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.6% |
| P btts no | 60.4% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.36 |
| Fair Over 1.5 odds | 1.64 |
| Fair Under 1.5 odds | 2.57 |
| Fair Over 2.5 odds | 2.91 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.81 |
| Fair Under 3.5 odds | 1.17 |
| Fair Over 4.5 odds | 17.59 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.24902485994418594, "-10": 1.0539812526476085e-07, "-11": 1.0342662723868037e-08, "-12": 9.291188605534102e-10, "-13": 7.218420242768157e-11, "-2": 0.12290405704559612, "-3": 0.04127880867157143, "-4": 0.010705858745749254, "-5": 0.0022553712611473454, "-6": 0.000399490553712612, "-7": 6.0996833359768444e-05, "-8": 8.180371052398659e-06, "-9": 9.778106068922416e-07, "0": 0.26997455196765646, "1": 0.19304987220709915, "10": 1.806113354375143e-08, "11": 1.497220141646331e-09, "12": 1.1362287007018592e-10, "13": 7.457234876776206e-12, "2": 0.08119866543911876, "3": 0.02303833068645548, "4": 0.00504761872248786, "5": 0.0008983059090265143, "6": 0.00013441691060447943, "7": 1.733787489707776e-05, "8": 1.9642771271879457e-06, "9": 1.9834702050386572e-07} |
| Raw goal margin distribution | {"-1": 0.22199790360831123, "-10": 9.395914471457721e-08, "-11": 9.220161565159177e-09, "-12": 8.282805150137606e-10, "-13": 6.434996737343779e-11, "-2": 0.10956513745332057, "-3": 0.036798771779618, "-4": 0.0095439395023281, "-5": 0.0020105932072218132, "-6": 0.0003561333814439272, "-7": 5.437677642163554e-05, "-8": 7.29254591199306e-06, "-9": 8.71687689753949e-07, "0": 0.3275171978767369, "1": 0.18589828208587675, "10": 1.739205346225308e-08, "11": 1.4417551747345355e-09, "12": 1.0941367694382549e-10, "13": 7.180979385556942e-12, "2": 0.0781906366485693, "3": 0.022184868851629923, "4": 0.004860628180724041, "5": 0.0008650278985757333, "6": 0.00012943739604166747, "7": 1.6695588147962924e-05, "8": 1.8915098948788224e-06, "9": 1.909991959433417e-07} |
| Unadjusted home-win probability | 29.2% |
| Unadjusted draw probability | 32.8% |
| Unadjusted away-win probability | 38.0% |
| Raw p over 1 5 | 60.6% |
| Raw p under 3 5 | 85.6% |
| Raw p btts yes | 40.9% |
| P home draw | 57.3% |
| P draw away | 69.7% |
| P home away | 73.0% |
| Raw p home draw | 62.0% |
| Raw p draw away | 70.8% |
| Raw p home away | 67.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.3433 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.31, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.72, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.19, "draw": 3.92, "home": 3.14}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.25, "draw": 4.16, "home": 3.02}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.14 |
| Reference draw odds | 3.92 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:50Z |
| Home probability edge | -0.5% |
| Draw probability edge | +2.5% |
| Away probability edge | -2.0% |
| Over 2.5 probability edge | -32.6% |
| Under 2.5 probability edge | +32.6% |
| Raw edge prob home | -0.0161 |
| Raw ev home | -0.0827 |
| Raw edge prob draw | 0.0822 |
| Raw ev draw | 0.3625 |
| Raw edge prob away | -0.0661 |
| Raw ev away | -0.1442 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 10.369353851708599, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,409.3829 |
| Elo away rating | 1,482.9965 |
| Elo rating diff | -13.6136 |
| Elo home expectancy | 0.4804 |

</details>


---

## 2026-11-07 — VfB Stuttgart vs Werder Bremen

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **60.9%**. Expected goals are 2.28 for VfB Stuttgart and 1.18 for Werder Bremen (3.47 combined). The most likely exact score is 2-1 at 9.5%. Goal-market probabilities: at least one goal: 96.4%; Over 2.5 goals: 67.6%; Under 3.5 goals: 54.4%; Double Chance 1X: 80.6%; Double Chance X2: 39.1%; Double Chance 12 (either team wins): 80.2%; Under 4.5 goals: 73.1%; BTTS Yes (both teams score): 62.9%; BTTS No (at least one team does not score): 37.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 60.9% | 1.64 |
| Draw | 19.8% | 5.06 |
| Werder Bremen win | 19.4% | 5.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.28 |
| Werder Bremen expected goals | 1.18 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.4% |
| Under 0.5 | 3.6% |
| Over 1.5 | 86.7% |
| Under 1.5 | 13.3% |
| Over 2.5 | 67.6% |
| Under 2.5 | 32.4% |
| Over 3.5 | 45.6% |
| Under 3.5 | 54.4% |
| Over 4.5 | 26.9% |
| Under 4.5 | 73.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.55% |
| 2 | 1-1 | 8.72% |
| 3 | 2-0 | 8.06% |
| 4 | 3-1 | 7.26% |
| 5 | 1-0 | 6.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 60.9% | 60.6% | 1.62 | -1.4% |
| Draw | 19.8% | 19.4% | 5.03 | -0.6% |
| Werder Bremen win | 19.4% | 20.0% | 5.08 | -1.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T17:30:00+00:00 |
| Fixture id | 716d6e3f3e91c47a6efaa2e93d570533 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:39:27Z |
| Market best draw last update utc | 2026-11-04T19:38:43Z |
| Market best away last update utc | 2026-11-04T19:38:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Stuttgart |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2830 |
| Dc lambda away | 1.1839 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-11-04T19:39:12.830329+00:00 |
| Bbs statistics weight | 0 |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 62.9% |
| P btts no | 37.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 27.57 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.52 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.08 |
| Fair Over 3.5 odds | 2.19 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.71 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.11701566117862491, "-10": 6.397422897813126e-08, "-11": 6.7497028818793295e-09, "-12": 6.547553281812248e-10, "-13": 5.8768180134256e-11, "-14": 4.907379759700339e-12, "-15": 3.8305593363079777e-13, "-16": 2.8054715369303748e-14, "-17": 1.9191682813839708e-15, "-18": 1.0975138254825358e-16, "-2": 0.05344338318721743, "-3": 0.01757171274058629, "-4": 0.004624824961853765, "-5": 0.001009422936004242, "-6": 0.00018764378706237389, "-7": 3.0324776081348593e-05, "-8": 4.329915490249356e-06, "-9": 5.533665825632675e-07, "0": 0.1975973864804119, "1": 0.21364206551664222, "10": 4.182851173868955e-05, "11": 8.510033890140968e-06, "12": 1.5918603173888634e-06, "13": 2.755163898088605e-07, "14": 4.436435234413908e-08, "15": 6.67768539148945e-09, "16": 9.430808115116801e-10, "17": 1.2440429674357533e-10, "18": 1.3718657213415521e-11, "2": 0.18277931381318424, "3": 0.11588480012662099, "4": 0.05881484585864522, "5": 0.024753927396783563, "6": 0.008873284682738606, "7": 0.0027652035781084027, "8": 0.0007613567616272666, "9": 0.00018762944738095298} |
| Raw goal margin distribution | {"-1": 0.10857730323513151, "-10": 5.936085126578883e-08, "-11": 6.262961121367609e-09, "-12": 6.075389148485798e-10, "-13": 5.45302265589346e-11, "-14": 4.553493565665224e-12, "-15": 3.5543259631168866e-13, "-16": 2.6031603865215136e-14, "-17": 1.7807711749710446e-15, "-18": 1.0183687399950717e-16, "-2": 0.04958941703856145, "-3": 0.016304562683134013, "-4": 0.00429131466023224, "-5": 0.0009366303545277056, "-6": 0.00017411221850858945, "-7": 2.8137963542298045e-05, "-8": 4.017672014429258e-06, "-9": 5.134616224014946e-07, "0": 0.2062024713903478, "1": 0.2155297829495819, "10": 4.2198103797313855e-05, "11": 8.585227599256626e-06, "12": 1.605925817386128e-06, "13": 2.779508218615795e-07, "14": 4.4756350807169234e-08, "15": 6.736688673894147e-09, "16": 9.51413768245909e-10, "17": 1.2550351921705005e-10, "18": 1.3839873736555115e-11, "2": 0.18439433141859593, "3": 0.11690874527938265, "4": 0.05933452726864535, "5": 0.024972650334926065, "6": 0.008951688035292496, "7": 0.0027896366081270898, "8": 0.0007680840249503144, "9": 0.00018928732022494246} |
| Unadjusted home-win probability | 61.4% |
| Unadjusted draw probability | 20.6% |
| Unadjusted away-win probability | 18.0% |
| Raw p over 1 5 | 86.7% |
| Raw p under 3 5 | 54.4% |
| Raw p btts yes | 63.0% |
| P home draw | 80.6% |
| P draw away | 39.1% |
| P home away | 80.2% |
| Raw p home draw | 82.0% |
| Raw p draw away | 38.6% |
| Raw p home away | 79.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6756 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.45, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:39:27Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 4.72, "draw": 4.86, "home": 1.62}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:38:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 5.08, "draw": 5.03, "home": 1.61}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.62 |
| Reference draw odds | 4.86 |
| Reference away odds | 4.72 |
| Market reference 1x2 last update utc | 2026-11-04T19:39:27Z |
| Market reference home last update utc | 2026-11-04T19:39:27Z |
| Market reference draw last update utc | 2026-11-04T19:39:27Z |
| Market reference away last update utc | 2026-11-04T19:39:27Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.32 |
| Reference Under 2.5 odds | 3.45 |
| Market reference over 2 5 last update utc | 2026-11-04T19:38:50Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:38:50Z |
| Home probability edge | +0.2% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0077 |
| Raw ev home | -0.0055 |
| Raw edge prob draw | 0.0123 |
| Raw ev draw | 0.0372 |
| Raw edge prob away | -0.0200 |
| Raw ev away | -0.0861 |
| Count model | {"corners": {"alpha": 0.011808948491057953, "mu": 10.720328364730342, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,547.4698 |
| Elo away rating | 1,475.4921 |
| Elo rating diff | 131.9777 |
| Elo home expectancy | 0.6813 |

</details>


---
