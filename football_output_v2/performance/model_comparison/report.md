# Production vs legacy model

First eligible pre-kickoff forecast per fixture only, with no backfill. Both models come from the same run and odds snapshot. 1X2 distance to the Pinnacle close is total variation; binary markets use absolute difference. Asian handicap is the home side and integer lines exclude refunds. Legacy probabilities are never used for selection or staking.

Production `dc-blend70-hl480-pinnacle-ou25-anchor-gated-shots-production-v2` vs legacy `dc-blend50-tuned-half-life-v1`.
Status: **COLLECT_MORE_DATA** (paired matches 10/300, weeks 1/6). No automatic production change.

Excluded fixtures: first_forecast_without_legacy_model: 239, pending_or_unverified_result: 48

| League | Market | Matches | Prod log loss | Legacy log loss | Prod Brier | Legacy Brier | Prod dist. to Pinnacle close | Legacy dist. to Pinnacle close | Close N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL | 1x2 | 10 | 0.8037 | 0.8062 | 0.4770 | 0.4807 | 0.0244 | 0.0351 | 2 |
| ALL | over_1_5 | 10 | 0.5873 | 0.5941 | 0.2058 | 0.2080 | n.a. | n.a. | 0 |
| ALL | under_3_5 | 10 | 0.5357 | 0.5417 | 0.1754 | 0.1790 | n.a. | n.a. | 0 |
| ALL | btts_yes | 10 | 0.6904 | 0.6934 | 0.2487 | 0.2501 | n.a. | n.a. | 0 |
| ALL | over_2_5 | 10 | 0.6543 | 0.6655 | 0.2392 | 0.2455 | 0.0033 | 0.0052 | 1 |
| ALL | ah_home_-2.5 | 10 | 0.4020 | 0.4017 | 0.1194 | 0.1172 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.5 | 10 | 0.4077 | 0.4080 | 0.1317 | 0.1320 | n.a. | n.a. | 0 |
| ALL | ah_home_-1.0 | 7 | 0.5027 | 0.5057 | 0.1895 | 0.1914 | n.a. | n.a. | 0 |
| ALL | ah_home_+0.0 | 9 | 0.4725 | 0.4792 | 0.1595 | 0.1631 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.0 | 9 | 0.2153 | 0.2197 | 0.0572 | 0.0593 | n.a. | n.a. | 0 |
| ALL | ah_home_+1.5 | 10 | 0.2421 | 0.2444 | 0.0753 | 0.0757 | n.a. | n.a. | 0 |
| ALL | ah_home_+2.5 | 10 | 0.2423 | 0.2580 | 0.0808 | 0.0854 | n.a. | n.a. | 0 |
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
| Eredivisie | 1x2 | 4 | 0.7504 | 0.7335 | 0.4807 | 0.4704 | n.a. | n.a. | 0 |
| Eredivisie | over_1_5 | 4 | 0.5146 | 0.5176 | 0.1824 | 0.1838 | n.a. | n.a. | 0 |
| Eredivisie | under_3_5 | 4 | 0.4341 | 0.4178 | 0.1286 | 0.1231 | n.a. | n.a. | 0 |
| Eredivisie | btts_yes | 4 | 0.7580 | 0.7628 | 0.2809 | 0.2831 | n.a. | n.a. | 0 |
| Eredivisie | over_2_5 | 4 | 0.6010 | 0.5955 | 0.2245 | 0.2244 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-2.5 | 4 | 0.3062 | 0.2834 | 0.0772 | 0.0675 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.5 | 4 | 0.3450 | 0.3298 | 0.1010 | 0.0955 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_-1.0 | 3 | 0.4579 | 0.4357 | 0.1700 | 0.1623 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+0.0 | 3 | 0.2466 | 0.2389 | 0.0843 | 0.0814 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.0 | 4 | 0.0766 | 0.0753 | 0.0141 | 0.0135 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+1.5 | 4 | 0.0625 | 0.0617 | 0.0095 | 0.0091 | n.a. | n.a. | 0 |
| Eredivisie | ah_home_+2.5 | 4 | 0.0222 | 0.0219 | 0.0015 | 0.0015 | n.a. | n.a. | 0 |
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
| Serie A | 1x2 | 2 | 0.5298 | 0.5474 | 0.2551 | 0.2677 | 0.0244 | 0.0351 | 2 |
| Serie A | over_1_5 | 2 | 0.2863 | 0.2885 | 0.0621 | 0.0629 | n.a. | n.a. | 0 |
| Serie A | under_3_5 | 2 | 0.8322 | 0.8467 | 0.3111 | 0.3168 | n.a. | n.a. | 0 |
| Serie A | btts_yes | 2 | 0.7077 | 0.6991 | 0.2572 | 0.2530 | n.a. | n.a. | 0 |
| Serie A | over_2_5 | 2 | 0.6837 | 0.6909 | 0.2453 | 0.2489 | 0.0033 | 0.0052 | 1 |
| Serie A | ah_home_-2.5 | 2 | 0.0883 | 0.0904 | 0.0115 | 0.0117 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.5 | 2 | 0.2237 | 0.2295 | 0.0541 | 0.0555 | n.a. | n.a. | 0 |
| Serie A | ah_home_-1.0 | 1 | 0.0625 | 0.0711 | 0.0037 | 0.0047 | n.a. | n.a. | 0 |
| Serie A | ah_home_+0.0 | 2 | 0.2721 | 0.2817 | 0.0572 | 0.0604 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.0 | 2 | 0.4097 | 0.4450 | 0.1392 | 0.1570 | n.a. | n.a. | 0 |
| Serie A | ah_home_+1.5 | 2 | 0.5596 | 0.5943 | 0.2133 | 0.2290 | n.a. | n.a. | 0 |
| Serie A | ah_home_+2.5 | 2 | 0.9303 | 0.9829 | 0.3543 | 0.3678 | n.a. | n.a. | 0 |
