# Super Lig — football model report

Fixtures in this report: **6**.

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
| Training as of utc | 2026-11-07T13:53:32.612675+00:00 |
| Training data provenance | {'bbs_confirmed_rows': 0, 'bbs_added_results': 0, 'bbs_result_conflicts': 0, 'bbs_rows_with_statistics': 0, 'bbs_statistics_used_as_predictor_features': False, 'note': 'Confirmed rows retain primary results; BBS-only verified additions extend score history. Statistics affect probabilities only after per-model validation and per-fixture coverage gates pass.'} |
| Bbs statistics model | {'status': 'NO_OBSERVATIONS'} |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Totals anchor enabled | 1 |
| Shot features model | {'version': 'football-data-lagged-shot-strength-v1', 'status': 'BASELINE_RETAINED_AUDIT_NOT_IMPROVED', 'cutoff_date': '2026-11-07', 'selected_weight': 0.0, 'feature_source': 'football-data.co.uk HST/AST (+HS/AS candidate)', 'lag_rule': 'matches dated strictly before the origin date', 'gates': {'min_form': 3, 'min_train': 60, 'min_tune': 20, 'min_audit': 40, 'min_audit_matchdays': 8, 'min_audit_gain': 0.01, 'bootstrap_lower95': '>0', 'market_brier_safety': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'max_goal_rate_ratio': 1.25}, 'bbs_shot_source_enabled': False, 'shot_matches': 1809, 'tune_start_date': '2025-11-08', 'audit_start_date': '2026-05-09', 'training_shot_matches': 1513, 'tuning_matches': 188, 'audit_matches': 94, 'audit_matchdays': 38, 'selected_shrinkage': 5.0, 'selected_component': 'shots_on_target', 'proposed_weight': 0.2, 'audit_baseline_poisson_score': 0.8406061330011584, 'audit_candidate_poisson_score': 0.832662940340293, 'audit_gain': 0.007943192660865406, 'audit_gain_lower95': 0.0007010941958230725, 'audit_baseline_briers': [0.604125448119081, 0.17290702296888374, 0.21645984578617375, 0.24465189323875286], 'audit_candidate_briers': [0.60048662707422, 0.17155931610656247, 0.21342015723215774, 0.2454632457185039], 'audit_brier_order': ['1x2', 'over_1_5', 'under_3_5', 'btts_yes'], 'failed_gates': ['audit_gain_below_minimum', 'market_brier_worse']} |
| Optimizer objective | 1667.217 |
| Base scoring parameter | 0.131 |
| Home-advantage parameter | 0.247 |
| Dixon-Coles low-score adjustment | -0.097 |
| Xi per day | 0.0014 |
| Elo ratings | {'version': 'venue-elo-v1', 'teams': 32, 'matches': 1840, 'k_factor': 20.0, 'home_advantage': 60.0, 'venue_weight': 0.5, 'season_regression': 0.2, 'last_match_date': '2026-11-02'} |
| Training data health | {'training_end': '2026-11-02', 'days_since_latest_result': 5, 'status': 'RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED'} |
| Training source | Football-Data.co.uk |
| Fixture provider mode | auto |
| Fixture sources | ['The Odds API'] |
| The odds api enabled | 1.00 |
| Odds regions | — |
| Live odds matched | 6.00 |
| Excluded started fixtures | [] |
| Excluded unresolved team fixtures | [] |
| Additional event odds calls used before this league | 55.00 |
| Over 1 5 in window quote fixtures | 5 |
| Odds provider health | — |
| Additional odds coverage mode | — |
| Additional odds coverage | — |
| Additional odds in window linked fixtures | 6.00 |
| Additional odds unrequested linked fixtures | 0.00 |
| Additional event odds hard cap applies | 0.00 |
| Additional event odds calls this league | 6.00 |
| Totals anchor fixtures | {'ANCHORED_ALTERNATE': 4, 'ANCHORED_MAIN': 1, 'NOT_ANCHORED_PINNACLE_NO_2_5_LINE': 1} |
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

## 2026-11-07 — Galatasaray vs Amed SK

The model's most likely 1X2 outcome is **Galatasaray win** at **64.0%**. Expected goals are 2.21 for Galatasaray and 1.53 for Amed SK (3.74 combined). The most likely exact score is 2-1 at 11.7%. Goal-market probabilities: at least one goal: 96.6%; Over 2.5 goals: 68.3%; Under 3.5 goals: 54.5%; Double Chance 1X: 82.8%; Double Chance X2: 36.0%; Double Chance 12 (either team wins): 81.2%; Under 4.5 goals: 72.8%; BTTS Yes (both teams score): 64.7%; BTTS No (at least one team does not score): 35.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Galatasaray win | 64.0% | 1.56 |
| Draw | 18.8% | 5.33 |
| Amed SK win | 17.2% | 5.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Galatasaray expected goals | 2.21 |
| Amed SK expected goals | 1.53 |
| Expected total goals | 3.74 |
| Over 0.5 | 96.6% |
| Under 0.5 | 3.4% |
| Over 1.5 | 87.0% |
| Under 1.5 | 13.0% |
| Over 2.5 | 68.3% |
| Under 2.5 | 31.7% |
| Over 3.5 | 45.5% |
| Under 3.5 | 54.5% |
| Over 4.5 | 27.2% |
| Under 4.5 | 72.8% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-1 | 11.70% |
| 2 | 2-0 | 8.39% |
| 3 | 1-1 | 8.17% |
| 4 | 3-1 | 7.89% |
| 5 | 1-0 | 7.18% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Galatasaray win | 64.0% | 68.9% | 1.45 | -7.2% |
| Draw | 18.8% | 17.4% | 5.37 | +0.7% |
| Amed SK win | 17.2% | 13.6% | 6.80 | +17.1% |

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
| Market best home last update utc | 2026-11-07T13:53:28Z |
| Market best draw last update utc | 2026-11-07T13:53:32Z |
| Market best away last update utc | 2026-11-07T13:53:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Matched home-team name | Galatasaray |
| Matched away-team name | Amedspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 2.2147 |
| Dc lambda away | 1.5272 |
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
| P btts yes | 64.7% |
| P btts no | 35.3% |
| Fair Over 0.5 odds | 1.03 |
| Fair Under 0.5 odds | 29.75 |
| Fair Over 1.5 odds | 1.15 |
| Fair Under 1.5 odds | 7.68 |
| Fair Over 2.5 odds | 1.46 |
| Fair Under 2.5 odds | 3.15 |
| Fair Over 3.5 odds | 2.20 |
| Fair Under 3.5 odds | 1.84 |
| Fair Over 4.5 odds | 3.68 |
| Fair Under 4.5 odds | 1.37 |
| Score matrix json | [[0.033608451343239754,0.024845907379211114,0.021530333877801833,0.01000994972627913,0.0034903926975074465,0.0009736585310377484,0.0002263381748180698,4.5098506081012716e-05,7.862751592068916e-06,1.2185249672010908e-06,1.699561241984439e-07,2.1549962551634636e-08,2.504768887577108e-09,2.687365232580988e-10,2.6773247018730405e-11,2.4895002389447872e-12,2.1701740997868941e-13,1.7805248571428763e-14],[0.07179296117379126,0.08171437242832479,0.043547986429568274,0.020246465164671636,0.007059787121166423,0.001969354898875085,0.0004577992994169432,9.12177740464402e-05,1.590346910428135e-05,2.4646300905938812e-06,3.43759043971291e-07,4.35876880536375e-08,5.066230841774069e-09,5.435556426757965e-10,5.415248107458459e-11,5.0353479531383434e-12,4.389468030719132e-13,3.601350204620392e-14],[0.08390015050337973,0.11702135600859914,0.052558415107089085,0.020475594926720776,0.007139682911865386,0.001991642138435151,0.0004629802257509237,9.22500879191049e-05,1.6083449069276832e-05,2.492522372115809e-06,3.476493738292072e-07,4.408097102974085e-08,5.12356550527312e-09,5.497070757310882e-10,5.476532608244507e-11,5.09233311419996e-12,4.4391437522448803e-13,3.642106776630807e-14],[0.056566433762660344,0.07889712645045217,0.0550216457719102,0.016474773477203403,0.0048136552568420286,0.0013427877355020584,0.0003121465231734738,6.219605634277658e-05,1.0843643914747451e-05,1.6804868741988531e-06,2.343891537661547e-07,2.9719891001234143e-08,3.4543660177463985e-09,3.706187498073167e-10,3.692340444858121e-11,3.433308785187343e-12,2.9929211034510866e-13,2.4555497278699615e-14],[0.028603298767293724,0.039895003620201715,0.02782216356939618,0.012935166736689926,0.002904819624447019,0.0006789920492561878,0.00015783954666409458,3.1449965348429005e-05,5.483180854586734e-06,8.49752493482359e-07,1.185208708952057e-07,1.5028115882406027e-08,1.746729582984762e-09,1.8740652582021633e-10,1.8670633778676453e-11,1.7360818140865817e-12,1.513396033911891e-13,1.24166962334781e-14],[0.011570801211245938,0.016138598557000172,0.011254811081313284,0.005232621739269442,0.0018245750685057416,0.0003277923863316827,6.385032833386766e-05,1.272235416298717e-05,2.218093660801051e-06,3.437476656394487e-07,4.794486984418272e-08,6.0792757810759386e-09,7.06598946469399e-10,7.581096409884887e-11,7.552771926714337e-12,7.022916384813772e-13,6.122092701526298e-14,5.022886520427539e-15],[0.0039005827544402734,0.005440413162667334,0.0037940606883459464,0.0017639464842647559,0.0006150746103457455,0.0001715774394140579,2.5687158285515042e-05,4.288777789717608e-06,7.477319610888246e-07,1.1587928890949778e-07,1.616248771920308e-08,2.0493583666534928e-09,2.3819851491575514e-10,2.5556306236948905e-11,2.5460822796721715e-12,2.367464969483381e-13,2.0637921935301127e-14,1.693243551712569e-15],[0.0011270644996685653,0.0015719949877212188,0.0010962851913742864,0.0005096883175896797,0.00017772440725146018,4.9576910190530816e-05,1.1524725566451252e-05,1.4789029748243222e-06,2.1605544649743067e-07,3.348305650689203e-08,4.670114001274904e-09,5.921574307132866e-10,6.882691816491022e-11,7.384436458766203e-12,7.356846736265433e-13,6.840736088155463e-14,5.963280521027397e-15,4.8925886632081e-16],[0.00028495487933084644,0.00039744632376099406,0.0002771729697032587,0.0001288641183160497,4.493392972396763e-05,1.2534493336533347e-05,2.9137877948200553e-06,5.805802608821865e-07,6.518976406363328e-08,8.465496277591116e-09,1.1807414500997287e-09,1.497147228604834e-10,1.740145853778864e-11,1.867001578572314e-12,1.8600260895490232e-13,1.7295382181833743e-14,1.5076917796497455e-15,1.236989553437193e-16],[6.403993799099685e-05,8.93209408737732e-05,6.229105405831062e-05,2.8960550405746192e-05,1.0098321811411072e-05,2.8169658926533955e-06,6.548362678940111e-07,1.3047793388553923e-07,2.2748327417885694e-08,2.2704612335572405e-09,2.653564291488902e-10,3.364645515402045e-11,3.91075361941435e-12,4.195845517775681e-13,4.1801690048639726e-14,3.88691432501934e-15,3.3883430353969564e-16,2.77997465716859e-17],[1.2952935920132814e-05,1.8066357647420122e-05,1.2599200700791733e-05,5.857659538492124e-06,2.0425209553212917e-06,5.697691134846023e-07,1.32449413323956e-07,2.6390911197451767e-08,4.601154163757915e-09,7.13060963560851e-10,6.405216175539473e-11,6.805446588828989e-12,7.910023435504117e-13,8.486660016779772e-14,8.454952167964391e-15,7.861805266910144e-16,6.853377999693769e-17,5.622871402367739e-18],[2.3817317501669436e-06,3.321966377665108e-06,2.316688395652434e-06,1.0770819674024827e-06,3.755702212738311e-07,1.0476676455578688e-07,2.4354244856128026e-08,4.852650511233495e-09,8.460410077534524e-10,1.3111467139104776e-10,1.828747212817481e-11,1.4933724052297271e-12,1.454462067678598e-13,1.5604915935251114e-14,1.5546612867345322e-15,1.445595912253814e-16,1.2601705187466793e-17,1.0339101056857272e-18],[4.0144764484307065e-07,5.599268592980918e-07,3.9048440287398127e-07,1.8154522191105684e-07,6.330342650594566e-08,1.765873544986799e-08,4.104977077598585e-09,8.179280134484754e-10,1.426026125651954e-10,2.209974991122314e-11,3.0824053193540728e-12,3.908403978633908e-13,2.925669947802028e-14,2.6302528610711753e-15,2.620425713536083e-16,2.436592930032471e-17,2.1240531676838304e-18,1.7426848211512166e-19],[6.246012893333469e-08,8.711747166599338e-08,6.075438843214346e-08,2.8246119048047013e-08,9.849205076365242e-09,2.7474738167403177e-09,6.386820319631444e-10,1.2725915778668672e-10,2.218714614837084e-11,3.438438975994096e-12,4.795829198273483e-13,6.080977670810862e-14,7.067967584353319e-15,4.883805130598996e-16,4.07704790475655e-17,3.7910275604524285e-18,3.304755586912245e-19,2.7113951225649873e-20],[9.023855971950045e-09,1.2586197473166055e-08,8.777421056250459e-09,4.08082587098372e-09,1.422952683017686e-09,3.9693814970235654e-10,9.227285896990718e-11,1.8385621845328066e-11,3.205462663793055e-12,4.967645539257066e-13,6.92871959926357e-14,8.785423214321214e-15,1.0211365647946456e-15,1.0955768875749563e-16,7.029459872345943e-18,5.477043879901166e-19,4.7745079858260843e-20,3.91725721462868e-21],[1.2167972239824238e-09,1.697151438747257e-09,1.183567380526622e-09,5.50267824176675e-10,1.9187416997083327e-10,5.3524041180609936e-11,1.244228176873724e-11,2.479158986150277e-12,4.322318621891548e-13,6.698486013834762e-14,9.342842793970953e-15,1.1846464096862886e-15,1.3769237244159677e-16,1.477300745495421e-17,1.4717812562498989e-18,8.813717752183155e-20,6.43805495244362e-21,5.282118552425501e-22],[1.5382096864553142e-10,2.1454476810183067e-10,1.4962023034044088e-10,6.956190239512558e-11,2.4255701855050614e-11,6.766221764772582e-12,1.5728864235602858e-12,3.134019614441672e-13,5.464043014808687e-14,8.467866188372327e-15,1.1810719979850101e-15,1.4975663541046026e-16,1.7406330066030487e-17,1.8675242445832022e-18,1.8605468027757983e-19,1.7300224014061157e-20,9.712675384545226e-22,6.677370528307181e-23],[1.8301384054858426e-11,2.5526209024469095e-11,1.7801586623387434e-11,8.276368966662032e-12,2.8859063824541786e-12,8.05034737512312e-13,1.8713962579825268e-13,3.7288086991267696e-14,6.50103497506387e-15,1.0074937936171565e-15,1.4052214351460321e-16,1.781781589040763e-17,2.0709785819783125e-18,2.2219518400405967e-19,2.2136501862828446e-20,2.058354245876839e-21,1.7943308470947167e-22,9.481143766022742e-24]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.09443049994097474, "-10": 2.190573905597598e-07, "-11": 2.7204622869573026e-08, "-12": 3.1066795276104485e-09, "-13": 3.2829304625346186e-10, "-14": 3.2277064844371935e-11, "-15": 2.9648681097830087e-12, "-16": 2.5303091202489334e-13, "-17": 1.7805248571428763e-14, "-2": 0.05043061402088036, "-3": 0.019407314271178238, "-4": 0.005990767579471252, "-5": 0.0015354513797467577, "-6": 0.00033544473072757243, "-7": 6.374464773563567e-05, "-8": 1.0706576104065453e-05, "-9": 1.6100145503510925e-06, "0": 0.18761585795369665, "1": 0.2587794109848115, "10": 1.669511090661866e-05, "11": 3.0066926512995236e-06, "12": 4.979178661260838e-07, "13": 7.630234159580494e-08, "14": 1.0878904010004404e-08, "15": 1.449143578707642e-09, "16": 1.7934717767000053e-10, "17": 1.8301384054858426e-11, "2": 0.1965197627841756, "3": 0.10967113594483645, "4": 0.04909353467402152, "5": 0.01824705696939478, "6": 0.005780862785500256, "7": 0.00159305342349158, "8": 0.0003880182485808024, "9": 8.461478816139128e-05} |
| Raw goal margin distribution | {"-1": 0.1357966562778841, "-10": 6.110433386779936e-07, "-11": 8.276072484179306e-08, "-12": 1.0313351271933968e-08, "-13": 1.1898413214152543e-09, "-14": 1.2776084632616211e-10, "-15": 1.2815936631426542e-11, "-16": 1.1900938268297512e-12, "-17": 8.917277135448487e-14, "-2": 0.07543489436176057, "-3": 0.030858952947049333, "-4": 0.010218042584715056, "-5": 0.002825091369241517, "-6": 0.000668223268924119, "-7": 0.00013782708964450537, "-8": 2.5171005340882162e-05, "-9": 4.120982887304271e-06, "0": 0.21885580618554273, "1": 0.2004104701561676, "10": 2.51316667902292e-05, "11": 4.936151636435442e-06, "12": 8.920289409155473e-07, "13": 1.492392679031408e-07, "14": 2.3238429307621783e-08, "15": 3.3804480785637435e-09, "16": 4.552186524447773e-10, "17": 4.9463636089497286e-11, "2": 0.15863614306805676, "3": 0.09410787564661678, "4": 0.045188447395783114, "5": 0.018117869944972206, "6": 0.006214571113047255, "7": 0.0018588274659979889, "8": 0.0004922888336510917, "9": 0.00011687864340973324} |
| Research history json | {"away": [], "h2h": [], "home": [{"away": "Galatasaray", "away_goals": 4.0, "away_xg": 2.8, "date": "2026-10-30T00:00:00+00:00", "home": "Konyaspor", "home_goals": 0.0, "home_xg": 1.38, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 1.0, "away_xg": 1.92, "date": "2026-10-17T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 0.0, "home_xg": 1.74, "source": "pipeline training history"}, {"away": "Kasimpasa", "away_goals": 1.0, "away_xg": 0.51, "date": "2026-10-09T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.4, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 0.0, "away_xg": 0.82, "date": "2026-09-13T00:00:00+00:00", "home": "Galatasaray", "home_goals": 1.0, "home_xg": 2.26, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 3.0, "away_xg": 2.12, "date": "2026-09-04T00:00:00+00:00", "home": "Buyuksehyr", "home_goals": 2.0, "home_xg": 1.98, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 0.63, "date": "2026-08-29T00:00:00+00:00", "home": "Galatasaray", "home_goals": 3.0, "home_xg": 2.92, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 4.0, "away_xg": 3.08, "date": "2026-08-21T00:00:00+00:00", "home": "Erzurumspor", "home_goals": 0.0, "home_xg": 0.48, "source": "pipeline training history"}, {"away": "Corum", "away_goals": 2.0, "away_xg": 0.61, "date": "2026-08-14T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.9, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 52.5% |
| Unadjusted draw probability | 21.9% |
| Unadjusted away-win probability | 25.6% |
| Raw p over 1 5 | 89.5% |
| Raw p under 3 5 | 48.5% |
| Raw p btts yes | 70.5% |
| P home draw | 82.8% |
| P draw away | 36.0% |
| P home away | 81.2% |
| Raw p home draw | 74.4% |
| Raw p draw away | 47.5% |
| Raw p home away | 78.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.9133 |
| Totals anchor target over 2 5 | 0.6826 |
| Totals anchor reference over odds | 1.43 |
| Totals anchor reference under odds | 2.93 |
| Totals anchor reference last update utc | 2026-11-07T13:53:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7345 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.12, "price": 1.79, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.79, "price": 2.12, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 3.82, "price": 1.29, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 2.25, "market_key": "alternate_spreads", "opposite_price": 3.36, "price": 1.35, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 3.04, "price": 1.41, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 2.0, "market_key": "alternate_spreads", "opposite_price": 3.0, "price": 1.42, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.71, "price": 1.51, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 2.46, "price": 1.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 2.37, "price": 1.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.14, "price": 1.78, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 2.0, "price": 1.9, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 1.9, "price": 2.0, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.78, "price": 2.14, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.6, "price": 2.46, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.51, "price": 2.71, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -2.0, "market_key": "alternate_spreads", "opposite_price": 1.42, "price": 3.0, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.41, "price": 3.04, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -2.25, "market_key": "alternate_spreads", "opposite_price": 1.35, "price": 3.36, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.29, "price": 3.82, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.73, "draw": 5.15, "home": 1.45}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 2.87, "home_away": 1.19, "home_draw": 1.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 6.8, "draw": 5.37, "home": 1.43}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.43, "under": 2.93}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.14, "under": 6.25}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.43 |
| Reference draw odds | 5.37 |
| Reference away odds | 6.80 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.39 |
| Reference Under 2.5 odds | 2.79 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:30Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:30Z |
| Home probability edge | -4.9% |
| Draw probability edge | +1.3% |
| Away probability edge | +3.6% |
| Over 2.5 probability edge | -0.5% |
| Under 2.5 probability edge | +0.5% |
| Raw edge prob home | -0.1643 |
| Raw ev home | -0.2385 |
| Raw edge prob draw | 0.0446 |
| Raw ev draw | 0.1753 |
| Raw edge prob away | 0.1197 |
| Raw ev away | 0.7406 |
| Market p home draw | 85.3% |
| Market home draw odds | 1.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T13:53:28Z |
| Market reference home draw last update utc | 2026-11-07T13:53:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 33.6% |
| Market draw away odds | 2.87 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T13:53:28Z |
| Market reference draw away last update utc | 2026-11-07T13:53:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 81.0% |
| Market home away odds | 1.19 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T13:53:28Z |
| Market reference home away last update utc | 2026-11-07T13:53:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.13 |
| Market reference dc draw away odds | 2.87 |
| Market reference dc home away odds | 1.19 |
| Market p over 1 5 | 86.6% |
| Market over 1 5 odds | 1.14 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference over 1 5 odds | 1.14 |
| Market reference over 1 5 opposite odds | 6.25 |
| Market reference over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 54.6% |
| Market under 3 5 odds | 1.78 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 3 5 odds | 1.78 |
| Market reference under 3 5 opposite odds | 2.12 |
| Market reference under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,693.8730 |
| Elo away rating | 1,457.7667 |
| Elo rating diff | 296.1063 |
| Elo home expectancy | 0.8461 |
| Research p home | 0.5329 |
| Research p draw | 0.2034 |
| Research p away | 0.2637 |
| Research p over 1 5 | 0.8876 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [2.214736111263906, 1.5272391870459034], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:12.950391+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:12.952475+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Galatasaray%22+%22Amed+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.013017+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Galatasaray_vs_Amed+SK&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"goals_against": 1.0408527377748258, "goals_for": 2.2981057758943, "last_match": "2026-10-30T00:00:00+00:00", "matches": 10, "points_per_game": 2.6034710533412406, "results": "WWWWLWWWWD", "xg_against": 1.1147534090307207, "xg_for": 2.2984475091718832, "xg_matches": 10}, "venue": {"goals_against": 1.1232992550353904, "goals_for": 2.1999854601202053, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 2.70260329000593, "results": "WWWWD", "xg_against": 0.5544118907898825, "xg_for": 2.502044081155706, "xg_matches": 5}}}, "goal_rates": [2.214736111263906, 1.5272391870459034], "h2h": [], "margin_distribution": {"-1": 0.14353627645920025, "-10": 6.110433386779937e-07, "-11": 8.276072484179308e-08, "-12": 1.0313351271933968e-08, "-13": 1.1898413214152543e-09, "-14": 1.2776084632616211e-10, "-15": 1.2815936631426542e-11, "-16": 1.1900938268297512e-12, "-17": 8.917277135448488e-14, "-2": 0.07543489436176057, "-3": 0.03085895294704934, "-4": 0.010218042584715058, "-5": 0.0028250913692415176, "-6": 0.000668223268924119, "-7": 0.00013782708964450537, "-8": 2.517100534088217e-05, "-9": 4.120982887304271e-06, "0": 0.20337656582291047, "1": 0.20815009033748377, "10": 2.51316667902292e-05, "11": 4.936151636435442e-06, "12": 8.920289409155474e-07, "13": 1.4923926790314083e-07, "14": 2.3238429307621783e-08, "15": 3.380448078563744e-09, "16": 4.5521865244477737e-10, "17": 4.946363608949729e-11, "2": 0.1586361430680568, "3": 0.09410787564661678, "4": 0.04518844739578312, "5": 0.01811786994497221, "6": 0.006214571113047256, "7": 0.001858827465997989, "8": 0.000492288833651092, "9": 0.00011687864340973326}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.013386+00:00", "p_over_1_5": 0.8875809104149881, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-07 — Goztepe vs Basaksehir

