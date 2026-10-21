# La Liga — football model report

Fixtures in this report: **14**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | La Liga |
| Training matches | 1,988 |
| Training data through | 2026-10-19 |
| Model fit succeeded | Yes |
| Recency half-life (days) | 1,000,000,000 |
| Maximum goals per team in score matrix | 10 |
| Bookmaker margin-removal method | power |
| Market blending weight | 50.0% |

<details>
<summary>Technical model diagnostics</summary>

| Parameter | Value |
| --- | --- |
| Training seasons requested | 6 |
| Training seasons loaded | ['2122', '2223', '2324', '2425', '2526', '2627'] |
| Training sha256 | d11389a7c232e44c18b16e5562a6aae7ce2af3a671931c9f3e570e9dafad7855 |
| Training as of utc | 2026-10-21T17:14:04.838687+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 88, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 88, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 574, 'added_results': 0, 'conflicts': 0, 'unmapped': 566, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 25, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:14:04.838687+00:00', 'observations': 161, 'observations_sha256': '6057b1a3c93e96afb5d880edb061d4fb875e687c5ae648edd977a0f408d8a940', 'eligible_training_matches': 72, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 98, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 9, 'retrospective_eligible_training_matches': 72, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.155286+00:00', 'retrospective_inputs_sha256': 'c670dc81d795c47ef92f5119dca4d2297704a73c73b72c2e3948b1366e612df4', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5521.524 |
| Base scoring parameter | 0.090 |
| Home-advantage parameter | 0.278 |
| Dixon-Coles low-score adjustment | -0.020 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-19', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 14.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/LaLiga/20261021T171404838687Z_1c9996898b6a83b97fb1e562a7d4f6a9b6145710f5da651655e01e2e3acb7443.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-21 — Levante vs Athletic Bilbao

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **44.1%**. Expected goals are 1.24 for Levante and 1.54 for Athletic Bilbao (2.78 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 93.1%; Over 2.5 goals: 52.0%; Under 3.5 goals: 69.7%; Double Chance 1X: 55.9%; Double Chance X2: 71.4%; Double Chance 12 (either team wins): 72.7%; Under 4.5 goals: 85.3%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 28.6% | 3.50 |
| Draw | 27.3% | 3.66 |
| Athletic Bilbao win | 44.1% | 2.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.24 |
| Athletic Bilbao expected goals | 1.54 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.1% |
| Under 0.5 | 6.9% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.0% |
| Under 2.5 | 48.0% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.7% |
| Under 4.5 | 85.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.91% |
| 2 | 0-1 | 9.34% |
| 3 | 1-2 | 9.14% |
| 4 | 0-2 | 7.37% |
| 5 | 1-0 | 7.00% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 28.6% | 26.7% | 3.49 | -0.2% |
| Draw | 27.3% | 29.0% | 3.24 | -11.6% |
| Athletic Bilbao win | 44.1% | 44.2% | 2.31 | +1.9% |
| Over 2.5 | 52.0% | 46.1% | 2.12 | +10.3% |
| Under 2.5 | 48.0% | 53.9% | 1.84 | -11.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-21T18:00:00+00:00 |
| Fixture id | a362cccad837f1ffae61ff43a3536688 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Levante |
| Matched away-team name | Ath Bilbao |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2405 |
| Dc lambda away | 1.5396 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.53 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.92 |
| Fair Under 2.5 odds | 2.08 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.80 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.2189780515347374, "-10": 1.5232893696844454e-06, "-11": 2.101978358031707e-07, "-12": 2.6644943729325076e-08, "-13": 3.122132628537519e-09, "-14": 3.380108155027429e-10, "-15": 3.0774739909635284e-11, "-2": 0.13335171690697012, "-3": 0.05971612223382354, "-4": 0.02108661252675742, "-5": 0.006119750309823916, "-6": 0.001504115327772187, "-7": 0.00032017303083411666, "-8": 6.005615072779278e-05, "-9": 1.006353274057486e-05, "0": 0.27286992661674475, "1": 0.1648716446128887, "10": 1.6457321440255718e-07, "11": 1.8297577631616567e-08, "12": 1.8688256378461384e-09, "13": 1.7643873761807173e-10, "14": 1.5390821753466e-11, "15": 1.129052718253305e-12, "2": 0.08110850742332834, "3": 0.029264965335174184, "4": 0.00832629610184005, "5": 0.0019470062888708895, "6": 0.0003855701515247599, "7": 6.612956015446909e-05, "8": 9.994406228231928e-06, "9": 1.349393414876569e-06} |
| Raw goal margin distribution | {"-1": 0.21846598800212172, "-10": 1.5197272732534574e-06, "-11": 2.0970630413780432e-07, "-12": 2.6582636553255333e-08, "-13": 3.1148317586473228e-09, "-14": 3.3722040289729876e-10, "-15": 3.070277551903535e-11, "-2": 0.1330398840508406, "-3": 0.05957648062001408, "-4": 0.021037303085808094, "-5": 0.0061054397387853504, "-6": 0.0015005980683811095, "-7": 0.0003194243305325653, "-8": 5.991571398319009e-05, "-9": 1.003999993402363e-05, "0": 0.25535262965186223, "1": 0.17556528827764376, "10": 1.7524750175934563e-07, "11": 1.948436615174154e-08, "12": 1.9900384485123266e-09, "13": 1.878826277616858e-10, "14": 1.6389076874446696e-11, "15": 1.2022835486733716e-12, "2": 0.08636923905854496, "3": 0.03116310319805869, "4": 0.008866343141277152, "5": 0.0020732899291845915, "6": 0.00041057839243757645, "7": 7.041875101963738e-05, "8": 1.064264758651074e-05, "9": 1.4369156348200758e-06} |
| Unadjusted home-win probability | 30.5% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 44.0% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.6% |
| Raw p btts yes | 56.1% |
| P home draw | 55.9% |
| P draw away | 71.4% |
| P home away | 72.7% |
| Raw p home draw | 56.0% |
| Raw p draw away | 69.5% |
| Raw p home away | 74.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.51, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.2, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.7, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.77, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.94, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.55 |
| Reference draw odds | 3.28 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +1.9% |
| Draw probability edge | -1.8% |
| Away probability edge | -0.1% |
| Over 2.5 probability edge | +5.9% |
| Under 2.5 probability edge | -5.9% |
| Raw edge prob home | 0.0371 |
| Raw ev home | 0.0628 |
| Raw edge prob draw | -0.0350 |
| Raw ev draw | -0.1727 |
| Raw edge prob away | -0.0021 |
| Raw ev away | 0.0167 |
| Market p over 1 5 | 72.3% |
| Market over 1 5 odds | 1.35 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-21T17:15:48Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.00 |
| Market reference over 1 5 last update utc | 2026-10-21T17:15:49Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 76.2% |
| Market reference under 3 5 odds | 1.26 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-10-21T17:15:49Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 51.8% |
| Market btts yes odds | 1.85 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-21T17:15:33Z |
| Market reference btts yes odds | 1.80 |
| Market reference btts yes opposite odds | 1.92 |
| Market reference btts yes last update utc | 2026-10-21T17:15:49Z |
| Market btts yes bookmakers | 2 |

</details>


---

## 2026-10-23 — Alavés vs Málaga

The model's most likely 1X2 outcome is **Alavés win** at **58.3%**. Expected goals are 1.63 for Alavés and 0.60 for Málaga (2.23 combined). The most likely exact score is 1-0 at 16.2%. Goal-market probabilities: at least one goal: 88.7%; Over 2.5 goals: 38.0%; Under 3.5 goals: 81.8%; Double Chance 1X: 83.6%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 74.6%; Under 4.5 goals: 92.6%; BTTS Yes (both teams score): 37.0%; BTTS No (at least one team does not score): 63.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alavés win | 58.3% | 1.72 |
| Draw | 25.4% | 3.94 |
| Málaga win | 16.4% | 6.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alavés expected goals | 1.63 |
| Málaga expected goals | 0.60 |
| Expected total goals | 2.23 |
| Over 0.5 | 88.7% |
| Under 0.5 | 11.3% |
| Over 1.5 | 64.8% |
| Under 1.5 | 35.2% |
| Over 2.5 | 38.0% |
| Under 2.5 | 62.0% |
| Over 3.5 | 18.2% |
| Under 3.5 | 81.8% |
| Over 4.5 | 7.4% |
| Under 4.5 | 92.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 16.19% |
| 2 | 2-0 | 13.34% |
| 3 | 0-0 | 11.27% |
| 4 | 1-1 | 11.09% |
| 5 | 2-1 | 8.06% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alavés win | 58.3% | 54.5% | 1.76 | +2.6% |
| Draw | 25.4% | 26.1% | 3.76 | -4.7% |
| Málaga win | 16.4% | 19.4% | 4.97 | -18.6% |
| Over 2.5 | 38.0% | 46.1% | 2.12 | -19.5% |
| Under 2.5 | 62.0% | 53.9% | 1.84 | +14.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T19:00:00+00:00 |
| Fixture id | 903eb4941471ffe20d525b02dd3b77aa |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alaves |
| Matched away-team name | Malaga |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6278 |
| Dc lambda away | 0.6043 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 37.0% |
| P btts no | 63.0% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.87 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.84 |
| Fair Over 2.5 odds | 2.63 |
| Fair Under 2.5 odds | 1.61 |
| Fair Over 3.5 odds | 5.48 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.53 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.12347485394636415, "-10": 2.5832356401373234e-10, "-11": 1.4086510597593267e-11, "-12": 7.049250378010008e-13, "-13": 3.259018785977183e-14, "-14": 1.3975151775045008e-15, "-15": 5.283449438794748e-17, "-2": 0.0330624212345262, "-3": 0.006176381986054312, "-4": 0.0008906203311147403, "-5": 0.00010429375350303243, "-6": 1.0267363569647255e-05, "-7": 8.712346498660801e-07, "-8": 6.49308754643515e-08, "-9": 4.312862789342517e-09, "0": 0.25354011387288544, "1": 0.25692381502297157, "10": 3.9619676793594356e-06, "11": 5.81979044704085e-07, "12": 7.845197364273986e-08, "13": 9.770230682182005e-09, "14": 1.1285778013732803e-09, "15": 1.1493427023507259e-10, "2": 0.18290493661212828, "3": 0.09204112888435403, "4": 0.03575175870269178, "5": 0.011277689150911445, "6": 0.00299073393978084, "7": 0.0006836140726875804, "8": 0.00013724108094249993, "9": 2.4555881536939292e-05} |
| Raw goal margin distribution | {"-1": 0.10030894936847098, "-10": 2.0985783319567526e-10, "-11": 1.1443650534109586e-11, "-12": 5.726695571234587e-13, "-13": 2.6475734932675918e-14, "-14": 1.1353184450241385e-15, "-15": 4.29218780430511e-17, "-2": 0.02685936959321105, "-3": 0.005017591583372765, "-4": 0.0007235253725355795, "-5": 8.472653747076192e-05, "-6": 8.341038029514974e-06, "-7": 7.077767625417594e-07, "-8": 5.2748779943755656e-08, "-9": 3.5036991042503682e-09, "0": 0.24604287354959523, "1": 0.273771845255209, "10": 4.221777581508937e-06, "11": 6.201428892617657e-07, "12": 8.359653847645677e-08, "13": 1.0410923106489255e-08, "14": 1.2025853935276662e-09, "15": 1.224711973177858e-10, "2": 0.1948991065624346, "3": 0.09807681585215884, "4": 0.03809621521570419, "5": 0.012017234637371478, "6": 0.003186854240382404, "7": 0.0007284427335215069, "8": 0.0001462407989352342, "9": 2.616615746436393e-05} |
| Unadjusted home-win probability | 62.1% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 13.3% |
| Raw p over 1 5 | 65.5% |
| Raw p under 3 5 | 81.3% |
| Raw p btts yes | 36.7% |
| P home draw | 83.6% |
| P draw away | 41.7% |
| P home away | 74.6% |
| Raw p home draw | 86.7% |
| Raw p draw away | 37.9% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.55, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.36, "price": 3.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.79 |
| Reference draw odds | 3.62 |
| Reference away odds | 4.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.06 |
| Reference Under 2.5 odds | 1.78 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +3.8% |
| Draw probability edge | -0.7% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -8.1% |
| Under 2.5 probability edge | +8.1% |
| Raw edge prob home | 0.0764 |
| Raw ev home | 0.0929 |
| Raw edge prob draw | -0.0150 |
| Raw ev draw | -0.0749 |
| Raw edge prob away | -0.0614 |
| Raw ev away | -0.3390 |

