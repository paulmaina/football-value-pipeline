> **ARCHIVED 2026-11-02.** No longer generated, captured or reviewed. This is the last report, frozen as committed; the code is kept for replay in `archive/model_comparison.py`.

# Production vs legacy model

First eligible pre-kickoff forecast per fixture only, with no backfill. Both models come from the same run and odds snapshot. 1X2 distance to the Pinnacle close is total variation; binary markets use absolute difference. Asian handicap is the home side and integer lines exclude refunds. Legacy probabilities are never used for selection or staking.

Production `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2` vs legacy `dc-blend50-tuned-half-life-v1`.
Status: **COLLECT_MORE_DATA** (paired matches 32/300, weeks 1/6). No automatic production change.

Excluded fixtures: first_forecast_without_legacy_model: 239, pending_or_unverified_result: 49

| League | Market | Matches | Prod log loss | Legacy log loss | Prod Brier | Legacy Brier | Prod dist. to Pinnacle close | Legacy dist. to Pinnacle close | Close N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL | 1x2 | 32 | 0.8195 | 0.8185 | 0.4759 | 0.4758 | 0.0268 | 0.0376 | 4 |
| ALL | over_1_5 | 32 | 0.4931 | 0.4990 | 0.1587 | 0.1612 | n.a. | n.a. | 0 |
| ALL | under_3_5 | 32 | 0.5586 | 0.5488 | 0.1884 | 0.1843 | n.a. | n.a. | 0 |
| ALL | btts_yes | 32 | 0.7467 | 0.7481 | 0.2748 | 0.2749 | n.a. | n.a. | 0 |
| ALL | over_2_5 | 32 | 0.6737 | 0.6629 | 0.2430 | 0.2384 | 0.0263 | 0.0730 | 2 |
| ALL | ah_home_-2.5 | 32 | 0.5439 | 0.5291 | 0.1705 | 0.1676 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.5 | 32 | 0.7723 | 0.7705 | 0.2805 | 0.2801 | 0.0008 | 0.0113 | 1 |
| ALL | ah_home_-1.0 | 24 | 0.8276 | 0.8230 | 0.3148 | 0.3131 | 0.0437 | 0.0681 | 1 |
| ALL | ah_home_+0.0 | 31 | 0.5198 | 0.5201 | 0.1729 | 0.1734 | 0.0377 | 0.0490 | 2 |
| ALL | ah_home_+1.0 | 29 | 0.2982 | 0.3048 | 0.0881 | 0.0912 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.5 | 32 | 0.3000 | 0.3056 | 0.0919 | 0.0938 | n.a. | n.a. | 0 |
| ALL | ah_home_+2.5 | 32 | 0.1719 | 0.1765 | 0.0507 | 0.0523 | n.a. | n.a. | 0 |
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
| Ligue 1 | 1x2 | 4 | 0.6310 | 0.6378 | 0.3311 | 0.3357 | n.a. | n.a. | 0 |
| Ligue 1 | over_1_5 | 4 | 0.4649 | 0.4712 | 0.1510 | 0.1529 | n.a. | n.a. | 0 |
| Ligue 1 | under_3_5 | 4 | 0.5412 | 0.5649 | 0.1800 | 0.1900 | n.a. | n.a. | 0 |
| Ligue 1 | btts_yes | 4 | 0.6867 | 0.6992 | 0.2466 | 0.2530 | n.a. | n.a. | 0 |
| Ligue 1 | over_2_5 | 4 | 0.6992 | 0.7127 | 0.2528 | 0.2597 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-2.5 | 4 | 0.6151 | 0.6201 | 0.2048 | 0.2064 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.5 | 4 | 0.8350 | 0.8278 | 0.3223 | 0.3196 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.0 | 3 | 0.7812 | 0.7747 | 0.2934 | 0.2902 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+0.0 | 4 | 0.3532 | 0.3555 | 0.0944 | 0.0958 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.0 | 4 | 0.1033 | 0.1022 | 0.0111 | 0.0111 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.5 | 4 | 0.0870 | 0.0858 | 0.0079 | 0.0078 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+2.5 | 4 | 0.0245 | 0.0237 | 0.0007 | 0.0007 | n.a. | n.a. | 0 |
| Primeira Liga | 1x2 | 7 | 0.6512 | 0.6387 | 0.3471 | 0.3387 | n.a. | n.a. | 0 |
| Primeira Liga | over_1_5 | 7 | 0.4699 | 0.4642 | 0.1452 | 0.1435 | n.a. | n.a. | 0 |
| Primeira Liga | under_3_5 | 7 | 0.3103 | 0.3154 | 0.0730 | 0.0758 | n.a. | n.a. | 0 |
| Primeira Liga | btts_yes | 7 | 0.6546 | 0.6535 | 0.2308 | 0.2302 | n.a. | n.a. | 0 |
| Primeira Liga | over_2_5 | 7 | 0.6962 | 0.6813 | 0.2515 | 0.2440 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-2.5 | 7 | 0.6820 | 0.6566 | 0.2320 | 0.2274 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.5 | 7 | 0.5074 | 0.5008 | 0.1800 | 0.1776 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.0 | 5 | 0.4675 | 0.4453 | 0.1703 | 0.1589 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+0.0 | 7 | 0.3707 | 0.3666 | 0.1004 | 0.1004 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.0 | 7 | 0.4946 | 0.5105 | 0.1756 | 0.1825 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.5 | 7 | 0.6015 | 0.6161 | 0.2201 | 0.2238 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+2.5 | 7 | 0.0837 | 0.0855 | 0.0141 | 0.0164 | n.a. | n.a. | 0 |
| Serie A | 1x2 | 7 | 0.7768 | 0.7923 | 0.4373 | 0.4488 | 0.0268 | 0.0376 | 4 |
| Serie A | over_1_5 | 7 | 0.2920 | 0.3206 | 0.0681 | 0.0792 | n.a. | n.a. | 0 |
| Serie A | under_3_5 | 7 | 0.5812 | 0.5553 | 0.2001 | 0.1897 | n.a. | n.a. | 0 |
| Serie A | btts_yes | 7 | 0.7753 | 0.7447 | 0.2898 | 0.2751 | n.a. | n.a. | 0 |
| Serie A | over_2_5 | 7 | 0.7748 | 0.7481 | 0.2881 | 0.2755 | 0.0263 | 0.0730 | 2 |
| Serie A | ah_home_-2.5 | 7 | 0.0916 | 0.0851 | 0.0112 | 0.0098 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.5 | 7 | 0.8936 | 0.9222 | 0.3224 | 0.3317 | 0.0008 | 0.0113 | 1 |
| Serie A | ah_home_-1.0 | 5 | 0.9575 | 0.9946 | 0.3610 | 0.3757 | 0.0437 | 0.0681 | 1 |
| Serie A | ah_home_+0.0 | 7 | 0.4876 | 0.4976 | 0.1558 | 0.1601 | 0.0377 | 0.0490 | 2 |
| Serie A | ah_home_+1.0 | 6 | 0.2772 | 0.2875 | 0.0764 | 0.0816 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.5 | 7 | 0.2802 | 0.2878 | 0.0813 | 0.0850 | n.a. | n.a. | 0 |
| Serie A | ah_home_+2.5 | 7 | 0.3079 | 0.3208 | 0.1045 | 0.1081 | n.a. | n.a. | 0 |
