# Eredivisie and Primeira Liga reliability validation (2026-10-24)

**Decision: both leagues stay `shortlist_validated=False`.** Each fails the draw / Double Chance 12 calibration check that all five existing domestic leagues pass. No threshold was changed.

> **Update (2026-10-24):** the league-level bar was replaced with per-market approval (`shortlist_approval=PER_MARKET_APPROVAL`). Each market below now qualifies or stays blocked on its own audit result:
> - **Eredivisie:** Home win, Away win, DC 1X, DC X2 and all 50 Asian-handicap lines may qualify. Draw, DC 12, Over 1.5, Under 3.5 and BTTS stay blocked.
> - **Primeira Liga:** every market except Draw and DC 12 may qualify.
>
> Thresholds are unchanged, and a qualifying market must still pass every quote, identity, timing and high-confidence check.

## Method

The production code path ran unchanged: `football_value_pipeline_v2_standalone.py --leagues Eredivisie PrimeiraLiga --tune-half-life`. It used validator v9 and the same settings recorded in the existing five leagues' reports: `min_train=500`, 56-day walk-forward steps, a 75% development / 25% audit split by date, market weight 0.5, l2 0.08, max goals 10, and power de-vig.

Inputs were six football-data.co.uk seasons per league (2021/22 to 2026/27), downloaded on 2026-10-24 and passed by the refresh validator. Eredivisie had 1,611 matches to 2026-10-18 and a tuned half-life of 365 days. Primeira Liga had 1,602 matches to 2026-10-19 and a tuned half-life of 730 days. The run was offline for odds (`--no-live-odds`, football-data.co.uk fixtures), wrote to a scratch directory, and spent no Odds API credits.

The existing-league figures are their committed reports in `football_output_v2/raw/` (training ends 2026-10-18 to 2026-10-21).

A market is `RELIABLE_FOR_RANKING` when it has at least 30 development and 12 audit matches, audit |overconfidence| ≤ 0.12, and audit Brier ≤ the constant-frequency baseline + 0.005. An Asian-handicap line needs at least 80 development and 40 audit matches, audit Brier ≤ reference + 0.01, and overconfidence ≤ 0.10. The confidence penalty is the development overconfidence, shrunk by n/(n+100); for Asian handicap it is the upper 95% bound of the development residual.

## Market status

| market | EPL | LaLiga | Bundesliga | SerieA | Ligue1 | Eredivisie | PrimeiraLiga |
|---|---|---|---|---|---|---|---|
| home_draw | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| draw_away | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| home_away | PASS | PASS | PASS | PASS | PASS | FAIL-audit | FAIL-audit |
| home | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| draw | PASS | PASS | PASS | PASS | PASS | FAIL-audit | FAIL-audit |
| away | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| over_1_5 | FAIL-audit | PASS | FAIL-audit | PASS | PASS | FAIL-audit | PASS |
| under_3_5 | FAIL-audit | PASS | FAIL-audit | PASS | PASS | FAIL-audit | PASS |
| btts_yes | FAIL-audit | FAIL-audit | FAIL-audit | PASS | FAIL-audit | FAIL-audit | PASS |

The league-level bar the existing five clear together: every 1X2 and double-chance market plus all 50 Asian-handicap lines. Goal markets vary among them; EPL and Bundesliga fail all three.

## Eredivisie

