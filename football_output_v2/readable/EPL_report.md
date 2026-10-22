# Premier League — football model report

Fixtures in this report: **16**.

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
| Training sha256 | 7f888cd21de905ec7ebd8bf6b7885a178ba3c6dbf56a30a35d9a27c323a70238 |
| Training as of utc | 2026-10-22T10:54:22.405766+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 70, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 70, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 60, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-22T10:54:22.405766+00:00', 'observations': 183, 'observations_sha256': '5cb7a1dab5f5cad3b3f5e2c0e689fbcfaceb0a0b035768bad5c1d3e9776a02c7', 'eligible_training_matches': 103, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 101, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 103, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': 'e7b8040af70a2d04fb867366305dac27229fd0a82372362664d7c723d32db320', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 928.080 |
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
| Live odds matched | 16.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261022T105422405766Z_a3205e99eed355944bd6141c600d09371896d2a30c2b9564feb6cada1239c708.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
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

The model's most likely 1X2 outcome is **Nottingham Forest win** at **44.0%**. Expected goals are 1.32 for Ipswich Town and 1.69 for Nottingham Forest (3.01 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 94.0%; Over 2.5 goals: 57.8%; Under 3.5 goals: 64.5%; Double Chance 1X: 56.0%; Double Chance X2: 70.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 81.4%; BTTS Yes (both teams score): 60.9%; BTTS No (at least one team does not score): 39.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Ipswich Town win | 29.8% | 3.36 |
| Draw | 26.2% | 3.81 |
| Nottingham Forest win | 44.0% | 2.27 |

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
| Over 2.5 | 57.8% |
| Under 2.5 | 42.2% |
| Over 3.5 | 35.5% |
| Under 3.5 | 64.5% |
| Over 4.5 | 18.6% |
| Under 4.5 | 81.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.19% |
| 2 | 1-2 | 9.04% |
| 3 | 2-1 | 7.45% |
| 4 | 0-1 | 7.14% |
| 5 | 0-2 | 6.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Ipswich Town win | 29.8% | 30.5% | 3.32 | -1.1% |
| Draw | 26.2% | 26.7% | 3.49 | -8.4% |
| Nottingham Forest win | 44.0% | 42.8% | 2.24 | -1.5% |
| Over 2.5 | 57.8% | 55.7% | 1.83 | +5.7% |
| Under 2.5 | 42.2% | 44.3% | 2.14 | -9.6% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ipswich |
| Matched away-team name | Nott'm Forest |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3208 |
| Dc lambda away | 1.6908 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 60.9% |
| P btts no | 39.1% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.64 |
| Fair Over 1.5 odds | 1.23 |
| Fair Under 1.5 odds | 5.32 |
| Fair Over 2.5 odds | 1.73 |
| Fair Under 2.5 odds | 2.37 |
| Fair Over 3.5 odds | 2.82 |
| Fair Under 3.5 odds | 1.55 |
| Fair Over 4.5 odds | 5.38 |
| Fair Under 4.5 odds | 1.23 |
| Goal margin distribution | {"-1": 0.20250427505508722, "-10": 3.0819062495762062e-06, "-11": 4.6594391736041477e-07, "-12": 6.473465186796822e-08, "-13": 8.314604522668698e-09, "-14": 9.84871570347178e-10, "-15": 9.662841342471317e-11, "-2": 0.13595712868259707, "-3": 0.06557423375524755, "-4": 0.02510078776189075, "-5": 0.007926744103202854, "-6": 0.002124978112433015, "-7": 0.000494146573586471, "-8": 0.00010136845719722227, "-9": 1.8591475284696876e-05, "0": 0.26232176197247564, "1": 0.16455676844033082, "10": 2.749498233652755e-07, "11": 3.2472917656021035e-08, "12": 3.5243426417071408e-09, "13": 3.5361977872685066e-10, "14": 3.272112260351498e-11, "15": 2.507881927926101e-12, "2": 0.08745947389384817, "3": 0.032952756116101864, "4": 0.009853704049591147, "5": 0.002430863900055006, "6": 0.0005090657869184645, "7": 9.247596681351741e-05, "8": 1.4819364220058178e-05, "9": 2.1232162626486885e-06} |
| Raw goal margin distribution | {"-1": 0.2081062996555198, "-10": 3.1671632873432167e-06, "-11": 4.788336664126996e-07, "-12": 6.652545412222258e-08, "-13": 8.544617538770144e-09, "-14": 1.0121167964731482e-09, "-15": 9.93015162466598e-11, "-2": 0.13971821066112267, "-3": 0.06738826198033801, "-4": 0.02579516930269574, "-5": 0.008146027451445237, "-6": 0.002183762943805054, "-7": 0.0005078165134467421, "-8": 0.0001041726873339552, "-9": 1.9105784930134596e-05, "0": 0.25763611798226477, "1": 0.16042394462584958, "10": 2.6804449100756416e-07, "11": 3.165736416231497e-08, "12": 3.4358291922872806e-09, "13": 3.447386597267298e-10, "14": 3.189933547185165e-11, "15": 2.444896769346019e-12, "2": 0.08526293953104827, "3": 0.032125151536112805, "4": 0.009606229435553823, "5": 0.0023698130401534102, "6": 0.0004962806597720408, "7": 9.015344382320565e-05, "8": 1.4447177637004709e-05, "9": 2.0698919368446725e-06} |
| Unadjusted home-win probability | 29.0% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 45.2% |
| Raw p over 1 5 | 81.2% |
| Raw p under 3 5 | 64.5% |
| Raw p btts yes | 60.8% |
| P home draw | 56.0% |
| P draw away | 70.2% |
| P home away | 73.8% |
| Raw p home draw | 54.8% |
| Raw p draw away | 71.0% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.7, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.48, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.31, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 7.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-22T10:54:19Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.21, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.31, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.18, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.88, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.44, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-22T10:54:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 6.21, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 3.20 |
| Reference draw odds | 3.65 |
| Reference away odds | 2.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.14 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -0.7% |
| Draw probability edge | -0.5% |
| Away probability edge | +1.2% |
| Over 2.5 probability edge | +2.1% |
| Under 2.5 probability edge | -2.1% |
| Raw edge prob home | -0.0150 |
| Raw ev home | -0.0359 |
| Raw edge prob draw | -0.0094 |
| Raw ev draw | -0.1008 |
| Raw edge prob away | 0.0243 |
| Raw ev away | 0.0124 |
| Market p home draw | 57.8% |
| Market home draw odds | 1.69 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-22T10:54:11Z |
| Market reference home draw last update utc | 2026-10-22T10:54:21Z |
| Market home draw bookmakers | 2 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 69.8% |
| Market draw away odds | 1.36 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-22T10:54:11Z |
| Market reference draw away last update utc | 2026-10-22T10:54:21Z |
| Market draw away bookmakers | 2 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.4% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-22T10:54:11Z |
| Market reference home away last update utc | 2026-10-22T10:54:21Z |
| Market home away bookmakers | 2 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.68 |
| Market reference dc draw away odds | 1.39 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 78.7% |
| Market over 1 5 odds | 1.24 |
| Best over 1 5 bookmaker | 1xBet |
| Market best over 1 5 last update utc | 2026-10-22T10:54:19Z |
| Market reference over 1 5 odds | 1.25 |
| Market reference over 1 5 opposite odds | 4.20 |
| Market reference over 1 5 last update utc | 2026-10-22T10:54:23Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.5% |
| Market under 3 5 odds | 1.44 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-22T10:54:21Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.90 |
| Market reference under 3 5 last update utc | 2026-10-22T10:54:23Z |
| Market under 3 5 bookmakers | 2 |
| Market p btts yes | 59.5% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-22T10:54:11Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-22T10:54:21Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-24 — Arsenal vs Everton

