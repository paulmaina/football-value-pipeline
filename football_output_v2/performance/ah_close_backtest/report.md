# Asian handicap backtest: production model vs Pinnacle close

Read-only walk-forward backtest. No production model, policy, threshold or workflow was changed, and nothing here is a recommendation to change production.

Matches scored: 9465 (half closing lines: 2323). Leagues: E0, SP1, D1, I1, F1, N1, P1, T1; seasons 2223-2526 scored, 2122 warm-up only. Weekly refits on matches dated strictly before the refit date.

## Variants

- `dc`: Dixon-Coles hl480 + gated CSV shots (no odds inputs)
- `blend70`: dc + 0.70 Pinnacle opening 1X2 blend
- `prod`: blend70 + Pinnacle opening O/U 2.5 anchor (production replica)

## Sign convention check (AHh/AHCh = home handicap)

| date | match | score | AHh | AHCh | PSCH | PSCA | home AH result |
|---|---|---|---|---|---|---|---|
| 2024-04-13 | Man City v Luton | 5-1 | -2.5000 | -2.7500 | 1.0800 | 26.0000 | WON |
| 2023-08-27 | Sheffield United v Man City | 1-2 | 2.0000 | 1.7500 | 16.0000 | 1.2000 | WON |
| 2023-08-19 | Almeria v Real Madrid | 1-3 | 1.2500 | 1.2500 | 6.8700 | 1.4400 | LOST |

## Verdict

- **dc**: half-line log-loss gain vs close -0.0188 [-0.0264, -0.0112] -> close better; all-line return skill -0.0401 [-0.0468, -0.0334] -> close better; simulated CLV (same line) -0.0250 [-0.0264, -0.0234].
  - Breakdown cells where the model's 95% interval excludes zero in its favour: none (out of 22 cells; ~0.6 expected by chance alone).
- **blend70**: half-line log-loss gain vs close -0.0059 [-0.0099, -0.0017] -> close better; all-line return skill -0.0142 [-0.0181, -0.0103] -> close better; simulated CLV (same line) -0.0248 [-0.0267, -0.0227].
  - Breakdown cells where the model's 95% interval excludes zero in its favour: none (out of 22 cells; ~0.6 expected by chance alone).
- **prod**: half-line log-loss gain vs close -0.0048 [-0.0086, -0.0011] -> close better; all-line return skill -0.0119 [-0.0155, -0.0084] -> close better; simulated CLV (same line) -0.0247 [-0.0268, -0.0225].
  - Breakdown cells where the model's 95% interval excludes zero in its favour: none (out of 22 cells; ~0.6 expected by chance alone).

## Primary: half closing lines (no push), home covers

Gain = Pinnacle log loss minus model log loss (positive = model better). 95% interval from a paired bootstrap over gameweek blocks.

| variant | n | model LL | Pinnacle LL (prop) | Pinnacle LL (Shin) | model Brier | Pinnacle Brier | LL gain [95%] |
|---|---|---|---|---|---|---|---|
| dc | 2323 | 0.7107 | 0.6919 | 0.6919 | 0.2581 | 0.2494 | -0.0188 [-0.0264, -0.0112] |
| blend70 | 2323 | 0.6977 | 0.6919 | 0.6919 | 0.2522 | 0.2494 | -0.0059 [-0.0099, -0.0017] |
| prod | 2323 | 0.6967 | 0.6919 | 0.6919 | 0.2517 | 0.2494 | -0.0048 [-0.0086, -0.0011] |

Sanity check, half lines unchanged open-to-close (n=1376): Pinnacle open LL 0.6930, close LL 0.6923; dc LL 0.7066, blend70 LL 0.6953, prod LL 0.6946.

## Secondary: all lines, expected vs settled home return per unit at Pinnacle fair close

Skill = mean(R^2) - mean((R - model expected return)^2); Pinnacle predicts zero at its own fair price. Model-side return = 1 unit on the side the model prefers at Pinnacle fair close odds.