| market | status | dev n | audit n | audit log loss | old-5 LL range | audit Brier | baseline Brier | Brier excess (limit +0.005) | audit overconf (limit ±0.12) | penalty | 75+/85+ |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| home_draw | PASS | 397 | 135 | 0.5242 | 0.5245–0.5955 | 0.1762 | 0.2291 | -0.0529 | +0.0365 | 0.0000 | PASSED/PASSED |
| draw_away | PASS | 397 | 135 | 0.5954 | 0.5800–0.6345 | 0.2027 | 0.2291 | -0.0265 | -0.1045 | 0.0000 | PASSED/INSUFF |
| home_away | FAIL-audit | 397 | 135 | 0.6183 | 0.5143–0.6044 | 0.2109 | 0.2054 | +0.0055 | +0.0680 | 0.0388 | PASSED/INSUFF |
| home | PASS | 397 | 135 | 0.5954 | 0.5800–0.6345 | 0.2027 | 0.2291 | -0.0265 | +0.1045 | 0.0078 | INSUFF/INSUFF |
| draw | FAIL-audit | 397 | 135 | 0.6183 | 0.5143–0.6044 | 0.2109 | 0.2054 | +0.0055 | -0.0680 | 0.0000 | INSUFF/INSUFF |
| away | PASS | 397 | 135 | 0.5242 | 0.5245–0.5955 | 0.1762 | 0.2291 | -0.0529 | -0.0365 | 0.0309 | INSUFF/INSUFF |
| over_1_5 | FAIL-audit | 397 | 135 | 0.3437 | 0.4675–0.5723 | 0.0950 | 0.0870 | +0.0079 | -0.0830 | 0.0000 | PASSED/PASSED |
| under_3_5 | FAIL-audit | 397 | 135 | 0.7434 | 0.5347–0.7312 | 0.2730 | 0.2497 | +0.0234 | +0.1377 | 0.0051 | INSUFF/INSUFF |
| btts_yes | FAIL-audit | 397 | 135 | 0.6592 | 0.6696–0.7154 | 0.2335 | 0.2246 | +0.0089 | -0.0816 | 0.0000 | INSUFF/INSUFF |

## Primeira Liga

| market | status | dev n | audit n | audit log loss | old-5 LL range | audit Brier | baseline Brier | Brier excess (limit +0.005) | audit overconf (limit ±0.12) | penalty | 75+/85+ |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| home_draw | PASS | 396 | 134 | 0.5540 | 0.5245–0.5955 | 0.1887 | 0.2179 | -0.0292 | -0.0097 | 0.0039 | PASSED/PASSED |
| draw_away | PASS | 396 | 134 | 0.5926 | 0.5800–0.6345 | 0.2039 | 0.2391 | -0.0351 | -0.0510 | 0.0000 | PASSED/PASSED |
| home_away | FAIL-audit | 396 | 134 | 0.6168 | 0.5143–0.6044 | 0.2082 | 0.2032 | +0.0050 | +0.0608 | 0.0148 | HIGH_CONFIDENCE_OVERESTIMATION/PASSED |
| home | PASS | 396 | 134 | 0.5926 | 0.5800–0.6345 | 0.2039 | 0.2391 | -0.0351 | +0.0510 | 0.0187 | PASSED/INSUFF |
| draw | FAIL-audit | 396 | 134 | 0.6168 | 0.5143–0.6044 | 0.2082 | 0.2032 | +0.0050 | -0.0608 | 0.0000 | INSUFF/INSUFF |
| away | PASS | 396 | 134 | 0.5540 | 0.5245–0.5955 | 0.1887 | 0.2179 | -0.0292 | +0.0097 | 0.0000 | INSUFF/INSUFF |
| over_1_5 | PASS | 396 | 134 | 0.5622 | 0.4675–0.5723 | 0.1890 | 0.1965 | -0.0075 | +0.0017 | 0.0000 | PASSED/INSUFF |
| under_3_5 | PASS | 396 | 134 | 0.6485 | 0.5347–0.7312 | 0.2259 | 0.2254 | +0.0004 | +0.0610 | 0.0060 | HIGH_CONFIDENCE_OVERESTIMATION/INSUFF |
| btts_yes | PASS | 396 | 134 | 0.6973 | 0.6696–0.7154 | 0.2520 | 0.2491 | +0.0029 | -0.0685 | 0.0000 | INSUFF/INSUFF |

## Existing five: audit Brier excess / overconfidence

