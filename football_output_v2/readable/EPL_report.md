# Premier League — football model report

Fixtures in this report: **6**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Premier League |
| Training matches | 1,975 |
| Training data through | 2026-10-24 |
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
| Training sha256 | f6f2bc2144c61128ab5f084483e7e42604e8300db658a4450112df043e19f77d |
| Training as of utc | 2026-10-25T10:16:28.509803+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 75, 'bbs_added_results': 5, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 75, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 1102, 'added_results': 0, 'conflicts': 0, 'unmapped': 38, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 101, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_PAIRED_AUDIT', 'cutoff_utc': '2026-10-25T10:16:28.509803+00:00', 'observations': 314, 'observations_sha256': 'e6db305002050c2d8101eee39c1bbcb3b1f667fd288527cb05689b9a6d86fbda', 'eligible_training_matches': 152, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 144, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 13, 'retrospective_eligible_training_matches': 152, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:26.478110+00:00', 'retrospective_inputs_sha256': '02c85eabc64ff05f5b784d7db92e75a2f61368cdcb9bac56bdb6bed0972768ff', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'training_matches': 91, 'tuning_matches': 21, 'audit_matches': 40, 'tuning_origin_utc': '2025-09-20T00:00:00+00:00', 'audit_origin_utc': '2025-10-18T00:00:00+00:00', 'supported_feature_columns': ['own_shots_on_target', 'own_shots_off_target', 'own_total_shots', 'own_blocked_shots', 'own_shots_inside_box', 'own_shots_outside_box', 'own_fouls', 'own_corner_kicks', 'own_offsides', 'own_ball_possession', 'own_yellow_cards', 'own_goalkeeper_saves', 'own_total_passes', 'own_accurate_passes', 'own_pass_percentage', 'opponent_conceded_shots_on_target', 'opponent_conceded_shots_off_target', 'opponent_conceded_total_shots', 'opponent_conceded_blocked_shots', 'opponent_conceded_shots_inside_box', 'opponent_conceded_shots_outside_box', 'opponent_conceded_fouls', 'opponent_conceded_corner_kicks', 'opponent_conceded_offsides', 'opponent_conceded_ball_possession', 'opponent_conceded_yellow_cards', 'opponent_conceded_goalkeeper_saves', 'opponent_conceded_total_passes', 'opponent_conceded_accurate_passes', 'opponent_conceded_pass_percentage', 'is_home'], 'paired_audit_matches': 33, 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 932.577 |
| Base scoring parameter | 0.204 |
| Home-advantage parameter | 0.184 |
| Dixon-Coles low-score adjustment | -0.092 |
| Xi per day | 0.0029 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 29, 'matches': 1975, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-24'} |
| Training data health | {'training_end': '2026-10-24', 'days_since_latest_result': 1, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Additional event odds calls used before this league | 0.00 |
| Bbs statistics model artifact | bbs/feature_models/EPL/20261025T101628509803Z_072f48178a32cd2b2b89f2afaa48572860da958c76ced67b1534c2c310c4e36e.json |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 5.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 5.00 |
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

## 2026-10-24 — Chelsea vs Tottenham Hotspur

The model's most likely 1X2 outcome is **Chelsea win** at **53.3%**. Expected goals are 1.99 for Chelsea and 1.24 for Tottenham Hotspur (3.22 combined). The most likely exact score is 1-1 at 10.5%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 62.6%; Under 3.5 goals: 59.8%; Double Chance 1X: 76.5%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 76.9%; Under 4.5 goals: 77.6%; BTTS Yes (both teams score): 62.1%; BTTS No (at least one team does not score): 37.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Chelsea win | 53.3% | 1.87 |
| Draw | 23.1% | 4.33 |
| Tottenham Hotspur win | 23.5% | 4.25 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Chelsea expected goals | 1.99 |
| Tottenham Hotspur expected goals | 1.24 |
| Expected total goals | 3.22 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 84.1% |
| Under 1.5 | 15.9% |
| Over 2.5 | 62.6% |
| Under 2.5 | 37.4% |
| Over 3.5 | 40.2% |
| Under 3.5 | 59.8% |
| Over 4.5 | 22.4% |
| Under 4.5 | 77.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.51% |
| 2 | 2-1 | 9.61% |
| 3 | 2-0 | 7.78% |
| 4 | 1-0 | 6.94% |
| 5 | 3-1 | 6.37% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Chelsea win | 53.3% | 52.7% | 1.93 | +2.9% |
| Draw | 23.1% | 22.7% | 3.90 | -9.9% |
| Tottenham Hotspur win | 23.5% | 24.5% | 3.94 | -7.2% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 5.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Chelsea |
| Matched away-team name | Tottenham |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9873 |
| Dc lambda away | 1.2352 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 62.1% |
| P btts no | 37.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 20.81 |
| Fair Over 1.5 odds | 1.19 |
| Fair Under 1.5 odds | 6.27 |
| Fair Over 2.5 odds | 1.60 |
| Fair Under 2.5 odds | 2.67 |
| Fair Over 3.5 odds | 2.49 |
| Fair Under 3.5 odds | 1.67 |
| Fair Over 4.5 odds | 4.47 |
| Fair Under 4.5 odds | 1.29 |
| Goal margin distribution | {"-1": 0.13677274601156844, "-10": 1.1818788269394154e-07, "-11": 1.3033200842491664e-08, "-12": 1.3210812155138546e-09, "-13": 1.2387549664770961e-10, "-14": 1.0804505823135624e-11, "-15": 8.804382749342712e-13, "-16": 6.679875190184191e-14, "-17": 4.2412427580448956e-15, "-2": 0.06707419335847813, "-3": 0.02333262416284476, "-4": 0.006468501914556251, "-5": 0.0014831166480381685, "-6": 0.0002891236824772854, "-7": 4.8943150095205764e-05, "-8": 7.3141862948145355e-06, "-9": 9.77767999457257e-07, "0": 0.23110424518398315, "1": 0.21402162259094992, "10": 1.3018457297102513e-05, "11": 2.309687936728571e-06, "12": 3.766581625570431e-07, "13": 5.6822314906053976e-08, "14": 7.973593104609995e-09, "15": 1.0453548146337976e-09, "16": 1.2759945089493602e-10, "17": 1.303434573401078e-11, "2": 0.16459507880351162, "3": 0.09211717718658537, "4": 0.041086239592776734, "5": 0.01515596665517866, "6": 0.004753435943142199, "7": 0.0012945879044403402, "8": 0.0003112585518262221, "9": 6.694324216395965e-05} |
| Raw goal margin distribution | {"-1": 0.1311237574834046, "-10": 1.1330648626829999e-07, "-11": 1.2494903526751118e-08, "-12": 1.2665179136219756e-09, "-13": 1.1875919036674688e-10, "-14": 1.0358258078411612e-11, "-15": 8.440744096183011e-13, "-16": 6.403982957123921e-14, "-17": 4.066070931902521e-15, "-2": 0.06430389474368071, "-3": 0.022368940022023897, "-4": 0.006201339821410561, "-5": 0.0014218609580340517, "-6": 0.00027718229493362576, "-7": 4.692169990514645e-05, "-8": 7.01209574185623e-06, "-9": 9.373842214517137e-07, "0": 0.23483744643794457, "1": 0.21642597354915868, "10": 1.3164708595909425e-05, "11": 2.3356353168886146e-06, "12": 3.808895967602688e-07, "13": 5.746066530092566e-08, "14": 8.063169643603334e-09, "15": 1.0570984871646646e-09, "16": 1.290329222344769e-10, "17": 1.3180775525897233e-11, "2": 0.1664441645671218, "3": 0.093152035349769, "4": 0.041547808561080896, "5": 0.015326231054209067, "6": 0.0048068367543608005, "7": 0.00130913149882508, "8": 0.00031475527700881915, "9": 6.769529257126894e-05} |
| Unadjusted home-win probability | 53.9% |
| Unadjusted draw probability | 23.5% |
| Unadjusted away-win probability | 22.6% |
| Raw p over 1 5 | 84.1% |
| Raw p under 3 5 | 59.8% |
| Raw p btts yes | 62.1% |
| P home draw | 76.5% |
| P draw away | 46.7% |
| P home away | 76.9% |
| Raw p home draw | 77.4% |
| Raw p draw away | 46.1% |
| Raw p home away | 76.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.78 |
| Reference draw odds | 3.80 |
| Reference away odds | 3.55 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:24Z |
| Market reference home last update utc | 2026-10-24T14:42:24Z |
| Market reference draw last update utc | 2026-10-24T14:42:24Z |
| Market reference away last update utc | 2026-10-24T14:42:24Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.55 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +0.6% |
| Draw probability edge | +0.4% |
| Away probability edge | -1.0% |
| Over 2.5 probability edge | +0.6% |
| Under 2.5 probability edge | -0.6% |
| Raw edge prob home | 0.0120 |
| Raw ev home | 0.0411 |
| Raw edge prob draw | 0.0075 |
| Raw ev draw | -0.0841 |
| Raw edge prob away | -0.0195 |
| Raw ev away | -0.1105 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.912800468011419, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,487.3698 |
| Elo away rating | 1,464.8455 |
| Elo rating diff | 82.5243 |
| Elo home expectancy | 0.6166 |

</details>


---

## 2026-10-25 — Crystal Palace vs Newcastle United

The model's most likely 1X2 outcome is **Newcastle United win** at **40.3%**. Expected goals are 1.50 for Crystal Palace and 1.59 for Newcastle United (3.09 combined). The most likely exact score is 1-1 at 11.5%. Goal-market probabilities: at least one goal: 94.6%; Over 2.5 goals: 60.0%; Under 3.5 goals: 62.6%; Double Chance 1X: 59.7%; Double Chance X2: 65.4%; Double Chance 12 (either team wins): 74.8%; Under 4.5 goals: 79.8%; BTTS Yes (both teams score): 62.8%; BTTS No (at least one team does not score): 37.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Crystal Palace win | 34.6% | 2.89 |
| Draw | 25.2% | 3.97 |
| Newcastle United win | 40.3% | 2.48 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Crystal Palace expected goals | 1.50 |
| Newcastle United expected goals | 1.59 |
| Expected total goals | 3.09 |
| Over 0.5 | 94.6% |
| Under 0.5 | 5.4% |
| Over 1.5 | 82.5% |
| Under 1.5 | 17.5% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 37.4% |
| Under 3.5 | 62.6% |
| Over 4.5 | 20.2% |
| Under 4.5 | 79.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.52% |
| 2 | 1-2 | 8.92% |
| 3 | 2-1 | 8.00% |
| 4 | 0-1 | 6.43% |
| 5 | 2-2 | 6.31% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Crystal Palace win | 34.6% | 33.9% | 2.95 | +2.0% |
| Draw | 25.2% | 24.5% | 3.68 | -7.4% |
| Newcastle United win | 40.3% | 41.7% | 2.37 | -4.6% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Crystal Palace |
| Matched away-team name | Newcastle |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5048 |
| Dc lambda away | 1.5885 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 62.8% |
| P btts no | 37.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 18.58 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.71 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.67 |
| Fair Under 3.5 odds | 1.60 |
| Fair Over 4.5 odds | 4.95 |
| Fair Under 4.5 odds | 1.25 |
| Goal margin distribution | {"-1": 0.1969630209609126, "-10": 1.6422516729550715e-06, "-11": 2.3300340998108477e-07, "-12": 3.038397511572341e-08, "-13": 3.6630787609308797e-09, "-14": 4.068665787232098e-10, "-15": 3.7165113842065814e-11, "-2": 0.12305210714383946, "-3": 0.05525157672243731, "-4": 0.019747661793921355, "-5": 0.005833226731397699, "-6": 0.00146433955414315, "-7": 0.00031911154397932964, "-8": 6.1378553968679e-05, "-9": 1.0558920309539691e-05, "0": 0.2516316703796723, "1": 0.17612911277055404, "10": 9.049259216155362e-07, "11": 1.2162737203764734e-07, "12": 1.5024823135636508e-08, "13": 1.7159584347003643e-09, "14": 1.8055447410818297e-10, "15": 1.5623827506114086e-11, "2": 0.10454337758621224, "3": 0.04446802884679952, "4": 0.015056173608024255, "5": 0.004213117010248321, "6": 0.001001918019650849, "7": 0.0002068371950948341, "8": 3.768760222529527e-05, "9": 6.141820187090668e-06} |
| Raw goal margin distribution | {"-1": 0.19021417210739683, "-10": 1.5859806619493725e-06, "-11": 2.250196534939817e-07, "-12": 2.9342881946941772e-08, "-13": 3.537565023502206e-09, "-14": 3.9292547937393184e-10, "-15": 3.5891668021017074e-11, "-2": 0.11883578233236533, "-3": 0.053358406428851285, "-4": 0.019071017091746672, "-5": 0.0056333538550251165, "-6": 0.0014141646214429757, "-7": 0.0003081773312158285, "-8": 5.9275445570152874e-05, "-9": 1.0197123679503519e-05, "0": 0.2584828106389379, "1": 0.1796690662434617, "10": 9.231136908523017e-07, "11": 1.2407191531202466e-07, "12": 1.5326801462797602e-08, "13": 1.7504468445079812e-09, "14": 1.8418337127125966e-10, "15": 1.5937844999135973e-11, "2": 0.10664455601568583, "3": 0.04536177520521476, "4": 0.01535878203665955, "5": 0.00429779488069001, "6": 0.001022055196960384, "7": 0.00021099433888318824, "8": 3.8445071313082e-05, "9": 6.265262344717325e-06} |
| Unadjusted home-win probability | 35.3% |
| Unadjusted draw probability | 25.8% |
| Unadjusted away-win probability | 38.9% |
| Raw p over 1 5 | 82.4% |
| Raw p under 3 5 | 62.6% |
| Raw p btts yes | 62.9% |
| P home draw | 59.7% |
| P draw away | 65.4% |
| P home away | 74.8% |
| Raw p home draw | 61.1% |
| Raw p draw away | 64.7% |
| Raw p home away | 74.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.23, "price": 1.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.76, "price": 2.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.13, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.19, "price": 1.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.76, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.88, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.44, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.62, "price": 2.44, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.76, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.19, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.38 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +0.7% |
| Draw probability edge | +0.7% |
| Away probability edge | -1.4% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | 0.0139 |
| Raw ev home | 0.0402 |
| Raw edge prob draw | 0.0137 |
| Raw ev draw | -0.0488 |
| Raw edge prob away | -0.0276 |
| Raw ev away | -0.0783 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.512402246102315, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,423.3950 |
| Elo away rating | 1,440.4285 |
| Elo rating diff | 42.9664 |
| Elo home expectancy | 0.5615 |
| Market p home draw | 58.9% |
| Market home draw odds | 1.61 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:16:13Z |
| Market reference home draw last update utc | 2026-10-25T10:16:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.5% |
| Market draw away odds | 1.46 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:16:13Z |
| Market reference draw away last update utc | 2026-10-25T10:16:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 73.6% |
| Market home away odds | 1.32 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:16:13Z |
| Market reference home away last update utc | 2026-10-25T10:16:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.65 |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home away odds | 1.32 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.76, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:13Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.76, "price": 2.07, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:13Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.19, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:13Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.19, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 84.2% |
| Market reference over 1 5 odds | 1.15 |
| Market reference over 1 5 opposite odds | 4.50 |
| Market reference over 1 5 last update utc | 2026-10-25T10:15:40Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 60.3% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market reference under 3 5 odds | 1.62 |
| Market reference under 3 5 opposite odds | 2.41 |
| Market reference under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.3% |
| Market btts yes odds | 1.48 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:16:13Z |
| Market reference btts yes odds | 1.46 |
| Market reference btts yes opposite odds | 2.56 |
| Market reference btts yes last update utc | 2026-10-25T10:16:21Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Hull City vs Brentford

The model's most likely 1X2 outcome is **Brentford win** at **45.0%**. Expected goals are 1.20 for Hull City and 1.08 for Brentford (2.28 combined). The most likely exact score is 0-1 at 14.0%. Goal-market probabilities: at least one goal: 90.3%; Over 2.5 goals: 41.4%; Under 3.5 goals: 80.2%; Double Chance 1X: 55.0%; Double Chance X2: 71.2%; Double Chance 12 (either team wins): 73.8%; Under 4.5 goals: 91.5%; BTTS Yes (both teams score): 46.5%; BTTS No (at least one team does not score): 53.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Hull City win | 28.8% | 3.48 |
| Draw | 26.2% | 3.82 |
| Brentford win | 45.0% | 2.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Hull City expected goals | 1.20 |
| Brentford expected goals | 1.08 |
| Expected total goals | 2.28 |
| Over 0.5 | 90.3% |
| Under 0.5 | 9.7% |
| Over 1.5 | 67.9% |
| Under 1.5 | 32.1% |
| Over 2.5 | 41.4% |
| Under 2.5 | 58.6% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.5% |
| Under 4.5 | 91.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 13.97% |
| 2 | 1-1 | 12.29% |
| 3 | 1-2 | 10.20% |
| 4 | 0-0 | 9.69% |
| 5 | 0-2 | 8.51% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Hull City win | 28.8% | 20.1% | 4.63 | +33.2% |
| Draw | 26.2% | 21.5% | 4.03 | +5.6% |
| Brentford win | 45.0% | 58.3% | 1.75 | -21.2% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hull |
| Matched away-team name | Brentford |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1987 |
| Dc lambda away | 1.0839 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 46.5% |
| P btts no | 53.5% |
| Fair Over 0.5 odds | 1.11 |
| Fair Under 0.5 odds | 10.32 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.11 |
| Fair Over 2.5 odds | 2.41 |
| Fair Under 2.5 odds | 1.71 |
| Fair Over 3.5 odds | 5.05 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 11.73 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2662851042238259, "-10": 1.004317698745071e-07, "-11": 9.798807138770778e-09, "-12": 8.741369722021318e-10, "-13": 6.625886322225274e-11, "-2": 0.12843030774594097, "-3": 0.04210901871063441, "-4": 0.010740610102370101, "-5": 0.0022343650338686946, "-6": 0.00039177861259862375, "-7": 5.931061292768844e-05, "-8": 7.895183294595734e-06, "-9": 9.374432157925969e-07, "0": 0.2620919110913263, "1": 0.16052235257762468, "10": 1.4896376791513925e-07, "11": 1.6074166684095475e-08, "12": 1.5859170634726175e-09, "13": 1.3295071826451634e-10, "2": 0.08509641356259069, "3": 0.03085777297013331, "4": 0.00870490698444174, "5": 0.0020027882493768422, "6": 0.000388389389788653, "7": 6.502865480624855e-05, "8": 9.573710705145693e-06, "9": 1.2572127544540466e-06} |
| Raw goal margin distribution | {"-1": 0.18759434512894935, "-10": 7.075285774871276e-08, "-11": 6.903130438334543e-09, "-12": 6.15817971986242e-10, "-13": 4.6678495559854054e-11, "-2": 0.09047745853653924, "-3": 0.029665248501486927, "-4": 0.007566618209127809, "-5": 0.0015740807077038019, "-6": 0.00027600286722831706, "-7": 4.178354483551613e-05, "-8": 5.562052538161416e-06, "-9": 6.604163859438804e-07, "0": 0.308702280978675, "1": 0.2087642366868739, "10": 1.9373194326794025e-07, "11": 2.090494616044224e-08, "12": 2.062533721242629e-09, "13": 1.7290648168168087e-10, "2": 0.1106704925321477, "3": 0.04013147899045111, "4": 0.011320998184090457, "5": 0.002604687468210441, "6": 0.0005051122986582178, "7": 8.457175754906678e-05, "8": 1.2450904036272432e-05, "9": 1.6350436984137872e-06} |
| Unadjusted home-win probability | 37.4% |
| Unadjusted draw probability | 30.9% |
| Unadjusted away-win probability | 31.7% |
| Raw p over 1 5 | 67.7% |
| Raw p under 3 5 | 80.3% |
| Raw p btts yes | 47.4% |
| P home draw | 55.0% |
| P draw away | 71.2% |
| P home away | 73.8% |
| Raw p home draw | 68.3% |
| Raw p draw away | 62.6% |
| Raw p home away | 69.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.46, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.45, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.81, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.76, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.76, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.81, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.48, "price": 2.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 9.4, "price": 1.03, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 3.0, "market_key": "alternate_spreads", "opposite_price": 9.35, "price": 1.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 5.16, "price": 1.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.54, "price": 1.28, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.15, "price": 5.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -3.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:31Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.03, "price": 9.4, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 4.20 |
| Reference draw odds | 3.95 |
| Reference away odds | 1.62 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.25 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +8.6% |
| Draw probability edge | +4.7% |
| Away probability edge | -13.3% |
| Over 2.5 probability edge | -17.5% |
| Under 2.5 probability edge | +17.5% |
| Raw edge prob home | 0.1729 |
| Raw ev home | 0.7321 |
| Raw edge prob draw | 0.0932 |
| Raw ev draw | 0.2441 |
| Raw edge prob away | -0.2661 |
| Raw ev away | -0.4449 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.96509439027004, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,401.6375 |
| Elo away rating | 1,497.6340 |
| Elo rating diff | -35.9965 |
| Elo home expectancy | 0.4484 |
| Market p home draw | 43.3% |
| Market home draw odds | 2.30 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:16:10Z |
| Market reference home draw last update utc | 2026-10-25T10:16:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.2% |
| Market draw away odds | 1.20 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:16:10Z |
| Market reference draw away last update utc | 2026-10-25T10:16:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.27 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:16:10Z |
| Market reference home away last update utc | 2026-10-25T10:16:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.24 |
| Market reference dc draw away odds | 1.21 |
| Market reference dc home away odds | 1.27 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.06, "price": 1.78, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:10Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.78, "price": 2.06, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.68, "price": 2.2, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:10Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.2, "price": 1.68, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 81.3% |
| Market reference over 1 5 odds | 1.20 |
| Market reference over 1 5 opposite odds | 4.40 |
| Market reference over 1 5 last update utc | 2026-10-25T10:16:31Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 64.5% |
| Market under 3 5 odds | 1.51 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market reference under 3 5 odds | 1.50 |
| Market reference under 3 5 opposite odds | 2.60 |
| Market reference under 3 5 last update utc | 2026-10-25T10:16:31Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 57.5% |
| Market btts yes odds | 1.70 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:16:10Z |
| Market reference btts yes odds | 1.64 |
| Market reference btts yes opposite odds | 2.15 |
| Market reference btts yes last update utc | 2026-10-25T10:16:21Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Liverpool vs Brighton and Hove Albion