| variant | lines | n | return skill [95%] | model-side return [95%] |
|---|---|---|---|---|
| dc | all_lines | 9465 | -0.0401 [-0.0468, -0.0334] | -0.0114 [-0.0302, +0.0079] |
| dc | half | 2323 | -0.0343 [-0.0487, -0.0200] | -0.0042 [-0.0452, +0.0371] |
| dc | quarter | 4933 | -0.0461 [-0.0553, -0.0366] | -0.0252 [-0.0487, -0.0015] |
| dc | whole | 2209 | -0.0329 [-0.0463, -0.0202] | +0.0119 [-0.0238, +0.0498] |
| blend70 | all_lines | 9465 | -0.0142 [-0.0181, -0.0103] | -0.0020 [-0.0197, +0.0152] |
| blend70 | half | 2323 | -0.0114 [-0.0194, -0.0034] | +0.0021 [-0.0374, +0.0432] |
| blend70 | quarter | 4933 | -0.0159 [-0.0214, -0.0105] | -0.0082 [-0.0344, +0.0172] |
| blend70 | whole | 2209 | -0.0132 [-0.0209, -0.0058] | +0.0077 [-0.0269, +0.0416] |
| prod | all_lines | 9465 | -0.0119 [-0.0155, -0.0084] | -0.0010 [-0.0194, +0.0164] |
| prod | half | 2323 | -0.0094 [-0.0169, -0.0022] | +0.0091 [-0.0322, +0.0511] |
| prod | quarter | 4933 | -0.0136 [-0.0187, -0.0089] | -0.0029 [-0.0291, +0.0223] |
| prod | whole | 2209 | -0.0108 [-0.0176, -0.0044] | -0.0076 [-0.0415, +0.0264] |

## Breakdowns (dc, half lines, LL gain [95%])

**league**

| league | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| D1 | 250 | 0.6901 | 0.6923 | +0.0022 [-0.0185, +0.0235] |
| E0 | 325 | 0.7129 | 0.6938 | -0.0191 [-0.0383, -0.0004] |
| F1 | 305 | 0.7125 | 0.6917 | -0.0208 [-0.0467, +0.0030] |
| I1 | 307 | 0.7162 | 0.6902 | -0.0260 [-0.0448, -0.0079] |
| N1 | 263 | 0.7066 | 0.6952 | -0.0114 [-0.0355, +0.0121] |
| P1 | 265 | 0.6985 | 0.6920 | -0.0065 [-0.0317, +0.0179] |
| SP1 | 323 | 0.7107 | 0.6904 | -0.0203 [-0.0389, -0.0029] |
| T1 | 285 | 0.7334 | 0.6898 | -0.0437 [-0.0686, -0.0169] |

**season**

| season | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2223 | 663 | 0.7153 | 0.6900 | -0.0253 [-0.0416, -0.0095] |
| 2324 | 640 | 0.7130 | 0.6929 | -0.0201 [-0.0325, -0.0075] |
| 2425 | 663 | 0.7108 | 0.6920 | -0.0187 [-0.0339, -0.0027] |
| 2526 | 357 | 0.6977 | 0.6931 | -0.0046 [-0.0191, +0.0118] |

**line_bucket**

| line_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| +0.25 to +1 | 566 | 0.7184 | 0.6950 | -0.0234 [-0.0385, -0.0092] |
| -1 to -0.25 | 1150 | 0.7040 | 0.6905 | -0.0134 [-0.0245, -0.0027] |
| <= -1.25 | 443 | 0.7096 | 0.6908 | -0.0188 [-0.0388, +0.0014] |
| >= +1.25 | 164 | 0.7340 | 0.6931 | -0.0410 [-0.0786, -0.0068] |

**home_role**

| home_role | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| away favourite | 730 | 0.7219 | 0.6946 | -0.0274 [-0.0409, -0.0135] |
| home favourite | 1593 | 0.7055 | 0.6906 | -0.0149 [-0.0244, -0.0057] |

**gap_bucket**