The model's most likely 1X2 outcome is **Goztepe win** at **46.7%**. Expected goals are 1.52 for Goztepe and 1.35 for Basaksehir (2.87 combined). The most likely exact score is 1-1 at 12.1%. Goal-market probabilities: at least one goal: 93.7%; Over 2.5 goals: 55.9%; Under 3.5 goals: 66.7%; Double Chance 1X: 72.5%; Double Chance X2: 53.3%; Double Chance 12 (either team wins): 74.2%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 59.3%; BTTS No (at least one team does not score): 40.7%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Goztepe win | 46.7% | 2.14 |
| Draw | 25.8% | 3.87 |
| Basaksehir win | 27.5% | 3.64 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Goztepe expected goals | 1.52 |
| Basaksehir expected goals | 1.35 |
| Expected total goals | 2.87 |
| Over 0.5 | 93.7% |
| Under 0.5 | 6.3% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 55.9% |
| Under 2.5 | 44.1% |
| Over 3.5 | 33.3% |
| Under 3.5 | 66.7% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.14% |
| 2 | 2-1 | 10.24% |
| 3 | 1-0 | 8.47% |
| 4 | 2-0 | 7.49% |
| 5 | 1-2 | 6.60% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Goztepe win | 46.7% | 49.4% | 1.98 | -7.6% |
| Draw | 25.8% | 25.3% | 3.79 | -2.0% |
| Basaksehir win | 27.5% | 25.2% | 3.81 | +4.7% |
| Over 2.5 | 55.9% | 56.3% | 1.71 | -4.4% |
| Under 2.5 | 44.1% | 43.7% | 2.23 | -1.6% |

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
| Market best home last update utc | 2026-11-07T13:53:28Z |
| Market best draw last update utc | 2026-11-07T13:53:28Z |
| Market best away last update utc | 2026-11-07T13:53:28Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 8.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Goztep |
| Matched away-team name | Buyuksehyr |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.5170 |
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
| P btts yes | 59.3% |
| P btts no | 40.7% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 15.76 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.96 |
| Fair Over 2.5 odds | 1.79 |
| Fair Under 2.5 odds | 2.27 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06346221379415455,0.05357682598970788,0.042971530122075545,0.019571030202401116,0.006685098635570698,0.0018268039364356518,0.0004160014189892726,8.119904017665186e-05,1.386803829642009e-05,2.1053613526308674e-06,2.876608570994715e-07,3.57307562790499e-08,4.068319817244992e-09,4.275883436355536e-10,4.1730342144369504e-11,3.801148267905993e-12],[0.08470927847676142,0.12142979040104217,0.06599619127656511,0.030057422880866016,0.010267054652288896,0.0028056273926316067,0.0006388999679775066,0.00012470645964312186,2.1298699521316087e-05,3.2334392128879436e-06,4.417929939656619e-07,5.487572397700344e-08,6.248174362662709e-09,6.566953057997981e-10,6.408995989606371e-11,5.8378490932635955e-12],[0.07493021911023053,0.10237905728138107,0.05809537156300353,0.02308127525469677,0.007884132828811147,0.0021544580973597268,0.0004906151162577948,9.57628381005996e-05,1.635539906954295e-05,2.4829773592966935e-06,3.392554890595541e-07,4.2139397477096226e-08,4.798010557177962e-09,5.0428026287248e-10,4.921506448795396e-11,4.482919322493717e-12],[0.03835957635784601,0.052411661301190945,0.03580569053637232,0.013545380282631754,0.00403618191503312,0.001102947527403751,0.0002511641930036053,4.9024571714650804e-05,8.372939341712355e-06,1.2711288014335995e-06,1.7367754948445815e-07,2.1572730660487222e-08,2.4562807171704935e-09,2.5815989168474806e-10,2.519502874273894e-11,2.2949737515685736e-12],[0.014728274344714742,0.02012361448690293,0.013747702227002915,0.0062612779841430405,0.0017764925786936132,0.0004234800097865158,9.643524489470412e-05,1.882313128564657e-05,3.214815162346583e-06,4.880537141582172e-07,6.668401581034842e-08,8.282914612202366e-09,9.43096345294235e-10,9.912126437645356e-11,9.673706820542938e-12,8.81162052252633e-13],[0.004523972072049517,0.006181217690320201,0.004222777188566738,0.0019232291626728407,0.0006569391860473751,0.000149113020264781,2.9621281112369646e-05,5.7817581511404065e-06,9.874703356864282e-07,1.499117493899844e-07,2.0482822231402938e-08,2.5441999180454645e-09,2.896837353450128e-10,3.0446325298539086e-11,2.971398988438573e-12,2.70659849351004e-13],[0.0011579950932964268,0.0015821980423378528,0.001080898640965536,0.0004922864019031832,0.0001681558466589672,4.595111895234541e-05,8.691710330089714e-06,1.4799489172385695e-06,2.5276146388379895e-07,3.837271040942567e-08,5.242960668871246e-09,6.512354573681311e-10,7.414995910559057e-11,7.793305251029681e-12,7.605850332491116e-13,6.928044039821431e-14],[0.0002540661072821536,0.0003471369610227887,0.0002371510135633934,0.00010800847993529704,3.689368083224016e-05,1.0081754219050987e-05,2.295826047544773e-06,3.722214032492413e-07,5.545629819301551e-08,8.41903840182553e-09,1.1503145526995506e-09,1.4288217500700573e-10,1.6268628057360703e-11,1.709864523133889e-12,1.6687365928691662e-13,1.5200247310773196e-14],[4.8774721790950025e-05,6.664213845115147e-05,4.552742131854133e-05,2.0735089840444715e-05,7.082719681449696e-06,1.9354598787663224e-06,4.4074464692394013e-07,8.602865437375857e-08,1.2204318865655445e-08,1.616257517341075e-09,2.2083336057765776e-10,2.7430019727554838e-11,3.1231942580085722e-12,3.2825380491799664e-13,3.203582088546002e-14,2.918090262678167e-15],[8.323200292618172e-06,1.1372199489618467e-05,7.7690621807082e-06,3.5383555147099903e-06,1.2086362025362229e-06,3.302780546518175e-07,7.521121268451583e-08,1.468042656042525e-08,2.507279855831355e-09,3.161700334356847e-10,3.7684280379039646e-11,4.68081702652106e-12,5.329599105367653e-13,5.601512555738316e-14,5.466777543313396e-15,4.979597799103321e-16],[1.2782870821316245e-06,1.7465560351702596e-06,1.1931818863814325e-06,5.43424883149147e-07,1.8562379738343178e-07,5.072449970324763e-08,1.1551028237460354e-08,2.2546375159344587e-09,3.850710469914548e-10,5.845914779181075e-11,6.634571566502244e-12,7.188854921742447e-13,8.185262218637167e-14,8.602870156505644e-15,8.395942508679639e-16,7.647726015256733e-17],[1.7847351181555274e-07,2.4385288213949677e-07,1.6659118634140478e-07,7.587258657253485e-08,2.591665945674354e-08,7.082117721184468e-09,1.612746153377686e-09,3.147908486010053e-10,5.3763339249625685e-11,8.162023656493899e-12,1.1151979767080173e-12,1.1505876040661078e-13,1.1428203521037496e-14,1.2011264683708022e-15,1.172235380824448e-16,1.0677699387135696e-17],[2.2841813308560375e-08,3.120934838969965e-08,2.1321061812212077e-08,9.710502360252213e-09,3.3169263655453237e-09,9.064001104193306e-10,2.0640624020231668e-10,4.028829668807394e-11,6.880865095846287e-12,1.0446111508937117e-12,1.4272786884125732e-13,1.772842766032534e-14,1.6766768834432625e-15,1.5372536950385412e-16,1.500277629441921e-17,1.3665782304880331e-18],[2.698517753736448e-09,3.687053193828004e-09,2.5188571087394416e-09,1.1471927671792973e-09,3.918596376018056e-10,1.0708155070327023e-10,2.4384706071439567e-11,4.759634553173788e-12,8.129011638164433e-13,1.2340971788703443e-13,1.686178250466467e-14,2.0944255230950153e-15,2.3847222249664986e-16,2.0818759589324868e-17,1.7724187497257052e-18,1.6144671033887017e-19],[2.96029709060303e-10,4.044728935903694e-10,2.7632078241180906e-10,1.258480292130547e-10,4.298733790100818e-11,1.1746937835233192e-11,2.6750231432993813e-12,5.221359874540265e-13,8.917595397923993e-14,1.3538151761546972e-14,1.8497519840966353e-15,2.297602739102987e-16,2.616060707656985e-17,2.7495308016236604e-18,2.2289019116928646e-19,1.771084241494543e-20],[3.030973181109839e-11,4.141295469464421e-11,2.829178475133632e-11,1.2885260829094502e-11,4.4013646035344636e-12,1.2027391997842825e-12,2.738888414924914e-13,5.34601807328425e-14,9.13049996802523e-15,1.3861370550036578e-15,1.8939141862817315e-16,2.3524572263951583e-17,2.678518271099717e-18,2.815174918358994e-19,2.747460595873926e-20,2.078742123118897e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.1471451127867895, "-10": 3.4760269589200754e-07, "-11": 4.250928709538008e-08, "-12": 4.776525161284312e-09, "-13": 4.96161222854111e-10, "-14": 4.75681912376331e-11, "-15": 3.801148267905993e-12, "-2": 0.08211851176830183, "-3": 0.032263557297671344, "-4": 0.010033735832109392, "-5": 0.002570348886229743, "-6": 0.0005584037106114568, "-7": 0.00010516297516819364, "-8": 1.7463280047483947e-05, "-9": 2.5918521867346013e-06, "0": 0.25846743809876394, "1": 0.22986057900523169, "10": 1.5446524089276135e-06, "11": 2.1233196670780843e-07, "12": 2.6818072545629282e-08, "13": 3.131282432078154e-09, "14": 3.374426637549472e-10, "15": 3.030973181109839e-11, "2": 0.14319150522042665, "3": 0.06323716109660513, "4": 0.02210582402649711, "5": 0.006365317232354525, "6": 0.0015543907483240083, "7": 0.00032904758077270213, "8": 6.141940248992204e-05, "9": 1.0246461896954368e-05} |
| Raw goal margin distribution | {"-1": 0.17603467476253437, "-10": 3.78067235994723e-07, "-11": 4.568611217750319e-08, "-12": 5.072283700451209e-09, "-13": 5.205916837744031e-10, "-14": 4.9328948461442904e-11, "-15": 3.90527502875255e-12, "-2": 0.09756659934249153, "-3": 0.037980340667947726, "-4": 0.01169106566514993, "-5": 0.002962575186502471, "-6": 0.0006364271871483016, "-7": 0.00011848906123783492, "-8": 1.94482703909128e-05, "-9": 2.852666021614933e-06, "0": 0.27091744216686237, "1": 0.19926553706807498, "10": 1.2173300683794384e-06, "11": 1.6535123371544022e-07, "12": 2.0635296090018778e-08, "13": 2.3806103937937464e-09, "14": 2.535577490692517e-10, "15": 2.2563713937895214e-11, "2": 0.12327330208641067, "3": 0.053939963469401594, "4": 0.018663359542583725, "5": 0.0053160497249846545, "6": 0.0012836667970048462, "7": 0.00026863696585873137, "8": 4.956241154817509e-05, "9": 8.171585057747102e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 40.2% |
| Unadjusted draw probability | 27.1% |
| Unadjusted away-win probability | 32.7% |
| Raw p over 1 5 | 79.1% |
| Raw p under 3 5 | 67.7% |
| Raw p btts yes | 58.9% |
| P home draw | 72.5% |
| P draw away | 53.3% |
| P home away | 74.2% |
| Raw p home draw | 67.3% |
| Raw p draw away | 59.8% |
| Raw p home away | 72.9% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0124 |
| Totals anchor target over 2 5 | 0.5589 |
| Totals anchor reference over odds | 1.74 |
| Totals anchor reference under odds | 2.18 |
| Totals anchor reference last update utc | 2026-11-07T13:53:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5514 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.85, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.47, "price": 2.85, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.75, "price": 1.3, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.63, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.29, "price": 1.37, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.23, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.84, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.28, "price": 1.69, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.22, "price": 1.72, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.99, "price": 1.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.92, "price": 1.99, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.84, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.23, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.37, "price": 3.29, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.63, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.3, "price": 3.75, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.81, "draw": 3.79, "home": 1.98}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.71, "under": 2.23}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.88, "home_away": 1.29, "home_draw": 1.29}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.8, "draw": 3.79, "home": 1.98}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.74, "under": 2.18}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.23, "under": 4.43}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.98 |
| Reference draw odds | 3.79 |
| Reference away odds | 3.80 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.74 |
| Reference Under 2.5 odds | 2.22 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Home probability edge | -2.8% |
| Draw probability edge | +0.5% |
| Away probability edge | +2.2% |
| Over 2.5 probability edge | -0.4% |
| Under 2.5 probability edge | +0.4% |
| Raw edge prob home | -0.0924 |
| Raw ev home | -0.2039 |
| Raw edge prob draw | 0.0178 |
| Raw ev draw | 0.0268 |
| Raw edge prob away | 0.0746 |
| Raw ev away | 0.2459 |
| Market p home draw | 74.5% |
| Market home draw odds | 1.29 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T13:53:28Z |
| Market reference home draw last update utc | 2026-11-07T13:53:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 51.1% |
| Market draw away odds | 1.88 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T13:53:28Z |
| Market reference draw away last update utc | 2026-11-07T13:53:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.5% |
| Market home away odds | 1.29 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T13:53:28Z |
| Market reference home away last update utc | 2026-11-07T13:53:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.29 |
| Market reference dc draw away odds | 1.88 |
| Market reference dc home away odds | 1.29 |
| Market p over 1 5 | 80.0% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.43 |
| Market reference over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 67.2% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.83 |
| Market reference under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,515.0066 |
| Elo away rating | 1,527.1311 |
| Elo rating diff | 47.8755 |
| Elo home expectancy | 0.5685 |
| Research p home | 0.4133 |
| Research p draw | 0.2484 |
| Research p away | 0.3383 |
| Research p over 1 5 | 0.7800 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.517020276254572, 1.3496074123345243], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:12.950391+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261107"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:13.023002+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Goztepe%22+%22Basaksehir%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.084407+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Goztepe_vs_Basaksehir&d=2026-11-07"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.517020276254572, 1.3496074123345243], "h2h": [], "margin_distribution": {"-1": 0.18727679121153723, "-10": 3.78067235994723e-07, "-11": 4.568611217750319e-08, "-12": 5.072283700451209e-09, "-13": 5.205916837744031e-10, "-14": 4.9328948461442904e-11, "-15": 3.90527502875255e-12, "-2": 0.09756659934249153, "-3": 0.037980340667947726, "-4": 0.01169106566514993, "-5": 0.002962575186502471, "-6": 0.0006364271871483016, "-7": 0.00011848906123783492, "-8": 1.94482703909128e-05, "-9": 2.852666021614933e-06, "0": 0.24843320926885656, "1": 0.21050765351707784, "10": 1.2173300683794384e-06, "11": 1.6535123371544022e-07, "12": 2.0635296090018778e-08, "13": 2.3806103937937464e-09, "14": 2.535577490692517e-10, "15": 2.2563713937895214e-11, "2": 0.12327330208641067, "3": 0.053939963469401594, "4": 0.018663359542583725, "5": 0.0053160497249846545, "6": 0.0012836667970048462, "7": 0.00026863696585873137, "8": 4.956241154817509e-05, "9": 8.171585057747102e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.084765+00:00", "p_over_1_5": 0.7800257884487768, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Alanyaspor vs Trabzonspor

The model's most likely 1X2 outcome is **Trabzonspor win** at **55.2%**. Expected goals are 1.18 for Alanyaspor and 1.61 for Trabzonspor (2.79 combined). The most likely exact score is 1-1 at 11.4%. Goal-market probabilities: at least one goal: 93.9%; Over 2.5 goals: 56.0%; Under 3.5 goals: 66.8%; Double Chance 1X: 44.8%; Double Chance X2: 79.3%; Double Chance 12 (either team wins): 75.9%; Under 4.5 goals: 82.9%; BTTS Yes (both teams score): 57.4%; BTTS No (at least one team does not score): 42.6%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Alanyaspor win | 20.7% | 4.82 |
| Draw | 24.1% | 4.16 |
| Trabzonspor win | 55.2% | 1.81 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Alanyaspor expected goals | 1.18 |
| Trabzonspor expected goals | 1.61 |
| Expected total goals | 2.79 |
| Over 0.5 | 93.9% |
| Under 0.5 | 6.1% |
| Over 1.5 | 79.8% |
| Under 1.5 | 20.2% |
| Over 2.5 | 56.0% |
| Under 2.5 | 44.0% |
| Over 3.5 | 33.2% |
| Under 3.5 | 66.8% |
| Over 4.5 | 17.1% |
| Under 4.5 | 82.9% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 11.36% |
| 2 | 1-2 | 11.16% |
| 3 | 0-1 | 9.71% |
| 4 | 0-2 | 9.16% |
| 5 | 1-3 | 6.19% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Alanyaspor win | 20.7% | 18.1% | 5.16 | +7.0% |
| Draw | 24.1% | 22.8% | 4.11 | -1.1% |
| Trabzonspor win | 55.2% | 59.0% | 1.68 | -7.3% |
| Over 2.5 | 56.0% | 56.4% | 1.73 | -3.0% |
| Under 2.5 | 44.0% | 43.6% | 2.21 | -2.9% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T15:30:00+00:00 |
| Fixture id | a85eafd97e49ac329956fa1022be891d |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-07T13:53:28Z |
| Market best draw last update utc | 2026-11-07T13:53:28Z |
| Market best away last update utc | 2026-11-07T13:53:28Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 12.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Alanyaspor |
| Matched away-team name | Trabzonspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.1770 |
| Dc lambda away | 1.6082 |
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
| P btts yes | 57.4% |
| P btts no | 42.6% |
| Fair Over 0.5 odds | 1.07 |
| Fair Under 0.5 odds | 16.38 |
| Fair Over 1.5 odds | 1.25 |
| Fair Under 1.5 odds | 4.94 |
| Fair Over 2.5 odds | 1.78 |
| Fair Under 2.5 odds | 2.28 |
| Fair Over 3.5 odds | 3.01 |
| Fair Under 3.5 odds | 1.50 |
| Fair Over 4.5 odds | 5.86 |
| Fair Under 4.5 odds | 1.21 |
| Score matrix json | [[0.06106521011674927,0.09711911477822896,0.09160409461498495,0.05082825405698316,0.021152259252218537,0.007042037225539447,0.0019537033725559004,0.0004645924482632007,9.66704453518016e-05,1.7879804670286362e-05,2.97628372865949e-06,4.503946312021065e-07,6.247748213892906e-08,8.000032048479965e-09,9.51207467775669e-10,1.0555906924512595e-10],[0.04412874921305017,0.1135634648484764,0.11160101847081573,0.06192392320118803,0.02576973971991167,0.008579294733305943,0.002380191486892759,0.0005660117117902424,0.00011777333974679733,2.178291723366686e-05,3.625998343988661e-06,5.487145500122662e-07,7.611614598127457e-08,9.746417211610981e-09,1.158853462031215e-09,1.2860232597790793e-10],[0.03202650746455605,0.05331152929816847,0.05250825385715463,0.037720873319076885,0.0156976017860206,0.005226065679828378,0.0014498903963259305,0.0003447852618799187,7.174146919793858e-05,1.326903430878424e-05,2.2087719433473287e-06,3.3424871938588463e-07,4.636604645942292e-08,5.937016744878902e-09,7.059140050708946e-10,7.833793138381497e-11],[0.0130059355466226,0.021649763550122172,0.01801916748303103,0.011831774889340054,0.006374781805086901,0.0021223005183904926,0.0005887991709727174,0.00014001698119591626,2.9134145377576018e-05,5.388542761865714e-06,8.969802768583564e-07,1.3573810087425403e-07,1.8829209287661005e-08,2.411017099150448e-09,2.8667103528447575e-10,3.1812962670413506e-11],[0.003961273945420965,0.006593961962074611,0.005488175642023942,0.0030452174328516003,0.001499666696110872,0.0006463982323852752,0.00017933310577303063,4.264557651693972e-05,8.873512450726233e-06,1.6412117351995037e-06,2.7319715583229896e-07,4.134233946236454e-08,5.734893571993676e-09,7.343338879846475e-10,8.73126349818132e-11,9.689411399988354e-12],[0.0009652018473824177,0.0016066811725356323,0.0013372458813569286,0.0007419960175355036,0.00030878282990852386,0.00012165208864210457,4.369620666832249e-05,1.0390997897133375e-05,2.1621152003668535e-06,3.998967555857645e-07,6.656706987250154e-08,1.0073451867753802e-08,1.3973610375087575e-09,1.7892739432919302e-10,2.1274548982326682e-11,2.360916693006738e-12],[0.00019598379608562775,0.00032623588127891575,0.0002715271679586467,0.0001506619538611494,6.269821316199606e-05,2.0873569380787285e-05,6.853018439477679e-06,2.1098873966318835e-06,4.3901650798897185e-07,8.119885432727802e-08,1.3516413259351294e-08,2.045409819803262e-09,2.8373352307169046e-10,3.6331126032803375e-11,4.319787494059829e-12,4.793830606439594e-13],[3.410950341538685e-05,5.6778897689291985e-05,4.725725824194797e-05,2.6221578173485517e-05,1.091215171203937e-05,3.6328875157321817e-06,1.0078879682517565e-06,2.836290117634657e-07,7.640751622199645e-08,1.4132048946493997e-08,2.352429912278002e-09,3.559881716137529e-10,4.938168240217744e-11,6.323158813391486e-12,7.518264735417309e-13,8.343301064119381e-14],[5.194439365252226e-06,8.646697012300724e-06,7.1966735931761035e-06,3.9932096408635725e-06,1.6617805812749593e-06,5.532421182285506e-07,1.5348839513416386e-07,3.6499680697219236e-08,8.987429759497248e-09,2.1521295829309886e-09,3.582448677579233e-10,5.4212427242798375e-11,7.520196112750834e-12,9.629358907114942e-13,1.1449351761134793e-13,1.2705776145677426e-14],[7.031523669372648e-07,1.1704719302452396e-06,9.741875331084885e-07,5.40546267501495e-07,2.2494919410752107e-07,7.489037364148772e-08,2.077716587817922e-08,4.9408290423769155e-09,1.0280669557140623e-09,2.250169956082018e-10,4.849430496622607e-11,7.338539128627786e-12,1.017981600071369e-12,1.3034912974285011e-13,1.549857111547659e-14,1.7199347114092857e-15],[8.566486096520696e-08,1.425982758258735e-07,1.1868500129108196e-07,6.585460424811248e-08,2.7405498926771636e-08,9.123873782256404e-09,2.5312764485994617e-09,6.019398538209541e-10,1.252491166427749e-10,2.3165609018858145e-11,4.563311895686251e-12,8.94052219264902e-13,1.2402042051724073e-13,1.588039890272209e-14,1.888186689251564e-15,2.0953917650007039e-16],[9.487751484015997e-09,1.57933718427974e-08,1.3144873924294974e-08,7.29368042093811e-09,3.0352767772340503e-09,1.0105082298882912e-09,2.803497444700051e-10,6.6667425558511e-11,1.3871877907813625e-11,2.5656907496303983e-12,4.2708652424975417e-13,7.648206658451258e-14,1.3735794531770136e-14,1.7588224221511582e-15,2.0912479003872857e-16,2.3207364261123216e-17],[9.632418116465678e-10,1.603418484505323e-09,1.3345303356685463e-09,7.404892459579606e-10,3.081557845056592e-10,1.0259161822284116e-10,2.8462444048295725e-11,6.768395217874213e-12,1.40833924975515e-12,2.604811698496063e-13,4.33598622435709e-14,6.561554927077832e-15,1.077114701530125e-15,1.7856404640568993e-16,2.1231346748117815e-17,2.3561223786359075e-18],[9.027037464045812e-11,1.5026464336541841e-10,1.2506574352698288e-10,6.939507903585675e-11,2.8878873174534557e-11,9.614391422768466e-12,2.6673629158920517e-12,6.343013401668788e-13,1.3198275880377376e-13,2.4411038334096332e-14,4.063477064388441e-15,6.149172661834069e-16,8.52996014014503e-17,1.2925283584607044e-17,1.9896993692558797e-18,2.2080442028846446e-19],[7.855439361837988e-12,1.3076214637268345e-11,1.0883375287101946e-11,6.0388453858460795e-12,2.5130751696148568e-12,8.366562022518009e-13,2.321172114911591e-13,5.519768511717569e-14,1.1485302489555198e-14,2.124278670125869e-15,3.5360878698753625e-16,5.3510859086276513e-17,7.422876542463445e-18,9.504744461303543e-19,1.3373615736776075e-19,1.9214673045396142e-20],[6.380173557390621e-13,1.0620477737344965e-12,8.839457606821826e-13,4.904739235226007e-13,2.0411150804377308e-13,6.795306452451351e-14,1.8852517685587897e-14,4.483145942474418e-15,9.328341785499743e-16,1.7253352709344626e-16,2.8720041343059647e-17,4.3461422391482315e-18,6.028846822505347e-19,7.71973615840821e-20,9.178801583089851e-21,1.2053999074852845e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.2535080713087068, "-10": 3.573865015782005e-06, "-11": 5.327441543749445e-07, "-12": 7.296162631828135e-08, "-13": 9.237223441894996e-09, "-14": 1.0798097937535768e-09, "-15": 1.0555906924512595e-10, "-2": 0.17153809773852038, "-3": 0.08245774992594396, "-4": 0.03133074865230652, "-5": 0.009797857994264919, "-6": 0.002597128657086542, "-7": 0.0005965745793917988, "-8": 0.00012080379085387687, "-9": 2.1859637030768598e-05, "0": 0.2405971683610122, "1": 0.11883536526570583, "10": 1.028647392509429e-07, "11": 1.1222478668942192e-08, "12": 1.1248803042226109e-09, "13": 1.0423053503840864e-10, "14": 8.917487135572486e-12, "15": 6.380173557390621e-13, "2": 0.059972932331998366, "3": 0.021099292130987768, "4": 0.005867443134420629, "5": 0.0013429225568643102, "6": 0.0002605283587511572, "7": 4.3799383156933073e-05, "8": 6.4912079839857715e-06, "9": 8.596657403152857e-07} |
| Raw goal margin distribution | {"-1": 0.21669389809062142, "-10": 2.3342490558849667e-06, "-11": 3.3648963924576706e-07, "-12": 4.455834277704646e-08, "-13": 5.454225258827072e-09, "-14": 6.169069130285133e-10, "-15": 5.872817627819451e-11, "-2": 0.1437057192653904, "-3": 0.06728960853858089, "-4": 0.024836524674121268, "-5": 0.007532798718045525, "-6": 0.0019345810378700859, "-7": 0.00043026590680531393, "-8": 8.432000487105607e-05, "-9": 1.4761354754685654e-05, "0": 0.2694853762503193, "1": 0.15557143050532532, "10": 1.0293529285833048e-07, "11": 1.0860017383657563e-08, "12": 1.0525180810686749e-09, "13": 9.429210186659096e-11, "14": 7.805551520716394e-12, "15": 5.438412977643157e-13, "2": 0.07697637853968278, "3": 0.02637989943270226, "4": 0.0071261944864324245, "5": 0.0015818486173309375, "6": 0.0002973289479824203, "7": 4.839816701181077e-05, "8": 6.9416755809190705e-06, "9": 8.894092031367177e-07} |
| Research history json | {"away": [{"away": "Gaziantep", "away_goals": 0.0, "away_xg": 0.51, "date": "2026-11-01T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 1.37, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 4.0, "away_xg": 2.63, "date": "2026-10-26T00:00:00+00:00", "home": "Rizespor", "home_goals": 3.0, "home_xg": 1.81, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 1.19, "date": "2026-10-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.35, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 3.0, "away_xg": 2.02, "date": "2026-10-10T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 1.66, "source": "pipeline training history"}, {"away": "Galatasaray", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-19T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": 2.28, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": 0.92, "date": "2026-09-12T00:00:00+00:00", "home": "Konyaspor", "home_goals": 1.0, "home_xg": 1.05, "source": "pipeline training history"}, {"away": "Genclerbirligi", "away_goals": 0.0, "away_xg": 0.86, "date": "2026-09-06T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": 3.2, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.84, "date": "2026-08-31T00:00:00+00:00", "home": "Amedspor", "home_goals": 2.0, "home_xg": 2.39, "source": "pipeline training history"}, {"away": "Buyuksehyr", "away_goals": 1.0, "away_xg": 1.95, "date": "2026-08-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": 0.86, "date": "2026-08-15T00:00:00+00:00", "home": "Kasimpasa", "home_goals": 1.0, "home_xg": 1.86, "source": "pipeline training history"}], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "home": [{"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.5, "date": "2026-11-02T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 5.0, "home_xg": 1.91, "source": "pipeline training history"}, {"away": "Kocaelispor", "away_goals": 2.0, "away_xg": 1.54, "date": "2026-10-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.5, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Erzurumspor", "away_goals": 0.0, "away_xg": 1.69, "date": "2026-10-10T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 0.0, "home_xg": 0.98, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 2.0, "away_xg": 1.16, "date": "2026-09-19T00:00:00+00:00", "home": "Corum", "home_goals": 1.0, "home_xg": 1.14, "source": "pipeline training history"}, {"away": "Goztep", "away_goals": 2.0, "away_xg": 1.79, "date": "2026-09-12T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": 1.73, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 2.06, "date": "2026-09-07T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.29, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 0.66, "date": "2026-08-30T00:00:00+00:00", "home": "Eyupspor", "home_goals": 2.0, "home_xg": 1.47, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 0.0, "away_xg": 0.74, "date": "2026-08-23T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": 0.54, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": 1.25, "date": "2026-08-15T00:00:00+00:00", "home": "Gaziantep", "home_goals": 1.0, "home_xg": 1.28, "source": "pipeline training history"}]} |
| Unadjusted home-win probability | 26.8% |
| Unadjusted draw probability | 26.9% |
| Unadjusted away-win probability | 46.3% |
| Raw p over 1 5 | 77.8% |
| Raw p under 3 5 | 69.5% |
| Raw p btts yes | 56.5% |
| P home draw | 44.8% |
| P draw away | 79.3% |
| P home away | 75.9% |
| Raw p home draw | 53.7% |
| Raw p draw away | 73.2% |
| Raw p home away | 73.1% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 1.0351 |
| Totals anchor target over 2 5 | 0.5605 |
| Totals anchor reference over odds | 1.72 |
| Totals anchor reference under odds | 2.16 |
| Totals anchor reference last update utc | 2026-11-07T13:53:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.5396 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.86, "price": 1.47, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.47, "price": 2.86, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.47, "price": 1.22, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 3.92, "price": 1.27, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.49, "price": 1.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.83, "price": 1.44, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.82, "price": 1.46, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.5, "price": 1.56, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.32, "price": 1.65, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.15, "price": 1.74, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 2.04, "price": 1.84, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.84, "price": 2.04, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.74, "price": 2.15, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.65, "price": 2.32, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.56, "price": 2.5, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.46, "price": 2.82, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.44, "price": 2.83, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.49, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.27, "price": 3.92, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.22, "price": 4.47, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.68, "draw": 4.11, "home": 5.16}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.73, "under": 2.21}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.19, "home_away": 1.26, "home_draw": 2.26}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.65, "draw": 4.07, "home": 5.06}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.72, "under": 2.16}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.23, "under": 4.25}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 5.06 |
| Reference draw odds | 4.07 |
| Reference away odds | 1.65 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / 1xBet |
| Reference Over 2.5 odds | 1.73 |
| Reference Under 2.5 odds | 2.21 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Home probability edge | +2.6% |
| Draw probability edge | +1.2% |
| Away probability edge | -3.8% |
| Over 2.5 probability edge | -0.3% |
| Under 2.5 probability edge | +0.3% |
| Raw edge prob home | 0.0865 |
| Raw ev home | 0.3828 |
| Raw edge prob draw | 0.0413 |
| Raw ev draw | 0.1076 |
| Raw edge prob away | -0.1278 |
| Raw ev away | -0.2230 |
| Market p home draw | 42.6% |
| Market home draw odds | 2.26 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T13:53:28Z |
| Market reference home draw last update utc | 2026-11-07T13:53:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 80.9% |
| Market draw away odds | 1.19 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T13:53:28Z |
| Market reference draw away last update utc | 2026-11-07T13:53:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.4% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T13:53:28Z |
| Market reference home away last update utc | 2026-11-07T13:53:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.26 |
| Market reference dc draw away odds | 1.19 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 79.6% |
| Market over 1 5 odds | 1.23 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference over 1 5 odds | 1.23 |
| Market reference over 1 5 opposite odds | 4.25 |
| Market reference over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 66.9% |
| Market under 3 5 odds | 1.45 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 3 5 odds | 1.45 |
| Market reference under 3 5 opposite odds | 2.77 |
| Market reference under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,452.1266 |
| Elo away rating | 1,593.6095 |
| Elo rating diff | -81.4829 |
| Elo home expectancy | 0.3848 |
| Research p home | 0.2847 |
| Research p draw | 0.2480 |
| Research p away | 0.4673 |
| Research p over 1 5 | 0.7654 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.1769807659221856, 1.6081540709089421], "coverage": {"form": "last ten, exponential rank half-life five matches", "h2h": "last four years; descriptive only", "training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED", "venue_splits": "home team home matches / away team away matches", "xg": "verified supplied xG; no goals-to-xG substitution"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:13.090327+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:13.229628+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Alanyaspor%22+%22Trabzonspor%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.290207+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Alanyaspor_vs_Trabzonspor&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 0.7743771520489182, "goals_for": 2.5504665648542564, "last_match": "2026-11-01T00:00:00+00:00", "matches": 10, "points_per_game": 2.445760234190055, "results": "WWWWWLWLWD", "xg_against": 1.304688418272264, "xg_for": 1.9416908629267322, "xg_matches": 10}, "venue": {"goals_against": 1.4632227425095123, "goals_for": 2.031257084649452, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.6015486554658407, "results": "WWLLD", "xg_against": 1.7335781977270697, "xg_for": 1.5880534238553998, "xg_matches": 5}}, "home": {"all": {"goals_against": 2.0080296773705193, "goals_for": 0.7681538045198641, "last_match": "2026-11-02T00:00:00+00:00", "matches": 10, "points_per_game": 0.9433296058372811, "results": "LLLDWDWLWD", "xg_against": 1.821921306986439, "xg_for": 0.9535220089451488, "xg_matches": 10}, "venue": {"goals_against": 1.069203922761527, "goals_for": 0.9657278891499795, "last_match": "2026-10-23T00:00:00+00:00", "matches": 4, "points_per_game": 1.0971691275701443, "results": "LDDW", "xg_against": 1.4768169943171596, "xg_for": 0.9185985305199439, "xg_matches": 4}}}, "goal_rates": [1.1876934944672028, 1.5916044802793843], "h2h": [{"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2026-04-11T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2025-11-08T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 3.0, "away_xg": null, "date": "2025-04-27T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 4.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-11-30T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 2.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 1.0, "away_xg": null, "date": "2024-03-04T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 3.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": null, "date": "2023-10-23T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 1.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 1.0, "away_xg": null, "date": "2023-06-03T00:00:00+00:00", "home": "Trabzonspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}, {"away": "Trabzonspor", "away_goals": 0.0, "away_xg": null, "date": "2023-01-09T00:00:00+00:00", "home": "Alanyaspor", "home_goals": 5.0, "home_xg": null, "source": "pipeline training history"}], "margin_distribution": {"-1": 0.22672827145928678, "-10": 2.1167158765593314e-06, "-11": 3.019967462541666e-07, "-12": 3.957980617126256e-08, "-13": 4.795029680867353e-09, "-14": 5.36780962420409e-10, "-15": 5.058175687191149e-11, "-2": 0.1414871176565577, "-3": 0.06557878586547793, "-4": 0.023958346913674707, "-5": 0.007192176920957305, "-6": 0.001828188579983723, "-7": 0.0004024350833626346, "-8": 7.805679797867532e-05, "-9": 1.3524615516627365e-05, "0": 0.24803373296712472, "1": 0.16919008231034877, "10": 1.1333259000489457e-07, "11": 1.2066011505798935e-08, "12": 1.1800607322155827e-09, "13": 1.0668201754027653e-10, "14": 8.911816795200252e-12, "15": 6.266604405249872e-13, "2": 0.0787871423440004, "3": 0.0272502848149546, "4": 0.007429057979713272, "5": 0.0016642037083119787, "6": 0.0003156722019763502, "7": 5.1853778369435556e-05, "8": 7.505239042282442e-06, "9": 9.703936581228765e-07}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.290579+00:00", "p_over_1_5": 0.7653733386698582, "version": "team-form-research-v1", "warnings": ["availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Besiktas JK vs Genclerbirligi SK