The model's most likely 1X2 outcome is **Arsenal win** at **67.5%**. Expected goals are 1.72 for Arsenal and 0.58 for Everton (2.29 combined). The most likely exact score is 1-0 at 17.3%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 41.3%; Under 3.5 goals: 79.7%; Double Chance 1X: 89.5%; Double Chance X2: 32.5%; Double Chance 12 (either team wins): 78.1%; Under 4.5 goals: 91.4%; BTTS Yes (both teams score): 36.1%; BTTS No (at least one team does not score): 63.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Arsenal win | 67.5% | 1.48 |
| Draw | 21.9% | 4.56 |
| Everton win | 10.5% | 9.50 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Arsenal expected goals | 1.72 |
| Everton expected goals | 0.58 |
| Expected total goals | 2.29 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 68.2% |
| Under 1.5 | 31.8% |
| Over 2.5 | 41.3% |
| Under 2.5 | 58.7% |
| Over 3.5 | 20.3% |
| Under 3.5 | 79.7% |
| Over 4.5 | 8.6% |
| Under 4.5 | 91.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 17.29% |
| 2 | 2-0 | 15.64% |
| 3 | 0-0 | 9.79% |
| 4 | 1-1 | 9.69% |
| 5 | 2-1 | 9.01% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Arsenal win | 67.5% | 70.8% | 1.43 | -3.4% |
| Draw | 21.9% | 19.2% | 4.43 | -2.9% |
| Everton win | 10.5% | 10.0% | 8.63 | -9.1% |
| Over 2.5 | 41.3% | 54.0% | 1.89 | -21.9% |
| Under 2.5 | 58.7% | 46.0% | 2.06 | +20.9% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 17.00 |
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
| Dc lambda away | 0.5763 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 36.1% |
| P btts no | 63.9% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.22 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.15 |
| Fair Over 2.5 odds | 2.42 |
| Fair Under 2.5 odds | 1.70 |
| Fair Over 3.5 odds | 4.92 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.64 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.07895262004665975, "-10": 1.1672443517086012e-10, "-11": 6.0703057582951225e-12, "-12": 2.897092402760111e-13, "-13": 1.277435395278684e-14, "-14": 5.233901347320148e-16, "-15": 1.9993352999460666e-17, "-16": 6.782420832757144e-19, "-2": 0.021848291985501398, "-3": 0.003891203399836598, "-4": 0.0005350166483800283, "-5": 5.9743329940044206e-05, "-6": 5.6087415131561746e-06, "-7": 4.538675983385781e-07, "-8": 3.2258276377563406e-08, "-9": 2.043418407487308e-09, "0": 0.2192747352256696, "1": 0.2791450162304518, "10": 7.078654662685449e-06, "11": 1.0959590639510183e-06, "12": 1.5571875927560665e-07, "13": 2.0441480854396395e-08, "14": 2.4934103793599984e-09, "15": 2.835624277483524e-10, "16": 2.863799485905981e-11, "2": 0.21470782046548223, "3": 0.1138437325676542, "4": 0.04660014967787331, "5": 0.015491884918646377, "6": 0.004329872257141048, "7": 0.0010431185277093146, "8": 0.00022071937608144805, "9": 4.1624729491335624e-05} |
| Raw goal margin distribution | {"-1": 0.08327666307331427, "-10": 1.2311714866969601e-10, "-11": 6.4027616447280805e-12, "-12": 3.055759109378908e-13, "-13": 1.3473974257938469e-14, "-14": 5.520549397881389e-16, "-15": 2.108834032940194e-17, "-16": 7.153877530310537e-19, "-2": 0.02304486981342386, "-3": 0.0041043151485843175, "-4": 0.0005643182093187854, "-5": 6.301532685494962e-05, "-6": 5.915918648176366e-06, "-7": 4.787248231204856e-07, "-8": 3.4024983738761344e-08, "-9": 2.1553314650933912e-09, "0": 0.24640380492789277, "1": 0.2655497624269301, "10": 6.73390157331902e-06, "11": 1.042582357342066e-06, "12": 1.4813475837560987e-07, "13": 1.944591545226893e-08, "14": 2.3719733306120133e-09, "15": 2.697520318959006e-10, "16": 2.7243233047473537e-11, "2": 0.20425086389055505, "3": 0.10829917920575663, "4": 0.04433057356038404, "5": 0.014737380646250308, "6": 0.004118993649786432, "7": 0.000992315323973604, "8": 0.00020996963754875317, "9": 3.959747222706674e-05} |
| Unadjusted home-win probability | 64.3% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 11.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 36.8% |
| P home draw | 89.5% |
| P draw away | 32.5% |
| P home away | 78.1% |
| Raw p home draw | 88.9% |
| Raw p draw away | 35.7% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.99, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.40 |
| Reference draw odds | 5.00 |
| Reference away odds | 9.50 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.78 |
| Reference Under 2.5 odds | 2.07 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -3.3% |
| Draw probability edge | +2.7% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -12.7% |
| Under 2.5 probability edge | +12.7% |
| Raw edge prob home | -0.0658 |
| Raw ev home | -0.0812 |
| Raw edge prob draw | 0.0543 |
| Raw ev draw | 0.0916 |
| Raw edge prob away | 0.0115 |
| Raw ev away | -0.0416 |

</details>


---

## 2026-10-24 — Aston Villa vs Manchester City

The model's most likely 1X2 outcome is **Manchester City win** at **55.0%**. Expected goals are 1.12 for Aston Villa and 1.82 for Manchester City (2.95 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 94.1%; Over 2.5 goals: 57.1%; Under 3.5 goals: 65.7%; Double Chance 1X: 45.0%; Double Chance X2: 78.4%; Double Chance 12 (either team wins): 76.6%; Under 4.5 goals: 82.1%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Aston Villa win | 21.6% | 4.62 |
| Draw | 23.4% | 4.27 |
| Manchester City win | 55.0% | 1.82 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Aston Villa expected goals | 1.12 |
| Manchester City expected goals | 1.82 |
| Expected total goals | 2.95 |
| Over 0.5 | 94.1% |
| Under 0.5 | 5.9% |
| Over 1.5 | 80.4% |
| Under 1.5 | 19.6% |
| Over 2.5 | 57.1% |
| Under 2.5 | 42.9% |
| Over 3.5 | 34.3% |
| Under 3.5 | 65.7% |
| Over 4.5 | 17.9% |
| Under 4.5 | 82.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.03% |
| 2 | 1-2 | 10.20% |
| 3 | 0-2 | 9.09% |
| 4 | 0-1 | 8.97% |
| 5 | 1-3 | 6.20% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Aston Villa win | 21.6% | 21.0% | 4.54 | -1.7% |
| Draw | 23.4% | 22.0% | 4.29 | +0.4% |
| Manchester City win | 55.0% | 57.1% | 1.71 | -6.0% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Aston Villa |
| Matched away-team name | Man City |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1221 |
| Dc lambda away | 1.8242 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.09 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.10 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.92 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.60 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.23307983172988622, "-10": 7.390549587007044e-06, "-11": 1.2071560078677374e-06, "-12": 1.8115897599136787e-07, "-13": 2.5140745482954484e-08, "-14": 3.243532104665981e-09, "-15": 3.885166581107758e-10, "-16": 3.9271982606187386e-11, "-2": 0.1711643064716322, "-3": 0.09006410000825554, "-4": 0.03747349374237416, "-5": 0.012835553191769537, "-6": 0.0037270716113166663, "-7": 0.0009379295072477027, "-8": 0.00020808714014513234, "-9": 4.125599491153271e-05, "0": 0.23403864210437297, "1": 0.13016780029076755, "10": 5.346551511067985e-08, "11": 5.3717620202804704e-09, "12": 4.958719763899051e-10, "13": 4.2329603809793006e-11, "14": 3.3592366294282684e-12, "15": 2.475075121053276e-13, "16": 1.538926616683457e-14, "2": 0.06041704394831118, "3": 0.01955484263603695, "4": 0.005004758676512391, "5": 0.0010544594680537308, "6": 0.00018833861884268543, "7": 2.9154002518984894e-05, "8": 3.978593543658369e-06, "9": 4.852077632702839e-07} |
| Raw goal margin distribution | {"-1": 0.22411352049142266, "-10": 7.106243702072314e-06, "-11": 1.1607181140371513e-06, "-12": 1.7418999995288173e-07, "-13": 2.4173610115238912e-08, "-14": 3.1187571803555528e-09, "-15": 3.7357087214510715e-10, "-16": 3.7761234909206565e-11, "-2": 0.16457981379652603, "-3": 0.08659943836810993, "-4": 0.03603193182947502, "-5": 0.012341784323047196, "-6": 0.0035836954820862525, "-7": 0.0009018484451527736, "-8": 0.00020008226881235538, "-9": 3.966892455849606e-05, "0": 0.2485359850371314, "1": 0.13416318134635868, "10": 5.5106589982679394e-08, "11": 5.536643320901903e-09, "12": 5.110923111888431e-10, "13": 4.362887211404754e-11, "14": 3.4623453119172175e-12, "15": 2.551045278248309e-13, "16": 1.586162555498643e-14, "2": 0.062271489612190326, "3": 0.02015506056734227, "4": 0.005158375146632316, "5": 0.0010868251327814107, "6": 0.00019411949973703388, "7": 3.004885784494734e-05, "8": 4.100712817677916e-06, "9": 5.00100769843841e-07} |
| Unadjusted home-win probability | 22.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 52.8% |
| Raw p over 1 5 | 80.2% |
| Raw p under 3 5 | 65.9% |
| Raw p btts yes | 57.5% |
| P home draw | 45.0% |
| P draw away | 78.4% |
| P home away | 76.6% |
| Raw p home draw | 47.2% |
| Raw p draw away | 77.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 4.60 |
| Reference draw odds | 4.40 |
| Reference away odds | 1.73 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.45 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | +0.7% |
| Draw probability edge | +1.4% |
| Away probability edge | -2.1% |
| Over 2.5 probability edge | -6.4% |
| Under 2.5 probability edge | +6.4% |
| Raw edge prob home | 0.0133 |
| Raw ev home | 0.0127 |
| Raw edge prob draw | 0.0290 |
| Raw ev draw | 0.0662 |
| Raw edge prob away | -0.0423 |
| Raw ev away | -0.0964 |

</details>