| market | EPL | LaLiga | Bundesliga | SerieA | Ligue1 |
|---|---|---|---|---|---|
| home_draw | -0.0130 / -0.027 | -0.0282 / -0.024 | -0.0173 / +0.003 | -0.0295 / +0.046 | -0.0288 / -0.015 |
| draw_away | -0.0249 / -0.020 | -0.0354 / +0.022 | -0.0370 / -0.010 | -0.0452 / +0.002 | -0.0206 / -0.013 |
| home_away | -0.0012 / +0.046 | -0.0079 / +0.002 | -0.0004 / +0.007 | +0.0027 / -0.048 | -0.0025 / +0.028 |
| home | -0.0249 / +0.020 | -0.0354 / -0.022 | -0.0370 / +0.010 | -0.0452 / -0.002 | -0.0206 / +0.013 |
| draw | -0.0012 / -0.046 | -0.0079 / -0.002 | -0.0004 / -0.007 | +0.0027 / +0.048 | -0.0025 / -0.028 |
| away | -0.0130 / +0.027 | -0.0282 / +0.024 | -0.0173 / -0.003 | -0.0295 / -0.046 | -0.0288 / +0.015 |
| over_1_5 | +0.0109 / -0.004 | -0.0013 / -0.033 | +0.0119 / -0.026 | +0.0004 / -0.024 | +0.0013 / -0.028 |
| under_3_5 | +0.0151 / +0.014 | -0.0173 / +0.045 | +0.0167 / +0.129 | -0.0034 / -0.021 | +0.0016 / +0.043 |
| btts_yes | +0.0098 / -0.020 | +0.0055 / -0.094 | +0.0128 / -0.073 | -0.0087 / +0.007 | +0.0057 / -0.068 |

## Asian handicap profitable-win

| league | version ok | reliable | failed | insufficient | min dev n | min audit n | penalty range | max audit overconf (limit 0.10) |
|---|---|---:|---:|---:|---:|---:|---|---|
| EPL | True | 50 | 0 | 0 | 421 | 230 | 0.010–0.052 | +0.036 |
| LaLiga | True | 50 | 0 | 0 | 427 | 231 | 0.000–0.070 | +0.042 |
| Bundesliga | True | 50 | 0 | 0 | 335 | 189 | 0.000–0.113 | +0.050 |
| SerieA | True | 50 | 0 | 0 | 423 | 229 | 0.000–0.077 | +0.039 |
| Ligue1 | True | 50 | 0 | 0 | 373 | 203 | 0.000–0.094 | +0.022 |
| Eredivisie | True | 50 | 0 | 0 | 344 | 188 | 0.000–0.081 | +0.059 |
| PrimeiraLiga | True | 50 | 0 | 0 | 343 | 187 | 0.018–0.073 | +0.044 |

Both new leagues pass all 50 lines on the same version and net-profit basis as the existing leagues.

## Why each failure fails

`draw` and `home_away` (Double Chance 12) are exact complements, so they fail together.

- **Eredivisie draw / DC 12:** audit Brier excess is +0.00548 (limit +0.005). The model under-forecasts draws: audit mean forecast 0.169 vs observed 0.278 (n=36), and 0.240 vs 0.293 (n=99).
- **Primeira Liga draw / DC 12:** audit Brier excess is +0.00505 (limit +0.005). Draw forecasts are 0.140 vs observed 0.200 (n=40), and 0.258 vs 0.319 (n=94).
- **Eredivisie over 1.5 / under 3.5 / BTTS:** Brier excess is +0.0079, +0.0234 and +0.0089. Under 3.5 also exceeds the overconfidence limit (+0.138 > 0.12).

The Primeira Liga DC 12 margin is very small (0.00005). Rounding it into a pass would loosen the check, so it stays failed.

## Calibration bins

Mean forecast → observed frequency (n), by 0.2-wide probability bin.

- **Eredivisie home_draw** dev: 0.0-0.2: 0.187->0.667 (3), 0.2-0.4: 0.320->0.290 (31), 0.4-0.6: 0.510->0.629 (89), 0.6-0.8: 0.704->0.709 (158), 0.8-1.0: 0.884->0.914 (116)
  audit: 0.0-0.2: 0.181->1.000 (1), 0.2-0.4: 0.347->0.308 (13), 0.4-0.6: 0.508->0.393 (28), 0.6-0.8: 0.705->0.622 (45), 0.8-1.0: 0.860->0.896 (48)
- **Eredivisie draw_away** dev: 0.0-0.2: 0.136->0.125 (24), 0.2-0.4: 0.304->0.359 (78), 0.4-0.6: 0.510->0.524 (126), 0.6-0.8: 0.692->0.693 (127), 0.8-1.0: 0.857->0.810 (42)
  audit: 0.0-0.2: 0.167->0.250 (4), 0.2-0.4: 0.327->0.371 (35), 0.4-0.6: 0.484->0.667 (39), 0.6-0.8: 0.692->0.805 (41), 0.8-1.0: 0.847->0.875 (16)