</details>


---

## 2026-10-24 — Atlético Madrid vs Deportivo La Coruña

The model's most likely 1X2 outcome is **Atlético Madrid win** at **72.5%**. Expected goals are 2.28 for Atlético Madrid and 0.89 for Deportivo La Coruña (3.17 combined). The most likely exact score is 2-0 at 11.6%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 62.4%; Under 3.5 goals: 60.3%; Double Chance 1X: 88.9%; Double Chance X2: 27.5%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 78.0%; BTTS Yes (both teams score): 52.3%; BTTS No (at least one team does not score): 47.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atlético Madrid win | 72.5% | 1.38 |
| Draw | 16.5% | 6.06 |
| Deportivo La Coruña win | 11.1% | 9.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atlético Madrid expected goals | 2.28 |
| Deportivo La Coruña expected goals | 0.89 |
| Expected total goals | 3.17 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 62.4% |
| Under 2.5 | 37.6% |
| Over 3.5 | 39.7% |
| Under 3.5 | 60.3% |
| Over 4.5 | 22.0% |
| Under 4.5 | 78.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.55% |
| 2 | 2-1 | 10.27% |
| 3 | 1-0 | 9.95% |
| 4 | 3-0 | 8.78% |
| 5 | 3-1 | 7.81% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atlético Madrid win | 72.5% | 76.4% | 1.29 | -6.5% |
| Draw | 16.5% | 14.5% | 5.86 | -3.3% |
| Deportivo La Coruña win | 11.1% | 9.1% | 10.25 | +13.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T19:00:00+00:00 |
| Fixture id | 70df1835c3b5ddff1c99e0189532136b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Ath Madrid |
| Matched away-team name | La Coruna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 90/100 |
| Dc lambda home | 2.2803 |
| Dc lambda away | 0.8891 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 52.3% |
| P btts no | 47.7% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.64 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.92 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.66 |
| Fair Over 3.5 odds | 2.52 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.55 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.07558306760673437, "-10": 3.657387860175825e-09, "-11": 2.9121383553335494e-10, "-12": 2.1303638490120417e-11, "-13": 1.4411684998262123e-12, "-14": 9.066059944923123e-14, "-15": 5.3292737085694465e-15, "-16": 2.939155526382887e-16, "-17": 1.5190316800728362e-17, "-18": 6.743879858202508e-19, "-2": 0.026490098243761737, "-3": 0.006801821948520156, "-4": 0.0013804839459085135, "-5": 0.00023059835414508648, "-6": 3.264987609298226e-05, "-7": 4.006036072034044e-06, "-8": 4.333033414963671e-07, "-9": 4.188083182595934e-08, "0": 0.1649373428404899, "1": 0.2434382927886796, "10": 5.588934565213994e-05, "11": 1.1412907861466485e-05, "12": 2.141235284387013e-06, "13": 3.7149388491738836e-07, "14": 5.993517743833894e-08, "15": 9.035611215843066e-09, "16": 1.2780221422069767e-09, "17": 1.693982591177928e-10, "18": 1.928760205480254e-11, "2": 0.2162873743965252, "3": 0.1424292408880111, "4": 0.07413641167872019, "5": 0.03176016172786637, "6": 0.011532788836412618, "7": 0.003629058417118411, "8": 0.001006693912768559, "9": 0.00024954392637752793} |
| Raw goal margin distribution | {"-1": 0.08874807655047576, "-10": 4.294429269244749e-09, "-11": 3.4193726964012644e-10, "-12": 2.5014292213728735e-11, "-13": 1.6921902801060052e-12, "-14": 1.0645180296063435e-13, "-15": 6.257523093762584e-15, "-16": 3.4510957005129724e-16, "-17": 1.7836156178145162e-17, "-18": 7.918524411010296e-19, "-2": 0.03110412611193784, "-3": 0.007986558816464186, "-4": 0.001620935730548142, "-5": 0.00027076382361938464, "-6": 3.8336810010677077e-05, "-7": 4.70380479705705e-06, "-8": 5.087758321848032e-07, "-9": 4.917560753457265e-08, "0": 0.18489320242051685, "1": 0.2302652121041178, "10": 5.286502745121457e-05, "11": 1.0795325662781434e-05, "12": 2.025367460788916e-06, "13": 3.513913822922728e-07, "14": 5.669192873167744e-08, "15": 8.546670736442171e-09, "16": 1.2088650321932152e-09, "17": 1.6023167768304672e-10, "18": 1.824389962340162e-11, "2": 0.20458350069063, "3": 0.1347220233399183, "4": 0.07012469716363598, "5": 0.03004153657566365, "6": 0.0109087195656346, "7": 0.0034326806049424616, "8": 0.0009522190806226191, "9": 0.00023604045394163184} |
| Unadjusted home-win probability | 68.5% |
| Unadjusted draw probability | 18.5% |
| Unadjusted away-win probability | 13.0% |
| Raw p over 1 5 | 82.6% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 53.0% |
| P home draw | 88.9% |
| P draw away | 27.5% |
| P home away | 83.5% |
| Raw p home draw | 87.0% |
| Raw p draw away | 31.5% |
| Raw p home away | 81.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.78, "price": 2.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.75, "market_key": "spreads", "opposite_price": 2.01, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.21, "price": 1.78, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.29 |
| Reference draw odds | 6.20 |
| Reference away odds | 9.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | -3.9% |
| Draw probability edge | +2.0% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0784 |
| Raw ev home | -0.1159 |
| Raw edge prob draw | 0.0399 |
| Raw ev draw | 0.0835 |
| Raw edge prob away | 0.0385 |
| Raw ev away | 0.3302 |

</details>


---

