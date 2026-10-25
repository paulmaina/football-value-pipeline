# Ligue 1 — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Ligue 1 |
| Training matches | 1,745 |
| Training data through | 2026-10-24 |
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
| Training sha256 | 0f4a83176017e5370c37b2f2572ba1a846251ca1c6772be9fcb10fbee84dd50e |
| Training as of utc | 2026-10-25T10:22:57.997574+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 65, 'bbs_added_results': 2, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 65, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 752, 'added_results': 2, 'conflicts': 0, 'unmapped': 242, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 66, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-25T10:22:57.997574+00:00', 'observations': 254, 'observations_sha256': 'bcf4d1aff1b290d0c16ed4473ca166f5b9bea74fc3bf249654b607892c4c7a5d', 'eligible_training_matches': 93, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 104, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 9, 'retrospective_eligible_training_matches': 93, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:29.253586+00:00', 'retrospective_inputs_sha256': '343e0ceb939f29bb74990d53890f933e8b010c52e7d393a1c0611d87ee68c4cb', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 5084.311 |
| Base scoring parameter | 0.216 |
| Home-advantage parameter | 0.187 |
| Dixon-Coles low-score adjustment | -0.057 |
| Xi per day | 0 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 26, 'matches': 1745, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-24'} |
| Training data health | {'training_end': '2026-10-24', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 7.00 |
| Additional event odds calls used before this league | 17.00 |
| Bbs statistics model artifact | bbs/feature_models/Ligue1/20261025T102257997574Z_9fbef83d8799904dbbfa2933150f06d149ef22760588983da82d9829d2a1526d.json |
| Over 1 5 in window quote fixtures | 2 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 7.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 7.00 |
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

## 2026-10-24 — RC Lens vs Paris FC

The model's most likely 1X2 outcome is **RC Lens win** at **52.2%**. Expected goals are 1.69 for RC Lens and 1.02 for Paris FC (2.71 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 50.9%; Under 3.5 goals: 71.1%; Double Chance 1X: 77.7%; Double Chance X2: 47.8%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 52.9%; BTTS No (at least one team does not score): 47.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RC Lens win | 52.2% | 1.91 |
| Draw | 25.5% | 3.93 |
| Paris FC win | 22.3% | 4.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RC Lens expected goals | 1.69 |
| Paris FC expected goals | 1.02 |
| Expected total goals | 2.71 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 76.0% |
| Under 1.5 | 24.0% |
| Over 2.5 | 50.9% |
| Under 2.5 | 49.1% |
| Over 3.5 | 28.9% |
| Under 3.5 | 71.1% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.13% |
| 2 | 1-0 | 10.55% |
| 3 | 2-1 | 9.69% |
| 4 | 2-0 | 9.45% |
| 5 | 0-0 | 7.29% |

### Market comparison

_No bookmaker prices were available in this run. This commonly occurs when the schedule fallback supplies fixtures before Football-Data publishes its next odds update. Match probabilities and scoreline estimates are still available._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T18:45:00+00:00 |
| Fixture id | fc6c50376190b578cfeb38c029db8487 |
| Matched home-team name | Lens |
| Matched away-team name | Paris FC |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6875 |
| Dc lambda away | 1.0250 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 52.9% |
| P btts no | 47.1% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.72 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.17 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.46 |
| Fair Under 3.5 odds | 1.41 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1399631756319283, "-10": 2.7364792396164953e-08, "-11": 2.5172035325688278e-09, "-12": 2.126675799228433e-10, "-13": 1.6607226444931368e-11, "-14": 1.1993355622075166e-12, "-15": 7.34794540101295e-14, "-2": 0.05985053365657297, "-3": 0.018044469051974318, "-4": 0.004273590787238913, "-5": 0.0008300451762194943, "-6": 0.0001363449370439642, "-7": 1.937945933827506e-05, "-8": 2.4257330151695907e-06, "-9": 2.711253803554879e-07, "0": 0.2545203446983996, "1": 0.23465371619007133, "10": 4.004063787664418e-06, "11": 6.063983980346275e-07, "12": 8.434743586987192e-08, "13": 1.0844226654798986e-08, "14": 1.2893566754548337e-09, "15": 1.3005563242957738e-10, "2": 0.1622294863399806, "3": 0.08052611679695006, "4": 0.03139904696162992, "5": 0.010040518597901523, "6": 0.0027153406020841335, "7": 0.0006354155481459343, "8": 0.00013094534462904653, "9": 2.4096175691913455e-05} |
| Raw goal margin distribution | {"-1": 0.1399631756319283, "-10": 2.7364792396164953e-08, "-11": 2.5172035325688278e-09, "-12": 2.126675799228433e-10, "-13": 1.6607226444931368e-11, "-14": 1.1993355622075166e-12, "-15": 7.34794540101295e-14, "-2": 0.05985053365657297, "-3": 0.018044469051974318, "-4": 0.004273590787238913, "-5": 0.0008300451762194943, "-6": 0.0001363449370439642, "-7": 1.937945933827506e-05, "-8": 2.4257330151695907e-06, "-9": 2.711253803554879e-07, "0": 0.2545203446983996, "1": 0.23465371619007133, "10": 4.004063787664418e-06, "11": 6.063983980346275e-07, "12": 8.434743586987192e-08, "13": 1.0844226654798986e-08, "14": 1.2893566754548337e-09, "15": 1.3005563242957738e-10, "2": 0.1622294863399806, "3": 0.08052611679695006, "4": 0.03139904696162992, "5": 0.010040518597901523, "6": 0.0027153406020841335, "7": 0.0006354155481459343, "8": 0.00013094534462904653, "9": 2.4096175691913455e-05} |
| Unadjusted home-win probability | 52.2% |
| Unadjusted draw probability | 25.5% |
| Unadjusted away-win probability | 22.3% |
| Raw p over 1 5 | 76.0% |
| Raw p under 3 5 | 71.1% |
| Raw p btts yes | 52.9% |
| P home draw | 77.7% |
| P draw away | 47.8% |
| P home away | 74.5% |
| Raw p home draw | 77.7% |
| Raw p draw away | 47.8% |
| Raw p home away | 74.5% |
| Market blending weight | 0.0% |
| Market blend applied | No |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.785800972762825, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,581.0094 |
| Elo away rating | 1,490.2537 |
| Elo rating diff | 150.7557 |
| Elo home expectancy | 0.7043 |

</details>


---

## 2026-10-25 — AS Monaco vs Lille