- **Eredivisie home_away** dev: 0.6-0.8: 0.752->0.710 (290), 0.8-1.0: 0.851->0.785 (107)
  audit: 0.6-0.8: 0.760->0.707 (99), 0.8-1.0: 0.831->0.722 (36)
- **Eredivisie home** dev: 0.0-0.2: 0.143->0.190 (42), 0.2-0.4: 0.308->0.307 (127), 0.4-0.6: 0.490->0.476 (126), 0.6-0.8: 0.696->0.641 (78), 0.8-1.0: 0.864->0.875 (24)
  audit: 0.0-0.2: 0.153->0.125 (16), 0.2-0.4: 0.308->0.195 (41), 0.4-0.6: 0.516->0.333 (39), 0.6-0.8: 0.673->0.629 (35), 0.8-1.0: 0.833->0.750 (4)
- **Eredivisie draw** dev: 0.0-0.2: 0.149->0.215 (107), 0.2-0.4: 0.248->0.290 (290)
  audit: 0.0-0.2: 0.169->0.278 (36), 0.2-0.4: 0.240->0.293 (99)
- **Eredivisie away** dev: 0.0-0.2: 0.116->0.086 (116), 0.2-0.4: 0.296->0.291 (158), 0.4-0.6: 0.490->0.371 (89), 0.6-0.8: 0.680->0.710 (31), 0.8-1.0: 0.813->0.333 (3)
  audit: 0.0-0.2: 0.140->0.104 (48), 0.2-0.4: 0.295->0.378 (45), 0.4-0.6: 0.492->0.607 (28), 0.6-0.8: 0.653->0.692 (13), 0.8-1.0: 0.819->0.000 (1)
- **Eredivisie over_1_5** dev: 0.6-0.8: 0.745->0.826 (178), 0.8-1.0: 0.853->0.868 (219)
  audit: 0.6-0.8: 0.762->0.936 (47), 0.8-1.0: 0.852->0.886 (88)
- **Eredivisie under_3_5** dev: 0.2-0.4: 0.326->0.312 (16), 0.4-0.6: 0.530->0.558 (113), 0.6-0.8: 0.685->0.671 (255), 0.8-1.0: 0.822->0.692 (13)
  audit: 0.2-0.4: 0.330->0.500 (4), 0.4-0.6: 0.538->0.500 (46), 0.6-0.8: 0.675->0.464 (84), 0.8-1.0: 0.812->1.000 (1)
- **Eredivisie btts_yes** dev: 0.2-0.4: 0.370->0.444 (9), 0.4-0.6: 0.531->0.623 (292), 0.6-0.8: 0.633->0.615 (96)
  audit: 0.4-0.6: 0.545->0.689 (90), 0.6-0.8: 0.642->0.600 (45)
- **PrimeiraLiga home_draw** dev: 0.0-0.2: 0.172->0.200 (5), 0.2-0.4: 0.304->0.151 (53), 0.4-0.6: 0.522->0.528 (53), 0.6-0.8: 0.702->0.710 (186), 0.8-1.0: 0.896->0.939 (99)
  audit: 0.0-0.2: 0.154->0.667 (3), 0.2-0.4: 0.286->0.278 (18), 0.4-0.6: 0.513->0.600 (15), 0.6-0.8: 0.711->0.672 (61), 0.8-1.0: 0.892->0.919 (37)
- **PrimeiraLiga draw_away** dev: 0.0-0.2: 0.150->0.118 (34), 0.2-0.4: 0.298->0.234 (47), 0.4-0.6: 0.524->0.548 (135), 0.6-0.8: 0.677->0.759 (116), 0.8-1.0: 0.880->0.891 (64)
  audit: 0.0-0.2: 0.158->0.231 (13), 0.2-0.4: 0.299->0.500 (16), 0.4-0.6: 0.511->0.528 (53), 0.6-0.8: 0.675->0.714 (28), 0.8-1.0: 0.888->0.917 (24)
- **PrimeiraLiga home_away** dev: 0.6-0.8: 0.734->0.701 (291), 0.8-1.0: 0.856->0.876 (105)
  audit: 0.6-0.8: 0.742->0.681 (94), 0.8-1.0: 0.860->0.800 (40)