---

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **57.4%**. Expected goals are 2.13 for Chelsea and 1.19 for Tottenham Hotspur (3.33 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.5%; Under 3.5 goals: 57.5%; Double Chance 1X: 79.6%; Double Chance X2: 42.6%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 62.3%; BTTS No (at least one team does not score): 37.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 57.4% | 1.74 |
| Draw | 22.2% | 4.51 |
| Tottenham Hotspur win | 20.4% | 4.90 |

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
| Over 3.5 | 42.5% |
| Under 3.5 | 57.5% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.99% |
| 2 | 2-1 | 9.64% |
| 3 | 2-0 | 8.08% |
| 4 | 3-1 | 6.86% |
| 5 | 1-0 | 6.77% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 57.4% | 56.8% | 1.69 | -3.0% |
| Draw | 22.2% | 22.2% | 4.40 | -2.4% |
| Tottenham Hotspur win | 20.4% | 21.0% | 4.57 | -6.7% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1331 |
| Dc lambda away | 1.1933 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.3% |
| P btts no | 37.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.63 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.77 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.82 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.14 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.1214851515426803, "-10": 7.505633389591903e-08, "-11": 7.990807158162409e-09, "-12": 7.820529739709063e-10, "-13": 7.080965220003183e-11, "-14": 5.964008287345738e-12, "-15": 4.693118852342234e-13, "-16": 3.4367024458862985e-14, "-17": 2.0982508061977397e-15, "-2": 0.057126948776735284, "-3": 0.019099444585179193, "-4": 0.005097396749561627, "-5": 0.001126258780726746, "-6": 0.000211709200309197, "-7": 3.457211646429608e-05, "-8": 4.985486312347732e-06, "-9": 6.432483910743883e-07, "0": 0.22180724869359844, "1": 0.2149490309315218, "10": 2.4006955363795605e-05, "11": 4.568579055133688e-06, "12": 7.992219875264376e-07, "13": 1.2934941524260043e-07, "14": 1.947381337898521e-08, "15": 2.7391453314239816e-09, "16": 3.5853884207795e-10, "17": 3.912843115029494e-11, "2": 0.17533342219853817, "3": 0.1047816362942016, "4": 0.049986604031181193, "5": 0.019741681551125555, "6": 0.006633251149029972, "7": 0.001936214346003211, "8": 0.0004990864183244487, "9": 0.00011510327719448759} |
| Raw goal margin distribution | {"-1": 0.11800542445269503, "-10": 7.290647809036528e-08, "-11": 7.761924633952549e-09, "-12": 7.59652451069356e-10, "-13": 6.878143507337895e-11, "-14": 5.793179828568348e-12, "-15": 4.558692771462065e-13, "-16": 3.338264188623493e-14, "-17": 2.0381501265739867e-15, "-2": 0.05549064846593748, "-3": 0.018552374808480005, "-4": 0.004951390844044681, "-5": 0.0010939990918687888, "-6": 0.00020564516507394257, "-7": 3.3581859394264996e-05, "-8": 4.84268588317979e-06, "-9": 6.248236797118263e-07, "0": 0.22122757711669272, "1": 0.21735623166204285, "10": 2.4275807752842787e-05, "11": 4.619742285743762e-06, "12": 8.081724244922829e-07, "13": 1.3079799123996634e-07, "14": 1.9691899394952682e-08, "15": 2.7698208483790115e-09, "16": 3.625540961073817e-10, "17": 3.9566627999291853e-11, "2": 0.1772969702088362, "3": 0.10595507927433279, "4": 0.050546400877990234, "5": 0.01996276740597048, "6": 0.006707536513064767, "7": 0.0019578978891573516, "8": 0.000504675655854747, "9": 0.00011639231158439474} |
| Unadjusted home-win probability | 58.0% |
| Unadjusted draw probability | 22.1% |
| Unadjusted away-win probability | 19.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 62.2% |
| P home draw | 79.6% |
| P draw away | 42.6% |
| P home away | 77.8% |
| Raw p home draw | 80.2% |
| Raw p draw away | 42.0% |
| Raw p home away | 77.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.89, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.49, "price": 2.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.74 |
| Reference draw odds | 4.35 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | +0.6% |
| Draw probability edge | -0.1% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +0.7% |
| Under 2.5 probability edge | -0.7% |
| Raw edge prob home | 0.0129 |
| Raw ev home | -0.0191 |
| Raw edge prob draw | -0.0012 |
| Raw ev draw | -0.0266 |
| Raw edge prob away | -0.0117 |
| Raw ev away | -0.0936 |

</details>


---

## 2026-10-24 — Coventry City vs Fulham

