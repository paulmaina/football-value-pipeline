# Bundesliga — football model report

Fixtures in this report: **15**.

> Probabilities are model estimates. They describe uncertainty; they are not guarantees. Market EV figures are only shown when bookmaker prices are available.

### Model context

| Item | Value |
| --- | --- |
| League | Bundesliga |
| Training matches | 1,586 |
| Training data through | 2026-10-18 |
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
| Training sha256 | 36e008b06627fefa8c0cd1c36857514046e5e9c91e95d456df742a17133ed250 |
| Training as of utc | 2026-10-21T17:18:16.494074+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 54, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 54, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.', 'api_football': {'status': 'AVAILABLE', 'matched_results': 254, 'added_results': 2, 'conflicts': 0, 'unmapped': 668, 'ambiguous': 0, 'excluded_phase': 0, 'statistics_observations': 13, 'source': 'api-football', 'usage': 'supplementary_cached_observations'}} |
| Bbs statistics model | {'version': 'bbs-lagged-poisson-v2', 'status': 'INSUFFICIENT_RETROSPECTIVE_EXAMPLES', 'cutoff_utc': '2026-10-21T17:18:16.494074+00:00', 'observations': 112, 'observations_sha256': '80049e9edf2057097a1415fd196c13c7a730cfe122a4ec9be55051637db8f79f', 'eligible_training_matches': 15, 'required_training_matches': 120, 'feature_fields': ['shots_on_target', 'shots_off_target', 'total_shots', 'blocked_shots', 'shots_inside_box', 'shots_outside_box', 'fouls', 'corner_kicks', 'offsides', 'ball_possession', 'yellow_cards', 'red_cards', 'goalkeeper_saves', 'total_passes', 'accurate_passes', 'pass_percentage'], 'minimum_team_matches': 3, 'max_form_matches': 8, 'max_form_age_days': 180, 'max_goal_rate_ratio': 1.25, 'selected_weight': 0.0, 'usable_current_matches': 54, 'validation_policy': 'auto', 'validation_mode': 'retrospective_backfill', 'strict_eligible_training_matches': 6, 'retrospective_eligible_training_matches': 15, 'retrospective_publication_delay_hours': 24, 'forward_accuracy_improvement_established': False, 'first_observed_at_utc': '2026-10-16T20:39:27.947476+00:00', 'retrospective_inputs_sha256': 'f3c52b31b22ce35cda6a56921bb9951a0f1b367416dc9fffed202ca6165e5247', 'historical_corrections_may_be_present': True, 'evaluation_note': 'Retrospective latest-revision study with assumed 24-hour publication delay; not a point-in-time replay or proof of forward improvement.', 'input_providers': ['api-football', 'bigballsdata']} |
| Optimizer objective | 4828.985 |
| Base scoring parameter | 0.233 |
| Home-advantage parameter | 0.236 |
| Dixon-Coles low-score adjustment | -0.111 |
| Xi per day | 0 |
| Training data health | {'training_end': '2026-10-18', 'days_since_latest_result': 3, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 15.00 |
| Additional event odds calls used before this league | 1.00 |
| Bbs statistics model artifact | bbs/feature_models/Bundesliga/20261021T171816494074Z_acb2c96ae589768b5627a576ba44aba5ac8d440f6d210f54722306b931f3091e.json |
| Over 1 5 in window quote fixtures | 0 |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 0.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 0.00 |
| Bbs statistics applied fixtures | 0 |
| Decay tuning | {'selected_half_life_days': 1000000000.0, 'selected_xi_per_day': 6.931471805599453e-10, 'selection_metric': 'walk_forward_1x2_log_loss', 'validation_days': 365} |
| Goal market reliability | {'home_draw': 'RELIABLE_FOR_RANKING', 'draw_away': 'RELIABLE_FOR_RANKING', 'home_away': 'RELIABLE_FOR_RANKING', 'home': 'RELIABLE_FOR_RANKING', 'draw': 'RELIABLE_FOR_RANKING', 'away': 'RELIABLE_FOR_RANKING', 'over_1_5': 'UNRELIABLE_AUDIT', 'under_3_5': 'UNRELIABLE_AUDIT', 'btts_yes': 'UNRELIABLE_AUDIT'} |

</details>

## Quick reference

- **Expected goals:** The model's average goal expectation for each team. It is not a prediction that the team will score exactly that many goals.
- **Fair odds:** Decimal odds implied by the model probability, before any bookmaker margin.
- **Expected value:** Model-estimated return per unit staked at the available decimal price. +5% EV means +0.05 expected units per 1 unit staked under the model; it is not a guaranteed return.
- **Probability edge:** Model probability minus the de-vigged market probability.
- **Fixture source:** Football-Data may include bookmaker prices. A schedule fallback may supply fixtures without betting prices, so EV fields can legitimately be blank.

---

## 2026-10-23 — VfB Stuttgart vs Borussia Monchengladbach

The model's most likely 1X2 outcome is **VfB Stuttgart win** at **64.5%**. Expected goals are 2.17 for VfB Stuttgart and 1.29 for Borussia Monchengladbach (3.46 combined). The most likely exact score is 2-1 at 10.9%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.8%; Under 3.5 goals: 53.8%; Double Chance 1X: 82.8%; Double Chance X2: 35.5%; Double Chance 12 (either team wins): 81.8%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 63.9%; BTTS No (at least one team does not score): 36.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| VfB Stuttgart win | 64.5% | 1.55 |
| Draw | 18.2% | 5.48 |
| Borussia Monchengladbach win | 17.2% | 5.80 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| VfB Stuttgart expected goals | 2.17 |
| Borussia Monchengladbach expected goals | 1.29 |
| Expected total goals | 3.46 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.8% |
| Under 2.5 | 31.2% |
| Over 3.5 | 46.2% |
| Under 3.5 | 53.8% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 10.91% |
| 2 | 2-0 | 8.47% |
| 3 | 1-1 | 7.99% |
| 4 | 3-1 | 7.88% |
| 5 | 1-0 | 6.70% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| VfB Stuttgart win | 64.5% | 72.6% | 1.38 | -11.0% |
| Draw | 18.2% | 14.1% | 5.81 | +6.0% |
| Borussia Monchengladbach win | 17.2% | 13.3% | 7.00 | +20.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-23T18:30:00+00:00 |
| Fixture id | d4d56a31d8ccd432e3a6183180e093f3 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Stuttgart |
| Matched away-team name | M'gladbach |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.1677 |
| Dc lambda away | 1.2876 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 63.9% |
| P btts no | 36.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.63 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.94 |
| Fair Over 2.5 odds | 1.45 |
| Fair Under 2.5 odds | 3.21 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.60 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.09868676123961637, "-10": 1.1422262068639261e-07, "-11": 1.3098462252820987e-08, "-12": 1.3811591814222784e-09, "-13": 1.347620892240922e-10, "-14": 1.2233493689066054e-11, "-15": 1.0375587149267508e-12, "-16": 8.177308307962866e-14, "-17": 5.3202500774515584e-15, "-2": 0.0495601519081566, "-3": 0.017636230360281464, "-4": 0.005031556448826027, "-5": 0.0011915148755233622, "-6": 0.0002404584461708915, "-7": 4.22045202627341e-05, "-8": 6.546665205264983e-06, "-9": 9.091239377902507e-07, "0": 0.1823896167037098, "1": 0.24050076478569224, "10": 2.9265125711962997e-05, "11": 5.64956969145812e-06, "12": 1.002849069654744e-06, "13": 1.6472380290833795e-07, "14": 2.5173054195256427e-08, "15": 3.5941390478513296e-09, "16": 4.768583021339068e-10, "17": 5.222853045362193e-11, "2": 0.19685961576152328, "3": 0.11793061157808211, "4": 0.05663956653160607, "5": 0.02257947417603503, "6": 0.007670985739562934, "7": 0.0022665582808453198, "8": 0.0005918679702514465, "9": 0.00013836446979301165} |
| Raw goal margin distribution | {"-1": 0.12109323137389363, "-10": 1.401564511913209e-07, "-11": 1.6072420457409162e-08, "-12": 1.694746349148661e-09, "-13": 1.6535933134151092e-10, "-14": 1.501106392785803e-11, "-15": 1.2731326466937278e-12, "-16": 1.0033936411668375e-13, "-17": 6.528193503397635e-15, "-2": 0.0608126041077387, "-3": 0.0216404723060618, "-4": 0.0061739530366096045, "-5": 0.001462043993488214, "-6": 0.00029505366162822, "-7": 5.178690305572449e-05, "-8": 8.033061724497357e-06, "-9": 1.1155372206316423e-06, "0": 0.22361007656875537, "1": 0.2105460010348623, "10": 2.562010642222666e-05, "11": 4.9459065428096e-06, "12": 8.77942577211712e-07, "13": 1.4420718374226417e-07, "14": 2.20377091081933e-08, "15": 3.1464831488692394e-09, "16": 4.174648203885513e-10, "17": 4.572338153159927e-11, "2": 0.1723404285253819, "3": 0.10324216095315297, "4": 0.04958501584892727, "5": 0.019767163723867467, "6": 0.00671555191477094, "7": 0.001984254738523079, "8": 0.0005181498461682914, "9": 0.00012113094869443307} |
| Unadjusted home-win probability | 56.5% |
| Unadjusted draw probability | 22.4% |
| Unadjusted away-win probability | 21.2% |
| Raw p over 1 5 | 86.9% |
| Raw p under 3 5 | 54.6% |
| Raw p btts yes | 65.1% |
| P home draw | 82.8% |
| P draw away | 35.5% |
| P home away | 81.8% |
| Raw p home draw | 78.8% |
| Raw p draw away | 43.5% |
| Raw p home away | 77.6% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 2.01, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.33 |
| Reference draw odds | 5.70 |
| Reference away odds | 6.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.70 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -8.0% |
| Draw probability edge | +4.1% |
| Away probability edge | +3.9% |
| Over 2.5 probability edge | -8.7% |
| Under 2.5 probability edge | +8.7% |
| Raw edge prob home | -0.1607 |
| Raw ev home | -0.2205 |
| Raw edge prob draw | 0.0824 |
| Raw ev draw | 0.2992 |
| Raw edge prob away | 0.0783 |
| Raw ev away | 0.4808 |

</details>


---

## 2026-10-24 — 1. FC Köln vs FC Schalke 04