The model's most likely 1X2 outcome is **Besiktas JK win** at **76.5%**. Expected goals are 1.92 for Besiktas JK and 0.81 for Genclerbirligi SK (2.73 combined). The most likely exact score is 2-0 at 14.7%. Goal-market probabilities: at least one goal: 95.2%; Over 2.5 goals: 55.4%; Under 3.5 goals: 68.8%; Double Chance 1X: 91.3%; Double Chance X2: 23.5%; Double Chance 12 (either team wins): 85.2%; Under 4.5 goals: 84.2%; BTTS Yes (both teams score): 45.6%; BTTS No (at least one team does not score): 54.4%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Besiktas JK win | 76.5% | 1.31 |
| Draw | 14.8% | 6.76 |
| Genclerbirligi SK win | 8.7% | 11.53 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Besiktas JK expected goals | 1.92 |
| Genclerbirligi SK expected goals | 0.81 |
| Expected total goals | 2.73 |
| Over 0.5 | 95.2% |
| Under 0.5 | 4.8% |
| Over 1.5 | 78.5% |
| Under 1.5 | 21.5% |
| Over 2.5 | 55.4% |
| Under 2.5 | 44.6% |
| Over 3.5 | 31.2% |
| Under 3.5 | 68.8% |
| Over 4.5 | 15.8% |
| Under 4.5 | 84.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 2-0 | 14.72% |
| 2 | 1-0 | 14.12% |
| 3 | 2-1 | 11.90% |
| 4 | 3-0 | 9.43% |
| 5 | 3-1 | 7.62% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Besiktas JK win | 76.5% | 82.5% | 1.22 | -6.6% |
| Draw | 14.8% | 11.2% | 7.55 | +11.7% |
| Genclerbirligi SK win | 8.7% | 6.4% | 13.10 | +13.6% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T18:00:00+00:00 |
| Fixture id | 1fa78d1150755a8ec1d24cc1e19eeb0a |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-07T13:53:28Z |
| Market best draw last update utc | 2026-11-07T13:53:28Z |
| Market best away last update utc | 2026-11-07T13:53:28Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 2.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Matched home-team name | Besiktas |
| Matched away-team name | Genclerbirligi |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.9218 |
| Dc lambda away | 0.8084 |
| Bbs statistics applied | 0 |
| Bbs statistics status | NO_OBSERVATIONS |
| Shot features applied | 0 |
| Shot features status | BASELINE_RETAINED_AUDIT_NOT_IMPROVED |
| Shot features version | football-data-lagged-shot-strength-v1 |
| Shot features weight | 0 |
| Goal rate features used | none |
| Score engine version | dc-positive-tail-bounded-v1 |
| Score grid max goals | 16 |
| Score grid omitted mass | 0 |
| P btts yes | 45.6% |
| P btts no | 54.4% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 21.00 |
| Fair Over 1.5 odds | 1.27 |
| Fair Under 1.5 odds | 4.65 |
| Fair Over 2.5 odds | 1.81 |
| Fair Under 2.5 odds | 2.24 |
| Fair Over 3.5 odds | 3.21 |
| Fair Under 3.5 odds | 1.45 |
| Fair Over 4.5 odds | 6.33 |
| Fair Under 4.5 odds | 1.19 |
| Score matrix json | [[0.04762999013519703,0.026437164592883096,0.01311950454701195,0.00353528811923708,0.0007144855608628194,0.0001155186450357256,1.5564295583028704e-05,1.7974634330066212e-06,1.8163465405745918e-07,1.6314915760984856e-08,1.3189048637351163e-09,9.692803728965508e-11,6.529753799451451e-12,4.0605240633586936e-13,2.3446751842367692e-14,1.2636303897909307e-15,6.384526786234814e-17],[0.14119660383936133,0.07055985815570319,0.025213295295054207,0.006794179077724597,0.001373110955946093,0.00022200577002991036,2.9911737839504655e-05,3.454396936718143e-06,3.490686825981375e-07,3.1354292940073976e-08,2.534694635477718e-09,1.8627801208474048e-10,1.2548996050850765e-11,7.803586781442417e-13,4.506038134238199e-14,2.4284671762897914e-15,1.2269896214730526e-16],[0.14715928950552448,0.11896420767110626,0.024993243439744312,0.006528586607836682,0.001319434429901093,0.0002133273027541612,2.8742452744049906e-05,3.319360488031618e-06,3.354231762740962e-07,3.012861666509237e-08,2.435610433994817e-09,1.789961849869528e-10,1.2058441001060211e-11,7.498535374413256e-13,4.3298917913481234e-14,2.333535531419379e-15,1.179025150656807e-16],[0.09427110626059483,0.07620917102993566,0.030803912139395623,0.00431440509190731,0.0008452374550260641,0.0001366587246635806,1.84125842543072e-05,2.1264018488802324e-06,2.148740592527425e-07,1.930056901377623e-08,1.5602663671729624e-09,1.1466600873003431e-10,7.724708217658156e-12,4.803605857675768e-13,2.7737541444417802e-14,1.4948765843086752e-15,7.55290445033775e-17],[0.045292968789761995,0.03661503234523228,0.014799875449381543,0.003988094493576263,0.000418930275290121,6.565828700393123e-05,8.846407314494336e-06,1.0216391468833586e-06,1.0323718947946633e-07,9.273043508677059e-09,7.496368577316659e-10,5.509178963381828e-11,3.711370133339105e-12,2.307913620835169e-13,1.3326624124616673e-14,7.182200481500068e-16,3.628826255581945e-17],[0.01740896529733721,0.014073483025981564,0.005688532348125422,0.0015328780712838678,0.0003097963197217207,2.6034098783553323e-05,3.40023632937379e-06,3.9268082728359047e-07,3.968061041405849e-08,3.5642197223280158e-09,2.88133067682801e-10,2.117527465146283e-11,1.4265153197791468e-12,8.870778226278078e-14,5.122268270667e-15,2.7605759189981843e-16,1.3947884636736834e-17],[0.005576142773408376,0.004507777994365685,0.0018220536374526002,0.0004909853534496448,9.922867212039355e-05,1.604337775307819e-05,1.1235201288077538e-06,1.2577682360297043e-07,1.2709816191007568e-08,1.1416300571601975e-09,9.228986879451047e-11,6.782502733850151e-12,4.569170513976213e-13,2.841336349181807e-14,1.6406775884209264e-15,8.842205839494324e-17,4.467548460985786e-18],[0.001530904222461106,0.0012375896109405953,0.0005002364036353053,0.00013479775918706944,2.7242773241522567e-05,4.404635200851093e-06,5.934543655723966e-07,3.5622597801219286e-08,3.4894212835272797e-09,3.1342925495553187e-10,2.5337756863341026e-11,1.86210477314562e-12,1.2544446434099008e-13,7.800757604590279e-15,4.504404477928442e-16,2.427586739727251e-17,1.2265447785140246e-18],[0.0003677648429009122,0.000297302693509902,0.00012017039322061787,3.238208896643568e-05,6.544455279669372e-06,1.058113204543065e-06,1.4256388369791553e-07,1.6464180241721338e-08,8.647417422280543e-10,7.529423396844777e-11,6.086818519141463e-12,4.4732822557639525e-13,3.0135173085477184e-14,1.8739541983549044e-15,1.0820804991473627e-16,5.831723780400063e-18,2.9464942428336955e-19],[7.853077369544602e-05,6.348461793930425e-05,2.566062019539958e-05,6.914718874022779e-06,1.3974721794332982e-06,2.2594451376779083e-07,3.044242075864049e-08,3.5156835613892905e-09,3.5526172923601705e-10,1.658602113739767e-11,1.2997505794232144e-12,9.552036397288312e-14,6.434923031743756e-15,4.0015535989200157e-16,2.3106237705732047e-17,1.2452788494966068e-18,6.291805131608287e-20],[1.5092182634162932e-05,1.2200585876255e-05,4.931503260069348e-06,1.3288828722783484e-06,2.6856866888848834e-07,4.342241527117904e-08,5.85047812844964e-09,6.756502692585652e-10,6.827482588356866e-11,6.132629473525216e-12,2.5768137216752684e-13,1.835727206701477e-14,1.2366748608449023e-15,7.690256302516853e-17,4.4405975267185276e-18,2.393198862391056e-19,1.2091702103057513e-20],[2.6367657132067937e-06,2.131572834715336e-06,8.615863606953752e-07,2.321700498481712e-07,4.6921818727780776e-08,7.586360339458103e-09,1.0221410984016934e-09,1.1804332794563567e-10,1.19283422635935e-11,1.0714359559225932e-12,8.661534721658215e-14,3.3085558038934335e-15,2.1606032410973923e-16,1.3435700213664654e-17,7.758198789682031e-19,4.181174359071247e-20,2.1125496750537354e-21],[4.222819054937739e-07,3.4137452327823236e-07,1.3798432235354039e-07,3.718237481525578e-08,7.51459825283565e-09,1.2149667616894995e-09,1.6369739964178407e-10,1.890481251558966e-11,1.9103415503405155e-12,1.7159204354613501e-13,1.3871575197001438e-14,1.01944013926333e-15,3.569577224338491e-17,2.151747142133917e-18,1.2424869421265419e-19,6.696212206897131e-21,3.383279362909329e-22],[6.242683199612168e-08,5.046612164811438e-08,2.0398515772516723e-08,5.496749530611894e-09,1.1108990381664297e-09,1.796111197901674e-10,2.4199734662299686e-11,2.794738631883659e-12,2.824098533866171e-13,2.536681665722876e-14,2.0506644567974386e-15,1.5070600344450015e-16,1.0152615549731105e-17,3.281488504975469e-19,1.8367948658091907e-20,9.899152888437215e-22,5.001573821575935e-23],[8.569499076806839e-09,6.927620208252844e-09,2.800159106130384e-09,7.545535873251337e-10,1.5249609787317504e-10,2.4655701338836235e-11,3.3219626435701757e-12,3.8364128628746213e-13,3.876715989733583e-14,3.4821711269787836e-15,2.815002236611654e-16,2.068781830010413e-17,1.393676834121593e-18,8.666572271027574e-20,2.6010914759068474e-21,1.3588833331139191e-22,6.865794863535442e-24],[1.0979343006944869e-09,8.875748489676309e-10,3.587596780707211e-10,9.667429307256939e-11,1.9537979417043163e-11,3.158917454212997e-12,4.256137610041593e-13,4.915257281695283e-14,4.9668941218502194e-15,4.461398603268862e-16,3.6066139740565587e-17,2.65054761248461e-18,1.7855951515378037e-19,1.1103714325102053e-20,6.411636287505803e-22,1.7960313690737322e-23,8.796537130868638e-25],[1.318768443140435e-10,1.0660981271859875e-10,4.3091917413603055e-11,1.1611897623234042e-11,2.3467770960089155e-12,3.794289558552397e-13,5.112200216566371e-14,5.90389259987214e-15,5.965915468869623e-16,5.358746590338064e-17,4.332033977412459e-18,3.1836682269375407e-19,2.1447426650056586e-20,1.3337071302288814e-21,7.701247332839798e-23,4.150481155981738e-24,1.0899705461233158e-25]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.059093471816990796, "-10": 1.5177352845559496e-09, "-11": 1.1025535658732437e-10, "-12": 7.354942560356039e-12, "-13": 4.535218522541741e-13, "-14": 2.5993121533723164e-14, "-15": 1.3863293519382359e-15, "-16": 6.384526786234814e-17, "-2": 0.021379028896872033, "-3": 0.0051412014493705934, "-4": 0.000967467081077375, "-5": 0.00014897418550893548, "-6": 1.937418754199438e-05, "-7": 2.1782775458116767e-06, "-8": 2.1554302518342175e-07, "-9": 1.903656729294614e-08, "0": 0.14794362122094093, "1": 0.29527926812094213, "10": 1.736739224689975e-05, "11": 2.999313223253241e-06, "12": 4.756472073181872e-07, "13": 6.972482378006848e-08, "14": 9.500165843188073e-09, "15": 1.2045441134130855e-09, "16": 1.318768443140435e-10, "2": 0.23980499351237433, "3": 0.13709398832402128, "4": 0.06133007958263411, "5": 0.02245080372023118, "6": 0.0069410938180041945, "7": 0.0018552445804125718, "8": 0.0004364208317312184, "9": 9.16312642934688e-05} |
| Raw goal margin distribution | {"-1": 0.09596856586771228, "-10": 2.464821817826913e-09, "-11": 1.790561313386302e-10, "-12": 1.194452226030527e-11, "-13": 7.365253794072636e-13, "-14": 4.2213167027010366e-14, "-15": 2.2514168762643945e-15, "-16": 1.0368554437222608e-16, "-2": 0.03471982064670755, "-3": 0.008349377939091355, "-4": 0.0015711791072752948, "-5": 0.0002419360124732488, "-6": 3.146393224306548e-05, "-7": 3.537551030692373e-06, "-8": 3.500446728481713e-07, "-9": 3.091563257285144e-08, "0": 0.23290290987775358, "1": 0.24161243937992197, "10": 1.4210879189536257e-05, "11": 2.4541898554078547e-06, "12": 3.891986145038947e-07, "13": 5.70523791461631e-08, "14": 7.77351643579101e-09, "15": 9.856189479014091e-10, "16": 1.0790830746502523e-10, "2": 0.19622058069542425, "3": 0.11217723870042368, "4": 0.05018337463927773, "5": 0.018370383696098606, "6": 0.005679554206447005, "7": 0.0015180549978072437, "8": 0.00035710160900156903, "9": 7.49773373196774e-05} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 62.6% |
| Unadjusted draw probability | 23.3% |
| Unadjusted away-win probability | 14.1% |
| Raw p over 1 5 | 76.7% |
| Raw p under 3 5 | 70.7% |
| Raw p btts yes | 48.3% |
| P home draw | 91.3% |
| P draw away | 23.5% |
| P home away | 85.2% |
| Raw p home draw | 85.9% |
| Raw p draw away | 37.4% |
| Raw p home away | 76.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 0 |
| Totals anchor status | NOT_ANCHORED_PINNACLE_NO_2_5_LINE |
| Unanchored p over 2 5 | 0.5539 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 1.5, "market_key": "spreads", "opposite_price": 1.67, "price": 2.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 2.0, "market_key": "spreads", "opposite_price": 1.97, "price": 1.88, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -2.0, "market_key": "spreads", "opposite_price": 1.88, "price": 1.97, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -1.5, "market_key": "spreads", "opposite_price": 2.32, "price": 1.67, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 13.1, "draw": 7.55, "home": 1.22}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 12.07, "draw": 7.26, "home": 1.19}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.19 |
| Reference draw odds | 7.26 |
| Reference away odds | 12.07 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / Nordic Bet |
| Reference Over 2.5 odds | 1.33 |
| Reference Under 2.5 odds | 3.08 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:30Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:30Z |
| Home probability edge | -6.0% |
| Draw probability edge | +3.6% |
| Away probability edge | +2.3% |
| Over 2.5 probability edge | -16.9% |
| Under 2.5 probability edge | +16.9% |
| Raw edge prob home | -0.1987 |
| Raw ev home | -0.2360 |
| Raw edge prob draw | 0.1214 |
| Raw ev draw | 0.7584 |
| Raw edge prob away | 0.0773 |
| Raw ev away | 0.8456 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,572.0567 |
| Elo away rating | 1,407.1890 |
| Elo rating diff | 224.8678 |
| Elo home expectancy | 0.7849 |
| Research p home | 0.6360 |
| Research p draw | 0.2133 |
| Research p away | 0.1507 |
| Research p over 1 5 | 0.7568 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.9218176421758777, 0.8084043356749167], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:13.090327+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:13.310106+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22Besiktas+JK%22+%22Genclerbirligi+SK%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.370744+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=Besiktas+JK_vs_Genclerbirligi+SK&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.9218176421758777, 0.8084043356749167], "h2h": [], "margin_distribution": {"-1": 0.10574612152047047, "-10": 2.464821817826913e-09, "-11": 1.790561313386302e-10, "-12": 1.194452226030527e-11, "-13": 7.365253794072636e-13, "-14": 4.2213167027010366e-14, "-15": 2.2514168762643945e-15, "-16": 1.0368554437222608e-16, "-2": 0.03471982064670755, "-3": 0.008349377939091355, "-4": 0.0015711791072752948, "-5": 0.0002419360124732488, "-6": 3.146393224306548e-05, "-7": 3.537551030692373e-06, "-8": 3.500446728481713e-07, "-9": 3.091563257285144e-08, "0": 0.2133477985722372, "1": 0.25138999503268017, "10": 1.4210879189536257e-05, "11": 2.4541898554078547e-06, "12": 3.891986145038947e-07, "13": 5.70523791461631e-08, "14": 7.77351643579101e-09, "15": 9.856189479014091e-10, "16": 1.0790830746502523e-10, "2": 0.19622058069542425, "3": 0.11217723870042368, "4": 0.05018337463927773, "5": 0.018370383696098606, "6": 0.005679554206447005, "7": 0.0015180549978072437, "8": 0.00035710160900156903, "9": 7.49773373196774e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.371097+00:00", "p_over_1_5": 0.7567715696097949, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çaykur Rizespor vs Erzurum BB

The model's most likely 1X2 outcome is **Çaykur Rizespor win** at **49.1%**. Expected goals are 1.42 for Çaykur Rizespor and 0.93 for Erzurum BB (2.35 combined). The most likely exact score is 1-1 at 12.7%. Goal-market probabilities: at least one goal: 92.7%; Over 2.5 goals: 52.7%; Under 3.5 goals: 69.4%; Double Chance 1X: 75.9%; Double Chance X2: 50.9%; Double Chance 12 (either team wins): 73.2%; Under 4.5 goals: 85.0%; BTTS Yes (both teams score): 55.8%; BTTS No (at least one team does not score): 44.2%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çaykur Rizespor win | 49.1% | 2.04 |
| Draw | 26.8% | 3.73 |
| Erzurum BB win | 24.1% | 4.15 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çaykur Rizespor expected goals | 1.42 |
| Erzurum BB expected goals | 0.93 |
| Expected total goals | 2.35 |
| Over 0.5 | 92.7% |
| Under 0.5 | 7.3% |
| Over 1.5 | 77.8% |
| Under 1.5 | 22.2% |
| Over 2.5 | 52.7% |
| Under 2.5 | 47.3% |
| Over 3.5 | 30.6% |
| Under 3.5 | 69.4% |
| Over 4.5 | 15.0% |
| Under 4.5 | 85.0% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-1 | 12.74% |
| 2 | 2-1 | 9.51% |
| 3 | 1-0 | 9.10% |
| 4 | 2-0 | 8.58% |
| 5 | 0-0 | 7.35% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çaykur Rizespor win | 49.1% | 50.0% | 2.01 | -1.3% |
| Draw | 26.8% | 25.6% | 3.71 | -0.7% |
| Erzurum BB win | 24.1% | 24.4% | 3.90 | -6.0% |
| Over 2.5 | 52.7% | 52.7% | 1.86 | -2.0% |
| Under 2.5 | 47.3% | 47.3% | 2.04 | -3.5% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T10:30:00+00:00 |
| Fixture id | cf2febfddf729564889172cf83e8fbab |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-07T13:53:28Z |
| Market best draw last update utc | 2026-11-07T13:53:32Z |
| Market best away last update utc | 2026-11-07T13:53:32Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 15.00 |
| Best home bookmaker | 1xBet |
| Best draw bookmaker | Pinnacle |
| Best away bookmaker | Pinnacle |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | Pinnacle |
| Matched home-team name | Rizespor |
| Matched away-team name | Erzurumspor |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.4174 |
| Dc lambda away | 0.9324 |
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
| P btts yes | 55.8% |
| P btts no | 44.2% |
| Fair Over 0.5 odds | 1.08 |
| Fair Under 0.5 odds | 13.61 |
| Fair Over 1.5 odds | 1.28 |
| Fair Under 1.5 odds | 4.51 |
| Fair Over 2.5 odds | 1.90 |
| Fair Under 2.5 odds | 2.11 |
| Fair Over 3.5 odds | 3.27 |
| Fair Under 3.5 odds | 1.44 |
| Fair Over 4.5 odds | 6.65 |
| Fair Under 4.5 odds | 1.18 |
| Score matrix json | [[0.07346228225413437,0.05731376627415682,0.03792041459188385,0.014006623681028544,0.0038802089004046497,0.0008599372099171802,0.00015881705168911236,2.5140894623807743e-05,3.4823496834417264e-06,4.287572808003773e-07,4.75108878473917e-08,4.786103647422567e-09,4.4195951843703006e-10,3.7672182184022086e-11,2.9817716437381437e-12,2.2027477160305585e-13],[0.09099961577273463,0.12741049454273504,0.06387932526256812,0.02359503923098754,0.006536456130643449,0.0014486183584459566,0.0002675373202344227,4.235141947551111e-05,5.866237236609393e-06,7.222686274322433e-07,8.003508112926873e-08,8.062492853111005e-09,7.445086277397811e-10,6.346116214665362e-11,5.0229820200810405e-12,3.7106671785653793e-13],[0.08582667933960161,0.09510513101505512,0.054224829272323374,0.01987366438158489,0.005505535893102389,0.0012201444036994058,0.00022534172797240918,3.567181594827119e-05,4.94102293629675e-06,6.083534828831733e-07,6.741206596626766e-08,6.79088835043012e-09,6.27085823085341e-10,5.345216108441907e-11,4.230764691025599e-12,3.1254262142409e-13],[0.048193481222415964,0.053403526514098784,0.0295884066869976,0.011246685879219535,0.003091473918426898,0.0006851366831477858,0.00012653410826596098,2.003047310347526e-05,2.7744880488469484e-06,3.416032448128693e-07,3.785328944691601e-08,3.81322629185034e-09,3.5212184686914763e-10,3.001450995589061e-11,2.3756631418375592e-12,1.754992395453949e-13],[0.02029623815875346,0.022490400468171825,0.012460883373123791,0.00460266339434713,0.0013121197252592874,0.00028853896709163206,5.328866750088438e-05,8.435648187862101e-06,1.1684499392797742e-06,1.4386304198544034e-07,1.594156218267733e-08,1.605904927586284e-09,1.482928537984969e-10,1.2640332817453483e-11,1.000488524354217e-12,7.390987893268639e-14],[0.006838058143104023,0.007577299047248579,0.004198228477286055,0.0015506952400491142,0.0004295840032029655,9.797208198205243e-05,1.7953622927036297e-05,2.8420760700668627e-06,3.9366549404898097e-07,4.846926992310555e-08,5.37091298616053e-09,5.410495866888617e-10,4.99617292894057e-11,4.2586872541527875e-12,3.370771789102154e-13,2.490116865688813e-14],[0.0019198565600650776,0.002127406199098437,0.0011786966875819737,0.0004353739566067176,0.00012061021555950879,2.6729801131309567e-05,5.08005855330411e-06,7.979426721933384e-07,1.1052571730226932e-07,1.3608256010119096e-08,1.5079401657936662e-09,1.5190534748123575e-10,1.402727963423254e-11,1.195671123445489e-12,9.463795417294424e-14,6.9912643324662544e-15],[0.0004620170314130959,0.0005119642358510161,0.00028365553753381104,0.00010477354775879261,2.9025071408985347e-05,6.4325760714808e-06,1.18799693123746e-06,1.9352698004484543e-07,2.6598218254944305e-08,3.2748519734680213e-09,3.628885894084428e-10,3.655630277747226e-11,3.3756907834769778e-12,2.8774046691379936e-13,2.2774798677933618e-14,1.6824606899803118e-15],[9.728709635732753e-05,0.00010780449757967854,5.972945094239917e-05,2.206220451512946e-05,6.111819969726402e-06,1.3545099109830208e-06,2.5015695107172227e-07,3.960009003704701e-08,5.644564332411227e-09,6.895867854141986e-10,7.641358383861766e-11,7.69767413097745e-12,7.108204507531027e-13,6.058961602546616e-14,4.7956977402371574e-15,3.5427636674540743e-16],[1.82095819449033e-05,2.0178162430668832e-05,1.117977997271967e-05,4.129463577861286e-06,1.1439717160686627e-06,2.535285782262043e-07,4.682279223234928e-08,7.412093808480119e-09,1.026673987295517e-09,1.3008112667939662e-10,1.430261019922241e-11,1.4408018444538418e-12,1.3304686572780847e-13,1.1340780219954136e-14,8.976283007058693e-16,6.631120439342017e-17],[3.0675186979702197e-06,3.3991384719340725e-06,1.8833043070002616e-06,6.956341324036786e-07,1.927092362475616e-07,4.270848482583421e-08,7.887594075387705e-09,1.2486138571119627e-09,1.7294969551072596e-10,2.129408241654344e-11,2.4281928245597323e-12,2.427121397572321e-13,2.241258198904538e-14,1.9104258120553394e-15,1.5121113733273633e-16,1.1170539772807594e-17],[4.6976621184024427e-07,5.20551155739494e-07,2.884131498945205e-07,1.0653086203591369e-07,2.9511894404603425e-08,6.540466450406448e-09,1.2079226091695069e-09,1.9121533051936987e-10,2.6485877120409384e-11,3.2610201978728674e-12,3.6135588088439186e-13,3.745990594996369e-14,3.432309555446091e-15,2.9256659375048146e-16,2.315678897731176e-17,1.7106797610573361e-18],[6.594589608805385e-08,7.307509897409814e-08,4.048750875220557e-08,1.49548285528468e-08,4.14288697806441e-09,9.181522851894382e-10,1.695684722718898e-10,2.684285501819262e-11,3.718093929193585e-12,4.577828155574168e-13,5.072722722704722e-14,5.110107982718591e-15,4.855937318499121e-16,4.1070570219865823e-17,3.250755718783195e-18,2.4014564461904837e-19],[8.545385607194495e-09,9.469200299951525e-09,5.246442843088965e-09,1.9378730786055457e-09,5.368426066621955e-10,1.1897579362018656e-10,2.197298191916841e-11,3.4783445299187403e-12,4.817971736452562e-13,5.93203052099245e-14,6.5733236357890654e-15,6.621768115551259e-16,6.114688822350796e-17,5.3635860071018054e-18,4.212386635053594e-19,3.111849647805159e-20],[1.0282314243263978e-09,1.1393902813997965e-09,6.312830860031218e-10,2.33176369958165e-10,6.459608301615191e-11,1.4315872373442396e-11,2.6439193658414966e-12,4.1853502167124357e-13,5.797269039288413e-14,7.137770572474184e-15,7.909412442307277e-16,7.96770371050317e-17,7.357555862458767e-18,6.271506174590015e-19,5.10820195906045e-20,3.7443618611644844e-21],[1.1547470372119435e-10,1.2795830982664513e-10,7.089573961247809e-11,2.6186684824714546e-11,7.254411187370979e-12,1.6077325412580777e-12,2.969232394674993e-13,4.700323923293047e-14,6.510576402023857e-15,8.016015875280966e-16,8.882602075524926e-17,8.948065615786429e-18,8.262843978787652e-19,7.043164605388834e-20,5.57469923030787e-21,4.237936282114919e-22]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.14446554767178144, "-10": 5.623150642323695e-08, "-11": 5.586514009267538e-09, "-12": 5.098269445142547e-10, "-13": 4.3007706825527217e-11, "-14": 3.3528383615946815e-12, "-15": 2.2027477160305585e-13, "-2": 0.06776237102113888, "-3": 0.021898601616296528, "-4": 0.005575417924354477, "-5": 0.0011660702234462294, "-6": 0.00020646759427738457, "-7": 3.165499571820429e-05, "-8": 4.275996250993555e-06, "-9": 5.15948356528206e-07, "0": 0.26775966311829863, "1": 0.22075335931882462, "10": 3.6305614393560825e-06, "11": 5.483281844385768e-07, "12": 7.60725661588332e-08, "13": 9.755671628206769e-09, "14": 1.1561897341530428e-09, "15": 1.1547470372119435e-10, "2": 0.15336908500381127, "3": 0.07534791180415694, "4": 0.02916338087247838, "5": 0.009272369999706783, "6": 0.002495879133244643, "7": 0.000581727395542615, "8": 0.00011945935851072684, "9": 2.191263985068701e-05} |
| Raw goal margin distribution | {"-1": 0.1500091349885399, "-10": 1.4707142624561748e-08, "-11": 1.2343262456243989e-09, "-12": 9.509171081259545e-11, "-13": 6.745688884864379e-12, "-14": 4.1049736629603796e-13, "-2": 0.06302504504075372, "-3": 0.017749261275717066, "-4": 0.003890655720383708, "-5": 0.0006957678807281318, "-6": 0.00010489266847324092, "-7": 1.3654682029607614e-05, "-8": 1.5631146884945197e-06, "-9": 1.596165219795867e-07, "0": 0.29408750854590415, "1": 0.23437614709148738, "10": 9.695815736244939e-07, "11": 1.2370624309690959e-07, "12": 1.4488049465757227e-08, "13": 1.5624249715885235e-09, "14": 1.4454026416052207e-10, "2": 0.14565465691324617, "3": 0.062358706375505, "4": 0.02077998463064008, "5": 0.005649270898065814, "6": 0.0012947286659156913, "7": 0.0002562246012202644, "8": 4.4589816343433176e-05, "9": 6.921947287958119e-06} |
| Research history json | {"away": [], "h2h": [], "home": []} |
| Unadjusted home-win probability | 47.0% |
| Unadjusted draw probability | 29.4% |
| Unadjusted away-win probability | 23.5% |
| Raw p over 1 5 | 69.3% |
| Raw p under 3 5 | 78.9% |
| Raw p btts yes | 47.2% |
| P home draw | 75.9% |
| P draw away | 50.9% |
| P home away | 73.2% |
| Raw p home draw | 76.5% |
| Raw p draw away | 53.0% |
| Raw p home away | 70.6% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_MAIN |
| Totals anchor scale | 1.1885 |
| Totals anchor target over 2 5 | 0.5271 |
| Totals anchor reference over odds | 1.84 |
| Totals anchor reference under odds | 2.04 |
| Totals anchor reference last update utc | 2026-11-07T13:53:32Z |
| Totals anchor reference source | live_pinnacle |
| Unanchored p over 2 5 | 0.4267 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -0.0, "market_key": "spreads", "opposite_price": 2.77, "price": 1.49, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 0.0, "market_key": "spreads", "opposite_price": 1.49, "price": 2.77, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 3.85, "price": 1.28, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 3.58, "price": 1.31, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 3.37, "price": 1.34, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 3.18, "price": 1.38, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 2.9, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.79, "price": 1.47, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.25, "price": 1.7, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.7, "price": 2.25, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.47, "price": 2.79, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 1.45, "price": 2.9, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.38, "price": 3.18, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.34, "price": 3.37, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.58, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 1.28, "price": 3.85, "quote_source": "The Odds API", "side": "away"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.77, "draw": 3.71, "home": 2.01}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.86, "under": 2.03}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.85, "home_away": 1.3, "home_draw": 1.3}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 3.9, "draw": 3.71, "home": 1.95}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.84, "under": 2.04}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.26, "under": 3.97}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 1.95 |
| Reference draw odds | 3.71 |
| Reference away odds | 3.90 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / Pinnacle |
| Reference Over 2.5 odds | 1.84 |
| Reference Under 2.5 odds | 2.04 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:32Z |
| Market best over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best under 2 5 last update utc | 2026-11-07T13:53:32Z |
| Home probability edge | -0.9% |
| Draw probability edge | +1.1% |
| Away probability edge | -0.2% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | -0.0296 |
| Raw ev home | -0.0545 |
| Raw edge prob draw | 0.0376 |
| Raw ev draw | 0.0911 |
| Raw edge prob away | -0.0080 |
| Raw ev away | -0.0816 |
| Market p home draw | 74.0% |
| Market home draw odds | 1.30 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T13:53:28Z |
| Market reference home draw last update utc | 2026-11-07T13:53:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 52.0% |
| Market draw away odds | 1.85 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T13:53:28Z |
| Market reference draw away last update utc | 2026-11-07T13:53:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 74.0% |
| Market home away odds | 1.30 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T13:53:28Z |
| Market reference home away last update utc | 2026-11-07T13:53:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 1.30 |
| Market reference dc draw away odds | 1.85 |
| Market reference dc home away odds | 1.30 |
| Market p over 1 5 | 77.7% |
| Market over 1 5 odds | 1.26 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference over 1 5 odds | 1.26 |
| Market reference over 1 5 opposite odds | 3.97 |
| Market reference over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 70.0% |
| Market under 3 5 odds | 1.39 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 3 5 odds | 1.39 |
| Market reference under 3 5 opposite odds | 3.05 |
| Market reference under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,458.4916 |
| Elo away rating | 1,419.5564 |
| Elo rating diff | 98.9351 |
| Elo home expectancy | 0.6387 |
| Research p home | 0.4826 |
| Research p draw | 0.2698 |
| Research p away | 0.2477 |
| Research p over 1 5 | 0.6805 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.4173983120252598, 0.9323657387296929], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:13.090327+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:13.091459+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87aykur+Rizespor%22+%22Erzurum+BB%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.152320+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87aykur+Rizespor_vs_Erzurum+BB&d=2026-11-08"}]}, "form": {"away": {"all": {"matches": 0}, "venue": {"matches": 0}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.4173983120252598, 0.9323657387296929], "h2h": [], "margin_distribution": {"-1": 0.16217655451327295, "-10": 1.4707142624561748e-08, "-11": 1.2343262456243989e-09, "-12": 9.509171081259545e-11, "-13": 6.745688884864379e-12, "-14": 4.1049736629603796e-13, "-2": 0.06302504504075372, "-3": 0.017749261275717066, "-4": 0.003890655720383708, "-5": 0.0006957678807281318, "-6": 0.00010489266847324092, "-7": 1.3654682029607614e-05, "-8": 1.5631146884945197e-06, "-9": 1.596165219795867e-07, "0": 0.26975266949643806, "1": 0.24654356661622043, "10": 9.695815736244939e-07, "11": 1.2370624309690959e-07, "12": 1.4488049465757227e-08, "13": 1.5624249715885235e-09, "14": 1.4454026416052207e-10, "2": 0.14565465691324617, "3": 0.062358706375505, "4": 0.02077998463064008, "5": 0.005649270898065814, "6": 0.0012947286659156913, "7": 0.0002562246012202644, "8": 4.4589816343433176e-05, "9": 6.921947287958119e-06}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.152683+00:00", "p_over_1_5": 0.6804604226195088, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---

