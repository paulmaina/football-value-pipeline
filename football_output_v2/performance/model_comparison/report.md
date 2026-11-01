# Production vs legacy model

First eligible pre-kickoff forecast per fixture only, with no backfill. Both models come from the same run and odds snapshot. 1X2 distance to the Pinnacle close is total variation; binary markets use absolute difference. Asian handicap is the home side and integer lines exclude refunds. Legacy probabilities are never used for selection or staking.

Production `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2` vs legacy `dc-blend50-tuned-half-life-v1`.
Status: **COLLECT_MORE_DATA** (paired matches 15/300, weeks 1/6). No automatic production change.

Excluded fixtures: first_forecast_without_legacy_model: 239, pending_or_unverified_result: 66

| League | Market | Matches | Prod log loss | Legacy log loss | Prod Brier | Legacy Brier | Prod dist. to Pinnacle close | Legacy dist. to Pinnacle close | Close N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL | 1x2 | 15 | 0.8728 | 0.8687 | 0.5227 | 0.5213 | 0.0244 | 0.0351 | 2 |
| ALL | over_1_5 | 15 | 0.6606 | 0.6623 | 0.2341 | 0.2350 | n.a. | n.a. | 0 |
| ALL | under_3_5 | 15 | 0.5772 | 0.5712 | 0.1947 | 0.1921 | n.a. | n.a. | 0 |
| ALL | btts_yes | 15 | 0.8010 | 0.8182 | 0.3003 | 0.3070 | n.a. | n.a. | 0 |
| ALL | over_2_5 | 15 | 0.6418 | 0.6430 | 0.2313 | 0.2331 | 0.0033 | 0.0052 | 1 |
| ALL | ah_home_-2.5 | 15 | 0.6355 | 0.6163 | 0.1960 | 0.1918 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.5 | 15 | 0.6936 | 0.6802 | 0.2410 | 0.2373 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.0 | 10 | 0.8717 | 0.8544 | 0.3342 | 0.3292 | n.a. | n.a. | 0 |
| ALL | ah_home_+0.0 | 14 | 0.5657 | 0.5647 | 0.1989 | 0.1987 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.0 | 14 | 0.2448 | 0.2461 | 0.0622 | 0.0629 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.5 | 15 | 0.2392 | 0.2400 | 0.0657 | 0.0656 | n.a. | n.a. | 0 |
| ALL | ah_home_+2.5 | 15 | 0.1931 | 0.2034 | 0.0570 | 0.0600 | n.a. | n.a. | 0 |
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
| Eredivisie | 1x2 | 8 | 0.8383 | 0.8211 | 0.5173 | 0.5063 | n.a. | n.a. | 0 |
| Eredivisie | over_1_5 | 8 | 0.7357 | 0.7310 | 0.2684 | 0.2679 | n.a. | n.a. | 0 |
| Eredivisie | under_3_5 | 8 | 0.5038 | 0.4736 | 0.1598 | 0.1461 | n.a. | n.a. | 0 |
| Eredivisie | btts_yes | 8 | 0.9545 | 0.9841 | 0.3728 | 0.3842 | n.a. | n.a. | 0 |
| Eredivisie | over_2_5 | 8 | 0.6191 | 0.6030 | 0.2255 | 0.2202 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-2.5 | 8 | 0.8376 | 0.7905 | 0.2568 | 0.2467 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.5 | 8 | 0.6855 | 0.6553 | 0.2384 | 0.2288 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.0 | 5 | 0.9026 | 0.8553 | 0.3528 | 0.3366 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+0.0 | 7 | 0.4771 | 0.4655 | 0.1674 | 0.1621 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.0 | 8 | 0.1700 | 0.1681 | 0.0360 | 0.0351 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.5 | 8 | 0.1367 | 0.1360 | 0.0243 | 0.0239 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+2.5 | 8 | 0.0537 | 0.0539 | 0.0047 | 0.0047 | n.a. | n.a. | 0 |
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
| Ligue 1 | 1x2 | 1 | 0.9139 | 0.9597 | 0.5384 | 0.5714 | n.a. | n.a. | 0 |
| Ligue 1 | over_1_5 | 1 | 1.1794 | 1.1797 | 0.4796 | 0.4797 | n.a. | n.a. | 0 |
| Ligue 1 | under_3_5 | 1 | 0.2424 | 0.2416 | 0.0463 | 0.0461 | n.a. | n.a. | 0 |
| Ligue 1 | btts_yes | 1 | 0.6669 | 0.6704 | 0.2369 | 0.2386 | n.a. | n.a. | 0 |
| Ligue 1 | over_2_5 | 1 | 0.5494 | 0.5481 | 0.1787 | 0.1780 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-2.5 | 1 | 0.0661 | 0.0601 | 0.0041 | 0.0034 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.5 | 1 | 0.2023 | 0.1880 | 0.0336 | 0.0294 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_-1.0 | 0 | n.a. | n.a. | n.a. | n.a. | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+0.0 | 1 | 0.5691 | 0.6112 | 0.1883 | 0.2091 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.0 | 1 | 0.1639 | 0.1792 | 0.0229 | 0.0269 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+1.5 | 1 | 0.1317 | 0.1427 | 0.0152 | 0.0177 | n.a. | n.a. | 0 |
| Ligue 1 | ah_home_+2.5 | 1 | 0.0379 | 0.0421 | 0.0014 | 0.0017 | n.a. | n.a. | 0 |
| Primeira Liga | 1x2 | 1 | 0.2956 | 0.2630 | 0.0998 | 0.0818 | n.a. | n.a. | 0 |
| Primeira Liga | over_1_5 | 1 | 0.2080 | 0.1915 | 0.0353 | 0.0304 | n.a. | n.a. | 0 |
| Primeira Liga | under_3_5 | 1 | 0.4722 | 0.5081 | 0.1417 | 0.1587 | n.a. | n.a. | 0 |
| Primeira Liga | btts_yes | 1 | 0.6275 | 0.6178 | 0.2172 | 0.2124 | n.a. | n.a. | 0 |
| Primeira Liga | over_2_5 | 1 | 0.9163 | 0.9701 | 0.3600 | 0.3856 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-2.5 | 1 | 0.0053 | 0.0043 | 0.0000 | 0.0000 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.5 | 1 | 0.0261 | 0.0220 | 0.0007 | 0.0005 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_-1.0 | 1 | 0.0283 | 0.0236 | 0.0008 | 0.0005 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+0.0 | 1 | 0.1264 | 0.1082 | 0.0141 | 0.0105 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.0 | 1 | 0.4063 | 0.3544 | 0.1115 | 0.0890 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+1.5 | 1 | 0.6722 | 0.6091 | 0.2395 | 0.2081 | n.a. | n.a. | 0 |
| Primeira Liga | ah_home_+2.5 | 1 | 0.3472 | 0.3918 | 0.0860 | 0.1051 | n.a. | n.a. | 0 |
| Serie A | 1x2 | 3 | 0.8031 | 0.8095 | 0.4547 | 0.4597 | 0.0244 | 0.0351 | 2 |
| Serie A | over_1_5 | 3 | 0.2604 | 0.2640 | 0.0532 | 0.0544 | n.a. | n.a. | 0 |
| Serie A | under_3_5 | 3 | 0.8905 | 0.9090 | 0.3417 | 0.3495 | n.a. | n.a. | 0 |
| Serie A | btts_yes | 3 | 0.6410 | 0.6386 | 0.2243 | 0.2231 | n.a. | n.a. | 0 |
| Serie A | over_2_5 | 3 | 0.6338 | 0.6431 | 0.2206 | 0.2252 | 0.0033 | 0.0052 | 1 |
| Serie A | ah_home_-2.5 | 3 | 0.0709 | 0.0726 | 0.0081 | 0.0083 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.5 | 3 | 0.8903 | 0.8864 | 0.3011 | 0.3005 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.0 | 2 | 1.0611 | 1.0527 | 0.3825 | 0.3801 | n.a. | n.a. | 0 |
| Serie A | ah_home_+0.0 | 3 | 0.5372 | 0.5383 | 0.1816 | 0.1814 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.0 | 3 | 0.4183 | 0.4383 | 0.1343 | 0.1446 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.5 | 3 | 0.4806 | 0.5010 | 0.1676 | 0.1769 | n.a. | n.a. | 0 |
| Serie A | ah_home_+2.5 | 3 | 0.6645 | 0.6976 | 0.2414 | 0.2499 | n.a. | n.a. | 0 |
