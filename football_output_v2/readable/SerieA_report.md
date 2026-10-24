# Serie A — football model report

Fixtures in this report: **7**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Serie A |
| Training matches | 1,971 |
| Training data through | 2026-10-23 |
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
| Training sha256 | 02f2b682fedb53563509a06be6e9732dd9f3bdfccb7da269a01265187d864e6a |
| Training as of utc | 2026-10-24T14:48:23.942089+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 71, 'bbs_added_results': 1, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 71, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 918, 'added_results': 0, 'conflicts': 0, 'unmapped': 223, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 79, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-24T14:48:23.942089+00:00', 'observations': 277, 'observations_sha256': '537d389f68b7206c864bce45be3986f4d2a743271fabdd5fdad5ba0f6404d5c0', 'eligible_training_matches': 107, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 114, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 8, 'retrospective_eligible_training_matches': 107, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:28.568690+00:00', 'retrospective_inputs_sha256': 'fd2adf57de435112298380c261fc09ad3451d79dc912a83577aa071fbe06c33c', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5477.659 |
| Base scoring parameter | 0.135 |
| Home-advantage parameter | 0.138 |
| Dixon-Coles low-score adjustment | -0.043 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 27, 'matches': 1971, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-23'} |
| Training data health | {'training_end': '2026-10-23', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 15.00 |
| Bbs statistics model artifact | bbs/feature_models/SerieA/20261024T144823942089Z_370d90c849f87f46e46414197f555dfaa6efab57a87919380c4d07d875d211ae.json |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-24 — Lazio vs Parma

The model's most likely 1X2 outcome is **Lazio win** at **62.8%**. Expected goals are 1.73 for Lazio and 0.76 for Parma (2.49 combined). The most likely exact score is 1-0 at 14.5%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 46.0%; Under 3.5 goals: 75.6%; Double Chance 1X: 85.8%; Double Chance X2: 37.2%; Double Chance 12 (either team wins): 77.0%; Under 4.5 goals: 89.0%; BTTS Yes (both teams score): 43.9%; BTTS No (at least one team does not score): 56.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lazio win | 62.8% | 1.59 |
| Draw | 23.0% | 4.34 |
| Parma win | 14.2% | 7.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lazio expected goals | 1.73 |
| Parma expected goals | 0.76 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 71.9% |
| Under 1.5 | 28.1% |
| Over 2.5 | 46.0% |
| Under 2.5 | 54.0% |
| Over 3.5 | 24.4% |
| Under 3.5 | 75.6% |
| Over 4.5 | 11.0% |
| Under 4.5 | 89.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.51% |
| 2 | 2-0 | 12.94% |
| 3 | 1-1 | 10.80% |
| 4 | 2-1 | 9.89% |
| 5 | 0-0 | 8.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lazio win | 62.8% | 65.6% | 1.51 | -5.2% |
| Draw | 23.0% | 21.7% | 4.28 | -1.4% |
| Parma win | 14.2% | 12.6% | 7.20 | +2.2% |
| Over 2.5 | 46.0% | 50.0% | 1.95 | -10.3% |
| Under 2.5 | 54.0% | 50.0% | 1.95 | +5.3% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Lazio |
| Matched away-team name | Parma |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7255 |
| Dc lambda away | 0.7641 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 43.9% |
| P btts no | 56.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.05 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.56 |
| Fair Over 2.5 odds | 2.17 |
| Fair Under 2.5 odds | 1.85 |
| Fair Over 3.5 odds | 4.11 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.11 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.0996097532830132, "-10": 1.572662737624373e-09, "-11": 1.0817615565656907e-10, "-12": 6.83109730091871e-12, "-13": 3.9865764543856446e-13, "-14": 2.1622249629206476e-14, "-15": 1.0922873224308164e-15, "-16": 4.819435836972971e-17, "-2": 0.03308840559368559, "-3": 0.007638612844794478, "-4": 0.0013724524001355119, "-5": 0.00020116929801519275, "-6": 2.4857341114432998e-05, "-7": 2.652139895994112e-06, "-8": 2.488320065654239e-07, "-9": 2.0825259370225302e-08, "0": 0.23045863061186384, "1": 0.2682574689656452, "10": 6.314589536998265e-06, "11": 9.807975780728841e-07, "12": 1.3985455800438145e-07, "13": 1.8429967248643795e-08, "14": 2.257166808865497e-09, "15": 2.574767294450841e-10, "16": 2.565284907146868e-11, "2": 0.19655263493330385, "3": 0.10246035135517984, "4": 0.04156970527743867, "5": 0.013758771788956826, "6": 0.003838936702004222, "7": 0.0009248919942762944, "8": 0.0001959472377849973, "9": 3.70306755978826e-05} |
| Raw goal margin distribution | {"-1": 0.11070673074702073, "-10": 1.747864486275608e-09, "-11": 1.2022746912637793e-10, "-12": 7.592112465642188e-12, "-13": 4.4306991192332107e-13, "-14": 2.4031066125064285e-14, "-15": 1.2139730750979995e-15, "-16": 5.3563428075199964e-17, "-2": 0.036774603772992645, "-3": 0.008489588896849592, "-4": 0.0015253498108082884, "-5": 0.00022358046853764295, "-6": 2.7626561447488987e-05, "-7": 2.9476002870425937e-06, "-8": 2.765530185965938e-07, "-9": 2.314528754313828e-08, "0": 0.2435194316508723, "1": 0.2559160826860312, "10": 6.024082104069028e-06, "11": 9.35675249066427e-07, "12": 1.334204440542577e-07, "13": 1.7582082767316355e-08, "14": 2.1533241550406367e-09, "15": 2.456313191817808e-10, "16": 2.4472670488615592e-11, "2": 0.18751008338258263, "3": 0.09774658595921548, "4": 0.03965725977373387, "5": 0.013125789162097262, "6": 0.003662323536581085, "7": 0.0008823416436288422, "8": 0.00018693253798464352, "9": 3.5327051562694716e-05} |
| Unadjusted home-win probability | 59.9% |
| Unadjusted draw probability | 24.4% |
| Unadjusted away-win probability | 15.8% |
| Raw p over 1 5 | 71.5% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 44.4% |
| P home draw | 85.8% |
| P draw away | 37.2% |
| P home away | 77.0% |
| Raw p home draw | 84.2% |
| Raw p draw away | 40.1% |
| Raw p home away | 75.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.49, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.63, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.53, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.49, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.06, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.56, "price": 1.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.17, "price": 5.56, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.50 |
| Reference draw odds | 4.35 |
| Reference away odds | 7.35 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.91 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market best over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market best under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | -2.9% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.6% |
| Over 2.5 probability edge | -4.0% |
| Under 2.5 probability edge | +4.0% |
| Raw edge prob home | -0.0577 |
| Raw ev home | -0.0959 |
| Raw edge prob draw | 0.0261 |
| Raw ev draw | 0.0423 |
| Raw edge prob away | 0.0316 |
| Raw ev away | 0.1358 |
| Market p home draw | 86.5% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 35.9% |
| Market draw away odds | 2.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.6% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.72 |
| Market reference dc home draw odds | 1.13 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.70 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.4% |
| Market under 3 5 odds | 1.36 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.36 |
| Market reference under 3 5 opposite odds | 3.40 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 45.8% |
| Market btts yes odds | 2.10 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 2.10 |
| Market reference btts yes opposite odds | 1.79 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,525.7636 |
| Elo away rating | 1,403.2770 |
| Elo rating diff | 182.4866 |
| Elo home expectancy | 0.7409 |

