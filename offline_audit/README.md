# Shortlist accuracy audit workspace

This branch preserves the offline comparison against the repository snapshot
`c522da7118211bd4b728ee88046fddf97a273937`. Its parent already contains the
archived forecasts and verified results. The audit tools are independent of
production forecast, shortlist and grading entry points.

| File | Contents |
| --- | --- |
| `replay.py` | Original archived comparison using the repository's result matcher and fixture keys |
| `replay_identity.py` | Corrected replay with reviewed, competition-scoped result aliases and one row per verified result identity |
| `coverage_audit.py` | Analysis of ungraded matches, Turkish result-source coverage and Europa training eligibility |
| `xg_timing.py` | Cross-competition xG join using pre-cutoff archived observations, and grid timestamp coverage check |
| `results/` | Replay logs, offer-level score CSVs and the historical benchmark summary |

The corrected replay recovered 10 verified results and collapsed 15 duplicate
identities. It paired 71 fixtures between the current model and the proposed
published grid, of which 69 also had a usable Pinnacle fit. On those 69,
Asian Handicap settlement log loss was 0.9206 for the current model, 0.9134
for the proposed grid and 0.9063 for the Pinnacle fit. All archived pairs came
from one gameweek. The release gate requires 300 paired fixtures over six
gameweeks.

The xG availability check found 18 pre-cutoff xG attachments across the 17
European fixtures it checked. No team reached the existing five-match xG
minimum from that evidence. The grid timestamp field checked by the audit was
absent in all 689 archived grid rows. These are coverage checks.

## Rerun the archive checks

Use a full checkout of this branch and run from its root. The commands work
without API keys and use the archives and verified results already in Git.

```sh
python -m pip install -r football_value_requirements.txt
python -m offline_audit.replay
python -m offline_audit.replay_identity
python -m offline_audit.coverage_audit
python -m offline_audit.xg_timing
```

The replays write fresh offer-level scores to
`workflow_artifacts/shortlist-audit/`. Their summaries print to the terminal.
The checked-in results preserve the original audit. Use the pinned branch
rather than a newer archive checkout to reproduce the same cohort.

## Rerun the historical comparison

The historical run reconstructs forecasts from five domestic leagues. Its
nominal opening odds lack observation timestamps, so the results are
diagnostic. The committed JSON summarizes the run. The full per-market
scores and pinned copies of the input CSVs are reproducible with these commands.

```sh
git fetch origin 1caa1ee2ad9ac255f2952727df8e91ba4081d389
python -m offline_audit.materialize_history
python research_backtest.py --mode historical --cache workflow_artifacts/shortlist-audit/pinned_inputs --source-commit c522da7118211bd4b728ee88046fddf97a273937 --output workflow_artifacts/shortlist-audit/historical
```
