# Super Lig — football model report

Fixtures in this report: **8**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Super Lig |
| Training matches | 1,831 |
| Training data through | 2026-10-26 |
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
| Training sha256 | 36930ef41a7cb5e7e2f4d6e9884819c8b34ead9559d248ba647b034c279b2986 |
| Training as of utc | 2026-10-30T07:28:48.223760+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'VALIDATED', 'cutoff_date': '2026-10-30', 'selected_weight': 0.3, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1800, 'tune_start_date': '2025-10-31', 'audit_start_date': '2026-05-01', 'training_shot_matches': 1503, 'tuning_matches': 189, 'audit_matches': 94, 'audit_matchdays': 36, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.3, 'audit_baseline_poisson_score': 0.88342479621755, 'audit_candidate_poisson_score': 0.8703833305136697, 'audit_gain': 0.013041465703880317, 'audit_gain_lower95': 0.0035143404939131564, 'audit_baseline_briers': [0.6143728531190132, 0.17437373082125635, 0.20593066792660297, 0.24831244922428455], 'audit_candidate_briers': [0.6097721846414722, 0.17271774778864193, 0.20182683299664475, 0.24790656013702597], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': []} |
| Optimizer objective | 1655.988 |
| Base scoring parameter | 0.124 |
| Home-advantage parameter | 0.246 |
| Dixon-Coles low-score adjustment | -0.096 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1831, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-10-26'} |
| Training data health | {'training_end': '2026-10-26', 'days_since_latest_result': 4, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 8.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 35.00 |
| Over 1 5 in window quote fixtures | 4 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 4.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 4.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 2, 'ANCHORED_MAIN': 2, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 4} |
| Shot features applied fixtures | 8 |
| Goal rate features used | {'shot_features': 8} |
| Legacy comparison status | {'AVAILABLE': 8} |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 365.0, 'selected_xi_per_day': 0.0018990333713971104, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365, 'applied_to_production': False} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'RELIABLE_FOR_RANKING', 'under_3_5': 'RELIABLE_FOR_RANKING', 'btts_yes': 'RELIABLE_FOR_RANKING'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-30 — Torku Konyaspor vs Galatasaray