The model's most likely 1X2 outcome is **1. FC Köln win** at **51.2%**. Expected goals are 1.76 for 1. FC Köln and 0.93 for FC Schalke 04 (2.69 combined). The most likely exact score is 1-1 at 11.8%. Goal-market probabilities: at least one goal: 92.3%; Over 2.5 goals: 50.5%; Under 3.5 goals: 72.1%; Double Chance 1X: 76.0%; Double Chance X2: 48.8%; Double Chance 12 (either team wins): 75.3%; Under 4.5 goals: 86.5%; BTTS Yes (both teams score): 51.4%; BTTS No (at least one team does not score): 48.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| 1. FC Köln win | 51.2% | 1.95 |
| Draw | 24.7% | 4.04 |
| FC Schalke 04 win | 24.0% | 4.16 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| 1. FC Köln expected goals | 1.76 |
| FC Schalke 04 expected goals | 0.93 |
| Expected total goals | 2.69 |
| Over 0.5 | 92.3% |
| Under 0.5 | 7.7% |
| Over 1.5 | 75.8% |
| Under 1.5 | 24.2% |
| Over 2.5 | 50.5% |
| Under 2.5 | 49.5% |
| Over 3.5 | 27.9% |
| Under 3.5 | 72.1% |
| Over 4.5 | 13.5% |
| Under 4.5 | 86.5% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.82% |
| 2 | 1-0 | 9.88% |
| 3 | 2-0 | 9.67% |
| 4 | 2-1 | 9.01% |
| 5 | 0-0 | 7.68% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| 1. FC Köln win | 51.2% | 46.9% | 2.09 | +7.1% |
| Draw | 24.7% | 23.6% | 3.92 | -3.1% |
| FC Schalke 04 win | 24.0% | 29.6% | 3.33 | -19.9% |
| Over 2.5 | 50.5% | 60.1% | 1.64 | -17.2% |
| Under 2.5 | 49.5% | 39.9% | 2.46 | +21.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 983440c6e348b558c6a3e10e2061ba55 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | FC Koln |
| Matched away-team name | Schalke 04 |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7564 |
| Dc lambda away | 0.9311 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 51.4% |
| P btts no | 48.6% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.01 |
| Fair Over 1.5 odds | 1.32 |
| Fair Under 1.5 odds | 4.14 |
| Fair Over 2.5 odds | 1.98 |
| Fair Under 2.5 odds | 2.02 |
| Fair Over 3.5 odds | 3.58 |
| Fair Under 3.5 odds | 1.39 |
| Fair Over 4.5 odds | 7.43 |
| Fair Under 4.5 odds | 1.16 |
| Goal margin distribution | {"-1": 0.1543728168193308, "-10": 1.3806105220222578e-08, "-11": 1.154441846556072e-09, "-12": 8.865187352943932e-11, "-13": 6.293231575521829e-12, "-14": 4.1525660263634477e-13, "-15": 2.5489342474787017e-14, "-16": 1.3457370779214134e-15, "-2": 0.06387738473124673, "-3": 0.01759938572062151, "-4": 0.003801287325869639, "-5": 0.0006725351456090927, "-6": 0.00010055715184915436, "-7": 1.3003769790223553e-05, "-8": 1.4804079190905373e-06, "-9": 1.504585406816209e-07, "0": 0.24725127241292913, "1": 0.21701493256405993, "10": 5.598901959378642e-06, "11": 8.831812633496893e-07, "12": 1.2794160857272488e-07, "13": 1.7133405903893252e-08, "14": 2.132714097048539e-09, "15": 2.4695670838050756e-10, "16": 2.4596228331443734e-11, "2": 0.1615139328267382, "3": 0.08394725067850482, "4": 0.03420469857074106, "5": 0.011416057749471407, "6": 0.003220032377665517, "7": 0.0007855297713360501, "8": 0.00016870225152021287, "9": 3.2344647818206814e-05} |
| Raw goal margin distribution | {"-1": 0.11901474332135975, "-10": 1.0643908059120939e-08, "-11": 8.900245708938997e-10, "-12": 6.834674776591024e-11, "-13": 4.851808472855552e-12, "-14": 3.201448220842195e-13, "-15": 1.965117703084587e-14, "-16": 1.0375048937164822e-15, "-2": 0.04924669190124604, "-3": 0.013568362729331802, "-4": 0.0029306275852217386, "-5": 0.0005184954150505373, "-6": 7.752520076420267e-05, "-7": 1.0025342257016527e-05, "-8": 1.1413302687070346e-06, "-9": 1.159970062649473e-07, "0": 0.25873798360184974, "1": 0.2354772162829617, "10": 6.075221792613391e-06, "11": 9.58316844420208e-07, "12": 1.3882608665455026e-07, "13": 1.8591009752307734e-08, "14": 2.3141521773031713e-09, "15": 2.679662525742516e-10, "16": 2.6688722799472834e-11, "2": 0.175254535914144, "3": 0.09108896180933139, "4": 0.03711462205882234, "5": 0.012387265097426105, "6": 0.003493972749593434, "7": 0.0008523577694682487, "8": 0.00018305439215304375, "9": 3.509632973130014e-05} |
| Unadjusted home-win probability | 55.6% |
| Unadjusted draw probability | 25.9% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 76.1% |
| Raw p under 3 5 | 71.7% |
| Raw p btts yes | 51.4% |
| P home draw | 76.0% |
| P draw away | 48.8% |
| P home away | 75.3% |
| Raw p home draw | 81.5% |
| Raw p draw away | 44.4% |
| Raw p home away | 74.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.61, "price": 2.54, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 2.1, "price": 1.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.83, "price": 2.1, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.54, "price": 1.61, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.00 |
| Reference draw odds | 3.75 |
| Reference away odds | 3.05 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / Codere (IT) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.23 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market best over 2 5 last update utc | 2026-10-21T17:19:22Z |
| Market best under 2 5 last update utc | 2026-10-21T17:19:22Z |
| Home probability edge | +4.4% |
| Draw probability edge | +1.1% |
| Away probability edge | -5.5% |
| Over 2.5 probability edge | -9.6% |
| Under 2.5 probability edge | +9.6% |
| Raw edge prob home | 0.0872 |
| Raw ev home | 0.1618 |
| Raw edge prob draw | 0.0230 |
| Raw ev draw | 0.0143 |
| Raw edge prob away | -0.1101 |
| Raw ev away | -0.3827 |

</details>


---

## 2026-10-24 — Augsburg vs Union Berlin

The model's most likely 1X2 outcome is **Augsburg win** at **46.6%**. Expected goals are 1.34 for Augsburg and 1.16 for Union Berlin (2.50 combined). The most likely exact score is 1-1 at 12.3%. Goal-market probabilities: at least one goal: 91.6%; Over 2.5 goals: 47.1%; Under 3.5 goals: 75.4%; Double Chance 1X: 72.5%; Double Chance X2: 53.4%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 88.7%; BTTS Yes (both teams score): 51.1%; BTTS No (at least one team does not score): 48.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 46.6% | 2.15 |
| Draw | 25.8% | 3.87 |
| Union Berlin win | 27.5% | 3.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.34 |
| Union Berlin expected goals | 1.16 |
| Expected total goals | 2.50 |
| Over 0.5 | 91.6% |
| Under 0.5 | 8.4% |
| Over 1.5 | 73.1% |
| Under 1.5 | 26.9% |
| Over 2.5 | 47.1% |
| Under 2.5 | 52.9% |
| Over 3.5 | 24.6% |
| Under 3.5 | 75.4% |
| Over 4.5 | 11.3% |
| Under 4.5 | 88.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.34% |
| 2 | 1-0 | 11.31% |
| 3 | 2-1 | 10.08% |
| 4 | 2-0 | 8.72% |
| 5 | 0-0 | 8.38% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 46.6% | 53.6% | 1.85 | -13.8% |
| Draw | 25.8% | 22.0% | 4.18 | +8.0% |
| Union Berlin win | 27.5% | 24.4% | 3.94 | +8.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04bb232a2940fcf03abf05b308e27577 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Union Berlin |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3432 |
| Dc lambda away | 1.1565 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 51.1% |
| P btts no | 48.9% |
| Fair Over 0.5 odds | 1.09 |
| Fair Under 0.5 odds | 11.93 |
| Fair Over 1.5 odds | 1.37 |
| Fair Under 1.5 odds | 3.71 |
| Fair Over 2.5 odds | 2.12 |
| Fair Under 2.5 odds | 1.89 |
| Fair Over 3.5 odds | 4.07 |
| Fair Under 3.5 odds | 1.33 |
| Fair Over 4.5 odds | 8.82 |
| Fair Under 4.5 odds | 1.13 |
| Goal margin distribution | {"-1": 0.1581172840213112, "-10": 9.997738512261338e-08, "-11": 1.0390511202453509e-08, "-12": 9.914325962891827e-10, "-13": 8.701497936381133e-11, "-14": 6.470376616001407e-12, "-2": 0.08024350296184302, "-3": 0.0276073386186249, "-4": 0.007432461585834489, "-5": 0.0016373564097276992, "-6": 0.0003046428030556433, "-7": 4.9002193736480996e-05, "-8": 6.936987907792375e-06, "-9": 8.765164891973164e-07, "0": 0.2584906213711867, "1": 0.24376148516457063, "10": 5.859080549674726e-07, "11": 7.071940309399661e-08, "12": 7.836801408062546e-09, "13": 7.988102813976816e-10, "14": 6.898476052393889e-11, "2": 0.14208419204373607, "3": 0.056772027110600747, "4": 0.01775074189291326, "5": 0.0045415179667220315, "6": 0.000981347254077578, "7": 0.00018332482893246822, "8": 3.0140515742143023e-05, "9": 4.422968118943602e-06} |
| Raw goal margin distribution | {"-1": 0.17631768733572914, "-10": 1.1148548015988455e-07, "-11": 1.1586531585033207e-08, "-12": 1.1055534099827161e-09, "-13": 9.703101099893391e-11, "-14": 7.215162138572943e-12, "-2": 0.08948009038684832, "-3": 0.030785136039107753, "-4": 0.008287989805398858, "-5": 0.0018258275639784572, "-6": 0.0003397093166045364, "-7": 5.464268835296449e-05, "-8": 7.735483647777666e-06, "-9": 9.774096566576089e-07, "0": 0.2969714563414985, "1": 0.20705879981810144, "10": 4.976890364095792e-07, "11": 6.007132225424986e-08, "12": 6.6568296992066634e-09, "13": 6.785349951281142e-10, "14": 5.859786138972053e-11, "2": 0.12069085589070173, "3": 0.048223975123984235, "4": 0.01507804774714968, "5": 0.0038577105768244817, "6": 0.0008335877363764364, "7": 0.00015572197154110854, "8": 2.5602317820033532e-05, "9": 3.757010545467813e-06} |
| Unadjusted home-win probability | 39.6% |
| Unadjusted draw probability | 29.7% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 72.7% |
| Raw p under 3 5 | 75.8% |
| Raw p btts yes | 52.1% |
| P home draw | 72.5% |
| P draw away | 53.4% |
| P home away | 74.2% |
| Raw p home draw | 69.3% |
| Raw p draw away | 60.4% |
| Raw p home away | 70.3% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.44, "price": 3.1, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.06, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.06, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.1, "price": 1.44, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.76 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.60 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -7.0% |
| Draw probability edge | +3.8% |
| Away probability edge | +3.2% |
| Over 2.5 probability edge | -16.7% |
| Under 2.5 probability edge | +16.7% |
| Raw edge prob home | -0.1404 |
| Raw ev home | -0.2675 |
| Raw edge prob draw | 0.0770 |
| Raw ev draw | 0.2413 |
| Raw edge prob away | 0.0634 |
| Raw ev away | 0.2100 |

</details>


---

## 2026-10-24 — Borussia Dortmund vs Eintracht Frankfurt