The model's most likely 1X2 outcome is **Fulham win** at **41.1%**. Expected goals are 1.10 for Coventry City and 1.37 for Fulham (2.47 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.4%; Double Chance 1X: 58.9%; Double Chance X2: 68.9%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 89.4%; BTTS Yes (both teams score): 50.6%; BTTS No (at least one team does not score): 49.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 31.1% | 3.21 |
| Draw | 27.8% | 3.60 |
| Fulham win | 41.1% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.10 |
| Fulham expected goals | 1.37 |
| Expected total goals | 2.47 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 23.6% |
| Under 3.5 | 76.4% |
| Over 4.5 | 10.6% |
| Under 4.5 | 89.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.22% |
| 2 | 0-1 | 10.29% |
| 3 | 0-0 | 9.15% |
| 4 | 1-0 | 8.78% |
| 5 | 1-2 | 8.58% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 31.1% | 33.2% | 3.09 | -3.8% |
| Draw | 27.8% | 26.4% | 3.55 | -1.4% |
| Fulham win | 41.1% | 40.5% | 2.33 | -4.2% |
| Over 2.5 | 45.3% | 55.3% | 1.81 | -18.1% |
| Under 2.5 | 54.7% | 44.7% | 2.15 | +17.7% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda away | 1.3666 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 50.6% |
| P btts no | 49.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.93 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.24 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.45 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21311847315136112, "-10": 5.987219711239814e-07, "-11": 7.355131825541111e-08, "-12": 8.295275466845944e-09, "-13": 8.607557475481927e-10, "-14": 7.586772883651299e-11, "-2": 0.12517673409668972, "-3": 0.051049463319610904, "-4": 0.016273230616295653, "-5": 0.004242169854291185, "-6": 0.0009336262658989426, "-7": 0.00017759306122690425, "-8": 2.9725881893700713e-05, "-9": 4.44041490132597e-06, "0": 0.2777298968131372, "1": 0.18445974441180826, "10": 7.503169365487397e-08, "11": 7.425791733212682e-09, "12": 6.747080096738614e-10, "13": 5.6402419487917364e-11, "14": 4.005047174187069e-12, "2": 0.08840588448229714, "3": 0.029045675923165665, "4": 0.0074592787251313965, "5": 0.0015665485515968084, "6": 0.00027775482811545507, "7": 4.2564476713781203e-05, "8": 5.7396948359119075e-06, "9": 6.907332398178009e-07} |
| Raw goal margin distribution | {"-1": 0.21648329437755115, "-10": 6.081748935630112e-07, "-11": 7.471258331714177e-08, "-12": 8.426245431838666e-09, "-13": 8.743457905279872e-10, "-14": 7.706556654901678e-11, "-2": 0.1271530870879883, "-3": 0.051855457822215276, "-4": 0.01653016053413298, "-5": 0.004309147357272281, "-6": 0.0009483668251304931, "-7": 0.00018039698945144603, "-8": 3.01952090096664e-05, "-9": 4.510522396430162e-06, "0": 0.29194184561781444, "1": 0.17219194709287886, "10": 7.004158801860557e-08, "11": 6.93192729571104e-09, "12": 6.29835448787849e-10, "13": 5.265128423192213e-11, "14": 3.738684954384858e-12, "2": 0.08252630638742434, "3": 0.02711394568927138, "4": 0.0069631871804037865, "5": 0.001462362675255424, "6": 0.0002592822885023278, "7": 3.973365649890981e-05, "8": 5.3579670332197715e-06, "9": 6.447948947628799e-07} |
| Unadjusted home-win probability | 29.1% |
| Unadjusted draw probability | 29.2% |
| Unadjusted away-win probability | 41.7% |
| Raw p over 1 5 | 71.7% |
| Raw p under 3 5 | 76.4% |
| Raw p btts yes | 50.9% |
| P home draw | 58.9% |
| P draw away | 68.9% |
| P home away | 72.2% |
| Raw p home draw | 58.3% |
| Raw p draw away | 70.9% |
| Raw p home away | 70.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.25, "price": 1.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.75, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.70 |
| Reference away odds | 2.43 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -2.1% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -10.0% |
| Under 2.5 probability edge | +10.0% |
| Raw edge prob home | -0.0414 |
| Raw ev home | -0.1022 |
| Raw edge prob draw | 0.0284 |
| Raw ev draw | 0.0364 |
| Raw edge prob away | 0.0130 |
| Raw ev away | -0.0272 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.0%**. Expected goals are 1.50 for Crystal Palace and 1.58 for Newcastle United (3.08 combined). The most likely exact score is 1-1 at 11.9%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 59.4%; Under 3.5 goals: 63.0%; Double Chance 1X: 60.0%; Double Chance X2: 65.9%; Double Chance 12 (either team wins): 74.1%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 62.6%; BTTS No (at least one team does not score): 37.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.1% | 2.93 |
| Draw | 25.9% | 3.87 |
| Newcastle United win | 40.0% | 2.50 |

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
| Over 2.5 | 59.4% |
| Under 2.5 | 40.6% |
| Over 3.5 | 37.0% |
| Under 3.5 | 63.0% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.87% |
| 2 | 1-2 | 8.87% |
| 3 | 2-1 | 7.90% |
| 4 | 0-1 | 6.50% |
| 5 | 2-2 | 6.44% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.1% | 33.0% | 2.97 | +1.3% |
| Draw | 25.9% | 25.8% | 3.65 | -5.6% |
| Newcastle United win | 40.0% | 41.1% | 2.36 | -5.5% |
| Over 2.5 | 59.4% | 59.1% | 1.69 | +0.3% |
| Under 2.5 | 40.6% | 40.9% | 2.36 | -4.1% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4954 |
| Dc lambda away | 1.5800 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.6% |
| P btts no | 37.4% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.91 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.61 |
| Fair Over 2.5 odds | 1.68 |
| Fair Under 2.5 odds | 2.46 |
| Fair Over 3.5 odds | 2.70 |
| Fair Under 3.5 odds | 1.59 |
| Fair Over 4.5 odds | 5.06 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1963908654458699, "-10": 1.570032395773732e-06, "-11": 2.2159866084672993e-07, "-12": 2.874570351706404e-08, "-13": 3.4474289820188108e-09, "-14": 3.8097748380638745e-10, "-15": 3.466780368423841e-11, "-2": 0.12218878358833539, "-3": 0.05465540923140707, "-4": 0.019450237436695234, "-5": 0.00571879101362338, "-6": 0.001428689053053014, "-7": 0.0003098001794145772, "-8": 5.928692837544203e-05, "-9": 1.0146959662033378e-05, "0": 0.2585623899428675, "1": 0.17452125050648257, "10": 8.529966287227589e-07, "11": 1.1395237573606958e-07, "12": 1.3990935220757651e-08, "13": 1.588132317835848e-09, "14": 1.6611475718953384e-10, "15": 1.4307138670974156e-11, "2": 0.10306937234999974, "3": 0.04363640780758437, "4": 0.014698001930575964, "5": 0.004090300075847461, "6": 0.0009671775621217451, "7": 0.00019850329123070494, "8": 3.595526952822456e-05, "9": 5.824478997454031e-06} |
| Raw goal margin distribution | {"-1": 0.19087030797264024, "-10": 1.5258987032212627e-06, "-11": 2.1536951092971255e-07, "-12": 2.793766029156019e-08, "-13": 3.350521573484791e-09, "-14": 3.70268186861315e-10, "-15": 3.3693289914084305e-11, "-2": 0.11875405050718119, "-3": 0.05311904282658549, "-4": 0.018903490247647196, "-5": 0.005558035499885909, "-6": 0.0013885285292381875, "-7": 0.00030109168020921867, "-8": 5.7620369725859155e-05, "-9": 9.861728096575267e-06, "0": 0.2588330868337087, "1": 0.18013670694606573, "10": 8.804429448464569e-07, "11": 1.176189470004621e-07, "12": 1.4441112417249126e-08, "13": 1.639232615508596e-09, "14": 1.7145972337710492e-10, "15": 1.476749013962781e-11, "2": 0.10638576831328163, "3": 0.04504046803814223, "4": 0.015170929951378757, "5": 0.004221910993337948, "6": 0.0009982978036606697, "7": 0.00020489040215149518, "8": 3.7112178782675025e-05, "9": 6.011889458922478e-06} |
| Unadjusted home-win probability | 35.2% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.2% |
| Raw p under 3 5 | 63.0% |
| Raw p btts yes | 62.6% |
| P home draw | 60.0% |
| P draw away | 65.9% |
| P home away | 74.1% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.8% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.95 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.38 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 2.30 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +1.1% |
| Draw probability edge | +0.0% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | +0.2% |
| Under 2.5 probability edge | -0.2% |
| Raw edge prob home | 0.0220 |
| Raw ev home | 0.0460 |
| Raw edge prob draw | 0.0005 |
| Raw ev draw | -0.0553 |
| Raw edge prob away | -0.0225 |
| Raw ev away | -0.0820 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **44.3%**. Expected goals are 1.19 for Hull City and 1.05 for Brentford (2.24 combined). The most likely exact score is 0-1 at 14.3%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.2%; Under 3.5 goals: 81.0%; Double Chance 1X: 55.7%; Double Chance X2: 71.2%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 92.0%; BTTS Yes (both teams score): 45.7%; BTTS No (at least one team does not score): 54.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.8% | 3.48 |
| Draw | 26.9% | 3.72 |
| Brentford win | 44.3% | 2.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.19 |
| Brentford expected goals | 1.05 |
| Expected total goals | 2.24 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 66.9% |
| Under 1.5 | 33.1% |
| Over 2.5 | 40.2% |
| Under 2.5 | 59.8% |
| Over 3.5 | 19.0% |
| Under 3.5 | 81.0% |
| Over 4.5 | 8.0% |
| Under 4.5 | 92.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 14.26% |
| 2 | 1-1 | 12.54% |
| 3 | 0-0 | 10.20% |
| 4 | 1-2 | 10.01% |
| 5 | 1-0 | 8.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.8% | 19.6% | 4.75 | +36.6% |
| Draw | 26.9% | 22.7% | 4.11 | +10.5% |
| Brentford win | 44.3% | 57.7% | 1.72 | -23.7% |
| Over 2.5 | 40.2% | 56.3% | 1.73 | -30.4% |
| Under 2.5 | 59.8% | 43.7% | 2.28 | +36.3% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
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
| Dc lambda home | 1.1913 |
| Dc lambda away | 1.0535 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 45.7% |
| P btts no | 54.3% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.81 |
| Fair Over 1.5 odds | 1.50 |
| Fair Under 1.5 odds | 3.02 |
| Fair Over 2.5 odds | 2.49 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.27 |
| Fair Under 3.5 odds | 1.23 |
| Fair Over 4.5 odds | 12.46 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2659353951206566, "-10": 7.873076055001543e-08, "-11": 7.468932135863653e-09, "-12": 6.47984752395604e-10, "-13": 4.7889351852931995e-11, "-2": 0.12518098809961822, "-3": 0.04001334492321192, "-4": 0.00993935775018057, "-5": 0.002012462597573811, "-6": 0.00034332347816830923, "-7": 5.055723897504921e-05, "-8": 6.545339769844366e-06, "-9": 7.557613740036543e-07, "0": 0.2689235249896802, "1": 0.16083663459135292, "10": 1.4286195073096098e-07, "11": 1.5325097167170467e-08, "12": 1.5034261654082707e-09, "13": 1.2564027293489177e-10, "2": 0.08498254841715862, "3": 0.030716294806728342, "4": 0.008627697033116373, "5": 0.001975317791706793, "6": 0.00038105288650401456, "7": 6.345088657137467e-05, "8": 9.288789827252154e-06, "9": 1.2127861448027268e-06} |
| Raw goal margin distribution | {"-1": 0.1860824594526392, "-10": 5.5090122738557254e-08, "-11": 5.226221431320882e-09, "-12": 4.5341311696728506e-10, "-13": 3.350952350793036e-11, "-2": 0.08759265058237128, "-3": 0.02799846041877897, "-4": 0.006954847566244811, "-5": 0.0014081765593597496, "-6": 0.00024023307306049937, "-7": 3.5376319001626704e-05, "-8": 4.579957932163218e-06, "-9": 5.28827443861316e-07, "0": 0.31066237877019526, "1": 0.21196691729016648, "10": 1.8827804605238557e-07, "11": 2.019697571980925e-08, "12": 1.9813683024682003e-09, "13": 1.655815629888587e-10, "2": 0.11199866782350526, "3": 0.040481065382278275, "4": 0.011370458901168246, "5": 0.0026032752055545616, "6": 0.0005021903491203623, "7": 8.36220482978534e-05, "8": 1.2241714395737254e-05, "9": 1.5983332472680355e-06} |
| Unadjusted home-win probability | 37.9% |
| Unadjusted draw probability | 31.1% |
| Unadjusted away-win probability | 31.0% |
| Raw p over 1 5 | 66.8% |
| Raw p under 3 5 | 81.0% |
| Raw p btts yes | 46.5% |
| P home draw | 55.7% |
| P draw away | 71.2% |
| P home away | 73.1% |
| Raw p home draw | 69.0% |
| Raw p draw away | 62.1% |
| Raw p home away | 68.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 4.40 |
| Reference draw odds | 3.85 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.17 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +9.1% |
| Draw probability edge | +4.2% |
| Away probability edge | -13.3% |
| Over 2.5 probability edge | -16.1% |
| Under 2.5 probability edge | +16.1% |
| Raw edge prob home | 0.1829 |
| Raw ev home | 0.8003 |
| Raw edge prob draw | 0.0835 |
| Raw ev draw | 0.2768 |
| Raw edge prob away | -0.2663 |
| Raw ev away | -0.4663 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.2%**. Expected goals are 1.64 for Liverpool and 1.47 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 11.2%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.5%; Under 3.5 goals: 62.1%; Double Chance 1X: 67.8%; Double Chance X2: 56.8%; Double Chance 12 (either team wins): 75.4%; Under 4.5 goals: 79.4%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.2% | 2.31 |
| Draw | 24.6% | 4.06 |
| Brighton and Hove Albion win | 32.2% | 3.11 |

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
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 37.9% |
| Under 3.5 | 62.1% |
| Over 4.5 | 20.6% |
| Under 4.5 | 79.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.25% |
| 2 | 2-1 | 9.34% |
| 3 | 1-2 | 7.57% |
| 4 | 1-0 | 6.72% |
| 5 | 2-0 | 6.34% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.2% | 45.7% | 2.16 | -6.7% |
| Draw | 24.6% | 23.6% | 4.00 | -1.5% |
| Brighton and Hove Albion win | 32.2% | 30.7% | 3.12 | +0.4% |
| Over 2.5 | 60.5% | 61.3% | 1.64 | -0.8% |
| Under 2.5 | 39.5% | 38.7% | 2.47 | -2.5% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda away | 1.4737 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.23 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.79 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.64 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.86 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16673393018518126, "-10": 7.045353624966039e-07, "-11": 9.271545290211197e-08, "-12": 1.1214287112829824e-08, "-13": 1.2540440188346436e-09, "-14": 1.291790863774294e-10, "-15": 1.0931799532518641e-11, "-2": 0.09667500415509335, "-3": 0.040214688687301346, "-4": 0.01332169216233216, "-5": 0.0036481202365245802, "-6": 0.0008491619049299352, "-7": 0.00017160415747762654, "-8": 3.0610625644102836e-05, "-9": 4.883933364892956e-06, "0": 0.2462947134947862, "1": 0.20666053723644334, "10": 2.2495400533953325e-06, "11": 3.2905660576927233e-07, "12": 4.424026462394762e-08, "13": 5.499033709506458e-09, "14": 6.296415293266809e-10, "15": 5.922708673670763e-11, "2": 0.1324599809117371, "3": 0.0612467087065662, "4": 0.022551996411730345, "5": 0.006864711644812021, "6": 0.0017761155391810542, "7": 0.0003989661706182071, "8": 7.910574568113223e-05, "9": 1.4029206511549947e-05} |
| Raw goal margin distribution | {"-1": 0.1743309100833558, "-10": 7.366364530214612e-07, "-11": 9.693989258973405e-08, "-12": 1.172524918080186e-08, "-13": 1.3111826419807046e-09, "-14": 1.3506493649434276e-10, "-15": 1.142989048021705e-11, "-2": 0.10107985481990095, "-3": 0.04204701028632718, "-4": 0.013928674960941325, "-5": 0.003814341329449216, "-6": 0.0008878526855939759, "-7": 0.000179423041932355, "-8": 3.2005352604779145e-05, "-9": 5.106462417953163e-06, "0": 0.25633822743342327, "1": 0.19484648997600798, "10": 2.1209418562724427e-06, "11": 3.1024561096638516e-07, "12": 4.171120617829236e-08, "13": 5.184673527346921e-09, "14": 5.936471644417801e-10, "15": 5.584128501973631e-11, "2": 0.12488771532327976, "3": 0.057745452390864094, "4": 0.02126277905563433, "5": 0.006472280516520304, "6": 0.0016745813362777134, "7": 0.0003761586948512893, "8": 7.458355179474146e-05, "9": 1.3227206715312943e-05} |
| Unadjusted home-win probability | 40.7% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.7% |
| Raw p under 3 5 | 62.2% |
| Raw p btts yes | 63.1% |
| P home draw | 67.8% |
| P draw away | 56.8% |
| P home away | 75.4% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.3% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 2.05 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.95 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -2.5% |
| Draw probability edge | +1.0% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -0.8% |
| Under 2.5 probability edge | +0.8% |
| Raw edge prob home | -0.0494 |
| Raw ev home | -0.1201 |
| Raw edge prob draw | 0.0201 |
| Raw ev draw | 0.0254 |
| Raw edge prob away | 0.0293 |
| Raw ev away | 0.0493 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **50.2%**. Expected goals are 1.76 for Manchester United and 1.27 for Bournemouth (3.04 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 94.4%; Over 2.5 goals: 58.8%; Under 3.5 goals: 63.8%; Double Chance 1X: 74.6%; Double Chance X2: 49.8%; Double Chance 12 (either team wins): 75.6%; Under 4.5 goals: 80.7%; BTTS Yes (both teams score): 60.3%; BTTS No (at least one team does not score): 39.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 50.2% | 1.99 |
| Draw | 24.4% | 4.10 |
| Bournemouth win | 25.4% | 3.94 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.76 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.04 |
| Over 0.5 | 94.4% |
| Under 0.5 | 5.6% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.8% |
| Under 2.5 | 41.2% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.3% |
| Under 4.5 | 80.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.33% |
| 2 | 2-1 | 9.93% |
| 3 | 1-0 | 7.85% |
| 4 | 2-0 | 7.81% |
| 5 | 1-2 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 50.2% | 52.3% | 1.91 | -4.1% |
| Draw | 24.4% | 23.5% | 3.87 | -5.5% |
| Bournemouth win | 25.4% | 24.1% | 3.97 | +0.8% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7643 |
| Dc lambda away | 1.2710 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.3% |
| P btts no | 39.7% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.96 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.43 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.19 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.14373926046812366, "-10": 1.6981557530921897e-07, "-11": 1.9297476161725443e-08, "-12": 2.015230685541488e-09, "-13": 1.9464428093150453e-10, "-14": 1.7478406374225916e-11, "-15": 1.4556469479135106e-12, "-16": 1.014155131299173e-13, "-2": 0.07362718719838697, "-3": 0.026679248099637388, "-4": 0.007673756461831713, "-5": 0.0018211298148517888, "-6": 0.00036690570281938217, "-7": 6.412520483260758e-05, "-8": 9.886943864059817e-06, "-9": 1.3629155253293088e-06, "0": 0.24405912825740564, "1": 0.22274793107215815, "10": 4.949830137624674e-06, "11": 7.808410079608492e-07, "12": 1.131973326062237e-07, "13": 1.5177575396201318e-08, "14": 1.8919598210798547e-09, "15": 2.187335775794677e-10, "16": 2.1155004400985375e-11, "2": 0.1556167641104151, "3": 0.07827824536666608, "4": 0.03125538364938111, "5": 0.010296913205213044, "6": 0.0028798504464165797, "7": 0.0006987045377161249, "8": 0.00014954647899086856, "9": 2.8617545900436384e-05} |
| Raw goal margin distribution | {"-1": 0.15091152693289794, "-10": 1.7828899135449463e-07, "-11": 2.02603769076926e-08, "-12": 2.115786173427128e-09, "-13": 2.0435659365760706e-10, "-14": 1.83505396208232e-11, "-15": 1.5282804633154237e-12, "-16": 1.0647591960105597e-13, "-2": 0.0773010185783373, "-3": 0.028010482696415186, "-4": 0.008056659685006748, "-5": 0.0019120001049626708, "-6": 0.0003852134738451658, "-7": 6.732490862035377e-05, "-8": 1.0380280170955784e-05, "-9": 1.4309219508862802e-06, "0": 0.2528423038185946, "1": 0.21322649400243648, "10": 4.7382479427447675e-06, "11": 7.474636900078988e-07, "12": 1.0835867361764094e-07, "13": 1.4528804705895455e-08, "14": 1.8110873465830292e-09, "15": 2.0938373543308514e-10, "16": 2.0250726448125663e-11, "2": 0.14896487190500088, "3": 0.07493221479480186, "4": 0.029919361505089302, "5": 0.00985676810207374, "6": 0.002756750246725466, "7": 0.0006688381714869456, "8": 0.00014315406321463068, "9": 2.7394279039687822e-05} |
| Unadjusted home-win probability | 48.1% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.7% |
| Raw p over 1 5 | 81.6% |
| Raw p under 3 5 | 63.9% |
| Raw p btts yes | 60.6% |
| P home draw | 74.6% |
| P draw away | 49.8% |
| P home away | 75.6% |
| Raw p home draw | 73.3% |
| Raw p draw away | 51.9% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.88 |
| Reference draw odds | 4.10 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Home probability edge | -2.1% |
| Draw probability edge | +0.9% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -2.5% |
| Under 2.5 probability edge | +2.5% |
| Raw edge prob home | -0.0429 |
| Raw ev home | -0.0822 |
| Raw edge prob draw | 0.0176 |
| Raw ev draw | -0.0215 |
| Raw edge prob away | 0.0253 |
| Raw ev away | 0.0586 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.9%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.28 combined). The most likely exact score is 1-1 at 14.2%. Goal-market probabilities: at least one goal: 88.8%; Over 2.5 goals: 40.0%; Under 3.5 goals: 80.3%; Double Chance 1X: 61.1%; Double Chance X2: 69.2%; Double Chance 12 (either team wins): 69.7%; Under 4.5 goals: 91.8%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 30.8% | 3.25 |
| Draw | 30.3% | 3.30 |
| Leeds United win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.28 |
| Over 0.5 | 88.8% |
| Under 0.5 | 11.2% |
| Over 1.5 | 67.7% |
| Under 1.5 | 32.3% |
| Over 2.5 | 40.0% |
| Under 2.5 | 60.0% |
| Over 3.5 | 19.7% |
| Under 3.5 | 80.3% |
| Over 4.5 | 8.2% |
| Under 4.5 | 91.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 14.22% |
| 2 | 0-1 | 11.43% |
| 3 | 0-0 | 11.25% |
| 4 | 1-0 | 9.65% |
| 5 | 1-2 | 8.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 30.8% | 30.4% | 3.18 | -2.2% |
| Draw | 30.3% | 29.9% | 3.18 | -3.5% |
| Leeds United win | 38.9% | 39.7% | 2.47 | -3.9% |
| Over 2.5 | 40.0% | 44.3% | 2.19 | -12.4% |
| Under 2.5 | 60.0% | 55.7% | 1.79 | +7.4% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0686 |
| Dc lambda away | 1.2112 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.89 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.09 |
| Fair Over 2.5 odds | 2.50 |
| Fair Under 2.5 odds | 1.67 |
| Fair Over 3.5 odds | 5.08 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.22 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2157836382624741, "-10": 2.1960185205918098e-07, "-11": 2.394678614256347e-08, "-12": 2.396952521955146e-09, "-13": 2.209493685070689e-10, "-14": 1.74974071034269e-11, "-2": 0.11537905251730537, "-3": 0.0422874834884616, "-4": 0.012055650322548243, "-5": 0.00280292624070164, "-6": 0.0005492580099284669, "-7": 9.292545395589376e-05, "-8": 1.3823665126002492e-05, "-9": 1.8342523229508885e-06, "0": 0.30345317317438875, "1": 0.18339450093394583, "10": 6.089385794975058e-08, "11": 5.858358904816617e-09, "12": 5.17344001988722e-10, "13": 4.20730502303056e-11, "14": 2.939518367869936e-12, "2": 0.08716346341210716, "3": 0.028184517155022397, "4": 0.007088929350898924, "5": 0.0014540954735287896, "6": 0.0002513905220145842, "7": 3.752307658481046e-05, "8": 4.924682095898714e-06, "9": 5.76507977665163e-07} |
| Raw goal margin distribution | {"-1": 0.21157928735553616, "-10": 2.1532310667651575e-07, "-11": 2.3480204464511172e-08, "-12": 2.35025004909522e-09, "-13": 2.1664436797343202e-10, "-14": 1.715648579902813e-11, "-2": 0.1131309950278737, "-3": 0.04146354975099919, "-4": 0.011820756774661729, "-5": 0.0027483137335761474, "-6": 0.0005385562095937413, "-7": 9.111488472199356e-05, "-8": 1.3554323393340536e-05, "-9": 1.798513559439213e-06, "0": 0.30787860166470743, "1": 0.18527462075523232, "10": 6.151812829996772e-08, "11": 5.918417503308198e-09, "12": 5.226476981606863e-10, "13": 4.25043738265811e-11, "14": 2.9696536593880747e-12, "2": 0.08805704394161339, "3": 0.028473458585036335, "4": 0.007161603485163861, "5": 0.0014690025383966132, "6": 0.00025396772199013534, "7": 3.790775485860539e-05, "8": 4.97516884645493e-06, "9": 5.824182098172626e-07} |
| Unadjusted home-win probability | 31.1% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.6% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 47.3% |
| P home draw | 61.1% |
| P draw away | 69.2% |
| P home away | 69.7% |
| Raw p home draw | 61.9% |
| Raw p draw away | 68.9% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Everygame |
| Reference home odds | 3.00 |
| Reference draw odds | 3.05 |
| Reference away odds | 2.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:39Z |
| Market reference home last update utc | 2026-10-21T17:11:39Z |
| Market reference draw last update utc | 2026-10-21T17:11:39Z |
| Market reference away last update utc | 2026-10-21T17:11:39Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 2.14 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.8% |
| Over 2.5 probability edge | -4.3% |
| Under 2.5 probability edge | +4.3% |
| Raw edge prob home | 0.0063 |
| Raw ev home | -0.0119 |
| Raw edge prob draw | 0.0089 |
| Raw ev draw | -0.0209 |
| Raw edge prob away | -0.0152 |
| Raw ev away | -0.0580 |