## 2026-10-24 — Rayo Vallecano vs Elche CF

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **51.8%**. Expected goals are 1.40 for Rayo Vallecano and 0.90 for Elche CF (2.30 combined). The most likely exact score is 1-0 at 14.8%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 40.9%; Under 3.5 goals: 79.8%; Double Chance 1X: 78.0%; Double Chance X2: 48.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 44.4%; BTTS No (at least one team does not score): 55.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 51.8% | 1.93 |
| Draw | 26.2% | 3.82 |
| Elche CF win | 22.0% | 4.55 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.40 |
| Elche CF expected goals | 0.90 |
| Expected total goals | 2.30 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.3% |
| Under 1.5 | 32.7% |
| Over 2.5 | 40.9% |
| Under 2.5 | 59.1% |
| Over 3.5 | 20.2% |
| Under 3.5 | 79.8% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.84% |
| 2 | 1-1 | 12.14% |
| 3 | 2-0 | 10.55% |
| 4 | 0-0 | 9.72% |
| 5 | 2-1 | 9.48% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 51.8% | 55.4% | 1.78 | -7.7% |
| Draw | 26.2% | 24.5% | 3.92 | +2.5% |
| Elche CF win | 22.0% | 20.1% | 4.55 | +0.1% |
| Over 2.5 | 40.9% | 52.7% | 1.85 | -24.3% |
| Under 2.5 | 59.1% | 47.3% | 2.04 | +20.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T12:00:00+00:00 |
| Fixture id | 734ad601156f5f4e6bc42317e5141516 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Vallecano |
| Matched away-team name | Elche |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3967 |
| Dc lambda away | 0.8984 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 44.4% |
| P btts no | 55.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.29 |
| Fair Over 1.5 odds | 1.48 |
| Fair Under 1.5 odds | 3.06 |
| Fair Over 2.5 odds | 2.44 |
| Fair Under 2.5 odds | 1.69 |
| Fair Over 3.5 odds | 4.95 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.75 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.14527614194092023, "-10": 9.793868723017405e-09, "-11": 7.923905034195092e-10, "-12": 5.884511449347271e-11, "-13": 4.025069556237208e-12, "-14": 2.37041005044828e-13, "-2": 0.055695341647739996, "-3": 0.01518121184589672, "-4": 0.0032157181931243956, "-5": 0.0005552184446353507, "-6": 8.077090787790315e-05, "-7": 1.0142605720844071e-05, "-8": 1.119728351582136e-06, "-9": 1.1025014583843611e-07, "0": 0.26153874889498097, "1": 0.2651991274510397, "10": 9.433978536142316e-07, "11": 1.1866631574167751e-07, "12": 1.3700808644257367e-08, "13": 1.4569906668019128e-09, "14": 1.3339957670247987e-10, "2": 0.15717329042615408, "3": 0.0666060846680482, "4": 0.021934767665985372, "5": 0.005887982800869738, "6": 0.0013316963321304593, "7": 0.00025998445053302375, "8": 4.462293141105881e-05, "9": 6.830809699634534e-06} |
| Raw goal margin distribution | {"-1": 0.1579793191339475, "-10": 1.0650260200183232e-08, "-11": 8.616783908628829e-10, "-12": 6.399062501135632e-11, "-13": 4.3770280478657525e-12, "-14": 2.5776824799654586e-13, "-2": 0.06056543101220805, "-3": 0.01650868118468007, "-4": 0.003496905712729046, "-5": 0.0006037676295793459, "-6": 8.783364468455613e-05, "-7": 1.1029491316438226e-05, "-8": 1.2176391817306175e-06, "-9": 1.198905941559052e-07, "0": 0.27785999932304006, "1": 0.2470093204845488, "10": 8.786909105153606e-07, "11": 1.1052708316760252e-07, "12": 1.2761080573055923e-08, "13": 1.3570567822683054e-09, "14": 1.2424980093605063e-10, "2": 0.146392893670634, "3": 0.062037623849378214, "4": 0.020430278591930025, "5": 0.005484130527299902, "6": 0.0012403562909611724, "7": 0.00024215231430038117, "8": 4.1562278397424837e-05, "9": 6.362289644325815e-06} |
| Unadjusted home-win probability | 48.3% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 23.9% |
| Raw p over 1 5 | 67.1% |
| Raw p under 3 5 | 80.0% |
| Raw p btts yes | 44.9% |
| P home draw | 78.0% |
| P draw away | 48.2% |
| P home away | 73.8% |
| Raw p home draw | 76.1% |
| Raw p draw away | 51.7% |
| Raw p home away | 72.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.13, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.44, "price": 3.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.76 |
| Reference draw odds | 3.84 |
| Reference away odds | 4.65 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.82 |
| Reference Under 2.5 odds | 2.01 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:48Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:48Z |
| Home probability edge | -3.6% |
| Draw probability edge | +1.6% |
| Away probability edge | +1.9% |
| Over 2.5 probability edge | -11.7% |
| Under 2.5 probability edge | +11.7% |
| Raw edge prob home | -0.0711 |
| Raw ev home | -0.1405 |
| Raw edge prob draw | 0.0326 |
| Raw ev draw | 0.0892 |
| Raw edge prob away | 0.0385 |
| Raw ev away | 0.0886 |

</details>


---

## 2026-10-24 — Real Racing Club de Santander vs Espanyol

The model's most likely 1X2 outcome is **Espanyol win** at **38.8%**. Expected goals are 1.90 for Real Racing Club de Santander and 2.13 for Espanyol (4.03 combined). The most likely exact score is 1-1 at 8.2%. Goal-market probabilities: at least one goal: 97.9%; Over 2.5 goals: 76.0%; Under 3.5 goals: 42.8%; Double Chance 1X: 61.2%; Double Chance X2: 62.2%; Double Chance 12 (either team wins): 76.7%; Under 4.5 goals: 62.8%; BTTS Yes (both teams score): 75.7%; BTTS No (at least one team does not score): 24.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 2.64 |
| Draw | 23.3% | 4.28 |
| Espanyol win | 38.8% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Racing Club de Santander expected goals | 1.90 |
| Espanyol expected goals | 2.13 |
| Expected total goals | 4.03 |
| Over 0.5 | 97.9% |
| Under 0.5 | 2.1% |
| Over 1.5 | 91.2% |
| Under 1.5 | 8.8% |
| Over 2.5 | 76.0% |
| Under 2.5 | 24.0% |
| Over 3.5 | 57.2% |
| Under 3.5 | 42.8% |
| Over 4.5 | 37.2% |
| Under 4.5 | 62.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 8.22% |
| 2 | 2-2 | 8.18% |
| 3 | 2-1 | 7.33% |
| 4 | 1-2 | 6.76% |
| 5 | 3-2 | 4.95% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Racing Club de Santander win | 37.8% | 40.4% | 2.43 | -8.1% |
| Draw | 23.3% | 25.9% | 3.68 | -14.1% |
| Espanyol win | 38.8% | 33.7% | 2.85 | +10.7% |
| Over 2.5 | 76.0% | 57.3% | 1.73 | +31.4% |
| Under 2.5 | 24.0% | 42.7% | 2.28 | -45.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T14:15:00+00:00 |
| Fixture id | 5960b1b6c20acfd78e78764fed47d505 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Santander |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9044 |
| Dc lambda away | 2.1305 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 75.7% |
| P btts no | 24.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 46.56 |
| Fair Over 1.5 odds | 1.10 |
| Fair Under 1.5 odds | 11.35 |
| Fair Over 2.5 odds | 1.32 |
| Fair Under 2.5 odds | 4.16 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.34 |
| Fair Over 4.5 odds | 2.69 |
| Fair Under 4.5 odds | 1.59 |
| Goal margin distribution | {"-1": 0.16433045324530482, "-10": 1.193785137194157e-05, "-11": 2.244896935870158e-06, "-12": 3.886773372435913e-07, "-13": 6.23352514919501e-08, "-14": 9.308269347607981e-09, "-15": 1.2981756437298074e-09, "-16": 1.6678030822938795e-10, "-17": 1.6874442534620214e-11, "-2": 0.11562348128918842, "-3": 0.0638308593199917, "-4": 0.02880050980544535, "-5": 0.01091791850899066, "-6": 0.0035554601793899923, "-7": 0.0010125458895785125, "-8": 0.0002558425052343019, "-9": 5.8038678263697616e-05, "0": 0.23338767746827108, "1": 0.17804475402245012, "10": 4.715867894443226e-06, "11": 7.926866999787247e-07, "12": 1.2267726476096427e-07, "13": 1.758645409038732e-08, "14": 2.3473789705382944e-09, "15": 2.9262904210829873e-10, "16": 3.3604577716615055e-11, "17": 3.039154689390965e-12, "2": 0.11207890908177248, "3": 0.05530676367392737, "4": 0.022305780874160852, "5": 0.0075583466417832555, "6": 0.0022001509454553578, "7": 0.0005600684062929982, "8": 0.00012649366033011091, "9": 2.5649758207534268e-05} |
| Raw goal margin distribution | {"-1": 0.18594714885223115, "-10": 1.3508204853062768e-05, "-11": 2.5401998013663518e-06, "-12": 4.398055336465025e-07, "-13": 7.053508378396737e-08, "-14": 1.0532716923457853e-08, "-15": 1.468942943281661e-09, "-16": 1.8871926771635712e-10, "-17": 1.9094175278026844e-11, "-2": 0.13083306387526297, "-3": 0.07222742994338721, "-4": 0.03258904590142545, "-5": 0.012354105876634405, "-6": 0.00402315985965371, "-7": 0.0011457402905602336, "-8": 0.0002894970680359253, "-9": 6.567332185335453e-05, "0": 0.20775697716749247, "1": 0.16605891696794822, "10": 4.398399264358083e-06, "11": 7.393236358807071e-07, "12": 1.1441872485738759e-07, "13": 1.640254741337688e-08, "14": 2.1893552084762638e-09, "15": 2.7292947816785943e-10, "16": 3.1342343173350135e-11, "17": 2.8345611135203037e-12, "2": 0.10453384239965575, "3": 0.0515835545232441, "4": 0.02080417271727348, "5": 0.007049524510250908, "6": 0.0020520384617580788, "7": 0.0005223650283189636, "8": 0.00011797820358740314, "9": 2.392303604685711e-05} |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 20.8% |
| Unadjusted away-win probability | 43.9% |
| Raw p over 1 5 | 91.2% |
| Raw p under 3 5 | 42.7% |
| Raw p btts yes | 75.1% |
| P home draw | 61.2% |
| P draw away | 62.2% |
| P home away | 76.7% |
| Raw p home draw | 56.1% |
| Raw p draw away | 64.7% |
| Raw p home away | 79.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.14, "price": 1.82, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.39 |
| Reference draw odds | 3.66 |
| Reference away odds | 2.84 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.68 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -2.5% |
| Draw probability edge | -2.6% |
| Away probability edge | +5.1% |
| Over 2.5 probability edge | +18.7% |
| Under 2.5 probability edge | -18.7% |
| Raw edge prob home | -0.0509 |
| Raw ev home | -0.1428 |
| Raw edge prob draw | -0.0513 |
| Raw ev draw | -0.2355 |
| Raw edge prob away | 0.1022 |
| Raw ev away | 0.2526 |

</details>


---

## 2026-10-24 — Valencia vs Villarreal