</details>


---

## 2026-10-24 — Napoli vs AS Roma

The model's most likely 1X2 outcome is **Napoli win** at **40.4%**. Expected goals are 1.36 for Napoli and 0.99 for AS Roma (2.35 combined). The most likely exact score is 1-1 at 13.5%. Goal-market probabilities: at least one goal: 89.9%; Over 2.5 goals: 41.6%; Under 3.5 goals: 79.1%; Double Chance 1X: 69.1%; Double Chance X2: 59.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 91.1%; BTTS Yes (both teams score): 47.4%; BTTS No (at least one team does not score): 52.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Napoli win | 40.4% | 2.48 |
| Draw | 28.7% | 3.49 |
| AS Roma win | 30.9% | 3.23 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Napoli expected goals | 1.36 |
| AS Roma expected goals | 0.99 |
| Expected total goals | 2.35 |
| Over 0.5 | 89.9% |
| Under 0.5 | 10.1% |
| Over 1.5 | 68.4% |
| Under 1.5 | 31.6% |
| Over 2.5 | 41.6% |
| Under 2.5 | 58.4% |
| Over 3.5 | 20.9% |
| Under 3.5 | 79.1% |
| Over 4.5 | 8.9% |
| Under 4.5 | 91.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.48% |
| 2 | 1-0 | 11.21% |
| 3 | 0-1 | 10.26% |
| 4 | 0-0 | 10.14% |
| 5 | 2-0 | 7.96% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Napoli win | 40.4% | 36.1% | 2.77 | +11.9% |
| Draw | 28.7% | 28.9% | 3.28 | -5.9% |
| AS Roma win | 30.9% | 35.0% | 2.77 | -14.3% |
| Over 2.5 | 41.6% | 53.5% | 1.86 | -22.7% |
| Under 2.5 | 58.4% | 46.5% | 2.05 | +19.8% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.3590 |
| Dc lambda away | 0.9919 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.4% |
| P btts no | 52.6% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 9.86 |
| Fair Over 1.5 odds | 1.46 |
| Fair Under 1.5 odds | 3.16 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 4.78 |
| Fair Under 3.5 odds | 1.26 |
| Fair Over 4.5 odds | 11.24 |
| Fair Under 4.5 odds | 1.10 |
| Goal margin distribution | {"-1": 0.19455750993777415, "-10": 3.15436789776775e-08, "-11": 2.815945128014755e-09, "-12": 2.307579861050437e-10, "-13": 1.7410469331668904e-11, "-14": 1.1252213485176096e-12, "-2": 0.08282784766041267, "-3": 0.02477241805443652, "-4": 0.00577042329097573, "-5": 0.0010969775873384807, "-6": 0.00017584074805244884, "-7": 2.4342054744084742e-05, "-8": 2.9635280497174743e-06, "-9": 3.2186079821303925e-07, "0": 0.286845174524959, "1": 0.21085189113963498, "10": 5.764885103696932e-07, "11": 7.051088113389567e-08, "12": 7.916666248526192e-09, "13": 8.183700308719209e-10, "14": 7.246542505133231e-11, "2": 0.1219061316334826, "3": 0.04995410897393346, "4": 0.01594278284865345, "5": 0.004152482925014321, "6": 0.0009119756982377065, "7": 0.00017297152724954313, "8": 2.8852275443677813e-05, "9": 4.293314998451095e-06} |
| Raw goal margin distribution | {"-1": 0.16870452601599473, "-10": 2.7352125407195997e-08, "-11": 2.441759705193181e-09, "-12": 2.0009464904597076e-10, "-13": 1.5096949880036166e-11, "-14": 9.757008831242522e-13, "-2": 0.07182160578095441, "-3": 0.021480635969695714, "-4": 0.0050036440460564735, "-5": 0.0009512101793515845, "-6": 0.00015247486495881962, "-7": 2.1107459738612207e-05, "-8": 2.5697316702017586e-06, "-9": 2.790916342577946e-07, "0": 0.28513840489023035, "1": 0.2331923749243047, "10": 6.375694527712649e-07, "11": 7.7981751744069e-08, "12": 8.755464292963534e-09, "13": 9.050791531175741e-10, "14": 8.0143386318639e-11, "2": 0.13482250597705464, "3": 0.05524691880114396, "4": 0.01763197557909466, "5": 0.004592452787039248, "6": 0.0010086026632052615, "7": 0.0001912984560659837, "8": 3.1909273359212005e-05, "9": 4.748206503511662e-06} |
| Unadjusted home-win probability | 44.7% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 26.8% |
| Raw p over 1 5 | 68.6% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.3% |
| P home draw | 69.1% |
| P draw away | 59.6% |
| P home away | 71.3% |
| Raw p home draw | 73.2% |
| Raw p draw away | 55.3% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.99, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.95, "price": 1.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.36, "price": 1.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.66, "price": 2.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.73, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 2.68 |
| Reference draw odds | 3.33 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.80 |
| Reference Under 2.5 odds | 2.05 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market best over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market best under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | +4.3% |
| Draw probability edge | -0.2% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -11.9% |
| Under 2.5 probability edge | +11.9% |
| Raw edge prob home | 0.0856 |
| Raw ev home | 0.2374 |
| Raw edge prob draw | -0.0034 |
| Raw ev draw | -0.0647 |
| Raw edge prob away | -0.0822 |
| Raw ev away | -0.2573 |
| Market p home draw | 65.1% |
| Market home draw odds | 1.49 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.6% |
| Market draw away odds | 1.50 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.3% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.49 |
| Market reference dc home away odds | 1.38 |
| Market p over 1 5 | 76.9% |
| Market over 1 5 odds | 1.25 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference over 1 5 odds | 1.28 |
| Market reference over 1 5 opposite odds | 3.95 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.8% |
| Market under 3 5 odds | 1.41 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.41 |
| Market reference under 3 5 opposite odds | 3.15 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.1% |
| Market btts yes odds | 1.62 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 1.62 |
| Market reference btts yes opposite odds | 2.39 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,562.3912 |
| Elo away rating | 1,591.2548 |
| Elo rating diff | 31.1364 |
| Elo home expectancy | 0.5447 |