| gap_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2-5pp | 617 | 0.6900 | 0.6889 | -0.0012 [-0.0076, +0.0052] |
| 5-10pp | 726 | 0.7037 | 0.6942 | -0.0095 [-0.0204, +0.0018] |
| <2pp | 439 | 0.6938 | 0.6924 | -0.0014 [-0.0036, +0.0007] |
| >=10pp | 541 | 0.7573 | 0.6916 | -0.0656 [-0.0951, -0.0355] |


## Breakdowns (blend70, half lines, LL gain [95%])

**league**

| league | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| D1 | 250 | 0.6890 | 0.6923 | +0.0032 [-0.0081, +0.0146] |
| E0 | 325 | 0.6981 | 0.6938 | -0.0043 [-0.0148, +0.0060] |
| F1 | 305 | 0.6950 | 0.6917 | -0.0033 [-0.0162, +0.0096] |
| I1 | 307 | 0.7008 | 0.6902 | -0.0106 [-0.0204, -0.0004] |
| N1 | 263 | 0.6956 | 0.6952 | -0.0004 [-0.0146, +0.0133] |
| P1 | 265 | 0.6958 | 0.6920 | -0.0038 [-0.0194, +0.0108] |
| SP1 | 323 | 0.7014 | 0.6904 | -0.0110 [-0.0210, -0.0017] |
| T1 | 285 | 0.7041 | 0.6898 | -0.0143 [-0.0274, +0.0003] |

**season**

| season | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2223 | 663 | 0.6976 | 0.6900 | -0.0075 [-0.0165, +0.0010] |
| 2324 | 640 | 0.6985 | 0.6929 | -0.0056 [-0.0122, +0.0009] |
| 2425 | 663 | 0.6969 | 0.6920 | -0.0049 [-0.0136, +0.0043] |
| 2526 | 357 | 0.6982 | 0.6931 | -0.0050 [-0.0147, +0.0045] |

**line_bucket**

| line_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| +0.25 to +1 | 566 | 0.7001 | 0.6950 | -0.0051 [-0.0133, +0.0025] |
| -1 to -0.25 | 1150 | 0.6943 | 0.6905 | -0.0038 [-0.0091, +0.0015] |
| <= -1.25 | 443 | 0.6993 | 0.6908 | -0.0084 [-0.0226, +0.0061] |
| >= +1.25 | 164 | 0.7094 | 0.6931 | -0.0163 [-0.0385, +0.0053] |

**home_role**

| home_role | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| away favourite | 730 | 0.7022 | 0.6946 | -0.0076 [-0.0154, +0.0004] |
| home favourite | 1593 | 0.6957 | 0.6906 | -0.0051 [-0.0104, +0.0000] |

**gap_bucket**

| gap_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2-5pp | 846 | 0.6949 | 0.6927 | -0.0021 [-0.0067, +0.0025] |
| 5-10pp | 504 | 0.7061 | 0.6936 | -0.0125 [-0.0249, -0.0001] |
| <2pp | 834 | 0.6912 | 0.6907 | -0.0006 [-0.0022, +0.0011] |
| >=10pp | 139 | 0.7236 | 0.6872 | -0.0365 [-0.0879, +0.0118] |


## Breakdowns (prod, half lines, LL gain [95%])

**league**

| league | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| D1 | 250 | 0.6922 | 0.6923 | +0.0001 [-0.0114, +0.0110] |
| E0 | 325 | 0.6973 | 0.6938 | -0.0035 [-0.0136, +0.0061] |
| F1 | 305 | 0.6942 | 0.6917 | -0.0025 [-0.0140, +0.0094] |
| I1 | 307 | 0.7012 | 0.6902 | -0.0110 [-0.0198, -0.0021] |
| N1 | 263 | 0.6945 | 0.6952 | +0.0007 [-0.0115, +0.0136] |
| P1 | 265 | 0.6927 | 0.6920 | -0.0007 [-0.0140, +0.0121] |
| SP1 | 323 | 0.6981 | 0.6904 | -0.0077 [-0.0175, +0.0010] |
| T1 | 285 | 0.7021 | 0.6898 | -0.0123 [-0.0252, +0.0018] |