The model's most likely 1X2 outcome is **Villarreal win** at **43.3%**. Expected goals are 1.27 for Valencia and 1.51 for Villarreal (2.78 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 52.4%; Under 3.5 goals: 69.7%; Double Chance 1X: 56.7%; Double Chance X2: 69.4%; Double Chance 12 (either team wins): 74.0%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Valencia win | 30.6% | 3.26 |
| Draw | 26.0% | 3.84 |
| Villarreal win | 43.3% | 2.31 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Valencia expected goals | 1.27 |
| Villarreal expected goals | 1.51 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 76.8% |
| Under 1.5 | 23.2% |
| Over 2.5 | 52.4% |
| Under 2.5 | 47.6% |
| Over 3.5 | 30.3% |
| Under 3.5 | 69.7% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.31% |
| 2 | 0-1 | 9.31% |
| 3 | 1-2 | 9.15% |
| 4 | 1-0 | 7.38% |
| 5 | 2-1 | 7.29% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Valencia win | 30.6% | 29.4% | 3.21 | -1.6% |
| Draw | 26.0% | 26.4% | 3.74 | -2.7% |
| Villarreal win | 43.3% | 44.2% | 2.20 | -4.7% |
| Over 2.5 | 52.4% | 55.3% | 1.79 | -6.1% |
| Under 2.5 | 47.6% | 44.7% | 2.19 | +4.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 0dae715cc56fe201f9e667917c126691 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Valencia |
| Matched away-team name | Villarreal |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2726 |
| Dc lambda away | 1.5056 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.29 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.31 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.30 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.73 |
| Fair Under 4.5 odds | 1.17 |
| Goal margin distribution | {"-1": 0.21897691433228972, "-10": 1.244067673100583e-06, "-11": 1.678718543492271e-07, "-12": 2.080920052984981e-08, "-13": 2.3844271394619404e-09, "-14": 2.524299073441972e-10, "-15": 2.2467376489714984e-11, "-2": 0.13035941153910086, "-3": 0.05706591264449437, "-4": 0.019701044073467122, "-5": 0.005590437701882907, "-6": 0.0013435170471512246, "-7": 0.0002796469763572431, "-8": 5.129269280320592e-05, "-9": 8.404807723031339e-06, "0": 0.26017335177796885, "1": 0.1739720192439205, "10": 2.1812093607613365e-07, "11": 2.487821148178403e-08, "12": 2.6066611712280607e-09, "13": 2.5246499101586e-10, "14": 2.259153992257014e-11, "15": 1.6995944723510769e-12, "2": 0.08771873902585528, "3": 0.03245747085351315, "4": 0.009471419468149658, "5": 0.0022717448933202264, "6": 0.000461471462669318, "7": 8.11894717957764e-05, "8": 1.2587312300430867e-05, "9": 1.7433846197992998e-06} |
| Raw goal margin distribution | {"-1": 0.21450690420364077, "-10": 1.2186723243879522e-06, "-11": 1.6444505983280863e-07, "-12": 2.03844190526738e-08, "-13": 2.3357534539416184e-09, "-14": 2.4727701601753337e-10, "-15": 2.200874640635927e-11, "-2": 0.12769836440670657, "-3": 0.055901017211113645, "-4": 0.01929888356800067, "-5": 0.005476319219452027, "-6": 0.0013160916227539048, "-7": 0.00027393849872810785, "-8": 5.024564701276207e-05, "-9": 8.233239063541113e-06, "0": 0.25673600020138876, "1": 0.18094567157100436, "10": 2.268642936577937e-07, "11": 2.587545229181555e-08, "12": 2.7111489435816535e-09, "13": 2.6258502686850173e-10, "14": 2.3497119714298312e-11, "15": 1.7677225598373302e-12, "2": 0.0912349365798932, "3": 0.033758525575603285, "4": 0.00985108044295413, "5": 0.0023628075775995374, "6": 0.0004799695036388524, "7": 8.444394427579915e-05, "8": 1.3091873551700582e-05, "9": 1.8132680313024999e-06} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 42.5% |
| Raw p over 1 5 | 76.8% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 56.3% |
| P home draw | 56.7% |
| P draw away | 69.4% |
| P home away | 74.0% |
| Raw p home draw | 57.5% |
| Raw p draw away | 68.1% |
| Raw p home away | 74.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 3.24 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.19 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.12 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | -2.8% |
| Under 2.5 probability edge | +2.8% |
| Raw edge prob home | 0.0246 |
| Raw ev home | 0.0231 |
| Raw edge prob draw | -0.0069 |
| Raw ev draw | -0.0398 |
| Raw edge prob away | -0.0177 |
| Raw ev away | -0.0660 |

</details>


---

## 2026-10-25 — Athletic Bilbao vs Getafe

The model's most likely 1X2 outcome is **Athletic Bilbao win** at **56.1%**. Expected goals are 1.27 for Athletic Bilbao and 0.62 for Getafe (1.89 combined). The most likely exact score is 1-0 at 20.4%. Goal-market probabilities: at least one goal: 86.3%; Over 2.5 goals: 30.5%; Under 3.5 goals: 87.3%; Double Chance 1X: 83.0%; Double Chance X2: 43.9%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 95.5%; BTTS Yes (both teams score): 32.8%; BTTS No (at least one team does not score): 67.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Athletic Bilbao win | 56.1% | 1.78 |
| Draw | 26.9% | 3.71 |
| Getafe win | 17.0% | 5.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Athletic Bilbao expected goals | 1.27 |
| Getafe expected goals | 0.62 |
| Expected total goals | 1.89 |
| Over 0.5 | 86.3% |
| Under 0.5 | 13.7% |
| Over 1.5 | 57.2% |
| Under 1.5 | 42.8% |
| Over 2.5 | 30.5% |
| Under 2.5 | 69.5% |
| Over 3.5 | 12.7% |
| Under 3.5 | 87.3% |
| Over 4.5 | 4.5% |
| Under 4.5 | 95.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 20.43% |
| 2 | 0-0 | 13.73% |
| 3 | 2-0 | 13.10% |
| 4 | 1-1 | 10.90% |
| 5 | 0-1 | 8.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Athletic Bilbao win | 56.1% | 60.3% | 1.64 | -8.0% |
| Draw | 26.9% | 23.8% | 4.08 | +9.9% |
| Getafe win | 17.0% | 15.9% | 5.51 | -6.4% |
| Over 2.5 | 30.5% | 41.1% | 2.36 | -28.1% |
| Under 2.5 | 69.5% | 58.9% | 1.69 | +17.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T13:00:00+00:00 |
| Fixture id | 9c4254cba9944a839b421db27260504d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Ath Bilbao |
| Matched away-team name | Getafe |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2663 |
| Dc lambda away | 0.6244 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 32.8% |
| P btts no | 67.2% |
| Fair Over 0.5 odds | 1.16 |
| Fair Under 0.5 odds | 7.28 |
| Fair Over 1.5 odds | 1.75 |
| Fair Under 1.5 odds | 2.34 |
| Fair Over 2.5 odds | 3.28 |
| Fair Under 2.5 odds | 1.44 |
| Fair Over 3.5 odds | 7.89 |
| Fair Under 3.5 odds | 1.15 |
| Fair Over 4.5 odds | 22.03 |
| Fair Under 4.5 odds | 1.05 |
| Goal margin distribution | {"-1": 0.12608133718972012, "-10": 3.775116798218443e-10, "-11": 2.1300851034387973e-11, "-12": 1.1026998951911408e-12, "-13": 5.265860261291072e-14, "-14": 2.2229108061443933e-15, "-2": 0.0356411697839103, "-3": 0.006975198295738892, "-4": 0.0010483716012337759, "-5": 0.00012761183792410168, "-6": 1.3037390713248587e-05, "-7": 1.1468561999715097e-06, "-8": 8.854350228370825e-08, "-9": 6.089511150863135e-09, "0": 0.26938616989977276, "1": 0.2976625566171732, "10": 5.129461742335534e-07, "11": 5.870078198595032e-08, "12": 6.163250139945589e-09, "13": 5.969353806218667e-10, "14": 5.1107608198641214e-11, "2": 0.16914108686324686, "3": 0.06713658635403502, "4": 0.020465552523279827, "5": 0.005052481349083903, "6": 0.0010469114886431168, "7": 0.0001867814664846466, "8": 2.924738484578193e-05, "9": 4.079606761657381e-06} |
| Raw goal margin distribution | {"-1": 0.1343888691556168, "-10": 4.0238602219100984e-10, "-11": 2.2704369626538567e-11, "-12": 1.1753570769142913e-12, "-13": 5.612829157907337e-14, "-14": 2.3693789749550847e-15, "-2": 0.037989575692996165, "-3": 0.007434795918209566, "-4": 0.0011174490775955825, "-5": 0.00013602021497982766, "-6": 1.3896427764380269e-05, "-7": 1.2224228520543118e-06, "-8": 9.43776565843364e-08, "-9": 6.490750617941092e-09, "0": 0.3008617547762464, "1": 0.27501133373705955, "10": 4.7391251729628213e-07, "11": 5.423382950421512e-08, "12": 5.6942453911711324e-09, "13": 5.515103983696269e-10, "14": 4.7218473342940116e-11, "2": 0.15626996024166273, "3": 0.062027694600239214, "4": 0.01890818569542688, "5": 0.004668002755483345, "6": 0.0009672446815898349, "7": 0.00017256796017300278, "8": 2.7021747062074048e-05, "9": 3.7691609902049523e-06} |
| Unadjusted home-win probability | 51.8% |
| Unadjusted draw probability | 30.1% |
| Unadjusted away-win probability | 18.1% |
| Raw p over 1 5 | 56.6% |
| Raw p under 3 5 | 87.6% |
| Raw p btts yes | 33.6% |
| P home draw | 83.0% |
| P draw away | 43.9% |
| P home away | 73.1% |
| Raw p home draw | 81.9% |
| Raw p draw away | 48.2% |
| Raw p home away | 69.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.08, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.62 |
| Reference draw odds | 3.94 |
| Reference away odds | 5.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.29 |
| Reference Under 2.5 odds | 1.64 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -4.3% |
| Draw probability edge | +3.1% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | -10.7% |
| Under 2.5 probability edge | +10.7% |
| Raw edge prob home | -0.0853 |
| Raw ev home | -0.1504 |
| Raw edge prob draw | 0.0630 |
| Raw ev draw | 0.2275 |
| Raw edge prob away | 0.0224 |
| Raw ev away | -0.0022 |

