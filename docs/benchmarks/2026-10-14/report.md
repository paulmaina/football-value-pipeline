# Historical football benchmark

Published results: [compact audit results](results.json). The full summary, calibration tables, ledger and fold evidence are retained by the Historical model benchmark workflow. This initial report was generated locally from the pinned inputs and validated before publication.

Retrospective diagnostics only. Historical periods were already examined by Claude and are not untouched evidence. Nominal opening odds lack exact availability timestamps; no historical betting edge/ROI/CLV claim is made. Closing inputs are explicitly oracle/evaluation-only. Baseline fixes half-life at 240 days rather than replaying production tuning. Fitted rho is retained for totals scaling. No bookmaker fallback, new data download or automatic production change.

Unique evaluated fixtures: 2019. Baseline: fixed half-life 240 days, L2 0.08. This is a named configuration reference, not a replay of per-run production tuning.

| League | Evaluated | Opening HDA | Closing HDA | Opening O/U | Closing O/U |
|---|---:|---:|---:|---:|---:|
| EPL | 440 | 210 | 210 | 210 | 210 |
| LaLiga | 458 | 189 | 188 | 188 | 188 |
| Bundesliga | 351 | 150 | 149 | 142 | 142 |
| SerieA | 440 | 200 | 198 | 200 | 198 |
| Ligue1 | 360 | 153 | 153 | 152 | 152 |

Paired comparisons below use the exact same fixtures as their baseline. Positive gain means lower candidate error. Approximate intervals assume independent fixtures and do not account for multiple comparisons.