</details>


---

## 2026-10-31 — Bournemouth vs Leeds United

The model's most likely 1X2 outcome is **Bournemouth win** at **43.3%**. Expected goals are 1.44 for Bournemouth and 1.22 for Leeds United (2.65 combined). The most likely exact score is 1-1 at 13.1%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 49.7%; Under 3.5 goals: 72.4%; Double Chance 1X: 70.7%; Double Chance X2: 56.7%; Double Chance 12 (either team wins): 72.6%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 54.5%; BTTS No (at least one team does not score): 45.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bournemouth win | 43.3% | 2.31 |
| Draw | 27.4% | 3.65 |
| Leeds United win | 29.3% | 3.41 |

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
| Over 2.5 | 49.7% |
| Under 2.5 | 50.3% |
| Over 3.5 | 27.6% |
| Under 3.5 | 72.4% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.06% |
| 2 | 1-0 | 9.53% |
| 3 | 2-1 | 9.33% |
| 4 | 0-0 | 7.94% |
| 5 | 2-0 | 7.67% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bournemouth win | 43.3% | 45.6% | 2.15 | -6.9% |
| Draw | 27.4% | 26.6% | 3.37 | -7.8% |
| Leeds United win | 29.3% | 27.8% | 3.48 | +2.1% |
| Over 2.5 | 49.7% | 52.6% | 1.88 | -6.5% |
| Under 2.5 | 50.3% | 47.4% | 1.95 | -2.0% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda away | 1.2157 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 54.5% |
| P btts no | 45.5% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.60 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.07 |
| Fair Over 2.5 odds | 2.01 |
| Fair Under 2.5 odds | 1.99 |
| Fair Over 3.5 odds | 3.62 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.63 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.16628255194950775, "-10": 1.5259756175106877e-07, "-11": 1.664660626799643e-08, "-12": 1.66745184717799e-09, "-13": 1.534786797084613e-10, "-14": 1.1849960917443459e-11, "-2": 0.08549872590302277, "-3": 0.030543243502132594, "-4": 0.008574102576947889, "-5": 0.001974265379106198, "-6": 0.00038450550678503987, "-7": 6.48035799135218e-05, "-8": 9.618728240428469e-06, "-9": 1.2749085352131224e-06, "0": 0.27362546307691643, "1": 0.21997293149559421, "10": 8.929601461708753e-07, "11": 1.1503333107553724e-07, "12": 1.3607075555645611e-08, "13": 1.4790166268329548e-09, "14": 1.3485138968449108e-10, "2": 0.13229275838683588, "3": 0.05580910913766365, "4": 0.01850086853355553, "5": 0.005030631183239057, "6": 0.0011569990954748092, "7": 0.00023027296875783768, "8": 4.036222725751458e-05, "9": 6.317569144554685e-06} |
| Raw goal margin distribution | {"-1": 0.17487772736796364, "-10": 1.6048535753181532e-07, "-11": 1.7507072380152584e-08, "-12": 1.7536427370837164e-09, "-13": 1.6141202063702613e-10, "-14": 1.2462487557148877e-11, "-2": 0.08991817062873347, "-3": 0.03212202932585005, "-4": 0.009017299501945047, "-5": 0.002076315516399947, "-6": 0.0004043806665142655, "-7": 6.81532887709477e-05, "-8": 1.0115922056374015e-05, "-9": 1.340808789774833e-06, "0": 0.28104725961768706, "1": 0.20850076202466006, "10": 8.463899156520009e-07, "11": 1.0903403898113212e-07, "12": 1.2897430620167275e-08, "13": 1.4018820026862706e-09, "14": 1.2781853348107933e-10, "2": 0.1253933415646278, "3": 0.052898516667508035, "4": 0.01753599936654771, "5": 0.004768270477821809, "6": 0.00109665853624891, "7": 0.0002182636251344931, "8": 3.825723048280079e-05, "9": 5.988091224803784e-06} |
| Unadjusted home-win probability | 41.0% |
| Unadjusted draw probability | 28.1% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 75.3% |
| Raw p under 3 5 | 72.5% |
| Raw p btts yes | 54.7% |
| P home draw | 70.7% |
| P draw away | 56.7% |
| P home away | 72.6% |
| Raw p home draw | 69.2% |
| Raw p draw away | 59.0% |
| Raw p home away | 71.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.14 |
| Reference draw odds | 3.60 |
| Reference away odds | 3.45 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.79 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market best under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -2.3% |
| Draw probability edge | +0.7% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -2.9% |
| Under 2.5 probability edge | +2.9% |
| Raw edge prob home | -0.0452 |
| Raw ev home | -0.1175 |
| Raw edge prob draw | 0.0148 |
| Raw ev draw | -0.0529 |
| Raw edge prob away | 0.0303 |
| Raw ev away | 0.0736 |

