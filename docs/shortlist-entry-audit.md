# Shortlist entry audit

Offline audit of the entry rules of the two lists that feed the master: the value shortlist and the cagey tier.
Nothing here changes a live list, probability, pick or stake. The judging rules were written into `docs/plan.md`
(Phase 4, "Shortlist entry audit", decided 14 Nov 2026) before any figure was computed. The holdout is never read
(locked run; never `--declaration`).

- Selection functions: `shortlist_entry_audit.py` (`value_select`, `cagey_select`, `Rules`, the rule tests).
- Backtest: `python evaluation_harness.py --mode lists --output evaluation/shortlist_entry_audit`
  (`results.json`, `today_picks.csv`).
- Reproduction on saved live runs: `python scripts/shortlist_entry_reproduction.py --output evaluation/shortlist_entry_audit`
  (`reproduction.json`); test `tests/test_shortlist_entry_audit.py`.

## 1. Inventory of entry rules

Live configuration: `cagey_correction_config.json` (value rule `local-research-profit-115-200-dc12-v2`, cagey rule
`no-loss-market-reference-v5`, `excluded_markets`, `quote_timing_rule: observed-by-cutoff-v2`) and
`shortlist_quote_policy.json` (Pinnacle only, no fallback, cost 0). Candidates for both lists come from
`price_edge_shortlist.offered_candidates` (every Pinnacle AH quote, main and alternate, both sides; 1X2 home/away;
double chance 1X/X2; native draw no bet) plus `profit_shortlist.dc12_candidates` (double chance 12).

### Value shortlist (`local-research-profit-115-200-dc12-v2`)

| # | Rule | Today | Where | Why it exists (record) | Testable offline |
| --- | --- | --- | --- | --- | --- |
| V1 | Markets | Pinnacle AH (any quarter line, main and alternate), home/away win, double chance 1X/X2; native AH 0 allowed | `price_edge_shortlist.offered_candidates`; `excluded_markets` | PR #135 (9 Nov): align all lists to native Pinnacle markets | Yes (tighter: drop DC, drop wins, main line only) |
| V2 | Excluded markets | Over 1.5, double chance 12, separate draw no bet quotes | `cagey_correction_config.json` `excluded_markets`; `price_edge_cagey_shortlist.apply_market_exclusions` | Over 1.5: PR #132 (7 Nov), no reason given beyond "exclude"; DC 12 and DNB: PR #135, "keep native AH 0 and DNB distinct, reject standalone DNB, DC 12 and totals" | Yes (looser: allow each; DC 12/DNB derived prices, Over 1.5 accuracy only) |
| V3 | Lowest odds | offered odds > 1.15 | `profit_shortlist.annotate` (line 110) | PR #128 (5 Nov) introduced the (1.15, 2.00] range; no rationale recorded | Yes |
| V4 | Highest odds | offered odds ≤ 2.00 | `profit_shortlist.annotate` (lines 90, 112) | PR #128; earlier rules used 3.00 | Yes |
| V5 | Bookmaker | Pinnacle only | `shortlist_quote_policy.json`; `quote_policy.usable_bookmaker` | Bets placed at Pinnacle only (CLAUDE.md) | No (one bookmaker per period in the files) |
| V6 | Kickoff window | 20 minutes to 24 hours | `shortlist_window.DEFAULT_HOURS`, `price_edge_shortlist.MIN_MINUTES` | PR #135 kept it; runs are 24-hour slates | No |
| V7 | Quote freshness and timing | quote ≤ 24 h old, stamped before evaluation and kickoff | `quote_freshness.quote_is_fresh`; `profit_shortlist.annotate` (line 114) | Pre-kickoff data only | No |
| V8 | Research distribution | team goal-rate distribution available (team history) | `profit_shortlist.probabilities` / `annotate` (line 123) | A bet needs a probability | No (the harness scores only matches whose fold knows both teams) |
| V9 | Europa | both teams ≥ 6 verified prior appearances | `europa_training.eligibility` | `docs/team_research_profit.md` | No (no European prices) |
| V10 | Per match | one pick per fixture and market group (AH, match winner, double chance) | `profit_shortlist.select`; group `price_edge_cagey_shortlist.market_group(rule=v2)` | PR #126/#128: one per fixture/group, no quota | Yes (looser 2 per group, tighter 1 per match) |
| V11 | Order within a group | research P(positive return), then research EV, then odds | `profit_shortlist.rank` | PR #126: rank by chance of a positive settlement return | Yes (chosen vs next; EV-first as context) |
| V12 | Floors | none: no edge, probability or EV floor; negative EV eligible and flagged | `profit_shortlist` docstring | PR #126: "no minimum edge, minimum probability or forced quota" | Yes (tighter: research EV ≥ 0) |
| — | List cap / order | no cap; listed by P(positive return) | `profit_shortlist.select` | PR #126 | Not an entry rule |