The model's most likely 1X2 outcome is **Borussia Dortmund win** at **65.3%**. Expected goals are 2.42 for Borussia Dortmund and 1.22 for Eintracht Frankfurt (3.64 combined). The most likely exact score is 2-1 at 9.7%. Goal-market probabilities: at least one goal: 96.8%; Over 2.5 goals: 71.2%; Under 3.5 goals: 50.3%; Double Chance 1X: 83.7%; Double Chance X2: 34.7%; Double Chance 12 (either team wins): 81.6%; Under 4.5 goals: 69.3%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Dortmund win | 65.3% | 1.53 |
| Draw | 18.4% | 5.44 |
| Eintracht Frankfurt win | 16.3% | 6.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Dortmund expected goals | 2.42 |
| Eintracht Frankfurt expected goals | 1.22 |
| Expected total goals | 3.64 |
| Over 0.5 | 96.8% |
| Under 0.5 | 3.2% |
| Over 1.5 | 88.9% |
| Under 1.5 | 11.1% |
| Over 2.5 | 71.2% |
| Under 2.5 | 28.8% |
| Over 3.5 | 49.7% |
| Under 3.5 | 50.3% |
| Over 4.5 | 30.7% |
| Under 4.5 | 69.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.73% |
| 2 | 2-0 | 7.95% |
| 3 | 1-1 | 7.87% |
| 4 | 3-1 | 7.85% |
| 5 | 3-0 | 6.42% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Dortmund win | 65.3% | 67.7% | 1.48 | -3.3% |
| Draw | 18.4% | 16.7% | 5.21 | -4.2% |
| Eintracht Frankfurt win | 16.3% | 15.6% | 5.89 | -4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T16:30:00+00:00 |
| Fixture id | 3ed4d1e775910625c50518a384e9c547 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Dortmund |
| Matched away-team name | Ein Frankfurt |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.4207 |
| Dc lambda away | 1.2229 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 31.44 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.00 |
| Fair Over 2.5 odds | 1.40 |
| Fair Under 2.5 odds | 3.47 |
| Fair Over 3.5 odds | 2.01 |
| Fair Under 3.5 odds | 1.99 |
| Fair Over 4.5 odds | 3.26 |
| Fair Under 4.5 odds | 1.44 |
| Goal margin distribution | {"-1": 0.09679277900737275, "-10": 6.757548269976811e-08, "-11": 7.350821181380767e-09, "-12": 7.35385480573505e-10, "-13": 6.808584494752263e-11, "-14": 5.865682422594714e-12, "-15": 4.724372581696474e-13, "-16": 3.5702208533573685e-14, "-17": 2.51643307324631e-15, "-18": 1.4681984631877626e-16, "-2": 0.04570947349640482, "-3": 0.015307341312822517, "-4": 0.00412149547912829, "-5": 0.0009227212224781454, "-6": 0.00017624700623643876, "-7": 2.930117788914005e-05, "-8": 4.307507102100867e-06, "-9": 5.671269270045752e-07, "0": 0.18383995817704496, "1": 0.21582311880364632, "10": 6.744537881203169e-05, "11": 1.4522468318209029e-05, "12": 2.8758164825391262e-06, "13": 5.270411037337507e-07, "14": 8.987682858549308e-08, "15": 1.4328966649450334e-08, "16": 2.1434203604717738e-09, "17": 2.990468222546588e-10, "18": 3.453664213648516e-11, "2": 0.1935695127467173, "3": 0.12831340854634712, "4": 0.06838622670835977, "5": 0.03030580756877675, "6": 0.011458259100332461, "7": 0.003770713248333018, "8": 0.0010972509560048394, "9": 0.00028595768440899745} |
| Raw goal margin distribution | {"-1": 0.1008006314439521, "-10": 7.037354848286398e-08, "-11": 7.655193128180763e-09, "-12": 7.658352364371845e-10, "-13": 7.09050430568021e-11, "-14": 6.108559937123004e-12, "-15": 4.919992423972296e-13, "-16": 3.718051285472194e-14, "-17": 2.620629817337425e-15, "-18": 1.5289914567190354e-16, "-2": 0.0476021438650629, "-3": 0.015941165093969187, "-4": 0.004292152276750733, "-5": 0.000960927900060063, "-6": 0.00018354478196546005, "-7": 3.0514437787264173e-05, "-8": 4.485865994280446e-06, "-9": 5.906096811888715e-07, "0": 0.20089572489951996, "1": 0.2079555884350204, "10": 6.498675172440305e-05, "11": 1.3993072018339661e-05, "12": 2.770982609150631e-06, "13": 5.078285563842156e-07, "14": 8.66004943250496e-08, "15": 1.3806624182663249e-08, "16": 2.06528496481898e-09, "17": 2.8814548801034117e-10, "18": 3.327765708268113e-11, "2": 0.18651320650660386, "3": 0.12363592244552431, "4": 0.06589330232469699, "5": 0.029201051680182593, "6": 0.011040564267901348, "7": 0.0036332571631967907, "8": 0.0010572522048690734, "9": 0.0002755334964040203} |
| Unadjusted home-win probability | 62.9% |
| Unadjusted draw probability | 20.1% |
| Unadjusted away-win probability | 17.0% |
| Raw p over 1 5 | 88.7% |
| Raw p under 3 5 | 50.6% |
| Raw p btts yes | 65.2% |
| P home draw | 83.7% |
| P draw away | 34.7% |
| P home away | 81.6% |
| Raw p home draw | 83.0% |
| Raw p draw away | 37.1% |
| Raw p home away | 79.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.25, "market_key": "spreads", "opposite_price": 2.0, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.19, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.19, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.25, "market_key": "spreads", "opposite_price": 1.91, "price": 2.0, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.42 |
| Reference draw odds | 5.00 |
| Reference away odds | 5.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.25 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -2.4% |
| Draw probability edge | +1.7% |
| Away probability edge | +0.7% |
| Over 2.5 probability edge | -1.7% |
| Under 2.5 probability edge | +1.7% |
| Raw edge prob home | -0.0476 |
| Raw ev home | -0.0687 |
| Raw edge prob draw | 0.0341 |
| Raw ev draw | 0.0467 |
| Raw edge prob away | 0.0135 |
| Raw ev away | 0.0002 |

</details>


---

## 2026-10-24 — FSV Mainz 05 vs Werder Bremen

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **53.2%**. Expected goals are 1.73 for FSV Mainz 05 and 1.16 for Werder Bremen (2.89 combined). The most likely exact score is 1-1 at 11.3%. Goal-market probabilities: at least one goal: 93.8%; Over 2.5 goals: 56.2%; Under 3.5 goals: 66.8%; Double Chance 1X: 77.1%; Double Chance X2: 46.8%; Double Chance 12 (either team wins): 76.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.1%; BTTS No (at least one team does not score): 42.9%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 1.88 |
| Draw | 23.8% | 4.19 |
| Werder Bremen win | 22.9% | 4.36 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FSV Mainz 05 expected goals | 1.73 |
| Werder Bremen expected goals | 1.16 |
| Expected total goals | 2.89 |
| Over 0.5 | 93.8% |
| Under 0.5 | 6.2% |
| Over 1.5 | 79.9% |
| Under 1.5 | 20.1% |
| Over 2.5 | 56.2% |
| Under 2.5 | 43.8% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.28% |
| 2 | 2-1 | 10.38% |
| 3 | 1-0 | 9.01% |
| 4 | 2-0 | 8.94% |
| 5 | 0-0 | 6.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FSV Mainz 05 win | 53.2% | 57.0% | 1.76 | -6.3% |
| Draw | 23.8% | 21.5% | 4.22 | +0.6% |
| Werder Bremen win | 22.9% | 21.5% | 4.34 | -0.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 4e5820453145833132980b8d190998c7 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Mainz |
| Matched away-team name | Werder Bremen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.7299 |
| Dc lambda away | 1.1608 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 57.1% |
| P btts no | 42.9% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.17 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.98 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.02 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.85 |
| Fair Under 4.5 odds | 1.21 |
| Goal margin distribution | {"-1": 0.13416603285151874, "-10": 7.67165805056047e-08, "-11": 7.975704841365542e-09, "-12": 7.617989760475288e-10, "-13": 6.728516320669057e-11, "-14": 5.52477964880308e-12, "-15": 4.212589473622982e-13, "-16": 2.715382832623251e-14, "-2": 0.06559848291630575, "-3": 0.022015395785502465, "-4": 0.005837845435299312, "-5": 0.0012737890175945656, "-6": 0.0002355484419690608, "-7": 3.774238765656451e-05, "-8": 5.33081349797985e-06, "-9": 6.727951744368275e-07, "0": 0.23849644314536608, "1": 0.2350730772719502, "10": 4.738312838955212e-06, "11": 7.341302638644599e-07, "12": 1.0449944863161988e-07, "13": 1.3755059860354402e-08, "14": 1.6831688917270306e-09, "15": 1.9126320679310384e-10, "16": 1.837312048183138e-11, "2": 0.166522072976867, "3": 0.08328639620328905, "4": 0.032913170954497674, "5": 0.010702474298362083, "6": 0.0029494191078796423, "7": 0.0007042959397620692, "8": 0.00014824800665865192, "9": 2.7883533089254323e-05} |
| Raw goal margin distribution | {"-1": 0.14248044903347032, "-10": 8.147079112675128e-08, "-11": 8.469968016523358e-09, "-12": 8.090084939800852e-10, "-13": 7.145489855535434e-11, "-14": 5.867156302099236e-12, "-15": 4.4736482628186967e-13, "-16": 2.883658084443077e-14, "-2": 0.0696636928377649, "-3": 0.023379714004359144, "-4": 0.006199623118691815, "-5": 0.0013527271198488175, "-6": 0.00025014563721972795, "-7": 4.008132480785166e-05, "-8": 5.661169856206685e-06, "-9": 7.144890291822179e-07, "0": 0.26202393390962314, "1": 0.21841210107921427, "10": 4.402481452733818e-06, "11": 6.820982447555145e-07, "12": 9.709297381957131e-08, "13": 1.278015993764697e-08, "14": 1.5638730661103219e-09, "15": 1.7770728719606852e-10, "16": 1.7070912136722062e-11, "2": 0.154719699325107, "3": 0.0773834119890804, "4": 0.030580425903196276, "5": 0.009943928608835537, "6": 0.0027403768725498424, "7": 0.0006543784501831102, "8": 0.00013774082081574514, "9": 2.5907267298374388e-05} |
| Unadjusted home-win probability | 49.5% |
| Unadjusted draw probability | 26.2% |
| Unadjusted away-win probability | 24.3% |
| Raw p over 1 5 | 79.6% |
| Raw p under 3 5 | 67.2% |
| Raw p btts yes | 57.7% |
| P home draw | 77.1% |
| P draw away | 46.8% |
| P home away | 76.2% |
| Raw p home draw | 75.7% |
| Raw p draw away | 50.5% |
| Raw p home away | 73.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.97, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.99, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.93, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 4.00 |
| Reference away odds | 4.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.50 |
| Reference Under 2.5 odds | 2.50 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -3.8% |
| Draw probability edge | +2.4% |
| Away probability edge | +1.4% |
| Over 2.5 probability edge | -7.6% |
| Under 2.5 probability edge | +7.6% |
| Raw edge prob home | -0.0755 |
| Raw ev home | -0.1295 |
| Raw edge prob draw | 0.0471 |
| Raw ev draw | 0.1057 |
| Raw edge prob away | 0.0284 |
| Raw ev away | 0.0562 |

</details>


---

## 2026-10-24 — RB Leipzig vs Elversberg

