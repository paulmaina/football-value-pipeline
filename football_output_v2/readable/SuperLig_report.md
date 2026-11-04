# Super Lig — football model report

Fixtures in this report: **5**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,840 |
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
| Training sha256 | 428b36b889bc8107b0a0c389334f72426054f163962dc5b037f54c55da735d9c |
| Training as of utc | 2026-11-04T19:40:48.254461+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-04', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-05', 'audit_start_date': '2026-05-06', 'training_shot_matches': 1512, 'tuning_matches': 189, 'audit_matches': 91, 'audit_matchdays': 37, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.8325808781597445, 'audit_candidate_poisson_score': 0.8249955374677742, 'audit_gain': 0.007585340691970255, 'audit_gain_lower95': -0.0033625185473820135, 'audit_baseline_briers': [0.5922711615757454, 0.16649579451704555, 0.22016577620350214, 0.2497311353345134], 'audit_candidate_briers': [0.5911122360258325, 0.16508071200426702, 0.21632094488190387, 0.24937852775967387], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'bootstrap_lower95_not_positive']} |
| Optimizer objective | 1673.871 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.097 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 2, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 5.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 19.00 |
| Over 1 5 in window quote fixtures | 1 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 1.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 1.00 |
| Totals anchor fixtures | {'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 3} |
| Shot features applied fixtures | 0 |
| Goal rate features used | {'none': 5} |
| Legacy comparison status | {'None': 5} |
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

## 2026-11-06 — Gazişehir Gaziantep vs Kasimpasa SK

The model's most likely 1X2 outcome is **Gazişehir Gaziantep win** at **36.9%**. Expected goals are 1.39 for Gazişehir Gaziantep and 1.41 for Kasimpasa SK (2.81 combined). The most likely exact score is 1-1 at 13.3%. Goal-market probabilities: at least one goal: 92.2%; Over 2.5 goals: 51.0%; Under 3.5 goals: 71.2%; Double Chance 1X: 64.7%; Double Chance X2: 63.1%; Double Chance 12 (either team wins): 72.2%; Under 4.5 goals: 86.1%; BTTS Yes (both teams score): 56.2%; BTTS No (at least one team does not score): 43.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 2.71 |
| Draw | 27.8% | 3.59 |
| Kasimpasa SK win | 35.3% | 2.83 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Gazişehir Gaziantep expected goals | 1.39 |
| Kasimpasa SK expected goals | 1.41 |
| Expected total goals | 2.81 |
| Over 0.5 | 92.2% |
| Under 0.5 | 7.8% |
| Over 1.5 | 76.5% |
| Under 1.5 | 23.5% |
| Over 2.5 | 51.0% |
| Under 2.5 | 49.0% |
| Over 3.5 | 28.8% |
| Under 3.5 | 71.2% |
| Over 4.5 | 13.9% |
| Under 4.5 | 86.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.27% |
| 2 | 2-1 | 8.54% |
| 3 | 1-2 | 8.08% |
| 4 | 1-0 | 8.08% |
| 5 | 0-0 | 7.76% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Gazişehir Gaziantep win | 36.9% | 37.4% | 2.61 | -3.8% |
| Draw | 27.8% | 28.0% | 3.46 | -3.6% |
| Kasimpasa SK win | 35.3% | 34.7% | 2.79 | -1.5% |
| Over 2.5 | 51.0% | 51.0% | 1.93 | -1.6% |
| Under 2.5 | 49.0% | 49.0% | 1.95 | -4.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-06T17:00:00+00:00 |
| Fixture id | 51baab3ec98943f452377895491bfd6a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:42Z |
| Market best draw last update utc | 2026-11-04T19:40:42Z |
| Market best away last update utc | 2026-11-04T19:40:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Gaziantep |
| Matched away-team name | Kasimpasa |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3919 |
| Dc lambda away | 1.4143 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 56.2% |
| P btts no | 43.8% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 12.89 |
| Fair Over 1.5 odds | 1.31 |
| Fair Under 1.5 odds | 4.26 |
| Fair Over 2.5 odds | 1.96 |
| Fair Under 2.5 odds | 2.04 |
| Fair Over 3.5 odds | 3.47 |
| Fair Under 3.5 odds | 1.40 |
| Fair Over 4.5 odds | 7.20 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1862727327419943, "-10": 4.732339682924109e-07, "-11": 5.7957324386427116e-08, "-12": 6.518011157653578e-09, "-13": 6.732362062757331e-10, "-14": 5.8061983634475924e-11, "-2": 0.1064470503868342, "-3": 0.04247913106238756, "-4": 0.013346539284259815, "-5": 0.003443378691218151, "-6": 0.0007519330678085535, "-7": 0.00014215744285260145, "-8": 2.3676539344703442e-05, "-9": 3.522145306510485e-06, "0": 0.2784739458376355, "1": 0.19666393242003286, "10": 4.331755824831387e-07, "11": 5.2210909885209157e-08, "12": 5.778736734233442e-09, "13": 5.874219221722583e-10, "14": 4.985852555075159e-11, "2": 0.11071403544835273, "3": 0.043482003783018086, "4": 0.01344520629890189, "5": 0.003413881678475369, "6": 0.0007336817859411743, "7": 0.0001365095491058729, "8": 2.2375694817894445e-05, "9": 3.275898600566125e-06} |
| Raw goal margin distribution | {"-1": 0.1907270954801859, "-10": 6.368710556228424e-07, "-11": 8.069345133122967e-08, "-12": 9.389290608514803e-09, "-13": 1.002605774303582e-09, "-14": 8.879782026856271e-11, "-2": 0.11125399100186605, "-3": 0.0456016881979012, "-4": 0.014756775287774544, "-5": 0.003927514114313424, "-6": 0.0008856348189776695, "-7": 0.00017301098162622475, "-8": 2.9788531598095093e-05, "-9": 4.5825540415531875e-06, "0": 0.27542988606089935, "1": 0.1875237329181577, "10": 5.428755376975547e-07, "11": 6.769427292460506e-08, "12": 7.75195591493991e-09, "13": 8.146547436310594e-10, "14": 7.100853791512926e-11, "2": 0.10775696515613241, "3": 0.04346858959200438, "4": 0.013843661398834578, "5": 0.0036261196885041137, "6": 0.0008047184139237471, "7": 0.00015471335458904954, "8": 2.621610116493534e-05, "9": 3.969094874167381e-06} |
| Unadjusted home-win probability | 35.7% |
| Unadjusted draw probability | 27.5% |
| Unadjusted away-win probability | 36.7% |
| Raw p over 1 5 | 78.1% |
| Raw p under 3 5 | 69.1% |
| Raw p btts yes | 58.0% |
| P home draw | 64.7% |
| P draw away | 63.1% |
| P home away | 72.2% |
| Raw p home draw | 63.3% |
| Raw p draw away | 64.3% |
| Raw p home away | 72.5% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9657 |
| Totals anchor target over 2 5 | 0.5098 |
| Totals anchor reference over odds | 1.88 |
| Totals anchor reference under odds | 1.95 |
| Totals anchor reference last update utc | 2026-11-04T19:40:43Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5309 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.8, "price": 1.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.26, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.39, "price": 1.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.74, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.56, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.86, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.61, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.74, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.33, "price": 3.39, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.26, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.19, "price": 4.8, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.79, "draw": 3.46, "home": 2.61}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.93, "under": 1.95}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.53, "home_away": 1.34, "home_draw": 1.48}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.76, "draw": 3.39, "home": 2.57}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.88, "under": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.88, "under": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.27, "under": 3.76}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.39 |
| Reference away odds | 2.76 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:43Z |
| Market reference home last update utc | 2026-11-04T19:40:43Z |
| Market reference draw last update utc | 2026-11-04T19:40:43Z |
| Market reference away last update utc | 2026-11-04T19:40:43Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.88 |
| Reference Under 2.5 odds | 1.95 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:43Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Home probability edge | -0.5% |
| Draw probability edge | -0.1% |
| Away probability edge | +0.6% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0163 |
| Raw ev home | -0.0677 |
| Raw edge prob draw | -0.0043 |
| Raw ev draw | -0.0470 |
| Raw edge prob away | 0.0206 |
| Raw ev away | 0.0249 |
| Market p home draw | 65.1% |
| Market home draw odds | 1.48 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-04T19:40:42Z |
| Market reference home draw last update utc | 2026-11-04T19:40:42Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.0% |
| Market draw away odds | 1.53 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-04T19:40:42Z |
| Market reference draw away last update utc | 2026-11-04T19:40:42Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market home away odds | 1.34 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-04T19:40:42Z |
| Market reference home away last update utc | 2026-11-04T19:40:42Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.48 |
| Market reference dc draw away odds | 1.53 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 75.3% |
| Market over 1 5 odds | 1.27 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-04T19:40:43Z |
| Market reference over 1 5 odds | 1.29 |
| Market reference over 1 5 opposite odds | 3.51 |
| Market reference over 1 5 last update utc | 2026-11-04T19:40:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 72.3% |
| Market under 3 5 odds | 1.35 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-04T19:40:43Z |
| Market reference under 3 5 odds | 1.34 |
| Market reference under 3 5 opposite odds | 3.19 |
| Market reference under 3 5 last update utc | 2026-11-04T19:40:47Z |
| Market under 3 5 bookmakers | 1 |
| Elo home rating | 1,396.7846 |
| Elo away rating | 1,500.7901 |
| Elo rating diff | -44.0056 |
| Elo home expectancy | 0.4370 |