</details>


---

## 2026-10-25 — Barcelona vs Real Madrid

The model's most likely 1X2 outcome is **Barcelona win** at **54.6%**. Expected goals are 1.78 for Barcelona and 1.33 for Real Madrid (3.11 combined). The most likely exact score is 2-1 at 10.7%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 61.3%; Under 3.5 goals: 61.9%; Double Chance 1X: 75.1%; Double Chance X2: 45.4%; Double Chance 12 (either team wins): 79.5%; Under 4.5 goals: 79.0%; BTTS Yes (both teams score): 60.5%; BTTS No (at least one team does not score): 39.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Barcelona win | 54.6% | 1.83 |
| Draw | 20.5% | 4.89 |
| Real Madrid win | 24.9% | 4.01 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Barcelona expected goals | 1.78 |
| Real Madrid expected goals | 1.33 |
| Expected total goals | 3.11 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 61.3% |
| Under 2.5 | 38.7% |
| Over 3.5 | 38.1% |
| Under 3.5 | 61.9% |
| Over 4.5 | 21.0% |
| Under 4.5 | 79.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.75% |
| 2 | 1-1 | 9.33% |
| 3 | 1-0 | 8.84% |
| 4 | 2-0 | 8.06% |
| 5 | 3-1 | 6.36% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Barcelona win | 54.6% | 61.5% | 1.62 | -11.5% |
| Draw | 20.5% | 17.3% | 5.84 | +19.4% |
| Real Madrid win | 24.9% | 21.2% | 4.04 | +0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T20:00:00+00:00 |
| Fixture id | 72089d103a5fe6a922c35e17efba6ffc |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Barcelona |
| Matched away-team name | Real Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7754 |
| Dc lambda away | 1.3331 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.5% |
| P btts no | 39.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.70 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.59 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.58 |
| Fair Over 3.5 odds | 2.63 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.77 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.1407551852272521, "-10": 2.3482370926477058e-07, "-11": 2.7964550258060417e-08, "-12": 3.0607854342667447e-09, "-13": 3.098811329244294e-10, "-14": 2.9168299718211756e-11, "-15": 2.5445610558973656e-12, "-16": 1.84690039528794e-13, "-2": 0.07119523102782876, "-3": 0.026863929231206528, "-4": 0.008065131301733797, "-5": 0.002000602460589254, "-6": 0.0004216741384156837, "-7": 7.714575861154544e-05, "-8": 1.2456223577033151e-05, "-9": 1.798724778405353e-06, "0": 0.20450075921728295, "1": 0.24770110789158825, "10": 5.428463667123994e-06, "11": 8.609416497317826e-07, "12": 1.2549593321972699e-07, "13": 1.6920873901842738e-08, "14": 2.1211415699802462e-09, "15": 2.464349524945097e-10, "16": 2.382120851057453e-11, "2": 0.16631782445968063, "3": 0.08357729559029196, "4": 0.03341651142320055, "5": 0.01103929535203371, "6": 0.0030987633297167505, "7": 0.0007550129195467781, "8": 0.00016235273584763043, "9": 3.122258247242681e-05} |
| Raw goal margin distribution | {"-1": 0.16188897325073984, "-10": 2.7008148315408315e-07, "-11": 3.2163307670597947e-08, "-12": 3.52034925387833e-09, "-13": 3.5640845740721615e-10, "-14": 3.354779495495912e-11, "-15": 2.9266159967603556e-12, "-16": 2.1242045769526727e-13, "-2": 0.08188488994445142, "-3": 0.030897433111959992, "-4": 0.009276076213192994, "-5": 0.00230098434885219, "-6": 0.000484986703717459, "-7": 8.872886375097791e-05, "-8": 1.4326472180842458e-05, "-9": 2.0687955975942834e-06, "0": 0.23628732515553275, "1": 0.21629909289389587, "10": 4.740276605949995e-06, "11": 7.517967903198171e-07, "12": 1.0958633470941248e-07, "13": 1.477575012519704e-08, "14": 1.8522363561129717e-09, "15": 2.1519345284980422e-10, "16": 2.0801302974909296e-11, "2": 0.1452330789673339, "3": 0.07298188278841793, "4": 0.0291801727091195, "5": 0.009639801739916964, "6": 0.0027059212734888336, "7": 0.0006592970496224654, "8": 0.00014177065977457945, "9": 2.7264376506327748e-05} |
| Unadjusted home-win probability | 47.7% |
| Unadjusted draw probability | 23.6% |
| Unadjusted away-win probability | 28.7% |
| Raw p over 1 5 | 81.9% |
| Raw p under 3 5 | 62.3% |
| Raw p btts yes | 61.4% |
| P home draw | 75.1% |
| P draw away | 45.4% |
| P home away | 79.5% |
| Raw p home draw | 71.3% |
| Raw p draw away | 52.3% |
| Raw p home away | 76.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.93, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.42, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.66, "price": 2.42, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.98, "price": 1.93, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.59 |
| Reference draw odds | 5.35 |
| Reference away odds | 4.40 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.18 |
| Reference Under 2.5 odds | 4.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | -6.9% |
| Draw probability edge | +3.2% |
| Away probability edge | +3.7% |
| Over 2.5 probability edge | -21.9% |
| Under 2.5 probability edge | +21.9% |
| Raw edge prob home | -0.1385 |
| Raw ev home | -0.2275 |
| Raw edge prob draw | 0.0636 |
| Raw ev draw | 0.3799 |
| Raw edge prob away | 0.0749 |
| Raw ev away | 0.1588 |

</details>


---

## 2026-10-25 — Celta Vigo vs Real Betis

The model's most likely 1X2 outcome is **Celta Vigo win** at **36.6%**. Expected goals are 1.33 for Celta Vigo and 1.28 for Real Betis (2.61 combined). The most likely exact score is 1-1 at 12.9%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 48.3%; Under 3.5 goals: 73.4%; Double Chance 1X: 63.7%; Double Chance X2: 63.4%; Double Chance 12 (either team wins): 72.9%; Under 4.5 goals: 87.6%; BTTS Yes (both teams score): 53.4%; BTTS No (at least one team does not score): 46.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Celta Vigo win | 36.6% | 2.73 |
| Draw | 27.1% | 3.69 |
| Real Betis win | 36.3% | 2.76 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Celta Vigo expected goals | 1.33 |
| Real Betis expected goals | 1.28 |
| Expected total goals | 2.61 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 48.3% |
| Under 2.5 | 51.7% |
| Over 3.5 | 26.6% |
| Under 3.5 | 73.4% |
| Over 4.5 | 12.4% |
| Under 4.5 | 87.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.89% |
| 2 | 0-1 | 9.37% |
| 3 | 1-0 | 9.25% |
| 4 | 1-2 | 8.20% |
| 5 | 2-1 | 8.09% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Celta Vigo win | 36.6% | 35.6% | 2.87 | +5.1% |
| Draw | 27.1% | 27.4% | 3.54 | -4.1% |
| Real Betis win | 36.3% | 37.0% | 2.49 | -9.6% |
| Over 2.5 | 48.3% | 51.7% | 1.88 | -9.1% |
| Under 2.5 | 51.7% | 48.3% | 2.01 | +3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T15:15:00+00:00 |
| Fixture id | 2013e3955186ebe5258e85eb741a7553 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Celta |
| Matched away-team name | Betis |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3279 |
| Dc lambda away | 1.2829 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.4% |
| P btts no | 46.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.03 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.80 |
| Fair Over 2.5 odds | 2.07 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.76 |
| Fair Under 3.5 odds | 1.36 |
| Fair Over 4.5 odds | 8.08 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.20256158529338714, "-10": 2.9113237674145265e-07, "-11": 3.352467795647792e-08, "-12": 3.544672828154487e-09, "-13": 3.4447187455961e-10, "-14": 2.814084756378104e-11, "-2": 0.10517081264652269, "-3": 0.03975180123744839, "-4": 0.011796318957221292, "-5": 0.0028698286645708775, "-6": 0.000590346601117026, "-7": 0.00010506700372303564, "-8": 1.6465876141665707e-05, "-9": 2.304097369581104e-06, "0": 0.27086188343140427, "1": 0.19988486939724914, "10": 3.917506851160547e-07, "11": 4.66950378562824e-08, "12": 5.110567534922683e-09, "13": 5.14083425918797e-10, "14": 4.347142393794783e-11, "2": 0.10737906578871995, "3": 0.04201148781984293, "4": 0.012904602013249479, "5": 0.0032496825314029146, "6": 0.0006919566577731092, "7": 0.00012747500300783223, "8": 2.06790406170798e-05, "9": 2.995251045998624e-06} |
| Raw goal margin distribution | {"-1": 0.19837888812811155, "-10": 2.8512077999593607e-07, "-11": 3.283242638640733e-08, "-12": 3.471478826593545e-09, "-13": 3.3735886973615947e-10, "-14": 2.7559766786974336e-11, "-2": 0.10299913898347746, "-3": 0.03893096570681384, "-4": 0.01155273659291667, "-5": 0.0028105695301069494, "-6": 0.000578156525434878, "-7": 0.00010289747361198409, "-8": 1.6125872022119687e-05, "-9": 2.2565200289796903e-06, "0": 0.26819042520376163, "1": 0.20543177120303197, "10": 4.026219561093999e-07, "11": 4.799084774217902e-08, "12": 5.2523882558883085e-09, "13": 5.28349489639132e-10, "14": 4.4677776978418e-11, "2": 0.11035888680129988, "3": 0.043177326926896006, "4": 0.013262710960795399, "5": 0.003339862793450841, "6": 0.0007111587897108553, "7": 0.00013101249599821484, "8": 2.1252893996210637e-05, "9": 3.0783707112635494e-06} |
| Unadjusted home-win probability | 37.6% |
| Unadjusted draw probability | 26.8% |
| Unadjusted away-win probability | 35.5% |
| Raw p over 1 5 | 73.7% |
| Raw p under 3 5 | 73.4% |
| Raw p btts yes | 53.4% |
| P home draw | 63.7% |
| P draw away | 63.4% |
| P home away | 72.9% |
| Raw p home draw | 64.5% |
| Raw p draw away | 62.4% |
| Raw p home away | 73.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.1, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.82, "price": 2.1, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.70 |
| Reference draw odds | 3.48 |
| Reference away odds | 2.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.97 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:48Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:48Z |
| Home probability edge | +1.0% |
| Draw probability edge | -0.3% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | -3.4% |
| Under 2.5 probability edge | +3.4% |
| Raw edge prob home | 0.0203 |
| Raw ev home | 0.0804 |
| Raw edge prob draw | -0.0053 |
| Raw ev draw | -0.0506 |
| Raw edge prob away | -0.0150 |
| Raw ev away | -0.1151 |