</details>


---

## 2026-10-25 — Atalanta BC vs Frosinone

The model's most likely 1X2 outcome is **Atalanta BC win** at **60.1%**. Expected goals are 2.42 for Atalanta BC and 1.05 for Frosinone (3.47 combined). The most likely exact score is 1-1 at 9.2%. Goal-market probabilities: at least one goal: 96.1%; Over 2.5 goals: 66.2%; Under 3.5 goals: 55.3%; Double Chance 1X: 80.7%; Double Chance X2: 39.9%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Atalanta BC win | 60.1% | 1.66 |
| Draw | 20.6% | 4.86 |
| Frosinone win | 19.3% | 5.18 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Atalanta BC expected goals | 2.42 |
| Frosinone expected goals | 1.05 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.1% |
| Under 0.5 | 3.9% |
| Over 1.5 | 85.8% |
| Under 1.5 | 14.2% |
| Over 2.5 | 66.2% |
| Under 2.5 | 33.8% |
| Over 3.5 | 44.7% |
| Under 3.5 | 55.3% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.23% |
| 2 | 2-1 | 8.54% |
| 3 | 2-0 | 8.13% |
| 4 | 3-1 | 6.90% |
| 5 | 3-0 | 6.57% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Atalanta BC win | 60.1% | 52.9% | 1.85 | +11.2% |
| Draw | 20.6% | 22.8% | 4.17 | -14.2% |
| Frosinone win | 19.3% | 24.3% | 3.93 | -24.1% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Atalanta |
| Matched away-team name | Frosinone |
| Home-name matching confidence | 95/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4250 |
| Dc lambda away | 1.0499 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.94 |
| Fair Over 1.5 odds | 1.17 |
| Fair Under 1.5 odds | 7.05 |
| Fair Over 2.5 odds | 1.51 |
| Fair Under 2.5 odds | 2.96 |
| Fair Over 3.5 odds | 2.24 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.1242583973600555, "-10": 2.3514839575136646e-08, "-11": 2.2026109888549212e-09, "-12": 1.8966014844345052e-10, "-13": 1.5108649638825004e-11, "-14": 1.1196260582022051e-12, "-15": 7.755129069225118e-14, "-16": 5.0400555881408175e-15, "-17": 3.061997719047996e-16, "-18": 1.5647037520964625e-17, "-2": 0.04985287749865131, "-3": 0.014663907430878637, "-4": 0.00344319662713164, "-5": 0.0006693276882095778, "-6": 0.0001106953400627468, "-7": 1.5903978712846816e-05, "-8": 2.017801325837055e-06, "-9": 2.2905577892496453e-07, "0": 0.2058512207949676, "1": 0.19436218717330467, "10": 6.739572814304749e-05, "11": 1.4580803911515298e-05, "12": 2.899833563797264e-06, "13": 5.335510201822267e-07, "14": 9.13222536208971e-08, "15": 1.460985720153173e-08, "16": 2.1930351145493052e-09, "17": 3.07729010436564e-10, "18": 3.632026593020064e-11, "2": 0.17642252528895191, "3": 0.119857946321087, "4": 0.06500282992015328, "5": 0.029185191625728635, "6": 0.011148242711785468, "7": 0.003699441639804458, "8": 0.001084081956595231, "9": 0.0002842354775590988} |
| Raw goal margin distribution | {"-1": 0.092303162116151, "-10": 1.7467584449442247e-08, "-11": 1.6361707820355925e-09, "-12": 1.4088570109287988e-10, "-13": 1.1223194299920167e-11, "-14": 8.316944991673205e-13, "-15": 5.760761050491964e-14, "-16": 3.743916531279225e-15, "-17": 2.2745510795669376e-16, "-18": 1.1623126256410057e-17, "-2": 0.03703233207153746, "-3": 0.0108928253832745, "-4": 0.0025577179749952483, "-5": 0.0004971982853973101, "-6": 8.22280838671008e-05, "-7": 1.1813990495708888e-05, "-8": 1.4988881786173304e-06, "-9": 1.7015005138436465e-07, "0": 0.1834837334581747, "1": 0.21764337004944523, "10": 7.546855493507099e-05, "11": 1.6327328620266657e-05, "12": 3.247182790984841e-06, "13": 5.974610793108464e-07, "14": 1.0226105873587373e-07, "15": 1.635986198512616e-08, "16": 2.45572227761408e-09, "17": 3.4458955143201653e-10, "18": 4.0670797098473055e-11, "2": 0.19755485115159663, "3": 0.13421482719407155, "4": 0.07278902945231006, "5": 0.03268106596937318, "6": 0.012483606761219906, "7": 0.004142569897458303, "8": 0.0012139359711609015, "9": 0.0003182819051548127} |
| Unadjusted home-win probability | 67.3% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 14.3% |
| Raw p over 1 5 | 86.5% |
| Raw p under 3 5 | 54.2% |
| Raw p btts yes | 59.6% |
| P home draw | 80.7% |
| P draw away | 39.9% |
| P home away | 79.4% |
| Raw p home draw | 85.7% |
| Raw p draw away | 32.7% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.06, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 3.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.46, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.39, "price": 1.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.63, "price": 2.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.85 |
| Reference draw odds | 4.17 |
| Reference away odds | 3.93 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | +7.2% |
| Draw probability edge | -2.2% |
| Away probability edge | -5.0% |
| Over 2.5 probability edge | -2.4% |
| Under 2.5 probability edge | +2.4% |
| Raw edge prob home | 0.1440 |
| Raw ev home | 0.2453 |
| Raw edge prob draw | -0.0447 |
| Raw ev draw | -0.2349 |
| Raw edge prob away | -0.0993 |
| Raw ev away | -0.4365 |
| Market p home draw | 75.7% |
| Market home draw odds | 1.28 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 47.5% |
| Market draw away odds | 2.04 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.9% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 2.04 |
| Market reference dc home draw odds | 1.28 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 87.5% |
| Market reference over 1 5 odds | 1.13 |
| Market reference over 1 5 opposite odds | 6.70 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.9% |
| Market under 3 5 odds | 1.83 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.84 |
| Market reference under 3 5 opposite odds | 2.06 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 68.2% |
| Market btts yes odds | 1.43 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 1.43 |
| Market reference btts yes opposite odds | 2.92 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,513.0173 |
| Elo away rating | 1,441.1854 |
| Elo rating diff | 131.8319 |
| Elo home expectancy | 0.6811 |