| Phase | Market | Variant | Paired N | Baseline loss | Candidate loss | Loss gain | Brier gain |
|---|---|---|---:|---:|---:|---:|---:|
| development | 1x2 | blend_50_fixed_baseline | 429 | 0.97238 | 0.97238 | 0.00000 | 0.00000 |
| development | 1x2 | half_life_365 | 429 | 0.97238 | 0.97220 | 0.00018 | 0.00016 |
| development | 1x2 | half_life_365_raw | 429 | 0.97238 | 0.99769 | -0.02531 | -0.01453 |
| development | 1x2 | half_life_480 | 429 | 0.97238 | 0.97218 | 0.00020 | 0.00019 |
| development | 1x2 | half_life_480_raw | 429 | 0.97238 | 0.99797 | -0.02559 | -0.01459 |
| development | 1x2 | l2_0.8 | 429 | 0.97238 | 0.97013 | 0.00225 | 0.00145 |
| development | 1x2 | l2_0.8_raw | 429 | 0.97238 | 0.98790 | -0.01552 | -0.00982 |
| development | 1x2 | l2_3 | 429 | 0.97238 | 0.96972 | 0.00266 | 0.00186 |
| development | 1x2 | l2_3_raw | 429 | 0.97238 | 0.98518 | -0.01280 | -0.00793 |
| development | 1x2 | market_weight_0.75 | 429 | 0.97238 | 0.96540 | 0.00698 | 0.00405 |
| development | 1x2 | market_weight_0.85 | 429 | 0.97238 | 0.96350 | 0.00888 | 0.00504 |
| development | 1x2 | pinnacle_closing_only | 429 | 0.97238 | 0.96397 | 0.00841 | 0.00400 |
| development | 1x2 | pinnacle_opening_only | 429 | 0.97238 | 0.96162 | 0.01076 | 0.00583 |
| development | 1x2 | raw_model | 429 | 0.97238 | 0.99784 | -0.02546 | -0.01489 |
| development | 1x2 | totals_closing_oracle | 424 | 0.97856 | 0.97856 | -0.00000 | 0.00000 |
| development | 1x2 | totals_opening_anchor | 424 | 0.97856 | 0.97856 | -0.00000 | 0.00000 |
| development | over_1_5 | blend_50_fixed_baseline | 429 | 0.56158 | 0.56158 | 0.00000 | 0.00000 |
| development | over_1_5 | half_life_365 | 429 | 0.56158 | 0.56035 | 0.00123 | 0.00047 |
| development | over_1_5 | half_life_365_raw | 429 | 0.56158 | 0.56151 | 0.00007 | 0.00024 |
| development | over_1_5 | half_life_480 | 429 | 0.56158 | 0.55998 | 0.00161 | 0.00064 |
| development | over_1_5 | half_life_480_raw | 429 | 0.56158 | 0.56117 | 0.00041 | 0.00039 |
| development | over_1_5 | l2_0.8 | 429 | 0.56158 | 0.55520 | 0.00638 | 0.00217 |
| development | over_1_5 | l2_0.8_raw | 429 | 0.56158 | 0.55563 | 0.00595 | 0.00200 |
| development | over_1_5 | l2_3 | 429 | 0.56158 | 0.55290 | 0.00868 | 0.00317 |
| development | over_1_5 | l2_3_raw | 429 | 0.56158 | 0.55307 | 0.00851 | 0.00309 |
| development | over_1_5 | market_weight_0.75 | 429 | 0.56158 | 0.56117 | 0.00041 | 0.00008 |
| development | over_1_5 | market_weight_0.85 | 429 | 0.56158 | 0.56103 | 0.00055 | 0.00010 |
| development | over_1_5 | raw_model | 429 | 0.56158 | 0.56266 | -0.00108 | -0.00021 |
| development | over_1_5 | totals_closing_oracle | 424 | 0.55664 | 0.55040 | 0.00624 | 0.00190 |
| development | over_1_5 | totals_opening_anchor | 424 | 0.55664 | 0.55348 | 0.00316 | 0.00072 |
| development | under_3_5 | blend_50_fixed_baseline | 429 | 0.60240 | 0.60240 | 0.00000 | 0.00000 |
| development | under_3_5 | half_life_365 | 429 | 0.60240 | 0.60135 | 0.00106 | 0.00042 |
| development | under_3_5 | half_life_365_raw | 429 | 0.60240 | 0.60174 | 0.00067 | 0.00030 |
| development | under_3_5 | half_life_480 | 429 | 0.60240 | 0.60132 | 0.00108 | 0.00043 |
| development | under_3_5 | half_life_480_raw | 429 | 0.60240 | 0.60175 | 0.00065 | 0.00028 |
| development | under_3_5 | l2_0.8 | 429 | 0.60240 | 0.59713 | 0.00527 | 0.00157 |
| development | under_3_5 | l2_0.8_raw | 429 | 0.60240 | 0.59759 | 0.00481 | 0.00141 |
| development | under_3_5 | l2_3 | 429 | 0.60240 | 0.59249 | 0.00991 | 0.00343 |
| development | under_3_5 | l2_3_raw | 429 | 0.60240 | 0.59289 | 0.00951 | 0.00327 |
| development | under_3_5 | market_weight_0.75 | 429 | 0.60240 | 0.60235 | 0.00006 | 0.00001 |
| development | under_3_5 | market_weight_0.85 | 429 | 0.60240 | 0.60235 | 0.00006 | 0.00001 |
| development | under_3_5 | raw_model | 429 | 0.60240 | 0.60273 | -0.00032 | -0.00010 |
| development | under_3_5 | totals_closing_oracle | 424 | 0.60221 | 0.58376 | 0.01846 | 0.00692 |
| development | under_3_5 | totals_opening_anchor | 424 | 0.60221 | 0.58512 | 0.01709 | 0.00647 |
| development | btts_yes | blend_50_fixed_baseline | 429 | 0.69792 | 0.69792 | 0.00000 | 0.00000 |
| development | btts_yes | half_life_365 | 429 | 0.69792 | 0.69557 | 0.00236 | 0.00112 |
| development | btts_yes | half_life_365_raw | 429 | 0.69792 | 0.69540 | 0.00252 | 0.00116 |
| development | btts_yes | half_life_480 | 429 | 0.69792 | 0.69475 | 0.00318 | 0.00152 |
| development | btts_yes | half_life_480_raw | 429 | 0.69792 | 0.69460 | 0.00332 | 0.00155 |
| development | btts_yes | l2_0.8 | 429 | 0.69792 | 0.69444 | 0.00348 | 0.00156 |
| development | btts_yes | l2_0.8_raw | 429 | 0.69792 | 0.69441 | 0.00352 | 0.00158 |
| development | btts_yes | l2_3 | 429 | 0.69792 | 0.69300 | 0.00492 | 0.00227 |
| development | btts_yes | l2_3_raw | 429 | 0.69792 | 0.69336 | 0.00456 | 0.00210 |
| development | btts_yes | market_weight_0.75 | 429 | 0.69792 | 0.69812 | -0.00020 | -0.00007 |
| development | btts_yes | market_weight_0.85 | 429 | 0.69792 | 0.69822 | -0.00030 | -0.00010 |
| development | btts_yes | raw_model | 429 | 0.69792 | 0.69771 | 0.00021 | 0.00006 |
| development | btts_yes | totals_closing_oracle | 424 | 0.69903 | 0.68848 | 0.01055 | 0.00483 |
| development | btts_yes | totals_opening_anchor | 424 | 0.69903 | 0.68831 | 0.01072 | 0.00484 |
| development | over_2_5 | blend_50_fixed_baseline | 429 | 0.69013 | 0.69013 | 0.00000 | 0.00000 |
| development | over_2_5 | half_life_365 | 429 | 0.69013 | 0.68760 | 0.00253 | 0.00114 |
| development | over_2_5 | half_life_365_raw | 429 | 0.69013 | 0.68928 | 0.00085 | 0.00045 |
| development | over_2_5 | half_life_480 | 429 | 0.69013 | 0.68676 | 0.00337 | 0.00152 |
| development | over_2_5 | half_life_480_raw | 429 | 0.69013 | 0.68846 | 0.00168 | 0.00082 |
| development | over_2_5 | l2_0.8 | 429 | 0.69013 | 0.68508 | 0.00505 | 0.00208 |
| development | over_2_5 | l2_0.8_raw | 429 | 0.69013 | 0.68645 | 0.00368 | 0.00148 |
| development | over_2_5 | l2_3 | 429 | 0.69013 | 0.68092 | 0.00921 | 0.00403 |
| development | over_2_5 | l2_3_raw | 429 | 0.69013 | 0.68183 | 0.00830 | 0.00361 |
| development | over_2_5 | market_weight_0.75 | 429 | 0.69013 | 0.68945 | 0.00068 | 0.00028 |
| development | over_2_5 | market_weight_0.85 | 429 | 0.69013 | 0.68921 | 0.00092 | 0.00038 |
| development | over_2_5 | raw_model | 429 | 0.69013 | 0.69181 | -0.00168 | -0.00069 |
| development | over_2_5 | totals_closing_oracle | 424 | 0.69410 | 0.66973 | 0.02436 | 0.01125 |
| development | over_2_5 | totals_opening_anchor | 424 | 0.69410 | 0.67530 | 0.01880 | 0.00846 |
| audit | 1x2 | blend_50_fixed_baseline | 458 | 0.97007 | 0.97007 | 0.00000 | 0.00000 |
| audit | 1x2 | half_life_365 | 458 | 0.97007 | 0.96860 | 0.00147 | 0.00113 |
| audit | 1x2 | half_life_365_raw | 458 | 0.97007 | 0.98351 | -0.01344 | -0.00854 |
| audit | 1x2 | half_life_480 | 458 | 0.97007 | 0.96794 | 0.00213 | 0.00165 |
| audit | 1x2 | half_life_480_raw | 458 | 0.97007 | 0.98244 | -0.01236 | -0.00764 |
| audit | 1x2 | l2_0.8 | 458 | 0.97007 | 0.97054 | -0.00047 | -0.00014 |
| audit | 1x2 | l2_0.8_raw | 458 | 0.97007 | 0.98666 | -0.01658 | -0.01074 |
| audit | 1x2 | l2_3 | 458 | 0.97007 | 0.97192 | -0.00184 | -0.00069 |
| audit | 1x2 | l2_3_raw | 458 | 0.97007 | 0.98875 | -0.01868 | -0.01165 |
| audit | 1x2 | market_weight_0.75 | 458 | 0.97007 | 0.96487 | 0.00520 | 0.00340 |
| audit | 1x2 | market_weight_0.85 | 458 | 0.97007 | 0.96332 | 0.00676 | 0.00438 |
| audit | 1x2 | pinnacle_closing_only | 454 | 0.96969 | 0.96110 | 0.00859 | 0.00529 |
| audit | 1x2 | pinnacle_opening_only | 458 | 0.97007 | 0.96156 | 0.00851 | 0.00546 |
| audit | 1x2 | raw_model | 458 | 0.97007 | 0.98632 | -0.01624 | -0.01077 |
| audit | 1x2 | totals_closing_oracle | 450 | 0.97388 | 0.97388 | -0.00000 | 0.00000 |
| audit | 1x2 | totals_opening_anchor | 452 | 0.97548 | 0.97548 | 0.00000 | 0.00000 |
| audit | over_1_5 | blend_50_fixed_baseline | 458 | 0.54175 | 0.54175 | 0.00000 | 0.00000 |
| audit | over_1_5 | half_life_365 | 458 | 0.54175 | 0.54035 | 0.00140 | 0.00049 |
| audit | over_1_5 | half_life_365_raw | 458 | 0.54175 | 0.54103 | 0.00073 | 0.00029 |
| audit | over_1_5 | half_life_480 | 458 | 0.54175 | 0.53992 | 0.00184 | 0.00064 |
| audit | over_1_5 | half_life_480_raw | 458 | 0.54175 | 0.54060 | 0.00115 | 0.00043 |
| audit | over_1_5 | l2_0.8 | 458 | 0.54175 | 0.54021 | 0.00154 | 0.00056 |
| audit | over_1_5 | l2_0.8_raw | 458 | 0.54175 | 0.54089 | 0.00087 | 0.00034 |
| audit | over_1_5 | l2_3 | 458 | 0.54175 | 0.53737 | 0.00439 | 0.00155 |
| audit | over_1_5 | l2_3_raw | 458 | 0.54175 | 0.53808 | 0.00367 | 0.00133 |
| audit | over_1_5 | market_weight_0.75 | 458 | 0.54175 | 0.54145 | 0.00030 | 0.00009 |
| audit | over_1_5 | market_weight_0.85 | 458 | 0.54175 | 0.54134 | 0.00042 | 0.00013 |
| audit | over_1_5 | raw_model | 458 | 0.54175 | 0.54240 | -0.00065 | -0.00020 |
| audit | over_1_5 | totals_closing_oracle | 450 | 0.54812 | 0.53058 | 0.01754 | 0.00561 |
| audit | over_1_5 | totals_opening_anchor | 452 | 0.54767 | 0.53185 | 0.01582 | 0.00523 |
| audit | under_3_5 | blend_50_fixed_baseline | 458 | 0.61089 | 0.61089 | 0.00000 | 0.00000 |
| audit | under_3_5 | half_life_365 | 458 | 0.61089 | 0.60806 | 0.00283 | 0.00120 |
| audit | under_3_5 | half_life_365_raw | 458 | 0.61089 | 0.60844 | 0.00246 | 0.00108 |
| audit | under_3_5 | half_life_480 | 458 | 0.61089 | 0.60703 | 0.00386 | 0.00163 |
| audit | under_3_5 | half_life_480_raw | 458 | 0.61089 | 0.60738 | 0.00351 | 0.00153 |
| audit | under_3_5 | l2_0.8 | 458 | 0.61089 | 0.60821 | 0.00268 | 0.00088 |
| audit | under_3_5 | l2_0.8_raw | 458 | 0.61089 | 0.60861 | 0.00228 | 0.00074 |
| audit | under_3_5 | l2_3 | 458 | 0.61089 | 0.60337 | 0.00752 | 0.00261 |
| audit | under_3_5 | l2_3_raw | 458 | 0.61089 | 0.60362 | 0.00728 | 0.00252 |
| audit | under_3_5 | market_weight_0.75 | 458 | 0.61089 | 0.61069 | 0.00020 | 0.00007 |
| audit | under_3_5 | market_weight_0.85 | 458 | 0.61089 | 0.61061 | 0.00028 | 0.00009 |
| audit | under_3_5 | raw_model | 458 | 0.61089 | 0.61136 | -0.00046 | -0.00015 |
| audit | under_3_5 | totals_closing_oracle | 450 | 0.60891 | 0.59259 | 0.01633 | 0.00666 |
| audit | under_3_5 | totals_opening_anchor | 452 | 0.61100 | 0.59332 | 0.01768 | 0.00701 |
| audit | btts_yes | blend_50_fixed_baseline | 458 | 0.70841 | 0.70841 | 0.00000 | 0.00000 |
| audit | btts_yes | half_life_365 | 458 | 0.70841 | 0.70759 | 0.00082 | 0.00037 |
| audit | btts_yes | half_life_365_raw | 458 | 0.70841 | 0.70687 | 0.00155 | 0.00068 |
| audit | btts_yes | half_life_480 | 458 | 0.70841 | 0.70750 | 0.00092 | 0.00041 |
| audit | btts_yes | half_life_480_raw | 458 | 0.70841 | 0.70678 | 0.00163 | 0.00072 |
| audit | btts_yes | l2_0.8 | 458 | 0.70841 | 0.70581 | 0.00260 | 0.00115 |
| audit | btts_yes | l2_0.8_raw | 458 | 0.70841 | 0.70515 | 0.00327 | 0.00143 |
| audit | btts_yes | l2_3 | 458 | 0.70841 | 0.70120 | 0.00721 | 0.00326 |
| audit | btts_yes | l2_3_raw | 458 | 0.70841 | 0.70078 | 0.00764 | 0.00345 |
| audit | btts_yes | market_weight_0.75 | 458 | 0.70841 | 0.70884 | -0.00042 | -0.00018 |
| audit | btts_yes | market_weight_0.85 | 458 | 0.70841 | 0.70901 | -0.00060 | -0.00025 |
| audit | btts_yes | raw_model | 458 | 0.70841 | 0.70767 | 0.00075 | 0.00032 |
| audit | btts_yes | totals_closing_oracle | 450 | 0.70830 | 0.69127 | 0.01703 | 0.00783 |
| audit | btts_yes | totals_opening_anchor | 452 | 0.70760 | 0.69336 | 0.01424 | 0.00648 |
| audit | over_2_5 | blend_50_fixed_baseline | 458 | 0.70267 | 0.70267 | 0.00000 | 0.00000 |
| audit | over_2_5 | half_life_365 | 458 | 0.70267 | 0.69901 | 0.00365 | 0.00169 |
| audit | over_2_5 | half_life_365_raw | 458 | 0.70267 | 0.70132 | 0.00135 | 0.00072 |
| audit | over_2_5 | half_life_480 | 458 | 0.70267 | 0.69756 | 0.00510 | 0.00236 |
| audit | over_2_5 | half_life_480_raw | 458 | 0.70267 | 0.69982 | 0.00285 | 0.00141 |
| audit | over_2_5 | l2_0.8 | 458 | 0.70267 | 0.70014 | 0.00253 | 0.00111 |
| audit | over_2_5 | l2_0.8_raw | 458 | 0.70267 | 0.70239 | 0.00028 | 0.00014 |
| audit | over_2_5 | l2_3 | 458 | 0.70267 | 0.69493 | 0.00773 | 0.00345 |
| audit | over_2_5 | l2_3_raw | 458 | 0.70267 | 0.69674 | 0.00593 | 0.00265 |
| audit | over_2_5 | market_weight_0.75 | 458 | 0.70267 | 0.70152 | 0.00115 | 0.00049 |
| audit | over_2_5 | market_weight_0.85 | 458 | 0.70267 | 0.70108 | 0.00159 | 0.00068 |
| audit | over_2_5 | raw_model | 458 | 0.70267 | 0.70516 | -0.00249 | -0.00106 |
| audit | over_2_5 | totals_closing_oracle | 450 | 0.70779 | 0.68529 | 0.02250 | 0.01047 |
| audit | over_2_5 | totals_opening_anchor | 452 | 0.70828 | 0.68787 | 0.02041 | 0.00943 |