The model's most likely 1X2 outcome is **AS Monaco win** at **46.6%**. Expected goals are 1.56 for AS Monaco and 1.26 for Lille (2.82 combined). The most likely exact score is 1-1 at 12.4%. Goal-market probabilities: at least one goal: 93.4%; Over 2.5 goals: 53.6%; Under 3.5 goals: 68.6%; Double Chance 1X: 72.9%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.2%; BTTS No (at least one team does not score): 42.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| AS Monaco win | 46.6% | 2.14 |
| Draw | 26.2% | 3.81 |
| Lille win | 27.1% | 3.69 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| AS Monaco expected goals | 1.56 |
| Lille expected goals | 1.26 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.4% |
| Under 0.5 | 6.6% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 53.6% |
| Under 2.5 | 46.4% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.41% |
| 2 | 2-1 | 9.78% |
| 3 | 1-0 | 9.22% |
| 4 | 2-0 | 7.74% |
| 5 | 0-0 | 6.63% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| AS Monaco win | 46.6% | 49.8% | 1.98 | -7.6% |
| Draw | 26.2% | 26.3% | 3.52 | -7.6% |
| Lille win | 27.1% | 23.9% | 4.17 | +13.0% |
| Over 2.5 | 53.6% | 52.9% | 1.88 | +0.8% |
| Under 2.5 | 46.4% | 47.1% | 2.03 | -5.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:00:00+00:00 |
| Fixture id | c177a3c900d7febf9870ca8de90a9e35 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Monaco |
| Matched away-team name | Lille |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5576 |
| Dc lambda away | 1.2640 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 57.2% |
| P btts no | 42.8% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.08 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.55 |
| Fair Over 2.5 odds | 1.87 |
| Fair Under 2.5 odds | 2.16 |
| Fair Over 3.5 odds | 3.19 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.40 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.1532950187100995, "-10": 1.8245470408012573e-07, "-11": 2.0661009176862834e-08, "-12": 2.1493937801453923e-09, "-13": 2.0670038917380355e-10, "-14": 1.8359864848850057e-11, "-15": 1.3676008562016348e-12, "-2": 0.07830900918686623, "-3": 0.028686258618577983, "-4": 0.008296283792586805, "-5": 0.0019733783980006646, "-6": 0.0003976936089910814, "-7": 6.943356530690476e-05, "-8": 1.0684326278437534e-05, "-9": 1.4689539323522594e-06, "0": 0.2624679134652084, "1": 0.22797140168634142, "10": 1.7650802032904848e-06, "11": 2.4630622035199474e-07, "12": 3.1575795975366e-08, "13": 3.741916429526624e-09, "14": 4.095781119568535e-10, "15": 3.7595952647402594e-11, "2": 0.1424640698520518, "3": 0.06431051648690121, "4": 0.022919553764596295, "5": 0.006718114448788976, "6": 0.001668399727936576, "7": 0.00035895122090577706, "8": 6.806558490482548e-05, "9": 1.1531958879859378e-05} |
| Raw goal margin distribution | {"-1": 0.17130812553194974, "-10": 2.0389425314309775e-07, "-11": 2.3088804733963607e-08, "-12": 2.401960759097258e-09, "-13": 2.3098895524487084e-10, "-14": 2.051726180499317e-11, "-15": 1.5283023618324303e-12, "-2": 0.08751079903930677, "-3": 0.03205707030680948, "-4": 0.009271148125672963, "-5": 0.002205262487791874, "-6": 0.0004444250522004069, "-7": 7.759243595657965e-05, "-8": 1.1939800280087645e-05, "-9": 1.6415650473283979e-06, "0": 0.26197072150683154, "1": 0.212650110238366, "10": 1.6464543229229412e-06, "11": 2.2975269934213447e-07, "12": 2.9453679037619523e-08, "13": 3.4904331655441325e-09, "14": 3.8205156442684183e-10, "15": 3.506923857925968e-11, "2": 0.1328894762016115, "3": 0.05998839468137179, "4": 0.021379197559882216, "5": 0.0062666096166505625, "6": 0.0015562714596785722, "7": 0.0003348271587189299, "8": 6.349109592862234e-05, "9": 1.0756929636465559e-05} |
| Unadjusted home-win probability | 43.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 30.3% |
| Raw p over 1 5 | 77.9% |
| Raw p under 3 5 | 68.7% |
| Raw p btts yes | 57.3% |
| P home draw | 72.9% |
| P draw away | 53.4% |
| P home away | 73.8% |
| Raw p home draw | 69.7% |
| Raw p draw away | 56.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 7.75, "price": 1.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 6.37, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 7.24, "price": 1.09, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 5.75, "price": 1.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.78, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.93, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.78, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.48, "price": 2.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 5.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 7.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.75, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 4.12, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.12, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.88 |
| Reference draw odds | 3.35 |
| Reference away odds | 3.65 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.70 |
| Reference Under 2.5 odds | 1.87 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:44Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:44Z |
| Market best over 2 5 last update utc | 2026-10-25T10:22:43Z |
| Market best under 2 5 last update utc | 2026-10-25T10:22:43Z |
| Home probability edge | -3.1% |
| Draw probability edge | -0.0% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | +0.8% |
| Under 2.5 probability edge | -0.8% |
| Raw edge prob home | -0.0627 |
| Raw ev home | -0.1384 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.0779 |
| Raw edge prob away | 0.0637 |
| Raw ev away | 0.2630 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.213302300229133, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,571.2442 |
| Elo away rating | 1,580.6904 |
| Elo rating diff | 50.5538 |
| Elo home expectancy | 0.5722 |
| Market p home draw | 76.5% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:22:41Z |
| Market reference home draw last update utc | 2026-10-25T10:22:41Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 50.9% |
| Market draw away odds | 1.91 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:22:41Z |
| Market reference draw away last update utc | 2026-10-25T10:22:41Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.6% |
| Market home away odds | 1.34 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:22:41Z |
| Market reference home away last update utc | 2026-10-25T10:22:41Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.27 |
| Market reference dc draw away odds | 1.91 |
| Market reference dc home away odds | 1.34 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.33, "price": 1.58, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.58, "price": 2.33, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.85, "price": 1.98, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.98, "price": 1.85, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.5, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.5, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 77.4% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference over 1 5 odds | 1.27 |
| Market reference over 1 5 opposite odds | 4.02 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 69.9% |
| Market under 3 5 odds | 1.40 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.40 |
| Market reference under 3 5 opposite odds | 3.09 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.5% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:22:41Z |
| Market reference btts yes odds | 1.72 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-25T10:22:41Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Angers vs Lorient