</details>


---

## 2026-10-25 — Genoa vs Venezia

The model's most likely 1X2 outcome is **Genoa win** at **46.1%**. Expected goals are 1.34 for Genoa and 0.86 for Venezia (2.20 combined). The most likely exact score is 1-0 at 13.9%. Goal-market probabilities: at least one goal: 88.2%; Over 2.5 goals: 37.5%; Under 3.5 goals: 82.1%; Double Chance 1X: 75.6%; Double Chance X2: 53.9%; Double Chance 12 (either team wins): 70.5%; Under 4.5 goals: 92.8%; BTTS Yes (both teams score): 43.1%; BTTS No (at least one team does not score): 56.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Genoa win | 46.1% | 2.17 |
| Draw | 29.5% | 3.39 |
| Venezia win | 24.4% | 4.09 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Genoa expected goals | 1.34 |
| Venezia expected goals | 0.86 |
| Expected total goals | 2.20 |
| Over 0.5 | 88.2% |
| Under 0.5 | 11.8% |
| Over 1.5 | 64.9% |
| Under 1.5 | 35.1% |
| Over 2.5 | 37.5% |
| Under 2.5 | 62.5% |
| Over 3.5 | 17.9% |
| Under 3.5 | 82.1% |
| Over 4.5 | 7.2% |
| Under 4.5 | 92.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 13.90% |
| 2 | 1-1 | 13.48% |
| 3 | 0-0 | 11.81% |
| 4 | 2-0 | 9.69% |
| 5 | 0-1 | 9.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Genoa win | 46.1% | 44.5% | 2.20 | +1.3% |
| Draw | 29.5% | 29.9% | 3.23 | -4.7% |
| Venezia win | 24.4% | 25.6% | 3.69 | -9.9% |
| Over 2.5 | 37.5% | 47.6% | 2.02 | -24.3% |
| Under 2.5 | 62.5% | 52.4% | 1.87 | +16.9% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.3429 |
| Dc lambda away | 0.8551 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 43.1% |
| P btts no | 56.9% |
| Fair Over 0.5 odds | 1.13 |
| Fair Under 0.5 odds | 8.47 |
| Fair Over 1.5 odds | 1.54 |
| Fair Under 1.5 odds | 2.85 |
| Fair Over 2.5 odds | 2.67 |
| Fair Under 2.5 odds | 1.60 |
| Fair Over 3.5 odds | 5.58 |
| Fair Under 3.5 odds | 1.22 |
| Fair Over 4.5 odds | 13.95 |
| Fair Under 4.5 odds | 1.08 |
| Goal margin distribution | {"-1": 0.1629877854953101, "-10": 7.4363902681442554e-09, "-11": 5.730970306507241e-10, "-12": 4.053583157978883e-11, "-13": 2.6419318473623126e-12, "-14": 1.4912571578113192e-13, "-2": 0.06137642189014711, "-3": 0.016039126111373952, "-4": 0.0032487632157008227, "-5": 0.0005356084030722454, "-6": 7.433694896002945e-05, "-7": 8.90063299491705e-06, "-8": 9.365658277870121e-07, "-9": 8.786984525976309e-08, "0": 0.29512712929995644, "1": 0.23929368202439638, "10": 6.267512539540153e-07, "11": 7.586070259163274e-08, "12": 8.42720296670012e-09, "13": 8.62624208363173e-10, "14": 7.647301935843548e-11, "2": 0.13972988019613208, "3": 0.057348767276441094, "4": 0.018243875875806552, "5": 0.004723915236642662, "6": 0.0010297104286443061, "7": 0.0001936363722228874, "8": 3.2000739618607054e-05, "9": 4.71538583578593e-06} |
| Raw goal margin distribution | {"-1": 0.1554324252428271, "-10": 7.091673593314011e-09, "-11": 5.465309017040915e-10, "-12": 3.865677782254826e-11, "-13": 2.5194641004163023e-12, "-14": 1.4221293699705388e-13, "-2": 0.05853129471095865, "-3": 0.015295626372800452, "-4": 0.0030981655718648614, "-5": 0.0005107800735923999, "-6": 7.089103166164623e-05, "-7": 8.488040796382823e-06, "-8": 8.931509657003102e-07, "-9": 8.379660545071895e-08, "0": 0.2911302533589747, "1": 0.24725290662766794, "10": 6.475978302547364e-07, "11": 7.838392997223374e-08, "12": 8.707502891971378e-09, "13": 8.913162313388645e-10, "14": 7.901661320518846e-11, "2": 0.14437748096377737, "3": 0.05925626318528588, "4": 0.018850691335794117, "5": 0.00488103891018546, "6": 0.0010639599604688676, "7": 0.00020007697426823316, "8": 3.30651265758412e-05, "9": 4.872225810166361e-06} |
| Unadjusted home-win probability | 47.6% |
| Unadjusted draw probability | 29.1% |
| Unadjusted away-win probability | 23.3% |
| Raw p over 1 5 | 65.0% |
| Raw p under 3 5 | 82.0% |
| Raw p btts yes | 43.0% |
| P home draw | 75.6% |
| P draw away | 53.9% |
| P home away | 70.5% |
| Raw p home draw | 76.7% |
| Raw p draw away | 52.4% |
| Raw p home away | 70.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.69, "price": 1.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.55, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.79, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.66, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.41, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.14, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.2, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 2.58, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.53, "price": 2.58, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 2.19 |
| Reference draw odds | 3.22 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 2.00 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market best over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market best under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | +1.5% |
| Draw probability edge | -0.4% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -10.1% |
| Under 2.5 probability edge | +10.1% |
| Raw edge prob home | 0.0306 |
| Raw ev home | 0.0470 |
| Raw edge prob draw | -0.0080 |
| Raw ev draw | -0.0596 |
| Raw edge prob away | -0.0226 |
| Raw ev away | -0.1404 |
| Market p home draw | 73.8% |
| Market home draw odds | 1.31 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 56.2% |
| Market draw away odds | 1.72 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.0% |
| Market home away odds | 1.38 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.72 |
| Market reference dc home draw odds | 1.31 |
| Market reference dc home away odds | 1.38 |
| Market p over 1 5 | 73.9% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.55 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.4% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.50 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.9% |
| Market btts yes odds | 1.76 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 1.76 |
| Market reference btts yes opposite odds | 2.12 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,396.1582 |
| Elo away rating | 1,364.9563 |
| Elo rating diff | 91.2019 |
| Elo home expectancy | 0.6283 |