The model's most likely 1X2 outcome is **Liverpool win** at **43.6%**. Expected goals are 1.65 for Liverpool and 1.48 for Brighton and Hove Albion (3.13 combined). The most likely exact score is 1-1 at 11.1%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 61.0%; Under 3.5 goals: 61.7%; Double Chance 1X: 67.9%; Double Chance X2: 56.4%; Double Chance 12 (either team wins): 75.7%; Under 4.5 goals: 79.1%; BTTS Yes (both teams score): 63.1%; BTTS No (at least one team does not score): 36.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Liverpool win | 43.6% | 2.29 |
| Draw | 24.3% | 4.11 |
| Brighton and Hove Albion win | 32.1% | 3.11 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Liverpool expected goals | 1.65 |
| Brighton and Hove Albion expected goals | 1.48 |
| Expected total goals | 3.13 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 83.0% |
| Under 1.5 | 17.0% |
| Over 2.5 | 61.0% |
| Under 2.5 | 39.0% |
| Over 3.5 | 38.3% |
| Under 3.5 | 61.7% |
| Over 4.5 | 20.9% |
| Under 4.5 | 79.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.08% |
| 2 | 2-1 | 9.39% |
| 3 | 1-2 | 7.56% |
| 4 | 1-0 | 6.65% |
| 5 | 2-0 | 6.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Liverpool win | 43.6% | 46.3% | 2.12 | -7.6% |
| Draw | 24.3% | 23.0% | 3.99 | -3.0% |
| Brighton and Hove Albion win | 32.1% | 30.7% | 3.21 | +3.1% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Liverpool |
| Matched away-team name | Brighton |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.6492 |
| Dc lambda away | 1.4802 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 63.1% |
| P btts no | 36.9% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.66 |
| Fair Over 1.5 odds | 1.20 |
| Fair Under 1.5 odds | 5.88 |
| Fair Over 2.5 odds | 1.64 |
| Fair Under 2.5 odds | 2.56 |
| Fair Over 3.5 odds | 2.61 |
| Fair Under 3.5 odds | 1.62 |
| Fair Over 4.5 odds | 4.78 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.16602500571692444, "-10": 7.255064281412e-07, "-11": 9.588063864181757e-08, "-12": 1.1646701557668413e-08, "-13": 1.3079735845146126e-09, "-14": 1.3528703369108416e-10, "-15": 1.1481603932008105e-11, "-2": 0.09658886565730479, "-3": 0.040294379468398894, "-4": 0.01339320639408218, "-5": 0.00368120989261441, "-6": 0.0008601844195201547, "-7": 0.0001745277212604857, "-8": 3.125960497181775e-05, "-9": 5.0082272508286415e-06, "0": 0.2431757288071207, "1": 0.2074860503961941, "10": 2.3850381404789064e-06, "11": 3.5118374836992416e-07, "12": 4.752869247829016e-08, "13": 5.947046321951146e-09, "14": 6.853429517257008e-10, "15": 6.480429132848739e-11, "2": 0.1337167167801292, "3": 0.06215163228895782, "4": 0.023016646972660766, "5": 0.007048512976614858, "6": 0.0018350500894439182, "7": 0.00041483003937356814, "8": 8.27825295950489e-05, "9": 1.4777081296588022e-05} |
| Raw goal margin distribution | {"-1": 0.17354430681164393, "-10": 7.58364739187727e-07, "-11": 1.002230892744112e-07, "-12": 1.2174182676517245e-08, "-13": 1.367211933361134e-09, "-14": 1.4141420674036068e-10, "-15": 1.2001607750964655e-11, "-2": 0.1009633920133707, "-3": 0.04211931885231537, "-4": 0.013999787017681335, "-5": 0.003847932522473088, "-6": 0.0008991423199847784, "-7": 0.00018243211180615088, "-8": 3.267535786319757e-05, "-9": 5.235050725323609e-06, "0": 0.2559593231339316, "1": 0.19447598879535885, "10": 2.235488360776988e-06, "11": 3.291633658392405e-07, "12": 4.454848626313031e-08, "13": 5.574146848257063e-09, "14": 6.423696819438344e-10, "15": 6.074084792796876e-11, "2": 0.12533223638229504, "3": 0.05825451938364306, "4": 0.021573427082035846, "5": 0.006606547900673889, "6": 0.0017199863795766962, "7": 0.00038881882389271276, "8": 7.759179119385031e-05, "9": 1.385050942545713e-05} |
| Unadjusted home-win probability | 40.8% |
| Unadjusted draw probability | 25.6% |
| Unadjusted away-win probability | 33.6% |
| Raw p over 1 5 | 82.9% |
| Raw p under 3 5 | 61.8% |
| Raw p btts yes | 63.4% |
| P home draw | 67.9% |
| P draw away | 56.4% |
| P home away | 75.7% |
| Raw p home draw | 66.4% |
| Raw p draw away | 59.2% |
| Raw p home away | 74.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.05, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.88, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 4.15, "price": 1.27, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.48, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.08, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.48, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.48, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 4.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 7.03, "price": 1.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 6.16, "price": 1.08, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 6.33, "price": 1.09, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.43, "price": 1.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.64, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.41, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.14, "price": 5.43, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.08, "price": 6.16, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.09, "price": 6.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:26Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.06, "price": 7.03, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 2.90 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Unibet (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.48 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | -2.7% |
| Draw probability edge | +1.3% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -1.2% |
| Under 2.5 probability edge | +1.2% |
| Raw edge prob home | -0.0546 |
| Raw ev home | -0.1341 |
| Raw edge prob draw | 0.0256 |
| Raw ev draw | 0.0213 |
| Raw edge prob away | 0.0291 |
| Raw ev away | 0.0773 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 10.311435294722774, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,558.0873 |
| Elo away rating | 1,540.2938 |
| Elo rating diff | 77.7935 |
| Elo home expectancy | 0.6101 |
| Market p home draw | 69.8% |
| Market home draw odds | 1.37 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:16:19Z |
| Market reference home draw last update utc | 2026-10-25T10:16:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 54.5% |
| Market draw away odds | 1.78 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:16:19Z |
| Market reference draw away last update utc | 2026-10-25T10:16:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 75.8% |
| Market home away odds | 1.30 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:16:19Z |
| Market reference home away last update utc | 2026-10-25T10:16:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.39 |
| Market reference dc draw away odds | 1.78 |
| Market reference dc home away odds | 1.28 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.22, "price": 1.67, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.67, "price": 2.22, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.77, "price": 2.07, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.07, "price": 1.77, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 85.5% |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.07 |
| Market reference over 1 5 last update utc | 2026-10-25T10:16:26Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 59.2% |
| Market under 3 5 odds | 1.62 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market reference under 3 5 odds | 1.67 |
| Market reference under 3 5 opposite odds | 2.40 |
| Market reference under 3 5 last update utc | 2026-10-25T10:16:26Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 65.8% |
| Market btts yes odds | 1.51 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:16:19Z |
| Market reference btts yes odds | 1.45 |
| Market reference btts yes opposite odds | 2.59 |
| Market reference btts yes last update utc | 2026-10-25T10:16:21Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Manchester United vs Bournemouth

The model's most likely 1X2 outcome is **Manchester United win** at **46.0%**. Expected goals are 1.77 for Manchester United and 1.27 for Bournemouth (3.05 combined). The most likely exact score is 1-1 at 11.6%. Goal-market probabilities: at least one goal: 94.3%; Over 2.5 goals: 58.7%; Under 3.5 goals: 63.8%; Double Chance 1X: 71.1%; Double Chance X2: 54.0%; Double Chance 12 (either team wins): 74.9%; Under 4.5 goals: 80.8%; BTTS Yes (both teams score): 60.8%; BTTS No (at least one team does not score): 39.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Manchester United win | 46.0% | 2.17 |
| Draw | 25.1% | 3.99 |
| Bournemouth win | 28.9% | 3.46 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Manchester United expected goals | 1.77 |
| Bournemouth expected goals | 1.27 |
| Expected total goals | 3.05 |
| Over 0.5 | 94.3% |
| Under 0.5 | 5.7% |
| Over 1.5 | 81.7% |
| Under 1.5 | 18.3% |
| Over 2.5 | 58.7% |
| Under 2.5 | 41.3% |
| Over 3.5 | 36.2% |
| Under 3.5 | 63.8% |
| Over 4.5 | 19.2% |
| Under 4.5 | 80.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.63% |
| 2 | 2-1 | 9.09% |
| 3 | 1-2 | 7.44% |
| 4 | 2-0 | 7.14% |
| 5 | 1-0 | 7.11% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Manchester United win | 46.0% | 43.9% | 2.21 | +1.7% |
| Draw | 25.1% | 24.9% | 3.71 | -7.0% |
| Bournemouth win | 28.9% | 31.3% | 3.21 | -7.2% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Man United |
| Matched away-team name | Bournemouth |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7726 |
| Dc lambda away | 1.2734 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 60.8% |
| P btts no | 39.2% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 17.56 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.46 |
| Fair Over 2.5 odds | 1.70 |
| Fair Under 2.5 odds | 2.42 |
| Fair Over 3.5 odds | 2.76 |
| Fair Under 3.5 odds | 1.57 |
| Fair Over 4.5 odds | 5.20 |
| Fair Under 4.5 odds | 1.24 |
| Goal margin distribution | {"-1": 0.16340927599326352, "-10": 1.959809313364996e-07, "-11": 2.2312026978607386e-08, "-12": 2.334384969378549e-09, "-13": 2.2589360748486797e-10, "-14": 2.032263892281748e-11, "-15": 1.6955628432666017e-12, "-16": 1.1826473979916636e-13, "-2": 0.08389798986540141, "-3": 0.030433671960963957, "-4": 0.008765584945437681, "-5": 0.002083434349211214, "-6": 0.00042044207060304775, "-7": 7.360790894099974e-05, "-8": 1.1369034164836305e-05, "-9": 1.5700445468115705e-06, "0": 0.25072741969833223, "1": 0.2034024463970868, "10": 4.700109964151433e-06, "11": 7.448585081533882e-07, "12": 1.0847952865703712e-07, "13": 1.4612341291121705e-08, "14": 1.8299386162833063e-09, "15": 2.125254119022716e-10, "16": 2.0634445898909665e-11, "2": 0.14273198929164438, "3": 0.07207168455290477, "4": 0.028895603909418238, "5": 0.009560293991449456, "6": 0.002685580337995092, "7": 0.0006544809614581217, "8": 0.00014071379099590213, "9": 2.7049897367505683e-05} |
| Raw goal margin distribution | {"-1": 0.15016638148339623, "-10": 1.8009838866039224e-07, "-11": 2.0503832077901804e-08, "-12": 2.1452034574540097e-09, "-13": 2.075869036812308e-10, "-14": 1.8675666547588977e-11, "-15": 1.5581522848283162e-12, "-16": 1.0868041562982221e-13, "-2": 0.07709879059948438, "-3": 0.02796728867349644, "-4": 0.008055210849205241, "-5": 0.0019145901931060525, "-6": 0.0003863689131604073, "-7": 6.764263085459686e-05, "-8": 1.0447673249375107e-05, "-9": 1.4428061499529054e-06, "0": 0.25268251721414564, "1": 0.2128940523013345, "10": 4.9194366845354234e-06, "11": 7.796167106187404e-07, "12": 1.1354163559296378e-07, "13": 1.5294214038133463e-08, "14": 1.915331179068993e-09, "15": 2.2244273340034374e-10, "16": 2.1597335146281942e-11, "2": 0.14939245880065316, "3": 0.07543484973969883, "4": 0.030243993221009954, "5": 0.01000641715517206, "6": 0.002810900709721019, "7": 0.000685021770912627, "8": 0.00014728008296083946, "9": 2.831215831918315e-05} |
| Unadjusted home-win probability | 48.2% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 26.6% |
| Raw p over 1 5 | 81.7% |
| Raw p under 3 5 | 63.7% |
| Raw p btts yes | 60.8% |
| P home draw | 71.1% |
| P draw away | 54.0% |
| P home away | 74.9% |
| Raw p home draw | 73.4% |
| Raw p draw away | 51.8% |
| Raw p home away | 74.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.82, "price": 2.13, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.13, "price": 1.82, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 8.35, "price": 1.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 7.85, "price": 1.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 5.63, "price": 1.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.91, "price": 1.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 4.34, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 4.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.12, "price": 5.63, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.05, "price": 7.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-25T10:16:05Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.04, "price": 8.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 4.42, "price": 1.24, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 3.94, "price": 1.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.73, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.98, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.45, "price": 1.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.17, "price": 1.77, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.77, "price": 2.17, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.58, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.94, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.24, "price": 4.42, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.10 |
| Reference draw odds | 3.50 |
| Reference away odds | 2.85 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 1.57 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | +2.1% |
| Draw probability edge | +0.2% |
| Away probability edge | -2.3% |
| Over 2.5 probability edge | -2.2% |
| Under 2.5 probability edge | +2.2% |
| Raw edge prob home | 0.0429 |
| Raw ev home | 0.0644 |
| Raw edge prob draw | 0.0039 |
| Raw ev draw | -0.0625 |
| Raw edge prob away | -0.0469 |
| Raw ev away | -0.1472 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 10.260798734512269, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,529.3488 |
| Elo away rating | 1,499.8325 |
| Elo rating diff | 89.5163 |
| Elo home expectancy | 0.6260 |
| Market p home draw | 67.3% |
| Market home draw odds | 1.43 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:16:19Z |
| Market reference home draw last update utc | 2026-10-25T10:16:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 59.8% |
| Market draw away odds | 1.60 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:16:19Z |
| Market reference draw away last update utc | 2026-10-25T10:16:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.9% |
| Market home away odds | 1.35 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:16:19Z |
| Market reference home away last update utc | 2026-10-25T10:16:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.44 |
| Market reference dc draw away odds | 1.62 |
| Market reference dc home away odds | 1.33 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 1.69, "price": 2.18, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:19Z", "line": 10.5, "market_key": "alternate_totals_corners", "opposite_price": 2.18, "price": 1.69, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 79.8% |
| Market reference over 1 5 odds | 1.22 |
| Market reference over 1 5 opposite odds | 4.09 |
| Market reference over 1 5 last update utc | 2026-10-25T10:16:05Z |
| Market over 1 5 bookmakers | 0 |
| Market p under 3 5 | 68.6% |
| Market under 3 5 odds | 1.42 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market reference under 3 5 odds | 1.42 |
| Market reference under 3 5 opposite odds | 2.94 |
| Market reference under 3 5 last update utc | 2026-10-25T10:16:21Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 60.7% |
| Market btts yes odds | 1.64 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:16:19Z |
| Market reference btts yes odds | 1.56 |
| Market reference btts yes opposite odds | 2.30 |
| Market reference btts yes last update utc | 2026-10-25T10:16:21Z |
| Market btts yes bookmakers | 1 |

</details>


---

## 2026-10-25 — Sunderland vs Leeds United

The model's most likely 1X2 outcome is **Leeds United win** at **38.1%**. Expected goals are 1.07 for Sunderland and 1.21 for Leeds United (2.29 combined). The most likely exact score is 1-1 at 13.9%. Goal-market probabilities: at least one goal: 89.0%; Over 2.5 goals: 40.4%; Under 3.5 goals: 80.2%; Double Chance 1X: 61.9%; Double Chance X2: 67.8%; Double Chance 12 (either team wins): 70.3%; Under 4.5 goals: 91.7%; BTTS Yes (both teams score): 47.2%; BTTS No (at least one team does not score): 52.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Sunderland win | 32.2% | 3.11 |
| Draw | 29.7% | 3.36 |
| Leeds United win | 38.1% | 2.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Sunderland expected goals | 1.07 |
| Leeds United expected goals | 1.21 |
| Expected total goals | 2.29 |
| Over 0.5 | 89.0% |
| Under 0.5 | 11.0% |
| Over 1.5 | 67.9% |
| Under 1.5 | 32.1% |
| Over 2.5 | 40.4% |
| Under 2.5 | 59.6% |
| Over 3.5 | 19.8% |
| Under 3.5 | 80.2% |
| Over 4.5 | 8.3% |
| Under 4.5 | 91.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.94% |
| 2 | 0-1 | 11.12% |
| 3 | 0-0 | 10.98% |
| 4 | 1-0 | 10.04% |
| 5 | 1-2 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Sunderland win | 32.2% | 33.4% | 3.01 | -3.1% |
| Draw | 29.7% | 28.6% | 3.24 | -3.7% |
| Leeds United win | 38.1% | 38.0% | 2.55 | -2.9% |

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
| Market best home last update utc | 2026-10-24T14:42:23Z |
| Market best draw last update utc | 2026-10-24T14:42:23Z |
| Market best away last update utc | 2026-10-24T14:42:23Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 17.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Sunderland |
| Matched away-team name | Leeds |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0712 |
| Dc lambda away | 1.2146 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_PAIRED_AUDIT |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-25T10:16:28.509803+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 47.2% |
| P btts no | 52.8% |
| Fair Over 0.5 odds | 1.12 |
| Fair Under 0.5 odds | 9.11 |
| Fair Over 1.5 odds | 1.47 |
| Fair Under 1.5 odds | 3.11 |
| Fair Over 2.5 odds | 2.48 |
| Fair Under 2.5 odds | 1.68 |
| Fair Over 3.5 odds | 5.04 |
| Fair Under 3.5 odds | 1.25 |
| Fair Over 4.5 odds | 12.05 |
| Fair Under 4.5 odds | 1.09 |
| Goal margin distribution | {"-1": 0.2107673943176832, "-10": 2.1987808982051056e-07, "-11": 2.4043553183477474e-08, "-12": 2.413341838302594e-09, "-13": 2.2307334285642782e-10, "-14": 1.7707672424828976e-11, "-2": 0.11310605205809388, "-3": 0.041552596754879115, "-4": 0.011876137720422978, "-5": 0.002768432416284222, "-6": 0.0005439516747309842, "-7": 9.227751275578852e-05, "-8": 1.3764877602619047e-05, "-9": 1.8314869028514251e-06, "0": 0.29723135751896185, "1": 0.19168702624975517, "10": 6.504297512960668e-08, "11": 6.27259601811977e-09, "12": 5.552617252441246e-10, "13": 4.52644031605326e-11, "14": 3.168843775559512e-12, "2": 0.09142447447259659, "3": 0.029621362095518716, "4": 0.007466418133062764, "5": 0.0015349747468788471, "6": 0.0002659854338370705, "7": 3.9794554081885176e-05, "8": 5.235164627301039e-06, "9": 6.143162921474476e-07} |
| Raw goal margin distribution | {"-1": 0.21116645096960646, "-10": 2.2029439621666405e-07, "-11": 2.408907606838478e-08, "-12": 2.4179111414296598e-09, "-13": 2.234956989880382e-10, "-14": 1.774119926371258e-11, "-2": 0.11332020151224771, "-3": 0.041631270404536375, "-4": 0.011898623417377359, "-5": 0.0027736740305039855, "-6": 0.0005449815661657049, "-7": 9.245222647470763e-05, "-8": 1.3790939347074429e-05, "-9": 1.8349545503680596e-06, "0": 0.30808395025908114, "1": 0.1847983286075853, "10": 6.270551182715427e-08, "11": 6.047176394028957e-09, "12": 5.353071659173363e-10, "13": 4.3637726627297035e-11, "14": 3.054964359345608e-12, "2": 0.08813893358828338, "3": 0.028556852873285844, "4": 0.00719809586840585, "5": 0.0014798120312455136, "6": 0.0002564266584375419, "7": 3.836444868436126e-05, "8": 5.047027396889464e-06, "9": 5.922394762248674e-07} |
| Unadjusted home-win probability | 31.0% |
| Unadjusted draw probability | 30.8% |
| Unadjusted away-win probability | 38.1% |
| Raw p over 1 5 | 67.8% |
| Raw p under 3 5 | 80.2% |
| Raw p btts yes | 47.4% |
| P home draw | 61.9% |
| P draw away | 67.8% |
| P home away | 70.3% |
| Raw p home draw | 61.9% |
| Raw p draw away | 69.0% |
| Raw p home away | 69.2% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.15, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-24T14:42:00Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.81, "price": 2.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.07, "price": 1.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.07, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 5.6, "price": 1.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.74, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.96, "price": 1.45, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.66, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.52, "price": 1.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.71, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.71, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.59, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.66, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-25T10:16:21Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.18, "price": 5.6, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.70 |
| Reference draw odds | 3.10 |
| Reference away odds | 2.40 |
| Market reference 1x2 last update utc | 2026-10-24T14:42:25Z |
| Market reference home last update utc | 2026-10-24T14:42:25Z |
| Market reference draw last update utc | 2026-10-24T14:42:25Z |
| Market reference away last update utc | 2026-10-24T14:42:25Z |
| O/U 2.5 market source | The Odds API / Tipico |
| Reference Over 2.5 odds | 2.05 |
| Reference Under 2.5 odds | 1.72 |
| Market reference over 2 5 last update utc | 2026-10-24T14:42:23Z |
| Market reference under 2 5 last update utc | 2026-10-24T14:42:23Z |
| Home probability edge | -1.2% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | -4.8% |
| Under 2.5 probability edge | +4.8% |
| Raw edge prob home | -0.0231 |
| Raw ev home | -0.0655 |
| Raw edge prob draw | 0.0217 |
| Raw ev draw | -0.0018 |
| Raw edge prob away | 0.0014 |
| Raw ev away | -0.0273 |
| Count model | {"corners": {"alpha": 0.009339470740713493, "mu": 9.537692996453805, "version": "count-markets-nb2-v1"}} |
| Elo home rating | 1,421.3554 |
| Elo away rating | 1,454.8163 |
| Elo rating diff | 26.5391 |
| Elo home expectancy | 0.5381 |
| Market p home draw | 63.4% |
| Market home draw odds | 1.53 |
| Best home draw bookmaker | Pinnacle |
| Market best home draw last update utc | 2026-10-25T10:16:18Z |
| Market reference home draw last update utc | 2026-10-25T10:16:21Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 67.3% |
| Market draw away odds | 1.44 |
| Best draw away bookmaker | Pinnacle |
| Market best draw away last update utc | 2026-10-25T10:16:18Z |
| Market reference draw away last update utc | 2026-10-25T10:16:21Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 69.3% |
| Market home away odds | 1.40 |
| Best home away bookmaker | Pinnacle |
| Market best home away last update utc | 2026-10-25T10:16:18Z |
| Market reference home away last update utc | 2026-10-25T10:16:21Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.53 |
| Market reference dc draw away odds | 1.44 |
| Market reference dc home away odds | 1.40 |
| Count market offers | [{"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:18Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 2.24, "price": 1.65, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:18Z", "line": 8.5, "market_key": "alternate_totals_corners", "opposite_price": 1.65, "price": 2.24, "quote_source": "The Odds API", "side": "Under"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:18Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 1.75, "price": 2.09, "quote_source": "The Odds API", "side": "Over"}, {"bookmaker": "Pinnacle", "kind": "corners", "last_update_utc": "2026-10-25T10:16:18Z", "line": 9.5, "market_key": "alternate_totals_corners", "opposite_price": 2.09, "price": 1.75, "quote_source": "The Odds API", "side": "Under"}] |
| Market p over 1 5 | 70.5% |
| Market over 1 5 odds | 1.39 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-25T10:16:21Z |
| Market reference over 1 5 odds | 1.39 |
| Market reference over 1 5 opposite odds | 3.15 |
| Market reference over 1 5 last update utc | 2026-10-25T10:16:21Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 78.3% |
| Market reference under 3 5 odds | 1.23 |
| Market reference under 3 5 opposite odds | 3.65 |
| Market reference under 3 5 last update utc | 2026-10-25T10:15:40Z |
| Market under 3 5 bookmakers | 0 |
| Market p btts yes | 50.3% |
| Market btts yes odds | 1.89 |
| Best btts yes bookmaker | Pinnacle |
| Market best btts yes last update utc | 2026-10-25T10:16:18Z |
| Market reference btts yes odds | 1.85 |
| Market reference btts yes opposite odds | 1.87 |
| Market reference btts yes last update utc | 2026-10-25T10:16:21Z |
| Market btts yes bookmakers | 1 |

</details>


---