- **PrimeiraLiga home** dev: 0.0-0.2: 0.120->0.109 (64), 0.2-0.4: 0.323->0.241 (116), 0.4-0.6: 0.476->0.452 (135), 0.6-0.8: 0.702->0.766 (47), 0.8-1.0: 0.850->0.882 (34)
  audit: 0.0-0.2: 0.112->0.083 (24), 0.2-0.4: 0.325->0.286 (28), 0.4-0.6: 0.489->0.472 (53), 0.6-0.8: 0.701->0.500 (16), 0.8-1.0: 0.842->0.769 (13)
- **PrimeiraLiga draw** dev: 0.0-0.2: 0.144->0.124 (105), 0.2-0.4: 0.266->0.299 (291)
  audit: 0.0-0.2: 0.140->0.200 (40), 0.2-0.4: 0.258->0.319 (94)
- **PrimeiraLiga away** dev: 0.0-0.2: 0.104->0.061 (99), 0.2-0.4: 0.298->0.290 (186), 0.4-0.6: 0.478->0.472 (53), 0.6-0.8: 0.696->0.849 (53), 0.8-1.0: 0.828->0.800 (5)
  audit: 0.0-0.2: 0.108->0.081 (37), 0.2-0.4: 0.289->0.328 (61), 0.4-0.6: 0.487->0.400 (15), 0.6-0.8: 0.714->0.722 (18), 0.8-1.0: 0.846->0.333 (3)
- **PrimeiraLiga over_1_5** dev: 0.4-0.6: 0.577->0.571 (28), 0.6-0.8: 0.703->0.746 (299), 0.8-1.0: 0.846->0.870 (69)
  audit: 0.4-0.6: 0.585->0.500 (4), 0.6-0.8: 0.707->0.710 (100), 0.8-1.0: 0.841->0.833 (30)
- **PrimeiraLiga under_3_5** dev: 0.2-0.4: 0.354->0.800 (5), 0.4-0.6: 0.542->0.605 (38), 0.6-0.8: 0.720->0.698 (242), 0.8-1.0: 0.831->0.811 (111)
  audit: 0.4-0.6: 0.549->0.474 (19), 0.6-0.8: 0.727->0.691 (94), 0.8-1.0: 0.830->0.667 (21)
- **PrimeiraLiga btts_yes** dev: 0.2-0.4: 0.371->0.377 (69), 0.4-0.6: 0.472->0.511 (321), 0.6-0.8: 0.621->0.500 (6)
  audit: 0.2-0.4: 0.365->0.526 (19), 0.4-0.6: 0.473->0.527 (112), 0.6-0.8: 0.621->0.667 (3)

## Outlook

Draw market, development vs audit (mean forecast vs observed draw rate):

| League | Development | Audit | Audit Brier excess |
|---|---|---|---|
| EPL | 0.235 vs 0.245 (n=486) | 0.251 vs 0.297 (n=165) | −0.0012 |
| LaLiga | 0.251 vs 0.251 (n=490) | 0.248 vs 0.250 (n=168) | −0.0079 |
| Eredivisie | 0.221 vs 0.270 (n=397) | 0.221 vs 0.289 (n=135) | +0.0055 |
| Primeira Liga | 0.234 vs 0.253 (n=396) | 0.223 vs 0.284 (n=134) | +0.0050 |

- **Eredivisie** under-forecasts draws by 5–7 points in both phases. That points to a persistent model bias, not sampling noise, so more history alone is unlikely to make this market pass. A league-specific draw calibration, tested first as a walk-forward paper experiment, is the likely route.
- **Primeira Liga** is close in development (2 points) and drifts only in the recent audit window, missing the limit by 0.00005. With about 134 audit matches, one matchweek moves the audit Brier by far more than that margin. A single passing run would therefore be weak evidence. A pre-agreed rule, such as several consecutive passing weekly runs, would separate a real pass from noise.

## Re-evaluation

This validation reruns automatically with each scheduled forecast. Under per-market approval, a market's eligibility follows its latest audit result: a market that later fails is blocked again, and draw/DC 12 qualifies only once it passes.