The model's most likely 1X2 outcome is **RB Leipzig win** at **67.7%**. Expected goals are 2.69 for RB Leipzig and 1.32 for Elversberg (4.01 combined). The most likely exact score is 2-1 at 8.9%. Goal-market probabilities: at least one goal: 97.6%; Over 2.5 goals: 76.7%; Under 3.5 goals: 42.9%; Double Chance 1X: 84.9%; Double Chance X2: 32.3%; Double Chance 12 (either team wins): 82.8%; Under 4.5 goals: 62.4%; BTTS Yes (both teams score): 68.7%; BTTS No (at least one team does not score): 31.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| RB Leipzig win | 67.7% | 1.48 |
| Draw | 17.2% | 5.82 |
| Elversberg win | 15.1% | 6.60 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| RB Leipzig expected goals | 2.69 |
| Elversberg expected goals | 1.32 |
| Expected total goals | 4.01 |
| Over 0.5 | 97.6% |
| Under 0.5 | 2.4% |
| Over 1.5 | 91.7% |
| Under 1.5 | 8.3% |
| Over 2.5 | 76.7% |
| Under 2.5 | 23.3% |
| Over 3.5 | 57.1% |
| Under 3.5 | 42.9% |
| Over 4.5 | 37.6% |
| Under 4.5 | 62.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 8.93% |
| 2 | 3-1 | 8.00% |
| 3 | 2-0 | 6.76% |
| 4 | 1-1 | 6.74% |
| 5 | 3-0 | 6.05% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| RB Leipzig win | 67.7% | 69.7% | 1.42 | -3.9% |
| Draw | 17.2% | 16.1% | 5.27 | -9.4% |
| Elversberg win | 15.1% | 14.2% | 6.87 | +4.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 04dac5e98ab5fc5564980542ca3fc746 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | RB Leipzig |
| Matched away-team name | Elversberg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.6858 |
| Dc lambda away | 1.3218 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 19 |
| Score grid omitted mass | 0 |
| P btts yes | 68.7% |
| P btts no | 31.3% |
| Fair Over 0.5 odds | 1.02 |
| Fair Under 0.5 odds | 41.94 |
| Fair Over 1.5 odds | 1.09 |
| Fair Under 1.5 odds | 12.10 |
| Fair Over 2.5 odds | 1.30 |
| Fair Under 2.5 odds | 4.30 |
| Fair Over 3.5 odds | 1.75 |
| Fair Under 3.5 odds | 2.33 |
| Fair Over 4.5 odds | 2.66 |
| Fair Under 4.5 odds | 1.60 |
| Goal margin distribution | {"-1": 0.0882549443759215, "-10": 1.0559503239243022e-07, "-11": 1.2363032291315834e-08, "-12": 1.3320016596393512e-09, "-13": 1.3287989789513205e-10, "-14": 1.2339742281477004e-11, "-15": 1.0716893861244939e-12, "-16": 8.74001717297334e-14, "-17": 6.712285350368597e-15, "-18": 4.812101618763544e-16, "-19": 2.8205948985952946e-17, "-2": 0.04267232507425902, "-3": 0.014980337015539417, "-4": 0.004267444168178764, "-5": 0.0010166792411250528, "-6": 0.00020743456856357656, "-7": 3.693314304937213e-05, "-8": 5.825431346380811e-06, "-9": 8.240212772428143e-07, "0": 0.17184266709561213, "1": 0.20387879571870743, "10": 0.00013866719705898884, "11": 3.298926459926638e-05, "12": 7.222204442982177e-06, "13": 1.464002031179414e-06, "14": 2.76252275746311e-07, "15": 4.875128707162488e-08, "16": 8.078799384862123e-09, "17": 1.2607307044183005e-09, "18": 1.8365556412682495e-10, "19": 2.1873959219021602e-11, "2": 0.19281352960112552, "3": 0.13754036208295442, "4": 0.07961480004652272, "5": 0.038541383331218926, "6": 0.015978715199656733, "7": 0.005780885575560501, "8": 0.0018527788090513132, "9": 0.0005325388471229038} |
| Raw goal margin distribution | {"-1": 0.09369774775119587, "-10": 1.121072227607075e-07, "-11": 1.3125477436566622e-08, "-12": 1.414148027530939e-09, "-13": 1.410747833135524e-10, "-14": 1.3100751099901487e-11, "-15": 1.1377819393439317e-12, "-16": 9.279026010443002e-14, "-17": 7.126241187280984e-15, "-18": 5.108870520698461e-16, "-19": 2.994544851687606e-17, "-2": 0.045303985845078644, "-3": 0.01590419493021474, "-4": 0.004530623298669443, "-5": 0.001079379243309594, "-6": 0.000220227342701163, "-7": 3.921086059902431e-05, "-8": 6.184693681411648e-06, "-9": 8.748397987521733e-07, "0": 0.18271079127874074, "1": 0.1977906376444483, "10": 0.00013452636518663293, "11": 3.2004150591083786e-05, "12": 7.006537472130741e-06, "13": 1.4202845089356875e-06, "14": 2.680029258460995e-07, "15": 4.72954930005968e-08, "16": 7.837553072160095e-09, "17": 1.2230832002209508e-09, "18": 1.7817130519896652e-10, "19": 2.1220766615220668e-11, "2": 0.1870557986760954, "3": 0.13343317936687055, "4": 0.07723737042700252, "5": 0.03739047387399013, "6": 0.015501564333544608, "7": 0.005608258770162966, "8": 0.0017974517691481293, "9": 0.0005166363562800542} |
| Unadjusted home-win probability | 65.7% |
| Unadjusted draw probability | 18.3% |
| Unadjusted away-win probability | 16.1% |
| Raw p over 1 5 | 91.6% |
| Raw p under 3 5 | 43.2% |
| Raw p btts yes | 69.1% |
| P home draw | 84.9% |
| P draw away | 32.3% |
| P home away | 82.8% |
| Raw p home draw | 83.9% |
| Raw p draw away | 34.3% |
| Raw p home away | 81.7% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.0, "price": 1.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.02, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 2.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.88, "price": 2.02, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.38 |
| Reference draw odds | 5.10 |
| Reference away odds | 5.70 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -2.0% |
| Draw probability edge | +1.1% |
| Away probability edge | +0.9% |
| Over 2.5 probability edge | -1.0% |
| Under 2.5 probability edge | +1.0% |
| Raw edge prob home | -0.0404 |
| Raw ev home | -0.0678 |
| Raw edge prob draw | 0.0217 |
| Raw ev draw | -0.0371 |
| Raw edge prob away | 0.0187 |
| Raw ev away | 0.1046 |

</details>


---

## 2026-10-24 — SC Paderborn vs Hamburger SV

The model's most likely 1X2 outcome is **SC Paderborn win** at **38.8%**. Expected goals are 1.02 for SC Paderborn and 0.96 for Hamburger SV (1.98 combined). The most likely exact score is 1-0 at 14.2%. Goal-market probabilities: at least one goal: 86.8%; Over 2.5 goals: 33.3%; Under 3.5 goals: 85.9%; Double Chance 1X: 68.0%; Double Chance X2: 61.2%; Double Chance 12 (either team wins): 70.7%; Under 4.5 goals: 94.6%; BTTS Yes (both teams score): 39.9%; BTTS No (at least one team does not score): 60.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Paderborn win | 38.8% | 2.58 |
| Draw | 29.3% | 3.41 |
| Hamburger SV win | 32.0% | 3.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Paderborn expected goals | 1.02 |
| Hamburger SV expected goals | 0.96 |
| Expected total goals | 1.98 |
| Over 0.5 | 86.8% |
| Under 0.5 | 13.2% |
| Over 1.5 | 60.7% |
| Under 1.5 | 39.3% |
| Over 2.5 | 33.3% |
| Under 2.5 | 66.7% |
| Over 3.5 | 14.1% |
| Under 3.5 | 85.9% |
| Over 4.5 | 5.4% |
| Under 4.5 | 94.6% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 14.15% |
| 2 | 0-0 | 13.19% |
| 3 | 1-1 | 12.92% |
| 4 | 0-1 | 11.95% |
| 5 | 2-0 | 8.04% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Paderborn win | 38.8% | 43.2% | 2.26 | -12.4% |
| Draw | 29.3% | 24.5% | 3.79 | +11.0% |
| Hamburger SV win | 32.0% | 32.3% | 3.05 | -2.5% |
| Over 2.5 | 33.3% | 61.5% | 1.64 | -45.5% |
| Under 2.5 | 66.7% | 38.5% | 2.47 | +64.8% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-24T13:30:00+00:00 |
| Fixture id | 7630f897583f3acc0f483fa2d17d1ac5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 10.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Paderborn |
| Matched away-team name | Hamburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.0154 |
| Dc lambda away | 0.9628 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 13 |
| Score grid omitted mass | 0 |
| P btts yes | 39.9% |
| P btts no | 60.1% |
| Fair Over 0.5 odds | 1.15 |
| Fair Under 0.5 odds | 7.58 |
| Fair Over 1.5 odds | 1.65 |
| Fair Under 1.5 odds | 2.55 |
| Fair Over 2.5 odds | 3.01 |
| Fair Under 2.5 odds | 1.50 |
| Fair Over 3.5 odds | 7.08 |
| Fair Under 3.5 odds | 1.16 |
| Fair Over 4.5 odds | 18.66 |
| Fair Under 4.5 odds | 1.06 |
| Goal margin distribution | {"-1": 0.19696270117631215, "-10": 2.8838700344688796e-08, "-11": 2.5056664808332233e-09, "-12": 1.9931646170120337e-10, "-13": 1.3729771530397241e-11, "-2": 0.08872350823687257, "-3": 0.026420392165049447, "-4": 0.006072000640597093, "-5": 0.0011331702830155647, "-6": 0.0001777753928619978, "-7": 2.4038623204478917e-05, "-8": 2.854814323910731e-06, "-9": 3.0216042746806703e-07, "0": 0.2928346181010414, "1": 0.23265736022369649, "10": 5.472229177588247e-08, "11": 5.013914032774254e-09, "12": 4.205927827673579e-10, "13": 3.055251631600128e-11, "2": 0.11007966069922508, "3": 0.03456787341954311, "4": 0.008377804836658509, "5": 0.0016487645240658713, "6": 0.0002727722158363138, "7": 3.889583523698821e-05, "8": 4.871204990077157e-06, "9": 5.437022773696443e-07} |
| Raw goal margin distribution | {"-1": 0.19476762215227597, "-10": 2.8517303319622497e-08, "-11": 2.477741721980613e-09, "-12": 1.9709515085599028e-10, "-13": 1.357675812577194e-11, "-2": 0.0877347163960493, "-3": 0.02612594632174029, "-4": 0.006004330360079477, "-5": 0.0011205415045511494, "-6": 0.000175794149542676, "-7": 2.3770721326368364e-05, "-8": 2.8229984369305624e-06, "-9": 2.9879295732134505e-07, "0": 0.3404603274737641, "1": 0.20621072287689068, "10": 4.8501897097668216e-08, "11": 4.443972183587332e-09, "12": 3.72783142075839e-10, "13": 2.7079549381859315e-11, "2": 0.09756668082627919, "3": 0.030638472641944876, "4": 0.007425482648938367, "5": 0.0014613460929604719, "6": 0.00024176564091613254, "7": 3.447446619959909e-05, "8": 4.317485169261446e-06, "9": 4.818985289715616e-07} |
| Unadjusted home-win probability | 34.4% |
| Unadjusted draw probability | 34.0% |
| Unadjusted away-win probability | 31.6% |
| Raw p over 1 5 | 60.3% |
| Raw p under 3 5 | 86.1% |
| Raw p btts yes | 40.9% |
| P home draw | 68.0% |
| P draw away | 61.2% |
| P home away | 70.7% |
| Raw p home draw | 68.4% |
| Raw p draw away | 65.6% |
| Raw p home away | 66.0% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.74, "price": 2.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.98, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.92, "price": 1.98, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.27, "price": 1.74, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.15 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.80 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.56 |
| Reference Under 2.5 odds | 2.40 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market best over 2 5 last update utc | 2026-10-21T17:19:22Z |
| Market best under 2 5 last update utc | 2026-10-21T17:19:22Z |
| Home probability edge | -4.4% |
| Draw probability edge | +4.8% |
| Away probability edge | -0.4% |
| Over 2.5 probability edge | -28.3% |
| Under 2.5 probability edge | +28.3% |
| Raw edge prob home | -0.0881 |
| Raw ev home | -0.2235 |
| Raw edge prob draw | 0.0953 |
| Raw ev draw | 0.2903 |
| Raw edge prob away | -0.0071 |
| Raw ev away | -0.0363 |

</details>


---

## 2026-10-25 — SC Freiburg vs Bayern Munich

