# Six domestic seasons

Downloaded and validated 2021/22 through 2026/27, including the current season,
from Football-Data.co.uk for EPL, LaLiga, Bundesliga, Serie A and Ligue 1.
Thirty source CSVs are retained in `.football_cache`, including their existing
odds and match-statistics columns. The two added seasons contribute 3,652
completed matches. The source returned the same bytes for the existing twenty
CSV files; this backfill does not claim newer current-season results.

The normal prediction command now uses six domestic seasons. UCL keeps its
separate football-data.org history and the existing four-season default.
`--domestic-seasons-back 4` restores the previous domestic window;
an explicit `--seasons-back N` still sets the shared window as before, unless
`--domestic-seasons-back` overrides domestic leagues. Programmatic callers without a domestic override
retain their explicit shared history setting. Forecast diagnostics record the
requested window and actual loaded season identifiers.

After merge, pull the repository before running the usual prediction command.
That run refits the model using the expanded cache. Existing forecasts and
immutable archives are not rewritten by this change. The full-history refresh
workflow now covers six seasons; routine four-hour refreshes still download
only the current season. The next normal BBS export also sees the older CSVs
through its existing cache reader; source history is consumed immediately even
before that export is rebuilt.

Validation rejects wrong season dates, contradictory result labels, invalid
scores, duplicate fixtures, wrong divisions and removals of existing completed
matches. Refresh metadata includes source hashes and nonempty statistics-field
counts. Those counts describe field availability, not correctness or historical
publication timing. Primary source values and disputed BBS values are not mixed
silently. Older CSV statistics are not automatically BBS predictor features.

## Retrospective diagnostic

The reproducible `docs/audits/history_window_audit.py` compares four- and six-season
score-only models on the same 297 Aug-Oct 2026 fixtures, with monthly fits using
only results dated before each fit origin. Both use half-life 240 days and L2
0.08, without bookmaker blending, BBS statistics or tuning on the comparison.
It does not replace the existing pinned benchmark inputs or forward experiments.

| Metric (lower is better) | Four seasons | Six seasons |
|---|---:|---:|
| Pooled 1X2 log loss | 1.033585 | 1.013945 |
| Pooled multiclass Brier sum | 0.604341 | 0.599691 |

Bundesliga, LaLiga and Ligue 1 improved in this comparison. EPL and Serie A were
slightly worse. The cohort is small and uses today's historical revisions;
publication/correction timing is not independently verified. This is exploratory
retrospective evidence, not proof of future accuracy or profitable selections.
The machine-readable audit includes per-league results, all thirty source hashes
and field-coverage counts in `docs/six_season_history_audit.json`.