</details>


---

## 2026-11-07 — Eyüpspor vs Kocaelispor

The model's most likely 1X2 outcome is **Kocaelispor win** at **43.1%**. Expected goals are 0.80 for Eyüpspor and 0.87 for Kocaelispor (1.67 combined). The most likely exact score is 0-1 at 19.5%. Goal-market probabilities: at least one goal: 83.2%; Over 2.5 goals: 25.1%; Under 3.5 goals: 90.9%; Double Chance 1X: 56.9%; Double Chance X2: 74.0%; Double Chance 12 (either team wins): 69.1%; Under 4.5 goals: 97.0%; BTTS Yes (both teams score): 32.0%; BTTS No (at least one team does not score): 68.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Eyüpspor win | 26.0% | 3.85 |
| Draw | 30.9% | 3.23 |
| Kocaelispor win | 43.1% | 2.32 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Eyüpspor expected goals | 0.80 |
| Kocaelispor expected goals | 0.87 |
| Expected total goals | 1.67 |
| Over 0.5 | 83.2% |
| Under 0.5 | 16.8% |
| Over 1.5 | 51.5% |
| Under 1.5 | 48.5% |
| Over 2.5 | 25.1% |
| Under 2.5 | 74.9% |
| Over 3.5 | 9.1% |
| Under 3.5 | 90.9% |
| Over 4.5 | 3.0% |
| Under 4.5 | 97.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 0-1 | 19.46% |
| 2 | 0-0 | 16.85% |
| 3 | 1-0 | 12.15% |
| 4 | 1-1 | 12.01% |
| 5 | 0-2 | 9.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Eyüpspor win | 26.0% | 24.5% | 3.84 | -0.2% |
| Draw | 30.9% | 28.3% | 3.46 | +7.0% |
| Kocaelispor win | 43.1% | 47.2% | 2.09 | -9.9% |
| Over 2.5 | 25.1% | 43.6% | 2.21 | -44.6% |
| Under 2.5 | 74.9% | 56.4% | 1.73 | +29.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T10:30:00+00:00 |
| Fixture id | a3dad1ddaa98a6ff741be7f63250f2ee |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:43Z |
| Market best draw last update utc | 2026-11-04T19:40:42Z |
| Market best away last update utc | 2026-11-04T19:40:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 13.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Eyupspor |
| Matched away-team name | Kocaelispor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.7986 |
| Dc lambda away | 0.8688 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 12 |
| Score grid omitted mass | 0 |
| P btts yes | 32.0% |
| P btts no | 68.0% |
| Fair Over 0.5 odds | 1.20 |
| Fair Under 0.5 odds | 5.94 |
| Fair Over 1.5 odds | 1.94 |
| Fair Under 1.5 odds | 2.06 |
| Fair Over 2.5 odds | 3.99 |
| Fair Under 2.5 odds | 1.33 |
| Fair Over 3.5 odds | 11.00 |
| Fair Under 3.5 odds | 1.10 |
| Fair Over 4.5 odds | 33.47 |
| Fair Under 4.5 odds | 1.03 |
| Goal margin distribution | {"-1": 0.27677057448712966, "-10": 1.745895540987433e-08, "-11": 1.369817816523661e-09, "-12": 9.37571439955454e-11, "-2": 0.1147292568354253, "-3": 0.03146698960490544, "-4": 0.006610626967380946, "-5": 0.0011231420774261037, "-6": 0.00016002484140837387, "-7": 1.9621226492225275e-05, "-8": 2.110750136363847e-06, "-9": 2.022151905855133e-07, "0": 0.309124074383664, "1": 0.17315300954614968, "10": 5.140830183733344e-09, "11": 3.707334431630127e-10, "12": 2.3323153760820983e-11, "2": 0.06631588479560899, "3": 0.01671793130832172, "4": 0.0032281517539768873, "5": 0.00050411537286592, "6": 6.601864412063735e-05, "7": 7.440280312817379e-06, "8": 7.356714881382495e-07, "9": 6.478057933561426e-08} |
| Raw goal margin distribution | {"-1": 0.2152002334767592, "-10": 1.357503877508481e-08, "-11": 1.0650883479313815e-09, "-12": 7.289994362783588e-11, "-2": 0.08920660335134982, "-3": 0.024466847757695066, "-4": 0.005140027871258743, "-5": 0.0008732880572205096, "-6": 0.00012442573888852773, "-7": 1.5256291352690762e-05, "-8": 1.6411929736328377e-06, "-9": 1.5723042923615936e-07, "0": 0.36950409019294744, "1": 0.1967783809311239, "10": 5.8422561805215485e-09, "11": 4.2131711654249267e-10, "12": 2.6505415339251094e-11, "2": 0.0753641676474404, "3": 0.018998962039366105, "4": 0.003668607766117023, "5": 0.0005728979654183054, "6": 7.502637081144489e-05, "7": 8.455448262016512e-06, "8": 8.3604809822524e-07, "9": 7.361938178755642e-08} |
| Unadjusted home-win probability | 29.5% |
| Unadjusted draw probability | 37.0% |
| Unadjusted away-win probability | 33.5% |
| Raw p over 1 5 | 50.9% |
| Raw p under 3 5 | 91.2% |
| Raw p btts yes | 33.2% |
| P home draw | 56.9% |
| P draw away | 74.0% |
| P home away | 69.1% |
| Raw p home draw | 66.5% |
| Raw p draw away | 70.5% |
| Raw p home away | 63.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.2507 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.05, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.7, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.51, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.05, "price": 1.81, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.09, "draw": 3.46, "home": 3.81}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 2.21, "under": 1.73}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 2.05, "draw": 3.34, "home": 3.84}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 3.84 |
| Reference draw odds | 3.34 |
| Reference away odds | 2.05 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:43Z |
| Market reference home last update utc | 2026-11-04T19:40:43Z |
| Market reference draw last update utc | 2026-11-04T19:40:43Z |
| Market reference away last update utc | 2026-11-04T19:40:43Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 2.21 |
| Reference Under 2.5 odds | 1.73 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Home probability edge | +1.5% |
| Draw probability edge | +2.6% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -18.6% |
| Under 2.5 probability edge | +18.6% |
| Raw edge prob home | 0.0507 |
| Raw ev home | 0.1346 |
| Raw edge prob draw | 0.0863 |
| Raw ev draw | 0.2785 |
| Raw edge prob away | -0.1369 |
| Raw ev away | -0.2998 |
| Elo home rating | 1,370.1212 |
| Elo away rating | 1,438.4311 |
| Elo rating diff | -8.3099 |
| Elo home expectancy | 0.4880 |