The model's most likely 1X2 outcome is **Bayern Munich win** at **67.2%**. Expected goals are 1.24 for SC Freiburg and 2.45 for Bayern Munich (3.68 combined). The most likely exact score is 1-2 at 9.9%. Goal-market probabilities: at least one goal: 97.1%; Over 2.5 goals: 72.4%; Under 3.5 goals: 49.2%; Double Chance 1X: 32.8%; Double Chance X2: 84.3%; Double Chance 12 (either team wins): 83.0%; Under 4.5 goals: 68.2%; BTTS Yes (both teams score): 64.9%; BTTS No (at least one team does not score): 35.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| SC Freiburg win | 15.7% | 6.36 |
| Draw | 17.0% | 5.87 |
| Bayern Munich win | 67.2% | 1.49 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| SC Freiburg expected goals | 1.24 |
| Bayern Munich expected goals | 2.45 |
| Expected total goals | 3.68 |
| Over 0.5 | 97.1% |
| Under 0.5 | 2.9% |
| Over 1.5 | 89.4% |
| Under 1.5 | 10.6% |
| Over 2.5 | 72.4% |
| Under 2.5 | 27.6% |
| Over 3.5 | 50.8% |
| Under 3.5 | 49.2% |
| Over 4.5 | 31.8% |
| Under 4.5 | 68.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 9.91% |
| 2 | 1-3 | 8.09% |
| 3 | 0-2 | 8.01% |
| 4 | 1-1 | 7.23% |
| 5 | 0-3 | 6.53% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| SC Freiburg win | 15.7% | 14.4% | 6.56 | +3.1% |
| Draw | 17.0% | 14.2% | 5.99 | +2.1% |
| Bayern Munich win | 67.2% | 71.4% | 1.39 | -6.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T16:30:00+00:00 |
| Fixture id | f2bd909f25eea6b4ce42d2f52275e5c4 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Freiburg |
| Matched away-team name | Bayern Munich |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.2378 |
| Dc lambda away | 2.4468 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.9% |
| P btts no | 35.1% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 34.83 |
| Fair Over 1.5 odds | 1.12 |
| Fair Under 1.5 odds | 9.42 |
| Fair Over 2.5 odds | 1.38 |
| Fair Under 2.5 odds | 3.62 |
| Fair Over 3.5 odds | 1.97 |
| Fair Under 3.5 odds | 2.03 |
| Fair Over 4.5 odds | 3.14 |
| Fair Under 4.5 odds | 1.47 |
| Goal margin distribution | {"-1": 0.22039266394032386, "-10": 7.446176314188662e-05, "-11": 1.619857388969317e-05, "-12": 3.241036274217318e-06, "-13": 6.001757280751257e-07, "-14": 1.0342200539260929e-07, "-15": 1.666198719801201e-08, "-16": 2.518621345064255e-09, "-17": 3.5494848860743347e-10, "-18": 4.130064834026844e-11, "-2": 0.19859256626757998, "-3": 0.13257928294917784, "-4": 0.07124255929794829, "-5": 0.03185418433075702, "-6": 0.012156979762889182, "-7": 0.004039529135850133, "-8": 0.001187156328368222, "-9": 0.00031251251880992745, "0": 0.17038798870111607, "1": 0.09294556071703092, "10": 7.098625014494758e-08, "11": 7.812248376562314e-09, "12": 7.907541765959525e-10, "13": 7.407887395372856e-11, "14": 6.457839399904635e-12, "15": 5.263315740347668e-13, "16": 4.024888449497446e-14, "17": 2.86955558322662e-15, "18": 1.6891356226162422e-16, "2": 0.044130330059417584, "3": 0.014904183708866871, "4": 0.004051635644933952, "5": 0.0009164646143748566, "6": 0.00017694294343374093, "7": 2.974381286933979e-05, "8": 4.422136547220392e-06, "9": 5.889114489301372e-07} |
| Raw goal margin distribution | {"-1": 0.20680929424296704, "-10": 6.987249216076566e-05, "-11": 1.5200213899937645e-05, "-12": 3.041282829033867e-06, "-13": 5.631853462172605e-07, "-14": 9.704783980572643e-08, "-15": 1.5635065847923396e-08, "-16": 2.3633921997469426e-09, "-17": 3.3307209554573726e-10, "-18": 3.8755182601452834e-11, "-2": 0.18635279295330207, "-3": 0.12440807896120483, "-4": 0.0668516961728856, "-5": 0.029890928592400938, "-6": 0.011407713668590676, "-7": 0.0037905625111245723, "-8": 0.0011139888144933103, "-9": 0.0002932515642837965, "0": 0.19914612627931016, "1": 0.10044864095262315, "10": 7.671665325782877e-08, "11": 8.442896316469591e-09, "12": 8.545882315831742e-10, "13": 8.005893078214795e-11, "14": 6.979151948801603e-12, "15": 5.688199726203789e-13, "16": 4.34979972813105e-14, "17": 3.101201996625424e-15, "18": 1.8254920016354765e-16, "2": 0.04769277462056279, "3": 0.016107331931879784, "4": 0.00437870610526369, "5": 0.0009904467118702959, "6": 0.00019122675743694104, "7": 3.2144898114825906e-05, "8": 4.77911589158686e-06, "9": 6.364516414782688e-07} |
| Unadjusted home-win probability | 17.0% |
| Unadjusted draw probability | 19.9% |
| Unadjusted away-win probability | 63.1% |
| Raw p over 1 5 | 89.1% |
| Raw p under 3 5 | 49.7% |
| Raw p btts yes | 65.7% |
| P home draw | 32.8% |
| P draw away | 84.3% |
| P home away | 83.0% |
| Raw p home draw | 36.9% |
| Raw p draw away | 83.0% |
| Raw p home away | 80.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.98, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.94, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.98, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.96, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 5.60 |
| Reference draw odds | 5.70 |
| Reference away odds | 1.35 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.25 |
| Reference Under 2.5 odds | 3.90 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +1.3% |
| Draw probability edge | +2.9% |
| Away probability edge | -4.1% |
| Over 2.5 probability edge | -5.6% |
| Under 2.5 probability edge | +5.6% |
| Raw edge prob home | 0.0254 |
| Raw ev home | 0.1142 |
| Raw edge prob draw | 0.0575 |
| Raw ev draw | 0.1929 |
| Raw edge prob away | -0.0829 |
| Raw ev away | -0.1229 |

</details>


---

## 2026-10-25 — TSG Hoffenheim vs Bayer Leverkusen

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **46.9%**. Expected goals are 1.50 for TSG Hoffenheim and 2.16 for Bayer Leverkusen (3.66 combined). The most likely exact score is 1-1 at 9.3%. Goal-market probabilities: at least one goal: 96.5%; Over 2.5 goals: 70.6%; Under 3.5 goals: 50.6%; Double Chance 1X: 53.1%; Double Chance X2: 69.6%; Double Chance 12 (either team wins): 77.3%; Under 4.5 goals: 69.7%; BTTS Yes (both teams score): 69.9%; BTTS No (at least one team does not score): 30.1%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| TSG Hoffenheim win | 30.4% | 3.29 |
| Draw | 22.7% | 4.41 |
| Bayer Leverkusen win | 46.9% | 2.13 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| TSG Hoffenheim expected goals | 1.50 |
| Bayer Leverkusen expected goals | 2.16 |
| Expected total goals | 3.66 |
| Over 0.5 | 96.5% |
| Under 0.5 | 3.5% |
| Over 1.5 | 88.8% |
| Under 1.5 | 11.2% |
| Over 2.5 | 70.6% |
| Under 2.5 | 29.4% |
| Over 3.5 | 49.4% |
| Under 3.5 | 50.6% |
| Over 4.5 | 30.3% |
| Under 4.5 | 69.7% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 9.32% |
| 2 | 1-2 | 8.16% |
| 3 | 2-1 | 7.40% |
| 4 | 2-2 | 6.80% |
| 5 | 1-3 | 5.87% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| TSG Hoffenheim win | 30.4% | 35.1% | 2.79 | -15.2% |
| Draw | 22.7% | 22.8% | 4.04 | -8.5% |
| Bayer Leverkusen win | 46.9% | 42.1% | 2.34 | +9.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-25T14:30:00+00:00 |
| Fixture id | 2fd479cbb110c8f057e363bb06195f2b |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Hoffenheim |
| Matched away-team name | Leverkusen |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5009 |
| Dc lambda away | 2.1590 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 69.9% |
| P btts no | 30.1% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 28.39 |
| Fair Over 1.5 odds | 1.13 |
| Fair Under 1.5 odds | 8.94 |
| Fair Over 2.5 odds | 1.42 |
| Fair Under 2.5 odds | 3.40 |
| Fair Over 3.5 odds | 2.02 |
| Fair Under 3.5 odds | 1.98 |
| Fair Over 4.5 odds | 3.30 |
| Fair Under 4.5 odds | 1.43 |
| Goal margin distribution | {"-1": 0.18176187137598238, "-10": 1.893513218555157e-05, "-11": 3.629197658659433e-06, "-12": 6.39900323513099e-07, "-13": 1.044424347169247e-07, "-14": 1.586439084191408e-08, "-15": 2.25126976623698e-09, "-16": 2.9602412438237965e-10, "-17": 3.1576580739348035e-11, "-2": 0.14283932005219274, "-3": 0.08321114299539806, "-4": 0.039150644580207644, "-5": 0.015359453406691849, "-6": 0.005150428798226127, "-7": 0.0015050997431529309, "-8": 0.0003892679078536031, "-9": 9.022477598804587e-05, "0": 0.22660524709748503, "1": 0.1613737145636915, "10": 6.506522747531379e-07, "11": 8.669348549074678e-08, "12": 1.0626332537985888e-08, "13": 1.2057111882037534e-09, "14": 1.2731657152865878e-10, "15": 1.2559845700615005e-11, "16": 1.1480983718474412e-12, "17": 8.513582079654288e-14, "2": 0.0899842578523505, "3": 0.03644143608320117, "4": 0.011919228435841395, "5": 0.0032507249018574377, "6": 0.0007577798899903595, "7": 0.00015394309031074407, "8": 2.7678257831475857e-05, "9": 4.459756969676455e-06} |
| Raw goal margin distribution | {"-1": 0.20044198738608465, "-10": 2.0881142441800853e-05, "-11": 4.0021792569128725e-06, "-12": 7.056644586842237e-07, "-13": 1.1517624143953466e-07, "-14": 1.7494813433369186e-08, "-15": 2.482638315014474e-09, "-16": 3.2644725407063665e-10, "-17": 3.4821783855645414e-11, "-2": 0.15751926942320074, "-3": 0.0917629574805819, "-4": 0.043174252926073284, "-5": 0.016937982332020006, "-6": 0.005679751074258487, "-7": 0.0016597825575189531, "-8": 0.00042927393124380877, "-9": 9.94973988416907e-05, "0": 0.22516584974253367, "1": 0.13651815401367967, "10": 5.504356623026226e-07, "11": 7.334053526751597e-08, "12": 8.98961337008061e-09, "13": 1.0200017154730072e-09, "14": 1.0770665698212646e-10, "15": 1.0625317477387988e-11, "16": 9.71262703932261e-13, "17": 7.202278962845734e-14, "2": 0.0761244469429708, "3": 0.030828549724698846, "4": 0.010083371184259384, "5": 0.0027500325192844456, "6": 0.0006410629637538824, "7": 0.00013023203047166201, "8": 2.3415118600225397e-05, "9": 3.7728436164216423e-06} |
| Unadjusted home-win probability | 25.7% |
| Unadjusted draw probability | 22.5% |
| Unadjusted away-win probability | 51.8% |
| Raw p over 1 5 | 88.9% |
| Raw p under 3 5 | 50.3% |
| Raw p btts yes | 69.7% |
| P home draw | 53.1% |
| P draw away | 69.6% |
| P home away | 77.3% |
| Raw p home draw | 48.2% |
| Raw p draw away | 74.3% |
| Raw p home away | 77.5% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.85, "price": 2.07, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.11, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.84, "price": 2.11, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.85, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.85 |
| Reference away odds | 2.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.36 |
| Reference Under 2.5 odds | 3.00 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -4.7% |
| Draw probability edge | -0.1% |
| Away probability edge | +4.8% |
| Over 2.5 probability edge | -0.2% |
| Under 2.5 probability edge | +0.2% |
| Raw edge prob home | -0.0936 |
| Raw ev home | -0.2827 |
| Raw edge prob draw | -0.0029 |
| Raw ev draw | -0.0903 |
| Raw edge prob away | 0.0965 |
| Raw ev away | 0.2115 |

</details>


---

## 2026-10-30 — Elversberg vs FSV Mainz 05

