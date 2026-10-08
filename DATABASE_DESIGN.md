# Database design proposal

## Recommendation

For the current local, single-user pipeline, start with **SQLite** rather than moving immediately to a hosted database.

SQLite fits this project because the pipeline is run from one machine, needs durable indexed cache entries, benefits from transactions, requires no database server, and ships with Python. If the pipeline later runs concurrently from multiple machines or as a hosted service, migrate the same logical schema to PostgreSQL.

DuckDB remains useful for analytical querying, but SQLite is the better first primary store for a cache plus frequently updated operational records.

## Keep exports

The database should become the durable machine-data store while the existing files remain useful exports:

```text
Providers -> database -> model -> database
                         |
                         +-> football_output_v2/raw exports
                         +-> football_output_v2/readable reports
```

CSV/JSON exports remain valuable for inspection, spreadsheets and debugging. They should become generated artifacts rather than the only source of truth.

## Proposed schema

### api_cache

Stores provider responses with TTL metadata.

- cache_key TEXT PRIMARY KEY
- provider TEXT NOT NULL
- endpoint TEXT NOT NULL
- params_hash TEXT NOT NULL
- fetched_at_utc TEXT NOT NULL
- expires_at_utc TEXT NOT NULL
- http_status INTEGER
- payload_json TEXT NOT NULL

API keys must never be included in cache keys, persisted request URLs, logs, parameter hashes, or diagnostic output.

### fixtures

Canonical fixture identity.

- id INTEGER PRIMARY KEY
- provider TEXT NOT NULL
- provider_event_id TEXT NOT NULL
- league TEXT NOT NULL
- kickoff_utc TEXT NOT NULL
- home_team TEXT NOT NULL
- away_team TEXT NOT NULL
- status TEXT
- first_seen_utc TEXT NOT NULL
- last_seen_utc TEXT NOT NULL
- UNIQUE(provider, provider_event_id)

### odds_snapshots

Store snapshots instead of overwriting prices so movement and closing-line value can be studied later.

- id INTEGER PRIMARY KEY
- fixture_id INTEGER NOT NULL
- provider TEXT NOT NULL
- bookmaker TEXT NOT NULL
- market TEXT NOT NULL
- outcome TEXT NOT NULL
- line REAL
- decimal_odds REAL NOT NULL
- observed_at_utc TEXT NOT NULL
- FOREIGN KEY(fixture_id) REFERENCES fixtures(id)

Recommended indexes:

- (fixture_id, market, observed_at_utc)
- (bookmaker, market, observed_at_utc)

### model_runs

- id INTEGER PRIMARY KEY
- started_at_utc TEXT NOT NULL
- pipeline_version TEXT NOT NULL
- parameters_json TEXT NOT NULL
- git_commit TEXT

### predictions

One row per run and fixture.

- run_id INTEGER NOT NULL
- fixture_id INTEGER NOT NULL
- expected-goal fields
- 1X2 probabilities
- fair odds
- O/U probabilities
- market reference probabilities
- best market prices
- EV/edge fields
- PRIMARY KEY(run_id, fixture_id)

### scoreline_probabilities

Normalize the score matrix instead of storing one large JSON object.

- run_id INTEGER NOT NULL
- fixture_id INTEGER NOT NULL
- home_goals INTEGER NOT NULL
- away_goals INTEGER NOT NULL
- probability REAL NOT NULL
- PRIMARY KEY(run_id, fixture_id, home_goals, away_goals)

### backtest_runs and backtest_bets

Keep historical evaluation separate from current predictions so test results cannot accidentally be mixed with production/current-fixture data.

## Suggested implementation phases

1. Stabilize trustworthy fixtures and dedicated odds acquisition.
2. Add a small StorageBackend interface while keeping file output working.
3. Implement SQLiteStorage with migrations/schema creation.
4. Move the HTTP cache into api_cache first; this gives immediate API-quota and stale-data benefits.
5. Persist fixtures and raw odds snapshots.
6. Persist prediction/backtest runs and generate the existing CSV/JSON files as exports.
7. Move to PostgreSQL only if the pipeline becomes hosted, multi-user, or concurrently written by several workers.

## Repository hygiene

Database files should remain local and ignored by Git. Commit schema/migration code, not live .db/.sqlite files.
