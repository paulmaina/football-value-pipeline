# Pinnacle-only shortlist execution

The value, cagey-tier and master shortlists use **Pinnacle offers only**.
`shortlist_quote_policy.json` names `Pinnacle` as the sole allowed bookmaker and
has no fallback bookmakers. A higher 1xBet price or a handicap quoted only at
1xBet cannot qualify. Missing Pinnacle offers remain unavailable; prices and
handicap lines are never copied from another bookmaker or invented to fill the
master's fifteen-fixture target.

The actual offered bookmaker/price and market-to-bet label remain in the outputs.
Asian Handicap offers come from captured same-book quotes. A computed fair price
is a probability reference, not evidence that a bookmaker offers that line.
Equivalent settlement does not authorize copying a Double Chance price to an AH
market. The master's existing 1X/X2 conversion requires an actual Pinnacle +0.5
quote; DC 12 and Over 1.5 remain excluded from the master. Draw-no-bet equivalents
retain their actual market-to-bet label.

## Provider requests and Kenya

Main and event-level The Odds API requests explicitly use `bookmakers=pinnacle`
under the production policy. Their caches are separated by bookmaker scope, so
switching from a broader allowlist cannot reuse its cached request response.
The selector independently enforces the allowlist even if a payload contains
other bookmakers. Other providers' statistics, research or historical odds do
not establish that a current Pinnacle offer is executable.

`regions=eu` means the provider's bookmaker group; it does not mean the bettor
must be in Europe, nor does it verify Kenyan account availability. The provider
lists Pinnacle under EU and says its Pinnacle odds come from the public website
and may incur a delay. `bookmakers` overrides the region filter. There is no
Kenya-account verification in this integration.

Feed-observed is not logged-in-account verified. Before placing a bet, check the
same event, full-match period, side, exact handicap, current decimal price and
multi-bet eligibility in your own Pinnacle account. The pipeline cannot certify
Kenyan account access or that every public-feed line is currently offered to it.
Pinnacle's own support directs country eligibility questions to registration and
its account terms. Do not infer eligibility from successful odds API access.

Official documentation checked 8 November 2026:

- https://the-odds-api.com/liveapi/guides/v4/
- https://the-odds-api.com/sports-odds-data/bookmaker-apis.html
- https://support.pinnacle.com/hc/en-us/articles/50392420556305-Registration-issues-and-restricted-territories

## Refresh and historical records

New prediction and stored-forecast refresh runs use the new policy. Your usual
command is unchanged. Regenerate the outputs after merging; formatting an old
CSV alone cannot discover missing Pinnacle offers. Fewer than fifteen valid
fixtures produces the existing visible shortfall, not a bookmaker fallback.

Historical snapshots keep their recorded execution policy, markets and prices.
Master replay and its audit now explicitly use that frozen policy in a scoped
context, restoring the live Pinnacle-only policy afterwards. Old 1xBet picks are
still replayed and graded as originally captured. Parsing and closing collectors
retain legacy bookmaker support for those historical records.

This change adds no probability-model or settlement formula. Restricting the
available offers can change selected lines, prices, EV and list membership; a
fresh forecast also uses the specifically requested Pinnacle market inputs.