The model's most likely 1X2 outcome is **Lorient win** at **38.9%**. Expected goals are 1.19 for Angers and 1.30 for Lorient (2.49 combined). The most likely exact score is 1-1 at 13.6%. Goal-market probabilities: at least one goal: 90.9%; Over 2.5 goals: 45.3%; Under 3.5 goals: 76.0%; Double Chance 1X: 61.1%; Double Chance X2: 67.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 89.3%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Angers win | 32.4% | 3.09 |
| Draw | 28.7% | 3.49 |
| Lorient win | 38.9% | 2.57 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Angers expected goals | 1.19 |
| Lorient expected goals | 1.30 |
| Expected total goals | 2.49 |
| Over 0.5 | 90.9% |
| Under 0.5 | 9.1% |
| Over 1.5 | 71.8% |
| Under 1.5 | 28.2% |
| Over 2.5 | 45.3% |
| Under 2.5 | 54.7% |
| Over 3.5 | 24.0% |
| Under 3.5 | 76.0% |
| Over 4.5 | 10.7% |
| Under 4.5 | 89.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.65% |
| 2 | 0-1 | 10.20% |
| 3 | 0-0 | 9.09% |
| 4 | 1-0 | 8.94% |
| 5 | 1-2 | 8.46% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Angers win | 32.4% | 31.7% | 3.20 | +3.7% |
| Draw | 28.7% | 28.9% | 3.35 | -3.9% |
| Lorient win | 38.9% | 39.5% | 2.40 | -6.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 1a83b5ebabe7cb572ae6e029b3149c42 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Angers |
| Matched away-team name | Lorient |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1900 |
| Dc lambda away | 1.2990 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.00 |
| Fair Over 1.5 odds | 1.39 |
| Fair Under 1.5 odds | 3.54 |
| Fair Over 2.5 odds | 2.21 |
| Fair Under 2.5 odds | 1.83 |
| Fair Over 3.5 odds | 4.17 |
| Fair Under 3.5 odds | 1.32 |
| Fair Over 4.5 odds | 9.33 |
| Fair Under 4.5 odds | 1.12 |
| Goal margin distribution | {"-1": 0.21136601548903383, "-10": 3.6500408274871845e-07, "-11": 4.260802822056971e-08, "-12": 4.566398374269081e-09, "-13": 4.5017076402173216e-10, "-14": 3.7615038519304745e-11, "-2": 0.11551556089305469, "-3": 0.04465861485542314, "-4": 0.01350792518370559, "-5": 0.0033429667679084583, "-6": 0.0006986932255448944, "-7": 0.0001262411127775878, "-8": 2.0074010300232334e-05, "-9": 2.8490021883548853e-06, "0": 0.2867192851676823, "1": 0.18588779303610664, "10": 1.463775335993434e-07, "11": 1.5653803587005247e-08, "12": 1.5369296218316512e-09, "13": 1.3880631073990896e-10, "14": 1.0625397260051476e-11, "2": 0.09336912074352832, "3": 0.03306890140247141, "4": 0.009163363306341394, "5": 0.0020775431805300877, "6": 0.0003977922088636711, "7": 6.584492314510622e-05, "8": 9.591960117078848e-06, "9": 1.2471472835966616e-06} |
| Raw goal margin distribution | {"-1": 0.20829148183439544, "-10": 3.596947271557917e-07, "-11": 4.198825111771412e-08, "-12": 4.499975465885758e-09, "-13": 4.436225724351292e-10, "-14": 3.706788952952724e-11, "-2": 0.11383526958047824, "-3": 0.04400900988451591, "-4": 0.013311438674341484, "-5": 0.003294339916470245, "-6": 0.0006885300220079612, "-7": 0.00012440480740495886, "-8": 1.9782013405136286e-05, "-9": 2.8075605540885203e-06, "0": 0.28485079468594615, "1": 0.1902076254199543, "10": 1.4977919004801277e-07, "11": 1.601758114636549e-08, "12": 1.572646213242221e-09, "13": 1.4203202011233782e-10, "14": 1.087232006453225e-11, "2": 0.09553891868911445, "3": 0.03383738710475158, "4": 0.009376310014186845, "5": 0.0021258230496033217, "6": 0.0004070364719636038, "7": 6.737508834137032e-05, "8": 9.814866953840768e-06, "9": 1.2761296451337749e-06} |
| Unadjusted home-win probability | 33.2% |
| Unadjusted draw probability | 28.5% |
| Unadjusted away-win probability | 38.4% |
| Raw p over 1 5 | 71.8% |
| Raw p under 3 5 | 76.0% |
| Raw p btts yes | 51.3% |
| P home draw | 61.1% |
| P draw away | 67.6% |
| P home away | 71.3% |
| Raw p home draw | 61.6% |
| Raw p draw away | 66.8% |
| Raw p home away | 71.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 8.8, "price": 1.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.94, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.25, "price": 1.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.68, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.87, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 5.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:13Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.87, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.41, "price": 1.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.05, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.9, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.17, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.73, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.73, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 4.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.41, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 2.85 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.33 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.92 |
| Reference Under 2.5 odds | 1.66 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:44Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:44Z |
| Home probability edge | +0.8% |
| Draw probability edge | -0.2% |
| Away probability edge | -0.6% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | 0.0151 |
| Raw ev home | 0.0610 |
| Raw edge prob draw | -0.0037 |
| Raw ev draw | -0.0457 |
| Raw edge prob away | -0.0113 |
| Raw ev away | -0.0794 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.677414961429498, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,396.7703 |
| Elo away rating | 1,477.7040 |
| Elo rating diff | -20.9337 |
| Elo home expectancy | 0.4699 |
| Market p home draw | 61.0% |
| Market home draw odds | 1.62 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:22:53Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 68.3% |
| Market draw away odds | 1.39 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:22:53Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 70.8% |
| Market home away odds | 1.37 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:22:53Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.59 |
| Market reference dc draw away odds | 1.42 |
| Market reference dc home away odds | 1.37 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.31, "price": 1.59, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.59, "price": 2.31, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.82, "price": 2.01, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.82, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.5, "price": 2.52, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.52, "price": 1.5, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 74.4% |
| Market over 1 5 odds | 1.32 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference over 1 5 odds | 1.32 |
| Market reference over 1 5 opposite odds | 3.60 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:05Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.7% |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.64 |
| Market reference under 3 5 last update utc | 2026-10-25T10:22:24Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 53.5% |
| Market btts yes odds | 1.78 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:22:53Z |
| Market reference btts yes odds | 1.75 |
| Market reference btts yes opposite odds | 1.98 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Auxerre vs Le Mans FC