The model's most likely 1X2 outcome is **FSV Mainz 05 win** at **38.8%**. Expected goals are 1.91 for Elversberg and 1.56 for FSV Mainz 05 (3.47 combined). The most likely exact score is 1-1 at 10.0%. Goal-market probabilities: at least one goal: 96.0%; Over 2.5 goals: 67.5%; Under 3.5 goals: 54.5%; Double Chance 1X: 61.2%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 73.1%; BTTS Yes (both teams score): 68.4%; BTTS No (at least one team does not score): 31.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Elversberg win | 37.7% | 2.65 |
| Draw | 23.5% | 4.25 |
| FSV Mainz 05 win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Elversberg expected goals | 1.91 |
| FSV Mainz 05 expected goals | 1.56 |
| Expected total goals | 3.47 |
| Over 0.5 | 96.0% |
| Under 0.5 | 4.0% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 67.5% |
| Under 2.5 | 32.5% |
| Over 3.5 | 45.5% |
| Under 3.5 | 54.5% |
| Over 4.5 | 26.9% |
| Under 4.5 | 73.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.05% |
| 2 | 1-2 | 9.12% |
| 3 | 2-1 | 7.39% |
| 4 | 2-2 | 6.74% |
| 5 | 0-1 | 4.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Elversberg win | 37.7% | 30.2% | 3.38 | +27.4% |
| Draw | 23.5% | 22.9% | 3.74 | -12.0% |
| FSV Mainz 05 win | 38.8% | 46.9% | 2.05 | -20.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-30T19:30:00+00:00 |
| Fixture id | b275fe870ec88a9f0054c9220beb2673 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 7.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Elversberg |
| Matched away-team name | Mainz |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9119 |
| Dc lambda away | 1.5583 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 68.4% |
| P btts no | 31.6% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.75 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.71 |
| Fair Over 2.5 odds | 1.48 |
| Fair Under 2.5 odds | 3.07 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.83 |
| Fair Over 4.5 odds | 3.72 |
| Fair Under 4.5 odds | 1.37 |
| Goal margin distribution | {"-1": 0.1978426453606417, "-10": 1.1952117316318022e-06, "-11": 1.6564869195974018e-07, "-12": 2.1114046526916764e-08, "-13": 2.4906081050834142e-09, "-14": 2.7315201162493613e-10, "-15": 2.765635271726837e-11, "-16": 2.270732969893602e-12, "-2": 0.11672008661424954, "-3": 0.049756662966965605, "-4": 0.017059065523891286, "-5": 0.0048641199394682385, "-6": 0.001183433100575995, "-7": 0.000250629689496726, "-8": 4.693807166147339e-05, "-9": 7.873186306777857e-06, "0": 0.23521052552738414, "1": 0.16228050304182753, "10": 6.102199379697027e-06, "11": 1.0376374477615877e-06, "12": 1.6227259454537113e-07, "13": 2.348524973915592e-08, "14": 3.1601687110189427e-09, "15": 3.9256976755344493e-10, "16": 3.954613923011289e-11, "2": 0.11605357099008927, "3": 0.060698817828974766, "4": 0.025532909401057343, "5": 0.008932343626486972, "6": 0.0026663732209074374, "7": 0.0006928286246999997, "8": 0.00015919690860088172, "9": 3.276242160066788e-05} |
| Raw goal margin distribution | {"-1": 0.15663017504242013, "-10": 9.462379680426856e-07, "-11": 1.3114252273520995e-07, "-12": 1.671579349000497e-08, "-13": 1.971791181573494e-09, "-14": 2.162518971378161e-10, "-15": 2.189527621430813e-11, "-16": 1.7977180900543326e-12, "-2": 0.09240620273768993, "-3": 0.039391885484730396, "-4": 0.013505502891940004, "-5": 0.003850878338982219, "-6": 0.000936912935814835, "-7": 0.0001984211850035701, "-8": 3.716043306582681e-05, "-9": 6.233128085829398e-06, "0": 0.2410949259636166, "1": 0.19450963584004666, "10": 7.314104633150515e-06, "11": 1.2437136828820426e-06, "12": 1.945001567052341e-07, "13": 2.8149452884049456e-08, "14": 3.787782596501876e-09, "15": 4.705346674267521e-10, "16": 4.7400057285664285e-11, "2": 0.1391019710199011, "3": 0.072753687168397, "4": 0.030603780592524346, "5": 0.010706319449467842, "6": 0.003195918637734815, "7": 0.0008304253497120518, "8": 0.00019081363526977376, "9": 3.9269083933893526e-05} |
| Unadjusted home-win probability | 45.2% |
| Unadjusted draw probability | 24.1% |
| Unadjusted away-win probability | 30.7% |
| Raw p over 1 5 | 87.1% |
| Raw p under 3 5 | 54.3% |
| Raw p btts yes | 68.3% |
| P home draw | 61.2% |
| P draw away | 62.3% |
| P home away | 76.5% |
| Raw p home draw | 69.3% |
| Raw p draw away | 54.8% |
| Raw p home away | 75.9% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 2.07, "price": 1.8, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.52, "price": 1.62, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.62, "price": 2.52, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.8, "price": 2.07, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.80 |
| Reference draw odds | 3.55 |
| Reference away odds | 1.92 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / LeoVegas (SE) |
| Reference Over 2.5 odds | 1.60 |
| Reference Under 2.5 odds | 2.35 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:06Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:06Z |
| Home probability edge | +7.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -8.1% |
| Over 2.5 probability edge | +7.2% |
| Under 2.5 probability edge | -7.2% |
| Raw edge prob home | 0.1498 |
| Raw ev home | 0.5276 |
| Raw edge prob draw | 0.0118 |
| Raw ev draw | -0.0983 |
| Raw edge prob away | -0.1615 |
| Raw ev away | -0.3707 |

</details>


---

## 2026-10-31 — Augsburg vs SC Freiburg

The model's most likely 1X2 outcome is **SC Freiburg win** at **41.2%**. Expected goals are 1.36 for Augsburg and 1.43 for SC Freiburg (2.80 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.2%; Over 2.5 goals: 53.9%; Under 3.5 goals: 69.1%; Double Chance 1X: 58.8%; Double Chance X2: 66.6%; Double Chance 12 (either team wins): 74.5%; Under 4.5 goals: 84.4%; BTTS Yes (both teams score): 57.5%; BTTS No (at least one team does not score): 42.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Augsburg win | 33.4% | 3.00 |
| Draw | 25.5% | 3.93 |
| SC Freiburg win | 41.2% | 2.43 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Augsburg expected goals | 1.36 |
| SC Freiburg expected goals | 1.43 |
| Expected total goals | 2.80 |
| Over 0.5 | 93.2% |
| Under 0.5 | 6.8% |
| Over 1.5 | 78.4% |
| Under 1.5 | 21.6% |
| Over 2.5 | 53.9% |
| Under 2.5 | 46.1% |
| Over 3.5 | 30.9% |
| Under 3.5 | 69.1% |
| Over 4.5 | 15.6% |
| Under 4.5 | 84.4% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.07% |
| 2 | 1-2 | 9.35% |
| 3 | 0-1 | 8.11% |
| 4 | 2-1 | 7.87% |
| 5 | 0-2 | 6.86% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Augsburg win | 33.4% | 32.3% | 3.06 | +2.1% |
| Draw | 25.5% | 23.0% | 3.81 | -3.0% |
| SC Freiburg win | 41.2% | 44.7% | 2.17 | -10.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 24400b6372faf9f4996cd5704d707374 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Augsburg |
| Matched away-team name | Freiburg |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.3643 |
| Dc lambda away | 1.4339 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 14 |
| Score grid omitted mass | 0 |
| P btts yes | 57.5% |
| P btts no | 42.5% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 14.79 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.62 |
| Fair Over 2.5 odds | 1.85 |
| Fair Under 2.5 odds | 2.17 |
| Fair Over 3.5 odds | 3.23 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.43 |
| Fair Under 4.5 odds | 1.18 |
| Goal margin distribution | {"-1": 0.21063967503065797, "-10": 8.056186628694272e-07, "-11": 1.0349915243105974e-07, "-12": 1.2210933112041776e-08, "-13": 1.3221977501024986e-09, "-14": 1.1881870509079908e-10, "-2": 0.12573943884149177, "-3": 0.05229313321187235, "-4": 0.017165398407845284, "-5": 0.004633565491906354, "-6": 0.0010596137763864625, "-7": 0.00020991119227819848, "-8": 3.664896801916085e-05, "-9": 5.716863360153348e-06, "0": 0.2545456763305242, "1": 0.1766557628372902, "10": 4.33157603541066e-07, "11": 5.2945743646806955e-08, "12": 5.943208232990854e-09, "13": 6.122747418649478e-10, "14": 5.23495051246922e-11, "2": 0.10068511219073958, "3": 0.03983971654932, "4": 0.01244237536620163, "5": 0.00319552745016784, "6": 0.000695268699551096, "7": 0.0001310444139598391, "8": 2.176819920236799e-05, "9": 3.2306982809195105e-06} |
| Raw goal margin distribution | {"-1": 0.19243131761685334, "-10": 7.359784464637434e-07, "-11": 9.455235948136359e-08, "-12": 1.115538156683664e-08, "-13": 1.207902809217831e-09, "-14": 1.0854764172429973e-10, "-2": 0.11487012543648448, "-3": 0.04777274995705161, "-4": 0.015681567266751333, "-5": 0.004233025486493686, "-6": 0.000968017421814477, "-7": 0.00019176580720958305, "-8": 3.348091571162264e-05, "-9": 5.222679672619623e-06, "0": 0.27921205471464733, "1": 0.18244220702175465, "10": 4.4734588846146964e-07, "11": 5.468000685733913e-08, "12": 6.137880867296738e-09, "13": 6.323300945036389e-10, "14": 5.4064238256649906e-11, "2": 0.10398310129984589, "3": 0.04114468556043487, "4": 0.012849931335066305, "5": 0.003300198483443732, "6": 0.0007180425590535628, "7": 0.0001353368365498843, "8": 2.2481227000939273e-05, "9": 3.3365213516143752e-06} |
| Unadjusted home-win probability | 34.5% |
| Unadjusted draw probability | 27.9% |
| Unadjusted away-win probability | 37.6% |
| Raw p over 1 5 | 78.2% |
| Raw p under 3 5 | 69.2% |
| Raw p btts yes | 58.0% |
| P home draw | 58.8% |
| P draw away | 66.6% |
| P home away | 74.5% |
| Raw p home draw | 62.4% |
| Raw p draw away | 65.5% |
| Raw p home away | 72.1% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.94, "price": 1.91, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.91, "price": 1.94, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.65 |
| Reference draw odds | 3.55 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +1.1% |
| Draw probability edge | +2.5% |
| Away probability edge | -3.6% |
| Over 2.5 probability edge | -12.3% |
| Under 2.5 probability edge | +12.3% |
| Raw edge prob home | 0.0219 |
| Raw ev home | 0.0545 |
| Raw edge prob draw | 0.0493 |
| Raw ev draw | 0.0638 |
| Raw edge prob away | -0.0712 |
| Raw ev away | -0.1837 |

</details>


---

## 2026-10-31 — Bayer Leverkusen vs VfB Stuttgart