</details>


---

## 2026-10-25 — Inter Milan vs Fiorentina

The model's most likely 1X2 outcome is **Inter Milan win** at **69.8%**. Expected goals are 2.24 for Inter Milan and 0.93 for Fiorentina (3.17 combined). The most likely exact score is 2-0 at 11.0%. Goal-market probabilities: at least one goal: 95.9%; Over 2.5 goals: 62.3%; Under 3.5 goals: 60.4%; Double Chance 1X: 87.4%; Double Chance X2: 30.2%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 78.1%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Inter Milan win | 69.8% | 1.43 |
| Draw | 17.6% | 5.68 |
| Fiorentina win | 12.6% | 7.92 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Inter Milan expected goals | 2.24 |
| Fiorentina expected goals | 0.93 |
| Expected total goals | 3.17 |
| Over 0.5 | 95.9% |
| Under 0.5 | 4.1% |
| Over 1.5 | 83.2% |
| Under 1.5 | 16.8% |
| Over 2.5 | 62.3% |
| Under 2.5 | 37.7% |
| Over 3.5 | 39.6% |
| Under 3.5 | 60.4% |
| Over 4.5 | 21.9% |
| Under 4.5 | 78.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.02% |
| 2 | 2-1 | 10.29% |
| 3 | 1-0 | 9.45% |
| 4 | 1-1 | 8.25% |
| 5 | 3-0 | 8.22% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Inter Milan win | 69.8% | 73.0% | 1.34 | -6.5% |
| Draw | 17.6% | 15.7% | 5.81 | +2.3% |
| Fiorentina win | 12.6% | 11.3% | 8.14 | +2.8% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Inter |
| Matched away-team name | Fiorentina |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2371 |
| Dc lambda away | 0.9335 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.21 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.96 |
| Fair Over 2.5 odds | 1.61 |
| Fair Under 2.5 odds | 2.65 |
| Fair Over 3.5 odds | 2.53 |
| Fair Under 3.5 odds | 1.66 |
| Fair Over 4.5 odds | 4.56 |
| Fair Under 4.5 odds | 1.28 |
| Goal margin distribution | {"-1": 0.0842488119686025, "-10": 6.335205887365079e-09, "-11": 5.293584710525195e-10, "-12": 4.064137220575222e-11, "-13": 2.8855501234375552e-12, "-14": 1.905224565115068e-13, "-15": 1.1752053535185415e-14, "-16": 6.762012937999889e-16, "-17": 3.3068814752055524e-17, "-2": 0.031462940976700375, "-3": 0.008450643026242384, "-4": 0.0017962735799044486, "-5": 0.0003144728557490183, "-6": 4.668620239323807e-05, "-7": 6.0080139781728206e-06, "-8": 6.81721292653257e-07, "-9": 6.91342934398501e-08, "0": 0.17609508875955296, "1": 0.24014690956113288, "10": 4.599811217882966e-05, "11": 9.210996175609421e-06, "12": 1.6947379626252182e-06, "13": 2.8836349314739627e-07, "14": 4.562840501702296e-08, "15": 6.74497488316935e-09, "16": 9.300794166734246e-10, "17": 1.0900342028379849e-10, "2": 0.20997080257784398, "3": 0.13515334831270684, "4": 0.06884731303991452, "5": 0.028885183970036813, "6": 0.010276801830898614, "7": 0.003169405653271303, "8": 0.0008618490611423465, "9": 0.00020945722377636503} |
| Raw goal margin distribution | {"-1": 0.09332086923682026, "-10": 7.017391775488286e-09, "-11": 5.863607035183537e-10, "-12": 4.501770520670829e-11, "-13": 3.19627113372188e-12, "-14": 2.1103824297741043e-13, "-15": 1.3017534913487767e-14, "-16": 7.490158144899973e-16, "-17": 3.6629721715758884e-17, "-2": 0.03485092468469088, "-3": 0.009360622831250281, "-4": 0.0019896994147085376, "-5": 0.00034833583482245944, "-6": 5.171345312651728e-05, "-7": 6.654967277627646e-06, "-8": 7.551302163330192e-07, "-9": 7.657879330434467e-08, "0": 0.19509844485587535, "1": 0.22892188842133962, "10": 4.384805418915352e-05, "11": 8.780452942807791e-06, "12": 1.6155219964833117e-06, "13": 2.748847175410829e-07, "14": 4.3495627993878514e-08, "15": 6.4296991805200235e-09, "16": 8.866053568451091e-10, "17": 1.0390834869103277e-10, "2": 0.20015628236609972, "3": 0.12883596869413724, "4": 0.06562923063484291, "5": 0.02753502376483983, "6": 0.009796440380434321, "7": 0.0030212603137224126, "8": 0.0008215642457003595, "9": 0.0001996667094238429} |
| Unadjusted home-win probability | 66.5% |
| Unadjusted draw probability | 19.5% |
| Unadjusted away-win probability | 14.0% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 60.9% |
| Raw p btts yes | 54.6% |
| P home draw | 87.4% |
| P draw away | 30.2% |
| P home away | 82.4% |
| Raw p home draw | 86.0% |
| Raw p draw away | 33.5% |
| Raw p home away | 80.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.09, "price": 1.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.63, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.95, "price": 1.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.95, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 5.51, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.28, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.26, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:16Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 6.7, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.13, "price": 6.7, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 1.35 |
| Reference draw odds | 5.85 |
| Reference away odds | 8.03 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.75 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | -3.3% |
| Draw probability edge | +1.9% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | -0.0652 |
| Raw ev home | -0.1089 |
| Raw edge prob draw | 0.0380 |
| Raw ev draw | 0.1335 |
| Raw edge prob away | 0.0272 |
| Raw ev away | 0.1390 |
| Market p home draw | 88.2% |
| Market home draw odds | 1.10 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.2% |
| Market draw away odds | 3.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 83.6% |
| Market home away odds | 1.16 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.44 |
| Market reference dc home draw odds | 1.10 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 86.9% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.60 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 53.5% |
| Market under 3 5 odds | 1.81 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.82 |
| Market reference under 3 5 opposite odds | 2.08 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 58.2% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 1.67 |
| Market reference btts yes opposite odds | 2.28 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,671.4331 |
| Elo away rating | 1,448.7633 |
| Elo rating diff | 282.6699 |
| Elo home expectancy | 0.8358 |