## 2026-11-08 — Çorum FK vs Fenerbahce

The model's most likely 1X2 outcome is **Fenerbahce win** at **53.8%**. Expected goals are 1.87 for Çorum FK and 2.27 for Fenerbahce (4.14 combined). The most likely exact score is 1-2 at 11.3%. Goal-market probabilities: at least one goal: 94.9%; Over 2.5 goals: 60.0%; Under 3.5 goals: 63.4%; Double Chance 1X: 46.2%; Double Chance X2: 76.3%; Double Chance 12 (either team wins): 77.5%; Under 4.5 goals: 80.2%; BTTS Yes (both teams score): 60.7%; BTTS No (at least one team does not score): 39.3%.

**Fixture source:** The Odds API

### Match outcome probabilities

| Outcome | Model probability | Model fair odds |
| --- | --- | --- |
| Çorum FK win | 23.7% | 4.22 |
| Draw | 22.5% | 4.45 |
| Fenerbahce win | 53.8% | 1.86 |

### Goals outlook

| Measure | Model estimate |
| --- | --- |
| Çorum FK expected goals | 1.87 |
| Fenerbahce expected goals | 2.27 |
| Expected total goals | 4.14 |
| Over 0.5 | 94.9% |
| Under 0.5 | 5.1% |
| Over 1.5 | 82.1% |
| Under 1.5 | 17.9% |
| Over 2.5 | 60.0% |
| Under 2.5 | 40.0% |
| Over 3.5 | 36.6% |
| Under 3.5 | 63.4% |
| Over 4.5 | 19.8% |
| Under 4.5 | 80.2% |