</details>


---

## 2026-10-25 — Real Sociedad vs Levante

The model's most likely 1X2 outcome is **Real Sociedad win** at **58.3%**. Expected goals are 2.01 for Real Sociedad and 1.04 for Levante (3.05 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.0%; Over 2.5 goals: 58.6%; Under 3.5 goals: 63.7%; Double Chance 1X: 80.4%; Double Chance X2: 41.7%; Double Chance 12 (either team wins): 77.9%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 56.5%; BTTS No (at least one team does not score): 43.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Real Sociedad win | 58.3% | 1.72 |
| Draw | 22.1% | 4.52 |
| Levante win | 19.6% | 5.10 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Real Sociedad expected goals | 2.01 |
| Levante expected goals | 1.04 |
| Expected total goals | 3.05 |
| Over 0.5 | 95.0% |
| Under 0.5 | 5.0% |
| Over 1.5 | 80.9% |
| Under 1.5 | 19.1% |
| Over 2.5 | 58.6% |
| Under 2.5 | 41.4% |
| Over 3.5 | 36.3% |
| Under 3.5 | 63.7% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 9.75% |
| 3 | 2-0 | 9.34% |
| 4 | 1-0 | 9.12% |
| 5 | 3-1 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Real Sociedad win | 58.3% | 57.1% | 1.75 | +2.0% |
| Draw | 22.1% | 22.6% | 4.18 | -7.5% |
| Levante win | 19.6% | 20.3% | 4.43 | -13.1% |
| Over 2.5 | 58.6% | 58.1% | 1.71 | +0.1% |
| Under 2.5 | 41.4% | 41.9% | 2.32 | -3.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T17:30:00+00:00 |
| Fixture id | 3cb8660cd2375b60e81144a7572cfb89 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sociedad |
| Matched away-team name | Levante |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.0053 |
| Dc lambda away | 1.0444 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.5% |
| P btts no | 43.5% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.81 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.24 |
| Fair Over 2.5 odds | 1.71 |
| Fair Under 2.5 odds | 2.41 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.21 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.12526050691645899, "-10": 2.5228676365797676e-08, "-11": 2.358441405595138e-09, "-12": 2.0257594943756983e-10, "-13": 1.6091430903407595e-11, "-14": 1.1886677779872682e-12, "-15": 8.203079200560611e-14, "-16": 5.28050509570977e-15, "-17": 2.8883013465826563e-16, "-2": 0.05109337125973353, "-3": 0.015348277209509622, "-4": 0.003649207040279698, "-5": 0.0007146535671712341, "-6": 0.00011868787227308826, "-7": 1.7087037324192007e-05, "-8": 2.1690498008610887e-06, "-9": 2.4608739449611384e-07, "0": 0.22119228300485166, "1": 0.2293564110076561, "10": 1.625097925171781e-05, "11": 2.9168087171629013e-06, "12": 4.810259761977979e-07, "13": 7.336232718937605e-08, "14": 1.0404871310622405e-08, "15": 1.3786401297300369e-09, "16": 1.7039124078678335e-10, "17": 1.7894191894181924e-11, "2": 0.17822446672973127, "3": 0.10279220618804252, "4": 0.04692419652461959, "5": 0.017643782479733867, "6": 0.005626006915064167, "7": 0.0015551005452535526, "8": 0.00037901728575351313, "9": 8.256132421750862e-05} |
| Raw goal margin distribution | {"-1": 0.12090852594744331, "-10": 2.4352145349596102e-08, "-11": 2.2765010369477877e-09, "-12": 1.9553776399161304e-10, "-13": 1.5532359231259832e-11, "-14": 1.1473693697688434e-12, "-15": 7.918076006441512e-14, "-16": 5.097042181108554e-15, "-17": 2.787951820602425e-16, "-2": 0.049318211755441314, "-3": 0.014815025253507946, "-4": 0.0035224210326046117, "-5": 0.0006898240434823137, "-6": 0.00011456424724473083, "-7": 1.6493374859602594e-05, "-8": 2.0936895481639603e-06, "-9": 2.375374717477091e-07, "0": 0.21630858047764195, "1": 0.23396261002012086, "10": 1.6577350091983307e-05, "11": 2.9753874216931875e-06, "12": 4.906864926263454e-07, "13": 7.483567374885176e-08, "14": 1.0613833893116828e-08, "15": 1.4063275650897349e-09, "16": 1.7381323349061286e-10, "17": 1.8253563619043298e-11, "2": 0.18180377527855635, "3": 0.10485659739713164, "4": 0.04786658216251307, "5": 0.017998125194974467, "6": 0.005738994851099771, "7": 0.00158633186145858, "8": 0.0003866291464365207, "9": 8.421941560639846e-05} |
| Unadjusted home-win probability | 59.4% |
| Unadjusted draw probability | 21.6% |
| Unadjusted away-win probability | 18.9% |
| Raw p over 1 5 | 81.0% |
| Raw p under 3 5 | 63.6% |
| Raw p btts yes | 56.3% |
| P home draw | 80.4% |
| P draw away | 41.7% |
| P home away | 77.9% |
| Raw p home draw | 81.1% |
| Raw p draw away | 40.6% |
| Raw p home away | 78.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.71 |
| Reference draw odds | 4.15 |
| Reference away odds | 4.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.66 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.5% |
| Away probability edge | -0.7% |
| Over 2.5 probability edge | +0.5% |
| Under 2.5 probability edge | -0.5% |
| Raw edge prob home | 0.0234 |
| Raw ev home | 0.0400 |
| Raw edge prob draw | -0.0098 |
| Raw ev draw | -0.0958 |
| Raw edge prob away | -0.0136 |
| Raw ev away | -0.1610 |

</details>


---

## 2026-10-26 — Sevilla vs CA Osasuna

The model's most likely 1X2 outcome is **Sevilla win** at **49.0%**. Expected goals are 1.48 for Sevilla and 0.98 for CA Osasuna (2.46 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 91.2%; Over 2.5 goals: 44.6%; Under 3.5 goals: 76.5%; Double Chance 1X: 75.9%; Double Chance X2: 51.0%; Double Chance 12 (either team wins): 73.1%; Under 4.5 goals: 89.6%; BTTS Yes (both teams score): 48.6%; BTTS No (at least one team does not score): 51.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sevilla win | 49.0% | 2.04 |
| Draw | 26.9% | 3.72 |
| CA Osasuna win | 24.1% | 4.14 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sevilla expected goals | 1.48 |
| CA Osasuna expected goals | 0.98 |
| Expected total goals | 2.46 |
| Over 0.5 | 91.2% |
| Under 0.5 | 8.8% |
| Over 1.5 | 70.8% |
| Under 1.5 | 29.2% |
| Over 2.5 | 44.6% |
| Under 2.5 | 55.4% |
| Over 3.5 | 23.5% |
| Under 3.5 | 76.5% |
| Over 4.5 | 10.4% |
| Under 4.5 | 89.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.72% |
| 2 | 1-0 | 12.49% |
| 3 | 2-0 | 9.44% |
| 4 | 2-1 | 9.25% |
| 5 | 0-0 | 8.84% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sevilla win | 49.0% | 49.3% | 1.99 | -2.6% |
| Draw | 26.9% | 27.1% | 3.38 | -9.1% |
| CA Osasuna win | 24.1% | 23.6% | 4.22 | +1.9% |
| Over 2.5 | 44.6% | 44.7% | 2.19 | -2.3% |
| Under 2.5 | 55.4% | 55.3% | 1.79 | -0.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T20:00:00+00:00 |
| Fixture id | 85e464708d03287f24590e1478aeca31 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Sevilla |
| Matched away-team name | Osasuna |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 95/100 |
| Dc lambda home | 1.4831 |
| Dc lambda away | 0.9791 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 48.6% |
| P btts no | 51.4% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.31 |
| Fair Over 1.5 odds | 1.41 |
| Fair Under 1.5 odds | 3.42 |
| Fair Over 2.5 odds | 2.24 |
| Fair Under 2.5 odds | 1.80 |
| Fair Over 3.5 odds | 4.26 |
| Fair Under 3.5 odds | 1.31 |
| Fair Over 4.5 odds | 9.64 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.1545766056429341, "-10": 2.1194734106194466e-08, "-11": 1.866185795477386e-09, "-12": 1.5087159407374845e-10, "-13": 1.1272105240705777e-11, "-14": 7.798382456000831e-13, "-15": 4.641003272469176e-14, "-2": 0.06312910575613281, "-3": 0.018508857148108585, "-4": 0.004236675035450418, "-5": 0.000792518580836186, "-6": 0.00012510792631449313, "-7": 1.706517071014533e-05, "-8": 2.0479130068020465e-06, "-9": 2.1929798352753291e-07, "0": 0.26891653593341747, "1": 0.24263361061036184, "10": 1.3890334642429329e-06, "11": 1.8525506946368843e-07, "12": 2.268575232429852e-08, "13": 2.5673272332786697e-09, "14": 2.6903650271865177e-10, "15": 2.4252082589833414e-11, "2": 0.14930367211193832, "3": 0.06630571169349313, "4": 0.022989365055543234, "5": 0.006513910117607171, "6": 0.001557570164662643, "7": 0.000321813246523755, "8": 5.849722566995842e-05, "9": 9.48831051379e-06} |
| Raw goal margin distribution | {"-1": 0.15817801954153274, "-10": 2.1688541106740672e-08, "-11": 1.9096652562486016e-09, "-12": 1.5438668650019266e-10, "-13": 1.153472917601277e-11, "-14": 7.980073617136203e-13, "-15": 4.7491320130337174e-14, "-2": 0.0645999236585612, "-3": 0.018940087055785253, "-4": 0.004335383506198976, "-5": 0.0008109831306304425, "-6": 0.000128022762118914, "-7": 1.7462764787993324e-05, "-8": 2.0956264517644394e-06, "-9": 2.2440731299253018e-07, "0": 0.26686231316311193, "1": 0.24086486140199603, "10": 1.3789076954589092e-06, "11": 1.839045980403956e-07, "12": 2.252037784726771e-08, "13": 2.54861194482356e-09, "14": 2.6707528184736333e-10, "15": 2.4075289886736418e-11, "2": 0.1482152789944729, "3": 0.0658223566678931, "4": 0.022821777304033727, "5": 0.00646642505016371, "6": 0.0015462157979333551, "7": 0.0003194672940252588, "8": 5.807079290437802e-05, "9": 9.419142678106487e-06} |
| Unadjusted home-win probability | 48.6% |
| Unadjusted draw probability | 26.7% |
| Unadjusted away-win probability | 24.7% |
| Raw p over 1 5 | 70.7% |
| Raw p under 3 5 | 76.6% |
| Raw p btts yes | 48.5% |
| P home draw | 75.9% |
| P draw away | 51.0% |
| P home away | 73.1% |
| Raw p home draw | 75.3% |
| Raw p draw away | 51.4% |
| Raw p home away | 73.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.96, "price": 1.48, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.97 |
| Reference draw odds | 3.50 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.12 |
| Reference Under 2.5 odds | 1.74 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -0.4% |
| Draw probability edge | -0.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.1% |
| Under 2.5 probability edge | +0.1% |
| Raw edge prob home | -0.0071 |
| Raw ev home | -0.0326 |
| Raw edge prob draw | -0.0041 |
| Raw ev draw | -0.0980 |
| Raw edge prob away | 0.0112 |
| Raw ev away | 0.0424 |