Development-selected candidates

| Family | Market | Selected | Development N | Audit N | Status |
|---|---|---|---:|---:|---|
| l2 | 1x2 | l2_3 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| l2 | over_1_5 | l2_3 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| l2 | under_3_5 | l2_3 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| l2 | btts_yes | l2_3 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| l2 | over_2_5 | l2_3 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| half_life | 1x2 | half_life_480 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| half_life | over_1_5 | half_life_480 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| half_life | under_3_5 | half_life_480 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| half_life | btts_yes | half_life_480 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| half_life | over_2_5 | half_life_480 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_l2 | 1x2 | l2_3_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_l2 | over_1_5 | l2_3_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_l2 | under_3_5 | l2_3_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_l2 | btts_yes | l2_3_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_l2 | over_2_5 | l2_3_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_half_life | 1x2 | half_life_365_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_half_life | over_1_5 | half_life_480_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_half_life | under_3_5 | half_life_365_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_half_life | btts_yes | half_life_480_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| raw_half_life | over_2_5 | half_life_480_raw | 429 | 1590 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| market_weight | 1x2 | market_weight_0.85 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| market_weight | over_1_5 | market_weight_0.85 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| market_weight | under_3_5 | market_weight_0.85 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| market_weight | btts_yes | blend_50_fixed_baseline | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| market_weight | over_2_5 | market_weight_0.85 | 429 | 458 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| totals | 1x2 | blend_50_fixed_baseline | 424 | 452 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| totals | over_1_5 | totals_opening_anchor | 424 | 452 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| totals | under_3_5 | totals_opening_anchor | 424 | 452 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| totals | btts_yes | totals_opening_anchor | 424 | 452 | RETROSPECTIVE_DIAGNOSTIC_ONLY |
| totals | over_2_5 | totals_opening_anchor | 424 | 452 | RETROSPECTIVE_DIAGNOSTIC_ONLY |

Closing-reference comparisons, RPS, calibration buckets, per-league results and development/audit metrics are in summary.json. Predictions and fold training hashes are retained in the workflow artifact. No setting is promoted automatically.

## Same-fixture 1X2 comparison

| Method | Paired N | Log loss | Brier | RPS |
|---|---:|---:|---:|---:|
| raw_model | 883 | 0.99201 | 0.59027 | 0.20090 |
| blend_50_fixed_baseline | 883 | 0.97100 | 0.57730 | 0.19508 |
| market_weight_0.75 | 883 | 0.96479 | 0.57349 | 0.19335 |
| market_weight_0.85 | 883 | 0.96301 | 0.57246 | 0.19288 |
| Pinnacle closing reference | 883 | 0.96249 | 0.57264 | 0.19318 |

These rows use the shared closing-reference cohort. The raw model and the nominal-opening blends have different information timing from the close. This is a forecasting diagnostic, not a historical betting simulation.