The model's most likely 1X2 outcome is **Auxerre win** at **44.7%**. Expected goals are 1.73 for Auxerre and 1.52 for Le Mans FC (3.24 combined). The most likely exact score is 1-1 at 11.0%. Goal-market probabilities: at least one goal: 95.4%; Over 2.5 goals: 62.7%; Under 3.5 goals: 59.3%; Double Chance 1X: 69.6%; Double Chance X2: 55.3%; Double Chance 12 (either team wins): 75.2%; Under 4.5 goals: 77.4%; BTTS Yes (both teams score): 64.8%; BTTS No (at least one team does not score): 35.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Auxerre win | 44.7% | 2.23 |
| Draw | 24.8% | 4.03 |
| Le Mans FC win | 30.4% | 3.28 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Auxerre expected goals | 1.73 |
| Le Mans FC expected goals | 1.52 |
| Expected total goals | 3.24 |
| Over 0.5 | 95.4% |
| Under 0.5 | 4.6% |
| Over 1.5 | 84.0% |
| Under 1.5 | 16.0% |
| Over 2.5 | 62.7% |
| Under 2.5 | 37.3% |
| Over 3.5 | 40.7% |
| Under 3.5 | 59.3% |
| Over 4.5 | 22.6% |
| Under 4.5 | 77.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.04% |
| 2 | 2-1 | 9.33% |
| 3 | 1-2 | 7.07% |
| 4 | 2-2 | 6.83% |
| 5 | 1-0 | 6.52% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Auxerre win | 44.7% | 47.1% | 2.17 | -2.9% |
| Draw | 24.8% | 25.3% | 3.65 | -9.5% |
| Le Mans FC win | 30.4% | 27.5% | 3.40 | +3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 8eab078a37a63df32ffa443302a2a7ba |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Auxerre |
| Matched away-team name | Le Mans |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7271 |
| Dc lambda away | 1.5150 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 64.8% |
| P btts no | 35.2% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.81 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.26 |
| Fair Over 2.5 odds | 1.59 |
| Fair Under 2.5 odds | 2.68 |
| Fair Over 3.5 odds | 2.46 |
| Fair Under 3.5 odds | 1.69 |
| Fair Over 4.5 odds | 4.42 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.15792760830410357, "-10": 7.924427910522005e-07, "-11": 1.0705490242885053e-07, "-12": 1.3295963182492082e-08, "-13": 1.5277719624689323e-09, "-14": 1.6321641972959655e-10, "-15": 1.613607793763076e-11, "-16": 1.3131548697531688e-12, "-2": 0.09058263896415077, "-3": 0.03829510603694328, "-4": 0.012940248686168953, "-5": 0.00362274811134484, "-6": 0.00086329553862032, "-7": 0.00017877618513267705, "-8": 3.270064197008302e-05, "-9": 5.352614120350508e-06, "0": 0.24805374194264146, "1": 0.2092985187813311, "10": 3.401035634915733e-06, "11": 5.237843143643259e-07, "12": 7.415977399403462e-08, "13": 9.71426159857188e-09, "14": 1.1830899662874833e-09, "15": 1.3333819510398911e-10, "16": 1.237015675320417e-11, "2": 0.136290916188329, "3": 0.06568525400049613, "4": 0.02530287646187356, "5": 0.008075474987029492, "6": 0.0021937750822766605, "7": 0.0005178988344642927, "8": 0.00010799265334387167, "9": 2.0151460782195335e-05} |
| Raw goal margin distribution | {"-1": 0.1730533365696604, "-10": 8.683400610239863e-07, "-11": 1.1730822913355448e-07, "-12": 1.4569401869285631e-08, "-13": 1.6740963689751321e-09, "-14": 1.7884869099500518e-10, "-15": 1.7681532420082436e-11, "-16": 1.4389240366757264e-12, "-2": 0.09925831256715041, "-3": 0.041962871122704005, "-4": 0.014179618340516046, "-5": 0.003969721665210388, "-6": 0.0009459788254139388, "-7": 0.00019589871377543805, "-8": 3.583258976477324e-05, "-9": 5.865267908780611e-06, "0": 0.24285070860736055, "1": 0.19809406401645327, "10": 3.218966740462812e-06, "11": 4.957443755677256e-07, "12": 7.018975147343646e-08, "13": 9.194224451203894e-09, "14": 1.1197551749701195e-09, "15": 1.2620015234968773e-10, "16": 1.1707940591414081e-11, "2": 0.12899480432768407, "3": 0.06216890108288669, "4": 0.023948328248206793, "5": 0.007643167607484174, "6": 0.002076334912050872, "7": 0.0004901739652328929, "8": 0.00010221144282037668, "9": 1.9072685203204204e-05} |
| Unadjusted home-win probability | 42.4% |
| Unadjusted draw probability | 24.3% |
| Unadjusted away-win probability | 33.4% |
| Raw p over 1 5 | 84.0% |
| Raw p under 3 5 | 59.3% |
| Raw p btts yes | 64.7% |
| P home draw | 69.6% |
| P draw away | 55.3% |
| P home away | 75.2% |
| Raw p home draw | 66.6% |
| Raw p draw away | 57.6% |
| Raw p home away | 75.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.33, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.95, "price": 1.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.62, "price": 1.08, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 6.22, "price": 1.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.68, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.99, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.6, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.59, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 3.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.11, "price": 6.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 6.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:39Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.03, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.3, "price": 1.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.95, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.54, "price": 1.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.17, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.58, "price": 2.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.95, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.25, "price": 4.3, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.97 |
| Reference draw odds | 3.45 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.63 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:44Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:44Z |
| Home probability edge | -2.4% |
| Draw probability edge | -0.5% |
| Away probability edge | +2.9% |
| Over 2.5 probability edge | +7.3% |
| Under 2.5 probability edge | -7.3% |
| Raw edge prob home | -0.0479 |
| Raw ev home | -0.0809 |
| Raw edge prob draw | -0.0104 |
| Raw ev draw | -0.1136 |
| Raw edge prob away | 0.0583 |
| Raw ev away | 0.1343 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.90446914912676, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,465.4208 |
| Elo away rating | 1,405.6867 |
| Elo rating diff | 119.7341 |
| Elo home expectancy | 0.6658 |
| Market p home draw | 72.3% |
| Market home draw odds | 1.36 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:22:53Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.4% |
| Market draw away odds | 1.76 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:22:53Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.4% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:22:53Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.34 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.35, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.35, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.86, "price": 1.96, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.86, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.51, "price": 2.48, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:53Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.48, "price": 1.51, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 80.2% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.33 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 66.0% |
| Market under 3 5 odds | 1.48 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.48 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.9% |
| Market btts yes odds | 1.61 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:22:53Z |
| Market reference btts yes odds | 1.58 |
| Market reference btts yes opposite odds | 2.26 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Marseille vs Le Havre

