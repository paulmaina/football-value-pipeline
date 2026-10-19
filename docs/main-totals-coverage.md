# Main-line Over 1.5 coverage

Some bookmakers publish 1.5 as the main `totals` line and omit it from
`alternate_totals`. The pipeline now carries these exact Over/Under 1.5 pairs
through the existing fixture identity join into predictions. It merges them
with the usual additional-markets response without making another API request.

Only complete, coherent pairs pass. Missing/invalid timestamps, stale or future
quotes, duplicate outcomes, invalid prices and mismatched lines are rejected.
Each bookmaker contributes its newest complete pair; the best executable price
comes from the configured bookmaker allowlist. The price keeps its own timestamp
and bookmaker, while the market reference keeps its own complementary pair.
Missing alternate lines and failed additional requests preserve a valid main
quote. Quotes are checked for freshness again before predictions are exported.

Coverage diagnostics include `over_1_5_quote` and `over_1_5_bookmakers` per fixture,
and `over_1_5_in_window_quote_fixtures` per league, including primary quotes when
an additional request fails. Existing additional-request status names describe
double-chance coverage and are retained.

An offline replay of the saved 19 October 2026 Getafe–Rayo response recovers the
1xBet Over 1.5 price of **1.63**, paired with Under 1.5 at **2.49**, timestamped
`2026-10-19T16:25:49Z`. The allowed Pinnacle alternate quote is 1.60, so it does
not overwrite 1.63. This is a historical validation, not a current offer.

The next normal prediction run uses the fix. It does not change model
probabilities, shortlist scoring, the 12-match limit, the 48-hour window or the
Under 3.5 exclusion. Better quote coverage does not guarantee more Over 1.5
selections; the existing probability/EV ranking still decides the market.