The model's most likely 1X2 outcome is **Bayer Leverkusen win** at **57.8%**. Expected goals are 2.29 for Bayer Leverkusen and 1.23 for VfB Stuttgart (3.51 combined). The most likely exact score is 2-1 at 9.2%. Goal-market probabilities: at least one goal: 96.2%; Over 2.5 goals: 68.3%; Under 3.5 goals: 53.6%; Double Chance 1X: 78.4%; Double Chance X2: 42.2%; Double Chance 12 (either team wins): 79.4%; Under 4.5 goals: 72.3%; BTTS Yes (both teams score): 64.5%; BTTS No (at least one team does not score): 35.5%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Bayer Leverkusen win | 57.8% | 1.73 |
| Draw | 20.6% | 4.85 |
| VfB Stuttgart win | 21.6% | 4.63 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Bayer Leverkusen expected goals | 2.29 |
| VfB Stuttgart expected goals | 1.23 |
| Expected total goals | 3.51 |
| Over 0.5 | 96.2% |
| Under 0.5 | 3.8% |
| Over 1.5 | 87.4% |
| Under 1.5 | 12.6% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 46.4% |
| Under 3.5 | 53.6% |
| Over 4.5 | 27.7% |
| Under 4.5 | 72.3% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 9.16% |
| 2 | 1-1 | 9.02% |
| 3 | 2-0 | 7.47% |
| 4 | 3-1 | 6.98% |
| 5 | 1-2 | 5.98% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Bayer Leverkusen win | 57.8% | 55.3% | 1.79 | +3.4% |
| Draw | 20.6% | 20.0% | 4.35 | -10.3% |
| VfB Stuttgart win | 21.6% | 24.7% | 3.79 | -18.2% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | a7ba9b844f121a4a8777d87b1f863137 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Leverkusen |
| Matched away-team name | Stuttgart |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2881 |
| Dc lambda away | 1.2252 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 18 |
| Score grid omitted mass | 0 |
| P btts yes | 64.5% |
| P btts no | 35.5% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 26.33 |
| Fair Over 1.5 odds | 1.14 |
| Fair Under 1.5 odds | 7.92 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.15 |
| Fair Over 3.5 odds | 2.16 |
| Fair Under 3.5 odds | 1.86 |
| Fair Over 4.5 odds | 3.62 |
| Fair Under 4.5 odds | 1.38 |
| Goal margin distribution | {"-1": 0.1271836651432902, "-10": 9.42073960764816e-08, "-11": 1.027871534018342e-08, "-12": 1.0312252360177789e-09, "-13": 9.573565834171824e-11, "-14": 8.26928129363176e-12, "-15": 6.677132438940678e-13, "-16": 5.058737998123583e-14, "-17": 3.577826098148249e-15, "-18": 2.1071787742397031e-16, "-2": 0.060963695679262304, "-3": 0.020628939185958657, "-4": 0.005597537761080787, "-5": 0.001260878914846107, "-6": 0.00024206340157036124, "-7": 4.041918755243839e-05, "-8": 5.964930642815118e-06, "-9": 7.880930429661965e-07, "0": 0.20627511212279742, "1": 0.20231078217107532, "10": 3.981517006768889e-05, "11": 8.11247801572448e-06, "12": 1.5199151552196484e-06, "13": 2.635060918821412e-07, "14": 4.2504588511177935e-08, "15": 6.4092787467460436e-09, "16": 9.068020127665663e-10, "17": 1.197679552057147e-10, "18": 1.317267294248145e-11, "2": 0.1741910795784167, "3": 0.11007346522481606, "4": 0.05577683846896584, "5": 0.023462882361654735, "6": 0.008411786312488649, "7": 0.0026229970268857945, "8": 0.0007228808763860117, "9": 0.00017835691426290574} |
| Raw goal margin distribution | {"-1": 0.10876303798888105, "-10": 8.056288192949983e-08, "-11": 8.789999138346446e-09, "-12": 8.818678829056506e-10, "-13": 8.186979855769763e-11, "-14": 7.071601171948643e-12, "-15": 5.710050958942727e-13, "-16": 4.326056435359289e-14, "-17": 3.0596321893388805e-15, "-18": 1.8019858510429758e-16, "-2": 0.05213402791652445, "-3": 0.01764114985855247, "-4": 0.0047868192150833325, "-5": 0.0010782597054447378, "-6": 0.0002070041849403639, "-7": 3.4565080557261245e-05, "-8": 5.101000803637935e-06, "-9": 6.739497047386936e-07, "0": 0.21226810114483338, "1": 0.21116242278408984, "10": 4.1557190797395815e-05, "11": 8.467420738527325e-06, "12": 1.5864155294058447e-06, "13": 2.750351918127044e-07, "14": 4.436427852802967e-08, "15": 6.689701922644077e-09, "16": 9.464770386748764e-10, "17": 1.2500812523056363e-10, "18": 1.374901279717604e-11, "2": 0.18181240760589346, "3": 0.11488947525029915, "4": 0.058217225102635016, "5": 0.024489446542673942, "6": 0.00877982457793642, "7": 0.002737760198486631, "8": 0.0007545088581234319, "9": 0.00018616050875727372} |
| Unadjusted home-win probability | 60.3% |
| Unadjusted draw probability | 21.2% |
| Unadjusted away-win probability | 18.5% |
| Raw p over 1 5 | 87.5% |
| Raw p under 3 5 | 53.4% |
| Raw p btts yes | 64.4% |
| P home draw | 78.4% |
| P draw away | 42.2% |
| P home away | 79.4% |
| Raw p home draw | 81.5% |
| Raw p draw away | 39.7% |
| Raw p home away | 78.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.75, "market_key": "spreads", "opposite_price": 1.99, "price": 1.87, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.82, "price": 1.51, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.51, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.75, "market_key": "spreads", "opposite_price": 1.87, "price": 1.99, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.66 |
| Reference draw odds | 3.95 |
| Reference away odds | 3.30 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.30 |
| Reference Under 2.5 odds | 3.30 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +2.5% |
| Draw probability edge | +0.6% |
| Away probability edge | -3.1% |
| Over 2.5 probability edge | -6.0% |
| Under 2.5 probability edge | +6.0% |
| Raw edge prob home | 0.0506 |
| Raw ev home | 0.0795 |
| Raw edge prob draw | 0.0120 |
| Raw ev draw | -0.0766 |
| Raw edge prob away | -0.0625 |
| Raw ev away | -0.3002 |

</details>


---

## 2026-10-31 — Borussia Monchengladbach vs SC Paderborn

The model's most likely 1X2 outcome is **Borussia Monchengladbach win** at **52.6%**. Expected goals are 1.55 for Borussia Monchengladbach and 0.85 for SC Paderborn (2.40 combined). The most likely exact score is 1-0 at 12.7%. Goal-market probabilities: at least one goal: 90.8%; Over 2.5 goals: 44.2%; Under 3.5 goals: 77.7%; Double Chance 1X: 77.5%; Double Chance X2: 47.4%; Double Chance 12 (either team wins): 75.0%; Under 4.5 goals: 90.1%; BTTS Yes (both teams score): 45.8%; BTTS No (at least one team does not score): 54.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Borussia Monchengladbach win | 52.6% | 1.90 |
| Draw | 25.0% | 4.00 |
| SC Paderborn win | 22.5% | 4.45 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Borussia Monchengladbach expected goals | 1.55 |
| SC Paderborn expected goals | 0.85 |
| Expected total goals | 2.40 |
| Over 0.5 | 90.8% |
| Under 0.5 | 9.2% |
| Over 1.5 | 70.7% |
| Under 1.5 | 29.3% |
| Over 2.5 | 44.2% |
| Under 2.5 | 55.8% |
| Over 3.5 | 22.3% |
| Under 3.5 | 77.7% |
| Over 4.5 | 9.9% |
| Under 4.5 | 90.1% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-0 | 12.71% |
| 2 | 1-1 | 11.75% |
| 3 | 2-0 | 10.91% |
| 4 | 2-1 | 9.25% |
| 5 | 0-0 | 9.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Borussia Monchengladbach win | 52.6% | 52.4% | 1.85 | -2.8% |
| Draw | 25.0% | 21.8% | 4.11 | +2.7% |
| SC Paderborn win | 22.5% | 25.8% | 3.74 | -16.0% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | aecb9d8c01176616c87d893bee4bc0de |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | M'gladbach |
| Matched away-team name | Paderborn |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5549 |
| Dc lambda away | 0.8482 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 15 |
| Score grid omitted mass | 0 |
| P btts yes | 45.8% |
| P btts no | 54.2% |
| Fair Over 0.5 odds | 1.10 |
| Fair Under 0.5 odds | 10.88 |
| Fair Over 1.5 odds | 1.42 |
| Fair Under 1.5 odds | 3.41 |
| Fair Over 2.5 odds | 2.26 |
| Fair Under 2.5 odds | 1.79 |
| Fair Over 3.5 odds | 4.49 |
| Fair Under 3.5 odds | 1.29 |
| Fair Over 4.5 odds | 10.12 |
| Fair Under 4.5 odds | 1.11 |
| Goal margin distribution | {"-1": 0.1483579896813156, "-10": 6.351106827676667e-09, "-11": 4.849398905530066e-10, "-12": 3.39929214488226e-11, "-13": 2.201897847563769e-12, "-14": 1.3214225432690307e-13, "-15": 6.86853901201193e-15, "-2": 0.05796628143000084, "-3": 0.014854102419904407, "-4": 0.0029625493481754126, "-5": 0.00048202399772130964, "-6": 6.611525428620636e-05, "-7": 7.830407617206913e-06, "-8": 8.155221124682096e-07, "-9": 7.576382932478231e-08, "0": 0.2497637942443235, "1": 0.24236513030280402, "10": 2.314370319081458e-06, "11": 3.239309591532318e-07, "12": 4.162307400180053e-08, "13": 4.9422412476089266e-09, "14": 5.436878142296972e-10, "15": 5.1802816231281614e-11, "2": 0.16569521443665458, "3": 0.0778326920764399, "4": 0.028455246024536848, "5": 0.008486849983109501, "6": 0.002133834101440091, "7": 0.00046325963703459466, "8": 8.84416725842661e-05, "9": 1.5061361645346294e-05} |
| Raw goal margin distribution | {"-1": 0.12647121789213275, "-10": 5.414148689832696e-09, "-11": 4.1339828542069005e-10, "-12": 2.8978056285199408e-11, "-13": 1.877059018214286e-12, "-14": 1.1264773724444807e-13, "-15": 5.855245786591948e-15, "-2": 0.04941470442460173, "-3": 0.01266272499226499, "-4": 0.0025254940764169427, "-5": 0.0004109125647765925, "-6": 5.6361485814050824e-05, "-7": 6.67521304425382e-06, "-8": 6.952107871195352e-07, "-9": 6.458663795229131e-08, "0": 0.2818122488559172, "1": 0.2428726439646323, "10": 2.319216620832854e-06, "11": 3.2460927202379215e-07, "12": 4.1710232904060164e-08, "13": 4.952590322783557e-09, "14": 5.44826298933113e-10, "15": 5.191129155908851e-11, "2": 0.1660421809533358, "3": 0.07799567408014779, "4": 0.028514831436390838, "5": 0.008504621484756354, "6": 0.0021383023595480245, "7": 0.0004642297047769095, "8": 8.862686984038699e-05, "9": 1.5092900203682636e-05} |
| Unadjusted home-win probability | 52.7% |
| Unadjusted draw probability | 28.2% |
| Unadjusted away-win probability | 19.2% |
| Raw p over 1 5 | 70.5% |
| Raw p under 3 5 | 77.8% |
| Raw p btts yes | 46.4% |
| P home draw | 77.5% |
| P draw away | 47.4% |
| P home away | 75.0% |
| Raw p home draw | 80.8% |
| Raw p draw away | 47.3% |
| Raw p home away | 71.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.46, "price": 3.02, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.85, "price": 2.01, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 2.01, "price": 1.85, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 3.02, "price": 1.46, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 1.74 |
| Reference draw odds | 3.70 |
| Reference away odds | 3.20 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.44 |
| Reference Under 2.5 odds | 2.62 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +0.1% |
| Draw probability edge | +3.2% |
| Away probability edge | -3.3% |
| Over 2.5 probability edge | -22.1% |
| Under 2.5 probability edge | +22.1% |
| Raw edge prob home | 0.0022 |
| Raw ev home | -0.0257 |
| Raw edge prob draw | 0.0641 |
| Raw ev draw | 0.1582 |
| Raw edge prob away | -0.0663 |
| Raw ev away | -0.2836 |

</details>


---

## 2026-10-31 — FC Schalke 04 vs RB Leipzig

