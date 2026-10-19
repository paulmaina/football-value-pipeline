# Bookmaker selection and coverage

Production shortlist quotes may come from **1xBet, Pinnacle or bet365**, as configured in `shortlist_quote_policy.json`. The parser chooses the highest valid available decimal price for each exact market among those bookmakers. Quote timestamps, complete same-book reference pairs, provider identity checks and exchange exclusions still apply. Reports and frozen selections retain the actual quoted bookmaker and price.

The policy applies to new prediction runs. Existing snapshots retain their frozen execution policy and quoted prices; broadening the current allowlist does not relabel historical selections. After merge, pull main and run the usual prediction command to obtain fresh offers. Reformatting existing outputs alone cannot recover offers discarded under an earlier allowlist.

## Provider coverage

The current The Odds API EU feed includes 1xBet (`onexbet`) and Pinnacle (`pinnacle`). Enabling Pinnacle reuses the existing responses, region and request layout; no new API key, extra region or additional request is required. Availability still depends on the competition and exact market.

Bet365 is allowed by the execution policy, but the current provider's published bookmaker list does not offer bet365 football coverage. The listed `bet365_au` feed is paid and limited to AFL and NRL; it is not a substitute for football quotes. Existing saved football responses inspected on 19 October contain no bet365 offers. A supported football quote source must be integrated before bet365 can contribute live shortlist prices. Do not use historical Football-Data CSV bet365 prices as current offers.

Provider coverage reference, checked 19 October 2026: https://the-odds-api.com/sports-odds-data/bookmaker-apis.html

## Model and ranking

The production policy remains twelve distinct matches within 48 hours, one market per fixture, ranked by the existing adjusted-probability/adjusted-EV balance. Under 3.5 remains excluded. This configuration does not change model fits or forecast probabilities, and it does not force market diversity. More usable bookmakers can change selected prices, EV and the winning market for a fixture on the next prediction run.