</details>


---

## 2026-10-30 — Villarreal vs Espanyol

The model's most likely 1X2 outcome is **Villarreal win** at **64.0%**. Expected goals are 2.22 for Villarreal and 0.99 for Espanyol (3.21 combined). The most likely exact score is 2-0 at 9.8%. Goal-market probabilities: at least one goal: 95.7%; Over 2.5 goals: 61.9%; Under 3.5 goals: 60.2%; Double Chance 1X: 84.0%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 79.9%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 56.3%; BTTS No (at least one team does not score): 43.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Villarreal win | 64.0% | 1.56 |
| Draw | 20.1% | 4.98 |
| Espanyol win | 16.0% | 6.27 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Villarreal expected goals | 2.22 |
| Espanyol expected goals | 0.99 |
| Expected total goals | 3.21 |
| Over 0.5 | 95.7% |
| Under 0.5 | 4.3% |
| Over 1.5 | 83.1% |
| Under 1.5 | 16.9% |
| Over 2.5 | 61.9% |
| Under 2.5 | 38.1% |
| Over 3.5 | 39.8% |
| Under 3.5 | 60.2% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 9.79% |
| 2 | 2-1 | 9.65% |
| 3 | 1-1 | 9.31% |
| 4 | 1-0 | 8.63% |
| 5 | 3-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Villarreal win | 64.0% | 62.7% | 1.56 | -0.2% |
| Draw | 20.1% | 20.7% | 4.31 | -13.5% |
| Espanyol win | 16.0% | 16.6% | 5.40 | -13.8% |
| Over 2.5 | 61.9% | 60.0% | 1.66 | +2.8% |
| Under 2.5 | 38.1% | 40.0% | 2.42 | -7.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T20:00:00+00:00 |
| Fixture id | 00b03cb40c27ed23e2ecb18f062a5122 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Villarreal |
| Matched away-team name | Espanol |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2233 |
| Dc lambda away | 0.9860 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 56.3% |
| P btts no | 43.7% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 23.01 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.90 |
| Fair Over 2.5 odds | 1.62 |
| Fair Under 2.5 odds | 2.63 |
| Fair Over 3.5 odds | 2.51 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.56 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.10505854069819393, "-10": 1.2262027505212768e-08, "-11": 1.0814015159678326e-09, "-12": 8.763744281593013e-11, "-13": 6.5685998631369e-12, "-14": 4.578714847897474e-13, "-15": 2.981764184811997e-14, "-16": 1.810406924915449e-15, "-17": 9.300898364559256e-17, "-2": 0.04012360274877425, "-3": 0.011312654014911553, "-4": 0.0025293404081313565, "-5": 0.0004663366930727738, "-6": 7.296510931364371e-05, "-7": 9.901173780760326e-06, "-8": 1.1850699080899263e-06, "-9": 1.268007890025992e-07, "0": 0.20061358375846616, "1": 0.22537551104154982, "10": 3.926756771355658e-05, "11": 7.808947629419832e-06, "12": 1.427016694082717e-06, "13": 2.4118260675893784e-07, "14": 3.7909721698529245e-08, "15": 5.566908889711236e-09, "16": 7.621682313414707e-10, "17": 8.829444070986828e-11, "2": 0.19222110545435628, "3": 0.12220795431370207, "4": 0.061613527327478386, "5": 0.025615462388208058, "6": 0.009037569902094044, "7": 0.002765393488615443, "8": 0.0007463594639147389, "9": 0.0001800776648779709} |
| Raw goal margin distribution | {"-1": 0.10089961792095992, "-10": 1.177661408572696e-08, "-11": 1.0385923795929608e-09, "-12": 8.416816412003845e-11, "-13": 6.3085705556309585e-12, "-14": 4.397458556454357e-13, "-15": 2.8637259282158014e-14, "-16": 1.738738857321374e-15, "-17": 8.932706328004831e-17, "-2": 0.03853524101951758, "-3": 0.010864823175639365, "-4": 0.0024292121237972416, "-5": 0.00044787595411912787, "-6": 7.007666013996221e-05, "-7": 9.50921881085026e-06, "-8": 1.13815688035686e-06, "-9": 1.2178116198275407e-07, "0": 0.19454827602858543, "1": 0.22973722731920634, "10": 4.00275171352514e-05, "11": 7.96007502489062e-06, "12": 1.4546339002037527e-06, "13": 2.458502394441685e-07, "14": 3.864339258162453e-08, "15": 5.674645870576064e-09, "16": 7.769185543272804e-10, "17": 9.000321242819314e-11, "2": 0.19594118098827187, "3": 0.1245730578740925, "4": 0.0628059404864154, "5": 0.026111201160987814, "6": 0.009212474955310563, "7": 0.0028189124434374498, "8": 0.0007608038381402054, "9": 0.0001835627271125977} |
| Unadjusted home-win probability | 65.2% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 15.3% |
| Raw p over 1 5 | 83.2% |
| Raw p under 3 5 | 60.0% |
| Raw p btts yes | 56.1% |
| P home draw | 84.0% |
| P draw away | 36.0% |
| P home away | 79.9% |
| Raw p home draw | 84.7% |
| Raw p draw away | 34.8% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.56, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 1.56 |
| Reference draw odds | 4.50 |
| Reference away odds | 5.55 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 1.61 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | +1.2% |
| Draw probability edge | -0.6% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | 0.0248 |
| Raw ev home | 0.0174 |
| Raw edge prob draw | -0.0121 |
| Raw ev draw | -0.1615 |
| Raw edge prob away | -0.0126 |
| Raw ev away | -0.1724 |

</details>


---

## 2026-10-31 — Levante vs Atlético Madrid

