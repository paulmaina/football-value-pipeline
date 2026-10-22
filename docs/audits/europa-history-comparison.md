# Europa League cross-source comparison

## Current status

Fixture Download: four completed season exports were inspected locally, with
660 rows. See [the audit](2026-10-22-europa-league-csv-audit.md) for checks,
source hashes, UEFA cross-checks, known extra-time contamination and limitations.
Raw exports are not committed or uploaded as Actions artifacts.

FootyStats: **no entitled Europa League export was available for inspection**.
The public dataset listing advertises 175, 175, 269 and 271 match rows for
2022/23 through 2025/26. These are advertised counts, not downloaded/validated
records. Additional qualifying coverage is a hypothesis. Overlap, score
agreement, extra-time handling, available stats and usable additions remain
unmeasured. No source has been admitted into production training.

Access evidence checked 22 October 2026:

- https://footystats.org/europe/uefa-europa-league/datasets
- https://footystats.org/download-stats-csv states that CSV downloads require
  login, except the advertised Premier League samples, and directs automated
  downloading to its API.
- https://footystats.org/terms-and-conditions separates API access from its
  website automation restrictions. Obtain an export/API entitlement that permits
  the intended local analysis; a public listing alone does not establish one.

## Offline audit tool

`scripts/compare_europa_history.py` accepts **local, entitled, single-season
Europa League exports**. It performs no network requests and imports no pipeline
code. Its implementation is validated with synthetic CSVs; compatibility with a
real FootyStats Europa export is pending and unsupported schemas fail explicitly.
The Fixture Download input must be its UTC export.

```powershell
py scripts/compare_europa_history.py `
  --fixture-download C:/local-data/europa-league-2024-UTC.csv `
  --footystats C:/local-data/footystats-europa-2024.csv `
  --season-start-year 2024 `
  --aliases C:/local-data/aliases.json `
  --output C:/local-data/europa-comparison-2024.json
```

Omit `--aliases` initially. Review unmatched names and provide an explicitly
verified JSON mapping, for example `{"Short Club Name": "Canonical Club Name"}`.
Mappings are applied to both sources after Unicode/case/whitespace normalization.
There is no fuzzy matching or automatic team reversal/date shift. Supplying the
correct competition/season files remains a caller requirement: the exports need
not contain an authoritative competition ID. The July–June range rejects
obviously wrong-season dates but cannot authenticate competition identity.

Completed FootyStats rows require `timestamp`, `status`,
`home_team_goal_count`, `away_team_goal_count`, and either
`team_a_name`/`team_b_name` or `home_team_name`/`away_team_name`.
Non-complete rows are skipped; invalid scores/dates are rejected. No placeholder
score is silently interpreted as a valid completed result.

Joins use UTC calendar date and canonical home/away names within the declared
season. Kickoff-time disagreements are flagged separately. Duplicate identities
on either side quarantine that identity on both sides. The report contains input
hashes, overlap/agree/conflict counts, duplicate/rejection counts and input CSV
line references for conflicts. It does not copy match rows or write merged data.

Unmatched rows are **candidates**, not verified additions: they can represent
unmapped names, date differences, a different competition stage or extra scope.
Even identical scores in both sources are not proof of a regulation-time score;
both sources may include extra time or share an upstream error. This tool does
not infer regulation scores from goal totals or ambiguous goal-minute strings.

## Completion criteria

1. Obtain entitled match exports for the same four seasons, or start with
   2024/25 to test the known Man Utd–Lyon and Lazio–Bodø/Glimt examples.
2. Run the comparison; inspect all duplicate identities, rejected rows,
   unmatched candidates, kickoff differences and score conflicts locally.
3. Confirm team aliases and competition stages against authoritative records.
4. Verify regulation-time labels independently for extra-time-capable matches.
5. Measure genuinely additional completed matches and per-field missingness
   from the real export. Historical price timestamps/bookmaker identity and
   point-in-time feature availability require separate validation.
6. Publish aggregate findings only; admit records through a separately reviewed
   staging/training adapter once these gates pass.

Tests: `py -m unittest tests.test_europa_history_comparison tests.test_europa_access_audit`.
All tests use synthetic or mocked inputs and require no API credits.