The model's most likely 1X2 outcome is **Galatasaray win** at **61.0%**. Expected goals are 0.98 for Torku Konyaspor and 1.78 for Galatasaray (2.76 combined). The most likely exact score is 1-2 at 10.5%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.5%; Under 3.5 goals: 62.2%; Double Chance 1X: 39.0%; Double Chance X2: 82.8%; Double Chance 12 (either team wins): 78.3%; Under 4.5 goals: 79.5%; BTTS Yes (both teams score): 57.9%; BTTS No (at least one team does not score): 42.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Torku Konyaspor win | 17.2% | 5.80 |
| Draw | 21.7% | 4.60 |
| Galatasaray win | 61.0% | 1.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Torku Konyaspor expected goals | 0.98 |
| Galatasaray expected goals | 1.78 |
| Expected total goals | 2.76 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.7% |
| Under 1.5 | 17.3% |
| Over 2.5 | 60.5% |
| Under 2.5 | 39.5% |
| Over 3.5 | 37.8% |
| Under 3.5 | 62.2% |
| Over 4.5 | 20.5% |
| Under 4.5 | 79.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 10.54% |
| 2 | 1-1 | 10.14% |
| 3 | 0-2 | 9.63% |
| 4 | 0-1 | 8.62% |
| 5 | 1-3 | 7.03% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Torku Konyaspor win | 17.2% | 16.3% | 5.74 | -1.0% |
| Draw | 21.7% | 20.2% | 4.67 | +1.5% |
| Galatasaray win | 61.0% | 63.5% | 1.55 | -5.4% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T17:00:00+00:00 |
| Fixture id | feb03ec355aa5c94e0d7ae612a59b813 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Konyaspor |
| Matched away-team name | Galatasaray |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9032 |
| Dc lambda away | 1.8386 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.1491 |
| Shot lambda away | 1.6581 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.9% |
| P btts no | 42.1% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.54 |
| Fair Over 1.5 odds | 1.21 |
| Fair Under 1.5 odds | 5.78 |
| Fair Over 2.5 odds | 1.65 |
| Fair Under 2.5 odds | 2.53 |
| Fair Over 3.5 odds | 2.65 |
| Fair Under 3.5 odds | 1.61 |
| Fair Over 4.5 odds | 4.88 |
| Fair Under 4.5 odds | 1.26 |
| Goal margin distribution | {"-1": 0.23797581913786772, "-10": 1.652442335617e-05, "-11": 2.9553762624091328e-06, "-12": 4.857085120578939e-07, "-13": 7.382743689605523e-08, "-14": 1.0436300365094351e-08, "-15": 1.3782690117680516e-09, "-16": 1.6970784159110923e-10, "-17": 1.7683886210057406e-11, "-2": 0.18891567304110504, "-3": 0.10803637614611634, "-4": 0.04899163486829761, "-5": 0.018319207392640063, "-6": 0.005813052186755587, "-7": 0.0015997441486243446, "-8": 0.0003883092907911773, "-9": 8.426014309211343e-05, "0": 0.2173862753911149, "1": 0.10547654523648527, "10": 3.3543550779577806e-08, "11": 3.2844455070578412e-09, "12": 2.9552318208374885e-10, "13": 2.4592359041382305e-11, "14": 1.9032486459703917e-12, "15": 1.3760984675193126e-13, "16": 9.276496588163913e-15, "17": 5.292079390479036e-16, "2": 0.04751363218821032, "3": 0.014876021920619202, "4": 0.003693220975680874, "5": 0.0007560605892044829, "6": 0.00013134716479964512, "7": 1.9789443020700863e-05, "8": 2.6298282254418463e-06, "9": 3.1241965803751876e-07} |
| Raw goal margin distribution | {"-1": 0.233602578873058, "-10": 6.674449240474072e-06, "-11": 1.0687906675737212e-06, "-12": 1.5719409366078111e-07, "-13": 2.137420223398302e-08, "-14": 2.701593611980213e-09, "-15": 3.1749940840335504e-10, "-16": 3.193110748623947e-11, "-2": 0.17344044092684646, "-3": 0.09095910041489655, "-4": 0.03748369516203954, "-5": 0.01266986224220898, "-6": 0.003622224105574799, "-7": 0.0008961362005115855, "-8": 0.00019525047709228612, "-9": 3.7988387876045806e-05, "0": 0.25296788649286195, "1": 0.12310199210720135, "10": 1.614659800279057e-08, "11": 1.4155486866108068e-09, "12": 1.1398165065203976e-10, "13": 8.485065360082828e-12, "14": 5.871537762672169e-13, "15": 3.777820490999477e-14, "16": 2.0800747350955096e-15, "2": 0.05198565120702077, "3": 0.014926082441201692, "4": 0.0033675080039279057, "5": 0.0006231673515052, "6": 9.753818623464668e-05, "7": 1.3211129216393373e-05, "8": 1.5758852201818613e-06, "9": 1.6786103716405845e-07} |
| Unadjusted home-win probability | 19.4% |
| Unadjusted draw probability | 25.3% |
| Unadjusted away-win probability | 55.3% |
| Raw p over 1 5 | 77.3% |
| Raw p under 3 5 | 70.1% |
| Raw p btts yes | 52.9% |
| P home draw | 39.0% |
| P draw away | 82.8% |
| P home away | 78.3% |
| Raw p home draw | 44.7% |
| Raw p draw away | 80.6% |
| Raw p home away | 74.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.1205 |
| Totals anchor target over 2 5 | 0.6049 |
| Totals anchor reference over odds | 1.61 |
| Totals anchor reference under odds | 2.41 |
| Totals anchor reference last update utc | 2026-10-30T07:28:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5367 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 4.54, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.89, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.21, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.94, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.61, "price": 1.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.47, "price": 1.6, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.31, "price": 1.68, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.18, "price": 1.75, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.01, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.75, "price": 2.18, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.68, "price": 2.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.54, "price": 2.61, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.54, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.42, "price": 1.62, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.62, "price": 2.42, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.74 |
| Reference draw odds | 4.67 |
| Reference away odds | 1.55 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.62 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:26Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:26Z |
| Home probability edge | +0.9% |
| Draw probability edge | +1.5% |
| Away probability edge | -2.5% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | 0.0309 |
| Raw ev home | 0.1142 |
| Raw edge prob draw | 0.0508 |
| Raw ev draw | 0.1814 |
| Raw edge prob away | -0.0818 |
| Raw ev away | -0.1430 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06833244625890933, 0.11352661079605147, 0.11383258147729655, 0.06958300782668128, 0.03190076326592177, 0.01170008286486482, 0.003575983901063872, 0.0009368183364924816, 0.0002147451001978817, 4.37561015598184e-05, 8.024102900387489e-06, 1.337709070813512e-06, 2.0442701802999203e-07, 2.8837181379669277e-08, 3.777310110539989e-09, 4.617950248943945e-10, 5.292820124717194e-11], [0.047198270746014195, 0.10698795210117003, 0.1026980038407399, 0.06277671921601811, 0.02878037786624019, 0.010555634769931946, 0.0032261976636199494, 0.0008451830914365148, 0.00019373972582094776, 3.947608169583925e-05, 7.239222196211389e-06, 1.206860544751843e-06, 1.844309108195209e-07, 2.6016461417736123e-08, 3.407831072664122e-09, 4.1662436733632295e-10, 4.7751008932795146e-11], [0.025772559040053742, 0.04726236076150142, 0.040418703774679716, 0.028318095168743576, 0.012982607080884757, 0.004761565652273848, 0.0014553129506050474, 0.0003812555915187925, 8.73945000993934e-05, 1.7807356808583138e-05, 3.2655574496426844e-06, 5.444055087377689e-07, 8.319536525433173e-08, 1.1735825630617079e-08, 1.5372463843265058e-09, 1.8793604748999364e-10, 2.1540112835609697e-11], [0.007750535429404653, 0.014213124936100918, 0.013032191278217998, 0.007430074310328411, 0.0039042361292123827, 0.0014319370936363089, 0.00043765365197170273, 0.00011465430984686831, 2.62819911791749e-05, 5.355174456462743e-06, 9.820452315533484e-07, 1.6371809166787118e-07, 2.5019192892868983e-08, 3.5292937811123617e-09, 4.6229334645931765e-10, 5.651767029691257e-11, 6.477719477771297e-12], [0.0017481034580937224, 0.0032057156666690637, 0.002939360621920501, 0.0017967575759610225, 0.0007682922630986775, 0.00032296790434136293, 9.87110980173724e-05, 2.5859838633632984e-05, 5.927802031792462e-06, 1.207839003034759e-06, 2.2149652510068282e-07, 3.692598592754185e-08, 5.6429827349486356e-09, 7.96018638916808e-10, 1.0426848634653987e-10, 1.2747343172524898e-11, 1.4610247153625212e-12], [0.0003154224095130896, 0.0005784294717300449, 0.0005303691869616736, 0.00032420140884484137, 0.00014863215484732043, 5.084400306181683e-05, 1.781112681755994e-05, 4.666069718971337e-06, 1.0695943602923312e-06, 2.1793875349721203e-07, 3.9966151501250666e-08, 6.662811288991361e-09, 1.0182024426856517e-09, 1.4363115406125358e-10, 1.881388486901844e-11, 2.3000913817495952e-12, 2.636228044422271e-13], [4.742820758233652e-05, 8.697502850004498e-05, 7.974848690466755e-05, 4.874825393958254e-05, 2.234894059807174e-05, 8.196808796067698e-06, 2.3366330788947837e-06, 7.016093864942829e-07, 1.6082859625335508e-07, 3.277016511622486e-08, 6.009474509418981e-09, 1.001847641022169e-09, 1.531010966756728e-10, 2.159696960220259e-11, 2.828932916895231e-12, 3.4585117677707674e-13, 3.963940644491459e-14], [6.112714179817118e-06, 1.1209647530517772e-05, 1.0278265436762385e-05, 6.282846396429892e-06, 2.880410056832965e-06, 1.056433542633667e-06, 3.2288569103613044e-07, 7.88946812086989e-08, 2.0728155056909575e-08, 4.2235341201361e-09, 7.745222077643027e-10, 1.291216470844089e-10, 1.973220773671987e-11, 2.7834933904950944e-12, 3.6460282258899944e-13, 4.457451588744026e-14, 5.1088660990343605e-15], [6.893495870966966e-07, 1.2641464445002272e-06, 1.1591116198916368e-06, 7.085359206669945e-07, 3.2483270523314126e-07, 1.1913726128634507e-07, 3.6412812908888094e-08, 9.539246193521163e-09, 2.039487447925699e-09, 4.763009386923007e-10, 8.7345252601933e-11, 1.4561445453604655e-11, 2.2252617831742044e-12, 3.139031145541938e-13, 4.111738219920116e-14, 5.026805313995787e-15, 5.761425501506132e-16], [6.91022880800597e-08, 1.2672149721761472e-07, 1.1619251911361646e-07, 7.102557863450646e-08, 3.2562118836370604e-08, 1.1942644928753034e-08, 3.6501199602261425e-09, 9.56240129638095e-10, 2.1919712120623729e-10, 4.1657125917484427e-11, 8.755727022547284e-12, 1.4596791199004784e-12, 2.2306632755389096e-13, 3.1466506772722813e-14, 4.121718853555447e-15, 5.039007137047669e-16, 5.775410505918427e-17], [6.234302125587191e-09, 1.1432618534223855e-08, 1.0482710327161768e-08, 6.407818440673856e-09, 2.9377042687792945e-09, 1.0774470532466021e-09, 3.2930820757080795e-10, 8.627051344331398e-11, 1.9775627068605996e-11, 4.0294486143137316e-12, 6.891957460148941e-13, 1.316900046685535e-13, 2.0124700913014242e-14, 2.8388598338554478e-15, 3.718551342326452e-16, 4.546114720390915e-17, 5.210486511166003e-18], [5.113174064520852e-10, 9.376665968566275e-10, 8.597581812844853e-10, 5.255486564653142e-10, 2.4094105440774896e-10, 8.8368741481807e-11, 2.7008799898774736e-11, 7.075630006136462e-12, 1.6219333198791492e-12, 3.304824138128836e-13, 6.060468827593659e-14, 9.423462419773735e-15, 1.6505632337311787e-15, 2.3283415180833043e-16, 3.049836196281871e-17, 3.728577058727308e-18, 4.273473430664126e-19], [3.8441891511619337e-11, 7.049569824063787e-11, 6.463838373994896e-11, 3.951182608098852e-11, 1.8114442726498122e-11, 6.6437432604405065e-12, 2.03057698108118e-12, 5.319603785046287e-13, 1.219402741528174e-13, 2.4846345807872407e-14, 4.5563847864377006e-15, 7.596010837099386e-16, 1.0826829459609086e-16, 1.750494915892227e-17, 2.2929294153936443e-18, 2.8032207191784594e-19, 3.212884989370541e-20], [2.6678217802039112e-12, 4.892318035916906e-12, 4.485827340896893e-12, 2.7420739731974185e-12, 1.2571208892622024e-12, 4.610679203162734e-13, 1.409196395778726e-13, 3.6917420766124614e-14, 8.46251072662732e-15, 1.724306996826232e-15, 3.162077123227436e-16, 5.2715416325842107e-17, 8.055903633177792e-18, 1.0599072833190123e-18, 1.5912658806105943e-19, 1.945402006840048e-20, 2.2297041625389776e-21], [1.7191912636342964e-13, 3.152695764267271e-13, 2.8907460130460244e-13, 1.7670406823800895e-13, 8.101108050728055e-14, 2.9712027483679394e-14, 9.081109354248355e-15, 2.3790235062921513e-15, 5.453390709073977e-16, 1.111173747348508e-16, 2.037698097200093e-17, 3.397074117871003e-18, 5.19136594865811e-19, 7.323120148811703e-20, 8.946745638363484e-21, 1.2536512593282763e-21, 1.436860567362578e-22], [1.0340186070007582e-14, 1.896209078897626e-14, 1.7386577217034296e-14, 1.0627979466611567e-14, 4.8724633721488765e-15, 1.7870489409593526e-15, 5.461891438798559e-16, 1.4308789394369258e-16, 3.279976802875989e-17, 6.683225739178284e-18, 1.2255865839504043e-18, 2.043192006347065e-19, 3.122380330920815e-20, 4.404537560972749e-21, 5.769393354457696e-22, 6.578635999731459e-23, 8.642089997466486e-24], [5.830473001173443e-16, 1.0692066626499754e-15, 9.803689059404078e-16, 5.992749735601136e-16, 2.7474134361007403e-16, 1.0076550394253652e-16, 3.0797715199366833e-17, 8.068231043281958e-18, 1.8494653833274416e-18, 3.7684396556509784e-19, 6.910658512277605e-20, 1.1520852476507927e-20, 1.7606021879657977e-21, 2.4835662683473467e-22, 3.2531612060526895e-23, 3.977152037219994e-24, 4.251568464556102e-25]] |
| Legacy trial inputs | {"lambda_home": 0.9021846162842458, "lambda_away": 1.8338249099769206, "rho": -0.0948277249952374, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.1672 |
| Legacy p draw | 0.2240 |
| Legacy p away | 0.6089 |
| Legacy p over 1 5 | 0.7709 |
| Legacy p under 3 5 | 0.7029 |
| Legacy p btts yes | 0.5035 |
| Legacy p over 2 5 | 0.5243 |
| Legacy goal margin distribution | {"-1": 0.24878844778863782, "-10": 9.317794712391911e-06, "-11": 1.5343511115760865e-06, "-12": 2.3203870452706693e-07, "-13": 3.2439426219301165e-08, "-14": 4.215474590711922e-09, "-15": 5.095460338271896e-10, "-16": 5.292820124717194e-11, "-2": 0.1911273871765277, "-3": 0.10358956798963566, "-4": 0.04403251717794419, "-5": 0.01533506693823519, "-6": 0.004514144982318849, "-7": 0.001149385430508593, "-8": 0.0002576562469230041, "-9": 5.1565563641144254e-05, "0": 0.2239907303208514, "1": 0.10944674197356319, "10": 7.239432009084129e-09, "11": 5.864806093307342e-10, "12": 4.363418686965107e-11, "13": 3.001077208821233e-12, "14": 1.918615860583463e-13, "15": 1.1409392732657558e-14, "16": 5.830473001173443e-16, "2": 0.043272688770224464, "3": 0.011538371822330664, "4": 0.0024129013749825496, "5": 0.00041341790648578874, "6": 5.9871020452437185e-05, "7": 7.499708690001143e-06, "8": 8.270979280346319e-07, "9": 8.143546400882315e-08} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.1711 |
| Legacy raw p draw | 0.2458 |
| Legacy raw p away | 0.5830 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 0.9022 |
| Legacy lambda away | 1.8338 |
| Legacy model home team | Konyaspor |
| Legacy model away team | Galatasaray |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 38.7% |
| Market reference home draw last update utc | 2026-10-30T07:28:46Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 83.0% |
| Market reference draw away last update utc | 2026-10-30T07:28:46Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 78.3% |
| Market reference home away last update utc | 2026-10-30T07:28:46Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.16 |
| Market reference dc home draw odds | 2.49 |
| Market reference dc home away odds | 1.23 |
| Market p over 1 5 | 82.2% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.60 |
| Market reference over 1 5 last update utc | 2026-10-30T07:28:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.3% |
| Market under 3 5 odds | 1.56 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 3 5 odds | 1.54 |
| Market reference under 3 5 opposite odds | 2.44 |
| Market reference under 3 5 last update utc | 2026-10-30T07:28:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 56.9% |
| Market reference btts yes odds | 1.65 |
| Market reference btts yes opposite odds | 2.11 |
| Market reference btts yes last update utc | 2026-10-30T07:28:46Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,456.7365 |
| Elo away rating | 1,677.5170 |
| Elo rating diff | -160.7805 |
| Elo home expectancy | 0.2838 |

</details>


---

## 2026-10-31 — Erzurum BB vs Çorum FK

The model's most likely 1X2 outcome is **Çorum FK win** at **36.9%**. Expected goals are 1.27 for Erzurum BB and 1.46 for Çorum FK (2.73 combined). The most likely exact score is 1-1 at 13.8%. Goal-market probabilities: at least one goal: 91.1%; Over 2.5 goals: 47.3%; Under 3.5 goals: 74.4%; Double Chance 1X: 63.1%; Double Chance X2: 65.7%; Double Chance 12 (either team wins): 71.2%; Under 4.5 goals: 88.3%; BTTS Yes (both teams score): 53.2%; BTTS No (at least one team does not score): 46.8%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Erzurum BB win | 34.3% | 2.91 |
| Draw | 28.8% | 3.47 |
| Çorum FK win | 36.9% | 2.71 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Erzurum BB expected goals | 1.27 |
| Çorum FK expected goals | 1.46 |
| Expected total goals | 2.73 |
| Over 0.5 | 91.1% |
| Under 0.5 | 8.9% |
| Over 1.5 | 73.7% |
| Under 1.5 | 26.3% |
| Over 2.5 | 47.3% |
| Under 2.5 | 52.7% |
| Over 3.5 | 25.6% |
| Under 3.5 | 74.4% |
| Over 4.5 | 11.7% |
| Under 4.5 | 88.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.76% |
| 2 | 0-0 | 8.88% |
| 3 | 1-0 | 8.72% |
| 4 | 0-1 | 8.67% |
| 5 | 2-1 | 8.21% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Erzurum BB win | 34.3% | 35.4% | 2.70 | -7.4% |
| Draw | 28.8% | 29.2% | 3.24 | -6.6% |
| Çorum FK win | 36.9% | 35.4% | 2.70 | -0.5% |
| Over 2.5 | 47.3% | 47.3% | 2.03 | -4.1% |
| Under 2.5 | 52.7% | 52.7% | 1.83 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T10:30:00+00:00 |
| Fixture id | 7ef8c62daf5d4e448691625fb8c2de1b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Erzurumspor |
| Matched away-team name | Corum |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2395 |
| Dc lambda away | 1.5081 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.3510 |
| Shot lambda away | 1.3443 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 53.2% |
| P btts no | 46.8% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 11.26 |
| Fair Over 1.5 odds | 1.36 |
| Fair Under 1.5 odds | 3.81 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.90 |
| Fair Over 3.5 odds | 3.91 |
| Fair Under 3.5 odds | 1.34 |
| Fair Over 4.5 odds | 8.51 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.19202243069099198, "-10": 5.30527592684222e-07, "-11": 6.524990918560168e-08, "-12": 7.368331092610326e-09, "-13": 7.650313881640453e-10, "-14": 6.700490367782656e-11, "-2": 0.11206076394307905, "-3": 0.04541019242376525, "-4": 0.014425990933078146, "-5": 0.0037540030509478966, "-6": 0.0008255829382158837, "-7": 0.00015703171674269633, "-8": 2.6294893733036653e-05, "-9": 3.930790438159538e-06, "0": 0.2881781910039504, "1": 0.1950166776287994, "10": 1.5922720008796372e-07, "11": 1.7086413300901702e-08, "12": 1.6834562792289604e-09, "13": 1.5250134611763768e-10, "14": 1.1653670220861129e-11, "2": 0.10015419642566606, "3": 0.03541038330981269, "4": 0.009814872321100902, "5": 0.002228411209729202, "6": 0.0004275856641976628, "7": 7.095965892069086e-05, "8": 1.0367099683571101e-05, "9": 1.3521580533637027e-06} |
| Raw goal margin distribution | {"-1": 0.2034861898433274, "-10": 9.269469176898198e-07, "-11": 1.2125780663493145e-07, "-12": 1.4570714665768373e-08, "-13": 1.6184218091327025e-09, "-14": 1.6613732320421207e-10, "-15": 1.4378966607626999e-11, "-2": 0.12345861180915452, "-3": 0.05256156471897607, "-4": 0.01762634498206802, "-5": 0.004855037907280519, "-6": 0.0011320662122770078, "-7": 0.00022855654845971047, "-8": 4.0654252954168124e-05, "-9": 6.4592476401181975e-06, "0": 0.27837970554588115, "1": 0.1760592275111718, "10": 2.369583418282899e-07, "11": 2.7045097998491947e-08, "12": 2.8354462469571696e-09, "13": 2.7478561951809375e-10, "14": 2.4611109987338664e-11, "15": 1.8584606983738862e-12, "2": 0.09398202899794157, "3": 0.034910287595704935, "4": 0.010214312033701482, "5": 0.0024547156637049097, "6": 0.0004993926096485932, "7": 8.796819181698326e-05, "8": 1.365210736354436e-05, "9": 1.892506409004363e-06} |
| Unadjusted home-win probability | 31.8% |
| Unadjusted draw probability | 27.8% |
| Unadjusted away-win probability | 40.3% |
| Raw p over 1 5 | 76.9% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 56.4% |
| P home draw | 63.1% |
| P draw away | 65.7% |
| P home away | 71.2% |
| Raw p home draw | 59.7% |
| Raw p draw away | 68.2% |
| Raw p home away | 72.2% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 0.9387 |
| Totals anchor target over 2 5 | 0.4726 |
| Totals anchor reference over odds | 2.03 |
| Totals anchor reference under odds | 1.83 |
| Totals anchor reference last update utc | 2026-10-30T07:28:45Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.5102 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.72, "price": 1.2, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.73, "price": 1.2, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.34, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.7, "price": 1.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.33, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.93, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.33, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.2, "price": 4.73, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.70 |
| Reference draw odds | 3.24 |
| Reference away odds | 2.70 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 2.03 |
| Reference Under 2.5 odds | 1.83 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market best over 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market best under 2 5 last update utc | 2026-10-30T07:28:45Z |
| Home probability edge | -1.1% |
| Draw probability edge | -0.4% |
| Away probability edge | +1.5% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | -0.0356 |
| Raw ev home | -0.1408 |
| Raw edge prob draw | -0.0140 |
| Raw ev draw | -0.0980 |
| Raw edge prob away | 0.0496 |
| Raw ev away | 0.0892 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.07826733156806688, 0.0787197488984, 0.06686669035187578, 0.03341594768933307, 0.012524459720903318, 0.003755382735426121, 0.0009383571429964112, 0.00020097189779036542, 3.7662622384826436e-05, 6.273837356246344e-06, 9.405859022084681e-07, 1.2819497124580151e-07, 1.6016032910566695e-08, 1.84704216397561e-09, 1.977943961760945e-10, 1.9769147122676945e-11], [0.07458805034046592, 0.1353518584688619, 0.08286185112086243, 0.04140936642631916, 0.015520431941546151, 0.004653706703400597, 0.0011628212712786858, 0.0002490463246580482, 4.6671886890917465e-05, 7.774600092125035e-06, 1.1655831713075623e-06, 1.5886045153294858e-07, 1.9847223297555978e-08, 2.288872561209531e-09, 2.4510873384396024e-10, 2.4498118824864638e-11], [0.05387429530759141, 0.08076939165036696, 0.057420696732087655, 0.025657444220511222, 0.009616534885338453, 0.0028834592379860646, 0.0007204896978885953, 0.000154310310316071, 2.8918127416907852e-05, 4.817179914003596e-06, 7.222009845381897e-07, 9.843070604097052e-08, 1.2297435788957522e-08, 1.4181965370464218e-09, 1.5187055995535432e-10, 1.5179153208606396e-11], [0.022253849729600015, 0.033363404463597715, 0.025009532528680788, 0.011853209517429344, 0.003972301095279902, 0.0011910702166442436, 0.0002976126068470062, 6.374094432039667e-05, 1.1945207975771196e-05, 1.9898320212752353e-06, 2.9831948785077464e-07, 4.065876181781877e-08, 5.079700561174743e-09, 5.85814300535696e-10, 6.273315688493899e-11, 6.2700512850941014e-12], [0.006894296597664764, 0.010336063587863067, 0.007748013809598475, 0.0038719910136917656, 0.0013763408217124622, 0.00036899644070427685, 9.220110712252638e-05, 1.9747099081716877e-05, 3.7006543904274653e-06, 6.164547842684128e-07, 9.242010057123077e-08, 1.2596182982803317e-08, 1.5737035488956849e-09, 1.8148669053312623e-10, 1.9434884090968396e-11, 1.9424770890094798e-12], [0.0017086958401934427, 0.0025617100463212923, 0.0019202827697761909, 0.0009596417625262164, 0.0003596784000560584, 0.00010228124247910001, 2.2851301212491204e-05, 4.894159335739398e-06, 9.171773615105035e-07, 1.5278334934176868e-07, 2.2905576973553988e-08, 3.121862420645167e-09, 3.9002973974263395e-10, 4.498001337358569e-11, 4.81677936689404e-12, 4.814272891575062e-13], [0.0003529054091952031, 0.000529082655245495, 0.0003966055050275328, 0.00019819956303444863, 7.428616021918166e-05, 2.2274251327792427e-05, 5.278414691066776e-06, 1.0108149516242174e-06, 1.894291801118901e-07, 3.155510135236617e-08, 4.730802185243895e-09, 6.447736976313956e-10, 8.055477263091488e-11, 9.289944794044737e-12, 9.94833283660543e-13, 9.943156089069243e-14], [6.247482933707627e-05, 9.36634795908896e-05, 7.02110554135333e-05, 3.508726007770292e-05, 1.3150875732916255e-05, 3.9432097498546676e-06, 9.852894620311895e-07, 2.0013241663029949e-07, 3.3534639567982776e-08, 5.586198228581918e-09, 8.374937063860601e-10, 1.141442598242401e-10, 1.4260607917232781e-11, 1.6445985253736197e-12, 1.7611529320922746e-13, 1.760236492699685e-14], [9.677426795180253e-06, 1.4508586525818162e-05, 1.0875777592137888e-05, 5.43505911818328e-06, 2.0370865922843257e-06, 6.108079701405941e-07, 1.5262253201883812e-07, 3.268780989661419e-08, 5.809616677053086e-09, 8.65308877096599e-10, 1.2972879031404448e-10, 1.768108421039847e-11, 2.2089854528323977e-12, 2.547503051331972e-13, 2.728047240190774e-14, 2.7266276644627383e-15], [1.3324845701124797e-06, 1.9976867910199925e-06, 1.4974854510618767e-06, 7.483531072779838e-07, 2.80486384413029e-07, 8.410212887576859e-08, 2.1014591303122508e-08, 4.500783445833045e-09, 8.434577631003207e-10, 1.332516121424915e-10, 1.7862352777384337e-11, 2.4345078905633332e-12, 3.0415513274334975e-13, 3.507656095011656e-14, 3.756247327959697e-15, 3.754292714616969e-16], [1.6512278009944777e-07, 2.475552843912637e-07, 1.855698492755828e-07, 9.273664276605466e-08, 3.4758144756912406e-08, 1.0422017367958479e-08, 2.6041485330913446e-09, 5.577414492227778e-10, 1.0452210394288448e-10, 1.7411285745586405e-11, 2.4756114614328516e-12, 3.016865786520336e-13, 3.769119900267137e-14, 4.346721448280677e-15, 4.654778114852546e-16, 4.6523559390434596e-17], [1.8601977306382302e-08, 2.7888446279476765e-08, 2.09054506161668e-08, 1.0447286093204535e-08, 3.915693640760097e-09, 1.1740968172212493e-09, 2.933714650748904e-10, 6.283260114093481e-11, 1.1774982254961267e-11, 1.961475831010546e-12, 2.9406827263928155e-13, 3.8010810231054645e-14, 4.246118119351945e-15, 4.89681760986489e-16, 5.243860163121225e-17, 5.241131450619803e-18], [1.9209792224944876e-09, 2.879969423043416e-09, 2.158853094437576e-09, 1.0788648532334182e-09, 4.0436379432487363e-10, 1.2124601347111088e-10, 3.029573037315099e-11, 6.488564054188328e-12, 1.2159726831438064e-12, 2.025566559262272e-13, 3.0367687930738865e-14, 4.138893504508123e-15, 4.90404726907644e-16, 5.0568198906834255e-17, 5.415201971871173e-18, 5.4123840993767305e-19], [1.8311508316365644e-10, 2.745296951856522e-10, 2.0579013000084037e-10, 1.0284152218244531e-10, 3.85455027098209e-11, 1.1557633513179755e-11, 2.8879048361488334e-12, 6.185147306551969e-13, 1.159111646764579e-13, 1.930847479293321e-14, 2.8947641056233084e-15, 3.945351513481544e-16, 4.929123121570498e-17, 5.391107050590352e-18, 5.161977536329297e-19, 5.159291432543675e-20], [1.6208427629067694e-11, 2.4299990036701716e-11, 1.821550890984752e-11, 9.103015113547786e-12, 3.411854339381714e-12, 1.0230236806557167e-12, 2.5562283416335854e-13, 5.474781801768466e-14, 1.0259874236467024e-14, 1.709089229035449e-15, 2.562299822526611e-16, 3.492227039557728e-17, 4.3630122658621266e-18, 5.031625285730617e-19, 5.1101293925110025e-20, 4.566745696580079e-21], [1.3390427132307843e-12, 2.007518886771728e-12, 1.5048556856791629e-12, 7.520363069867373e-13, 2.818668655780463e-13, 8.451605771974375e-14, 2.111801966576908e-14, 4.522935133473058e-15, 8.476090432342362e-16, 1.4119466309593992e-16, 2.116817858577281e-17, 2.885067742093047e-18, 3.6044580733185284e-19, 4.1568258986963125e-20, 4.451424470311364e-21, 4.2194844575446035e-22]] |
| Legacy trial inputs | {"lambda_home": 1.2392096974564548, "lambda_away": 1.4992194550150482, "rho": -0.0948277249952374, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:28:45Z", "over": 2.03, "under": 1.83, "bookmaker": "pinnacle", "event_id": "7ef8c62daf5d4e448691625fb8c2de1b", "kickoff_utc": "2026-10-31T10:30:00Z", "home_team": "Erzurum BB", "away_team": "\u00c7orum FK"}} |
| Legacy p home | 0.3281 |
| Legacy p draw | 0.2844 |
| Legacy p away | 0.3875 |
| Legacy p over 1 5 | 0.7684 |
| Legacy p under 3 5 | 0.7070 |
| Legacy p btts yes | 0.5655 |
| Legacy p over 2 5 | 0.5123 |
| Legacy goal margin distribution | {"-1": 0.19160423831003873, "-10": 1.11234952014229e-06, "-11": 1.4952506671437786e-07, "-12": 1.8463046083016676e-08, "-13": 2.1073300510281764e-09, "-14": 2.2229251500095914e-10, "-15": 1.9769147122676945e-11, "-2": 0.11918095229421573, "-3": 0.05213814816274022, "-4": 0.017966255351443652, "-5": 0.00508509954465075, "-6": 0.0012184070512826614, "-7": 0.00025277227976464647, "-8": 4.6201701919305394e-05, "-9": 7.543117337057511e-06, "0": 0.28437720284312745, "1": 0.18462193702302857, "10": 1.9527641736594164e-07, "11": 2.1697121741405687e-08, "12": 2.2144764628969742e-09, "13": 2.089199288860373e-10, "14": 1.8215946515839422e-11, "15": 1.3390427132307843e-12, "2": 0.09602374194311264, "3": 0.03472217891828999, "4": 0.00988982326602913, "5": 0.0023137158183501056, "6": 0.00045822898265172884, "7": 7.857767783987687e-05, "8": 1.187154690314264e-05, "9": 1.602063759617554e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.3024 |
| Legacy raw p draw | 0.2764 |
| Legacy raw p away | 0.4212 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2392 |
| Legacy lambda away | 1.4992 |
| Legacy model home team | Erzurumspor |
| Legacy model away team | Corum |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 63.8% |
| Market reference home draw last update utc | 2026-10-30T07:28:46Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 64.3% |
| Market reference draw away last update utc | 2026-10-30T07:28:46Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 71.9% |
| Market reference home away last update utc | 2026-10-30T07:28:46Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.50 |
| Market reference dc home draw odds | 1.51 |
| Market reference dc home away odds | 1.34 |
| Market p over 1 5 | 72.9% |
| Market over 1 5 odds | 1.31 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference over 1 5 odds | 1.33 |
| Market reference over 1 5 opposite odds | 3.25 |
| Market reference over 1 5 last update utc | 2026-10-30T07:28:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 75.3% |
| Market under 3 5 odds | 1.31 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 3 5 odds | 1.29 |
| Market reference under 3 5 opposite odds | 3.51 |
| Market reference under 3 5 last update utc | 2026-10-30T07:28:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 53.6% |
| Market reference btts yes odds | 1.74 |
| Market reference btts yes opposite odds | 1.98 |
| Market reference btts yes last update utc | 2026-10-30T07:28:46Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,438.6446 |
| Elo away rating | 1,451.6385 |
| Elo rating diff | 47.0060 |
| Elo home expectancy | 0.5672 |

</details>


---

## 2026-10-31 — Fenerbahce vs Goztepe

The model's most likely 1X2 outcome is **Fenerbahce win** at **71.9%**. Expected goals are 2.40 for Fenerbahce and 1.05 for Goztepe (3.45 combined). The most likely exact score is 2-1 at 10.5%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 67.4%; Under 3.5 goals: 55.1%; Double Chance 1X: 88.4%; Double Chance X2: 28.1%; Double Chance 12 (either team wins): 83.5%; Under 4.5 goals: 73.6%; BTTS Yes (both teams score): 58.0%; BTTS No (at least one team does not score): 42.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Fenerbahce win | 71.9% | 1.39 |
| Draw | 16.5% | 6.04 |
| Goztepe win | 11.6% | 8.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Fenerbahce expected goals | 2.40 |
| Goztepe expected goals | 1.05 |
| Expected total goals | 3.45 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 86.5% |
| Under 1.5 | 13.5% |
| Over 2.5 | 67.4% |
| Under 2.5 | 32.6% |
| Over 3.5 | 44.9% |
| Under 3.5 | 55.1% |
| Over 4.5 | 26.4% |
| Under 4.5 | 73.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.53% |
| 2 | 2-0 | 10.18% |
| 3 | 3-1 | 8.27% |
| 4 | 3-0 | 8.00% |
| 5 | 1-0 | 7.78% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Fenerbahce win | 71.9% | 74.2% | 1.32 | -5.1% |
| Draw | 16.5% | 15.3% | 5.74 | -5.0% |
| Goztepe win | 11.6% | 10.5% | 8.18 | -5.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T16:00:00+00:00 |
| Fixture id | dc20aff5555a04cd21c2355e222a3297 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Fenerbahce |
| Matched away-team name | Goztep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.5518 |
| Dc lambda away | 1.0230 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 2.0452 |
| Shot lambda away | 1.1229 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 58.0% |
| P btts no | 42.0% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.70 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.43 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.06 |
| Fair Over 3.5 odds | 2.23 |
| Fair Under 3.5 odds | 1.81 |
| Fair Over 4.5 odds | 3.79 |
| Fair Under 4.5 odds | 1.36 |
| Goal margin distribution | {"-1": 0.07357518868774401, "-10": 1.3138587622316633e-08, "-11": 1.2131974385616256e-09, "-12": 1.0296903317853997e-10, "-13": 8.084500055676507e-12, "-14": 5.904257493012866e-13, "-15": 4.030145329031444e-14, "-16": 2.581094429729892e-15, "-17": 1.5461409838014544e-16, "-18": 7.823855278751995e-18, "-2": 0.030781493211073468, "-3": 0.00897377786215363, "-4": 0.0020842788881070646, "-5": 0.00040030002182216476, "-6": 6.5358150333353e-05, "-7": 9.265708298936798e-06, "-8": 1.1595746964661176e-06, "-9": 1.2980657691812195e-07, "0": 0.1654560506063451, "1": 0.2357678596448119, "10": 6.660290051946138e-05, "11": 1.4016620235394071e-05, "12": 2.711351467389249e-06, "13": 4.851764498657628e-07, "14": 8.075681724387608e-08, "15": 1.2563249166146869e-08, "16": 1.8338023309129188e-09, "17": 2.503600790698283e-10, "18": 2.88738141854098e-11, "2": 0.21433606691177387, "3": 0.14241254551046595, "4": 0.07538694164944627, "5": 0.03299842943867445, "6": 0.012279332807796818, "7": 0.003967537149998878, "8": 0.001131640466531849, "9": 0.00028871795810201783} |
| Raw goal margin distribution | {"-1": 0.08975072302219127, "-10": 1.8352489286149777e-08, "-11": 1.7242947093887327e-09, "-12": 1.4892297619696913e-10, "-13": 1.1899156862028253e-11, "-14": 8.844286446058619e-13, "-15": 6.14431741656572e-14, "-16": 4.00510975401773e-15, "-17": 2.4407372005031864e-16, "-18": 1.2520235307184777e-17, "-2": 0.037876730208613506, "-3": 0.011185656750552476, "-4": 0.0026360500634945473, "-5": 0.000514186410942133, "-6": 8.531855711132388e-05, "-7": 1.2297407394217912e-05, "-8": 1.5651379577900888e-06, "-9": 1.7822236649230007e-07, "0": 0.19423079555287226, "1": 0.21438323655785999, "10": 6.940145711795023e-05, "11": 1.4861151658508294e-05, "12": 2.9252974892371805e-06, "13": 5.327112667549925e-07, "14": 9.024140602906591e-08, "15": 1.4288415068755235e-08, "16": 2.122717484208967e-09, "17": 2.9482625559038183e-10, "18": 3.44687066852694e-11, "2": 0.19674658479633045, "3": 0.1324230453109352, "4": 0.07112513404444312, "5": 0.03161967484186242, "6": 0.01195770039748336, "7": 0.003928123083534724, "8": 0.001139440132419551, "9": 0.0002957116637129334} |
| Unadjusted home-win probability | 66.4% |
| Unadjusted draw probability | 19.4% |
| Unadjusted away-win probability | 14.2% |
| Raw p over 1 5 | 86.7% |
| Raw p under 3 5 | 54.7% |
| Raw p btts yes | 60.0% |
| P home draw | 88.4% |
| P draw away | 28.1% |
| P home away | 83.5% |
| Raw p home draw | 85.8% |
| Raw p draw away | 33.6% |
| Raw p home away | 80.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9822 |
| Totals anchor target over 2 5 | 0.6736 |
| Totals anchor reference over odds | 1.44 |
| Totals anchor reference under odds | 2.81 |
| Totals anchor reference last update utc | 2026-10-30T07:28:45Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.6839 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.52, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 2.5, "market_key": "alternate_spreads", "opposite_price": 3.33, "price": 1.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 3.11, "price": 1.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.4, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.72, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 2.67, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.19, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.91, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.19, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.22, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.5, "price": 2.67, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.4, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.11, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -2.5, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.33, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.99, "price": 1.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.9, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.32 |
| Reference draw odds | 5.74 |
| Reference away odds | 8.18 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.61 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:25Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.2% |
| Away probability edge | +1.1% |
| Over 2.5 probability edge | +1.2% |
| Under 2.5 probability edge | -1.2% |
| Raw edge prob home | -0.0785 |
| Raw ev home | -0.1239 |
| Raw edge prob draw | 0.0411 |
| Raw ev draw | 0.1149 |
| Raw edge prob away | 0.0374 |
| Raw ev away | 0.1621 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.03172138831291119, 0.01972684891851152, 0.013572529984166845, 0.004715919693957312, 0.0012289472883352563, 0.0002562064726321444, 4.4510830015286664e-05, 6.6281831266646205e-06, 8.636372339568632e-07, 1.0002664314865411e-07, 1.042659585712017e-08, 9.880449461500044e-10, 8.582667758884004e-11, 6.8818593865749245e-12, 5.123946717069604e-13, 3.5607394143914566e-14, 2.3197813638514344e-15, 1.4224105990153963e-16, 8.237194495813165e-18], [0.06519040067645367, 0.07389235656117119, 0.03470583341757372, 0.012058910424222179, 0.0031424973765169784, 0.0006551364535608499, 0.00011381705942742893, 1.6948691196375808e-05, 2.2083760367364517e-06, 2.557745695523237e-07, 2.6661477215501616e-08, 2.5264945702945598e-09, 2.1946434295278057e-10, 1.7597357733028187e-11, 1.3102261804585553e-12, 9.105040040686619e-14, 5.931830371562223e-15, 3.6371955234880944e-16, 2.1063036908619183e-17], [0.09249039744420978, 0.09641031273857877, 0.04497407638942002, 0.015417705352971031, 0.004017784104798038, 0.0008376130555462754, 0.00014551877612996542, 2.1669447553017316e-05, 2.823479887086126e-06, 3.270160247827765e-07, 3.4087557293557765e-08, 3.230204677732748e-09, 2.8059223064903105e-10, 2.2498788611422568e-11, 1.6751663695488175e-12, 1.164108693371975e-13, 7.5840361736869e-15, 4.650271618208969e-16, 2.692977105489951e-17], [0.07883463461782812, 0.08217579325162921, 0.04282927820539032, 0.01331951029579135, 0.003424577584566322, 0.0007139435120812867, 0.0001240336279575316, 1.8470057729428162e-05, 2.4066066467439115e-06, 2.7873367982309115e-07, 2.9054693227725353e-08, 2.753280476099874e-09, 2.391641358570303e-10, 1.9176950565004728e-11, 1.4278361031707526e-12, 9.922336375813922e-14, 6.464289669007445e-15, 3.963681355313615e-16, 2.295371973869352e-17], [0.05039630967427152, 0.052532199134483815, 0.02737930578391058, 0.00951323058441187, 0.002218895193160708, 0.00045639988691783433, 7.929049401793697e-05, 1.18072818317272e-05, 1.538462053149904e-06, 1.781849933485586e-07, 1.8573680521178865e-08, 1.760078881145421e-09, 1.5288952516949596e-10, 1.2259174460150496e-11, 9.127672217716532e-13, 6.343013310227526e-14, 4.1324012670672104e-15, 2.5338471345860403e-16, 1.4673534972736922e-17], [0.025773322003430334, 0.026865643389214027, 0.01400212969481302, 0.0048651886761086165, 0.0012678461082372288, 0.00023657306403103605, 4.055018010929183e-05, 6.038396037353438e-06, 7.867893133876413e-07, 9.112610108624736e-08, 9.498819496015097e-09, 9.001270142277348e-10, 7.818967278782096e-11, 6.26949974908565e-12, 4.668009160382511e-13, 3.243898721417675e-14, 2.1133632440924608e-15, 1.295842067191982e-16, 7.504234818487465e-18], [0.010984007416843784, 0.011449530107377363, 0.005967391258253967, 0.00207343347107559, 0.0005403273607663282, 0.00011264548812024555, 1.7515853659696037e-05, 2.5734279365035894e-06, 3.353118256386603e-07, 3.883588503128069e-08, 4.0481822165417216e-09, 3.836137925511877e-10, 3.3322671625633124e-11, 2.6719191160026415e-12, 1.989400017301298e-13, 1.3824763300128498e-14, 9.006676572196255e-16, 5.522586058250652e-17, 3.1981353002547754e-18], [0.004012402068327691, 0.004182455140532108, 0.00217985768931854, 0.0007574147059593048, 0.00019737883794472414, 4.114882413756873e-05, 7.148797989760281e-06, 9.528043740531101e-07, 1.224877052308011e-07, 1.418655136611541e-08, 1.47878038335181e-09, 1.4013216818399624e-10, 1.2172602537381948e-11, 9.760384694399525e-13, 7.267177125090242e-14, 5.050115750514996e-15, 3.2900931632312255e-16, 2.017372611080214e-17, 1.1682625663431451e-18], [0.0012824963174713616, 0.0013368508998793396, 0.0006967545653588621, 0.0002420947738162043, 6.308880029971408e-05, 1.3152524230131219e-05, 2.284992116962856e-06, 3.402620483377508e-07, 3.968188391800277e-08, 4.534490705275806e-09, 4.726670866232582e-10, 4.479087254836275e-11, 3.890766095318425e-12, 3.119741544966456e-13, 2.322830001237848e-14, 1.614183908428454e-15, 1.0516225179149078e-16, 6.4481896395699366e-18, 3.734153291868857e-19], [0.00036438063258603616, 0.0003798237624039983, 0.00019796070041217879, 6.878354785676935e-05, 1.792468067871645e-05, 3.7368724056280956e-06, 6.492080029318476e-07, 9.667466387956986e-08, 1.2596489522261473e-08, 1.3057973339171976e-09, 1.3429335404717643e-10, 1.272590513587762e-11, 1.1054377246491293e-12, 8.863755647276538e-14, 6.5995843708125905e-15, 4.586191364845727e-16, 2.9878516850252934e-17, 1.832048472882796e-18, 1.0609411661681338e-19], [9.317447483905756e-05, 9.712338260742056e-05, 5.061982622065302e-05, 1.7588396242789965e-05, 4.5834563078839384e-06, 9.555423444541948e-07, 1.6600666809646e-07, 2.4720334265006493e-08, 3.2210035086738074e-09, 3.7305729289431063e-10, 3.480521266174721e-11, 3.2540959146809018e-12, 2.826675466543786e-13, 2.2665194131626074e-14, 1.687556233552903e-15, 1.1727186730486425e-16, 7.640129215251096e-18, 4.684665952992078e-19, 2.712894900348812e-20], [2.165937580142017e-05, 2.2577340485501953e-05, 1.1767105111239238e-05, 4.08860564682446e-06, 1.0654720921510715e-06, 2.2212575674242269e-07, 3.8589976665321916e-08, 5.746498820705509e-09, 7.487557678491401e-10, 8.672104797172665e-11, 9.039644749082945e-12, 7.667034817225874e-13, 6.570901129765445e-14, 5.268760120805611e-15, 3.922899990763309e-16, 2.7261065321567914e-17, 1.7760275024932635e-18, 1.0889993268568432e-19, 6.306406369116443e-21], [4.615368255891537e-06, 4.81097615806676e-06, 2.5074371437145325e-06, 8.712356665410091e-07, 2.2704006416149643e-07, 4.7332488982329924e-08, 8.223088002611959e-09, 1.2245139695052226e-09, 1.5955139400277757e-10, 1.847927546924555e-11, 1.9262461578748935e-12, 1.8253491431045273e-13, 1.4191668482247987e-14, 1.1227132504843025e-15, 8.359256635280794e-17, 5.80902499963551e-18, 3.784513936020388e-19, 2.3205345204513106e-20, 1.3438239417252175e-21], [9.078303015587029e-07, 9.463058404482199e-07, 4.932060221656452e-07, 1.7136967063787185e-07, 4.4658159108004724e-08, 9.310171012140002e-09, 1.6174588997585718e-09, 2.408585457465378e-10, 3.138332243516147e-11, 3.6348228985665082e-12, 3.7888734623670136e-13, 3.5904117963267576e-14, 3.118816779087305e-15, 2.2382843954689507e-16, 1.6442428970486662e-17, 1.142619315468352e-18, 7.444035312685659e-20, 4.564427878077861e-21, 2.6432649067621414e-22], [1.6581289694318892e-07, 1.7284035631942631e-07, 9.008282625585409e-08, 3.130023473316312e-08, 8.156699243387502e-09, 1.7004790696112403e-09, 2.954247565817448e-10, 4.3992201136254475e-11, 5.7320840687314366e-12, 6.638911629761008e-13, 6.920281068692889e-14, 6.557795880416998e-15, 5.69643956902062e-16, 4.567588682148728e-17, 3.0438812800840557e-18, 2.0869651351773011e-19, 1.3596341276828284e-20, 8.336811494977439e-22, 4.8278561623904753e-23], [2.826628386654899e-08, 2.9464261618891292e-08, 1.5356505949723586e-08, 5.335781090419865e-09, 1.39048035754813e-09, 2.8988230093600604e-10, 5.036134211928532e-11, 7.499392798485012e-12, 9.771538789844502e-13, 1.1317416446565886e-13, 1.1797069632707683e-14, 1.117913764924223e-15, 9.710775268690156e-17, 7.786412315049766e-18, 5.797439264347749e-19, 3.605900225560474e-20, 2.3177813617777943e-21, 1.4211842661411313e-22, 8.230092789450093e-24], [4.5174192852709735e-09, 4.708875927654769e-09, 2.4542234295522674e-09, 8.527459963837728e-10, 2.2222173995825261e-10, 4.6327982231040826e-11, 8.048574732917822e-12, 1.198526902780821e-12, 1.5616533812658627e-13, 1.8087101776991215e-14, 1.8853666835047133e-15, 1.7866109407168868e-16, 1.5519423664186496e-17, 1.2443973647594889e-18, 9.265266018553271e-20, 6.438630165138049e-21, 3.7544148113507534e-22, 2.2712873195854755e-23, 1.3153048367503908e-24], [6.794901231290795e-10, 7.082881800044756e-10, 3.6915337608134173e-10, 1.282662612190718e-10, 3.342560606196507e-11, 6.968449099495859e-12, 1.2106308250189092e-12, 1.8027708771673248e-13, 2.3489695804440555e-14, 2.7205814287744922e-15, 2.8358847364358317e-16, 2.6873407391022332e-17, 2.3343627036908706e-18, 1.8717671865413468e-19, 1.3936401184405e-20, 9.684701214157562e-22, 6.309473055026034e-23, 3.462684523523278e-24, 1.9784230531574111e-25], [9.652777849292608e-11, 1.0061880551520825e-10, 5.244160894083585e-11, 1.8221393997684863e-11, 4.748412652538658e-12, 9.899318448041464e-13, 1.7198116666654525e-13, 2.5610006971602193e-14, 3.3369258452731395e-15, 3.8648344190696266e-16, 4.0286332994739736e-17, 3.8176129831661884e-18, 3.316175442644592e-19, 2.659016256789182e-20, 1.9797930841464895e-21, 1.3758002680971797e-22, 8.963182785615593e-24, 5.495917155746437e-25, 2.848632532389478e-26]] |
| Legacy trial inputs | {"lambda_home": 2.5570644130504854, "lambda_away": 1.0423818623628847, "rho": -0.0948277249952374, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7180 |
| Legacy p draw | 0.1664 |
| Legacy p away | 0.1156 |
| Legacy p over 1 5 | 0.8834 |
| Legacy p under 3 5 | 0.5113 |
| Legacy p btts yes | 0.5993 |
| Legacy p over 2 5 | 0.7034 |
| Legacy goal margin distribution | {"-1": 0.07377461592839644, "-10": 1.3253805736052551e-08, "-11": 1.2315015137078477e-09, "-12": 1.0520269023878428e-10, "-13": 8.315221614987963e-12, "-14": 6.114401499580176e-13, "-15": 4.202720539703638e-14, "-16": 2.710430687255143e-15, "-17": 1.6330409681015883e-16, "-18": 8.237194495813165e-18, "-2": 0.030448846899381654, "-3": 0.008832698185708001, "-4": 0.0020497063562052394, "-5": 0.00039428766617726694, "-6": 6.458124290851186e-05, "-7": 9.194470896200932e-06, "-8": 1.156412004400902e-06, "-9": 1.301702293134486e-07, "0": 0.16638130949778682, "1": 0.2153312158400023, "10": 0.00011843907695264499, "11": 2.6996296260966348e-05, "12": 5.657322065856255e-06, "13": 1.0969143253621432e-06, "14": 1.9786439666550408e-07, "15": 3.3362534564282784e-08, "16": 5.278149074216285e-09, "17": 7.801089286442878e-10, "18": 9.652777849292608e-11, "2": 0.20749454631723022, "3": 0.1476536029763332, "4": 0.08405375661682764, "5": 0.03966372464351543, "6": 0.01593681472244987, "7": 0.005565916531889762, "8": 0.0017172651650610867, "9": 0.00047418876619315976} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.6939 |
| Legacy raw p draw | 0.1796 |
| Legacy raw p away | 0.1265 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.5571 |
| Legacy lambda away | 1.0424 |
| Legacy model home team | Fenerbahce |
| Legacy model away team | Goztep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 88.8% |
| Market reference home draw last update utc | 2026-10-30T07:28:46Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 28.5% |
| Market reference draw away last update utc | 2026-10-30T07:28:46Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 82.7% |
| Market reference home away last update utc | 2026-10-30T07:28:46Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 3.36 |
| Market reference dc home draw odds | 1.08 |
| Market reference dc home away odds | 1.16 |
| Market p over 1 5 | 86.0% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 5.50 |
| Market reference over 1 5 last update utc | 2026-10-30T07:28:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 56.7% |
| Market under 3 5 odds | 1.71 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 3 5 odds | 1.68 |
| Market reference under 3 5 opposite odds | 2.15 |
| Market reference under 3 5 last update utc | 2026-10-30T07:28:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 54.7% |
| Market reference btts yes odds | 1.71 |
| Market reference btts yes opposite odds | 2.02 |
| Market reference btts yes last update utc | 2026-10-30T07:28:46Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,643.4256 |
| Elo away rating | 1,515.6231 |
| Elo rating diff | 187.8026 |
| Elo home expectancy | 0.7467 |

</details>


---

## 2026-10-31 — Kocaelispor vs Çaykur Rizespor

The model's most likely 1X2 outcome is **Kocaelispor win** at **38.5%**. Expected goals are 1.19 for Kocaelispor and 0.89 for Çaykur Rizespor (2.09 combined). The most likely exact score is 1-1 at 13.7%. Goal-market probabilities: at least one goal: 91.7%; Over 2.5 goals: 49.6%; Under 3.5 goals: 72.2%; Double Chance 1X: 67.2%; Double Chance X2: 61.5%; Double Chance 12 (either team wins): 71.3%; Under 4.5 goals: 86.9%; BTTS Yes (both teams score): 55.0%; BTTS No (at least one team does not score): 45.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kocaelispor win | 38.5% | 2.59 |
| Draw | 28.7% | 3.48 |
| Çaykur Rizespor win | 32.8% | 3.05 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kocaelispor expected goals | 1.19 |
| Çaykur Rizespor expected goals | 0.89 |
| Expected total goals | 2.09 |
| Over 0.5 | 91.7% |
| Under 0.5 | 8.3% |
| Over 1.5 | 75.6% |
| Under 1.5 | 24.4% |
| Over 2.5 | 49.6% |
| Under 2.5 | 50.4% |
| Over 3.5 | 27.8% |
| Under 3.5 | 72.2% |
| Over 4.5 | 13.1% |
| Under 4.5 | 86.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 13.70% |
| 2 | 0-0 | 8.32% |
| 3 | 1-2 | 8.29% |
| 4 | 0-1 | 8.05% |
| 5 | 1-0 | 8.02% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kocaelispor win | 38.5% | 37.3% | 2.57 | -1.0% |
| Draw | 28.7% | 27.2% | 3.47 | -0.4% |
| Çaykur Rizespor win | 32.8% | 35.5% | 2.69 | -11.9% |
| Over 2.5 | 49.6% | 49.6% | 1.94 | -3.8% |
| Under 2.5 | 50.4% | 50.4% | 1.91 | -3.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T13:00:00+00:00 |
| Fixture id | 7d597f0fe7ec1c85b6e7f9f2ce731746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 14.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | Pinnacle |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Kocaelispor |
| Matched away-team name | Rizespor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1503 |
| Dc lambda away | 0.8781 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2856 |
| Shot lambda away | 0.9314 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 55.0% |
| P btts no | 45.0% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 12.02 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.10 |
| Fair Over 2.5 odds | 2.02 |
| Fair Under 2.5 odds | 1.98 |
| Fair Over 3.5 odds | 3.60 |
| Fair Under 3.5 odds | 1.38 |
| Fair Over 4.5 odds | 7.61 |
| Fair Under 4.5 odds | 1.15 |
| Goal margin distribution | {"-1": 0.19156952579204084, "-10": 1.058597300015844e-07, "-11": 1.0907717441428479e-08, "-12": 1.032300902136238e-09, "-13": 9.030202252444395e-11, "-14": 7.304295946727633e-12, "-15": 5.005763730025693e-13, "-2": 0.09377491040988477, "-3": 0.03162218395813424, "-4": 0.008381455609821786, "-5": 0.001822427777888241, "-6": 0.0003351958067738541, "-7": 5.335446062479647e-05, "-8": 7.479663309966292e-06, "-9": 9.363716303779016e-07, "0": 0.2870610778528432, "1": 0.18633807137931477, "10": 1.3344793652675289e-06, "11": 1.8314742964631847e-07, "12": 2.308655455905174e-08, "13": 2.689900168378788e-09, "14": 2.89803024550786e-10, "15": 2.645335546570354e-11, "2": 0.11933856055487145, "3": 0.05360087335154233, "4": 0.018922796650807178, "5": 0.005480271410809905, "6": 0.0013425676738131947, "7": 0.0002846388727573433, "8": 5.3148546728964103e-05, "9": 8.862239041482894e-06} |
| Raw goal margin distribution | {"-1": 0.1690830574672, "-10": 1.2316835452712863e-08, "-11": 9.931027972681856e-10, "-12": 7.3286580330521e-11, "-13": 4.658874618476682e-12, "-2": 0.06984384678635372, "-3": 0.01919602076434632, "-4": 0.004080838229423859, "-5": 0.000705315957293515, "-6": 0.00010255265391419175, "-7": 1.2858057189034381e-05, "-8": 1.4163577555055578e-06, "-9": 1.3907872270480756e-07, "0": 0.3217911490824978, "1": 0.2294302133555721, "10": 2.1645011403817437e-07, "11": 2.324549253298529e-08, "12": 2.28483515685897e-09, "13": 1.9346272736937942e-10, "2": 0.1239081540052621, "3": 0.045359558093658624, "4": 0.012843779788564614, "5": 0.0029567394053261983, "6": 0.0005726141970397382, "7": 9.562609664043217e-05, "8": 1.4030072283168693e-05, "9": 1.8349891682752189e-06} |
| Unadjusted home-win probability | 41.5% |
| Unadjusted draw probability | 32.2% |
| Unadjusted away-win probability | 26.3% |
| Raw p over 1 5 | 62.9% |
| Raw p under 3 5 | 84.1% |
| Raw p btts yes | 42.4% |
| P home draw | 67.2% |
| P draw away | 61.5% |
| P home away | 71.3% |
| Raw p home draw | 73.7% |
| Raw p draw away | 58.5% |
| Raw p home away | 67.8% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.2844 |
| Totals anchor target over 2 5 | 0.4959 |
| Totals anchor reference over odds | 1.94 |
| Totals anchor reference under odds | 1.91 |
| Totals anchor reference last update utc | 2026-10-30T07:28:45Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.3565 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.61, "price": 1.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 4.38, "price": 1.23, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.3, "price": 1.35, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 3.15, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.69, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 2.58, "price": 1.53, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.34, "price": 1.64, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 2.24, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.98, "price": 1.89, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.89, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.24, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.64, "price": 2.34, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.49, "price": 2.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.15, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.3, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.23, "price": 4.38, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.21, "price": 4.61, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "away"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 2.57 |
| Reference draw odds | 3.47 |
| Reference away odds | 2.69 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.94 |
| Reference Under 2.5 odds | 1.91 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market best over 2 5 last update utc | 2026-10-30T07:28:45Z |
| Market best under 2 5 last update utc | 2026-10-30T07:28:45Z |
| Home probability edge | +1.3% |
| Draw probability edge | +1.5% |
| Away probability edge | -2.8% |
| Over 2.5 probability edge | -0.0% |
| Under 2.5 probability edge | +0.0% |
| Raw edge prob home | 0.0426 |
| Raw ev home | 0.0670 |
| Raw edge prob draw | 0.0496 |
| Raw ev draw | 0.1166 |
| Raw edge prob away | -0.0922 |
| Raw ev away | -0.2925 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.13034779079219613, 0.11892145530102081, 0.05897850877778446, 0.01735061301248363, 0.003828222069540875, 0.0006757241004995252, 9.939406415945225e-05, 1.2531547352997471e-05, 1.3824740978236568e-06, 1.355678736102367e-07, 1.1964624542130667e-08, 9.599501484314873e-10, 7.060081664435324e-11, 4.79301361701942e-12], [0.13158493385391146, 0.1334227940721429, 0.06855679141169523, 0.020168403403409498, 0.004449936550413762, 0.0007854636743079342, 0.00011553595140586049, 1.4566707360848644e-05, 1.606991941991388e-06, 1.5758449350155296e-07, 1.3907714624400084e-08, 1.1158488652129593e-09, 8.206659612942637e-11, 5.571413072064433e-12], [0.08346238885965455, 0.07366023523877693, 0.03125526889822955, 0.011721905605006465, 0.0025863096423091275, 0.00045651263822116267, 6.714966421859471e-05, 8.466191658520433e-06, 9.339860709472248e-07, 9.158833848621295e-08, 8.083184114664532e-09, 6.485329951932993e-10, 4.7697225898937595e-11, 3.2381134396686064e-12], [0.03233897511906583, 0.028540957755917296, 0.012594497299711991, 0.0035627037977319057, 0.0010021113020557881, 0.00017688387608696566, 2.6018322145922667e-05, 3.280375330000687e-06, 3.618893818233011e-07, 3.54875176707766e-08, 3.131972299600991e-09, 2.5128555127646924e-10, 1.8481131712967715e-11, 1.2546641833394219e-12], [0.009397729858087307, 0.008294023230286603, 0.0036599701408386, 0.0010767095823022137, 0.0002284329354302703, 5.140258395933704e-05, 7.560943474176954e-06, 9.532794737921486e-07, 1.0516531944392173e-07, 1.0312698629940136e-08, 9.101534444519169e-10, 7.302376526906525e-11, 5.370630413324553e-12, 3.646063307272248e-13], [0.0021847897445214253, 0.0019281993809131142, 0.000850872003101637, 0.0002503140746504282, 5.522904949836714e-05, 9.373843498975809e-06, 1.7577725696246053e-06, 2.2161897069339212e-07, 2.4448895091687924e-08, 2.3975022207777144e-09, 2.1159300612032178e-10, 1.697660774201746e-11, 1.248567305704026e-12, 8.476389342846626e-14], [0.0004232676667527208, 0.0003735574350070513, 0.00016484268491334084, 4.849430229995027e-05, 1.0699734826549639e-05, 1.8886231153567359e-06, 2.6712478415949055e-07, 4.293509014712046e-08, 4.736577881734612e-09, 4.644772676948541e-10, 4.09927217144462e-11, 3.2889430968625816e-12, 2.4188971574692026e-13, 1.6421633013570453e-14], [7.028679657392043e-05, 6.20320367120207e-05, 2.7373374276593903e-05, 8.05284558327038e-06, 1.776771873264643e-06, 3.136201490000286e-07, 4.613122602606909e-08, 5.592642913103141e-09, 7.865445725730516e-10, 7.712996241395217e-11, 6.807151404356802e-12, 5.461538703532312e-13, 4.016761633238534e-14, 2.7269363329628416e-15], [1.0212697284933652e-05, 9.013277653669889e-06, 3.977361307966781e-06, 1.170081412627227e-06, 2.5816560393320216e-07, 4.556912251399294e-08, 6.70288403728311e-09, 8.450958256431864e-10, 8.964707073506645e-11, 1.1207011787819592e-11, 9.890815921919796e-13, 7.935635739276285e-14, 5.83636936460152e-15, 3.9622484792783844e-16], [1.3190299163829752e-06, 1.1641178170820493e-06, 5.136996042379403e-07, 1.5112289582261827e-07, 3.3343606049240134e-08, 5.885520169872357e-09, 8.657168938381745e-10, 1.0914909598644542e-10, 1.2041274213917044e-11, 1.1354030878346274e-12, 1.277457045328846e-13, 1.0249340261035016e-14, 7.538014277900449e-16, 5.117476935325702e-17], [1.533244239591816e-07, 1.353173961468376e-07, 5.971259251179359e-08, 1.7566569689780102e-08, 3.875870536917576e-09, 6.841345890170221e-10, 1.0063118539680706e-10, 1.2687522898402676e-11, 1.3996812427469878e-12, 1.372552369046604e-13, 1.1647938194166888e-14, 1.1913863150231768e-15, 8.762209883188134e-17, 5.9485701839487e-18], [1.6202250877661022e-08, 1.4299394342199403e-08, 6.31000840863545e-09, 1.8563120070779128e-09, 4.0957484259123303e-10, 7.229455007305461e-11, 1.0633998614268716e-11, 1.3407285265308769e-12, 1.479085070606914e-13, 1.450417177627318e-14, 1.2800744378170534e-15, 9.875581416369796e-17, 9.259289492450987e-18, 6.286032192064167e-19], [1.5694619910970024e-09, 1.3851381567441384e-09, 6.112310218890695e-10, 1.7981520967205002e-10, 3.9674249757653117e-11, 7.002949735802262e-12, 1.030082595590711e-12, 1.2987223063376418e-13, 1.432744016522532e-14, 1.4049743141916375e-15, 1.2399685643052788e-16, 9.948561303899136e-18, 7.035568053236363e-19, 6.089085198562922e-20], [1.403344013085534e-10, 1.2385297322202422e-10, 5.4653594674225114e-11, 1.6078286660425095e-11, 3.547497243443696e-12, 6.261730224385935e-13, 9.210546363696469e-14, 1.161260472441044e-14, 1.2810968021376869e-15, 1.2562663534028383e-16, 1.1087254556039319e-17, 8.895566776282878e-19, 6.542363475292189e-20, 4.2708217928388524e-21]] |
| Legacy trial inputs | {"lambda_home": 1.1624029300231924, "lambda_away": 0.8825560380573296, "rho": -0.0948277249952374, "max_goals": 13, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": {"updated_at_utc": "2026-10-30T07:28:45Z", "over": 1.94, "under": 1.91, "bookmaker": "pinnacle", "event_id": "7d597f0fe7ec1c85b6e7f9f2ce731746", "kickoff_utc": "2026-10-31T13:00:00Z", "home_team": "Kocaelispor", "away_team": "\u00c7aykur Rizespor"}} |
| Legacy p home | 0.3911 |
| Legacy p draw | 0.2988 |
| Legacy p away | 0.3101 |
| Legacy p over 1 5 | 0.6191 |
| Legacy p under 3 5 | 0.8486 |
| Legacy p btts yes | 0.4103 |
| Legacy p over 2 5 | 0.3433 |
| Legacy goal margin distribution | {"-1": 0.20025546770927793, "-10": 1.3129425297425903e-08, "-11": 1.0452548580005823e-09, "-12": 7.617222971641767e-11, "-13": 4.79301361701942e-12, "-2": 0.08191789307674219, "-3": 0.022284058722997897, "-4": 0.004684223387763832, "-5": 0.0008000986605668724, "-6": 0.00011493117248358774, "-7": 1.4233333894528882e-05, "-8": 1.5483985163854574e-06, "-9": 1.501429669678738e-07, "0": 0.298826637147451, "1": 0.21897354063581798, "10": 1.6825112760993048e-07, "11": 1.7642042629079386e-08, "12": 1.6933149643190266e-09, "13": 1.403344013085534e-10, "2": 0.11592465099948387, "3": 0.041534187874303546, "4": 0.0114990889226075, "5": 0.0025869246737234876, "6": 0.0004894321368753131, "7": 7.983175707141583e-05, "8": 1.1438424306957353e-05, "9": 1.4608406836453639e-06} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.4096 |
| Legacy raw p draw | 0.3255 |
| Legacy raw p away | 0.2649 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.1624 |
| Legacy lambda away | 0.8826 |
| Legacy model home team | Kocaelispor |
| Legacy model away team | Rizespor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Market p home draw | 64.1% |
| Market reference home draw last update utc | 2026-10-30T07:28:46Z |
| Market home draw bookmakers | 0 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 63.7% |
| Market reference draw away last update utc | 2026-10-30T07:28:46Z |
| Market draw away bookmakers | 0 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 72.3% |
| Market reference home away last update utc | 2026-10-30T07:28:46Z |
| Market home away bookmakers | 0 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc draw away odds | 1.51 |
| Market reference dc home draw odds | 1.50 |
| Market reference dc home away odds | 1.33 |
| Market p over 1 5 | 74.7% |
| Market over 1 5 odds | 1.29 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference over 1 5 odds | 1.30 |
| Market reference over 1 5 opposite odds | 3.44 |
| Market reference over 1 5 last update utc | 2026-10-30T07:28:47Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 73.5% |
| Market under 3 5 odds | 1.33 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-10-30T07:28:45Z |
| Market reference under 3 5 odds | 1.32 |
| Market reference under 3 5 opposite odds | 3.31 |
| Market reference under 3 5 last update utc | 2026-10-30T07:28:47Z |
| Market under 3 5 bookmakers | 1 |
| Market p btts yes | 55.7% |
| Market reference btts yes odds | 1.68 |
| Market reference btts yes opposite odds | 2.06 |
| Market reference btts yes last update utc | 2026-10-30T07:28:46Z |
| Market btts yes bookmakers | 0 |
| Elo home rating | 1,459.3997 |
| Elo away rating | 1,449.0338 |
| Elo rating diff | 70.3660 |
| Elo home expectancy | 0.5999 |

</details>


---

## 2026-11-01 — Amed SK vs Eyüpspor

The model's most likely 1X2 outcome is **Amed SK win** at **76.9%**. Expected goals are 2.68 for Amed SK and 0.82 for Eyüpspor (3.51 combined). The most likely exact score is 2-0 at 10.9%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 68.4%; Under 3.5 goals: 53.3%; Double Chance 1X: 91.8%; Double Chance X2: 23.1%; Double Chance 12 (either team wins): 85.1%; Under 4.5 goals: 72.2%; BTTS Yes (both teams score): 52.7%; BTTS No (at least one team does not score): 47.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Amed SK win | 76.9% | 1.30 |
| Draw | 14.9% | 6.70 |
| Eyüpspor win | 8.2% | 12.22 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Amed SK expected goals | 2.68 |
| Eyüpspor expected goals | 0.82 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 87.2% |
| Under 1.5 | 12.8% |
| Over 2.5 | 68.4% |
| Under 2.5 | 31.6% |
| Over 3.5 | 46.7% |
| Under 3.5 | 53.3% |
| Over 4.5 | 27.8% |
| Under 4.5 | 72.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.91% |
| 2 | 3-0 | 9.76% |
| 3 | 2-1 | 9.00% |
| 4 | 3-1 | 8.05% |
| 5 | 1-0 | 7.49% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Amed SK win | 76.9% | 77.3% | 1.27 | -2.3% |
| Draw | 14.9% | 14.6% | 5.94 | -11.3% |
| Eyüpspor win | 8.2% | 8.1% | 10.28 | -15.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T10:30:00+00:00 |
| Fixture id | 5706f8b2f4d8a94519bbea0efc91e36b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Amedspor |
| Matched away-team name | Eyupspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 3.0102 |
| Dc lambda away | 0.7473 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.9189 |
| Shot lambda away | 1.0061 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 52.7% |
| P btts no | 47.3% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.79 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.84 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.16 |
| Fair Over 3.5 odds | 2.14 |
| Fair Under 3.5 odds | 1.88 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.39 |
| Goal margin distribution | {"-1": 0.05650608384633331, "-10": 1.4366656362355116e-09, "-11": 1.059899359644698e-10, "-12": 7.185572819191119e-12, "-13": 4.5055361648558747e-13, "-14": 2.6274245667694288e-14, "-15": 1.4318845106841933e-15, "-16": 7.323423470197105e-17, "-17": 3.527591718035928e-18, "-18": 1.5971988354712476e-19, "-19": 6.211225302297895e-21, "-2": 0.01965978559088659, "-3": 0.004631860961788277, "-4": 0.0008657386840666321, "-5": 0.00013346638526286078, "-6": 1.7464097756634148e-05, "-7": 1.982075117349109e-06, "-8": 1.984314487754823e-07, "-9": 1.7760030282295208e-08, "0": 0.149249084328617, "1": 0.20491268596061266, "10": 0.00019697850652856686, "11": 4.726004780951542e-05, "12": 1.0419750315705464e-05, "13": 2.1247546474199084e-06, "14": 4.0295723199801235e-07, "15": 7.141724288465905e-08, "16": 1.1878883600832962e-08, "17": 1.86082779316042e-09, "18": 2.7400169224934936e-10, "19": 3.4652768202504955e-11, "2": 0.2154322859352677, "3": 0.16506458998130874, "4": 0.10033480644791108, "5": 0.05030406514525432, "6": 0.021406404525837655, "7": 0.007901036616301321, "8": 0.00257241396557744, "9": 0.0007487562281601593} |
| Raw goal margin distribution | {"-1": 0.05787311935097225, "-10": 1.4714224765497264e-09, "-11": 1.0855412013252981e-10, "-12": 7.35941132464685e-12, "-13": 4.614537311025243e-13, "-14": 2.6909890968880292e-14, "-15": 1.4665256825971336e-15, "-16": 7.500596956975825e-17, "-17": 3.612933734260935e-18, "-18": 1.6358394095020892e-19, "-19": 6.3614916973049166e-21, "-2": 0.02013540915364168, "-3": 0.004743918247593734, "-4": 0.0008866832521254799, "-5": 0.00013669529930026474, "-6": 1.788660167240239e-05, "-7": 2.030026893048983e-06, "-8": 2.032320439901625e-07, "-9": 1.8189693608909477e-08, "0": 0.15610235344758255, "1": 0.2025588842670474, "10": 0.00019471584357976334, "11": 4.6717178635503444e-05, "12": 1.0300060186103881e-05, "13": 2.1003479052796535e-06, "14": 3.9832852191759495e-07, "15": 7.05968835864359e-08, "16": 1.174243262315811e-08, "17": 1.839452739730023e-09, "18": 2.708542753667253e-10, "19": 3.425471698327757e-11, "2": 0.2129576471538477, "3": 0.16316851746815872, "4": 0.09918227537725774, "5": 0.049726229794665656, "6": 0.021160512325509247, "7": 0.007810278578158451, "8": 0.002542865027109614, "9": 0.0007401553761941191} |
| Unadjusted home-win probability | 76.0% |
| Unadjusted draw probability | 15.6% |
| Unadjusted away-win probability | 8.4% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 53.5% |
| Raw p btts yes | 53.0% |
| P home draw | 91.8% |
| P draw away | 23.1% |
| P home away | 85.1% |
| Raw p home draw | 91.6% |
| Raw p draw away | 24.0% |
| Raw p home away | 84.4% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6839 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.84, "price": 2.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.88, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.84, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.27 |
| Reference draw odds | 5.94 |
| Reference away odds | 10.28 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.65 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:46Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:46Z |
| Home probability edge | -0.4% |
| Draw probability edge | +0.3% |
| Away probability edge | +0.1% |
| Over 2.5 probability edge | +9.2% |
| Under 2.5 probability edge | -9.2% |
| Raw edge prob home | -0.0126 |
| Raw ev home | -0.0347 |
| Raw edge prob draw | 0.0098 |
| Raw ev draw | -0.0728 |
| Raw edge prob away | 0.0028 |
| Raw ev away | -0.1386 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.03033389663211894, 0.014569801697614833, 0.007417205976072802, 0.0017796915292011934, 0.0003202656717362201, 4.610691181462911e-05, 5.531468362805814e-06, 5.688110718175339e-07, 5.118040318155809e-08, 4.09342503979502e-09, 2.946541012442182e-10, 1.9281705869999002e-11, 1.1566177586305655e-12, 6.404307148080678e-14, 3.292833452364375e-15, 1.5801712453847863e-16, 7.109021381763918e-18, 3.0101389791240234e-19, 1.2037593985630489e-20, 4.560492423178782e-22, 1.6413734013926232e-23], [0.06147238275104449, 0.061001650060154414, 0.022919116183461836, 0.005499234760375576, 0.0009896187545250438, 0.00014247004493997103, 1.709219974222886e-05, 1.7576223558413356e-06, 1.581470988696507e-07, 1.2648655622885607e-08, 9.104791753303035e-10, 5.958034042406747e-11, 3.573941033243993e-12, 1.9789265671593568e-13, 1.0174833045082486e-14, 4.882718435967569e-16, 2.1966827876287413e-17, 9.301309039207616e-19, 3.7196083810535215e-20, 1.4091890671205752e-21, 5.071832683131116e-23], [0.1019324468308104, 0.0733733077229149, 0.03098267986482302, 0.008496299064618469, 0.001528957621337443, 0.0002201157365169398, 2.640739066616117e-05, 2.715520582152299e-06, 2.4433673169947936e-07, 1.9542130063577164e-08, 1.4066872397324484e-09, 9.205142400214283e-11, 5.5217267821602635e-12, 3.057434838507673e-13, 1.5720082566120405e-14, 7.54378343314686e-16, 3.393867461028142e-17, 1.4370490937933652e-18, 5.746782340773117e-20, 2.1771923321253907e-21, 7.83596430399441e-23], [0.10499018989613487, 0.07557434115088757, 0.027200070054359458, 0.007657017598983419, 0.001574822894949284, 0.0002267187112107644, 2.719955271262705e-05, 2.796980063279091e-06, 2.5166628151592013e-07, 2.0128349805586833e-08, 1.4488846781939395e-09, 9.48127587110308e-11, 5.68736610802469e-12, 3.149150974691921e-13, 1.6191649519993952e-14, 7.770079889242939e-16, 3.495675815641803e-17, 1.4801573192671533e-18, 5.919172824831593e-20, 2.2425031822267715e-21, 8.071025525966635e-23], [0.08110474375781368, 0.05838105045597199, 0.021012008018423622, 0.005041641394688032, 0.0010644440476551926, 0.0001751398201683579, 2.1011608372812125e-05, 2.160662358572564e-06, 1.9441177594804916e-07, 1.5549116111369738e-08, 1.1192609583409078e-09, 7.324269541599012e-11, 4.393480679523926e-12, 2.432713790781135e-13, 1.2508021812653008e-14, 6.002373545740104e-16, 2.7004036431260153e-17, 1.1434190205692195e-18, 4.5725509753921686e-20, 1.73232990768483e-21, 6.234853540067707e-23], [0.050122621677534694, 0.03607941002661556, 0.012985392466532625, 0.0031157275462743972, 0.000560692996051119, 9.470349443534761e-05, 1.2985145486086574e-05, 1.335286408092362e-06, 1.2014621394525918e-07, 9.609332674763064e-09, 6.917017547195136e-10, 4.5263886461942007e-11, 2.715165103103113e-12, 1.5034138243399225e-13, 7.729940521383612e-15, 3.7094587130285974e-16, 1.6688457901453124e-17, 7.066314044222211e-19, 2.825830303159595e-20, 1.0705775341926307e-21, 3.8531310343181304e-23], [0.025813093532185624, 0.018580855398881258, 0.0066874624485371075, 0.0016045961659829932, 0.00028875625945950703, 4.157067261890984e-05, 5.851223383036002e-06, 6.876709914755528e-07, 6.187516443292918e-08, 4.948795470264132e-09, 3.5622562215165295e-10, 2.331085038586529e-11, 1.3983069603308576e-12, 7.742564208819351e-14, 3.980910634731209e-15, 1.9103670460259477e-16, 8.594536963560919e-18, 3.6391437488007394e-19, 1.4552994133233226e-20, 5.513462205022128e-22, 1.984358129159877e-23], [0.011394612003249465, 0.008202102459929694, 0.0029520305186345854, 0.0007083130392907145, 0.00012746498345687143, 1.835044236817116e-05, 2.201511387514442e-06, 2.656034877568595e-07, 2.7313405519233494e-08, 2.1845349220459623e-09, 1.572478225042308e-10, 1.0290052809111828e-11, 6.172512897203368e-13, 3.417781559569342e-14, 1.7572838391420388e-15, 8.432887459272449e-17, 3.79386585049384e-18, 1.6064185019099539e-19, 6.424093316323938e-21, 2.433794405249189e-22, 8.759504523964854e-24], [0.004401159230483864, 0.003168055124702754, 0.0011402192862778977, 0.0002735853112029968, 4.923324184664656e-05, 7.087842814578238e-06, 8.503319078711415e-07, 8.744119503044369e-08, 9.230749698707186e-09, 8.437747624697636e-10, 6.073683819077133e-11, 3.9745241777494356e-12, 2.384127875969815e-13, 1.3201152311624543e-14, 6.787493937498296e-16, 3.257195635132149e-17, 1.4653774698389717e-18, 6.204777850869194e-20, 2.4813005996663945e-21, 9.400510266350262e-23, 3.383351199594948e-24], [0.001511061353991942, 0.0010876965398337012, 0.00039147442942694566, 9.393075077023685e-05, 1.6903375949437658e-05, 2.433487360806342e-06, 2.9194664786283035e-07, 3.002141109601468e-08, 2.701262334897416e-09, 2.534749995918434e-10, 2.085293536258774e-11, 1.364583640579507e-12, 8.185487749228322e-14, 4.532385683320115e-15, 2.3303678059111465e-16, 1.118301381270026e-17, 5.031118275265686e-19, 2.1303023884284326e-20, 8.519113368640177e-22, 3.2275014439149726e-23, 1.1616146967098349e-24], [0.0004669169340072335, 0.00033609749343912923, 0.00012096533330521224, 2.9024538310620077e-05, 5.223131709266867e-06, 7.51945944783332e-07, 9.021131627361382e-08, 9.276595676601934e-09, 8.346882302478952e-10, 6.675863200995811e-11, 5.637912172609048e-12, 4.216554198627263e-13, 2.529310165418895e-14, 1.400504103558321e-15, 7.200820722273588e-17, 3.4555436869536876e-18, 1.5546121363695078e-19, 6.582619938532254e-21, 2.632400255646216e-22, 9.972957581871518e-24, 3.5893815380337684e-25], [0.0001311609237060551, 9.441263420547318e-05, 3.398018726062455e-05, 8.15323878337584e-06, 1.467221961187674e-06, 2.112279883455163e-07, 2.5341123247851546e-08, 2.605874341177477e-09, 2.344709975419103e-10, 1.875306548561178e-11, 1.3498885658142177e-12, 1.0363730498871235e-13, 7.105046604077929e-15, 3.9341347142912643e-16, 2.02277156510343e-17, 9.70691506083717e-19, 4.367037238527517e-20, 1.8491137259339808e-21, 7.394635404019517e-23, 2.8014883017699877e-24, 1.0082876926769943e-25], [3.377386375730769e-05, 2.4311199971192123e-05, 8.74987902311605e-06, 2.0994543806938768e-06, 3.7780882612520544e-07, 5.439108766952289e-08, 6.525324920310617e-09, 6.710111707114259e-10, 6.037614940687491e-11, 4.828903768338452e-12, 3.475955431019289e-13, 2.2746111442239655e-14, 1.6007989618555516e-15, 1.013037466411452e-16, 5.2086253528577e-18, 2.49952514441874e-19, 1.124509621841803e-20, 4.761457398045052e-22, 1.9041144390689398e-23, 7.213816550554137e-25, 2.596335112503544e-26], [8.027770003911411e-06, 5.778572546222226e-06, 2.079774374183834e-06, 4.990230618274465e-07, 8.980205473010648e-08, 1.2928314782433959e-08, 1.5510161359524885e-09, 1.5949384373770773e-10, 1.4350914797401943e-11, 1.1477907621645594e-12, 8.262060552083543e-14, 5.406563858188363e-15, 3.2431403184510715e-16, 2.106848292165663e-17, 1.2380474638539469e-18, 5.941165962702587e-20, 2.6728670063335995e-21, 1.1317593139356934e-22, 4.525923621831638e-24, 1.7146649413402673e-25, 6.1712753050791035e-27], [1.7718396350255156e-06, 1.2754107138443425e-06, 4.5903490836108053e-07, 1.1014127700555077e-07, 1.9820552880813338e-08, 2.8534575024498362e-09, 3.4233066753354256e-10, 3.520249256510155e-11, 3.1674449597486916e-12, 2.533332624288465e-13, 1.8235507925650286e-14, 1.1933032621222473e-15, 7.158058284406593e-17, 3.963487807024562e-18, 2.3908942538245145e-19, 1.3112973248924602e-20, 5.899386378367063e-22, 2.4979490054691358e-23, 9.98933807813663e-25, 3.7845021747946345e-26, 1.3620856326060238e-27], [3.6499816404014413e-07, 2.62734030635685e-07, 9.456098366357938e-08, 2.268905328527887e-08, 4.0830249356360514e-09, 5.878109558971272e-10, 7.05199627970737e-11, 7.251697558799593e-12, 6.524922301954443e-13, 5.218653756749123e-14, 3.756506391226541e-15, 2.458199326890342e-16, 1.4745567715348722e-17, 8.164766969662182e-19, 4.1979900693114997e-20, 2.3635294892135052e-21, 1.215270927741948e-22, 5.145763661896011e-24, 2.057799129458839e-25, 7.796057376186205e-27, 2.8058902472824384e-28], [7.049011578089861e-08, 5.074039834637268e-08, 1.826204990463529e-08, 4.381813802390472e-09, 7.885324607211624e-10, 1.1352074180272314e-10, 1.36191379359477e-11, 1.4004810185062246e-12, 1.260122854961949e-13, 1.0078502956338372e-14, 7.25473705177654e-16, 4.747387034691201e-17, 2.8477315173445425e-18, 1.576817161612473e-19, 8.10735053451622e-21, 3.8905709554483365e-22, 2.0535450517516426e-23, 9.937734269487897e-25, 3.974115849893211e-26, 1.5056102775943077e-27, 5.418863651535512e-29], [1.2812587052795341e-08, 9.222793347753032e-09, 3.319388847266406e-09, 7.964573496626534e-10, 1.4332705635422665e-10, 2.0634018976025454e-11, 2.475473170319892e-12, 2.545574619450531e-13, 2.2904535760164054e-14, 1.831912106532994e-15, 1.318652253458418e-16, 8.629055149285998e-18, 5.176159460764157e-19, 2.8660907881465135e-20, 1.4736269523785382e-21, 7.071669339670288e-23, 3.1814683811841264e-24, 1.5804820487151962e-25, 7.223524138181149e-27, 2.7366620887985303e-28, 9.849559969277452e-30], [2.1994892852363448e-09, 1.5832427178636128e-09, 5.698271686281047e-10, 1.3672487839593254e-10, 2.4604424027449593e-11, 3.5421654863394525e-12, 4.2495529525559417e-13, 4.369893509546531e-14, 3.931936679158205e-15, 3.1447755501766435e-16, 2.263681402111352e-17, 1.481317884074573e-18, 8.885720913124752e-20, 4.920111725342391e-21, 2.529720718256459e-22, 1.2139672399685843e-23, 5.461508738944354e-25, 2.3125405674112294e-26, 1.0849949888390703e-27, 4.6979262789177713e-29, 1.690837418504962e-30], [3.5770563055989495e-10, 2.5748469816342394e-10, 9.267168884724678e-11, 2.2235734071596856e-11, 4.001447549837081e-12, 5.760667020946185e-13, 6.911099902577366e-14, 7.106811221151133e-15, 6.394556675409004e-16, 5.1143869110705894e-17, 3.681452729795585e-18, 2.409085378770585e-19, 1.4450956517694485e-20, 8.001637829982055e-22, 4.114115721037132e-23, 1.974289758839886e-24, 8.882118409876875e-26, 3.760912987454193e-27, 1.503995126877259e-28, 6.685035310727283e-30, 2.7498295582539818e-31], [5.526539867389169e-11, 3.9781298589443363e-11, 1.4317744514978708e-11, 3.435413377055225e-12, 6.182222901223945e-13, 8.90021102105138e-14, 1.0677625923673537e-14, 1.0979999247488499e-15, 9.879568388569174e-17, 7.901710441919432e-18, 5.687831988911694e-19, 3.722028744384182e-20, 2.2326678836992306e-21, 1.2362503325035211e-22, 6.3562948438288985e-24, 3.050270985370979e-25, 1.372284283650284e-26, 5.810597817656396e-28, 2.323667373095612e-29, 8.803310247579548e-31, 3.717293817275908e-32]] |
| Legacy trial inputs | {"lambda_home": 3.0899932208161287, "lambda_away": 0.7198228827441123, "rho": -0.0948277249952374, "max_goals": 20, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.8028 |
| Legacy p draw | 0.1311 |
| Legacy p away | 0.0660 |
| Legacy p over 1 5 | 0.8936 |
| Legacy p under 3 5 | 0.4798 |
| Legacy p btts yes | 0.5021 |
| Legacy p over 2 5 | 0.7233 |
| Legacy goal margin distribution | {"-1": 0.04774888065575242, "-10": 3.600839712732918e-10, "-11": 2.3178199332859865e-11, "-12": 1.3710352313691387e-12, "-13": 7.500841186478969e-14, "-14": 3.81657094382155e-15, "-15": 1.8148196409802577e-16, "-16": 8.098924960810038e-18, "-17": 3.404678843103226e-19, "-18": 1.3525142695791008e-20, "-19": 5.067675691491893e-22, "-2": 0.014694528085603958, "-20": 1.6413734013926232e-23, "-3": 0.0030189114916294147, "-4": 0.0004921444752729473, "-5": 6.618256317993163e-05, "-6": 7.554721758171885e-06, "-7": 7.480252225054825e-07, "-8": 6.53351066916756e-08, "-9": 5.1018942014485704e-09, "0": 0.13114051801500898, "1": 0.16769195731365336, "10": 0.000570598892539166, "11": 0.00015766623839393352, "12": 4.003496986381688e-05, "13": 9.402270454652562e-06, "14": 2.053657364083854e-06, "15": 4.1919876656183925e-07, "16": 8.030559025364146e-08, "17": 1.4491936872883257e-08, "18": 2.4712917279147473e-09, "19": 3.9748692914933833e-10, "2": 0.201942511455337, "20": 5.526539867389169e-11, "3": 0.1780960832735212, "4": 0.12463168888019754, "5": 0.07194677425489024, "6": 0.0352547870769002, "7": 0.014984689295619975, "8": 0.005618365429257292, "9": 0.0018833312165282888} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.8329 |
| Legacy raw p draw | 0.1160 |
| Legacy raw p away | 0.0511 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 3.0900 |
| Legacy lambda away | 0.7198 |
| Legacy model home team | Amedspor |
| Legacy model away team | Eyupspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,486.7305 |
| Elo away rating | 1,373.7821 |
| Elo rating diff | 172.9484 |
| Elo home expectancy | 0.7302 |

</details>


---

## 2026-11-01 — Basaksehir vs Samsunspor

The model's most likely 1X2 outcome is **Basaksehir win** at **53.3%**. Expected goals are 1.75 for Basaksehir and 1.03 for Samsunspor (2.78 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 93.0%; Over 2.5 goals: 53.0%; Under 3.5 goals: 69.5%; Double Chance 1X: 78.0%; Double Chance X2: 46.7%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 84.9%; BTTS Yes (both teams score): 54.1%; BTTS No (at least one team does not score): 45.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Basaksehir win | 53.3% | 1.88 |
| Draw | 24.7% | 4.05 |
| Samsunspor win | 22.0% | 4.54 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Basaksehir expected goals | 1.75 |
| Samsunspor expected goals | 1.03 |
| Expected total goals | 2.78 |
| Over 0.5 | 93.0% |
| Under 0.5 | 7.0% |
| Over 1.5 | 77.7% |
| Under 1.5 | 22.3% |
| Over 2.5 | 53.0% |
| Under 2.5 | 47.0% |
| Over 3.5 | 30.5% |
| Under 3.5 | 69.5% |
| Over 4.5 | 15.1% |
| Under 4.5 | 84.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.77% |
| 2 | 2-1 | 9.80% |
| 3 | 1-0 | 9.76% |
| 4 | 2-0 | 9.49% |
| 5 | 0-0 | 6.97% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Basaksehir win | 53.3% | 53.3% | 1.82 | -3.1% |
| Draw | 24.7% | 24.3% | 3.85 | -4.9% |
| Samsunspor win | 22.0% | 22.4% | 4.15 | -8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | f4e049de3ce6858d46dd45ab5cfa0e8c |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Buyuksehyr |
| Matched away-team name | Samsunspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8390 |
| Dc lambda away | 1.0100 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.5493 |
| Shot lambda away | 1.0853 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 54.1% |
| P btts no | 45.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.35 |
| Fair Over 1.5 odds | 1.29 |
| Fair Under 1.5 odds | 4.49 |
| Fair Over 2.5 odds | 1.89 |
| Fair Under 2.5 odds | 2.13 |
| Fair Over 3.5 odds | 3.28 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.62 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.13653672976894649, "-10": 2.8785944610567715e-08, "-11": 2.6660779877383036e-09, "-12": 2.2681033128009057e-10, "-13": 1.78396919587984e-11, "-14": 1.3043654850283666e-12, "-15": 8.864868619436499e-14, "-16": 5.13993580372584e-15, "-2": 0.060304070116628514, "-3": 0.018225239545015003, "-4": 0.0043342050816868455, "-5": 0.0008461150049623033, "-6": 0.0001397786737085061, "-7": 1.9989006994946873e-05, "-8": 2.5180254819677354e-06, "-9": 2.832963490886394e-07, "0": 0.24691102264869377, "1": 0.23012302263019085, "10": 5.472797019555656e-06, "11": 8.60070874709805e-07, "12": 1.2415286933688363e-07, "13": 1.6569668339727034e-08, "14": 2.055693199942844e-09, "15": 2.370630353736083e-10, "16": 2.3322858017073672e-11, "2": 0.16684576585337213, "3": 0.08556070339904454, "4": 0.034525747845888875, "5": 0.011436564157076305, "6": 0.003205823627866008, "7": 0.0007778976623927466, "8": 0.0001662738311552574, "9": 3.174221996423763e-05} |
| Raw goal margin distribution | {"-1": 0.13097093384904382, "-10": 2.7612511693760873e-08, "-11": 2.5573977372928204e-09, "-12": 2.1756461389278564e-10, "-13": 1.7112473100659436e-11, "-14": 1.2511942093802811e-12, "-15": 8.503500292569226e-14, "-16": 4.930410983749922e-15, "-2": 0.057845829407504726, "-3": 0.017482304189301186, "-4": 0.004157525143618189, "-5": 0.0008116238943991829, "-6": 0.00013408072288507023, "-7": 1.917417325926525e-05, "-8": 2.4153804576034965e-06, "-9": 2.717480304307284e-07, "0": 0.25684926778047584, "1": 0.22971111252970908, "10": 5.463000953327792e-06, "11": 8.585313856296858e-07, "12": 1.2393064115519557e-07, "13": 1.654000936135643e-08, "14": 2.052013599427997e-09, "15": 2.3663870295521226e-10, "16": 2.3281111125869422e-11, "2": 0.1665471192625525, "3": 0.08540755349891033, "4": 0.03446394827406915, "5": 0.011416093209679274, "6": 0.0032000853444140165, "7": 0.000776505259752548, "8": 0.00016597620830242045, "9": 3.168540278503694e-05} |
| Unadjusted home-win probability | 53.2% |
| Unadjusted draw probability | 25.7% |
| Unadjusted away-win probability | 21.1% |
| Raw p over 1 5 | 77.7% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 54.3% |
| P home draw | 78.0% |
| P draw away | 46.7% |
| P home away | 75.3% |
| Raw p home draw | 78.9% |
| Raw p draw away | 46.8% |
| Raw p home away | 74.3% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5304 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.98, "price": 1.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.37, "price": 2.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.82 |
| Reference draw odds | 3.85 |
| Reference away odds | 4.15 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.71 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:46Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:46Z |
| Home probability edge | -0.0% |
| Draw probability edge | +0.4% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -3.9% |
| Under 2.5 probability edge | +3.9% |
| Raw edge prob home | -0.0014 |
| Raw ev home | -0.0323 |
| Raw edge prob draw | 0.0142 |
| Raw ev draw | -0.0111 |
| Raw edge prob away | -0.0128 |
| Raw ev away | -0.1226 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.0638140783892726, 0.048999772062449196, 0.03037101992117638, 0.010275388316473042, 0.002607344237903545, 0.0005292836642702973, 8.953593251162032e-05, 1.2982533215952834e-05, 1.6471364454294794e-06, 1.857578554702183e-07, 1.8854165280707855e-08, 1.7397015325648537e-09, 1.4714774848080558e-10, 1.1488686807300801e-11, 8.329184378802521e-13, 5.636004590812054e-14, 3.575291668319087e-15], [0.08935861927101069, 0.11446541249102213, 0.05804182928863549, 0.019637217850669637, 0.004982876095233986, 0.0010115100568427052, 0.00017111145175650598, 2.481082224469422e-05, 3.147830156143293e-06, 3.5500044990941547e-07, 3.603205442038959e-08, 3.3247306026723527e-09, 2.8121296287369385e-10, 2.1955943532703172e-11, 1.5917842044249002e-12, 1.0770926270467128e-13, 6.8327131985766835e-15], [0.09447987187274477, 0.0958957625495642, 0.05070027742093534, 0.01876427016857596, 0.004761368640839363, 0.000966544656639378, 0.00016350490859308976, 2.3707888522919298e-05, 3.007897347976368e-06, 3.392193539187699e-07, 3.44302950150327e-08, 3.176933908901409e-09, 2.6871199629166273e-10, 2.0979919833174922e-11, 1.5210234509305524e-12, 1.0292118366348188e-13, 6.528973575455631e-15], [0.06018659244549992, 0.061088558477247853, 0.031002020759086476, 0.010927219384227277, 0.0030331386801091906, 0.0006157187576194358, 0.00010415766979008628, 1.5102656216492131e-05, 1.916123383871545e-06, 2.1609319106014226e-07, 2.1933159865407206e-08, 2.0238048868110004e-09, 1.711778295784129e-10, 1.3364856021812848e-11, 9.689388514889979e-13, 6.55639684133546e-14, 4.159157542070558e-15], [0.028755536801635614, 0.02918647193794922, 0.014811932569039092, 0.005011302197268968, 0.0013247426418365462, 0.00029417387951005116, 4.976373615990245e-05, 7.2156433682309475e-06, 9.154722711920616e-07, 1.0324352078479234e-07, 1.0479074492495724e-08, 9.669196001538201e-10, 8.178416783643975e-11, 6.385369125720216e-12, 4.629329501874743e-13, 3.132470256193175e-14, 1.9871337270524036e-15], [0.010990898313427222, 0.011155609697380118, 0.005661394736417845, 0.0019154124385848629, 0.00048602927997831854, 0.00010278585278202238, 1.9020620884343875e-05, 2.7579524275015757e-06, 3.49910443711901e-07, 3.946158426092462e-08, 4.005296196011141e-09, 3.695745649215585e-10, 3.125942243886215e-11, 2.440606247020111e-12, 1.7694154056466752e-13, 1.197288101180438e-14, 7.595192842295447e-16], [0.003500770610120846, 0.0035532337260237735, 0.0018032415313434316, 0.0006100884004236483, 0.00015480782102475239, 3.142555922556799e-05, 5.538251564281698e-06, 8.784503802126721e-07, 1.1145187250294897e-07, 1.2569123148076425e-08, 1.2757486065260804e-09, 1.1771519836053824e-10, 9.956608117248351e-12, 7.773707277418273e-13, 5.635860939242373e-14, 3.81354724330343e-15, 2.4191860503363195e-16], [0.0009557566515648328, 0.0009700797756910114, 0.0004923087742386942, 0.00016656219778059738, 4.22645814698375e-05, 8.579593067922948e-06, 1.4513613734249227e-06, 2.192393142431704e-07, 3.0427834421968044e-08, 3.4315367646144816e-09, 3.4829623308845633e-10, 3.2137805172980014e-11, 2.718285627619578e-12, 2.1223248436303528e-13, 1.5386645341464923e-14, 1.041148806867459e-15, 6.604697697979069e-17], [0.0002283174246188402, 0.000231739026558655, 0.0001176059525899224, 3.978947148717828e-05, 1.0096440739373577e-05, 2.049549527422717e-06, 3.467107348184257e-07, 5.027237115694804e-08, 6.644775265612292e-09, 8.197480345011224e-10, 8.320329114424723e-11, 7.677289923102457e-12, 6.493619195433973e-13, 5.069948942640397e-14, 3.675662871019469e-15, 2.4871646337983296e-16, 1.5777735538848844e-17], [4.848174717485138e-05, 4.9208302497801514e-05, 2.497287304830471e-05, 8.449040190790386e-06, 2.1439147192088098e-06, 4.352087545518192e-07, 7.362181058382002e-08, 1.0675016996098014e-08, 1.354374316427402e-09, 1.5912452287084577e-10, 1.766768757183188e-11, 1.6302234910947477e-12, 1.3788785705180623e-13, 1.0765712833212028e-14, 7.805035393608299e-16, 5.281335279571663e-17, 3.3503013914209025e-18], [9.265310484931875e-06, 9.40416192993724e-06, 4.772547112603921e-06, 1.6146897591171834e-06, 4.0972194040459623e-07, 8.317241996540061e-08, 1.406980922246491e-08, 2.040094523492718e-09, 2.5883346384485396e-10, 2.919026489952491e-11, 3.0865900412055887e-12, 3.115507935460189e-13, 2.6351645353853814e-14, 2.0574273371704416e-15, 1.4916144834230604e-16, 1.0093120399266209e-17, 6.402735961156931e-19], [1.6097150593150369e-06, 1.6338385101585121e-06, 8.291617394735924e-07, 2.8052923057459856e-07, 7.118332177574144e-08, 1.445001731520111e-08, 2.444427936216957e-09, 3.544372185080108e-10, 4.496860901567499e-11, 5.0713906534030055e-12, 5.147391335901112e-13, 4.9480652322296176e-14, 4.578221143566945e-15, 3.574485467568275e-16, 2.5914666330538772e-17, 1.7535351814276596e-18, 1.1123837149606357e-19], [2.563595353909627e-07, 2.6020138094895324e-07, 1.32050400513655e-07, 4.467644307452155e-08, 1.1336492873328492e-08, 2.301276678676667e-09, 3.892939973438037e-10, 5.644686004282197e-11, 7.1615977298129544e-12, 8.076580660465964e-13, 8.197617607606793e-14, 7.564062212781633e-15, 6.665224170168276e-16, 5.692643728620369e-17, 4.1271104360144724e-18, 2.7926399880596747e-19, 1.7715568397870785e-20], [3.768667638348854e-08, 3.825145502547869e-08, 1.9412348765879386e-08, 6.567755123861862e-09, 1.6665451417256556e-09, 3.3830405147946863e-10, 5.722898847338048e-11, 8.29809019607427e-12, 1.0528058401283154e-12, 1.1873148434753056e-13, 1.2051081362053197e-14, 1.1119709837316426e-15, 9.405293009707572e-17, 7.650148968476147e-18, 6.067146094791946e-19, 4.105379553176722e-20, 2.604314647949111e-21], [5.144480407364797e-09, 5.221576424764978e-09, 2.649913907790304e-09, 8.965419824041665e-10, 2.2749442647462772e-10, 4.6180738966166015e-11, 7.81213516784413e-12, 1.1327441559944311e-12, 1.4371495544436752e-13, 1.62076323406121e-14, 1.6450522546425438e-15, 1.5179138858400076e-16, 1.2838846578459355e-17, 1.0024039703614328e-18, 7.571042025807327e-20, 5.604114425268582e-21, 3.5550616203601536e-22], [6.554385383565376e-10, 6.65261046551057e-10, 3.376153782228948e-10, 1.1422497900487987e-10, 2.8984193264557127e-11, 5.883711016738702e-12, 9.953142106489852e-13, 1.4431859296694428e-13, 1.8310171849732483e-14, 2.064952339276672e-15, 2.0958980498000334e-16, 1.9339159252346986e-17, 1.6357482523448394e-18, 1.2771244929534797e-19, 9.25902634035979e-21, 6.527020473386183e-22, 4.529367803365519e-23], [7.828773089284131e-11, 7.946096351989039e-11, 4.032588920064557e-11, 1.3643406504592949e-11, 3.461967201579822e-12, 7.027697606623205e-13, 1.188835970379301e-13, 1.723788655662429e-14, 2.1870270398927584e-15, 2.466446868522356e-16, 2.503409441150681e-17, 2.3099326735315722e-18, 1.9537914158832727e-19, 1.5254394236826332e-20, 1.1059285044199087e-21, 7.483347521857391e-23, 4.945575608715506e-24]] |
| Legacy trial inputs | {"lambda_home": 1.9110925296310335, "lambda_away": 1.0149861621184932, "rho": -0.0948277249952374, "max_goals": 16, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.5531 |
| Legacy p draw | 0.2413 |
| Legacy p away | 0.2056 |
| Legacy p over 1 5 | 0.7978 |
| Legacy p under 3 5 | 0.6659 |
| Legacy p btts yes | 0.5548 |
| Legacy p over 2 5 | 0.5585 |
| Legacy goal margin distribution | {"-1": 0.12915311441611077, "-10": 2.2461447883443488e-08, "-11": 2.0428954383450577e-09, "-12": 1.706922665665797e-10, "-13": 1.3187551352931252e-11, "-14": 9.47156674160379e-13, "-15": 6.319275910669722e-14, "-16": 3.575291668319087e-15, "-2": 0.05543796182716172, "-3": 0.016336545217185073, "-4": 0.0037984181019579755, "-5": 0.0007261264972355491, "-6": 0.00011758160411697819, "-7": 1.6492514857912337e-05, "-8": 2.038675277430358e-06, "-9": 2.251445878193482e-07, "0": 0.24134028047799097, "1": 0.22178666263396576, "10": 1.1038000647748993e-05, "11": 1.890255017975299e-06, "12": 2.9737859127043814e-07, "13": 4.325951159298101e-08, "14": 5.8500673431165e-09, "15": 7.34899501876428e-10, "16": 7.828773089284131e-11, "2": 0.17245952042144902, "3": 0.09568893735898146, "4": 0.04189149630916213, "5": 0.015078459874260063, "6": 0.004597329948288183, "7": 0.0012141567839096534, "8": 0.0002825904862153858, "9": 5.8761461025769524e-05} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.5731 |
| Legacy raw p draw | 0.2400 |
| Legacy raw p away | 0.1869 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.9111 |
| Legacy lambda away | 1.0150 |
| Legacy model home team | Buyuksehyr |
| Legacy model away team | Samsunspor |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,539.1035 |
| Elo away rating | 1,443.8010 |
| Elo rating diff | 155.3026 |
| Elo home expectancy | 0.7097 |

</details>


---

## 2026-11-01 — Kasimpasa SK vs Besiktas JK

The model's most likely 1X2 outcome is **Besiktas JK win** at **55.9%**. Expected goals are 1.23 for Kasimpasa SK and 1.55 for Besiktas JK (2.79 combined). The most likely exact score is 1-2 at 11.8%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 54.3%; Under 3.5 goals: 68.9%; Double Chance 1X: 44.1%; Double Chance X2: 79.4%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 84.3%; BTTS Yes (both teams score): 55.9%; BTTS No (at least one team does not score): 44.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Kasimpasa SK win | 20.6% | 4.86 |
| Draw | 23.5% | 4.25 |
| Besiktas JK win | 55.9% | 1.79 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Kasimpasa SK expected goals | 1.23 |
| Besiktas JK expected goals | 1.55 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 78.3% |
| Under 1.5 | 21.7% |
| Over 2.5 | 54.3% |
| Under 2.5 | 45.7% |
| Over 3.5 | 31.1% |
| Under 3.5 | 68.9% |
| Over 4.5 | 15.7% |
| Under 4.5 | 84.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.76% |
| 2 | 1-1 | 11.16% |
| 3 | 0-1 | 10.83% |
| 4 | 0-2 | 9.53% |
| 5 | 0-0 | 6.30% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Kasimpasa SK win | 20.6% | 16.9% | 5.37 | +10.5% |
| Draw | 23.5% | 21.9% | 4.20 | -1.3% |
| Besiktas JK win | 55.9% | 61.2% | 1.59 | -11.1% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T16:00:00+00:00 |
| Fixture id | bf609ced8c6472e7d11428e42a2e468e |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Kasimpasa |
| Matched away-team name | Besiktas |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2413 |
| Dc lambda away | 1.5812 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.2162 |
| Shot lambda away | 1.4845 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 55.9% |
| P btts no | 44.1% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.88 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.61 |
| Fair Over 2.5 odds | 1.84 |
| Fair Under 2.5 odds | 2.19 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.37 |
| Fair Under 4.5 odds | 1.19 |
| Goal margin distribution | {"-1": 0.2700589171188791, "-10": 2.104500648133385e-06, "-11": 2.9276458101596395e-07, "-12": 3.741374530366368e-08, "-13": 4.419720533824696e-09, "-14": 4.823794238826447e-10, "-15": 4.4264696872393666e-11, "-2": 0.1727839085414863, "-3": 0.07798225858566919, "-4": 0.027756061142877562, "-5": 0.008120054975325055, "-6": 0.002011860152645315, "-7": 0.00043172194491216423, "-8": 8.163707899920283e-05, "-9": 1.3791029019382858e-05, "0": 0.235072913891863, "1": 0.11632617231242488, "10": 1.1646678956966836e-07, "11": 1.2878848739611061e-08, "12": 1.3082633097352723e-09, "13": 1.2284691462344733e-10, "14": 1.0657704797984045e-11, "15": 7.7738807573003e-13, "2": 0.05999465918158953, "3": 0.021523384988909895, "4": 0.006089449988525084, "5": 0.0014160698300811126, "6": 0.0002788874410849296, "7": 4.7570833553678006e-05, "8": 7.150387227679246e-06, "9": 9.601614045797692e-07} |
| Raw goal margin distribution | {"-1": 0.21043078667009504, "-10": 1.6398337505718847e-06, "-11": 2.2812311383597458e-07, "-12": 2.9152912040519116e-08, "-13": 3.4438606164791082e-09, "-14": 3.758716161792536e-10, "-15": 3.4491195787735517e-11, "-2": 0.13463378356921124, "-3": 0.06076402955163141, "-4": 0.021627613127797273, "-5": 0.006327173249790907, "-6": 0.001567647975145404, "-7": 0.00033639914378616627, "-8": 6.361187750630293e-05, "-9": 1.0746014671536911e-05, "0": 0.27259178398892897, "1": 0.16494145989602668, "10": 1.6514084422403516e-07, "11": 1.8261205287373304e-08, "12": 1.855015564825691e-09, "13": 1.7418736505223844e-10, "14": 1.5111796026427095e-11, "15": 1.1022757954443448e-12, "2": 0.08506775796592575, "3": 0.030518484975507392, "4": 0.008634366205857606, "5": 0.0020078768212280413, "6": 0.00039544068858098324, "7": 6.745174004127753e-05, "8": 1.0138692649387086e-05, "9": 1.3614341524266846e-06} |
| Unadjusted home-win probability | 29.2% |
| Unadjusted draw probability | 27.3% |
| Unadjusted away-win probability | 43.6% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 57.0% |
| P home draw | 44.1% |
| P draw away | 79.4% |
| P home away | 76.5% |
| Raw p home draw | 56.4% |
| Raw p draw away | 70.8% |
| Raw p home away | 72.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5430 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.53, "price": 2.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.0, "market_key": "spreads", "opposite_price": 1.83, "price": 2.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.0, "market_key": "spreads", "opposite_price": 2.04, "price": 1.83, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.65, "price": 1.53, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.37 |
| Reference draw odds | 4.20 |
| Reference away odds | 1.59 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.72 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:46Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:46Z |
| Home probability edge | +3.7% |
| Draw probability edge | +1.6% |
| Away probability edge | -5.3% |
| Over 2.5 probability edge | -2.3% |
| Under 2.5 probability edge | +2.3% |
| Raw edge prob home | 0.1228 |
| Raw ev home | 0.5661 |
| Raw edge prob draw | 0.0536 |
| Raw ev draw | 0.1449 |
| Raw edge prob away | -0.1764 |
| Raw ev away | -0.3071 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.06667998401444274, 0.10305302888584186, 0.0904212673578789, 0.04679182801291651, 0.018160621108012833, 0.00563873091579599, 0.0014589848988665536, 0.0003235738629197498, 6.27919721721446e-05, 1.0831342552933939e-05, 1.6815236039988116e-06, 2.3731815306003662e-07, 3.070226321418792e-08, 3.666466449177243e-09, 4.065747058614511e-10, 4.2079422832627326e-11], [0.051660859126076965, 0.1169072183817178, 0.10997171205543865, 0.05690892847605815, 0.022087221884800147, 0.006857909767795173, 0.0017744394861924624, 0.0003935354228208136, 7.636854564067886e-05, 1.3173242525905385e-05, 2.0450944229910493e-06, 2.8862992475600126e-07, 3.734055657810637e-08, 4.459211913210512e-09, 4.944823025434424e-10, 5.117763006896761e-11], [0.03683860307126985, 0.05719049166800104, 0.050404187970464344, 0.03460674948838403, 0.013431406549557592, 0.004170346757589633, 0.0010790500616576159, 0.00023931186471196254, 4.644028974980722e-05, 8.010748335132103e-06, 1.2436373741655933e-06, 1.755180385285991e-07, 2.2707074651721953e-08, 2.7116804643583558e-09, 3.0069842516468227e-10, 3.112150361346301e-11], [0.014934555287175966, 0.023185313462188675, 0.017997146550508263, 0.010574386653056949, 0.0054451598859715025, 0.0016906795867753972, 0.0004374523315197142, 9.701823566717513e-05, 1.8827127442350643e-05, 3.24759773521345e-06, 5.041768572424364e-07, 7.115589712320998e-08, 9.205562467721546e-09, 1.0993289223743325e-09, 1.219046565555313e-10, 1.2616814362806089e-11], [0.00454090796808057, 0.007049582168228495, 0.005472100414271533, 0.0028317406837551, 0.001247861187626961, 0.000514057516908579, 0.00013300903439414802, 2.949876115618168e-05, 5.724459240674482e-06, 9.874443630480375e-07, 1.5329687857126108e-07, 2.1635219396198313e-08, 2.7989860532529213e-09, 3.342551128681771e-10, 3.7065571465289466e-11, 3.836190082007663e-12], [0.0011045441810930128, 0.00171476167713331, 0.0013310502466525752, 0.0006888011641266869, 0.00026733422248453073, 9.424478795720907e-05, 3.2353519605674134e-05, 7.175367836905464e-06, 1.3924347704549066e-06, 2.401889518626012e-07, 3.728839615245078e-08, 5.262616168114669e-09, 6.808338287877315e-10, 8.130522409050121e-11, 9.015941650580989e-12, 9.331264721578057e-13], [0.00022389388799228275, 0.00034758651165372816, 0.0002698072380782715, 0.00013962173114463023, 5.4189320345905854e-05, 1.6825360439110385e-05, 4.942946548800998e-06, 1.4544651361883877e-06, 2.8225003568828536e-07, 4.86869056085141e-08, 7.558451834228303e-09, 1.0667455544641729e-09, 1.3800673220071124e-10, 1.6480773741157575e-11, 1.8275540848557065e-12, 1.8914708656850061e-13], [3.890044723945683e-05, 6.039142416517756e-05, 4.6877663002793256e-05, 2.425857996650862e-05, 9.41512435181167e-06, 2.9233225253072463e-06, 7.563906635430627e-07, 1.904675114060735e-07, 4.903953707751685e-08, 8.459107213063802e-09, 1.3132433378418462e-09, 1.8534172384727632e-10, 2.3977981948523134e-11, 2.86345230382271e-12, 3.1752841443190123e-13, 3.2863363656486e-14], [5.913913987891824e-06, 9.181120358865541e-06, 7.126665286015078e-06, 3.687956452202756e-06, 1.4313520679896801e-06, 4.4442363007071623e-07, 1.1499171970703947e-07, 2.5502878733219262e-08, 5.619167871992479e-09, 1.2860117562266146e-09, 1.996482996033823e-10, 2.8176925742093243e-11, 3.645298008372426e-12, 4.3532174653410617e-13, 4.827285712430676e-14, 4.996114950065085e-15], [7.991768421556968e-07, 1.2406908167538525e-06, 9.630620042900655e-07, 4.983720421895722e-07, 1.9342577995741094e-07, 6.005719291597232e-08, 1.55394075087461e-08, 3.446331842773269e-09, 6.687869385206344e-10, 1.3098394341910636e-10, 2.6979475512403077e-11, 3.807689219411342e-12, 4.926073928386688e-13, 5.882720976820423e-14, 6.5233531629683e-15, 6.751500574771154e-16], [9.71970954787363e-08, 1.5089469240666724e-07, 1.17129056605832e-07, 6.061276104794268e-08, 2.352473571663728e-08, 7.304246577381931e-09, 1.8899262286385557e-09, 4.1914808776226103e-10, 8.133887831756973e-11, 1.403060333116654e-11, 2.473142464829801e-12, 4.630969180915986e-13, 5.991165568076283e-14, 7.154654167861686e-15, 7.933800715649611e-16, 8.211277046275172e-17], [1.0746597875542595e-08, 1.668367324003936e-08, 1.2950375365485231e-08, 6.7016505575631486e-09, 2.6010126499142387e-09, 8.07594099024331e-10, 2.0895971318466596e-10, 4.634311269588383e-11, 8.993233929689206e-12, 1.5512938036742199e-12, 2.40832300785161e-13, 3.8591782413453774e-14, 6.624132835327151e-15, 7.910544127052142e-16, 8.772007588892505e-17, 9.078799322794304e-18], [1.0891812306972935e-09, 1.6909112970061783e-09, 1.3125368550983338e-09, 6.792207251563595e-10, 2.636159082066502e-10, 8.185067915131057e-11, 2.117833012907228e-11, 4.6969328437719705e-12, 9.11475586313681e-13, 1.572255809537921e-13, 2.4408657027896696e-14, 3.4448623800230755e-15, 5.060150323094586e-16, 8.017436111010038e-17, 8.890540180255456e-18, 9.20147746679838e-19], [1.018983596519446e-10, 1.5819322131686445e-10, 1.2279439706431466e-10, 6.354450093739512e-11, 2.4662588619176073e-11, 7.65754101048603e-12, 1.9813388621636896e-12, 4.394215936582947e-13, 8.527310652305143e-14, 1.4709240613941525e-14, 2.2835521236968773e-15, 3.222841303704055e-16, 4.1694459832934277e-17, 5.653374913454933e-18, 8.3175456503942685e-19, 8.608443056265527e-20], [8.85216608406097e-12, 1.3742641915460645e-11, 1.0667457265438894e-11, 5.520270178518568e-12, 2.1425009319632572e-12, 6.652297941975436e-13, 1.7212387654311613e-13, 3.817365599674541e-14, 7.407888645354346e-15, 1.2778286257971222e-15, 1.9837790058271192e-16, 2.7997630757165405e-17, 3.62210230358011e-18, 4.3255171382372455e-19, 5.446064610351067e-20, 7.478370399634749e-21], [7.177425459803973e-13, 1.1142672542780223e-12, 8.649281841445921e-13, 4.475890685742686e-13, 1.7371613445454319e-13, 5.393750203230735e-14, 1.3955977350731875e-14, 3.095158493898769e-15, 6.006390759239719e-16, 1.0360763258358473e-16, 1.608468007472838e-17, 2.2700761136022733e-18, 2.9368370458548946e-19, 3.507172881754147e-20, 3.889106316858372e-21, 4.57015936541843e-22]] |
| Legacy trial inputs | {"lambda_home": 1.216215114749287, "lambda_away": 1.5524609214241212, "rho": -0.0948277249952374, "max_goals": 15, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.2281 |
| Legacy p draw | 0.2459 |
| Legacy p away | 0.5260 |
| Legacy p over 1 5 | 0.7786 |
| Legacy p under 3 5 | 0.6944 |
| Legacy p btts yes | 0.5580 |
| Legacy p over 2 5 | 0.5344 |
| Legacy goal margin distribution | {"-1": 0.2536245661702845, "-10": 1.9939979310268464e-06, "-11": 2.774961309491389e-07, "-12": 3.5474790366925915e-08, "-13": 4.192070255334148e-09, "-14": 4.577523359304187e-10, "-15": 4.2079422832627326e-11, "-2": 0.1625927572851607, "-3": 0.07351779021157834, "-4": 0.026200571568823827, "-5": 0.00767233521806743, "-6": 0.0019023669095862598, "-7": 0.0004084796666093264, "-8": 7.728289012103359e-05, "-9": 1.3061504037122914e-05, "0": 0.24591302216199026, "1": 0.12996518018786918, "10": 1.1525904651324538e-07, "11": 1.256599755592606e-08, "12": 1.258489498348171e-09, "13": 1.1650592975154982e-10, "14": 9.966433338338992e-12, "15": 7.177425459803973e-13, "2": 0.0662420492756944, "3": 0.023464684948891913, "4": 0.006551228809715293, "5": 0.0015028972559714847, "6": 0.0002919347034407438, "7": 4.91079272471026e-05, "8": 7.278706960477324e-06, "9": 9.637264724273966e-07} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.2873 |
| Legacy raw p draw | 0.2728 |
| Legacy raw p away | 0.4399 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 1.2162 |
| Legacy lambda away | 1.5525 |
| Legacy model home team | Kasimpasa |
| Legacy model away team | Besiktas |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,457.3688 |
| Elo away rating | 1,573.4966 |
| Elo rating diff | -56.1278 |
| Elo home expectancy | 0.4199 |

</details>


---

## 2026-11-01 — Trabzonspor vs Gazişehir Gaziantep

The model's most likely 1X2 outcome is **Trabzonspor win** at **70.9%**. Expected goals are 2.27 for Trabzonspor and 0.97 for Gazişehir Gaziantep (3.25 combined). The most likely exact score is 2-0 at 10.8%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 64.5%; Under 3.5 goals: 58.4%; Double Chance 1X: 88.0%; Double Chance X2: 29.1%; Double Chance 12 (either team wins): 82.9%; Under 4.5 goals: 76.4%; BTTS Yes (both teams score): 55.6%; BTTS No (at least one team does not score): 44.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Trabzonspor win | 70.9% | 1.41 |
| Draw | 17.1% | 5.86 |
| Gazişehir Gaziantep win | 12.0% | 8.33 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Trabzonspor expected goals | 2.27 |
| Gazişehir Gaziantep expected goals | 0.97 |
| Expected total goals | 3.25 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 84.8% |
| Under 1.5 | 15.2% |
| Over 2.5 | 64.5% |
| Under 2.5 | 35.5% |
| Over 3.5 | 41.6% |
| Under 3.5 | 58.4% |
| Over 4.5 | 23.6% |
| Under 4.5 | 76.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 10.83% |
| 2 | 2-1 | 10.55% |
| 3 | 1-0 | 8.64% |
| 4 | 3-0 | 8.21% |
| 5 | 3-1 | 7.99% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Trabzonspor win | 70.9% | 73.1% | 1.34 | -5.0% |
| Draw | 17.1% | 15.7% | 5.64 | -3.7% |
| Gazişehir Gaziantep win | 12.0% | 11.2% | 7.75 | -6.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-01T13:00:00+00:00 |
| Fixture id | cd2960ff2b4d605144a83562b0085400 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-30T07:28:45Z |
| Market best draw last update utc | 2026-10-30T07:28:45Z |
| Market best away last update utc | 2026-10-30T07:28:45Z |
| Odds bookmakers 1x2 | 1.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Trabzonspor |
| Matched away-team name | Gaziantep |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.3916 |
| Dc lambda away | 0.8904 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 1 |
| Shot features status | APPLIED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0.3000 |
| Shot lambda home | 1.9971 |
| Shot lambda away | 1.1671 |
| Goal rate features used | shot_features |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 55.6% |
| P btts no | 44.4% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 25.16 |
| Fair Over 1.5 odds | 1.18 |
| Fair Under 1.5 odds | 6.59 |
| Fair Over 2.5 odds | 1.55 |
| Fair Under 2.5 odds | 2.81 |
| Fair Over 3.5 odds | 2.40 |
| Fair Under 3.5 odds | 1.71 |
| Fair Over 4.5 odds | 4.23 |
| Fair Under 4.5 odds | 1.31 |
| Goal margin distribution | {"-1": 0.07765728220794671, "-10": 8.61363207822596e-09, "-11": 7.498570774431355e-10, "-12": 5.998717007221956e-11, "-13": 4.438398722363878e-12, "-14": 3.0541331073049447e-13, "-15": 1.9634059362368737e-14, "-16": 1.1766853128112909e-15, "-17": 5.961752942255693e-17, "-2": 0.031356407516226904, "-3": 0.008717514688015437, "-4": 0.0019226988146576489, "-5": 0.00034976969796892446, "-6": 5.400592305056746e-05, "-7": 7.232687641953849e-06, "-8": 8.544252002477284e-07, "-9": 9.023829753153825e-08, "0": 0.17074360514710465, "1": 0.2387846887913249, "10": 5.1989558120848216e-05, "11": 1.0569492563093362e-05, "12": 1.9746032651985445e-06, "13": 3.411879030655935e-07, "14": 5.4827835996585174e-08, "15": 8.23131226959624e-09, "16": 1.1520335966402195e-09, "17": 1.3630902784223784e-10, "2": 0.213938742161478, "3": 0.1388998125620579, "4": 0.07154282157895275, "5": 0.030393647450326997, "6": 0.010959427467317576, "7": 0.0034276148592522373, "8": 0.0009456102910600482, "9": 0.0002332248745349881} |
| Raw goal margin distribution | {"-1": 0.09013981440115876, "-10": 9.99817627884617e-09, "-11": 8.703881447605288e-10, "-12": 6.962943104654895e-11, "-13": 5.151821254842731e-12, "-14": 3.545050555744668e-13, "-15": 2.2790012945935232e-14, "-16": 1.36582420462978e-15, "-17": 6.920037483175001e-17, "-2": 0.03639659634535291, "-3": 0.010118756846433596, "-4": 0.002231750962369288, "-5": 0.0004059912317513723, "-6": 6.268676603059462e-05, "-7": 8.395260600564254e-06, "-8": 9.917644138481309e-07, "-9": 1.0474308603265847e-07, "0": 0.20263484705429183, "1": 0.22154883852495666, "10": 4.8236870945965396e-05, "11": 9.80657014905126e-06, "12": 1.832073330022565e-06, "13": 3.16560429504783e-07, "14": 5.087027750969249e-08, "15": 7.637163346176512e-09, "16": 1.0688780196473034e-09, "17": 1.2647003018399106e-10, "2": 0.19849631097070408, "3": 0.1288738080327708, "4": 0.06637874943257681, "5": 0.02819978670006581, "6": 0.010168358945345108, "7": 0.00318020428705898, "8": 0.0008773546693552113, "9": 0.00021639034030992928} |
| Unadjusted home-win probability | 65.8% |
| Unadjusted draw probability | 20.3% |
| Unadjusted away-win probability | 13.9% |
| Raw p over 1 5 | 84.3% |
| Raw p under 3 5 | 59.2% |
| Raw p btts yes | 56.6% |
| P home draw | 88.0% |
| P draw away | 29.1% |
| P home away | 82.9% |
| Raw p home draw | 86.1% |
| Raw p draw away | 34.2% |
| Raw p home away | 79.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.6446 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.92, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-30T07:28:46Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-30T07:28:45Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.34 |
| Reference draw odds | 5.64 |
| Reference away odds | 7.75 |
| Market reference 1x2 last update utc | 2026-10-30T07:28:45Z |
| Market reference home last update utc | 2026-10-30T07:28:45Z |
| Market reference draw last update utc | 2026-10-30T07:28:45Z |
| Market reference away last update utc | 2026-10-30T07:28:45Z |
| O/U 2.5 market source | The Odds API / Betsson |
| Reference Over 2.5 odds | 1.38 |
| Reference Under 2.5 odds | 2.83 |
| Market reference over 2 5 last update utc | 2026-10-30T07:28:25Z |
| Market reference under 2 5 last update utc | 2026-10-30T07:28:25Z |
| Home probability edge | -2.2% |
| Draw probability edge | +1.4% |
| Away probability edge | +0.8% |
| Over 2.5 probability edge | -4.9% |
| Under 2.5 probability edge | +4.9% |
| Raw edge prob home | -0.0731 |
| Raw ev home | -0.1183 |
| Raw edge prob draw | 0.0456 |
| Raw ev draw | 0.1429 |
| Raw edge prob away | 0.0276 |
| Raw ev away | 0.0801 |
| Legacy model version | dc-blend50-tuned-half-life-v1 |
| Legacy status | AVAILABLE |
| Legacy half life days | 365 |
| Legacy trial matrix | [[0.04040544519048617, 0.024603974836923465, 0.014019915342987096, 0.004086539202768554, 0.0008933614565717209, 0.0001562387443237552, 2.2770314158484892e-05, 2.8444775834404048e-06, 3.1091670861818117e-07, 3.020877296047106e-08, 2.641585172600572e-09, 2.0999234630025618e-10, 1.530219574162051e-11, 1.0292999075311802e-12, 6.429029685826094e-14, 3.747880240950652e-15, 2.0483174056202065e-16, 1.053609959119019e-17, 5.1184550655661325e-19], [0.08169349332816664, 0.07887669316249779, 0.034404789085077284, 0.010028342962104957, 0.0021923037149765606, 0.0003834089517569678, 5.587821587064648e-05, 6.98033111622531e-06, 7.629877585805619e-07, 7.413214964553079e-08, 6.482434343589015e-09, 5.153199721391124e-10, 3.7551497576792886e-11, 2.525895867239574e-12, 1.5776800711795215e-13, 9.197275878740269e-15, 5.026558762703704e-16, 2.5855525896280807e-17, 1.2560658368050339e-18], [0.10930107734602705, 0.0955775680277847, 0.03864986295910592, 0.012304747070267593, 0.0026899501558662656, 0.0004704416466083505, 6.856240513754794e-05, 8.56484557582806e-06, 9.361837167437262e-07, 9.095992773785402e-08, 7.953927712573593e-09, 6.322960773669197e-10, 4.607557614834662e-11, 3.099266737253005e-12, 1.9358087679114427e-13, 1.1285030223938175e-14, 6.167572692978964e-16, 3.172465358680853e-17, 1.5411890562472167e-18], [0.08940806514315154, 0.0781822616569368, 0.03418296787883196, 0.009215321484000009, 0.0022003739085401037, 0.00038482033670036596, 5.608391183101044e-05, 7.006026745375927e-06, 7.657964291385209e-07, 7.440504103043973e-08, 6.506297141228932e-09, 5.172169410188857e-10, 3.768973018205437e-11, 2.535194062754512e-12, 1.583487744390484e-13, 9.231132408787493e-15, 5.045062267440034e-16, 2.5950703903435903e-17, 1.2606896005483156e-18], [0.054851715372405185, 0.04796470158157414, 0.02097120010003236, 0.006112706763293964, 0.0012359347678831466, 0.0002360867058738541, 3.440739673540838e-05, 4.298187018291096e-06, 4.698149735938886e-07, 4.5647382328868384e-08, 3.991603647250153e-09, 3.173118262779798e-10, 2.312259357250109e-11, 1.5553377977856135e-12, 9.714673828578179e-14, 5.663286042943535e-15, 3.0951382192043644e-16, 1.592071835964412e-17, 7.734312003230305e-19], [0.026921156828329493, 0.023541018630589463, 0.010292640128721914, 0.003000109227267934, 0.0006558561697708832, 0.00010608661260416165, 1.688710949656969e-05, 2.109545089179053e-06, 2.3058463164821082e-07, 2.240368109064475e-08, 1.9590743344047475e-09, 1.5573626787633064e-10, 1.1348541492581766e-11, 7.633579458898717e-13, 4.7679503895112814e-14, 2.7795340709157323e-15, 1.519090165892536e-16, 7.813869682465142e-18, 3.7959911551452393e-19], [0.011010726526584289, 0.009628253345557678, 0.004209679636598907, 0.0012270417078276469, 0.0002682445250094528, 4.6912912406171626e-05, 6.3235815436803965e-06, 8.628018558254032e-07, 9.430888637147638e-08, 9.16308341617443e-09, 8.012594658889819e-10, 6.369597958928256e-11, 4.641542250477141e-12, 3.1221264515808915e-13, 1.9500869953695594e-14, 1.136826686956147e-15, 6.213063759676543e-17, 3.195864974771606e-18, 1.5525566294630356e-19], [0.0038600367971764068, 0.003375382370696188, 0.001475789836607345, 0.00043016472459372, 9.403863901965454e-05, 1.6446286965108365e-05, 2.396890237162345e-06, 2.7693132576109105e-07, 3.306192110172746e-08, 3.212307478224374e-09, 2.8089799659903566e-10, 2.23299365807699e-11, 1.6271881641264192e-12, 1.0945256845170806e-13, 6.836431312363912e-15, 3.985379922994202e-16, 2.1781173728773436e-17, 1.1203762414443084e-18, 5.442806798405335e-20], [0.0011840634253002225, 0.001035396039350726, 0.0004526974380748862, 0.0001319527103001577, 2.8846282789229755e-05, 5.044886331555522e-06, 7.352443029452825e-07, 9.184703924257499e-08, 9.285325922116956e-09, 9.853729370057207e-10, 8.616525216969951e-11, 6.84969148840858e-12, 4.99138762778861e-13, 3.357449421301818e-14, 2.0970702358248455e-15, 1.2225123362023723e-16, 6.681358890468645e-18, 3.4367458129931144e-19, 1.6695769495465342e-20], [0.00032285384686470776, 0.00028231730428469767, 0.00012343520306880252, 3.597901870318184e-05, 7.865400760849165e-06, 1.3755690145778358e-06, 2.0047612865928835e-07, 2.504356549572542e-08, 2.7373964911254623e-09, 2.459898428979119e-10, 2.34943352988051e-11, 1.8676780311058394e-12, 1.3609817366125157e-13, 9.154623292634317e-15, 5.717997687580496e-16, 3.333375578951114e-17, 1.821779453684737e-18, 9.370837597991603e-20, 4.552368811333484e-21], [7.922814250260289e-05, 6.928049899988288e-05, 3.0290925610903248e-05, 8.829229846884967e-06, 1.930164680929991e-06, 3.375638201851985e-07, 4.919672304987025e-08, 6.145676116723072e-09, 6.717554750893105e-10, 6.526799000965528e-11, 5.278642094672568e-12, 4.583270809204338e-13, 3.339841108257317e-14, 2.246539125458891e-15, 1.403193240596642e-16, 8.180083897049104e-18, 4.470635972484869e-19, 2.29959798773451e-20, 1.117148605820626e-21], [1.767503561066915e-05, 1.545581214285856e-05, 6.757613796578099e-06, 1.9697161517240884e-06, 4.306011524727168e-07, 7.530723748131395e-08, 1.0975315138886626e-08, 1.3710411576435798e-09, 1.4986217736299267e-10, 1.4560660028342267e-11, 1.2732468043133315e-12, 9.361423399630562e-14, 7.450863879647993e-15, 5.01181244302716e-16, 3.1303889896675394e-17, 1.8248979417112314e-18, 9.973558324103401e-20, 5.130181655097523e-21, 2.492250956109472e-22], [3.614536044972652e-06, 3.160705942847789e-06, 1.381928680867383e-06, 4.0280597932566216e-07, 8.805772281895145e-08, 1.540029283783829e-08, 2.2444465204072014e-09, 2.8037723898289435e-10, 3.0646741188439076e-11, 2.977647777935264e-12, 2.6037834207014345e-13, 2.069873027158598e-14, 1.3950328599275052e-15, 1.0249131670789489e-16, 6.4016300092254686e-18, 3.731907269669104e-19, 2.0395877469886466e-20, 1.0491196124331568e-21, 5.096640885146257e-23], [6.823115394471197e-07, 5.966425872564376e-07, 2.6086498347698325e-07, 7.603719106203481e-08, 1.6622548418177722e-08, 2.9070944053073892e-09, 4.2368141899587976e-10, 5.2926467788979817e-11, 5.785147775301692e-12, 5.620869218111994e-13, 4.915130052822933e-14, 3.9072739462232655e-15, 2.847240473029061e-16, 1.771343444909948e-17, 1.2084278513810081e-18, 7.044675616898127e-20, 3.8501047940049936e-21, 1.9804102349983584e-22, 9.620866537463412e-24], [1.1959917645057445e-07, 1.0458266927308845e-07, 4.5725794428042074e-08, 1.3328201129359833e-08, 2.9136882294776597e-09, 5.095708875458386e-10, 7.426512063738177e-11, 9.277231285182488e-12, 1.0140513087783984e-12, 9.852556941471448e-14, 8.615499994935238e-15, 6.848876489964534e-16, 4.9907937363473435e-17, 3.3570499411122423e-18, 1.9393301295662009e-19, 1.2348280124723827e-20, 6.7486673753829e-22, 3.471367834875216e-23, 1.686396386544905e-24], [1.9566377969556103e-08, 1.7109683333881353e-08, 7.480721885296863e-09, 2.18048843387388e-09, 4.766782420693899e-10, 8.336559568304751e-11, 1.2149744366728142e-11, 1.5177513693991607e-12, 1.658983930903638e-13, 1.6118744192446152e-14, 1.4094923920088733e-15, 1.1204734852403669e-16, 8.164918815625856e-18, 5.492120427570275e-19, 3.430390405034755e-20, 1.849584887425781e-21, 1.1040793137244022e-22, 5.6791440496747525e-24, 2.758937819213784e-25], [3.000985966804582e-09, 2.624191337882709e-09, 1.147352945663919e-09, 3.3443160512470003e-10, 7.311034864792455e-11, 1.2786167329916193e-11, 1.863462537703465e-12, 2.327845535720606e-13, 2.544460453305384e-14, 2.472206414457871e-15, 2.161803730520705e-16, 1.718522053808228e-17, 1.2522913961856672e-18, 8.42351934363307e-20, 5.261348565476954e-21, 3.067166476580263e-22, 1.5503842381474085e-23, 8.710366130641773e-25, 4.2315106513987257e-26], [4.332001035639969e-10, 3.7880882213954026e-10, 1.6562337191309912e-10, 4.827606912449377e-11, 1.0553668346408238e-11, 1.8457163988021325e-12, 2.689956478471385e-13, 3.3603053739998415e-14, 3.6729946226974946e-15, 3.5686940446278526e-16, 3.120619724002818e-17, 2.4807311327731213e-18, 1.8077150927085933e-19, 1.2159568529807782e-20, 7.594893040695518e-22, 4.4275343170543764e-23, 2.4197666474270527e-24, 1.1511887673559945e-25, 6.108295315922253e-27], [5.905947135490851e-11, 5.164414457909229e-11, 2.2579931788405006e-11, 6.581621514234978e-12, 1.438813306520418e-12, 2.5163206076712254e-13, 3.6672984673643254e-14, 4.581205252416807e-15, 5.007503897650596e-16, 4.865307786612631e-17, 4.2544346061560864e-18, 3.3820552689133825e-19, 2.4645122855998307e-20, 1.6577505022875388e-21, 1.035434581594661e-22, 6.036190527648791e-24, 3.2989405548045718e-25, 1.696903328335136e-26, 7.624415836422793e-28]] |
| Legacy trial inputs | {"lambda_home": 2.453994067966103, "lambda_away": 0.8744430553525447, "rho": -0.0948277249952374, "max_goals": 18, "score_engine_version": "dc-positive-tail-bounded-v1", "reference": null} |
| Legacy p home | 0.7222 |
| Legacy p draw | 0.1685 |
| Legacy p away | 0.1093 |
| Legacy p over 1 5 | 0.8533 |
| Legacy p under 3 5 | 0.5724 |
| Legacy p btts yes | 0.5372 |
| Legacy p over 2 5 | 0.6511 |
| Legacy goal margin distribution | {"-1": 0.07376775558928896, "-10": 3.205615904490852e-09, "-11": 2.508072778340937e-10, "-12": 1.803122110100728e-11, "-13": 1.1988737514172896e-12, "-14": 7.413105414140287e-14, "-15": 4.2835214604083795e-15, "-16": 2.3222845551454864e-16, "-17": 1.1792165427995223e-17, "-18": 5.1184550655661325e-19, "-2": 0.027159643348743958, "-3": 0.006809906698803895, "-4": 0.0013528318829641348, "-5": 0.00022149527401335386, "-6": 3.076538612552517e-05, "-7": 3.705260546440993e-06, "-8": 3.9354390877500693e-07, "-9": 3.736279728786682e-08, "0": 0.16849595422613606, "1": 0.21827199662148944, "10": 9.614491946878237e-05, "11": 2.1110424476109535e-05, "12": 4.259159907829036e-06, "13": 7.94720167511037e-07, "14": 1.3790592761255074e-07, "15": 2.2362774300866143e-08, "16": 3.402374720732527e-09, "17": 4.848442481430892e-10, "18": 5.905947135490851e-11, "2": 0.21174010011668762, "3": 0.1489917388613209, "4": 0.08306285081497285, "5": 0.03816536694695318, "6": 0.014876793124380333, "7": 0.0050281437040151835, "8": 0.0014987324119734497, "9": 0.00039931191014605066} |
| Legacy market blend applied | 1 |
| Legacy raw p home | 0.7132 |
| Legacy raw p draw | 0.1799 |
| Legacy raw p away | 0.1069 |
| Legacy market weight | 0.5000 |
| Legacy lambda home | 2.4540 |
| Legacy lambda away | 0.8744 |
| Legacy model home team | Trabzonspor |
| Legacy model away team | Gaziantep |
| Legacy home name match score | 100/100 |
| Legacy away name match score | 100/100 |
| Elo home rating | 1,616.7819 |
| Elo away rating | 1,414.5620 |
| Elo rating diff | 262.2199 |
| Elo home expectancy | 0.8190 |

</details>


---