</details>


---

## 2026-10-25 — Lecce vs Juventus

The model's most likely 1X2 outcome is **Juventus win** at **61.7%**. Expected goals are 0.61 for Lecce and 1.42 for Juventus (2.03 combined). The most likely exact score is 0-1 at 19.9%. Goal-market probabilities: at least one goal: 87.9%; Over 2.5 goals: 34.4%; Under 3.5 goals: 84.7%; Double Chance 1X: 38.3%; Double Chance X2: 86.6%; Double Chance 12 (either team wins): 75.1%; Under 4.5 goals: 94.2%; BTTS Yes (both teams score): 34.1%; BTTS No (at least one team does not score): 65.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Lecce win | 13.4% | 7.46 |
| Draw | 24.9% | 4.02 |
| Juventus win | 61.7% | 1.62 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Lecce expected goals | 0.61 |
| Juventus expected goals | 1.42 |
| Expected total goals | 2.03 |
| Over 0.5 | 87.9% |
| Under 0.5 | 12.1% |
| Over 1.5 | 61.5% |
| Under 1.5 | 38.5% |
| Over 2.5 | 34.4% |
| Under 2.5 | 65.6% |
| Over 3.5 | 15.3% |
| Under 3.5 | 84.7% |
| Over 4.5 | 5.8% |
| Under 4.5 | 94.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.92% |
| 2 | 0-2 | 14.54% |
| 3 | 0-0 | 12.06% |
| 4 | 1-1 | 10.44% |
| 5 | 1-2 | 8.80% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Lecce win | 13.4% | 11.5% | 7.63 | +2.3% |
| Draw | 24.9% | 21.6% | 4.20 | +4.4% |
| Juventus win | 61.7% | 66.9% | 1.50 | -7.4% |

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
| Market best home last update utc | 2026-10-24T14:48:14Z |
| Market best draw last update utc | 2026-10-24T14:48:14Z |
| Market best away last update utc | 2026-10-24T14:48:14Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 16.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Lecce |
| Matched away-team name | Juventus |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.6053 |
| Dc lambda away | 1.4221 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 34.1% |
| P btts no | 65.9% |
| Fair Over 0.5 odds | 1.14 |
| Fair Under 0.5 odds | 8.29 |
| Fair Over 1.5 odds | 1.63 |
| Fair Under 1.5 odds | 2.60 |
| Fair Over 2.5 odds | 2.91 |
| Fair Under 2.5 odds | 1.52 |
| Fair Over 3.5 odds | 6.55 |
| Fair Under 3.5 odds | 1.18 |
| Fair Over 4.5 odds | 17.21 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.30080930410464024, "-10": 1.449865837624534e-06, "-11": 1.8623711086867568e-07, "-12": 2.1949748003292136e-08, "-13": 2.3859750400288044e-09, "-14": 2.2832872677788168e-10, "-2": 0.19192709976092656, "-3": 0.08512057424398449, "-4": 0.029047029093341486, "-5": 0.008035699463543123, "-6": 0.0018669401682048802, "-7": 0.0003736138601136397, "-8": 6.563848079005433e-05, "-9": 1.0274306744846276e-05, "0": 0.24866553301053335, "1": 0.10010167733577476, "10": 2.2676885943317161e-10, "11": 1.2398988172223619e-11, "12": 6.220337940611767e-13, "13": 2.8781588427713456e-14, "14": 1.1723946785609456e-15, "2": 0.027853291850969217, "3": 0.005258225356832964, "4": 0.0007637844130395387, "5": 8.994088951835548e-05, "6": 8.894638742666152e-06, "7": 7.576791113230229e-07, "8": 5.666113595026909e-08, "9": 3.775232518809414e-09} |
| Raw goal margin distribution | {"-1": 0.27539094915664974, "-10": 1.3273523249610896e-06, "-11": 1.705000943470673e-07, "-12": 2.0094996577210778e-08, "-13": 2.184360397007654e-09, "-14": 2.0903497308453178e-10, "-2": 0.1757092797690138, "-3": 0.0779278945629141, "-4": 0.02659255815243495, "-5": 0.007356683693643056, "-6": 0.001709183917934161, "-7": 0.00034204352774601523, "-8": 6.009203598199058e-05, "-9": 9.406128892228431e-06, "0": 0.28165052185185363, "1": 0.11441642290248455, "10": 2.5919727233928294e-10, "11": 1.4172068960617099e-11, "12": 7.109859048835861e-13, "13": 3.289741471868046e-14, "14": 1.340049526851551e-15, "2": 0.03183636982382395, "3": 0.006010162388447371, "4": 0.0008730071536716016, "5": 0.00010280262154688252, "6": 1.01665903612387e-05, "7": 8.660287812633055e-07, "8": 6.476379482908276e-08, "9": 4.315098527054732e-09} |
| Unadjusted home-win probability | 15.3% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 56.5% |
| Raw p over 1 5 | 60.6% |
| Raw p under 3 5 | 85.2% |
| Raw p btts yes | 34.9% |
| P home draw | 38.3% |
| P draw away | 86.6% |
| P home away | 75.1% |
| Raw p home draw | 43.5% |
| Raw p draw away | 84.7% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.36, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:47:52Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.69, "price": 2.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:04Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 5.87, "price": 1.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:04Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 4.25, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.79, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.75, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.43, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.41, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.12, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.12, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:14Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.25, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 7.98 |
| Reference draw odds | 4.36 |
| Reference away odds | 1.47 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.85 |
| Reference Under 2.5 odds | 1.98 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:18Z |
| Home probability edge | +1.9% |
| Draw probability edge | +3.3% |
| Away probability edge | -5.2% |
| Over 2.5 probability edge | -17.4% |
| Under 2.5 probability edge | +17.4% |
| Raw edge prob home | 0.0383 |
| Raw ev home | 0.1693 |
| Raw edge prob draw | 0.0660 |
| Raw ev draw | 0.1829 |
| Raw edge prob away | -0.1043 |
| Raw ev away | -0.1524 |
| Market p home draw | 36.2% |
| Market home draw odds | 2.79 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:04Z |
| Market reference home draw last update utc | 2026-10-24T14:48:15Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 86.2% |
| Market draw away odds | 1.12 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:04Z |
| Market reference draw away last update utc | 2026-10-24T14:48:15Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.7% |
| Market home away odds | 1.24 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:04Z |
| Market reference home away last update utc | 2026-10-24T14:48:15Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.10 |
| Market reference dc home draw odds | 2.62 |
| Market reference dc home away odds | 1.22 |
| Market p over 1 5 | 77.5% |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.05 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:17Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 69.1% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:14Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:17Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 48.0% |
| Market btts yes odds | 2.04 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:04Z |
| Market reference btts yes odds | 2.04 |
| Market reference btts yes opposite odds | 1.89 |
| Market reference btts yes last update utc | 2026-10-24T14:48:16Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,374.5856 |
| Elo away rating | 1,557.5355 |
| Elo rating diff | -122.9499 |
| Elo home expectancy | 0.3301 |