The model's most likely 1X2 outcome is **Marseille win** at **66.6%**. Expected goals are 2.11 for Marseille and 0.81 for Le Havre (2.92 combined). The most likely exact score is 2-0 at 11.9%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 56.1%; Under 3.5 goals: 66.5%; Double Chance 1X: 86.2%; Double Chance X2: 33.4%; Double Chance 12 (either team wins): 80.4%; Under 4.5 goals: 82.8%; BTTS Yes (both teams score): 49.2%; BTTS No (at least one team does not score): 50.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Marseille win | 66.6% | 1.50 |
| Draw | 19.6% | 5.10 |
| Le Havre win | 13.8% | 7.24 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Marseille expected goals | 2.11 |
| Le Havre expected goals | 0.81 |
| Expected total goals | 2.92 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 79.4% |
| Under 1.5 | 20.6% |
| Over 2.5 | 56.1% |
| Under 2.5 | 43.9% |
| Over 3.5 | 33.5% |
| Under 3.5 | 66.5% |
| Over 4.5 | 17.2% |
| Under 4.5 | 82.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.95% |
| 2 | 1-0 | 10.79% |
| 3 | 2-1 | 9.68% |
| 4 | 1-1 | 9.35% |
| 5 | 3-0 | 8.41% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Marseille win | 66.6% | 66.3% | 1.50 | -0.1% |
| Draw | 19.6% | 18.8% | 4.96 | -2.8% |
| Le Havre win | 13.8% | 14.9% | 6.17 | -14.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | fcc34b753fc61a0cc0e11d7cb0a0c36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Marseille |
| Matched away-team name | Le Havre |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1121 |
| Dc lambda away | 0.8099 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 49.2% |
| P btts no | 50.8% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.63 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.84 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 2.99 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.80 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.09568892865279492, "-10": 2.288669722139868e-09, "-11": 1.6638374434474447e-10, "-12": 1.1109372885642441e-11, "-13": 6.85754163572078e-13, "-14": 3.9354338890792456e-14, "-15": 2.1097091623314945e-15, "-16": 1.0567576938718961e-16, "-17": 4.574454814558517e-18, "-2": 0.03279768095258295, "-3": 0.007823140732591227, "-4": 0.001465258284605658, "-5": 0.00022501181698000164, "-6": 2.921876395026524e-05, "-7": 3.282782851724069e-06, "-8": 3.2478239145833923e-07, "-9": 2.869115462589345e-08, "0": 0.19605041984869992, "1": 0.23659665071357963, "10": 3.0434689702704982e-05, "11": 5.769687053260036e-06, "12": 1.004584604921558e-06, "13": 1.6170410221849596e-07, "14": 2.4199189231574905e-08, "15": 3.3828784512275415e-09, "16": 4.4187032181256564e-10, "17": 4.9878612839271925e-11, "2": 0.20397831977918815, "3": 0.12687545896190278, "4": 0.06196782868598233, "5": 0.024814928612862792, "6": 0.008402821801314712, "7": 0.0024618471201306676, "8": 0.000635136408895614, "9": 0.0001463114013706948} |
| Raw goal margin distribution | {"-1": 0.0879302870007537, "-10": 2.103099996530432e-09, "-11": 1.5289303160221018e-10, "-12": 1.0208603649199693e-11, "-13": 6.301519022503277e-13, "-14": 3.616341370012015e-14, "-15": 1.9386499017565243e-15, "-16": 9.710737555602924e-17, "-17": 4.203549254643696e-18, "-2": 0.030138382148513453, "-3": 0.007188825494744848, "-4": 0.0013464523358089064, "-5": 0.00020676742779097577, "-6": 2.6849650593084112e-05, "-7": 3.016608529087329e-06, "-8": 2.9844841295428975e-07, "-9": 2.63648208435044e-08, "0": 0.20409603098613596, "1": 0.23771453529120878, "10": 3.057848916115449e-05, "11": 5.796947980898416e-06, "12": 1.0093311202816802e-06, "13": 1.6246813045585364e-07, "14": 2.4313526862101445e-08, "15": 3.398862057238935e-09, "16": 4.439580944694333e-10, "17": 5.0114281991300863e-11, "2": 0.20494208751285695, "3": 0.12747492695278667, "4": 0.06226061761510831, "5": 0.02493217552192774, "6": 0.008442523905600319, "7": 0.0024734789877829543, "8": 0.0006381373355530867, "9": 0.00014700270134738636} |
| Unadjusted home-win probability | 66.9% |
| Unadjusted draw probability | 20.4% |
| Unadjusted away-win probability | 12.7% |
| Raw p over 1 5 | 79.4% |
| Raw p under 3 5 | 66.5% |
| Raw p btts yes | 49.3% |
| P home draw | 86.2% |
| P draw away | 33.4% |
| P home away | 80.4% |
| Raw p home draw | 87.3% |
| Raw p draw away | 33.1% |
| Raw p home away | 79.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.37, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.68, "price": 2.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.96, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.4, "price": 1.36, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.68, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.3, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.68, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.4, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.44 |
| Reference draw odds | 4.40 |
| Reference away odds | 5.40 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:05Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:05Z |
| Home probability edge | +0.3% |
| Draw probability edge | +0.8% |
| Away probability edge | -1.1% |
| Over 2.5 probability edge | -7.7% |
| Under 2.5 probability edge | +7.7% |
| Raw edge prob home | 0.0063 |
| Raw ev home | 0.0036 |
| Raw edge prob draw | 0.0161 |
| Raw ev draw | 0.0123 |
| Raw edge prob away | -0.0224 |
| Raw ev away | -0.2174 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.654879906369993, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,561.9354 |
| Elo away rating | 1,427.0514 |
| Elo rating diff | 194.8840 |
| Elo home expectancy | 0.7543 |
| Market p home draw | 83.7% |
| Market home draw odds | 1.16 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:23:04Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 36.1% |
| Market draw away odds | 2.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:23:04Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 80.2% |
| Market home away odds | 1.21 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:23:04Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.16 |
| Market reference dc draw away odds | 2.69 |
| Market reference dc home away odds | 1.21 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.61, "price": 1.47, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.47, "price": 2.61, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.01, "price": 1.82, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.82, "price": 2.01, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.61, "price": 2.27, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.61, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.9% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 5.00 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 58.5% |
| Market under 3 5 odds | 1.68 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.60 |
| Market reference under 3 5 opposite odds | 2.16 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 59.5% |
| Market btts yes odds | 1.67 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:23:04Z |
| Market reference btts yes odds | 1.59 |
| Market reference btts yes opposite odds | 2.24 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Rennes vs Strasbourg