### 5 most likely scorelines

| Rank | Score | Probability |
| --- | --- | --- |
| 1 | 1-2 | 11.33% |
| 2 | 1-1 | 10.40% |
| 3 | 0-1 | 8.59% |
| 4 | 0-2 | 8.24% |
| 5 | 1-3 | 6.28% |

### Market comparison

| Selection | Model | Market fair | Available odds | Model EV |
| --- | --- | --- | --- | --- |
| Çorum FK win | 23.7% | 20.2% | 4.64 | +10.1% |
| Draw | 22.5% | 23.0% | 4.11 | -7.6% |
| Fenerbahce win | 53.8% | 56.8% | 1.76 | -5.3% |
| Over 2.5 | 60.0% | 59.9% | 1.66 | -0.5% |
| Under 2.5 | 40.0% | 40.1% | 2.33 | -6.7% |

_EV is a model estimate, not a guarantee or a recommendation to bet._

<details>
<summary>Additional technical details</summary>

| Field | Value |
| --- | --- |
| Kickoff utc | 2026-11-08T13:00:00+00:00 |
| Fixture id | 6692a3ca274d09ffbfabd943320d62f5 |
| Odds source | — |
| Odds match method | — |
| Odds event id | — |
| Odds last update utc | — |
| Odds h2h last update utc | — |
| Market best home last update utc | 2026-11-07T13:53:32Z |
| Market best draw last update utc | 2026-11-07T13:53:28Z |
| Market best away last update utc | 2026-11-07T13:53:28Z |
| Odds bookmakers 1x2 | 2.00 |
| Odds bookmakers ou25 | 11.00 |
| Best home bookmaker | Pinnacle |
| Best draw bookmaker | 1xBet |
| Best away bookmaker | 1xBet |
| Best over 2 5 bookmaker | 1xBet |
| Best under 2 5 bookmaker | 1xBet |
| Matched home-team name | Corum |
| Matched away-team name | Fenerbahce |
| Home-name matching confidence | 100/100 |
| Away-name matching confidence | 100/100 |
| Dc lambda home | 1.8741 |
| Dc lambda away | 2.2663 |
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
| P btts yes | 60.7% |
| P btts no | 39.3% |
| Fair Over 0.5 odds | 1.05 |
| Fair Under 0.5 odds | 19.76 |
| Fair Over 1.5 odds | 1.22 |
| Fair Under 1.5 odds | 5.58 |
| Fair Over 2.5 odds | 1.67 |
| Fair Under 2.5 odds | 2.50 |
| Fair Over 3.5 odds | 2.73 |
| Fair Under 3.5 odds | 1.58 |
| Fair Over 4.5 odds | 5.04 |
| Fair Under 4.5 odds | 1.25 |
| Score matrix json | [[0.050604374899397994,0.08589260277192598,0.08235923803402931,0.0456590460488444,0.018984650682681587,0.0063149275814108185,0.0017504628267421543,0.00041590162832034724,8.646421481926801e-05,1.597826651568805e-05,2.657452001871622e-06,4.017986861498683e-07,5.568818128727083e-08,7.124517384870503e-09,8.4637569450103e-10,9.384425531930709e-11],[0.04268574362241861,0.10396780024310091,0.11326740817621381,0.0627941919959745,0.026109301509924722,0.008684823913394526,0.0024073849179125596,0.0005719831875648065,0.000118912920351732,2.197466706325021e-05,3.6547533438850025e-06,5.525876255678736e-07,7.658710924268253e-08,9.798240464017298e-09,1.164007627412291e-09,1.2906257787199136e-10],[0.034965382965099524,0.058153258906765995,0.05421898420777001,0.04317994887813805,0.01795386274760436,0.00597205315771954,0.0016554199422158153,0.000393319891747092,8.176956591888395e-05,1.5110712794362841e-05,2.513163360096667e-06,3.7998268094988945e-07,5.266454359402233e-08,6.737685586576117e-09,8.004209983090093e-10,8.874890077334793e-11],[0.016029119901559315,0.02665909767421651,0.02216926110629063,0.013779621187375423,0.008230558177061578,0.0027377579767715247,0.0007588912945039201,0.0001803089561688867,3.748548035983218e-05,6.927177872486916e-06,1.1521051226981895e-06,1.7419480174266123e-07,2.4142915427869918e-08,3.0887455239382127e-09,3.6693561075613393e-10,4.068500473875862e-11],[0.005511151237961998,0.009165962950711691,0.00762226195455378,0.004225697297436484,0.001969906926487557,0.0009412992326208094,0.0002609229154731697,6.199404166345573e-05,1.2888302836301843e-05,2.3817106080680938e-06,3.96118165701837e-07,5.989186575223148e-08,8.300846151595227e-09,1.0619761922390827e-09,1.261602419777449e-10,1.398836714738699e-11],[0.0015158805051915761,0.002521161903992721,0.0020965562009588943,0.001162307452189151,0.00048327774833673156,0.00018023291624667503,7.176866390438453e-05,1.7051892633310983e-05,3.545017396724539e-06,6.551060792723784e-07,1.0895505842835693e-07,1.647367451794556e-08,2.2832055072491357e-09,2.92103942948246e-10,3.4701252621591385e-11,3.8475977418517825e-12],[0.0003474612361375418,0.0005778859406556455,0.000480560312453482,0.0002664172952461579,0.00011077409021341487,3.684715454008948e-05,1.145143784812565e-05,3.908534790548081e-06,8.125680900153342e-07,1.501595721599652e-07,2.4974039282978026e-08,3.775999026393902e-09,5.233429714201435e-10,6.695435210747082e-11,7.95401754302227e-12,8.819237815680459e-13],[6.826545093085555e-05,0.00011353682144227223,9.441532757376057e-05,5.234280807243351e-05,2.1763703208839735e-05,7.2393330783017735e-06,2.0067028925676155e-06,5.345549451677354e-07,1.5964464897880863e-07,2.9501739586935236e-08,4.906630944415706e-09,7.418677234809968e-10,1.0282080479719407e-10,1.3154471817369821e-11,1.5627199175432955e-12,1.7327091017300131e-13],[1.1735554625523122e-05,1.951818309079398e-05,1.623099560787799e-05,8.998283538908978e-06,3.7414112758107963e-06,1.2445180927438456e-06,3.4497349818688684e-07,8.19640596940404e-08,1.910472491868742e-08,5.071661752020267e-09,8.435018693979785e-10,1.2753492542870705e-10,1.7675986240242046e-11,2.2613931421768644e-12,2.6864811858194364e-13,2.978710612208481e-14],[1.7933033212837106e-06,2.982562280100516e-06,2.480249060240001e-06,1.3750225081891868e-06,5.717228951930122e-07,1.901740906442863e-07,5.271520092522495e-08,1.2524880601343281e-08,2.6038704663740466e-09,5.394909716897414e-10,1.2889503327014557e-10,1.948853826248334e-11,2.7010572438265352e-12,3.4556217937703185e-13,4.105196377015241e-14,4.551750474919196e-15],[2.466302798863615e-07,4.101872567732341e-07,3.411048831811657e-07,1.8910475546434059e-07,7.862818073517965e-08,2.6154353614401377e-08,7.2498414541201605e-09,1.7225277908041378e-09,3.5810634725750516e-10,6.617672605250859e-11,1.2339927055559815e-11,2.6802290439141625e-12,3.714722970329189e-13,4.752464126196485e-14,5.645814176750573e-15,6.259953239804426e-16],[3.083517045935685e-08,5.128402720333646e-08,4.2646941901280665e-08,2.364299052048552e-08,9.83055834423702e-09,3.2699713608805734e-09,9.064178864984083e-10,2.1536057160093327e-10,4.477256509359149e-11,8.273804129855775e-12,1.376071511036009e-12,2.3326825116383143e-13,4.6443654871643016e-14,5.94181061225608e-15,7.058729471586851e-16,7.826562306376674e-17],[3.533928435528604e-09,5.877511922989815e-09,4.887640912247303e-09,2.7096537900254476e-09,1.1266514552145208e-09,3.747618256500812e-10,1.0388189511682936e-10,2.4681843379960548e-11,5.131252351088787e-12,9.482364212330409e-13,1.5770751935945013e-13,2.3844898809067234e-14,3.705284439396723e-15,6.809734847697467e-16,8.089802789066489e-17,8.969793477677359e-18],[3.738583123319775e-10,6.217886774810616e-10,5.170690963537238e-10,2.866573592035212e-10,1.1918974006327413e-10,3.964648017639692e-11,1.098978394688858e-11,2.611120309767675e-12,5.428410278038349e-13,1.0031501050497984e-13,1.668405801233138e-14,2.522578990808345e-15,3.4962243778765986e-16,5.0149113379824935e-17,8.558294467461474e-18,9.48924663503898e-19],[3.6725832440036915e-11,6.108117976524766e-11,5.0794090611915216e-11,2.8159679200775965e-11,1.1708559841377506e-11,3.89465725320736e-12,1.0795773438019539e-12,2.5650243371385006e-13,5.3325786724779575e-14,9.85440779434908e-15,1.6389522414487398e-15,2.478046101350801e-16,3.4345030306735696e-17,4.393962234858875e-18,5.85242152743081e-19,9.321726183559224e-20],[3.367231940536838e-12,5.600267871586672e-12,4.657089381928011e-12,2.581838584460643e-12,1.0735069583499313e-12,3.570841946701999e-13,9.898175406275975e-14,2.3517593210089823e-14,4.889209594012747e-15,9.035078165861728e-16,1.5026840699747777e-16,2.272012757291449e-17,3.1489465415485592e-18,4.028632981127482e-19,4.7859200182911804e-20,5.9495140202409535e-21]] |
| Score matrix version | published-score-matrix-v1 |
| Goal margin distribution | {"-1": 0.25158765928258825, "-10": 3.265922924397176e-06, "-11": 4.855044049570305e-07, "-12": 6.632752775433589e-08, "-13": 8.377273913056142e-09, "-14": 9.754382723730214e-10, "-15": 9.384425531930709e-11, "-2": 0.1661238684956837, "-3": 0.07856498626654011, "-4": 0.029518772637310668, "-5": 0.0091556124182197, "-6": 0.0024115558867091945, "-7": 0.0005511396102072589, "-8": 0.00011113484112174053, "-9": 2.0038243015319453e-05, "0": 0.2247329260299647, "1": 0.12775617717418827, "10": 3.0310067100518485e-07, "11": 3.725898466485952e-08, "12": 4.209093042206042e-09, "13": 4.3959658147915323e-10, "14": 4.2326100311623586e-11, "15": 3.367231940536838e-12, "2": 0.07052742133426988, "3": 0.027581119053244094, "4": 0.008569155318282345, "5": 0.0021977788658612742, "6": 0.000478686080395222, "7": 9.046320440869934e-05, "8": 1.5084032180355618e-05, "9": 2.248970357127321e-06} |
| Raw goal margin distribution | {"-1": 0.1842860717604046, "-10": 2.293162008666449e-05, "-11": 4.581053942673143e-06, "-12": 8.427554828846091e-07, "-13": 1.4363336234812344e-07, "-14": 2.279529663021859e-08, "-15": 3.378449149161052e-09, "-16": 4.6057182164750295e-10, "-17": 4.912702488375257e-11, "-2": 0.13991359496384523, "-3": 0.08143614743500001, "-4": 0.03883768771437488, "-5": 0.015587392895078631, "-6": 0.0053801138362693434, "-7": 0.0016252063364751703, "-8": 0.0004358195266329087, "-9": 0.0001049713691302266, "0": 0.2129383020385642, "1": 0.15125812692817384, "10": 3.4277053689507663e-06, "11": 5.662275900235609e-07, "12": 8.613587754643317e-08, "13": 1.2139329444291877e-08, "14": 1.593094334819528e-09, "15": 1.952407676088843e-10, "16": 2.2009357176776582e-11, "17": 1.9412762149398244e-12, "2": 0.09566953539862497, "3": 0.046045568988887446, "4": 0.018158537364316267, "5": 0.006026398629592097, "6": 0.0017200168951349028, "7": 0.0004296419010573318, "8": 9.527121019960858e-05, "9": 1.8975041467562877e-05} |
| Research history json | {"away": [{"away": "Goztep", "away_goals": 2.0, "away_xg": 1.4, "date": "2026-10-31T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 1.51, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 0.31, "date": "2026-10-26T00:00:00+00:00", "home": "Galatasaray", "home_goals": 2.0, "home_xg": 2.27, "source": "pipeline training history"}, {"away": "Alanyaspor", "away_goals": 0.0, "away_xg": 0.96, "date": "2026-10-17T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 3.0, "home_xg": 3.84, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 3.0, "away_xg": 0.96, "date": "2026-10-10T00:00:00+00:00", "home": "Rizespor", "home_goals": 0.0, "home_xg": 1.52, "source": "pipeline training history"}, {"away": "Eyupspor", "away_goals": 0.0, "away_xg": 0.72, "date": "2026-09-20T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 8.0, "home_xg": 5.14, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 0.0, "away_xg": 1.33, "date": "2026-09-14T00:00:00+00:00", "home": "Gaziantep", "home_goals": 0.0, "home_xg": 0.49, "source": "pipeline training history"}, {"away": "Besiktas", "away_goals": 2.0, "away_xg": 1.75, "date": "2026-09-05T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 1.0, "home_xg": 0.59, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 2.0, "away_xg": 1.56, "date": "2026-08-30T00:00:00+00:00", "home": "Samsunspor", "home_goals": 0.0, "home_xg": 0.46, "source": "pipeline training history"}, {"away": "Konyaspor", "away_goals": 2.0, "away_xg": 2.15, "date": "2026-08-22T00:00:00+00:00", "home": "Fenerbahce", "home_goals": 4.0, "home_xg": 2.36, "source": "pipeline training history"}, {"away": "Fenerbahce", "away_goals": 1.0, "away_xg": 2.9, "date": "2026-08-15T00:00:00+00:00", "home": "Genclerbirligi", "home_goals": 2.0, "home_xg": 1.19, "source": "pipeline training history"}], "h2h": [], "home": []} |
| Unadjusted home-win probability | 31.9% |
| Unadjusted draw probability | 21.3% |
| Unadjusted away-win probability | 46.8% |
| Raw p over 1 5 | 92.5% |
| Raw p under 3 5 | 40.7% |
| Raw p btts yes | 76.5% |
| P home draw | 46.2% |
| P draw away | 76.3% |
| P home away | 77.5% |
| Raw p home draw | 53.2% |
| Raw p draw away | 68.1% |
| Raw p home away | 78.7% |
| Market blending weight | 70.0% |
| Market blend applied | Yes |
| Totals anchor applied | 1 |
| Totals anchor status | ANCHORED_ALTERNATE |
| Totals anchor scale | 0.7339 |
| Totals anchor target over 2 5 | 0.5995 |
| Totals anchor reference over odds | 1.62 |
| Totals anchor reference under odds | 2.37 |
| Totals anchor reference last update utc | 2026-11-07T13:53:32Z |
| Totals anchor reference source | live_pinnacle_alternate |
| Unanchored p over 2 5 | 0.7790 |
| Model version | dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2 |
| Bet365 pinnacle quotes | [] |
| Asian handicap offers | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": 1.5, "market_key": "spreads", "opposite_price": 2.94, "price": 1.45, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "line": -1.5, "market_key": "spreads", "opposite_price": 1.45, "price": 2.94, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 4.06, "price": 1.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.75, "market_key": "alternate_spreads", "opposite_price": 3.59, "price": 1.31, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.0, "market_key": "alternate_spreads", "opposite_price": 3.55, "price": 1.32, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.5, "market_key": "alternate_spreads", "opposite_price": 2.92, "price": 1.43, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 2.65, "price": 1.52, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.25, "market_key": "alternate_spreads", "opposite_price": 2.6, "price": 1.53, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 1.0, "market_key": "alternate_spreads", "opposite_price": 2.26, "price": 1.69, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.5, "market_key": "alternate_spreads", "opposite_price": 2.21, "price": 1.72, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.75, "market_key": "alternate_spreads", "opposite_price": 1.96, "price": 1.93, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.75, "market_key": "alternate_spreads", "opposite_price": 1.93, "price": 1.96, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.5, "market_key": "alternate_spreads", "opposite_price": 1.72, "price": 2.21, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.0, "market_key": "alternate_spreads", "opposite_price": 1.69, "price": 2.26, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.25, "market_key": "alternate_spreads", "opposite_price": 1.53, "price": 2.6, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": 0.25, "market_key": "alternate_spreads", "opposite_price": 1.52, "price": 2.65, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.5, "market_key": "alternate_spreads", "opposite_price": 1.43, "price": 2.92, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.0, "market_key": "alternate_spreads", "opposite_price": 1.32, "price": 3.55, "quote_source": "The Odds API", "side": "home"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -1.75, "market_key": "alternate_spreads", "opposite_price": 1.31, "price": 3.59, "quote_source": "The Odds API", "side": "away"}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "line": -0.25, "market_key": "alternate_spreads", "opposite_price": 1.26, "price": 4.06, "quote_source": "The Odds API", "side": "home"}] |
| Price edge quotes | [{"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.76, "draw": 4.11, "home": 4.54}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "totals", "market_key": "totals", "point": 2.5, "prices": {"over": 1.66, "under": 2.33}}, {"bookmaker": "1xBet", "last_update_utc": "2026-11-07T13:53:28Z", "market": "double_chance", "market_key": "double_chance", "point": null, "prices": {"draw_away": 1.23, "home_away": 1.26, "home_draw": 2.13}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "h2h", "market_key": "h2h", "point": null, "prices": {"away": 1.72, "draw": 4.1, "home": 4.64}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 2.5, "prices": {"over": 1.62, "under": 2.37}}, {"bookmaker": "Pinnacle", "last_update_utc": "2026-11-07T13:53:32Z", "market": "totals", "market_key": "alternate_totals", "point": 1.5, "prices": {"over": 1.19, "under": 4.85}}] |
| 1X2 market source | The Odds API / Pinnacle |
| Reference home odds | 4.64 |
| Reference draw odds | 4.10 |
| Reference away odds | 1.72 |
| Market reference 1x2 last update utc | 2026-11-07T13:53:32Z |
| Market reference home last update utc | 2026-11-07T13:53:32Z |
| Market reference draw last update utc | 2026-11-07T13:53:32Z |
| Market reference away last update utc | 2026-11-07T13:53:32Z |
| O/U 2.5 market source | The Odds API / Matchbook |
| Reference Over 2.5 odds | 1.64 |
| Reference Under 2.5 odds | 2.42 |
| Market reference over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market reference under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best over 2 5 last update utc | 2026-11-07T13:53:28Z |
| Market best under 2 5 last update utc | 2026-11-07T13:53:28Z |
| Home probability edge | +3.5% |
| Draw probability edge | -0.5% |
| Away probability edge | -3.0% |
| Over 2.5 probability edge | +0.0% |
| Under 2.5 probability edge | -0.0% |
| Raw edge prob home | 0.1174 |
| Raw ev home | 0.4821 |
| Raw edge prob draw | -0.0168 |
| Raw ev draw | -0.1248 |
| Raw edge prob away | -0.1006 |
| Raw ev away | -0.1770 |
| Market p home draw | 45.2% |
| Market home draw odds | 2.13 |
| Best home draw bookmaker | 1xBet |
| Market best home draw last update utc | 2026-11-07T13:53:28Z |
| Market reference home draw last update utc | 2026-11-07T13:53:28Z |
| Market home draw bookmakers | 1 |
| Market reference home draw method | proportional_overlap_sum_two |
| Market p draw away | 78.3% |
| Market draw away odds | 1.23 |
| Best draw away bookmaker | 1xBet |
| Market best draw away last update utc | 2026-11-07T13:53:28Z |
| Market reference draw away last update utc | 2026-11-07T13:53:28Z |
| Market draw away bookmakers | 1 |
| Market reference draw away method | proportional_overlap_sum_two |
| Market p home away | 76.5% |
| Market home away odds | 1.26 |
| Best home away bookmaker | 1xBet |
| Market best home away last update utc | 2026-11-07T13:53:28Z |
| Market reference home away last update utc | 2026-11-07T13:53:28Z |
| Market home away bookmakers | 1 |
| Market reference home away method | proportional_overlap_sum_two |
| Market reference dc home draw odds | 2.13 |
| Market reference dc draw away odds | 1.23 |
| Market reference dc home away odds | 1.26 |
| Market p over 1 5 | 82.5% |
| Market over 1 5 odds | 1.19 |
| Best over 1 5 bookmaker | Pinnacle |
| Market best over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference over 1 5 odds | 1.19 |
| Market reference over 1 5 opposite odds | 4.85 |
| Market reference over 1 5 last update utc | 2026-11-07T13:53:32Z |
| Market over 1 5 bookmakers | 1 |
| Market p under 3 5 | 62.7% |
| Market under 3 5 odds | 1.55 |
| Best under 3 5 bookmaker | Pinnacle |
| Market best under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market reference under 3 5 odds | 1.55 |
| Market reference under 3 5 opposite odds | 2.53 |
| Market reference under 3 5 last update utc | 2026-11-07T13:53:32Z |
| Market under 3 5 bookmakers | 1 |
| Training data status | RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED |
| Training cutoff | 2026-11-02 |
| Elo home rating | 1,445.1258 |
| Elo away rating | 1,661.7220 |
| Elo rating diff | -156.5962 |
| Elo home expectancy | 0.2888 |
| Research p home | 0.3260 |
| Research p draw | 0.1999 |
| Research p away | 0.4742 |
| Research p over 1 5 | 0.9182 |
| Research probability basis | team_form_poisson_v1 |
| Team research json | {"base_rates": [1.8740576142222731, 2.2663452166092246], "coverage": {"training_cache": "RESULT_DATE_ONLY_NOT_COMPLETENESS_VERIFIED"}, "evidence": {"coverage": {}, "errors": ["free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"], "news": [], "review_links": [{"label": "Sofascore", "status": "reference only; no authorized public bulk API", "url": "https://www.sofascore.com/football"}, {"label": "Sports Mole previews", "status": "reference only; article reproduction requires permission", "url": "https://www.sportsmole.co.uk/football/"}], "sources": [{"observed_at_utc": "2026-11-07T13:54:13.090327+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/scoreboard?dates=20261108"}, {"observed_at_utc": "2026-11-07T13:54:12.951430+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://site.api.espn.com/apis/site/v2/sports/soccer/tur.1/news?limit=20"}, {"observed_at_utc": "2026-11-07T13:54:13.158375+00:00", "reason": "free research request budget reached", "status": "unavailable", "url": "https://www.bing.com/news/search?q=%22%C3%87orum+FK%22+%22Fenerbahce%22+injury+suspension+lineup+preview&format=rss"}, {"observed_at_utc": "2026-11-07T13:53:41.045208+00:00", "reason": null, "status": "available", "url": "https://feeds.bbci.co.uk/sport/football/rss.xml"}, {"observed_at_utc": "2026-11-07T13:53:41.166595+00:00", "reason": null, "status": "available", "url": "https://www.theguardian.com/football/rss"}, {"observed_at_utc": "2026-11-07T13:54:13.219425+00:00", "reason": "TheSportsDB free source limit: 30 requests per minute", "status": "unavailable", "url": "https://www.thesportsdb.com/api/v1/json/123/searchevents.php?e=%C3%87orum+FK_vs_Fenerbahce&d=2026-11-08"}]}, "form": {"away": {"all": {"goals_against": 1.0089728918892988, "goals_for": 2.3331960885564245, "last_match": "2026-10-31T00:00:00+00:00", "matches": 10, "points_per_game": 1.4847509690034097, "results": "LLWWWDLWWL", "xg_against": 1.3380003484001706, "xg_for": 1.9676008712062978, "xg_matches": 10}, "venue": {"goals_against": 0.8151944568095735, "goals_for": 1.425370020202056, "last_match": "2026-10-26T00:00:00+00:00", "matches": 5, "points_per_game": 1.384791003310632, "results": "LWDWL", "xg_against": 1.2819506533747527, "xg_for": 1.2552734770676013, "xg_matches": 5}}, "home": {"all": {"matches": 0}, "venue": {"matches": 0}}}, "goal_rates": [1.8740576142222731, 2.2663452166092246], "h2h": [], "margin_distribution": {"-1": 0.19081083452421982, "-10": 2.293162008666449e-05, "-11": 4.581053942673143e-06, "-12": 8.427554828846091e-07, "-13": 1.4363336234812344e-07, "-14": 2.279529663021859e-08, "-15": 3.378449149161052e-09, "-16": 4.6057182164750295e-10, "-17": 4.912702488375257e-11, "-2": 0.13991359496384523, "-3": 0.08143614743500001, "-4": 0.03883768771437488, "-5": 0.015587392895078631, "-6": 0.0053801138362693434, "-7": 0.0016252063364751703, "-8": 0.0004358195266329087, "-9": 0.0001049713691302266, "0": 0.19988877651093376, "1": 0.15778288969198903, "10": 3.4277053689507663e-06, "11": 5.662275900235609e-07, "12": 8.613587754643317e-08, "13": 1.2139329444291877e-08, "14": 1.593094334819528e-09, "15": 1.952407676088843e-10, "16": 2.2009357176776582e-11, "17": 1.9412762149398244e-12, "2": 0.09566953539862497, "3": 0.046045568988887446, "4": 0.018158537364316267, "5": 0.006026398629592097, "6": 0.0017200168951349028, "7": 0.0004296419010573318, "8": 9.527121019960858e-05, "9": 1.8975041467562877e-05}, "model_note": "Poisson team rates with ten-match shrinkage; qualitative context has no fitted coefficient", "observed_at_utc": "2026-11-07T13:54:13.219801+00:00", "p_over_1_5": 0.9181830940588468, "version": "team-form-research-v1", "warnings": ["form unavailable or unconfirmed", "venue_splits unavailable or unconfirmed", "xg unavailable or unconfirmed", "availability unavailable or unconfirmed", "lineups unavailable or unconfirmed", "rotation unavailable or unconfirmed", "h2h unavailable or unconfirmed", "tactics unavailable or unconfirmed", "motivation unavailable or unconfirmed", "rivalry unavailable or unconfirmed", "weather unavailable or unconfirmed", "travel unavailable or unconfirmed", "free-source fixture identity missing or ambiguous", "TheSportsDB venue: exact fixture identity/time unavailable", "weather unavailable: verified venue coordinates/location missing"]} |

</details>


---
