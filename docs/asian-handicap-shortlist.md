# Asian handicap shortlist — policy v20

New prediction runs replace double chance with full-time Asian goal handicaps.
The market pool is Home win, Draw, Away win, Over 1.5, and supported home/away
Asian handicap lines. BTTS, double chance and Under 3.5 are excluded from this
production shortlist. Their general probability outputs and old archives remain
available. Historical policies retain their original eligibility and settlement.

## Objective and limits

Choose the lowest **estimated chance of any net loss**, including half-losses,
among eligible real quotes. A full refund is not a win. No model guarantees a
refund, a winner, an accurate probability, or preservation of your bankroll.
The objective applies to individual selections; an accumulator can lose even
when another leg refunds. Reports assume one hypothetical flat stake per match.

The selector:

1. Requires a supported competition, reliable team mapping, fresh exact-market
   quotes and a fresh linked 1X2 reference, with kickoff 20 minutes to 48 hours away.
2. Prefers **Pinnacle and bet365**, allowing **1xBet as a fallback** for each
   exact side/handicap line when no eligible primary-book quote exists. Invalid,
   incomplete, stale or disallowed primary quotes cannot block a valid fallback.
   For binary markets, executable-quote extraction also prefers primary books
   for that exact market. Reference data in the model blend is separate.
3. Requires chronological historical no-loss calibration to pass for that side
   and handicap: at least 80 development and 40 audit examples. Matchdays never
   straddle the partition. The report compares audit Brier against a constant
   development-frequency reference and checks overconfidence. This is a
   retrospective diagnostic, not proof of a betting edge or a wholly untouched
   final holdout; existing model tuning periods may overlap.
4. Uses development overconfidence plus a descriptive 1.96-standard-error
   allowance as a conservative penalty. It takes the worse raw/blended loss
   estimate and adds that penalty. `loss_probability_upper` is the implementation
   field name; **it is a conservative ranking estimate, not a guaranteed or
   formally calibrated upper confidence bound**.
5. Requires **adjusted estimated EV >=1% and unblended EV >=0 for every
   shortlisted market**, including Home win, Draw, Away win, Over 1.5 and Asian
   handicaps. An adjusted EV of exactly 1% qualifies; a value below 1% or a
   negative unblended estimate rejects the pick. Zero adjusted EV is excluded. The adjusted EV allowance
   moves penalty mass from the best payoff to a full loss. Nonnegative estimates
   do not guarantee a profit or prevent losses.
6. For each fixture, find the minimum conservative loss estimate among eligible
   candidates after bookmaker preference and EV gates. Keep candidates with
   `risk <= fixture_minimum + tolerance`, then rank **adjusted EV descending,
   unblended EV descending, full-refund probability descending**, lower loss
   risk and higher price. Kickoff, market and bookmaker resolve remaining ties.
   The risk band is anchored to the minimum; successive near-ties never widen it.
   Choose one market per fixture, then order those representatives by risk and
   cap at twelve. No quote, identity or reliability gate is bypassed.

The default tolerance is **0.01 (1 percentage point)**, an absolute probability
difference, configured as `asian_handicap_risk_tolerance` in
`shortlist_quote_policy.json`. A 10% minimum admits lines up to 11%; a 12% line
is excluded even if another line is at 11%. A zero tolerance requires a minimum-
risk line, with EV before refund tie-breaks. The value must be finite, numeric
and between 0 and 1. It is frozen in the run's execution policy and summary;
selected rows record the minimum and tolerance for deterministic replay.

**The tolerance is a provisional policy choice, not a statistical confidence
interval or historically optimized threshold.** The available history validates
no-loss probabilities, but lacks a sufficient historical set of executable
handicap prices to optimize this EV/risk tradeoff or establish ROI. Later tuning
needs development-only quote data and separate evaluation data. The existing
raw/blended model and calibration penalty are unchanged.

Binary markets retain their probability, calibration and quote-integrity rules,
with the current adjusted EV floor set to 1% (previously 1.5%), and compete
in the same per-fixture risk-band comparison. Therefore the shortlist need not consist only
of handicaps. Nonzero per-stake costs currently make Asian picks ineligible:
refunds can lose fees, and the historical no-loss calibration is presently for
zero costs. Costs are never silently ignored to call such a refund safe.

The initial supported handicap scope is **−3 to +3 in steps of 0.25**, both sides.
Lines outside that validation scope are omitted. Only quoted lines are offered;
the model never fabricates bookmaker prices or handicap availability.

## Probability and settlement

The pipeline exports the complete signed goal-margin distribution from both the
raw Dixon–Coles grid and the final market-blended grid. It does not reconstruct
handicap probabilities from the exported top twenty scorelines. The two-stage
model and its configured 50/50 market blend otherwise retain their existing behavior.

For the selected team, evaluate goal difference plus its handicap. Quarter lines
split the stake equally across the neighboring half/integer lines. Expected
profit per unit stake at decimal price `o` is:

`P(full win)*(o−1) + P(half win)*(o−1)/2 − P(half loss)/2 − P(full loss) − cost`.

An integer-line refund contributes zero gross profit, not `o−1`. The reported
no-loss probability includes full wins, half-wins and full refunds at zero cost;
half-losses are losses. `p_refund` means the probability of a **full** refund;
partial returned stakes are represented by the half-settlement probabilities.

