# Production vs legacy model

First eligible pre-kickoff forecast per fixture only, with no backfill. Both models come from the same run and odds snapshot. 1X2 distance to the Pinnacle close is total variation; binary markets use absolute difference. Asian handicap is the home side and integer lines exclude refunds. Legacy probabilities are never used for selection or staking.

Production `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2` vs legacy `dc-blend50-tuned-half-life-v1`.
Status: **COLLECT_MORE_DATA** (paired matches 28/300, weeks 1/6). No automatic production change.

Excluded fixtures: first_forecast_without_legacy_model: 239, pending_or_unverified_result: 53

| League | Market | Matches | Prod log loss | Legacy log loss | Prod Brier | Legacy Brier | Prod dist. to Pinnacle close | Legacy dist. to Pinnacle close | Close N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL | 1x2 | 28 | 0.8369 | 0.8378 | 0.4898 | 0.4912 | 0.0212 | 0.0316 | 3 |
| ALL | over_1_5 | 28 | 0.5210 | 0.5236 | 0.1717 | 0.1729 | n.a. | n.a. | 0 |
| ALL | under_3_5 | 28 | 0.5904 | 0.5839 | 0.2034 | 0.2006 | n.a. | n.a. | 0 |
| ALL | btts_yes | 28 | 0.7466 | 0.7569 | 0.2746 | 0.2789 | n.a. | n.a. | 0 |
| ALL | over_2_5 | 28 | 0.6578 | 0.6567 | 0.2355 | 0.2358 | 0.0033 | 0.0052 | 1 |
| ALL | ah_home_-2.5 | 28 | 0.4546 | 0.4465 | 0.1371 | 0.1355 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.5 | 28 | 0.6880 | 0.6872 | 0.2423 | 0.2429 | 0.0008 | 0.0113 | 1 |
| ALL | ah_home_-1.0 | 20 | 0.7757 | 0.7726 | 0.2910 | 0.2908 | n.a. | n.a. | 0 |
| ALL | ah_home_+0.0 | 27 | 0.5375 | 0.5395 | 0.1821 | 0.1833 | 0.0204 | 0.0282 | 1 |
| ALL | ah_home_+1.0 | 25 | 0.3271 | 0.3363 | 0.1001 | 0.1040 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.5 | 28 | 0.3288 | 0.3364 | 0.1036 | 0.1061 | n.a. | n.a. | 0 |
| ALL | ah_home_+2.5 | 28 | 0.1923 | 0.1983 | 0.0578 | 0.0597 | n.a. | n.a. | 0 |
| Bundesliga | 1x2 | 1 | 0.8789 | 0.9217 | 0.5194 | 0.5501 | n.a. | n.a. | 0 |
| Bundesliga | over_1_5 | 1 | 0.1373 | 0.1402 | 0.0164 | 0.0171 | n.a. | n.a. | 0 |
| Bundesliga | under_3_5 | 1 | 0.7655 | 0.7929 | 0.2861 | 0.2997 | n.a. | n.a. | 0 |
| Bundesliga | btts_yes | 1 | 0.3718 | 0.3777 | 0.0964 | 0.0990 | n.a. | n.a. | 0 |
| Bundesliga | over_2_5 | 1 | 0.3847 | 0.4008 | 0.1020 | 0.1090 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_-2.5 | 1 | 2.3004 | 2.3787 | 0.8096 | 0.8233 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_-1.5 | 1 | 1.4845 | 1.5383 | 0.5981 | 0.6166 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_-1.0 | 1 | 1.2755 | 1.3361 | 0.5194 | 0.5434 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_+0.0 | 1 | 0.6105 | 0.6403 | 0.2088 | 0.2236 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_+1.0 | 1 | 0.2417 | 0.2524 | 0.0461 | 0.0498 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_+1.5 | 1 | 0.1959 | 0.2041 | 0.0316 | 0.0341 | n.a. | n.a. | 0 |
| Bundesliga | ah_home_+2.5 | 1 | 0.0755 | 0.0788 | 0.0053 | 0.0057 | n.a. | n.a. | 0 |
| Eredivisie | 1x2 | 12 | 0.9114 | 0.9012 | 0.5595 | 0.5527 | n.a. | n.a. | 0 |
| Eredivisie | over_1_5 | 12 | 0.5609 | 0.5555 | 0.1910 | 0.1900 | n.a. | n.a. | 0 |
| Eredivisie | under_3_5 | 12 | 0.6857 | 0.6586 | 0.2472 | 0.2349 | n.a. | n.a. | 0 |
| Eredivisie | btts_yes | 12 | 0.8313 | 0.8464 | 0.3142 | 0.3196 | n.a. | n.a. | 0 |
| Eredivisie | over_2_5 | 12 | 0.5965 | 0.5820 | 0.2102 | 0.2049 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-2.5 | 12 | 0.5818 | 0.5519 | 0.1731 | 0.1667 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.5 | 12 | 0.7953 | 0.7742 | 0.2833 | 0.2768 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.0 | 9 | 0.9267 | 0.8990 | 0.3563 | 0.3470 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+0.0 | 11 | 0.5836 | 0.5763 | 0.2112 | 0.2077 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.0 | 11 | 0.2606 | 0.2617 | 0.0707 | 0.0713 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.5 | 12 | 0.2359 | 0.2376 | 0.0636 | 0.0644 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+2.5 | 12 | 0.2143 | 0.2181 | 0.0654 | 0.0663 | n.a. | n.a. | 0 |
| La Liga | 1x2 | 1 | 1.8870 | 1.8887 | 1.1796 | 1.1866 | n.a. | n.a. | 0 |
| La Liga | over_1_5 | 1 | 1.7172 | 1.7824 | 0.6731 | 0.6918 | n.a. | n.a. | 0 |
| La Liga | under_3_5 | 1 | 0.4758 | 0.5096 | 0.1434 | 0.1594 | n.a. | n.a. | 0 |
| La Liga | btts_yes | 1 | 0.7904 | 0.8190 | 0.2985 | 0.3126 | n.a. | n.a. | 0 |
| La Liga | over_2_5 | 1 | 0.9218 | 0.9723 | 0.3626 | 0.3866 | n.a. | n.a. | 0 |
| La Liga | ah_home_-2.5 | 1 | 0.2473 | 0.2593 | 0.0480 | 0.0522 | n.a. | n.a. | 0 |
| La Liga | ah_home_-1.5 | 1 | 0.5367 | 0.5534 | 0.1725 | 0.1806 | n.a. | n.a. | 0 |
| La Liga | ah_home_-1.0 | 1 | 0.7786 | 0.8023 | 0.2926 | 0.3044 | n.a. | n.a. | 0 |
| La Liga | ah_home_+0.0 | 1 | 1.6627 | 1.6729 | 0.6567 | 0.6598 | n.a. | n.a. | 0 |
| La Liga | ah_home_+1.0 | 0 | n.a. | n.a. | n.a. | n.a. | n.a. | n.a. | 0 |
| La Liga | ah_home_+1.5 | 1 | 0.0524 | 0.0528 | 0.0026 | 0.0026 | n.a. | n.a. | 0 |
| La Liga | ah_home_+2.5 | 1 | 0.0132 | 0.0136 | 0.0002 | 0.0002 | n.a. | n.a. | 0 |
| Ligue 1 | 1x2 | 3 | 0.6454 | 0.6612 | 0.3427 | 0.3536 | n.a. | n.a. | 0 |
| Ligue 1 | over_1_5 | 3 | 0.5550 | 0.5535 | 0.1909 | 0.1904 | n.a. | n.a. | 0 |
| Ligue 1 | under_3_5 | 3 | 0.5627 | 0.6143 | 0.1921 | 0.2147 | n.a. | n.a. | 0 |
| Ligue 1 | btts_yes | 3 | 0.6149 | 0.6602 | 0.2110 | 0.2335 | n.a. | n.a. | 0 |
| Ligue 1 | over_2_5 | 3 | 0.6246 | 0.6730 | 0.2160 | 0.2400 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-2.5 | 3 | 0.7622 | 0.7688 | 0.2646 | 0.2667 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.5 | 3 | 0.7442 | 0.7395 | 0.2803 | 0.2789 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.0 | 2 | 0.7457 | 0.7473 | 0.2756 | 0.2764 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+0.0 | 3 | 0.3616 | 0.3738 | 0.0998 | 0.1053 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.0 | 3 | 0.1033 | 0.1069 | 0.0116 | 0.0124 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.5 | 3 | 0.0863 | 0.0888 | 0.0081 | 0.0085 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+2.5 | 3 | 0.0239 | 0.0246 | 0.0007 | 0.0008 | n.a. | n.a. | 0 |
| Primeira Liga | 1x2 | 5 | 0.6533 | 0.6489 | 0.3496 | 0.3478 | n.a. | n.a. | 0 |
| Primeira Liga | over_1_5 | 5 | 0.5205 | 0.5184 | 0.1694 | 0.1695 | n.a. | n.a. | 0 |
| Primeira Liga | under_3_5 | 5 | 0.3222 | 0.3233 | 0.0783 | 0.0799 | n.a. | n.a. | 0 |
| Primeira Liga | btts_yes | 5 | 0.6528 | 0.6493 | 0.2298 | 0.2282 | n.a. | n.a. | 0 |
| Primeira Liga | over_2_5 | 5 | 0.6602 | 0.6515 | 0.2336 | 0.2291 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-2.5 | 5 | 0.0678 | 0.0785 | 0.0072 | 0.0102 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.5 | 5 | 0.1821 | 0.2016 | 0.0370 | 0.0452 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.0 | 3 | 0.0970 | 0.1056 | 0.0104 | 0.0126 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+0.0 | 5 | 0.3778 | 0.3804 | 0.1050 | 0.1086 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.0 | 5 | 0.6551 | 0.6802 | 0.2426 | 0.2527 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.5 | 5 | 0.8105 | 0.8332 | 0.3059 | 0.3113 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+2.5 | 5 | 0.1089 | 0.1123 | 0.0196 | 0.0228 | n.a. | n.a. | 0 |
| Serie A | 1x2 | 6 | 0.7548 | 0.7678 | 0.4211 | 0.4307 | 0.0212 | 0.0316 | 3 |
| Serie A | over_1_5 | 6 | 0.2894 | 0.3032 | 0.0677 | 0.0724 | n.a. | n.a. | 0 |
| Serie A | under_3_5 | 6 | 0.6272 | 0.6140 | 0.2219 | 0.2156 | n.a. | n.a. | 0 |
| Serie A | btts_yes | 6 | 0.7763 | 0.7689 | 0.2901 | 0.2870 | n.a. | n.a. | 0 |
| Serie A | over_2_5 | 6 | 0.7967 | 0.7924 | 0.2986 | 0.2970 | 0.0033 | 0.0052 | 1 |
| Serie A | ah_home_-2.5 | 6 | 0.0957 | 0.0906 | 0.0124 | 0.0111 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.5 | 6 | 0.7592 | 0.7723 | 0.2647 | 0.2699 | 0.0008 | 0.0113 | 1 |
| Serie A | ah_home_-1.0 | 4 | 0.8341 | 0.8529 | 0.3047 | 0.3135 | n.a. | n.a. | 0 |
| Serie A | ah_home_+0.0 | 6 | 0.4745 | 0.4818 | 0.1507 | 0.1535 | 0.0204 | 0.0282 | 1 |
| Serie A | ah_home_+1.0 | 5 | 0.2969 | 0.3109 | 0.0863 | 0.0931 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.5 | 6 | 0.3027 | 0.3131 | 0.0917 | 0.0965 | n.a. | n.a. | 0 |
| Serie A | ah_home_+2.5 | 6 | 0.3513 | 0.3677 | 0.1215 | 0.1258 | n.a. | n.a. | 0 |