The model's most likely 1X2 outcome is **Atlético Madrid win** at **60.3%**. Expected goals are 1.20 for Levante and 2.11 for Atlético Madrid (3.32 combined). The most likely exact score is 1-2 at 10.1%. Goal-market probabilities: at least one goal: 96.3%; Over 2.5 goals: 64.6%; Under 3.5 goals: 57.4%; Double Chance 1X: 39.7%; Double Chance X2: 81.0%; Double Chance 12 (either team wins): 79.3%; Under 4.5 goals: 75.8%; BTTS Yes (both teams score): 61.5%; BTTS No (at least one team does not score): 38.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Levante win | 19.0% | 5.26 |
| Draw | 20.7% | 4.84 |
| Atlético Madrid win | 60.3% | 1.66 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Levante expected goals | 1.20 |
| Atlético Madrid expected goals | 2.11 |
| Expected total goals | 3.32 |
| Over 0.5 | 96.3% |
| Under 0.5 | 3.7% |
| Over 1.5 | 84.7% |
| Under 1.5 | 15.3% |
| Over 2.5 | 64.6% |
| Under 2.5 | 35.4% |
| Over 3.5 | 42.6% |
| Under 3.5 | 57.4% |
| Over 4.5 | 24.2% |
| Under 4.5 | 75.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.13% |
| 2 | 1-1 | 9.25% |
| 3 | 0-2 | 8.42% |
| 4 | 0-1 | 7.78% |
| 5 | 1-3 | 7.14% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Levante win | 19.0% | 17.1% | 4.56 | -13.3% |
| Draw | 20.7% | 20.3% | 4.63 | -4.3% |
| Atlético Madrid win | 60.3% | 62.6% | 1.61 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 005711684f3e51024ac40c1ee69978e9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Levante |
| Matched away-team name | Ath Madrid |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2030 |
| Dc lambda away | 2.1128 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 61.5% |
| P btts no | 38.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.68 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.52 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.83 |
| Fair Over 3.5 odds | 2.35 |
| Fair Under 3.5 odds | 1.74 |
| Fair Over 4.5 odds | 4.13 |
| Fair Under 4.5 odds | 1.32 |
| Goal margin distribution | {"-1": 0.2323999647945099, "-10": 2.317087298621429e-05, "-11": 4.36770533225774e-06, "-12": 7.568412139927351e-07, "-13": 1.2132928108394165e-07, "-14": 1.8093180175085614e-08, "-15": 2.520818803094678e-09, "-16": 3.268394415717095e-10, "-17": 3.5336886909951875e-11, "-2": 0.1825242123462395, "-3": 0.10806552896594898, "-4": 0.05107082452398227, "-5": 0.019980351398003776, "-6": 0.006650188826485894, "-7": 0.0019228349202636242, "-8": 0.0004909531753616214, "-9": 0.00011215636773951764, "0": 0.20670592857413445, "1": 0.11492516842361537, "10": 7.254013283469666e-08, "11": 7.785840066726188e-09, "12": 7.681979052623921e-10, "13": 7.012133353157322e-11, "14": 5.954093467251789e-12, "15": 4.723441783591916e-13, "16": 3.487125636522838e-14, "17": 2.1467309566326154e-15, "2": 0.05171622937077325, "3": 0.017434510205729174, "4": 0.004691499068540574, "5": 0.0010451005695798021, "6": 0.00019806381359175896, "7": 3.260839011670591e-05, "8": 4.740712607516879e-06, "9": 6.166570320855339e-07} |
| Raw goal margin distribution | {"-1": 0.22359767122539112, "-10": 2.229326172470759e-05, "-11": 4.202275769512616e-06, "-12": 7.281753811185225e-07, "-13": 1.1673385891348095e-07, "-14": 1.740788969476698e-08, "-15": 2.4253412191844837e-09, "-16": 3.144601939361738e-10, "-17": 3.39984802855138e-11, "-2": 0.1756109939988771, "-3": 0.10397247967697223, "-4": 0.04913648520222493, "-5": 0.019223583130956526, "-6": 0.006398308778257138, "-7": 0.001850006348761563, "-8": 0.00047235801773306863, "-9": 0.00010790837538133378, "0": 0.2103738058419147, "1": 0.1265238480816783, "10": 7.986115550226135e-08, "11": 8.571616289998724e-09, "12": 8.457273232249643e-10, "13": 7.719824188841822e-11, "14": 6.555002943636148e-12, "15": 5.200149269714116e-13, "16": 3.839059453459809e-14, "17": 2.3633871079314312e-15, "2": 0.05693562548584779, "3": 0.019194066459987655, "4": 0.00516498277588245, "5": 0.0011505760444760775, "6": 0.0002180531575902581, "7": 3.589935132491329e-05, "8": 5.219163130059074e-06, "9": 6.78892375937179e-07} |
| Unadjusted home-win probability | 20.9% |
| Unadjusted draw probability | 21.0% |
| Unadjusted away-win probability | 58.0% |
| Raw p over 1 5 | 84.5% |
| Raw p under 3 5 | 57.7% |
| Raw p btts yes | 61.7% |
| P home draw | 39.7% |
| P draw away | 81.0% |
| P home away | 79.3% |
| Raw p home draw | 42.0% |
| Raw p draw away | 79.1% |
| Raw p home away | 79.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.6, "price": 2.57, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.57, "price": 1.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 5.10 |
| Reference draw odds | 4.35 |
| Reference away odds | 1.54 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.53 |
| Reference Under 2.5 odds | 2.54 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:53Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:53Z |
| Home probability edge | +1.9% |
| Draw probability edge | +0.4% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | +1.3% |
| Under 2.5 probability edge | -1.3% |
| Raw edge prob home | 0.0384 |
| Raw ev home | -0.0459 |
| Raw edge prob draw | 0.0073 |
| Raw ev draw | -0.0260 |
| Raw edge prob away | -0.0457 |
| Raw ev away | -0.0656 |

</details>


---

## 2026-10-31 — Rayo Vallecano vs Celta Vigo

The model's most likely 1X2 outcome is **Rayo Vallecano win** at **41.0%**. Expected goals are 1.22 for Rayo Vallecano and 1.07 for Celta Vigo (2.29 combined). The most likely exact score is 1-1 at 13.2%. Goal-market probabilities: at least one goal: 89.8%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.0%; Double Chance 1X: 69.4%; Double Chance X2: 59.0%; Double Chance 12 (either team wins): 71.7%; Under 4.5 goals: 91.6%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rayo Vallecano win | 41.0% | 2.44 |
| Draw | 28.3% | 3.53 |
| Celta Vigo win | 30.6% | 3.26 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rayo Vallecano expected goals | 1.22 |
| Celta Vigo expected goals | 1.07 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.8% |
| Under 0.5 | 10.2% |
| Over 1.5 | 67.1% |
| Under 1.5 | 32.9% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 20.0% |
| Under 3.5 | 80.0% |
| Over 4.5 | 8.4% |
| Under 4.5 | 91.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.24% |
| 2 | 1-0 | 12.61% |
| 3 | 0-0 | 10.17% |
| 4 | 0-1 | 10.14% |
| 5 | 2-1 | 8.43% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rayo Vallecano win | 41.0% | 42.8% | 2.32 | -4.8% |
| Draw | 28.3% | 27.8% | 3.46 | -2.0% |
| Celta Vigo win | 30.6% | 29.3% | 3.03 | -7.2% |
| Over 2.5 | 40.4% | 46.4% | 2.11 | -14.7% |
| Under 2.5 | 59.6% | 53.6% | 1.84 | +9.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T15:15:00+00:00 |
| Fixture id | 77383723574e3d39c7aba22eec6c4ce3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:15:48Z |
| Market best draw last update utc | 2026-10-21T17:15:48Z |
| Market best away last update utc | 2026-10-21T17:15:48Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Vallecano |
| Matched away-team name | Celta |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2208 |
| Dc lambda away | 1.0727 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:14:04.838687+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.83 |
| Fair Over 1.5 odds | 1.49 |
| Fair Under 1.5 odds | 3.04 |
| Fair Over 2.5 odds | 2.47 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.01 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.97 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.18595736805441543, "-10": 6.059451897267065e-08, "-11": 5.851297093451526e-09, "-12": 5.186538185511717e-10, "-13": 4.233466718962302e-11, "-14": 2.966192677275043e-12, "-2": 0.08438841303224535, "-3": 0.027363902281120872, "-4": 0.006904386951950543, "-5": 0.0014210272607355899, "-6": 0.00024653406798716914, "-7": 3.693004832190159e-05, "-8": 4.864485336242309e-06, "-9": 5.715553769219463e-07, "0": 0.28337307248453353, "1": 0.23097484725812292, "10": 2.4072650508578886e-07, "11": 2.6456150358332177e-08, "12": 2.6689228040808414e-09, "13": 2.4793538596074173e-10, "14": 1.9770864303587312e-11, "2": 0.11909730427427855, "3": 0.04395224618195044, "4": 0.012621532764413227, "5": 0.0029564689172604654, "6": 0.0005837565707703695, "7": 9.95218975819312e-05, "8": 1.4919683245209124e-05, "9": 1.995101297906057e-06} |
| Raw goal margin distribution | {"-1": 0.19376228648014443, "-10": 6.313776467772706e-08, "-11": 6.096885084811625e-09, "-12": 5.404225217079092e-10, "-13": 4.411151866613299e-11, "-14": 3.0906883728387276e-12, "-2": 0.08793032528172753, "-3": 0.02851240759364644, "-4": 0.007194174753872285, "-5": 0.0014806699732928732, "-6": 0.000256881484225282, "-7": 3.848005958322643e-05, "-8": 5.06865531148855e-06, "-9": 5.955444403257541e-07, "0": 0.2884369652444219, "1": 0.22088656475175197, "10": 2.3021229966946133e-07, "11": 2.5300625754618012e-08, "12": 2.5523523309107743e-09, "13": 2.371063184384983e-10, "14": 1.8907332768195423e-11, "2": 0.11389549435632049, "3": 0.042032545047663884, "4": 0.012070262400118874, "5": 0.0028273392998467684, "6": 0.0005582598499334876, "7": 9.517508220226941e-05, "8": 1.4268036621042148e-05, "9": 1.9079613094569645e-06} |
| Unadjusted home-win probability | 39.2% |
| Unadjusted draw probability | 28.8% |
| Unadjusted away-win probability | 31.9% |
| Raw p over 1 5 | 67.0% |
| Raw p under 3 5 | 80.1% |
| Raw p btts yes | 46.6% |
| P home draw | 69.4% |
| P draw away | 59.0% |
| P home away | 71.7% |
| Raw p home draw | 68.1% |
| Raw p draw away | 60.8% |
| Raw p home away | 71.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:15:48Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:15:49Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.38, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Marathon Bet |
| Reference home odds | 2.26 |
| Reference draw odds | 3.42 |
| Reference away odds | 3.25 |
| Market reference 1x2 last update utc | 2026-10-21T17:15:54Z |
| Market reference home last update utc | 2026-10-21T17:15:54Z |
| Market reference draw last update utc | 2026-10-21T17:15:54Z |
| Market reference away last update utc | 2026-10-21T17:15:54Z |
| O/U 2.5 market source | The Odds API / Marathon Bet |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.79 |
| Market reference over 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:15:54Z |
| Market best over 2 5 last update utc | 2026-10-21T17:15:49Z |
| Market best under 2 5 last update utc | 2026-10-21T17:15:49Z |
| Home probability edge | -1.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +1.3% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.0358 |
| Raw ev home | -0.0897 |
| Raw edge prob draw | 0.0101 |
| Raw ev draw | -0.0020 |
| Raw edge prob away | 0.0257 |
| Raw ev away | -0.0329 |

</details>


---