Both outcomes must form a complete opposite-handicap pair at the same bookmaker
and update time. Three-way European handicaps, corners, cards, halftime and
in-play markets are excluded. Identity binding checks event ID, ordered teams
and kickoff. Extra-market responses cannot replace valid linked main quotes
with another event's lines.

## Coverage and collection

Main odds requests add `spreads` to the existing H/D/A and totals request.
Per-event requests obtain alternate spreads and draw-no-bet alongside existing
alternate totals/BTTS research quotes. Production no longer requests double
chance. Additional markets can increase provider credits; existing provider
quota/exhaustion handling remains active. No BBS/API-Football budget is restored.

Provider documentation lists Pinnacle in its EU region, with a potential public
website delay. It does **not** list bet365 football; its bet365 Australian feed
is paid and restricted to AFL/NRL. Provider/bookmaker/event coverage must still
be verified on the account. Missing quotes stay missing; the implementation
cannot promise automated bet365 football coverage.

- https://the-odds-api.com/sports-odds-data/bookmaker-apis.html
- https://the-odds-api.com/sports-odds-data/betting-markets.html

No provider credentials were available in the implementation environment. Tests
use provider-shaped responses, disable live network access, and do not establish
account-level coverage.

## Optional confirmed bookmaker quotes

To use fresh bet365/Pinnacle/1xBet prices you have actually observed, save a JSON array
of event-odds objects and add `--asian-handicap-quotes PATH` to your normal command.
This is an explicit user-supplied quote input, not an automated bookmaker API or
scraper. It records that provenance; accepted execution is still unverified.

Template only — replace every placeholder with the actual current fixture,
handicap, complementary prices and observation time. This is not a live quote:

```json
[
  {
    "id": "EXACT_ODDS_EVENT_ID_FROM_PREDICTIONS",
    "home_team": "EXACT_HOME_TEAM",
    "away_team": "EXACT_AWAY_TEAM",
    "commence_time": "ACTUAL_KICKOFF_ISO_TIMESTAMP_WITH_TIMEZONE",
    "bookmakers": [
      {
        "title": "bet365",
        "markets": [
          {
            "key": "spreads",
            "last_update": "ACTUAL_OBSERVATION_ISO_TIMESTAMP_WITH_TIMEZONE",
            "outcomes": [
              {"name": "EXACT_HOME_TEAM", "point": 0, "price": 1.90},
              {"name": "EXACT_AWAY_TEAM", "point": 0, "price": 1.90}
            ]
          }
        ]
      }
    ]
  }
]
```

The template must match a linked forecast event exactly; merely supplying a
favourable number does not bypass mapping, kickoff, calibration or quote-integrity checks.
Duplicate event objects fail rather than choosing one arbitrarily.

## Outputs, tracking and compatibility

- `asian_handicap_best_per_match.csv`: the best eligible Asian line for every
  fixture, even beyond the twelve-match shortlist cap. No row is fabricated for
  a fixture without an eligible quote.
- `conservative_bet_shortlist.csv`: the chosen market per shortlisted match,
  with all five settlement probabilities, no-loss/loss estimates, raw no-loss
  probability, full-refund probability, line, side, book, quote timestamp/source,
  opposite quote, EV and historical sample sizes.
- Readable shortlist CSV/Markdown: loss, refund and partial-settlement details.
- Current run bundles retain the additional evidence under their normal hashes.
  A code merge does not regenerate predictions or rewrite captured archives.

Grading uses 90-minute plus stoppage-time scores from the existing verified
results path. It records `WON`, `HALF_WON`, `REFUNDED`, `HALF_LOST`, `LOST`.
Refunds are included in settled stake/ROI denominators but not wins. Half-wins
and half-losses retain their actual half-stake profit. Separate counts and
no-loss rates are available in AH-cohort JSON metrics. Excel formulas and cached
values account for split settlement; the workbook notes explain that Asian
probability/Brier measures **no net loss**, not outright winning.

Near-close collection requests exact handicap markets for archived selections.
An exact same-book, same-line offered-price CLV can be recorded. Fair-close EV
is left unavailable for AH: a binary reciprocal-price normalization is not a
settlement-aware no-loss probability. Versioned normalization preserves old
closing observations. Missing bet365 close coverage remains explicit.

The probability/EV weighting, legacy shortlist-policy and EV-filter experiments
are not generated for v17/v18/v19/v20: they compare a different ranking objective and market
pool. Existing immutable experiments continue to be graded under their original
rules. Other probability-model research sidecars remain separate and unchanged.
The summary explicitly identifies these ranking experiments as not applicable.

The normal prediction command remains valid. The first run invalidates old
goal-validation caches and can take longer while building AH calibration.
Subsequent unchanged inputs can reuse the versioned cache. Refreshing an old
forecast alone cannot invent missing margin distributions, quotes or calibration.

## Policy version and replay

New runs use v20 with a common 1% adjusted EV floor. Frozen v17 archives retain
their original Asian EV floors and
Pinnacle/bet365 scope; frozen v18 archives retain floorless loss-first ranking.
Frozen v19 archives retain zero adjusted EV for Asian picks and 1.5% for
binary markets. All remain reproducible under their original rules. The default
execution allowlist includes 1xBet and
marks it as a fallback, not a higher-price substitute for valid primary quotes.
Live 1xBet handicap coverage and account entitlement have not been verified;
when absent from provider responses, a validated user-supplied quote file can
provide it. No extra API endpoint or scraper was added for this fallback.