</details>


---

## 2026-10-31 — Brentford vs Nottingham Forest

The model's most likely 1X2 outcome is **Brentford win** at **48.4%**. Expected goals are 1.60 for Brentford and 1.08 for Nottingham Forest (2.68 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 92.4%; Over 2.5 goals: 50.5%; Under 3.5 goals: 71.8%; Double Chance 1X: 74.3%; Double Chance X2: 51.6%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 53.6%; BTTS No (at least one team does not score): 46.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Brentford win | 48.4% | 2.07 |
| Draw | 26.0% | 3.85 |
| Nottingham Forest win | 25.7% | 3.89 |

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
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 28.2% |
| Under 3.5 | 71.8% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.40% |
| 2 | 1-0 | 9.92% |
| 3 | 2-1 | 9.49% |
| 4 | 2-0 | 8.77% |
| 5 | 0-0 | 7.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Brentford win | 48.4% | 48.4% | 2.01 | -2.8% |
| Draw | 26.0% | 24.9% | 3.81 | -1.0% |
| Nottingham Forest win | 25.7% | 26.7% | 3.42 | -12.2% |
| Over 2.5 | 50.5% | 56.4% | 1.78 | -10.1% |
| Under 2.5 | 49.5% | 43.6% | 2.21 | +9.4% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda away | 1.0815 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.6% |
| P btts no | 46.4% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.15 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.55 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.39 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.15518803254246397, "-10": 5.037453353036537e-08, "-11": 4.8896361435603535e-09, "-12": 4.3591129769875887e-10, "-13": 3.5919661515595326e-11, "-14": 2.737268292567633e-12, "-15": 1.7697673230069497e-13, "-2": 0.07166002985237231, "-3": 0.022799683783047753, "-4": 0.005698221892612592, "-5": 0.0011678896223351596, "-6": 0.00020243599491452682, "-7": 3.0362374955871275e-05, "-8": 4.010330556218591e-06, "-9": 4.729865647152531e-07, "0": 0.2597390384304085, "1": 0.22566614060213022, "10": 2.400671480309673e-06, "11": 3.442565447622636e-07, "12": 4.5340651351340135e-08, "13": 5.519577459986887e-09, "14": 6.214052682510081e-10, "15": 5.935505384381018e-11, "2": 0.15049668823324028, "3": 0.07073962434071039, "4": 0.026119042353665956, "5": 0.00790867372977169, "6": 0.0020252263224675915, "7": 0.00044875110741819717, "8": 8.756568161349123e-05, "9": 1.525761082170697e-05} |
| Raw goal margin distribution | {"-1": 0.14910647704031724, "-10": 4.840044109204645e-08, "-11": 4.698019605189536e-09, "-12": 4.188286740741413e-10, "-13": 3.451203096866096e-11, "-14": 2.6299993957797225e-12, "-15": 1.7004131464997676e-13, "-2": 0.06885179495376022, "-3": 0.021906202887089752, "-4": 0.005474918251631199, "-5": 0.0011221220109913597, "-6": 0.00019450287198916137, "-7": 2.9172525033515986e-05, "-8": 3.853172510845958e-06, "-9": 4.5445102432621934e-07, "0": 0.2705168434415616, "1": 0.22533189000762763, "10": 2.3971156705308654e-06, "11": 3.4374664126304495e-07, "12": 4.527349400275039e-08, "13": 5.5114020108810486e-09, "14": 6.204848595455385e-10, "15": 5.92671387406357e-11, "2": 0.1502737766020208, "3": 0.07063484671909788, "4": 0.026080355533342554, "5": 0.007896959615776345, "6": 0.0020222266119196077, "7": 0.00044808642939411265, "8": 8.743598169014768e-05, "9": 1.5235011660511426e-05} |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 75.8% |
| Raw p under 3 5 | 71.9% |
| Raw p btts yes | 53.8% |
| P home draw | 74.3% |
| P draw away | 51.6% |
| P home away | 74.0% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.71, "price": 1.55, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.02 |
| Reference draw odds | 3.85 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | -0.1% |
| Draw probability edge | +1.1% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0014 |
| Raw ev home | -0.0296 |
| Raw edge prob draw | 0.0216 |
| Raw ev draw | 0.0307 |
| Raw edge prob away | -0.0201 |
| Raw ev away | -0.1563 |

</details>


---

## 2026-10-31 — Chelsea vs Manchester United