The model's most likely 1X2 outcome is **RB Leipzig win** at **57.3%**. Expected goals are 0.91 for FC Schalke 04 and 2.08 for RB Leipzig (3.00 combined). The most likely exact score is 1-1 at 10.6%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 57.2%; Under 3.5 goals: 65.6%; Double Chance 1X: 42.7%; Double Chance X2: 79.6%; Double Chance 12 (either team wins): 77.8%; Under 4.5 goals: 82.0%; BTTS Yes (both teams score): 54.0%; BTTS No (at least one team does not score): 46.0%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| FC Schalke 04 win | 20.4% | 4.89 |
| Draw | 22.2% | 4.49 |
| RB Leipzig win | 57.3% | 1.75 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| FC Schalke 04 expected goals | 0.91 |
| RB Leipzig expected goals | 2.08 |
| Expected total goals | 3.00 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 80.5% |
| Under 1.5 | 19.5% |
| Over 2.5 | 57.2% |
| Under 2.5 | 42.8% |
| Over 3.5 | 34.4% |
| Under 3.5 | 65.6% |
| Over 4.5 | 18.0% |
| Under 4.5 | 82.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.58% |
| 2 | 0-2 | 9.82% |
| 3 | 1-2 | 8.95% |
| 4 | 0-1 | 8.47% |
| 5 | 0-3 | 6.82% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| FC Schalke 04 win | 20.4% | 26.4% | 4.04 | -17.4% |
| Draw | 22.2% | 22.3% | 3.68 | -18.1% |
| RB Leipzig win | 57.3% | 51.3% | 1.88 | +7.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 3966f2fe1c2f73bfa12e61db83bd0bf9 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Schalke 04 |
| Matched away-team name | RB Leipzig |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 0.9120 |
| Dc lambda away | 2.0841 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 17 |
| Score grid omitted mass | 0 |
| P btts yes | 54.0% |
| P btts no | 46.0% |
| Fair Over 0.5 odds | 1.06 |
| Fair Under 0.5 odds | 16.48 |
| Fair Over 1.5 odds | 1.24 |
| Fair Under 1.5 odds | 5.13 |
| Fair Over 2.5 odds | 1.75 |
| Fair Under 2.5 odds | 2.33 |
| Fair Over 3.5 odds | 2.91 |
| Fair Under 3.5 odds | 1.52 |
| Fair Over 4.5 odds | 5.56 |
| Fair Under 4.5 odds | 1.22 |
| Goal margin distribution | {"-1": 0.20752513356680177, "-10": 2.2860549208731964e-05, "-11": 4.27040740695903e-06, "-12": 7.328126152993437e-07, "-13": 1.1627550343171721e-07, "-14": 1.7154791077276834e-08, "-15": 2.364356585684661e-09, "-16": 3.042373170803327e-10, "-17": 3.354640891472977e-11, "-2": 0.17719053905816962, "-3": 0.10746971149635234, "-4": 0.05138916849493785, "-5": 0.02019393841456896, "-6": 0.0067198752748478295, "-7": 0.001936590763616745, "-8": 0.0004917789891910822, "-9": 0.00011156101955462619, "0": 0.22248088367518185, "1": 0.1337228643022314, "10": 9.214098062604436e-09, "11": 7.532170593619795e-10, "12": 5.6562479965968775e-11, "13": 3.927429536402114e-12, "14": 2.5356556486521024e-13, "15": 1.529334497518938e-14, "16": 8.611655721840829e-16, "17": 4.1553238900246276e-17, "2": 0.05310425954457556, "3": 0.01409482146091478, "4": 0.0029493733680323775, "5": 0.0005071820315513283, "6": 7.385649806939038e-05, "7": 9.314295739743139e-06, "8": 1.0350630485511604e-06, "9": 1.0275287379418289e-07} |
| Raw goal margin distribution | {"-1": 0.22943730102165957, "-10": 2.5274349280859165e-05, "-11": 4.721311259391103e-06, "-12": 8.10188846618827e-07, "-13": 1.2855280333415789e-07, "-14": 1.8966131459416087e-08, "-15": 2.614004310459363e-09, "-16": 3.3636113226985524e-10, "-17": 3.708850772953224e-11, "-2": 0.1958997368142541, "-3": 0.11881722528496676, "-4": 0.056815248922273215, "-5": 0.022326176339237894, "-6": 0.007429413583617672, "-7": 0.002141071543243572, "-8": 0.0005437049577555933, "-9": 0.0001233405264504921, "0": 0.22199559330700885, "1": 0.0944668645264177, "10": 6.509185680063662e-09, "11": 5.321008810050406e-10, "12": 3.99578647982507e-11, "13": 2.7744840486950216e-12, "14": 1.7912825895314515e-13, "15": 1.080379451536231e-14, "16": 6.083597735273102e-16, "17": 2.935477197789827e-17, "2": 0.037514847728919255, "3": 0.009957112393755858, "4": 0.0020835483583871274, "5": 0.00035829247686846883, "6": 5.2175010114559046e-05, "7": 6.579969090526147e-06, "8": 7.312074961450834e-07, "9": 7.258849755473862e-08} |
| Unadjusted home-win probability | 14.4% |
| Unadjusted draw probability | 22.2% |
| Unadjusted away-win probability | 63.4% |
| Raw p over 1 5 | 81.1% |
| Raw p under 3 5 | 64.8% |
| Raw p btts yes | 53.4% |
| P home draw | 42.7% |
| P draw away | 79.6% |
| P home away | 77.8% |
| Raw p home draw | 36.6% |
| Raw p draw away | 85.6% |
| Raw p home away | 77.8% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.5, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.86, "price": 1.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.5, "price": 2.86, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.5, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 3.15 |
| Reference draw odds | 3.65 |
| Reference away odds | 1.78 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | -6.0% |
| Draw probability edge | -0.0% |
| Away probability edge | +6.1% |
| Over 2.5 probability edge | -11.4% |
| Under 2.5 probability edge | +11.4% |
| Raw edge prob home | -0.1200 |
| Raw ev home | -0.4165 |
| Raw edge prob draw | -0.0010 |
| Raw ev draw | -0.1831 |
| Raw edge prob away | 0.1210 |
| Raw ev away | 0.1911 |

</details>


---

## 2026-10-31 — Werder Bremen vs TSG Hoffenheim

The model's most likely 1X2 outcome is **TSG Hoffenheim win** at **38.8%**. Expected goals are 1.82 for Werder Bremen and 1.59 for TSG Hoffenheim (3.42 combined). The most likely exact score is 1-1 at 10.2%. Goal-market probabilities: at least one goal: 95.8%; Over 2.5 goals: 66.7%; Under 3.5 goals: 55.5%; Double Chance 1X: 61.2%; Double Chance X2: 62.3%; Double Chance 12 (either team wins): 76.5%; Under 4.5 goals: 74.0%; BTTS Yes (both teams score): 67.8%; BTTS No (at least one team does not score): 32.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Werder Bremen win | 37.7% | 2.65 |
| Draw | 23.5% | 4.25 |
| TSG Hoffenheim win | 38.8% | 2.58 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Werder Bremen expected goals | 1.82 |
| TSG Hoffenheim expected goals | 1.59 |
| Expected total goals | 3.42 |
| Over 0.5 | 95.8% |
| Under 0.5 | 4.2% |
| Over 1.5 | 86.6% |
| Under 1.5 | 13.4% |
| Over 2.5 | 66.7% |
| Under 2.5 | 33.3% |
| Over 3.5 | 44.5% |
| Under 3.5 | 55.5% |
| Over 4.5 | 26.0% |
| Under 4.5 | 74.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 10.15% |
| 2 | 1-2 | 8.94% |
| 3 | 2-1 | 7.71% |
| 4 | 2-2 | 6.64% |
| 5 | 0-1 | 4.91% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Werder Bremen win | 37.7% | 32.9% | 2.92 | +10.0% |
| Draw | 23.5% | 22.5% | 3.91 | -8.0% |
| TSG Hoffenheim win | 38.8% | 44.6% | 2.21 | -14.3% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-10-31T14:30:00+00:00 |
| Fixture id | 2fad25b09c01b71e47a5b0fd1d0b4e61 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-10-21T17:20:06Z |
| Market best draw last update utc | 2026-10-21T17:20:06Z |
| Market best away last update utc | 2026-10-21T17:20:06Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 3.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Werder Bremen |
| Matched away-team name | Hoffenheim |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8231 |
| Dc lambda away | 1.5937 |
| Bbs statistics applied | 0 |
| Bbs statistics status | INSUFFICIENT_RETROSPECTIVE_EXAMPLES |
| Bbs statistics version | bbs-lagged-poisson-v2 |
| Bbs statistics validation mode | retrospective_backfill |
| Bbs statistics cutoff utc | 2026-10-21T17:18:16.494074+00:00 |
| Bbs statistics weight | 0 |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 67.8% |
| P btts no | 32.2% |
| Fair Over 0.5 odds | 1.04 |
| Fair Under 0.5 odds | 24.04 |
| Fair Over 1.5 odds | 1.16 |
| Fair Under 1.5 odds | 7.44 |
| Fair Over 2.5 odds | 1.50 |
| Fair Under 2.5 odds | 3.00 |
| Fair Over 3.5 odds | 2.25 |
| Fair Under 3.5 odds | 1.80 |
| Fair Over 4.5 odds | 3.84 |
| Fair Under 4.5 odds | 1.35 |
| Goal margin distribution | {"-1": 0.19391706005644768, "-10": 1.4602387124605638e-06, "-11": 2.0708100764296908e-07, "-12": 2.7006193356597128e-08, "-13": 3.2592057305933157e-09, "-14": 3.657021917435193e-10, "-15": 3.790129026885856e-11, "-16": 3.19495596668074e-12, "-2": 0.11755131380313888, "-3": 0.051452306341291096, "-4": 0.018090320525820103, "-5": 0.005285712497320001, "-6": 0.001317157121746925, "-7": 0.0002856116330127848, "-8": 5.475397721202212e-05, "-9": 9.399684340547384e-06, "0": 0.23530826546793382, "1": 0.1685930310144829, "10": 4.22502355426272e-06, "11": 6.854164394073435e-07, "12": 1.0225547964542414e-07, "13": 1.4117050331659709e-08, "14": 1.8120439267432044e-09, "15": 2.1483454852552166e-10, "16": 2.07168621431683e-11, "2": 0.11597409725069135, "3": 0.058069398888581654, "4": 0.023355959629459105, "5": 0.007806636568908028, "6": 0.0022253943410479086, "7": 0.0005520192945045957, "8": 0.00012106065146384099, "9": 2.3774400559937107e-05} |
| Raw goal margin distribution | {"-1": 0.16481506209206787, "-10": 1.2410941770330688e-06, "-11": 1.7600343736043098e-07, "-12": 2.2953253487043834e-08, "-13": 2.7700821923671697e-09, "-14": 3.108196330011831e-10, "-15": 3.221327461963917e-11, "-16": 2.715474677042993e-12, "-2": 0.09990986392754103, "-3": 0.04373062928012366, "-4": 0.015375425451791314, "-5": 0.004492462051523605, "-6": 0.0011194854787017529, "-7": 0.00024274862157829964, "-8": 4.653680367967727e-05, "-9": 7.989031794222709e-06, "0": 0.24554945189089142, "1": 0.19006621503116033, "10": 4.763152014908796e-06, "11": 7.727158564881443e-07, "12": 1.1527945055292376e-07, "13": 1.591509629904246e-08, "14": 2.042838476500822e-09, "15": 2.4219737465106926e-10, "16": 2.335550616286195e-11, "2": 0.13074536695529862, "3": 0.06546552244463327, "4": 0.02633073750723736, "5": 0.008800944237420644, "6": 0.002508836081833086, "7": 0.0006223283210422073, "8": 0.0001364797801811994, "9": 2.6802473992378535e-05} |
| Unadjusted home-win probability | 42.5% |
| Unadjusted draw probability | 24.6% |
| Unadjusted away-win probability | 33.0% |
| Raw p over 1 5 | 86.6% |
| Raw p under 3 5 | 55.5% |
| Raw p btts yes | 67.9% |
| P home draw | 61.2% |
| P draw away | 62.3% |
| P home away | 76.5% |
| Raw p home draw | 67.0% |
| Raw p draw away | 57.5% |
| Raw p home away | 75.4% |
| Market blending weight | 50.0% |
| Market blend applied | Yes |
| Asian handicap offers | [{"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": -0.25, "market_key": "spreads", "opposite_price": 1.89, "price": 1.96, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": 0.0, "market_key": "spreads", "opposite_price": 2.32, "price": 1.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-10-21T17:19:22Z", "line": -0.0, "market_key": "spreads", "opposite_price": 1.71, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-10-21T17:20:06Z", "line": 0.25, "market_key": "spreads", "opposite_price": 1.96, "price": 1.89, "quote_source": "The Odds API", "side": "home"}] |
| 1X2 market source | The Odds API / Winamax (FR) |
| Reference home odds | 2.60 |
| Reference draw odds | 3.60 |
| Reference away odds | 2.00 |
| Market reference 1x2 last update utc | 2026-10-21T17:20:07Z |
| Market reference home last update utc | 2026-10-21T17:20:07Z |
| Market reference draw last update utc | 2026-10-21T17:20:07Z |
| Market reference away last update utc | 2026-10-21T17:20:07Z |
| O/U 2.5 market source | The Odds API / William Hill |
| Reference Over 2.5 odds | 1.40 |
| Reference Under 2.5 odds | 2.80 |
| Market reference over 2 5 last update utc | 2026-10-21T17:20:05Z |
| Market reference under 2 5 last update utc | 2026-10-21T17:20:05Z |
| Home probability edge | +4.8% |
| Draw probability edge | +1.0% |
| Away probability edge | -5.8% |
| Over 2.5 probability edge | -1.9% |
| Under 2.5 probability edge | +1.9% |
| Raw edge prob home | 0.0960 |
| Raw ev home | 0.2401 |
| Raw edge prob draw | 0.0205 |
| Raw ev draw | -0.0399 |
| Raw edge prob away | -0.1164 |
| Raw ev away | -0.2713 |

</details>


---