The model's most likely 1X2 outcome is **Rennes win** at **53.6%**. Expected goals are 1.90 for Rennes and 1.25 for Strasbourg (3.15 combined). The most likely exact score is 1-1 at 10.3%. Goal-market probabilities: at least one goal: 95.3%; Over 2.5 goals: 61.4%; Under 3.5 goals: 61.1%; Double Chance 1X: 76.2%; Double Chance X2: 46.4%; Double Chance 12 (either team wins): 77.4%; Under 4.5 goals: 78.7%; BTTS Yes (both teams score): 61.1%; BTTS No (at least one team does not score): 38.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Rennes win | 53.6% | 1.87 |
| Draw | 22.6% | 4.42 |
| Strasbourg win | 23.8% | 4.21 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Rennes expected goals | 1.90 |
| Strasbourg expected goals | 1.25 |
| Expected total goals | 3.15 |
| Over 0.5 | 95.3% |
| Under 0.5 | 4.7% |
| Over 1.5 | 82.9% |
| Under 1.5 | 17.1% |
| Over 2.5 | 61.4% |
| Under 2.5 | 38.6% |
| Over 3.5 | 38.9% |
| Under 3.5 | 61.1% |
| Over 4.5 | 21.3% |
| Under 4.5 | 78.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.35% |
| 2 | 2-1 | 9.96% |
| 3 | 2-0 | 7.96% |
| 4 | 1-0 | 7.77% |
| 5 | 3-1 | 6.32% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Rennes win | 53.6% | 55.1% | 1.79 | -4.1% |
| Draw | 22.6% | 21.8% | 4.30 | -2.7% |
| Strasbourg win | 23.8% | 23.1% | 4.15 | -1.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 31dcb6d13ed240fc4a5c7a696149967e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Rennes |
| Matched away-team name | Strasbourg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9030 |
| Dc lambda away | 1.2514 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 61.1% |
| P btts no | 38.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.42 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.86 |
| Fair Over 2.5 odds | 1.63 |
| Fair Under 2.5 odds | 2.59 |
| Fair Over 3.5 odds | 2.57 |
| Fair Under 3.5 odds | 1.64 |
| Fair Over 4.5 odds | 4.69 |
| Fair Under 4.5 odds | 1.27 |
| Goal margin distribution | {"-1": 0.13803167194894114, "-10": 1.3337541221381822e-07, "-11": 1.49088635534543e-08, "-12": 1.5317196212217302e-09, "-13": 1.4556482796610375e-10, "-14": 1.2861405004067636e-11, "-15": 1.0530982959390976e-12, "-16": 7.169704326341953e-14, "-2": 0.0672400638667757, "-3": 0.023797265192688113, "-4": 0.006702987952303918, "-5": 0.001560229299276712, "-6": 0.00030861744165597667, "-7": 5.299095213919275e-05, "-8": 8.03051527668781e-06, "-9": 1.088439821059884e-06, "0": 0.22638028920701664, "1": 0.22558160818159415, "10": 9.344957787195679e-06, "11": 1.5884240185538242e-06, "12": 2.4815413546418827e-07, "13": 3.58607219794745e-08, "14": 4.818050279742687e-09, "15": 5.998907420143156e-10, "16": 6.210475197457467e-11, "2": 0.1648037152533067, "3": 0.08869237143632912, "4": 0.03798813665820367, "5": 0.01344585173639433, "6": 0.004044275120693372, "7": 0.0010559473971714214, "8": 0.00024333484856160813, "9": 5.015169959509124e-05} |
| Raw goal margin distribution | {"-1": 0.1420731706193202, "-10": 1.3728057791609853e-07, "-11": 1.5345387659678537e-08, "-12": 1.5765676095504596e-09, "-13": 1.4982689369618183e-10, "-14": 1.323798054277714e-11, "-15": 1.083932490024573e-12, "-16": 7.379629701386607e-14, "-2": 0.06920881947827259, "-3": 0.024494037276058107, "-4": 0.006899248104153878, "-5": 0.0016059120367925316, "-6": 0.00031765360678023737, "-7": 5.454250084963573e-05, "-8": 8.26564476802077e-06, "-9": 1.1203087974150234e-06, "0": 0.23494300807956378, "1": 0.21904775371991303, "10": 9.07428592425312e-06, "11": 1.5424161394349085e-06, "12": 2.409664794391365e-07, "13": 3.4822034738110046e-08, "14": 4.678497948457066e-09, "15": 5.825152173302457e-10, "16": 6.030591999508981e-11, "2": 0.16003026098595968, "3": 0.08612344282775285, "4": 0.03688782995236909, "5": 0.01305639960389503, "6": 0.003927134786183758, "7": 0.0010253624276434312, "8": 0.00023628678068598205, "9": 4.8699081587791227e-05} |
| Unadjusted home-win probability | 52.0% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 24.5% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.3% |
| Raw p btts yes | 61.3% |
| P home draw | 76.2% |
| P draw away | 46.4% |
| P home away | 77.4% |
| Raw p home draw | 75.5% |
| Raw p draw away | 48.0% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 1.5, "market_key": "spreads", "opposite_price": 3.04, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.46, "price": 3.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.67, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.22, "price": 1.39, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.97, "price": 1.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.51, "price": 1.59, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.67, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.67, "price": 2.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.39, "price": 3.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.67, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.71 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.75 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.70 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:05Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:05Z |
| Home probability edge | -1.6% |
| Draw probability edge | +0.9% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -5.4% |
| Under 2.5 probability edge | +5.4% |
| Raw edge prob home | -0.0310 |
| Raw ev home | -0.0685 |
| Raw edge prob draw | 0.0171 |
| Raw ev draw | 0.0103 |
| Raw edge prob away | 0.0139 |
| Raw ev away | 0.0154 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 10.570285217678062, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,575.7087 |
| Elo away rating | 1,512.6354 |
| Elo rating diff | 123.0732 |
| Elo home expectancy | 0.6701 |
| Market p home draw | 76.5% |
| Market home draw odds | 1.27 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:22:47Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 46.5% |
| Market draw away odds | 2.12 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:22:47Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.1% |
| Market home away odds | 1.26 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:22:47Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.27 |
| Market reference dc draw away odds | 2.09 |
| Market reference dc home away odds | 1.26 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.56, "price": 1.49, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.56, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.96, "price": 1.87, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.87, "price": 1.96, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.6, "price": 2.3, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:47Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.3, "price": 1.6, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 86.3% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.80 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 55.7% |
| Market under 3 5 odds | 1.75 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.04 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 67.3% |
| Market btts yes odds | 1.49 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:22:47Z |
| Market reference btts yes odds | 1.42 |
| Market reference btts yes opposite odds | 2.69 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Toulouse vs Troyes

