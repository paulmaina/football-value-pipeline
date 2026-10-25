# Gated-shots production release benchmark

2,019 identical pinned fixtures. The exact release uses market weight 0.70, fixed 480 days, the Pinnacle O/U 2.5 anchor, gated shots, and BBS priority with no stacking.

Source base: `b5a0f9eb7ff36ea78a14bfaeb677cb353613c5ca` plus the exact working-tree file hashes in results.json. No commit was made before presenting the diff and test output.

| Phase | Market | N | Legacy log loss | Release log loss | Legacy Brier | Release Brier |
|---|---|---:|---:|---:|---:|---:|
| development | 1x2 | 429 | 0.97173 | 0.96683 | 0.57642 | 0.57373 |
| development | over_1_5 | 429 | 0.56081 | 0.55826 | 0.18657 | 0.18606 |
| development | under_3_5 | 429 | 0.60282 | 0.58564 | 0.20599 | 0.19944 |
| development | btts_yes | 429 | 0.69614 | 0.68660 | 0.25127 | 0.24695 |
| development | over_2_5 | 429 | 0.68702 | 0.67176 | 0.24664 | 0.23979 |
| development | ah_home_-2.5 | 429 | 0.24276 | 0.24003 | 0.06490 | 0.06452 |
| development | ah_home_-1.5 | 429 | 0.47717 | 0.47300 | 0.15241 | 0.15135 |
| development | ah_home_-1.0 | 327 | 0.50418 | 0.49766 | 0.16375 | 0.16178 |
| development | ah_home_+0.0 | 322 | 0.56223 | 0.55829 | 0.19174 | 0.19028 |
| development | ah_home_+1.0 | 359 | 0.37358 | 0.37424 | 0.11363 | 0.11351 |
| development | ah_home_+1.5 | 429 | 0.34866 | 0.34985 | 0.10359 | 0.10359 |
| development | ah_home_+2.5 | 429 | 0.19781 | 0.20076 | 0.05329 | 0.05368 |
| audit | 1x2 | 1590 | 0.99692 | 0.99510 | 0.59449 | 0.59312 |
| audit | over_1_5 | 1590 | 0.53694 | 0.53299 | 0.17664 | 0.17520 |
| audit | under_3_5 | 1590 | 0.62352 | 0.61941 | 0.21305 | 0.21143 |
| audit | btts_yes | 1590 | 0.69577 | 0.69058 | 0.25030 | 0.24793 |
| audit | over_2_5 | 1590 | 0.69671 | 0.69238 | 0.24976 | 0.24782 |
| audit | ah_home_-2.5 | 1590 | 0.31314 | 0.31299 | 0.09062 | 0.09063 |
| audit | ah_home_-1.5 | 1590 | 0.47395 | 0.47451 | 0.15272 | 0.15293 |
| audit | ah_home_-1.0 | 1253 | 0.50702 | 0.50761 | 0.16655 | 0.16688 |
| audit | ah_home_+0.0 | 1187 | 0.58230 | 0.57882 | 0.19979 | 0.19796 |
| audit | ah_home_+1.0 | 1305 | 0.39172 | 0.38922 | 0.11997 | 0.11903 |
| audit | ah_home_+1.5 | 1590 | 0.36231 | 0.36074 | 0.10780 | 0.10726 |
| audit | ah_home_+2.5 | 1590 | 0.17998 | 0.17917 | 0.04453 | 0.04431 |

The baseline replays legacy per-fold half-life tuning. The original fixed-240 benchmark comparisons remain available separately. Full per-league and per-variant paired tables, approximate intervals, shot gate counts, input hashes and fit errors are in results.json.

876 fixtures (43%) had usable anchor quotes in the anchor-only variant; one solver failure retained the unanchored baseline. Quote coverage and results are retrospective: nominal-opening prices have no verified availability timestamps. Existing historical periods were already inspected; the table does not establish live betting profitability.

Pinned Football-Data CSVs contain shots but no timestamped BBS observations. The production BBS-priority rule runs unchanged; BBS therefore cannot activate on these pinned inputs.

All shot, BBS and selection thresholds remain unchanged. User requested direct production adoption; the prospective promotion thresholds were not rewritten. Legacy companion forecasts continue prospective comparisons.

Reproduce the standard sequential calculation from the reviewed release checkout:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python historical_benchmark.py --materialize-pinned-data --source-commit <full-reviewed-commit-SHA> --out-dir workflow_artifacts/shots-production-release
python historical_benchmark.py --out-dir workflow_artifacts/shots-production-release --validate-only
```

The final run scheduled each independent league calculation in a separate process,
then used the unchanged benchmark input checks, aggregation and report reconciliation.
It recomputed all forecasts; no earlier predictions were reused. Its complete
model-upgrade comparison equals the standard sequential rerun.