</details>


---

## 2026-10-25 — Udinese vs AC Milan

The model's most likely 1X2 outcome is **AC Milan win** at **52.8%**. Expected goals are 1.07 for Udinese and 1.71 for AC Milan (2.78 combined). The most likely exact score is 1-1 at 12.0%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 52.5%; Under 3.5 goals: 69.6%; Double Chance 1X: 47.2%; Double Chance X2: 78.0%; Double Chance 12 (either team wins): 74.7%; Under 4.5 goals: 85.1%; BTTS Yes (both teams score): 54.3%; BTTS No (at least one team does not score): 45.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Udinese win | 22.0% | 4.55 |
| Draw | 25.3% | 3.96 |
| AC Milan win | 52.8% | 1.89 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Udinese expected goals | 1.07 |
| AC Milan expected goals | 1.71 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 77.1% |
| Under 1.5 | 22.9% |
| Over 2.5 | 52.5% |
| Under 2.5 | 47.5% |
| Over 3.5 | 30.4% |
| Under 3.5 | 69.6% |
| Over 4.5 | 14.9% |
| Under 4.5 | 85.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.01% |
| 2 | 0-1 | 10.32% |
| 3 | 1-2 | 9.89% |
| 4 | 0-2 | 9.23% |
| 5 | 0-0 | 6.79% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Udinese win | 22.0% | 20.6% | 4.57 | +0.3% |
| Draw | 25.3% | 25.6% | 3.70 | -6.5% |
| AC Milan win | 52.8% | 53.8% | 1.83 | -3.4% |
| Over 2.5 | 52.5% | 50.6% | 1.95 | +2.3% |
| Under 2.5 | 47.5% | 49.4% | 1.93 | -8.3% |

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
| Market best home last update utc | 2026-10-24T14:48:15Z |
| Market best draw last update utc | 2026-10-24T14:48:15Z |
| Market best away last update utc | 2026-10-24T14:48:15Z |
| Odds bookmakers 1x2 | 1.00 |
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
| Dc lambda home | 1.0715 |
| Dc lambda away | 1.7067 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-24T14:48:23.942089+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 54.3% |
| P btts no | 45.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.72 |
| Fair Over 1.5 odds | 1.30 |
| Fair Under 1.5 odds | 4.36 |
| Fair Over 2.5 odds | 1.91 |
| Fair Under 2.5 odds | 2.10 |
| Fair Over 3.5 odds | 3.29 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.71 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.23728054123011116, "-10": 4.319133296542571e-06, "-11": 6.610629730510022e-07, "-12": 9.293774421241322e-08, "-13": 1.2077454284681094e-08, "-14": 1.4507344957984244e-09, "-15": 1.471237993456535e-10, "-2": 0.1631374683540612, "-3": 0.0813895438231892, "-4": 0.031964773491580674, "-5": 0.010307690783244658, "-6": 0.002813240047028173, "-7": 0.0006647116426405173, "-8": 0.00013835907368290966, "-9": 2.5722608099368795e-05, "0": 0.2526991441929699, "1": 0.13587344125765966, "10": 3.7969868402636085e-08, "11": 3.648735814139462e-09, "12": 3.220689197272241e-10, "13": 2.6277811580096208e-11, "14": 1.9817954746768653e-12, "15": 1.2618592877558458e-13, "2": 0.05939356352894533, "3": 0.018604216357414285, "4": 0.004587451660007826, "5": 0.0009287917603384166, "6": 0.00015915521208879132, "7": 2.3610460776106417e-05, "8": 3.0855737083521638e-06, "9": 3.6016406809535066e-07} |
| Raw goal margin distribution | {"-1": 0.23266146889462033, "-10": 4.235053965722057e-06, "-11": 6.481942494927736e-07, "-12": 9.11285517645666e-08, "-13": 1.184234594128169e-08, "-14": 1.4224934628804065e-09, "-15": 1.4425978248221098e-10, "-2": 0.15996171798258227, "-3": 0.07980515688474522, "-4": 0.03134252440120118, "-5": 0.01010703391904143, "-6": 0.002758475508785988, "-7": 0.000651771891476422, "-8": 0.00013566567722359747, "-9": 2.522187345483155e-05, "0": 0.24943042885300842, "1": 0.14425320018633844, "10": 4.0311594208817583e-08, "11": 3.8737652697410476e-09, "12": 3.419319619873831e-10, "13": 2.789845005201712e-11, "14": 2.1040192747810113e-12, "15": 1.3396822716696516e-13, "2": 0.06305655859023859, "3": 0.019751599147524675, "4": 0.0048703747879717, "5": 0.000986073381930822, "6": 0.0001689708338703705, "7": 2.5066595011520456e-05, "8": 3.2758711174214506e-06, "9": 3.823765625863677e-07} |
| Unadjusted home-win probability | 23.3% |
| Unadjusted draw probability | 24.9% |
| Unadjusted away-win probability | 51.7% |
| Raw p over 1 5 | 77.0% |
| Raw p under 3 5 | 69.7% |
| Raw p btts yes | 54.3% |
| P home draw | 47.2% |
| P draw away | 78.0% |
| P home away | 74.7% |
| Raw p home draw | 48.3% |
| Raw p draw away | 76.7% |
| Raw p home away | 75.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.19, "price": 1.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 4.16, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.96, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.09, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 2.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:15Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 8.5, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.99, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.4, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.99, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:48:20Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 3.38, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-24T14:48:29Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 1.35, "price": 3.38, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / BetAnything |
| Reference home odds | 4.60 |
| Reference draw odds | 3.73 |
| Reference away odds | 1.82 |
| Market reference 1x2 last update utc | 2026-10-24T14:48:18Z |
| Market reference home last update utc | 2026-10-24T14:48:18Z |
| Market reference draw last update utc | 2026-10-24T14:48:18Z |
| Market reference away last update utc | 2026-10-24T14:48:18Z |
| O/U 2.5 market source | The Odds API / BetAnything |
| Reference Over 2.5 odds | 1.89 |
| Reference Under 2.5 odds | 1.93 |
| Market reference over 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:48:18Z |
| Market best over 2 5 last update utc | 2026-10-24T14:48:15Z |
| Market best under 2 5 last update utc | 2026-10-24T14:48:15Z |
| Home probability edge | +1.4% |
| Draw probability edge | -0.3% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +1.9% |
| Under 2.5 probability edge | -1.9% |
| Raw edge prob home | 0.0271 |
| Raw ev home | 0.0653 |
| Raw edge prob draw | -0.0065 |
| Raw ev draw | -0.0771 |
| Raw edge prob away | -0.0205 |
| Raw ev away | -0.0531 |
| Market p home draw | 47.1% |
| Market home draw odds | 2.06 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-24T14:48:29Z |
| Market reference home draw last update utc | 2026-10-24T14:48:29Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.9% |
| Market draw away odds | 1.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-24T14:48:29Z |
| Market reference draw away last update utc | 2026-10-24T14:48:29Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.0% |
| Market home away odds | 1.31 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-24T14:48:29Z |
| Market reference home away last update utc | 2026-10-24T14:48:29Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.23 |
| Market reference dc home draw odds | 2.06 |
| Market reference dc home away odds | 1.31 |
| Market p over 1 5 | 75.1% |
| Market over 1 5 odds | 1.30 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market reference over 1 5 last update utc | 2026-10-24T14:48:20Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.0% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-24T14:48:15Z |
| Market reference under 3 5 odds | 1.35 |
| Market reference under 3 5 opposite odds | 3.21 |
| Market reference under 3 5 last update utc | 2026-10-24T14:48:20Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.4% |
| Market btts yes odds | 1.81 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-24T14:48:29Z |
| Market reference btts yes odds | 1.81 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-24T14:48:29Z |
| Market btts yes bookmakers | 1 |
| Elo home rating | 1,386.6713 |
| Elo away rating | 1,580.4486 |
| Elo rating diff | -133.7773 |
| Elo home expectancy | 0.3165 |

</details>


---