The model's most likely 1X2 outcome is **Toulouse win** at **62.0%**. Expected goals are 1.91 for Toulouse and 0.91 for Troyes (2.82 combined). The most likely exact score is 2-0 at 11.2%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 54.0%; Under 3.5 goals: 68.6%; Double Chance 1X: 83.8%; Double Chance X2: 38.0%; Double Chance 12 (either team wins): 78.2%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Toulouse win | 62.0% | 1.61 |
| Draw | 21.8% | 4.59 |
| Troyes win | 16.2% | 6.17 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Toulouse expected goals | 1.91 |
| Troyes expected goals | 0.91 |
| Expected total goals | 2.82 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 78.0% |
| Under 1.5 | 22.0% |
| Over 2.5 | 54.0% |
| Under 2.5 | 46.0% |
| Over 3.5 | 31.4% |
| Under 3.5 | 68.6% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 11.21% |
| 2 | 1-0 | 11.14% |
| 3 | 1-1 | 10.37% |
| 4 | 2-1 | 10.20% |
| 5 | 3-0 | 7.12% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Toulouse win | 62.0% | 63.9% | 1.52 | -5.7% |
| Draw | 21.8% | 20.5% | 4.62 | +0.5% |
| Troyes win | 16.2% | 15.6% | 6.30 | +2.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:15:00+00:00 |
| Fixture id | 18e4425261f7dd6b245f82056d424411 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Toulouse |
| Matched away-team name | Troyes |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9073 |
| Dc lambda away | 0.9104 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.10 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.54 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.18 |
| Fair Under 3.5 odds | 1.46 |
| Fair Over 4.5 odds | 6.35 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.10727302884087794, "-10": 7.244180357947097e-09, "-11": 5.918472801348571e-10, "-12": 4.4411261876517454e-11, "-13": 3.0809461864508667e-12, "-14": 1.9867825291877055e-13, "-15": 1.1913050163345825e-14, "-16": 6.114839705703445e-16, "-2": 0.0409580792710539, "-3": 0.010963427926183211, "-4": 0.0023056263144545825, "-5": 0.00039767437045379393, "-6": 5.801191340622786e-05, "-7": 7.322963931030858e-06, "-8": 8.140770279568311e-07, "-9": 8.081226123259383e-08, "0": 0.2176389014387724, "1": 0.24764261037963553, "10": 1.2653325141081907e-05, "11": 2.1657926725832798e-06, "12": 3.404804243247839e-07, "13": 4.9485157580698356e-08, "14": 6.685486060681428e-09, "15": 8.398417033067924e-10, "16": 9.031322547877024e-11, "2": 0.1927615953950085, "3": 0.1080983602632765, "4": 0.047627026819436466, "5": 0.017210122573420774, "6": 0.005259753141865871, "7": 0.0013909991902370683, "8": 0.0003239644026404774, "9": 6.73753232891183e-05} |
| Raw goal margin distribution | {"-1": 0.11153588733991748, "-10": 7.532052492640496e-09, "-11": 6.153663439248681e-10, "-12": 4.617609435294736e-11, "-13": 3.203378057517704e-12, "-14": 2.065734087485309e-13, "-15": 1.2386455712597469e-14, "-16": 6.357833650140196e-16, "-2": 0.04258568779680864, "-3": 0.011399097007393383, "-4": 0.0023972482145387217, "-5": 0.0004134773135444914, "-6": 6.0317214009570636e-05, "-7": 7.613966798842672e-06, "-8": 8.464271462950223e-07, "-9": 8.402361117157022e-08, "0": 0.23001545041423535, "1": 0.24013316661843748, "10": 1.2269629324786628e-05, "11": 2.100117794385838e-06, "12": 3.301557932189487e-07, "13": 4.7984583801022043e-08, "14": 6.482757291541103e-09, "15": 8.143745834536181e-10, "16": 8.757459303346714e-11, "2": 0.18691634785170985, "3": 0.10482041647230135, "4": 0.04618279846606323, "5": 0.016688247733746345, "6": 0.005100257890398136, "7": 0.0013488189282258407, "8": 0.0003141405986572721, "9": 6.533225323604244e-05} |
| Unadjusted home-win probability | 60.2% |
| Unadjusted draw probability | 23.0% |
| Unadjusted away-win probability | 16.8% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 68.8% |
| Raw p btts yes | 51.5% |
| P home draw | 83.8% |
| P draw away | 38.0% |
| P home away | 78.2% |
| Raw p home draw | 83.2% |
| Raw p draw away | 39.8% |
| Raw p home away | 77.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 6.93, "price": 1.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.39, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 4.08, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.47, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.44, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.83, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.65, "price": 2.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:43Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.07, "price": 6.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.1, "price": 1.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.98, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.62, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.38, "price": 1.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.38, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.4, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.11, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.36, "price": 3.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.98, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.49 |
| Reference draw odds | 4.10 |
| Reference away odds | 5.25 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / PMU (FR) |
| Reference Over 2.5 odds | 1.45 |
| Reference Under 2.5 odds | 2.28 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:44Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:44Z |
| Home probability edge | -1.9% |
| Draw probability edge | +1.2% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -9.5% |
| Under 2.5 probability edge | +9.5% |
| Raw edge prob home | -0.0376 |
| Raw ev home | -0.0856 |
| Raw edge prob draw | 0.0248 |
| Raw ev draw | 0.0627 |
| Raw edge prob away | 0.0129 |
| Raw ev away | 0.0609 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.488052748621195, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,462.4700 |
| Elo away rating | 1,403.0517 |
| Elo rating diff | 119.4184 |
| Elo home expectancy | 0.6654 |
| Market p home draw | 82.6% |
| Market home draw odds | 1.15 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:23:04Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 39.6% |
| Market draw away odds | 2.68 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:23:04Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 77.8% |
| Market home away odds | 1.23 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:23:04Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.15 |
| Market reference dc draw away odds | 2.40 |
| Market reference dc home away odds | 1.22 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.27, "price": 1.62, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.62, "price": 2.27, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.03, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:23:04Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.03, "price": 1.78, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 83.0% |
| Market reference over 1 5 odds | 1.18 |
| Market reference over 1 5 opposite odds | 4.80 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 61.8% |
| Market under 3 5 odds | 1.60 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.52 |
| Market reference under 3 5 opposite odds | 2.31 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.8% |
| Market btts yes odds | 1.72 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:23:04Z |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.20 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-26 — Paris Saint Germain vs Lyon