Not entry rules: research warnings (coverage, quality review) are shown, never exclude; the v27 tags (balanced,
low total, high draw, even odds) and the cagey score are tracking only.

### Cagey tier (`no-loss-market-reference-v5`)

| # | Rule | Today | Where | Why it exists (record) | Testable offline |
| --- | --- | --- | --- | --- | --- |
| K1 | Markets | as V1 | `cagey_tier_v3.annotate` ("market outside cagey rule"); `excluded_markets` | PR #129 widened the plus-line list to all markets; PR #135 native markets | Yes |
| K2 | Excluded markets | as V2 | as V2 | as V2 | Yes |
| K3 | Odds | (1.15, 2.00] | `cagey_tier_v3.annotate` (line 69) | PR #129; no rationale recorded | Yes |
| K4 | Bookmaker | Pinnacle only | `cagey_tier_v3.annotate` (line 71) | as V5 | No |
| K5 | Window, freshness, timing | as V6, V7 | `cagey_tier_v3.annotate`, `price_edge_cagey_shortlist.apply_cutoff_timing` | as V6, V7 | No |
| K6 | Corrected distribution | Pinnacle 1X2 + O/U 2.5 (+ main AH) with a usable fit | `price_edge_cagey_shortlist.corrected_context`; `cagey_tier_v3.annotate` (line 76) | The tier is the Pinnacle view | No (harness scores only matches with complete prices and a usable fit) |
| K7 | Input synchronisation | offer and every input within 10 minutes, all fresh and before evaluation | `cagey_tier_v3.annotate` (lines 79-84); `apply_execution_checks` | Execution v2 | No |
| K8 | Price guard | win, DC, AH ±0.5, Over 1.5: offered ≤ 1.15 × independent margin-free Pinnacle fair (no reference: no guard); other AH lines: ≤ 1.15 × cagey fair | `cagey_market_basis.annotate` (line 102), `cagey_tier_v3.annotate` (line 110) | Suspected bookmaker price error (PR #129, `docs/cagey-market-basis-v5.md`) | Yes (looser 1.20, tighter 1.10) |
| K9 | Per match | one pick per fixture and market group | `cagey_tier_v3.select` | PR #129 | Yes |
| K10 | Order within a group | cagey no-loss, then cagey EV, then odds | `price_edge_cagey_shortlist._tier_rank` | Safest first (v3-v5) | Yes |
| K11 | No narrow gate | none (v3 had P(narrow) ≥ 67%) | `cagey_tier_v3.select` | v4 (6 Nov) removed the general gate; 67% kept as information | Yes (tighter: P(narrow) ≥ 0.67) |
| K12 | No EV or no-loss floor | none; negative EV eligible and flagged | `cagey_tier_v3` | v3-v5 by design (value-v1 had EV ≥ 0 and no-loss ≥ 85%) | Yes (tighter: no-loss ≥ 0.75; EV ≥ 0) |

## 2. Judging rules

Decided 14 Nov 2026 and committed (596f9e3) before anything was computed; full text in `docs/plan.md`. In short:

- **Quality** of a set of bets is its actual no-loss rate minus the rate the cagey tier (D) predicted for those
  bets. For Over 1.5 the prediction is M's, which is the cagey tier's v5 basis. Quality is a mean per bet, with
  95% intervals from resampling whole calendar weeks. Flat-stake return is reported beside it but never decides.
  All figures below are in percentage points.
- **Pass vs fail.** Remove the rule (keep every other rule as today), then compare the picks that pass it with the
  picks that fail it. **Looser / tighter**: today's list with the rule moved one step, minus today's list.
- **Verdict order:** tighten (tighter is clearly better) > keep (pass is clearly better than fail) > loosen
  (looser is not clearly worse and adds bets or matches) > no evidence. Development decides and validation must
  point the same way. The retrospective is a diagnostic only.
- The value list is judged with C; C6 is shown for information. The cagey tier is judged with D.

**Reading "loosen".** As decided, it means "adds bets with no measurable harm", not "better". The bets a step
adds are shown separately as context.

**Reading "keep" on a rule that is absent today** (alternate lines allowed). The split is today's list divided by
the tighter criterion, so "keep" means no change.

## 3. Reproduction and pricing limits

**Reproduction (proved first).** I rebuilt the 29 saved live runs (27 Oct – 8 Nov 2026) under today's
production rules, as the master replays do. On every run, `value_select` and `cagey_select` pick exactly the live
lists: 663 of 663 value picks and 676 of 676 cagey picks (`reproduction.json`, `all_identical: true`).
`tests/test_shortlist_entry_audit.py` repeats the check on two full slates (31 Oct and 8 Nov). It also confirms
that many groups contain competing offers, and that a changed rule changes the picks.

**Rules the backtest can't reproduce** (each offer carries the live reason as a block instead):

- kickoff window, quote freshness and observed-by-cutoff timing;
- the 10-minute input synchronisation;
- Pinnacle as the only bookmaker;
- the value list's team-history requirement and the cagey tier's corrected-distribution requirement (the harness
  only scores matches that have both);
- the Europa six-appearance rule;
- everything European, because no European prices are cached.

**How often rules bind live** (29 runs; one row can carry several reasons):

| Reason | Rows |
| --- | ---: |
| Kickoff window | 13,390 |
| Odds above 2.00 (value) | 8,269 |
| Odds outside (1.15, 2.00] (cagey) | 13,084 |
| No offered quote / stale | 4,494 |
| Market excluded (value / cagey) | 1,200 / 2,400 |
| Europa six-appearance rule | 1,159 |
| Odds ≤ 1.15 (value) | 321 |
| Price guard | **0** |

**Pricing limits:**

| Offers | Price used | Judged on |
| --- | --- | --- |
| Home/away win, main AH line | Real: Pinnacle to 15 Jan 2026; after that Bet365 margin-free plus Pinnacle's average margin | Quality and return |
| Double chance 1X/X2/12, draw no bet | **Derived**: margin-free 1X2 plus that match's 1X2 overround | Quality; return labelled "derived" |
| Alternate AH lines (main −1.00 to +1.00), Over 1.5 | None historically. M's fair odds / (1 + 2.70%) is used for the odds window and ties only | Accuracy only, never return |

Offline, every match gets alternate lines; live, only about 60% of fixtures had them. Today's lists pick an
alternate (synthetic) line in the AH group on almost every match, so most bets carry no return. A main-line-only
sensitivity run is reported below.

## 4. Results

Development 6,875 matches (106 weeks), validation 1,305 (22), retrospective 1,436 (29). Both lists today:
15,737 bets on development (148 a week, 2.3 per match), at average odds of 1.43 for the value list and 1.39 for
the cagey tier.

- Quality: value list +1.4 (+0.6 to +2.2), cagey tier +2.0 (+1.0 to +2.9). Both lists' bets did slightly
  better than the cagey tier predicted.
- Return at real prices: −0.3% (−3.1% to +2.2%).

### Coverage is not limited by the entry rules

**Offline:** every priced match already gets picks from both lists (64.9 matches a week on development, which is
every scored fixture). Every kickoff day with 15 or more priced matches is already covered: 186 of 186 on
development, 36 of 36 on validation. No entry change can add matches. A rule change can only add bets on matches
already covered, or change which bet a match gets.

**Live (29 runs):** the two lists together covered 342 of 342 priced fixtures in their windows. The 8 runs that
reached 15 covered matches are exactly the 8 runs with 15 or more priced fixtures.

Each list alone misses some matches, and the other list covers them:

- The value list's 25 misses (three runs on 4–5 Nov, for example 7 of 17 covered on 5 Nov) are UEL matches blocked by the Europa
  six-appearance rule (1,159 live rows). Nothing offline can test that rule.
- The cagey tier's misses (for example 8 of 9 on 4 Nov, 09:31) come from its missing corrected Pinnacle
  distribution.

**So the 15-match shortfall comes from fixture supply in the 24-hour window and from the master's own inclusion
rule (cagey no-loss ≥ 0.75), not from the lists' entry rules.**

### Value list (research model C)

| Rule | Pass / fail bets (dev) | Pass − fail, dev | Pass − fail, val | Looser − today, dev; bets added, their quality | Looser − today, val | Tighter − today, dev | Tighter − today, val | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lowest odds > 1.15 | 15,731 / 1,836 | −1.5 (−2.9 to −0.1) | −3.2 (−5.0 to −1.4) | +0.1 (−0.0 to +0.2); +779, +2.5 (+0.3 to +4.5) | +0.2 (−0.1 to +0.4) | −0.1 (−0.2 to +0.1) | −0.3 (−0.6 to +0.1) | **loosen** |
| Highest odds ≤ 2.00 | 15,644 / 4,981 | +2.2 (+0.6 to +3.8) | +2.9 (+0.0 to +5.7) | +0.0 (−0.2 to +0.2); +943, +2.1 (−1.0 to +5.2) | −0.2 (−0.6 to +0.3) | −0.1 (−0.3 to +0.1) | +0.5 (−0.1 to +1.0) | **keep** |
| Draw no bet excluded | 15,737 / 0 | — | — | +0.0; +0 | +0.0 | — | — | no evidence (never chosen) |
| Double chance 12 excluded | 12,407 / 4,435 | +1.0 (−0.6 to +2.6) | +1.2 (−2.7 to +5.6) | −0.2 (−0.8 to +0.3); +4,435, +0.5 (−0.8 to +1.7) | −0.5 (−1.7 to +0.6) | — | — | **loosen** |
| Over 1.5 excluded | 15,737 / 5,760 | +1.6 (+0.2 to +3.0) | +0.8 (−2.3 to +3.9) | −0.4 (−0.8 to −0.1); +5,760, −0.2 (−1.4 to +0.9) | −0.2 (−1.0 to +0.6) | — | — | **keep** |
| DC 1X/X2 allowed | 10,602 / 5,135 | −0.2 (−1.4 to +0.9) | −2.3 (−4.6 to −0.2) | — | — | −0.1 (−0.4 to +0.3) | −0.8 (−1.5 to −0.1) | no evidence |
| Alternate AH lines allowed | 8,862 / 6,875 | +2.1 (+0.7 to +3.4) | +3.9 (+1.3 to +6.6) | — | — | −0.0 (−0.5 to +0.6) | +0.3 (−0.8 to +1.3) | keep (no change) |
| Home/away win allowed | 12,010 / 3,727 | −2.5 (−4.1 to −0.7) | −2.5 (−6.7 to +1.7) | — | — | −0.6 (−1.0 to −0.2) | −0.6 (−1.6 to +0.4) | no evidence |
| One pick per market group | 15,737 / 61,217 | +0.9 (+0.2 to +1.6) | −0.2 (−1.6 to +1.5) | −0.7 (−1.0 to −0.3); +10,517, −0.3 (−1.1 to +0.5) | −0.1 (−1.0 to +0.8) | −0.8 (−1.5 to −0.1) | −1.3 (−2.8 to +0.2) | no evidence (validation disagrees) |
| Order within a group | 15,737 / 10,517 | +1.7 (+0.7 to +2.6) | +0.1 (−2.0 to +2.4) | — | — | — | — | **keep** |
| No research EV floor | 6,960 / 8,777 | −2.3 (−4.0 to −0.6) | −4.7 (−7.8 to −1.4) | — | — | −1.8 (−2.8 to −0.8) | −2.1 (−4.0 to −0.2) | no evidence (a floor is clearly worse) |

### Cagey tier (D)

| Rule | Pass / fail bets (dev) | Pass − fail, dev | Pass − fail, val | Looser − today, dev; bets added, their quality | Looser − today, val | Tighter − today, dev | Tighter − today, val | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lowest odds > 1.15 | 15,713 / 1,854 | −0.9 (−2.2 to +0.5) | −2.8 (−4.6 to −1.0) | +0.0 (−0.1 to +0.1); +797, +2.4 (+0.3 to +4.4) | +0.1 (−0.1 to +0.4) | −0.0 (−0.2 to +0.2) | −0.1 (−0.5 to +0.3) | **loosen** |
| Highest odds ≤ 2.00 | 15,737 / 4,888 | +1.8 (−0.0 to +3.5) | +3.2 (+0.7 to +5.7) | +0.0 (−0.1 to +0.2); +921, +2.8 (−0.4 to +5.8) | −0.2 (−0.5 to +0.2) | −0.1 (−0.2 to +0.1) | +0.5 (−0.0 to +1.0) | **loosen** (borderline: see below) |
| Draw no bet excluded | 15,241 / 496 | +1.6 (−1.6 to +5.1) | −3.8 (−11.0 to +5.6) | −0.1 (−0.2 to +0.1); +496, +0.3 (−3.2 to +3.8) | +0.2 (−0.1 to +0.4) | — | — | no evidence (no bets added: DNB replaces an AH pick) |
| Double chance 12 excluded | 13,947 / 2,895 | +1.4 (−0.4 to +3.2) | +0.2 (−4.3 to +5.1) | −0.2 (−0.6 to +0.3); +2,895, +0.7 (−0.9 to +2.2) | +0.3 (−0.8 to +1.4) | — | — | **loosen** |
| Over 1.5 excluded | 15,737 / 5,760 | +2.2 (+0.7 to +3.7) | +1.3 (−1.6 to +4.2) | −0.6 (−1.0 to −0.2); +5,760, −0.2 (−1.4 to +0.9) | −0.4 (−1.1 to +0.4) | — | — | **keep** |
| DC 1X/X2 allowed | 10,602 / 5,135 | −0.7 (−2.0 to +0.6) | −1.9 (−4.2 to +0.4) | — | — | −0.2 (−0.6 to +0.2) | −0.6 (−1.4 to +0.1) | no evidence |
| Alternate AH lines allowed | 8,862 / 6,875 | +1.9 (+0.8 to +3.1) | +3.0 (+0.3 to +5.6) | — | — | −0.3 (−0.8 to +0.3) | +0.2 (−0.7 to +1.1) | keep (no change) |
| Home/away win allowed | 12,010 / 3,727 | −1.8 (−3.2 to −0.1) | −1.9 (−5.9 to +2.0) | — | — | −0.4 (−0.7 to −0.0) | −0.4 (−1.4 to +0.5) | no evidence |
| One pick per market group | 15,737 / 61,217 | +1.6 (+0.7 to +2.4) | +0.4 (−1.1 to +2.0) | −0.8 (−1.2 to −0.3); +10,517, +0.1 (−0.8 to +1.0) | −0.6 (−1.3 to +0.1) | −1.1 (−1.7 to −0.4) | −1.6 (−3.0 to −0.1) | **keep** |
| Order within a group | 15,737 / 10,517 | +1.9 (+0.8 to +2.9) | +1.5 (−0.3 to +3.3) | — | — | — | — | **keep** |
| No no-loss floor (tighter ≥ 0.75) | 8,741 / 6,996 | −1.0 (−2.3 to +0.4) | −0.0 (−3.7 to +3.5) | — | — | −0.5 (−1.0 to +0.2) | −0.0 (−1.6 to +1.5) | no evidence |
| No EV floor (tighter EV ≥ 0) | 1,944 / 13,793 | −2.4 (−4.2 to −0.4) | −5.8 (−9.8 to −2.0) | — | — | −2.2 (−3.7 to −0.6) | −3.7 (−7.3 to −0.4) | no evidence (a floor is clearly worse) |
| No P(narrow) gate (tighter ≥ 0.67) | 5,566 / 10,171 | −1.3 (−2.8 to +0.1) | −1.3 (−5.1 to +2.3) | — | — | −0.8 (−1.8 to +0.1) | −0.8 (−3.2 to +1.4) | no evidence |
| Price guard 1.15× | 15,737 / 0 | — | — | +0.0; +0 | +0.0 | +0.0 | +0.0 | no evidence (never fires offline, or in the 29 live runs) |

Retrospective (diagnostic) and the C6 view are in `results.json` (`rule_tests`, keys `value:C6` and the
`retrospective` period). C6 points the same way as C on every rule.

### What the evidence says, beyond the verdicts

- **The value list hardly depends on its research model.** Inside the odds window, the highest P(positive
  return) in each group is nearly always the same safest offer, whichever model ranks it. That explains why
  value-list picks coincide with cagey picks on 55% of bets (development 8,588 of 15,737), and why C6 picks
  almost exactly what C picks.
- **Floors on expected return make things worse, on both lists.** Bets with research EV ≥ 0 did 2.3 points
  worse than the cagey tier predicted, relative to the rest (validation −4.7). Bets with cagey EV ≥ 0 did 2.4
  points worse (validation −5.8). This matches the master evidence that research "edges" are mostly error. Do
  not add EV floors.
- **The odds floor shuts out good short-priced bets; the ceiling keeps out bad long-priced value bets.**
  - The bets between 1.10 and 1.15 that loosening adds (mostly double chance at derived prices) won 87.8%
    against D's 85.3% (+2.5, +0.3 to +4.5; validation +4.0). Their return is close to zero
    (development −1.3%, validation +0.8%).
  - Above 2.00, failing bets are clearly worse on the value list in both periods.
  - On the cagey tier, the ceiling's pass − fail is +1.8 (−0.0 to +3.5) on development and +3.2 (+0.7 to +5.7) on
    validation. The bets 2.00–2.20 adds did worse than predicted on validation (−1.7, at −9.1% return). The decided
    rule calls this "loosen", but the validation evidence leans the other way.
- **Over 1.5 should stay out.** Allowing it makes both lists measurably worse on development.
- **Double chance 12 (derived prices)** adds about 3,000–4,400 development bets at unchanged quality. At derived
  prices they lose about the margin: return −4.1% (value) and −3.6% (cagey) on development, −5.7% and −2.9% on
  validation. Pinnacle's real DC 12 margin is unknown.
- **Wins are the best bets on both lists.** Dropping home/away wins makes both lists clearly worse on development.
  The bets most underestimated by the cagey tier are short-priced favourites, consistent with the master
  evidence that the cagey tier is too cautious on short prices.

### Combined effect of the "loosen" verdicts

Value list: lowest odds 1.10 and double chance 12 allowed. Cagey tier: lowest odds 1.10, highest odds 2.20 and
double chance 12 allowed.

| | Development: bets/week, quality | Validation: bets/week, quality | Return, real + derived prices, dev / val |
| --- | --- | --- | --- |
| Value list today | 148.5, +1.4 (+0.6 to +2.2) | 135.8, +0.9 (−0.4 to +2.4) | −0.8% / −1.3% |
| Value list proposed | 163.2, +1.3 (+0.6 to +1.9) | 148.8, +0.4 (−0.8 to +1.6) | −1.9% / −3.4% |
| Cagey tier today | 148.5, +2.0 (+1.0 to +2.9) | 135.8, +1.4 (−0.0 to +3.0) | −0.0% / −1.2% |
| Cagey tier proposed | 171.9, +1.9 (+1.1 to +2.7) | 156.6, +1.7 (+0.4 to +2.9) | −0.7% / −1.5% |
| Both lists today | 215.9, +1.3 (+0.6 to +2.1) | 196.7, +0.6 (−0.6 to +2.0) | −0.7% / −1.3% |
| Both lists proposed | 252.4, +1.3 (+0.7 to +1.9) | 230.0, +0.5 (−0.6 to +1.5) | −1.4% / −3.0% |

- Proposed minus today, quality, development: value −0.1 (−0.7 to +0.4), cagey −0.1 (−0.6 to +0.4), both
  +0.0 (−0.4 to +0.4). Validation: −0.6, +0.2, −0.2, none clear.
- **Matches per week are unchanged** (64.9 development, 59.3 validation). **Runs covering 15 matches are
  unchanged:** 186 of 537 kickoff days on development (35%) and 36 of 100 on validation; every day with 15 priced
  matches is covered, today and proposed.
- The extra bets are 10% more per week on the value list and 16% on the cagey tier (17% for both together), on matches already covered, with no measurable change in
  quality. The real-plus-derived return falls by about 1–2 points, mostly from double chance 12 at derived prices.
- Main-line-only sensitivity (today's rules, no alternate lines): same matches and quality (development value
  +1.4, cagey +1.7), average odds 1.64, return at real prices −0.7%.

## 5. Proposed rule changes, for Paul's decision

Nothing is changed. Any adopted change gets its own test, fixed in advance, before it reaches a live list or
the new master.

| # | List | Proposal | Evidence | Caveats | Recommendation |
| --- | --- | --- | --- | --- | --- |
| P1 | Both | Lower the odds floor from 1.15 to 1.10 | Bets at or below 1.15 beat the cagey tier's prediction more than passing bets did: pass − fail −1.5 / −0.9 on development, −3.2 / −2.8 on validation (clear for value both periods, cagey validation). Added bets +2.5 (+0.3 to +4.5), validation +4.0. No measurable harm to list quality. | Mostly double chance at derived prices. Return about zero (−1.3% development, +0.8% validation). No new matches, only about 7 more bets a week. Most useful to the new master, whose safe threshold (no-loss ≥ 0.75) these bets meet. | Worth a fixed test |
| P2 | Both | Allow double chance 12 | "Loosen" on both lists. Adds 27–42 bets a week at unchanged quality. | Derived prices only. Loses about the margin (−3% to −6%). No new matches. DC 12 is not one of the live master's native Pinnacle markets. | Low value; only if Pinnacle's real DC 12 prices are checked first |
| P3 | Cagey | Raise the odds ceiling from 2.00 to 2.20 | "Loosen" on development. Added bets +2.8 (−0.4 to +5.8). | On validation the ceiling's failing bets are clearly worse (+3.2, +0.7 to +5.7) and the added bets did worse than predicted (−1.7; return −9.1%). On the value list the same ceiling is a clear "keep". Such bets are never safe enough for the new master (predicted no-loss about 0.45). | Do not adopt |
| — | Both | Keep: highest odds 2.00 on the value list, Over 1.5 excluded, one pick per market group (cagey), order within groups | Pass clearly better than fail on development, validation the same way | — | Keep |
| — | Both | Do not add EV floors (research or cagey) | Passing bets clearly worse in both periods, on both lists | — | Keep as is |
| — | Both | Price guard, draw no bet, P(narrow) gate, no-loss floor, DC 1X/X2, wins, alternate lines | No evidence for a change | The price guard never fired, offline or live | Keep as is |

**The main finding for the 15-match goal:** the entry rules don't limit how many matches the master can fill.
Both lists already put forward every priced match in the window, offline and live. More matches would need
either more fixtures in the window (a longer lookahead, more leagues, UCL/UEL) or a change to the master's own
inclusion rule (cagey no-loss ≥ 0.75). Both are outside this audit.