The model's most likely 1X2 outcome is **Chelsea win** at **48.0%**. Expected goals are 1.83 for Chelsea and 1.49 for Manchester United (3.33 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.6%; Over 2.5 goals: 64.8%; Under 3.5 goals: 57.3%; Double Chance 1X: 71.9%; Double Chance X2: 52.0%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 75.6%; BTTS Yes (both teams score): 65.8%; BTTS No (at least one team does not score): 34.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 48.0% | 2.08 |
| Draw | 23.8% | 4.20 |
| Manchester United win | 28.1% | 3.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.83 |
| Manchester United expected goals | 1.49 |
| Expected total goals | 3.33 |
| Over 0.5 | 95.6% |
| Under 0.5 | 4.4% |
| Over 1.5 | 85.4% |
| Under 1.5 | 14.6% |
| Over 2.5 | 64.8% |
| Under 2.5 | 35.2% |
| Over 3.5 | 42.7% |
| Under 3.5 | 57.3% |
| Over 4.5 | 24.4% |
| Under 4.5 | 75.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.47% |
| 2 | 2-1 | 9.65% |
| 3 | 1-2 | 6.72% |
| 4 | 2-2 | 6.58% |
| 5 | 2-0 | 6.45% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 48.0% | 51.2% | 1.88 | -9.7% |
| Draw | 23.8% | 23.3% | 3.92 | -6.7% |
| Manchester United win | 28.1% | 25.5% | 3.78 | +6.4% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Man United |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8316 |
| Dc lambda away | 1.4947 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 65.8% |
| P btts no | 34.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 22.89 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 6.86 |
| Fair Over 2.5 odds | 1.54 |
| Fair Under 2.5 odds | 2.84 |
| Fair Over 3.5 odds | 2.34 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.10 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.14700009306925224, "-10": 6.447319485032975e-07, "-11": 8.585901803771046e-08, "-12": 1.0512907950466066e-08, "-13": 1.1910431350600652e-09, "-14": 1.2545873694777067e-10, "-15": 1.2219885771282392e-11, "-16": 9.747949292808363e-13, "-2": 0.08399104364977872, "-3": 0.03479781230674921, "-4": 0.011547692767670543, "-5": 0.003179035982997993, "-6": 0.0007455590096975532, "-7": 0.00015203399903435165, "-8": 2.7394719682461617e-05, "-9": 4.4185560443499344e-06, "0": 0.23807411888698676, "1": 0.21309404490724043, "10": 5.764420825729047e-06, "11": 9.406668217282947e-07, "12": 1.4113872599231335e-07, "13": 1.959405141629777e-08, "14": 2.529129609295822e-09, "15": 3.018635973426866e-10, "16": 2.95073549148229e-11, "2": 0.14771414634308294, "3": 0.07499192028301031, "4": 0.030495178230760357, "5": 0.010287380913382499, "6": 0.00295641108503906, "7": 0.0007387490583530102, "8": 0.00016311597786624796, "9": 3.2239138874271194e-05} |
| Raw goal margin distribution | {"-1": 0.1607680356522459, "-10": 7.051171650230802e-07, "-11": 9.390052335851676e-08, "-12": 1.1497540749127807e-08, "-13": 1.302595537204807e-09, "-14": 1.372091287384621e-10, "-15": 1.3364393112447797e-11, "-16": 1.066093651181708e-12, "-2": 0.09185759558394038, "-3": 0.03805695501781818, "-4": 0.01262924290598535, "-5": 0.003476782630427444, "-6": 0.0008153876296897441, "-7": 0.00016627341430044783, "-8": 2.996049307614003e-05, "-9": 4.832395414435843e-06, "0": 0.24353635316149896, "1": 0.1989807857525197, "10": 5.382642137235913e-06, "11": 8.78366279077852e-07, "12": 1.317910813053691e-07, "13": 1.8296333661446815e-08, "14": 2.361624873875331e-09, "15": 2.81871113833689e-10, "16": 2.7553077182357424e-11, "2": 0.1379310103147357, "3": 0.07002519112863628, "4": 0.02847547677205716, "5": 0.009606045717379743, "6": 0.0027606074161509496, "7": 0.0006898215676041228, "8": 0.00015231277560452284, "9": 3.0103934570201216e-05} |
| Unadjusted home-win probability | 44.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 30.8% |
| Raw p over 1 5 | 85.3% |
| Raw p under 3 5 | 57.5% |
| Raw p btts yes | 66.0% |
| P home draw | 71.9% |
| P draw away | 52.0% |
| P home away | 76.2% |
| Raw p home draw | 69.2% |
| Raw p draw away | 55.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.89, "price": 1.5, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.91 |
| Reference draw odds | 4.10 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -3.2% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.6% |
| Over 2.5 probability edge | +3.0% |
| Under 2.5 probability edge | -3.0% |
| Raw edge prob home | -0.0636 |
| Raw ev home | -0.1565 |
| Raw edge prob draw | 0.0109 |
| Raw ev draw | -0.0453 |
| Raw edge prob away | 0.0527 |
| Raw ev away | 0.1635 |

</details>


---

## 2026-10-31 — Coventry City vs Sunderland

The model's most likely 1X2 outcome is **Sunderland win** at **38.2%**. Expected goals are 1.15 for Coventry City and 1.24 for Sunderland (2.39 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 90.2%; Over 2.5 goals: 43.4%; Under 3.5 goals: 77.9%; Double Chance 1X: 61.8%; Double Chance X2: 66.8%; Double Chance 12 (either team wins): 71.4%; Under 4.5 goals: 90.3%; BTTS Yes (both teams score): 49.5%; BTTS No (at least one team does not score): 50.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Coventry City win | 33.2% | 3.01 |
| Draw | 28.6% | 3.50 |
| Sunderland win | 38.2% | 2.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Coventry City expected goals | 1.15 |
| Sunderland expected goals | 1.24 |
| Expected total goals | 2.39 |
| Over 0.5 | 90.2% |
| Under 0.5 | 9.8% |
| Over 1.5 | 70.3% |
| Under 1.5 | 29.7% |
| Over 2.5 | 43.4% |
| Under 2.5 | 56.6% |
| Over 3.5 | 22.1% |
| Under 3.5 | 77.9% |
| Over 4.5 | 9.7% |
| Under 4.5 | 90.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.54% |
| 2 | 0-1 | 10.45% |
| 3 | 0-0 | 9.80% |
| 4 | 1-0 | 9.46% |
| 5 | 1-2 | 8.33% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Coventry City win | 33.2% | 33.6% | 2.74 | -9.0% |
| Draw | 28.6% | 27.1% | 3.43 | -2.0% |
| Sunderland win | 38.2% | 39.2% | 2.54 | -2.9% |
| Over 2.5 | 43.4% | 51.0% | 1.92 | -16.7% |
| Under 2.5 | 56.6% | 49.0% | 1.92 | +8.7% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda away | 1.2432 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 49.5% |
| P btts no | 50.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.21 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.37 |
| Fair Over 2.5 odds | 2.30 |
| Fair Under 2.5 odds | 1.77 |
| Fair Over 3.5 odds | 4.53 |
| Fair Under 3.5 odds | 1.28 |
| Fair Over 4.5 odds | 10.36 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.21028211516998238, "-10": 2.59131858619289e-07, "-11": 2.8974952732882427e-08, "-12": 2.974231264982573e-09, "-13": 2.809871738098289e-10, "-14": 2.2637644966792165e-11, "-2": 0.11374250684392467, "-3": 0.04240191693493736, "-4": 0.01233482281469938, "-5": 0.002931571484495932, "-6": 0.0005878770527566049, "-7": 0.00010185339819156973, "-8": 1.552412037361506e-05, "-9": 2.1112391935394194e-06, "0": 0.2855728474585435, "1": 0.1912519617475335, "10": 1.1837023497791049e-07, "11": 1.2254422118977526e-08, "12": 1.1646441101106895e-09, "13": 1.0187166314454925e-10, "14": 7.598826785879902e-12, "2": 0.0962182145788727, "3": 0.03320996281235098, "4": 0.00894466776291644, "5": 0.001968249670434238, "6": 0.00036543875880846473, "7": 5.862083797630649e-05, "8": 8.27240714249768e-06, "9": 1.0416234273957032e-06} |
| Raw goal margin distribution | {"-1": 0.20478088850887813, "-10": 2.523526653996203e-07, "-11": 2.8216934000050494e-08, "-12": 2.89642188819375e-09, "-13": 2.7363621992227916e-10, "-14": 2.204541763478506e-11, "-2": 0.11076686951668538, "-3": 0.04129263307722152, "-4": 0.012012129388901522, "-5": 0.002854878137577648, "-6": 0.0005724974998475912, "-7": 9.918879388509983e-05, "-8": 1.5117991184642009e-05, "-9": 2.056006701084801e-06, "0": 0.2999443701546074, "1": 0.18873623486109084, "10": 1.1681319378488176e-07, "11": 1.2093227541307124e-08, "12": 1.1493243901236586e-09, "13": 1.0053164404305798e-10, "14": 7.498871874693714e-12, "2": 0.09495256089788658, "3": 0.0327731192078128, "4": 0.008827009669499494, "5": 0.0019423593288665018, "6": 0.0003606317800853063, "7": 5.784973990831663e-05, "8": 8.163591960296026e-06, "9": 1.0279219205567453e-06} |
| Unadjusted home-win probability | 32.8% |
| Unadjusted draw probability | 30.0% |
| Unadjusted away-win probability | 37.2% |
| Raw p over 1 5 | 70.2% |
| Raw p under 3 5 | 78.0% |
| Raw p btts yes | 49.8% |
| P home draw | 61.8% |
| P draw away | 66.8% |
| P home away | 71.4% |
| Raw p home draw | 62.8% |
| Raw p draw away | 67.2% |
| Raw p home away | 70.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.12, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.88 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.48 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.92 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market best under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -0.4% |
| Draw probability edge | +1.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0087 |
| Raw ev home | -0.1022 |
| Raw edge prob draw | 0.0287 |
| Raw ev draw | 0.0288 |
| Raw edge prob away | -0.0200 |
| Raw ev away | -0.0541 |

</details>


---

## 2026-10-31 — Hull City vs Ipswich Town