**season**

| season | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2223 | 663 | 0.6956 | 0.6900 | -0.0055 [-0.0135, +0.0030] |
| 2324 | 640 | 0.6989 | 0.6929 | -0.0060 [-0.0120, -0.0003] |
| 2425 | 663 | 0.6969 | 0.6920 | -0.0048 [-0.0126, +0.0036] |
| 2526 | 357 | 0.6945 | 0.6931 | -0.0014 [-0.0108, +0.0075] |

**line_bucket**

| line_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| +0.25 to +1 | 566 | 0.7001 | 0.6950 | -0.0051 [-0.0133, +0.0025] |
| -1 to -0.25 | 1150 | 0.6943 | 0.6905 | -0.0038 [-0.0091, +0.0015] |
| <= -1.25 | 443 | 0.6954 | 0.6908 | -0.0046 [-0.0157, +0.0067] |
| >= +1.25 | 164 | 0.7052 | 0.6931 | -0.0122 [-0.0328, +0.0081] |

**home_role**

| home_role | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| away favourite | 730 | 0.7012 | 0.6946 | -0.0067 [-0.0140, +0.0006] |
| home favourite | 1593 | 0.6946 | 0.6906 | -0.0040 [-0.0087, +0.0006] |

**gap_bucket**

| gap_bucket | n | model LL | Pinnacle LL | LL gain [95%] |
|---|---|---|---|---|
| 2-5pp | 850 | 0.6941 | 0.6916 | -0.0025 [-0.0076, +0.0024] |
| 5-10pp | 500 | 0.7054 | 0.6921 | -0.0133 [-0.0256, -0.0020] |
| <2pp | 871 | 0.6923 | 0.6920 | -0.0002 [-0.0017, +0.0013] |
| >=10pp | 102 | 0.7139 | 0.6920 | -0.0219 [-0.0720, +0.0293] |

## Simulated CLV (SIMULATED, not achievable execution)

Bet the side where model EV at the Pinnacle OPENING price and line is >= 2%. CLV = opening odds x Pinnacle fair closing probability - 1, only where the opening and closing lines match; moved lines report whether the move favoured the bet. ROI settles at opening odds on the opening line. Assumes every opening price was available to bet at Pinnacle limits.

| variant | bets | mean model EV | ROI at open [95%] | same-line bets | mean CLV [95%] | CLV (Shin) | CLV > 0 | moved bets | moved favourably |
|---|---|---|---|---|---|---|---|---|---|
| dc | 7176 | 0.1285 | -0.0393 [-0.0596, -0.0194] | 4441 | -0.0250 [-0.0264, -0.0234] | -0.0250 | 0.2961 | 2735 | 0.4801 |
| blend70 | 3860 | 0.0664 | -0.0485 [-0.0740, -0.0232] | 2306 | -0.0248 [-0.0267, -0.0227] | -0.0249 | 0.2944 | 1554 | 0.4640 |
| prod | 3551 | 0.0582 | -0.0409 [-0.0680, -0.0126] | 2139 | -0.0247 [-0.0268, -0.0225] | -0.0248 | 0.2959 | 1412 | 0.4462 |

| variant | bet side | bets | ROI at open | mean CLV |
|---|---|---|---|---|
| dc | favourite | 2498 | -0.0236 | -0.0231 |
| dc | level | 813 | -0.0672 | -0.0298 |
| dc | underdog | 3865 | -0.0436 | -0.0252 |
| blend70 | favourite | 1531 | -0.0427 | -0.0231 |
| blend70 | level | 359 | -0.0863 | -0.0319 |
| blend70 | underdog | 1970 | -0.0461 | -0.0247 |
| prod | favourite | 1517 | -0.0306 | -0.0239 |
| prod | level | 359 | -0.0863 | -0.0319 |
| prod | underdog | 1675 | -0.0404 | -0.0238 |