The model's most likely 1X2 outcome is **Paris Saint Germain win** at **68.3%**. Expected goals are 2.42 for Paris Saint Germain and 1.10 for Lyon (3.52 combined). The most likely exact score is 2-1 at 9.8%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 68.8%; Under 3.5 goals: 52.9%; Double Chance 1X: 85.9%; Double Chance X2: 31.7%; Double Chance 12 (either team wins): 82.4%; Under 4.5 goals: 71.8%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Paris Saint Germain win | 68.3% | 1.46 |
| Draw | 17.6% | 5.68 |
| Lyon win | 14.1% | 7.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Paris Saint Germain expected goals | 2.42 |
| Lyon expected goals | 1.10 |
| Expected total goals | 3.52 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 47.1% |
| Under 3.5 | 52.9% |
| Over 4.5 | 28.2% |
| Under 4.5 | 71.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.85% |
| 2 | 2-0 | 8.99% |
| 3 | 3-1 | 7.95% |
| 4 | 1-1 | 7.80% |
| 5 | 3-0 | 7.26% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Paris Saint Germain win | 68.3% | 70.5% | 1.39 | -5.0% |
| Draw | 17.6% | 16.4% | 5.74 | +1.0% |
| Lyon win | 14.1% | 13.1% | 6.96 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-26T19:30:00+00:00 |
| Fixture id | 8664b2167f22c59026d86615421463b1 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-25T10:22:43Z |
| Market best draw last update utc | 2026-10-25T10:22:43Z |
| Market best away last update utc | 2026-10-25T10:22:43Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Paris SG |
| Matched away-team name | Lyon |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4231 |
| Dc lambda away | 1.0957 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:22:57.997574+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.27 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.83 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.20 |
| Fair Over 3.5 odds | 2.13 |
| Fair Under 3.5 odds | 1.89 |
| Fair Over 4.5 odds | 3.55 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.08867772237344548, "-10": 2.4146757505612293e-08, "-11": 2.358615120152188e-09, "-12": 2.1181080018732993e-10, "-13": 1.7599097775454193e-11, "-14": 1.3603879510998276e-12, "-15": 9.829449111336723e-14, "-16": 6.6638744330364794e-15, "-17": 4.2208457657722154e-16, "-18": 2.2390905131856343e-17, "-2": 0.037141825763666286, "-3": 0.011332054628198423, "-4": 0.002765351520586578, "-5": 0.0005593287083530815, "-6": 9.632179483421505e-05, "-7": 1.4417443701862296e-05, "-8": 1.9063506488796899e-06, "-9": 2.2559001218979058e-07, "0": 0.17603947063310446, "1": 0.2226102512490038, "10": 7.474858182438085e-05, "11": 1.6146429955173316e-05, "12": 3.2065855671663316e-06, "13": 5.891968748249074e-07, "14": 1.0071823469483807e-07, "15": 1.6093474085417115e-08, "16": 2.4128078072631555e-09, "17": 3.379642051200903e-10, "18": 3.96477156667623e-11, "2": 0.2010041394801807, "3": 0.13562061530866246, "4": 0.07318847430309848, "5": 0.03273668937527146, "6": 0.012467159375133019, "7": 0.004126734293512555, "8": 0.001206691704993228, "9": 0.0003157829709946689} |
| Raw goal margin distribution | {"-1": 0.09500869645117942, "-10": 2.5870668446689148e-08, "-11": 2.5270038742312643e-09, "-12": 2.2693262164912724e-10, "-13": 1.8855551243425422e-11, "-14": 1.457510211613068e-12, "-15": 1.0531203575216731e-13, "-16": 7.139628829559649e-15, "-17": 4.5221848666648065e-16, "-18": 2.398946039661392e-17, "-2": 0.03979349441071642, "-3": 0.01214108469999549, "-4": 0.0029627784314732552, "-5": 0.0005992608971682527, "-6": 0.0001031985026464449, "-7": 1.5446749145221437e-05, "-8": 2.042450857794648e-06, "-9": 2.416955737800476e-07, "0": 0.187744870282027, "1": 0.21552756985617652, "10": 7.237034278706185e-05, "11": 1.563270689721685e-05, "12": 3.104563203849049e-06, "13": 5.704506862795897e-07, "14": 9.751373192468664e-08, "15": 1.5581435898445967e-08, "16": 2.3360406823662166e-09, "17": 3.2721136344449185e-10, "18": 3.8386263705563185e-11, "2": 0.19460888916897603, "3": 0.13130564057977628, "4": 0.07085987244308736, "5": 0.03169512215453442, "6": 0.012070497868161818, "7": 0.003995436008596152, "8": 0.0011682989857097182, "9": 0.0003057358587871818} |
| Unadjusted home-win probability | 66.2% |
| Unadjusted draw probability | 18.8% |
| Unadjusted away-win probability | 15.1% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.3% |
| Raw p btts yes | 61.1% |
| P home draw | 85.9% |
| P draw away | 31.7% |
| P home away | 82.4% |
| Raw p home draw | 84.9% |
| Raw p draw away | 33.8% |
| Raw p home away | 81.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 4.92, "price": 1.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 5.34, "price": 1.14, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.8, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.27, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.14, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:22:02Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.8, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.13, "price": 4.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:21:56Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:22:41Z", "line": -0.0, "market_key": "draw_no_bet", "opposite_price": 5.76, "price": 1.16, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:22:41Z", "line": 0.0, "market_key": "draw_no_bet", "opposite_price": 1.16, "price": 5.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.81, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 4.03, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.76, "price": 1.48, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.53, "price": 1.57, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.87, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.57, "price": 2.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:23:05Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.03, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / PMU (FR) |
| Reference home odds | 1.36 |
| Reference draw odds | 4.90 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-25T10:22:44Z |
| Market reference home last update utc | 2026-10-25T10:22:44Z |
| Market reference draw last update utc | 2026-10-25T10:22:44Z |
| Market reference away last update utc | 2026-10-25T10:22:44Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 2.90 |
| Market reference over 2 5 last update utc | 2026-10-25T10:22:05Z |
| Market reference under 2 5 last update utc | 2026-10-25T10:22:05Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.0% |
| Over 2.5 probability edge | -1.6% |
| Under 2.5 probability edge | +1.6% |
| Raw edge prob home | -0.0435 |
| Raw ev home | -0.0803 |
| Raw edge prob draw | 0.0234 |
| Raw ev draw | 0.0777 |
| Raw edge prob away | 0.0201 |
| Raw ev away | 0.0484 |
| Count model | {"corners": {"alpha": 0.015553586640413052, "mu": 9.539580188438363, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,650.2101 |
| Elo away rating | 1,562.7526 |
| Elo rating diff | 147.4576 |
| Elo home expectancy | 0.7003 |
| Market p home draw | 84.8% |
| Market home draw odds | 1.12 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:22:41Z |
| Market reference home draw last update utc | 2026-10-25T10:23:06Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.9% |
| Market draw away odds | 3.23 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:22:41Z |
| Market reference draw away last update utc | 2026-10-25T10:23:06Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.2% |
| Market home away odds | 1.17 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:22:41Z |
| Market reference home away last update utc | 2026-10-25T10:23:06Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.12 |
| Market reference dc draw away odds | 2.80 |
| Market reference dc home away odds | 1.17 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.32, "price": 1.57, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.57, "price": 2.32, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.83, "price": 1.98, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.98, "price": 1.83, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.49, "price": 2.51, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:22:41Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.51, "price": 1.49, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 88.6% |
| Market reference over 1 5 odds | 1.11 |
| Market reference over 1 5 opposite odds | 6.50 |
| Market reference over 1 5 last update utc | 2026-10-25T10:23:06Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 52.0% |
| Market under 3 5 odds | 1.92 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:23:05Z |
| Market reference under 3 5 odds | 1.77 |
| Market reference under 3 5 opposite odds | 1.90 |
| Market reference under 3 5 last update utc | 2026-10-25T10:23:06Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 63.0% |
| Market btts yes odds | 1.58 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:22:41Z |
| Market reference btts yes odds | 1.53 |
| Market reference btts yes opposite odds | 2.50 |
| Market reference btts yes last update utc | 2026-10-25T10:23:06Z |
| Market btts yes bookmakers | 1 |

</details>


---
