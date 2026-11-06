# Recommendation history, latest picks and actual placed bets

The existing immutable pre-kickoff snapshots already store generation/capture
times and prices. The latest-view selectors do not include every older pick.
Keep three separate views rather than infer execution from a prediction.

## All captured recommendations

`football_output_v2/performance/price_edge_v27/all_recommendation_generations.csv`
contains both lists' captured recommendations, each graded from its own actual
quoted price after verified regulation results are available. An earlier pick
remains here when its line changes, its group disappears, or a later run drops it.
Each row has its generation, capture, snapshot, list and stable recommendation ID.
Identical re-uploads of a generation deduplicate. Preserve all eligible captures;
post-cutoff uploads are not made into forward observations after the event.

The summary/report adds `recommendation_history` counts and hypothetical flat-unit
returns. Repeated generations of a fixture and overlapping lists are correlated,
not independent samples or proof multiple bets were placed. Do not pool them
as actual account ROI or use their raw row count as distinct-match evidence.

## Latest model-evaluation view

Existing `picks.csv`, `cagey_tier_picks.csv`, latest-view summary figures and review
flags retain their existing semantics. The all-generation report is additional;
it does not silently replace latest evaluation with repeated exposure.

## Private user-recorded placed bets

Initialize a local ledger (the default root is `football_output_v2`):

```sh
python bet_ledger.py init
python bet_ledger.py add --file football_output_v2/.football_bets/placed-bet.json
```

An example `placed-bet.json` structure (replace every example value with your own
actual entry; this file does not place a bet):

```json
{
  "bet_id": "your-ticket-id",
  "placed_at_utc": "2026-11-06T12:00:00+00:00",
  "league": "Premier League",
  "home_team": "Home team",
  "away_team": "Away team",
  "kickoff_utc": "2026-11-07T15:00:00+00:00",
  "market": "Over 1.5",
  "bookmaker": "your bookmaker",
  "offered_decimal_odds": 1.5,
  "stake": 100,
  "currency": "KES",
  "per_stake_cost": 0
}
```

`--root <output-root>` supports other output locations. Put any JSON import file
inside the ignored `.football_bets/` directory too, not in a public repository
folder. The ledger is `<output-root>/.football_bets/placed_bets.csv`. Nothing is
automatically marked executed. Add one unique ticket ID per actual bet. Market
labels determine AH side/line; prices/stakes must be finite and positive,
placement must precede kickoff and report time, and timestamps require timezones.
The CLI records entry time separately from your stated placement time.

The normal performance review reads an existing ledger and writes
`.football_bets/graded_bets.csv` and `.football_bets/summary.json` privately.
Profit uses your entered stake, entry price and execution cost; currencies are
never combined. Pending/unverified results do not enter ROI. Invalid input
produces a visible invalid status and clears stale generated ROI, without
changing the source ledger. These are user-reported executions, not broker-verified
statements, and must not serve as proof of pre-registered model evaluation.

The entire `.football_bets/` directory is ignored by Git. Public pipeline reports
show only whether a private ledger exists/is invalid; they do not copy stakes,
ticket IDs or actual financial returns. On GitHub Actions there is no actual-bet
ROI without a separately supplied ledger. Recommendation snapshots alone cannot
establish which offers you saw or which bets you placed.