The model's most likely 1X2 outcome is **Hull City win** at **48.6%**. Expected goals are 1.86 for Hull City and 0.87 for Ipswich Town (2.73 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 92.1%; Over 2.5 goals: 50.1%; Under 3.5 goals: 72.0%; Double Chance 1X: 74.2%; Double Chance X2: 51.4%; Double Chance 12 (either team wins): 74.4%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.2%; BTTS No (at least one team does not score): 48.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 48.6% | 2.06 |
| Draw | 25.6% | 3.90 |
| Ipswich Town win | 25.8% | 3.88 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.86 |
| Ipswich Town expected goals | 0.87 |
| Expected total goals | 2.73 |
| Over 0.5 | 92.1% |
| Under 0.5 | 7.9% |
| Over 1.5 | 75.5% |
| Under 1.5 | 24.5% |
| Over 2.5 | 50.1% |
| Under 2.5 | 49.9% |
| Over 3.5 | 28.0% |
| Under 3.5 | 72.0% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.23% |
| 2 | 2-0 | 9.17% |
| 3 | 1-0 | 9.08% |
| 4 | 2-1 | 7.98% |
| 5 | 0-0 | 7.93% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 48.6% | 37.5% | 2.63 | +27.9% |
| Draw | 25.6% | 27.2% | 3.41 | -12.6% |
| Ipswich Town win | 25.8% | 35.4% | 2.66 | -31.5% |
| Over 2.5 | 50.1% | 54.2% | 1.81 | -9.3% |
| Under 2.5 | 49.9% | 45.8% | 2.17 | +8.2% |

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
| Market best home last update utc | 2026-10-21T17:11:33Z |
| Market best draw last update utc | 2026-10-21T17:11:33Z |
| Market best away last update utc | 2026-10-21T17:11:33Z |
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
| Dc lambda home | 1.8624 |
| Dc lambda away | 0.8709 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.2% |
| P btts no | 48.8% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.62 |
| Fair Over 1.5 odds | 1.33 |
| Fair Under 1.5 odds | 4.08 |
| Fair Over 2.5 odds | 1.99 |
| Fair Under 2.5 odds | 2.01 |
| Fair Over 3.5 odds | 3.57 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1712018653933729, "-10": 8.301266497373002e-09, "-11": 6.493226296528108e-10, "-12": 4.6642869408951854e-11, "-13": 3.097240137588203e-12, "-14": 1.9116967403906631e-13, "-15": 1.0977093278025813e-14, "-16": 5.424924752114727e-16, "-2": 0.06537821404767978, "-3": 0.016862844184214725, "-4": 0.0034086500071512896, "-5": 0.0005643020128125996, "-6": 7.89421800534629e-05, "-7": 9.55069929998621e-06, "-8": 1.0171769446615825e-06, "-9": 9.670889871088632e-08, "0": 0.2562407429608987, "1": 0.19538243456173546, "10": 8.465380048717124e-06, "11": 1.4160075241891686e-06, "12": 2.1751699775463517e-07, "13": 3.088771187867299e-08, "14": 4.076925512446826e-09, "15": 5.006152210038626e-10, "16": 5.290702386609856e-11, "2": 0.15244451761765304, "3": 0.08408383340272546, "4": 0.03634686897117304, "5": 0.012867646217428351, "6": 0.0038494576534227887, "7": 0.0009959293261708809, "8": 0.00022682596922908596, "9": 4.611748587291502e-05} |
| Raw goal margin distribution | {"-1": 0.10735136644284476, "-10": 5.205272148475639e-09, "-11": 4.071548601139758e-10, "-12": 2.9247203319666446e-11, "-13": 1.9421106201602677e-12, "-14": 1.198720918336524e-13, "-15": 6.8831374019143845e-15, "-16": 3.401674880416753e-16, "-2": 0.04099511764947678, "-3": 0.010573771267788426, "-4": 0.002137378790542477, "-5": 0.0003538430613631925, "-6": 4.950034206253671e-05, "-7": 5.988723417133564e-06, "-8": 6.378162683723052e-07, "-9": 6.064088378909795e-08, "0": 0.24054891211225485, "1": 0.2402767118720337, "10": 1.0410524812097006e-05, "11": 1.7413726707900564e-06, "12": 2.674972758630777e-07, "13": 3.7984979888830703e-08, "14": 5.013706881456663e-09, "15": 6.156447967582903e-10, "16": 6.506381066443631e-11, "2": 0.18747267387803107, "3": 0.10340431603752509, "4": 0.04469852258124884, "5": 0.015824327962703184, "6": 0.0047339722709965944, "7": 0.0012247704062345365, "8": 0.0002789452295228262, "9": 5.6714196904162896e-05} |
| Unadjusted home-win probability | 59.8% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 50.1% |
| P home draw | 74.2% |
| P draw away | 51.4% |
| P home away | 74.4% |
| Raw p home draw | 83.9% |
| Raw p draw away | 40.2% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:33Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.92, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.75 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.75 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:38Z |
| Market best over 2 5 last update utc | 2026-10-21T17:10:44Z |
| Market best under 2 5 last update utc | 2026-10-21T17:10:44Z |
| Home probability edge | +11.2% |
| Draw probability edge | -1.6% |
| Away probability edge | -9.6% |
| Over 2.5 probability edge | -4.1% |
| Under 2.5 probability edge | +4.1% |
| Raw edge prob home | 0.2235 |
| Raw ev home | 0.5727 |
| Raw edge prob draw | -0.0314 |
| Raw ev draw | -0.1797 |
| Raw edge prob away | -0.1921 |
| Raw ev away | -0.5705 |

</details>


---

## 2026-10-31 — Manchester City vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Manchester City win** at **56.5%**. Expected goals are 1.97 for Manchester City and 1.14 for Brighton and Hove Albion (3.11 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 94.8%; Over 2.5 goals: 60.3%; Under 3.5 goals: 62.2%; Double Chance 1X: 79.3%; Double Chance X2: 43.5%; Double Chance 12 (either team wins): 77.2%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 59.2%; BTTS No (at least one team does not score): 40.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester City win | 56.5% | 1.77 |
| Draw | 22.8% | 4.39 |
| Brighton and Hove Albion win | 20.7% | 4.84 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester City expected goals | 1.97 |
| Brighton and Hove Albion expected goals | 1.14 |
| Expected total goals | 3.11 |
| Over 0.5 | 94.8% |
| Under 0.5 | 5.2% |
| Over 1.5 | 82.6% |
| Under 1.5 | 17.4% |
| Over 2.5 | 60.3% |
| Under 2.5 | 39.7% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.58% |
| 2 | 2-1 | 10.01% |
| 3 | 2-0 | 8.78% |
| 4 | 1-0 | 8.02% |
| 5 | 3-1 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester City win | 56.5% | 57.4% | 1.67 | -5.6% |
| Draw | 22.8% | 22.1% | 4.41 | +0.5% |
| Brighton and Hove Albion win | 20.7% | 20.6% | 4.40 | -9.0% |

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
| Market best home last update utc | 2026-10-21T17:11:34Z |
| Market best draw last update utc | 2026-10-21T17:11:34Z |
| Market best away last update utc | 2026-10-21T17:11:34Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man City |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9682 |
| Dc lambda away | 1.1398 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-22T10:54:22.405766+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 59.2% |
| P btts no | 40.8% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.24 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.75 |
| Fair Over 2.5 odds | 1.66 |
| Fair Under 2.5 odds | 2.52 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.89 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.12439080665932149, "-10": 5.554220638564432e-08, "-11": 5.660431880591268e-09, "-12": 5.301243192117429e-10, "-13": 4.5919681348566024e-11, "-14": 3.697970143231327e-12, "-15": 2.761974058162234e-13, "-16": 1.725643736800533e-14, "-2": 0.05755921148170271, "-3": 0.01870388083056521, "-4": 0.004824539215964118, "-5": 0.0010267938597890418, "-6": 0.00018552157089974378, "-7": 2.9078255857449002e-05, "-8": 4.020709718636886e-06, "-9": 4.97063283160943e-07, "0": 0.22794079294916453, "1": 0.22559230875089428, "10": 1.3344553623378955e-05, "11": 2.348315652284568e-06, "12": 3.7976121960894324e-07, "13": 5.680122900421185e-08, "14": 7.898565947426184e-09, "15": 1.0186627479537015e-09, "16": 1.0989753468466954e-10, "2": 0.1749797974240897, "3": 0.09818175290762049, "4": 0.043730140926399444, "5": 0.01607068098747311, "6": 0.005013850860139097, "7": 0.0013569733959671833, "8": 0.0003239900557235307, "9": 6.91618539028271e-05} |
| Raw goal margin distribution | {"-1": 0.12497308077081998, "-10": 5.580219978662322e-08, "-11": 5.686928396149656e-09, "-12": 5.326058343272301e-10, "-13": 4.6134631652174545e-11, "-14": 3.7152803636352764e-12, "-15": 2.7749028752821585e-13, "-16": 1.733721485475002e-14, "-2": 0.057828646495625025, "-3": 0.018791433808833274, "-4": 0.004847122912949531, "-5": 0.0010316002880007198, "-6": 0.00018638999848503401, "-7": 2.921437134739589e-05, "-8": 4.039530684927623e-06, "-9": 4.99390039368528e-07, "0": 0.23523402865761403, "1": 0.22229585741366947, "10": 1.3149557296243396e-05, "11": 2.3140010592248037e-06, "12": 3.742119861836655e-07, "13": 5.597122514307089e-08, "14": 7.783148722327865e-09, "15": 1.0037776120363192e-09, "16": 1.0829166488718003e-10, "2": 0.17242291775740345, "3": 0.09674707912616286, "4": 0.04309113739683744, "5": 0.01583584932089459, "6": 0.004940586326148261, "7": 0.0013371447201116868, "8": 0.00031925577440715516, "9": 6.815123130205984e-05} |
| Unadjusted home-win probability | 55.7% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 20.8% |
| Raw p over 1 5 | 82.5% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 59.4% |
| P home draw | 79.3% |
| P draw away | 43.5% |
| P home away | 77.2% |
| Raw p home draw | 79.2% |
| Raw p draw away | 44.3% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:10:44Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:11:34Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Unibet (SE) |
| Reference home odds | 1.71 |
| Reference draw odds | 4.30 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:11:38Z |
| Market reference home last update utc | 2026-10-21T17:11:38Z |
| Market reference draw last update utc | 2026-10-21T17:11:38Z |
| Market reference away last update utc | 2026-10-21T17:11:38Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:11:33Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:11:33Z |
| Home probability edge | -0.8% |
| Draw probability edge | +0.7% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -5.9% |
| Under 2.5 probability edge | +5.9% |
| Raw edge prob home | -0.0165 |
| Raw ev home | -0.0697 |
| Raw edge prob draw | 0.0146 |
| Raw ev draw | 0.0374 |
| Raw edge prob away | 0.0019 |
| Raw ev away | -0.0862 |

</details>


---