</details>


---

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.6%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 97.3%; Over 2.5 goals: 73.5%; Under 3.5 goals: 47.6%; Double Chance 1X: 83.3%; Double Chance X2: 35.4%; Double Chance 12 (either team wins): 81.3%; Under 4.5 goals: 66.8%; BTTS Yes (both teams score): 69.4%; BTTS No (at least one team does not score): 30.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.6% | 1.55 |
| Draw | 18.7% | 5.35 |
| Amed SK win | 16.7% | 5.98 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 97.3% |
| Under 0.5 | 2.7% |
| Over 1.5 | 89.9% |
| Under 1.5 | 10.1% |
| Over 2.5 | 73.5% |
| Under 2.5 | 26.5% |
| Over 3.5 | 52.4% |
| Under 3.5 | 47.6% |
| Over 4.5 | 33.2% |
| Under 4.5 | 66.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.92% |
| 2 | 3-1 | 8.06% |
| 3 | 1-1 | 7.51% |
| 4 | 2-0 | 7.15% |
| 5 | 3-2 | 6.16% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.6% | 69.8% | 1.45 | -6.3% |
| Draw | 18.7% | 17.3% | 5.15 | -3.7% |
| Amed SK win | 16.7% | 12.9% | 6.79 | +13.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | e300554369b00b495db88afb743c95ab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:42Z |
| Market best draw last update utc | 2026-11-04T19:40:42Z |
| Market best away last update utc | 2026-11-04T19:40:43Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2143 |
| Dc lambda away | 1.5277 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.4% |
| P btts no | 30.6% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 37.23 |
| Fair Over 1.5 odds | 1.11 |
| Fair Under 1.5 odds | 9.95 |
| Fair Over 2.5 odds | 1.36 |
| Fair Under 2.5 odds | 3.77 |
| Fair Over 3.5 odds | 1.91 |
| Fair Under 3.5 odds | 2.10 |
| Fair Over 4.5 odds | 3.01 |
| Fair Under 4.5 odds | 1.50 |
| Goal margin distribution | {"-1": 0.08862757892949215, "-10": 3.99838105628071e-07, "-11": 5.4170944011313354e-08, "-12": 6.752615481730266e-09, "-13": 7.792762873311447e-10, "-14": 8.3700968036751e-11, "-15": 8.398723897909157e-12, "-16": 7.801416634432503e-13, "-17": 5.847210939985141e-14, "-2": 0.049244932227896776, "-3": 0.02015089783573139, "-4": 0.006674319038591221, "-5": 0.0018458614649814818, "-6": 0.0004367334077660595, "-7": 9.010693412690756e-05, "-8": 1.6460894013833634e-05, "-9": 2.6957723010668583e-06, "0": 0.18696350719501012, "1": 0.24656190640269626, "10": 3.0858699788280635e-05, "11": 6.0597296552400325e-06, "12": 1.0948440654951813e-06, "13": 1.831323687712981e-07, "14": 2.8510020898019872e-08, "15": 4.146424503784169e-09, "16": 5.582482022105144e-10, "17": 6.064514317699549e-11, "2": 0.19512268393192983, "3": 0.11572682048162768, "4": 0.05555715343304613, "5": 0.02227027243504818, "6": 0.007637236579737402, "7": 0.002283870347515141, "8": 0.0006047279678043516, "9": 0.00014354340558772897} |
| Raw goal margin distribution | {"-1": 0.13585594995036526, "-10": 6.129061215772438e-07, "-11": 8.30378663984475e-08, "-12": 1.0350987830208413e-08, "-13": 1.1945414911242358e-09, "-14": 1.2830401847538234e-10, "-15": 1.2874283911433724e-11, "-16": 1.195868013807068e-12, "-17": 8.963106139273184e-14, "-2": 0.07548685328959162, "-3": 0.03088902349463892, "-4": 0.01023096833076059, "-5": 0.0028294946768356805, "-6": 0.0006694624032810441, "-7": 0.0001381236324041393, "-8": 2.523266933716819e-05, "-9": 4.132310858933432e-06, "0": 0.21888507032812346, "1": 0.20039013897586855, "10": 2.5080026470465912e-05, "11": 4.924970306590975e-06, "12": 8.898209688692005e-07, "13": 1.488385670133638e-07, "14": 2.317116676015709e-08, "15": 3.369955216071327e-09, "16": 4.537093197247052e-10, "17": 4.928858981809315e-11, "2": 0.15858354731652216, "3": 0.094055541579375, "4": 0.045153389102080776, "5": 0.018099888394766877, "6": 0.006207069542630813, "7": 0.0018561873690007276, "8": 0.000491485174165507, "9": 0.00011666312697880698} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 83.3% |
| P draw away | 35.4% |
| P home away | 81.3% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.7348 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 1.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.79, "draw": 5.15, "home": 1.4}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.40 |
| Reference draw odds | 5.15 |
| Reference away odds | 6.79 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:43Z |
| Market reference home last update utc | 2026-11-04T19:40:43Z |
| Market reference draw last update utc | 2026-11-04T19:40:43Z |
| Market reference away last update utc | 2026-11-04T19:40:43Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.76 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:46Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:46Z |
| Home probability edge | -5.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +3.8% |
| Over 2.5 probability edge | +5.2% |
| Under 2.5 probability edge | -5.2% |
| Raw edge prob home | -0.1728 |
| Raw ev home | -0.2388 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1273 |
| Raw edge prob away | 0.1272 |
| Raw ev away | 0.7391 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **44.9%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.2%. Goal-market probabilities: at least one goal: 93.5%; Over 2.5 goals: 55.1%; Under 3.5 goals: 67.6%; Double Chance 1X: 70.7%; Double Chance X2: 55.1%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 83.5%; BTTS Yes (both teams score): 58.6%; BTTS No (at least one team does not score): 41.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 44.9% | 2.23 |
| Draw | 25.8% | 3.88 |
| Basaksehir win | 29.3% | 3.41 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.5% |
| Under 0.5 | 6.5% |
| Over 1.5 | 79.3% |
| Under 1.5 | 20.7% |
| Over 2.5 | 55.1% |
| Under 2.5 | 44.9% |
| Over 3.5 | 32.4% |
| Under 3.5 | 67.6% |
| Over 4.5 | 16.5% |
| Under 4.5 | 83.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.15% |
| 2 | 2-1 | 9.87% |
| 3 | 1-0 | 8.39% |
| 4 | 2-0 | 7.31% |
| 5 | 1-2 | 7.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 44.9% | 46.9% | 2.09 | -6.1% |
| Draw | 25.8% | 25.2% | 3.77 | -2.8% |
| Basaksehir win | 29.3% | 27.9% | 3.48 | +2.0% |
| Over 2.5 | 55.1% | 58.4% | 1.67 | -7.9% |
| Under 2.5 | 44.9% | 41.6% | 2.31 | +3.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T16:00:00+00:00 |
| Fixture id | c7ad58db2278db2259846b11c28ae1c2 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:42Z |
| Market best draw last update utc | 2026-11-04T19:40:42Z |
| Market best away last update utc | 2026-11-04T19:40:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5169 |
| Dc lambda away | 1.3496 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 58.6% |
| P btts no | 41.4% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.43 |
| Fair Over 1.5 odds | 1.26 |
| Fair Under 1.5 odds | 4.82 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.23 |
| Fair Over 3.5 odds | 3.08 |
| Fair Under 3.5 odds | 1.48 |
| Fair Over 4.5 odds | 6.06 |
| Fair Under 4.5 odds | 1.20 |
| Goal margin distribution | {"-1": 0.15779892216922697, "-10": 3.389934767117047e-07, "-11": 4.096552660794718e-08, "-12": 4.548307924563047e-09, "-13": 4.668265098745536e-10, "-14": 4.423565082776624e-11, "-15": 3.5021689015108167e-12, "-2": 0.08746198108460923, "-3": 0.03404803021489871, "-4": 0.010480961237863042, "-5": 0.002656009492252618, "-6": 0.0005705868818783892, "-7": 0.0001062340804150858, "-8": 1.7437288151014902e-05, "-9": 2.557767763708813e-06, "0": 0.25773721365716323, "1": 0.22259769191142842, "10": 1.3588225614541198e-06, "11": 1.8455399132293504e-07, "12": 2.3029698437454614e-08, "13": 2.6566075006965854e-09, "14": 2.829292167287856e-10, "15": 2.5175375398706768e-11, "2": 0.13769646229062016, "3": 0.06024610243529026, "4": 0.02084354436384993, "5": 0.005936542358990761, "6": 0.001433373011044168, "7": 0.00029994028169328643, "8": 5.533289187141275e-05, "9": 9.122188150697449e-06} |
| Raw goal margin distribution | {"-1": 0.17605010061295925, "-10": 3.782017954357794e-07, "-11": 4.570363968175696e-08, "-12": 5.074369689796259e-09, "-13": 5.208201228654463e-10, "-14": 4.935198968315063e-11, "-15": 3.907233199054091e-12, "-2": 0.09757791978605138, "-3": 0.03798605885645865, "-4": 0.01169319951670842, "-5": 0.002963206160803771, "-6": 0.0006365815214846544, "-7": 0.00011852121857679147, "-8": 1.945410203823304e-05, "-9": 2.853601697371633e-06, "0": 0.2709222472813699, "1": 0.1992582967776254, "10": 1.2163498502315658e-06, "11": 1.6520348283374398e-07, "12": 2.061503174873643e-08, "13": 2.3780618803814672e-09, "14": 2.532640538628651e-10, "15": 2.2535734219021768e-11, "2": 0.12325897143286974, "3": 0.053929291250346345, "4": 0.018658096196263293, "5": 0.005314095168926565, "6": 0.0012830836760936498, "7": 0.0002684915065920187, "8": 4.9531231413061e-05, "9": 8.165725611010654e-06} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 70.7% |
| P draw away | 55.1% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5515 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.57, "price": 2.55, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.81, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.81, "price": 2.06, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.55, "price": 1.57, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.48, "draw": 3.77, "home": 2.09}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.67, "under": 2.31}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.39, "draw": 3.73, "home": 2.06}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.06 |
| Reference draw odds | 3.73 |
| Reference away odds | 3.39 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:43Z |
| Market reference home last update utc | 2026-11-04T19:40:43Z |
| Market reference draw last update utc | 2026-11-04T19:40:43Z |
| Market reference away last update utc | 2026-11-04T19:40:43Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.67 |
| Reference Under 2.5 odds | 2.31 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Home probability edge | -2.0% |
| Draw probability edge | +0.6% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | -3.3% |
| Under 2.5 probability edge | +3.3% |
| Raw edge prob home | -0.0673 |
| Raw ev home | -0.1598 |
| Raw edge prob draw | 0.0188 |
| Raw ev draw | 0.0214 |
| Raw edge prob away | 0.0484 |
| Raw ev away | 0.1381 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |

</details>


---

## 2026-11-07 — Samsunspor vs Torku Konyaspor

The model's most likely 1X2 outcome is **Samsunspor win** at **41.4%**. Expected goals are 1.41 for Samsunspor and 1.08 for Torku Konyaspor (2.49 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.4%; Over 2.5 goals: 48.5%; Under 3.5 goals: 73.2%; Double Chance 1X: 70.1%; Double Chance X2: 58.6%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 87.5%; BTTS Yes (both teams score): 53.9%; BTTS No (at least one team does not score): 46.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Samsunspor win | 41.4% | 2.41 |
| Draw | 28.7% | 3.48 |
| Torku Konyaspor win | 29.9% | 3.35 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Samsunspor expected goals | 1.41 |
| Torku Konyaspor expected goals | 1.08 |
| Expected total goals | 2.49 |
| Over 0.5 | 91.4% |
| Under 0.5 | 8.6% |
| Over 1.5 | 74.8% |
| Under 1.5 | 25.2% |
| Over 2.5 | 48.5% |
| Under 2.5 | 51.5% |
| Over 3.5 | 26.8% |
| Under 3.5 | 73.2% |
| Over 4.5 | 12.5% |
| Under 4.5 | 87.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.71% |
| 2 | 1-0 | 9.04% |
| 3 | 0-0 | 8.61% |
| 4 | 2-1 | 8.58% |
| 5 | 0-1 | 7.59% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Samsunspor win | 41.4% | 40.6% | 2.37 | -1.8% |
| Draw | 28.7% | 28.6% | 3.48 | -0.1% |
| Torku Konyaspor win | 29.9% | 30.8% | 3.18 | -5.1% |
| Over 2.5 | 48.5% | 48.5% | 1.98 | -4.0% |
| Under 2.5 | 51.5% | 51.5% | 1.90 | -2.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-07T13:00:00+00:00 |
| Fixture id | 605767f0e7114a23442d92831c12c767 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-04T19:40:43Z |
| Market best draw last update utc | 2026-11-04T19:40:42Z |
| Market best away last update utc | 2026-11-04T19:40:42Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Samsunspor |
| Matched away-team name | Konyaspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4120 |
| Dc lambda away | 1.0825 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 53.9% |
| P btts no | 46.1% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.61 |
| Fair Over 1.5 odds | 1.34 |
| Fair Under 1.5 odds | 3.96 |
| Fair Over 2.5 odds | 2.06 |
| Fair Under 2.5 odds | 1.94 |
| Fair Over 3.5 odds | 3.74 |
| Fair Under 3.5 odds | 1.37 |
| Fair Over 4.5 odds | 8.02 |
| Fair Under 4.5 odds | 1.14 |
| Goal margin distribution | {"-1": 0.1749123324687656, "-10": 9.096774132194028e-08, "-11": 9.293305369704335e-09, "-12": 8.719484733902986e-10, "-13": 7.561626039046899e-11, "-14": 6.06559570891337e-12, "-15": 4.1359715376035584e-13, "-2": 0.08545616843940361, "-3": 0.02867862593376735, "-4": 0.007553819687413432, "-5": 0.001630863180053694, "-6": 0.0002976886910378278, "-7": 4.700931452365456e-05, "-8": 6.5364664178231725e-06, "-9": 8.114916964134845e-07, "0": 0.28710763249571664, "1": 0.20412504892515398, "10": 1.1410412880088276e-06, "11": 1.520501752241035e-07, "12": 1.8608454628153472e-08, "13": 2.1049289969816525e-09, "14": 2.2024115930382174e-10, "15": 1.9588687375162376e-11, "2": 0.1279190457797539, "3": 0.05599547112245489, "4": 0.01923817835218078, "5": 0.00541773339559918, "6": 0.0012899272208799265, "7": 0.0002656987791068504, "8": 4.818939165489825e-05, "9": 7.803604652219769e-06} |
| Raw goal margin distribution | {"-1": 0.16524503802635168, "-10": 5.770363149566151e-08, "-11": 5.614189316660189e-09, "-12": 5.014804037269771e-10, "-13": 4.120775787883671e-11, "-14": 2.872637889811552e-12, "-2": 0.07821800163078522, "-3": 0.02522858011731453, "-4": 0.006363982052782822, "-5": 0.0013131962607183668, "-6": 0.00022881405249773138, "-7": 3.4463319847038454e-05, "-8": 4.567979169192735e-06, "-9": 5.403777816091211e-07, "0": 0.29027268759906033, "1": 0.2192474150653719, "10": 8.226798069728959e-07, "11": 1.0440409048718178e-07, "12": 1.2164302090610996e-08, "13": 1.3038120317128218e-09, "14": 1.1855493942562465e-10, "2": 0.1330798352188119, "3": 0.05598879444466068, "4": 0.018422137645694645, "5": 0.00495842197133044, "6": 0.0011269361435420188, "7": 0.00022139942819552195, "8": 3.82777382388666e-05, "9": 5.906393897316522e-06} |
| Unadjusted home-win probability | 43.3% |
| Unadjusted draw probability | 29.0% |
| Unadjusted away-win probability | 27.7% |
| Raw p over 1 5 | 72.4% |
| Raw p under 3 5 | 75.9% |
| Raw p btts yes | 51.2% |
| P home draw | 70.1% |
| P draw away | 58.6% |
| P home away | 71.3% |
| Raw p home draw | 72.3% |
| Raw p draw away | 56.7% |
| Raw p home away | 71.0% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.0513 |
| Totals anchor target over 2 5 | 0.4847 |
| Totals anchor reference over odds | 1.97 |
| Totals anchor reference under odds | 1.86 |
| Totals anchor reference last update utc | 2026-11-04T19:40:43Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4555 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.68, "price": 2.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.03, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.83, "price": 2.03, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.29, "price": 1.68, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.18, "draw": 3.48, "home": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-04T19:40:42Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.98, "under": 1.9}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.09, "draw": 3.32, "home": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-04T19:40:43Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.97, "under": 1.86}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.37 |
| Reference draw odds | 3.32 |
| Reference away odds | 3.09 |
| Market reference 1x2 last update utc | 2026-11-04T19:40:43Z |
| Market reference home last update utc | 2026-11-04T19:40:43Z |
| Market reference draw last update utc | 2026-11-04T19:40:43Z |
| Market reference away last update utc | 2026-11-04T19:40:43Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.97 |
| Reference Under 2.5 odds | 1.86 |
| Market reference over 2 5 last update utc | 2026-11-04T19:40:43Z |
| Market reference under 2 5 last update utc | 2026-11-04T19:40:43Z |
| Market best over 2 5 last update utc | 2026-11-04T19:40:42Z |
| Market best under 2 5 last update utc | 2026-11-04T19:40:42Z |
| Home probability edge | +0.8% |
| Draw probability edge | +0.1% |
| Away probability edge | -0.9% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.0268 |
| Raw ev home | 0.0264 |
| Raw edge prob draw | 0.0045 |
| Raw ev draw | 0.0101 |
| Raw edge prob away | -0.0314 |
| Raw ev away | -0.1203 |
| Elo home rating | 1,436.0175 |
| Elo away rating | 1,425.6973 |
| Elo rating diff | 70.3203 |
| Elo home expectancy | 0.5998 |

</details>


---
